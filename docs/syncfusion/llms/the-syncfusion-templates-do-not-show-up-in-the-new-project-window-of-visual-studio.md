# Source: https://docs.syncfusion.com/extension/faq/the-syncfusion-templates-do-not-show-up-in-the-new-project-window-of-visual-studio.md

# SyncfusionÂ® template not shown in new project window of Visual Studio

If the SyncfusionÂ® templates do not appear in Visual Studioâs New Project window, it is caused by one of the following two reasons:

1. The required SyncfusionÂ® Visual Studio extension is not installed.

2. The SyncfusionÂ® Extension is installed and listed in the Extension manager but the template is not shown in project window due to the incomplete installation process. 

> **Note:** Installing only the Syncfusion build will not make the templates available in the new project window of Visual Studio. You must also install the corresponding Visual Studio extension from the build.

Primarily check if the required SyncfusionÂ® Extension is installed:

- Open Visual Studio  â Extensions â Manage Extensions.

- In the Installed section, search for â{YourSyncfusionPlatform} Extension - Syncfusionâ.

- If the extension is not installed, follow the steps given in **Case1**.

- If the extension is installed and still the issue exist, follow the steps given in **Case2**.

## Case 1: SyncfusionÂ® Extension is not installed :

Install SyncfusionÂ® Extension in Visual Studio by following one of the options below:

  **Option 1: Install from Syncfusion Setup**

  - Navigate to the following location to install the {YourSyncfusionPlatform} extension:

    `C:\Program Files (x86)\Syncfusion\Essential Studio\YourSyncfusionPlatform\YourBuildVERSION\Utilities\Extensions\VS2022\`

  -  Double-click on â.vsixâ to begin the installation.

  **Option 2: Install via Visual Studio Marketplace**

  - Open Visual Studio â Extensions â Manage Extensions â Online.

  - Search for â{YourSyncfusionPlatform} Extension - Syncfusionâ and install it.

## Case 2: If the SyncfusionÂ® Extension Installed and the template is not shown in project window :

If the extension appears in the Extension Manager after installation but the SyncfusionÂ® template is still not shown in new project window, the issue is usually due to cached or incomplete installation of extension files. In such cases  uninstall existing SyncfusionÂ® extensions and reinstall to resolve this issue as mentioned below:

  - Open Visual Studio  â Extensions â Manage Extensions â Installed.

  - Search for âSyncfusionâ and uninstall all related extensions.

  - Manually delete any remaining Syncfusion extension-related files from the following locations:

      `%appdata%\Local\Microsoft\VisualStudio\17.0_xx\Extensions\Visual Studio Install Path\Common7\IDE\Extensions\`

  - Reinstall the extension by one of the option mentioned earlier in the installation steps.
