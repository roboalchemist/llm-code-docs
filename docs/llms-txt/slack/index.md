# Slack platform overview

[![Slack Developer Docs](https://docs.slack.dev/img/logos/slack-developers-white.png)](https://docs.slack.dev/)

## More doing, less reading

Hello there, fellow developer! 👋

Welcome to the Slack API documentation, the place where ideas turn into interactive apps, workflows get automated, and Slack becomes the platform that powers your workday. **With new tools for building AI agents and intelligent apps,** our documentation on APIs, SDKs, and tools can assist you in creating apps that make work life simpler, more pleasant and more productive.

**The Slack developer platform revolves around Slack apps.**

Which brings us to...

## What is a Slack app?

A Slack app is a tool or integration that extends the functionality of Slack: it adds new features, automates tasks, integrates with external services, or enhances the user experience. A Slack app allows you to do more within Slack than just chat. With the Slack platform, individual and enterprise developers alike can create apps that integrate directly with the tools teams already use, whether that's connecting a CRM, managing project boards, or sending automated alerts.

We know our platform is deep and wide, and possibly a little intimidating as a result. It's okay to not know where to start.

- **If you want to take it slow**, [this guide on designing your app](https://docs.slack.dev/surfaces/app-design) is a little light reading on how to define the look and feel of your app.
- **If you'd rather stop the chitchat and get into it**, build an app with the [Quickstart](https://docs.slack.dev/quickstart) guide. If you're just looking to get a token to call the Web API methods, completing the first three steps of [this guide](https://docs.slack.dev/app-management/quickstart-app-settings) will get you there.

✨ Our [sample apps and tutorials](https://docs.slack.dev/samples) are also particularly useful for those floating aimlessly, as they utilize our [Bolt framework and SDK](https://docs.slack.dev/tools). No matter what you try to do, we'll be right beside you.

### The path of app creation

There are three high-level steps to creating a Slack app:

1. **Create an app** using the [CLI](https://docs.slack.dev/tools/slack-cli/) or the [app settings](https://api.slack.com/apps) page. Then, decide which scopes your app needs and get tokens in return.
2. **Code the logic of your app**—which [APIs](https://docs.slack.dev/apis) your app will use, events it will respond to, which actions it will take, etc.—in the code editor of your choice. We recommend VS Code and using the [Bolt](https://docs.slack.dev/tools) framework (a Slack-created open source framework for JavaScript, Python, or Java) to make things easier.
3. **Deploy your app** locally to test it. Then, look into [distribution](https://docs.slack.dev/app-management/distribution) and [authentication](https://docs.slack.dev/authentication).

Along the way, you can decide to use different surfaces, methods, and blocks that make up the visual structure of your app.

### Go deeper

#### Build AI-Powered Apps & Agents

Integrate your app with your chosen Large Language Model (LLM) to build intelligent, autonomous **AI agents** and **AI-enabled apps** that take action for your users right in Slack.

- **[Learn about the AI features available for Slack apps](https://docs.slack.dev/ai)**
- **[Explore developing Slack apps with AI features](https://docs.slack.dev/ai/developing-ai-apps)**

Define where your app lives across the several available [Surfaces](https://docs.slack.dev/surfaces).

![Message Abstract](https://docs.slack.dev/assets/images/message-abstract-06be210d128e91ff97e3ca6d791ef7d9.png)

[Surfaces](https://docs.slack.dev/surfaces) encompass all the areas that a Slack app can touch: [messages](https://docs.slack.dev/messaging), [modals](https://docs.slack.dev/surfaces/modals), the [App Home](https://docs.slack.dev/surfaces/app-home), and [canvases](https://docs.slack.dev/surfaces/canvases). Messages, modals, and canvases are available for all types of Slack apps, while the App Home is available for Bolt apps.

![Block Kit](https://docs.slack.dev/assets/images/bk_landing_bkb-e64c290c97543b50e0b09c0b291c7c78.png)

[Block Kit](https://docs.slack.dev/block-kit) allows you to build beautiful surfaces with reusable components. Customize the order, appearance, and direct user interactivity with stackable, versatile blocks.

### Further customization

Make your app _yours_. Introduce personality and further custom functionality.

✨ [Build AI agents and context-aware apps](https://docs.slack.dev/ai): Integrate your LLM and take advantage of features like the split-view pane and text streaming, all outlined [here](https://docs.slack.dev/ai#ai-features).

✨ [Interactivity](https://docs.slack.dev/interactivity) covers the ways users can initiate interaction with Slack apps, including slash commands and shortcuts. Slash commands allow you to start your app from a simple keystroke and provide even wider functionality. Shortcuts are a simple and reliable way to save your app's location for ease of discovery by users.

---

## Tools of the trade

Slack provides several tools to aid you in your quest to creating Slack apps.

- ✨ The **[Slack CLI](https://docs.slack.dev/tools/slack-cli/)** is the recommended way to manage your app's entire lifecycle, from creation to installation and administration.
- ✨ **[Developer sandboxes](https://docs.slack.dev/tools/developer-sandboxes)** let you play around with platform features outside of a production environment.
- ✨ The **Bolt framework**, available for [Python](https://docs.slack.dev/tools/bolt-python/), [JavaScript](https://docs.slack.dev/tools/bolt-js/), and [Java](https://docs.slack.dev/tools/java-slack-sdk/guides/bolt-basics/), uses the **Slack SDKs** (available for [Python](https://docs.slack.dev/tools/python-slack-sdk/), [Node](https://docs.slack.dev/tools/node-slack-sdk/), and [Java](https://docs.slack.dev/tools/java-slack-sdk/)) under the hood to handle the fiddly bits of app development, including token rotation and navigating rate limiting. It is the fastest way to build a capable and secure app.
- ✨ Use the **[App settings](https://api.slack.com/apps)** to create apps for times when you don't need any code but want to enable access to the platform via tokens to use with the **[Web API](https://docs.slack.dev/apis/web-api)**.

---

## App vs. workflow

For the non-technically inclined, Slack offers a no-code tool to build workflows: [Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder). This tool is accessed via the Slack client. The Slack platform extends Workflow Builder by providing an avenue to write custom workflow steps. These steps are coded as a function in an app. Once deployed, they are available to use as a step in Workflow Builder.

Those custom workflow steps can be created in an app built with the Bolt framework, in any of Bolt's flavors ([Python](https://docs.slack.dev/tools/bolt-python/concepts/custom-steps), [JavaScript](https://docs.slack.dev/tools/bolt-js/concepts/custom-steps), and [Java](https://docs.slack.dev/tools/java-slack-sdk/guides/custom-steps)).

The Slack platform offers many options on the road to creating custom Slack apps and workflows. While there is power in those possibilities, it can be daunting to recognize which pieces of the platform apply where. We encourage you to read through a detailed comparison of the options [here](https://docs.slack.dev/workflows/comparing-workflows-apps).

---

## How to use these docs

This documentation is broken down into four categories:

- **Guides**: These are more lengthy explanations of a concept within a Slack app, i.e. how to build out a feature, how to implement OAuth, what a surface is, etc. You are here.
- **Reference**: Have you landed here looking for reference documentation? We admire a straight-shooter. Direct your attention to the [Reference](https://docs.slack.dev/reference) section for referential material on API methods, scopes, events, Block Kit payloads, etc.
- **Samples**: Our collection of [sample apps and accompanying tutorials](https://docs.slack.dev/samples).
- **Tools**: The library of available [tools](https://docs.slack.dev/tools) you can use to build a Slack app. Psst...check out Bolt.

---

## What's next?

Each developer's needs differ. Maybe you want to explore how to [distribute your app](https://docs.slack.dev/app-management/distribution) or even have it listed on the [Slack Marketplace](https://www.slack.com/marketplace). Perhaps you're interested in managing apps [as an admin](https://docs.slack.dev/admins). Better yet, explore the [tools](https://docs.slack.dev/tools) that make the job of app building easier.

Keep the end-goal in sight like a guiding horizon: a user wants to accomplish something with your app. The rest is getting there as productively and pleasantly as possible. Ready?

[Get Started](https://docs.slack.dev/quickstart)