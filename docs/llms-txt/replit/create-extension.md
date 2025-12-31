# Source: https://docs.replit.com/extensions/basics/create-extension.md

# Create your first Replit Extension

> Learn how to build a basic Replit extension by creating, previewing, and adding features to a sample project using Extension Devtools and the Extensions API.

#### Learn the basics of extension development by building and previewing a simple extension.

In this guide, you'll build a sample "Hello, world!" React.js extension with a custom Tool UI.

## Before you begin

* Make sure you have a Replit account — you'll need to be logged in to create an extension.
* You'll also need to make sure you've verified your email address, as this is required to publish an extension.
* You'll need to be familiar with JavaScript, and ideally React.js, which is our preferred framework for building UI Extensions.

## Create an Extension Replit App

To start building a Replit extension, you need to create an Extension Replit App. This is a special Replit App that contains all the configuration necessary to build, preview, and release your extension.

1. Fork a template below. Give it a name and click "Create Extension Replit App"

<CardGroup cols={2}>
  <Card title="React Extension" icon="react" iconType="solid" href="https://replit.com/new/extension?template=656d6107-3a39-4802-b8d9-59479cc5e358" horizontal={true}>
    A starter template for Replit Extensions using the React JavaScript
    framework.
  </Card>

  <Card title="JavaScript Extension" icon="js" iconType="solid" href="https://replit.com/new/extension?template=44dadedd-8045-46a9-ad28-2b86699a861" horizontal={true}>
    A starter template for a Replit Extension with Vanilla JavaScript
  </Card>
</CardGroup>

2. After creating the Replit App, your Workspace should open. On the left side you'll find a code editor, and on the right side, you'll find the Extension Devtools tab. [Learn more about devtools](/extensions/development/devtools)

### Preview your extension

Building an extension is a lot easier when you can see what you're building. We've made it easy to preview your extension in a Replit App, similar to the Preview tool you're familiar with in other Replit Apps.

<Note>
  Extension Replit Apps do not support the regular Preview tool. Read more in
  the [FAQ](/extensions/faq)
</Note>

1. **Open Extension Devtools**
2. **Click "Load Locally"** This will run your Replit App's development server, if it's not already running, and load your extension in the preview window.
3. **Open a development preview tab** Click the "Preview" button next to any Tool or File Handler in the Extension Devtools to open a preview tab. This will open a new tab in your Workspace, where you can see your extension in action.

### Add features

Next, it's time to start adding features using the Replit Extensions API.

There are two ways to use the APIs, depending on which template you chose:

* **React Extensions** In React Extensions, some APIs have hooks, while others are available on the `replit` object returned by [`useReplit()`](/extensions/development/react/hooks/useReplit).
* **JavaScript Extensions** In JavaScript Extensions, all APIs are available on the global `replit` object created by the [`init` API](/extensions/api/init)

Features are added through the Devtools UI, which is available in the [Extension Devtools](/extensions/development/devtools) tab. Features are divided into three categories:

1. **Tools (*UI Extensions*)** An custom user interface presented as a Tab in the workspace. Examples include a ReplDB editor or a Chat Extension. Learn how to [build your first tool](/extensions/examples/snippet-manager).
2. **File Handlers (*File Editors and Icons*)** File handlers allow you to build Tools and add icons for specific file types. Examples include a JSON file editor or a CSV file editor. Learn how to [build your first file handler](/extensions/examples/json-editor). Under the hood, file handlers are just tools with a filetype association.

### Using devtools to scaffold features

Extension developer tools make it easy to scaffold out new functionality without manually editing the Manifest file. (*Behind the scenes, all the edits you make here are reflected in the Manifest file.*)
