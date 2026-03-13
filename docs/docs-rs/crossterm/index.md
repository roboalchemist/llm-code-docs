# Crate crossterm 
Source 
## Modules§
clipboardA module for clipboard interactioncursorA module to work with the terminal cursoreventA module to read events.styleA module to apply attributes and colors on your text.terminalA module to work with the terminal.ttyA module to query if the current instance is a tty.
Making it a little more convenient and safe to query whether
something is a terminal teletype or not.
This module defines the IsTty trait and the is_tty method to
return true if the item represents a terminal.
## Macros§
executeExecutes one or more command(s).queueQueues one or more command(s) for further execution.
## Traits§
CommandAn interface for a command that performs an action on the terminal.ExecutableCommandAn interface for types that can directly execute commands.QueueableCommandAn interface for types that can queue commands for further execution.SynchronizedUpdateAn interface for types that support synchronized updates.