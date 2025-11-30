# Source: https://www.electronjs.org/docs/latest/development/debugging-with-xcode

On this page

# Debugging with XCode

## Debugging with XCode[â€‹](#debugging-with-xcode "Direct link to Debugging with XCode") 

### Generate xcode project for debugging sources (cannot build code from xcode)[â€‹](#generate-xcode-project-for-debugging-sources-cannot-build-code-from-xcode "Direct link to Generate xcode project for debugging sources (cannot build code from xcode)") 

Run `gn gen` with the \--ide=xcode argument.

``` 
$ gn gen out/Testing --ide=xcode
```

This will generate the electron.ninja.xcworkspace. You will have to open this workspace to set breakpoints and inspect.

See `gn help gen` for more information on generating IDE projects with GN.

### Debugging and breakpoints[â€‹](#debugging-and-breakpoints "Direct link to Debugging and breakpoints") 

Launch Electron app after build. You can now open the xcode workspace created above and attach to the Electron process through the Debug \> Attach To Process \> Electron debug menu. \[Note: If you want to debug the renderer process, you need to attach to the Electron Helper as well.\]

You can now set breakpoints in any of the indexed files. However, you will not be able to set breakpoints directly in the Chromium source. To set break points in the Chromium source, you can choose Debug \> Breakpoints \> Create Symbolic Breakpoint and set any function name as the symbol. This will set the breakpoint for all functions with that name, from all the classes if there are more than one. You can also do this step of setting break points prior to attaching the debugger, however, actual breakpoints for symbolic breakpoint functions may not show up until the debugger is attached to the app.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/development/debugging-with-xcode.md)