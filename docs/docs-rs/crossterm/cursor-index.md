crossterm
# Module cursor 
Source 
## Structs§
DisableBlinkingA command that disables blinking of the terminal cursor.EnableBlinkingA command that enables blinking of the terminal cursor.HideA command that hides the terminal cursor.MoveDownA command that moves the terminal cursor a given number of rows down.MoveLeftA command that moves the terminal cursor a given number of columns to the left.MoveRightA command that moves the terminal cursor a given number of columns to the right.MoveToA command that moves the terminal cursor to the given position (column, row).MoveToColumnA command that moves the terminal cursor to the given column on the current row.MoveToNextLineA command that moves the terminal cursor down the given number of lines,
and moves it to the first column.MoveToPreviousLineA command that moves the terminal cursor up the given number of lines,
and moves it to the first column.MoveToRowA command that moves the terminal cursor to the given row on the current column.MoveUpA command that moves the terminal cursor a given number of rows up.RestorePositionA command that restores the saved terminal cursor position.SavePositionA command that saves the current terminal cursor position.ShowA command that shows the terminal cursor.
## Enums§
SetCursorStyleA command that sets the style of the cursor.
It uses two types of escape codes, one to control blinking, and the other the shape.
## Functions§
positionReturns the cursor position (column, row).