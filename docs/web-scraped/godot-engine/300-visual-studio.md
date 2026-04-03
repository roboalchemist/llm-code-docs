# Visual Studio

# Visual Studio
Visual Studio Communityis a Windows-only IDE
byMicrosoftthat's free for individual use or non-commercial use within organizations.
It has many useful features, such as memory view, performance view, source
control and more.
Note
This documentation is for contributions to the game engine, and not using
Visual Studio as a C# editor. To code C# in an external editor, seethe C# guide to configure an external editor.

## Importing the project
Visual Studio requires a solution file to work on a project. While Godot does not come
with the solution file, it can be generated using SCons.
- Navigate to the Godot root folder and open a Command Prompt or PowerShell window.
Navigate to the Godot root folder and open a Command Prompt or PowerShell window.
- Runsconsplatform=windowsvsproj=yesdev_build=yesto generate the solution with debug symbols.Thevsprojparameter signals that you want Visual Studio solution generated.Thedev_buildparameter makes sure the debug symbols are included, allowing to e.g. step through code using breakpoints.
- You can now open the project by double-clicking on thegodot.slnin the project root
or by using theOpen a project or solutionoption inside of the Visual Studio.
You can now open the project by double-clicking on thegodot.slnin the project root
or by using theOpen a project or solutionoption inside of the Visual Studio.
- Use theBuildtop menu to build the project.
Use theBuildtop menu to build the project.
Warning
Visual Studio must be configured with the C++ package. It can be selected
in the installer:

## Debugging the project
Visual Studio features a powerful debugger. This allows the user to examine Godot's
source code, stop at specific points in the code, inspect the current execution context,
and make live changes to the codebase.
You can launch the project with the debugger attached using theDebug > Start Debuggingoption from the top menu. However, unless you want to debug the Project Manager specifically,
you'd need to configure debugging options first. This is due to the fact that when the Godot
Project Manager opens a project, the initial process is terminated and the debugger gets detached.
- To configure the launch options to use with the debugger useProject > Propertiesfrom the top menu:
To configure the launch options to use with the debugger useProject > Propertiesfrom the top menu:
- Open theDebuggingsection and underCommand Argumentsadd two new arguments:
the-eflag opens the editor instead of the Project Manager, and the--pathargument
tells the executable to open the specified project (must be provided as anabsolutepath
to the project root, not theproject.godotfile; if the path contains spaces be sure to pass it inside double quotation marks).
Open theDebuggingsection and underCommand Argumentsadd two new arguments:
the-eflag opens the editor instead of the Project Manager, and the--pathargument
tells the executable to open the specified project (must be provided as anabsolutepath
to the project root, not theproject.godotfile; if the path contains spaces be sure to pass it inside double quotation marks).
To learn more about command line arguments, refer to thecommand line tutorial.
Even if you start the project without a debugger attached it can still be connected to the running
process usingDebug > Attach to Process...menu.
To check that everything is working, put a breakpoint inmain.cppand pressF5to
start debugging.
If you run into any issues, ask for help in one ofGodot's community channels.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.