import logging

CSI = "\033["
DEFAULT_FORMAT = "%(asctime)s [%(levelname)s] : %(message)s"

def code_to_chars(code):
    return CSI + str(code) + "m"

def clear_screen(mode=2):
    return CSI + str(mode) + "J"

def clear_line(mode=2):
    return CSI + str(mode) + "K"


class AnsiCode(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith("_"):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))


class FontColor(AnsiCode):
    BLACK   = 30
    RED     = 31
    GREEN   = 32
    YELLOW  = 33
    BLUE    = 34
    MAGENTA = 35
    CYAN    = 36
    WHITE   = 37
    RESET   = 39


class Background(AnsiCode):
    BLACK   = 40
    RED     = 41
    GREEN   = 42
    YELLOW  = 43
    BLUE    = 44
    MAGENTA = 45
    CYAN    = 46
    WHITE   = 47
    RESET   = 49

    
class FontStyle (AnsiCode):
    BRIGHT  = 1
    DIM     = 2
    NORMAL  = 22
    RESET_ALL = 0

color = FontColor()
background = Background()
style = FontStyle()


TIME_FORMAT = f'{color.YELLOW}%(asctime)s{style.RESET_ALL}'
COLORS = {
    "DEBUG":    color.GREEN,
    "INFO":     color.WHITE,
    "WARNING":  color.MAGENTA,
    "ERROR":    color.WHITE,
    "CRITICAL": color.RED,
}
MSG_FORMAT = {
    "DEBUG":    style.DIM+COLORS["DEBUG"],
    "INFO":     COLORS["INFO"],
    "WARNING":  COLORS["WARNING"],
    "ERROR":    style.BRIGHT+background.RED+COLORS["ERROR"],
    "CRITICAL": style.BRIGHT+COLORS["CRITICAL"],
}
FORMATS = {
    "DEBUG":    f'{TIME_FORMAT} {MSG_FORMAT["DEBUG"]}[%(levelname)+8s]{style.RESET_ALL} - %(message)s',
    "INFO":     f'{TIME_FORMAT} {MSG_FORMAT["INFO"]}[%(levelname)+8s]{style.RESET_ALL} - %(message)s',
    "WARNING":  f'{TIME_FORMAT} {MSG_FORMAT["WARNING"]}[%(levelname)+8s]{style.RESET_ALL} - %(message)s',
    "ERROR":    f'{TIME_FORMAT} {MSG_FORMAT["ERROR"]}[%(levelname)+8s] - %(message)s{style.RESET_ALL}',
    "CRITICAL": f'{TIME_FORMAT} {MSG_FORMAT["CRITICAL"]}[%(levelname)+8s] - %(message)s{style.RESET_ALL}',
}

class ColoredFormatter(logging.Formatter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def format(self, record):
        levelname = record.levelname
        if levelname in FORMATS:
            msg = logging.Formatter(FORMATS[levelname]).format(record)
        else:
            msg = logging.Formatter(DEFAULT_FORMAT).format(record)
        return msg