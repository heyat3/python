class Television:
    '''
    A class representing the functions of a television
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    '''
    constructor method to initialize instance variables
    '''
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    '''
    power method changes status variable to true or false depending if television is on or off
    '''
    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    '''
    mure method changes muted variable to true or false depending if television is muted
    '''
    def mute(self):
        if self.__muted:
            self.__muted = False
        else:
            self.__muted = True
            self.__volume = 0

    '''
    channel up and down change channel variable up or down
    set channel to minimum or maximum respectively if over maximum or minimum
    '''
    def channel_up(self):
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    '''
        volume up and down change volume variable up or down
        set volume to maximum or minimum respectively if over maximum or minimum
    '''
    def volume_up(self):
        self.__muted = False
        if self.__status:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = self.MAX_VOLUME

    def volume_down(self):
        self.__muted = False
        if self.__status:
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = self.MIN_VOLUME

    '''
    :return: Power = [status], Channel = [channel], Valume = [volume]
    '''
    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'