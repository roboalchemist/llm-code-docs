# Source: https://docs.windsurf.com/troubleshooting/plugins-enterprise/visualstudio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.windsurf.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Visual Studio Troubleshooting

> Troubleshoot Visual Studio plugin issues including IntelliCode conflicts, Tab key bindings, and marketplace visibility problems.

<Note>
  We strongly recommend using the native Windsurf Editor or the JetBrains local plugin for their advanced agentic AI capabilities and cutting-edge features.
  The Visual Studio plugin is under maintenance mode.
</Note>

# Supported Versions

Visual Studio 17.5.5 or greater.

# Gathering extension logs

Go to `View > Output`, select `Codeium` in the dropdown, and copy the logs.

# Known IDE issues and solutions

## Don't see Codeium in the VS Marketplace

Make sure that you are using VS version 2022 17.5.5 or greater.

## Seeing overlapping autocomplete suggestions

This happens if Visual Studio's IntelliCode suggestions are displayed at the same time as Codeium's. Disable all IntelliCode options as shown below:

<Frame>
  <img src="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-disable-intellicode.jpg?fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=97b198bc53016b25ea553ddd054875d8" data-og-width="653" width="653" data-og-height="473" height="473" data-path="assets/plugins/troubleshooting-visualstudio-disable-intellicode.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-disable-intellicode.jpg?w=280&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=b032036da49a875f3854575e868f2b83 280w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-disable-intellicode.jpg?w=560&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=ec243d5e51b41d2f46ed3e3fd84f7232 560w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-disable-intellicode.jpg?w=840&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=862348338e23a5093572c7399ec34147 840w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-disable-intellicode.jpg?w=1100&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=1a8dad7959abb04d44577ac4a8e8c359 1100w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-disable-intellicode.jpg?w=1650&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=4e09f2520c0cac6706b8a7f6b65608cb 1650w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-disable-intellicode.jpg?w=2500&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=42d638451565f63c48db111eb003437d 2500w" />
</Frame>

## Tab key is not always accepting completions

You can rebind this to a different keyboard shortcut in your settings:

<Frame>
  <img src="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-keybindings.jpg?fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=b8ce35af4c3ab56df5a5a24f8ff1acfb" data-og-width="854" width="854" data-og-height="577" height="577" data-path="assets/plugins/troubleshooting-visualstudio-keybindings.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-keybindings.jpg?w=280&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=d7113b4cc5dee3c760ed228efd7b7558 280w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-keybindings.jpg?w=560&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=a7ad49c9077b52a9dfb1a12fb813ee0b 560w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-keybindings.jpg?w=840&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=3cd6a94281f0cfffbe464dcdef7d7db4 840w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-keybindings.jpg?w=1100&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=973712226fe19b3c63f06655f2b35ed3 1100w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-keybindings.jpg?w=1650&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=f6032a95e9267b5d611f8ab89243c246 1650w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/plugins/troubleshooting-visualstudio-keybindings.jpg?w=2500&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=b5ede19300c8a150f8f0279b7611cb6f 2500w" />
</Frame>
