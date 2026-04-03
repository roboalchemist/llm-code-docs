# Source: https://firebase.google.com/docs/studio/open-in-firebase-studio.md.txt

WithFirebase Studio, you can simplify the steps for someone new to your codebase to set up their development environment and get productive by adding an "Open in Firebase Studio" button.

For example:

- If you're**working on a team with other contributors** , you can[customize your environment](https://firebase.google.com/docs/studio/customize-workspace)precisely for your project and then commit your`.idx/dev.nix`file to your project's Git repository. That way, when a teammate imports your Git repository inFirebase Studio, their new workspace will have the exact same configuration as yours, complete with the same system packages, IDE extensions, starter scripts, and more.

- If you're**building a framework or library** for others to use, you can include a`.idx/dev.nix`file in your sample code repositories, so that when a user imports your samples intoFirebase Studio, they can skip the environment setup and jump straight into trying out your framework. You can even[build your own, custom template](https://firebase.google.com/docs/studio/custom-templates)as an opinionated, customizable starting point for your users.

After you're happy with your environment customizations, you can make it even easier for others to import your project intoFirebase Studioby adding an "Open inFirebase Studio" button to your documentation, such as your project's`README.md`file.

## Common "Open inFirebase Studio" entry points

There are several URL patterns available for an "Open inFirebase Studio" button:

- To link to the**import a Git repository**flow, prefilled with your Git repository URL, use this URL pattern:

      https://studio.firebase.google.com/import?url=https://github.com/my-org/my-repo

  At this time, only GitHub repositories are supported (both private and public).
- To link to a**predefined workspace template** , find the template you're looking for in the[Templates](https://studio.firebase.google.com/templates)page inFirebase Studio, and copy its URL, which should follow this URL pattern:

      https://studio.firebase.google.com/new/gemini

- To link to a**custom template**, prefilled with your template's GitHub URL, use this URL pattern:

      https://studio.firebase.google.com/new?template=https://github.com/my-org/my-template

- To open theApp Prototyping agentwith a pre-filled prompt, use this URL pattern:

      https://studio.firebase.google.com/?prototypePrompt=Create an app that transforms sketches into a high-quality photograph with Gemini

## Add an "Open inFirebase Studio" button

Install the[Open inFirebase StudioSDK](https://www.npmjs.com/package/@firebase-studio/open-sdk)or use this tool to generate the HTML for aFirebase Studiobutton: