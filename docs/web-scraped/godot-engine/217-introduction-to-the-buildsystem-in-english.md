# Introduction to the buildsystem in English

# Introduction to the buildsystem
Godot is a primarily C++ project and ituses the SCons build system.We love SCons for how maintainable and easy to set up it makes our buildsystem. And thanks to
that compiling Godot from source can be as simple as running:
```
scons
```
This produces an editor build for your current platform, operating system, and architecture.
You can change what gets built by specifying a target, a platform, and/or an architecture.
For example, to build an export template used for running exported games, you can run:
```
scons target=template_release
```
If you plan to debug or develop the engine, then you might want to enable thedev_buildoption to enable dev-only debugging code:
```
scons dev_build=yes
```
Following sections in the article will explain these and other universal options in more detail. But
before you can compile Godot, you need to install a few prerequisites. Please refer to the platform
documentation to learn more:
- Compiling for Android
Compiling for Android
- Compiling for iOS
Compiling for iOS
- Compiling for Linux, *BSD
Compiling for Linux, *BSD
- Compiling for macOS
Compiling for macOS
- Compiling for the Web
Compiling for the Web
- Compiling for Windows
Compiling for Windows
These articles cover in great detail both how to setup your environment to compile Godot on a specific
platform, and how to compile for that platform. Please feel free to go back and forth between them and
this article to reference platform-specific and universal configuration options.

## Using multi-threading
The build process may take a while, depending on how powerful your system is. By default, Godot's
SCons setup is configured to use all CPU threads but one (to keep the system responsive during
compilation). If the system has 4 CPU threads or fewer, it will use all threads by default.
If you want to adjust how many CPU threads SCons will use, use the-j<threads>parameter to specify how many threads will be used for the build.
Example for using 12 threads:
```
scons -j12
```

## Platform selection
Godot's build system will begin by detecting the platforms it can build
for. If not detected, the platform will simply not appear on the list of
available platforms. The build requirements for each platform are
described in the rest of this tutorial section.
SCons is invoked by just callingscons. If no platform is specified,
SCons will detect the target platform automatically based on the host platform.
It will then start building for the target platform right away.
To list the available target platforms, usesconsplatform=list:
```
scons platform=list
scons: Reading SConscript files ...
The following platforms are available:

    android
    ios
    linuxbsd
    macos
    web
    windows

Please run SCons again and select a valid platform: platform=<string>
```
To build for a platform (for example,linuxbsd), run with theplatform=(orp=to make it short) argument:
```
scons platform=linuxbsd
```

## Resulting binary
The resulting binaries will be placed in thebin/subdirectory,
generally with this naming convention:
```
godot.<platform>.<target>[.dev][.double].<arch>[.<extra_suffix>][.<ext>]
```
For the previous build attempt, the result would look like this:
```
ls bin
bin/godot.linuxbsd.editor.x86_64
```
This means that the binary is for Linuxor*BSD (notboth), is not optimized, has the
whole editor compiled in, and is meant for 64 bits.
A Windows binary with the same configuration will look like this:
```
C:\godot> dir bin/
godot.windows.editor.64.exe
```
Copy that binary to any location you like, as it contains the Project Manager,
editor and all means to execute the game. However, it lacks the data to export
it to the different platforms. For that the export templates are needed (which
can be either downloaded fromgodotengine.org, or
you can build them yourself).
Aside from that, there are a few standard options that can be set in all
build targets, and which will be explained below.

## Target
Thetargetoption controls if the editor is compiled and debug flags are used.
Optimization levels (optimize) and whether each build contains debug symbols
(debug_symbols) is controlled separately from the target. Each mode means:
- target=editor: Build an editor binary (definesTOOLS_ENABLEDandDEBUG_ENABLED)
target=editor: Build an editor binary (definesTOOLS_ENABLEDandDEBUG_ENABLED)
- target=template_debug: Build a debug export template (definesDEBUG_ENABLED)
target=template_debug: Build a debug export template (definesDEBUG_ENABLED)
- target=template_release: Build a release export template
target=template_release: Build a release export template
The editor is enabled by default in all PC targets (Linux, Windows, macOS),
disabled for everything else. Disabling the editor produces a binary that can
run projects but does not include the editor or the Project Manager.
The list ofcommand line argumentsavailable varies depending on the build type.
```
scons platform=<platform> target=editor|template_debug|template_release
```

## Development and production aliases
When creating builds for development (running debugging/profilingtools), you often have different goals compared to production builds
(making binaries as fast and small as possible).
Godot provides two aliases for this purpose:
- dev_mode=yesis an alias forverbose=yeswarnings=extrawerror=yestests=yes. This enables warnings-as-errors behavior (similar to Godot's
continuous integration setup) and also buildsunit testsso you can run them locally.
dev_mode=yesis an alias forverbose=yeswarnings=extrawerror=yestests=yes. This enables warnings-as-errors behavior (similar to Godot's
continuous integration setup) and also buildsunit testsso you can run them locally.
- production=yesis an alias foruse_static_cpp=yesdebug_symbols=nolto=auto. Statically linking libstdc++ allows for better binary portability
when compiling for Linux. This alias also enables link-time optimization when
compiling for Linux, Web and Windows with MinGW, but keeps LTO disabled when
compiling for macOS, iOS or Windows with MSVC. This is because LTO on those
platforms is very slow to link or has issues with the generated code.
production=yesis an alias foruse_static_cpp=yesdebug_symbols=nolto=auto. Statically linking libstdc++ allows for better binary portability
when compiling for Linux. This alias also enables link-time optimization when
compiling for Linux, Web and Windows with MinGW, but keeps LTO disabled when
compiling for macOS, iOS or Windows with MSVC. This is because LTO on those
platforms is very slow to link or has issues with the generated code.
You can manually override options from those aliases by specifying them on the
same command line with different values. For example, you can usesconsproduction=yesdebug_symbols=yesto create production-optimized binaries with
debugging symbols included.

## Dev build
Note
dev_buildshouldnotbe confused withdev_mode, which is an
alias for several development-related options (see above).
When doing engine development thedev_buildoption can be used together
withtargetto enable dev-specific code.dev_builddefinesDEV_ENABLED,
disables optimization (-O0//0d), enables generating debug symbols, and
does not defineNDEBUG(soassert()works in thirdparty libraries).
```
scons platform=<platform> dev_build=yes
```
This flag appends the.devsuffix (for development) to the generated
binary name.
See also
There are additional SCons options to enablesanitizers, which are tools
you can enable at compile-time to better debug certain engine issues.
SeeUsing sanitizersfor more information.

## Debugging symbols
By default,debug_symbols=nois used, which meansnodebugging symbols
are included in compiled binaries. Usedebug_symbols=yesto include debug
symbols within compiled binaries, which allows debuggers and profilers to work
correctly. Debugging symbols are also required for Godot's crash stacktraces to
display with references to source code files and lines.
The downside is that debugging symbols are large files (significantly larger
than the binaries themselves). As a result, official binaries currently do not
include debugging symbols. This means you need to compile Godot yourself to have
access to debugging symbols.
When usingdebug_symbols=yes, you can also useseparate_debug_symbols=yesto put debug information in a separate file with
a.debugsuffix. This allows distributing both files independently. Note
that on Windows, when compiling with MSVC, debugging information isalwayswritten to a separate.pdbfile regardless ofseparate_debug_symbols.
Use thestrip<path/to/binary>command to remove debugging symbols from
a binary you've already compiled.

## Optimization level
Several compiler optimization levels can be chosen from:
- optimize=speed_trace(default when targeting non-Web platforms): Favors
execution speed at the cost of larger binary size. Optimizations may sometimes
negatively impact debugger usage (stack traces may be less accurate. If this
occurs to you, useoptimize=debuginstead.
optimize=speed_trace(default when targeting non-Web platforms): Favors
execution speed at the cost of larger binary size. Optimizations may sometimes
negatively impact debugger usage (stack traces may be less accurate. If this
occurs to you, useoptimize=debuginstead.
- optimize=speed: Favors even more execution speed, at the cost of even
larger binary size compared tooptimize=speed_trace. Even less friendly to
debugging compared tooptimize=debug, as this uses the most aggressive
optimizations available.
optimize=speed: Favors even more execution speed, at the cost of even
larger binary size compared tooptimize=speed_trace. Even less friendly to
debugging compared tooptimize=debug, as this uses the most aggressive
optimizations available.
- optimize=size(default when targeting the Web platform): Favors small
binaries at the cost of slower execution speed.
optimize=size(default when targeting the Web platform): Favors small
binaries at the cost of slower execution speed.
- optimize=size_extra: Favors even smaller binaries, at the cost of even
slower execution speed compared tooptimize=size.
optimize=size_extra: Favors even smaller binaries, at the cost of even
slower execution speed compared tooptimize=size.
- optimize=debug: Only enables optimizations that do not impact debugging in
any way. This results in faster binaries thanoptimize=none, but slower
binaries thanoptimize=speed_trace.
optimize=debug: Only enables optimizations that do not impact debugging in
any way. This results in faster binaries thanoptimize=none, but slower
binaries thanoptimize=speed_trace.
- optimize=none: Do not perform any optimization. This provides the fastest
build times, but the slowest execution times.
optimize=none: Do not perform any optimization. This provides the fastest
build times, but the slowest execution times.
- optimize=custom(advanced users only): Do not pass optimization
arguments to the C/C++ compilers. You will have to pass arguments manually
using thecflags,ccflagsandcxxflagsSCons options.
optimize=custom(advanced users only): Do not pass optimization
arguments to the C/C++ compilers. You will have to pass arguments manually
using thecflags,ccflagsandcxxflagsSCons options.

## Architecture
Thearchoption is meant to control the CPU or OS version intended to run the
binaries. It is focused mostly on desktop platforms and ignored everywhere
else.
Supported values for thearchoption areauto,x86_32,x86_64,arm32,arm64,rv64,ppc32,ppc64andwasm32.
```
scons platform=<platform> arch={auto|x86_32|x86_64|arm32|arm64|rv64|ppc32|ppc64|wasm32}
```
This flag appends the value ofarchto resulting binaries when
relevant.  The default valuearch=autodetects the architecture
that matches the host platform.

## Custom modules
It's possible to compile modules residing outside of Godot's directory
tree, along with the built-in modules.
Acustom_modulesbuild option can be passed to the command line before
compiling. The option represents a comma-separated list of directory paths
containing a collection of independent C++ modules that can be seen as C++
packages, just like the built-inmodules/directory.
For instance, it's possible to provide both relative, absolute, and user
directory paths containing such modules:
```
scons custom_modules="../modules,/abs/path/to/modules,~/src/godot_modules"
```
Note
If there's any custom module with the exact directory name as a built-in
module, the engine will only compile the custom one. This logic can be used
to override built-in module implementations.
See also
Custom modules in C++

## Cleaning generated files
Sometimes, you may encounter an error due to generated files being present. You
can remove them by usingscons--clean<options>, where<options>is the
list of build options you've used to build Godot previously.
Alternatively, you can usegitclean-fixdwhich will clean build artifacts
for all platforms and configurations. Beware, as this will remove all untracked
and ignored files in the repository. Don't run this command if you have
uncommitted work!

## Other build options
There are several other build options that you can use to configure the
way Godot should be built (compiler, debug options, etc.) as well as the
features to include/disable.
Check the output ofscons--helpfor details about each option for
the version you are willing to compile.

### Overriding the build options

#### Using a file
The defaultcustom.pyfile can be created at the root of the Godot Engine
source to initialize any SCons build options passed via the command line:
```
optimize = "size"
module_mono_enabled = "yes"
use_llvm = "yes"
extra_suffix = "game_title"
```
You can also disable some of the built-in modules before compiling, saving some
time it takes to build the engine. SeeOptimizing a build for sizepage for more details.
See also
You can use the onlineGodot build options generatorto generate acustom.pyfile containing SCons options.
You can then save this file and place it at the root of your Godot source directory.
Another custom file can be specified explicitly with theprofilecommand
line option, both overriding the default build configuration:
```
scons profile=path/to/custom.py
```
Note
Build options set from the file can be overridden by the command line
options.
It's also possible to override the options conditionally:
```
import version

# Override options specific for Godot 3.x and 4.x versions.
if version.major == 3:
    pass
elif version.major == 4:
    pass
```

#### Using the SCONSFLAGS
SCONSFLAGSis an environment variable which is used by the SCons to set the
options automatically without having to supply them via the command line.
For instance, you may want to force a number of CPU threads with the
aforementioned-joption for all future builds:
```
export SCONSFLAGS="-j4"
```
```
set SCONSFLAGS=-j4
```
```
$env:SCONSFLAGS="-j4"
```

#### SCU (single compilation unit) build
Regular builds tend to be bottlenecked by including large numbers of headers
in each compilation translation unit. Primarily to speed up development (rather
than for production builds), Godot offers a "single compilation unit" build
(aka "Unity / Jumbo" build).
For the folders accelerated by this option, multiple.cppfiles are
compiled in each translation unit, so headers can be shared between multiple
files, which can dramatically decrease build times.
To perform an SCU build, use thescu_build=yesSCons option.
Note
When developing a Pull Request using SCU builds, be sure to make a
regular build prior to submitting the PR. This is because SCU builds
by nature include headers from earlier.cppfiles in the
translation unit, therefore won't catch all the includes you will
need in a regular build. The CI will catch these errors, but it will
usually be faster to catch them on a local build on your machine.

## Export templates
Official export templates are downloaded from the Godot Engine site:godotengine.org. However, you might want
to build them yourself (in case you want newer ones, you are using custom
modules, or simply don't trust your own shadow).
If you download the official export templates package and unzip it, you
will notice that most files are optimized binaries or packages for each
platform:
```
android_debug.apk
android_release.apk
android_source.zip
ios.zip
linux_debug.arm32
linux_debug.arm64
linux_debug.x86_32
linux_debug.x86_64
linux_release.arm32
linux_release.arm64
linux_release.x86_32
linux_release.x86_64
macos.zip
version.txt
web_debug.zip
web_dlink_debug.zip
web_dlink_nothreads_debug.zip
web_dlink_nothreads_release.zip
web_dlink_release.zip
web_nothreads_debug.zip
web_nothreads_release.zip
web_release.zip
windows_debug_x86_32_console.exe
windows_debug_x86_32.exe
windows_debug_x86_64_console.exe
windows_debug_x86_64.exe
windows_debug_arm64_console.exe
windows_debug_arm64.exe
windows_release_x86_32_console.exe
windows_release_x86_32.exe
windows_release_x86_64_console.exe
windows_release_x86_64.exe
windows_release_arm64_console.exe
windows_release_arm64.exe
```
To create those yourself, follow the instructions detailed for each
platform in this same tutorial section. Each platform explains how to
create its own template.
Theversion.txtfile should contain the corresponding Godot version
identifier. This file is used to install export templates in a version-specific
directory to avoid conflicts. For instance, if you are building export templates
for Godot 4.4.1,version.txtshould contain4.4.1.stableon the first
line (and nothing else). This version identifier is based on themajor,minor,patch(if present) andstatuslines of theversion.py file in the Godot Git repository.
If you are developing for multiple platforms, macOS is definitely the most
convenient host platform for cross-compilation, since you can cross-compile for
every target. Linux and Windows come in second place,
but Linux has the advantage of being the easier platform to set this up.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.