nix

# Module pty

Source Available on **crate feature `term`** only.

## Structs§

OpenptyResultRepresentation of a master/slave pty pairPtyMasterRepresentation of the Master device in a master/slave pty pairWinsize

## Enums§

ForkptyResult`process`A successful result of `forkpty()`.

## Functions§

forkpty⚠`process`Create a new process operating in a pseudoterminal.grantptGrant access to a slave pseudoterminal (see
`grantpt(3)`)openptyNon-`target_os=aix`Create a new pseudoterminal, returning the slave and master file descriptors
in `OpenptyResult`
(see `openpty`).posix_openptOpen a pseudoterminal device (see
`posix_openpt(3)`)ptsname⚠Get the name of the slave pseudoterminal (see
`ptsname(3)`)ptsname_r`linux_android`Get the name of the slave pseudoterminal (see
`ptsname(3)`)unlockptUnlock a pseudoterminal master/slave pseudoterminal pair (see
`unlockpt(3)`)

## Type Aliases§

SessionId
