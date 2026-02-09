# Commands Reference

This chapter describes the commands available to perform actions in AppleScript scripts. For information on how commands work, seeCommands Overview.
The commands described in this chapter are available to any scriptâthey are either built into the AppleScript language or added to it through the standard scripting additions (described inScripting Additions).
Note:In the command descriptions below, if the first item in the Parameters list does not include a parameter name, it is the direct parameter of the command (described inDirect Parameter).
Table 7-1lists each command according to the suite (or related group) of commands to which it belongs and provides a brief description. Detailed command descriptions follow the table, in alphabetical order.
Command
Description
AppleScript suite
activate
Brings an application to the front, and opens it if it is on the local computer and not already running.
In Script Editor, displays a value in the Event Log History window or in the Event Log pane of a script window.
Clipboard Commands suite
clipboard info
Returns information about the clipboard.
set the clipboard to
Places data on the clipboard.
the clipboard
Returns the contents of the clipboard.
File Commands suite
info for
Returns information for a file or folder.
list disks
Returns a list of the currently mounted volumes.
DeprecatedUsetell application "System Events" to get the name of every disk.
list folder
Returns the contents of a specified folder.
DeprecatedUsetell application "System Events" to get the name of every disk item of ....
mount volume
Mounts the specified AppleShare volume.
path to (application)
Returns the full path to the specified application.
path to (folder)
Returns the full path to the specified folder.
path to resource
Returns the full path to the specified resource.
File Read/Write suite
close access
Closes a file that was opened for access.
get eof
Returns the length, in bytes, of a file.
open for access
Opens a disk file for thereadandwritecommands.
read
Reads data from a file that has been opened for access.
set eof
Sets the length, in bytes, of a file.
write
Writes data to a file that was opened for access with write permission.
Internet suite
open location
Opens a URL with the appropriate program.
Miscellaneous Commands suite
current date
Returns the current date and time.
do shell script
Executes a shell script using theshshell.
get volume settings
Returns the sound output and input volume settings.
random number
Generates a random number.
round
Rounds a number to an integer.
set volume
Sets the sound output and/or input volume.
system attribute
Gets environment variables or attributes of this computer.
system info
Returns information about the system.
time to GMT
Returns the difference between local time and GMT (Universal Time).
Scripting suite
load script
Returns ascriptobject loaded from a file.
run script
Runs a script or script file
scripting components
Returns a list of all scripting components.
store script
Stores ascriptobject into a file.
Standard suite
copy
Copies one or more values into variables.
count
Counts the number of elements in an object.
Returns the value of a script expression or an application object.
launch
Launches the specified application without sending it aruncommand.
For an application, launches it. For a script application, launches it and sends it theruncommand. For a script script object, executes itsrunhandler.
Assigns one or more values to one or more script variables or application objects.
String Commands suite
ASCII character
Converts a number to a character.
Deprecatedstarting in AppleScript 2.0. Use theidproperty of thetextclass instead.
ASCII number
Converts a character to its numeric value.
Deprecatedstarting in AppleScript 2.0. Use theidproperty of thetextclass instead.
localized string
Returns the localized string for the specified key.
offset
Finds one piece of text inside another.
summarize
Summarizes the specified text or text file.
User Interaction suite
beep
Beeps one or more times.
choose application
Allows the user to choose an application.
choose color
Allows the user to choose a color.
choose file
Allows the user to choose a file.
choose file name
Allows the user to specify a new file reference.
choose folder
Allows the user to choose a folder.
choose from list
Allows the user to choose one or more items from a list.
choose remote application
Allows the user to choose a running application on a remote machine.
choose URL
Allows the user to specify a URL.
delay
Pauses for a fixed amount of time.
display alert
Displays an alert.
display dialog
Displays a dialog box, optionally requesting user input.
display notification
Displays a notification.
Speaks the specified text.
Brings an application to the front, launching it if necessary.

##### Syntax

##### Parameters

The application to activate.

##### Result

None.

##### Examples

```

activate application "TextEdit"```

```

tell application "TextEdit" to activate```

##### Discussion

Theactivatecommand does not launch applications on remote machines. For examples of other ways to specify an application, see theapplicationclass andRemote Applications.
Returns the character for a specified number.
Important:This command is deprecated starting in AppleScript 2.0âuse theidproperty of thetextclass instead.

##### Syntax

##### Parameters

The character code, an integer between 0 and 255.

##### Result

Atextobject containing the character that corresponds to the specified number.
Signals an error ifintegeris out of range.

##### Examples

```

set theChar to ASCII character 65 --result: "A"```

```

set theChar to ASCII character 194 --result: "Â¬"```

```

set theChar to ASCII character 2040 --result: invalid range error```

##### Discussion

The name âASCIIâ is something of a misnomer.ASCII characteruses the primary text encoding, as determined by the userâs language preferences, to map between integers and characters. If the primary language is English, the encoding is Mac OS Roman, if it is Japanese, the encoding is MacJapanese, and so on. For integers below 128, this is generally the same as ASCII, but for integers from 128 to 255, the results vary considerably.
Because of this unpredictability,ASCII characterandASCII numberare deprecated starting in AppleScript 2.0. Use theidproperty of thetextclass instead, since it always uses the same encoding, namely Unicode.
Returns the number associated with a specified character.
Important:This command is deprecated starting in AppleScript 2.0âuse theidproperty of thetextclass instead.

##### Syntax

##### Parameters

Atextobject containing at least one character. If there is more than one character, only the first one is used.

##### Result

The character code of the specified character as an integer.

##### Examples

```

set codeValue to ASCII number "Â¬" --result: 194```

##### Discussion

The result ofASCII numberdepends on the userâs language preferences; see the Discussion section ofASCII characterfor details.
Plays the system alert sound one or more times.

##### Syntax

##### Parameters

Number of times to beep.

##### Result

None.

##### Examples

Audible alerts can be useful when no one is expected to be looking at the screen:

```

beep 3 --result: three beeps, to get attention```

```

display dialog "Something is amiss here!" -- to show message```
Allows the user to choose an application.

##### Syntax

##### Parameters

Title text for the dialog.
"Choose Application"
A prompt to be displayed in the dialog.
"Select an application:"
Allow multiple items to be selected? Iftrue, the results will be returned in a list, even if there is exactly one item.
false
Specifies the desired class of the result. If specified, the value must be one ofapplicationoralias.
application

##### Result

The selected application, as either anapplicationoraliasobject; for example,application "TextEdit". If multiple selections are allowed, returns a list containing one item for each selected application, if any.
Signals a âuser canceledâ error if the user cancels the dialog. For an example of how to handle such errors, seetry Statements.

##### Examples

```

choose application with prompt "Choose a web browser:"```

```

choose application with multiple selections allowed```

```

choose application as alias```

##### Discussion

Thechoose applicationdialog initially presents a list of all applications registered with the system. To choose an application not in that list, use the Browse button, which allows the user to choose an application anywhere in the file system.
Allows the user to choose a color from a color picker dialog.

##### Syntax

##### Parameters

The color to show when the color picker dialog is first opened.
{0, 0, 0}: black.

##### Result

The selected color, represented as a list of three integers from 0 to 65535 corresponding to the red, green, and blue components of a color; for example, {0, 65535, 0} represents green.
Signals a âuser canceledâ error if the user cancels thechoose colordialog. For an example of how to handle such errors, seetry Statements.

##### Examples

This example lets the user choose a color, then uses that color to set the background color in their home folder (when it is in icon view):

```

tell application "Finder"```

```

    tell icon view options of window of home```

```

        choose color default color (get background color)```

```

        set background color to the result```

```

    end tell```

```

end tell```
Allows the user to choose a file.

##### Syntax

##### Parameters

The prompt to be displayed in the dialog.
None; no prompt is displayed.
A list of Uniform Type Identifiers (UTIs); for example,{"public.html", "public.rtf"}. Only files of the specified types will be selectable. For a list of system-defined UTIs, seeUniform Type Identifiers Overview. To get the UTI for a particular file, useinfo for.
Note:Four-character file type codes, such as"PICT"or"MooV", are also supported, but are deprecated. To get the file type code for a particular file, useinfo for.
None; any file can be chosen.
The folder to begin browsing in.
Browsing begins in the last selected location, or, if this is the first invocation, in the userâsDocumentsfolder.
Show invisible files and folders?
true: This is only for historical compatibility reasons. Unless you have a specific need to choose invisible files, you should always useinvisibles false.
Allow multiple items to be selected? Iftrue, the results will be returned in a list, even if there is exactly one item.
false
Show the contents of packages? Iftrue, packages are treated as folders, so that the user can choose a file inside a package (such as an application).
false. Manipulating the contents of packages is discouraged unless you control the package format or the package itself.

##### Result

The selected file, as analias. If multiple selections are allowed, returns a list containing onealiasfor each selected file, if any.
Signals a âuser canceledâ error if the user cancels the dialog. For an example of how to handle such errors, seetry Statements.

##### Examples

```

set aFile to choose file with prompt "HTML or RTF:" Â¬```

```

    of type {"public.html", "public.rtf"} invisibles false```
A UTI can specify a general class of files, not just a specific format. The following script allows the user to choose any image file, whether its format isJPEG,PNG,GIF, or whatever. It also uses thedefault locationparameter combined withpath to (folder)to begin browsing in the userâsPicturesfolder:

```

set picturesFolder to path to pictures folder```

```

choose file of type "public.image" with prompt "Choose an image:" Â¬```

```

    default location picturesFolder invisibles false```
Allows the user to specify a new filename and location. This does not create a fileârather, it returns a file specifier that can be used to create a file.

##### Syntax

##### Parameters

The prompt to be displayed near the top of the dialog.
"Specify new file name and location"
The default file name.
"untitled"
The default file location. Seechoose filefor examples.
Browsing starts in the last location in which a search was made or, if this is the first invocation, in the userâsDocumentsfolder.

##### Result

The selected location, as afile. For example:
file "HD:Users:currentUser:Documents:untitled"
Signals a âuser canceledâ error if the user cancels the dialog. For an example of how to handle such errors, seetry Statements.

##### Examples

The following example supplies a non-default prompt and search location:

```

set fileName to choose file name with prompt "Save report as:" Â¬```

```

default name "Quarterly Report" Â¬```

```

default location (path to desktop folder)```

##### Discussion

If you choose the name of a file or folder that exists in the selected location,choose file nameoffers the choice of replacing the chosen item. However, choosing to replace does not actually replace the item.
Allows the user to choose a directory, such as a folder or a disk.

##### Syntax

##### Parameters

The prompt to be displayed in the dialog.
None; no prompt is displayed.
The folder to begin browsing in.
Browsing begins in the last selected location, or, if this is the first invocation, in the userâsDocumentsfolder.
Show invisible folders?
false
Allow multiple items to be selected? Iftrue, the results will be returned in a list, even if there is exactly one item.
false
Show the contents of packages? Iftrue, packages are treated as folders, so that the user can choose a package folder, such as an application, or a folder inside a package.
false. Manipulating the contents of packages is discouraged unless you control the package format or the package itself.

##### Result

The selected directory, as analias. If multiple selections are allowed, returns a list containing onealiasfor each selected directory, if any.
Signals a âuser canceledâ error if the user cancels thechoose folderdialog. For an example of how to handle such errors, seetry Statements.

##### Examples

The following example specifies a prompt and allows multiple selections:

```

set foldersList to choose folder Â¬```

```

    with prompt "Select as many folders as you like:" Â¬```

```

    with multiple selections allowed```
The following example gets a POSIX path to a chosen folder and uses thequoted formproperty (of thetextclass) to ensure correct quoting of the resulting string for use with shell commands:

```

set folderName to quoted form of POSIX path of (choose folder)```
Suppose that you choose the folder namediWork '08in yourApplicationsfolder. The previous statement would return the following result, which properly handles the embedded single quote and space characters in the folder name:

```

"'/Applications/iWork '\\''08/'"```
Allows the user to choose items from a list.

##### Syntax

##### Parameters

A list of numbers and/ortextobjects for the user to choose from.
Title text for the dialog.
None; no title is displayed.
The prompt to be displayed in the dialog.
"Please make your selection:"
A list of numbers and/ortextobjects to be initially selected. The list cannot include multiple items unless you also specifymultiple selections allowed true. If an item in the default items list is not in the list to choose from, it is ignored.
None; no items are selected.
The name of the OK button.
"OK"
The name of the Cancel button.
"Cancel"
Allow multiple items to be selected?
false
Allow the user to choose OK with no items selected? Iffalse, the OK button will not be enabled unless at least one item is selected.
false

##### Result

If the user clicks the OK button, returns alistof the chosennumberand/ortextitems; if empty selection is allowed and nothing is selected, returns an empty list ({}). If the user clicks the Cancel button, returnsfalse.

##### Examples

This script selects from a list of all the people in Address Book who have defined birthdays, and gets the birthday of the selected one. Notice theif the result is not falsetest (choose from listreturnsfalseif the user clicks Cancel) and theset aName to item 1 of the result(choose from listreturns a list, even if it contains only one item).

```

tell application "Address Book"```

```

    set bDayList to name of every person whose birth date is not missing value```

```

    choose from list bDayList with prompt "Whose birthday would you like?"```

```

    if the result is not false then```

```

        set aName to item 1 of the result```

```

        set theBirthday to birth date of person named aName```

```

        display dialog aName & "'s birthday is " & date string of theBirthday```

```

    end if```

```

end tell```

##### Discussion

For historical reasons,choose from listis the only dialog command that returns a result (false) instead of signaling an error when the user presses the âCancelâ button.
Allows the user to choose a running application on a remote machine.

##### Syntax

##### Parameters

Title text for thechoose remote applicationdialog.
None; no title is displayed.
The prompt to be displayed in the dialog.
"Select an application:"

##### Result

The selected application, as anapplicationobject.
Signals a âuser canceledâ error if the user cancels the dialog. For an example of how to handle such errors, seetry Statements.

##### Examples

```

set myApp to choose remote application with prompt "Choose a remote web browser:"```

##### Discussion

The user may choose a remote machine usingBonjour or by entering a specific IP address. There is no way to limit the precise kind of application returned, so either limit your script to generic operations or validate the userâs choice. If you want your script to send application-specific commands to the resulting application, you will need a using terms from statement.
For information on targeting other machines, seeRemote Applications.
Allows the user to specify a URL.

##### Syntax

##### Parameters

A list that specifies the types of services to show, if available. The list can contain one or more of the following service types, or one or moretextobjects representing Bonjour service types (described below), or both:

- Web servers: showshttpandhttpsservices
Web servers: showshttpandhttpsservices

- FTP Servers: showsftpservices
FTP Servers: showsftpservices

- Telnet hosts: showstelnetservices
Telnet hosts: showstelnetservices

- File servers: showsafp,nfs, andsmbservices
File servers: showsafp,nfs, andsmbservices

- News servers: showsnntpservices
News servers: showsnntpservices

- Directory services: showsldapservices
Directory services: showsldapservices

- Media servers: showsrtspservices
Media servers: showsrtspservices

- Remote applications: showseppcservices
Remote applications: showseppcservices
Atextobject is interpreted as a Bonjour service typeâfor example,"_ftp._tcp"represents the file transfer protocol. These types are listed inTechnical Q&A 1312: Bonjour service types used in OS X.
File servers
Allow user to type in a URL? If you specifyeditable URL false, the text field in the dialog is inactive.
choose URLdoes not attempt to verify that the user-entered text is a valid URL. Your script should be prepared to verify the returned value.
true: the user can enter a text string. Iffalse, the user is restricted to choosing an item from the Bonjour-supplied list of services.

##### Result

The URL for the service, as atextobject. This result may be passed toopen locationor to any application that can handle the URL, such as a browser forhttpURLs.
Signals a âuser canceledâ error if the user cancels the dialog. For an example of how to handle such errors, seetry Statements.

##### Examples

The following script asks the user to choose an URL, either by typing in the text input field or choosing one of the Bonjour-located servers:

```

set myURL to choose URL```

```

tell application Finder to open location myURL```
Returns information about the current clipboard contents.

##### Syntax

##### Parameters

Restricts returned information to only this data type.
None; returns information for all types of data as a list of lists, where each list represents a scrap flavor.

##### Result

Alistcontaining one entry{class, size}for each type of data on the clipboard. To retrieve the actual data, use thethe clipboardcommand.

##### Examples

```

clipboard info```

```

clipboard info for Unicode text```
Closes a file opened with theopen for accesscommand.

##### Syntax

##### Parameters

The alias or file specifier or integer file descriptor of the file to close. A file descriptor must be obtained as the result of an earlieropen for accesscall.

##### Result

None.
Signals an error if the specified file is not open.

##### Examples

You should always close files that you open, being sure to account for possible errors while using the open file:

```

set aFile to choose file```

```

set fp to open for access aFile```

```

try```

```

    --file reading and writing here```

```

on error e number n```

```

    --deal with errors here and don't resignal```

```

end```

```

close access fp```

##### Discussion

Any files left open will be automatically closed when the application exits.
Copies one or more values, storing the result in one or more variables. This command only copies AppleScript values, not application-defined objects.

##### Syntax

##### Parameters

The expression whose value is to be copied.
The name of the variable or pattern of variables in which to store the value or pattern of values. Patterns may be lists or records.

##### Result

The new copy of the value.

##### Examples

As mentioned in the Discussion,copycreates an independent copy of the original value, and it creates a deep copy. For example:

```

set alpha to {1, 2, {"a", "b"}}```

```

copy alpha to beta```

```

set item 2 of item 3 of alpha to "change" --change the original list```

```

set item 1 of beta to 42 --change a different item in the copy```

```

{alpha, beta}```

```

--result: {{1, 2, {"a", "change"}}, {42, 2, {"a", "b"}}}```
Each variable reflects only the changes that were made directly to that variable. Compare this with the similar example inset.
See thesetcommand for examples of using variable patterns. The behavior is the same except that the values are copied.

##### Discussion

Thecopycommand may be used to assign new values to existing variables, or to define new variables. SeeDeclaring Variables with the copy Commandfor additional details.
Using thecopycommand creates a new value that is independent of the originalâa subsequent change to that value does not change the original value. The copy is a âdeepâ copy, so sub-objects, such as lists within lists, are also copied. Contrast this with the behavior of thesetcommand.
When usingcopywith an object specifier, the specifier itself is the value copied, not the object in the target application that it refers to.copytherefore copies the object specifier, but does not affect the application data at all. To copy the object in the target application, use the applicationâsduplicatecommand, if it has one.

##### Special Considerations

The syntaxputexpressionintovariablePatternis also supported, but is deprecated. It will be transformed into thecopyform when you compile the script.
Counts the number of elements in another object.

##### Syntax

##### Parameters

An expression that evaluates to an object with elements, such as alist,record, or application-defined container object.countwill count the contained elements.

##### Result

The number of elements, as aninteger.

##### Examples

In its simplest form,count, or the equivalent pseudo-propertynumber, counts theitemelements of a value. This may be an AppleScript value, such as a list:

```

set aList to {"Yes", "No", 4, 5, 6}```

```

count aList  --result: 5```

```

number of aList  --result: 5```
â¦or an application-defined object that hasitemelements:

```

tell application "Finder" to count disk 1  --result: 4```
If the value is an object specifier that evaluates to a list,countcounts the items of that list. This may be anEveryspecifier:

```

count every integer of aList  --result: 3```

```

count words of "hello world"  --result: 2```

```

tell application "Finder" to count folders of disk 1  --result: 4```
â¦or aFilterspecifier:

```

tell application "Finder"```

```

    count folders of disk 1 whose name starts with "A"  --result: 1```

```

end tell```
â¦or similar. For more on object specifiers, seeObject Specifiers.
Returns the current date and time.

##### Syntax

##### Result

The current date and time, as adateobject.

##### Examples

```

current date  --result: date "Tuesday, November 13, 2007 11:13:29 AM"```
See thedateclass for information on how to access the properties of a date, such as the day of the week or month.
Waits for a specified number of seconds.

##### Syntax

##### Parameters

The number of seconds to delay. The number may be fractional, such as0.5to delay half a second.

##### Result

None.

##### Examples

```

set startTime to current date```

```

delay 3  --delay for three seconds```

```

set elapsedTime to ((current date) - startTime)```

```

display dialog ("Elapsed time: " & elapsedTime & " seconds")```

##### Discussion

delaydoes not make any guarantees about the actual length of the delay, and it cannot be more precise than 1/60th of a second.delayis not suitable for real-time tasks such as audio-video synchronization.
Displays a standardized alert containing a message, explanation, and from one to three buttons.

##### Syntax

##### Parameters

The alert text, which is displayed in emphasized system font.
An explanatory message, which is displayed in small system font, below the alert text.
The type of alert to show. You can specify one of the following alert types:

- informational: the standard alert dialog
informational: the standard alert dialog

- warning: the alert dialog dialog is badged with a warning icon
warning: the alert dialog dialog is badged with a warning icon

- critical: currently the same as the standard alert dialog
critical: currently the same as the standard alert dialog
informational
A list of up to three button names.
If you supply one name, a button with that name serves as the default and is displayed on the right side of the alert dialog. If you supply two names, two buttons are displayed on the right, with the second serving as the default button. If you supply three names, the first is displayed on the left, and the next two on the right, as in the case with two buttons.
{"OK"}: One button labeled âOKâ, which is the default button.
The name or number of the default button. This may be the same as the cancel button.
The rightmost button.
The name or number of the cancel button. See âResultâ below. This may be the same as the default button.
None; there is no cancel button.
The number of seconds to wait before automatically dismissing the alert.
None; the dialog will wait until the user clicks a button.

##### Result

If the user clicks a button that was not specified as the cancel button,display alertreturns a record that identifies the button that was clickedâfor example,{button returned: "OK"}. If the command specifies agiving up aftervalue, the record will also contain agave up:falseitem.
If thedisplay alertcommand specifies agiving up aftervalue, and the dialog is dismissed due to timing out before the user clicks a button, the command returns a record indicating that no button was returned and the command gave up:{button returned:"", gave up:true}
If the user clicks the specified cancel button, the command signals a âuser canceledâ error. For an example of how to handle such errors, seetry Statements.

##### Examples

```

set alertResult to display alert "Insert generic warning here." Â¬```

```

    buttons {"Cancel", "OK"} as warning Â¬```

```

    default button "Cancel" cancel button "Cancel" giving up after 5```
For an additional example, see the Examples section for thetrystatement.
Displays a dialog containing a message, one to three buttons, and optionally an icon and a ï¬eld in which the user can enter text.

##### Syntax

##### Parameters

The dialog text, which is displayed in emphasized system font.
The initial contents of an editable text field. This edit field is not present unless this parameter is present; to have the field present but blank, specify an empty string:default answer ""
None; there is no edit field.
If true, any text in the edit field is obscured as in a password dialog: each character is displayed as a bullet.
false: text in the edit field is shown in cleartext.
A list of up to three button names.
If you donât specify any buttons, by default, Cancel and OK buttons are shown, with the OK button set as the default button.
If you specify any buttons, there is no default or cancel button unless you use the following parameters to specify them.
The name or number of the default button. This button is highlighted, and will be pressed if the user presses the Return or Enter key.
If there are no buttons specified usingbuttons, the OK button. Otherwise, there is no default button.
The name or number of the cancel button. This button will be pressed if the user presses the Escape key or Command-period.
If there are no buttons specified usingbuttons, the Cancel button. Otherwise, there is no cancel button.
The dialog window title.
None; no title is displayed.
The resource name or ID of the icon to display.
The type of icon to show. You may specify one of the following constants:

- stop(or0): Shows a stop icon
stop(or0): Shows a stop icon

- note(or1): Shows the application icon
note(or1): Shows the application icon

- caution(or2): Shows a warning icon, badged with the application icon
caution(or2): Shows a warning icon, badged with the application icon
Analiasorfilespecifier that specifies a.icnsfile.
The number of seconds to wait before automatically dismissing the dialog.
None; the dialog will wait until the user presses a button.

##### Result

A record containing the button clicked and text entered, if any. For example:
{text returned:"Cupertino", button returned:"OK"}
If the dialog does not allow text input, there is notext returneditem in the returned record.
If the user clicks the specified cancel button, the command signals a âuser canceledâ error. For an example of how to handle such errors, seetry Statements.
If thedisplay dialogcommand specifies agiving up aftervalue, and the dialog is dismissed due to timing out before the user clicks a button, it returns a record indicating that no button was returned and the command gave up:{button returned:"", gave up:true}

##### Examples

The following example shows how to use many of the parameters to adisplay dialogcommand, how to process possible returned values, and one way to handle a user cancelled error. The dialog displays two buttons and prompts a user to enter a name, giving up if they do not make a response within fifteen seconds. It shows one way to handle the case where the user cancels the dialog, which results in AppleScript signaling an âerrorâ with the error number -128. The script uses additionaldisplay dialogcommands to show the flow of logic and indicate where you could add statements to handle particular outcomes.

```

set userCanceled to false```

```

try```

```

    set dialogResult to display dialog Â¬```

```

        "What is your name?" buttons {"Cancel", "OK"} Â¬```

```

        default button "OK" cancel button "Cancel" Â¬```

```

        giving up after 15 Â¬```

```

        default answer (long user name of (system info))```

```

on error number -128```

```

    set userCanceled to true```

```

end try```

```

 ```

```

if userCanceled then```

```

    -- statements to execute when user cancels```

```

    display dialog "User cancelled."```

```

else if gave up of dialogResult then```

```

    -- statements to execute if dialog timed out without an answer```

```

    display dialog "User timed out."```

```

else if button returned of dialogResult is "OK" then```

```

    set userName to text returned of dialogResult```

```

    -- statements to process user name```

```

    display dialog "User name: " & userName```

```

end if```

```

end```
The following example displays a dialog that asks for a password. It supplies a default answer of"wrong", and specifies that the default answer, as well as any text entered by the user, is hidden (displayed as a series of bullets). It gives the user up to three chances to enter a correct password.

```

set prompt to "Please enter password:"```

```

repeat 3 times```

```

    set dialogResult to display dialog prompt Â¬```

```

        buttons {"Cancel", "OK"} default button 2 Â¬```

```

        default answer "wrong" with icon 1 with hidden answer```

```

    set thePassword to text returned of dialogResult```

```

    if thePassword = "magic" then```

```

        exit repeat```

```

    end if```

```

end repeat```

```

if thePassword = "magic" or thePassword = "admin" then```

```

    display dialog "User entered valid password."```

```

end if```
The password text is copied from the return valuedialogResult. The script doesnât check for a user cancelled error, so if the user cancels AppleScript stops execution of the script.
Posts a notification using the Notification Center, containing a title, subtitle, and explanation, and optionally playing a sound.

##### Syntax

##### Parameters

The body text of the notification. At least one of this and the title must be specified.
The title of the notification. At least one of this and the body text must be specified.
The subtitle of the notification.
The name of a sound to play when the notification appears. This may be the base name of any sound installed inLibrary/Sounds.

##### Result

None.

##### Examples

```

display notification "Encoding complete" subtitle "The encoded files are in the folder " & folderName```

##### Discussion

Exactly how the notification is presented is controlled by the âNotificationsâ preferences in System Preferences. Users may opt to display a reduced form of notification, turn off the sound, or even not display them at all.
Executes a shell script using theshshell.

##### Syntax

##### Parameters

The shell script to execute.
Specifies the desired type of the result. The raw bytes returned by the command will be interpreted as the specified class.
Â«class utf8Â»: UTF-8 text. If there is noasparameter and the output is not valid UTF-8, the output will be interpreted as text in the primary encoding.
Execute the command as the administrator? Once a script is correctly authenticated, it will not ask for authentication again for five minutes. The elevated privileges and the grace period do not extend to any other scripts or to the rest of the system. For security reasons, you may not tell another application todo shell script with administrator privileges. Put the command outside of anytellblock, or put it inside atell meblock.
false
The name of an administrator account. You can avoid a password dialog by specifying a name in this parameter and a password in thepasswordparameter. If you specify a user name, you must also specify a password.
An administrator password, typically used in conjunction with the administrator specified by theuser nameparameter. Ifuser nameis omitted, it is assumed to be the current user.
Should thedo shell scriptcommand change all line endings in the command output to Mac-style and trim a trailing one? For example, the result ofdo shell script "echo foo; echo bar"is"foo\rbar", not the"foo\nbar\n"that the shell script actually returned.
true

##### Result

The output of the shell script.
Signals an error if the shell script exits with a non-zero status. The error number will be the status, the error message will be the contents of stderr.

##### Examples

```

do shell script "uptime"```

##### Discussion

For additional documentation and examples of thedo shell scriptcommand, see Technical Note TN2065,do shell script in AppleScript.
Evaluates an object specifier and returns the result.
The command namegetis typically optionalâexpressions that appear as statements or operands are automatically evaluated as if they were preceded byget. However,getcan be used to force early evaluation of part of an object specifier.

##### Syntax

##### Parameters

An object specifier to be evaluated. If the specifier refers to an application-defined object, thegetcommand is sent to that application. Technically, all values respond toget, but for all values other than object specifiers,getis an identity operation: the result is the exact same value.
The desired class for the returned data. If the data is not of the desired type, AppleScript attempts to coerce it to that type.
None; no coercion is performed.

##### Result

The value of the evaluated expression. SeeReference Formsfor details on what the results of evaluating various object specifiers are.

##### Examples

getcan get properties or elements of AppleScript-defined objects, such as lists:

```

get item 1 of {"How", "are", "you?"}  --result: "How"```
â¦or of application-defined objects:

```

tell application "Finder" to get name of home  --result: "myname"```
As noted above, thegetis generally optional. For example, these statements are equivalent to the above two:

```

item 1 of {"How", "are", "you?"}  --result: "How"```

```

tell application "Finder" to name of home  --result: "myname"```
However, an explicitgetcan be useful for forcing early evaluation of part of an object specifier. Consider:

```

tell application "Finder" to get word 1 of name of home```

```

--Finder got an error: Canât get word 1 of name of folder "myname" of folder "Users" of startup disk.```
This fails because Finder does not know about elements oftext, such aswords. AppleScript does, however, so the script has to make Finder get only thename of ...part:

```

tell application "Finder" to get word 1 of (get name of home)```

```

--result: "myname"```
The explicitgetforces that part of the specifier to be evaluated; Finder returns atextresult, from which AppleScript can then getword 1.
For more information on specifiers, seeObject Specifiers.
Returns the length of a file, in bytes.

##### Syntax

##### Parameters

The file to obtain the length for, as an alias, a file specifier, or anintegerfile descriptor. A file descriptor must be obtained as the result of an earlieropen for accesscall.

##### Result

The logical size of the file, that is, the length of its contents in bytes.

##### Examples

This example obtains an alias to a desktop picture folder and usesget eofto obtain its length:

```

set desktopPicturesFolderPath to Â¬```

```

     (path to desktop pictures folder as text) & "Flow 1.jpg" as alias```

```

--result: alias "Leopard:Library:Desktop Pictures:Flow 1.jpg"```

```

get eof desktopPicturesFolderPath --result: 531486```
Returns the sound output and input volume settings.

##### Syntax

##### Result

A record containing the sound output and input volume settings. All the integer settings are between 0 (silent) and 100 (full volume):
The base output volume.
The input volume.
The alert volume. 100 for this setting means âas loud as the output volume.â
Is the output muted? If true, this overrides the output and alert volumes.

##### Examples

```

set volSettings to get volume settings```

```

--result: {output volume:43, input volume:35, alert volume:78, output muted:false}```
Return information for a file or folder.

##### Syntax

##### Parameters

An alias or file specifier for the file or folder.
Return the size of the file or folder? For a file, its âsizeâ is its length in bytes; for a folder, it is the sum of the sizes of all the files the folder contains.
true: Because getting the size of a folder requires getting the sizes of all the files inside it,size truemay take a long time for large folders such as/System. If you do not need the size, ask to not get it usingsize false. Alternatively, target the Finder or System Events applications to ask for the specific properties you want.

##### Result

A record containing information about the specified file or folder, with the following fields. Some fields are only present for certain kinds of items:
The itemâs full name, as it appears in the file system. This always includes the extension, if any. For example,"OmniOutliner Professional.app".
The itemâs name as it appears in Finder. This may be different than thenameif the extension is hidden or if the item has a localized name. For example,"OmniOutliner Professional".
The applicationâsCFBundleName, which is the name displayed in the menu bar when the application is active. This is often, but not always, the same as the displayed name. For example,"OmniOutliner Pro".
The extension part of the item name. For example, the name extension of the file âfoo.txtâ is"txt".
The packageâs bundle identifier. If the package is an application, this is the applicationâsid.
The itemâs type, as a Uniform Type Identifier (UTI). This is the preferred form for identifying item types, and may be used withchoose file.
The itemâs type, as displayed in Finder. This may be localized, and should only be used for display purposes.
The application that will open this item.
The date the item was created.
The date the item was last modified. Folder modification dates do not change when an item inside them changes, though they do change when an item is added or removed.
The itemâs type, as a four-character code. This is the classic equivalent of the type identifier, but less accurate and harder to interpret; usetype identifierif possible.
The itemâs four-character creator code. For applications, this is the classic equivalent of the bundle identifier, and will work for referencing an application by id. For files, this can be used to infer the default application, but not reliably; usedefault applicationif possible.
The itemâs short version string, as it appears in a Finder âGet Infoâ window. Any item may have this attribute, but typically only applications do.
The itemâs long version string, as it appears in a Finder âGet Infoâ window. Any item may have this attribute, but typically only applications do.
The itemâs size, in bytes. For more details, see thesizeparameter.
Is the item an alias file?
Is the item a folder? This is true for packages, such as application packages, as well as normal folders.
Is the item a package folder, such as an application? A package folder appears in Finder as if it is a file.
Is the itemâs name extension hidden?
Is the item visible? Typically, only special system files are invisible.
Is the item locked?
Is the item currently in use?
Iftrue, the item is reliably busy. Iffalse, the item may still be busy, because this status may not be supported by some applications or file systems.
The folderâs windowâs bounding rectangle, as list of four integers: {top, left, bottom, right}.

##### Examples

```

set downloadsFolder to path to downloads folder```

```

    --result: alias "HD:Users:me:Downloads:"```

```

info for downloadsFolder```

```

    --result: {name:"Downloads", folder:true, alias:false, ...}```

##### Special Considerations

Becauseinfo forreturns so much information, it can be slow, and because it only works on one file at a time, it can be difficult to use. The recommended technique is to use System Events or Finder to ask for the particular properties you want.
Launches an application, if it is not already running, but does not send it aruncommand.
If an application is already running, sending it alaunchcommand has no effect. That allows you to open an application without performing its usual startup procedures, such as opening a new window or, in the case of a script application, running its script. For example, you can use thelaunchcommand when you donât want an application to open and close visibly. This is less useful in AppleScript 2.0, which launches applications as hidden by default (even with theruncommand).
See theapplicationclass reference for information on how to use anapplicationobjectâsis runningproperty to determine if it is running without having to launch it.

##### Syntax

##### Parameters

The application to launch.

##### Result

None.

##### Examples

```

launch application "TextEdit"```

```

tell application "TextEdit" to launch```

##### Discussion

Thelaunchcommand does not launch applications on remote machines. For examples of other ways to specify an application, see theapplicationclass.
Many applications also support thereopencommand, which reactivates a running application or launches it if it isnât running. If the application is already running, this command has the same effect as double-clicking the application icon in the Finder. Each application determines how it will implement thereopencommandâsome may perform their usual startup procedures, such as opening a new window, while others perform no additional operations.
Returns the names of the currently mounted volumes.
Important:This command is deprecated; usetell application "System Events" to get the name of every disk.

##### Syntax

##### Result

Alistof text objects, one for each currently mounted volume.
Returns the names of the items in a specified folder.
Important:This command is deprecated; usetell application "System Events" to get the name of every disk item of ....

##### Syntax

##### Parameters

Specifies the folder to list.
Show invisible files and folders?
true

##### Result

Alistoftextobjects, one for each item in the specified folder.
Returns ascriptobject loaded from a specified file.

##### Syntax

##### Parameters

Analiasorfilespecifier that specifies ascriptobject. The file must be a compiled script (with extensionscpt) or script bundle (with extensionscptd).

##### Result

Thescriptobject. You can get this objectâs properties or call its handlers as if it were a localscriptobject.

##### Examples

For examples, seeParameter SpecificationsinAbout Handlers.
Returns the localized text for the specified key.

##### Syntax

##### Parameters

The key for which to obtain the localized text.
The name of the strings file excluding the.stringssuffix.
"Localizable"
Analiasorfilespecifier that specifies the strings file.
The current script bundle for a document-based script (ascptdbundle); otherwise, the current application.

##### Result

Atextobject containing the localized text, or the original key if there is no localized text for that key.

##### Examples

In order forlocalized stringto be useful, you must create localized string data for it to use:

- Save your script as an application bundle or script bundle.
Save your script as an application bundle or script bundle.

- Createlprojfolders in theResourcesdirectory of the bundle for each localization: for example,English.lproj,French.lproj. Create files namedLocalized.stringsin each one. When you are done, the folder structure should look like this:Figure 7-1Bundle structure with localized string data
Createlprojfolders in theResourcesdirectory of the bundle for each localization: for example,English.lproj,French.lproj. Create files namedLocalized.stringsin each one. When you are done, the folder structure should look like this:

- Add key/value pairs to each Localized.strings file. Each pair is a line of text"key" = "value";, for example:Figure 7-2Key/value pair for localized string data
Add key/value pairs to each Localized.strings file. Each pair is a line of text"key" = "value";, for example:
Nowlocalized stringwill return the appropriate values, as defined in your files. For example, when running in French:

```

localized string "hello"  --result: "bonjour"```
In Script Editor, displays a value in the Event Log History window or in the Event Log pane of a script window.

##### Syntax

##### Parameters

The value to display. Expressions are evaluated but object specifiers are not resolved.
The displayed value is enclosed in block comment charactersâfor example,(*window 1*).
If you do not specify a value,logwill display just the comment characters:(**).

##### Result

None.

##### Examples

The following shows a simple use of logging:

```

set area to 7 * 43 as square feet```

```

log area -- result (in Event Log pane): (*square feet 301.0*)```
Log statements can be useful for tracking a scriptâs progress. For an example that shows how to log statements in a repeat loop, seeLogging.
Mounts the specified network volume.

##### Syntax

##### Parameters

The name or URL (for example,afp://server/volume/) of the volume to mount.
The server on which the volume resides; omit if URL path provided in direct parameter.
The AppleTalk zone in which the server resides; omit if URL path provided.
The user name with which to log in to the server; omit for guest access.
The password for the user name; omit for guest access.

##### Result

None.

##### Examples

```

mount volume "afp://myserver.com/" -- guest access```

```

mount volume "http://idisk.mac.com/myname/Public"```

```

mount volume "http://idisk.mac.com/somebody" Â¬```

```

    as user name "myname" with password "mypassword"```

##### Discussion

Themount volumecommand can connect to any file server that is supported by the FinderÂ ÂConnect To...Â command, including Windows (smb), Samba, and FTP servers. On some kinds of servers, theas user nameandwith passwordparameters may not bypass the login dialog, but encoding the name and password in the URL (for example,smb://myname:passwd@server.domain.com/sharename) will mount it silently.
Finds one piece of text inside another.

##### Syntax

##### Parameters

The source text to find the position of.
The target text to search in.

##### Result

Anintegervalue indicating the position, in characters, of the source text in the target, or 0 if not found.

##### Examples

```

set myString to "Yours, mine, and ours"```

```

offset of "yours" in myString  --result: 1, because case is ignored by default```

```

offset of "mine" in myString  --result: 8```

```

offset of "theirs" in myString  --result: 0, because "theirs" doesn't appear```

```

considering case```

```

    offset of "yours" in myString -- result: 0, because case is now considered```

```

end considering```

##### Discussion

offsetcompares text as theequalsoperator does, includingconsideringandignoringconditions. The values returned are counted the same waycharacterelements oftextare countedâfor example,offset of "c" in "Ã©cole"is always2, regardless of whether"Ã©cole"is in Normalization Form C or D. The result of matching part of a character cluster is undefined.
Opens a file for reading and writing.

##### Syntax

##### Parameters

Analiasorfilespecifier that specifies the file to open. You can only use an alias if the file exists.
Should writing to the file be allowed?
false:writeandset eofcommands on this file will fail with an error.

##### Result

A file descriptor, as aninteger. This file descriptor may be used with any of the other file commands:read,write,get eof,set eof, andclose access.

##### Examples

The following example opens a file named "NewFile" in the specified locationpath to desktop, but does not ask for write access:

```

set theFile to (path to desktop as text) & "NewFile"```

```

set referenceNumber to open for access theFile```
To open the file with write access, you would substitute the following line:

```

set referenceNumber to open for access theFile with write permission```

##### Discussion

Opening a file usingopen for accessis not the same as opening a file using Finder. It is âopenâ only in the sense that AppleScript has access to read (and optionally write) its contents; it does not appear in one of the target applicationâs windows, and it does not even have to be one of the target applicationâs files.open for accessand the associated file commands (read,write,get eof,set eof) are typically used with text files. They can also read and write arbitrary binary data, but this is not recommended unless you create the file yourself or have detailed knowledge of the file format.
Callingopen for accesson a file returns an integer, termed afile descriptor, which represents an open communication channel to the fileâs data. This file descriptor remains open until the script callsclose accesson it (or on the same file). Each file descriptor maintains afile pointer, which marks the current position within the file and is initially set to the beginning of the file.readandwritecommands begin reading or writing at the file pointer, unless instructed otherwise using afromorstarting atparameter, and advance the file pointer by the number of bytes read or written, so the next operation will begin where the previous one left off.
A single file may be opened more than once, and therefore have several different file descriptors. Each file descriptor maintains its own file pointer, and each must be closed separately. If you open more than one channel at once with write permission, behavior is unspecified.
It is not strictly necessary to useopen for accessâall the other file commands can accept an alias; if the file is not open, they will open it, do the operation, and then close it. Explicitly opening and closing the file does have two potential advantages, however.
One is performance: if you are performing a number of operations on the same file, opening and closing it repeatedly could become expensive. It is cheaper to explicitly open the file, do the work, and then explicitly close it.
Two is ease of sequential read and write operations: because the file pointer tracks the progress through the file, reading or writing several pieces of data from the same file is a simple matter. Doing the same thing without using the file pointer requires calculating the data size yourself, which is not even possible in some cases.
Opens a URL with the appropriate program.

##### Syntax

##### Parameters

The URL to open.
This parameter exists only for historical reasons; it is no longer supported.

##### Result

None.

##### Examples

This example opens an Apple web page:

```

open location "http://www.apple.com"```
Returns the location of the specified application.

##### Syntax

##### Parameters

The application to locate. See theapplicationclass reference for possible ways to specify an application. You may also use one of the following identifiers:
The application executing the script, such as Script Editor.
The frontmost application.
The script itself. For script applications, this is the same ascurrent application, but for script documents, it is the location of the document.
Note:Some older applications may treatmeidentically tocurrent application.
The application of the current target.
The class of the returned location. If specified, must be one ofaliasortext.
alias

##### Result

The location of the specified application, as either analiasor atextobject containing the path.

##### Examples

```

path to application "TextEdit"```

```

    --result: alias "Leopard:Applications:TextEdit.app:"```

```

path to  --result: alias "Leopard:Applications:AppleScript:Script Editor.app:"```

```

path to me  --result: same as above```

```

path to it  --result: same as above```

```

path to frontmost application  --result: same as above```

```

path to current application```

```

    --result: same, but could be different for a script application```
Returns the location of the specified special folder.

##### Syntax

##### Parameters

The special folder for which to return the path. You may specify one of the following folders:

```

application support```

```

applications folder```

```

desktop```

```

desktop pictures folder```

```

documents folder```

```

downloads folder```

```

favorites folder```

```

Folder Action scripts```

```

fonts```

```

help```

```

home folder```

```

internet plugins```

```

keychain folder```

```

library folder```

```

modem scripts```

```

movies folder```

```

music folder```

```

pictures folder```

```

preferences```

```

printer descriptions```

```

public folder```

```

scripting additions```

```

scripts folder```

```

services folder```

```

shared documents```

```

shared libraries```

```

sites folder```

```

startup disk```

```

startup items```

```

system folder```

```

system preferences```

```

temporary items```

```

trash```

```

users folder```

```

utilities folder```

```

workflows folder```
The following folders are also defined, but are only meaningful when used withfrom Classic domain:

```

apple menu```

```

control panels```

```

control strip modules```

```

extensions```

```

launcher items folder```

```

printer drivers```

```

printmonitor```

```

shutdown folder```

```

speakable items```

```

stationery```

```

voices```
The domain in which to look for the specified folder. You may specify one of the following domains:
A folder in/System.
A folder in/Library.
A folder in/Network.
A folder in~, the userâs home folder.
A folder in the Classic Mac OS system folder. Only meaningful on systems that support Classic.
The default domain for the specified folder. This varies depending on the folder.
The class of the returned location.
alias
Create the folder if it doesnât exist? Your script may not have permission to create the folder (for example, asking to create something in the system domain), so your script should be prepared for that error.
true

##### Result

The location of the specified folder, as either analiasor atextobject containing the path.

##### Examples

```

path to desktop --result: alias "Leopard:Users:johndoe:Desktop:"```

```

path to desktop as string --result: "Leopard:Users:johndoe:Desktop:"```
Returns the location of the specified resource.

##### Syntax

##### Parameters

The name of the requested resource.
Analiasorfilespecifier that specifies the bundle containing the resource.
The current script bundle for a document-based script (ascptdbundle); otherwise, the current application.
The name of a subdirectory in the bundleâsResourcesdirectory.

##### Result

The location of the specified resource, as analias.

##### Examples

The following example shows how you can get the path to a.icnsfileâin this case, in the Finder application.

```

tell application "Finder"```

```

set gearIconPath to path to resource "Gear.icns"```

```

end```

```

--result: alias "HD:System:Library:CoreServices:Finder.app:Contents:Resources:Gear.icns"```
Returns a random number.

##### Syntax

##### Parameters

The lowest number to return. Can be negative.
The highest number to return. Can be negative.
An initial seed for the random number generator. Once called with any particular seed value,random numberwill always generate the same sequence of numbers. This can be useful when testing randomized algorithms: you can force it to behave the same way every time.

##### Result

A number between thefromandtolimits, including the limit values. Depending on the limit values, the result may be an integer or a real. If at least one limit is specified, and all specified limits are integers, the result is an integer. Otherwise, the result is a real, and may have a fractional part.

##### Examples

```

random number  --result: 0.639215561057```

```

random number from 1 to 10  --result: 8```

##### Discussion

Random numbers are, by definition, random, which means that you may get the same number twice (or even more) in a row, especially if the range of possible numbers is small.
The numbers generated are only pseudo-random, and are not considered cryptographically secure.
If you need to select one of a set of objects in a relationship, usesomeobjectrather thanobject(random number from 1 to countobjects). See theArbitraryreference form for more details.
Reads data from a file.

##### Syntax

##### Parameters

The file to read from, as an alias, a file specifier, or anintegerfile descriptor. A file descriptor must be obtained as the result of an earlieropen for accesscall.
The byte position in the file to start reading from. The position is 1-based, so1is the first byte of the file,2the second, and so on. Negative integers count from the end of the file, so-1is the last byte,-2the second-to-last, and so on.
The current file pointer (seeopen for access) if the file is open, or the beginning of the file if not.
The number of bytes to read.
Read until the end of the file.
Stop reading at this byte position in the file; useeofto indicate the last byte. The position is 1-based, like thefromparameter.
A single character; read up to the next occurrence of that character. Thebeforecharacter is also read, but is not part of the result, so the nextreadwill start just after it.
A single character; read up to and including the next occurrence of that character.
A delimiter, such as a tab or return character, used to separate the data read into a list of text objects. The resulting items consist of the text between occurrences of the delimiter text. The delimiter is considered a separator, so a leading or trailing delimiter will produce an empty string on the other side. For example, the result of reading"axbxcx"using a delimiter of"x"would be{"a", "b", "c", ""}.
None;readreturns a single item.
Asusing delimiterabove, but all of the strings in the list count as delimiters.
Interpret the raw bytes read as this class. The most common ones control the use of three different text encodings:
The primary text encoding, as determined by the userâs language preferences set in the International preference panel. (For example, Mac OS Roman for English, MacJapanese for Japanese, and so on.)
UTF-16.
UTF-8. (SeeDouble Angle Bracketsfor information on chevron or ârawâ syntax.)
Any other class is possible, for exampledateorlist, but is typically only useful if the data was written using awritestatement specifying the same value for theasparameter.
text

##### Result

The data read from the file. If the file is open, the file pointer is advanced by the number of bytes read, so the nextreadcommand will start where the previous one left off.

##### Examples

The following example opens a file for read access, reads up to (and including) the first occurrence of".", closes the file, and displays the text it read. (See the Examples section for thewritecommand for how to create a similar file for reading.)

```

set fp to open for access file "Leopard:Users:myUser:NewFile"```

```

set myText to read fp until "."```

```

close access fp```

```

display dialog myText```
To read all the text in the file, replaceset myText to read fp until "."withset myText to read fp.

##### Discussion

At most one ofto,for,before, anduntilis allowed. Use ofbefore,until, orusing delimiter(s)will interpret the file first as text and then coerce the text to whatever is specified in theasparameter. Otherwise, it is treated as binary data (which may be interpreted as text if so specified.)
readcannot automatically detect the encoding used for a text file. If a file is not in the primary encoding, you must supply an appropriateasparameter.
When reading binary data,readalways uses big-endian byte order. This is only a concern if you are reading binary files produced by other applications.
Rounds a number to an integer.

##### Syntax

##### Parameters

The number to round.
The direction to round. You may specify one of the following rounding directions:
Rounds to the next largest integer. This is the same as the math âceilingâ function.
Rounds down to the next smallest integer. This is the same as the math âfloorâ function.
Rounds toward zero, discarding any fractional part. Also known as truncation.
Rounds to the nearest integer; .5 cases are rounded to the nearest even integer. For example, 1.5 rounds to 2, 0.5 rounds to 0. Also known as âunbiased roundingâ or âbankersâ rounding.â See Discussion for details.
Rounds to the nearest integer; .5 cases are rounded away from zero. This matches the rules commonly taught in elementary mathematics classes.
to nearest

##### Result

The rounded value, as anintegerif it is within the allowable range (Â±229), or as arealif not.

##### Examples

Rounding up or down is not the same as rounding away from or toward zero, though it may appear so for positive numbers. For example:

```

round 1.1 rounding down --result: 1```

```

round -1.1 rounding down --result: -2```
To round to the nearest multiple of something other than 1, divide by that number first, round, and then multiply. For example, to round a number to the nearest 0.01:

```

set x to 5.1234```

```

set quantum to 0.01```

```

(round x/quantum) * quantum --result: 5.12```

##### Discussion

The definition ofto nearestis more accurate thanas taught in school, but may be surprising if you have not seen it before. For example:

```

round 1.5 --result: 2```

```

round 0.5 --result: 0```
Rounding 1.5 to 2 should come as no surprise, butas taught in schoolwould have rounded 0.5 up to 1. The problem is that when dealing with large data sets or with many subsequent rounding operations, always rounding up introduces a slight upward skew in the results. The round-to-even rule used byto nearesttends to reduce the total rounding error, because on average an equal portion of numbers will round down as will round up.
Executes therunhandler of the specified target.
To run an application, it must be on a local or mounted volume. If the application is already running, the effect of theruncommand depends on the application. Some applications are not affected; others repeat their startup procedures each time they receive aruncommand.
Theruncommand launches an application as hidden; useactivateto bring the application to the front.
For ascriptobject, theruncommand causes either the explicit or the implicitrunhandler, if any, to be executed. For related information, seerun Handlers.

##### Syntax

##### Parameters

Ascriptorapplicationobject.
it(the current target)

##### Result

The result, if any, returned by the specified objectâsrunhandler.

##### Examples

```

run application "TextEdit"```

```

tell application "TextEdit" to run```

```

run myScript --where myScript is a script object```
For information about using theruncommand withscriptobjects, seeSending Commands to Script Objects.

##### Discussion

To specify an application to run, you can supply a string with only the application name, as shown in the Examples section. Or you can specify a location more precisely, using one of the forms described inAliases and Files. For examples of other ways to specify an application, see theapplicationclass.
It is not necessary to explicitly tell an application torunbefore sending it other commands; AppleScript will do that automatically. To launch an application without invoking its usual startup behavior, use thelaunchcommand. For further details, seeCalling a Script Application From a Script.
Runs a specified script or script file.
See alsostore script.

##### Syntax

##### Parameters

The script text, or analiasorfilespecifier that specifies the script file to run.
A list of parameter values to be passed to the script.
The scripting component to use.
"AppleScript"

##### Result

The result of the scriptâsrunhandler.

##### Examples

The following script targets the application Finder, escaping the double quotes around the application name with the backslash character (for more information on using the backslash, see the Special String Characters section in thetextclass description):

```

run script "get name of front window of app \"Finder\"" --result: a window name```
This example executes a script stored on disk:

```

set scriptAlias to "Leopard:Users:myUser:Documents:savedScript.scptd:" as alias```

```

run script scriptAlias --result: script is executed```
Speaks the specified text.

##### Syntax

##### Parameters

The text to speak.
The text to display in the feedback window, if different from the spoken text. This parameter is ignored unless Speech Recognition is turned on (in System Preferences).
The voice to speak withâfor example:"Zarvox".
You can use any of the voices from the System Voice pop-up on the Text to Speech tab in the Speech preferences pane.
The current System Voice (set in the Speech panel in System Preferences.
Should the command wait for speech to complete before returning? This parameter is ignored unless Speech Recognition is turned on (in System Preferences).
true
Analiasorfilespecifier to anAIFFfile (existing or not) to contain the sound output. You can only use analiasspecifier if the file exists. If this parameter is specified, the sound is not played audibly, only saved to the file.
None; the text is spoken out loud, and no file is saved.

##### Result

None.

##### Examples

```

say "You are not listening to me!" using "Bubbles" -- result: spoken in Bubbles```
The following example saves the spoken text into a sound file:

```

set soundFile to choose file name -- specify name ending in ".aiff"```

```

    --result: a file URL```

```

say "I love oatmeal." using "Victoria" saving to soundFile```

```

    --result: saved to specified sound file```
Returns a list of the names of all currently available scripting components, such as the AppleScript component.

##### Syntax

##### Result

Alistoftextitems, one for each installed scripting component.

##### Examples

```

scripting components --result: {"AppleScript"}```

##### Discussion

A scripting component is a software component, such as AppleScript, that conforms to the Open Scripting Architecture (OSA) interface. The OSA provides an abstract interface for applications to compile, execute, and manipulate scripts without needing to know the details of the particular scripting language. Each scripting language corresponds to a single scripting component.
Assigns one or more values to one or more variables.

##### Syntax

##### Parameters

The name of the variable or pattern of variables in which to store the value or pattern of values. Patterns can be lists or records.
The expression whose value is to be set. It can evaluate to any type of object or value.

##### Result

The value assigned.

##### Examples

setmay be used to create new variables:

```

set myWeight to 125```
...assign new values to existing variables:

```

set myWeight to myWeight + 23```
...change properties or elements of objects, such as lists:

```

set intList to {1, 2, 3}```

```

set item 3 of intList to 42```
...or application-defined objects:

```

tell application "Finder" to set name of startup disk to "Happy Fun Ball"```
As mentioned in the Discussion, setting one variable to another makes both variables refer to the exact same object. If the object is mutable, that is, it has writable properties or elements, changes to the object will appear in both variables:

```

set alpha to {1, 2, {"a", "b"}}```

```

set beta to alpha```

```

set item 2 of item 3 of alpha to "change" --change the original variable```

```

set item 1 of beta to 42 --change a different item in the new variable```

```

{alpha, beta}```

```

--result: {{42, 2, {"a", "change"}}, {42, 2, {"a", "change"}}}```
Both variables show the same changes, because they both refer to the same object. Compare this with the similar example incopy. Assigning a new object to a variable is not the same thing as changing the object itself, and does not affect any other variables that refer to the same object. For example:

```

set alpha to {1, 2, 3}```

```

set beta to alpha --result: beta refers to the same object as alpha```

```

set alpha to {4, 5, 6}```

```

    --result: assigns a new object to alpha; this does not affect beta.```

```

{alpha, beta}```

```

--result: {{4, 5, 6}, {1, 2, 3}}```
setcan assign several variables at once using a pattern, which may be a list or a record. For example:

```

tell application "Finder" to set {x, y} to position of front window```
Sinceposition of front windowevaluates to a list of two integers, this setsxto the first item in the list andyto the second item.
You can think of pattern assignment as shorthand for a series of simple assignments, but that is not quite accurate, because the assignments are effectively simultaneous. That means that you can use pattern assignment to exchange two variables:

```

set {x, y} to {1, 2} --now x is 1, and y is 2.```

```

set {x, y} to {y, x} --now x is 2, and y is 1.```
To accomplish the second statement using only simple assignments, you would need a temporary third variable.
For more information on using the set command, including a more complex pattern example, seeDeclaring Variables with the set Command.

##### Discussion

Using thesetcommand to assign a value to a variable causes the variable to refer to the original value. In a sense, it creates a new name for the same object. If multiple variables refer to a mutable object (that is, one with writable properties or elements, such as a list orscriptobject), changes to the object are observable through any of the variables. If you want a separate copy, use thecopycommand. This sharing only applies to values in AppleScript itself; it does not apply to values in other applications. Changing the object a variable refers to is not the same as altering the object itself, and does not affect other variables that refer to the same object.
Sets the length of a file, in bytes.

##### Syntax

##### Parameters

The file to set the length of, as an alias, a file specifier, or as an integer file descriptor, which must be obtained as the result of an earlieropen for accesscall.
The new length of the file, in bytes. If the new length is shorter than the existing length of the file, any data beyond that position is lost. If the new length is longer, the contents of the new bytes are unspecified.

##### Result

None.
Signals a âwrite permissionâ error if the file was opened usingopen for accesswithout write permission.

##### Examples

If you want to completely replace the contents of an existing file, the first step must be to change its length to zero:

```

set theFile to choose file with prompt "Choose a file to clobber:"```

```

set eof theFile to 0```
Places data on the clipboard.

##### Syntax

##### Parameters

The data (of any type) to place on the clipboard.

##### Result

None.

##### Examples

The following script places text on the clipboard, then retrieves the text in TextEdit with athe clipboardcommand:

```

set the clipboard to "Important new text."```

```

tell application "TextEdit"```

```

    activate  --make sure TextEdit is running```

```

    set clipText to the clipboard  --result: "Important new text."```

```

    --perform operations with retrieved text```

```

end tell```

##### Discussion

It is not necessary to use the clipboard to move data between scriptable applications. You can simplygetthe data from the first application into a variable andsetthe appropriate data in the second application.
Sets the sound output, input, and alert volumes.

##### Syntax

##### Parameters

The sound output volume, a real number from 0 to 7.
Important:This parameter is deprecated; if specified, all other parameters will be ignored.
The sound output volume, an integer from 0 to 100.
None; the output volume is not changed.
The sound input volume, an integer from 0 to 100.
None; the input volume is not changed.
The alert input volume, an integer from 0 to 100.
None; the alert volume is not changed.
Should the sound output be muted?
None; the output muting is not changed.

##### Result

None.

##### Examples

The following example saves the current volume settings, before increasing the output volume, saying some text, and restoring the original value:

```

set savedSettings to get volume settings```

```

-- {output volume:32, input volume:70, alert volume:78, output muted:false}```

```

set volume output volume 90```

```

say "This is pretty loud."```

```

set volume output volume (output volume of savedSettings)```

```

delay 1```

```

say "That's better."```
Stores ascriptobject into a file.
See alsorun script.

##### Syntax

##### Parameters

Thescriptobject to store.
Analiasorfilespecifier that specifies the file to store thescriptobject in.
None; a standard Save As dialog will be presented to allow the user to choose where to save thescriptobject.
Allow overwriting an existing file? You may specify one of the following constants:
Overwrite without asking.
Never overwrite; signal an error if the file exists.
Present a dialog asking the user what to do; the options are Replace (overwrite the file), Cancel (signal a âuser canceledâ error), or Save As (save to a different location).

##### Result

None.

##### Examples

This example stores a script on disk, using the Save As dialog to specify a location on the desktop and the namestoredScript. It then creates an alias to the stored script and runs it withrun script:

```

script test```

```

    display dialog "Test"```

```

end script```

```

 ```

```

store script test --specify "Leopard:Users:myUser:Desktop:storedScript"```

```

 ```

```

set localScript to alias "Leopard:Users:myUser:Desktop:storedScript" run script localScript --result: displays dialog "Test"```
Thestore scriptcommand stores only the contents of the scriptâin this case, the one statement,display dialog "Test". It does not store the beginning and ending statements of the script definition.
Summarizes the specified text or text file.

##### Syntax

##### Parameters

Thetext, or analiasto a text file, to summarize.
The number of sentences desired in the summary.

##### Result

Atextobject containing a summarized version of the text or file.

##### Examples

This example summarizes Lincolnâs famous Gettysburg Address down to one sentenceâa tough job even for AppleScript:

```

set niceSpeech to "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.```

```

Now we are engaged in a great civil war, testing whether that nation, or any nation, so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.```

```

But, in a larger sense, we can not dedicateâwe can not consecrateâwe can not hallowâthis ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before usâthat from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotionâthat we here highly resolve that these dead shall not have died in vainâthat this nation, under God, shall have a new birth of freedomâand that government of the people, by the people, for the people, shall not perish from the earth."```

```

set greatSummary to summarize niceSpeech in 1```

```

display dialog greatSummary --result: displays one inspiring sentence```
Get environment variables or attributes of this computer.

##### Syntax

##### Parameters

The attribute to test: either a Gestalt value or a shell environment variable name. Gestalt values are described inGestalt Manager Reference.
If the attribute is omitted,system attributewill return a list of the names of all currently defined environment variables.
For Gestalt values, an integer mask that is bitwise-ANDed with the Gestalt response. If the result is non-zero,system attributereturnstrue, otherwisefalse.
For environment variables, this parameter is ignored.
None;system attributereturns the original Gestalt response code.

##### Result

If the attribute specified is a Gestalt selector, either the Gestalt response code ortrueorfalsedepending on thehasparameter.
If the attribute specified is an environment variable, the value of that variable, or an empty string ("") if it is not defined.
If no attribute is supplied, a list of all defined environment variables.

##### Examples

To get the current shell:

```

system attribute "SHELL" --result: "/bin/bash" (for example)```
To get a list of all defined environment variables:

```

system attribute```

```

(* result: (for example)```

```

{"PATH", "TMPDIR", "SHELL", "HOME", "USER", "LOGNAME", "DISPLAY", "SSH_AUTH_SOCK", "Apple_PubSub_Socket_Render", "__CF_USER_TEXT_ENCODING", "SECURITYSESSIONID", "COMMAND_MODE"}```

```

*)```
Gets information about the system.

##### Syntax

##### Result

A record containing various information about the system and the current user. This record contains the following fields:
The version number of AppleScript, for example,"2.0". This can be useful for testing for the existence of AppleScript features. When comparing version numbers, useconsidering numeric stringsto make them compare in numeric order, since standard lexicographic ordering would consider"1.9"to come after"1.10".
The version number of AppleScript Studio, for example,"1.5".
Note:AppleScript Studio is deprecated in OS X v10.6.
The version number of OS X, for example,"10.5.1".
The current userâs short name, for example,"hoser". This is set in the Advanced Options panel in the Accounts preference pane, or in the âShort Nameâ field when creating the account. This is also available from System Events usingname of current user.
The current userâs long name, for example,"Random J. Hoser". This is the âUser Nameâ field in the Accounts preference pane, or in the âNameâ field when creating the account. This is also available from System Events usingfull name of current user.
The current userâs user ID. This is set in the Advanced Options panel in the Accounts preference pane.
The current userâs locale code, for example"en_US".
The location of the current userâs home folder. This is also available from Finderâshomeproperty, or System Eventsâhome folderproperty.
The name of the boot volume, for example,"Macintosh HD". This is also available from Finder or System Events usingname of startup disk.
The computerâs name, for example"mymac". This is the âComputer Nameâ field in the Sharing preference pane.
The computerâs DNS name, for example"mymac.local".
The computerâs IPv4 address, for example"192.201.168.13".
The MAC address of the primary Ethernet interface, for example"00:1c:63:91:4e:db".
The CPU type, for example"Intel 80486".
The clock speed of the CPU in MHz, for example2400.
The amount of physical RAM installed in the computer, in megabytes (MB), for example2048.

##### Examples

```

system info --result: long record of information```
Returns the contents of the clipboard.

##### Syntax

##### Parameters

The type of data desired.the clipboardwill attempt to find that âflavorâ of data on the clipboard; if it is not found, it will attempt to coerce whatever flavor is there.

##### Result

The data from the clipboard, which can be of any type.

##### Examples

The following script places text on the clipboard, and then appends the clipboard contents to the frontmost TextEdit document:

```

 ```

```

set the clipboard to "Add this sentence at the end."```

```

tell application "TextEdit"```

```

    activate  --make sure TextEdit is running```

```

    make new paragraph at end of document 1 with data (return & the clipboard)```

```

end tell```

##### Discussion

It is not necessary to use the clipboard to move data between scriptable applications. You can simplygetthe data from the first application into a variable andsetthe appropriate data in the second application.
Returns the difference between local time and GMT (Greenwich Mean Time) or Universal Time, in seconds.

##### Syntax

##### Result

Theintegernumber of seconds difference between the current time zone and Universal Time.

##### Examples

The following example computes the time difference between the current location and Cupertino:

```

set localOffset to time to GMT  --local difference, in seconds```

```

set cupertinoOffset to -8.0 * hours```

```

    --doesn't account for Daylight Savings; may actually be -7.0.```

```

set difference to (localOffset - cupertinoOffset) / hours```

```

display dialog ("Hours to Cupertino: " & difference)```
Writes data to a specified file.

##### Syntax

##### Parameters

The data to write to the file. This is typicallytext, but may be of any type. When reading the data back, thereadcommand must specify the same type, or the results are undefined.
The file to write to, as an alias, a file specifier, or anintegerfile descriptor. A file descriptor must be obtained as the result of an earlieropen for accesscall.
The byte position in the file to start reading from. The position is 1-based, so1is the first byte of the file,2the second, and so on. Negative integers count from the end of the file, so-1is the last byte,-2the second-to-last, and so on. The constanteofis the position just after the last byte; use this to append data to the file.
The current file pointer (seeopen for access) if the file is open, or the beginning of the file if not.
The number of bytes to write.
Write all the data provided.
Write the data as this class. The most common ones control the use of three different text encodings:
The primary text encoding, as determined by the userâs language preferences set in the International preference panel. (For example, Mac OS Roman for English, MacJapanese for Japanese, and so on.)
UTF-16.
UTF-8.
Any other class is possible, for exampledateorlist, but is typically only useful if the data will be read using areadstatement specifying the same value for theasparameter.
The class of the supplied data. See Special Considerations.

##### Result

None. If the file is open,writewill advance the file pointer by the number of bytes written, so the nextwritecommand will start writing where the last one ended.
Signals an error if the file is open without write permission, or if there is any other problem that prevents writing to the file, such as a lack of disk space.

##### Examples

The following example opens a file with write permission, creating it if it doesnât already exist, writes text to it, and closes it.

```

set fp to open for access file "HD:Users:myUser:NewFile" with write permission```

```

write "Some text. And some more text." to fp```

```

close access fp```

##### Special Considerations

As specified above,writewith noasparameter writes as the class of the supplied data, which means that in AppleScript 2.0writealways writestextdata using the primary encoding. Prior to 2.0,stringandUnicode textwere distinct types, which meant that it would use primary encoding forstringand UTF-16 forUnicode text. For reliable results when creating scripts that will run on both 2.0 and pre-2.0, always specify the encoding explicitly usingas textoras Unicode text, as appropriate.
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25