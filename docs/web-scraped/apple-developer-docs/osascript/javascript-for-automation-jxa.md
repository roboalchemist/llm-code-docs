# JavaScript for Automation (JXA)

# Source: https://github.com/JXA-Cookbook/JXA-Cookbook/wiki/Using-JavaScript-for-Automation

# Source: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/

JavaScript for Automation (JXA) is a JavaScript-based scripting interface for macOS that provides peer functionality to AppleScript. It was introduced in OS X 10.10 (Yosemite) and uses the same automation framework as AppleScript.

## Overview

JXA provides:

- **Modern JavaScript syntax** - Familiar to web developers
- **Apple Event integration** - Access to scriptable macOS applications
- **Objective-C bridge** - Direct access to Objective-C frameworks
- **Standard library** - Common utilities for file and system operations
- **Object-oriented approach** - Work with application objects and properties

## Basic Syntax

### Hello World

```javascript
// Simple alert
var app = Application.currentApplication()
app.activate()
app.displayAlert('Hello World')

// Console output
console.log('Hello from JXA')

// Return value (displayed by osascript)
'Done'
```

### The Run Handler

```javascript
// Implicit: the last expression is returned
Application("Safari").activate()

// Explicit run function (for arguments)
function run(argv) {
  console.log(argv[0])  // First argument
  return "Finished"
}
```

### Comments

```javascript
// Single-line comment
console.log('test')

/* Multi-line
   comment */
var x = 1
```

## Running JXA Scripts

### With osascript (One-Liner)

```bash
osascript -l JavaScript -e 'Application("Safari").activate()'
```

### From File

Create `script.js`:

```javascript
Application("Safari").activate()
```

Run with osascript:

```bash
osascript -l JavaScript script.js
```

### Executable Script (Shebang)

Create `script.js` with shebang:

```javascript
#!/usr/bin/osascript -l JavaScript

Application("Safari").activate()
```

Make executable:

```bash
chmod +x script.js
./script.js
```

### Interactive REPL

```bash
osascript -i -l JavaScript
```

Then type commands directly:

```javascript
> Application("Safari").activate()
```

## Accessing Applications

### Get Application Reference

```javascript
var safari = Application("Safari")
var finder = Application("Finder")
var system = Application("System Events")
```

### Activate (Bring to Front)

```javascript
Application("Safari").activate()
```

### Check if Application is Running

```javascript
var safari = Application("Safari")
if (safari.running()) {
  console.log("Safari is running")
}
```

### Get Current Application

```javascript
var app = Application.currentApplication()
```

## Working with Application Objects

### Access Application Properties

```javascript
var safari = Application("Safari")

// Get window information
var windows = safari.windows()  // Array of windows
var activeWindow = safari.windows()[0]

// Get tabs (if supported)
var tabs = activeWindow.tabs()
var currentTab = activeWindow.currentTab()

// Get URL
var url = currentTab.url()
```

### Manipulate Application Properties

```javascript
var safari = Application("Safari")

// Open a new tab
safari.open(Path("https://example.com"))

// Set URL
safari.windows()[0].currentTab().url = "https://example.com"

// Get/set properties
var finder = Application("Finder")
finder.desktop()  // Get desktop folder object
```

### Call Application Methods

```javascript
// Open location
Application("Safari").openLocation("https://example.com")

// Activate window
Application("Safari").activate()
```

## Common Applications

### Safari

```javascript
var safari = Application("Safari")

// Activate
safari.activate()

// Open URL
safari.openLocation("https://example.com")

// Get current tab URL
var url = safari.windows()[0].currentTab().url()

// Execute JavaScript in page
safari.windows()[0].currentTab().doJavaScript("console.log('test')")

// Close current tab
safari.windows()[0].currentTab().close()
```

### Finder

```javascript
var finder = Application("Finder")

// Activate
finder.activate()

// Get desktop files
var desktop = finder.desktop()
var files = desktop.files()

// Reveal file/folder
finder.reveal("/Users/username/Documents")

// Get home folder
var homeFolder = finder.home()

// Make new folder
var newFolder = finder.make({ new: "folder", at: homeFolder })

// List folder contents
var contents = finder.items({ from: homeFolder })
```

### System Events

```javascript
var system = Application("System Events")

// Get system information
var sysInfo = system.systemInfo()

// Check dark mode
var isDarkMode = system.appearancePreferences.darkMode()

// Set dark mode
system.appearancePreferences.darkMode = true

// Simulate keyboard
system.keystroke("a", { using: "command down" })

// Simulate mouse click
system.click(point)
```

### Mail

```javascript
var mail = Application("Mail")

// Activate
mail.activate()

// Get accounts
var accounts = mail.accounts()

// Get mailboxes
var mailboxes = mail.mailboxes()

// Create message
var newMessage = mail.make({ new: "outgoing message" })
newMessage.subject = "Hello"
newMessage.content = "Message body"
newMessage.send()
```

### Finder with File Operations

```javascript
var finder = Application("Finder")

// Get Documents folder
var docs = finder.home().folders.byName("Documents")[0]

// List files
finder.items({ from: docs }).forEach(function(item) {
  console.log(item.name())
})

// Delete a file
var file = docs.files.byName("oldfile.txt")[0]
file.delete()

// Move file
file.moveTo(otherFolder)
```

## File and Folder Operations

### Working with Paths

```javascript
// Import ObjC for path utilities
ObjC.import('Foundation')

// Create path
var path = "/Users/username/Documents"

// Home directory
var home = $.NSHomeDirectory()

// Expand tilde
var expanded = $.NSString.stringWithString("~/Documents")
                         .stringByExpandingTildeInPath()

// Join paths
var joined = $.NSString.stringWithString(home)
                       .stringByAppendingPathComponent("Documents")
```

### Read File

```javascript
// Simple read
var file = $.NSString.stringWithContentsOfFile_encoding_error(
  "/path/to/file",
  $.NSUTF8StringEncoding,
  null
)

// Or using ObjC
ObjC.import('Foundation')
var contents = $.NSString.stringWithContentsOfFile_encoding_error(
  "/path/to/file.txt",
  $.NSUTF8StringEncoding,
  null
)
console.log(ObjC.unwrap(contents))
```

### Write File

```javascript
ObjC.import('Foundation')

var content = "File content here"
var path = "/tmp/test.txt"

var string = $.NSString.stringWithString(content)
string.writeToFile_atomically_encoding_error(
  path,
  true,
  $.NSUTF8StringEncoding,
  null
)

console.log("File written")
```

### Check File Existence

```javascript
ObjC.import('Foundation')

var path = "/path/to/file"
var manager = $.NSFileManager.defaultManager

if (manager.fileExistsAtPath(path)) {
  console.log("File exists")
} else {
  console.log("File does not exist")
}
```

### List Files in Directory

```javascript
ObjC.import('Foundation')

var path = "/Users/username/Documents"
var manager = $.NSFileManager.defaultManager

var contents = manager.contentsOfDirectoryAtPath_error(path, null)
var files = ObjC.unwrap(contents)

files.forEach(function(file) {
  console.log(file)
})
```

## User Interaction

### Display Alert

```javascript
var app = Application.currentApplication()
app.activate()

app.displayAlert("Alert Title", {
  message: "This is the message",
  buttons: ["Cancel", "OK"],
  defaultButton: 1,
  cancelButton: 1
})
```

### Display Dialog (with Input)

```javascript
var app = Application.currentApplication()
app.activate()

var result = app.displayDialog("Enter your name:", {
  defaultAnswer: "Default",
  buttons: ["Cancel", "OK"],
  defaultButton: "OK",
  cancelButton: "Cancel"
})

var userName = result.textReturned
```

### Display Notification

```javascript
// Simple notification
var app = Application.currentApplication()
app.activate()
app.displayNotification("This is a notification", {
  withTitle: "Title",
  subtitle: "Subtitle"
})
```

### Alert with Buttons

```javascript
var app = Application.currentApplication()
app.activate()

var response = app.displayAlert("Proceed?", {
  message: "Do you want to continue?",
  buttons: ["No", "Yes"],
  defaultButton: 2
})

if (response.buttonReturned === "Yes") {
  console.log("User clicked Yes")
}
```

## Data Types and Operators

### Basic Types

```javascript
// String
var str = "Hello"
console.log(str)

// Number
var num = 42
var decimal = 3.14

// Boolean
var flag = true

// Array
var arr = [1, 2, 3, 4, 5]

// Object
var obj = { name: "John", age: 30 }

// Null/Undefined
var empty = null
var notSet = undefined
```

### String Operations

```javascript
var str = "Hello World"

// Length
str.length  // 11

// Concatenation
str + " from JXA"

// Substring
str.substring(0, 5)  // "Hello"

// Methods
str.toLowerCase()
str.toUpperCase()
str.includes("World")
str.split(" ")  // ["Hello", "World"]
```

### Array Operations

```javascript
var arr = [1, 2, 3, 4, 5]

// Length
arr.length

// Access elements
arr[0]  // 1

// Add element
arr.push(6)

// Remove element
arr.pop()

// Iterate
arr.forEach(function(item) {
  console.log(item)
})

// Map/Filter
arr.map(x => x * 2)
arr.filter(x => x > 2)
```

## Control Flow

### If/Else

```javascript
var x = 10

if (x > 5) {
  console.log("x is greater than 5")
} else if (x === 5) {
  console.log("x is 5")
} else {
  console.log("x is less than 5")
}
```

### Loops

```javascript
// For loop
for (var i = 0; i < 5; i++) {
  console.log(i)
}

// While loop
var j = 0
while (j < 5) {
  console.log(j)
  j++
}

// ForEach
[1, 2, 3].forEach(function(item) {
  console.log(item)
})

// For...in (object properties)
var obj = { a: 1, b: 2, c: 3 }
for (var key in obj) {
  console.log(key + ": " + obj[key])
}
```

### Try/Catch

```javascript
try {
  // Code that might error
  Application("NonExistentApp").activate()
} catch (error) {
  console.log("Error: " + error)
}
```

## Functions

### Define and Call

```javascript
function greet(name) {
  return "Hello, " + name
}

console.log(greet("World"))
```

### Arrow Functions

```javascript
var add = (a, b) => a + b
console.log(add(5, 3))  // 8

var double = x => x * 2
console.log(double(5))  // 10
```

### Default Parameters

```javascript
function greet(name = "World") {
  return "Hello, " + name
}

console.log(greet())  // "Hello, World"
```

## Objective-C Integration

### Import Frameworks

```javascript
ObjC.import('Foundation')
ObjC.import('Cocoa')
ObjC.import('AppKit')
```

### Access Objective-C Classes

```javascript
ObjC.import('Foundation')

// Create object
var array = $.NSMutableArray.array()
array.addObject_("hello")

// Call methods
var string = $.NSString.stringWithString("test")
console.log(ObjC.unwrap(string))

// Access properties
var value = obj.property
obj.property = newValue
```

### Converting Types

```javascript
// Unwrap ObjC objects to JavaScript
var nsString = $.NSString.stringWithString("hello")
var jsString = ObjC.unwrap(nsString)

// Wrap JavaScript values to ObjC
var nsArray = $(["a", "b", "c"])
```

### JSON and Serialization

```javascript
ObjC.import('Foundation')

var dict = { name: "John", age: 30 }
var jsonData = $.NSJSONSerialization.dataWithJSONObject_options_error(
  dict,
  0,
  null
)
var jsonString = $.NSString.alloc.initWithData_encoding(jsonData, $.NSUTF8StringEncoding)
console.log(ObjC.unwrap(jsonString))
```

## Scripting Bridge Concepts

### Reference Forms

```javascript
// By index
var file = finder.documents()[0]

// By name
var file = finder.documents.byName("file.txt")[0]

// By ID
var file = finder.documents.byId(123)[0]

// All items
var allFiles = finder.documents()
```

### Property Access

```javascript
var finder = Application("Finder")
var desktop = finder.desktop()

// Get properties
var name = desktop.name()
var kind = desktop.kind()

// Set properties
desktop.name = "New Name"

// Properties with parameters
var items = finder.items({ from: someFolder })
```

## Debugging

### Console Output

```javascript
console.log("Log message")
console.log("Value:", variable)
console.log({ property: value })
```

### Inspect Objects

```javascript
var app = Application("Safari")
console.log(app.windows())  // Show window objects
console.log(app.windows()[0].currentTab())  // Show tab object
```

### Error Messages

```javascript
try {
  someFunction()
} catch (error) {
  console.log("Error name: " + error.name)
  console.log("Error message: " + error.message)
  console.log("Full error: " + error)
}
```

### Script Editor Debugging

1. Open `/Applications/Utilities/Script Editor.app`
2. Change language to "JavaScript"
3. Paste JXA code
4. Click "Run"
5. View results in output panel
6. Errors show in console

## Common Patterns

### Process Finder Files

```javascript
var finder = Application("Finder")
var desktop = finder.desktop()
var files = desktop.files()

files.forEach(function(file) {
  var name = file.name()
  var kind = file.kind()
  console.log(name + ": " + kind)
})
```

### Batch Rename Files

```javascript
var finder = Application("Finder")
var docs = finder.documents()  // Or any folder

docs.forEach(function(file, index) {
  var oldName = file.name()
  var newName = "file_" + (index + 1)
  file.name = newName
  console.log(oldName + " -> " + newName)
})
```

### Create Folder Structure

```javascript
var finder = Application("Finder")
var desktop = finder.desktop()

var mainFolder = finder.make({
  new: "folder",
  at: desktop,
  withProperties: { name: "MyProject" }
})

var subFolder = finder.make({
  new: "folder",
  at: mainFolder,
  withProperties: { name: "SubFolder" }
})

console.log("Folders created")
```

### Check System Properties

```javascript
var system = Application("System Events")

// Dark mode
var isDark = system.appearancePreferences.darkMode()
console.log("Dark mode: " + isDark)

// Get computer name
var computerName = system.computerName()
console.log("Computer: " + computerName)

// Get user name
var userName = system.userName()
console.log("User: " + userName)
```

### Open Multiple Applications

```javascript
var apps = ["Safari", "Mail", "Finder"]

apps.forEach(function(appName) {
  Application(appName).activate()
  delay(0.5)  // Wait 0.5 seconds
})
```

## Limitations

- **No multi-threading** - Single-threaded execution
- **Limited documentation** - Less comprehensive than AppleScript
- **Performance** - Can be slower than compiled languages
- **Compatibility** - Requires macOS 10.10+
- **Sandboxing** - Restricted for sandboxed apps
- **Error recovery** - Cryptic error messages sometimes

## Performance Tips

1. **Minimize application activation** - Bringing apps to front is slow
2. **Batch operations** - Do multiple operations per app access
3. **Cache references** - Store application objects instead of recreating
4. **Use background scripts** - Don't rely on UI automation when possible
5. **Avoid redundant operations** - Check before repeating actions

## Resources

- **JXA Cookbook**: https://github.com/JXA-Cookbook/JXA-Cookbook
- **Apple Automation Guide**: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/
- **Objective-C Bridge**: Bridge between JXA and native Objective-C frameworks
- **Script Editor**: Built-in IDE for writing and testing JXA scripts

## Tips for Learning

1. **Start with Script Editor** - Test syntax interactively
2. **Check application dictionary** - Open/Show Library in Script Editor
3. **Use console.log** - Debug output like JavaScript in browser
4. **Try existing examples** - JXA Cookbook has many working examples
5. **Convert AppleScript** - Most AppleScript can be converted to JXA
