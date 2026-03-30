iced
# Module task 
Source 
## Structs§
HandleA handle to a `Task` that can be used for aborting it.TaskA set of concurrent actions to be performed by the iced runtime.
## Traits§
Sipper`sipper`A sipper is both a `Stream` that produces a bunch of progress
and a `Future` that produces some final output.Straw`sipper`A `Straw` is a `Sipper` that can fail.
## Functions§
sipper`sipper`Creates a new `Sipper` from the given async closure, which receives
a `Sender` that can be used to notify progress asynchronously.stream`sipper`Turns a `Sipper` into a `Stream`.
## Type Aliases§
Never`sipper`A type with no possible values.