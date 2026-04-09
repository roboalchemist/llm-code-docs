# Welcome to PyAutoGUI’s documentation!

PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications. The API is designed to be simple. PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.

To install with pip, run `pip install pyautogui`. See the Installation page for more details.

The source code is available on: https://github.com/asweigart/pyautogui

PyAutoGUI has several features:

- 

Moving the mouse and clicking in the windows of other applications.

- 

Sending keystrokes to applications (for example, to fill out forms).

- 

Take screenshots, and given an image (for example, of a button or checkbox), and find it on the screen.

- 

Locate an application’s window, and move, resize, maximize, minimize, or close it (Windows-only, currently).

- 

Display alert and message boxes.

Here’s a YouTube video of a bot automatically playing the game Sushi Go Round [https://www.youtube.com/watch?v=lfk_T6VKhTE]. The bot watches the game’s application window and searches for images of sushi orders. When it finds one, it clicks the ingredient buttons to make the sushi. It also clicks the phone in the game to order more ingredients as needed. The bot is completely autonomous and can finish all seven days of the game. This is the kind of automation that PyAutoGUI is capable of.

# Examples

```
>>> import pyautogui

>>> screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
>>> screenWidth, screenHeight
(2560, 1440)

>>> currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
>>> currentMouseX, currentMouseY
(1314, 345)

>>> pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

>>> pyautogui.click()          # Click the mouse.
>>> pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
>>> pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

>>> pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
>>> pyautogui.doubleClick()     # Double click the mouse.
>>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

>>> pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
>>> pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

>>> with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
        pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
>>> # Shift key is released automatically.

>>> pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

>>> pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.

```