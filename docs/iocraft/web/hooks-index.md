iocraft
# Module hooks 
Source 
## Structs§
Ref`Ref` is a copyable wrapper for a value that is owned by a component but does not cause
re-renders.RefMutRefA mutable reference to the value of a `Ref`.RefRefA reference to the value of a `Ref`.State`State` is a copyable wrapper for a value that can be observed for changes. States used by a
component will cause the component to be re-rendered when its value changes.StateMutRefA mutable reference to the value of a `State`.StateRefA reference to the value of a `State`.StderrHandleA handle to write to stderr, obtained from `UseOutput::use_output`.StdoutHandleA handle to write to stdout, obtained from `UseOutput::use_output`.
## Traits§
UseAsyncHandler`UseAsyncHandler` is a hook that allows you to create a `Handler` which executes an
asynchronous task that is bound to the lifetime of the component.UseConst`UseConst` is a hook that allows you to store a value which doesn’t change.UseContext`UseContext` provides methods for accessing context from a component.UseEffect`UseEffect` is a hook that allows you to execute a function after each update pass.UseFuture`UseFuture` is a hook that allows you to spawn an async task which is bound to the lifetime of
the component.UseMemo`UseMemo` is a hook that allows you to memoize a value, recomputing it only if any of its
listed dependencies change.UseOutput`UseOutput` is a hook that allows you to write to stdout and stderr from a component. The
output will be appended to stdout or stderr, above the rendered component output.UseRef`UseRef` is a hook that allows you to store a value which can be modified but doesn’t impact
rendering.UseState`UseState` is a hook that allows you to store state in a component.UseTerminalEvents`UseTerminalEvents` is a hook that allows you to listen for user input such as key strokes.UseTerminalSize`UseTerminalSize` is a hook that returns the current terminal size.