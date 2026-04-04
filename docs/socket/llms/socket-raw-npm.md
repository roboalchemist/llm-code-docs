# Source: https://docs.socket.dev/docs/socket-raw-npm.md

# socket raw-npm

Temporarily disable the Socket npm wrapper

```
$ socket raw-npm --help

  Temporarily disable the Socket npm wrapper

  Usage
    $ socket raw-npm ...

  This does the opposite of `socket npm`: it will execute the real `npm`
  command without Socket. This can be useful when you have the wrapper on
  and want to install a certain package anyways. Use at your own risk.

  Note: Everything after "raw-npm" is sent straight to the npm command.
        Only the `--dryRun` and `--help` flags are caught here.

  Examples
    $ socket raw-npm install -g socket
```

When you have `socket wrapper on` to protect your system and you want to run the raw `npm` command without the Socket wrapper anyways, this is what you want.

```
socket raw-npm install log4j-no-not-really
```

This would then NOT warn you about bad packages.