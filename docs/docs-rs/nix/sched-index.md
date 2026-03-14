nix

# Module sched

Source Available on **crate feature `sched`** only.

## Structs§

CloneFlags`linux_android`Options for use with `clone`CpuSet`linux_android` or `freebsdlike`CpuSet represent a bit-mask of CPUs.
CpuSets are used by sched_setaffinity and
sched_getaffinity for example.

## Functions§

clone⚠`linux_android``clone` create a child process
(`clone(2)`)sched_getaffinity`linux_android` or `freebsdlike``sched_getaffinity` get a thread’s CPU affinity mask
(`sched_getaffinity(2)`)sched_getcpu`linux_android` or `freebsdlike`Determines the CPU on which the calling thread is running.sched_setaffinity`linux_android` or `freebsdlike``sched_setaffinity` set a thread’s CPU affinity mask
(`sched_setaffinity(2)`)sched_yieldExplicitly yield the processor to other threads.setns`linux_android`reassociate thread with a namespaceunshare`linux_android`disassociate parts of the process execution context

## Type Aliases§

CloneCb`linux_android`Type for the function executed by `clone`.
