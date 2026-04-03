# C# basics

# C# basics

## Introduction
This page provides a brief introduction to C#, both what it is and
how to use it in Godot. Afterwards, you may want to look athow to use specific features, read about thedifferences between the C# and the GDScript API,
and (re)visit theScripting sectionof the
step-by-step tutorial.
C# is a high-level programming language developed by Microsoft. In Godot,
it is implemented with the modern .NET runtime.
Attention
Projects written in C# using Godot 4 currently cannot be exported to the web
platform. To use C# on the web platform, consider Godot 3 instead.
Android and iOS platform support is available as of Godot 4.2, but is
experimental andsome limitations apply.
Note
This isnota full-scale tutorial on the C# language as a whole.
If you aren't already familiar with its syntax or features, see theMicrosoft C# guideor look for a suitable introduction elsewhere.

## Prerequisites
Godot bundles the parts of .NET needed to run already-compiled games.
However, Godot does not bundle the tools required to build and compile
games, such as MSBuild and the C# compiler. These are
included in the .NET SDK, and need to be installed separately.
In summary, you must have installed the .NET SDKandthe .NET-enabled
version of Godot.
Download and install the latest stable version of the SDK from the.NET download page.
Godot 4.5 requires .NET 8 or later, but exporting to Android requires .NET 9 or later.
Important
Be sure to install the 64-bit version of the SDK(s)
if you are using the 64-bit version of Godot.
If you are building Godot from source, make sure to follow the steps to enable
.NET support in your build as outlined in theCompiling with .NETpage.

## Configuring an external editor
C# support in Godot's built-in script editor is minimal. Consider using an
external IDE or editor, such asVisual Studio CodeorVisual Studio. These provide autocompletion, debugging, and other
useful features for C#. To select an external editor in Godot,
click onEditor → Editor Settingsand scroll down toDotnet. UnderDotnet, click onEditor, and select your
external editor of choice. Godot currently supports the following
external editors:
- Visual Studio 2022
Visual Studio 2022
- Visual Studio Code
Visual Studio Code
- MonoDevelop
MonoDevelop
- Visual Studio for Mac
Visual Studio for Mac
- JetBrains Rider
JetBrains Rider
See the following sections for how to configure an external editor:

### JetBrains Rider
After reading the "Prerequisites" section, you can download and installJetBrains Rider.
In Godot'sEditor → Editor Settingsmenu:
- SetDotnet->Editor->External EditortoJetBrains Rider.
SetDotnet->Editor->External EditortoJetBrains Rider.
In Rider:
- SetMSBuild versionto.NET Core.
SetMSBuild versionto.NET Core.
- If you are using a Rider version below 2024.2, install theGodot supportplugin. This functionality is now built into Rider.
If you are using a Rider version below 2024.2, install theGodot supportplugin. This functionality is now built into Rider.

### Visual Studio Code
After reading the "Prerequisites" section, you can download and installVisual Studio Code(aka VS Code).
In Godot'sEditor → Editor Settingsmenu:
- SetDotnet->Editor->External EditortoVisual Studio Code.
SetDotnet->Editor->External EditortoVisual Studio Code.
In Visual Studio Code:
- Install theC#extension.
Install theC#extension.
To configure a project for debugging, you need atasks.jsonandlaunch.jsonfile in
the.vscodefolder with the necessary configuration.
Here is an examplelaunch.json:
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Play",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            "program": "${env:GODOT4}",
            "args": [],
            "cwd": "${workspaceFolder}",
            "stopAtEntry": false,
        }
    ]
}
```
For this launch configuration to work, you need to either setup a GODOT4
environment variable that points to the Godot executable, or replaceprogramparameter with the path to the Godot executable.
Here is an exampletasks.json:
```
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "build",
            "command": "dotnet",
            "type": "process",
            "args": [
                "build"
            ],
            "problemMatcher": "$msCompile"
        }
    ]
}
```
Now, when you start the debugger in Visual Studio Code, your Godot project will run.

### Visual Studio (Windows only)
Download and install the latest version ofVisual Studio.
Visual Studio will include the required SDKs if you have the correct
workloads selected, so you don't need to manually install the things
listed in the "Prerequisites" section.
While installing Visual Studio, select this workload:
- .NET desktop development
.NET desktop development
In Godot'sEditor → Editor Settingsmenu:
- SetDotnet->Editor->External EditortoVisual Studio.
SetDotnet->Editor->External EditortoVisual Studio.
Note
If you see an error like "Unable to find package Godot.NET.Sdk",
your NuGet configuration may be incorrect and need to be fixed.
A simple way to fix the NuGet configuration file is to regenerate it.
In a file explorer window, go to%AppData%\NuGet. Rename or delete
theNuGet.Configfile. When you build your Godot project again,
the file will be automatically created with default values.
To debug your C# scripts using Visual Studio, open the .sln file that is generated
after opening the first C# script in the editor. In theDebugmenu, go to theDebug Propertiesmenu item for your project. Click theCreate a new profilebutton and chooseExecutable. In theExecutablefield, browse to the path
of the C# version of the Godot editor, or type%GODOT4%if you have created an
environment variable for the Godot executable path. It must be the path to the main Godot
executable, not the 'console' version. For theWorking Directory, type a single period,., meaning the current directory. Also check theEnable native code debuggingcheckbox. You may now close this window, click downward arrow on the debug profile
dropdown, and select your new launch profile. Hit the green start button, and your
game will begin playing in debug mode.

## Creating a C# script
After you successfully set up C# for Godot, you should see the following option
when selectingAttach Scriptin the context menu of a node in your scene:
Note that while some specifics change, most concepts work the same
when using C# for scripting. If you're new to Godot, you may want to follow
the tutorials onScripting languagesat this point.
While some documentation pages still lack C# examples, most notions
can be transferred from GDScript.

## Project setup and workflow
When you create the first C# script, Godot initializes the C# project files
for your Godot project. This includes generating a C# solution (.sln)
and a project file (.csproj), as well as some utility files and folders
(.godot/mono).
All of these but.godot/monoare important and should be committed to your
version control system. Everything under.godotcan be safely added to the
ignore list of your VCS.
When troubleshooting, it can sometimes help to delete the.godot/monofolder
and let it regenerate.

## Example
Here's a blank C# script with some comments to demonstrate how it works.
```
using Godot;

public partial class YourCustomClass : Node
{
    // Member variables here, example:
    private int _a = 2;
    private string _b = "textvar";

    public override void _Ready()
    {
        // Called every time the node is added to the scene.
        // Initialization here.
        GD.Print("Hello from C# to Godot :)");
    }

    public override void _Process(double delta)
    {
        // Called every frame. Delta is time since the last frame.
        // Update game logic here.
    }
}
```
As you can see, functions normally in global scope in GDScript like Godot'sprintfunction are available in theGDstatic class which is part of
theGodotnamespace. For a full list of methods in theGDclass, see the
class reference pages for@GDScriptand@GlobalScope.
Note
Keep in mind that the class you wish to attach to your node should have the same
name as the.csfile. Otherwise, you will get the following error:
"Cannot find class XXX for script res://XXX.cs"

## General differences between C# and GDScript
The C# API usesPascalCaseinstead ofsnake_casein GDScript/C++.
Where possible, fields and getters/setters have been converted to properties.
In general, the C# Godot API strives to be as idiomatic as is reasonably possible.
For more information, see theC# API differences to GDScriptpage.
Warning
You need to (re)build the project assemblies whenever you want to see new
exported variables or signals in the editor. This build can be manually
triggered by clicking theBuildbutton in the top right corner of the
editor.
You will also need to rebuild the project assemblies to apply changes in
"tool" scripts.

## Current gotchas and known issues
As C# support is quite new in Godot, there are some growing pains and things
that need to be ironed out. Below is a list of the most important issues
you should be aware of when diving into C# in Godot, but if in doubt, also
take a look over the officialissue tracker for .NET issues.
- Writing editor plugins is possible, but it is currently quite convoluted.
Writing editor plugins is possible, but it is currently quite convoluted.
- State is currently not saved and restored when hot-reloading,
with the exception of exported variables.
State is currently not saved and restored when hot-reloading,
with the exception of exported variables.
- Attached C# scripts should refer to a class that has a class name
that matches the file name.
Attached C# scripts should refer to a class that has a class name
that matches the file name.
- There are some methods such asGet()/Set(),Call()/CallDeferred()and signal connection methodConnect()that rely on Godot'ssnake_caseAPI
naming conventions.
So when using e.g.CallDeferred("AddChild"),AddChildwill not work because
the API is expecting the originalsnake_caseversionadd_child. However, you
can use any custom properties or methods without this limitation.
Prefer using the exposedStringNamein thePropertyName,MethodNameandSignalNameto avoid extraStringNameallocations and worrying about snake_case naming.
There are some methods such asGet()/Set(),Call()/CallDeferred()and signal connection methodConnect()that rely on Godot'ssnake_caseAPI
naming conventions.
So when using e.g.CallDeferred("AddChild"),AddChildwill not work because
the API is expecting the originalsnake_caseversionadd_child. However, you
can use any custom properties or methods without this limitation.
Prefer using the exposedStringNamein thePropertyName,MethodNameandSignalNameto avoid extraStringNameallocations and worrying about snake_case naming.
As of Godot 4.0, exporting .NET projects is supported for desktop platforms
(Linux, Windows and macOS). Other platforms will gain support in future 4.x
releases.

## Common pitfalls
You might encounter the following error when trying to modify some values in Godot
objects, e.g. when trying to change the X coordinate of aNode2D:
```
public partial class MyNode2D : Node2D
{
    public override void _Ready()
    {
        Position.X = 100.0f;
        // CS1612: Cannot modify the return value of 'Node2D.Position' because
        // it is not a variable.
    }
}
```
This is perfectly normal. Structs (in this example, aVector2) in C# are
copied on assignment, meaning that when you retrieve such an object from a
property or an indexer, you get a copy of it, not the object itself. Modifying
said copy without reassigning it afterwards won't achieve anything.
The workaround is simple: retrieve the entire struct, modify the value you want
to modify, and reassign the property.
```
var newPosition = Position;
newPosition.X = 100.0f;
Position = newPosition;
```
Since C# 10, it is also possible to usewith expressionson structs, allowing you to do the same thing in a single line.
```
Position = Position with { X = 100.0f };
```
You can read more about this error on theC# language reference.

## Performance of C# in Godot
See also
For a performance comparison of the languages Godot supports,
seeWhich programming language is fastest?.
Most properties of Godot C# objects that are based onGodotObject(e.g. anyNodelikeControlorNode3DlikeCamera3D) require native (interop) calls as they talk to
Godot's C++ core.
Consider assigning values of such properties into a local variable if you need to modify or read them multiple times at
a single code location:
```
using Godot;

public partial class YourCustomClass : Node3D
{
    private void ExpensiveReposition()
    {
        for (var i = 0; i < 10; i++)
        {
            // Position is read and set 10 times which incurs native interop.
            // Furthermore the object is repositioned 10 times in 3D space which
            // takes additional time.
            Position += new Vector3(i, i);
        }
    }

    private void Reposition()
    {
        // A variable is used to avoid native interop for Position on every loop.
        var newPosition = Position;
        for (var i = 0; i < 10; i++)
        {
            newPosition += new Vector3(i, i);
        }
        // Setting Position only once avoids native interop and repositioning in 3D space.
        Position = newPosition;
    }
}
```
Passing raw arrays (such asbyte[]) orstringto Godot's C# API requires marshalling which is
comparatively pricey.
The implicit conversion fromstringtoNodePathorStringNameincur both the native interop and marshalling
costs as thestringhas to be marshalled and passed to the respective native constructor.

## Using NuGet packages in Godot
NuGetpackages can be installed and used with Godot,
as with any C# project. Many IDEs are able to add packages directly.
They can also be added manually by adding the package reference in
the.csprojfile located in the project root:
```
    <ItemGroup>
        <PackageReference Include="Newtonsoft.Json" Version="11.0.2" />
    </ItemGroup>
    ...
</Project>
```
Godot automatically downloads and sets up newly added NuGet packages
the next time it builds the project.

## Profiling your C# code
The following tools may be used for performance and memory profiling of your managed code:
- JetBrains Rider with dotTrace/dotMemory plugin.
JetBrains Rider with dotTrace/dotMemory plugin.
- Standalone JetBrains dotTrace/dotMemory.
Standalone JetBrains dotTrace/dotMemory.
- Visual Studio.
Visual Studio.
Profiling managed and unmanaged code at once is possible with both JetBrains tools and Visual Studio, but limited to Windows.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.