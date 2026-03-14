taos
# Crate tokio 
Source 
## Modules§
ioTraits, helpers, and type definitions for asynchronous I/O functionality.netTCP/UDP/Unix bindings for `tokio`.runtimeThe Tokio runtime.streamDue to the `Stream` trait’s inclusion in `std` landing later than Tokio’s 1.0
release, most of the Tokio stream utilities have been moved into the `tokio-stream`
crate.syncSynchronization primitives for use in asynchronous contexts.taskAsynchronous green-threads.timeUtilities for tracking time.
## Macros§
joinWaits on multiple concurrent branches, returning when **all** branches
complete.pinPins a value on the stack.selectWaits on multiple concurrent branches, returning when the **first** branch
completes, cancelling the remaining branches.task_localDeclares a new task-local key of type `tokio::task::LocalKey`.try_joinWaits on multiple concurrent branches, returning when **all** branches
complete with `Ok(_)` or on the first `Err(_)`.
## Functions§
spawnSpawns a new asynchronous task, returning a
`JoinHandle` for it.
## Attribute Macros§
mainMarks async function to be executed by the selected runtime. This macro
helps set up a `Runtime` without requiring the user to use
Runtime or
Builder directly.testMarks async function to be executed by runtime, suitable to test environment.
This macro helps set up a `Runtime` without requiring the user to use
Runtime or
Builder directly.