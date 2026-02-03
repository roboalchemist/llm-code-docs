# Run and test collections from the command line using Newman CLI

Newman is a command-line tool for running Postman Collections. Use Newman to run and test collections from the command line instead of in the Postman app. Newman is built with extensibility in mind, so you can incorporate it in your continuous integration (CI) pipelines and build systems.

The topics in this section will help you get started with Newman. For complete usage information, see Newman in the [npm registry](https://www.npmjs.com/package/newman) or on [GitHub](https://github.com/postmanlabs/newman).

> **You can also run collections from the command line with the [Postman CLI](/docs/postman-cli/postman-cli-overview/).** For more information on the differences between Newman and the Postman CLI, see [Decide which command-line companion to use](/docs/postman-cli/postman-cli-overview/#decide-which-command-line-companion-to-use).

![Running Newman](https://assets.postman.com/postman-docs/newman-running-in-terminal.gif)

## Get started in Newman

To get started, install Node.js and Newman, then run your collections. Learn more about [installing and running Newman](/docs/collections/using-newman-cli/installing-running-newman/).

You can also run Newman using Docker. Learn more about [running Newman with Docker on macOS, Ubuntu, and Windows](/docs/collections/using-newman-cli/newman-with-docker/).

## Newman options

Newman provides a rich set of options to customize a collection run. Learn more about [Newman options](/docs/collections/using-newman-cli/newman-options/).

## Upload files in Newman

Newman supports file uploads, so you can use a data file (such as a text file) to fill in form data fields. Learn more about [uploading files in Newman](/docs/collections/using-newman-cli/newman-file-uploads/).

## Newman reporters

Reporters can generate collection run reports for specific use cases, for example, logging the response body when a request (or its tests) fail. Learn more about using [Newman built-in reporters](/docs/collections/using-newman-cli/newman-built-in-reporters/) and [Newman external and custom reporters](/docs/collections/using-newman-cli/newman-custom-reporters/).

## Newman and continuous integration (CI)

You can integrate Newman in your continuous integration (CI) environment. Run your collections and tests automatically after every code push. Learn more about [using Newman with CI](/docs/collections/using-newman-cli/continuous-integration/), [using Newman with Travis CI](/docs/collections/using-newman-cli/integration-with-travis/), or [using Newman with Jenkins](/docs/collections/using-newman-cli/integration-with-jenkins/).

## Troubleshoot vault secrets

You can reference vault secrets stored in your local vault or a cloud vault by adding the vault secret inside double curly braces (`{{vault:secret-name}}`) and appending the prefix `vault:` to the vault secret's name. For example, to reference a vault secret named "postman-api-key", use the following syntax:

```txt
{{vault:postman-api-key}}
```

To learn more about troubleshooting empty and unresolved vault secrets, see [Troubleshoot vault secrets](/docs/sending-requests/postman-vault/troubleshoot-vault-secrets/).