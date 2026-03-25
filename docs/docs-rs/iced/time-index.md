iced
# Module time 
Source 
## Structs§
DurationA `Duration` type to represent a span of time, typically used for system
timeouts.InstantA measurement of a monotonically nondecreasing clock.
Opaque and useful only with `Duration`.SystemTimeA measurement of the system clock, useful for talking to
external entities like the file system or other processes.
## Functions§
daysCreates a `Duration` representing the given amount of days.every`tokio` or `smol` or WebAssemblyReturns a `Subscription` that produces messages at a set interval.hoursCreates a `Duration` representing the given amount of hours.millisecondsCreates a `Duration` representing the given amount of milliseconds.minutesCreates a `Duration` representing the given amount of minutes.nowReturns a `Task` that produces the current `Instant`
by calling `Instant::now`.repeat`tokio` or `smol` or WebAssemblyReturns a `Subscription` that runs the given async function at a
set interval; producing the result of the function as output.secondsCreates a `Duration` representing the given amount of seconds.