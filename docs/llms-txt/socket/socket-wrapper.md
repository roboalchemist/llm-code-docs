# Source: https://docs.socket.dev/docs/socket-wrapper.md

# socket wrapper

Enable or disable the Socket npm/npx wrapper

You can use `socket wrapper` to enable or disable the `socket npm` and `socket npx`wrappers on the current system.

## socket wrapper --help

```
$ socket wrapper --help

  Enable or disable the Socket npm/npx wrapper

  Usage
    $ socket wrapper <"on" | "off">

  Options
    (none)

  While enabled, the wrapper makes it so that when you call npm/npx on your
  machine, it will automatically actually run `socket npm` / `socket npx`
  instead.

  Examples
    $ socket wrapper on
    $ socket wrapper off
```

Once enabled, running `npm ...` on your system should actually run `socket npm ...` and make sure installed packages are safe.

## Installation

We leverage shell aliases and your RC file (like `.bashrc`) to make this work.

When you run `socket manifest` you still need to "finish" the installation before the change takes effect, regardless of whether you're turning it on or off.

This is a limitation of how a "shell" works that we can't circumvent: we cannot change aliases in your current terminal(s) because any command we would run, would run in a new shell.

As such, changes in command aliases only take effect after (re)starting a terminal or by "sourcing" your RC file (like `source ~/.bashrc` in bash). Future terminal sessions will start by reading your RC so that's covered.