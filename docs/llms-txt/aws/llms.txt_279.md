# Source: https://docs.aws.amazon.com/dcv/latest/sm-cli/llms.txt

# Amazon DCV Session Manager CLI Guide

- [What is Session Manager CLI?](https://docs.aws.amazon.com/dcv/latest/sm-cli/what-is-sm-cli.html)
- [Installing the Session Manager CLI](https://docs.aws.amazon.com/dcv/latest/sm-cli/installing-sm-cli.html)
- [Release Notes and Document History](https://docs.aws.amazon.com/dcv/latest/sm-cli/doc-history-release-notes.html)

## [Configuring the Session Manager CLI](https://docs.aws.amazon.com/dcv/latest/sm-cli/configuring-sm-cli.html)

- [Configuration basics](https://docs.aws.amazon.com/dcv/latest/sm-cli/credentials-and-configuration.html): The Amazon DCV Session Manager CLI has a set of configuration parameters that the user can specify.

### [Configuring the CLI settings](https://docs.aws.amazon.com/dcv/latest/sm-cli/configuration-hierarchy.html)

The Amazon DCV Session Manager uses credentials and configuration settings that are located in multiple places.

- [Command line options](https://docs.aws.amazon.com/dcv/latest/sm-cli/command-line-options.html): In the Amazon DCV Session Manager, you can use the following command line options to override the default configuration settings, any corresponding profile setting, or environment variable setting for that single command.
- [Environment variables](https://docs.aws.amazon.com/dcv/latest/sm-cli/environment-variables.html): Environment variables provide another way to specify some configuration options and credentials.
- [Configuration file](https://docs.aws.amazon.com/dcv/latest/sm-cli/configuration-file.html): The configuration file is the third way to specify some configuration options and credentials.


## [Working with the CLI](https://docs.aws.amazon.com/dcv/latest/sm-cli/working-with-sm-cli.html)

- [Getting help with commands](https://docs.aws.amazon.com/dcv/latest/sm-cli/getting-help-sm-cli.html): You can get help with any command when using the Amazon DCV Session Manager CLI.
- [Using the command structure](https://docs.aws.amazon.com/dcv/latest/sm-cli/sm-cli-command-structure.html): This topic covers how the Amazon DCV Session Manager CLI command is structured.
- [Using return codes](https://docs.aws.amazon.com/dcv/latest/sm-cli/return-codes.html): A return code is usually, but not always, a hidden code sent after running a Amazon DCV Session Manager CLI command describing its status.


## [CLI command reference](https://docs.aws.amazon.com/dcv/latest/sm-cli/sm-cli-reference.html)

- [close-servers](https://docs.aws.amazon.com/dcv/latest/sm-cli/close-server.html): Closes one or more Amazon DCV servers.
- [create-session](https://docs.aws.amazon.com/dcv/latest/sm-cli/create-session.html): Creates a new Amazon DCV session with the specified details.
- [delete-session](https://docs.aws.amazon.com/dcv/latest/sm-cli/delete-session.html): Deletes the specified Amazon DCV session, and removes it from the cache of the broker.
- [describe-servers](https://docs.aws.amazon.com/dcv/latest/sm-cli/describe-servers.html): Describe the specified Amazon DCV server.
- [describe-sessions](https://docs.aws.amazon.com/dcv/latest/sm-cli/describe-sessions.html): Describes one or more Amazon DCV servers.
- [get-session-connection-data](https://docs.aws.amazon.com/dcv/latest/sm-cli/get-session-connection-data.html): Gets connection information for a specific user's connection to a specific Amazon DCV session.
- [get-session-screenshots](https://docs.aws.amazon.com/dcv/latest/sm-cli/get-session-screenshots.html): Gets screenshots of one or more Amazon DCV sessions.
- [open-servers](https://docs.aws.amazon.com/dcv/latest/sm-cli/open-server.html): Opens one or more Amazon DCV servers.
- [update-session-permissions](https://docs.aws.amazon.com/dcv/latest/sm-cli/update-session-permissions.html): Updates the user permissions for a specific Amazon DCV session.
