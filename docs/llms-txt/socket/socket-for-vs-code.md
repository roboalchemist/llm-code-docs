# Source: https://docs.socket.dev/docs/socket-for-vs-code.md

# Guide to Socket for VS Code

The Socket VS Code Extension is available in the [VS Code extension marketplace](https://marketplace.visualstudio.com/items?itemName=SocketSecurity.vscode-socket-security) and [OpenVSX registry](https://open-vsx.org/extension/SocketSecurity/vscode-socket-security).

<br />

<Image align="center" border={false} src="https://files.readme.io/c4a55b3b28444234a2745da0c6ed61b7827c1a0ad4cf4fa065a8b266bef6df20-CleanShot_2024-08-23_at_17.12.512x.png" />

# Settings

The extension comes with various settings that can be configured by looking in your [editor preferences](https://code.visualstudio.com/docs/getstarted/settings) under the "Extensions" tab "Socket Security" section.

These settings can adjust which issues are shown and can disable reports if desiring to work in a zero network configuration.

# Team Management

It may be desirable to suggest installing the VS Code extension for any team member. This can be done by adding a [Workspace Recommended Extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions) in the `.vscode/extensions.json` file of the workspace root directory:

```json
{
  "recommendations": [
    "SocketSecurity.vscode-socket-security"
  ]
}
```

# Limitations

* Requires an internet connection for reports on package manifest files. This is to access the <Anchor label="Socket API" target="_blank" href="https://docs.socket.dev/reference/introduction-to-socket-api#/">Socket API</Anchor> for analysis. Some analysis, such as bin confusion, cannot be done using a reference to a single dependency.

* The extension only works on local files and does not integrate any organization-level settings like the [GitHub App](https://docs.socket.dev/docs/socket-for-github#/) does. This will likely change in the future.

* The extension only works on the current files on disk and not historical data. If you need historical diffing or other tracking features, use the [GitHub App](https://docs.socket.dev/docs/socket-for-github#/).

.

# Auth and Permissions

The extension can be configured to use an <Anchor label="API token" target="_blank" href="https://docs.socket.dev/reference/creating-and-managing-api-tokens#/">API token</Anchor> for authentication. While the extension will still function without an API token, providing one enables additional functionality. By default, it will reuse the same configuration already set up in the CLI.

The API token requires the following scopes:

* `report:read`
* `report:write`

***

[Github App]: socket-for-github-installation

[Socket API]: https://docs.socket.dev/reference