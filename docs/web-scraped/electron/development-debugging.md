# Source: https://www.electronjs.org/docs/latest/development/debugging

On this page

# Electron Debugging

There are many different approaches to debugging issues and bugs in Electron, many of which are platform specific.

Some of the more common approaches are outlined below.

## Generic Debugging[â€‹](#generic-debugging "Direct link to Generic Debugging") 

Chromium contains logging macros which can aid debugging by printing information to console in C++ and Objective-C++.

You might use this to print out variable values, function names, and line numbers, amongst other things.

Some examples:

``` 
LOG(INFO) << "bitmap.width(): " << bitmap.width();

LOG(INFO, bitmap.width() > 10) << "bitmap.width() is greater than 10!";
```

There are also different levels of logging severity: `INFO`, `WARN`, and `ERROR`.

See [logging.h](https://chromium.googlesource.com/chromium/src/base/+/refs/heads/main/logging.h) in Chromium\'s source tree for more information and examples.

## Printing Stacktraces[â€‹](#printing-stacktraces "Direct link to Printing Stacktraces") 

Chromium contains a helper to print stack traces to console without interrupting the program.

``` 
#include "base/debug/stack_trace.h"
...
base::debug::StackTrace().Print();
```

This will allow you to observe call chains and identify potential issue areas.

## Breakpoint Debugging[â€‹](#breakpoint-debugging "Direct link to Breakpoint Debugging") 

> Note that this will increase the size of the build significantly, taking up around 50G of disk space

Write the following file to `electron/.git/info/exclude/debug.gn`

``` 
import("//electron/build/args/testing.gn")
is_debug = true
symbol_level = 2
forbid_non_component_debug_builds = false
```

Then execute:

``` 
$ gn gen out/Debug --args="import(\"//electron/.git/info/exclude/debug.gn\") $GN_EXTRA_ARGS"
$ ninja -C out/Debug electron
```

Now you can use `LLDB` for breakpoint debugging.

## Platform-Specific Debugging[â€‹](#platform-specific-debugging "Direct link to Platform-Specific Debugging") 

- [macOS Debugging](/docs/latest/development/debugging-on-macos)
  - [Debugging with Xcode](/docs/latest/development/debugging-with-xcode)
- [Windows Debugging](/docs/latest/development/debugging-on-windows)

## Debugging with the Symbol Server[â€‹](#debugging-with-the-symbol-server "Direct link to Debugging with the Symbol Server") 

Debug symbols allow you to have better debugging sessions. They have information about the functions contained in executables and dynamic libraries and provide you with information to get clean call stacks. A Symbol Server allows the debugger to load the correct symbols, binaries and sources automatically without forcing users to download large debugging files.

For more information about how to set up a symbol server for Electron, see [debugging with a symbol server](/docs/latest/development/debugging-with-symbol-server).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/development/debugging.md)