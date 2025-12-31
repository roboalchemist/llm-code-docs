# Source: https://lingui.dev/tools/crowdin.md

# Crowdin

![Crowdin agile localization for developers](https://support.crowdin.com/assets/logos/crowdin-dark-symbol.png#gh-light-mode-only)![Crowdin agile localization for developers](https://support.crowdin.com/assets/logos/symbol/png/crowdin-symbol-cWhite.png#gh-dark-mode-only)

Crowdin is a localization management platform that helps translate your LinguiJS-based product. Automate localization, release several multilingual versions of your app simultaneously, and provide an enhanced experience for your global customers.

[Website](https://crowdin.com/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev) | [GitHub](https://github.com/crowdin) | [Support](https://crowdin.com/contacts?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev)

## Features[​](#features "Direct link to Features")

### Keep all translations in one place while connecting your teams via Crowdin[​](#keep-all-translations-in-one-place-while-connecting-your-teams-via-crowdin "Direct link to Keep all translations in one place while connecting your teams via Crowdin")

Connect with your content, marketing, and translation teams in one collaborative space:

* Screenshots for additional context.
* Highlight HTML, placeholders, plurals, and more.
* Describe the context and set character limits to ensure the translation fits the UI.
* All translations are done online or can be uploaded to the platform.
* Jira integration to notify you about source string issues.
* Tips for translators to ensure there is no extra space or broken code.

### Ship faster with localization running in parallel[​](#ship-faster-with-localization-running-in-parallel "Direct link to Ship faster with localization running in parallel")

Keep developing new features and improvements while translators receive new texts in real-time. Release multilingual versions for customers around the globe simultaneously.

### Release your product in several languages at once[​](#release-your-product-in-several-languages-at-once "Direct link to Release your product in several languages at once")

Help users from different regions use the latest version of your product in their language:

* Get feature branches translated independently from the master branch.
* Translators work together in one place to boost productivity.
* Never deal with translations in spreadsheets or email attachments.
* Source texts are updated for translators automatically and in real-time.
* Automatically pull completed translations that are ready to be merged.

### Seamlessly integrate localization during any phase of your development cycle[​](#seamlessly-integrate-localization-during-any-phase-of-your-development-cycle "Direct link to Seamlessly integrate localization during any phase of your development cycle")

Automate the integration of source texts and translations between Crowdin and your source code with one-click integration or customizable solutions.

### Define your translation strategy[​](#define-your-translation-strategy "Direct link to Define your translation strategy")

Decide who will translate your content:

* Invite your team of translators (in-house translators, freelancers, or translation agencies you already work with).
* Order professional translations from a vendor (translation agency) from Crowdin Vendors Marketplace.
* Configure machine translation engines.
* Engage your community.

### VCS: GitHub, GitLab, Bitbucket[​](#vcs-github-gitlab-bitbucket "Direct link to VCS: GitHub, GitLab, Bitbucket")

Source strings are pulled automatically and are always up to date for your translators. Translated content is automatically pushed to your repository as a request.

![Automatically pull source strings to Crowdin and push translated content to your repository](/assets/images/Crowdin__js-lingui-vcs-a0145c95baafee2bd889e6d08d7ec993.png)

## CLI[​](#cli "Direct link to CLI")

Connect cross-platform [Crowdin CLI](https://crowdin.github.io/crowdin-cli/) directly to your code repository and never deal with localization files manually again.

With Crowdin CLI, you can:

* Automate the process of updating your source files in your Crowdin project.
* Download translations from Crowdin and automatically save them in the correct locations.
* Upload all your existing translations to Crowdin in minutes.

### Create the `crowdin.yml` configuration file[​](#create-the-crowdinyml-configuration-file "Direct link to create-the-crowdinyml-configuration-file")

crowdin.yml

```
project_id: "123456" # Your Crowdin project ID
api_token_env: CROWDIN_PERSONAL_TOKEN

preserve_hierarchy: true

files: # Paths to the source and translation files
  - source: /**/locales/en/*
    translation: /**/locales/%two_letters_code%/%original_file_name%
```

### Install the Crowdin CLI as an npm package[​](#install-the-crowdin-cli-as-an-npm-package "Direct link to Install the Crowdin CLI as an npm package")

* npm
* Yarn
* pnpm

```
npm install --save-dev @crowdin/cli
```

```
yarn add --dev @crowdin/cli
```

```
pnpm add --save-dev @crowdin/cli
```

### Add the synchronization scripts[​](#add-the-synchronization-scripts "Direct link to Add the synchronization scripts")

Add the following scripts to your `package.json`:

package.json

```
{
  "scripts": {
    "crowdin": "crowdin",
    "sync": "crowdin push && crowdin pull",
    "sync:sources": "crowdin push",
    "sync:translations": "crowdin pull"
  }
}
```

### Configuration[​](#configuration "Direct link to Configuration")

Set the `CROWDIN_PERSONAL_TOKEN` env variable on your computer, to allow the CLI to authenticate with the Crowdin API.

#### Usage[​](#usage "Direct link to Usage")

Test that you can run the Crowdin CLI:

* npm
* Yarn
* pnpm

```
npm run crowdin --version
```

```
yarn crowdin --version
```

```
pnpm run crowdin --version
```

Upload all the source files to Crowdin:

* npm
* Yarn
* pnpm

```
npm run sync:sources
```

```
yarn sync:sources
```

```
pnpm run sync:sources
```

Download translation files from Crowdin:

* npm
* Yarn
* pnpm

```
npm run sync:translations
```

```
yarn sync:translations
```

```
pnpm run sync:translations
```

Upload sources to Crowdin and download translations from Crowdin:

* npm
* Yarn
* pnpm

```
npm run sync
```

```
yarn sync
```

```
pnpm run sync
```

To run other Crowdin CLI commands you can use the following command:

* npm
* Yarn
* pnpm

```
npm run crowdin <command> <options>
```

```
yarn crowdin <command> <options>
```

```
pnpm run crowdin <command> <options>
```

To see the full list of possible commands and options:

* npm
* Yarn
* pnpm

```
npm run crowdin -h
```

```
yarn crowdin -h
```

```
pnpm run crowdin -h
```

## Over-The-Air Content Delivery[​](#over-the-air-content-delivery "Direct link to Over-The-Air Content Delivery")

Over-the-Air Content Delivery is a feature that allows you to instantly update sources and translations in your mobile, server, desktop, or web apps with a single click without preparing a new release.

Visit the following pages to learn more about how to integrate Over-The-Air Content Delivery into your Lingui project:

* [Lingui tutorial - Crowdin OTA JS Client](https://crowdin.github.io/ota-client-js/tutorials/lingui/)
* [Lingui String Exporter - Crowdin Marketplace](https://store.crowdin.com/lingui-string-exporter?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev)

## API and Webhooks[​](#api-and-webhooks "Direct link to API and Webhooks")

Customize your experience. Automate and scale your localization workflow. Seamlessly add new content for translation to your Crowdin project, check translation status, merge new content, etc.

See the [API](https://support.crowdin.com/developer/api/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev) and [Webhooks](https://support.crowdin.com/developer/webhooks/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev) documentation for more information.

## Next Steps[​](#next-steps "Direct link to Next Steps")

To get started, register a [Crowdin.com](https://accounts.crowdin.com/register?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev) or [Crowdin Enterprise](https://accounts.crowdin.com/workspace/create?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev) account. Once you have signed up, [create your localization project](https://support.crowdin.com/creating-project/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev).

Depending on how you'd like to work with Crowdin, you have the following options:

1. [Integrate Crowdin with GitHub](https://support.crowdin.com/github-integration/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev).
2. Manage and synchronize your localization resources with [Crowdin CLI](https://developer.crowdin.com/cli-tool/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev).
3. [Upload files for the test via UI](https://support.crowdin.com/uploading-files/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev).
