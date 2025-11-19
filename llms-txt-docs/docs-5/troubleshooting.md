# Source: https://docs.apify.com/cli/docs/troubleshooting.md

# Troubleshooting

Copy for LLM

## Problems with installation[](#problems-with-installation)

If you receive a permission error, read npm's [official guide](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally) on installing packages globally.

The best practice is to use a Node.js version manager to install Node.js 22+. It prevents permission issues from happening in the first place. We recommend:

* [fnm (Fast Node Manager)](https://github.com/Schniz/fnm)
* [Volta](https://volta.sh/).

Once you have the correct version of Node.js on your machine, install the Apify CLI with the following command:

```
npm install -g apify-cli
```

## Migrations[](#migrations)

You can find the differences and migration info in [migration guidelines](https://github.com/apify/apify-cli/blob/master/MIGRATIONS.md).

## Help command[](#help-command)

To see all CLI commands simply run:

```
apify help
```

To get information about a specific command run:

```
apify help COMMAND
```

## Need help?[](#need-help)

For general support, reach out to us at [apify.com/contact](https://apify.com/contact). You can also join [Apify Discord](https://apify.com/discord), if you have a question. If you believe you are encountering a bug, file it on [GitHub](https://github.com/apify/apify-cli/issues/new).
