# Source: https://docs.socket.dev/docs/socket-npm-socket-npx.md

# socket npm & socket npx

System global package manager integration for npm

![](https://files.readme.io/9940353-npm.gif "npm.gif")

Socket has integration with `npm` and `npx` in beta. During this beta, these integrations do not perform authentication against organizations, do not use `socket.yml`, and are limited to default issue sets. Windows support is limited to WSL for now.

These integrations act the same as `npm` and `npx` and do not use command line flags. Additionally, for some tooling that needs to run these as a single bin, aliases as `socket-npm` and `socket-npx` are made available upon installation.

```
$ socket npm --help

  npm wrapper functionality

  Usage
    $ socket npm ...

  This runs npm but checks packages through Socket before installing anything.
  See docs for more details.

  Note: Everything after "npm" is sent straight to the npm command.
        Only the `--dryRun` and `--help` flags are caught here.

  Use `socket wrapper on` to automatically enable this such that you don't
  have to write `socket npm` for that purpose.

  Examples
    $ socket npm
    $ socket npm install -g socket
```

## `socket npm [args...]` and `socket npm [args...]`

Calls `npm` and `npx` and checks all packages with Socket before they get installed so you can be prevent installing malicious packages. Uses the builtin resolution of `npm` to precisely determine package installations.

## `socket wrapper --enabled`

When you enable the wrapper like this we create an alias in your system to run `socket npm` whenever you would run `npm`. Same for `npx`.

## FAQ

### Not seeing an alert with `socket npm install foo`

We only prompt for accepting the risk of installing packages for those that we alert on. Additionally, if you have already installed a package at a different version and it shares the same issue as the version you are installing, we do not prompt.

**NOTE:** In the beta you cannot configure what is considered to be an issue. Issues will always use our default issue set.

### Seeing alerts with `socket npm rm foo` OR Seeing alerts for an unrelated package with `socket npm install foo`

One might think that removing a package reduces vulnerabilities, however with package management this is not so straight forward.

`npm` normally creates what is called the ideal tree for a given `package.json` by removing a package you might actually change what the ideal tree is! If `foo` depends on `bar@1.1.x` it will constrain `bar` to be on `1.1.x` but a different dependency `baz` might depend on on `bar@1.x.x` which constrains `bar` to any version `1.x.x`. If `bar@1.2.0` exists it would be available only to upgrade if `bar` is removed from the `package.json`!

This ideal tree also performs things like automatic updates when using `npm install` in its default configuration. If a package `bar` exists in your `package.json` it will automatically be updated upon being found even if what is being installed is unrelated to `bar` in any way.

### Aliasing as `npm` or `npx`

`socket npm` will automatically detect if it is in front of `npm` in the `PATH` variable, and if it is not it will prepend itself to the `PATH` to intercept commands. This means if you use something like `socket npm run script-with-npx` it will already intercept `npx` without you needing to change your `package.json`.

For people wishing to avoid typing out `socket npm` a shell alias like the following in your `.bashrc` or `.zsh`. This is what `socket wrapper --enable` would do for you:

```sh
alias npm="socket-npm"
alias npx="socket-npx"
```

For `zsh` autocompletions you may wish to add the following as well.

```zsh
compdef _npm socket-npm
```

For `bash` autocompletions you may wish to add the following as well.

```bash
$(complete -p npm | sed 's/npm$/socket-npm/')
```

### Combining with `npq`

[npq](https://socket.dev/npm/package/npq), an alternative CLI to perform pre-install syntactic and CVE checks, **does not** directly integrate into a package manager for installation. You can configure the environment variable `NPQ_PKG_MGR=socket-npm` and alias `alias yarn="NPQ_PKG_MGR=yarn npq-hero"` to use both.

**NOTE:** Due to `socket npm` doing a full transitive scan and integrating into `npm` it is expected that `npq` will be faster since it is doing less.