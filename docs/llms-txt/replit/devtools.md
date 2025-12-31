# Source: https://docs.replit.com/extensions/development/devtools.md

# Extension Devtools

> Learn how to use Replit's Extension Devtools to manage metadata, file handlers, and tools while developing your extension.

# Developing your Extension

In every extension Replit App, you will see a button labeled **Extension Devtools** in the top-right corner of the workspace.

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools-button.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=855c3350d7873e06bd3e71cf8001adb1" alt="Devtools button" data-og-width="686" width="686" data-og-height="229" height="229" data-path="images/extensions/devtools-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools-button.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=536ebeda853a33f6709800a92b458b78 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools-button.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=cf7d95dcaf61ade86482588e2a1e269b 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools-button.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=40e9d8392f7e24cdc369c05c8597c5a4 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools-button.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=86d750664e2e248a2b3d6c6a05c2d250 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools-button.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f1655901bb84964fd37d89aeefe0bfc5 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools-button.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f7021b5f68f0fb6230892c7ea4d5aec4 2500w" />
</Frame>

If you do not see this button, make sure your Replit App is [configured to be an Extension](/replit-app/configuration/).

## Developer Tools

The Extension Devtools pane makes it easy to edit your Extension's metadata and manage [Tools](/extensions/basics/key-concepts#tool-extension-ui) and [File Handlers](/extensions/basics/key-concepts#file-handler-file-editors-and-icons).

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=a3cb90eae7b4e2ca6791209f3ec44d62" alt="Devtools" data-og-width="545" width="545" data-og-height="415" height="415" data-path="images/extensions/devtools.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=689cc845598422233336336c676b705d 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=99eda6cccdb7f136ba1fbb80aae9e2c2 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=5e48d6f9863be3d44b82b498ab0d6009 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=68c41777cbed0653c8160d518f3ad61b 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=bfa7f7a96a91ef8ebc9a2d95cdc70ba4 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/devtools.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6db69bf4b984d6b036dfe3783083b2af 2500w" />
</Frame>

### Extension Metadata

Click the **Edit** button in the top-right corner of your Extension preview to edit it. See [docs on the manifest file](/extensions/api/manifest).

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/preview-card.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=0d546c19f186add92f3fbf7e03f9fa86" alt="Extension preview" data-og-width="532" width="532" data-og-height="79" height="79" data-path="images/extensions/preview-card.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/preview-card.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=458499a5c9e3f56bee3d447a3008c8b6 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/preview-card.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d4080215adad00f8a3d0f602fdda5d33 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/preview-card.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=1dcc19f94a81c6a75b6b37866805081b 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/preview-card.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=20bea19ca32492723b2d3840a99509a0 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/preview-card.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6fc4ff2d10d4b19a46ecdc28ee2131dc 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/preview-card.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=de24b5482e05379ad4407014b9ebd0a2 2500w" />
</Frame>

### File Handlers

Click the "+" Icon next to **File Handlers** or click **New File Handler**. You will then be prompted to fill out the necessary information for the file handler. See [Type Definition](/extensions/api/manifest#filehandler).

To preview a file handler in action, click the **Open** button on the right side of an existing file handler.

### Tools

Click the "+" Icon next to **Tools** or click **New Tool**. You will then be prompted to fill out the necessary information for the new tool. See [Type Definition](/extensions/api/manifest#tool).

To preview a tool in action, click the **Open** button on the right side of an existing tool.
