# osascript - macOS AppleScript and JXA Execution

# Source: https://developer.apple.com/library/archive/documentation/AppleScript/
# Source: https://ss64.com/mac/osascript.html
# Source: https://www.manpagez.com/man/1/osascript/

osascript is the command-line tool for executing AppleScript and JavaScript for Automation (JXA) scripts on macOS. It enables automation of Mac applications and system tasks.

## Overview

osascript executes scripts written in AppleScript or JavaScript for Automation (JXA) and is part of the Open Scripting Architecture (OSA) framework. It allows users to:

- Automate macOS applications via Apple Events
- Combine features from multiple scriptable applications
- Create powerful workflow solutions
- Reduce errors and save time on repetitive tasks
- Control system functions and settings

## Syntax

```bash
osascript [-l language] [-s flags] [-e statement | programfile] [argument ...]
```

## Common Options

### Language Selection
- **`-l language`** - Override the default language for plain text files
  - Default language is AppleScript
  - Can specify `JavaScript` for JXA scripts
  - Used when processing plain text files, not compiled scripts

### Script Input
- **`-e statement`** - Enter one line of script code
  - Multiple `-e` flags can be combined to build multi-line scripts
  - Useful for quick one-liners from shell
  - Arguments following the script are passed to the run handler

- **`programfile`** - Read script from a file
  - Can be plain text or pre-compiled script
  - File extension determines processing (if plain text)
  - Use for larger scripts or reusable script files

### Output Formatting
- **`-s flags`** - Modify output formatting using modifier characters:
  - **`h`** - Human-readable form (default, without quotes or escape sequences)
  - **`s`** - Source form (recompilable, with escape sequences and quotes)
  - **`e`** - Errors to stderr (default)
  - **`o`** - Errors to stdout

### Interactive Mode
- **`-i`** - Interactive mode with line-by-line prompts
  - Shows input/output for debugging
  - Useful for testing script snippets

## Script Arguments

Script arguments are passed to the script's `run` handler as a list of strings. In AppleScript, access them via:

```applescript
on run argv
    -- argv is a list of strings passed from command line
    log argv
end run
```

## Common Usage Examples

### Simple AppleScript Command

```bash
osascript -e 'tell app "Safari" to activate'
```

This brings Safari to the front.

### Multi-line AppleScript

```bash
osascript -e 'tell application "System Events"' \
          -e 'set volume output volume 50' \
          -e 'end tell'
```

### Display a Dialog

```bash
osascript -e 'display dialog "Hello, World!" buttons {"OK"} default button "OK"'
```

Returns the button clicked.

### Get Dialog Input

```bash
osascript -e 'display dialog "Enter your name:" default answer "" buttons {"Cancel", "OK"} default button "OK"' \
          -e 'text returned of result'
```

### System Control Examples

**Adjust system volume:**
```bash
osascript -e 'set volume output volume 75'
```

**Toggle dark mode:**
```bash
osascript -e 'tell application "System Events"' \
          -e '  tell appearance preferences' \
          -e '    set dark mode to not dark mode' \
          -e '  end tell' \
          -e 'end tell'
```

**Get current date and time:**
```bash
osascript -e 'current date'
```

**Get system information:**
```bash
osascript -e 'system info'
```

### Working with Files and Clipboard

**Get clipboard contents:**
```bash
osascript -e 'the clipboard'
```

**Set clipboard contents:**
```bash
osascript -e 'set the clipboard to "Hello World"'
```

**Get file information:**
```bash
osascript -e 'info for (path to home folder)'
```

### Running Shell Commands from AppleScript

```bash
osascript -e 'do shell script "ls -la ~"'
```

This executes a shell command and returns its output.

### Using Arguments

```bash
osascript -e 'on run argv' \
          -e '  display dialog item 1 of argv' \
          -e 'end run' \
          "Hello from command line"
```

### Text-to-Speech

```bash
osascript -e 'say "Hello, I am speaking to you"'
```

With specific voice:
```bash
osascript -e 'say "Hello" using "Victoria"'
```

### Notification Center

```bash
osascript -e 'display notification "Alert message" with title "Title" subtitle "Subtitle"'
```

## JavaScript for Automation (JXA)

JXA is a JavaScript-based scripting interface introduced in OS X 10.10 that provides peer functionality to AppleScript.

### Basic JXA Syntax

```javascript
// Simple JXA to activate Safari
Application("Safari").activate()
```

### Running JXA with osascript

```bash
osascript -l JavaScript -e 'Application("Safari").activate()'
```

### JXA Script File

Create a script file with shebang:

```bash
#!/usr/bin/osascript -l JavaScript

// Get Safari URL
var safari = Application("Safari")
var window = safari.windows[0]
var tab = window.currentTab
safari.activate()
```

Make executable and run:
```bash
chmod +x script.js
./script.js
```

### Accessing Applications

```javascript
// Get application reference
var app = Application("Finder")

// List volumes
app.disks()

// Get home folder
Application("Finder").home()
```

### System Events

```javascript
// Get system information
var sys = Application("System Events")

// Check if dark mode is enabled
sys.appearancePreferences.darkMode()

// List running processes
sys.processes.whose({ visible: true })()
```

### File Operations

```javascript
// Read file content
var fileContents = $('/path/to/file').contents
var text = ObjC.unwrap(fileContents)

// Path handling
var Path = $.NSString.stringWithString(path)
var manager = $.NSFileManager.defaultManager

// Check file existence
manager.fileExistsAtPath(Path)
```

### User Interaction

```javascript
// Alert dialog
var app = Application.currentApplication()
app.activate()
app.displayAlert('Alert Title', {
    message: 'This is the message',
    buttons: ['Cancel', 'OK'],
    defaultButton: 'OK',
    cancelButton: 'Cancel'
})

// Input dialog
app.displayDialog('Enter text:', {
    defaultAnswer: 'default value',
    buttons: ['Cancel', 'OK'],
    defaultButton: 'OK'
})
```

### Objective-C Bridge

JXA can access Objective-C libraries directly:

```javascript
// Import frameworks
ObjC.import('Foundation')
ObjC.import('Cocoa')

// Use Objective-C APIs
var alert = $.NSAlert.alloc.init
alert.messageText = "Title"
alert.informativeText = "Message"
alert.runModal
```

## Output Formatting

### Default Human-Readable Format

```bash
$ osascript -e 'return {1, 2, 3}'
1, 2, 3
```

### Source Form (Recompilable)

```bash
$ osascript -s 's' -e 'return {1, 2, 3}'
{1, 2, 3}
```

Useful for capturing output that can be re-compiled.

### Error Handling

Default (errors to stderr):
```bash
osascript -e 'error "test error"' 2>/dev/null
```

Redirect errors to stdout:
```bash
osascript -s 'o' -e 'error "test error"'
```

## AppleScript Language Basics

### Tell Statements

The `tell` statement targets an application:

```applescript
tell application "Finder"
    -- Finder commands here
    activate
    make new folder at desktop
end tell
```

### Variables and Data Types

```applescript
set myString to "Hello"
set myNumber to 42
set myList to {1, 2, 3, 4}
set myRecord to {name:"John", age:30}
```

### Control Flow

**If statements:**
```applescript
if x > 5 then
    display dialog "Greater than 5"
else
    display dialog "Less than or equal to 5"
end if
```

**Repeat loops:**
```applescript
repeat 5 times
    beep
end repeat

repeat with i from 1 to 10
    log i
end repeat
```

### Handlers (Functions)

```applescript
on myHandler(param1, param2)
    return param1 + param2
end myHandler

myHandler(5, 3)  -- Returns 8
```

### Working with Properties

```applescript
tell application "Finder"
    set folderContents to every file of the desktop
    set folderCount to count of folderContents
end tell
```

## Scripting Additions

AppleScript has standard scripting additions that provide built-in commands:

### File Operations

```applescript
-- Read a file
open for access file "/path/to/file"
read file "/path/to/file"
close access file "/path/to/file"

-- Write to a file
open for access file "/path/to/file" with write permission
write "text" to file "/path/to/file"
close access file "/path/to/file"

-- File information
info for file "/path/to/file"
list folder "/path/to/folder"
```

### User Interaction

```applescript
-- Dialogs
display dialog "Message" buttons {"Button1", "Button2"}
display alert "Alert Title" message "Message text"
display notification "Notification text" with title "Title"

-- File/Folder selection
choose file
choose folder
choose from list myList

-- Color and application selection
choose color
choose application
```

### System Commands

```applescript
-- Shell execution
do shell script "ls -la"

-- System information
system info
current date

-- Beep sound
beep
beep 3  -- Beep 3 times

-- Volume control
set volume output volume 50

-- Text-to-speech
say "Hello world"
```

### Clipboard

```applescript
-- Get clipboard
the clipboard

-- Set clipboard
set the clipboard to "text"

-- Get clipboard information
clipboard info
```

## Inter-Application Communication

AppleScript uses Apple Events to communicate between applications. Each scriptable application defines its own command vocabulary.

### Common Application Targets

```applescript
-- Finder
tell application "Finder"
    make new folder at desktop with properties {name:"New Folder"}
    reveal file "/path/to/file"
    delete item
end tell

-- Safari
tell application "Safari"
    open location "https://example.com"
    set the URL of document 1 to "https://example.com"
    tell document 1 to do JavaScript "console.log('test')"
end tell

-- Mail
tell application "Mail"
    set newMessage to make new outgoing message
    tell newMessage
        set sender to "email@example.com"
        set subject to "Hello"
        set content to "Message body"
        send
    end tell
end tell

-- System Events
tell application "System Events"
    keystroke "a" using command down  -- Command+A
    click menu item "Copy" of menu 1 of menu bar item "Edit"
end tell
```

## Error Handling

```applescript
try
    -- Code that might error
    tell application "NonExistentApp"
        activate
    end tell
on error errMsg number errNum
    display dialog "Error: " & errMsg & " (Code: " & errNum & ")"
end try
```

## Compiling and Saving Scripts

### Using osacompile

```bash
# Compile AppleScript to .scpt
osacompile -o script.scpt script.applescript

# Run compiled script with osascript
osascript script.scpt
```

### Script Bundles

AppleScript can be saved as script bundles (.scptd) containing resources:

```bash
# Create script bundle
osacompile -o script.scptd script.applescript
```

## Performance Considerations

1. **Local execution** - osascript runs locally without network overhead
2. **Application activation** - Bringing apps to front is slower than background execution
3. **UI Automation** - UI automation via System Events is slower than direct Apple Events
4. **Script compilation** - Use pre-compiled scripts for repeated execution
5. **Threading** - AppleScript doesn't support multi-threading natively

## Security and Sandboxing

- **Script Editor** - Scripts must be approved in System Preferences > Security
- **Sandboxed apps** - Limited Apple Event access for sandboxed applications
- **Elevated privileges** - Use `sudo osascript` for admin commands
- **Credentials** - Never embed passwords in scripts; use Keychain instead

## Related Commands

- **`osacompile`** - Compile AppleScript to binary format
- **`osalang`** - List available OSA languages
- **`open`** - Open files and applications
- **`defaults`** - Read/write user defaults
- **`launchctl`** - Control launch daemons and agents

## Debugging Tips

### Print Debug Output

```applescript
log "Debug message"  -- Shows in Script Editor's Event Log
display dialog "Debug: " & myVar
```

### Test in Script Editor

1. Open `/Applications/Utilities/Script Editor.app`
2. Write or paste script
3. Click "Run" button
4. Check "Event Log" tab for results
5. Use "Compile" to check syntax

### Error Messages

Most errors include a line number. Use the Script Editor to debug:

```applescript
try
    1 / 0  -- Will error
on error message number n from object partial result pResult
    log "Error: " & message
    log "Error Number: " & n
    log "Object: " & object
end try
```

### Testing with osascript

```bash
# Run with error output
osascript -e 'tell app "Finder" to activate' 2>&1

# Use source format for debugging
osascript -s 's' -e 'return {1, 2, 3}'

# Interactive mode
osascript -i -e 'display dialog "Test"'
```

## Limitations

- **AppleScript complexity** - Language can be verbose and unintuitive
- **Documentation gaps** - Individual application dictionaries vary in quality
- **Maintenance burden** - Scripts may break with OS/app updates
- **JXA limitations** - Less documentation than AppleScript; some features missing
- **Performance** - Slower than compiled languages or direct APIs
- **Limited error recovery** - Error messages can be cryptic

## Real-World Examples

### Batch Rename Files

```applescript
tell application "Finder"
    set folderPath to choose folder
    set fileList to every file of folderPath

    repeat with thisFile in fileList
        set oldName to name of thisFile
        set newName to "renamed_" & oldName
        set name of thisFile to newName
    end repeat
end tell
```

### Backup Important Files

```applescript
set sourceFolder to (path to home folder as text) & "Documents:"
set backupFolder to (path to home folder as text) & "Backups:"

tell application "Finder"
    duplicate every file of folder sourceFolder to folder backupFolder
end tell
```

### Create Time-Based Notes

```applescript
set currentDate to current date
set dateStr to (month of currentDate as integer) & "-" & (day of currentDate) & "-" & (year of currentDate)

tell application "Notes"
    activate
    make new note with properties {name:dateStr, body:""}
end tell
```

### Automate Web Browsing

```applescript
tell application "Safari"
    activate
    open location "https://example.com"
    delay 2
    do JavaScript "window.scrollTo(0, document.body.scrollHeight);"
    -- Scroll to bottom
end tell
```

### System Monitoring

```bash
osascript -e 'do shell script "top -l 1 | grep CPU"'
```

### Control Presentation Software

```applescript
tell application "Keynote"
    activate
    present slideshow of document 1
    play slideshow
end tell
```

## Installation and Requirements

- **Available on** - macOS (Mac OS X 10.5 Leopard or later)
- **Location** - `/usr/bin/osascript`
- **Shebang** - `#!/usr/bin/osascript` or `#!/usr/bin/env osascript`
- **No installation required** - Built into macOS

## Version Information

- **AppleScript 2.0+** - Modern AppleScript version
- **JXA (JavaScript for Automation)** - Introduced in OS X 10.10 (Yosemite)
- **Compatibility** - Most scripts work across multiple macOS versions
- **Current support** - Still maintained and available in latest macOS

## Additional Resources

### Official Documentation
- Apple AppleScript Language Guide: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/
- Mac Automation Scripting Guide: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/

### Community Resources
- JXA Cookbook: https://github.com/JXA-Cookbook/JXA-Cookbook
- MacScripter Forums: https://www.macscripter.net/
- AppleScript User Manual: https://developer.apple.com/library/archive/documentation/AppleScript/

### Practical Guides
- SS64 osascript reference: https://ss64.com/mac/osascript.html
- O'Reilly AppleScript: The Definitive Guide (available online)
- DEVONtechnologies JXA Guide: https://www.devontechnologies.com/blog/20211005-jxa-javascript-for-applications

## Related Topics

- **Apple Events** - Inter-application communication framework
- **Script Editor** - IDE for writing and debugging AppleScript
- **Automator** - GUI-based automation alternative
- **Keyboard Maestro** - Advanced macro automation tool
- **FastScripts** - Script management and scheduling
- **LaunchAgents** - Scheduled script execution
