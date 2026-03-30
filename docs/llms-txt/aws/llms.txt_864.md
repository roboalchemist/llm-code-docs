# Source: https://docs.aws.amazon.com/wickr/latest/wickrio/llms.txt

# AWS Wickr Bots and Integrations Guide

> AWS Wickr bots allow external services and workflows to communicate with AWS Wickr users.

- [What are AWS Wickr bots?](https://docs.aws.amazon.com/wickr/latest/wickrio/bot-overview.html)
- [CLI commands](https://docs.aws.amazon.com/wickr/latest/wickrio/cli-commands.html)
- [Logging](https://docs.aws.amazon.com/wickr/latest/wickrio/logging.html)
- [Troubleshooting](https://docs.aws.amazon.com/wickr/latest/wickrio/troubleshooting.html)
- [Release Notes](https://docs.aws.amazon.com/wickr/latest/wickrio/release-notes.html)

## [Setting up](https://docs.aws.amazon.com/wickr/latest/wickrio/setting-up.html)

- [Prerequisites](https://docs.aws.amazon.com/wickr/latest/wickrio/prerequisites.html): Before you start, complete the following before continuing with this guide:
- [Host machine and requirements](https://docs.aws.amazon.com/wickr/latest/wickrio/host-machine-requirements.html): You should provision a host machine capable of running Docker to deploy the Wickr IO Docker container.
- [Security Recommendations](https://docs.aws.amazon.com/wickr/latest/wickrio/security-recommendations.html): We recommend following best practices and if applicable, your organization's security policies to secure your bot deployment.
- [Version 6.48 announcement](https://docs.aws.amazon.com/wickr/latest/wickrio/version-6-48-announcement.html): Version 6.48 of the Bots docker image contains the upgrade to Node 20.


## [Quick start](https://docs.aws.amazon.com/wickr/latest/wickrio/quick-start.html)

- [Step 1: Create a bot user](https://docs.aws.amazon.com/wickr/latest/wickrio/create-bot-user.html): You can create a bot user in the Wickr console.
- [Step 2: Configure the host](https://docs.aws.amazon.com/wickr/latest/wickrio/configure-host.html): Complete the following procedure to configure the host.
- [Step 3: Deploy and configure the Docker container](https://docs.aws.amazon.com/wickr/latest/wickrio/deploy-docker.html): Complete the following procedure to deploy and configure the Docker container.
- [Deploy existing bot](https://docs.aws.amazon.com/wickr/latest/wickrio/deploy-existing-bot.html): Learn how to deploy an existing bot in Wickr.

### [AWS Wickr managed Integrations](https://docs.aws.amazon.com/wickr/latest/wickrio/aws-wickr-managed-integrations.html)

This section describes the production-ready bots that are built, maintained, and dispersed by AWS Wickr.

- [BroadcastBot Integration](https://docs.aws.amazon.com/wickr/latest/wickrio/broadcastbot-integration.html): The Wickr IO BroadcastBot allows you to broadcast messages to all of the members of your network or specific security groups.
- [Web Interface Integration](https://docs.aws.amazon.com/wickr/latest/wickrio/webinterface-integration.html): The Web Interface integration allows remote software the ability to interact with the associated Wickr IO client via a REST API.

### [Sample integrations](https://docs.aws.amazon.com/wickr/latest/wickrio/sample-integrations.html)

This section describes how to set up and use the following public sample bot integrations that are available for Wickr IO:

- [Wickr IO rekognition bot](https://docs.aws.amazon.com/wickr/latest/wickrio/wickr-io-rekognition-bot.html)
- [Wickr IO translation bot](https://docs.aws.amazon.com/wickr/latest/wickrio/wickr-io-translation-bot.html)
- [Wickr IO lex bot](https://docs.aws.amazon.com/wickr/latest/wickrio/wickr-io-lex-bot.html)


## [Develop a custom Wickr IO integration](https://docs.aws.amazon.com/wickr/latest/wickrio/develop-new-integration.html)

- [Integration setup](https://docs.aws.amazon.com/wickr/latest/wickrio/integration-setup.html): Complete the following procedure to setup a new custom Wickr IO integration.
- [Add a custom slash command](https://docs.aws.amazon.com/wickr/latest/wickrio/custom-slash-command.html): To add custom behavior, you have to make changes to index.js.
- [Build](https://docs.aws.amazon.com/wickr/latest/wickrio/build.html): Custom integrations in Wickr IO must be made available to the Wickr IO Docker container as a tarball named software.tar.gz.
- [Deploy](https://docs.aws.amazon.com/wickr/latest/wickrio/deploy.html): In this section you can deploy your custom integration using the Wickr IO Docker container.
- [Node.js Addon API](https://docs.aws.amazon.com/wickr/latest/wickrio/nodejs-addon-api.html): Learn about the Node.js addon API and how to use it.
- [Node.js Bot API (Development toolkit)](https://docs.aws.amazon.com/wickr/latest/wickrio/nodejs-bot-api.html): This section describes the Wickr IO Node.js Bot API framework and how to use it with several examples.
- [Addon and Bot API Usage Examples](https://docs.aws.amazon.com/wickr/latest/wickrio/addon-bot-api-usage-examples.html): This section contains several examples of the use of the Wickr IO addon and the Wickr IO Bot API.
- [Logging API](https://docs.aws.amazon.com/wickr/latest/wickrio/logging-api.html): This section describes the logging module that can be imported from the WickrIOAPI.
- [Python Bot Development](https://docs.aws.amazon.com/wickr/latest/wickrio/python-bot-development.html): To develop Wickr IO integrations in languages other than JavaScript such as Python, you will need to set up a Web REST API Interface integration on your machine and send HTTP/HTTPS requests to it.
- [Automatic Configuration](https://docs.aws.amazon.com/wickr/latest/wickrio/automatic-configuration.html): As of the 5.116 release you can use AWS services to define the bot credentials, token values and other configuration information.


## [Definitions](https://docs.aws.amazon.com/wickr/latest/wickrio/definitions.html)

### [Wickr message formats](https://docs.aws.amazon.com/wickr/latest/wickrio/message-formats.html)

This section describes the format of the Wickr messages utilized by the Wickr IO addon APIs and the Wickr IO Web Interface REST messaging APIs.

- [Text message](https://docs.aws.amazon.com/wickr/latest/wickrio/text-message.html): The msgtype for all text-based messages is 1000.
- [File transfer messages](https://docs.aws.amazon.com/wickr/latest/wickrio/file-transfer-messages.html): The msgtype for file transfer messages is 6000.
- [Calling messages](https://docs.aws.amazon.com/wickr/latest/wickrio/calling-messages.html): The msgtype for all location type messages is 7000 Calling messages will have a call object with a subset of the following values:
- [Location messages](https://docs.aws.amazon.com/wickr/latest/wickrio/location-messages.html): The msgtype for all location type messages is 8000.
- [Edit messages](https://docs.aws.amazon.com/wickr/latest/wickrio/edit-messages.html)
- [Edit reaction messages](https://docs.aws.amazon.com/wickr/latest/wickrio/edit-reaction-messages.html)
- [Wickr control messages](https://docs.aws.amazon.com/wickr/latest/wickrio/control-messages.html): Wickr control messages are used to setup and configure the Wickr group and secure room conversations.
- [Text message meta data](https://docs.aws.amazon.com/wickr/latest/wickrio/text-message-metadata.html): As of the 5.81 release of WickrIO, support was added to record the text message meta data fields.
