# osascript Command-Line Reference

# Source: https://www.manpagez.com/man/1/osascript/
# Source: https://ss64.com/mac/osascript.html

Quick reference for osascript command-line usage, options, and patterns.

## Basic Syntax

```bash
osascript [OPTIONS] [SCRIPT_SOURCE] [ARGUMENTS]
```

## Options

### Language Selection

```bash
-l LANGUAGE       Override language for plain text files (default: AppleScript)
                  Common values: AppleScript, JavaScript
```

Example:
```bash
osascript -l JavaScript -e 'console.log("test")'
osascript -l AppleScript -e 'display dialog "test"'
```

### Script Input Methods

```bash
-e STATEMENT      Execute inline script statement
                  Multiple -e flags concatenate to form multi-line script

PROGRAMFILE       Read script from file
                  Can be plain text or pre-compiled .scpt
                  Stdin used if no file specified and no -e flags
```

Examples:
```bash
# Single -e statement
osascript -e 'tell app "Safari" to activate'

# Multiple -e for multi-line script
osascript -e 'tell application "Finder"' \
          -e '  activate' \
          -e 'end tell'

# From file
osascript ~/my-script.applescript

# From stdin
echo 'display dialog "test"' | osascript
```

### Output Formatting

```bash
-s FLAGS          Style flags for output formatting

  Flags:
    h             Human-readable output (default)
                  - No quotes around strings
                  - No escape sequences
                  - Reader-friendly format

    s             Source form (recompilable)
                  - With quotes and escape sequences
                  - Can be re-parsed as valid code
                  - More precise representation

    e             Errors to stderr (default)

    o             Errors to stdout
                  Instead of to stderr
```

Examples:
```bash
# Default: human-readable, errors to stderr
osascript -e 'return {1, 2, 3}'
# Output: 1, 2, 3

# Source form: recompilable format
osascript -s 's' -e 'return {1, 2, 3}'
# Output: {1, 2, 3}

# String with quotes (source form)
osascript -s 's' -e 'return "hello"'
# Output: "hello"

# String without quotes (human form)
osascript -e 'return "hello"'
# Output: hello

# Errors to stdout instead of stderr
osascript -s 'o' -e 'error "test"'
```

### Interactive Mode

```bash
-i                Interactive mode
                  Show input/output line by line
                  Useful for debugging scripts
```

Example:
```bash
osascript -i << 'EOF'
tell application "Finder"
  activate
end tell
EOF
```

## Script Arguments

Arguments following the script are passed to the `run` handler as a list of strings.

### AppleScript Arguments

```applescript
on run argv
    log argv  -- argv is a list of arguments
    log item 1 of argv  -- First argument
end run
```

Usage:
```bash
osascript script.applescript arg1 arg2 arg3
# argv = {"arg1", "arg2", "arg3"}
```

### JXA Arguments

```javascript
function run(argv) {
    console.log(argv)  // Array of arguments
    console.log(argv[0])  // First argument
}
```

Usage:
```bash
osascript -l JavaScript script.js arg1 arg2 arg3
# argv = ["arg1", "arg2", "arg3"]
```

## Common Patterns

### One-Liner Commands

Activate an application:
```bash
osascript -e 'tell app "Safari" to activate'
osascript -e 'tell application "Finder" to activate'
osascript -e 'tell application "Mail" to activate'
```

Get system information:
```bash
osascript -e 'system info'
osascript -e 'current date'
osascript -e 'system attribute "SystemVersion"'
```

Get clipboard:
```bash
osascript -e 'the clipboard'
```

Set clipboard:
```bash
osascript -e 'set the clipboard to "new content"'
```

Control volume:
```bash
osascript -e 'set volume output volume 50'  # Set to 50%
osascript -e 'set volume output volume 0'   # Mute
osascript -e 'set volume output volume 100' # Max
```

Text-to-speech:
```bash
osascript -e 'say "Hello world"'
osascript -e 'say "test" using "Victoria"'
```

### Multi-Line Scripts

```bash
osascript -e 'tell application "System Events"' \
          -e '  keystroke "a" using command down' \
          -e 'end tell'
```

With variables:
```bash
osascript -e 'set myVar to 42' \
          -e 'set myText to "hello"' \
          -e 'display dialog myText & ": " & myVar'
```

### Script Files

Create a script file:
```bash
cat > my-script.applescript << 'EOF'
tell application "Finder"
  activate
  set folderContents to every file of the desktop
  display dialog "Files: " & (count of folderContents)
end tell
EOF
```

Execute the script:
```bash
osascript my-script.applescript
```

With arguments:
```bash
osascript my-script.applescript arg1 arg2
```

### Shebang Scripts

Create an executable script:
```bash
#!/usr/bin/osascript
tell application "Safari" to activate
```

Or with specific language:
```bash
#!/usr/bin/osascript -l JavaScript
Application("Safari").activate()
```

Make executable and run:
```bash
chmod +x script.applescript
./script.applescript
```

### JavaScript for Automation (JXA)

Inline JXA:
```bash
osascript -l JavaScript -e 'Application("Safari").activate()'
```

JXA script file:
```bash
#!/usr/bin/osascript -l JavaScript
var app = Application("Finder")
app.activate()
var home = app.home()
console.log(home)
```

### Error Handling

Capture error output:
```bash
output=$(osascript -e 'some-command' 2>&1)
if [ $? -ne 0 ]; then
  echo "Error: $output"
fi
```

Suppress errors:
```bash
osascript -e 'command' 2>/dev/null
```

Errors to stdout (not stderr):
```bash
osascript -s 'o' -e 'error "test error"'
```

### Passing Shell Variables

```bash
VAR="hello world"
osascript -e "display dialog \"$VAR\""
```

Note: Be careful with special characters. Use single quotes when possible:
```bash
VAR="hello"
osascript -e 'tell app "Finder" to activate' \
          -e "set myVar to \"$VAR\"" \
          -e 'display dialog myVar'
```

## Return Values

osascript prints the result of the script to stdout.

### Different Data Types

```bash
# Boolean
osascript -e 'return true'
# Output: true

# Number
osascript -e 'return 42'
# Output: 42

# String (human-readable)
osascript -e 'return "hello"'
# Output: hello

# String (source form)
osascript -s 's' -e 'return "hello"'
# Output: "hello"

# List
osascript -e 'return {1, 2, 3}'
# Output: 1, 2, 3

# List (source form)
osascript -s 's' -e 'return {1, 2, 3}'
# Output: {1, 2, 3}

# Record
osascript -e 'return {name:"test", value:42}'
# Output: value:42, name:"test"
```

### Capturing Output

```bash
# Store in variable
result=$(osascript -e 'the clipboard')
echo "Clipboard: $result"

# Parse structured output
osascript -s 's' -e 'return {1, 2, 3}' | tr ',' '\n'
```

## Exit Status

- **0** - Script executed successfully
- **Non-zero** - Error occurred during execution

Example:
```bash
osascript -e 'tell app "Safari" to activate'
echo $?  # Prints 0 if successful
```

Error example:
```bash
osascript -e 'error "test"'
echo $?  # Prints non-zero error code
```

## Performance Tips

1. **Combine multiple -e flags** rather than calling osascript multiple times:
   ```bash
   # Slow (multiple process starts)
   osascript -e 'tell app "Safari" to activate'
   osascript -e 'tell app "Safari" to open location "test"'

   # Fast (single process)
   osascript -e 'tell application "Safari"' \
             -e '  activate' \
             -e '  open location "test"' \
             -e 'end tell'
   ```

2. **Use pre-compiled scripts** for repeated execution:
   ```bash
   osacompile -o script.scpt script.applescript
   osascript script.scpt  # Faster than parsing source
   ```

3. **Minimize application activation** when possible (slow operation)

4. **Use background-only commands** when UI isn't needed

## Common Scripting Tasks

### Application Control

Activate and focus:
```bash
osascript -e 'tell app "Safari" to activate'
```

Open URL:
```bash
osascript -e 'tell app "Safari" to open location "https://example.com"'
```

Quit application:
```bash
osascript -e 'tell app "Safari" to quit'
```

### File Operations

Get home folder:
```bash
osascript -e 'path to home folder'
```

Get desktop:
```bash
osascript -e 'path to desktop folder'
```

List files:
```bash
osascript -e 'tell application "Finder" to list folder (path to desktop folder)'
```

Make new folder:
```bash
osascript -e 'tell application "Finder"' \
          -e '  make new folder at desktop' \
          -e '  with properties {name:"NewFolder"}' \
          -e 'end tell'
```

### User Interaction

Simple dialog:
```bash
osascript -e 'display dialog "Are you sure?" buttons {"No", "Yes"} default button "Yes"'
```

Get text input:
```bash
osascript -e 'display dialog "Enter name:" default answer ""' \
          -e 'text returned of result'
```

Alert notification:
```bash
osascript -e 'display notification "Message" with title "Title"'
```

### System Commands

Run shell command:
```bash
osascript -e 'do shell script "uptime"'
```

With elevated privileges:
```bash
osascript -e 'do shell script "sudo command" with administrator privileges'
```

System sleep:
```bash
osascript -e 'tell application "System Events" to sleep'
```

Restart computer:
```bash
osascript -e 'tell application "System Events" to restart'
```

## Shell Integration Examples

### Loop with osascript

```bash
for i in {1..5}; do
  osascript -e "display dialog \"Number: $i\""
done
```

### Conditional Execution

```bash
if osascript -e 'tell app "Safari" to activate' 2>/dev/null; then
  echo "Safari activated"
else
  echo "Failed to activate Safari"
fi
```

### Pipe Data to osascript

```bash
echo "Hello from pipe" | osascript -e 'read from stdin' 2>/dev/null || \
  osascript -e 'display dialog "Hello"'
```

### Capture and Process Output

```bash
clipboard=$(osascript -e 'the clipboard')
if [ -z "$clipboard" ]; then
  echo "Clipboard is empty"
else
  echo "Clipboard: $clipboard"
fi
```

## Troubleshooting

### "osascript: command not found"
osascript is only available on macOS. On Linux/Windows, use a remote Mac or virtual machine.

### "Permission denied" errors
Use `sudo` for commands requiring elevated privileges:
```bash
sudo osascript -e 'command'
```

### "User canceled" errors
Some dialogs can be cancelled by the user, returning an error. Handle with try/catch:
```bash
osascript -e 'try' \
          -e '  display dialog "Continue?" buttons {"Cancel", "OK"}' \
          -e 'on error' \
          -e '  log "User cancelled"' \
          -e 'end try'
```

### Script syntax errors
Use Script Editor to test syntax before using in osascript:
1. Open `/Applications/Utilities/Script Editor.app`
2. Paste your script
3. Click "Compile" to check syntax
4. Use "Event Log" to see execution details

### Can't find application
Make sure application is installed and properly named:
```bash
# Check if app is installed
osascript -e 'tell application "Finder" to open location "/Applications"'

# Find exact app name
ls /Applications | grep -i appname
```

## Related Tools

- **osacompile** - Compile AppleScript to binary format
- **osalang** - List available OSA languages
- **open** - Open files and applications
- **say** - Text-to-speech (not via osascript)
- **defaults** - Read/write user preferences
- **launchctl** - Control launch agents/daemons
