nix

# Module time

Source Available on **crate feature `time`** only.

## Structs§

ClockIdClock identifierClockNanosleepFlagsFlags that are used for arming the timer.

## Functions§

clock_getcpuclockid`process`Get the clock id of the specified process id, (see
clock_getcpuclockid(3)).clock_getresNon-RedoxGet the resolution of the specified clock, (see
clock_getres(2)).clock_gettimeGet the time of the specified clock, (see
clock_gettime(2)).clock_nanosleep`linux_android` or `solarish` or `freebsdlike` or NetBSD or `target_os=hurd` or `target_os=aix`Suspend execution of this thread for the amount of time specified by `request`
and measured against the clock speficied by `clock_id`.clock_settimeNeither iOS nor tvOS nor watchOS nor Redox nor HermitCoreSet the time of the specified clock, (see
clock_settime(2)).
