import ctypes
from ctypes import wintypes

def get_win_desktop():
    CSIDL_DESKTOP = 0
    buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOP, None, 0, buf)
    return buf.value