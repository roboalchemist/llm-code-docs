# Source: https://docs.zapier.com/platform/publish/public-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build your first public integration on Zapier

> This guide gives an overview of the process to publishing a public integration.

## Benefits to building a public integration

* Building a public integration on the Zapier Platform is free.
* There are no fees for publishing an integration.
* Users of your integration are responsible for their own Zapier plans and billing.
* Partners do not incur fees as a result of the usage of their integration.
* You'll get support from [Zapier's Partner Program](/platform/publish/partner-program) once your app has been successfully reviewed.

To see how your integration will show up on Zapier's website, you can browse the [app directory](https://zapier.com/apps). It's a great idea to explore similar apps to see what triggers and actions they provide for building Zapier workflows, called Zaps.

## 1. Before you start

Consider workflows your app will support, and what types of activities your users want to automate. Learn [how Zapier works](/platform/quickstart/how-zapier-works) and set up a few Zaps to get a sense of the user experience.

To design useful triggers and actions for your integration, consider how your users might need data from your app to run other parts of their business. Some of the most popular use cases for Zapier integrations include:

* Sending follow-up emails or messages
* Copying data from a bill or invoice into another system
* Updating contact records in multiple databases
* Creating or updating records in a project management tool

Learn more about [recommended integration features](/platform/quickstart/must-have-triggers-and-actions) by app category and how to design [popular app type integrations](/platform/quickstart/must-have-triggers-and-actions).

## 2. Build your integration

Building a Zapier integration means identifying the relevant APIs for your triggers and actions, and designing an intuitive experience for your users to select and map the data they need.

There are two ways to build an integration on Zapier's Platform:

* The Platform UI lets you create a Zapier integration in your browser without code using API endpoint URLs. You can set any custom options your API may need, including custom URL params, HTTP headers, and request body items.
* Zapier Platform CLI lets you build a Zapier integration in your local development environment, collaborate with version control and CI tools, and push new versions of your integration from the command line.

Both of these tools run on the same Zapier platform, so choose the one that fits your workflow the best.

Learn more about the difference between building with the [Platform UI and the CLI](/platform/quickstart/ui-vs-cli).

## 3. Test your integration

While you're building your integration, you can test your API requests within the Integration Builder. For developers building on Zapier Platform CLI, you can write unit tests that run locally, in a CI tool like [Travis](https://travis-ci.com/).

To get a sense of the user experience, it's recommended to test your integration within the Zap editor. [Create a new Zap](https://help.zapier.com/hc/en-us/articles/8496309697421) that uses your integration's triggers or actions to ensure they all work as expected. After you're done building, invite users to try your integration before making it available to a wider audience.

Learn more about testing your integration:

* [Testing using Zapier Platform UI](/platform/build/test-auth)
* [Testing using Zapier Platform CLI](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#testing)

## 4. Submit your integration for app review

After you've confirmed your integration is working as expected, you're almost ready to publish your app. To publish your integration, you need to submit your app for review by Zapier.

Before submitting your integration, review [Zapier's integration publishing requirements](/platform/publish/integration-publishing-requirements) or ask the [PublishBot](https://publishbot.zapier.app/) for a smoother app review process.

To submit your integration for app review:

1. [Log into the Platform UI](https://zapier.com/app/developer)
2. Select your **integration**.
3. In *Integration Home*, click **Publish.**
4. You'll need to complete the online form.
5. Click **Submit for Review**.

After you've submitted your integration for review, one of our developers will reach out to you in 1 week or less with any oustanding requirements. In the meantime, Zapier will update your:

* App version to **Pending**.
* App status will remain as **Private**.

## 5. Beta phase

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/wQj_022fa_mZMaTw/images/launch_process.webp?fit=max&auto=format&n=wQj_022fa_mZMaTw&q=85&s=bdb6578016449a7ff40cdf93a1574b96" data-og-width="3032" width="3032" data-og-height="1928" height="1928" data-path="images/launch_process.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/wQj_022fa_mZMaTw/images/launch_process.webp?w=280&fit=max&auto=format&n=wQj_022fa_mZMaTw&q=85&s=2d61e89bcce0756d33d25153185bed5f 280w, https://mintcdn.com/zapier-82f0e938/wQj_022fa_mZMaTw/images/launch_process.webp?w=560&fit=max&auto=format&n=wQj_022fa_mZMaTw&q=85&s=a2a9c6ff766c5234069ebb85f68f0fbb 560w, https://mintcdn.com/zapier-82f0e938/wQj_022fa_mZMaTw/images/launch_process.webp?w=840&fit=max&auto=format&n=wQj_022fa_mZMaTw&q=85&s=e07267750322206efb7a3ec7a5781697 840w, https://mintcdn.com/zapier-82f0e938/wQj_022fa_mZMaTw/images/launch_process.webp?w=1100&fit=max&auto=format&n=wQj_022fa_mZMaTw&q=85&s=a95e0e070d57f3d8276ecf67fd2c10df 1100w, https://mintcdn.com/zapier-82f0e938/wQj_022fa_mZMaTw/images/launch_process.webp?w=1650&fit=max&auto=format&n=wQj_022fa_mZMaTw&q=85&s=07f8419f995b811e9e30e0b7cdfd96c8 1650w, https://mintcdn.com/zapier-82f0e938/wQj_022fa_mZMaTw/images/launch_process.webp?w=2500&fit=max&auto=format&n=wQj_022fa_mZMaTw&q=85&s=47e42c7a82aada80a64ff8d657a6c1fd 2500w" />
</Frame>

When your integration is approved, Zapier will update your:

* App status to **Beta**.
* Integration will be added to [Zapier's app directory](https://zapier.com/apps) with a Beta tag.

Your integration will remain in beta for 90 days. Whilst in public beta, we recommend completing these tasks to improve your integration:

### Publish a support article in your help center

Publishing help documentation for your Zapier integration on your own website is an effective way to support
users and reduce friction in adoption. When users can easily find clear, step-by-step guides, they're more likely
to successfully set up and maintain their automations without needing to contact support, improving the user experience.
Consider [embedding Zap templates](https://docs.zapier.com/powered-by-zapier/integration-marketplace/low-code/zap-templates), troubleshooting tips for common API responses, and visual guides to aid users.

[Learn more about writing help documentation](https://docs.zapier.com/platform/publish/user-help)

### Create Zap templates

As soon as your app is published and in beta you can begin creating and sharing [Zap Templates](/platform/publish/zap-templates). Zap Templates are readymade integrations or Zaps with the apps and core fields pre-selected. In a few clicks, they help people discover a use case, connect apps, and turn on the Zap.

Learn more about creating [Zap templates](/platform/publish/zap-templates).

### Embed Zapier in your product or website

The best way to ensure users are able to discover your Zapier integration is to surface your integration where users are looking at it. By embedding Zapier in your product, you can create end-to-end user experience, helping your customers discover available integrations within your product without having to leave your app.

Learn more about [embedding Zapier](https://platform.zapier.com/embed/embed-benefits).

### Grow active usage

During the beta stage of your integration, it's important to actively work on growing the usage of your app. By encouraging more people to use your integration, you'll be able to gather valuable insights and feedback early on, which will help you optimize it further.

Learn more strategy [tips for a successful integration](/platform/publish/partner-faq).

### Manage bugs and feature requests

With the Zapier Issue Manager, you have the ability to conveniently address bugs and new feature requests within your preferred issue-tracking tool. Regularly reviewing and taking action on these items will greatly contribute to enhancing the overall health score of your integration.

Learn more about [Zapier Issue Manager](/platform/manage/user-feedback).

### Exit Beta early by embedding your integration

When one signup for Zapier is detected from your implementation of a [Zapier embed tool](https://platform.zapier.com/embed/embed-benefits), you'll exit Beta the next business day and unlock Partner Program benefits. The simplest option is to feature your Zap templates in a launch announcement. Additionally, you can present a dynamic gallery of the 6,000+ applications that are now compatible with your app for creating workflows.

## 6. Public phase

After 90 days in public beta, your integration will become public:

* Your app status will be updated to public, and the beta tag will be removed.
* You're added to our [Partner Program](https://zapier.com/developer-platform/partner-program), where you can earn marketing and support benefits.

Learn more about [maintaining your Zapier integration](/platform/manage/user-feedback).

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
