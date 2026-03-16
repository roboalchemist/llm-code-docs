# Keyboard Control Functions

## The write() Function

The primary keyboard function is `write()`. This function will type the characters in the string that is passed. To add a delay interval in between pressing each character key, pass an int or float for the `interval` keyword argument.

For example:

```
>>> pyautogui.write('Hello world!')                 # prints out "Hello world!" instantly
>>> pyautogui.write('Hello world!', interval=0.25)  # prints out "Hello world!" with a quarter second delay after each character

```