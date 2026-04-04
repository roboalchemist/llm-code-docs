# Desktop MSI installer and group policy guide

.. raw:: html

> \<div class=\"mm-badge mm-badge\--note\"\>

[\|plans-img-yellow\|](##SUBST##|plans-img-yellow|) Available on [Entry,
Professional, Enterprise, and Enterprise Advanced
plans](https://mattermost.com/pricing/)

</div>

This page provides guidance on installing the desktop app MSI and use
Group Policies in Windows for Mattermost Enterprise or Professional. The
MSI installer package can be downloaded
[here](https://github.com/mattermost/desktop/releases/tag/v6.0.4).

:::: tip
::: title
Tip
:::

Want to
`distribute the official Windows desktop app silently </deployment-guide/desktop/silent-windows-desktop-distribution>`{.interpreted-text
role="doc"} to your end users instead?
::::

## Download group policy and MSI installer files

1. Using a newly created Windows VM or dedicated Windows computer, make
    sure to use a Windows version that supports `Edit group policy` out
    of the box (i.e. Windows 10 Pro or Enterprise).

    ![When downloading group policy and MIS installer files, ensure to use a Windows version that supports Edit group policy.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00001.png)

2. Navigate to the [Mattermost
    Desktop](https://github.com/mattermost/desktop) repository on
    [GitHub.com](https://github.com/).

    ![Go to the mattermost/desktop repository on GitHub.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00002.png)

3. Navigate to the release page for [version
    v6.0.4](https://github.com/mattermost/desktop/releases/tag/v6.0.4)
    and download the appropriate installer for your version of Windows
    (32-bit vs. 64-bit).

4. Download the
    [source.zip](https://github.com/mattermost/desktop/archive/v6.0.4.zip)
    file as well to extract group policy files.

    ![In the mattermost/desktop repository on GitHub, go to the release page for the latest desktop release, then download the installer for your version of Windows. Download the source.zip file as well to extract group policy files.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00003.png)

## Install group policy files locally

The following group policies are available supporting a state option of
Not Configured, Enabled, or Disabled:

> ------------------------------------------------------------------------------------
> Group policy  Description                    Mattermost   Setting
> release
> ------------- ------------------------------ ------------ --------------------------
> Enable Server If disabled, management of     v4.3 or      `EnableServerManagement`
> Management    servers in the app settings    later
> are disabled.
>
> Default       Define one or more default,    v4.3 or      `DefaultServerList`
> Server List   permanent servers.             later
>
> Automatic     If disabled, automatic desktop v5.1 or      `EnableAutoUpdates`
> Updates       app updates are disabled.      later
> ------------------------------------------------------------------------------------

1. Browse to the folder the above files were downloaded to and unzip
    the `desktop-6.0.3.zip` file in place.

    ![Go to the install download directory on your machine and unzip the ZIP file.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00004.png)

2. Navigate to the unzipped `desktop-6.0.3\resources\windows\gpo`
    folder and copy the contents.

    ![Go to the \\resources\\windows\\gpo directory and copy its contents.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00005.png)

3. Navigate to the `C:\Windows\PolicyDefinitions` folder and paste the
    files copied in the last step.

    ![Go to the Windows\\PolicyDefinitions directory and paste the files you copied in the previous step.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00006.png)

4. Verify the `mattermost.admx` file is in the
    `C:\Windows\PolicyDefinitions` folder.

    ![Verify the mattermost.admx file is present in the Windows\\PolicyDefinitions directory.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00007.png)

5. Verify the `mattermost.adml` file is in the
    `C:\Windows\PolicyDefinitions\en-US` folder.

    ![Verify the mattermost.adml file is present in the Windows\\PolicyDefinitions\\en-US directory.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00008.png)

:::: note
::: title
Note
:::

- `\\FQDNDomain\sysvol\FQDNDomain\Policies\PolicyDefinitions` can be
  used instead of `C:\Windows\PolicyDefinitions` if available.
- `\\FQDNDomain\sysvol\FQDNDomain\Policies\PolicyDefinitions\en-US` can
  be used instead of `C:\Windows\PolicyDefinitions\en-US` if available.
::::

**Disable automatic updates**

Automatic desktop app updates can be disabled by configuring the
supported group policy. Changes to group policies require you to restart
Mattermost for those changes to take effect.

## Configure Mattermost using group policy settings

1. Run the `Edit group policy` application by selecting **Start**,
    typing `gpedit` into the search field, then selecting the resulting
    **Edit group policy** search option.

    ![When configuring Mattermost using group policy settings, run the Edit group policy application by going to Start, typing gpedit into the search field, then selecting the resulting Edit group policy search option.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00009.png)

2. In the **Edit group policy** window, navigate to
    `Local Computer Policy\Computer Configuration\Administrative Templates\Mattermost`.
    In this example, double-click on `DefaultServerList` to set one or
    more default servers that will appear on app launch.

    ![In the Edit group policy window, go to Local Computer Policy \> Computer Configuration \> Administrative Templates \> Mattermost. To set one or more default servers to appear on app launch, for example, double-click on DefaultServerList to begin.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00010.png)

3. In the resulting window for **DefaultServerList**, select
    **Enabled** to turn the feature on, then select the **Show...**
    button in the **Options:** section of the window to add default
    servers.

    ![In the DefaultServerList window, enable the feature, then select Show\..., located under Options, to add the default servers.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00011.png)

4. In the resulting window, add desired Mattermost servers using a
    memorable name (i.e., Community) and the web URL of the Mattermost
    server (i.e., <https://community.mattermost.com>).

5. Select **OK** twice, then close the **Edit group policy** app.

    ![Add the default servers by name and by URL, then select OK twice to close the Edit group policy application.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00012.png)

## Multi-view and Group Policies

From desktop v6.0, users can run multiple Mattermost workspaces at the
same time in the desktop app. Use existing methods to pre-provision
multiple workspaces for users, as follows:

- On Windows, seed the approved list using the `DefaultServerList` Group
  Policy.
- For scripted installs, seed `config.json` on first run to include
  multiple entries in the `teams` array. See the
  `Silent Windows desktop distribution </deployment-guide/desktop/silent-windows-desktop-distribution>`{.interpreted-text
  role="doc"} documentation for details.
- To prevent users from adding or removing workspaces, use the existing
  `EnableServerManagement` Group Policy.
- Disable `EnableAutoUpdates` to turn off automatic updates.

### Verify group policy settings have been applied

1. Open up the Registry Editor by selecting **Start**, typing
    `Registry Editor` in the search field, then selecting the **Registry
    Editor** option in the search results.

    ![When verifying group policy settings, open the Registery Editor by going to Start, typing Registry Editor into the search field, then selecting the resulting Registry Editor search option.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00013.png)

2. In the **Registry Editor** window, navigate to
    `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Mattermost\DefaultServerList`
    and verify the servers you added using the **Edit group policy** app
    are listed.

3. Once verified, close the **Registry Editor**.

    ![Go to Computer \> HKEY_LOCAL_MACHINE \> SOFTWARE \> Policies \> Mattermost \> DefaultServerList to veryfiy the servers you added, then close the Registry Editor.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00014.png)

## Install the Mattermost Desktop App using the MSI installer

:::: important
::: title
Important
:::

- If the desktop app is running when you install via the MSI, Mattermost
  prompts you to close the app manually. After acknkowledging the
  prompt, select **Retry** to continue the MSI installation.
- Avoid selecting **Ignore**. If you do, force close the desktop app
  using Task Manager, ensure the `Mattermost.exe` process is stopped,
  and then restart the MSI installation.
::::

1. Within the folder the MSI installer was downloaded to, double-click
    on the MSI installer to begin the Mattermost Desktop installation
    process.

    ![Go to the folder where you downloaded the Mattermost Desktop App, and double-click on the MSI file to begin the installation process.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00015.png)

2. Installation of the MSI requires admin permission, so accept the
    resulting request to allow the installer to make changes to your
    device.

    ![You\'ll be prompted to allow the Mattermost Desktop App to make changes to your system. You must select Yes to continue with the installation process.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00016.png)

3. Select **Finish** when the installation is complete.

    ![When the installation is complete, select Finish.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00017.png)

### Verify group policy settings in the installed desktop app

1. Launch the newly installed Mattermost app from the **Start** menu.

2. Verify the app loads the first server you defined in the **Edit
    group policy** app.

    ![Verify group policy settings in the Mattermost Desktop App by opening the app from the Start menu, and verifying that the app loads the first server you defined in the Edit group policy.](../../images/desktop/msi_gpo/msi_gpo_installation_test_00018.png)

## Advanced MSI options

:::: important
::: title
Important
:::

You must be a system admin to run these commands, or you must run them
from an admin command prompt or PowerShell.
::::

### Silent installation

Perform a silent installation of the MSI by running the following
command:

:::: important
::: title
Important
:::

Ensure the desktop app is closed before proceeding with a silent
installation. Because it\'s a silent installation, Mattermost won\'t
prompt you to close the desktop app.
::::

**Command Prompt:** `msiexec /i mattermost-desktop-v6.0.4-x64.msi /qn`

**PowerShell:**
`Start-Process -FilePath "$env:systemroot\system32\msiexec.exe" -ArgumentList '/i mattermost-desktop-v6.0.4-x64.msi /qn'`

:::: note
::: title
Note
:::

\- You\'ll need to update the version details in this command as new
versions of the Mattermost desktop app are released.
::::

From version v5.9.0 of the Mattermost desktop app, the following silent
MSI installation options are also available.

### Install for all users

Use the `ALLUSERS` parameter to install the MSI for all users:

**Command Prompt:**
`msiexec /i mattermost-desktop-v6.0.4-x64.msi ALLUSERS=1`

**PowerShell:**
`Start-Process -FilePath "$env:systemroot\system32\msiexec.exe" -ArgumentList '/i mattermost-desktop-v6.0.4-x64.msi ALLUSERS=1'`

:::: note
::: title
Note
:::

\- Installing the MSI for all users disables automatic updates for the
desktop app on Windows. - To disable automatic updates on a per-user
basis, use the `DISABLEAUTOUPDATE` parameter:
`msiexec /i mattermost-desktop-v6.0.4-x64.msi DISABLEAUTOUPDATE=1`
::::

### Specify an install directory

Use the `APPLICATIONFOLDER` parameter to specify an installation
directory for the MSI installation:

- **Command Prompt:**
  `msiexec /i mattermost-desktop-v6.0.4-x64.msi APPLICATIONFOLDER="<install directory>"`
- **PowerShell:**
  `Start-Process -FilePath "$env:systemroot\system32\msiexec.exe" -ArgumentList '/i mattermost-desktop-v6.0.4-x64.msi APPLICATIONFOLDER="<install directory>"'`

Change this command as new versions of the Mattermost Desktop App are
released.
