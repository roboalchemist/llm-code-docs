# Source: https://docs.socket.dev/docs/socket-raw-npx.md

# socket raw-npx

Temporarily disable the Socket npm/npx wrapper

```
$ socket raw-npx --help

  Temporarily disable the Socket npx wrapper

  Usage
    $ socket raw-npx ...

  This does the opposite of `socket npx`: it will execute the real `npx`
  command without Socket. This can be useful when you have the wrapper on
  and want to run a certain package anyways. Use at your own risk.

  Note: Everything after "raw-npx" is sent straight to the npx command.
        Only the `--dryRun` and `--help` flags are caught here.

  Examples
    $ socket raw-npx prettier
```

When you have `socket wrapper on` to protect your system and you want to run the raw `npx` command without the Socket wrapper anyways, this is what you want.

```
socket raw-npx log4j-joke
```

This would run `npx` and NOT warn you about bad packages.