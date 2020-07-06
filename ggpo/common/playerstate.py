# -*- coding: utf-8 -*-


# noinspection PyClassHasNoInit
class PlayerStates:
    AVAILABLE = 0x0
    AFK = 0x1
    PLAYING = 0x2
    QUIT = 0xff  # my own, not GGPO server's

    @staticmethod
    def codeToString(code):
        """codeToString: Determines the players state (AFK, PLAYING, etc)

        Args:
            code [Hex code]: Hex code of the players state.

        Returns:
            [string]: Hex code identifier.
        """
        if code == 0:
            return 'AVAILABLE'
        elif code == 1:
            return 'AFK'
        elif code == 2:
            return 'PLAYING'
        elif code == 0xff:
            return 'QUIT'
        else:
            return 'Unknown (' + hex(code) + ')'
