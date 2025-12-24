# Source: https://help.realvnc.com/hc/en-us/articles/360002250657-Deploying-and-Licensing-RealVNC-Connect-using-Windows-MSIs

# Deploying and Licensing RealVNC Connect using Windows MSIs 

[Follow](/hc/en-us/articles/360002250657-Deploying-and-Licensing-RealVNC-Connect-using-Windows-MSIs/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360022267298/MicrosoftTeams-image__3_.png)

**[Tegan](/hc/en-us/profiles/366602748777-Tegan)**

Updated April 24, 2025 10:51

RealVNC Server and RealVNC Viewer are available as separate MSIs, in both 32-bit and 64-bit versions.

You can remotely deploy to target Windows computers using any suitable tool, for example SCCM or Group Policy.

**\*You can only license RealVNC Server as part of the deployment process if you have an Enterprise subscription**

To get started:

1.  Download the MSI installers for [RealVNC Server](https://downloads.realvnc.com/download/file/vnc.files/VNC-Server-Latest-Windows-msi.zip) and/or [RealVNC Viewer](https://downloads.realvnc.com/download/file/viewer.files/VNC-Viewer-Latest-Windows-msi.zip).
2.  Extract appropriate MSI(s).

# Installing at the command line 

You can use [`msiexec`] to install RealVNC Server and RealVNC Viewer. For example, running the following command at an Administrator Command Prompt:

[`msiexec`]` `[`/i`]` `[`"<RealVNC`]` `[`Server>.msi"`]` `[`transforms="vnc.mst"`]` `[`/qn`]

\...installs RealVNC Server silently and without restarting, and simultaneously [applies a transform](#h_3c1ddd39-e47f-49fc-8e8d-c50fdbe7479b) to configure RealVNC Server, perhaps by applying an offline license or disabling automatic update checks.

It is also possible to set properties directly on the command line. For example, running the following command at an Administrator Command Prompt:

[`msiexec`]` `[`/i`]` `[`"<VNC`]` `[`Server>.msi"`]` /`[`qn OFFLINELICENSE=<offline-license>`]

\...installs RealVNC Server 7.x silently and without restarting, and simultaneously applies the offline license to RealVNC Server.[]

# Creating a Group Policy Object (GPO) 

You can choose to deploy RealVNC Server and RealVNC Viewer to computers, to users, or to both in the standard way for a GPO.

If you choose to deploy to users, then once RealVNC Server is installed on a particular computer:

-   RealVNC Server in [User Mode](https://help.realvnc.com/hc/en-us/articles/360002253238) is available just to those users. RealVNC Server in Service Mode, however, is available to any user on the computer, since it is a system-wide service.
-   The RealVNC Printer Driver component must always be deployed to computers (that is, using the **Computer Configuration** section of Group Policy Management Editor), since this too is a system-wide service. See below for more information.

## Deploying RealVNC Server 

To deploy RealVNC Server, create a new GPO in the standard way, using Group Policy Management Editor. Create a new package for either users or computers and assign the appropriate versions of the RealVNC Server MSI to it.

When you have created the package in accordance with the instructions below, add users or computers to the GPO and link it to an appropriate Organizational Unit.

**\*If you need to [create a transform](#h_3c1ddd39-e47f-49fc-8e8d-c50fdbe7479b), do so on the Modifications tab of the Properties dialog *before* creating the package. It is not possible to add a transform once the package has been created.**

### Deploying RealVNC Printer Driver 

RealVNC Printer Driver is a required component for RealVNC Server if connected users will [print](https://help.realvnc.com/hc/en-us/articles/360002250537) to local printers. To deploy it:

1.  In Group Policy Management Editor, expand **Computer Configuration \> Policies \> Administrative Templates \> System \> Driver Installation**.
2.  Edit the **Allow non-administrators to install drivers for these device setup classes** policy setting.
3.  Choose **Enabled**, and click **Show** to add the RealVNC Printer Driver GUID: [`4658ee7e-f050-11d1-b6bd-00c04fa372a7`]
4.  Expand **Computer Configuration \> Policies \> Windows Settings \> Security Settings \> Local Policies \> Security Options**.
5.  Edit the **Devices: Prevent users from installing printer drivers** policy to **Define this policy setting** as **Disabled**.
6.  Edit the **User Account Control: Detect application installations and prompt for elevation** policy to **Define this policy setting** as **Disabled**.

**\*If you choose *not* to deploy RealVNC Printer Driver, you must explicitly exclude it from the installation process using a [transform](#h_3c1ddd39-e47f-49fc-8e8d-c50fdbe7479b).**

## Deploying RealVNC Viewer 

To deploy RealVNC Viewer, create a new GPO in the standard way, using Group Policy Management Editor. Create a new package for either users or computers and assign the appropriate versions of the RealVNC Viewer MSI to it.

When you have created the package (there are no custom instructions), add users or computers to the GPO and link it to an Organizational Unit.

# Creating a transform file 

## RealVNC Server 

Create a transform for RealVNC Server if you want to:

-   License RealVNC Server as part of the installation process. You can only do this if you have a subscription that includes offline licensing.\
    Note, RealVNC Server can be licensed post-installation, either desk-side (requires user interaction and elevated privileges), or using [Group Policy](/hc/en-us/articles/360005488898).
-   Omit one or both of the RealVNC Mirror Driver or RealVNC Printer Driver components.
-   Disable or enable automatic update checks. By default, RealVNC Server prompts the user to decide when the user interface first starts.
-   Disable or enable sending anonymous analytics to RealVNC. By default, RealVNC Server prompts the user to decide when the user interface first starts.

To create a transform:

1.  In [Orca](https://msdn.microsoft.com/en-us/library/windows/desktop/aa370557(v=vs.85).aspx), open the appropriate RealVNC Server MSI.
2.  Select **Transform \> New Transform**.
3.  Open the [`Property`] table.
4.  Add properties (**Tables \> Add row**) for the actions you wish to perform:

+-------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| To                                                                                  | Property                                       | Value                                                                                                            |
+-------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| License RealVNC Server 7.x with an offline license                                  | [`OFFLINELICENSE`]         | [`<offline-license-key>`]                                                                    |
+-------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| License RealVNC Server 6.x with an offline license                                  | [`LICENSEKEY`]             | [`<license-key>`]                                                                            |
+-------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| License RealVNC Server 7.9.0 and later online/join to the cloud                     | [`JOINCLOUD`]              | [`<cloud-connectivity-token>`]                                                               |
|                                                                                     |                                                |                                                                                                                  |
|                                                                                     |                                                | See [Using Cloud connectivity tokens](/hc/en-us/articles/360005474138#generating-a-cloud-connectivity-token-0-0) |
+-------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Specify the name of the computer group to add the RealVNC Server to the cloud       | [`JOINGROUP`]              | [`<computer-group-name>`]                                                                    |
|                                                                                     |                                                |                                                                                                                  |
| *used with [`JOINCLOUD`]*                                       |                                                | See [Using Cloud connectivity tokens](/hc/en-us/articles/360005474138#additional-options-0-4)                    |
|                                                                                     |                                                |                                                                                                                  |
|                                                                                     |                                                | Note: the group must already exist in the portal                                                                 |
|                                                                                     |                                                |                                                                                                                  |
|                                                                                     |                                                | Note 2: the name must be URL encoded, e.g. spaces are replaced by %20                                            |
|                                                                                     |                                                |                                                                                                                  |
|                                                                                     |                                                | Note 3: multiple group names can be provided as a comma separated list                                           |
+-------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Specify the name of the computer to use when adding the RealVNC Server to the cloud | [`JOINNAME`]               | [`<computer-name>`]                                                                          |
|                                                                                     |                                                |                                                                                                                  |
| *used with [`JOINCLOUD`]*                                       |                                                | See [Using Cloud connectivity tokens](/hc/en-us/articles/360005474138#additional-options-0-4)                    |
|                                                                                     |                                                |                                                                                                                  |
|                                                                                     |                                                | Note: the name must be URL encoded, e.g. spaces are replaced by %20                                              |
+-------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Exclude RealVNC Printer Driver                                                      | [`ADDLOCAL`]               | [`FeatureServer`]                                                                            |
+-------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Control automatic update checks                                                     | [`ENABLEAUTOUPDATECHECKS`] | [`0`] to disable \                                                                           |
|                                                                                     |                                                | [`1`] to enable                                                                              |
+-------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Control analytics                                                                   | [`ENABLEANALYTICS`]        | [`0`] to disable \                                                                           |
|                                                                                     |                                                | [`1`] to enable                                                                              |
+-------------------------------------------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

5.  Select **Transform \> Generate Transform**, and save the file in a suitable location.

**\*For a GPO, you should save the transform in the network share containing the RealVNC Server MSIs, and add it to the GPO before [creating the package](#h_642559f8-c510-4661-94a4-8b60a520711c).**

#### Looking to set RealVNC Server parameters? 

Do not use the Properties table detailed above to set RealVNC Server parameters. Please [see this guide](https://help.realvnc.com/hc/en-us/articles/360007759877) instead.

## RealVNC Viewer 

VNC Viewer does not support any properties via Transform file at this time.