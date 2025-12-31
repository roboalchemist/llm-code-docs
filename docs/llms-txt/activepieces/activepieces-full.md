# Activepieces Documentation

Source: https://www.activepieces.com/docs/llms-full.txt

---

# Breaking Changes
Source: https://www.activepieces.com/docs/about/breaking-changes

This list shows all versions that include breaking changes and how to upgrade.

## 0.71.0

### What has changed?

* In separate workers setup, now they have access to Redis.
* `AP_EXECUTION_MODE` mode `SANDBOXED` is now deprecated and replaced with `SANDBOX_PROCESS`
* Code Copilot has been deprecated. It will be reintroduced in a different, more powerful form in the future.

### When is action necessary?

* If you have separate workers setup, you should make sure that workers have access to Redis.
* If you are using `AP_EXECUTION_MODE` mode `SANDBOXED`, you should replace it with `SANDBOX_PROCESS`

## 0.70.0

### What has changed?

* `AP_QUEUE_MODE` is now deprecated and replaced with `AP_REDIS_TYPE`
* If you are using Sentinel Redis, you should add `AP_REDIS_TYPE` to `SENTINEL`

### When is action necessary?

* If you are using `AP_QUEUE_MODE`, you should replace it with `AP_REDIS_TYPE`
* If you are using Sentinel Redis, you should add `AP_REDIS_TYPE` to `SENTINEL`

## 0.69.0

### What has changed?

* `AP_FLOW_WORKER_CONCURRENCY` and `AP_SCHEDULED_WORKER_CONCURRENCY` are now deprecated all jobs have single queue and replaced with `AP_WORKER_CONCURRENCY`

### When is action necessary?

* If you are using `AP_FLOW_WORKER_CONCURRENCY` or `AP_SCHEDULED_WORKER_CONCURRENCY`, you should replace them with `AP_WORKER_CONCURRENCY`

## 0.66.0

### What has changed?

* If you use embedding the embedding SDK, please upgrade to version 0.6.0, `embedding.dashboard.hideSidebar` used to hide the navbar above the flows table in the dashboard now it relies on `embedding.dashboard.hideFlowsPageNavbar`

## 0.64.0

### What has changed?

* MCP management is removed from the embedding SDK.

## 0.63.0

### What has changed?

* Replicate provider's text models have been removed.

### When is action necessary?

* If you are using one of Replicate's text models, you should replace it with another model from another provider.

## 0.46.0

### What has changed?

* The UI for "Array of Properties" inputs in the pieces has been updated, particularly affecting the "Dynamic Value" toggle functionality.

### When is action necessary?

* No action is required for this change.
* Your published flows will continue to work without interruption.
* When editing existing flows that use the "Dynamic Value" toggle on "Array of Properties" inputs (such as the "files" parameter in the "Extract Structured Data" action of the "Utility AI" piece), the end user will need to remap the values again.
* For details on the new UI implementation, refer to this [announcement](https://community.activepieces.com/t/inline-items/8964).

## 0.38.6

### What has changed?

* Workers no longer rely on the `AP_FLOW_WORKER_CONCURRENCY` and `AP_SCHEDULED_WORKER_CONCURRENCY` environment variables. These values are now retrieved from the app server.

### When is action necessary?

* If `AP_CONTAINER_TYPE` is set to `WORKER` on the worker machine, and `AP_SCHEDULED_WORKER_CONCURRENCY` or `AP_FLOW_WORKER_CONCURRENCY` are set to zero on the app server, workers will stop processing the queues. To fix this, check the [Separate Worker from App](https://www.activepieces.com/docs/install/configuration/separate-workers) documentation and set the `AP_CONTAINER_TYPE` to fetch the necessary values from the app server. If no container type is set on the worker machine, this is not a breaking change.

## 0.35.1

### What has changed?

* The 'name' attribute has been renamed to 'externalId' in the `AppConnection` entity.
* The 'displayName' attribute has been added to the `AppConnection` entity.

### When is action necessary?

* If you are using the connections API, you should update the `name` attribute to `externalId` and add the `displayName` attribute.

## 0.35.0

### What has changed?

* All branches are now converted to routers, and downgrade is not supported.

## 0.33.0

### What has changed?

* Files from actions or triggers are now stored in the database / S3 to support retries from certain steps, and the size of files from actions is now subject to the limit of `AP_MAX_FILE_SIZE_MB`.
* Files in triggers were previously passed as base64 encoded strings; now they are passed as file paths in the database / S3. Paused flows that have triggers from version 0.29.0 or earlier will no longer work.

### When is action necessary?

* If you are dealing with large files in the actions, consider increasing the `AP_MAX_FILE_SIZE_MB` to a higher value, and make sure the storage system (database/S3) has enough capacity for the files.

## 0.30.0

### What has changed?

* `AP_SANDBOX_RUN_TIME_SECONDS` is now deprecated and replaced with `AP_FLOW_TIMEOUT_SECONDS`
* `AP_CODE_SANDBOX_TYPE` is now deprecated and replaced with new mode in `AP_EXECUTION_MODE`

### When is action necessary?

* If you are using `AP_CODE_SANDBOX_TYPE` to `V8_ISOLATE`, you should switch to `AP_EXECUTION_MODE` to `SANDBOX_CODE_ONLY`
* If you are using `AP_SANDBOX_RUN_TIME_SECONDS` to set the sandbox run time limit, you should switch to `AP_FLOW_TIMEOUT_SECONDS`

## 0.28.0

### What has changed?

* **Project Members:**
  * The `EXTERNAL_CUSTOMER` role has been deprecated and replaced with the `OPERATOR` role. Please check the permissions page for more details.
  * All pending invitations will be removed.
  * The User Invitation entity has been introduced to send invitations. You can still use the Project Member API to add roles for the user, but it requires the user to exist. If you want to send an email, use the User Invitation, and later a record in the project member will be created after the user accepts and registers an account.
* **Authentication:**
  * The `SIGN_UP_ENABLED` environment variable, which allowed multiple users to sign up for different platforms/projects, has been removed. It has been replaced with inviting users to the same platform/project. All old users should continue to work normally.

### When is action necessary?

* **Project Members:**

If you use the embedding SDK or the create project member API with the `EXTERNAL_CUSTOMER` role, you should start using the `OPERATOR` role instead.

* **Authentication:**

Multiple platforms/projects are no longer supported in the community edition. Technically, everything is still there, but you have to hack using the API as the authentication system has now changed. If you have already created the users/platforms, they should continue to work, and no action is required.


# Changelog
Source: https://www.activepieces.com/docs/about/changelog

A log of all notable changes to Activepieces



# Editions
Source: https://www.activepieces.com/docs/about/editions



Activepieces operates on an open-core model, providing a core software platform as open source licensed under the permissive **MIT** license while offering additional features as proprietary add-ons in the cloud.

### Community / Open Source Edition

The Community edition is free and open source. It has all the pieces and features to build and run flows without any limitations.

### Commercial Editions

Learn more at: [https://www.activepieces.com/pricing](https://www.activepieces.com/pricing)

## Feature Comparison

| Feature                  | Community | Enterprise | Embed    |
| ------------------------ | --------- | ---------- | -------- |
| Flow History             | ✅         | ✅          | ✅        |
| All Pieces               | ✅         | ✅          | ✅        |
| Flow Runs                | ✅         | ✅          | ✅        |
| Unlimited Flows          | ✅         | ✅          | ✅        |
| Unlimited Connections    | ✅         | ✅          | ✅        |
| Unlimited Flow steps     | ✅         | ✅          | ✅        |
| Custom Pieces            | ✅         | ✅          | ✅        |
| On Premise               | ✅         | ✅          | ✅        |
| Cloud                    | ❌         | ✅          | ✅        |
| Project Team Members     | ❌         | ✅          | ✅        |
| Manage Multiple Projects | ❌         | ✅          | ✅        |
| Limits Per Project       | ❌         | ✅          | ✅        |
| Pieces Management        | ❌         | ✅          | ✅        |
| Templates Management     | ❌         | ✅          | ✅        |
| Custom Domain            | ❌         | ✅          | ✅        |
| All Languages            | ✅         | ✅          | ✅        |
| JWT Single Sign On       | ❌         | ❌          | ✅        |
| Embed SDK                | ❌         | ❌          | ✅        |
| Audit Logs               | ❌         | ✅          | ❌        |
| Git Sync                 | ❌         | ✅          | ❌        |
| Private Pieces           | ❌         | <b>5</b>   | <b>2</b> |
| Custom Email Branding    | ❌         | ✅          | ✅        |
| Custom Branding          | ❌         | ✅          | ✅        |


# i18n Translations
Source: https://www.activepieces.com/docs/about/i18n



This guide helps you understand how to change or add new translations.

Activepieces uses Crowdin because it helps translators who don't know how to code. It also makes the approval process easier. Activepieces automatically sync new text from the code and translations back into the code.

## Contribute to existing translations

1. Create Crowdin account
2. Join the project [https://crowdin.com/project/activepieces](https://crowdin.com/project/activepieces)

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f35baceeb1f6be0f60093a5e04572c7c" alt="Join Project" data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="resources/crowdin.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=385b4c7a8cf38fadc3ff0ec14d9db71f 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=04d599483cc42ec7130ac4abf9530b7a 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f06487a1755576698428f76132431d06 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=098f0dd3c0e1b1fcaecdb4ca0ee48e24 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=c940c4229f3a3e107f4302e15f04870e 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=516f8920d49365f926389a989743fd5c 2500w" />

3. Click on the language you want to translate

4. Click on "Translate All"

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin-translate-all.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=37cd80d9ab9d97df1da60fa495dba477" alt="Translate All" data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="resources/crowdin-translate-all.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin-translate-all.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=6801cd01effecf67dd1afd35fc5ad7a4 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin-translate-all.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=b8329e504a59a2f36a3f2641aebf694a 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin-translate-all.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=6a23e65823b5a68967f144b20338c625 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin-translate-all.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=9274f2cce14a585cc95e0b5b5623fc41 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin-translate-all.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=1bd232597ff601a688d9214c855bcf62 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/crowdin-translate-all.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=0acfc2f4d28f4a9ac17a3225ab5118a9 2500w" />

5. Select Strings you want to translate and click on "Save" button

## Adding a new language

* Please contact us ([support@activepieces.com](mailto:support@activepieces.com)) if you want to add a new language. We will add it to the project and you can start translating.


# License
Source: https://www.activepieces.com/docs/about/license



Activepieces' **core** is released as open source under the [MIT license](https://github.com/activepieces/activepieces/blob/main/LICENSE) and enterprise / cloud editions features are released under [Commercial License](https://github.com/activepieces/activepieces/blob/main/packages/ee/LICENSE)

The MIT license is a permissive license that grants users the freedom to use, modify, or distribute the software without any significant restrictions. The only requirement is that you include the license notice along with the software when distributing it.

Using the enterprise features (under the packages/ee and packages/server/api/src/app/ee folder) with a self-hosted instance requires an Activepieces license. If you are looking for these features, contact us at [sales@activepieces.com](mailto:sales@activepieces.com).

**Benefits of Dual Licensing Repo**

* **Transparency** - Everyone can see what we are doing and contribute to the project.
* **Clarity** - Everyone can see what the difference is between the open source and commercial versions of our software.
* **Audit** - Everyone can audit our code and see what we are doing.
* **Faster Development** - We can develop faster and more efficiently.

<Tip>
  If you are still confused or have feedback, please open an issue on GitHub or send a message in the #contribution channel on Discord.
</Tip>


# Telemetry
Source: https://www.activepieces.com/docs/about/telemetry



# Why Does Activepieces need data?

As a self-hosted product, gathering usage metrics and insights can be difficult for us. However, these analytics are essential in helping us understand key behaviors and delivering a higher quality experience that meets your needs.

To ensure we can continue to improve our product, we have decided to track certain basic behaviors and metrics that are vital for understanding the usage of Activepieces.

We have implemented a minimal tracking plan and provide a detailed list of the metrics collected in a separate section.

# What Does Activepieces Collect?

We value transparency in data collection and assure you that we do not collect any personal information. The following events are currently being collected:

[Exact Code](https://github.com/activepieces/activepieces/blob/main/packages/shared/src/lib/common/telemetry.ts)

1. `flow.published`: Event fired when a flow is published
2. `signed.up`: Event fired when a user signs up
3. `flow.test`: Event fired when a flow is tested
4. `flow.created`: Event fired when a flow is created
5. `start.building`: Event fired when a user starts building
6. `demo.imported`: Event fired when a demo is imported
7. `flow.imported`: Event fired when a flow template is imported

# Opting out?

To opt out, set the environment variable `AP_TELEMETRY_ENABLED=false`


# Appearance
Source: https://www.activepieces.com/docs/admin-console/appearance



<Snippet file="enterprise-feature.mdx" />

Customize the brand by going to the **Platform Admin -> Setup -> Branding**. Here, you can customize:

* Logo / FavIcon
* Primary color
* Platform Name

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/branding.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=a1684adc19f715524214dca6a5cead7e" alt="Branding Platform" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/branding.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/branding.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=17a7d79d9f60fcc4d820afa278fa74f1 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/branding.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=a82e97a06c101be45f08d1d186a3a77a 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/branding.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=be9cfed5d8051097c2eaf7b244e27cae 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/branding.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=bde33f4aec689d05de68aa6884319be6 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/branding.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f01b364791965b2399b1fdbf2b289123 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/branding.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=1af3521ec69ccc6a09578d931a4d9a58 2500w" />

<video controls autoplay muted loop playsinline className="w-full aspect-video" src="https://cdn.activepieces.com/videos/showcase/appearance.mp4" />


# Custom Domains
Source: https://www.activepieces.com/docs/admin-console/custom-domain



<Snippet file="enterprise-feature.mdx" />

You can set up a unique domain for your platform, like app.example.com.<br />
This is also used to determine the theme and branding on the authentication pages when a user is not logged in.

**Platform Admin -> Setup -> Branding**
<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/custom-domain.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=71327690a63cdc2cd5a58fecb871f22b" alt="Manage Projects" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/custom-domain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/custom-domain.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b07ed3ec2fb1ac724c75a3b2b1fa82a7 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/custom-domain.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c2d4c63b97fb7b4174197818574ad519 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/custom-domain.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=dbe98c0050b22e67bd1184dd39e094bd 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/custom-domain.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=f91fa5b56a71c5ab091eeec21c24c224 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/custom-domain.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ab8aa9a8d2b9951c6ed42f5a65a99488 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/custom-domain.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=f97c5490949082efa795f62264d395c9 2500w" />


# Customize Emails
Source: https://www.activepieces.com/docs/admin-console/customize-emails



<Snippet file="enterprise-feature.mdx" />

You can add your own mail server to Activepieces, or override it if it's in the cloud. From the platform, all email templates are automatically whitelabeled according to the [appearance settings](./appearance).

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-smtp.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e9ec8c1dc37d7ff3d4041c6010c52c31" alt="Manage SMTP" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/manage-smtp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-smtp.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=a554f7f418b3a6f7fff01ee9278d4b6a 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-smtp.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=df990ed546ba180b7978af821e7f4f98 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-smtp.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7f8e886ba84f5b275feb138e157c5a3d 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-smtp.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=861955bda2f073e76749266cead1e76e 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-smtp.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3734672d2b5f695016335fdf3a0e47b9 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-smtp.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7046ba889c796bf13cd9f766fb8615b2 2500w" />


# Manage AI Providers
Source: https://www.activepieces.com/docs/admin-console/manage-ai-providers



Set your AI providers so your users enjoy a seamless building experience with our universal AI pieces like [Text AI](https://www.activepieces.com/pieces/text-ai).

## Manage AI Providers

You can manage the AI providers that you want to use in your flows. To do this, go to the **AI** page in the **Admin Console**.

You can define the provider's base URL and the API key.

These settings will be used for all the projects for every request to the AI provider.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=80d92caf90c116589c7ecbc7f80a9514" alt="Manage AI Providers" data-og-width="1420" width="1420" data-og-height="800" height="800" data-path="resources/screenshots/configure-ai-provider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1d94288df818cc7c1d241d5681dcbcab 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=14038529f8d565a38edd58ac89c802d9 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=894ea0d5839737c4bfd66bdaffda5e80 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0176a920881ca1d8de1c71e1e9ba758f 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=20df3793ad011b2c71ab6c1b0f01a39b 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=18d3a1c09352aad3355efe6cee91745c 2500w" />

## Configure AI Credits Limits Per Project

You can configure the token limits per project. To do this, go to the project general settings and change the **AI Credits** field to the desired value.

<Note>
  This limit is per project and is an accumulation of all the reported usage by the AI piece in the project.
  Since only the AI piece goes through the Activepieces API,
  using any other piece like the standalone OpenAI, Anthropic or Perplexity pieces will not count towards or respect this limit.
</Note>

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=3a37db4f477f8fcf4c6a7749afedbdd0" alt="Manage AI Providers" data-og-width="1420" width="1420" data-og-height="800" height="800" data-path="resources/screenshots/ai-credits-limit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=1e4619f6a62a954d9e3edc1d83a3f351 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=9339b91b24aee4f662222ed815982bd4 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=91726634f998e19818cdcea4c83b8882 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f8299e5908cde2cf4f10c04d750b64ea 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=8f255a7d9bd82ebe13e3b200932a3810 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/ai-credits-limit.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=c5b35d163e6e0487bf289a850a42df1b 2500w" />

### AI Credits Explained

AI credits are the number tasks that can be run by any of our universal AI pieces.

So if you have a flow run that contains 5 universal AI pieces steps, the AI credits consumed will be 5.


# Replace OAuth2 Apps
Source: https://www.activepieces.com/docs/admin-console/manage-oauth2



<Snippet file="enterprise-feature.mdx" />

Your project automatically uses Activepieces OAuth2 Apps as the default setting. <br />
If you prefer to use your own OAuth2 Apps, Go to **Platform Admin -> Setup -> Pieces** then choose a piece that uses OAuth2 like Google Sheets and click the open lock icon to configure your own OAuth2 app.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-oauth2.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=8ebbd16358d5bf3e58d970927516b517" alt="Manage Oauth2 apps" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/manage-oauth2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-oauth2.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d6b09e80d3bb74f7ceea91183bc790f2 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-oauth2.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e12e8e0c50387de42ed67ce151f5a910 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-oauth2.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=167e940662e51d66366f20b3d46e6979 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-oauth2.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b6f8ea7ad199309435c92491a6cc6d8b 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-oauth2.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=546eb6cb1ca0ca065d5c63949c9d9b51 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-oauth2.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=5b1b48bbeee1ecd701923383fc5985c7 2500w" />


# Manage Pieces
Source: https://www.activepieces.com/docs/admin-console/manage-pieces



<Snippet file="enterprise-feature.mdx" />

## Show Specific Pieces in Project

If you go to **Pieces Settings** in your project, you can manage which pieces you would like to be available to your users.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d8dbe5cdd7a9fead03b9ef30d4d2de6d" alt="Manage Pieces" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/manage-pieces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b433e17a00980ba9b07a673a8b86ec79 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b544c35312cd3554475ab777742ce576 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=672831ff44e56bfba9b39d5fb6340ab5 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1e1430e6b4745c24d0777b5e224bb313 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=dc7d1ed57cad8ec386db6bb713dc4a48 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0b3b9c923c6b8eb4b179607c03b91b70 2500w" />
<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces-2.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=564a5736574d05ae8e080e36545e9b54" alt="Manage Pieces" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/manage-pieces-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces-2.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=32ddda09dc1c166322544331d381f685 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces-2.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=6a9e0f2df1cd1eec59a8c1a3b68dab29 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces-2.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=86696de9743539b90a075ba5d45b416f 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces-2.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=46c74aa21964a3244dd1328e6390e234 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces-2.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=4528915c4c57a0a523fd80828f5cda31 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/manage-pieces-2.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3f9630171874a96df816369827cdbebc 2500w" />

## Install Piece

* Go to **Platform Admin -> Setup -> Pieces** and hit Install pieces.
* You can choose to install a piece from NPM or upload a tar file directly for private pieces.
* You can check the [Sharing Pieces Doc](/developers/sharing-pieces/overview) for more info.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1106164b9b77b33e96ccdcd4df789948" alt="Manage Projects" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/install-piece.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c9009ba8db60863675f21036a561f4ce 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c7ad50fd4c721848169fe6c9c2c6af0b 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=6cfedfb7edde2f9311a1af6b783520cf 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=615c3b9f24457a4384ede39ed276d50a 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=44499b6321130356ec94bc0826eb19fd 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b7cfc85def669ee351fef9150f4c3bce 2500w" />


# Managed Projects
Source: https://www.activepieces.com/docs/admin-console/manage-projects



<Snippet file="enterprise-feature.mdx" />

This feature helps you unlock these use cases:

1. Set up projects for different teams inside the company.
2. Set up projects automatically using the embedding feature for your SaaS customers.

You can **create** new projects and sets **limits** on the number of tasks for each project.


# Manage Templates
Source: https://www.activepieces.com/docs/admin-console/manage-templates



<Snippet file="enterprise-feature.mdx" />

You can create custom templates for your users within the Platform dashboard's.

<video controls autoplay muted loop playsinline className="w-full aspect-video" src="https://cdn.activepieces.com/videos/showcase/templates.mp4" />


# Overview
Source: https://www.activepieces.com/docs/admin-console/overview



<Snippet file="enterprise-feature.mdx" />

The platform is the admin panel for managing your instance. It's suitable for SaaS, Embed, or agencies that want to white-label Activepieces and offer it to their customers. With this platform, you can:

1. **Custom Branding:** Tailor the appearance of the software to align with your brand's identity by selecting your own branding colors and fonts.

2. **Projects Management:** Manage your projects, including creating, editing, and deleting projects.

3. **Piece Management:** Take full control over Activepieces pieces. You can show or hide existing pieces and create your own unique pieces to customize the platform according to your specific needs.

4. **User Authentication Management:** adding and removing users, and assigning roles to users.

5. **Template Management:** Control prebuilt templates and add your own unique templates to meet the requirements of your users.

6. **AI Provider Management:** Manage the AI providers that you want to use in your flows.


# MCP
Source: https://www.activepieces.com/docs/ai/mcp

Give AI access to your tools through Activepieces

## What is an MCP?

LLMs produce text by default, but they're evolving to be able to use tools too. Say you want to ask Claude what meetings you have tomorrow, it can happen if you give it access to your calendar.

**These tools live in an MCP Server that has a URL**. You provide your LLM (or MCP Client) with this URL so it can access your tools.

There are many [MCP clients](https://github.com/punkpeye/awesome-mcp-clients) you can use for this purpose, and the most popular ones today are Claude Desktop, Cursor and Windsurf.

**Official docs:** [https://modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction)

## MCPs on Activepieces

To use MCPs on Activepieces, we'll let you connect any of our [open source MCP tools](https://www.activepieces.com/mcp), and give you an MCP Server URL. Then, you'll configure your LLM to work with it.

## Use Activepieces MCP Server

1. **You need to run Activepieces.** It can run on our cloud or you can self-host it in your machine or infrastructure.

   ***Both options are for free, and all our MCP tools are open source.***

<CardGroup cols={2}>
  <Card title="Activepieces Cloud (Easy)" icon="cloud" color="#00FFFF" href="https://cloud.activepieces.com/sign-up">
    Use our cloud to run your MCP tools, or to just give it a test drive
  </Card>

  <Card title="Self-hosting" icon="download" color="#248fe0" href="/install/overview">
    Deploy Activepieces using Docker or one of the other methods
  </Card>
</CardGroup>

2. **Connect your tools.** Go to AI → MCP in your Activepieces Dashboard, and start connecting the tools that you want to give AI access to.

3. **Follow the instructions.** Click on your choice of MCP client (Claude Desktop, Cursor or Windsurf) and follow the instructions.

4. **Chat with your LLM with superpowers 🚀**

## Things to try out with the MCP

* Cancel all my meetings for tomorrow
* What tasks do I have to do today?
* Tweet this idea for me

And many more!


# Create Action
Source: https://www.activepieces.com/docs/developers/building-pieces/create-action



## Action Definition

Now let's create first action which fetch random ice-cream flavor.

```bash  theme={null}
npm run cli actions create
```

You will be asked three questions to define your new piece:

1. `Piece Folder Name`: This is the name associated with the folder where the action resides. It helps organize and categorize actions within the piece.
2. `Action Display Name`: The name users see in the interface, conveying the action's purpose clearly.
3. `Action Description`: A brief, informative text in the UI, guiding users about the action's function and purpose.
   Next, Let's create the action file:

**Example:**

```bash  theme={null}
npm run cli actions create

? Enter the piece folder name : gelato
? Enter the action display name : get icecream flavor
? Enter the action description : fetches random icecream flavor.
```

This will create a new TypeScript file named `get-icecream-flavor.ts` in the `packages/pieces/community/gelato/src/lib/actions` directory.

Inside this file, paste the following code:

```typescript  theme={null}
import {
  createAction,
  Property,
  PieceAuth,
} from '@activepieces/pieces-framework';
import { httpClient, HttpMethod } from '@activepieces/pieces-common';
import { gelatoAuth } from '../..';

export const getIcecreamFlavor = createAction({
  name: 'get_icecream_flavor', // Must be a unique across the piece, this shouldn't be changed.
  auth: gelatoAuth,
  displayName: 'Get Icecream Flavor',
  description: 'Fetches random icecream flavor',
  props: {},
  async run(context) {
    const res = await httpClient.sendRequest<string[]>({
      method: HttpMethod.GET,
      url: 'https://cloud.activepieces.com/api/v1/webhooks/RGjv57ex3RAHOgs0YK6Ja/sync',
      headers: {
        Authorization: context.auth, // Pass API key in headers
      },
    });
    return res.body;
  },
});
```

The createAction function takes an object with several properties, including the `name`, `displayName`, `description`, `props`, and `run` function of the action.

The `name` property is a unique identifier for the action. The `displayName` and `description` properties are used to provide a human-readable name and description for the action.

The `props` property is an object that defines the properties that the action requires from the user. In this case, the action doesn't require any properties.

The `run` function is the function that is called when the action is executed. It takes a single argument, context, which contains the values of the action's properties.

The `run` function utilizes the httpClient.sendRequest function to make a GET request, fetching a random ice cream flavor. It incorporates API key authentication in the request headers. Finally, it returns the response body.

## Expose The Definition

To make the action readable by Activepieces, add it to the array of actions in the piece definition.

```typescript  theme={null}
import { createPiece } from '@activepieces/pieces-framework';
// Don't forget to add the following import.
import { getIcecreamFlavor } from './lib/actions/get-icecream-flavor';

export const gelato = createPiece({
  displayName: 'Gelato',
  logoUrl: 'https://cdn.activepieces.com/pieces/gelato.png',
  authors: [],
  auth: gelatoAuth,
  // Add the action here.
  actions: [getIcecreamFlavor], // <--------
  triggers: [],
});
```

# Testing

By default, the development setup only builds specific components. Open the file `packages/server/api/.env` and include "gelato" in the `AP_DEV_PIECES`.

For more details, check out the [Piece Development](../development-setup/getting-started) section.

Once you edit the environment variable, restart the backend. The piece will be rebuilt. After this process, you'll need to **refresh** the frontend to see the changes.

<Tip>
  If the build fails, try debugging by running `npx nx run-many -t build --projects=gelato`.
  It will display any errors in your code.
</Tip>

To test the action, use the flow builder in Activepieces. It should function as shown in the screenshot.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-action.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9d8d8ac84393a2940f18940bb98e2d51" alt="Gelato Action" data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="resources/screenshots/gelato-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-action.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9a7e10b771fad182dc9f6035cb8282de 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-action.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=67cf9aa6312c95f8c18222ce488f70d2 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-action.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7064d346404be788450611e815206de6 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-action.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=559f3e935a86f7cf1dafbb02dbb743db 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-action.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=de79af41125ec16aee55d175e99c64de 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-action.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=5fb31597729b477e3084acf9dca47080 2500w" />


# Create Trigger
Source: https://www.activepieces.com/docs/developers/building-pieces/create-trigger



This tutorial will guide you through the process of creating trigger for a Gelato piece that fetches new icecream flavor.

## Trigger Definition

To create trigger run the following command,

```bash  theme={null}
npm run cli triggers create
```

1. `Piece Folder Name`: This is the name associated with the folder where the trigger resides. It helps organize and categorize triggers within the piece.
2. `Trigger Display Name`: The name users see in the interface, conveying the trigger's purpose clearly.
3. `Trigger Description`: A brief, informative text in the UI, guiding users about the trigger's function and purpose.
4. `Trigger Technique`: Specifies the trigger type - either [polling](../piece-reference/triggers/polling-trigger) or [webhook](../piece-reference/triggers/webhook-trigger).

**Example:**

```bash  theme={null}
npm run cli triggers create

? Enter the piece folder name : gelato
? Enter the trigger display name : new flavor created
? Enter the trigger description : triggers when a new icecream flavor is created.
? Select the trigger technique: polling
```

This will create a new TypeScript file at `packages/pieces/community/gelato/src/lib/triggers` named `new-flavor-created.ts`.

Inside this file, paste the following code:

```ts  theme={null}
import { gelatoAuth } from '../../';
import {
  DedupeStrategy,
  HttpMethod,
  HttpRequest,
  Polling,
  httpClient,
  pollingHelper,
} from '@activepieces/pieces-common';
import {
  PiecePropValueSchema,
  TriggerStrategy,
  createTrigger,
} from '@activepieces/pieces-framework';
import dayjs from 'dayjs';

const polling: Polling<
  PiecePropValueSchema<typeof gelatoAuth>,
  Record<string, never>
> = {
  strategy: DedupeStrategy.TIMEBASED,
  items: async ({ auth, propsValue, lastFetchEpochMS }) => {
    const request: HttpRequest = {
      method: HttpMethod.GET,
      url: 'https://cloud.activepieces.com/api/v1/webhooks/aHlEaNLc6vcF1nY2XJ2ed/sync',
      headers: {
        authorization: auth,
      },
    };
    const res = await httpClient.sendRequest(request);
    return res.body['flavors'].map((flavor: string) => ({
      epochMilliSeconds: dayjs().valueOf(),
      data: flavor,
    }));
  },
};

export const newFlavorCreated = createTrigger({
  auth: gelatoAuth,
  name: 'newFlavorCreated',
  displayName: 'new flavor created',
  description: 'triggers when a new icecream flavor is created.',
  props: {},
  sampleData: {},
  type: TriggerStrategy.POLLING,
  async test(context) {
    return await pollingHelper.test(polling, context);
  },
  async onEnable(context) {
    const { store, auth, propsValue } = context;
    await pollingHelper.onEnable(polling, { store, auth, propsValue });
  },

  async onDisable(context) {
    const { store, auth, propsValue } = context;
    await pollingHelper.onDisable(polling, { store, auth, propsValue });
  },

  async run(context) {
    return await pollingHelper.poll(polling, context);
  },
});
```

The way polling triggers usually work is as follows:

`Run`:The run method executes every 5 minutes, fetching data from the endpoint within a specified timestamp range or continuing until it identifies the last item ID. It then returns the new items as an array. In this example, the httpClient.sendRequest method is utilized to retrieve new flavors, which are subsequently stored in the store along with a timestamp.

## Expose The Definition

To make the trigger readable by Activepieces, add it to the array of triggers in the piece definition.

```typescript  theme={null}
import { createPiece } from '@activepieces/pieces-framework';
import { getIcecreamFlavor } from './lib/actions/get-icecream-flavor';
// Don't forget to add the following import.
import { newFlavorCreated } from './lib/triggers/new-flavor-created';

export const gelato = createPiece({
  displayName: 'Gelato Tutorial',
  logoUrl: 'https://cdn.activepieces.com/pieces/gelato.png',
  authors: [],
  auth: gelatoAuth,
  actions: [getIcecreamFlavor],
  // Add the trigger here.
  triggers: [newFlavorCreated], // <--------
});
```

# Testing

By default, the development setup only builds specific components. Open the file `packages/server/api/.env` and include "gelato" in the `AP_DEV_PIECES`.

For more details, check out the [Piece Development](../development-setup/getting-started) section.

Once you edit the environment variable, restart the backend. The piece will be rebuilt. After this process, you'll need to **refresh** the frontend to see the changes.

To test the trigger, use the load sample data from flow builder in Activepieces. It should function as shown in the screenshot.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0ac29f0025296b3ecc2111709a2b9a33" alt="Gelato Action" data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="resources/screenshots/gelato-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=eca339aa40eb13c77c0523a69a53e98a 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=904295025aa163dec6da607b7c8a2b50 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=797d6f9dd13b1c2c4bf48f9e7b074c89 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9faad30e7502ed152a76af3085047433 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=21ae16d188441fee36496bf699763488 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/gelato-trigger.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=462aa47d42e057d2f34b3872a83cc35b 2500w" />


# Overview
Source: https://www.activepieces.com/docs/developers/building-pieces/overview

This section helps developers build and contribute pieces.

Building pieces is fun and important; it allows you to customize Activepieces for your own needs.

<Tip>
  We love contributions! In fact, most of the pieces are contributed by the community. Feel free to open a pull request.
</Tip>

<Tip>
  **Friendly Tip:**
  For the fastest support, we recommend joining our Discord community. We are dedicated to addressing every question and concern raised there.
</Tip>

<CardGroup cols={2}>
  <Card title="Code with TypeScript" icon="code">
    Build pieces using TypeScript for a more powerful and flexible development process.
  </Card>

  <Card title="Hot Reloading" icon="cloud-bolt">
    See your changes in the browser within 7 seconds.
  </Card>

  <Card title="Open Source" icon="earth-americas">
    Work within the open-source environment, explore, and contribute to other pieces.
  </Card>

  <Card title="Community Support" icon="people">
    Join our large community, where you can ask questions, share ideas, and develop alongside others.
  </Card>

  <Card title="Universal AI SDK" icon="brain">
    Use the Universal SDK to quickly build AI-powered pieces that support multiple AI providers.
  </Card>
</CardGroup>


# Add Piece Authentication
Source: https://www.activepieces.com/docs/developers/building-pieces/piece-authentication



### Piece Authentication

Activepieces supports multiple forms of authentication, you can check those forms [here](../piece-reference/authentication)

Now, let's establish authentication for this piece, which necessitates the inclusion of an API Key in the headers.

Modify `src/index.ts` file to add authentication,

```ts  theme={null}
import { PieceAuth, createPiece } from '@activepieces/pieces-framework';

export const gelatoAuth = PieceAuth.SecretText({
  displayName: 'API Key',
  required: true,
  description: 'Please use **test-key** as value for API Key',
});

export const gelato = createPiece({
  displayName: 'Gelato',
  logoUrl: 'https://cdn.activepieces.com/pieces/gelato.png',
  auth: gelatoAuth,
  authors: [],
  actions: [],
  triggers: [],
});
```

<Note>
  Use the value **test-key** as the API key when testing actions or triggers for
  Gelato.
</Note>


# Create Piece Definition
Source: https://www.activepieces.com/docs/developers/building-pieces/piece-definition



This tutorial will guide you through the process of creating a Gelato piece with an action that fetches random icecream flavor and trigger that fetches new icecream flavor created. It assumes that you are familiar with the following:

* [Activepieces Local development](../development-setup/local) Or [GitHub Codespaces](../development-setup/codespaces).
* TypeScript syntax.

## Piece Definition

To get started, let's generate a new piece for Gelato

```bash  theme={null}
npm run cli pieces create
```

You will be asked three questions to define your new piece:

1. `Piece Name`: Specify a name for your piece. This name uniquely identifies your piece within the ActivePieces ecosystem.
2. `Package Name`: Optionally, you can enter a name for the npm package associated with your piece. If left blank, the default name will be used.
3. `Piece Type`: Choose the piece type based on your intention. It can be either "custom" if it's a tailored solution for your needs, or "community" if it's designed to be shared and used by the broader community.

**Example:**

```bash  theme={null}
npm run cli pieces create

? Enter the piece name: gelato
? Enter the package name: @activepieces/piece-gelato
? Select the piece type: community
```

The piece will be generated at `packages/pieces/community/gelato/`,
the `src/index.ts` file should contain the following code

```ts  theme={null}
import { PieceAuth, createPiece } from '@activepieces/pieces-framework';

export const gelato = createPiece({
  displayName: 'Gelato',
  logoUrl: 'https://cdn.activepieces.com/pieces/gelato.png',
  auth: PieceAuth.None(),
  authors: [],
  actions: [],
  triggers: [],
});
```


# Fork Repository
Source: https://www.activepieces.com/docs/developers/building-pieces/setup-fork



To start building pieces, we need to fork the repository that contains the framework library and the development environment. Later, we will publish these pieces as `npm` artifacts.

Follow these steps to fork the repository:

1. Go to the repository page at [https://github.com/activepieces/activepieces](https://github.com/activepieces/activepieces).
2. Click the `Fork` button located in the top right corner of the page.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/fork-repository.jpg?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=013243ea91cbc40b0235037959836604" alt="Fork Repository" data-og-width="1320" width="1320" data-og-height="248" height="248" data-path="resources/screenshots/fork-repository.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/fork-repository.jpg?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=a95b6ef9d11a7e303c2ca3f27e4f1b06 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/fork-repository.jpg?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=a58a580aef73487f2025ddf8f6641df1 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/fork-repository.jpg?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=540701c8d9775e6d317b1e7784302222 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/fork-repository.jpg?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9bb72b7cc3607d740c3f62b657f9dd7a 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/fork-repository.jpg?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=235de7ff957d3633ed25254df6ce5d2d 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/fork-repository.jpg?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=2fc0ee213e1a8a02e7de4a5379a54009 2500w" />

<Tip>
  If you are an enterprise customer and want to use the private pieces feature, you can refer to the tutorial on how to set up a [private fork](../misc/private-fork).
</Tip>


# Start Building
Source: https://www.activepieces.com/docs/developers/building-pieces/start-building



This section guides you in creating a Gelato piece, from setting up your development environment to contributing the piece. By the end of this tutorial, you will have a piece with an action that fetches a random ice cream flavor and a trigger that fetches newly created ice cream flavors.

<Info>
  These are the next sections. In each step, we will do one small thing. This tutorial should take around 30 minutes.
</Info>

## Steps Overview

<Steps>
  <Step title="Fork Repository" icon="code-branch">
    Fork the repository to create your own copy of the codebase.
  </Step>

  <Step title="Setup Development Environment" icon="code">
    Set up your development environment with the necessary tools and dependencies.
  </Step>

  <Step title="Create Piece Definition" icon="gear">
    Define the structure and behavior of your Gelato piece.
  </Step>

  <Step title="Add Piece Authentication" icon="lock">
    Implement authentication mechanisms for your Gelato piece.
  </Step>

  <Step title="Create Action" icon="ice-cream">
    Create an action that fetches a random ice cream flavor.
  </Step>

  <Step title="Create Trigger" icon="ice-cream">
    Create a trigger that fetches newly created ice cream flavors.
  </Step>

  <Step title="Sharing Pieces" icon="share">
    Share your Gelato piece with others.
  </Step>
</Steps>

<Card title="Contribution" icon="gift" iconType="duotone" color="#6e41e2">
  Contribute a piece to our repo and receive +1,400 tasks/month on [Activepieces Cloud](https://cloud.activepieces.com).
</Card>


# GitHub Codespaces
Source: https://www.activepieces.com/docs/developers/development-setup/codespaces



GitHub Codespaces is a cloud development platform that enables developers to write, run, and debug code directly in their browsers, seamlessly integrated with GitHub.

### Steps to setup Codespaces

1. Go to [Activepieces repo](https://github.com/activepieces/activepieces).

2. Click Code `<>`, then under codespaces click create codespace on main.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=2228948ff3bf64691d9ff82072da37b2" alt="Create Codespace" data-og-width="1383" width="1383" data-og-height="713" height="713" data-path="resources/screenshots/development-setup_codespaces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=a4ad0df90c9bae41b9dc1037c74098b8 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e538e737312e98184bdd9d0c1ee76a41 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=189866428f49bd5cf73b93e6355e1d1c 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0e1257933c43de7b1837306618a7f275 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=863628159653952542cf694a26f9cd25 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/development-setup_codespaces.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=8e09af5ec8413cc2e059eaa425bedebd 2500w" />

<Note>
  By default, the development setup only builds specific pieces.Open the file
  `packages/server/api/.env` and add comma-separated list of pieces to make
  available.

  For more details, check out the [Piece Development](/developers/development-setup/getting-started) section.
</Note>

3. Open the terminal and run `npm start`

4. Access the frontend URL by opening port 4200 and signing in with these details:

Email: `dev@ap.com`
Password: `12345678`


# Dev Containers
Source: https://www.activepieces.com/docs/developers/development-setup/dev-container



## Using Dev Containers in Visual Studio Code

The project includes a dev container configuration that allows you to use Visual Studio Code's [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension to develop the project in a consistent environment. This can be especially helpful if you are new to the project or if you have a different environment setup on your local machine.

## Prerequisites

Before you can use the dev container, you will need to install the following:

* [Visual Studio Code](https://code.visualstudio.com/).
* The [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension for Visual Studio Code.
* [Docker](https://www.docker.com/).

## Using the Dev Container

To use the dev container for the Activepieces project, follow these steps:

1. Clone the Activepieces repository to your local machine.
2. Open the project in Visual Studio Code.
3. Press `Ctrl+Shift+P` and type `> Dev Containers: Reopen in Container`.
4. Run `npm start`.
5. The backend will run at `localhost:3000` and the frontend will run at `localhost:4200`.

<Note>
  By default, the development setup only builds specific pieces.Open the file
  `packages/server/api/.env` and add comma-separated list of pieces to make
  available.

  For more details, check out the [Piece Development](/developers/development-setup/getting-started) section.
</Note>

The login credentials are:\
Email: `dev@ap.com`
Password: `12345678`

## Exiting the Dev Container

To exit the dev container and return to your local environment, follow these steps:

1. In the bottom left corner of Visual Studio Code, click the `Remote-Containers: Reopen folder locally` button.
2. Visual Studio Code will close the connection to the dev container and reopen the project in your local environment.

## Troubleshoot

One of the best trouble shoot after an error occur is to reset the dev container.

1. Exit the dev container
2. Run the following
   ```sh  theme={null}
   sh tools/reset-dev.sh
   ```
3. Rebuild the dev container from above steps


# Getting Started
Source: https://www.activepieces.com/docs/developers/development-setup/getting-started



## Development Setup

To set up the development environment, you can choose one of the following methods:

* **Codespaces**: This is the quickest way to set up the development environment. Follow the [Codespaces](./codespaces) guide.
* **Local Environment**: It is recommended for local development. Follow the [Local Environment](./local) guide.
* **Dev Container**: This method is suitable for remote development on another machine. Follow the [Dev Container](./dev-container) guide.

## Pieces Development

To avoid making the dev environment slow, not all pieces are functional during development at first. By default, only these pieces are functional at first, as specified in `AP_DEV_PIECES`.

[https://github.com/activepieces/activepieces/blob/main/packages/server/api/.env#L4](https://github.com/activepieces/activepieces/blob/main/packages/server/api/.env#L4)

To override the default list available at first, define an `AP_DEV_PIECES` environment variable with a comma-separated list of pieces to make available. For example, to make `google-sheets` and `cal-com` available, you can use:

```sh  theme={null}
AP_DEV_PIECES=google-sheets,cal-com npm start
```


# Local Dev Environment
Source: https://www.activepieces.com/docs/developers/development-setup/local



## Prerequisites

* Node.js v18+
* npm v9+

## Instructions

1. Setup the environment

```bash  theme={null}
node tools/setup-dev.js
```

2. Start the environment

This command will start activepieces with sqlite3 and in memory queue.

```bash  theme={null}
npm start
```

<Note>
  By default, the development setup only builds specific pieces.Open the file
  `packages/server/api/.env` and add comma-separated list of pieces to make
  available.

  For more details, check out the [Piece Development](/developers/development-setup/getting-started) section.
</Note>

3. Go to ***localhost:4200*** on your web browser and sign in with these details:

Email: `dev@ap.com`
Password: `12345678`


# Build Custom Pieces
Source: https://www.activepieces.com/docs/developers/misc/build-piece



You can use the CLI to build custom pieces for the platform. This process compiles the pieces and exports them as a `.tgz` packed archive.

### How It Works

The CLI scans the `packages/pieces/` directory for the specified piece. It checks the **name** in the `package.json` file. If the piece is found, it builds and packages it into a `.tgz` archive.

### Usage

To build a piece, follow these steps:

1. Ensure you have the CLI installed by cloning the repository.
2. Run the following command:

```bash  theme={null}
npm run build-piece
```

You will be prompted to enter the name of the piece you want to build. For example:

```bash  theme={null}
? Enter the piece folder name : google-drive
```

The CLI will build the piece and you will be given the path to the archive. For example:

```bash  theme={null}
Piece 'google-drive' built and packed successfully at dist/packages/pieces/community/google-drive
```

You may also build the piece non-interactively by passing the piece name as an argument.  For example:

```bash  theme={null}
npm run build-piece google-drive
```


# Create New AI Provider
Source: https://www.activepieces.com/docs/developers/misc/create-new-ai-provider



ActivePieces currently supports the following AI providers:

* OpenAI
* Anthropic

To create a new AI provider, you need to follow these steps:

## Implement the AI Interface

Create a new factory that returns an instance of the `AI` interface in the `packages/pieces/community/common/src/lib/ai/providers/your-ai-provider.ts` file.

```typescript  theme={null}
export const yourAiProvider = ({
  serverUrl,
  engineToken,
}: { serverUrl: string, engineToken: string }): AI<YourAiProviderSDK> => {
  const impl = new YourAiProviderSDK(serverUrl, engineToken);
  return {
    provider: "YOUR_AI_PROVIDER" as const,
    chat: {
      text: async (params) => {
        try {
          const response = await impl.chat.text(params);
          return response;
        } catch (e: any) {
          if (e?.error?.error) {
            throw e.error.error;
          }
          throw e;
        }
      }
    },
  };
};
```

## Register the AI Provider

Add the new AI provider to the `AiProviders` enum in `packages/pieces/community/common/src/lib/ai/providers/index.ts` file.

```diff  theme={null}
export const AiProviders = [
+  {
+    logoUrl: 'https://cdn.activepieces.com/pieces/openai.png',
+    defaultBaseUrl: 'https://api.your-ai-provider.com',
+    label: 'Your AI Provider' as const,
+    value: 'your-ai-provider' as const,
+    models: [
+      { label: 'model-1', value: 'model-1' },
+      { label: 'model-2', value: 'model-2' },
+      { label: 'model-3', value: 'model-3' },
+    ],
+    factory: yourAiProvider,
+  },
...
]
```

## Define Authentication Header

Now we need to tell ActivePieces how to authenticate to your AI provider. You can do this by adding an `auth` property to the `AiProvider` object.

The `auth` property is an object that defines the authentication mechanism for your AI provider. It consists of two properties: `name` and `mapper`. The `name` property specifies the name of the header that will be used to authenticate with your AI provider, and the `mapper` property defines a function that maps the value of the header to the format that your AI provider expects.

Here's an example of how to define the authentication header for a bearer token:

```diff  theme={null}
export const AiProviders = [
  {
    logoUrl: 'https://cdn.activepieces.com/pieces/openai.png',
    defaultBaseUrl: 'https://api.your-ai-provider.com',
    label: 'Your AI Provider' as const,
    value: 'your-ai-provider' as const,
    models: [
      { label: 'model-1', value: 'model-1' },
      { label: 'model-2', value: 'model-2' },
      { label: 'model-3', value: 'model-3' },
    ],
+    auth: authHeader({ bearer: true }), // or authHeader({ name: 'x-api-key', bearer: false })
    factory: yourAiProvider,
  },
...
]
```

## Test the AI Provider

To test the AI provider, you can use a **universal AI** piece in a flow. Follow these steps:

* Add the required headers from the admin console for the newly created AI provider. These headers will be used to authenticate the requests to the AI provider.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=80d92caf90c116589c7ecbc7f80a9514" alt="Configure AI Provider" data-og-width="1420" width="1420" data-og-height="800" height="800" data-path="resources/screenshots/configure-ai-provider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1d94288df818cc7c1d241d5681dcbcab 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=14038529f8d565a38edd58ac89c802d9 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=894ea0d5839737c4bfd66bdaffda5e80 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0176a920881ca1d8de1c71e1e9ba758f 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=20df3793ad011b2c71ab6c1b0f01a39b 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/configure-ai-provider.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=18d3a1c09352aad3355efe6cee91745c 2500w" />

* Create a flow that uses our **universal AI** pieces. And select **"Your AI Provider"** as the AI provider in the **Ask AI** action settings.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=a8a84f27f69dd930bee70e90dd3cf04c" alt="Configure AI Provider" data-og-width="396" width="396" data-og-height="346" height="346" data-path="resources/screenshots/use-ai-provider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0d5aa117ae018abf79c21b20c272e1ba 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ba68de87edb99ea946286144dc0156c5 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=45b38c46cfb36795aa94617cdef23f82 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e261625b74c3ffff781bfa91f61257e5 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=754f91e9bfc7839e70ced50c821d960c 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/use-ai-provider.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=70c00d59a33ae118191072cdfbdd902d 2500w" />


# Custom Pieces CI/CD
Source: https://www.activepieces.com/docs/developers/misc/pieces-ci-cd



You can use the CLI to sync custom pieces. There is no need to rebuild the Docker image as they are loaded directly from npm.

### How It Works

Use the CLI to sync items from `packages/pieces/custom/` to instances. In production, Activepieces acts as an npm registry, storing all piece versions.

The CLI scans the directory for `package.json` files, checking the **name** and **version** of each piece. If a piece isn't uploaded, it packages and uploads it via the API.

### Usage

To use the CLI, follow these steps:

1. Generate an API Key from the Admin Interface. Go to Settings and generate the API Key.
2. Install the CLI by cloning the repository.
3. Run the following command, replacing `API_KEY` with your generated API Key and `INSTANCE_URL` with your instance URL:

```bash  theme={null}
AP_API_KEY=your_api_key_here npm run sync-pieces -- --apiUrl https://INSTANCE_URL/api
```

### Developer Workflow

1. Developers create and modify the pieces offline.
2. Increment the piece version in their corresponding `package.json`. For more information, refer to the [piece versioning](../../developers/piece-reference/piece-versioning) documentation.
3. Open a pull request towards the main branch.
4. Once the pull request is merged to the main branch, manually run the CLI or use a GitHub/GitLab Action to trigger the synchronization process.

### GitHub Action

```yaml  theme={null}
name: Sync Custom Pieces

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  sync-pieces:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Check out the repository code with full history
      - name: Check out repository code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      # Step 2: Cache Node.js dependencies
      - name: Cache Node.js dependencies
        uses: actions/cache@v3
        with:
          path: ~/.npm
          key: npm-${{ hashFiles('package-lock.json') }}
          restore-keys: |
            npm-

      # Step 3: Set up Node.js
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20' # Use Node.js version 20
          cache: 'npm'

      # Step 4: Install dependencies using npm ci
      - name: Install dependencies
        run: npm ci --ignore-scripts

      # Step 6: Sync Custom Pieces
      - name: Sync Custom Pieces
        env:
          AP_API_KEY: ${{ secrets.AP_API_KEY }}
        run: npm run sync-pieces -- --apiUrl ${{ secrets.INSTANCE_URL }}/api

```


# Setup Private Fork
Source: https://www.activepieces.com/docs/developers/misc/private-fork



<Tip>
  **Friendly Tip #1:** If you want to experiment, you can fork or clone the public repository.
</Tip>

<Tip>
  For private piece installation, you will need the paid edition. However, you can still develop pieces, contribute them back, **OR** publish them to the public npm registry and use them in your own instance or project.
</Tip>

## Create a Private Fork (Private Pieces)

By following these steps, you can create a private fork on GitHub, GitLab or another platform and configure the "activepieces" repository as the upstream source, allowing you to incorporate changes from the "activepieces" repository.

1. **Clone the Repository:**

Begin by creating a bare clone of the repository. Remember that this is a temporary step and will be deleted later.

```bash  theme={null}
git clone --bare git@github.com:activepieces/activepieces.git
```

2. **Create a Private Git Repository**

Generate a new private repository on GitHub or your chosen platform. When initializing the new repository, do not include a README, license, or gitignore files. This precaution is essential to avoid merge conflicts when synchronizing your fork with the original repository.

3. **Mirror-Push to the Private Repository:**

Mirror-push the bare clone you created earlier to your newly created "activepieces" repository. Make sure to replace `<your_username>` in the URL below with your actual GitHub username.

```bash  theme={null}
cd activepieces.git
git push --mirror git@github.com:<your_username>/activepieces.git
```

4. **Remove the Temporary Local Repository:**

```bash  theme={null}
cd ..
rm -rf activepieces.git
```

5. **Clone Your Private Repository:**

Now, you can clone your "activepieces" repository onto your local machine into your desired directory.

```bash  theme={null}
cd ~/path/to/directory
git clone git@github.com:<your_username>/activepieces.git
```

6. **Add the Original Repository as a Remote:**

If desired, you can add the original repository as a remote to fetch potential future changes. However, remember to disable push operations for this remote, as you are not permitted to push changes to it.

```bash  theme={null}
git remote add upstream git@github.com:activepieces/activepieces.git
git remote set-url --push upstream DISABLE
```

You can view a list of all your remotes using `git remote -v`. It should resemble the following:

```
origin	git@github.com:<your_username>/activepieces.git (fetch)
origin	git@github.com:<your_username>/activepieces.git (push)
upstream	git@github.com:activepieces/activepieces.git (fetch)
upstream	DISABLE (push)
```

> When pushing changes, always use `git push origin`.

### Sync Your Fork

To retrieve changes from the "upstream" repository, fetch the remote and rebase your work on top of it.

```bash  theme={null}
git fetch upstream
git merge upstream/main
```

Conflict resolution should not be necessary since you've only added pieces to your repository.


# Publish Custom Pieces
Source: https://www.activepieces.com/docs/developers/misc/publish-piece



You can use the CLI to publish custom pieces to the platform. This process packages the pieces and uploads them to the specified API endpoint.

### How It Works

The CLI scans the `packages/pieces/` directory for the specified piece. It checks the **name** and **version** in the `package.json` file. If the piece is not already published, it builds, packages, and uploads it to the platform using the API.

### Usage

To publish a piece, follow these steps:

1. Ensure you have an API Key. Generate it from the Admin Interface by navigating to Settings.
2. Install the CLI by cloning the repository.
3. Run the following command:

```bash  theme={null}
npm run publish-piece-to-api
```

4. You will be asked three questions to publish your piece:

* `Piece Folder Name`: This is the name associated with the folder where the action resides. It helps organize and categorize actions within the piece.

* `API URL`: This is the URL of the API endpoint where the piece will be published (ex: [https://cloud.activepieces.com/api](https://cloud.activepieces.com/api)).

* `API Key Source`: This is the source of the API key. It can be either `Env Variable (AP_API_KEY)` or `Manually`.

In case you choose `Env Variable (AP_API_KEY)`, the CLI will use the API key from the `.env` file in the `packages/server/api` directory.

In case you choose `Manually`, you will be asked to enter the API key.

Examples:

```bash  theme={null}
npm run publish-piece-to-api

? Enter the piece folder name : google-drive
? Enter the API URL : https://cloud.activepieces.com/api
? Enter the API Key Source : Env Variable (AP_API_KEY)

```

```bash  theme={null}
npm run publish-piece-to-api

? Enter the piece folder name : google-drive
? Enter the API URL : https://cloud.activepieces.com/api
? Enter the API Key Source : Manually
? Enter the API Key : ap_1234567890abcdef1234567890abcdef

```


# AI SDK & Providers
Source: https://www.activepieces.com/docs/developers/piece-reference/ai-providers

The AI Toolkit to build AI pieces tailored for specific use cases that work with many AI providers using the AI SDK

**What it provides:**

* 🔐 **Centralized Credentials Management**: Admin manages credentials, end users use without hassle.
* 🌐 **Support for Multiple AI Providers**: OpenAI, Anthropic, and many open-source models.
* 💬 **Support for Various AI Capabilities**: Chat, Image, Agents, and more.

## Using the AI SDK

Activepieces integrates with the [AI SDK](https://ai-sdk.dev/) to provide a unified interface for calling LLMs across multiple AI providers. Here's an example on how to use the AI SDK's `generateText` function to call an LLM in your actions.

```typescript  theme={null}
import { SUPPORTED_AI_PROVIDERS, createAIModel, aiProps } from '@activepieces/common-ai';
import { createAction, Property } from '@activepieces/pieces-framework';
import { LanguageModel, generateText } from 'ai';

export const askAI = createAction({
  name: 'askAi',
  displayName: 'Ask AI',
  description: 'Generate text using AI providers',
  props: {
    // AI provider selection (OpenAI, Anthropic, etc.)
    provider: aiProps({ modelType: 'language' }).provider,
    // Model selection within the chosen provider
    model: aiProps({ modelType: 'language' }).model,
    prompt: Property.LongText({
      displayName: 'Prompt',
      required: true,
    }),
    creativity: Property.Number({
      displayName: 'Creativity',
      required: false,
      defaultValue: 100,
      description: 'Controls the creativity of the AI response (0-100)',
    }),
    maxTokens: Property.Number({
      displayName: 'Max Tokens',
      required: false,
      defaultValue: 2000,
    }),
  },
  async run(context) {
    const providerName = context.propsValue.provider as string;
    const modelInstance = context.propsValue.model as LanguageModel;

    // The `createAIModel` function creates a standardized AI model instance compatible with the AI SDK:
    const baseURL = `${context.server.apiUrl}v1/ai-providers/proxy/${providerName}`;
    const engineToken = context.server.token;
    const provider = createAIModel({
      providerName,           // Provider name (e.g., 'openai', 'anthropic')
      modelInstance,          // Model instance with configuration
      engineToken,            // Authentication token
      baseURL,               // Proxy URL for API requests
    });

    // Generate text using the AI SDK
    const response = await generateText({
      model: provider,                                        // AI provider instance
      messages: [
        {
          role: 'user',
          content: context.propsValue.prompt,
        },
      ],
      maxTokens: context.propsValue.maxTokens,               // Limit response length
      temperature: (context.propsValue.creativity ?? 100) / 100, // Control randomness (0-1)
      headers: {
        'Authorization': `Bearer ${engineToken}`,            // Required for proxy authentication
      },
    });

    return response.text ?? '';
  },
});
```

## AI Properties Helper

Use `aiProps` to create consistent AI-related properties:

```typescript  theme={null}
import { aiProps } from '@activepieces/ai-common';

// For language models (text generation)
props: {
  provider: aiProps({ modelType: 'language' }).provider,
  model: aiProps({ modelType: 'language' }).model,
}

// For image models (image generation)
props: {
  provider: aiProps({ modelType: 'image' }).provider,
  model: aiProps({ modelType: 'image' }).model,
  advancedOptions: aiProps({ modelType: 'image' }).advancedOptions,
}

// For function calling support
props: {
  provider: aiProps({ modelType: 'language', functionCalling: true }).provider,
  model: aiProps({ modelType: 'language', functionCalling: true }).model,
}
```

### Advanced Options

The `aiProps` helper includes an `advancedOptions` property that provides provider-specific configuration options. These options are dynamically generated based on the selected provider and model.

To add advanced options for your new provider, update the `advancedOptions` property in `packages/pieces/community/common/src/lib/ai/index.ts`:

```typescript  theme={null}
// In packages/pieces/community/common/src/lib/ai/index.ts
advancedOptions: Property.DynamicProperties({
    displayName: 'Advanced Options',
    required: false,
    refreshers: ['provider', 'model'],
    props: async (propsValue): Promise<InputPropertyMap> => {
        const provider = propsValue['provider'] as unknown as string;

        const providerMetadata = SUPPORTED_AI_PROVIDERS.find(p => p.provider === provider);
        if (isNil(providerMetadata)) {
            return {};
        }

        if (modelType === 'image') {
            // Existing OpenAI options
            if (provider === 'openai') {
                return {
                    quality: Property.StaticDropdown({
                        options: {
                            options: [
                                { label: 'Standard', value: 'standard' },
                                { label: 'HD', value: 'hd' },
                            ],
                            disabled: false,
                            placeholder: 'Select Image Quality',
                        },
                        defaultValue: 'standard',
                        description: 'Standard images are less detailed and faster to generate.',
                        displayName: 'Image Quality',
                        required: true,
                    }),
                };
            }

        return {};
    },
})
```

The advanced options automatically update when users change their provider or model selection, ensuring only relevant options are shown.

## Adding a New AI Provider

To add support for a new AI provider, you need to update several files in the Activepieces codebase. Here's a complete guide:

Before starting, check the [Vercel AI SDK Providers](https://ai-sdk.dev/providers/ai-sdk-providers) documentation to see all available providers and their capabilities.

### 1. Install Required Dependencies

First, add the AI SDK for your provider to the project dependencies:

```bash  theme={null}
npm install @ai-sdk/openai
```

### 2. Update SUPPORTED\_AI\_PROVIDERS Array

First, add your new provider to the `SUPPORTED_AI_PROVIDERS` array in `packages/ai-providers-shared/src/lib/supported-ai-providers.ts`:

```typescript  theme={null}
import { openai } from '@ai-sdk/openai' // Import the OpenAI SDK

export const SUPPORTED_AI_PROVIDERS: SupportedAIProvider[] = [
  // ... existing providers
  {
    provider: 'openai',                                    // Unique provider identifier
    baseUrl: 'https://api.openai.com',                    // OpenAI's API base URL
    displayName: 'OpenAI',                                // Display name in UI
    markdown: `Follow these instructions to get your OpenAI API Key:

1. Visit: https://platform.openai.com/account/api-keys
2. Create a new API key for Activepieces integration.
3. Add your credit card and upgrade to paid plan to avoid rate limits.
`,                                                        // Instructions for users
    logoUrl: 'https://cdn.activepieces.com/pieces/openai.png', // OpenAI logo
    auth: {
      headerName: 'Authorization',                        // HTTP header name for auth
      bearer: true,                                       // Whether to use "Bearer" prefix
    },
    languageModels: [                                     // Available language models
      {
        displayName: 'GPT-4o',
        instance: openai('gpt-4o'),                       // Model instance from AI SDK
        functionCalling: true,                            // Whether model supports function calling
      },
      {
        displayName: 'GPT-4o Mini',
        instance: openai('gpt-4o-mini'),
        functionCalling: true,
      },
    ],
    imageModels: [                                        // Available image models
      {
        displayName: 'DALL-E 3',
        instance: openai.image('dall-e-3'),              // Image model instance
      },
      {
        displayName: 'DALL-E 2',
        instance: openai.image('dall-e-2'),
      },
    ],
  },
];
```

### 3. Update createAIModel Function

Add a case for your provider in the `createAIModel` function in `packages/shared/src/lib/ai/ai-sdk.ts`:

```typescript  theme={null}
import { createOpenAI } from '@ai-sdk/openai' // Import the OpenAI SDK

export function createAIModel<T extends LanguageModel | ImageModel>({
    providerName,
    modelInstance,
    engineToken,
    baseURL,
}: CreateAIModelParams<T>): T {
    const isImageModel = SUPPORTED_AI_PROVIDERS
        .flatMap(provider => provider.imageModels)
        .some(model => model.instance.modelId === modelInstance.modelId)

    switch (providerName) {
        // ... existing cases
        case 'openai': {
            const openaiVersion = 'v1'                     // OpenAI API version
            const provider = createOpenAI({
                apiKey,                                     // OpenAI API key
                baseURL: `${baseURL}/${openaiVersion}`,    // Full API URL
            })
            
            if (isImageModel) {
                return provider.imageModel(modelInstance.modelId) as T
            }
            return provider(modelInstance.modelId) as T
        }
        default:
            throw new Error(`Provider ${providerName} is not supported`)
    }
}
```

### 4. Handle Provider-Specific Requirements

OpenAI supports both language and image models, but some providers may have specific requirements or limitations:

```typescript  theme={null}
// Example: Anthropic only supports language models
case 'anthropic': {
    const provider = createAnthropic({
        apiKey,
        baseURL: `${baseURL}/v1`,
    })
    
    if (isImageModel) {
        throw new Error(`Provider ${providerName} does not support image models`)
    }
    return provider(modelInstance.modelId) as T
}

// Example: Replicate primarily supports image models
case 'replicate': {
    const provider = createReplicate({
        apiToken: apiKey,  // Note: Replicate uses 'apiToken' instead of 'apiKey'
        baseURL: `${baseURL}/v1`,
    })
    
    if (!isImageModel) {
        throw new Error(`Provider ${providerName} does not support language models`)
    }
    return provider.imageModel(modelInstance.modelId) as unknown as T
}
```

### 5. Test Your Integration

After adding the provider, test it by:

1. **Configure credentials** in the Admin panel for your new provider
2. **Create a test action** using `aiProps` to select your provider and models
3. **Verify functionality** by running a flow with your new provider

Once these changes are made, your new AI provider will be available in the `aiProps` dropdowns and can be used with `generateText` and other [AI SDK functions](https://ai-sdk.dev/docs/introduction) throughout Activepieces.


# Piece Auth
Source: https://www.activepieces.com/docs/developers/piece-reference/authentication

Learn about piece authentication

Piece authentication is used to gather user credentials and securely store them for future use in different flows. The authentication must be defined as the `auth` parameter in the `createPiece`, `createTrigger`, and `createAction` functions.

This requirement ensures that the type of authentication can be inferred correctly in triggers and actions.

<Tip>
  Friendly Tip: Only at most one authentication is allowed per piece.
</Tip>

### Secret Text

This authentication collects sensitive information, such as passwords or API keys. It is displayed as a masked input field.

**Example:**

```typescript  theme={null}
PieceAuth.SecretText({
    displayName: 'API Key',
    description: 'Enter your API key',
    required: true,
    // Optional Validation
    validate: async ({auth}) => {
        if(auth.startsWith('sk_')){
            return {
                valid: true,
            }
        }
        return {
            valid: false,
            error: 'Invalid Api Key'
        }
    }
})
```

### Username and Password

This authentication collects a username and password as separate fields.

**Example:**

```typescript  theme={null}
PieceAuth.BasicAuth({
    displayName: 'Credentials',
    description: 'Enter your username and password',
    required: true,
    username: {
        displayName: 'Username',
        description: 'Enter your username',
    },
    password: {
        displayName: 'Password',
        description: 'Enter your password',
    },
    // Optional Validation
    validate: async ({auth}) => {
        if(auth){
            return {
                valid: true,
            }
        }
        return {
            valid: false,
            error: 'Invalid Api Key'
        }
    }
})
```

### Custom

This authentication allows for custom authentication by collecting specific properties, such as a base URL and access token.

**Example:**

```typescript  theme={null}
PieceAuth.CustomAuth({
    displayName: 'Custom Authentication',
    description: 'Enter custom authentication details',
    props: {
        base_url: Property.ShortText({
            displayName: 'Base URL',
            description: 'Enter the base URL',
            required: true,
        }),
        access_token: PieceAuth.SecretText({
            displayName: 'Access Token',
            description: 'Enter the access token',
            required: true
        })
    },
    // Optional Validation
    validate: async ({auth}) => {
        if(auth){
            return {
                valid: true,
            }
        }
        return {
            valid: false,
            error: 'Invalid Api Key'
        }
    },
    required: true
})
```

### OAuth2

This authentication collects OAuth2 authentication details, including the authentication URL, token URL, and scope.

**Example:**

```typescript  theme={null}
PieceAuth.OAuth2({
    displayName: 'OAuth2 Authentication',
    grantType: OAuth2GrantType.AUTHORIZATION_CODE,
    required: true,
    authUrl: 'https://example.com/auth',
    tokenUrl: 'https://example.com/token',
    scope: ['read', 'write']
})
```

<Tip>
  Please note `OAuth2GrantType.CLIENT_CREDENTIALS` is also supported for service-based authentication.
</Tip>


# Enable Custom API Calls
Source: https://www.activepieces.com/docs/developers/piece-reference/custom-api-calls

Learn how to enable custom API calls for your pieces

Custom API Calls allow the user to send a request to a specific endpoint if no action has been implemented for it.

This will show in the actions list of the piece as `Custom API Call`, to enable this action for a piece, you need to call the `createCustomApiCallAction` in your actions array.

## Basic Example

The example below implements the action for the OpenAI piece. The OpenAI piece uses a `Bearer token` authorization header to identify the user sending the request.

```typescript  theme={null}
actions: [
  ...yourActions,
  createCustomApiCallAction({
    // The auth object defined in the piece
    auth: openaiAuth,
    // The base URL for the API
    baseUrl: () => {
      'https://api.openai.com/v1'
    },
    // Mapping the auth object to the needed authorization headers
    authMapping: async (auth) => {
      return {
        'Authorization': `Bearer ${auth}`
      }
    }
  })
]
```

## Dynamic Base URL and Basic Auth Example

The example below implements the action for the Jira Cloud piece. The Jira Cloud piece uses a dynamic base URL for it's actions, where the base URL changes based on the values the user authenticated with. We will also implement a Basic authentication header.

```typescript  theme={null}
actions: [
  ...yourActions,
  createCustomApiCallAction({
    baseUrl: (auth) => {
      return `${(auth as JiraAuth).instanceUrl}/rest/api/3`
    },
    auth: jiraCloudAuth,
    authMapping: async (auth) => {
      const typedAuth = auth  as JiraAuth
      return {
        'Authorization': `Basic ${typedAuth.email}:${typedAuth.apiToken}`
      }
    }
  })
]
```


# Piece Examples
Source: https://www.activepieces.com/docs/developers/piece-reference/examples

Explore a collection of example triggers and actions

To get the full benefit, it is recommended to read the tutorial first.

## Triggers:

**Webhooks:**

* [New Form Submission on Typeform](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/typeform/src/lib/trigger/new-submission.ts)

**Polling:**

* [New Completed Task On Todoist](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/todoist/src/lib/triggers/task-completed-trigger.ts)

## Actions:

* [Send a message On Discord](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/discord/src/lib/actions/send-message-webhook.ts)
* [Send an mail On Gmail](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/gmail/src/lib/actions/send-email-action.ts)

## Authentication

**OAuth2:**

* [Slack](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/slack/src/index.ts)
* [Gmail](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/gmail/src/index.ts)

**API Key:**

* [Sendgrid](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/sendgrid/src/index.ts)

**Basic Authentication:**

* [Twilio](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/twilio/src/index.ts)


# External Libraries
Source: https://www.activepieces.com/docs/developers/piece-reference/external-libraries

Learn how to install and use external libraries.

The Activepieces repository is structured as a monorepo, employing Nx as its build tool.

To use an external library in your project, you can simply add it to the main `package.json` file and then use it in any part of your project.

Nx will automatically detect where you're using the library and include it in the build.

Here's how to install and use an external library:

* Install the library using:

```bash  theme={null}
npm install --save <library-name>
```

* Import the library into your piece.

Guidelines:

* Make sure you are using well-maintained libraries.
* Ensure that the library size is not too large to avoid bloating the bundle size; this will make the piece load faster in the sandbox.


# Files
Source: https://www.activepieces.com/docs/developers/piece-reference/files

Learn how to use files object to create file references.

The `ctx.files` object allow you to store files in local storage or in a remote storage depending on the run environment.

## Write

You can use the `write` method to write a file to the storage, It returns a string that can be used in other actions or triggers properties to reference the file.

**Example:**

```ts  theme={null}
const fileReference = await files.write({
    fileName: 'file.txt',
    data: Buffer.from('text')
});
```

<Tip>
  This code will store the file in the database If the run environment is testing mode since it will be required to test other steps, other wise it will store it in the local temporary directory.
</Tip>

For Reading the file If you are using the file property in a trigger or action, It will be automatically parsed and you can use it directly, please refer to `Property.File` in the [properties](./properties#file) section.


# Flow Control
Source: https://www.activepieces.com/docs/developers/piece-reference/flow-control

Learn How to Control Flow from Inside the Piece

Flow Controls provide the ability to control the flow of execution from inside a piece. By using the `ctx` parameter in the `run` method of actions, you can perform various operations to control the flow.

## Stop Flow

You can stop the flow and provide a response to the webhook trigger. This can be useful when you want to terminate the execution of the piece and send a specific response back.

**Example with Response:**

```typescript  theme={null}
context.run.stop({
  response: {
    status: context.propsValue.status ?? StatusCodes.OK,
    body: context.propsValue.body,
    headers: (context.propsValue.headers as Record<string, string>) ?? {},
  },
});
```

**Example without Response:**

```typescript  theme={null}
context.run.stop();
```

## Pause Flow and Wait for Webhook

You can pause flow and return HTTP response, also provide a callback to URL that you can call with certain payload and continue the flow.

**Example:**

```typescript  theme={null}
ctx.run.pause({
  pauseMetadata: {
    type: PauseType.WEBHOOK,
    response: {
      callbackUrl: context.generateResumeUrl({
        queryParams: {},
      }),
    },
  },
});
```

## Pause Flow and Delay

You can pause or delay the flow until a specific timestamp. Currently, the only supported type of pause is a delay based on a future timestamp.

**Example:**

```typescript  theme={null}
ctx.run.pause({
    pauseMetadata: {
        type: PauseType.DELAY,
        resumeDateTime: futureTime.toUTCString()
    }
});
```

These flow hooks give you control over the execution of the piece by allowing you to stop the flow or pause it until a certain condition is met. You can use these hooks to customize the behavior and flow of your actions.


# Piece i18n
Source: https://www.activepieces.com/docs/developers/piece-reference/i18n

Learn about translating pieces to multiple locales

<Steps>
  <Step title="Generate">
    Run the following command to create a translation file with all the strings that need translation in your piece

    ```bash  theme={null}
    npm run cli pieces generate-translation-file PIECE_FOLDER_NAME
    ```
  </Step>

  <Step title="Translate">
    Make a copy of `packages/pieces/<community_or_custom>/<your_piece>/src/i18n/translation.json`, name it `<locale>.json` i.e fr.json and translate the values.

    <Tip>
      For open source pieces, you can use the [Crowdin project](https://crowdin.com/project/activepieces) to translate to different languages. These translations will automatically sync back to your code.
    </Tip>
  </Step>

  <Step title="Test Locally">
    After following the steps to [setup your development environment](/developers/development-setup/getting-started), click the small cog icon next to the logo in your dashboard and change the locale.

        <img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/i18n-pieces.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=faaaa3e7cb92bed169bd75dedfcc6d40" alt="Locales" data-og-width="317" width="317" data-og-height="615" height="615" data-path="resources/i18n-pieces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/i18n-pieces.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=683a91e3fe4e651b228a5d746828043c 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/i18n-pieces.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f761d69988b4ded29d6c728f26183f95 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/i18n-pieces.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=0eda6eeeb2e3c9a57af696cd11c84291 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/i18n-pieces.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=624186c9f925e29e20e119c2eeca1b45 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/i18n-pieces.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=ef8cba83277d18fcdd0f400a8fdda992 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/i18n-pieces.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=a4a528a62f88bc936abbbea7f76be2ec 2500w" />

    <br />

    In the builder your piece will now appear in the translated language:
    <img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/french-webhooks.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=b60c90a2735aaccda2293086a8a28e79" alt="French Webhooks" data-og-width="567" width="567" data-og-height="845" height="845" data-path="resources/french-webhooks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/french-webhooks.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=b3c018350e47f3057aa7f92e4466e7b7 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/french-webhooks.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=5916ebfe369ba93274c7df0e353ff88e 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/french-webhooks.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=506b9c3ca72e507361a866142955f7e5 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/french-webhooks.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=370083b6ec56e0fc1edd420ba250cfc1 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/french-webhooks.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=0231788f8e1638960dfcfa6a0c57b040 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/french-webhooks.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=a9b2e04abac5944e653e0dd7110c7a68 2500w" />
  </Step>

  <Step title="Publish">
    Follow the docs here to [publish your piece](/developers/sharing-pieces/overview)
  </Step>
</Steps>


# Persistent Storage
Source: https://www.activepieces.com/docs/developers/piece-reference/persistent-storage

Learn how to store and retrieve data from a key-value store

The `ctx` parameter inside triggers and actions provides a simple key/value storage mechanism. The storage is persistent, meaning that the stored values are retained even after the execution of the piece.

By default, the storage operates at the flow level, but it can also be configured to store values at the project level.

<Tip>
  The storage scope is completely isolated. If a key is stored in a different scope, it will not be fetched when requested in different scope.
</Tip>

## Put

You can store a value with a specified key in the storage.

**Example:**

```typescript  theme={null}
ctx.store.put('KEY', 'VALUE', StoreScope.PROJECT);
```

## Get

You can retrieve the value associated with a specific key from the storage.

**Example:**

```typescript  theme={null}
const value = ctx.store.get<string>('KEY', StoreScope.PROJECT);
```

## Delete

You can delete a key-value pair from the storage.

**Example:**

```typescript  theme={null}
ctx.store.delete('KEY', StoreScope.PROJECT);
```

These storage operations allow you to store, retrieve, and delete key-value pairs in the persistent storage. You can use this storage mechanism to store and retrieve data as needed within your triggers and actions.


# Piece Versioning
Source: https://www.activepieces.com/docs/developers/piece-reference/piece-versioning

Learn how to version your pieces

Pieces are npm packages and follows **semantic versioning**.

## Semantic Versioning

The version number consists of three numbers: `MAJOR.MINOR.PATCH`, where:

* **MAJOR** It should be incremented when there are breaking changes to the piece.
* **MINOR** It should be incremented for new features or functionality that is compatible with the previous version, unless the major version is less than 1.0, in which case it can be a breaking change.
* **PATCH** It should be incremented for bug fixes and small changes that do not introduce new features or break backward compatibility.

## Engine

The engine will use the most up-to-date compatible version for a given piece version during the **DRAFT** flow versions. Once the flow is published, all pieces will be locked to a specific version.

**Case 1: Piece Version is Less Than 1.0**:
The engine will select the latest **patch** version that shares the same **minor** version number.

**Case 2: Piece Version Reaches Version 1.0**:
The engine will select the latest **minor** version that shares the same **major** version number.

## Examples

<Tip>
  when you make a change, remember to increment the version accordingly.
</Tip>

### Breaking changes

* Remove an existing action.
* Add a required `action` prop.
* Remove an existing action prop, whether required or optional.
* Remove an attribute from an action output.
* Change the existing behavior of an action/trigger.

### Non-breaking changes

* Add a new action.
* Add an optional `action` prop.
* Add an attribute to an action output.

i.e., any removal is breaking, any required addition is breaking, everything else is not breaking.


# Props
Source: https://www.activepieces.com/docs/developers/piece-reference/properties

Learn about different types of properties used in triggers / actions

Properties are used in actions and triggers to collect information from the user. They are also displayed to the user for input. Here are some commonly used properties:

## Basic Properties

These properties collect basic information from the user.

### Short Text

This property collects a short text input from the user.

**Example:**

```typescript  theme={null}
Property.ShortText({
  displayName: 'Name',
  description: 'Enter your name',
  required: true,
  defaultValue: 'John Doe',
});
```

### Long Text

This property collects a long text input from the user.

**Example:**

```typescript  theme={null}
Property.LongText({
  displayName: 'Description',
  description: 'Enter a description',
  required: false,
});
```

### Checkbox

This property presents a checkbox for the user to select or deselect.

**Example:**

```typescript  theme={null}
Property.Checkbox({
  displayName: 'Agree to Terms',
  description: 'Check this box to agree to the terms',
  required: true,
  defaultValue: false,
});
```

### Markdown

This property displays a markdown snippet to the user, useful for documentation or instructions. It includes a `variant` option to style the markdown, using the `MarkdownVariant` enum:

* **BORDERLESS**: For a minimalistic, no-border layout.
* **INFO**: Displays informational messages.
* **WARNING**: Alerts the user to cautionary information.
* **TIP**: Highlights helpful tips or suggestions.

The default value for `variant` is **INFO**.

**Example:**

```typescript  theme={null}
Property.MarkDown({
    value: '## This is a markdown snippet',
    variant: MarkdownVariant.WARNING,
}),
```

<Tip>
  If you want to show a webhook url to the user, use `{{ webhookUrl }}` in the
  markdown snippet.
</Tip>

### DateTime

This property collects a date and time from the user.

**Example:**

```typescript  theme={null}
Property.DateTime({
  displayName: 'Date and Time',
  description: 'Select a date and time',
  required: true,
  defaultValue: '2023-06-09T12:00:00Z',
});
```

### Number

This property collects a numeric input from the user.

**Example:**

```typescript  theme={null}
Property.Number({
  displayName: 'Quantity',
  description: 'Enter a number',
  required: true,
});
```

### Static Dropdown

This property presents a dropdown menu with predefined options.

**Example:**

```typescript  theme={null}
Property.StaticDropdown({
  displayName: 'Country',
  description: 'Select your country',
  required: true,
  options: {
    options: [
      {
        label: 'Option One',

        value: '1',
      },
      {
        label: 'Option Two',
        value: '2',
      },
    ],
  },
});
```

### Static Multiple Dropdown

This property presents a dropdown menu with multiple selection options.

**Example:**

```typescript  theme={null}
Property.StaticMultiSelectDropdown({
  displayName: 'Colors',
  description: 'Select one or more colors',
  required: true,
  options: {
    options: [
      {
        label: 'Red',
        value: 'red',
      },
      {
        label: 'Green',
        value: 'green',
      },
      {
        label: 'Blue',
        value: 'blue',
      },
    ],
  },
});
```

### JSON

This property collects JSON data from the user.

**Example:**

```typescript  theme={null}
Property.Json({
  displayName: 'Data',
  description: 'Enter JSON data',
  required: true,
  defaultValue: { key: 'value' },
});
```

### Dictionary

This property collects key-value pairs from the user.

**Example:**

```typescript  theme={null}
Property.Object({
  displayName: 'Options',
  description: 'Enter key-value pairs',
  required: true,
  defaultValue: {
    key1: 'value1',
    key2: 'value2',
  },
});
```

### File

This property collects a file from the user, either by providing a URL or uploading a file.

**Example:**

```typescript  theme={null}
Property.File({
  displayName: 'File',
  description: 'Upload a file',
  required: true,
});
```

### Array of Strings

This property collects an array of strings from the user.

**Example:**

```typescript  theme={null}
Property.Array({
  displayName: 'Tags',
  description: 'Enter tags',
  required: false,
  defaultValue: ['tag1', 'tag2'],
});
```

### Array of Fields

This property collects an array of objects from the user.

**Example:**

```typescript  theme={null}
Property.Array({
  displayName: 'Fields',
  description: 'Enter fields',
  properties: {
    fieldName: Property.ShortText({
      displayName: 'Field Name',
      required: true,
    }),
    fieldType: Property.StaticDropdown({
      displayName: 'Field Type',
      required: true,
      options: {
        options: [
          { label: 'TEXT', value: 'TEXT' },
          { label: 'NUMBER', value: 'NUMBER' },
        ],
      },
    }),
  },
  required: false,
  defaultValue: [],
});
```

## Dynamic Data Properties

These properties provide more advanced options for collecting user input.

### Dropdown

This property allows for dynamically loaded options based on the user's input.

**Example:**

```typescript  theme={null}
Property.Dropdown({
  displayName: 'Options',
  description: 'Select an option',
  required: true,
  refreshers: ['auth'],
  refreshOnSearch: false,
  options: async ({ auth }, { searchValue }) => {
    // Search value only works when refreshOnSearch is true
    if (!auth) {
      return {
        disabled: true,
      };
    }
    return {
      options: [
        {
          label: 'Option One',
          value: '1',
        },
        {
          label: 'Option Two',
          value: '2',
        },
      ],
    };
  },
});
```

<Tip>
  When accessing the Piece auth, be sure to use exactly `auth` as it is
  hardcoded. However, for other properties, use their respective names.
</Tip>

### Multi-Select Dropdown

This property allows for multiple selections from dynamically loaded options.

**Example:**

```typescript  theme={null}
Property.MultiSelectDropdown({
  displayName: 'Options',
  description: 'Select one or more options',
  required: true,
  refreshers: ['auth'],
  options: async ({ auth }) => {
    if (!auth) {
      return {
        disabled: true,
      };
    }
    return {
      options: [
        {
          label: 'Option One',
          value: '1',
        },
        {
          label: 'Option Two',
          value: '2',
        },
      ],
    };
  },
});
```

<Tip>
  When accessing the Piece auth, be sure to use exactly `auth` as it is
  hardcoded. However, for other properties, use their respective names.
</Tip>

### Dynamic Properties

This property is used to construct forms dynamically based on API responses or user input.

**Example:**

```typescript  theme={null}

import {
	httpClient,
	HttpMethod,
} from '@activepieces/pieces-common';


Property.DynamicProperties({
  description: 'Dynamic Form',
  displayName: 'Dynamic Form',
  required: true,
  refreshers: ['authentication'],
  props: async (propsValue) => {
    const authentication = propsValue['authentication'];
    const apiEndpoint = 'https://someapi.com';
    const response = await httpClient.sendRequest<{ values: [string[]][] }>({
        method: HttpMethod.GET,
        url: apiEndpoint 
	  });

    const properties = {
      prop1: Property.ShortText({
        displayName: 'Property 1',
        description: 'Enter property 1',
        required: true,
      }),
      prop2: Property.Number({
        displayName: 'Property 2',
        description: 'Enter property 2',
        required: false,
      }),
    };

    return properties;
  },
});
```

### Custom Property (BETA)

<Warning>
  This feature is still in BETA and not fully released yet, please let us know if you use it and face any issues and consider it a possibility could have breaking changes in the future
</Warning>

This is a property that lets you inject JS code into the frontend and manipulate the DOM of this content however you like, it is extremely useful in case you are [embedding](/embedding/overview) Activepieces and want to have a way to communicate with the SaaS embedding it.
It has a `code` property which is a function that takes in an object parameter which will have the following schema:

| Parameter Name | Type                                                             | Description                                                                                                       |
| -------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| onChange       | `(value:unknown)=>void`                                          | A callback you call to set the value of your input (only call this inside event handlers)                         |
| value          | `unknown`                                                        | Whatever the type of the value you pass to onChange                                                               |
| containerId    | `string`                                                         | The ID of an HTML element in which you can modify the DOM however you like                                        |
| isEmbedded     | `boolean`                                                        | The flag that tells you if the code is running inside an [embedded instance](/embedding/overview) of Activepieces |
| projectId      | `string`                                                         | The project ID of the flow the step that contains this property is in                                             |
| disabled       | `boolean`                                                        | The flag that tells you whether or not the property is disabled                                                   |
| property       | `{ displayName:string, description?: string, required: boolean}` | The current property information                                                                                  |

* You can return a clean up function at the end of the `code` property function to remove any listeners or HTML elements you inserted (this is important for development mode, the component gets [mounted twice](https://react.dev/reference/react/useEffect#my-effect-runs-twice-when-the-component-mounts)).
* This function must be pure without any imports from external packages or variables outside the function scope.
* **Must** mark your piece `minimumSupportedRelease` property to be at least `0.58.0` after introducing this property to it.

Here is how to define such a property:

```typescript  theme={null}
 Property.Custom({
      code:(({value,onChange,containerId})=>{
        const container = document.getElementById(containerId);
        const input = document.createElement('input');
        input.classList.add(...['border','border-solid', 'border-border', 'rounded-md']) 
        input.type = 'text';
        input.value = `${value}`;
        input.oninput = (e: Event) => {
          const value = (e.target as HTMLInputElement).value;
          onChange(value);
        }
       container!.appendChild(input);
       const windowCallback = (e:MessageEvent<{type:string,value:string,propertyName:string}>) => {
        if(e.data.type === 'updateInput' && e.data.propertyName === 'YOUR_PROPERTY_NAME'){
          input.value= e.data.value;
          onChange(e.data.value);
        }
       }
       window.addEventListener('message', windowCallback);
        return ()=>{
          window.removeEventListener('message', windowCallback);
          container!.removeChild(input);
        }
      }),
      displayName: 'Custom Property',
      required: true
    })
```

* If you would like to know more about how to setup communication between Activepieces and the SaaS that's embedding it, check the [window postMessage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage).


# Props Validation
Source: https://www.activepieces.com/docs/developers/piece-reference/properties-validation

Learn about different types of properties validation 

Activepieces uses Zod for runtime validation of piece properties. Zod provides a powerful schema validation system that helps ensure your piece receives valid inputs.

To use Zod validation in your piece, first import the validation helper and Zod:

<Warning>
  Please make sure the `minimumSupportedRelease` is set to at least `0.36.1` for the validation to work.
</Warning>

```typescript  theme={null}
import { createAction, Property } from '@activepieces/pieces-framework';
import { propsValidation } from '@activepieces/pieces-common';
import { z } from 'zod';

export const getIcecreamFlavor = createAction({
  name: 'get_icecream_flavor', // Unique name for the action.
  displayName: 'Get Ice Cream Flavor',
  description: 'Fetches a random ice cream flavor based on user preferences.',
  props: {
    sweetnessLevel: Property.Number({
      displayName: 'Sweetness Level',
      required: true,
      description: 'Specify the sweetness level (0 to 10).',
    }),
    includeToppings: Property.Checkbox({
      displayName: 'Include Toppings',
      required: false,
      description: 'Should the flavor include toppings?',
      defaultValue: true,
    }),
    numberOfFlavors: Property.Number({
      displayName: 'Number of Flavors',
      required: true,
      description: 'How many flavors do you want to fetch? (1-5)',
      defaultValue: 1,
    }),
  },
  async run({ propsValue }) {
    // Validate the input properties using Zod
    await propsValidation.validateZod(propsValue, {
      sweetnessLevel: z.number().min(0).max(10, 'Sweetness level must be between 0 and 10.'),
      numberOfFlavors: z.number().min(1).max(5, 'You can fetch between 1 and 5 flavors.'),
    });

    // Action logic
    const sweetnessLevel = propsValue.sweetnessLevel;
    const includeToppings = propsValue.includeToppings ?? true; // Default to true
    const numberOfFlavors = propsValue.numberOfFlavors;

    // Simulate fetching random ice cream flavors
    const allFlavors = [
      'Vanilla',
      'Chocolate',
      'Strawberry',
      'Mint',
      'Cookie Dough',
      'Pistachio',
      'Mango',
      'Coffee',
      'Salted Caramel',
      'Blackberry',
    ];
    const selectedFlavors = allFlavors.slice(0, numberOfFlavors);

    return {
      message: `Here are your ${numberOfFlavors} flavors: ${selectedFlavors.join(', ')}`,
      sweetnessLevel: sweetnessLevel,
      includeToppings: includeToppings,
    };
  },
});

```


# Overview
Source: https://www.activepieces.com/docs/developers/piece-reference/triggers/overview



This tutorial explains three techniques for creating triggers:

* `Polling`: Periodically call endpoints to check for changes.
* `Webhooks`: Listen to user events through a single URL.
* `App Webhooks (Subscriptions)`: Use a developer app (using OAuth2) to receive all authorized user events at a single URL (Not Supported).

to create new trigger run following command,

```bash  theme={null}
npm run cli triggers create
```

1. `Piece Folder Name`: This is the name associated with the folder where the trigger resides. It helps organize and categorize triggers within the piece.
2. `Trigger Display Name`: The name users see in the interface, conveying the trigger's purpose clearly.
3. `Trigger Description`: A brief, informative text in the UI, guiding users about the trigger's function and purpose.
4. `Trigger Technique`: Specifies the trigger type - either polling or webhook.

# Trigger Structure

```typescript  theme={null}
export const createNewIssue = createTrigger({
    auth: PieceAuth | undefined
    name: string, // Unique name across the piece.
    displayName: string, // Display name on the interface.
	description: string, // Description for the action
    sampleData: null,
    type: TriggerStrategy.WEBHOOK | TriggerStrategy.POLLING | TriggerStrategy.APP_WEBHOOK,

    props: {}; // Required properties from the user.
    // Run when the user enable or publish the flow.

	onEnable: (ctx) => {},
    // Run when the user disable the flow or
    // the old flow is deleted after new one is published.
	onDisable: (ctx) => {},

    // Trigger implementation, It takes context as parameter.
    // should returns an array of payload, each payload considered
    run: async run(ctx): unknown[] => {}
})
```

<Tip>
  It's important to note that the `run` method returns an array. The reason for
  this is that a single polling can contain multiple triggers, so each item in
  the array will trigger the flow to run.
</Tip>

## Context Object

The Context object contains multiple helpful pieces of information and tools that can be useful while developing.

```typescript  theme={null}
// Store: A simple, lightweight key-value store that is helpful when you are developing triggers that persist between runs, used to store information like the last polling date.
await context.store.put('_lastFetchedDate', new Date());
const lastFetchedData = await context.store.get('_lastFetchedDate', new Date());

// Webhook URL: A unique, auto-generated URL that will trigger the flow. Useful when you need to develop a trigger based on webhooks.
context.webhookUrl;

// Payload: Contains information about the HTTP request sent by the third party. It has three properties: status, headers, and body.
context.payload;

// PropsValue: Contains the information filled by the user in defined properties.
context.propsValue;
```

**App Webhooks (Not Supported)**

Certain services, such as `Slack` and `Square`, only support webhooks at the developer app level.
This means that all authorized users for the app will be sent to the same endpoint. While this technique will be supported soon, for now, a workaround is to perform polling on the endpoint.


# Polling Trigger
Source: https://www.activepieces.com/docs/developers/piece-reference/triggers/polling-trigger

Periodically call endpoints to check for changes

The way polling triggers usually work is as follows:

**On Enable:**
Store the last timestamp or most recent item id using the context store property.

**Run:**
This method runs every **5 minutes**, fetches the endpoint between a certain timestamp or traverses until it finds the last item id, and returns the new items as an array.

**Testing:**
You can implement a test function which should return some of the most recent items. It's recommended to limit this to five.

**Examples:**

* [New Record Airtable](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/airtable/src/lib/trigger/new-record.trigger.ts)
* [New Updated Item Salesforce](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/salesforce/src/lib/trigger/new-updated-record.ts)

# Polling library

There multiple strategy to implement polling triggers, and we have created a library to help you with that.

## Strategies

**Timebased:**

This strategy fetches new items using a timestamp. You need to implement the items method, which should return the most recent items.
The library will detect new items based on the timestamp.

The polling object's generic type consists of the props value and the object type.

```typescript  theme={null}
const polling: Polling<{ authentication: OAuth2PropertyValue, object: string }> = {
  strategy: DedupeStrategy.TIMEBASED,
  items: async ({ propsValue, lastFetchEpochMS }) => {
    // Todo implement the logic to fetch the items
    const items = [ {id: 1, created_date: '2021-01-01T00:00:00Z'}, {id: 2, created_date: '2021-01-01T00:00:00Z'}];
    return items.map((item) => ({
      epochMilliSeconds: dayjs(item.created_date).valueOf(),
      data: item,
    }));
  }
}
```

**Last ID Strategy:**

This strategy fetches new items based on the last item ID. To use this strategy, you need to implement the items method, which should return the most recent items.
The library will detect new items after the last item ID.

The polling object's generic type consists of the props value and the object type

```typescript  theme={null}
const polling: Polling<{ authentication: AuthProps}> = {
    strategy: DedupeStrategy.LAST_ITEM,
    items: async ({ propsValue }) => {
        // Implement the logic to fetch the items
        const items = [{ id: 1 }, { id: 2 }];
        return items.map((item) => ({
            id: item.id,
            data: item,
        }));
    }
}
```

## Trigger Implementation

After implementing the polling object, you can use the polling helper to implement the trigger.

```typescript  theme={null}
export const newTicketInView = createTrigger({
    name: 'new_ticket_in_view',
    displayName: 'New ticket in view',
    description: 'Triggers when a new ticket is created in a view',
    type: TriggerStrategy.POLLING,
    props: {
        authentication: Property.SecretText({
            displayName: 'Authentication',
            description: markdownProperty,
            required: true,
        }),
    },
    sampleData: {},
    onEnable: async (context) => {
        await pollingHelper.onEnable(polling, {
            store: context.store,
            propsValue: context.propsValue,
            auth: context.auth
        })
    },
    onDisable: async (context) => {
        await pollingHelper.onDisable(polling, {
            store: context.store,
            propsValue: context.propsValue,
            auth: context.auth

        })
    },
    run: async (context) => {
        return await pollingHelper.poll(polling, context);
    },
    test: async (context) => {
        return await pollingHelper.test(polling, context);
    }
});
```


# Webhook Trigger
Source: https://www.activepieces.com/docs/developers/piece-reference/triggers/webhook-trigger

Listen to user events through a single URL

The way webhook triggers usually work is as follows:

**On Enable:**
Use `context.webhookUrl` to perform an HTTP request to register the webhook in a third-party app, and store the webhook Id in the `store`.

**On Handshake:**
Some services require a successful handshake request usually consisting of some challenge. It works similar to a normal run except that you return the correct challenge response. This is optional and in order to enable the handshake you need to configure one of the available handshake strategies in the `handshakeConfiguration` option.

**Run:**
You can find the HTTP body inside `context.payload.body`. If needed, alter the body; otherwise, return an array with a single item `context.payload.body`.

**Disable:**
Using the `context.store`, fetch the webhook ID from the enable step and delete the webhook on the third-party app.

**Testing:**
You cannot test it with Test Flow, as it uses static sample data provided in the piece.
To test the trigger, publish the flow, perform the event. Then check the flow runs from the main dashboard.

**Examples:**

* [New Form Submission on Typeform](https://github.com/activepieces/activepieces/blob/main/packages/pieces/community/typeform/src/lib/trigger/new-submission.ts)

<Warning>
  To make your webhook accessible from the internet, you need to configure the backend URL. Follow these steps:

  1. Install ngrok.
  2. Run the command `ngrok http 4200`.
  3. Replace the `AP_FRONTEND_URL` environment variable in `packages/server/api/.env` with the ngrok URL.

  Once you have completed these configurations, you are good to go!
</Warning>


# Community (Public NPM)
Source: https://www.activepieces.com/docs/developers/sharing-pieces/community

Learn how to publish your piece to the community.

You can publish your pieces to the npm registry and share them with the community. Users can install your piece from Settings -> My Pieces -> Install Piece -> type in the name of your piece package.

<Steps>
  <Step title="Login to npm">
    Make sure you are logged in to npm. If not, please run:

    ```bash  theme={null}
    npm login
    ```
  </Step>

  <Step title="Rename Piece">
    Rename the piece name in `package.json` to something unique or related to your organization's scope (e.g., `@my-org/piece-PIECE_NAME`). You can find it at `packages/pieces/PIECE_NAME/package.json`.

    <Tip>
      Don't forget to increase the version number in `package.json` for each new release.
    </Tip>
  </Step>

  <Step title="Publish">
    <Tip>
      Replace `PIECE_FOLDER_NAME` with the name of the folder.
    </Tip>

    Run the following command:

    ```bash  theme={null}
    npm run publish-piece PIECE_FOLDER_NAME
    ```
  </Step>
</Steps>

**Congratulations! You can now import the piece from the settings page.**


# Contribute
Source: https://www.activepieces.com/docs/developers/sharing-pieces/contribute

Learn how to contribute a piece to the main repository.

<Steps>
  <Step title="Open a pull request">
    * Build and test your piece.
    * Open a pull request from your repository to the main fork.
    * A maintainer will review your work closely.
  </Step>

  <Step title="Merge the pull request">
    * Once the pull request is approved, it will be merged into the main branch.
    * Your piece will be available within a few minutes.
    * An automatic GitHub action will package it and create an npm package on npmjs.com.
  </Step>
</Steps>


# Overview
Source: https://www.activepieces.com/docs/developers/sharing-pieces/overview

Learn the different ways to publish your own piece on activepieces.

## Methods

* [Contribute Back](/developers/sharing-pieces/contribute): Publish your piece by contributing back your piece to main repository.
* [Community](/developers/sharing-pieces/community): Publish your piece on npm directly and share it with the community.
* [Private](/developers/sharing-pieces/private): Publish your piece on activepieces privately.


# Private
Source: https://www.activepieces.com/docs/developers/sharing-pieces/private

Learn how to share your pieces privately.

<Snippet file="enterprise-feature.mdx" />

This guide assumes you have already created a piece and created a private fork of our repository, and you would like to package it as a file and upload it.

<Tip>
  Friendly Tip: There is a CLI to easily upload it to your platform. Please check out [Publish Custom Pieces](../misc/publish-piece).
</Tip>

<Steps>
  <Step title="Build Piece">
    Build the piece using the following command. Make sure to replace `${name}` with your piece name.

    ```bash  theme={null}
    npm run pieces -- build --name=${name}
    ```

    <Info>
      More information about building pieces can be found [here](../misc/build-piece).
    </Info>
  </Step>

  <Step title="Upload Tarball">
    Upload the generated tarball inside `dist/packages/pieces/${name}`from Activepieces Platform Admin -> Pieces

        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1106164b9b77b33e96ccdcd4df789948" alt="Manage Pieces" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/install-piece.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c9009ba8db60863675f21036a561f4ce 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c7ad50fd4c721848169fe6c9c2c6af0b 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=6cfedfb7edde2f9311a1af6b783520cf 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=615c3b9f24457a4384ede39ed276d50a 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=44499b6321130356ec94bc0826eb19fd 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b7cfc85def669ee351fef9150f4c3bce 2500w" />
  </Step>
</Steps>


# Show/Hide Pieces
Source: https://www.activepieces.com/docs/embedding/customize-pieces



<Snippet file="enterprise-feature.mdx" />

<Snippet file="replace-oauth2-apps.mdx" />

If you would like to only show specific pieces to your embedding users, we recommend you do the following:

<Steps>
  <Step title="Tag Pieces">
    Tag the pieces you would like to show to your user by going to **Platform Admin -> Setup -> Pieces**, selecting the pieces you would like to tag and hit **Apply Tags**

        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=2cb4bd65c2a93d5680fb877d8add35d6" alt="Bulk Tag" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/tag-pieces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1fdf24f613938a6149c3d18f12476d3f 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3bafd772b35a2a39f87bbb9f41f2a04d 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=2c7712ea0a1ba76fe15933f3852b13fb 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=20baa4b9210a32bd3274e80465afd440 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b9f2c83196e8b5ce48da8110828e5ab5 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=fe1eb1911ea54eeed58ba48705faefa5 2500w" />
  </Step>

  <Step title="Add Tags to Provision Token">
    You need to specify the tags of pieces in the token, check how to generate token in [provisioning users](./provision-users).

    You should specify the `pieces` claim like this:

    ```json  theme={null}
    {
        /// Other claims
        "piecesFilterType": "ALLOWED",
        "piecesTags": [ "free" ]
    }
    ```

    Each time the token is used by the embedding SDK, it will sync all pieces with these tags to the token's project.
    The project will only contain the pieces that contain these tags.
  </Step>
</Steps>


# Embed Builder
Source: https://www.activepieces.com/docs/embedding/embed-builder



<Snippet file="enterprise-feature.mdx" />

This documentation explains how to embed the Activepieces iframe inside your application and customize it.

## Configure SDK

Adding the embedding SDK script will initialize an object in your window called `activepieces`, which has a method called `configure` that you should call after the container has been rendered.

<Tip>
  The following scripts shouldn't contain the `async` or `defer` attributes.
</Tip>

<Tip>
  These steps assume you have already generated a JWT token from the backend. If not, please check the [provision-users](./provision-users) page.
</Tip>

```html  theme={null}
<script src="https://cdn.activepieces.com/sdk/embed/0.8.1.js">
</script>
<script>
const instanceUrl = 'YOUR_INSTANCE_URL';
const jwtToken = 'GENERATED_JWT_TOKEN';
const containerId = 'YOUR_CONTAINER_ID';
activepieces.configure({
  instanceUrl,
  jwtToken,
  prefix: "/",
  embedding: {
    containerId,
    builder: {
      disableNavigation: false,
      hideFlowName: false
    },
    dashboard: {
      hideSidebar: false
    },
    hideFolders: false,
    navigation: {
      handler: ({ route }) => {
          // The iframe route has changed, make sure you check the navigation section.
        }
    }
  },
});

</script>
```

<Tip>
  `configure` returns a promise which is resolved after authentication is done.
</Tip>

<Tip>
  Please check the [navigation](./navigation) section, as it's very important to understand how navigation works and how to supply an auto-sync experience.
</Tip>

**Configure Parameters:**

| Parameter Name                             | Required | Type                                                                                | Description                                                                                                                                                                                                                |
| ------------------------------------------ | -------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instanceUrl                                | ✅        | string                                                                              | The url of the instance hosting Activepieces, could be [https://cloud.activepieces.com](https://cloud.activepieces.com) if you are a cloud user.                                                                           |
| jwtToken                                   | ✅        | string                                                                              | The jwt token you generated to authenticate your users to Activepieces.                                                                                                                                                    |
| prefix                                     | ❌        | string                                                                              | Some customers have an embedding prefix, like this `<embedding_url_prefix>/<Activepieces_url>`. For example if the prefix is `/automation` and the Activepieces url is `/flows` the full url would be `/automation/flows`. |
| embedding.containerId                      | ❌        | string                                                                              | The html element's id that is going to be containing Activepieces's iframe.                                                                                                                                                |
| embedding.builder.disableNavigation        | ❌        | boolean \| `keep_home_button_only`                                                  | Hides the folder name, home button (if not set to [`keep_home_button_only`](./sdk-changelog#20%2F05%2F2025-0-4-0)) and delete option in the builder, by default it is false.                                               |
| embedding.builder.hideFlowName             | ❌        | boolean                                                                             | Hides the flow name and flow actions dropdown in the builder's header, by default it is false.                                                                                                                             |
| embedding.builder.homeButtonClickedHandler | ❌        | `()=>void`                                                                          | Callback that stops home button from navigating to dashboard and overrides it with this handler (added in [0.4.0](./sdk-changelog#20%2F05%2F2025-0-4-0))                                                                   |
| embedding.builder.homeButtonIcon           | ❌        | `logo`  \| `back`                                                                   | if set to **`back`** the tooltip shown on hovering the home button is removed (added in [0.5.0](./sdk-changelog#03%2F07%2F2025-0-5-0))                                                                                     |
| embedding.dashboard.hideSidebar            | ❌        | boolean                                                                             | Controls the visibility of the sidebar in the dashboard, by default it is false.                                                                                                                                           |
| embedding.dashboard.hideFlowsPageNavbar    | ❌        | boolean                                                                             | Controls the visibility of the navbar showing flows,issues and runs above the flows table in the dashboard, by default it is false. (added in [0.6.0](./sdk-changelog#07%2F07%2F2025-0-6-0))                               |
| embedding.dashboard.hidePageHeader         | ❌        | boolean                                                                             | Hides the page header in the dashboard by default it is false. (added in [0.8.0](./sdk-changelog#09%2F21%2F2025-0-8-0))                                                                                                    |
| embedding.hideFolders                      | ❌        | boolean                                                                             | Hides all things related to folders in both the flows table and builder by default it is false.                                                                                                                            |
| embedding.styling.fontUrl                  | ❌        | string                                                                              | The url of the font to be used in the embedding, by default it is `https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap`.                                                                     |
| embedding.styling.fontFamily               | ❌        | string                                                                              | The font family to be used in the embedding, by default it is `Roboto`.                                                                                                                                                    |
| embedding.styling.mode                     | ❌        | `light` \| `dark`                                                                   | Controls light/dark mode (added in [0.5.0](./sdk-changelog#03%2F07%2F2025-0-5-0))                                                                                                                                          |
| embedding.hideExportAndImportFlow          | ❌        | boolean                                                                             | Hides the option to export or import flows (added in [0.4.0](./sdk-changelog#20%2F05%2F2025-0-4-0))                                                                                                                        |
| embedding.hideDuplicateFlow                | ❌        | boolean                                                                             | Hides the option to duplicate a flow  (added in [0.5.0](./sdk-changelog#03%2F07%2F2025-0-5-0))                                                                                                                             |
| embedding.locale                           | ❌        | `en` \| `nl` \| `de` \| `fr`  \| `es` \| `ja` \| `zh` \| `pt` \| `zh-TW` \| `ru` \| | it takes [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) locale codes (added in [0.5.0](./sdk-changelog#03%2F07%2F2025-0-5-0))                                                                   |
| navigation.handler                         | ❌        | `({route:string}) => void`                                                          | This callback will be triggered each time a route in Activepieces changes, you can read more about it [here](/embedding/navigation)                                                                                        |

<Tip>
  For the font to be loaded, you need to set both the `fontUrl` and `fontFamily` properties.
  If you only set one of them, the default font will be used.
  The default font is `Roboto`.
  The font weights we use are the default font-weights from [tailwind](https://tailwindcss.com/docs/font-weight).
</Tip>


# Create/Update Connections
Source: https://www.activepieces.com/docs/embedding/embed-connections



<Info>
  **Requirements:**

  * Activepieces version 0.34.5 or higher
  * SDK version 0.3.2 or higher
</Info>

<Snippet file="replace-oauth2-apps.mdx" />

<Info>
  "connectionName" is the externalId of the connection (you can get it by hovering the connection name in the connections table).  <br />
  We kept the same parameter name for backward compatibility, anyone upgrading their instance from \< 0.35.1, will not face issues in that regard.
</Info>

<Warning>
  **Breaking Change:** <br /><br /> If your Activepieces instance version is \< 0.45.0 and (you are using the connect method from the embed sdk, and need the connection externalId to be returned after the user creates it OR if you want to reconnect a specific connection with an externalId), you must upgrade your instance to >= 0.45.0
</Warning>

* You can use the embedded SDK in your SaaS to allow your users to create connections and store them in Activepieces.

<Steps>
  <Step title="Initialize the SDK">
    Follow the instructions in the [Embed Builder](./embed-builder).
  </Step>

  <Step title="Call Connect Method">
    After initializing the SDK, you will have access to a property called `activepieces` inside your `window` object. Call its `connect` method to open a new connection dialog as follows.

    ```html  theme={null}
    <script> 
    activepieces.connect({pieceName:'@activepieces/piece-google-sheets'});
    </script>
    ```

    **Connect Parameters:**

    | Parameter Name | Required | Type                                                              | Description                                                                                                                                                                                                   |
    | -------------- | -------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | pieceName      | ✅        | string                                                            | The name of the piece you want to create a connection for.                                                                                                                                                    |
    | connectionName | ❌        | string                                                            | The external Id of the connection (you can get it by hovering the connection name in the connections table), when provided the connection created/upserted will use this as the external Id and display name. |
    | newWindow      | ❌        | \{ width?: number, height?: number, top?: number, left?: number } | If set the connection dialog will be opened in a new window instead of an iframe taking the full page.                                                                                                        |

    **Connect Result**

    The `connect` method returns a `promise` that resolves to the following:

    ```ts  theme={null}
    {
        connection?: {
            id: string,
            name: string
        }
    }
    ```

    <Info>
      `name` is the externalId of the connection.
      `connection` is undefined if the user closes the dialog and doesn't create a connection.
    </Info>

    <Tip>
      You can use the `connections` piece in the builder to retrieve the created connection using its name.
      <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c8d14d795364249e9d64fd48c8e2d484" alt="Connections in Builder" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/connections-piece.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=4a5f42ec16c8293fd15825e2c94ad8ca 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=51f4632b11ce07e408de35aff0a59f6b 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=8b69d0a232717898fa91b8e3e6f5d185 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=75bf08645aa881589852c475ec2d2511 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=256226de97f2f5f0e956aa51a2e93fcf 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=110fab4a94a0ce9ae11db921b90b2cbc 2500w" />
      <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=402d7a7e10ef1f72517a6618d99ea3c8" alt="Connections in Builder" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/connections-piece-usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d7cb20b21c1830e162bb40b14807dd79 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e1c8b2b823c90d3f84757b667b109b41 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e28b5f05c90d7d4b95b853ea4977f95e 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=f3439d8a86f3c8dcb021fa76e4710920 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=920cb29c9b9b24c577431f5842cae52a 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3a5c9dbbe461c92f0ae6efd07a409d7d 2500w" />
    </Tip>
  </Step>
</Steps>


# Navigation
Source: https://www.activepieces.com/docs/embedding/navigation



By default, navigating within your embedded instance of Activepieces doesn't affect the client's browser history or viewed URL. Activepieces only provide a **handler**, that trigger on every route change in the **iframe**.

## Automatically Sync URL

You can use the following snippet when configuring the SDK, which will implement a handler that syncs the Activepieces iframe with your browser:

<Tip>
  The following snippet listens when the user clicks backward, so it syncs the route back to the iframe using `activepieces.navigate` and in the handler, it updates the URL of the browser.
</Tip>

```js  theme={null}
const instanceUrl = 'YOUR_INSTANCE_URL';
const jwtToken = 'YOUR_GENERATED_JWT_TOKEN';
const containerId = 'YOUR_CONTAINER_ID';
activepieces.configure({
  instanceUrl,
  jwtToken,
  embedding: {
    containerId,
    builder: {
      disableNavigation: false,
      hideFlowName: false
    },
    dashboard: {
      hideSidebar: false
    },
    hideFolders: false,
    navigation: {
      handler: ({ route }) => {
        //route can include search params at the end of it
        if (!window.location.href.endsWith(route)) {
          window.history.pushState({}, "", window.location.origin + route);
        }
      }
    }
  },
});

window.addEventListener("popstate", () => {
  const route = activepieces.extractActivepiecesRouteFromUrl({ vendorUrl: window.location.href });
  activepieces.navigate({ route });
});
```

## Navigate Method

If you use `activepieces.navigate({ route: '/flows' })` this will tell the embedded sdk where to navigate to.

Here is the list for routes the sdk can navigate to:

| Route               | Description                    |
| ------------------- | ------------------------------ |
| `/flows`            | Flows table                    |
| `/flows/{flowId}`   | Opens up a flow in the builder |
| `/runs`             | Runs table                     |
| `/runs/{runId}`     | Opens up a run in the builder  |
| `/connections`      | Connections table              |
| `/tables`           | Tables table                   |
| `/tables/{tableId}` | Opens up a table               |
| `todos`             | Todos table                    |
| `todos/{todoId}`    | Opens up a todo                |

## Navigate to Initial Route

You can call the `navigate` method after initializing the sdk using the `configure` sdk:

```js  theme={null}
const flowId = '1234';
const instanceUrl = 'YOUR_INSTANCE_URL';
const jwtToken = 'YOUR_GENERATED_JWT_TOKEN';
activepieces.configure({
	instanceUrl,
	jwtToken,
}).then(() => {
	activepieces.navigate({
		route: `/flows/${flowId}`
	})
});
```


# Overview
Source: https://www.activepieces.com/docs/embedding/overview

Understanding how embedding works

<Snippet file="enterprise-feature.mdx" />

This section provides an overview of how to embed the Activepieces builder in your application and automatically provision the user.

The embedding process involves the following steps:

<Steps>
  <Step title="Provision Users">
    Generate a JSON Web Token (JWT) to identify your customer and pass it to the SDK, read more [here](./provision-users).
  </Step>

  <Step title="Embed Builder">
    You can use the SDK to embed and customize Activepieces in your SaaS, read more [here](./embed-builder).
  </Step>
</Steps>

Here is an example of how it looks like in one of the SaaS that embed Activepieces:
<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/embedding-example.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=09dd50eecbdf2a7578ac5c978f898407" alt="Embedding Example" data-og-width="2630" width="2630" data-og-height="2284" height="2284" data-path="resources/screenshots/embedding-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/embedding-example.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=aa425d97900f54fdcff4ab1f8a8559da 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/embedding-example.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3b80ddc00e4a2117465da44cd9153c6e 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/embedding-example.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7b3d9d829a7b6e0ad8c19d7627d51492 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/embedding-example.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c452252de8ced0ec22d390192c1a3729 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/embedding-example.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=2f29a375b063b9b2228ebc637e462a84 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/embedding-example.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=2c7ba3547b50f1594fcc5ca64f50a581 2500w" />

<Tip>
  In case, you need to gather connections from your users in your SaaS. You can do this with the SDK. Find more info [here](./embed-connections).
</Tip>

<Tip>
  If you are looking for a way to communicate between Activpieces and the SaaS embedding it through a piece, we recommend you check the [custom property doc](/developers/piece-reference/properties#custom-property-beta)
</Tip>


# Predefined Connection
Source: https://www.activepieces.com/docs/embedding/predefined-connection



Use predefined connections to allow users to access your piece in the embedded app without re-entering authentication credentials.

The high-level steps are:

* Create a global connection for a project using the API in the platform admin. Only platform admins can edit or delete global connections.
* (Optional) Hide the connections dropdown in the piece settings.

### Prerequisites

* [Run the Enterprise Edition](/handbook/engineering/playbooks/run-ee)
* [Create your piece](/developers/building-pieces/overview). Later we will customize the piece logic to use predefined connections.

### Create a Predefined Connection

<Steps>
  <Step title="Create an API Key">
    Go to **Platform Admin → Security → API Keys** and create an API key. Save it for use in the next step.
    <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-api-key.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=cb42e0171f14b314bfbcf58f2c7ef415" alt="Create API Key" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/create-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-api-key.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=11cd9dfa90858803063a6adb33aba934 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-api-key.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=fce77edd69bb3f90fc32ea951b813a0a 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-api-key.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=710d6cf4d50818b00b5c54bce30dbb10 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-api-key.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e43e20030ecbf0977ad755136e363611 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-api-key.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3f0dc4414fece6dd7a2479afe212f868 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-api-key.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3a8479614b105ff9a3395b3a0215b553 2500w" />
  </Step>

  <Step title="Create a Global Connection via API">
    Add the following snippet to your backend to create a global connection each time you generate the <b>JWT token</b>.

    The snippet does the following:

    * Create Project If it doesn't exist.
    * Create a global connection for the project with certain naming convention.

    ```js  theme={null}
    const apiKey = 'YOUR_API_KEY';
    const instanceUrl = 'https://cloud.activepieces.com';

    // The name of the user / organization in your SAAS
    const externalProjectId = 'org_1234';
    const pieceName = '@activepieces/piece-gelato';
    // This will depend on what your piece auth type is, can be one of this ['PLATFORM_OAUTH2','SECRET_TEXT','BASIC_AUTH','CUSTOM_AUTH']
    const pieceAuthType = "CUSTOM_AUTH"
    const connectionProps = {
        // Fill in the props required by your piece's auth
    }
    const { id: projectId, externalId } = await getOrCreateProject({
      projectExternalId: externalProjectId,
      apiKey,
      instanceUrl,
    });

    await createGlobalConnection({
      projectId,
      externalProjectId,
      apiKey,
      instanceUrl,
      pieceName,
      props,
      pieceAuthType
    });

    ```

    Implementation:

    ```js  theme={null}
    async function getOrCreateProject({
        projectExternalId,
        apiKey,
        instanceUrl,
    }: {
        projectExternalId: string,
        apiKey: string,
        instanceUrl: string
    }): Promise<{ id: string, externalId: string }> {

        const projects = await fetch(`${instanceUrl}/api/v1/projects?externalId=${projectExternalId}`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            },
        })
            .then(response => response.json())
            .then(data => data.data)
            .catch(err => {
                console.error('Error fetching projects:', err);
                return [];
            });

        if (projects.length > 0) {
            return {
                id: projects[0].id,
                externalId: projects[0].externalId
            };
        }

        const newProject = await fetch(`${instanceUrl}/api/v1/projects`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                displayName: projectExternalId,
                metadata: {},
                externalId: projectExternalId
            })
        })
            .then(response => response.json())
            .catch(err => {
                console.error('Error creating project:', err);
                throw err;
            });

        return {
            id: newProject.id,
            externalId: newProject.externalId
        };
    } 

    async function createGlobalConnection({
        projectId,
        externalProjectId,
        apiKey,
        instanceUrl,
        pieceName,
        props,
        pieceAuthType
    }: {
        projectId: string,
        externalProjectId: string,
        apiKey: string,
        instanceUrl: string,
        pieceName: string,
        props: Record<string, any>,
        pieceAuthType
    }) {

        const displayName = 'Gelato Connection';
        const connectionExternalId = 'gelato_' + externalProjectId;

        return fetch(`${instanceUrl}/api/v1/global-connections`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                displayName,
                pieceName,
                metadata: {},
                type: pieceAuthType,
                value: {
                    type: pieceAuthType,
                    props
                },
                scope: 'PLATFORM',
                projectIds: [projectId],
                externalId: connectionExternalId
            })
        });
    }
    ```
  </Step>
</Steps>

### Hide the Connections Dropdown (Optional)

<Steps>
  <Step title="Modify Trigger / Action Definition">
    Wherever you call `createTrigger` or `createAction` set `requireAuth` to `false`, this will hide the connections dropdown in the piece settings in the builder,
    next we need to fetch it based on a naming convention.
  </Step>

  <Step title="Fetch the connection">
    Here is example how you can fetch the connection value based on naming convention, make sure this naming convention is followed when creating a global connection.

    ```js  theme={null}
    import {
       ConnectionsManager,
       Property,
       TriggerStrategy
    } from "@activepieces/pieces-framework";
    import {
       createTrigger
    } from "@activepieces/pieces-framework";
    import {
       isNil
    } from "@activepieces/shared";
    // Add this import from the index.ts file, where it contains the definition of the auth object.
    import { auth } from '../..';

    const fetchConnection = async (
    	connections: ConnectionsManager,
    	projectExternalId: string | undefined,
    ): Promise<PiecePropValueSchema<typeof auth>> => {
    	if (isNil(projectExternalId)) {
    		throw new Error('This project is missing an external id');
    	}
    	// the naming convention here is gelato_projectExternalId
    	const connection = await connections.get(`gelato_${projectExternalId}`);
    	if (isNil(connection)) {
    		throw new Error(`Connection not found for project ${projectExternalId}`);
    	}

    	return connection as PiecePropValueSchema<typeof auth>;
    };


    export const newFlavorCreated = createTrigger({
       requireAuth: false,
       name: 'newFlavorCreated',
       displayName: 'new flavor created',
       description: 'triggers when a new icecream flavor is created.',
       props: {
          dropdown: Property.Dropdown({
             displayName: 'Dropdown',
             required: true,
             refreshers: [],
             options: async (_, {
                connections,
                project
             }) => {
                const connection = await fetchConnection(connections, (await project.externalId()));
                // your logic
                return {
                   options: [{
                      label: 'test',
                      value: 'test'
                   }]
                }
             }
          })
       },
       sampleData: {},
       type: TriggerStrategy.POLLING,
       async test({connections,project}) {
          const connection = await fetchConnection(connections, (await project.externalId()));
          // use the connection with your own logic
          return []
       },
       async onEnable({connections,project}) {
          const connection = await fetchConnection(connections, (await project.externalId()));
          // use the connection with your own logic
       },

       async onDisable({connections,project}) {
          const connection = await fetchConnection(connections, (await project.externalId()));
          // use the connection with your own logic
       },

       async run({connections,project}) {
        const connection = await fetchConnection(connections, (await project.externalId()));
          // use the connection with your own logic
          return []
       },
    });
    ```
  </Step>
</Steps>


# Provision Users
Source: https://www.activepieces.com/docs/embedding/provision-users

Automatically authenticate your SaaS users to your Activepieces instance

<Snippet file="enterprise-feature.mdx" />

## Overview

In Activepieces, there are **Projects** and **Users**. Each project is provisioned with their corresponding workspace, project, or team in your SaaS. The users are then mapped to the respective users in Activepieces.

To achieve this, the backend will generate a signed token that contains all the necessary information to automatically create a user and project. If the user or project already exists, it will skip the creation and log in the user directly.

<Steps>
  <Step title="Step 1: Obtain Signing Key">
    You can generate a signing key by going to **Platform Settings -> Signing Keys -> Generate Signing Key**.

    This will generate a public and private key pair. The public key will be used by Activepieces to verify the signature of the JWT tokens you send. The private key will be used by you to sign the JWT tokens.

        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-signing-key.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=2146a966a36cf2e3cc2c9b38ac74be8e" alt="Create Signing Key" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/create-signing-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-signing-key.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3d2b33b383c4e0f5447e4a91ba0fda75 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-signing-key.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=12a14d0b34bebe2fa2d1b892780c10c5 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-signing-key.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=8ba571040baf3f3f09b45dfa4bf0a0f1 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-signing-key.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=80dc36826ac3d116096a6f41f265b19a 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-signing-key.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=cb24d71a6f4c47d87b84eb06ec7a674a 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/create-signing-key.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e951422b1b7e4193ad6aa5556d023437 2500w" />

    <Warning>
      Please store your private key in a safe place, as it will not be stored in Activepieces.
    </Warning>
  </Step>

  <Step title="Step 2: Generate a JWT">
    The signing key will be used to generate JWT tokens for the currently logged-in user on your website, which will then be sent to the Activepieces Iframe as a query parameter to authenticate the user and exchange the token for a longer lived token.

    To generate these tokens, you will need to add code in your backend to generate the token using the RS256 algorithm, so the JWT header would look like this:

    <Tip>
      To obtain the `SIGNING_KEY_ID`, refer to the signing key table and locate the value in the first column.
      <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/signing-key-id.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=bd1f93195c14e25fd91710fb386f5b46" alt="Signing Key ID" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/signing-key-id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/signing-key-id.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b3d91cc4aa415c00bcd81d2505371538 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/signing-key-id.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=bddae17b3079768a2b7ef2792763666e 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/signing-key-id.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7374263ba089a74dd10dafe313e9b6cf 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/signing-key-id.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e2bf0b0c07680b91a6bf3a6f7ffb1150 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/signing-key-id.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b5223cfbb2841bbb97c189cb69281a3e 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/signing-key-id.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=152f7c8deff439e2d797537b9f8dc9fc 2500w" />
    </Tip>

    ```json  theme={null}
    {
      "alg": "RS256",
      "typ": "JWT",
      "kid": "SIGNING_KEY_ID"
    }
    ```

    The signed tokens must include these claims in the payload:

    ```json  theme={null}
    {
      "version": "v3",
      "externalUserId": "user_id",
      "externalProjectId": "user_project_id",
      "firstName": "John",
      "lastName": "Doe",
      "role": "EDITOR",
      "piecesFilterType": "NONE",
      "exp": 1856563200,
      "tasks": 50000,
      "aiCredits": 250
    }
    ```

    | Claim              | Description                                                                            |
    | ------------------ | -------------------------------------------------------------------------------------- |
    | externalUserId     | Unique identification of the user in **your** software                                 |
    | externalProjectId  | Unique identification of the user's project in **your** software                       |
    | projectDisplayName | Display name of the user's project                                                     |
    | firstName          | First name of the user                                                                 |
    | lastName           | Last name of the user                                                                  |
    | role               | Role of the user in the Activepieces project (e.g., **EDITOR**, **VIEWER**, **ADMIN**) |
    | exp                | Expiry timestamp for the token (Unix timestamp)                                        |
    | piecesFilterType   | Customize the project pieces, check [customize pieces](/embedding/customize-pieces)    |
    | piecesTags         | Customize the project pieces, check [customize pieces](/embedding/customize-pieces)    |
    | tasks              | Customize the tasks limit for your user's project                                      |
    | aiCredits          | Customize the ai credits limit for your user's project                                 |

    You can use any JWT library to generate the token. Here is an example using the jsonwebtoken library in Node.js:

    <Tip>
      **Friendly Tip #1**: You can also use this [tool](https://dinochiesa.github.io/jwt/) to generate a quick example.
    </Tip>

    <Tip>
      **Friendly Tip #2**: Make sure the expiry time is very short, as it's a temporary token and will be exchanged for a longer-lived token.
    </Tip>

    ```javascript Node.js theme={null}
    const jwt = require('jsonwebtoken');

    // JWT NumericDates specified in seconds:
    const currentTime = Math.floor(Date.now() / 1000);
    let token = jwt.sign(
      {
        version: "v3",
        externalUserId: "user_id",
        externalProjectId: "user_project_id",
        firstName: "John",
        lastName: "Doe",
        role: "EDITOR",
        piecesFilterType: "NONE",
        exp: currentTime + (60 * 60), // 1 hour from now
      },
      process.env.ACTIVEPIECES_SIGNING_KEY,
      {
        algorithm: "RS256",
        header: {
          kid: signingKeyID, // Include the "kid" in the header
        },
      }
    );
    ```

    Once you have generated the token, please check the embedding docs to know how to embed the token in the iframe.
  </Step>
</Steps>


# SDK Changelog
Source: https://www.activepieces.com/docs/embedding/sdk-changelog

A log of all notable changes to Activepieces SDK

<Warning>
  **Breaking Change:** <br /> <br /> If your Activepieces image version is \< 0.45.0 and (you are using the connect method from the embed SDk, and need the connection externalId to be returned after the user creates it OR if you want to reconnect a specific connection with an externalId), you must upgrade your Activepieces image to >= 0.45.0
</Warning>

<Warning>
  Between Acitvepieces image version 0.32.1 and 0.46.4 the navigation handler was including the project id in the path, this might have broken implementation logic for people using the navigation handler, this has been fixed from 0.46.5 and onwards, the handler won't show the project id prepended to routes.
</Warning>

Change log format: MM/DD/YYYY (version)

### 10/27/2025 (0.8.1)

* SDK URL: [https://cdn.activepieces.com/sdk/embed/0.8.1.js](https://cdn.activepieces.com/sdk/embed/0.8.1.js)
* Fixed a bug where if you didn't start your navigation route with '/' it would redirect you to '/flows'

### 09/21/2025 (0.8.0)

* SDK URL: [https://cdn.activepieces.com/sdk/embed/0.8.0.js](https://cdn.activepieces.com/sdk/embed/0.8.0.js)
* This version requires you to **upgrade Activepieces to [0.70.0](https://github.com/activepieces/activepieces/releases/tag/0.70.0)**.
* Removed `embedding.dashboard.hideSettings`.
* Added `embedding.dashboard.hidePageHeader` parameter to the [configure](./embed-builder#configure-parameters) method **(value: true | false)**.

### 07/30/2025 (0.7.0)

* SDK URL: [https://cdn.activepieces.com/sdk/embed/0.7.0.js](https://cdn.activepieces.com/sdk/embed/0.7.0.js)
* This version requires you to **upgrade Activepieces to [0.66.7](https://github.com/activepieces/activepieces/releases/tag/0.66.7)**
* Added `embedding.dashboard.hideSettings` parameter to the [configure](./embed-builder#configure-parameters) method **(value: true | false)**.

### 07/07/2025 (0.6.0)

* SDK URL: [https://cdn.activepieces.com/sdk/embed/0.6.0.js](https://cdn.activepieces.com/sdk/embed/0.6.0.js)
* This version requires you to **upgrade Activepieces to [0.66.1](https://github.com/activepieces/activepieces/releases/tag/0.66.1)**
* Added `embedding.dashboard.hideFlowsPageNavbar` parameter to the [configure](./embed-builder#configure-parameters) method **(value: true | false)**.
* **(Breaking Change)** `embedding.dashboard.hideSidebar` used to hide the navbar above the flows table in the dashboard now it relies on `embedding.dashboard.hideFlowsPageNavbar`.

### 03/07/2025 (0.5.0)

* SDK URL: [https://cdn.activepieces.com/sdk/embed/0.5.0.js](https://cdn.activepieces.com/sdk/embed/0.5.0.js)
* This version requires you to **upgrade Activepieces to [0.64.2](https://github.com/activepieces/activepieces/releases/tag/0.64.2)**
* Added `embedding.hideDuplicateFlow` parameter to the [configure](./embed-builder#configure-parameters) method **(value: true | false)**.
* Added `embedding.builder.homeButtonIcon` parameter to the [configure](./embed-builder#configure-parameters) method **(value: 'logo' | 'back')**, if set to **'back'** the tooltip shown on hovering the home button is removed.
* Added `embedding.locale` parameter to the [configure](./embed-builder#configure-parameters) method, it takes [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) locale codes, here are the ones supported: **('en' | 'nl' | 'it' | 'de' | 'fr' | 'bg' | 'uk' | 'hu' | 'es' | 'ja' | 'id' | 'vi' | 'zh' | 'pt')**
* Added `embedding.styling.mode` parameter to [configure](./embed-builder#configure-parameters) method **(value: 'light' | 'dark')**
* **(Breaking Change)** Removed `embedding.builder.hideLogo` parameter from the [configure](./embed-builder#configure-parameters) method.
* **(Breaking Change)** Removed MCP methods from sdk.

### 17/06/2025 (0.5.0-rc.1)

* SDK URL: [https://cdn.activepieces.com/sdk/embed/0.5.0-rc.1.js](https://cdn.activepieces.com/sdk/embed/0.5.0-rc.1.js)
* This version requires you to **upgrade Activepieces to [0.64.0-rc.0](https://github.com/activepieces/activepieces/pkgs/container/activepieces/438888138?tag=0.64.0-rc.0)**
* Revert back the `prefix` parameter from the [configure](./embed-builder#configure-parameters) method.

### 16/06/2025 (0.5.0-rc.0)

* SDK URL: [https://cdn.activepieces.com/sdk/embed/0.5.0-rc.0.js](https://cdn.activepieces.com/sdk/embed/0.5.0-rc.0.js)
* This version requires you to **upgrade Activepieces to [0.64.0-rc.0](https://github.com/activepieces/activepieces/pkgs/container/activepieces/438888138?tag=0.64.0-rc.0)**
* Added `embedding.hideDuplicateFlow` parameter to the [configure](./embed-builder#configure-parameters) method **(value: true | false)**.
* Added `embedding.builder.homeButtonIcon` parameter to the [configure](./embed-builder#configure-parameters) method **(value: 'logo' | 'back')**, if set to **'back'** the tooltip shown on hovering the home button is removed.
* Added `embedding.locale` parameter to the [configure](./embed-builder#configure-parameters) method, it takes [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) locale codes, here are the ones supported: **('en' | 'nl' | 'it' | 'de' | 'fr' | 'bg' | 'uk' | 'hu' | 'es' | 'ja' | 'id' | 'vi' | 'zh' | 'pt')**
* Added `embedding.styling.mode` parameter to [configure](./embed-builder#configure-parameters) method **(value: 'light' | 'dark')**
* **(Breaking Change)** Removed `prefix` parameter from the [configure](./embed-builder#configure-parameters) method.
* **(Breaking Change)** Removed `embedding.builder.hideLogo` parameter from the [configure](./embed-builder#configure-parameters) method.

### 26/05/2025 (0.4.1)

* Fixed an issue where sometimes the embed HTML file was getting cached.

### 20/05/2025 (0.4.0)

\-- Note: we didn't consider adding optional new parameters as a breaking change so we were bumping the patch version, but that was wrong and we will begin bumping the minor version for those changes from now on, and patch version will only get bumped for bug fixes.

* This version requires you to update Activepieces to 0.56.0
* Added `embedding.hideExportAndImportFlow` parameter to the [configure](./embed-builder#configure-parameters) method.
* Added new possible value to the configure method param `embed.builder.disableNavigation` which is "keep\_home\_button\_only" that keeps only the home button and hides the folder name with the delete flow action.
* Added new param to the configure method `embed.builder.homeButtonClickedHandler`, that overrides the navigation behaviour on clicking the home button.

### 17/04/2025 (0.3.7)

* Added MCP methods to update MCP configurations.

### 16/04/2025 (0.3.6)

* Added the [request](./sdk-server-requests) method which allows you to call our backend API.

### 24/2/2025 (0.3.5)

* Added a new parameter to the connect method to make the connection dialog a popup instead of an iframe taking the full page.
* Fixed a bug where the returned promise from the connect method was always resolved to \{connection: undefined}
* Now when you use the connect method with the "connectionName" parameter, the user will reconnect to the connection with the matching externalId instead of creating a new one.

### 04/02/2025 (0.3.4)

* This version requires you to update Activepieces to 0.41.0
* Adds the ability to pass font family name and font url to the embed sdk

### 26/01/2025 (0.3.3)

* This version requires you to update Activepieces to 0.39.8
* activepieces.configure method was being resolved before the user was authenticated, this is fixed now, so you can use activepieces.navigate method to navigate to your desired initial route.

### 04/12/2024 (0.3.0)

* add custom navigation handler ([#4500](https://github.com/activepieces/activepieces/pull/4500))
* allow passing a predefined name for connection in connect method ([#4485](https://github.com/activepieces/activepieces/pull/4485))
* add changelog ([#4503](https://github.com/activepieces/activepieces/pull/4503))


# API Requests
Source: https://www.activepieces.com/docs/embedding/sdk-server-requests

Send requests to your Activepieces instance from the embedded app

<Info>
  **Requirements:**

  * Activepieces version 0.34.5 or higher
  * SDK version 0.3.6 or higher
</Info>

You can use the embedded SDK to send requests to your instance and retrieve data.

<Steps>
  <Step title="Initialize the SDK">
    Follow the instructions in the [Embed Builder](./embed-builder) to initialize the SDK.
  </Step>

  <Step title="Call (request) Method">
    ```html  theme={null}
    <script> 
    activepieces.request({path:'/flows',method:'GET'}).then(console.log);
    </script>
    ```

    **Request Parameters:**

    | Parameter Name | Required | Type                   | Description                                                                                         |
    | -------------- | -------- | ---------------------- | --------------------------------------------------------------------------------------------------- |
    | path           | ✅        | string                 | The path within your instance you want to hit (we prepend the path with your\_instance\_url/api/v1) |
    | method         | ✅        | string                 | The http method to use 'GET', 'POST','PUT', 'DELETE', 'OPTIONS', 'PATCH' and 'HEAD                  |
    | body           | ❌        | JSON object            | The json body of your request                                                                       |
    | queryParams    | ❌        | Record\<string,string> | The query params to include in your request                                                         |
  </Step>
</Steps>


# Delete Connection
Source: https://www.activepieces.com/docs/endpoints/connections/delete

DELETE /v1/app-connections/{id}
Delete an app connection



# List Connections
Source: https://www.activepieces.com/docs/endpoints/connections/list

GET /v1/app-connections
List app connections



# Connection Schema
Source: https://www.activepieces.com/docs/endpoints/connections/schema





# Upsert Connection
Source: https://www.activepieces.com/docs/endpoints/connections/upsert

POST /v1/app-connections
Upsert an app connection based on the app name



# Get Flow Run
Source: https://www.activepieces.com/docs/endpoints/flow-runs/get

GET /v1/flow-runs/{id}
Get Flow Run



# List Flows Runs
Source: https://www.activepieces.com/docs/endpoints/flow-runs/list

GET /v1/flow-runs
List Flow Runs



# Flow Run Schema
Source: https://www.activepieces.com/docs/endpoints/flow-runs/schema





# Create Flow Template
Source: https://www.activepieces.com/docs/endpoints/flow-templates/create

POST /v1/flow-templates
Create a flow template



# Delete Flow Template
Source: https://www.activepieces.com/docs/endpoints/flow-templates/delete

DELETE /v1/flow-templates/{id}
Delete a flow template



# Get Flow Template
Source: https://www.activepieces.com/docs/endpoints/flow-templates/get

GET /v1/flow-templates/{id}
Get a flow template



# List Flow Templates
Source: https://www.activepieces.com/docs/endpoints/flow-templates/list

GET /v1/flow-templates
List flow templates



# Flow Template Schema
Source: https://www.activepieces.com/docs/endpoints/flow-templates/schema





# Create Flow
Source: https://www.activepieces.com/docs/endpoints/flows/create

POST /v1/flows
Create a flow



# Delete Flow
Source: https://www.activepieces.com/docs/endpoints/flows/delete

DELETE /v1/flows/{id}
Delete a flow



# Get Flow
Source: https://www.activepieces.com/docs/endpoints/flows/get

GET /v1/flows/{id}
Get a flow by id



# List Flows
Source: https://www.activepieces.com/docs/endpoints/flows/list

GET /v1/flows
List flows



# Flow Schema
Source: https://www.activepieces.com/docs/endpoints/flows/schema





# Apply Flow Operation
Source: https://www.activepieces.com/docs/endpoints/flows/update

POST /v1/flows/{id}
Apply an operation to a flow



# Create Folder
Source: https://www.activepieces.com/docs/endpoints/folders/create

POST /v1/folders
Create a new folder



# Delete Folder
Source: https://www.activepieces.com/docs/endpoints/folders/delete

DELETE /v1/folders/{id}
Delete a folder



# Get Folder
Source: https://www.activepieces.com/docs/endpoints/folders/get

GET /v1/folders/{id}
Get a folder by id



# List Folders
Source: https://www.activepieces.com/docs/endpoints/folders/list

GET /v1/folders
List folders



# Folder Schema
Source: https://www.activepieces.com/docs/endpoints/folders/schema





# Update Folder
Source: https://www.activepieces.com/docs/endpoints/folders/update

POST /v1/folders/{id}
Update an existing folder



# Configure
Source: https://www.activepieces.com/docs/endpoints/git-repos/configure

POST /v1/git-repos
Upsert a git repository information for a project.



# Git Repos Schema
Source: https://www.activepieces.com/docs/endpoints/git-repos/schema





# Delete Global Connection
Source: https://www.activepieces.com/docs/endpoints/global-connections/delete

DELETE /v1/global-connections/{id}



# List Global Connections
Source: https://www.activepieces.com/docs/endpoints/global-connections/list

GET /v1/global-connections



# Global Connection Schema
Source: https://www.activepieces.com/docs/endpoints/global-connections/schema





# Update Global Connection
Source: https://www.activepieces.com/docs/endpoints/global-connections/update

POST /v1/global-connections/{id}



# Upsert Global Connection
Source: https://www.activepieces.com/docs/endpoints/global-connections/upsert

POST /v1/global-connections



# List MCP servers
Source: https://www.activepieces.com/docs/endpoints/mcp-servers/list

GET /v1/mcp-servers
List MCP servers



# Rotate MCP server token
Source: https://www.activepieces.com/docs/endpoints/mcp-servers/rotate

POST /v1/mcp-servers/{id}/rotate
Rotate the MCP token



# MCP Server Schema
Source: https://www.activepieces.com/docs/endpoints/mcp-servers/schema





# Update MCP Server
Source: https://www.activepieces.com/docs/endpoints/mcp-servers/update

POST /v1/mcp-servers/{id}
Update the project MCP server configuration



# Overview
Source: https://www.activepieces.com/docs/endpoints/overview



<Tip>
  API keys are generated under the platform dashboard at this moment to manage multiple projects, which is only available in the Platform and Enterprise editions,
  Please contact [sales@activepieces.com](mailto:sales@activepieces.com) for more information.
</Tip>

### Authentication:

The API uses "API keys" to authenticate requests. You can view and manage your API keys from the Platform Dashboard. After creating the API keys, you can pass the API key as a Bearer token in the header.

Example:
`Authorization: Bearer {API_KEY}`

### Pagination

All endpoints use seek pagination, to paginate through the results, you can provide the `limit` and `cursor` as query parameters.

The API response will have the following structure:

```json  theme={null}
{
    "data": [],
    "next": "string",
    "previous": "string"
}
```

* **`data`**: Holds the requested results or data.

* **`next`**: Provides a starting cursor for the next set of results, if available.

* **`previous`**: Provides a starting cursor for the previous set of results, if applicable.


# Install Piece
Source: https://www.activepieces.com/docs/endpoints/pieces/install

POST /v1/pieces
Add a piece to a platform



# Piece Schema
Source: https://www.activepieces.com/docs/endpoints/pieces/schema





# Delete Project Member
Source: https://www.activepieces.com/docs/endpoints/project-members/delete

DELETE /v1/project-members/{id}



# List Project Member
Source: https://www.activepieces.com/docs/endpoints/project-members/list

GET /v1/project-members



# Project Member Schema
Source: https://www.activepieces.com/docs/endpoints/project-members/schema





# Create Project Release
Source: https://www.activepieces.com/docs/endpoints/project-releases/create

POST /v1/project-releases



# Project Release Schema
Source: https://www.activepieces.com/docs/endpoints/project-releases/schema





# Create Project
Source: https://www.activepieces.com/docs/endpoints/projects/create

POST /v1/projects



# Delete Project
Source: https://www.activepieces.com/docs/endpoints/projects/delete

DELETE /v1/projects/{id}



# List Projects
Source: https://www.activepieces.com/docs/endpoints/projects/list

GET /v1/projects



# Project Schema
Source: https://www.activepieces.com/docs/endpoints/projects/schema





# Update Project
Source: https://www.activepieces.com/docs/endpoints/projects/update

POST /v1/projects/{id}



# Queue Stats
Source: https://www.activepieces.com/docs/endpoints/queue-metrics/metrics

GET /v1/queue-metrics
Get metrics



# Get Sample Data
Source: https://www.activepieces.com/docs/endpoints/sample-data/get

GET /v1/sample-data



# Delete User Invitation
Source: https://www.activepieces.com/docs/endpoints/user-invitations/delete

DELETE /v1/user-invitations/{id}



# List User Invitations
Source: https://www.activepieces.com/docs/endpoints/user-invitations/list

GET /v1/user-invitations



# User Invitation Schema
Source: https://www.activepieces.com/docs/endpoints/user-invitations/schema





# Send User Invitation (Upsert)
Source: https://www.activepieces.com/docs/endpoints/user-invitations/upsert

POST /v1/user-invitations
Send a user invitation to a user. If the user already has an invitation, the invitation will be updated.



# List Users
Source: https://www.activepieces.com/docs/endpoints/users/list

GET /v1/users
List users



# User Schema
Source: https://www.activepieces.com/docs/endpoints/users/schema





# Update User
Source: https://www.activepieces.com/docs/endpoints/users/update

POST /v1/users/{id}



# Building Flows
Source: https://www.activepieces.com/docs/flows/building-flows

Flow consists of two parts, trigger and actions

## Trigger

The flow's starting point determines its frequency of execution. There are various types of triggers available, such as Schedule Trigger, Webhook Trigger, or Event Trigger based on specific service.

## Action

Actions come after the flow and control what occurs when the flow is activated, like running code or communicating with other services.

In real-life scenario:

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-parts.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=91002b43854c0692dfa97093210f7758" alt="Flow Parts" data-og-width="1190" width="1190" data-og-height="1026" height="1026" data-path="resources/flow-parts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-parts.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=fb7004ca4b33fadc51a5917f941499cb 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-parts.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=ccc3ef72de0af2923cf7c9e4aa0f76b4 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-parts.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=2f0fa784bd525a2bb45210744ac291bd 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-parts.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=fa7ef73fce399243155d8ba4738c75e0 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-parts.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=d93aca188ef10e5a807e737cf70e2141 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-parts.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=947bdbac576d57f46c991363d082b1df 2500w" />


# Debugging Runs
Source: https://www.activepieces.com/docs/flows/debugging-runs

Ensuring your business automations are running properly

You can monitor each run that results from an enabled flow:

1. Go to the Dashboard, click on **Runs**.
2. Find the run that you're looking for, and click on it.
3. You will see the builder in a view-only mode, each step will show a ✅ or a ❌ to indicate its execution status.
4. Click on any of these steps, you will see the **input** and **output** in the **Run Details** panel.

The debugging experience looks like this:
<img src="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/screenshots/using-activepieces-debugging.png?fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=1ca6ba93a4c1eed347626116b6a102c2" alt="Debugging Business Automations" data-og-width="2880" width="2880" data-og-height="1642" height="1642" data-path="resources/screenshots/using-activepieces-debugging.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/screenshots/using-activepieces-debugging.png?w=280&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=227dd11b4ecf414d7c68467eb0167b70 280w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/screenshots/using-activepieces-debugging.png?w=560&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=abc74e55dc2f3687ea49be734712eff6 560w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/screenshots/using-activepieces-debugging.png?w=840&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=14ac5ece3d44da0e591f4db183455936 840w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/screenshots/using-activepieces-debugging.png?w=1100&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=26863c804032aebd4cbd1f872a1e2147 1100w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/screenshots/using-activepieces-debugging.png?w=1650&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=0972b746f60677ffea409cda9177dac2 1650w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/screenshots/using-activepieces-debugging.png?w=2500&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=75013f1b03c2a47dedff56bda1b9631b 2500w" />


# Technical Limits
Source: https://www.activepieces.com/docs/flows/known-limits

Technical limits for Activepieces execution

### Execution Limits

* **Flow Execution Time**\
  Maximum: **600 seconds (10 minutes)**\
  Flows exceeding this limit will be marked as timed out.

* **Memory Usage**\
  Maximum: **1 GB RAM**\
  (Self hosted can be configured via `AP_SANDBOX_MEMORY_LIMIT`)

<Note>
  The memory usage is measured for the entire Node.js process running the flow. There is approximately 300 MB of overhead for a warm process with pieces already loaded.
</Note>

<Tip>
  **Note 1:** Flows paused by steps like **Wait for Approval** or **Delay** do **not** count toward the 600-second limit.
</Tip>

<Tip>
  **Note 2:** To handle longer processes, split them into multiple flows.\
  For example:

  * Have one flow call another via **webhook**.
  * Process smaller **batches of items** in separate flows.
</Tip>

***

### File Storage Limits

<Info>
  Files from actions or triggers are stored in the database/S3 to support retries for certain steps.
</Info>

* **Maximum File Size**: **10 MB**\
  (Configurable via `AP_MAX_FILE_SIZE_MB`, default: **4 MB**)

***

### Key / Value Storage Limits

Some pieces use the built-in Activepieces key store (e.g., **Store Piece**, **Queue Piece**).

* **Maximum Key Length**: **128 characters**
* **Maximum Value Size**: **512 KB**


# Passing Data
Source: https://www.activepieces.com/docs/flows/passing-data

Using data from previous steps in the current one

## Data flow

Any Activepieces flow is a vertical diagram that **starts with a trigger step** followed by **any number of action steps**.

Steps are connected vertically. Data flows from parent steps to the children. Children steps have access to the output data of the parent steps.

## Example Steps

<video width="450" autoPlay muted loop playsinline src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-3steps.mp4?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=525e82220343a9d0e119dd469dc998c1" data-path="resources/passing-data-3steps.mp4" />

This flow has 3 steps, they can access data as follows:

* **Step 1** is the main data producer to be used in the next steps. Data produced by Step 1 will be accessible in Steps 2 and 3. Some triggers don't produce data though, like Schedules.

* **Step 2** can access data produced by Step 1. After execution, this step will also produce data to be used in the next step(s).

* **Step 3** can access data produced by Steps 1 and 2 as they're its parent steps. This step can produce data but since it's the last step in the flow, it can't be used by other ones.

## Data to Insert Panel

In order to use data from a previous step in your current step, place your cursor in any input, the **Data to Insert** panel will pop up.

<video autoPlay muted loop playsinline src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-data-to-insert-panel.mp4?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=3d46b25cb67d411f95ee083d71fc447c" data-path="resources/passing-data-data-to-insert-panel.mp4" />

This panel shows the accessible steps and their data. You can expand the data items to view their content, and you can click the items to insert them in your current settings input.

If an item in this panel has a caret (⌄) to the right, it means you can click on the item to expand its child properties. You can select the parent item or its properties as you need.

When you insert data from this panel, it gets inserted at the cursor's position in the input. This means you can combine static text and dynamic data in any field.

<video autoPlay muted loop playsinline src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-main-insert-data-example.mp4?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=2ae302d3f0edd883c207ffbf1dabee7a" data-path="resources/passing-data-main-insert-data-example.mp4" />

We generally recommend that you expand the items before inserting them to understand the type of data they contain and whether they're the right fit to the input you're filling.

## Testing Steps to Generate Data

We require you to test steps before accessing their data. This approach protects you from selecting the wrong data and breaking your flows after publishing them.

If a step is not tested and you try to access its data, you will see the following message:

<img width="350" src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=3bc8bb574124a5a119ba97ae4995acc8" alt="Test your automation step first" data-og-width="798" data-og-height="988" data-path="resources/passing-data-test-step-first.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=cabf8db7e71bab1723dc2799e1de0e29 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=395766bb57845ebb1d0e6c6aa176ed7f 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=34a3bce214b6665784158841a0c0598e 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=330141a5e22a170def0fedaf1c268def 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=4f2dee5f9d48e411fe12805e063a4ed3 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-test-step-first.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=04841ffe0b6ca0ba9835947574e951b7 2500w" />

To fix this, go to the step and use the Generate Sample Data panel to test it. Steps use different approaches for testing. These are the common ones:

* **Load Data:** Some triggers will let you load data from your connected account without having to perform any action in that account.
* **Test Trigger:** Some triggers will require you to head to your connected account and fire the trigger in order to generate sample data.
* **Send Data:** Webhooks require you to send a sample request to the webhook URL to generate sample data.
* **Test Action:** Action steps will let you run the action in order to generate sample data.

Follow the instructions in the Generate Sample Data panel to know how your step should be tested. Some triggers will also let you Use Mock Data, which will generate static sample data from the piece. We recommend that you test the step instead of using mock data.

This is an example for generating sample data for a trigger using the **Load Data** button:

<video autoPlay muted loop playsinline src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-load-data.mp4?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=318c97848c527caceb7186d926d50af7" data-path="resources/passing-data-load-data.mp4" />

## Advanced Tips

### Switching to Dynamic Values

Dropdowns and some other input types don't let you select data from previous steps. If you'd like to bypass this and use data from previous steps instead, switch the input into a dynamic one using this button:

<video autoPlay muted loop playsinline src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/passing-data-dynamic-value.mp4?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=e25b49eb497509a2267dc9bd39cb3240" data-path="resources/passing-data-dynamic-value.mp4" />

### Accessing data by path

If you can't find the data you're looking for in the **Data to Insert** panel but you'd like to use it, you can write a JSON path instead.

Use the following syntax to write JSON paths:

`{{step_slug.path.to.property}}`

The `step_slug` can be found by moving your cursor over any of your flow steps, it will show to the right of the step.


# Publishing Flows
Source: https://www.activepieces.com/docs/flows/publishing-flows

Make your flow work by publishing your updates

The changes you make won't work right away to avoid disrupting the flow that's already published. To enable your changes, simply click on the publish button once you're done with your changes.

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/publish-flow.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=5919308ee42dd2a8b034e3f10c74f2a0" alt="Flow Parts" data-og-width="802" width="802" data-og-height="402" height="402" data-path="resources/publish-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/publish-flow.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=45bda33a231ec2bdc1f843ea1b0540d6 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/publish-flow.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=3dcfbd55219e9836c046d2e6a769fde0 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/publish-flow.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=c0400e12be4aa89c866aba03a10594eb 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/publish-flow.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=4f1754569e994ce6a89576fe50447587 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/publish-flow.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=2ce7fce9fc5f91f9aa057bac2ccbe7bd 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/publish-flow.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=c6b7f714c07a8c6786ef56dd6886047a 2500w" />


# Version History
Source: https://www.activepieces.com/docs/flows/versioning

Learn how flow versioning works in Activepieces

Activepieces keeps track of all published flows and their versions. Here’s how it works:

1. You can edit a flow as many times as you want in **draft** mode.
2. Once you're done with your changes, you can publish it.
3. The published flow will be **immutable** and cannot be edited.
4. If you try to edit a published flow, Activepieces will create a new **draft** if there is none and copy the **published** version to the new version.

This means you can always go back to a previous version and edit the flow in draft mode without affecting the published version.

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-history.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=4c9e91670db9365e93bb8b75f1f1e697" alt="Flow History" data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="resources/flow-history.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-history.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=ca50bf21ed60647e215faedd0fdd641e 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-history.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=95e7b7a4ba206f9a4e4fbb6880a83492 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-history.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=0c149d538508942f7a8481c36110b48b 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-history.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=707ec6249c84e7b89dea8d55ef43e4a1 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-history.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=ecef496a6299b12a50ae897814e31cfc 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/flow-history.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=167071f8391e6f6697198c7b63b68702 2500w" />

As you can see in the following screenshot, the yellow dot refers to DRAFT and the green dot refers to PUBLISHED.


# 🥳 Welcome to Activepieces
Source: https://www.activepieces.com/docs/getting-started/introduction

Your friendliest open source all-in-one automation tool, designed to be extensible.

<CardGroup cols={2}>
  <Card href="/flows/building-flows" title="Learn Concepts" icon="shapes" color="#8143E3">
    Learn how to work with Activepieces
  </Card>

  <Card href="https://www.activepieces.com/pieces" title="Pieces" icon="puzzle-piece" color="#8143E3">
    Browse available pieces
  </Card>

  <Card href="/install/overview" title="Install" icon="server" color="#8143E3">
    Learn how to install Activepieces
  </Card>

  <Card href="/developers/building-pieces/overview" title="Developers" icon="code" color="#8143E3">
    How to Build Pieces and Contribute
  </Card>
</CardGroup>

# 🔥 Why Activepieces is Different:

* **💖 Loved by Everyone**: Intuitive interface and great experience for both technical and non-technical users with a quick learning curve.

<img src="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/templates.gif?s=fd757d47135bd89176c05f19d551e449" alt="" data-og-width="1000" width="1000" data-og-height="484" height="484" data-path="resources/templates.gif" data-optimize="true" data-opv="3" />

* **🌐 Open Ecosystem:** All pieces are open source and available on npmjs.com, **60% of the pieces are contributed by the community**.

* **🛠️  Pieces are written in Typescript**: Pieces are npm packages in TypeScript, offering full customization with the best developer experience, including **hot reloading** for **local** piece development on your machine. 😎

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/create-action.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=86de2df0a46f609b603556e80d13d1d2" alt="" data-og-width="1450" width="1450" data-og-height="752" height="752" data-path="resources/create-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/create-action.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=54e99162279ac0c892daca018df3396e 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/create-action.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=035684dda0c008b4563f0de8325da847 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/create-action.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=d166e4c429238d4247f6cc2f307f5828 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/create-action.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=e324c1dfb217a5151b38cfabb8d76f89 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/create-action.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=48ca5658ef5fc2f9e4f0dda191c6259e 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/create-action.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=b9306752938ea71f9c990f7d23459e4f 2500w" />

* **🤖 AI-Ready**: Native AI pieces let you experiment with various providers, or create your own agents using our AI SDK to help you build flows inside the builder.

* **🏢 Enterprise-Ready**: Developers set up the tools, and anyone in the organization can use the no-code builder. Full customization from branding to control.

* **🔒 Secure by Design**: Self-hosted and network-gapped for maximum security and control over your data.

* **🧠 Human in Loop**: Delay execution for a period of time or require approval. These are just pieces built on top of the piece framework, and you can build many pieces like that. 🎨

* **💻 Human Input Interfaces**: Built-in support for human input triggers like "Chat Interface" 💬 and "Form Interface" 📝


# Product Principles
Source: https://www.activepieces.com/docs/getting-started/principles



## 🌟 Keep It Simple

* Design the product to be accessible for everyone, regardless of their background and technical expertise.

* The code is in a monorepository under one service, making it easy to develop, maintain, and scale.

* Keep the technology stack simple to achieve massive adoption.

* Keep the software unopinionated and unlock niche use cases by making it extensible through pieces.

## 🧩 Keep It Extensible

* Automation pieces framework has minimal abstraction and allow you to extend for any usecase.

* All contributions are welcome. The core is open source, and commercial code is available.


# How to handle Requests
Source: https://www.activepieces.com/docs/handbook/customer-support/handle-requests



As a support engineer, you should:

* Fix the urgent issues (please see the definition below)
* Open tickets for all non-urgent issues. **(DO NOT INCLUDE ANY SENSITIVE INFO IN ISSUE)**
* Keep customers updated
* Write clear ticket descriptions
* Help the team prioritize work
* Route issues to the right people

<Note>
  Our support hours are from **8 am to 6 pm New York time (ET)**. Please keep this in mind when communicating response expectations to customers.
</Note>

### Ticket fields

When handling support tickets, ensure you set the appropriate status and priority to help with ticket management and response time:

### Requests

### Type 1: Quick Fixes & Urgent Issues

* Understand the issue and how urgent it is.
* Open a ticket for on linear with "require attention" label and assign someone.

### Type 2: Complex Technical Issues

* Assess the issue and determine its urgency.
* Always create a Linear issue for the feature request, and send it to the customer.
* Leave a comment on the Linear issue with an estimated completion time.

### Type 3: Feature Enhancement Requests

* Always create a Linear issue for the feature request and send it to the customer.
* Evaluate the request and dig deeper into what the customer is trying to solve, then either evaluate and open a new ticket or append to an existing ticket in the backlog.
* Add it to our roadmap and discuss it with the team.

### Type 4: Business Case

* These cases involve purchasing new features, billing, or discussing agreements.
* Change the Team to "Success" on Pylon.
* Tag someone from the Success Team to handle it.

<Tip>
  New features will always have the status "Backlog". Please make sure to communicate that we will discuss and address it in future production cycles so the customer doesn't expect immediate action.
</Tip>

### Frequently Asked Questions

<AccordionGroup>
  <Accordion title="What if I don't understand the feature or issue?">
    If you don't understand the feature or issue, reach out to the customer for clarification. It's important to fully grasp the problem before proceeding. You can also consult with your team for additional insights.
  </Accordion>

  <Accordion title="How do I prioritize multiple urgent issues?">
    When faced with multiple urgent issues, assess the impact of each on the customer and the system. Prioritize based on severity, number of affected users, and potential risks. Communicate with your team to ensure alignment on priorities.
  </Accordion>

  <Accordion title="What if there is an angry or abusive customer?">
    If you encounter an abusive or rude customer, escalate the issue to Mohammad AbuAboud or Ashraf Samhouri. It's important to handle such situations with care and ensure that the customer feels heard while maintaining a respectful and professional demeanor.
  </Accordion>
</AccordionGroup>


# Overview
Source: https://www.activepieces.com/docs/handbook/customer-support/overview



At Activepieces, we take a unique approach to customer support. Instead of having dedicated support staff, our full-time engineers handle support requests on rotation. This ensures you get expert technical help from the people who build the product.

### Support Schedule

Our on-call engineer handles customer support as part of their rotation. For more details about how this works, check out our on-call documentation.

### Support Channels

* Community Support
  * GitHub Issues: We actively monitor and respond to issues on our [GitHub repository](https://github.com/activepieces/activepieces)
  * Community Forum: We engage with users on our [Community Platform](https://community.activepieces.com/) to provide help and gather feedback
  * Email: only for account related issues, delete account request or billing issues.

* Enterprise Support
  * Enterprise customers receive dedicated support through Slack
  * We use [Pylon](https://usepylon.com) to manage support tickets and customer channels efficiently
  * For detailed information on using Pylon, see our [Pylon Guide](/docs/handbook/customer-support/pylon)

### Support Hours & SLA:

<Warning>
  Work in progress—coming soon!
</Warning>


# How to use Pylon
Source: https://www.activepieces.com/docs/handbook/customer-support/pylon

Guide for using Pylon to manage customer support tickets

At Activepieces, we use Pylon to manage Slack-based customer support requests through a Kanban board.

Learn more about Pylon's features: [https://docs.usepylon.com/pylon-docs](https://docs.usepylon.com/pylon-docs)

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=5e653ec9a78ead22b3edc7f3cbac1a31" alt="Pylon board showing different columns for ticket management" data-og-width="1693" width="1693" data-og-height="1022" height="1022" data-path="resources/pylon-board.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=5afae234a251cddb52fbc2e98fd6f9df 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=edc15a6de060b8d731356098bf781b8b 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=ab9422f6444c07fe2739dd07f2b2059d 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=990ffc64f2da10c0c8bdb6659826ddbb 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=096a95126fe07af16cb9735913d688ab 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=8e737a78dc7abb9402b62abd98e1265f 2500w" />

### New Column

Contains new support requests that haven't been reviewed yet

* Action Items:
  * Respond fast even if you don't have an answer, the important thing here is to reply that you will take a look into it, the key to winning the customer's heart.

### On You Column

Contains active tickets that require your attention and response. These tickets need immediate review and action.

* Action items:
  * Set ticket fields (status and priority) according to the guide below
  * Check the [handle request page](./handle-requests) on how to handle tickets

<Tip>
  The goal as a support engineer is to keep the "New" and "On You" columns empty.
</Tip>

### On Hold

Contains only tickets that have a linked Linear issue.

* Place tickets here after:
  * You have identified the customer's issue
  * You have created a Linear issue (if one doesn't exist - avoid duplicates!)
  * You have linked the issue in Pylon
  * You have assigned it to a team member (for urgent cases only)

<Warning>
  Please do not place tickets on hold without a ticket.
</Warning>

<Note>
  Tickets will automatically move back to the "On You" column when the linked GitHub issue is closed.
</Note>

### Closed Column

This means you did awesome job and the ticket reached it's Final destination for resolved tickets and no further attention required.


# Tone & Communication
Source: https://www.activepieces.com/docs/handbook/customer-support/tone



Our customers are fellow engineers and great people to work with. This guide will help you understand the tone and communication style that reflects Activepieces' culture in customer support.

#### Casual

Chat with them like you're talking to a friend. There's no need to sound like a robot. For example:

* ✅ "Hey there! How can I help you today?"
* ❌ "Greetings. How may I assist you with your inquiry?"
* ✅ "No worries, we'll get this sorted out together!"
* ❌ "Please hold while I process your request."

#### Fast

Reply quickly! People love fast responses. Even if you don't know the answer right away, let them know you'll get back to them with the information. This is the fastest way to make customers happy; everyone likes to be heard.

#### Honest

Explain the issue clearly, don't be defensive, and be honest. We're all about open source and transparency here – it's part of our culture. For example:

* ✅ "I'm sorry, I forgot to follow up on this. Let's get it sorted out now."
* ❌ "I apologize for the delay; there were unforeseen circumstances."

### Always Communicate the Next Step

Always clarify the next step, such as whether the ticket will receive an immediate response or be added to the backlog for team discussion.

#### Use "we," not "I"

* ✅ "We made a mistake here. We'll fix that for you."
* ❌ "I'll look into this for you."
* You're speaking on behalf of the company in every email you send.
* Use "we" to show customers they have the whole team's support.

<Tip>
  Customers are real people who want to talk to real people. Be yourself, be helpful, and focus on solving their problems!
</Tip>


# Trial Key Management
Source: https://www.activepieces.com/docs/handbook/customer-support/trial

Description of your new file.

Please read more how to create development / production keys for the customer in the following document.

* [Trial Key Management Guide](https://docs.google.com/document/d/1k4-_ZCgyejS9UKA7AwkSB-l2TEZcnK2454o2joIgm4k/edit?tab=t.0#heading=h.ziaohggn8z8d): Includes detailed instructions on generating and extending 14-day trial keys.


# Handling Downtime
Source: https://www.activepieces.com/docs/handbook/engineering/onboarding/downtime-incident



![Downtime Incident](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTZnbGxjc3k5d3NxeXQwcmhxeTRsbnNybnd4NG41ZnkwaDdsa3MzeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2UCt7zbmsLoCXybx6t/giphy.gif)

## 📋 What You Need Before Starting

Make sure these are ready:

* **[Incident.io Setup](../playbooks/setup-incident-io)**: For managing incidents.
* **ClickStack**: For checking logs and errors.
* **Checkly Debugging**: For testing and monitoring.

***

## 🚨 Stay Calm and Take Action

<Warning>
  Don’t panic! Follow these steps to fix the issue.
</Warning>

1. **Tell Your Users**:
   * Let your users know there’s an issue. Post on [Community](https://community.activepieces.com) and Discord.
   * Example message: *“We’re looking into a problem with our services. Thanks for your patience!”*

2. **Find Out What’s Wrong**:
   * Gather details. What’s not working? When did it start?

3. **Update the Status Page**:
   * Use [Incident.io](https://incident.io) to update the status page. Set it to *“Investigating”* or *“Partial Outage”*.

***

## 🔍 Check for Infrastructure Problems

1. **Look at DigitalOcean**:
   * Check if the CPU, memory, or disk usage is too high.
   * If it is:
     * **Increase the machine size** temporarily to fix the issue.
     * Keep looking for the root cause.

***

## 📜 Check Logs and Errors

1. **Use Clickstack**:
   * Go to [https://watch.activepieces.com](https://watch.activepieces.com).
   * Search for recent errors in the logs.
   * Credentials are in the [Master Playbook](https://docs.google.com/document/d/15OwWnRwkhlx9l-EN5dXFoysw0OoxC0lVvnjbdbId4BE/edit?pli=1\&tab=t.4lk480a2s8yh#heading=h.1qegnmb1w65k).

2. **Check Sentry**:
   * Look for grouped errors (errors that happen a lot).
   * Try to **reproduce the error** and fix it if possible.

***

## 🛠️ Debugging with Checkly

1. **Check Checkly Logs**:
   * Watch the **video recordings** of failed checks to see what went wrong.
   * If the issue is a **timeout**, it might mean there’s a bigger performance problem.
   * If it's an E2E test failure due to UI changes, it's likely not urgent.
     * Fix the test and the issue will go away.

***

## 🚨 When Should You Ask for Help?

Ask for help right away if:

* Flows are failing.
* The whole platform is down.
* There's a lot of data loss or corruption.
* You're not sure what is causing the issue.
* You've spent **more than 5 minutes** and still don't know what's wrong.

💡 **How to Ask for Help**:

* Use **Incident.io** to create a **critical alert**.
* Go to the **Slack incident channel** and escalate the issue to the engineering team.

<Warning>
  If you’re unsure, **ask for help!** It’s better to be safe than sorry.
</Warning>

***

## 💡 Helpful Tips

1. **Stay Organized**:
   * Keep a list of steps to follow during downtime.
   * Write down everything you do so you can refer to it later.

2. **Communicate Clearly**:
   * Keep your team and users updated.
   * Use simple language in your updates.

3. **Take Care of Yourself**:
   * If you feel stressed, take a short break. Grab a coffee ☕, take a deep breath, and tackle the problem step by step.


# Engineering Workflow
Source: https://www.activepieces.com/docs/handbook/engineering/onboarding/how-we-work



Activepieces work is based on one-week sprints, as priorities change fast, the sprint has to be short to adapt.

## Sprints

Sprints are shared publicly on our GitHub account. This would give everyone visibility into what we are working on.

* There should be a GitHub issue for the sprint set up in advance that outlines the changes.
* Each *individual* should come prepared with specific suggestions for what they will work on over the next sprint. **if you're in an engineering role, no one will dictate to you what to build – it is up to you to drive this.**
* Teams generally meet once a week to pick the **priorities** together.
* Everyone in the team should attend the sprint planning.
* Anyone can comment on the sprint issue before or after the sprint.

## Pull Requests

When it comes to code review, we have a few guidelines to ensure efficiency:

* Create a pull request in draft state as soon as possible.
* Be proactive and review other people’s pull requests. Don’t wait for someone to ask for your review; it’s your responsibility.
* Assign only one reviewer to your pull request.
* Add the PR to the current project (sprint) so we can keep track of unmerged PRs at the end of each sprint.
* It is the **responsibility** of the **PR owner** to draft the test scenarios within the PR description. Upon review, the reviewer may assume that these scenarios have been tested and provide additional suggestions for scenarios.
* Large, incomplete features should be broken down into smaller tasks and continuously merged into the main branch.

## Planning is everyone's job.

Every engineer is responsible for discovering bugs/opportunities and bringing them up in the sprint to convert them into actionable tasks.


# On-Call
Source: https://www.activepieces.com/docs/handbook/engineering/onboarding/on-call



## Prerequisites:

* [Setup Incident IO](../playbooks/setup-incident-io)

## Why On-Call?

We need to ensure there is **exactly one person** at the same time who is the main point of contact for the users and the **first responder** for the issues. It's also a great way to learn about the product and the users and have some fun.

<Tip>
  You can listen to [Queen - Under Pressure](https://www.youtube.com/watch?v=a01QQZyl-_I) while on-call, it's fun and motivating.
</Tip>

<Tip>
  If you ever feel burn out in middle of your rotation, please reach out to the team and we will help you with the rotation or take over the responsibility.
</Tip>

## On-Call Schedule

The on-call rotation is managed through Incident.io, with each engineer taking a one-week shift. You can:

* View the current schedule and upcoming rotations on [Incident.io On-Call Schedule](https://app.incident.io/activepieces/on-call/schedules)
* Add the schedule to your Google Calendar using [this link](https://calendar.google.com/calendar/r?cid=webcal://app.incident.io/api/schedule_feeds/cc024d13704b618cbec9e2c4b2415666dfc8b1efdc190659ebc5886dfe2a1e4b)

<Warning>
  Make sure to update the on-call schedule in Incident.io if you cannot be available during your assigned rotation. This ensures alerts are routed to the correct person and maintains our incident response coverage.

  To modify the schedule:

  1. Go to [Incident.io On-Call Schedule](https://app.incident.io/activepieces/on-call/schedules)
  2. Find your rotation slot
  3. Click "Override schedule" to mark your unavailability
  4. Coordinate with the team to find coverage for your slot
</Warning>

## What it means to be on-call

The primary objective of being on-call is to triage issues and assist users. It is not about fixing the issues or coding missing features. Delegation is key whenever possible.

You are responsible for the following:

* Respond to Slack messages as soon as possible, referring to the [customer support guidelines](/handbook/customer-support/overview).

* Check [community.activepieces.com](https://community.activepieces.com) for any new issues or to learn about existing issues.

* Monitor your Incident.io notifications and respond promptly when paged.

<Tip>
  **Friendly Tip #1**: always escalate to the team if you are unsure what to do.
</Tip>

## How do you get paged?

Monitor and respond to incidents that come through these channels:

#### Slack Fire Emoji (🔥)

When a customer reports an issue in Slack and someone reacts with 🔥, you'll be automatically paged and a dedicated incident channel will be created.

#### Automated Alerts

Watch for notifications from:

* Digital Ocean about CPU, Memory, or Disk outages
* Checkly about e2e test failures or website downtime


# Onboarding Check List
Source: https://www.activepieces.com/docs/handbook/engineering/onboarding/onboarding-check-list



🎉 Welcome to Activepieces!

This guide provides a checklist for the new hire onboarding process.

***

## 📧 Essentials

* [ ] Set up your @activepieces.com email account and setup 2FA
* [ ] Confirm access to out private Discord server.
* [ ] Get Invited to the Activepieces Github Organization and Setup 2FA
* [ ] Get Assigned to a buddy who will be your onboarding buddy.

<Tip>
  During your first two months, we'll schedule 1:1 meetings every two weeks to ensure you're progressing well and to maintain open communication in both directions.
  After two months, we will decrease the frequency of the 1:1 to once a month.
</Tip>

<Tip>
  If you don't setup the 2FA, We will be alerted from security perspective.
</Tip>

***

### Engineering Checklist

* [ ] Setup your development environment using our setup guide
* [ ] Learn the repository structure and our tech stack (Fastify, React, PostgreSQL, SQLite, Redis)
* [ ] Understand the key database tables (Platform, Projects, Flows, Connections, Users)
* [ ] Complete your first "warmup" task within your first day (it's our tradition!)

***

## 🌟 Tips for Success

* Don't hesitate to ask questions—the team is especially helpful during your first days
* Take time to understand the product from a business perspective
* Work closely with your onboarding buddy to get up to speed quickly
* Review our documentation, explore the codebase, and check out community resources, outside your scope.
* Provide your ideas and feedback regularly

***

Welcome again to the team. We can't wait to see the impact you'll make at Activepieces! 😉


# Overview
Source: https://www.activepieces.com/docs/handbook/engineering/overview



Welcome to the engineering team! This section contains essential information to help you get started, including our development processes, guidelines, and practices. We're excited to have you on board.


# Queues Dashboard
Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/bullboard



The Bull Board is a tool that allows you to check issues with scheduling and internal flow runs issues.

![BullBoard Overview](https://raw.githubusercontent.com/felixmosh/bull-board/master/screenshots/overview.png)

## Setup BullBoard

To enable the Bull Board UI in your self-hosted installation:

1. Define these environment variables:
   * `AP_QUEUE_UI_ENABLED`: Set to `true`
   * `AP_QUEUE_UI_USERNAME`: Set your desired username
   * `AP_QUEUE_UI_PASSWORD`: Set your desired password

2. Access the UI at `/api/ui`

<Tip>
  For cloud installations, please ask your team for access to the internal documentation that explains how to access BullBoard.
</Tip>

## Queue Overview

We have one main queue called `workerJobs` that handles all job types. Each job has a `jobType` field that tells us what it does:

### Low Priority Jobs

#### RENEW\_WEBHOOK

Renews webhooks for pieces that have webhooks channel with expiration like Google Sheets.

#### EXECUTE\_POLLING

Checks external services for new data at regular intervals.

### Medium Priority Jobs

#### EXECUTE\_FLOW

Runs flows when they're triggered.

#### EXECUTE\_WEBHOOK

Processes incoming webhook requests that start flow runs.

#### EXECUTE\_AGENT

Runs AI agent tasks within flows.

#### DELAYED\_FLOW

Runs flows that were scheduled for later, like paused flows or delayed executions.

### High Priority Jobs

#### EXECUTE\_TOOL

Runs tool operations in flows, usually for AI-powered features.

#### EXECUTE\_PROPERTY

Loads dynamic properties for pieces that need them at runtime.

#### EXECUTE\_EXTRACT\_PIECE\_INFORMATION

Gets information about pieces when they're being installed or set up.

#### EXECUTE\_VALIDATION

Checks that flow settings, inputs, or data are correct before running.

#### EXECUTE\_TRIGGER\_HOOK

Runs special logic before or after triggers fire.

<Info>
  Failed jobs are not normal and need to be checked right away to find and fix what's causing them.
  They require immediate investigation as they represent executions that failed for unknown reasons that could indicate system issues.
</Info>

<Tip>
  Delayed jobs represent either paused flows scheduled for future execution, upcoming polling job iterations, or jobs being retried due to temporary failures. They indicate an internal system error occurred and the job will be retried automatically according to the backoff policy.
</Tip>


# Database Migrations
Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/database-migration

Guide for creating database migrations in Activepieces

Activepieces uses TypeORM as its database driver in Node.js. We support two database types across different editions of our platform.

The database migration files contain both what to do to migrate (up method) and what to do when rolling back (down method).

<Tip>
  Read more about TypeORM migrations here:
  [https://orkhan.gitbook.io/typeorm/docs/migrations](https://orkhan.gitbook.io/typeorm/docs/migrations)
</Tip>

## Database Support

* PostgreSQL
* SQLite

<Tip>
  **Why Do we have SQLite?**
  We support SQLite to simplify development and self-hosting. It's particularly helpful for:

  * Developers creating pieces who want a quick setup
  * Self-hosters using platforms to manage docker images but doesn't support docker compose.
</Tip>

## Editions

* **Enterprise & Cloud Edition** (Must use PostgreSQL)
* **Community Edition** (Can use PostgreSQL or SQLite)

<Tip>
  If you are generating a migration for an entity that will only be used in Cloud & Enterprise editions, you only need to create the PostgreSQL migration file. You can skip generating the SQLite migration.
</Tip>

### How To Generate

<Steps>
  <Step title="Uncomment Database Connection Export">
    Uncomment the following line in `packages/server/api/src/app/database/database-connection.ts`:

    ```typescript  theme={null}
    export const exportedConnection = databaseConnection()
    ```
  </Step>

  <Step title="Configure Database Type">
    Edit your `.env` file to set the database type:

    ```env  theme={null}
    # For SQLite migrations (default)
    AP_DATABASE_TYPE=SQLITE
    ```

    For PostgreSQL migrations:

    ```env  theme={null}
    AP_DB_TYPE=POSTGRES
    AP_POSTGRES_DATABASE=activepieces
    AP_POSTGRES_HOST=db
    AP_POSTGRES_PORT=5432
    AP_POSTGRES_USERNAME=postgres
    AP_POSTGRES_PASSWORD=password
    ```
  </Step>

  <Step title="Generate Migration">
    Run the migration generation command:

    ```bash  theme={null}
    nx db-migration server-api --name=<MIGRATION_NAME>
    ```

    Replace `<MIGRATION_NAME>` with a descriptive name for your migration.
  </Step>

  <Step title="Move Migration File">
    The command will generate a new migration file in `packages/server/api/src/app/database/migrations`.
    Review the generated file and:

    * For PostgreSQL migrations: Move it to `postgres-connection.ts`
    * For SQLite migrations: Move it to `sqlite-connection.ts`
  </Step>

  <Step title="Re-comment Export">
    After moving the file, remember to re-comment the line from step 1:

    ```typescript  theme={null}
    // export const exportedConnection = databaseConnection()
    ```
  </Step>
</Steps>

<Tip>
  Always test your migrations by running them both up and down to ensure they work as expected.
</Tip>


# E2E Tests
Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/e2e-tests



## Overview

Our e2e test suite uses Playwright to ensure critical user workflows function correctly across the application. The tests are organized using the Page Object Model pattern to maintain clean, reusable, and maintainable test code. This playbook outlines the structure, conventions, and best practices for writing e2e tests.

## Project Structure

```
packages/tests-e2e/
├── scenarios/           # Test files (*.spec.ts)
├── pages/              # Page Object Models
│   ├── base.ts         # Base page class
│   ├── index.ts        # Page exports
│   ├── authentication.page.ts
│   ├── builder.page.ts
│   ├── flows.page.ts
│   └── agent.page.ts
├── helper/             # Utilities and configuration
│   └── config.ts       # Environment configuration
├── playwright.config.ts # Playwright configuration
└── project.json        # Nx project configuration
```

This playbook provides a comprehensive guide for writing e2e tests following the established patterns in your codebase. It covers the Page Object Model structure, test organization, configuration management, and best practices for maintaining reliable e2e tests.

## Page Object Model Pattern

### Base Page Structure

All page objects extend the `BasePage` class and follow a consistent structure:

```typescript  theme={null}
export class YourPage extends BasePage {
  url = `${configUtils.getConfig().instanceUrl}/your-path`;

  getters = {
    // Locator functions that return page elements
    elementName: (page: Page) => page.getByRole('button', { name: 'Button Text' }),
  };

  actions = {
    // Action functions that perform user interactions
    performAction: async (page: Page, params: { param1: string }) => {
      // Implementation
    },
  };
}
```

### Page Object Guidelines

#### ❌ Don't do

```typescript  theme={null}
// Direct element selection in test files
test('should create flow', async ({ page }) => {
  await page.getByRole('button', { name: 'Create Flow' }).click();
  await page.getByText('From scratch').click();
  // Test logic mixed with element selection
});
```

#### ✅ Do

```typescript  theme={null}
// flows.page.ts
export class FlowsPage extends BasePage {
  getters = {
    createFlowButton: (page: Page) => page.getByRole('button', { name: 'Create Flow' }),
    fromScratchButton: (page: Page) => page.getByText('From scratch'),
  };

  actions = {
    newFlowFromScratch: async (page: Page) => {
      await this.getters.createFlowButton(page).click();
      await this.getters.fromScratchButton(page).click();
    },
  };
}

// integration.spec.ts
test('should create flow', async ({ page }) => {
  await flowsPage.actions.newFlowFromScratch(page);
  // Clean test logic focused on behavior
});
```

## Test Organization

### Test File Structure

Test files should be organized by feature or workflow:

```typescript  theme={null}
import { test, expect } from '@playwright/test';
import { 
  AuthenticationPage, 
  FlowsPage, 
  BuilderPage 
} from '../pages';
import { configUtils } from '../helper/config';

test.describe('Feature Name', () => {
  let authenticationPage: AuthenticationPage;
  let flowsPage: FlowsPage;
  let builderPage: BuilderPage;

  test.beforeEach(async () => {
    // Initialize page objects
    authenticationPage = new AuthenticationPage();
    flowsPage = new FlowsPage();
    builderPage = new BuilderPage();
  });

  test('should perform specific workflow', async ({ page }) => {
    // Test implementation
  });
});
```

### Test Naming Conventions

* Use descriptive test names that explain the expected behavior
* Follow the pattern: `should [action] [expected result]`
* Include context when relevant

```typescript  theme={null}
// Good test names
test('should send Slack message via flow', async ({ page }) => {});
test('should handle webhook with dynamic parameters', async ({ page }) => {});
test('should authenticate user with valid credentials', async ({ page }) => {});

// Avoid vague names
test('should work', async ({ page }) => {});
test('test flow', async ({ page }) => {});
```

## Configuration Management

### Environment Configuration

Use the centralized config utility to handle different environments:

```typescript  theme={null}
// helper/config.ts
export const configUtils = {
  getConfig: (): Config => {
    return process.env.E2E_INSTANCE_URL ? prodConfig : localConfig;
  },
};

// Usage in pages
export class AuthenticationPage extends BasePage {
  url = `${configUtils.getConfig().instanceUrl}/sign-in`;
}
```

### Environment Variables

Required environment variables for CI/CD:

* `E2E_INSTANCE_URL`: Target application URL
* `E2E_EMAIL`: Test user email
* `E2E_PASSWORD`: Test user password

## Writing Effective Tests

### Test Structure

Follow this pattern for comprehensive tests:

```typescript  theme={null}
test('should complete user workflow', async ({ page }) => {
  // 1. Set up test data and timeouts
  test.setTimeout(120000);
  const config = configUtils.getConfig();

  // 2. Authentication (if required)
  await authenticationPage.actions.signIn(page, {
    email: config.email,
    password: config.password
  });

  // 3. Navigate to relevant page
  await flowsPage.actions.navigate(page);

  // 4. Clean up existing data (if needed)
  await flowsPage.actions.cleanupExistingFlows(page);

  // 5. Perform the main workflow
  await flowsPage.actions.newFlowFromScratch(page);
  await builderPage.actions.waitFor(page);
  await builderPage.actions.selectInitialTrigger(page, {
    piece: 'Schedule',
    trigger: 'Every Hour'
  });

  // 6. Add assertions and validations
  await builderPage.actions.testFlowAndWaitForSuccess(page);
  
  // 7. Clean up (if needed)
  await builderPage.actions.exitRun(page);
});
```

### Wait Strategies

Use appropriate wait strategies instead of fixed timeouts:

```typescript  theme={null}
// Good - Wait for specific conditions
await page.waitForURL('**/flows/**');
await page.waitForSelector('.react-flow__nodes', { state: 'visible' });
await page.waitForFunction(() => {
  const element = document.querySelector('.target-element');
  return element && element.textContent?.includes('Expected Text');
}, { timeout: 10000 });

// Avoid - Fixed timeouts
await page.waitForTimeout(5000);
```

### Error Handling

Implement proper error handling and cleanup:

```typescript  theme={null}
test('should handle errors gracefully', async ({ page }) => {
  try {
    await flowsPage.actions.navigate(page);
    // Test logic
  } catch (error) {
    // Log error details
    console.error('Test failed:', error);
    // Take screenshot for debugging
    await page.screenshot({ path: 'error-screenshot.png' });
    throw error;
  } finally {
    // Clean up resources
    await flowsPage.actions.cleanupExistingFlows(page);
  }
});
```

## Best Practices

### Element Selection

Prefer semantic selectors over CSS selectors:

```typescript  theme={null}
// Good - Semantic selectors
getters = {
  createButton: (page: Page) => page.getByRole('button', { name: 'Create Flow' }),
  emailField: (page: Page) => page.getByPlaceholder('email@example.com'),
  searchInput: (page: Page) => page.getByRole('textbox', { name: 'Search' }),
};

// Avoid - Fragile CSS selectors
getters = {
  createButton: (page: Page) => page.locator('button.btn-primary'),
  emailField: (page: Page) => page.locator('input[type="email"]'),
};
```

### Test Data Management

Use dynamic test data to avoid conflicts:

```typescript  theme={null}
// Good - Dynamic test data
const runVersion = Math.floor(Math.random() * 100000);
const uniqueFlowName = `Test Flow ${Date.now()}`;

// Avoid - Static test data
const flowName = 'Test Flow';
```

### Assertions

Use meaningful assertions that verify business logic:

```typescript  theme={null}
// Good - Business logic assertions
await builderPage.actions.testFlowAndWaitForSuccess(page);
const response = await apiRequest.get(urlWithParams);
const body = await response.json();
expect(body.targetRunVersion).toBe(runVersion.toString());

// Avoid - Implementation details
expect(await page.locator('.success-message').isVisible()).toBe(true);
```

## Running Tests

### Local Development & Debugging with Checkly

We use [Checkly](https://checklyhq.com/) to run and debug E2E tests. Checkly provides video recordings for each test run, making it easy to debug failures.

```bash  theme={null}
# Run tests with Checkly (includes video reporting)
npx nx run tests-e2e:test-checkly
```

* Test results, including video recordings, are available in the Checkly dashboard.
* You can debug failed tests by reviewing the video and logs provided by Checkly.

### Deploying Tests

Manual deployment is rarely needed, but you can trigger it with:

```bash  theme={null}
npx nx run tests-e2e:deploy-checkly
```

<Info>
  Tests are deployed to Checkly automatically after successful test runs in the CI pipeline.
</Info>

## Debugging Tests

### 1. Checkly Videos and Reports

When running tests with Checkly, each test execution is recorded and detailed reports are generated. This is the fastest way to debug failures:

* **Video recordings**: Watch the exact browser session for any test run.
* **Step-by-step logs**: Review detailed logs and screenshots for each test step.
* **Access**: Open the Checkly dashboard and navigate to the relevant test run to view videos and reports.

### 2. VSCode Extension

For the best local debugging experience, install the **Playwright Test for VSCode** extension:

1. Open VSCode Extensions (Ctrl+Shift+X)
2. Search for "Playwright Test for VSCode"
3. Install the extension by Microsoft

**Benefits:**

* Debug tests directly in VSCode with breakpoints
* Step-through test execution
* View test results and traces in the Test Explorer
* Auto-completion for Playwright APIs
* Integrated test runner

### 3. Debugging Tips

1. **Use Checkly dashboard**: Review videos and logs for failed tests.
2. **Use VSCode Extension**: Set breakpoints directly in your test files.
3. **Step Through**: Use F10 (step over) and F11 (step into) in debug mode.
4. **Inspect Elements**: Use `await page.pause()` to pause execution and inspect the page.
5. **Console Logs**: Add `console.log()` statements to track execution flow.
6. **Manual Screenshots**: Take screenshots at critical points for visual debugging.

```typescript  theme={null}
test('should debug workflow', async ({ page }) => {
  await page.goto('/flows');
  
  // Pause execution for manual inspection
  await page.pause();
  
  // Take screenshot for debugging
  await page.screenshot({ path: 'debug-screenshot.png' });
  
  // Continue with test logic
  await flowsPage.actions.newFlowFromScratch(page);
});
```

## Common Patterns

### Authentication Flow

```typescript  theme={null}
test('should authenticate user', async ({ page }) => {
  const config = configUtils.getConfig();
  
  await authenticationPage.actions.signIn(page, {
    email: config.email,
    password: config.password
  });

  await agentPage.actions.waitFor(page);
});
```

### Flow Creation and Testing

```typescript  theme={null}
test('should create and test flow', async ({ page }) => {
  await flowsPage.actions.navigate(page);
  await flowsPage.actions.cleanupExistingFlows(page);
  await flowsPage.actions.newFlowFromScratch(page);
  
  await builderPage.actions.waitFor(page);
  await builderPage.actions.selectInitialTrigger(page, {
    piece: 'Schedule',
    trigger: 'Every Hour'
  });
  
  await builderPage.actions.testFlowAndWaitForSuccess(page);
});
```

### API Integration Testing

```typescript  theme={null}
test('should handle webhook integration', async ({ page }) => {
  const apiRequest = await page.context().request;
  const response = await apiRequest.get(urlWithParams);
  const body = await response.json();
  
  expect(body.targetRunVersion).toBe(expectedValue);
});
```

## Maintenance Guidelines

### Updating Selectors

When UI changes occur:

1. Update page object getters with new selectors
2. Test the changes locally
3. Update related tests if necessary
4. Ensure all tests pass before merging

### Adding New Tests

1. Create or update relevant page objects
2. Write test scenarios in appropriate spec files
3. Follow the established patterns and conventions
4. Add proper error handling and cleanup
5. Test locally before submitting

### Performance Considerations

* Keep tests focused and avoid unnecessary steps
* Use appropriate timeouts (not too short, not too long)
* Clean up test data to avoid conflicts
* Group related tests in the same describe block


# Frontend Best Practices
Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/frontend-best-practices



## Overview

Our frontend codebase is large and constantly growing, with multiple developers contributing to it. Establishing consistent rules across key areas like data fetching and state management will make the code easier to follow, refactor, and test. It will also help newcomers understand existing patterns and adopt them quickly.

## Data Fetching with React Query

### Hook Organization

All `useMutation` and `useQuery` hooks should be grouped by domain/feature in a single location: `features/lib/feature-hooks.ts`. Never call data fetching hooks directly from component bodies.

**Benefits:**

* Easier refactoring and testing
* Simplified mocking for tests
* Cleaner components focused on UI logic
* Reduced clutter in `.tsx` files

#### ❌ Don't do

```tsx  theme={null}
// UserProfile.tsx
import { useMutation, useQuery } from '@tanstack/react-query';
import { updateUser, getUser } from '../api/users';

function UserProfile({ userId }) {
  const { data: user } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => getUser(userId)
  });

  const updateUserMutation = useMutation({
    mutationFn: updateUser,
    onSuccess: () => {
      // refetch logic here
    }
  });

  return (
    <div>
      {/* UI logic */}
    </div>
  );
}
```

#### ✅ Do

```tsx  theme={null}
// features/users/lib/user-hooks.ts
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { updateUser, getUser } from '../api/users';
import { userKeys } from './user-keys';

export function useUser(userId: string) {
  return useQuery({
    queryKey: userKeys.detail(userId),
    queryFn: () => getUser(userId)
  });
}

export function useUpdateUser() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: updateUser,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: userKeys.all });
    }
  });
}

// UserProfile.tsx
import { useUser, useUpdateUser } from '../lib/user-hooks';

function UserProfile({ userId }) {
  const { data: user } = useUser(userId);
  const updateUserMutation = useUpdateUser();

  return (
    <div>
      {/* Clean UI logic only */}
    </div>
  );
}
```

### Query Keys Management

Query keys should be unique identifiers for specific queries. Avoid using boolean values, empty strings, or inconsistent patterns.

**Best Practice:** Group all query keys in one centralized location (inside the hooks file) for easy management and refactoring.

```tsx  theme={null}
// features/users/lib/user-hooks.ts
export const userKeys = {
  all: ['users'] as const,
  lists: () => [...userKeys.all, 'list'] as const,
  list: (filters: string) => [...userKeys.lists(), { filters }] as const,
  details: () => [...userKeys.all, 'detail'] as const,
  detail: (id: string) => [...userKeys.details(), id] as const,
  preferences: (id: string) => [...userKeys.detail(id), 'preferences'] as const,
};

// Usage examples:
// userKeys.all          // ['users']
// userKeys.list('active') // ['users', 'list', { filters: 'active' }]
// userKeys.detail('123')  // ['users', 'detail', '123']
```

**Benefits:**

* Easy key renaming and refactoring
* Consistent key structure across the app
* Better query specificity control
* Centralized key management

### Refetch vs Query Invalidation

Prefer using `invalidateQueries` over passing `refetch` functions between components. This approach is more maintainable and easier to understand.

#### ❌ Don't do

```tsx  theme={null}
function UserList() {
  const { data: users, refetch } = useUsers();
  
  return (
    <div>
      <UserForm onSuccess={refetch} />
      <EditUserModal onSuccess={refetch} />
      {/* Passing refetch everywhere */}
    </div>
  );
}
```

#### ✅ Do

```tsx  theme={null}
// In your mutation hooks
export function useCreateUser() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: createUser,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: userKeys.lists() });
    }
  });
}

// Components don't need to handle refetching
function UserList() {
  const { data: users } = useUsers();
  
  return (
    <div>
      <UserForm /> {/* Handles its own invalidation */}
      <EditUserModal /> {/* Handles its own invalidation */}
    </div>
  );
}
```

## Dialog State Management

Use a centralized store or context to manage all dialog states in one place. This eliminates the need to pass local state between different components and provides global access to dialog controls.

### Implementation Example

```tsx  theme={null}
// stores/dialog-store.ts
import { create } from 'zustand';
import { immer } from 'zustand/middleware/immer';

interface DialogState {
  createUser: boolean;
  editUser: boolean;
  deleteConfirmation: boolean;
  // Add more dialogs as needed
}

interface DialogStore {
  dialogs: DialogState;
  setDialog: (dialog: keyof DialogState, isOpen: boolean) => void;
}

export const useDialogStore = create<DialogStore>()(
  immer((set) => ({
    dialogs: {
      createUser: false,
      editUser: false,
      deleteConfirmation: false,
    },
    setDialog: (dialog, isOpen) =>
      set((state) => {
        state.dialogs[dialog] = isOpen;
      }),
  }))
);

// Usage in components
function UserManagement() {
  const { dialogs, setDialog } = useDialogStore();

  return (
    <div>
      <button onClick={() => setDialog('createUser', true)}>
        Create User
      </button>
      
      <CreateUserDialog 
        open={dialogs.createUser}
        onClose={() => setDialog('createUser', false)}
      />
      
      <EditUserDialog 
        open={dialogs.editUser}
        onClose={() => setDialog('editUser', false)}
      />
    </div>
  );
}

// Any component can control dialogs - no provider needed
function Sidebar() {
  const setDialog = useDialogStore((state) => state.setDialog);

  return (
    <button onClick={() => setDialog('d', true)}>
      Quick Create User
    </button>
  );
}

// You can also use selectors for better performance
function UserDialog() {
  const isOpen = useDialogStore((state) => state.dialogs.createUser);
  const setDialog = useDialogStore((state) => state.setDialog);

  return (
    <CreateUserDialog 
      open={isOpen}
      onClose={() => setDialog('createUser', false)}
    />
  );
}
```

**Benefits:**

* Centralized dialog state management
* No prop drilling of dialog states
* Easy to open/close dialogs from anywhere in the app
* Consistent dialog behavior across the application
* Simplified component logic


# Cloud Infrastructure
Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/infrastructure



<Warning>
  The playbooks are private, Please ask your team for an access.
</Warning>

Our infrastructure stack consists of several key components that help us monitor, deploy, and manage our services effectively.

## Hosting Providers

We use two main hosting providers:

* **DigitalOcean**: Hosts our databases including Redis and PostgreSQL
* **Hetzner**: Provides the machines that run our services

## Grafana (Loki) for Logs

We use Grafana Loki to collect and search through logs from all our services in one centralized place.

## Kamal for Deployment

Kamal is a deployment tool that helps us deploy our Docker containers to production with zero downtime.


# Feature Announcement
Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/product-announcement



When we develop new features, our marketing team handles the public announcements. As engineers, we need to clearly communicate:

1. The problem the feature solves
2. The benefit to our users
3. How it integrates with our product

### Handoff to Marketing Team

There is an integration between GitHub and Linear, that automatically open a ticket for the marketing team after 5 minutes of issue get closed.\
\
Please make sure of the following:

* Github Pull Request is linked to an issue.
* The pull request must have one of these labels: **"Pieces"**, **"Polishing"**, or **"Feature"**.
  * If none of these labels are added, the PR will not be merged.
  * You can also add any other relevant label.
* The GitHub issue must include the correct template (see "Ticket templates" below).

<Tip>
  Bonus: Please include a video showing the marketing team  on how to use this feature so they can create a demo video and market it correctly.
</Tip>

Ticket templates:

```
### What Problem Does This Feature Solve?

### Explain How the Feature Works
[Insert the video link here]

### Target Audience
Enterprise / Everyone 

### Relevant User Scenarios
[Insert Pylon tickets or community posts here]
```


# How to create Release
Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/releases



Pre-releases are versions of the software that are released before the final version. They are used to test new features and bug fixes before they are released to the public. Pre-releases are typically labeled with a version number that includes a pre-release identifier, such as `official` or `rc`.

## Types of Releases

There are several types of releases that can be used to indicate the stability of the software:

* **Official**: Official releases are considered to be stable and are close to the final release.
* **Release Candidate (RC)**: Release candidates are versions of the software that are feature-complete and have been tested by a larger group of users. They are considered to be stable and are close to the final release. They are typically used for final testing before the final release.

## Why Use Pre-Releases

We do pre-release when we release hot-fixes / bug fixes / small and beta features.

## How to Release a Pre-Release

To release a pre-release version of the software, follow these steps:

1. **Create a new branch**: Create a new branch from the `main` branch. The branch name should be `release/vX.Y.Z` where `X.Y.Z` is the version number.
2. **Increase the version number**: Update the `package.json` file with the new version number.
3. **Open a Pull Request**: Open a pull request from the new branch to the `main` branch. Assign the `pre-release` label to the pull request.
4. **Check the Changelog**: Check the [Activepieces Releases](https://github.com/activepieces/activepieces/releases) page to see if there are any new features or bug fixes that need to be included in the pre-release. Make sure all PRs are labeled correctly so they show in the correct auto-generated changelog. If not, assign the labels and rerun the changelog by removing the "pre-release" label and adding it again to the PR.
5. Go to [https://github.com/activepieces/activepieces/actions/workflows/release-rc.yml](https://github.com/activepieces/activepieces/actions/workflows/release-rc.yml) and run it on the release branch to build the rc image.
6. **Merge the Pull Request**: Merge the pull request to the `main` branch.
7. **Release the Notes**: Release the notes for the new version.


# Run Enterprise Edition
Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/run-ee



The enterprise edition requires a postgres and redis instance to run, and a license key to activate.

<Steps>
  <Step title="Run the dev container">
    Follow the instructions [here](/developers/development-setup/dev-container) to run the dev container.
  </Step>

  <Step title="Add the following env variables in `server/api/.env`">
    Pase the following env variables in `server/api/.env`

    ```bash  theme={null}
    ## these variables are set to align with the .devcontainer/docker-compose.yml file
    AP_DB_TYPE=POSTGRES
    AP_DEV_PIECES="your_piece_name"
    AP_ENVIRONMENT="dev"
    AP_EDITION=ee
    AP_EXECUTION_MODE=UNSANDBOXED
    AP_FRONTEND_URL="http://localhost:4200"
    AP_WEBHOOK_URL="http://localhost:3000"
    AP_PIECES_SOURCE='FILE'
    AP_PIECES_SYNC_MODE='NONE'
    AP_LOG_LEVEL=debug
    AP_LOG_PRETTY=true
    AP_REDIS_HOST="redis"
    AP_REDIS_PORT="6379"
    AP_TRIGGER_DEFAULT_POLL_INTERVAL=1
    AP_CACHE_PATH=/workspace/cache
    AP_POSTGRES_DATABASE=activepieces
    AP_POSTGRES_HOST=db
    AP_POSTGRES_PORT=5432
    AP_POSTGRES_USERNAME=postgres
    AP_POSTGRES_PASSWORD=A79Vm5D4p2VQHOp2gd5
    AP_ENCRYPTION_KEY=427a130d9ffab21dc07bcd549fcf0966
    AP_JWT_SECRET=secret
    ```
  </Step>

  <Step title="Activate Your License Key">
    After signing in, activate the license key by going to **Platform Admin -> Setup -> License Keys**
    <img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=abc2db5befaabf039899a23fd75d9470" alt="Activation License Key" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/activation-license-key-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=4a9e7f5cce1de95854a23131197452df 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f3aee8442dde13d03ae2ae978b1dd2f4 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f6638ba4fa57d7256ec79d9e82ff55aa 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=2bce94354609c5ee9d77656dd0490648 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=e956a826e5d82a0e77a885ec6dfee2b0 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=a9c2344b6be067b18b8367440d4cbf3c 2500w" />
  </Step>
</Steps>


# Setup Incident.io
Source: https://www.activepieces.com/docs/handbook/engineering/playbooks/setup-incident-io



Incident.io is our primary tool for managing and responding to urgent issues and service disruptions.
This guide explains how we use Incident.io to coordinate our on-call rotations and emergency response procedures.

## Setup and Notifications

### Personal Setup

1. Download the Incident.io mobile app from your device's app store
2. Ask your team to add you to the Incident.io workspace
3. Configure your notification preferences:
   * Phone calls for critical incidents
   * Push notifications for high-priority issues
   * Slack notifications for standard updates

### On-Call Rotations

Our team operates on a weekly rotation schedule through Incident.io, where every team member participates. When you're on-call:

* You'll receive priority notifications for all urgent issues
* Phone calls will be placed for critical service disruptions
* Rotations change every week, with handoffs occurring on Monday mornings
* Response is expected within 15 minutes for critical incidents

<Tip>
  If you are unable to respond to an incident, please escalate to the engineering team.
</Tip>


# Our Compensation
Source: https://www.activepieces.com/docs/handbook/hiring/compensation



The packages include three factors for the salary:

* **Role**: The specific position and responsibilities of the employee.
* **Location**: The geographical area where the employee is based.
* **Level**: The seniority and experience level of the employee.

<Tip>Salaries are fixed and based on levels and seniority, not negotiation. This ensures fair pay for everyone.</Tip>

<Tip>Salaries are updated based on market trends and the company's performance. It's easier to justify raises when the business is great.</Tip>


# Our Hiring Process
Source: https://www.activepieces.com/docs/handbook/hiring/hiring



Engineers are the majority of the Activepieces team, and we are always looking for highly talented product engineers.

<Steps>
  <Step title="Technical Interview">
    Here, you'll face a real challenge from Activepieces. We'll guide you through it to see how you solve problems.
  </Step>

  <Step title="Product & Leadership Interview">
    We'll chat about your past experiences and how you design products. It's like having a friendly conversation where we reflect on what you've done before.
  </Step>

  <Step title="Work Trial">
    You'll do open source task for one day. This open source contribution task help us understand how well we work together.
  </Step>
</Steps>

## Interviewing Tips

Every interview should make us say **HELL YES**. If not, we'll kindly pass.

**Avoid Bias:** Get opinions from others to make fair decisions.

**Speak Up Early:** If you're unsure about something, ask or test it right away.


# Our Roles & Levels
Source: https://www.activepieces.com/docs/handbook/hiring/levels



**Product Engineers** are full stack engineers who handle both the engineering and product side, delivering features end-to-end.

### Our Levels

We break out seniority into three levels, **L1 to L3**.

### L1 Product Engineers

They tend to be early-career.

* They get more management support than folks at other levels.
* They focus on continuously absorbing new information about our users and how to be effective at **Activepieces**.
* They aim to be increasingly autonomous as they gain more experience here.

### L2 Product Engineers

They are generally responsible for running a project start-to-finish.

* They independently decide on the implementation details.
* They work with **Stakeholders** / **teammates** / **L3s** on the plan.
* They have personal responsibility for the **“how”** of what they’re working on, but share responsibility for the **“what”** and **“why”**.
* They make consistent progress on their work by continuously defining the scope, incorporating feedback, trying different approaches and solutions, and deciding what will deliver the most value for users.

### L3 Product Engineers

Their scope is bigger than coding, they lead a product area, make key product decisions and guide the team with strong leadership skills.

* **Planning**: They help **L2s** figure out what the next priority things to focus on and guide **L1s** in determining the right sequence of work to get a project done.
* **Day-to-Day Work**: They might be hands-on with the day-to-day work of the team, providing support and resources to their teammates as needed.
* **Customer Communication**: They handle direct communication with customers regarding planning and product direction, ensuring that customer needs and feedback are incorporated into the development process.

### How to Level Up

There is no formal process, but it happens at the end of **each year** and is based on two things:

1. **Manager Review**: Managers look at how well the engineer has performed and grown over the year.
2. **Peer Review**: Colleagues give feedback on how well the engineer has worked with the team.

This helps make sure promotions are fair and based on merit.


# Our Team Structure
Source: https://www.activepieces.com/docs/handbook/hiring/team



We are big believers in small teams with 10x engineers who would outperform other team types.

## No product management by default

Engineers decide what to build. If you need help, feel free to reach out to the team for other opinions or help.

## No Process by default

We trust the engineers' judgment to make the call whether this code is risky and requires external approval or if it's a fix that can be easily reversed or fixed with no big impact on the end user.

## They Love Users

When the engineer loves the users, that means they would ship fast, they wouldn't over-engineer because they understand the requirements very well, they usually have empathy which means they don't complicate everyone else.

## Pragmatic & Speed

Engineering planning sometimes seems sexy from a technical perspective, but being pragmatic means you would take decisions in a timely manner, taking them in baby steps and iterating faster rather than planning for the long run, and it's easy to reverse wrong decisions early on without investing too much time.

## Starts With Hiring

We hire very **slowly**. We are always looking for highly talented engineers. We love to hire people with a broader skill set and flexibility, low egos, and who are builders at heart.

We found that working with strong engineers is one of the strongest reasons to retain employees, and this would allow everyone to be free and have less process.


# Activepieces Handbook
Source: https://www.activepieces.com/docs/handbook/overview



Welcome to the Activepieces Handbook!

This guide serves as a complete resource for understanding our organization. Inside, you'll find detailed sections covering various aspects of our internal processes and policies.


# Interface Design
Source: https://www.activepieces.com/docs/handbook/product/interface-design



This page is a collection of resources for interface design. It's a work in progress and will be updated as we go.

## Color Palette

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/color-palette.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=9fc41c6dc7fe3184e561c8e13fe28281" alt="Color Palette" data-og-width="1600" width="1600" data-og-height="1200" height="1200" data-path="resources/color-palette.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/color-palette.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=a33ccfc74d4ce5e79e39cf033032c6ef 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/color-palette.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=e9fe79a3a9b323b0f98570101b6c9ce6 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/color-palette.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=91d414188c2af50c8e74ad7cff438c72 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/color-palette.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=22bb2e62f03300c000ff796b7f5e819e 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/color-palette.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=4fa23d662b35a9289adbb97ad3b3565d 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/color-palette.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=27f2870bf469d258909a800e9e043536 2500w" />

The palette includes:

* Primary colors for main actions and branding
* Secondary colors for supporting elements
* Semantic colors for status and feedback (success, warning, destructive)

## Tech Stack

Our frontend is built with:

* **React** - Core UI framework
* **Shadcn UI** - Component library
* **Tailwind CSS** - Utility-first styling

## Learning Resources

* [Interface Design (Chapters 46-53)](https://basecamp.com/gettingreal/09.1-interface-first) from Getting Real by Basecamp


# Marketing & Content
Source: https://www.activepieces.com/docs/handbook/teams/content



### Mission Statement

We aim to share and teach Activepieces' vision of democratized automation, helping users discover and learn how to unlock the full potential of our platform while building a vibrant community of automation enthusiasts.

### People

<CardGroup col={3}>
  <Snippet file="profile/ash.mdx" />

  <Snippet file="profile/kareem.mdx" />

  <Snippet file="profile/ginika.mdx" />
</CardGroup>


# Overview
Source: https://www.activepieces.com/docs/handbook/teams/overview



<CardGroup cols={2}>
  <Card title="Product" icon="rocket" href="/handbook/teams/product" color="#8E44AD">
    Build workflows quickly and easily, turning ideas into working automations
  </Card>

  <Card title="Platform" icon="layer-group" href="/handbook/teams/platform" color="#34495E">
    Build and maintain infrastructure and management systems that power Activepieces
  </Card>

  <Card title="Pieces" icon="puzzle-piece" href="/handbook/teams/pieces" color="#F1C40F">
    Build and manage integration pieces to connect with external services
  </Card>

  <Card title="Marketing Website & Content" icon="pencil" href="/handbook/teams/content" color="#FF6B6B">
    Create and manage educational content, documentation, and marketing copy
  </Card>

  <Card title="Sales" icon="handshake" href="/handbook/teams/sales" color="#27AE60">
    Grow revenue by selling Activepieces to businesses
  </Card>
</CardGroup>

### People

<CardGroup col={3}>
  <Snippet file="profile/ash.mdx" />

  <Snippet file="profile/mo.mdx" />

  <Snippet file="profile/abdulyki.mdx" />

  <Snippet file="profile/kishan.mdx" />

  <Snippet file="profile/hazem.mdx" />

  <Snippet file="profile/amr.mdx" />

  <Snippet file="profile/ginika.mdx" />

  <Snippet file="profile/kareem.mdx" />

  <Snippet file="profile/louai.mdx" />

  <Snippet file="profile/david.mdx" />

  <Snippet file="profile/sanket.mdx" />

  <Snippet file="profile/chaker.mdx" />
</CardGroup>


# Pieces
Source: https://www.activepieces.com/docs/handbook/teams/pieces



### Mission Statement

We build and maintain integration pieces that enable users to connect and automate across different services and platforms.

### People

<CardGroup col={3}>
  <Snippet file="profile/kishan.mdx" />

  <Snippet file="profile/david.mdx" />

  <Snippet file="profile/sanket.mdx" />
</CardGroup>

### Roadmap

#### Third Party Pieces

[https://linear.app/activepieces/project/third-party-pieces-38b9d73a164c/issues](https://linear.app/activepieces/project/third-party-pieces-38b9d73a164c/issues)

#### Core Pieces

[https://linear.app/activepieces/project/core-pieces-3419406029ca/issues](https://linear.app/activepieces/project/core-pieces-3419406029ca/issues)

#### Universal AI Pieces

[https://linear.app/activepieces/project/universal-ai-pieces-92ed6f9cd12b/issues](https://linear.app/activepieces/project/universal-ai-pieces-92ed6f9cd12b/issues)


# Platform
Source: https://www.activepieces.com/docs/handbook/teams/platform



### Mission Statement

We build and maintain the infrastructure and management systems that power Activepieces, ensuring reliability, scalability, and ease of deployment for self-hosted environments.

### People

<CardGroup col={3}>
  <Snippet file="profile/mo.mdx" />

  <Snippet file="profile/amr.mdx" />

  <Snippet file="profile/chaker.mdx" />
</CardGroup>

### Roadmap

[https://linear.app/activepieces/project/self-hosting-devxp-infrastructure-cc6611474f1f/overview](https://linear.app/activepieces/project/self-hosting-devxp-infrastructure-cc6611474f1f/overview)


# Product
Source: https://www.activepieces.com/docs/handbook/teams/product



### Mission Statement

We help you build workflows quickly and easily, turning your ideas into working automations in minutes.

### People

<CardGroup col={3}>
  <Snippet file="profile/ash.mdx" />

  <Snippet file="profile/abdulyki.mdx" />

  <Snippet file="profile/hazem.mdx" />

  <Snippet file="profile/louai.mdx" />
</CardGroup>

### Roadmap

[https://linear.app/activepieces/view/product-team-e839e4389a1c](https://linear.app/activepieces/view/product-team-e839e4389a1c)


# Sales
Source: https://www.activepieces.com/docs/handbook/teams/sales



### Mission Statement

We grow revenue by selling Activepieces to businesses.

### People

<CardGroup col={3}>
  <Snippet file="profile/ash.mdx" />
</CardGroup>


# Engine
Source: https://www.activepieces.com/docs/install/architecture/engine



The Engine file contains the following types of operations:

* **Extract Piece Metadata**: Extracts metadata when installing new pieces.
* **Execute Step**: Executes a single test step.
* **Execute Flow**: Executes a flow.
* **Execute Property**: Executes dynamic dropdowns or dynamic properties.
* **Execute Trigger Hook**: Executes actions such as OnEnable, OnDisable, or extracting payloads.
* **Execute Auth Validation**: Validates the authentication of the connection.

The engine takes the flow JSON with an engine token scoped to this project and implements the API provided for the piece framework, such as:

* Storage Service: A simple key/value persistent store for the piece framework.
* File Service: A helper to store files either locally or in a database, such as for testing steps.
* Fetch Metadata: Retrieves metadata of the current running project.


# Overview
Source: https://www.activepieces.com/docs/install/architecture/overview



This page focuses on describing the main components of Activepieces and focus mainly on workflow executions.

## Components

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/architecture.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=57d042ab0821b030bd6bc166bb1cfeac" alt="Architecture" data-og-width="964" width="964" data-og-height="422" height="422" data-path="resources/architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/architecture.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=6d7cef204f1db77b7062345ea00fb07b 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/architecture.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=3c48a4048db2360f8a66f6a82200ff63 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/architecture.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=e0da38ce0dabc6b6c5dfdf0567447e73 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/architecture.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=9c0c5e25920cc6f2170e836755c79df8 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/architecture.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=112e16fe315c1ac794af3e396cacaae9 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/architecture.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=e9b38add32bc671e44d34496a79189db 2500w" />

**Activepieces:**

* **App**: The main application that organizes everything from APIs to scheduled jobs.
* **Worker**: Polls for new jobs and executes the flows with the engine, ensuring proper sandboxing, and sends results back to the app through the API.
* **Engine**: TypeScript code that parses flow JSON and executes it. It is compiled into a single JS file.
* **UI**: Frontend written in React.

**Third Party**:

* **Postgres**: The main database for Activepieces.
* **Redis**: This is used to power the queue using [BullMQ](https://docs.bullmq.io/).

## Reliability & Scalability

<Tip>
  Postgres and Redis availability is outside the scope of this documentation, as many cloud providers already implement best practices to ensure their availability.
</Tip>

* **Webhooks**:\
  All webhooks are sent to the Activepieces app, which performs basic validation and adds them to the queue. In case of a spike, webhooks will be added to the queue.

* **Polling Trigger**:\
  All recurring jobs are added to Redis. In case of a failure, the missed jobs will be executed again.

* **Flow Execution**:\
  Workers poll jobs from the queue. In the event of a spike, the flow execution will still work but may be delayed depending on the size of the spike.

To scale Activepieces, you typically need to increase the replicas of either workers, the app, or the Postgres database. A small Redis instance is sufficient as it can handle thousands of jobs per second and rarely acts as a bottleneck.

## Repository Structure

The repository is structured as a monorepo using the NX build system, with TypeScript as the primary language. It is divided into several packages:

```
.
├── packages
│   ├── react-ui
│   ├── server
|       |── api
|       |── worker
|       |── shared
|   ├── ee
│   ├── engine
│   ├── pieces
│   ├── shared
```

* `react-ui`: This package contains the user interface, implemented using the React framework.
* `server-api`: This package contains the main application written in TypeScript with the Fastify framework.
* `server-worker`: This package contains the logic of accepting flow jobs and executing them using the engine.
* `server-shared`: this package contains the shared logic between worker and app.
* `engine`: This package contains the logic for flow execution within the sandbox.
* `pieces`: This package contains the implementation of triggers and actions for third-party apps.
* `shared`: This package contains shared data models and helper functions used by the other packages.
* `ee`: This package contains features that are only available in the paid edition.


# Performance & Benchmarking
Source: https://www.activepieces.com/docs/install/architecture/performance



## Performance

On average, Activepieces (self-hosted) can handle 95 flow executions per second on a single instance (including PostgreSQL and Redis) with under 300ms latency.\
It can scale up much more with increasing instance resources and/or adding more instances.\
\
The result of **5000** requests with concurrency of **25**

```
This is ApacheBench, Version 2.3 <$Revision: 1913912 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 500 requests
Completed 1000 requests
Completed 1500 requests
Completed 2000 requests
Completed 2500 requests
Completed 3000 requests
Completed 3500 requests
Completed 4000 requests
Completed 4500 requests
Completed 5000 requests
Finished 5000 requests


Server Software:        
Server Hostname:        localhost
Server Port:            4200

Document Path:          /api/v1/webhooks/GMtpNwDsy4mbJe3369yzy/sync
Document Length:        16 bytes

Concurrency Level:      25
Time taken for tests:   52.087 seconds
Complete requests:      5000
Failed requests:        0
Total transferred:      1375000 bytes
HTML transferred:       80000 bytes
Requests per second:    95.99 [#/sec] (mean)
Time per request:       260.436 [ms] (mean)
Time per request:       10.417 [ms] (mean, across all concurrent requests)
Transfer rate:          25.78 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       1
Processing:    32  260  23.8    254     756
Waiting:       31  260  23.8    254     756
Total:         32  260  23.8    254     756

Percentage of the requests served within a certain time (ms)
  50%    254
  66%    261
  75%    267
  80%    272
  90%    289
  95%    306
  98%    327
  99%    337
 100%    756 (longest request)
```

#### Benchmarking

Here is how to reproduce the benchmark:

1. Run Activepieces with PostgreSQL and Redis with the following environment variables:

```env  theme={null}
AP_EXECUTION_MODE=SANDBOX_CODE_ONLY
AP_FLOW_WORKER_CONCURRENCY=25
```

2. Create a flow with a Catch Webhook trigger and a webhook Return Response action.

   <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3932ff8bbe1bc53cb4968458b5d617b0" alt="Simple Webhook Flow" data-og-width="719" width="719" data-og-height="847" height="847" data-path="resources/screenshots/simple-webhook-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=f7f3771d8d0ddf3ea65aceaf8989177f 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=5f63616909a658a7c36ccf60e376af4f 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=76c7ada115f8b4a9cc2e5ee37d5ec064 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=38ead94383a663547736a50dcd43e372 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=6609bba1e3550712e3bf97019d8b33eb 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/simple-webhook-flow.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0b43adade90df31e0c038cec274282a9 2500w" />
3. Get the webhook URL from the webhook trigger and append `/sync` to it.
4. Install a benchmark tool like [ab](https://httpd.apache.org/docs/2.4/programs/ab.html):

```bash  theme={null}
sudo apt-get install apache2-utils
```

5. Run the benchmark:

```bash  theme={null}
ab -c 25 -n 5000 http://localhost:4200/api/v1/webhooks/GMtpNwDsy4mbJe3369yzy/sync
```

6. Check the results:

Instance specs used to get the above results:

* 16GB RAM
* AMD Ryzen 7 8845HS (8 cores, 16 threads)
* Ubuntu 24.04 LTS

<Tip>
  These benchmarks are based on running Activepieces in `SANDBOX_CODE_ONLY` mode. This does **not** represent the performance of Activepieces Cloud, which uses a different sandboxing mechanism to support multi-tenancy. For more information, see [Sandboxing](/install/architecture/workers#sandboxing).
</Tip>


# Stack & Tools
Source: https://www.activepieces.com/docs/install/architecture/stack



## Language

Activepieces uses **Typescript** as its one and only language.
The reason behind unifying the language is the ability for it to break data models and features into packages, which can be shared across its components (worker / frontend / backend).

This enables it to focus on learning fewer tooling options and perfect them across all its packages.

## Frontend

* Web framework/library: [React](https://reactjs.org/)
* Layout/components: [shadcn](https://shadcn.com/) / Tailwind

## Backend

* Framework: [Fastify](https://www.fastify.io/)
* Database: [PostgreSQL](https://www.postgresql.org/)
* Task Queuing: [Redis](https://redis.io/)
* Task Worker: [BullMQ](https://github.com/taskforcesh/bullmq)

## Testing

* Unit & Integration Tests: [Jest](https://jestjs.io/)
* E2E Test: [Playwright](https://playwright.dev/)

## Additional Tools

* Application monitoring: [Sentry](https://sentry.io/welcome/)
* CI/CD: [GitHub Actions](https://github.com/features/actions) / [Depot](https://depot.dev/) / [Kamal](https://kamal-deploy.org/)
* Containerization: [Docker](https://www.docker.com/)
* Linter: [ESLint](https://eslint.org/)
* Logging: [Loki](https://grafana.com/)
* Building: [NX Monorepo](https://nx.dev/)

## Adding New Tool

Adding a new tool isn't a simple choice. A simple choice is one that's easy to do or undo, or one that only affects your work and not others'.

We avoid adding new stuff to increase the ease of setup, which increases adoption. Having more dependencies means more moving parts and support.

If you're thinking about a new tool, ask yourself these:

* Is this tool open source? How can we give it to customers who use their own servers?
* What does it fix, and why do we need it now?
* Can we use what we already have instead?

These questions only apply to required services for everyone. If this tool speeds up your own work, we don't need to think so hard.


# Workers & Sandboxing
Source: https://www.activepieces.com/docs/install/architecture/workers



This component is responsible for polling jobs from the app, preparing the sandbox, and executing them with the engine.

## Jobs

There are three types of jobs:

* **Recurring Jobs**: Polling/schedule triggers jobs for active flows.
* **Flow Jobs**: Flows that are currently being executed.
* **Webhook Jobs**: Webhooks that still need to be ingested, as third-party webhooks can map to multiple flows or need mapping.

<Tip>
  This documentation will not discuss how the engine works other than stating that it takes the jobs and produces the output. Please refer to [engine](./engine) for more information.
</Tip>

## Sandboxing

Sandbox in Activepieces means in which environment the engine will execute the flow. There are four types of sandboxes, each with different trade-offs:

<Snippet file="execution-mode.mdx" />

### No Sandboxing & V8 Sandboxing

The difference between the two modes is in the execution of code pieces. For V8 Sandboxing, we use [isolated-vm](https://www.npmjs.com/package/isolated-vm), which relies on V8 isolation to isolate code pieces.

These are the steps that are used to execute the flow:

<Steps>
  <Step title="Prepare Code Pieces">
    If the code doesn't exist, it will be built with bun with the necessary npm packages will be prepared, if possible.
  </Step>

  <Step title="Install Pieces">
    Pieces are npm packages, we use `bun` to install the pieces.
  </Step>

  <Step title="Execution">
    There is a pool of worker threads kept warm and the engine stays running and listening. Each thread executes one engine operation and sends back the result upon completion.
  </Step>
</Steps>

#### Security:

In a self-hosted environment, all piece installations are done by the **platform admin**. It is assumed that the pieces are secure, as they have full access to the machine.

Code pieces provided by the end user are isolated using V8, which restricts the user to browser JavaScript instead of Node.js with npm.

#### Performance

The flow execution is fast as the javascript can be, although there is overhead in polling from queue and prepare the files first time the flow get executed.

#### Benchmark

TBD

### Kernel Namespaces Sandboxing

This consists of two steps: the first one is preparing the sandbox, and the other one is the execution part.

#### Prepare the folder

Each flow will have a folder with everything required to execute this flows, which means the **engine**, **code pieces** and **npms**

<Steps>
  <Step title="Prepare Code Pieces">
    If the code doesn't exist, it will be compiled using TypeScript Compiler (tsc) and the necessary npm packages will be prepared, if possible.
  </Step>

  <Step title="Install Pieces">
    Pieces are npm packages, we perform simple check If they don't exist we use `pnpm` to install the pieces.
  </Step>
</Steps>

#### Execute Flow using Sandbox

In this mode, we use kernel namespaces to isolate everything (file system, memory, CPU). The folder prepared earlier will be bound as a **Read Only** Directory.

Then we use the command line and to spin up the isolation with new node process, something like that.

```bash  theme={null}
./isolate node path/to/flow.js --- rest of args
```

#### Security

The flow execution is isolated in their own namespaces, which means pieces are isolated in different process and namespaces, So the user can run bash scripts and use the file system safely as It's limited and will be removed after the execution, in this mode the user can use any **NPM package** in their code piece.

#### Performance

This mode is **Slow** and **CPU Intensive**. The reason behind this is the **cold boot** of Node.js, since each flow execution will require a new **Node.js** process. The Node.js process consumes a lot of resources and takes some time to compile the code and start executing.

#### Benchmark

TBD


# Environment Variables
Source: https://www.activepieces.com/docs/install/configuration/environment-variables



To configure activepieces, you will need to set some environment variables, There is file called `.env` at the root directory for our main repo.

<Tip> When you execute the [tools/deploy.sh](https://github.com/activepieces/activepieces/blob/main/tools/deploy.sh) script in the Docker installation tutorial,
it will produce these values. </Tip>

## Environment Variables

| Variable                                  | Description                                                                                                                                                                                                                                                                                                                   | Default Value                                          | Example                                                                |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------- |
| `AP_CONFIG_PATH`                          | Optional parameter for specifying the path to store SQLite3 and local settings.                                                                                                                                                                                                                                               | `~/.activepieces`                                      |                                                                        |
| `AP_CLOUD_AUTH_ENABLED`                   | Turn off the utilization of Activepieces oauth2 applications                                                                                                                                                                                                                                                                  | `false`                                                |                                                                        |
| `AP_DB_TYPE`                              | The type of database to use. (POSTGRES / SQLITE3)                                                                                                                                                                                                                                                                             | `SQLITE3`                                              |                                                                        |
| `AP_EXECUTION_MODE`                       | You can choose between 'SANDBOX\_PROCESS', 'UNSANDBOXED', 'SANDBOX\_CODE\_ONLY', 'SANDBOX\_CODE\_AND\_PROCESS' as possible values. If you decide to change this, make sure to carefully read [https://www.activepieces.com/docs/install/architecture/workers](https://www.activepieces.com/docs/install/architecture/workers) | `UNSANDBOXED`                                          |                                                                        |
| `AP_WORKER_CONCURRENCY`                   | The number of different scheduled worker jobs can be processed in same time                                                                                                                                                                                                                                                   | `10`                                                   |                                                                        |
| `AP_AGENTS_WORKER_CONCURRENCY`            | The number of different agents can be processed in same time                                                                                                                                                                                                                                                                  | `10`                                                   |                                                                        |
| `AP_ENCRYPTION_KEY`                       | ❗️ Encryption key used for connections is a 32-character (16 bytes) hexadecimal key. You can generate one using the following command: `openssl rand -hex 16`.                                                                                                                                                                | None                                                   |                                                                        |
| `AP_EXECUTION_DATA_RETENTION_DAYS`        | The number of days to retain execution data, logs and events.                                                                                                                                                                                                                                                                 | `30`                                                   |                                                                        |
| `AP_FRONTEND_URL`                         | ❗️ Url that will be used to specify redirect url and webhook url.                                                                                                                                                                                                                                                             |                                                        |                                                                        |
| `AP_INTERNAL_URL`                         | (BETA) Used to specify the SSO authentication URL.                                                                                                                                                                                                                                                                            | None                                                   | [https://demo.activepieces.com/api](https://demo.activepieces.com/api) |
| `AP_JWT_SECRET`                           | ❗️ Encryption key used for generating JWT tokens is a 32-character hexadecimal key. You can generate one using the following command: `openssl rand -hex 32`.                                                                                                                                                                 | None                                                   | [https://demo.activepieces.com](https://demo.activepieces.com)         |
| `AP_REDIS_TYPE`                           | Where to spin redis instance, either in memory (MEMORY) or in a dedicated instance (STANDALONE), or in a sentinel instance (SENTINEL)                                                                                                                                                                                         | `STANDALONE`                                           |                                                                        |
| `AP_QUEUE_UI_ENABLED`                     | Enable the queue UI (only works with redis)                                                                                                                                                                                                                                                                                   | `true`                                                 |                                                                        |
| `AP_QUEUE_UI_USERNAME`                    | The username for the queue UI. This is required if `AP_QUEUE_UI_ENABLED` is set to `true`.                                                                                                                                                                                                                                    | None                                                   |                                                                        |
| `AP_QUEUE_UI_PASSWORD`                    | The password for the queue UI. This is required if `AP_QUEUE_UI_ENABLED` is set to `true`.                                                                                                                                                                                                                                    | None                                                   |                                                                        |
| `AP_REDIS_FAILED_JOB_RETENTION_DAYS`      | The number of days to retain failed jobs in Redis.                                                                                                                                                                                                                                                                            | `30`                                                   |                                                                        |
| `AP_REDIS_FAILED_JOB_RETENTION_MAX_COUNT` | The maximum number of failed jobs to retain in Redis.                                                                                                                                                                                                                                                                         | `2000`                                                 |                                                                        |
| `AP_TRIGGER_DEFAULT_POLL_INTERVAL`        | The default polling interval determines how frequently the system checks for new data updates for pieces with scheduled triggers, such as new Google Contacts.                                                                                                                                                                | `5`                                                    |                                                                        |
| `AP_PIECES_SOURCE`                        | `AP_PIECES_SOURCE`: `FILE` for local development, `DB` for database. You can find more information about it in [Setting Piece Source](#setting-piece-source) section.                                                                                                                                                         | `CLOUD_AND_DB`                                         |                                                                        |
| `AP_PIECES_SYNC_MODE`                     | `AP_PIECES_SYNC_MODE`: None for no metadata syncing / 'OFFICIAL\_AUTO' for automatic syncing for pieces metadata from cloud                                                                                                                                                                                                   | `OFFICIAL_AUTO`                                        |                                                                        |
| `AP_POSTGRES_DATABASE`                    | ❗️ The name of the PostgreSQL database                                                                                                                                                                                                                                                                                        | None                                                   |                                                                        |
| `AP_POSTGRES_HOST`                        | ❗️ The hostname or IP address of the PostgreSQL server                                                                                                                                                                                                                                                                        | None                                                   |                                                                        |
| `AP_POSTGRES_PASSWORD`                    | ❗️ The password for the PostgreSQL,  you can generate a 32-character hexadecimal key using the following command: `openssl rand -hex 32`.                                                                                                                                                                                     | None                                                   |                                                                        |
| `AP_POSTGRES_PORT`                        | ❗️ The port number for the PostgreSQL server                                                                                                                                                                                                                                                                                  | None                                                   |                                                                        |
| `AP_POSTGRES_USERNAME`                    | ❗️ The username for the PostgreSQL user                                                                                                                                                                                                                                                                                       | None                                                   |                                                                        |
| `AP_POSTGRES_USE_SSL`                     | Use SSL to connect the postgres database                                                                                                                                                                                                                                                                                      | `false`                                                |                                                                        |
| `AP_POSTGRES_SSL_CA`                      | Use SSL Certificate to connect to the postgres database                                                                                                                                                                                                                                                                       |                                                        |                                                                        |
| `AP_POSTGRES_URL`                         | Alternatively, you can specify only the connection string (e.g postgres\://user:password\@host:5432/database) instead of providing the database, host, port, username, and password.                                                                                                                                          | None                                                   |                                                                        |
| `AP_POSTGRES_POOL_SIZE`                   | Maximum number of clients the pool should contain for the PostgreSQL database                                                                                                                                                                                                                                                 | None                                                   |                                                                        |
| `AP_POSTGRES_IDLE_TIMEOUT_MS`             | Sets the idle timout  pool for your PostgreSQL                                                                                                                                                                                                                                                                                | `30000`                                                |                                                                        |
| `AP_REDIS_TYPE`                           | Type of Redis, Possible values are `DEFAULT` or `SENTINEL`.                                                                                                                                                                                                                                                                   | `30000`                                                |                                                                        |
| `AP_REDIS_URL`                            | If a Redis connection URL is specified, all other Redis properties will be ignored.                                                                                                                                                                                                                                           | None                                                   |                                                                        |
| `AP_REDIS_USER`                           | ❗️ Username to use when connect to redis                                                                                                                                                                                                                                                                                      | None                                                   |                                                                        |
| `AP_REDIS_PASSWORD`                       | ❗️ Password to use when connect to redis                                                                                                                                                                                                                                                                                      | None                                                   |                                                                        |
| `AP_REDIS_HOST`                           | ❗️ The hostname or IP address of the Redis server                                                                                                                                                                                                                                                                             | None                                                   |                                                                        |
| `AP_REDIS_PORT`                           | ❗️ The port number for the Redis server                                                                                                                                                                                                                                                                                       | None                                                   |                                                                        |
| `AP_REDIS_DB`                             | The Redis database index to use                                                                                                                                                                                                                                                                                               | `0`                                                    |                                                                        |
| `AP_REDIS_USE_SSL`                        | Connect to Redis with SSL                                                                                                                                                                                                                                                                                                     | `false`                                                |                                                                        |
| `AP_REDIS_SSL_CA_FILE`                    | The path to the CA file for the Redis server.                                                                                                                                                                                                                                                                                 | None                                                   |                                                                        |
| `AP_REDIS_SENTINEL_HOSTS`                 | If specified, this should be a comma-separated list of `host:port` pairs for Redis Sentinels. Make sure to set `AP_REDIS_CONNECTION_MODE` to `SENTINEL`                                                                                                                                                                       | None                                                   | `sentinel-host-1:26379,sentinel-host-2:26379,sentinel-host-3:26379`    |
| `AP_REDIS_SENTINEL_NAME`                  | The name of the master node monitored by the sentinels.                                                                                                                                                                                                                                                                       | None                                                   | `sentinel-host-1`                                                      |
| `AP_REDIS_SENTINEL_ROLE`                  | The role to connect to, either `master` or `slave`.                                                                                                                                                                                                                                                                           | None                                                   | `master`                                                               |
| `AP_TRIGGER_TIMEOUT_SECONDS`              | Maximum allowed runtime for a trigger to perform polling in seconds                                                                                                                                                                                                                                                           | `60`                                                   |                                                                        |
| `AP_FLOW_TIMEOUT_SECONDS`                 | Maximum allowed runtime for a flow to run in seconds                                                                                                                                                                                                                                                                          | `600`                                                  |                                                                        |
| `AP_AGENT_TIMEOUT_SECONDS`                | Maximum allowed runtime for an agent to run in seconds                                                                                                                                                                                                                                                                        | `600`                                                  |                                                                        |
| `AP_SANDBOX_MEMORY_LIMIT`                 | The maximum amount of memory (in kilobytes) that a single sandboxed worker process can use. This helps prevent runaway memory usage in custom code or pieces. If not set, the default is 524288 KB (512 MB).                                                                                                                  | `524288`                                               | `1048576`                                                              |
| `AP_SANDBOX_PROPAGATED_ENV_VARS`          | Environment variables that will be propagated to the sandboxed code. If you are using it for pieces, we strongly suggests keeping everything in the authentication object to make sure it works across AP instances.                                                                                                          | None                                                   |                                                                        |
| `AP_TELEMETRY_ENABLED`                    | Collect telemetry information.                                                                                                                                                                                                                                                                                                | `true`                                                 |                                                                        |
| `AP_TEMPLATES_SOURCE_URL`                 | This is the endpoint we query for templates, remove it and templates will be removed from UI                                                                                                                                                                                                                                  | `https://cloud.activepieces.com/api/v1/flow-templates` |                                                                        |
| `AP_WEBHOOK_TIMEOUT_SECONDS`              | The default timeout for webhooks. The maximum allowed is 15 minutes. Please note that Cloudflare limits it to 30 seconds. If you are using a reverse proxy for SSL, make sure it's configured correctly.                                                                                                                      | `30`                                                   |                                                                        |
| `AP_TRIGGER_FAILURE_THRESHOLD`            | The maximum number of consecutive trigger failures is 576 by default, which is equivalent to approximately 2 days.                                                                                                                                                                                                            | `30`                                                   |                                                                        |
| `AP_PROJECT_RATE_LIMITER_ENABLED`         | Enforce rate limits and prevent excessive usage by a single project.                                                                                                                                                                                                                                                          | `true`                                                 |                                                                        |
| `AP_MAX_CONCURRENT_JOBS_PER_PROJECT`      | The maximum number of active runs a project can have. This is used to enforce rate limits and prevent excessive usage by a single project.                                                                                                                                                                                    | `100`                                                  |                                                                        |
| `AP_S3_ACCESS_KEY_ID`                     | The access key ID for your S3-compatible storage service. Not required if `AP_S3_USE_IRSA` is `true`.                                                                                                                                                                                                                         | None                                                   |                                                                        |
| `AP_S3_SECRET_ACCESS_KEY`                 | The secret access key for your S3-compatible storage service. Not required if `AP_S3_USE_IRSA` is `true`.                                                                                                                                                                                                                     | None                                                   |                                                                        |
| `AP_S3_BUCKET`                            | The name of the S3 bucket to use for file storage.                                                                                                                                                                                                                                                                            | None                                                   |                                                                        |
| `AP_S3_ENDPOINT`                          | The endpoint URL for your S3-compatible storage service. Not required if `AWS_ENDPOINT_URL` is set.                                                                                                                                                                                                                           | None                                                   | `https://s3.amazonaws.com`                                             |
| `AP_S3_REGION`                            | The region where your S3 bucket is located. Not required if `AWS_REGION` is set.                                                                                                                                                                                                                                              | None                                                   | `us-east-1`                                                            |
| `AP_S3_USE_SIGNED_URLS`                   | It is used to route traffic to S3 directly. It should be enabled if the S3 bucket is public.                                                                                                                                                                                                                                  | None                                                   |                                                                        |
| `AP_S3_USE_IRSA`                          | Use IAM Role for Service Accounts (IRSA) to connect to S3. When `true`, `AP_S3_ACCESS_KEY_ID` and `AP_S3_ACCESS_KEY_ID` are not required.                                                                                                                                                                                     | None                                                   | `true`                                                                 |
| `AP_SMTP_HOST`                            | The host name for the SMTP server that activepieces uses to send emails                                                                                                                                                                                                                                                       | `None`                                                 | `mail.example.com`                                                     |
| `AP_SMTP_PORT`                            | The port number for the SMTP server that activepieces uses to send emails                                                                                                                                                                                                                                                     | `None`                                                 | 587                                                                    |
| `AP_SMTP_USERNAME`                        | The user name for the SMTP server that activepieces uses to send emails                                                                                                                                                                                                                                                       | `None`                                                 | [test@mail.example.com](mailto:test@mail.example.com)                  |
| `AP_SMTP_PASSWORD`                        | The password for the SMTP server that activepieces uses to send emails                                                                                                                                                                                                                                                        | `None`                                                 | secret1234                                                             |
| `SMTP_SENDER_EMAIL`                       | The email address from which activepieces sends emails.                                                                                                                                                                                                                                                                       | `None`                                                 | [test@mail.example.com](mailto:test@mail.example.com)                  |
| `SMTP_SENDER_NAME`                        | The sender name activepieces uses to send emails.                                                                                                                                                                                                                                                                             |                                                        |                                                                        |
| `AP_MAX_FILE_SIZE_MB`                     | The maximum allowed file size in megabytes for uploads including logs of flow runs. If logs exceed this size, they will be truncated which may cause flow execution issues.                                                                                                                                                   | `10`                                                   | `10`                                                                   |
| `AP_FILE_STORAGE_LOCATION`                | The location to store files. Possible values are `DB` for storing files in the database or `S3` for storing files in an S3-compatible storage service.                                                                                                                                                                        | `DB`                                                   |                                                                        |
| `AP_PAUSED_FLOW_TIMEOUT_DAYS`             | The maximum allowed pause duration in days for a paused flow, please note it can not exceed `AP_EXECUTION_DATA_RETENTION_DAYS`                                                                                                                                                                                                | `30`                                                   |                                                                        |
| `AP_MAX_RECORDS_PER_TABLE`                | The maximum allowed number of records per table                                                                                                                                                                                                                                                                               | `1500`                                                 | `1500`                                                                 |
| `AP_MAX_FIELDS_PER_TABLE`                 | The maximum allowed number of fields per table                                                                                                                                                                                                                                                                                | `15`                                                   | `15`                                                                   |
| `AP_MAX_TABLES_PER_PROJECT`               | The maximum allowed number of tables per project                                                                                                                                                                                                                                                                              | `20`                                                   | `20`                                                                   |
| `AP_MAX_MCPS_PER_PROJECT`                 | The maximum allowed number of mcp per project                                                                                                                                                                                                                                                                                 | `20`                                                   | `20`                                                                   |
| `AP_ENABLE_FLOW_ON_PUBLISH`               | Whether publishing a new flow version should automatically enable the flow                                                                                                                                                                                                                                                    | `true`                                                 | `false`                                                                |
| `AP_ISSUE_ARCHIVE_DAYS`                   | Controls the automatic archival of issues in the system. Issues that have not been updated for this many days will be automatically moved to an archived state.                                                                                                                                                               | `14`                                                   | `1`                                                                    |
| `AP_APP_TITLE`                            | Initial title shown in the browser tab while loading the app                                                                                                                                                                                                                                                                  | `Activepieces`                                         | `Activepieces`                                                         |
| `AP_FAVICON_URL`                          | Initial favicon shown in the browser tab while loading the app                                                                                                                                                                                                                                                                | `https://cdn.activepieces.com/brand/favicon.ico`       | `https://cdn.activepieces.com/brand/favicon.ico`                       |

### OpenTelemetry Configuration

Activepieces supports both standard OpenTelemetry environment variables and vendor-specific configuration for observability and tracing.

#### OpenTelemetry Environment Variables

| Variable                      | Description                                                 | Default Value | Example                                 |
| ----------------------------- | ----------------------------------------------------------- | ------------- | --------------------------------------- |
| `AP_OTEL_ENABLED`             | Enable OpenTelemetry tracing                                | `false`       | `true`                                  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP exporter endpoint URL                                  | None          | `https://your-collector:4317/v1/traces` |
| `OTEL_EXPORTER_OTLP_HEADERS`  | Headers for OTLP exporter (comma-separated key=value pairs) | None          | `Authorization=Bearer token`            |

**Note**: Both `AP_OTEL_ENABLED` and `OTEL_EXPORTER_OTLP_ENDPOINT` must be set for OpenTelemetry to be enabled.

<Warning>
  The frontend URL is essential for webhooks and app triggers to work. It must
  be accessible to third parties to send data.
</Warning>

### Setting Webhook (Frontend URL):

The default URL is set to the machine's IP address. To ensure proper operation, ensure that this address is accessible or specify an `AP_FRONTEND_URL` environment variable.

One possible solution for this is using a service like ngrok ([https://ngrok.com/](https://ngrok.com/)), which can be used to expose the frontend port (4200) to the internet.

### Setting Piece Source

These are the different options for the `AP_PIECES_SOURCE` environment variable:

1. `FILE`: **Only for Local Development**, this option loads pieces directly from local files. For Production, please consider using other options, as this one only supports a single version per piece.

2. `DB`: This option will only load pieces that are manually installed in the database from "My Pieces" or the Admin Console in the EE Edition. Pieces are loaded from npm, which provides multiple versions per piece, making it suitable for production.

You can also set AP\_PIECES\_SYNC\_MODE to `OFFICIAL_AUTO`, where it will update the metadata of pieces periodically.

### Redis Configuration

Set the `AP_REDIS_URL` environment variable to the connection URL of your Redis server.

Please note that if a Redis connection URL is specified, all other **Redis properties** will be ignored.

<Info>
  If you don't have the Redis URL, you can use the following command to get it. You can use the following variables:

  * `REDIS_USER`: The username to use when connecting to Redis.
  * `REDIS_PASSWORD`: The password to use when connecting to Redis.
  * `REDIS_HOST`: The hostname or IP address of the Redis server.
  * `REDIS_PORT`: The port number for the Redis server.
  * `REDIS_DB`: The Redis database index to use.
  * `REDIS_USE_SSL`: Connect to Redis with SSL.
</Info>

<Info>
  If you are using **Redis Sentinel**, you can set the following environment variables:

  * `AP_REDIS_TYPE`: Set this to `SENTINEL`.
  * `AP_REDIS_SENTINEL_HOSTS`: A comma-separated list of `host:port` pairs for Redis Sentinels. When set, all other Redis properties will be ignored.
  * `AP_REDIS_SENTINEL_NAME`: The name of the master node monitored by the sentinels.
  * `AP_REDIS_SENTINEL_ROLE`: The role to connect to, either `master` or `slave`.
  * `AP_REDIS_PASSWORD`: The password to use when connecting to Redis.
  * `AP_REDIS_USE_SSL`: Connect to Redis with SSL.
  * `AP_REDIS_SSL_CA_FILE`: The path to the CA file for the Redis server.
</Info>

### SMTP Configuration

SMTP can be configured both from the platform admin screen and through environment variables. The enviroment variables are only used if the platform admin screen has no email configuration entered.

Activepieces will only use the configuration from the environment variables if `AP_SMTP_HOST`, `AP_SMTP_PORT`, `AP_SMTP_USERNAME` and `AP_SMTP_PASSWORD` all have a value set. TLS is supported.


# Hardware Requirements
Source: https://www.activepieces.com/docs/install/configuration/hardware

Specifications for hosting Activepieces

More information about architecture please visit our [architecture](../architecture/overview) page.

### Technical Specifications

Activepieces is designed to be memory-intensive rather than CPU-intensive. A modest instance will suffice for most scenarios, but requirements can vary based on specific use cases.

| Component    | Memory (RAM) | CPU Cores | Notes |
| ------------ | ------------ | --------- | ----- |
| PostgreSQL   | 1 GB         | 1         |       |
| Redis        | 1 GB         | 1         |       |
| Activepieces | 4 GB         | 1         |       |

<Tip>
  The above recommendations are designed to meet the needs of the majority of use cases.
</Tip>

## Scaling Factors

### Redis

Redis requires minimal scaling as it primarily stores jobs during processing. Activepieces leverages BullMQ, capable of handling a substantial number of jobs per second.

### PostgreSQL

<Tip>
  **Scaling Tip:** Since files are stored in the database, you can alleviate the load by configuring S3 storage for file management.
</Tip>

PostgreSQL is typically not the system's bottleneck.

### Activepieces Container

<Tip>
  **Scaling Tip:** The Activepieces container is stateless, allowing for seamless horizontal scaling.
</Tip>

* `FLOW_WORKER_CONCURRENCY` and `SCHEDULED_WORKER_CONCURRENCY` dictate the number of concurrent jobs processed for flows and scheduled flows, respectively. By default, these are set to 20 and 10.

## Expected Performance

Activepieces ensures no request is lost; all requests are queued. In the event of a spike, requests will be processed later, which is acceptable as most flows are asynchronous, with synchronous flows being prioritized.

It's hard to predict exact performance because flows can be very different. But running a flow doesn't slow things down, as it runs as fast as regular JavaScript.
(Note: This applies to `SANDBOX_CODE_ONLY` and `UNSANDBOXED` execution modes, which are recommended and used in self-hosted setups.)

You can anticipate handling over **20 million executions** monthly with this setup.


# Deployment Checklist
Source: https://www.activepieces.com/docs/install/configuration/overview

Checklist to follow after deploying Activepieces

<Info>
  This tutorial assumes you have already followed the quick start guide using one of the installation methods listed in [Install Overview](../overview).
</Info>

In this section, we will go through the checklist after using one of the installation methods and ensure that your deployment is production-ready.

<AccordionGroup>
  <Accordion title="Decide on Sandboxing" icon="code">
    You should decide on the sandboxing mode for your deployment based on your use case and whether it is multi-tenant or not. Here is a simplified way to decide:

    <Tip>
      **Friendly Tip #1**: For multi-tenant setups, use V8/Code Sandboxing.

      It is secure and does not require privileged Docker access in Kubernetes.
      Privileged Docker is usually not allowed to prevent root escalation threats.
    </Tip>

    <Tip>
      **Friendly Tip #2**: For single-tenant setups, use No Sandboxing. It is faster and does not require privileged Docker access.
    </Tip>

    <Snippet file="execution-mode.mdx" />

    More Information at [Sandboxing & Workers](../architecture/workers#sandboxing)
  </Accordion>

  <Accordion title="Enterprise Edition (Optional)" icon="building">
    <Tip>
      For licensing inquiries regarding the self-hosted enterprise edition, please reach out to `sales@activepieces.com`, as the code and Docker image are not covered by the MIT license.
    </Tip>

    <Note>You can request a trial key from within the app or in the cloud by filling out the form. Alternatively, you can contact sales at [https://www.activepieces.com/sales](https://www.activepieces.com/sales).<br />Please know that when your trial runs out, all enterprise [features](/about/editions#feature-comparison) will be shut down meaning any user other than the platform admin will be deactivated, and your private pieces will be deleted, which could result in flows using them to fail.</Note>

    <Warning>
      Enterprise Edition only works on Fresh Installation as the database migration scripts are different from the community edition.
    </Warning>

    <Warning>
      Enterprise edition must use `PostgreSQL` as the database backend and `Redis` as the Queue System.
    </Warning>

    ## Installation

    1. Set the `AP_EDITION` environment variable to `ee`.
    2. Set the `AP_EXECUTION_MODE` to anything other than `UNSANDBOXED`, check the above section.
    3. Once your instance is up, activate the license key by going to **Platform Admin -> Setup -> License Keys**.

        <img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=abc2db5befaabf039899a23fd75d9470" alt="Activation License Key" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/activation-license-key-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=4a9e7f5cce1de95854a23131197452df 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f3aee8442dde13d03ae2ae978b1dd2f4 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=f6638ba4fa57d7256ec79d9e82ff55aa 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=2bce94354609c5ee9d77656dd0490648 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=e956a826e5d82a0e77a885ec6dfee2b0 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/activation-license-key-settings.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=a9c2344b6be067b18b8367440d4cbf3c 2500w" />
  </Accordion>

  <Accordion title="Setup HTTPS" icon="lock">
    Setting up HTTPS is highly recommended because many services require webhook URLs to be secure (HTTPS). This helps prevent potential errors.

    To set up SSL, you can use any reverse proxy. For a step-by-step guide, check out our example using [Nginx](./setup-ssl).
  </Accordion>

  <Accordion title="Configure S3 (Optional)" icon="cloud">
    Run logs and files are stored in the database by default, but you can switch to S3 later without any migration; for most cases, the database is enough.

    It's recommended to start with the database and switch to S3 if needed. After switching, expired files in the database will be deleted, and everything will be stored in S3. No manual migration is needed.

    Configure the following environment variables:

    * `AP_S3_ACCESS_KEY_ID`
    * `AP_S3_SECRET_ACCESS_KEY`
    * `AP_S3_ENDPOINT`
    * `AP_S3_BUCKET`
    * `AP_S3_REGION`
    * `AP_MAX_FILE_SIZE_MB`
    * `AP_FILE_STORAGE_LOCATION` (set to `S3`)
    * `AP_S3_USE_SIGNED_URLS`

    <Tip>
      **Friendly Tip #1**: If the S3 bucket supports signed URLs but needs to be accessible over a public network, you can set `AP_S3_USE_SIGNED_URLS` to `true` to route traffic directly to S3 and reduce heavy traffic on your API server.
    </Tip>
  </Accordion>

  <Accordion title="Troubleshooting (Optional)" icon="wrench">
    If you encounter any issues, check out our [Troubleshooting](./troubleshooting) guide.
  </Accordion>
</AccordionGroup>


# Separate Workers from App
Source: https://www.activepieces.com/docs/install/configuration/separate-workers



Benefits of separating workers from the main application (APP):

* **Availability**: The application remains lightweight, allowing workers to be scaled independently.
* **Security**: Workers lack direct access to Redis and the database, minimizing impact in case of a security breach.

<Steps>
  <Step title="Create Worker Token">
    To create a worker token, use the local CLI command to generate the JWT and sign it with your `AP_JWT_SECRET` used for the app server. Follow these steps:

    1. Open your terminal and navigate to the root of the repository.
    2. Run the command: `npm run workers token`.
    3. When prompted, enter the JWT secret (this should be the same as the `AP_JWT_SECRET` used for the app server).
    4. The generated token will be displayed in your terminal, copy it and use it in the next step.
       <img src="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=385159c04bb0a8add654f66efcf801ca" alt="Workers Token" data-og-width="1596" width="1596" data-og-height="186" height="186" data-path="resources/worker-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=280&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=e9afc1093ed882c2688803ec9963534c 280w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=560&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=579f183a1795dcc0c8f6f8c598b02781 560w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=840&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=7431803b6afe1b8929ad90010f60dc8d 840w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=1100&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=0598c948aa2735fabff5df63d6d2aea1 1100w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=1650&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=1cc59fff58465f5edac646a3f3ced201 1650w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/worker-token.png?w=2500&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=8c72dc84eb5a54a7b53a756ea9e45727 2500w" />
  </Step>

  <Step title="Configure Environment Variables">
    Define the following environment variables in the `.env` file on the worker machine:

    * Set `AP_CONTAINER_TYPE` to `WORKER`
    * Specify `AP_FRONTEND_URL`
    * Provide `AP_WORKER_TOKEN`
  </Step>

  <Step title="Configure Persistent Volume">
    Configure a persistent volume for the worker to cache flows and pieces. This is important as first uncached execution of pieces and flows are very slow. Having a persistent volume significantly improves execution speed.

    Add the following volume mapping to your docker configuration:

    ```yaml  theme={null}
    volumes:
      - <your path>:/usr/src/app/cache
    ```

    Note: This setup works whether you attach one volume per worker, It cannot be shared across multiple workers.
  </Step>

  <Step title="Launch Worker Machine">
    Launch the worker machine and supply it with the generated token.
  </Step>

  <Step title="Verify Worker Operation">
    Verify that the workers are visible in the Platform Admin Console under Infra -> Workers.
    <img src="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=0156f35f93278e16e9a0f461cf3a2282" alt="Workers Infrastructure" data-og-width="1846" width="1846" data-og-height="1002" height="1002" data-path="resources/workers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=280&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=df0e889fac81ad27560d0eb42dd99c1b 280w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=560&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=686369eaa1c9d299c185dd90e66fe250 560w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=840&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=91dba13ef1a08af7feb9873afe874aab 840w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=1100&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=e826bd5fc83a83484a8bf18791eff058 1100w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=1650&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=60e0e99f7f110057e2b353a3dcc59bec 1650w, https://mintcdn.com/activepieces/GuwRiJeBZ7P6V9LF/resources/workers.png?w=2500&fit=max&auto=format&n=GuwRiJeBZ7P6V9LF&q=85&s=04fb7d7d3172c787634fcce9e1fae150 2500w" />
  </Step>

  <Step title="Configure App Container Type">
    On the APP machine, set `AP_CONTAINER_TYPE` to `APP`.
  </Step>
</Steps>


# Setup App Webhooks
Source: https://www.activepieces.com/docs/install/configuration/setup-app-webhooks



Certain apps like Slack and Square only support one webhook per OAuth2 app. This means that manual configuration is required in their developer portal, and it cannot be automated.

## Slack

**Configure Webhook Secret**

1. Visit the "Basic Information" section of your Slack OAuth settings.
2. Copy the "Signing Secret" and save it.
3. Set the following environment variable in your activepieces environment:
   ```
   AP_APP_WEBHOOK_SECRETS={"@activepieces/piece-slack": {"webhookSecret": "SIGNING_SECRET"}}
   ```
4. Restart your application instance.

**Configure Webhook URL**

1. Go to the "Event Subscription" settings in the Slack OAuth2 developer platform.
2. The URL format should be: `https://YOUR_AP_INSTANCE/api/v1/app-events/slack`.
3. When connecting to Slack, use your OAuth2 credentials or update the OAuth2 app details from the admin console (in platform plans).
4. Add the following events to the app:
   * `message.channels`
   * `reaction_added`
   * `message.im`
   * `message.groups`
   * `message.mpim`
   * `app_mention`


# Setup HTTPS
Source: https://www.activepieces.com/docs/install/configuration/setup-ssl



To enable SSL, you can use a reverse proxy. In this case, we will use Nginx as the reverse proxy.

## Install Nginx

```bash  theme={null}
sudo apt-get install nginx
```

## Create Certificate

To proceed with this documentation, it is assumed that you already have a certificate for your domain.

<Tip>
  You have the option to use Cloudflare or generate a certificate using Let's Encrypt or Certbot.
</Tip>

Add the certificate to the following paths: `/etc/key.pem` and `/etc/cert.pem`

## Setup Nginx

```bash  theme={null}
sudo nano /etc/nginx/sites-available/default
```

```bash  theme={null}
server {
    listen 80;
    listen [::]:80;

    server_name example.com www.example.com;

    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;

    server_name example.com www.example.com;

    ssl_certificate /etc/cert.pem;
    ssl_certificate_key /etc/key.pem;

    location / {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;        
    }
}
```

## Restart Nginx

```bash  theme={null}
sudo systemctl restart nginx
```

## Test

Visit your domain and you should see your application running with SSL.


# Troubleshooting
Source: https://www.activepieces.com/docs/install/configuration/troubleshooting



### Websocket Connection Issues

If you're experiencing issues with websocket connections, it's likely due to incorrect proxy configuration. Common symptoms include:

* Test Flow button not working
* Test step in flows not working
* Real-time updates not showing

To resolve these issues:

1. Ensure your reverse proxy is properly configured for websocket connections
2. Check our [Setup HTTPS](./setup-ssl) guide for correct configuration examples
3. Some browser block http websocket connections, please setup ssl to resolve this issue.

### Runs with Internal Errors or Scheduling Issues

If you're experiencing issues with flow runs showing internal errors or scheduling problems:

[BullBoard dashboard](/handbook/engineering/playbooks/bullboard)

### Truncated logs

If you see `(truncated)` in the flow run logs in your flow runs, it means that the logs have exceeded the maximum allowed file size. You can increase the `AP_MAX_FILE_SIZE_MB` environment variable to a higher value to resolve this issue.

### Reset Password

If you forgot your password on self hosted instance, you can reset it using the following steps:

**Postgres**

1. **Locate PostgreSQL Docker Container**:
   * Use a command like `docker ps` to find the PostgreSQL container.

2. **Access the Container**:
   * Use SSH to access the PostgreSQL Docker container.
   ```bash  theme={null}
   docker exec -it POSTGRES_CONTAINER_ID /bin/bash
   ```

3. **Open the PostgreSQL Console**:
   * Inside the container, open the PostgreSQL console with the `psql` command.
   ```bash  theme={null}
   psql -U postgres
   ```

4. **Connect to the ActivePieces Database**:
   * Connect to the ActivePieces database.
   ```sql  theme={null}
   \c activepieces
   ```

5. **Create a Secure Password**:
   * Use a tool like [bcrypt-generator.com](https://bcrypt-generator.com/) to generate a new secure password, number of rounds is 10.

6. **Update Your Password**:
   * Run the following SQL query within the PostgreSQL console, replacing `HASH_PASSWORD` with your new password and `YOUR_EMAIL_ADDRESS` with your email.
   ```sql  theme={null}
   UPDATE public.user_identity SET password='HASH_PASSWORD' WHERE email='YOUR_EMAIL_ADDRESS';
   ```

**SQLite3**

1. **Open the SQLite3 Shell**:
   * Access the SQLite3 database by opening the SQLite3 shell. Replace "database.db" with the actual name of your SQLite3 database file if it's different.
   ```bash  theme={null}
   sqlite3 ~/.activepieces/database.sqlite
   ```

2. **Create a Secure Password**:
   * Use a tool like [bcrypt-generator.com](https://bcrypt-generator.com/) to generate a new secure password, number of rounds is 10.

3. **Reset Your Password**:
   * Once inside the SQLite3 shell, you can update your password with an SQL query. Replace `HASH_PASSWORD` with your new password and `YOUR_EMAIL_ADDRESS` with your email.
   ```sql  theme={null}
   UPDATE user_identity SET password = 'HASH_PASSWORD' WHERE email = 'YOUR_EMAIL_ADDRESS';
   ```

4. **Exit the SQLite3 Shell**:
   * After making the changes, exit the SQLite3 shell by typing:
   ```bash  theme={null}
   .exit
   ```


# AWS (Pulumi)
Source: https://www.activepieces.com/docs/install/options/aws

Get Activepieces up & running on AWS with Pulumi for IaC

# Infrastructure-as-Code (IaC) with Pulumi

Pulumi is an IaC solution akin to Terraform or CloudFormation that lets you deploy & manage your infrastructure using popular programming languages e.g. Typescipt (which we'll use), C#, Go etc.

## Deploy from Pulumi Cloud

If you're already familiar with Pulumi Cloud and have [integrated their services with your AWS account](https://www.pulumi.com/docs/pulumi-cloud/deployments/oidc/aws/#configuring-openid-connect-for-aws), you can use the button below to deploy Activepieces in a few clicks.
The template will deploy the latest Activepieces image that's available on [Docker Hub](https://hub.docker.com/r/activepieces/activepieces).

[![Deploy with Pulumi](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new?template=https://github.com/activepieces/activepieces/tree/main/deploy/pulumi)

## Deploy from a local environment

Or, if you're currently using an S3 bucket to maintain your Pulumi state, you can scaffold and deploy Activepieces direct from Docker Hub using the template below in just few commands:

```bash  theme={null}
$ mkdir deploy-activepieces && cd deploy-activepieces 
$ pulumi new https://github.com/activepieces/activepieces/tree/main/deploy/pulumi
$ pulumi up
```

## What's Deployed?

The template is setup to be somewhat flexible, supporting what could be a development or more production-ready configuration.
The configuration options that are presented during stack configuration will allow you to optionally add any or all of:

* PostgreSQL RDS instance. Opting out of this will use a local SQLite3 Db.
* Single node Redis 7 cluster. Opting out of this will mean using an in-memory cache.
* Fully qualified domain name with SSL. Note that the hosted zone must already be configured in Route 53.
  Opting out of this will mean relying on using the application load balancer's url over standard HTTP to access your Activepieces deployment.

For a full list of all the currently available configuration options, take a look at the [Activepieces Pulumi template file on GitHub](https://github.com/activepieces/activepieces/tree/main/deploy/pulumi/Pulumi.yaml).

## Setting up Pulumi for the first time

If you're new to Pulumi then read on to get your local dev environment setup to be able to deploy Activepieces.

### Prerequisites

1. Make sure you have [Node](https://nodejs.org/en/download) and [Pulumi](https://www.pulumi.com/docs/install/) installed.
2. [Install and configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
3. [Install and configure Pulumi](https://www.pulumi.com/docs/clouds/aws/get-started/begin/).
4. Create an S3 bucket which we'll use to maintain the state of all the various service we'll provision for our Activepieces deployment:

```bash  theme={null}
aws s3api create-bucket --bucket pulumi-state --region us-east-1
```

<Tip>
  Note: [Pulumi supports to two different state management approaches](https://www.pulumi.com/docs/concepts/state/#deciding-on-a-state-backend).
  If you'd rather use Pulumi Cloud instead of S3 then feel free to skip this step and setup an account with Pulumi.
</Tip>

5. Login to the Pulumi backend:

```bash  theme={null}
pulumi login s3://pulumi-state?region=us-east-1
```

6. Next we're going to use the Activepieces Pulumi deploy template to create a new project, a stack in that project and then kick off the deploy:

```bash  theme={null}
$ mkdir deploy-activepieces && cd deploy-activepieces 
$ pulumi new https://github.com/activepieces/activepieces/tree/main/deploy/pulumi
```

This step will prompt you to create you stack and to populate a series of config options, such as whether or not to provision a PostgreSQL RDS instance or use SQLite3.

<Tip>
  Note: When choosing a stack name, use something descriptive like `activepieces-dev`, `ap-prod` etc.
  This solution uses the stack name as a prefix for every AWS service created\
  e.g. your VPC will be named `<stack name>-vpc`.
</Tip>

7. Nothing left to do now but kick off the deploy:

```bash  theme={null}
pulumi up
```

8. Now choose `yes` when prompted. Once the deployment has finished, you should see a bunch of Pulumi output variables that look like the following:

```json  theme={null}
    _: {
        activePiecesUrl: "http://<alb name & id>.us-east-1.elb.amazonaws.com"
        activepiecesEnv: [
         . . . .
        ]
       }
```

The config value of interest here is the `activePiecesUrl` as that is the URL for our Activepieces deployment.
If you chose to add a fully qualified domain during your stack configuration, that will be displayed here.
Otherwise you'll see the URL to the application load balancer. And that's it.

Congratulations! You have successfully deployed Activepieces to AWS.

## Deploy a locally built Activepieces Docker image

To deploy a locally built image instead of using the official Docker Hub image, read on.

1. Clone the Activepieces repo locally:

```bash  theme={null}
git clone https://github.com/activepieces/activepieces
```

2. Move into the `deploy/pulumi` folder & install the necessary npm packages:

```bash  theme={null}
cd deploy/pulumi && npm i
```

3. This folder already has two Pulumi stack configuration files reday to go: `Pulumi.activepieces-dev.yaml` and `Pulumi.activepieces-prod.yaml`.
   These files already contain all the configurations we need to create our environments. Feel free to have a look & edit the values as you see fit.
   Lets continue by creating a development stack that uses the existing `Pulumi.activepieces-dev.yaml` file & kick off the deploy.

```bash  theme={null}
pulumi stack init activepieces-dev && pulumi up
```

<Tip>
  Note: Using `activepieces-dev` or `activepieces-prod` for the `pulumi stack init` command is required here as the stack name needs to match the existing stack file name in the folder.
</Tip>

4. You should now see a preview in the terminal of all the services that will be provisioned, before you continue.
   Once you choose `yes`, a new image will be built based on the `Dockerfile` in the root of the solution (make sure Docker Desktop is running) and then pushed up to a new ECR, along with provisioning all the other AWS services for the stack.

Congratulations! You have successfully deployed Activepieces into AWS using a locally built Docker image.

## Customising the deploy

All of the current configuration options, as well as the low-level details associated with the provisioned services are fully customisable, as you would expect from any IaC.
For example, if you'd like to have three availability zones instead of two for the VPC, use an older version of Redis or add some additional security group rules for PostgreSQL, you can update all of these and more in the `index.ts` file inside the `deploy` folder.

Or maybe you'd still like to deploy the official Activepieces Docker image instead of a local build, but would like to change some of the services. Simply set the `deployLocalBuild` config option in the stack file to `false` and make whatever changes you'd like to the `index.ts` file.

Checking out the [Pulumi docs](https://www.pulumi.com/docs/clouds/aws/) before doing so is highly encouraged.


# Docker
Source: https://www.activepieces.com/docs/install/options/docker

Single docker image deployment with SQLite3 and Memory Queue

<Warning>
  This setup is only meant for personal use or testing. It runs on SQLite3 and an in-memory Redis queue, which supports only a single instance on a single machine. For production or multi-instance setups, you must use Docker Compose with PostgreSQL and Redis.
</Warning>

To get up and running quickly with Activepieces, we will use the Activepieces Docker image. Follow these steps:

## Prerequisites

You need to have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker](https://docs.docker.com/get-docker/) installed on your machine in order to set up Activepieces via Docker Compose.

## Install

### Pull Image and Run Docker image

Pull the Activepieces Docker image and run the container with the following command:

```bash  theme={null}
docker run -d -p 8080:80 -v ~/.activepieces:/root/.activepieces -e AP_REDIS_TYPE=MEMORY -e AP_DB_TYPE=SQLITE3 -e AP_FRONTEND_URL="http://localhost:8080" activepieces/activepieces:latest
```

### Configure Webhook URL (Important for Triggers, Optional If you have public IP)

**Note:** By default, Activepieces will try to use your public IP for webhooks. If you are self-hosting on a personal machine, you must configure the frontend URL so that the webhook is accessible from the internet.

**Optional:** The easiest way to expose your webhook URL on localhost is by using a service like ngrok. However, it is not suitable for production use.

1. Install ngrok
2. Run the following command:

```bash  theme={null}
ngrok http 8080
```

3. Replace `AP_FRONTEND_URL` environment variable in the command line above.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=85cc8d40c4ad2ede8e8ad83fcb6e6b42" alt="Ngrok" data-og-width="961" width="961" data-og-height="509" height="509" data-path="resources/screenshots/docker-ngrok.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3c787f690f4700e8d2ac0115b86554e5 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ce675bfcc849cfe97d79fe6defdb69bc 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d5f1a1530820f43048b1d6110bb88d50 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0d917892d782b38aaabcd94d2d3b0c09 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ff5dfdbbed7b1b24ec65fe48e826ad20 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=09c2e4f0aacdcc60602ed8f3137e908d 2500w" />

## Upgrade

Please follow the steps below:

### Step 1: Back Up Your Data (Recommended)

Before proceeding with the upgrade, it is always a good practice to back up your Activepieces data to avoid any potential data loss during the update process.

1. **Stop the Current Activepieces Container:** If your Activepieces container is running, stop it using the following command:
   ```bash  theme={null}
   docker stop activepieces_container_name
   ```

2. **Backup Activepieces Data Directory:** By default, Activepieces data is stored in the `~/.activepieces` directory on your host machine. Create a backup of this directory to a safe location using the following command:
   ```bash  theme={null}
   cp -r ~/.activepieces ~/.activepieces_backup
   ```

### Step 2: Update the Docker Image

1. **Pull the Latest Activepieces Docker Image:** Run the following command to pull the latest Activepieces Docker image from Docker Hub:
   ```bash  theme={null}
   docker pull activepieces/activepieces:latest
   ```

### Step 3: Remove the Existing Activepieces Container

1. **Stop and Remove the Current Activepieces Container:** If your Activepieces container is running, stop and remove it using the following commands:
   ```bash  theme={null}
   docker stop activepieces_container_name
   docker rm activepieces_container_name
   ```

### Step 4: Run the Updated Activepieces Container

Now, run the updated Activepieces container with the latest image using the same command you used during the initial setup. Be sure to replace `activepieces_container_name` with the desired name for your new container.

```bash  theme={null}
docker run -d -p 8080:80 -v ~/.activepieces:/root/.activepieces -e AP_REDIS_TYPE=MEMORY -e AP_DB_TYPE=SQLITE3 -e AP_FRONTEND_URL="http://localhost:8080" --name activepieces_container_name activepieces/activepieces:latest
```

Congratulations! You have successfully upgraded your Activepieces Docker deployment


# Docker Compose
Source: https://www.activepieces.com/docs/install/options/docker-compose



To get up and running quickly with Activepieces, we will use the Activepieces Docker image. Follow these steps:

## Prerequisites

You need to have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker](https://docs.docker.com/get-docker/) installed on your machine in order to set up Activepieces via Docker Compose.

## Installing

**1. Clone Activepieces repository.**

Use the command line to clone Activepieces repository:

```bash  theme={null}
git clone https://github.com/activepieces/activepieces.git
```

**2. Go to the repository folder.**

```bash  theme={null}
cd activepieces
```

**3.Generate Environment variable**

Run the following command from the command prompt / terminal

```bash  theme={null}
sh tools/deploy.sh
```

<Tip>
  If none of the above methods work, you can rename the .env.example file in the root directory to .env and fill in the necessary information within the file.
</Tip>

**4. Run Activepieces.**

<Warning>
  Please note that "docker-compose" (with a dash) is an outdated version of Docker Compose and it will not work properly. We strongly recommend downloading and installing version 2 from the [here](https://docs.docker.com/compose/install/) to use Docker Compose.
</Warning>

```bash  theme={null}
docker compose -p activepieces up
```

## 4. Configure Webhook URL (Important for Triggers, Optional If you have public IP)

**Note:** By default, Activepieces will try to use your public IP for webhooks. If you are self-hosting on a personal machine, you must configure the frontend URL so that the webhook is accessible from the internet.

**Optional:** The easiest way to expose your webhook URL on localhost is by using a service like ngrok. However, it is not suitable for production use.

1. Install ngrok
2. Run the following command:

```bash  theme={null}
ngrok http 8080
```

3. Replace `AP_FRONTEND_URL` environment variable in `.env` with the ngrok url.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=85cc8d40c4ad2ede8e8ad83fcb6e6b42" alt="Ngrok" data-og-width="961" width="961" data-og-height="509" height="509" data-path="resources/screenshots/docker-ngrok.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3c787f690f4700e8d2ac0115b86554e5 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ce675bfcc849cfe97d79fe6defdb69bc 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d5f1a1530820f43048b1d6110bb88d50 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0d917892d782b38aaabcd94d2d3b0c09 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ff5dfdbbed7b1b24ec65fe48e826ad20 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/docker-ngrok.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=09c2e4f0aacdcc60602ed8f3137e908d 2500w" />

<Warning>
  When deploying for production, ensure that you update the database credentials and properly set the environment variables.

  Review the [configurations guide](/install/configuration/environment-variables) to make any necessary adjustments.
</Warning>

## Upgrading

To upgrade to new versions, which are installed using docker compose, perform the following steps. First, open a terminal in the activepieces repository directory and run the following commands.

### Automatic Pull

**1. Run the update script**

```bash  theme={null}
sh tools/update.sh
```

### Manually Pull

**1. Pull the new docker compose file**

```bash  theme={null}
git pull
```

**2. Pull the new images**

```bash  theme={null}
docker compose pull
```

**3. Review changelog for breaking changes**

<Warning>
  Please review breaking changes in the [changelog](../../about/breaking-changes).
</Warning>

**4. Run the updated docker images**

```
docker compose up -d --remove-orphans
```

Congratulations! You have now successfully updated the version.

## Deleting

The following command is capable of deleting all Docker containers and associated data, and therefore should be used with caution:

```
sh tools/reset.sh
```

<Warning>
  Executing this command will result in the removal of all Docker containers and the data stored within them. It is important to be aware of the potentially hazardous nature of this command before proceeding.
</Warning>


# Easypanel
Source: https://www.activepieces.com/docs/install/options/easypanel

Run Activepieces with Easypanel 1-Click Install

Easypanel is a modern server control panel. If you [run Easypanel](https://easypanel.io/docs) on your server, you can deploy Activepieces with 1 click on it.

<a target="_blank" rel="noopener" href="https://easypanel.io/docs/templates/activepieces">![Deploy to Easypanel](https://easypanel.io/img/deploy-on-easypanel-40.svg)</a>

## Instructions

1. Create a VM that runs Ubuntu on your cloud provider.
2. Install Easypanel using the instructions from the website.
3. Create a new project.
4. Install Activepieces using the dedicated template.


# Elestio
Source: https://www.activepieces.com/docs/install/options/elestio

Run Activepieces with Elestio 1-Click Install

You can deploy Activepieces on Elestio using one-click deployment. Elestio handles version updates, maintenance, security, backups, etc. So go ahead and click below to deploy and start using.

[![Deploy on Elestio](https://elest.io/images/logos/deploy-to-elestio-btn.png)](https://elest.io/open-source/activepieces)


# GCP
Source: https://www.activepieces.com/docs/install/options/gcp



This documentation is to deploy activepieces on VM Instance or VM Instance Group, we should first create VM template

## Create VM Template

First choose machine type (e.g e2-medium)

After configuring the VM Template, you can proceed to click on "Deploy Container" and specify the following container-specific settings:

* Image: activepieces/activepieces
* Run as a privileged container: true
* Environment Variables:
  * `AP_REDIS_TYPE`: MEMORY
  * `AP_DB_TYPE`: SQLITE3
  * `AP_FRONTEND_URL`: [http://localhost:80](http://localhost:80)
  * `AP_EXECUTION_MODE`: SANDBOX\_PROCESS
* Firewall: Allow HTTP traffic (for testing purposes only)

Once these details are entered, click on the "Deploy" button and patiently wait for the container deployment process to complete.\\

After a successful deployment, you can access the ActivePieces application by visiting the external IP address of the VM on GCP.

## Production Deployment

Please visit [ActivePieces](/install/configuration/environment-variables) for more details on how to customize the application.


# Helm
Source: https://www.activepieces.com/docs/install/options/helm

Deploy Activepieces on Kubernetes using Helm

This guide walks you through deploying Activepieces on Kubernetes using the official Helm chart.

## Prerequisites

* Kubernetes cluster (v1.19+)
* Helm 3.x installed
* kubectl configured to access your cluster

## Using External PostgreSQL and Redis

The Helm chart supports using external PostgreSQL and Redis services instead of deploying the Bitnami subcharts.

### Using External PostgreSQL

To use an external PostgreSQL instance:

```yaml  theme={null}
postgresql:
  enabled: false  # Disable Bitnami PostgreSQL subchart
  host: "your-postgres-host.example.com"
  port: 5432
  useSSL: true  # Enable SSL if required
  auth:
    database: "activepieces"
    username: "postgres"
    password: "your-password"
    # Or use external secret reference:
    # externalSecret:
    #   name: "postgresql-credentials"
    #   key: "password"
```

Alternatively, you can use a connection URL:

```yaml  theme={null}
postgresql:
  enabled: false
  url: "postgresql://user:password@host:5432/database?sslmode=require"
```

### Using External Redis

To use an external Redis instance:

```yaml  theme={null}
redis:
  enabled: false  # Disable Bitnami Redis subchart
  host: "your-redis-host.example.com"
  port: 6379
  useSSL: false  # Enable SSL if required
  auth:
    enabled: true
    password: "your-password"
    # Or use external secret reference:
    # externalSecret:
    #   name: "redis-credentials"
    #   key: "password"
```

Alternatively, you can use a connection URL:

```yaml  theme={null}
redis:
  enabled: false
  url: "redis://:password@host:6379/0"
```

### External Secret References

For better security, you can reference passwords from existing Kubernetes secrets (useful with External Secrets Operator or Sealed Secrets):

```yaml  theme={null}
postgresql:
  enabled: false
  host: "your-postgres-host.example.com"
  auth:
    externalSecret:
      name: "postgresql-credentials"
      key: "password"

redis:
  enabled: false
  host: "your-redis-host.example.com"
  auth:
    enabled: true
    externalSecret:
      name: "redis-credentials"
      key: "password"
```

## Quick Start

### 1. Clone the Repository

```bash  theme={null}
git clone https://github.com/activepieces/activepieces.git
cd activepieces
```

### 2. Install Dependencies

```bash  theme={null}
helm dependency update
```

### 3. Create a Values File

Create a `my-values.yaml` file with your configuration. You can use the [example values file](https://github.com/activepieces/activepieces/blob/main/deploy/activepieces-helm/values.yaml) as a reference.
The Helm chart has sensible defaults for required values while leaving the optional ones empty, but you should customize these core values for production

### 4. Install Activepieces

```bash  theme={null}
helm install activepieces deploy/activepieces-helm -f my-values.yaml
```

### 5. Verify Installation

```bash  theme={null}
# Check deployment status
kubectl get pods
kubectl get services

```

## Production Checklist

* [ ] Set `frontendUrl` to your actual domain
* [ ] Set strong passwords for PostgreSQL and Redis (or keep auto-generated)
* [ ] Configure proper ingress with TLS
* [ ] Set appropriate resource limits
* [ ] Configure persistent storage
* [ ] Choose appropriate [execution mode](/docs/install/architecture/workers) for your security requirements
* [ ] Review [environment variables](/docs/install/configuration/environment-variables) for advanced configuration
* [ ] Consider using a [separate workers](/docs/install/configuration/separate-workers) setup for better availability and security

## Upgrading

```bash  theme={null}
# Update dependencies
helm dependency update

# Upgrade release
helm upgrade activepieces deploy/activepieces-helm -f my-values.yaml

# Check upgrade status
kubectl rollout status deployment/activepieces
```

## Troubleshooting

### Common Issues

1. **Pod won't start**: Check logs with `kubectl logs deployment/activepieces`
2. **Database connection**: Verify PostgreSQL credentials and connectivity
3. **Frontend URL**: Ensure `frontendUrl` is accessible from external sources
4. **Webhooks not working**: Check ingress configuration and DNS resolution

### Useful Commands

```bash  theme={null}
# View logs
kubectl logs deployment/activepieces -f

# Port forward for testing
kubectl port-forward svc/activepieces 4200:80 --namespace default

# Get all resources
kubectl get all --namespace default
```

## Editions

Activepieces supports three editions:

* **`ce` (Community Edition)**: Open-source version with all core features (default)
* **`ee` (Enterprise Edition)**: Self-hosted edition with advanced features like SSO, RBAC, and audit logs
* **`cloud`**: For Activepieces Cloud deployments

Set the edition in your values file:

```yaml  theme={null}
activepieces:
  edition: "ce"  # or "ee" for Enterprise Edition
```

For Enterprise Edition features and licensing, visit [activepieces.com](https://www.activepieces.com/docs/admin-console/overview).

## Environment Variables

For a complete list of configuration options, see the [Environment Variables](/docs/install/configuration/environment-variables) documentation. Most environment variables can be configured through the Helm values file under the `activepieces` section.

## Execution Modes

Understanding execution modes is crucial for security and performance. See the [Workers & Sandboxing](/docs/install/architecture/workers) guide to choose the right mode for your deployment.

## Uninstalling

```bash  theme={null}
helm uninstall activepieces

# Clean up persistent volumes (optional)
kubectl delete pvc -l app.kubernetes.io/instance=activepieces
```


# Railway
Source: https://www.activepieces.com/docs/install/options/railway

Deploy Activepieces to the cloud in minutes using Railway's one-click template

Railway simplifies your infrastructure stack from servers to observability with a single, scalable, easy-to-use platform. With Railway's one-click deployment, you can get Activepieces up and running in minutes without managing servers, databases, or infrastructure.

<a href="https://railway.com/deploy/kGEO1J" target="_blank">
  <img alt="Deploy on Railway" src="https://railway.app/button.svg" />
</a>

## What Gets Deployed

The Railway template deploys Activepieces with the following components:

* **Activepieces Application**: The main Activepieces container running the latest version from [Docker Hub](https://hub.docker.com/r/activepieces/activepieces)
* **PostgreSQL Database**: Managed PostgreSQL database for storing flows, executions, and application data
* **Redis Cache**: Redis instance for job queuing and caching (optional, can use in-memory cache)
* **Automatic SSL**: Railway provides automatic HTTPS with SSL certificates
* **Custom Domain Support**: Configure your own domain through Railway's dashboard

## Prerequisites

Before deploying, ensure you have:

* A [Railway account](https://railway.app/) (free tier available)
* Basic understanding of environment variables (optional, for advanced configuration)

## Quick Start

1. **Click the deploy button** above to open Railway's deployment interface
2. **Configure environment variables for advanced usage** (see [Configuration](#configuration) below)
3. **Deploy** - Railway will automatically provision resources and start your instance

Once deployed, Railway will provide you with a public URL where your Activepieces instance is accessible.

## Configuration

### Environment Variables

Railway allows you to configure Activepieces through environment variables. You can set these in the Railway dashboard under your project's **Variables** tab.

#### Execution Mode

Configure the execution mode for security and performance:
See the [Workers & Sandboxing](/docs/install/architecture/workers) documentation for details on each mode.

#### Other Important Variables

* `AP_TELEMETRY_ENABLED`: Enable/disable telemetry (default: `false`)

For a complete list of all available environment variables, see the [Environment Variables](/docs/install/configuration/environment-variables) documentation.

## Custom Domain Setup

Railway supports custom domains with automatic SSL:

1. Go to your Railway project dashboard
2. Navigate to **Settings** → **Networking**
3. Add your custom domain
4. Update `AP_FRONTEND_URL` environment variable to match your custom domain
5. Railway will automatically provision SSL certificates

For more details on SSL configuration, see the [Setup SSL](/docs/install/configuration/setup-ssl) guide.

## Production Considerations

Before deploying to production, review these important points:

* [ ] Review [Security Practices](/docs/security/practices) documentation
* [ ] Configure `AP_WORKER_CONCURRENCY` based on your workload and hardware resources
* [ ] Ensure PostgreSQL backups are configured in Railway
* [ ] Consider database scaling options in Railway

## Observability

Railway provides built-in observability features for Activepieces. You can view logs and metrics in the Railway dashboard.

## Upgrading

To upgrade to a new version of Activepieces on Railway:

1. Go to your Railway project dashboard
2. Navigate to **Deployments**
3. Click **Redeploy** on the latest deployment
4. Railway will pull the latest Activepieces image and redeploy

<Warning>
  Before upgrading, review the [Breaking Changes](/docs/about/breaking-changes) documentation to ensure compatibility with your flows and configuration.
</Warning>

## Next Steps

After deploying Activepieces on Railway:

1. **Access your instance** using the Railway-provided URL
2. **Create your first flow** - see [Building Flows](/docs/flows/building-flows)
3. **Configure webhooks** - see [Setup App Webhooks](/docs/install/configuration/setup-app-webhooks)
4. **Explore pieces** - browse available integrations in the piece library

## Additional Resources

* [Troubleshooting](/docs/install/configuration/troubleshooting): Troubleshooting guide
* [Configuration Guide](/docs/install/configuration/overview): Comprehensive configuration documentation
* [Environment Variables](/docs/install/configuration/environment-variables): Complete list of configuration options
* [Architecture Overview](/docs/install/architecture/overview): Understand Activepieces architecture
* [Railway Documentation](https://docs.railway.app/): Official Railway platform documentation


# Overview
Source: https://www.activepieces.com/docs/install/overview

Introduction to the different ways to install Activepieces

Activepieces Community Edition can be deployed using **Docker**, **Docker Compose**, and **Kubernetes**.

<Tip>
  Community Edition is **free** and **open source**.

  You can read the difference between the editions [here](../about/editions).
</Tip>

## Recommended Options

<CardGroup cols={2}>
  <Card title="Docker (Fastest)" icon="docker" color="#248fe0" href="./options/docker">
    Deploy Activepieces as a single Docker container using the SQLite database.
  </Card>

  <Card title="Docker Compose" icon="layer-group" color="#00FFFF" href="./options/docker-compose">
    Deploy Activepieces with **Redis** and **PostgreSQL** setup.
  </Card>
</CardGroup>

## Other Options

<CardGroup cols={2}>
  <Card title="Helm" icon="ship" color="#ff9900" href="./options/helm">
    Install on Kubernetes with Helm.
  </Card>

  <Card
    title="Railway"
    icon={
  <img src="https://railway.com/brand/logo-light.png" alt="Railway" width="24" height="24" />
}
    href="./options/railway"
  >
    1-Click Install on Railway.
  </Card>

  <Card
    title="Easypanel"
    icon={
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 245 245">
        <g clip-path="url(#a)">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M242.291 110.378a15.002 15.002 0 0 0 0-15l-48.077-83.272a15.002 15.002 0 0 0-12.991-7.5H85.07a15 15 0 0 0-12.99 7.5L41.071 65.812a.015.015 0 0 0-.013.008L2.462 132.673a15 15 0 0 0 0 15l48.077 83.272a15 15 0 0 0 12.99 7.5h96.154a15.002 15.002 0 0 0 12.991-7.5l31.007-53.706c.005 0 .01-.003.013-.007l38.598-66.854Zm-38.611 66.861 3.265-5.655a15.002 15.002 0 0 0 0-15l-48.077-83.272a14.999 14.999 0 0 0-12.99-7.5H41.072l-3.265 5.656a15 15 0 0 0 0 15l48.077 83.271a15 15 0 0 0 12.99 7.5H203.68Z" fill="url(#b)" />
        </g>
        <defs>
          <linearGradient id="b" x1="188.72" y1="6.614" x2="56.032" y2="236.437" gradientUnits="userSpaceOnUse">
            <stop stop-color="#12CD87" />
            <stop offset="1" stop-color="#12ABCD" />
          </linearGradient>
          <clipPath id="a">
            <path fill="#fff" d="M0 0h245v245H0z" />
          </clipPath>
        </defs>
      </svg>
      }
    href="./options/easypanel"
  >
    1-Click Install with Easypanel template, maintained by the community.
  </Card>

  <Card title="Elestio" icon="cloud" color="#ff9900" href="./options/elestio">
    1-Click Install on Elestio.
  </Card>

  <Card title="AWS (Pulumi)" icon="aws" color="#ff9900" href="./options/aws">
    Install on AWS with Pulumi.
  </Card>

  <Card title="GCP" icon="cloud" color="#4385f5" href="./options/gcp">
    Install on GCP as a VM template.
  </Card>

  <Card
    title="PikaPods"
    icon={
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 402.2 402.2">
  <path d="M393 277c-3 7-8 9-15 9H66c-27 0-49-18-55-45a56 56 0 0 1 54-68c7 0 12-5 12-11s-5-11-12-11H22c-7 0-12-5-12-11 0-7 4-12 12-12h44c18 1 33 15 33 33 1 19-14 34-33 35-18 0-31 12-34 30-2 16 9 35 31 37h37c5-46 26-83 65-110 22-15 47-23 74-24l-4 16c-4 30 19 58 49 61l8 1c6-1 11-6 10-12 0-6-5-10-11-10-14-1-24-7-30-20-7-12-4-27 5-37s24-14 36-10c13 5 22 17 23 31l2 4c33 23 55 54 63 93l3 17v14m-57-59c0-6-5-11-11-11s-12 5-12 11 6 12 12 12c6-1 11-6 11-12" 
        fill="#4daf4e"/>
</svg>
}
    href="https://www.pikapods.com/pods?run=activepieces"
  >
    Instantly run on PikaPods from \$2.9/month.
  </Card>

  <Card title="RepoCloud" icon="cloud" href="https://repocloud.io/details/?app_id=177">
    Easily install on RepoCloud using this template, maintained by the community.
  </Card>

  <Card
    title="Zeabur"
    icon={
  <svg viewBox="0 0 294 229" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M113.865 144.888H293.087V229H0V144.888H82.388L195.822 84.112H0V0H293.087V84.112L113.865 144.888Z" fill="black"/>
    <path d="M194.847 0H0V84.112H194.847V0Z" fill="#6300FF"/>
    <path d="M293.065 144.888H114.772V229H293.065V144.888Z" fill="#FF4400"/>
  </svg>
}
    href="https://zeabur.com/templates/LNTQDF"
  >
    1-Click Install on Zeabur.
  </Card>
</CardGroup>

## Cloud Edition

<CardGroup cols={2}>
  <Card title="Activepieces Cloud" icon="cloud" color="##5155D7" href="https://cloud.activepieces.com/">
    This is the fastest option.
  </Card>
</CardGroup>


# Connection Deleted
Source: https://www.activepieces.com/docs/operations/audit-logs/connection-deleted





# Connection Upserted
Source: https://www.activepieces.com/docs/operations/audit-logs/connection-upserted





# Flow Created
Source: https://www.activepieces.com/docs/operations/audit-logs/flow-created





# Flow Deleted
Source: https://www.activepieces.com/docs/operations/audit-logs/flow-deleted





# Flow Run Finished
Source: https://www.activepieces.com/docs/operations/audit-logs/flow-run-finished





# Flow Run Started
Source: https://www.activepieces.com/docs/operations/audit-logs/flow-run-started





# Flow Updated
Source: https://www.activepieces.com/docs/operations/audit-logs/flow-updated





# Folder Created
Source: https://www.activepieces.com/docs/operations/audit-logs/folder-created





# Folder Deleted
Source: https://www.activepieces.com/docs/operations/audit-logs/folder-deleted





# Folder Updated
Source: https://www.activepieces.com/docs/operations/audit-logs/folder-updated





# Overview
Source: https://www.activepieces.com/docs/operations/audit-logs/overview



<Snippet file="enterprise-feature.mdx" />

This table in admin console contains all application events. We are constantly adding new events, so there is no better place to see the events defined in the code than [here](https://github.com/activepieces/activepieces/blob/main/packages/ee/shared/src/lib/audit-events/index.ts).

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/audit-logs.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=9742354a878008a7027bf6a93cd3544f" alt="Audit Logs" data-og-width="2640" width="2640" data-og-height="1440" height="1440" data-path="resources/screenshots/audit-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/audit-logs.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=69e1dec6e069dbca6b095afe10e533d0 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/audit-logs.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=5d03c631c71645dfcfbf4fc0a0e50866 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/audit-logs.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=2e4ee413867694fd57edc0105be670c9 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/audit-logs.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=554b247d1d8087bbc44bc38d6abc5601 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/audit-logs.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=d7916cfcf18f713dc6eebaa64837bac9 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/screenshots/audit-logs.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=ed699e8ec97c29317069229c1de7db03 2500w" />


# Signing Key Created
Source: https://www.activepieces.com/docs/operations/audit-logs/signing-key-created





# User Email Verified
Source: https://www.activepieces.com/docs/operations/audit-logs/user-email-verified





# User Password Reset
Source: https://www.activepieces.com/docs/operations/audit-logs/user-password-reset





# User Signed In
Source: https://www.activepieces.com/docs/operations/audit-logs/user-signed-in





# User Signed Up
Source: https://www.activepieces.com/docs/operations/audit-logs/user-signed-up





# Environments & Releases
Source: https://www.activepieces.com/docs/operations/git-sync



<Snippet file="enterprise-feature.mdx" />

The Project Releases feature allows for the creation of an **external backup**, **environments**, and maintaining a **version history** from the Git Repository or an existing project.

### How It Works

This example explains how to set up development and production environments using either Git repositories or existing projects as sources. The setup can be extended to include multiple environments, Git branches, or projects based on your needs.

### Requirements

You have to enable the project releases feature in the Settings -> Environments.

## Git-Sync

**Requirements**

* Empty Git Repository
* Two Projects in Activepieces: one for Development and one for Production

### 1. Push Flow to Repository

After making changes in the flow:

1. Click the 3-dot menu near the flow name
2. Select "Push to Git"
3. Add commit message and push

### 2. Deleting Flows

When you delete a flow from a project configured with Git sync (Release from Git), it will automatically delete the flow from the repository.

## Project-Sync

### 1. **Initialize Projects**

* Create a source project (e.g., Development)
* Create a target project (e.g., Production)

### 2. **Develop**

* Build and test your flows in the source project
* When ready, sync changes to the target project using releases

## Creating a Release

<Note>
  Credentials are not synced automatically. Create identical credentials with the same names in both environments manually.
</Note>

You can create a release in two ways:

1. **From Git Repository**:
   * Click "Create Release" and select "From Git"

2. **From Existing Project**:
   * Click "Create Release" and select "From Project"
   * Choose the source project to sync from

For both methods:

* Review the changes between environments
* Choose the operations you want to perform:
  * **Update Existing Flows**: Synchronize flows that exist in both environments
  * **Delete Missing Flows**: Remove flows that are no longer present in the source
  * **Create New Flows**: Add new flows found in the source
* Confirm to create the release

### Important Notes

* Enabled flows will be updated and republished (failed republishes become drafts)
* New flows start in a disabled state

### Approval Workflow (Optional)

To manage your approval workflow, you can use Git by creating two branches: development and production. Then, you can use standard pull requests as the approval step.

### GitHub action

This GitHub action can be used to automatically pull changes upon merging.

<Tip>
  Don't forget to replace `INSTANCE_URL` and `PROJECT_ID`, and add `ACTIVEPIECES_API_KEY` to the secrets.
</Tip>

```yml  theme={null}
name: Auto Deploy
on:
  workflow_dispatch:
  push:
    branches: [ "main" ]
jobs:
  run-pull:
    runs-on: ubuntu-latest
    steps:
      - name: deploy
        # Use GitHub secrets
        run: |
          curl --request POST \
            --url {INSTANCE_URL}/api/v1/git-repos/pull \
            --header 'Authorization: Bearer ${{ secrets.ACTIVEPIECES_API_KEY }}' \
            --header 'Content-Type: application/json' \
            --data '{
              "projectId": "{PROJECT_ID}"
            }'
```


# Project Permissions
Source: https://www.activepieces.com/docs/security/permissions

Documentation on project permissions in Activepieces

Activepieces utilizes Role-Based Access Control (RBAC) for managing permissions within projects. Each project consists of multiple flows and users, with each user assigned specific roles that define their actions within the project.

The supported roles in Activepieces are:

* **Admin:**
  * View Flows
  * Edit Flows
  * Publish/Turn On and Off Flows
  * View Runs
  * Retry Runs
  * View Issues
  * Resolve Issues
  * View Connections
  * Edit Connections
  * View Project Members
  * Add/Remove Project Members
  * Configure Git Repo to Sync Flows With
  * Push/Pull Flows to/from Git Repo

* **Editor:**
  * View Flows
  * Edit Flows
  * Publish/Turn On and Off Flows
  * View Runs
  * Retry Runs
  * View Connections
  * Edit Connections
  * View Issues
  * Resolve Issues
  * View Project Members

* **Operator:**
  * Publish/Turn On and Off Flows
  * View Runs
  * Retry Runs
  * View Issues
  * View Connections
  * Edit Connections
  * View Project Members

* **Viewer:**
  * View Flows
  * View Runs
  * View Connections
  * View Project Members
  * View Issues


# Security & Data Practices
Source: https://www.activepieces.com/docs/security/practices

We prioritize security and follow these practices to keep information safe.

## External Systems Credentials

**Storing Credentials**

All credentials are stored with 256-bit encryption keys, and there is no API to retrieve them for the user. They are sent only during processing, after which access is revoked from the engine.

**Data Masking**

We implement a robust data masking mechanism where third-party credentials or any sensitive information are systematically censored within the logs, guaranteeing that sensitive information is never stored or documented.

**OAuth2**

Integrations with third parties are always done using OAuth2, with a limited number of scopes when third-party support allows.

## Vulnerability Disclosure

Activepieces is an open-source project that welcomes contributors to test and report security issues.

For detailed information about our security policy, please refer to our GitHub Security Policy at: [https://github.com/activepieces/activepieces/security/policy](https://github.com/activepieces/activepieces/security/policy)

## Access and Authentication

**Role-Based Access Control (RBAC)**

To manage user access, we utilize Role-Based Access Control (RBAC). Team admins assign roles to users, granting them specific permissions to access and interact with projects, folders, and resources. RBAC allows for fine-grained control, enabling administrators to define and enforce access policies based on user roles.

**Single Sign-On (SSO)**

Implementing Single Sign-On (SSO) serves as a pivotal component of our security strategy. SSO streamlines user authentication by allowing them to access Activepieces with a single set of credentials. This not only enhances user convenience but also strengthens security by reducing the potential attack surface associated with managing multiple login credentials.

**Audit Logs**

We maintain comprehensive audit logs to track and monitor all access activities within Activepieces. This includes user interactions, system changes, and other relevant events. Our meticulous logging helps identify security threats and ensures transparency and accountability in our security measures.

**Password Policy Enforcement**

Users log in to Activepieces using a password known only to them. Activepieces enforces password length and complexity standards. Passwords are not stored; instead, only a secure hash of the password is stored in the database. For more information.

## Privacy & Data

**Supported Cloud Regions**

Presently, our cloud services are available in Germany as the supported data region.

We have plans to expand to additional regions in the near future.
If you opt for **self-hosting**, the available regions will depend on where you choose to host.

**Policy**

To better understand how we handle your data and prioritize your privacy, please take a moment to review our [Privacy Policy](https://www.activepieces.com/privacy). This document outlines in detail the measures we take to safeguard your information and the principles guiding our approach to privacy and data protection.


# Single Sign-On
Source: https://www.activepieces.com/docs/security/sso



<Snippet file="enterprise-feature.mdx" />

## Enforcing SSO

You can enforce SSO by specifying the domain. As part of the SSO configuration, you have the option to disable email and user login. This ensures that all authentication is routed through the designated SSO provider.

<img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=36f19b78f46392cf25a2dd8656d3d90f" alt="SSO" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=f4bd7b419d0fadb83d39982bb589e86c 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=65958659542c0230d5ca1891617dd2f6 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=03431f73ceb60577d149ecb8f7de8c83 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=a79b56ec6c0f486748f9c87b74ebf501 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=96f01414d4221451bcd4b5576f600cff 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/sso.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=55b6a93c69bfee31129c6bdea8235112 2500w" />

## Supported SSO Providers

You can enable various SSO providers, including Google and GitHub, to integrate with your system by configuring SSO.

### Google:

<Steps>
  <Step title="Go to the Developer Console" />

  <Step title="Create an OAuth2 App" />

  <Step title="Copy the Redirect URL from the Configure Screen into the Google App" />

  <Step title="Fill in the Client ID & Client Secret in Activepieces" />

  <Step title="Click Finish" />
</Steps>

### GitHub:

<Steps>
  <Step title="Go to the GitHub Developer Settings" />

  <Step title="Create a new OAuth App" />

  <Step title="Fill in the App details and click Register a new application" />

  <Step title="Use the following Redirect URL from the Configure Screen" />

  <Step title="Fill in the Homepage URL with the URL of your application" />

  <Step title="Click Register application" />

  <Step title="Copy the Client ID and Client Secret and fill them in Activepieces" />

  <Step title="Click Finish" />
</Steps>

### SAML with OKTA:

<Steps>
  <Step title="Go to the Okta Admin Portal and create a new app" />

  <Step title="Select SAML 2.0 as the Sign-on method" />

  <Step title="Fill in the App details and click Next" />

  <Step title="Use the following Single Sign-On URL from the Configure Screen" />

  <Step title="Fill in Audience URI (SP Entity ID) with 'Activepieces'" />

  <Step title="Add the following attributes (firstName, lastName, email)" />

  <Step title="Click Next and Finish" />

  <Step title="Go to the Sign On tab and click on View Setup Instructions" />

  <Step title="Copy the Identity Provider metadata and paste it in the Idp Metadata field" />

  <Step title="Copy the Signing Certificate and paste it in the Signing Key field" />

  <Step title="Click Save" />
</Steps>

### SAML with JumpCloud:

<Steps>
  <Step title="Go to the JumpCloud Admin Portal and create a new app" />

  <Step title="Create SAML App" />

  <Step title="Copy the ACS URL from Activepieces and paste it in the ACS urls">
        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d7f62e7318652bbe11537dda4ddca5f3" alt="JumpCloud ACS URL" data-og-width="608" width="608" data-og-height="263" height="263" data-path="resources/screenshots/jumpcloud/acl-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9a1191ab5bde4eb2eba360ba7af814db 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9344cf812f7a202a51981fbeac50544d 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=96f3c402c5d280d86b74a91082743c9a 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7015a842ce73840f1b7c07f482e8a438 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7aa35de4f66ff7864b7998affa7013eb 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/acl-url.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c7e3856dd592069ad300d0188b6d7624 2500w" />
  </Step>

  <Step title="Fill in Audience URI (SP Entity ID) with 'Activepieces'" />

  <Step title="Add the following attributes (firstName, lastName, email)">
        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0243c183611ae3ab374208725f7814ed" alt="JumpCloud User Attributes" data-og-width="599" width="599" data-og-height="368" height="368" data-path="resources/screenshots/jumpcloud/user-attribute.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9fb7f5b67fc82613aeff7d7c3f0ceede 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=674e1f8521feb2bcf4553e8f8feac308 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=32104d11cd660681c84af754dc9036fc 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b8894c36701e917f179bb9cb27a70173 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1555a1c74092ef42d822823a2d58411e 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-attribute.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7aed8876641785c56c8949a28cd275df 2500w" />
  </Step>

  <Step title="Include the HTTP-Redirect binding and export the metadata">
    JumpCloud does not provide the `HTTP-Redirect` binding by default. You need to tick this box.
    <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=891bb41c7e66420ab976016959bc2f22" alt="JumpCloud Redirect Binding" data-og-width="597" width="597" data-og-height="243" height="243" data-path="resources/screenshots/jumpcloud/declare-login.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d1148fa680d295d13064d86852d7d3cc 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=7b97005f2b0ab717d8cf0d2193c2d3e3 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=5614ad2fc17cf5b83dd35923b3043402 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9a23ecb850326cac6b7a1c716c460461 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=0bfa94531658cac50b0f2a4c0e75bd7f 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/declare-login.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=bdbadbe645d0a25aaaa3aa03ec1cb4e1 2500w" />

    Make sure you press `Save` and then Refresh the Page and Click on `Export Metadata`

        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3ba991481241c93ca5be2fe2d32174c1" alt="JumpCloud Export Metadata" data-og-width="618" width="618" data-og-height="250" height="250" data-path="resources/screenshots/jumpcloud/export-metadata.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=048119e60b4f613cb90f6c76e2d2d2f5 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b2ca2a0fc41bf696785958707a740076 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1e8182bab4cf800d1aedf46f43b63c2a 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=9bdec90ed3a27901439c9f280eaeddeb 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c22cc7cd4197a6775995482a761a4aeb 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/export-metadata.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=00915125e7b80014525eda44ead8cc56 2500w" />

    <Tip>
      Please Verify ` Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"` inside the xml.
    </Tip>

    After you export the metadata, paste it in the `Idp Metadata` field.
  </Step>

  <Step title="Copy the Certificate and paste it in the Signing Key field">
    Find the `<ds:X509Certificate>` element in the IDP metadata and copy its value. Paste it between these lines:

    ```
    -----BEGIN CERTIFICATE-----
    [PASTE THE VALUE FROM IDP METADATA]
    -----END CERTIFICATE-----
    ```
  </Step>

  <Step title="Make sure you Assigned the App to the User">
        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ec58a49538b08a0d97a72ab7a3dbdd66" alt="JumpCloud Assign App" data-og-width="939" width="939" data-og-height="526" height="526" data-path="resources/screenshots/jumpcloud/user-groups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=22b8ecba77376c52a043559ec8c5cbd3 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d9539e73d13f585eb444d72b14e638ae 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=dff266c6731286720c420d6cb047267c 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=ed455d0c87abd7e4f41c53b28367c62b 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3d9b6c62fa7ce2778a80504e6dad350e 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/jumpcloud/user-groups.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b22832eaec8cf2fbe46567a08c9c1f7f 2500w" />
  </Step>

  <Step title="Click Next and Finish" />
</Steps>


