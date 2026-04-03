# Visual Studio Code

# Visual Studio Code
Note
This documentation is for contributions to the game engine, and not using
Visual Studio Code as a C# or GDScript editor. To code C# or GDScript in an external editor, seethe C# guide to configure an external editororthe GDScript guide to using an external text editor.
Visual Studio Codeis a free cross-platform code editor
byMicrosoft(not to be confused withVisual Studio).

## Importing the project
- Make sure the C/C++ extension is installed. You can find instructions in
theofficial documentation.
Alternatively,clangdcan be used instead.
Make sure the C/C++ extension is installed. You can find instructions in
theofficial documentation.
Alternatively,clangdcan be used instead.
- When using the clangd extension, runsconscompiledb=yes.
When using the clangd extension, runsconscompiledb=yes.
- From the Visual Studio Code's main screen open the Godot root folder withFile > Open Folder....
From the Visual Studio Code's main screen open the Godot root folder withFile > Open Folder....
- PressCtrl+Shift+Pto open the command prompt window and enterConfigure Task.
PressCtrl+Shift+Pto open the command prompt window and enterConfigure Task.
- Select theCreate tasks.json file from templateoption.
Select theCreate tasks.json file from templateoption.
- Then selectOthers.
Then selectOthers.
- If there is no such option asCreate tasks.json file from templateavailable, either delete the file if it already exists in your folder or create a.vscode/tasks.jsonfile manually. SeeTasks in Visual Studio Codefor more details on tasks.
If there is no such option asCreate tasks.json file from templateavailable, either delete the file if it already exists in your folder or create a.vscode/tasks.jsonfile manually. SeeTasks in Visual Studio Codefor more details on tasks.
- Within thetasks.jsonfile find the"tasks"array and add a new section to it:.vscode/tasks.json{"label":"build","group":"build","type":"shell","command":"scons","args":[// enable for debugging with breakpoints"dev_build=yes",],"problemMatcher":"$msCompile"}
Within thetasks.jsonfile find the"tasks"array and add a new section to it:
```
{
  "label": "build",
  "group": "build",
  "type": "shell",
  "command": "scons",
  "args": [
    // enable for debugging with breakpoints
    "dev_build=yes",
  ],
  "problemMatcher": "$msCompile"
}
```
An example of a filled outtasks.json.
Arguments can be different based on your own setup and needs. SeeIntroduction to the buildsystemfor a full list of arguments.

## Debugging the project
To run and debug the project you need to create a new configuration in thelaunch.jsonfile.
- PressCtrl+Shift+Dto open the Run panel.
PressCtrl+Shift+Dto open the Run panel.
- Iflaunch.jsonfile is missing you will be prompted to create a new one.
Iflaunch.jsonfile is missing you will be prompted to create a new one.
- SelectC++ (GDB/LLDB). There may be another platform-specific option here. If selected,
adjust the configuration example provided accordingly.
SelectC++ (GDB/LLDB). There may be another platform-specific option here. If selected,
adjust the configuration example provided accordingly.
- Within thelaunch.jsonfile find the"configurations"array and add a new section to it:
Within thelaunch.jsonfile find the"configurations"array and add a new section to it:
```
{
  "name": "Launch Project",
  "type": "lldb",
  "request": "launch",
  // Change to godot.linuxbsd.editor.dev.x86_64.llvm for llvm-based builds.
  "program": "${workspaceFolder}/bin/godot.linuxbsd.editor.dev.x86_64",
  // Change the arguments below for the project you want to test with.
  // To run the project instead of editing it, remove the "--editor" argument.
  "args": [ "--editor", "--path", "path-to-your-godot-project-folder" ],
  "stopAtEntry": false,
  "cwd": "${workspaceFolder}",
  "environment": [],
  "externalConsole": false,
  "preLaunchTask": "build"
}
```
```
{
  "name": "Launch Project",
  "type": "cppdbg",
  "request": "launch",
  // Change to godot.linuxbsd.editor.dev.x86_64.llvm for llvm-based builds.
  "program": "${workspaceFolder}/bin/godot.linuxbsd.editor.dev.x86_64",
  // Change the arguments below for the project you want to test with.
  // To run the project instead of editing it, remove the "--editor" argument.
  "args": [ "--editor", "--path", "path-to-your-godot-project-folder" ],
  "stopAtEntry": false,
  "cwd": "${workspaceFolder}",
  "environment": [],
  "externalConsole": false,
  "setupCommands":
  [
    {
      "description": "Enable pretty-printing for gdb",
      "text": "-enable-pretty-printing",
      "ignoreFailures": true
    },
    {
        "description": "Load custom pretty-printers for Godot types.",
        "text": "source ${workspaceRoot}/misc/utility/godot_gdb_pretty_print.py"
    }
  ],
  "preLaunchTask": "build"
}
```
```
{
  "name": "Launch Project",
  "type": "cppvsdbg",
  "request": "launch",
  "program": "${workspaceFolder}/bin/godot.windows.editor.dev.x86_64.exe",
  // Change the arguments below for the project you want to test with.
  // To run the project instead of editing it, remove the "--editor" argument.
  "args": [ "--editor", "--path", "path-to-your-godot-project-folder" ],
  "stopAtEntry": false,
  "cwd": "${workspaceFolder}",
  "environment": [],
  "console": "internalConsole",
  "visualizerFile": "${workspaceFolder}/platform/windows/godot.natvis",
  "preLaunchTask": "build"
}
```
```
{
  "name": "Launch Project",
  "type": "lldb",
  "request": "launch",
  "program": "${workspaceFolder}/bin/godot.macos.editor.x86_64",
  // Change the arguments below for the project you want to test with.
  // To run the project instead of editing it, remove the "--editor" argument.
  "args": ["--editor", "--path", "path-to-your-godot-project-folder"],
  "cwd": "${workspaceFolder}",
  "preLaunchTask": "build"
}
```
```
{
  "name": "Launch Project",
  "type": "lldb",
  "request": "launch",
  "program": "${workspaceFolder}/bin/godot.macos.editor.arm64",
  // Change the arguments below for the project you want to test with.
  // To run the project instead of editing it, remove the "--editor" argument.
  "args": ["--editor", "--path", "path-to-your-godot-project-folder"],
  "cwd": "${workspaceFolder}",
  "preLaunchTask": "build"
}
```
An example of a filled outlaunch.json.
Note
Due to sporadic performance issues, it is recommended to use LLDB over GDB on Unix-based systems.
Make sure that theCodeLLDB extensionis installed for configurations usinglldb.
If you encounter issues with lldb, you may consider using gdb (see the LinuxBSD_gdb configuration).
Do note that lldb may work better with LLVM-based builds. SeeCompiling for Linux, *BSDfor further information.
The name underprogramdepends on your build configuration,
e.g.godot.linuxbsd.editor.dev.x86_64for 64-bit LinuxBSD platform withtarget=editoranddev_build=yes.

## Configuring IntelliSense
For the C/C++ extension:
To fix include errors you may be having, you need to configure some settings in thec_cpp_properties.jsonfile.
- First, make sure to build the project since some files need to be generated.
First, make sure to build the project since some files need to be generated.
- Edit the C/C++ Configuration file either with the UI or with text:
Edit the C/C++ Configuration file either with the UI or with text:
- Add an include path for your platform, for example,${workspaceFolder}/platform/windows.
Add an include path for your platform, for example,${workspaceFolder}/platform/windows.
- Add defines for the editorTOOLS_ENABLED, debug buildsDEBUG_ENABLED, and testsTESTS_ENABLED.
Add defines for the editorTOOLS_ENABLED, debug buildsDEBUG_ENABLED, and testsTESTS_ENABLED.
- Make sure the compiler path is configured correctly to the compiler you are using. SeeIntroduction to the buildsystemfor further information on your platform.
Make sure the compiler path is configured correctly to the compiler you are using. SeeIntroduction to the buildsystemfor further information on your platform.
- Thec_cpp_properties.jsonfile should look similar to this for Windows:.vscode/c_cpp_properties.json{"configurations":[{"name":"Win32","includePath":["${workspaceFolder}/**","${workspaceFolder}/platform/windows"],"defines":["_DEBUG","UNICODE","_UNICODE","TOOLS_ENABLED","DEBUG_ENABLED","TESTS_ENABLED"],"windowsSdkVersion":"10.0.22621.0","compilerPath":"C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.39.33519/bin/Hostx64/x64/cl.exe","cStandard":"c17","cppStandard":"c++17","intelliSenseMode":"windows-msvc-x64"}],"version":4}
Thec_cpp_properties.jsonfile should look similar to this for Windows:
```
{
  "configurations": [
    {
      "name": "Win32",
      "includePath": [
        "${workspaceFolder}/**",
        "${workspaceFolder}/platform/windows"
      ],
      "defines": [
        "_DEBUG",
        "UNICODE",
        "_UNICODE",
        "TOOLS_ENABLED",
        "DEBUG_ENABLED",
        "TESTS_ENABLED"
      ],
      "windowsSdkVersion": "10.0.22621.0",
      "compilerPath": "C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.39.33519/bin/Hostx64/x64/cl.exe",
      "cStandard": "c17",
      "cppStandard": "c++17",
      "intelliSenseMode": "windows-msvc-x64"
    }
  ],
  "version": 4
}
```
- Alternatively, you can use the scons argumentcompiledb=yesand set the compile commands settingcompileCommandstocompile_commands.json, found in the advanced section of the C/C++ Configuration UI.This argument can be added to your build task intasks.jsonsince it will need to be run whenever files are added or moved.
Alternatively, you can use the scons argumentcompiledb=yesand set the compile commands settingcompileCommandstocompile_commands.json, found in the advanced section of the C/C++ Configuration UI.
- This argument can be added to your build task intasks.jsonsince it will need to be run whenever files are added or moved.
This argument can be added to your build task intasks.jsonsince it will need to be run whenever files are added or moved.

## Linting class reference XML files
To get linting on class reference XML files, install thevscode-xml extension.

## Displaying documentation on hover
By installing theGodot Hover Docs extension,
you can make class reference documentation appear when hovering symbols in C++
source or header files. The information is sourced from local XML files, so it works offline.
Note
This is only effective for symbols that are documented in the class reference XML,
i.e. those that are exposed to the scripting API. Internal engine symbols will not
show documentation on hover, unless they have a comment right above their declaration.

## Troubleshooting
If you run into any issues, ask for help in one ofGodot's community channels.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.