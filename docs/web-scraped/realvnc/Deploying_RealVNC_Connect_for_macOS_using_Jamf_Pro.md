# Source: https://help.realvnc.com/hc/en-us/articles/18100694568733-Deploying-RealVNC-Connect-for-macOS-using-Jamf-Pro

# Deploying RealVNC Connect for macOS using Jamf Pro 

[Follow](/hc/en-us/articles/18100694568733-Deploying-RealVNC-Connect-for-macOS-using-Jamf-Pro/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360077753378/Jack_Naisbett_Professional_Headshot_for_web_-_Copy.jpg)

**[Jack N RealVNC](/hc/en-us/profiles/364261730191-Jack-N-RealVNC)**

Updated October 21, 2025 17:00

#### Important: Changes to Privacy Settings required RealVNC Server 7.15.0 

This article is undergoing updates to address the change in RealVNC Server 7.15.0 where vncagent has been replaced by RealVNC Server Agent.app.

This article covers how to deploy the RealVNC Server and RealVNC Viewer applications for macOS with Jamf Pro. The steps below require that you have already enrolled your macOS devices to Jamf Pro.

# Deploying the RealVNC Server application 

## Creating the package 

1.  Download the [latest PKG installer for RealVNC Server for macOS](https://downloads.realvnc.com/download/file/vnc.files/VNC-Server-Latest-MacOSX-universal.pkg) and make a note of the download location.
2.  Log in to your Jamf Pro Cloud Dashboard.
3.  On the left menu, click **Settings.\
    \
    ![Jamf_Settings.png](/hc/article_attachments/18146537206429)\
    \
    **
4.  In the search bar, type **packages** and click the **Packages** option.\
    \
    ![Jamf_Settings_Packages.png](/hc/article_attachments/18146556305437)\
    \
5.  Click **New.\
    \
    [![Jamf_Settings_Packages_New.png](/hc/article_attachments/18146556309917)](/hc/article_attachments/18146556309917)\
    \
    **
6.  Complete the package details. The below is the minimum required to deploy the application, please customise to meet your requirements.
    -   Enter a **Display Name** for the package, for example: **RealVNC Server 7.10.0**
    -   Under **Filename**, click **Choose File** and upload the PKG installer you downloaded in step 1.\
        \
        [![Jamf_Settings_Packages_Server.png](/hc/article_attachments/18146556314397)](/hc/article_attachments/18146556314397)\
        \
7.  Click **Save**. The package will be uploaded by Jamf.\
    \
    ![Jamf_Save.png](/hc/article_attachments/18147644866973)

## Deploying the package with a policy 

1.  Log in to your Jamf Pro Cloud Dashboard.
2.  On the left menu, click **Computers**, then click **Policies.\
    \
    ![Jamf_Computers_Policies.png](/hc/article_attachments/18146758291869)\
    \
    **
3.  Click **New.\
    \
    [![Jamf_Computers_Policies_New.png](/hc/article_attachments/18146758293533)](/hc/article_attachments/18146758293533)\
    \
    **
4.  Complete the policy details. The below is the minimum required to deploy the application, please customise to meet your requirements.
    -   Under the **Options** tab 
        -   In the **General** section:
            -   Enter a **Display Name** for the policy, for example: **RealVNC Server 7.10.0**
            -   Select the **Trigger(s)** for when the application should be deployed, for example on **Startup** or during a **Recurring Check-In.**
            -   Choose the **Execution Frequency**, for example, **Once per computer.\
                \
                [![Jamf_Computers_Policies_Server_General.png](/hc/article_attachments/18146738608541)](/hc/article_attachments/18146738608541)\
                **
        -   In the **Packages** section:
            -   Click **Configure** to enable the Packages section.\
                \
                [![Jamf_Computers_Policies_Server_Packages_Configure.png](/hc/article_attachments/18146738610845)](/hc/article_attachments/18146738610845)\
                \
            -   Click **Add** next to the package you wish to deploy, for example: **RealVNC Server 7.10.0\
                \
                [![Jamf_Computers_Policies_Server_Packages_Add.png](/hc/article_attachments/18146738617245)](/hc/article_attachments/18146738617245)\
                **
        -   In the **Maintenance** section:
            -   Click **Configure** to enable the Maintenance section.\
                \
                [![Jamf_Computers_Policies_Server_Maintenance_Configure.png](/hc/article_attachments/18146979997597)](/hc/article_attachments/18146979997597)\
                \
            -   Ensure **Update Inventory** is **enabled.\
                \
                [![Jamf_Computers_Policies_Server_Maintenance.png](/hc/article_attachments/18147010945181)](/hc/article_attachments/18147010945181)\
                **
    -   Under the **Scope** tab\
        -   Set **Target Users** to **All Users** as RealVNC Server is a system application.
        -   Define the Computers that RealVNC Server should be installed to. For example, you can choose **All Computers** or target specific computers/computer groups.
        -   Click **Done** once you have assigned/selected the appropriate deployment targets.\
            \
            [![Jamf_Computers_Policies_Server_Scope_1.png](/hc/article_attachments/18147537434397)](/hc/article_attachments/18147537434397)\
            \
            [![Jamf_Computers_Policies_Server_Scope_2.png](/hc/article_attachments/18147537432349)](/hc/article_attachments/18147537432349)
5.  Click **Save.\
    \
    ![Jamf_Save.png](/hc/article_attachments/18147644866973)\
    \
    **
6.  Jamf Pro will begin deploying the policy.
    -   You can choose to **Show in Jamf Pro Dashboard** to easily track the progress of the deployment.

## Configuring the required privacy settings 

1.  Log in to your Jamf Pro Cloud Dashboard.
2.  On the left menu, click **Computers**, then click **Configuration Profiles.\
    \
    ![Jamf_Computers_Configuration_Profiles.png](/hc/article_attachments/18148011551261)\
    \
    **
3.  Click **New.\
    \
    [![Jamf_Computers_Configuration_Profiles_New.png](/hc/article_attachments/18148032414237)](/hc/article_attachments/18148032414237)\
    \
    **
4.  Complete the policy details. The below is the minimum required to deploy the configuration profile, please customise to meet your requirements.
    -   Under the **Options** tab 
        -   In the **General** section:
            -   Enter a **Display Name** for the policy, for example: **RealVNC Server Accessibility and Screen Recording**
            -   Set the **Level** at which to apply the profile to **Computer Level**
            -   Set the **Distribution Method** to **Install Automatically\
                \
                ![Jamf_Computers_Configuration_Profiles_General.png](/hc/article_attachments/18148032417565)\
                **
        -   Scroll down to find the **Privacy Preferences Policy Control** section:
            -   Click **Configure** to enable the **Privacy Preferences Policy Control** section.\
                \
                [![Jamf_Computers_Configuration_Profiles_PPPC_Configure.png](/hc/article_attachments/18148011565341)](/hc/article_attachments/18148011565341)\
                \

            ```
            <!-- -->
            ```
            -   Set the **Identifier** to **/Library/vnc/vncagent**
            -   Set the **Identifier Type** to **Path**
            -   Set the **Code Requirement** to **identifier \"com.realvnc.vncagent\" and anchor apple generic\
                \
                [![Jamf_Computers_Configuration_Profiles_PPPC_Options.png](/hc/article_attachments/18148011570717)](/hc/article_attachments/18148011570717)\
                \
                **
            -   Click **Add** and select **Accessibility** from the dropdown. Set it to **Allow** and click **Save.\
                \
                [![Jamf_Computers_Configuration_Profiles_PPPC_Accessibility.png](/hc/article_attachments/18148032428317)](/hc/article_attachments/18148032428317)\
                \
                **
            -   Click **Add** and select **ScreenCapture** from the dropdown. Set it to **Allow Standard Users to Allow Access** and click **Save.\
                \
                [![Jamf_Computers_Configuration_Profiles_PPPC_ScreenCapture.png](/hc/article_attachments/18148011581981)](/hc/article_attachments/18148011581981)\
                \
                **
    -   Under the **Scope** tab\
        -   Set **Target Users** to **All Users** as RealVNC Server is a system application.
        -   Define the Computers that the configuration profile should be applied to. For example, you can choose **All Computers** or target specific computers/computer groups.
        -   Click **Done** once you have assigned/selected the appropriate deployment targets.\
            \
            [![Jamf_Computers_Policies_Server_Scope_1.png](/hc/article_attachments/18147537434397)](/hc/article_attachments/18147537434397)\
            \
            [![Jamf_Computers_Policies_Server_Scope_2.png](/hc/article_attachments/18147537432349)](/hc/article_attachments/18147537432349)\
            \
5.  Click **Save.\
    \
    ![Jamf_Save.png](/hc/article_attachments/18147644866973)\
    \
    **
6.  Jamf Pro will begin deploying the configuration profile.
    -   You can choose to **Show in Jamf Pro Dashboard** to easily track the progress of the deployment.

# Deploying the RealVNC Viewer application 

1.  Download the [latest DMG installer for RealVNC Viewer for macOS](https://downloads.realvnc.com/download/file/viewer.files/VNC-Viewer-Latest-MacOSX-universal.dmg) and make a note of the download location.
2.  Log in to your Jamf Pro Cloud Dashboard.
3.  On the left menu, click **Settings.\
    \
    ![Jamf_Settings.png](/hc/article_attachments/18146537206429)\
    \
    **
4.  In the search bar, type **packages** and click the **Packages** option.\
    \
    ![Jamf_Settings_Packages.png](/hc/article_attachments/18146556305437)\
    \
5.  Click **New.\
    \
    [![Jamf_Settings_Packages_New.png](/hc/article_attachments/18146556309917)](/hc/article_attachments/18146556309917)\
    \
    **
6.  Complete the package details. The below is the minimum required to deploy the application, please customise to meet your requirements.
    -   Enter a **Display Name** for the package, for example: **RealVNC Viewer 7.10.0**
    -   Under **Filename**, click **Choose File** and upload the DMG installer you downloaded in step 1.\
        \
        [![Jamf_Settings_Packages_Viewer.png](/hc/article_attachments/18148298092573)](/hc/article_attachments/18148298092573)\
        \
7.  Click **Save**. The package will be uploaded by Jamf.

## Deploying the package with a policy 

1.  Log in to your Jamf Pro Cloud Dashboard.
2.  On the left menu, click **Computers**, then click **Policies.\
    \
    ![Jamf_Computers_Policies.png](/hc/article_attachments/18146758291869)\
    \
    **
3.  Click **New.\
    \
    [![Jamf_Computers_Policies_New.png](/hc/article_attachments/18146758293533)](/hc/article_attachments/18146758293533)\
    \
    **
4.  Complete the policy details. The below is the minimum required to deploy the application, please customise to meet your requirements.
    -   Under the **Options** tab 
        -   In the **General** section:
            -   Enter a **Display Name** for the policy, for example: **RealVNC Viewer 7.10.0**
            -   Select the **Trigger(s)** for when the application should be deployed, for example on **Startup** or during a **Recurring Check-In.**
            -   Choose the **Execution Frequency**, for example, **Once per computer.**
            -   Set the **Target Drive** to **/Applications\
                \
                [![Jamf_Computers_Policies_Viewer_General.png](/hc/article_attachments/18148335297309)](/hc/article_attachments/18148335297309)\
                **
        -   In the **Packages** section:
            -   Click **Configure** to enable the Packages section.\
                \
                [![Jamf_Computers_Policies_Server_Packages_Configure.png](/hc/article_attachments/18146738610845)](/hc/article_attachments/18146738610845)\
                \
            -   Click **Add** next to the package you wish to deploy, for example: **RealVNC Viewer 7.10.0\
                \
                [![Jamf_Computers_Policies_Viewer_Packages_Add.png](/hc/article_attachments/18161208536605)](/hc/article_attachments/18161208536605)\
                **
        -   In the **Maintenance** section:
            -   Click **Configure** to enable the Maintenance section.\
                \
                [![Jamf_Computers_Policies_Server_Maintenance_Configure.png](/hc/article_attachments/18146979997597)](/hc/article_attachments/18146979997597)\
                \
            -   Ensure **Update Inventory** is **enabled.\
                \
                [![Jamf_Computers_Policies_Server_Maintenance.png](/hc/article_attachments/18147010945181)](/hc/article_attachments/18147010945181)\
                **
    -   Under the **Scope** tab
        -   Set **Target Users** to **All Users** as RealVNC Viewer is a system application.
        -   Define the Computers that RealVNC Viewer should be installed to. For example, you can choose **All Computers** or target specific computers/computer groups.
        -   Click **Done** once you have assigned/selected the appropriate deployment targets.\
            \
            [![Jamf_Computers_Policies_Server_Scope_1.png](/hc/article_attachments/18147537434397)](/hc/article_attachments/18147537434397)\
            \
            [![Jamf_Computers_Policies_Server_Scope_2.png](/hc/article_attachments/18147537432349)](/hc/article_attachments/18147537432349)
5.  Click **Save.\
    \
    ![Jamf_Save.png](/hc/article_attachments/18147644866973)\
    \
    **
6.  Jamf Pro will begin deploying the policy.
    -   You can choose to **Show in Jamf Pro Dashboard** to easily track the progress of the deployment.