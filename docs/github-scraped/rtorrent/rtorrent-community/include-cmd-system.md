
`execute.*` commands
^^^^^^^^^^^^^^^^^^^^

Call operating system commands, possibly catching their output for use within *rTorrent*.



> The `.bg` variants detach the child process from the *rTorrent* parent,
> i.e. it runs in the background. This **must** be used if you want to call
> back into *rTorrent* via XMLRPC, since otherwise there *will* be a deadlock.

> `throw` means to raise an error when the called command fails,
> while the `nothrow` variants will return the exit code.



> execute.throw
> execute.throw.bg
> execute2

```ini

            method.insert = log_stamp, private|simple,\
                "execute.capture_nothrow = bash, -c, \"echo -n $(date +%Y-%m-%d-%H%M%S)\""


    execute.raw
    execute.raw.bg
    execute.raw_nothrow
    execute.raw_nothrow.bg

        The ``execute.raw`` variants function identically to other ``execute.*`` commands,
        except that a tilde in the path to the executable is not expanded.



```

`system.*` commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

Commands related to the operating system and the XMLRPC API.


> system.listMethods
> system.methodExist
> system.methodHelp
> system.methodSignature
> system.getCapabilities

```ini

            system.umask.set ≫ value ‹time›

        Set the `umask`_ for the running *rTorrent* process.





```

`log.*` commands
^^^^^^^^^^^^^^^^^^^^^^^^^^


> log.add_output

```

            log.messages = (cat, (cfg.logs), "messages.log")

```