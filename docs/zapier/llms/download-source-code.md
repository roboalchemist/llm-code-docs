# Source: https://docs.zapier.com/platform/build-cli/download-source-code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Download the source code of a CLI integration

> If at any point you do not have the source code for your CLI integration and need it to make changes, you can download a zip file of the source code directly from the Platform UI.

## Prerequisites

Before doing this, you would have to ensure that:

* You are an admin for the integration. If you are not, you can have an admin [invite you](https://docs.zapier.com/platform/manage/add-team) to be a member of the integration team.
* Your dev environment meets the [requirements for running Platform CLI](https://docs.zapier.com/platform/build-cli/overview#requirements) with the proper version of Node.js installed.
* You have installed the Platform CLI tool in your local environment and set up your authentication.

```bash  theme={null}
# install the CLI globally
npm install -g zapier-platform-cli

# setup auth to Zapier's platform with a deploy key
zapier-platform login
```

## Downloading the source code

The steps to downloading the source code are:

1. Log in to the Platform UI and access the CLI integration for which you would like to get the source code.
2. On the sidebar, click on “Advanced”.
3. Go to the “View Source” section.
4. Click the “Download” button

![](https://cdn.zappy.app/7f1ed0ccac3d28a4dd4cb046560add1c.png)

Note that, after getting the source code, you would need to go into the directory and run the `npm install` command in order to install all the libraries needed for your integration. Then you can start making changes to the integration code, following our [best practices](https://docs.zapier.com/platform/build-cli/overview).

***

[*Need help? Tell us about your problem and we'll connect you with the right resource or contact support.*](https://developer.zapier.com/contact)
