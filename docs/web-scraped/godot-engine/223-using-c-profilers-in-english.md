# Using C++ profilers in English

# Using C++ profilers
To optimize Godot's performance, you need to know what to optimize first.
To this end, profilers are useful tools.
Note
There is abuilt-in GDScript profilerin the editor,
but using a C++ profiler may be useful in cases where the GDScript profiler
is not accurate enough or is missing information due to bugs in the profiler.
There are two main types of profilers: sampling profilers and tracing profilers.
Sampling profilers periodically interrupt the running program and take a "sample",
which records which functions are running. Using this information, the profiler
estimates which functions the program spent the most time in.
Tracing profilers work by recording application-specific events (such as the
start and end of a single frame), producing a log called a "trace". The profiler
can use the trace to produce a graph showing an accurate high-level timeline of
what happened. However, any code that is not explicitly instrumented will not
appear in a tracing profiler's timeline!
Godot supports both sampling profilers and tracing profilers, and already
includes the logging code for common Godot events for use with a tracing profiler!
Different problems may be easier to debug with one kind of profiler over the other,
but it's difficult to provide a set of rules for which to use. Give both a try,
and see what you can learn from them!

## Sampling profilers
We recommend the following sampling profilers:
- VerySleepy(Windows only)
VerySleepy(Windows only)
- Hotspot(Linux only)
Hotspot(Linux only)
- Instruments(Apple only)
Instruments(Apple only)
These profilers may not be the most powerful or flexible options, but their
standalone operation and limited feature set tends to make them easier to use.

### Setting up Godot
To get useful profiling information, it isabsolutely requiredto use a Godot
build that includes debugging symbols. Official binaries do not include debugging
symbols, since these would make the download size significantly larger.
To get profiling data that best matches the production environment (but with debugging symbols),
you should compile binaries with theproduction=yesdebug_symbols=yesSCons options.
It is possible to run a profiler on less optimized builds (e.g.target=template_debugwithout LTO),
but results will naturally be less representative of real world conditions.
Warning
Donotstrip debugging symbols on the binaries using thestripcommand
after compiling the binaries. Otherwise, you will no longer get useful
profiling information when running a profiler.

### Benchmarking startup/shutdown times
If you're looking into optimizing Godot's startup/shutdown performance,
you can tell the profiler to use the--quitcommand line option on the Godot binary.
This will exit Godot just after it's done starting.
The--quitoption works with--editor,--project-manager, and--path<pathtoprojectdirectory>(which runs a project directly).
See also
SeeCommand line tutorialfor more command line arguments
supported by Godot.

## Tracing profilers
Godot currently supports three tracing profilers:
- Tracy
Tracy
- Perfetto
Perfetto
- Instruments(Apple only)
Instruments(Apple only)
In order to use either of them, you'll need to build the engine from source.
If you've never done this before, please readthese docsfor the platform you want to profile on.
You'll need to perform the same steps here, but with some additional arguments
forscons.

## All recommended profilers

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.