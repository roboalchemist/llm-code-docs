# Source: https://docs.airbrake.io/docs/devops-tools/cli

Title: CLI

URL Source: https://docs.airbrake.io/docs/devops-tools/cli

Published Time: 2021-10-07T12:15:29+02:00

Markdown Content:
1.   [Home](https://docs.airbrake.io/)
2.   [Docs](https://docs.airbrake.io/docs/)
3.   [DevOps Tools](https://docs.airbrake.io/docs/devops-tools/)
4.   CLI

The official command line interface for interacting with Airbrake.

### On this page

*   [Installation and Authentication](https://docs.airbrake.io/docs/devops-tools/cli#installation-and-authentication)
    *   [Homebrew](https://docs.airbrake.io/docs/devops-tools/cli#homebrew)
    *   [Global flags](https://docs.airbrake.io/docs/devops-tools/cli#global-flags)

*   [Commands](https://docs.airbrake.io/docs/devops-tools/cli#commands)
    *   [Login Command](https://docs.airbrake.io/docs/devops-tools/cli#login-command)
    *   [Config Command](https://docs.airbrake.io/docs/devops-tools/cli#config-command)
    *   [Install Command](https://docs.airbrake.io/docs/devops-tools/cli#install-command)
    *   [Projects List Command](https://docs.airbrake.io/docs/devops-tools/cli#projects-list-command)
    *   [Notices Create Command](https://docs.airbrake.io/docs/devops-tools/cli#notices-create-command)
    *   [Source Maps Create Command](https://docs.airbrake.io/docs/devops-tools/cli#source-maps-create-command)
    *   [Capture Command](https://docs.airbrake.io/docs/devops-tools/cli#capture-command)
        *   [Other Capture use cases](https://docs.airbrake.io/docs/devops-tools/cli#other-capture-use-cases)

    *   [Going further](https://docs.airbrake.io/docs/devops-tools/cli#going-further)

*   [Issues](https://docs.airbrake.io/docs/devops-tools/cli#issues)

Installation and Authentication
-------------------------------

### Homebrew

```
brew install airbrake/airbrake-cli/airbrake
```

Depending on how you use the CLI, you may need to use the [`login` command](https://docs.airbrake.io/docs/devops-tools/cli#login-command), the [`config` command](https://docs.airbrake.io/docs/devops-tools/cli#config-command) or [global flags](https://docs.airbrake.io/docs/devops-tools/cli#global-flags) to specify api ID/KEY..

See the [Airbrake CLI Repo](https://github.com/airbrake/airbrake-cli) for further installation and authentication instructions.

### Global flags

Alternative to the `login` and `config` commands, you may specify the `--user-key` flag to the Airbrake CLI. The following are global flags for the `airbrake` command:

```
Flags:
      --config string        config file (default is $HOME/.airbrake.yaml)
      --project-key string   Project key used to access the API
      --user-key string      User key used to access the API
      --user-id string       User ID used to access the API
```

Commands
--------

### Login Command

_**Note:** the `login` command requires username and password and does not support two-factor authentication. For alternative authentication methods (eg: in cases where GitHub logins, SSO, or two-factor authentication are used), please use the [`config` command](https://docs.airbrake.io/docs/devops-tools/cli#config-command) or [global flags](https://docs.airbrake.io/docs/devops-tools/cli#global-flags)._

Log in with the Airbrake CLI by issuing the following command:

```
airbrake login
```

The `login` command will prompt you for your email, password, and an optional subdomain ([account subdomains](https://airbrake.io/docs/airbrake-faq/what-is-my-subdomain/) are used to differentiate if you have multiple Airbrake accounts using the same email address).

```
Enter your email: myemail@example.com
Enter your password:
Enter your subdomain (optional):
Done! The Airbrake CLI is configured for myemail@example.com
```

Completing the `login` command will generate a file in `$HOME/.airbrake.yaml` with contents like:

```
project-key: ""
user-key: ""
user-token: YOUR_USER_TOKEN
```

### Config Command

If your account requires GitHub or SSO logins, or you have you two-factor authentication enabled, you cannot authenticate with the `login` command. To authenticate in this situation, you can set credentials using the `airbrake config set` command. To set your user key (which can be retreived from [your profile settings page](https://airbrake.io/users/edit)) with the `config set` command, invoke:

```
airbrake config set user-key YOUR_USER_KEY_HERE
```

To check the values the Airbrake CLI is using, invoke:

```
airbrake config show
```

### Install Command

The Airbrake CLI offers an installation command which supports Ruby, Rails, Go, C#, Java, JavaScript, PHP, Python, Swift, and TypeScript via the `install` command:

```
# Use the --project-id flag if you already have an Airbrake project in
# your account you want to use
airbrake install --project-id 12345

# Or have the install command create a new Airbrake project:
airbrake install --create-project=DESIRED_PROJECT_NAME
```

### Projects List Command

This short example will show you how to send a test error notice to an Airbrake project with some basic commands.

Before we send the test error notice, we need to get the `id` of the project we want to send the notice to. To do this, invoke:

```
airbrake projects list
```

We’ll be using the `id` field from the `project list` output in the next command.

### Notices Create Command

Quickly create an error notice using the `notices create` command. Use the project ID you found when you listed your projects above.

```
airbrake notices create --project-id YOUR_PROJECT_ID \
    --type "Sample Error" \
    --message "My first error from the CLI"
```

This will send an error notice to the project you specified and provide you a direct link.

### Source Maps Create Command

If your project uses minified code, you can upload your source maps easily to Airbrake using the `sourcemaps create` command:

```
airbrake sourcemaps create --project-id YOUR_PROJECT_ID \
    --from-file '/path/to/your/file/app.min.js.map'
    --name 'unique-name'
    --pattern '%app.min.js'
```

This assumes that there is a source map file at the location specified. The pattern value tells Airbrake what minified files to match the source map to. In this example, `%app.min.js` tells Airbrake to match the source map to all files that end with `app.min.js`. For more info about pattern options, visit our [source maps doc](https://docs.airbrake.io/docs/features/private-sourcemaps/#pattern-matching-option). Patterns are optional and are generated from the file value if not specified.

### Capture Command

This section is intended as a guide to deploying the Airbrake CLI to capture output of entire commands, and send it to airbrake.io as a notification.

Note that this subcommand is available in version 1.2.5 and above.

To capture output of a regular unix shell (such as bash/csh/zsh/sh) command, run `airbrake capture` as so:

```
airbrake capture --project-key <KEY> --project-id <ID> -- echo my wish is your command
```

Alternatively, you can set the env vars:

```
export AB_PROJECT_KEY=<KEY>
export AB_PROJECT_ID=<ID>
airbrake capture -- echo my command is your wish
```

Your KEY and ID can be found on the right hand side of your airbrake project setting’s page in your airbrake.io account. You will need these for all forms of the airbrake capture command.

It may additionally be useful to export these variables in your `.bash_profile` (or equivalent) shell config/aliases file.

#### Other Capture use cases

For more OS-level cases, see the [OS/Shell](https://docs.airbrake.io/docs/platforms/os-shell) platform doc

For more use DevOps-focused cases and details for how to implement them, see [Shell Capture for IT/DevOps Use](https://docs.airbrake.io/docs/features/cli-capture-devops/)

### Going further

For information on all the available commands like deploys and more, invoke:

```
airbrake --help
```

Issues
------

For questions, suggestions, or issues, please visit our [official GitHub repository](https://github.com/airbrake/airbrake-cli).
