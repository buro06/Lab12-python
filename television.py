class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """ Init television status with default values """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """ set power to opposite of what it is now """
        self.__status = not self.__status

    def mute(self) -> None:
        """ toggle mute on and off only when the power is ON """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """ set channel up 1, only when TV on, and wraps to low channel when reaching max channel """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """ set channel down 1, only when TV on, and wraps to high channel when reaching low channel """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """ set volume up by 1 , only when TV on, if muted, unmutes first, then increases volume. """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """ decrease volume down by 1 , only when TV on, if muted, unmutes first , then decreases volume. """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """ return string representation of the TV state """
        volume_display = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}"