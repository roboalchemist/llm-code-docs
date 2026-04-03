# Custom platform ports

# Custom platform ports
Similar toCustom modules in C++, Godot's multi-platform architecture
is designed in a way that allows creating platform ports without modifying any
existing source code.
An example of a custom platform port distributed independently from the engine
isFRT, which targets single-board
computers. Note that this platform port currently targets Godot 3.x; therefore,
it does not use theDisplayServerabstraction that is new in Godot 4.
Some reasons to create custom platform ports might be:
- You want to port your game to consoles
(see also theGodot website on console support),
but wish to write the platform layer yourself. This is a long and arduous process, as it
requires signing NDAs with console manufacturers, but it allows you to have
full control over the console porting process.
You want to port your game to consoles
(see also theGodot website on console support),
but wish to write the platform layer yourself. This is a long and arduous process, as it
requires signing NDAs with console manufacturers, but it allows you to have
full control over the console porting process.
- You want to port Godot to an exotic platform that isn't currently supported.
You want to port Godot to an exotic platform that isn't currently supported.
If you have questions about creating a custom platform port, feel free to ask in
the#platformschannel of theGodot Contributors Chat.
Note
Godot is a modern engine with modern requirements. Even if you only
intend to run simple 2D projects on the target platform, it still requires
an amount of memory that makes it unviable to run on most retro consoles.
For reference, in Godot 4, an empty project with nothing visible requires
about 100 MB of RAM to run on Linux (50 MB in headless mode).
If you want to run Godot on heavily memory-constrained platforms, older
Godot versions have lower memory requirements. The porting process is
similar, with the exception ofDisplayServernot being split
from theOSsingleton.

## Official platform ports
The official platform ports can be used as a reference when creating a custom platform port:
- Windows
Windows
- macOS
macOS
- Linux/*BSD
Linux/*BSD
- Android
Android
- iOS
- Web
While platform code is usually self-contained, there are exceptions to this
rule. For instance, audio drivers that are shared across several platforms and
rendering drivers are located in thedrivers/ folderof the Godot source code.

## Creating a custom platform port
Creating a custom platform port is a large undertaking which requires prior
knowledge of the platform's SDKs. Depending on what features you need, the
amount of work needed varies:

### Required features of a platform port
At the very least, a platform port must have methods from theOSsingleton implemented to be buildable and usable for headless operation.
Alogo.svg(32×32) vector image must also be present within the platform
folder. This logo is displayed in the Export dialog for each export preset
targeting the platform in question.
Seethis implementationfor the Linux/*BSD platform as an example. See also theOS singleton headerfor reference.
Note
If your target platform is UNIX-like, consider inheriting from theOS_Unixclass to get much of the work done automatically.
If the platform is not UNIX-like, you might use theWindows portas a reference.
detect.py file
Adetect.pyfile must be created within the platform's folder with all
methods implemented. This file is required for SCons to detect the platform as a
valid option for compiling. See thedetect.py filefor the Linux/*BSD platform as an example.
All methods should be implemented withindetect.pyas follows:
- is_active(): Can be used to temporarily disable building for a platform.
This should generally always returnTrue.
is_active(): Can be used to temporarily disable building for a platform.
This should generally always returnTrue.
- get_name(): Returns the platform's user-visible name as a string.
get_name(): Returns the platform's user-visible name as a string.
- can_build(): ReturnTrueif the host system is able to build for the
target platform,Falseotherwise. Do not put slow checks here, as this is
queried when the list of platforms is requested by the user. Useconfigure()for extensive dependency checks instead.
can_build(): ReturnTrueif the host system is able to build for the
target platform,Falseotherwise. Do not put slow checks here, as this is
queried when the list of platforms is requested by the user. Useconfigure()for extensive dependency checks instead.
- get_opts(): Returns the list of SCons build options that can be defined by
the user for this platform.
get_opts(): Returns the list of SCons build options that can be defined by
the user for this platform.
- get_flags(): Returns the list of overridden SCons flags for this platform.
get_flags(): Returns the list of overridden SCons flags for this platform.
- configure(): Perform build configuration, such as selecting compiler
options depending on SCons options chosen.
configure(): Perform build configuration, such as selecting compiler
options depending on SCons options chosen.

### Optional features of a platform port
In practice, headless operation doesn't suffice if you want to see anything on
screen and handle input devices. You may also want audio output for most
games.
Some links on this list point to the Linux/*BSD platform implementation as a reference.
- One or moreDisplayServers,
with the windowing methods implemented. DisplayServer also covers features such
as mouse support, touchscreen support and tablet driver (for pen input).
See theDisplayServer singleton headerfor reference.For platforms not featuring full windowing support (or if it's not relevant
for the port you are making), most windowing functions can be left mostly
unimplemented. These functions can be made to only check if the window ID isMAIN_WINDOW_IDand specific operations like resizing may be tied to the
platform's screen resolution feature (if relevant). Any attempt to create
or manipulate other window IDs can be rejected.
One or moreDisplayServers,
with the windowing methods implemented. DisplayServer also covers features such
as mouse support, touchscreen support and tablet driver (for pen input).
See theDisplayServer singleton headerfor reference.
- For platforms not featuring full windowing support (or if it's not relevant
for the port you are making), most windowing functions can be left mostly
unimplemented. These functions can be made to only check if the window ID isMAIN_WINDOW_IDand specific operations like resizing may be tied to the
platform's screen resolution feature (if relevant). Any attempt to create
or manipulate other window IDs can be rejected.
For platforms not featuring full windowing support (or if it's not relevant
for the port you are making), most windowing functions can be left mostly
unimplemented. These functions can be made to only check if the window ID isMAIN_WINDOW_IDand specific operations like resizing may be tied to the
platform's screen resolution feature (if relevant). Any attempt to create
or manipulate other window IDs can be rejected.
- If the target platform supports the graphics APIs in question:Rendering
context forVulkan,Direct3D 12OpenGL 3.3 or OpenGL ES 3.0.
If the target platform supports the graphics APIs in question:Rendering
context forVulkan,Direct3D 12OpenGL 3.3 or OpenGL ES 3.0.
- Input handlers forkeyboardandcontroller.
Input handlers forkeyboardandcontroller.
- One or moreaudio drivers.
The audio driver can be located in theplatform/folder (this is done for
the Android and Web platforms), or in thedrivers/folder if multiple
platforms may be using this audio driver. See theAudioServer singleton headerfor reference.
One or moreaudio drivers.
The audio driver can be located in theplatform/folder (this is done for
the Android and Web platforms), or in thedrivers/folder if multiple
platforms may be using this audio driver. See theAudioServer singleton headerfor reference.
- Crash handler,
for printing crash backtraces when the game crashes. This allows for easier
troubleshooting on platforms where logs aren't readily accessible.
Crash handler,
for printing crash backtraces when the game crashes. This allows for easier
troubleshooting on platforms where logs aren't readily accessible.
- Text-to-speech driver(for accessibility).
Text-to-speech driver(for accessibility).
- Export handler(for exporting from the editor, includingOne-click deploy).
Not required if you intend to export only a PCK from the editor, then run the
export template binary directly by renaming it to match the PCK file. See theEditorExportPlatform headerfor reference.run_icon.svg(16×16) should be present within the platform folder ifOne-click deployis implemented for the target platform. This icon
is displayed at the top of the editor when one-click deploy is set up for the
target platform.
Export handler(for exporting from the editor, includingOne-click deploy).
Not required if you intend to export only a PCK from the editor, then run the
export template binary directly by renaming it to match the PCK file. See theEditorExportPlatform headerfor reference.run_icon.svg(16×16) should be present within the platform folder ifOne-click deployis implemented for the target platform. This icon
is displayed at the top of the editor when one-click deploy is set up for the
target platform.
If the target platform doesn't support running Vulkan, Direct3D 12, OpenGL 3.3,
or OpenGL ES 3.0, you have two options:
- Use a library at runtime to translate Vulkan or OpenGL calls to another graphics API.
For example,MoltenVKis used on macOS
to translate Vulkan to Metal at runtime.
Use a library at runtime to translate Vulkan or OpenGL calls to another graphics API.
For example,MoltenVKis used on macOS
to translate Vulkan to Metal at runtime.
- Create a new renderer from scratch. This is a large undertaking, especially if
you want to support both 2D and 3D rendering with advanced features.
Create a new renderer from scratch. This is a large undertaking, especially if
you want to support both 2D and 3D rendering with advanced features.

## Distributing a custom platform port
Danger
Before distributing a custom platform port, make sure you're allowed to
distribute all the code that is being linked against. Console SDKs are
typically under NDAs which prevent redistribution to the public.
Platform ports are designed to be as self-contained as possible. Most of the
code can be kept within a single folder located inplatform/. LikeCustom modules in C++, this allows for streamlining the build process
by making it possible togitclonea platform folder within a Godot repository
clone'splatform/folder, then runsconsplatform=<name>. No other steps are
necessary for building, unless third-party platform-specific dependencies need
to be installed first.
However, when a custom rendering driver is needed, another folder must be added
indrivers/. In this case, the platform port can be distributed as a fork of
the Godot repository, or as a collection of several folders that can be added
over a Godot Git repository clone.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.