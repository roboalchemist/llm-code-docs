# Source: https://www.electronjs.org/docs/latest/development/debugging-on-macos

On this page

# Debugging on macOS

If you experience crashes or issues in Electron that you believe are not caused by your JavaScript application, but instead by Electron itself, debugging can be a little bit tricky especially for developers not used to native/C++ debugging. However, using `lldb` and the Electron source code, you can enable step-through debugging with breakpoints inside Electron\'s source code. You can also use [XCode for debugging](/docs/latest/development/debugging-with-xcode) if you prefer a graphical interface.

## Requirements[â€‹](#requirements "Direct link to Requirements") 

- **A testing build of Electron**: The easiest way is usually to build it from source, which you can do by following the instructions in the [build instructions](/docs/latest/development/build-instructions-macos). While you can attach to and debug Electron as you can download it directly, you will find that it is heavily optimized, making debugging substantially more difficult. In this case the debugger will not be able to show you the content of all variables and the execution path can seem strange because of inlining, tail calls, and other compiler optimizations.

- **Xcode**: In addition to Xcode, you should also install the Xcode command line tools. They include [LLDB](https://lldb.llvm.org/), the default debugger in Xcode on macOS. It supports debugging C, Objective-C and C++ on the desktop and iOS devices and simulator.

- **.lldbinit**: Create or edit `~/.lldbinit` to allow Chromium code to be properly source-mapped.

  :::: 
  ::: codeBlockContent_QJqH
  ``` 
  # e.g: ['~/electron/src/tools/lldb']
  script sys.path[:0] = ['<...path/to/electron/src/tools/lldb>']
  script import lldbinit
  ```
  :::
  ::::

## Attaching to and Debugging Electron[â€‹](#attaching-to-and-debugging-electron "Direct link to Attaching to and Debugging Electron") 

To start a debugging session, open up Terminal and start `lldb`, passing a non-release build of Electron as a parameter.

``` 
$ lldb ./out/Testing/Electron.app
(lldb) target create "./out/Testing/Electron.app"
Current executable set to './out/Testing/Electron.app' (x86_64).
```

### Setting Breakpoints[â€‹](#setting-breakpoints "Direct link to Setting Breakpoints") 

LLDB is a powerful tool and supports multiple strategies for code inspection. For this basic introduction, let\'s assume that you\'re calling a command from JavaScript that isn\'t behaving correctly - so you\'d like to break on that command\'s C++ counterpart inside the Electron source.

Relevant code files can be found in `./shell/`.

Let\'s assume that you want to debug `app.setName()`, which is defined in `browser.cc` as `Browser::SetName()`. Set the breakpoint using the `breakpoint` command, specifying file and line to break on:

``` 
(lldb) breakpoint set --file browser.cc --line 117
Breakpoint 1: where = Electron Framework`atom::Browser::SetName(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&) + 20 at browser.cc:118, address = 0x000000000015fdb4
```

Then, start Electron:

``` 
(lldb) run
```

The app will immediately be paused, since Electron sets the app\'s name on launch:

``` 
(lldb) run
Process 25244 launched: '/Users/fr/Code/electron/out/Testing/Electron.app/Contents/MacOS/Electron' (x86_64)
Process 25244 stopped
* thread #1: tid = 0x839a4c, 0x0000000100162db4 Electron Framework`atom::Browser::SetName(this=0x0000000108b14f20, name="Electron") + 20 at browser.cc:118, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
    frame #0: 0x0000000100162db4 Electron Framework`atom::Browser::SetName(this=0x0000000108b14f20, name="Electron") + 20 at browser.cc:118
   115     }
   116
   117   void Browser::SetName(const std::string& name) 
   120
   121   int Browser::GetBadgeCount() 
(lldb) frame variable
(atom::Browser *) this = 0x0000000108b14f20
(const string &) name = "Electron": 
```

To do a source level single step in the currently selected thread, execute `step` (or `s`). This would take you into `name_override_.empty()`. To proceed and do a step over, run `next` (or `n`).

``` 
(lldb) step
Process 25244 stopped
* thread #1: tid = 0x839a4c, 0x0000000100162dcc Electron Framework`atom::Browser::SetName(this=0x0000000108b14f20, name="Electron") + 44 at browser.cc:119, queue = 'com.apple.main-thread', stop reason = step in
    frame #0: 0x0000000100162dcc Electron Framework`atom::Browser::SetName(this=0x0000000108b14f20, name="Electron") + 44 at browser.cc:119
   116
   117    void Browser::SetName(const std::string& name) 
   120
   121   int Browser::GetBadgeCount()  

LLDB is a powerful tool with a great documentation. To learn more about it, consider Apple\'s debugging documentation, for instance the [LLDB Command Structure Reference](https://developer.apple.com/library/mac/documentation/IDEs/Conceptual/gdb_to_lldb_transition_guide/document/lldb-basics.html#//apple_ref/doc/uid/TP40012917-CH2-SW2) or the introduction to [Using LLDB as a Standalone Debugger](https://developer.apple.com/library/mac/documentation/IDEs/Conceptual/gdb_to_lldb_transition_guide/document/lldb-terminal-workflow-tutorial.html).

You can also check out LLDB\'s fantastic [manual and tutorial](https://lldb.llvm.org/tutorial.html), which will explain more complex debugging scenarios.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/development/debugging-on-macos.md)