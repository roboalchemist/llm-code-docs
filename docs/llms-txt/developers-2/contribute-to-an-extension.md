# Source: https://developers.raycast.com/basics/contribute-to-an-extension.md

# Contribute to an Extension

All published extensions are open-source and can be found in [this repository](https://github.com/raycast/extensions). This makes it easy for multiple developers to collaborate. This guide explains how to import an extension in order to fix a bug, add a new feature or otherwise contribute to it.

## Get source code

First, you need to find the source code of the extension. The easiest way to do this is to use the `Fork Extension` action in the Raycast's root search.

![Fork an extension](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-d8248b215be20ea329b284134cce26609fb91dde%2Ffork-extension.webp?alt=media)

## Develop the extension

After you have the source code locally, open the Terminal and navigate to the extension's folder. Once there, run `npm install && npm run dev` from the extension folder in your Terminal to start developing the extension.

![Open imported extension](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-d93798084581d66e02d4e51c48bb8c6edd66709d%2Fbasics-open-command.webp?alt=media) ![Icon list command](https://2922539984-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Me_8A39tFhZg3UaVoSN%2Fuploads%2Fgit-blob-64a3aa26124f0f72eab167839b9858c06e41e84b%2Fbasics-icon-list.webp?alt=media)

You should see your forked extension at the top of your root search and can open its commands.

When you're done editing the extension, make sure to add yourself to the contributors section of its [manifest](https://developers.raycast.com/information/manifest#extension-properties). If you used the `Fork Extension` action, this should have happened automatically.

Additionally, ensure the `CHANGELOG.md` file is updated with your changes; create it if it doesn't exist. Use the `{PR_MERGE_DATE}` placeholder for the date – see the [Version History documentation](https://developers.raycast.com/prepare-an-extension-for-store#version-history) for details.

Once everything is ready, see [how to publish an extension](https://developers.raycast.com/basics/publish-an-extension) for instructions on validating and publishing the changes.
