crossterm
# Module terminal 
Source 
## Structs§
BeginSynchronizedUpdateA command that instructs the terminal emulator to begin a synchronized frame.ClearA command that clears the terminal screen buffer.DisableLineWrapDisables line wrapping.EnableLineWrapEnable line wrapping.EndSynchronizedUpdateA command that instructs the terminal to end a synchronized frame.EnterAlternateScreenA command that switches to alternate screen.LeaveAlternateScreenA command that switches back to the main screen.ScrollDownA command that scrolls the terminal screen a given number of rows down.ScrollUpA command that scrolls the terminal screen a given number of rows up.SetSizeA command that sets the terminal buffer size `(columns, rows)`.SetTitleA command that sets the terminal titleWindowSize
## Enums§
ClearTypeDifferent ways to clear the terminal buffer.
## Functions§
disable_raw_modeDisables raw mode.enable_raw_modeEnables raw mode.is_raw_mode_enabledTells whether the raw mode is enabled.sizeReturns the terminal size `(columns, rows)`.supports_keyboard_enhancementQueries the terminal’s support for progressive keyboard enhancement.window_sizeReturns the terminal size `[WindowSize]`.