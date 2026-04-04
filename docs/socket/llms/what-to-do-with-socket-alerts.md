# Source: https://docs.socket.dev/docs/what-to-do-with-socket-alerts.md

# What to do when you receive an alert

What should a developer do when they receive a Socket Alert on their pull request?

Developers sometimes ask "What do I do when I receive a Socket alert on added or updated dependencies?". Like all good questions, the first part of the answer tends to be "It depends!".

<Image title="Screenshot 2022-12-14 at 3.42.51 PM.png" alt={2130} src="https://files.readme.io/6546f11-Screenshot_2022-12-14_at_3.42.51_PM.png">
  An example of a Socket alert
</Image>

## Remove a package entirely

If you happen to install a dependency that Socket reports as [Known Malware](https://socket.dev/npm/issue/malware) or a [Protestware/Troll Package](), you should consider immediately removing it, or picking a different dependency.

## Take a closer look

On the other hand, if you add or update a package that introduces an [Install Script](https://socket.dev/npm/issue/installScripts) or [Native Code](https://socket.dev/npm/issue/hasNativeCode) you should take a quick moment to audit the source code of the package to make sure it's not doing anything malicious.

If Socket detects a [Potential Typo Squat](https://socket.dev/npm/issue/didYouMean), you should ensure you actually installed the correct package before dismissing the alert. If you're not sure what to do, you can always [ask us](https://socket.dev/contact), or someone on your security team, for help.

## Disable the offending package behavior

Finally, if you add or update a package which collects [Telemetry](https://socket.dev/npm/issue/telemetry), then you can follow the instructions in the pull request alert to disable the offending package behavior, i.e. stop the collection of telemetry, in your app.

## Ignoring pull request alerts

If a pull request triggers a dependency alert, repository contributors can use a bot command to mark the dependency as ignored for the GitHub App.

Marking a dependency as ignored will rerun the pull request alert report and the dependency will be excluded from the new result.

This can be useful if the repository utilizes protected branches that require all checks to pass, and you accept the implications of merging a given dependency change.

Bot commands are issued by a repository contributor by writing a new comment in the pull request discussion, like this:

```
@SocketSecurity ignore foo@1.0.0
```

Bot commands start with `@SocketSecurity ignore` followed by a space separated list of `package-name@version` specifiers.

Bot commands must be the very first thing written in a comment, must be made by a contributor on the repo and can only be written in comments to the main pull request thread.

Reports check the state of the pull request discussion whenever they are run, so re-running older check runs will take into account all the bot commands currently present in the pull request thread.