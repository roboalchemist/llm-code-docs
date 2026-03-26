# Source: https://docs.socket.dev/docs/safe-npm-faq.md

# safe-npm FAQ

Start protecting your NPM usage today!

# How do I start using "safe npm"?

Install the [Socket CLI](https://docs.socket.dev/docs/socket-cli) by running `npm install -g socket` – that's it!

That command will add a `socket` binary to your PATH. Then, you can use `socket npm install` instead of `npm install` to benefit from Socket’s protections.

# How can I use this without replacing all my code that uses npm?

`socket npm` will automatically detect if it is in front of `npm` in the `PATH` variable, and if it is not it will prepend itself to the `PATH` to intercept commands. This means if you use something like `socket npm run script-with-npx` it will already intercept `npx` without you needing to change your `package.json`.

You can use `socket wrapper on` to create an alias such that this happens implicitly when running `npm` or `npx`.

If you'd rather do this yourself you can create a shell alias like the following in your `.bashrc` or `.zsh`:

```shell
alias npm="socket-npm"  
alias npx="socket-npx"
```

For `zsh` autocompletions you may wish to add the following as well:

```shell
compdef \_npm socket-npm
```

For `bash` autocompletions you may wish to add the following as well:

```shell
$(complete -p npm | sed 's/npm$/socket-npm/')
```

# Why do I see an alert when using socket `npm uninstall foo`?

You might think that removing a package could never cause a new package to be installed, but you'd be mistaken! It's possible for `npm uninstall` or `npm rm` to actually install new packages.

So, as counterintuitive as it might seem, you also need to be careful when running `npm uninstall`. Fortunately, Socket protects you in that situation if you use `socket npm uninstall` – so not to worry!

# Wait, why would `npm uninstall` ever install new packages?

`npm` creates what is called the "ideal tree" for a given `package.json`. So by removing a package you might actually change what the ideal tree is. Removing a package may remove a constraint which is keeping a package on an older version, so then npm may update those packages to a more ideal/recent version.

For example, if `foo` depends on `[bar@1.1.x](mailto:bar@1.1.x)` it will constrain `bar` to be on `1.1.x` but a different dependency `baz` might depend on `[bar@1.x.x](mailto:bar@1.x.x)` which constrains `bar` to any version `1.x.x`. If `[bar@1.2.0](mailto:bar@1.2.0)` exists it would be available to use if `foo` is removed from the `package.json`!

This "ideal tree” step also performs automatic updates when using `npm install` in its default configuration. If a package `bar` exists in your `package.json` it will automatically be updated upon being found even if what you’re installing is unrelated to `bar` in any way.

# Why am I seeing alerts for an unrelated package when using socket npm install foo?

Same reason as above.

# When will you support yarn and pnpm?

Socket supports `yarn` and `pnpm` throughout the product. See our full list of [supported language ecosystems and package managers](https://docs.socket.dev/docs/language-support) for more information.

However, for this current release of "safe npm", we only support `npm`.

# When will you support pip, poetry, etc.?

Socket supports Python. Specifically, [Socket for GitHub](https://docs.socket.dev/docs/socket-for-github) already supports `pip`, `poetry`, and other popular Python package managers. You can [read the announcement](https://socket.dev/blog/python-support) where we introduced Python support.

If you would like to see support for "safe pip" functionality, similar to "safe npm", please [vote for this feature request](https://socketdev.canny.io/feature-requests/p/support-safe-pip-functionality) here. With enough demand, we'd love to bring this feature to more ecosystems!

# How is the wrapper implemented?

There were lots of interesting things we had to do in order to completely cover various situations in `npm` and avoid some escapes that would bypass our wrapper. When you alias the wrapper with `alias npm="socket npm"` it would have been buggy if we didn't guard against basic child process invocation. For example running `npm run` will invoke a child process that can remove that alias. To that end, we are doing some tricks to protect against this. More information can be found in [our documentation](https://docs.socket.dev/docs/socket-npm-socket-npx).

If you'd like to get involved and contribute to the CLI, the codebase is online here: [https://github.com/SocketDev/socket-cli-js](https://github.com/SocketDev/socket-cli-js)