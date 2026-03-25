# Crate nix

Source Available on **Unix** only.

## Re-exports§

`pub use libc;`

## Modules§

dir`dir`List directory contentsenv`env`Environment variableserrnoSafe wrappers around errno functionsfcntlFile control optionsfeatures`feature`Feature tests for OS functionalityifaddrs`net`Query network interface addresseskmod`kmod`Load and unload kernel modules.mount`mount`Mount file systemsmqueue`mqueue`Posix Message Queue functionsnet`net`Functionality involving network interfacespoll`poll`Wait for events to trigger on specific file descriptorspty`term`Create master and slave virtual pseudo-terminals (PTYs)sched`sched`Execution schedulingspawn`process`Safe wrappers around posix_spawn* functions found in the libc “spawn.h” header.sysMostly platform-specific functionalitysyslog`syslog`Interfaces for controlling system log.time`time`Sleep, query system clocks, and set system clockucontext`ucontext`unistdSafe wrappers around functions found in libc “unistd.h” header

## Macros§

cmsg_space`uio`Create a buffer large enough for storing some control messages as returned
by `recvmsg`.getsockopt_implHelper for implementing `GetSockOpt` for a given socket option. See
`::sys::socket::GetSockOpt`.ioctl_noneGenerates a wrapper function for an ioctl that passes no data to the kernel.ioctl_none_badGenerates a wrapper function for a “bad” ioctl that passes no data to the kernel.ioctl_readGenerates a wrapper function for an ioctl that reads data from the kernel.ioctl_read_badGenerates a wrapper function for a “bad” ioctl that reads data from the kernel.ioctl_read_bufGenerates a wrapper function for an ioctl that reads an array of elements from the kernel.ioctl_readwriteGenerates a wrapper function for an ioctl that reads and writes data to the kernel.ioctl_readwrite_badGenerates a wrapper function for a “bad” ioctl that reads and writes data to the kernel.ioctl_readwrite_bufGenerates a wrapper function for an ioctl that reads and writes an array of elements to the kernel.ioctl_write_bufGenerates a wrapper function for an ioctl that writes an array of elements to the kernel.ioctl_write_intGenerates a wrapper function for a ioctl that writes an integer to the kernel.ioctl_write_int_badGenerates a wrapper function for a “bad” ioctl that writes an integer to the kernel.ioctl_write_ptrGenerates a wrapper function for an ioctl that writes data through a pointer to the kernel.ioctl_write_ptr_badGenerates a wrapper function for a “bad” ioctl that writes data through a pointer to the kernel.request_code_noneGenerate an ioctl request code for a command that passes no data.request_code_readGenerate an ioctl request code for a command that reads.request_code_readwriteGenerate an ioctl request code for a command that reads and writes.request_code_writeGenerate an ioctl request code for a command that writes.setsockopt_implHelper for implementing `SetSockOpt` for a given socket option. See
`::sys::socket::SetSockOpt`.sockopt_implHelper to generate the sockopt accessors. See
`::sys::socket::GetSockOpt` and
`::sys::socket::SetSockOpt`.

## Traits§

NixPathCommon trait used to represent file system paths by many Nix functions.

## Type Aliases§

ErrorNix’s main error type.ResultNix Result Type
