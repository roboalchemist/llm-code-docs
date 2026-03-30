# Source: https://firebase.google.com/docs/studio/import-workspace.md.txt

# Create a button to import code to Firebase Studio

{ # disableFinding("simple") #}

Add an "Open in Firebase Studio" button to your website to provide a
seamless way for users to import code from your site directly into a
Firebase Studio workspace, letting them
continue working in an agentic cloud-based development environment.

This feature is designed for:

- Code playgrounds, where your users can move from a basic
  editor to a complete development environment.

- App prototyping tools, where your site generates the code and the visual
  prototype, and the user then iterates on it in Firebase Studio.

## Use the Open in Firebase Studio SDK

The "Open in Firebase Studio" button is powered by the
[Open in Firebase Studio
SDK](https://www.npmjs.com/package/@firebase-studio/open-sdk/),
a JavaScript library that generates the
appropriate links to create and populate a new workspace. It provides several
options for how the code is imported.

### Import methods

You can configure the button to import code using the following methods:

- **From a Git repository or template** : Link to a Git repository or
  Firebase Studio template. This is great for complete projects or
  predefined templates. For more information about these use-cases, refer to
  [Create a shortcut to a predefined workspace in
  Firebase Studio](https://firebase.google.com/docs/studio/open-in-firebase-studio).

- **From a set of project files**: Dynamically create a workspace from a set of
  files and code snippets directly from your web application. This is the most
  powerful option for code playgrounds and app prototypers, as it exports the
  user's current work, even if it's not saved elsewhere.

### Add the "Open in Firebase Studio" button to your site

[The Open in Firebase Studio SDK](https://www.npmjs.com/package/@firebase-studio/open-sdk):
provides everything you need, including helper functions to
generate button images, create deep links, and send file content to create
Firebase Studio workspaces.

To add the "Open in Firebase Studio" button to your website:

1. Install the package in your project directory:

       npm install @firebase-studio/open-sdk

2. Add the following to your code to import the library:

       import * as FirebaseStudio from '@firebase-studio/open-sdk';

For detailed instructions, code examples, and the full API reference, refer to
the [official SDK documentation](https://www.npmjs.com/package/@firebase-studio/open-sdk/).

## Understand workspace environments

When a user creates a workspace from your site, Firebase Studio sets
up the development environment for them. The level of automation depends on the
type of project.

### Optimized environment

For React, Angular, and simple HTML projects, Firebase Studio provides an
optimized, pre-configured environment, provided the caller correctly sets the
`baselineEnvironment` property within the `settings` object. This means that
when a user opens the link in
Firebase Studio, Firebase Studio creates the workspace and
automatically:

- Installs all necessary dependencies.
- Configures and starts the correct development server.
- Sets up the environment with the correct tooling and extensions.

This opens an environment where your users can see open a live preview of
your application and interact directly with the code.

### Generic environment

For all other project types, Firebase Studio uses a generic importer. It
uploads the files into the workspace, but your user must
perform the initial setup manually. They might need to:

- Install language runtimes and dependencies.
- Configure the [`dev.nix`](https://firebase.google.com/docs/studio/customize-workspace#nix+fs) file.

For these projects, Firebase Studio creates a non-customized environment,
giving the user full control over the setup process.

### User experience

For both types of workspaces, after a user clicks the "Open in
Firebase Studio" button, they're prompted to name their workspace and review
the list of files to import.

![Open in Firebase Studio Import Workspace dialog](https://firebase.google.com/static/docs/studio/images/import_bundle.png)

When the user clicks
**Import** , a new Firebase Studio workspace opens. It contains your
project files, an app preview, and a README file with next steps.

## Design an "Open in Firebase Studio" button

You can design your button using the [Open in Firebase Studio
SDK](https://www.npmjs.com/package/@firebase-studio/open-sdk) or
use the following tool to generate the HTML for a Firebase Studio button:
<iframe allow="clipboard-write" width="100%" height="600" src="https://fire-studio-tools.web.app/button-generator"></iframe>

If you use the SDK, you can include optional configuration properties
for the button:

- `label`: Sets the text label shown on the button.
  - Allowed values: `open`, `try`, `export`, or `continue`.
- `color`: Defines the button's color scheme.
  - Allowed values: `dark`, `light`, `blue`, or `bright`.
- `size`: Specifies the button's height in pixels.
  - Allowed values: `20` or `32`.
- `imageFormat`: Determines the file format of the generated image.
  - Allowed values: `svg` or `png`.

For example:

    img.src = FirebaseStudio.getButtonImageUrl({
      label: 'export',
      color: 'dark',
      size: 32,
      imageFormat: 'svg'
    });

![Example of an Export to Firebase Studio button](https://cdn.firebasestudio.dev/btn/export_dark_32.svg)

## Next steps

- [Install the Open in Firebase Studio SDK](https://www.npmjs.com/package/@firebase-studio/open-sdk/)
- [Understand how to customize a Firebase Studio workspace](https://firebase.google.com/docs/studio/customize-workspace)