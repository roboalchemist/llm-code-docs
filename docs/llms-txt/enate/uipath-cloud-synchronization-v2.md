# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/uipath/setting-up-enate-and-uipath-orchestrator-synchronization/uipath-cloud-synchronization-v2.md

# UiPath Cloud Synchronization V2

UiPath Cloud Synchronization V2 supports synchronisation with classic folders in UiPath Cloud Orchestrator.

{% hint style="info" %}
UiPath Cloud Synchronization V2 only works with version 2019.9.6 and above of Enate.&#x20;
{% endhint %}

See here for more information regarding which version of UiPath in Enate works with which versions of UiPath Orchestrator:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtGJqznyX0FkJ1sb56UE0%2FEnate%20%26%20UiPath%20Orchestrator%20Sync%20Settings.xlsx?alt=media&token=3a1d8504-9e2d-4e65-9e0a-a93865ea9eb8>" %}

## Synchronization between Enate and Uipath orchestrator

In Enate, we have a dedicated RPA section available in the Builder, where we can create and maintain the connections to Orchestrators :

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oKsnUoDqfM-5Yp%2F1.jpeg?generation=1632305156554686\&alt=media)

Within this section, we can configure multiple UiPath Orchestrators with which the Enate environment can be synchronised.

### Details Required to Configure a Connection

To add a new connection, click on Add Connection, give a name to the RPA connection based on the release version select the relevant technology (here we have selected the technology as UiPath cloud synchronization V2). The popups are dynamically launched according to the RPA Technology selected.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oLCkjvRnFQRjfc%2F2.png?generation=1632305156603206\&alt=media)

To establish a connection, we need below details:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oMHH3dS6lxB59r%2F3.png?generation=1632305156576001\&alt=media)

* URL - URL of the UiPath Orchestrator
* Account Logical Name - Account logical name for UiPath Orchestrator
* Client Id - Client Id for UiPath Orchestrator
* Folder Name - The name of the folder
* Tenant Logical Name - Tenant logical name for UiPath Orchestrator
* User Key - User key for UiPath Orchestrator
* Credential Store Name – The name of the credential store, used to store robot credentials

### Extracting Details from Orchestrator

Open the URL [https://cloud.uipath.com/portal](https://cloud.uipath.com/portal_/cloudrpa)

&#x20;Login into UiPath Orchestrator with the username and Password.

To get the details required to establish the RPA connection, click on admin (on the left-hand side) and then go to Tenants.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oNqVvfEpuwHU5W%2F4.png?generation=1632305156569561\&alt=media)

Expand the Tenants, click on the ellipses on the right-hand side of the orchestrator, select API access, copy the User Key, Account Logical Name, Tenant logical Name, Client Id and paste it in the desired sections of RPA connection in Enate

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oOlRMVP7IoCq6O%2F5.png?generation=1632305156563651\&alt=media)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oPpFT9SFl7x-OM%2F6.png?generation=1632305156607385\&alt=media)

Copy and paste the relevant data in the relevant fields of the below-highlighted section.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oQXCKi-yMM5qwi%2F7.png?generation=1632305156618288\&alt=media)

To create or access the folders, select the orchestrator (on the left side) and then go to tenants, click on the folders tab, we can use an available folder or else can create a new one. (As of now Enate supports only the classic folders).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oRuqLSiPRaWdi_%2F8.png?generation=1632305156566379\&alt=media)

Copy and paste the folder name in the below-highlighted section of the RPA connection.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oSlYEYDKY2bp0v%2F9.png?generation=1632305156565407\&alt=media)

To get the credential store name, go to the credential stores tab in the Uipath orchestrator, copy and paste the credential store name in the dedicated section of the RPA connection (as shown below).

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oTh8LYlFYGNMyq%2F10.png?generation=1632305156569619\&alt=media)

The URL will be the URL of the Uipath orchestrator. i.e., [https://cloud.uipath.com/portal](https://cloud.uipath.com/portal_/cloudrpa).

Test the connection and enable it, once the connection is successful.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oULP-38jrqDdri%2F11.png?generation=1632305156563688\&alt=media)

After establishing the connection, we need to connect the machine to the orchestrator. To do that, go to the machines tab in the tenant, and then click on add a new standard machine, basically the name of the machine will be the laptop’s name (Open the Control Panel. Click System and Security > System). Give License as 1.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oVtWJJVIdYpM3W%2F12.png?generation=1632305156606618\&alt=media)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oWVVp6YDjpxOSF%2F13.png?generation=1632305156559598\&alt=media)

The next step is to create a Robot, Click on the folder which we created and then go to the Robots tab, click on Add robot(standard). Provide the Machine name, name of the robot, select the type (Non-Production), domain name/Username (the one which we use to login into the system), the password is the password used for logging into the system and the credential type will be windows.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oXRP7iWxdVZmCm%2F14.png?generation=1632305156570068\&alt=media)

Once the Robot is created, we need to create the Environment, (environment is the bot farm that we create on Enate), click on Add environment, give the name to the Environment, and click on create.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oY60r-JCTxzJt7%2F15.png?generation=1632305156598438\&alt=media)

Since the connection between Enate and UiPath orchestrator is already established, environments and robots will be synced into Enate automatically.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oZqqeR8DqkhzlG%2F16.png?generation=1632305156566995\&alt=media)

In the Assets section, Enate will sync the environment URL and robot credentials.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-o_FRTHvEgVeDVJ%2F17.png?generation=1632305156580152\&alt=media)

To connect the machine (laptop) to the UiPath Orchestrator, copy the machine key from the machines tab in tenants and then open the Uipath Assistant in the machine(laptop), click on preferences in UiPath Assistant and then go to Orchestrator settings (on the left-hand side), select the connection type as Machine Key, give the machine name & machine key and orchestrator URL e.g. <https://cloud.uipath.com/AnkitEnate/AnkitEnate>, where ([https://cloud.uipath.com-](https://cloud.uipath.com-/) is the URL of UiPath Orchestrator, /AnkitEnate is the Account Logical Name/ AnkitEnate is the Tenant Name) after filling in the details click on connect, now the machine got connected to the Uipath Orchestrator.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oa8xJgfpFvJ-e1%2F18.png?generation=1632305156563828\&alt=media)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-obDKiNhni_jyLh%2F19.png?generation=1632305156573689\&alt=media)

And now when we go to the Robots section (under user management) in Enate, we can see the bot farm and the robot’s name.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oc9d6Wh1RyBSYs%2F20.jpeg?generation=1632305156569697\&alt=media)

Once the machine is connected to the orchestrator the relevant folder will appear at the bottom of the routine as shown below screenshot. (e.g., Amidha Folder).

In the Main file of UiPath Bot Routine, below Routine is published.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-od7jeu-DCzV7cI%2F21.png?generation=1632305156563356\&alt=media)

Get credential activity is used along with Enate activities. The output from getting credential activity will be username and password which is synchronized with Enate and UiPath orchestrator which will then be used for authentication of bot into Enate instance.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oe5ArmHbnxcNbl%2F22.png?generation=1632305156625012\&alt=media)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-ofz3P9z1DCsiUK%2F23.png?generation=1632305156560930\&alt=media)

Username is the Username of the Bot created in Enate and password is the password created in Enate and it is a secure password. So Please tick the checkbox of “Secure String “ in Authentication.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-ogLazdmdoh22lX%2F24.png?generation=1632305156578274\&alt=media)

The next step is to publish the Main file of the UiPath bot routine, to do that, select the package name that needs to be published. (Publish will publish the process in the relevant folder)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oh6zvu2J-brBsB%2F25.png?generation=1632305156563336\&alt=media)

Once the package is published, go to the folders in the Uipath orchestrator, and then go to the Automations tab, click on Add Process. In the Package source name, select the package which was published recently.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oi03t2xMWBFwmJ%2F26.png?generation=1632305156569534\&alt=media)

Go to the Robots in the User management tab on Enate, select the Bot Farm and define the integration process. (In the Integration process user needs to select which process needs to be triggered when the Action for the Bot Farm is available to work on)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-ojuswNR-6_fkXs%2F27.png?generation=1632305156565284\&alt=media)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-okElK8s4e_cN_S%2F28.png?generation=1632305156577494\&alt=media)

## Enate Process and Queue Configuration

### Builder Configuration

In Builder, we now need to configure an action that can be performed by the bot. To achieve that we need to go configure the Bot Farm in the Action General Settings in the Action Info.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-ol6rREWs-SY_IP%2F29.png?generation=1632305156571378\&alt=media)

In the general settings, the user needs to define the bot farm (can be performed by Robotics Group) and the estimated duration for the bot to complete the action.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-omJ8zUldxg9lRE%2F30.png?generation=1632305156580180\&alt=media)

### Adding Robots to the Queue

Team Leaders are the only people who can access the Queues Page. To add the robot to the queue, navigate to the queues section from work manager, click on edit and then add the queue in which the bot needs to be added.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-onAjkkE3ZxFEWO%2F31.png?generation=1632305156587912\&alt=media)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-ooY6XTBSYieuAa%2F32.png?generation=1632305156614900\&alt=media)

Once the respective queue is added, click on the ‘+’ icon on the queue and then add the robot.

The below screenshot explains how to add a robot to the queue.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-opQGeqKs3LF6SC%2F33.png?generation=1632305156612510\&alt=media)

As shown in the below Screenshot, the bot is now added to the queue.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oqKOMfkHse2mKt%2F34.png?generation=1632305156588362\&alt=media)

## Manage Page View and Running a Work Item

Once a Bot Action is launched in Enate, it sends a message to the UiPath Orchestrator which in turn creates a job in Orchestrator (which is available in Automation’s tab in UiPath Orchestrator). Orchestrator, then invokes the bot to perform the action defined in the bot routine.

Team Leaders can see the bot farm and the current status of Bots in the Work manager.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-orOGuPvRMJPDOh%2F35.png?generation=1632305156583286\&alt=media)

In the above screenshots, there is an action that is available for a bot to perform. When the Bot Routines executes the bot will get the action. If there are multiple work items then the bot will get the single most important piece of work based on the SLA.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-oshL5fgH-PPRCV%2F36.png?generation=1632305156577163\&alt=media)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MkBxS4vgw5Q70KUiP58%2F-MkBy-otwLVO_u5558aM%2F37.png?generation=1632305156579195\&alt=media)

We can now see that the Action is completed by the Bot which was created in the Uipath orchestrator and synchronized in Enate.
