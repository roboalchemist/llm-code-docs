Source: https://docs.slack.dev/tools/slack-cli/guides/uninstalling-the-slack-cli

# Uninstalling the Slack CLI

All good things come to an end! If you need to uninstall the Slack CLI, run the commands below. Note that these instructions will uninstall the Slack CLI, but not its dependencies. Follow [these instructions](https://docs.deno.com/runtime/manual/tools/script_installer#uninstall) to uninstall Deno.

✨ **Just need to uninstall an app?** Refer to [Removing an app](/tools/slack-cli/guides/removing-an-app).

* MacOS & Linux uninstallation
* Windows uninstallation

Run the following commands in your terminal window

```text
rm -rf ~/.slack  # Delete the download binary$ rm /usr/local/bin/slack  # Delete the command alias (replacing `slack` with a command name)
```

The command binary is stored in `$HOME\AppData\Local\slack-cli` or `$HOME\.slack-cli`. This binary can be removed with the following command:

```text
rd -r $HOME\AppData\Local\slack-cli
```

where `$HOME` is substituted for the full path, e.g. `C:\Users\<your_username>`.

As with installation, PowerShell is required for uninstallation of the Slack CLI from Windows machines; an alternative shell will not work.

Removing the command from the `$env:path` can be done with the following command:

```bash
$env:Path = ($env:Path -split ';' -ne  "$HOME\AppData\Local\slack-cli\bin") -join ';'
```

Removing the command from the system path can be done with the following command:

```json
[System.Environment]::SetEnvironmentVariable('Path', (([System.Environment]::GetEnvironmentVariable('Path', [System.EnvironmentVariableTarget]::User) -split ';' -ne '$HOME\AppData\Local\slack-cli\bin') -join ';'), [System.EnvironmentVariableTarget]::User)
```

Finally, general configurations can be removed with the following command:

```text
rd -r $HOME\.slack
```

To check that uninstallation was successful, run the following commands and verify that you receive an error — in this case, that's a good thing!

```text
slack versionecho $env:path
```

Until next time!
