# C#/.NET

# C#/.NET
C# is a high-level programming language developed by Microsoft. Godot supports
C# as an option for a scripting language, alongside Godot's ownGDScript.
The standard Godot executable does not contain C# support out of the box. Instead,
to enable C# support for your project you need todownload a .NET versionof the editor from the Godot website.

## Godot API for C#
As a general purpose game engine Godot offers some high-level features as a part
of its API. Articles below explain how these features integrate into C# and how
C# API may be different from GDScript.

## C# platform support
See also
SeeSystem requirementsfor hardware and software version
requirements for the Godot engine.
Note
Since C# projects use the .NET runtime, also check the system requirements
for the version of .NET that you'll be using.
Seesupported OS.
Since Godot 4.2, projects written in C# support all desktop platforms (Windows, Linux,
and macOS), as well as Android and iOS.
Android support is currently experimental.
iOS support is currently experimental and has a few limitations.
- The official export templates for the iOS simulator only supports thex64architecture.
The official export templates for the iOS simulator only supports thex64architecture.
- Exporting to iOS can only be done from a MacOS device.
Exporting to iOS can only be done from a MacOS device.
Currently, projects written in C# cannot be exported to the web platform. To use C#
on that platform, consider Godot 3 instead.