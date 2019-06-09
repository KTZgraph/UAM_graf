# coding=utf-8


class SingletonInitialSettings:
    """
    Initial settings for transmitters (points) in city with given radius
    """
    _instances = {}


    def __call__(cls, cityCircleRadius=100, rangeRadiusTransmitter=10, totalNumberTransmitters = 20):
        # type: (Union[int, float], Union[int, float], int) -> None
        """
        Bezpieczniejszy sposób implementacji Singletonu - wpływam na proces tworzenia instancji wszystkich klas danego
        typu (jakby komus przyszlo do głowy dziedziczyc z Singletonu)
        Dzięki nadpisaniu metody __call__ metaklasy można z kodu singletonu korzystać bez żadnych obaw

        @note: org nie zapewnia bezpieczeństwa przy dziedziczeniu :<
        """
        if cls._instance is None:
            cls._instances[cls] = super().__call__(cls, cityCircleRadius, rangeRadiusTransmitter,
                                                   totalNumberTransmitters)

        return cls._instance


