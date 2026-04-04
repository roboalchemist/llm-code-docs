# Source: https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/functions.md

# StackState functions

## Overview

Functions in StackState are predefined scripts that transform input into an output. They're called by StackState on-demand. For example, when a component changes state, new telemetry flows in or a user triggers an action. Advanced users can develop their own functions to customize StackState. These functions can then be exported and [packaged with a custom StackPack](https://archivedocs.stackstate.com/5.1/develop/developer-guides/stackpack/develop_stackpacks).

## Function types

In StackState, different function types complete different tasks. Depending on the function type, it may be possible to specify [asynchronous or synchronous execution](#asynchronous-and-synchronous-execution) when creating a custom function. Some default functions are implemented as [native functions](#native-functions).

| Function type                                                                                                                        | Synchronous execution | Asynchronous execution | Native functions |
| ------------------------------------------------------------------------------------------------------------------------------------ | :-------------------: | :--------------------: | ---------------- |
| [Propagation functions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/propagation-functions#propagation-functions) |           ✅           |            ✅           | ✅                |
| [Event handler functions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/event-handler-functions)  |           ✅           |            ✅           | -                |
| [Component actions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/component-actions)              |           -           |            ✅           | -                |
| [Monitor functions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/monitor-functions)              |           -           |            ✅           | -                |
| [Check functions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/check-functions)                  |           ✅           |            -           | -                |
| [Component mapping functions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/mapping-functions)    |           ✅           |            -           | -                |
| [ID extractor functions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/id-extractor-functions)    |           ✅           |            -           | -                |
| [Relation mapping functions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/mapping-functions)     |           ✅           |            -           | -                |

## Asynchronous and synchronous execution

Functions in StackState run with either synchronous or asynchronous execution. For some functions it's possible to choose the execution type.

* **Asynchronous execution** - functions have access to all StackState [Script APIs](https://archivedocs.stackstate.com/5.1/develop/reference/scripting). Selecting asynchronous execution also makes it possible for more functions to run in parallel.
* **Synchronous execution** - functions don't have access to the StackState script APIs. If the function offers the possibility to be run with either asynchronous or synchronous execution, it's recommended to use asynchronous execution.

## Native functions

To improve performance, some default StackState functions have been implemented as native functions. It isn't possible to view or edit the script body of a native function in the StackState UI. It isn't possible to create a custom native function.
