class Television:
    """
    A class representing the functions of a television
    """
    #class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self):
        """
        constructor method to initialize instance variables
        """
        #instance variables (private)
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL


    def power(self):
        """
        toggle power status of television
        """
        '''if self.__status:
            self.__status = False
        else:
            self.__status = True'''

        self.__status = not self.__status


    def mute(self):
        """
        toggle mute status if television is on
        """
        if self.__status:
            if not self.__muted:
                self.__temp_volume = self.__volume
                self.__volume = 0
                #self.__muted = True
            else:
                self.__volume = self.__temp_volume
                #self.__muted = False
            self.__muted = not self.__muted

    def channel_up(self):
        """
        increase channel, set to MIN_CHANNEL at MAX_CHANNEL
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        decrease channel, set to MAX_CHANNEL at MIN_CHANNEL
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        increase volume, unmutes if muted
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__temp_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        decrease volume, unmutes if muted
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__temp_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        :return: television status as formatted string
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'