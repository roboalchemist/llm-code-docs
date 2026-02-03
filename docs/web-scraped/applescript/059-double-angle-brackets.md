# Double Angle Brackets

When you type English language script statements in a Script Editor script window, AppleScript is able to compile the script because the English terms are described either in the terminology built into the AppleScript language or in the dictionary of an available scriptable application or scripting addition. When AppleScript compiles your script, it converts it into an internal executable format, then reformats the text to conform to settings in Script Editorâs Formatting preferences.
When you open, compile, edit, or run scripts with Script Editor, you may occasionally see terms enclosed in double angle brackets, or chevrons(Â«Â»). For example, you might see the termÂ«event sysodlogÂ»as part of a scriptâthis is the event code representation for adisplay dialogcommand. The event code representation is also known asraw format.
For compatibility with Asian national encodings, âãâ and âãâ are allowed as synonyms for âÂ«â and âÂ»â ( (Option- \ and Option-Shift- \, respectively, on a U.S. keyboard), since the latter do not exist in some Asian encodings.
The following sections provide more information about when chevrons appear in scripts.

## When a Dictionary Is Not Available

AppleScript uses double angle brackets in a Script Editor script window when it canât identify a term. That happens when it encounters a term that isnât part of the AppleScript language and isnât defined in an application or scripting addition dictionary that is available when the script is opened or compiled.
For example, if a script is compiled on one machine and later opened on another, the dictionary may not be available, or may be from an older version of the application or scripting addition that does not support the term.
This can also happen if the fileStandardAdditions.osaxis not present in/System/ScriptingAdditions. Then, scripting addition commands such asdisplay dialogwill not be present and will be replaced with chevron notation (Â«event sysodlogÂ») when you compile or run the script.

## When AppleScript Displays Data in Raw Format

Double angle brackets can also occur in results. For example, if the value of a variable is ascriptobject namedJoe, AppleScript represents thescriptobject as shown in this script:

```

script Joe```

```

    property theCount : 0```

```

end script```

```

 ```

```

set scriptObjectJoe to Joe```

```

scriptObjectJoe```

```

--result: Â«script JoeÂ»```
Similarly, if Script Editor canât display a variableâs data directly in its native format, it uses double angle brackets to enclose both the worddataand a sequence of numerical values that represent the data. Although this may not visually resemble the original data, the dataâs original format is preserved.
This may occur because an application command returns a value that does not belong to any of the normal AppleScript classes. You can store such data in variables and send them as parameters to other commands, but Script Editor cannot display the data in its native format.

## Entering Script Information in Raw Format

You can enter double angle brackets, or chevrons (Â«Â»), directly into a script by typing Option-Backslash and Shift-Option-Backslash. You might want to do this if youâre working on a script that needs to use terminology that isnât available on your current machineâfor example, if youâre working at home and donât have the latest dictionary for a scriptable application you are developing, but you know the codes for a supported term.
You can also use AppleScript to display the underlying codes for a script, using the following steps:

- Create a script using standard terms compiled against an available application or scripting addition.
Create a script using standard terms compiled against an available application or scripting addition.

- Save the script as text and quit Script Editor.
Save the script as text and quit Script Editor.

- Remove the application or scripting addition from the computer.
Remove the application or scripting addition from the computer.

- Open the script again and compile it.
Open the script again and compile it.

- When AppleScript asks you to locate the application or scripting addition, cancel the dialog.
When AppleScript asks you to locate the application or scripting addition, cancel the dialog.
Script Editor can compile the script, but displays chevron format for any terms that rely on a missing dictionary.

## Sending Raw Apple Events From a Script

The termÂ«event sysodlogÂ»is actually the raw form for an Apple event with event class'syso'and event ID'dlog'(thedisplay dialogcommand). For a list of many of the four-character codes and their related terminology used by Apple, seeAppleScript Terminology and Apple Event Codes Reference.
You can use raw syntax to enter and execute events (even complex events with numerous parameters) when there is no dictionary to support them. However, providing detailed documentation for how to do so is beyond the scope of this guide.
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25