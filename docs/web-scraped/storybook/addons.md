# Storybook Documentation
# Source: https://storybook.js.org/docs/addons
# Page: /docs/addons

# Introduction to addons

Addons extend Storybook with features and integrations that are not built into the core. Most Storybook features are implemented as addons. For instance: [documentation](./writing-docs), [accessibility testing](./writing-tests/accessibility-testing), [interactive controls](./essentials/controls), among others. The [addon API](./addons/addons-api) makes it easy for you to configure and customize Storybook in new ways. There are countless addons made by the community that unlocks time-saving workflows.

Browse our [addon catalog](https://storybook.js.org/addons) to install an existing addon or as inspiration for your own addon.

## 

Storybook basics

Before writing your first [addon](https://storybook.js.org/addons), let’s take a look at the basics of Storybook’s architecture. While Storybook presents a unified user interface, under the hood it’s divided down the middle into **Manager** and **Preview**.

The **Manager** is the UI responsible for rendering the:

  * 🔍 Search
  * 🧭 Navigation
  * 🔗 Toolbars
  * 📦 Addons



The **Preview** area is an `iframe` where your stories are rendered.

![Storybook detailed window](/docs-assets/10.1/addons/manager-preview.png)

Because both elements run in their own separate `iframes`, they use a communication channel to keep in sync. For example, when you select a story in the Manager an event is dispatched across the channel notifying the Preview to render the story.

## 

Anatomy of an addon

Storybook addons allow you to extend what's already possible with Storybook, everything from the [user interface](./addons/addon-types) to the [API](./addons/addons-api). Each one is classified into two broader categories.

### 

UI-based addons

[UI-based addons](./addons/addon-types#ui-based-addons) focus on customizing Storybook's user interface to extend your development workflow. Examples of UI-based addons include: [Controls](./essentials/controls), [Docs](./writing-docs) and [Accessibility](./writing-tests/accessibility-testing).

[Learn how to write an addon »](./addons/writing-addons)

### 

Preset addons

[Preset addons](./addons/addon-types#preset-addons) help you integrate Storybook with other technologies and libraries. An examples of a preset addons is [preset-create-react-app](https://github.com/storybookjs/presets/tree/master/packages/preset-create-react-app).

[Learn how to write a preset addon »](./addons/writing-presets)

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/addons/index.mdx)