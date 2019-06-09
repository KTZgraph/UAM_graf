#coding=utf-8

from lxml import etree


class GlobalSightXMLConverter: #GlobalSightXMLConverter
    """
    Klasa do parsowania macierzy grafu do GXMl, który w praktyce jest danymi w formacie XMl z strukturą
    (nazwami tagów etc.) zdefiniowanymi przez programistę
    """
    @staticmethod
    def converToXml(matrix, point_list, weight):
        """
        Konwertuje macierz na XML który jest potem wysyłany do Javacriptu
        bazując na:
            - http://www.globalsight.com/wiki/index.php/Converting_Content_to_GXML
            - http://docs.roxen.com/(en)/roxen/5.4/web_developer_manual/graphics/gxml.tag
            - https://metacpan.org/pod/XML::GXML
            - https://books.google.pl/books?id=BYxiIiFBJzkC&pg=PA250&lpg=PA250&dq=gxml+format&source=bl&ots=xs5TfO_ri8&sig=ACfU3U2nzmOwaq00i2dImuYKqIXuOZQwIQ&hl=pl&sa=X&ved=2ahUKEwiJp8mEw9riAhUCx4sKHUjvDFoQ6AEwDXoECAkQAQ#v=onepage&q=gxml%20format&f=false
        """
        root = etree.Element("root", weight=str(weight))
        print(matrix)

        for row, point1 in zip(matrix, point_list):
            vertex = etree.SubElement(root, "vertex", x=str(point1.x), y=str(point1.y))

            for column, point2 in zip(row, point_list):
                if column > 0:
                    neighbour = etree.Element("neighbour", x=str(point2.x), y=str(point2.y))
                    vertex.append(neighbour)


        print(etree.tostring(root, pretty_print=False))
        return etree.tostring(root, pretty_print=False)
