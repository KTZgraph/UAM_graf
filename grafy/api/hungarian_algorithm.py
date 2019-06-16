#coding=utf-8
"""
https://zasoby1.open.agh.edu.pl/dydaktyka/matematyka/c_badania_operacyjne/krok/krok8_03.html

Założenie: mamy 'N' zadań do wykonania oraz 'N' maszyn, które mogą wykonywać zadania

Dane przedstawiamy w postaci macierzy NxN takiej, że indeksami wierszy będą np. maszyny a kolumn zadania. Każda maszyna będzie posiadała swój indywidualny koszt wykonania danego zadania.

Posiadając tak zdefiniowaną macierz możemy przystąpić do wykonywania algorytmu

Krok 1: Dla każdego wiersza odejmujemy od niego jego minimum
Krok 2: Dla każdej kolumny odejmujemy od niej jej minimum
Krok 3: Zakreślamy wszystkie 'zera' występujące w macierzy jak najmniejszą liczbą linii.
UWAGA! Nie ma jednej jasno zdefiniowanej metody zakreślania, można przykładowo stosować:

metoda rogu północno – zachodniego,
minimum w wierszu,
minimum w kolumnie,
minimum w tabeli.
Ważne natomiast jest, aby po wybraniu określonej metody wybierania, stosować ją do samego końca.

Załóżmy, że udało się nam zakreślić wszystkie 'zera' przy użyciu k linii.

Jeżeli k < N znajdujemy minimum ze wszystkich niezakreślonych elementów. Załóżmy, że jest to m. Odejmujemy m od każdego niezakreślonego elementu oraz dodajemy m do wszystkich elementów, które leżą na przecięciu linii zakreśleń.
Jeżeli k = N to idziemy do kroku 4.
Krok 4: Startując od pierwszego wiersza i idąc w dół dokonujemy przypisań 'maszyna - zadanie'. Po wykonaniu danego przypisania kasujemy dany wiersz i kolumnę z macierzy i idziemy dalej.
Przypisanie może być jednoznaczne tylko wtedy, jeżeli w danym wierszu występuje dokładnie jedno zero. Pozycja tego zera definiuje nam przypisanie np.: jeżeli jakieś 'zero' ma współrzędne (2,3) i jest jedynym zerem w wierszu drugim to znaczy, że do 3 zadania została przypisana 2 maszyna. Jeżeli po przejściu wszystkich wierszy nie byliśmy w stanie dokonać wszystkich N przypisań to przechodzimy na kolumny. Startujemy z kolumny pierwszej i idziemy w prawo.

Może wystąpić taka sytuacja, że będziemy mieli więcej zer w danym wierszu. Wtedy należy arbitralnie wybrać przypisanie.
"""

import numpy as np

class Hungarian:

    def __init__(self, input_matrix=None):
        #type: (List[List]) -> None

        if input_matrix is not None:
            # zapis danych wejsciowych
            my_matrix = np.array(input_matrix)
            self._input_matrix = np.array(input_matrix)
            self._maxColumn = my_matrix.shape[1]
            self._maxRow = my_matrix.shape[0]

            # Dodaje zera "sztuczne" jak trzeba
            matrix_size = max(self._maxColumn, self._maxRow)
            pad_columns = matrix_size - self._maxRow
            pad_rows = matrix_size - self._maxColumn
            my_matrix = np.pad(my_matrix, ((0,pad_columns),(0,pad_rows)), 'constant', constant_values=(0))

            self._cost_matrix = my_matrix
            self._size = len(my_matrix)
            self._shape = my_matrix.shape

            self._results = [] #wynik algorytmu
        else:
            self._cost_matrix = None

    def get_results(self):
        """Wynik po obliczeniach"""
        return self._results


    def calculate(self, input_matrix=None):
        # type: (List[List]) -> None
        """
        implementacja Hungarian (Munkres) Algorithm.
        ogólnie temat jest na tyle cieżki, że jest wbudowana biblioteka pythonowa która to ogarnia
        http://software.clapper.org/munkres/
        """
        # Handle invalid and new matrix inputs.
        if input_matrix is None and self._cost_matrix is None:
            raise ValueError("Invalid input")
        elif input_matrix is not None:
            self.__init__(input_matrix)

        result_matrix = self._cost_matrix.copy()

        # 1) Odejmuję od każdego wiersza minimu z wiersza
        for index, row in enumerate(result_matrix):
            result_matrix[index] -= row.min()

        # 2) Odejmuję od każdej kolumny minimum z kolumny
        for index, column in enumerate(result_matrix.T):
            result_matrix[:, index] -= column.min()

        # 3) Używm minimalnej ilości linii do pokrycia wszsytkich  zer
        # dopasowanie macierzy jak liczba kolumn!= wiersz
        total_covered = 0
        while total_covered < self._size:
            # Szukam minimalną liczbę linii, aby pokryć wszytkie zera w macierzy i znajduję całą(total) liczbę wierszy i kolumn
            cover_zeros = CoverZeros(result_matrix)
            covered_rows = cover_zeros.get_covered_rows()
            covered_columns = cover_zeros.get_covered_columns()
            total_covered = len(covered_rows) + len(covered_columns)

            # jak rozmiar się nie zgadza to ją dopasowuję "pseudoprawonik"
            if total_covered < self._size:
                result_matrix = self._adjust_matrix_by_min_uncovered_num(result_matrix, covered_rows, covered_columns)

        # 4) Zaczynam od pierwszefo z góry wiersza i jadę w dół wykonując kroki:
        # Znajduje pojedyncze zera w wierszach lub kolumnach
        # Dodaję je do końcowego wyniku i uwuam je oraz związany z nimi wiersz / albo kolumnę z macierzy.
        expected_results = min(self._maxColumn, self._maxRow)
        zero_locations = (result_matrix == 0)
        while len(self._results) != expected_results:

            # Jak liczba zer w macierzy wynosi zero przed znalezieniem wszystkich wyników,to błąd.
            if not zero_locations.any():
                raise BaseException("Unable to find results. Algorithm has failed.")

            # Zanjduje zakreślenia zaznaczam wiersze i kolumny do usuniecia
            matched_rows, matched_columns = self.__find_matches(zero_locations)

            # ybieram kombinajce wierszy z kolumnami z minimalną liczbą zer w nim
            total_matched = len(matched_rows) + len(matched_columns)
            if total_matched == 0:
                matched_rows, matched_columns = self.select_arbitrary_match(zero_locations)

            # redukcja wierszy i kolumn
            for row in matched_rows:
                zero_locations[row] = False
            for column in matched_columns:
                zero_locations[:, column] = False

            # zachowanie wyniku
            self.__set_results(zip(matched_rows, matched_columns))



    def _adjust_matrix_by_min_uncovered_num(self, result_matrix, covered_rows, covered_columns):
        """Odejmuję m od kązdego niezakreślonego numeru i dodaje minum do każdego podwójnie zakreślonego"""
        # Szukam minimu jak w kroku 1 na kartce
        elements = []
        for row_index, row in enumerate(result_matrix):
            if row_index not in covered_rows:
                for index, element in enumerate(row):
                    if index not in covered_columns:
                        elements.append(element)
        min_uncovered_num = min(elements)

        # Dodaje min do kadego elemnetu
        adjusted_matrix = result_matrix
        for row in covered_rows:
            adjusted_matrix[row] += min_uncovered_num
        for column in covered_columns:
            adjusted_matrix[:, column] += min_uncovered_num

        # Odejmuje minimum od każdego elementu
        m_matrix = np.ones(self._shape, dtype=int) * min_uncovered_num
        adjusted_matrix -= m_matrix

        return adjusted_matrix

    def __find_matches(self, zero_locations):
        """Zwraca wierszer i kolumny z dopasowaniami w nich"""
        marked_rows = np.array([], dtype=int)
        marked_columns = np.array([], dtype=int)

        # Oznacza wiersze i kolumny dopasowaniami
        # Iteruje po wierszach
        for index, row in enumerate(zero_locations): # zero_locations to tam gdzie zera
            row_index = np.array([index])
            if np.sum(row) == 1:
                column_index, = np.where(row)
                marked_rows, marked_columns = self.__mark_rows_and_columns(marked_rows, marked_columns, row_index,
                                                                           column_index)

        # Iteruję po kolumnach
        for index, column in enumerate(zero_locations.T):
            column_index = np.array([index])
            if np.sum(column) == 1:
                row_index, = np.where(column)
                marked_rows, marked_columns = self.__mark_rows_and_columns(marked_rows, marked_columns, row_index,
                                                                           column_index)

        return marked_rows, marked_columns

    @staticmethod
    def __mark_rows_and_columns(marked_rows, marked_columns, row_index, column_index):
        """Sprawdza czy kolumna/ albo wiersz jest zaznacozny jak nie to go zaznaczam"""
        new_marked_rows = marked_rows
        new_marked_columns = marked_columns
        if not (marked_rows == row_index).any() and not (marked_columns == column_index).any():
            new_marked_rows = np.insert(marked_rows, len(marked_rows), row_index)
            new_marked_columns = np.insert(marked_columns, len(marked_columns), column_index)
        return new_marked_rows, new_marked_columns

    @staticmethod
    def select_arbitrary_match(zero_locations):
        """Wybieram kombinajce wierszy z kolumnami z minimalną liczbą zer w nim"""
        # Zlicza zera w kombinacjach wierszy i kolumn
        rows, columns = np.where(zero_locations)
        zero_count = []
        for index, row in enumerate(rows):
            total_zeros = np.sum(zero_locations[row]) + np.sum(zero_locations[:, columns[index]])
            zero_count.append(total_zeros)

        # Kombinajca z kolumn z wiersza z minimalną liczbą zer
        indices = zero_count.index(min(zero_count))
        row = np.array([rows[indices]])
        column = np.array([columns[indices]])

        return row, column

    def __set_results(self, result_lists):
        """Ustawia wyniki podczas obliczęń - pomocnicza

        Sprawdza, czy wartości wyników są poza zakresem z macierzy wejściowej (z powodu wypełnienia macierzy).
        Dodaje wyniki do listy
        """
        for result in result_lists:
            row, column = result
            if row < self._maxRow and column < self._maxColumn:
                new_result = (int(row), int(column))
                self._results.append(new_result)


class CoverZeros:
    """
    Uzywa minimalnej liczby linii do pokrycia wszsystikch zer w macierzy
    """

    def __init__(self, matrix):
        """
        Macierz wejsćiowa jest zapisywana jako boolowska żeby stworzyc lokalizację zer
        metoda calculate generuje wynik
        """
        # szukam zer/ "pseudoprawoników" w macierzy
        self._zero_locations = (matrix == 0)
        self._shape = matrix.shape

        # Wybory na początku inicjalizowane na zera
        self._choices = np.zeros(self._shape, dtype=bool)

        self._marked_rows = []
        self._marked_columns = []

        # ogarnia wszystkie wiersze i kolumny
        self.__calculate()

        # Rysuje krechy przez wszsytkie nieoznacozne wiersze i kolumny
        self._covered_rows = list(set(range(self._shape[0])) - set(self._marked_rows))
        self._covered_columns = self._marked_columns

    def get_covered_rows(self):
        """lista już przejrzanych wierszy"""
        return self._covered_rows

    def get_covered_columns(self):
        """Lista już przejrzanych kolumn."""
        return self._covered_columns

    def __calculate(self): #Najważniejsza!
        """
        Oblicza minimalną liczbę linii potrzebnych do pokrycia wszystkich zer w macierzy
        """
        while True:
            # Zeruje wszystki zaznaczenia
            self._marked_rows = []
            self._marked_columns = []

            # Zapamietuje/zaznacza wszystkie wiersze w których nie okonano wyboru
            for index, row in enumerate(self._choices):
                if not row.any():
                    self._marked_rows.append(index)

            # Jak nie ma zaznarzonych wierszy to True
            if not self._marked_rows:
                return True

            # Zapmamietuje/ zaznacza  wszystkie kolumny które jeszcze nie zostały zaznaczone a które mają zera
            # w oznaczonych rzedach
            num_marked_columns = self.__mark_new_columns_with_zeros_in_marked_rows()

            # Jak nie ma nowych zaznaczonych kolumn to koniec
            if num_marked_columns == 0:
                return True

            # Jak jeszcze istnieje jeszcze jakiś wybór zaznaczenia w jakieś kolumnie
            while self.__choice_in_all_marked_columns():
                # Jakieś wybory w zaznaczonej kolumnie

                # Zaznacza wszsytkie wiersze, które nie zostały jeszcze zaznaczone a mają zaznaczone kolumny
                num_marked_rows = self.__mark_new_rows_with_choices_in_marked_columns()

                if num_marked_rows == 0: #Jak nie ma nowych zaznaczeń/zakeśleń to prawda
                    return True

                # Zakreśla wszsytkie kolumny, które jeszcze nie zostały zaznaczone a mają zera w oznaczonych rzędach
                num_marked_columns = self.__mark_new_columns_with_zeros_in_marked_rows()

                # Jak nie mam nowych kolumn to true
                if num_marked_columns == 0:
                    return True

            # Brak wyboru w jednej lub więcej zaznaczonyc kolumnach
            # Szukam zaznaczonej kolumny, która nie ma wyboru.
            choice_column_index = self.__find_marked_column_without_choice()

            while choice_column_index is not None:
                # Znajduje zero w kolumnie indeksowanej która nie ma wiersza z wyborem
                choice_row_index = self.__find_row_without_choice(choice_column_index)

                # Sprawdzam czy znaleziono dostępny wiersz
                new_choice_column_index = None
                if choice_row_index is None:
                    # Zamiana rzędami - szukam najlepszego rzędu żeby udało się wcisnąc zamianę
                    # zwraca parę kolumn które trzeba zamienić ze sobą
                    choice_row_index, new_choice_column_index = \
                        self.__find_best_choice_row_and_new_column(choice_column_index)

                    # Usuwa stary wybór
                    self._choices[choice_row_index, new_choice_column_index] = False

                # Ustawia True w macierzy wyborów
                self._choices[choice_row_index, choice_column_index] = True

                # Znowu pętla jak już wybrana wartość zostanaie dodana do wiersza już z wybranym wyborem
                choice_column_index = new_choice_column_index

    def __mark_new_columns_with_zeros_in_marked_rows(self):
        """Zaznacza wszystkie kolumny, które nie są jeszcze zaznaczone/przejrzane i mają zera w oznaczonych wierszach"""
        num_marked_columns = 0
        for index, column in enumerate(self._zero_locations.T):
            if index not in self._marked_columns:
                if column.any():
                    row_indices, = np.where(column)
                    zeros_in_marked_rows = (set(self._marked_rows) & set(row_indices)) != set([])
                    if zeros_in_marked_rows:
                        self._marked_columns.append(index)
                        num_marked_columns += 1
        return num_marked_columns

    def __mark_new_rows_with_choices_in_marked_columns(self):
        """Zaznacza wszsytkie wiersze które nie zostały jeszcze zaznaczone, a które mają zaznaczone kolumny"""
        num_marked_rows = 0
        for index, row in enumerate(self._choices):
            if index not in self._marked_rows:
                if row.any():
                    column_index, = np.where(row)
                    if column_index in self._marked_columns:
                        self._marked_rows.append(index)
                        num_marked_rows += 1
        return num_marked_rows

    def __choice_in_all_marked_columns(self):
        """Zwraca True jeśli istneije wybór we wszsytkich zaznaczonych kolumnach"""
        for column_index in self._marked_columns:
            if not self._choices[:, column_index].any():
                return False
        return True

    def __find_marked_column_without_choice(self):
        """Znajdź zaznaczona kolumnę która nie ma wyboru"""
        for column_index in self._marked_columns:
            if not self._choices[:, column_index].any():
                return column_index

        raise BaseException(
            "Algorytm się nie udał :< nie znalazło kolumny bez wyboru - nie dało się pokryć zer macierzy")

    def __find_row_without_choice(self, choice_column_index):
        """
        Znajduje wiersz bez wyboru w indeksowanej kolumnie; jak nie istnieje to zwraca None
        """
        row_indices, = np.where(self._zero_locations[:, choice_column_index])
        for row_index in row_indices:
            if not self._choices[row_index].any():
                return row_index

        # Wszystkie wiersze mają wybory, to Nic nie zwracam
        return None

    def __find_best_choice_row_and_new_column(self, choice_column_index):
        """
        Znajduje indeks wierszy który ma zostać użyty do wyboru , aby kolumna która wymaga zmiany yła optymalna
        Jak nie ma to randomow zwraca
        """
        row_indices, = np.where(self._zero_locations[:, choice_column_index])
        for row_index in row_indices:
            column_indices, = np.where(self._choices[row_index])
            column_index = column_indices[0]
            if self.__find_row_without_choice(column_index) is not None:
                return row_index, column_index

        # jak nie moge znaleźc optymalnego dopasowania to zwracam randomowe kolejnosci
        from random import shuffle

        shuffle(row_indices)
        column_index, = np.where(self._choices[row_indices[0]])
        return row_indices[0], column_index[0]


if __name__ == '__main__':

    cost_matrix = [
        [5, 1, 6, 4],
        [4, 8, 5, 3],
        [7, 2, 5, 6]]
    hungarian = Hungarian(cost_matrix)
    hungarian.calculate()
    print("Wynik:\n\t", hungarian.get_results())
    print("-" * 80)
