"""Water once, no click needed.

Does exactly two things: focuses the Stardew window by itself, then
presses the tool key once. No screenshots, no soil checks, no decisions.

Before you run it: test save only, watering can selected, facing down.
"""

import ctypes
import time

import pydirectinput

TOOL_KEY = "c"    # tool key for the watering can
HOLD_TIME = 0.5   # how long to hold the tool key
WINDOW_TITLE = "Stardew Valley"


def focus_game():
    """Focus the Stardew window, no click needed. True if it worked.

    Windows only lets the foreground window's thread hand over focus, so
    this briefly borrows that thread's input, makes the switch, then
    gives it back. It verifies the result: if the game is not actually
    in front afterwards, it returns False and nothing gets pressed.
    """
    user32 = ctypes.windll.user32
    hwnd = user32.FindWindowW(None, WINDOW_TITLE)
    if not hwnd:
        return False
    if user32.IsIconic(hwnd):
        user32.ShowWindow(hwnd, 9)  # SW_RESTORE: un-minimize if minimized
    if user32.GetForegroundWindow() == hwnd:
        return True
    foreground_thread = user32.GetWindowThreadProcessId(
        user32.GetForegroundWindow(), None)
    our_thread = ctypes.windll.kernel32.GetCurrentThreadId()
    user32.AttachThreadInput(foreground_thread, our_thread, True)
    try:
        user32.SetForegroundWindow(hwnd)
        user32.BringWindowToTop(hwnd)
    finally:
        user32.AttachThreadInput(foreground_thread, our_thread, False)
    time.sleep(0.3)
    return user32.GetForegroundWindow() == hwnd


def main():
    if not focus_game():
        print("Could not focus the Stardew Valley window. "
              "Start the game and try again.")
        return
    try:
        pydirectinput.keyDown(TOOL_KEY)
        time.sleep(HOLD_TIME)
    finally:
        pydirectinput.keyUp(TOOL_KEY)
    print("Watered once.")


if __name__ == "__main__":
    main()