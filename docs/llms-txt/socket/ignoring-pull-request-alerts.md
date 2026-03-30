# Source: https://docs.socket.dev/docs/ignoring-pull-request-alerts.md

# Ignoring pull request alerts

Bot commands for the GitHub App

If a pull request triggers a dependency alert, repository contributors can use a <Glossary>bot command</Glossary> to mark the dependency as ignored for the [GitHub App](https://docs.socket.dev/docs/socket-for-github).

Marking a dependency as ignored will rerun the pull request alert report and the dependency will be excluded from the new result.

This can be useful if the repository utilizes protected branches that require all checks to pass, and you accept the implications of merging a given dependency change.

Bot commands are issued by a repository contributor by writing a new comment in the pull request discussion, like this:

```
@SocketSecurity ignore foo@1.0.0 bar@2.3.1 baz@3.2.6-beta-1
```

Bot commands start with `@SocketSecurity ignore ` followed by a space separated list of `package-name@version` specifiers.

> 🚧 Note
>
> Bot commands must be *the very first thing* written in a comment, must be made by a *contributor* on the repo and can only be written in comments to the main pull request thread.

> 📘 Good to know
>
> Reports check the state of the pull request discussion whenever they are run, so re-running older check runs will take into account all the bot commands currently present in the pull request thread.

> 📘 Multiple comments possible
>
> Pull requests are allowed to have more than one bot command comment in them. All such comments will be taken into account.

## Un-ignoring

To un-ignore a package, edit or delete the comment that ignores the package you no longer want to ignore.