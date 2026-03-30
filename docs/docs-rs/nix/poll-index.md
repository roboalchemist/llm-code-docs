nix

# Module poll

Source Available on **crate feature `poll`** only.

## Structs§

PollFdThis is a wrapper around `libc::pollfd`.PollFlagsThese flags define the different events that can be monitored by `poll` and `ppoll`PollTimeoutPollTimeout argument for polling.

## Enums§

PollTimeoutTryFromErrorError type for integer conversions into `PollTimeout`.

## Functions§

poll`poll` waits for one of a set of file descriptors to become ready to perform I/O.
(`poll(2)`)ppoll`signal``ppoll()` allows an application to safely wait until either a file
descriptor becomes ready or until a signal is caught.
(`poll(2)`)
