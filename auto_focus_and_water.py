import ctypes
import time

import pydirectinput

user32 = ctypes.windll.user32


def focus_game():
    """Bring the Stardew window to the front. Return True if it worked."""
    hwnd = user32.FindWindowW(None, "Stardew Valley")
    if not hwnd:
        print("Game window not found. Start the game and try again.")
        return False
    if user32.IsIconic(hwnd):
        user32.ShowWindow(hwnd, 9)  # minimized: restore it
    if user32.GetForegroundWindow() != hwnd:
        fg = user32.GetWindowThreadProcessId(user32.GetForegroundWindow(), None)
        me = ctypes.windll.kernel32.GetCurrentThreadId()
        user32.AttachThreadInput(fg, me, True)  # borrow the foreground thread
        user32.SetForegroundWindow(hwnd)
        user32.AttachThreadInput(fg, me, False)  # give it back
        time.sleep(0.3)
    if user32.GetForegroundWindow() == hwnd:
        return True
    print("Could not bring the game to the front.")
    return False


# Watering: only water after confirming the game is in front
if focus_game():
    try:
        pydirectinput.keyDown('c')
        time.sleep(0.5)
    finally:
        pydirectinput.keyUp('c')
    print("Watered once.")
