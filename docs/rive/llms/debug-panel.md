# Source: https://uat.rive.app/docs/scripting/debugging/debug-panel.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Debug Panel

The Debug Panel lets you inspect script output and detect issues
in your code.

## Toolbar

Switch between [Console](#console) and [Problems](#problems) using the tabs to the left of the panel. Use the icons at the right end of the panel to open and close the panel and toggle fullscreen mode. Additional options to copy and clear the console show up when the Console tab is active.

<img src="https://mintcdn.com/rive/PNFYxEcCteEOymSI/images/scripting/debugging/debug-panel-toolbar.png?fit=max&auto=format&n=PNFYxEcCteEOymSI&q=85&s=36beeee24f03ad9dd25d13404362ac9b" alt="Debug panel toolbar" width="567" height="45" data-path="images/scripting/debugging/debug-panel-toolbar.png" />

## Console

The Console shows all log output from your scripts during playback. You can use the standard [Luau print()](https://create.roblox.com/docs/reference/engine/globals/LuaGlobals#print) function to log information, variable values, and messages.

```lua  theme={null}
print("Rive is so cool!")
print("Elapsed time:", seconds)
```

<img src="https://mintcdn.com/rive/PNFYxEcCteEOymSI/images/scripting/debugging/console-print.png?fit=max&auto=format&n=PNFYxEcCteEOymSI&q=85&s=3b6d4c0b18199498598631ae0631172b" alt="Debug panel toolbar" width="564" height="181" data-path="images/scripting/debugging/console-print.png" />

## Problems

The Problems tab lists problems detected *before* the script runs such as type mismatches, syntax errors, or missing data bindings.

The tab badge shows the number of issues found across your scripts.

Clicking a problem will jump directly to the affected line of code.
You can also hover any underlined code in the editor to see an explanation or suggested fix.

<img src="https://mintcdn.com/rive/PNFYxEcCteEOymSI/images/scripting/debugging/problems-panel.png?fit=max&auto=format&n=PNFYxEcCteEOymSI&q=85&s=99015303248a0e296b08d516264375c7" alt="Problems panel" width="1450" height="684" data-path="images/scripting/debugging/problems-panel.png" />
