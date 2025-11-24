# Source: https://graphite-58cc94ce.mintlify.dev/docs/configure-cli.md

# Configure The CLI

> Learn how to configure the Graphite CLI to customize and speed up your workflow.

## Set up shell completion

Graphite supports `zsh`, `bash`, and `fish` tab completion. You can run one of the following commands:

### For zsh

```bash Terminal theme={null}
gt completion >> ~/.zshrc
```

### For bash

```bash Terminal theme={null}
gt completion >> ~/.bashrc
```

or

```bash Terminal theme={null}
gt completion >> ~/.bash_profile
```

### For fish

```bash Terminal theme={null}
gt fish >> ~/.config/fish/completions/gt.fish
```

## Configuration options

Run `gt config` to open an interactive menu which lets you configure your Graphite CLI. The options are described in more detail below.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=3139dd5351544c2b66fe054e09e06e9d" data-og-width="572" width="572" data-og-height="187" height="187" data-path="images/gt-config-1-7-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=280&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=11fc09ca35b4c615ee30cdfa6fe955c2 280w, https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=560&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=6ab4bf8af5fbcca4334a621322658552 560w, https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=840&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=53fae0a8870efb26f0b224b88ec01d1f 840w, https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=1100&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=6999220fc1dd6ec8381d0de244a4ceb5 1100w, https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=1650&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=ee7a2b62ce7abe79b35277ef72409b0c 1650w, https://mintcdn.com/graphite-58cc94ce/O2mERWnQNL78a2yp/images/gt-config-1-7-5.png?w=2500&fit=max&auto=format&n=O2mERWnQNL78a2yp&q=85&s=387242e43ef6a65fbd75566c03f0c5a0 2500w" />
</Frame>

## User-level configuration

<Note>
  User configuration is stored in `~/.config/graphite/`, [unless you have `$XDG_CONFIG_HOME` set.](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
</Note>

### Branch naming settings

If you don't specify a name for your branch when using [`gt create`](/command-reference#create-name), then Graphite will generate one for you based on the commit message.

There are several options to configure:

1. A custom prefix (for example, initials).

2. Whether or not the date is prepended to the branch.

3. Whether to allow certain characters like slashes and uppercase letters

4. The character to replace unsupported symbols (for example, whitespace and anything other than alphanumeric characters, periods, dashes, underscores, and slashes.)

### Submit settings

**Set PR metadata in CLI**

Graphite lets you prepare your PR for review in the web UI by default. This allows you to preview markdown, pull options like reviewers and labels from downstack PR's, and update all PR's in a stack at once.

Enable this setting to instead default to writing PR description in the CLI.

**PR description**

Graphite includes your GitHub PR template in the commit message by default.

Graphite can include the commit messages of your branch in the body of your PR automatically on submit. If you enable this, you can choose whether or not to also include your PR template.

If you only have a single commit on your branch, the first line of the message (its title) will not be included as this is already the default for the name of the PR.

### Rebase behavior

The `git rebase` flag `--committer-date-is-author-date` is useful if you don't want your Graphite restack operations to update the committer date of the commits in your branches. In order to have Graphite's internal rebases use this flag, you can enable this configuration.

### Empty branch settings

Specify how Graphite should handle empty branches after an operation (keep or delete).

### Default utilities

By default, Graphite uses the `git` editor for drafting PR descriptions and other flows that require editing text. You can configure a different editor.

By default, Graphite opens PR descriptions and other flows that require editing text in the `git` pager. You can configure a different pager, or disable paging entirely.

Note that just like git, Graphite sets the environment variables `LESS=FRX` and `LV=-c` if they are not already set. If something else is setting your `LESS` env var, you can use `gt user pager --set "less -FRX"` to get the recommended pager settings.

<Tip>
  You can also set the editor or pager on a per-command basis with the `GT_EDITOR` and `GT_PAGER` environment variables, respectively.
</Tip>

### Tips

Toggle on and off inline tips in the Graphite CLI.

### Yubikey

If you use a Yubikey to protect your GitHub SSH key, you may be used to Git commands reminding you to touch it. Graphite is not able to print this output directly to the CLI due to how Git calls SSH, so you can enable this configuration to be reminded when Graphite is about to run a command that requires you to touch your Yubikey.

### Update settings

You can individually enable or disable automatic updates and update prompts.

As of [version 1.7.4](/cli-changelog#1-7-4), `gt` is able to automatically update in the background. These automatic updates are disabled by default for existing `gt` installs that get updated to `1.7.4` or higher. They are enabled by default for new `gt` installs.

The configuration for automatic updates and update prompts gets set in the `~/.config/graphite/user_config` file:

```json  theme={null}
"updateAutomatically": true,
"promptForUpdates": true,
```

## Repository-level configuration

<Note>
  Repository-level configuration is stored in the `.git` folder of your repository.
</Note>

### Git remote name

Graphite defaults to pushing to and pulling from `origin`.If you have configured a different name for your remote, you can set it manually.

### GitHub repository information

Once the remote URL is set, Graphite infers the GitHub repository name and owner from the remote URL, but in cases where they are not inferred correctly, you can override them.

## Using Graphite CLI with multiple GitHub user accounts/auth tokens

<Note> Multiple profiles are supported from `gt` version `1.7.2` onwards </Note>

In your `~/.config/graphite/user_config` file you can set alternative named profiles so that each can make use of separate auth tokens:

```shell  theme={null}
{
  "alternativeProfiles": [
    {
      "name": "work_github_account",
      "authToken": "xxxx"
    },
    {
      "name": "personal_github_account",
      "authToken": "xxxx"
    }
  ]
}
```

Then set the `GRAPHITE_PROFILE` environment variable with the name of the profile you want to run `gt` commands with:

```shell  theme={null}
GRAPHITE_PROFILE=work_github_account gt sync
```

You can also name one of the profiles as "default" for it to always be used when not specifying the `GRAPHITE_PROFILE` environment variable:

```shell  theme={null}
{
  "alternativeProfiles": [
    {
      "name": "default",
      "authToken": "xxxx"
    },
    {
      "name": "personal_github_account",
      "authToken": "xxxx"
    }
  ]
}
```
