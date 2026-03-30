# Source: https://docs.socket.dev/docs/incremental-rollout.md

# Incremental Rollout

# Rolling Out Socket Incrementally in Your Project

Implementing new tools into your development workflow should be a seamless process, with minimal interruptions to productivity. This is why rolling out Socket incrementally can be the ideal approach for integrating Socket into your GitHub repositories. In this guide, we will discuss two main methods for implementing Socket incrementally: using `projectIgnorePaths` and leveraging the silent mode.

## Using `projectIgnorePaths` for Incremental Rollout

The `projectIgnorePaths` key in the `socket.yml` file allows you to exclude certain folders or files from being processed by Socket. This feature works similarly to the `.gitignore` file patterns. By adding paths to `projectIgnorePaths`, you can control where Socket runs and where it doesn't.

To incrementally rollout Socket using `projectIgnorePaths`, you can start by adding all project subfolders to `projectIgnorePaths`. This prevents Socket from running on any of them.

```yml
projectIgnorePaths:
  - "subfolder1"
  - "subfolder2"
  - "subfolder3"
```

Once you've set this up, you can gradually remove subfolders from `projectIgnorePaths` as you see fit, effectively enabling Socket incrementally. For example, to enable Socket in `subfolder1`, you would update `projectIgnorePaths` as follows:

```yml
projectIgnorePaths:
  - "subfolder2"
  - "subfolder3"
```

This approach gives you the flexibility to introduce Socket into your codebase at your own pace and ensure that each part of your project integrates well with Socket.

> 🚧 Mind the YAML
>
> When using directives like `!` and `*` in your project ignore paths, be sure that you wrap your selector rules in `"` (double quotes). YAML supports some unquoted strings, however some characters break this feature so its safer to wrap your strings in `"`.

## Using `triggerPaths` for Incremental Rollout

The `triggerPaths` key in `socket.yml` works similarly to `projectIgnorePaths`. It uses the same [`.gitignore`](https://git-scm.com/docs/gitignore) style syntax, except instead of matching files to ignore, it matches files to trigger Pull Request alerts on against the set of files modified in a pull request.

```yaml
triggerPaths:
  - "/subfolder1"
```

In this example, only pull requests that directly modify files inside of the `subfolder1` directory would trigger a Pull Request alert report. Any other Pull Requests would not see a Socket check run generated in their check suite.

`triggerPaths` can be used along side `projectIgnorePaths`. `triggerPaths` determines when reports are run and `projectIgnorePaths` determines which package manifest files are included in the report.

## Leveraging Silent Mode for Incremental Rollout

Silent mode allows you to deploy Socket in a non-intrusive way. In silent mode, Socket does not produce any visible indicators like PR alerts, GitHub checks, Dependency Overview Comments, or Security Alerts on your GitHub repository. Instead, all alerts are sent exclusively to a designated Slack channel.

To leverage silent mode for an incremental rollout, you would first enable silent mode for your entire repository. This allows you to observe Socket's behavior and interactions with your codebase in the Slack channel without any visible changes in your GitHub repository.

Once you have a thorough understanding of how Socket interacts with your project and you are confident in its performance, you can disable silent mode. This will enable Socket to start producing visible alerts and comments on your GitHub repository.

Remember, to enable silent mode, you need to contact Socket support, as it cannot be enabled directly through the `socket.yml` file.

## Conclusion

An incremental rollout of Socket provides a measured and controlled integration of the tool into your project. Whether you prefer to use `projectIgnorePaths` to selectively choose where Socket runs, or silent mode to observe Socket's operation in a non-intrusive manner, you have the flexibility to implement Socket in a way that best suits your team's needs and comfort levels.