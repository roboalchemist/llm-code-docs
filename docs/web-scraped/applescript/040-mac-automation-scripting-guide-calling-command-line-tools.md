# Mac Automation Scripting Guide: Calling Command-Line Tools

## Calling Command-Line Tools
In AppleScript, thedo shell scriptcommand is used to execute command-line tools. This command is implemented by the Standard Additions scripting addition included with OSÂ X.
Note
The Terminal app in/Applications/Utilities/is scriptable and provides another way to execute command-line tools from scripts.

### Executing Commands
The direct parameter of thedo shell scriptcommand is a string containing the shell code you want to execute, as demonstrated inListing 39-1, which simply lists a directory.
APPLESCRIPT
Open in Script Editor
- do shell script "ls /Applications/"
- (*
- --> Result:
- "App Store.app
- Automator.app
- Calculator.app
- Calendar.app
- ..."
- *)
Since the direct parameter ofdo shell scriptis a string, you can concatenate it with other strings at run time.Listing 39-2, for example, concatenates a shell command to a previously defined parameter value.
APPLESCRIPT
Open in Script Editor
- set theHostName to "www.apple.com"
- do shell script "ping -c1 " & theHostName

### Quoting Strings
The shell uses space characters to separate parameters and gives special meaning to certain punctuation marks, such as$,(,), and*. To ensure that strings are treated as expectedâfor example, spaces arenât seen as delimitersâitâs best to wrap strings in quotes. This process is known asquoting. If your string contains quotes, they must also beescaped(preceded by a/character) so they are interpreted as part of the string.Listing 39-3shows an example of an error occurring as a result of a parameter that contains a space.
APPLESCRIPT
Open in Script Editor
- set thePath to "/Library/Application Support/"
- do shell script "ls " & thePath
- --> Result: error "ls: /Library/Application: No such file or directory\rls: Support: No such file or directory" number 1
The easiest way to quote a string is to use thequoted formproperty of the text class, as demonstrated inListing 39-4. This property returns the string in a form thatâs safe from further interpretation by the shell, regardless of its contents.
APPLESCRIPT
Open in Script Editor
- set thePath to quoted form of "/Library/Application Support/"
- --> Result: "'/Library/Application Support/'"
- do shell script "ls " & thePath
- (*
- --> Result:
- "App Store
- Apple
- ...
- "
- *)

### More Information
For more information about thedo shell scriptcommand, seeCommands ReferenceinAppleScript Language GuideandTechnical Note TN2065.
Manipulating Images
Making a Systemwide Service
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13