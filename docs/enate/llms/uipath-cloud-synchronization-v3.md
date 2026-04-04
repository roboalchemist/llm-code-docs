# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/uipath/setting-up-enate-and-uipath-orchestrator-synchronization/uipath-cloud-synchronization-v3.md

# UiPath Cloud Synchronization V3

UiPath Cloud Synchronization V3 supports the latest features of UiPath cloud orchestrator. This synchronization majorly covers the modern folders features which can be widely used for orchestration along with its sub folders.&#x20;

{% hint style="info" %}
UiPath Cloud Synchronization V3 only works with version 2022.6 and above of Enate.&#x20;
{% endhint %}

See here for more information regarding which version of UiPath in Enate works with which versions of UiPath Orchestrator:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtGJqznyX0FkJ1sb56UE0%2FEnate%20%26%20UiPath%20Orchestrator%20Sync%20Settings.xlsx?alt=media&token=3a1d8504-9e2d-4e65-9e0a-a93865ea9eb8>" %}

## **Steps to synchronize Enate and UiPath Cloud Orchestrator V3**

### Create a new RPA Sync Connection in Enate

You do this by going to the [RPA Sync Integration section in Enate Builder](https://docs.enate.net/enate-help/integrations/enate-integrations/uipath/setting-up-enate-and-uipath-orchestrator-synchronization/uipath-cloud-synchronization-v3) and selecting the '+' icon  to add a new connection. Enter a Name for the connection and from the Technology dropdown select 'UiPath Cloud Synchronisation V3'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0y4YOoY9X4xTUrA1fufi%2Fimage.png?alt=media&#x26;token=4ff5fe79-827c-404d-ba0c-47c363d981e9" alt=""><figcaption></figcaption></figure>

In the following pop-up, fill in the following details:

* URL - URL of the UiPath Orchestrator
* Tenant Name - Tenant logical name for UiPath Orchestrator
* Account Logical Name - Account logical name for UiPath Orchestrator (Field name: Organization ID)
* User Key - User key for UiPath Orchestrator
* Client ID - Client ID for UiPath Orchestrator
* Credential Store Name – The name of the credential store, used to store robot credentials

[See below for where you can find these details](#extracting-details-from-orchestrator).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FuVXxmYJxJHKNPUTUaXkX%2Fimage.png?alt=media&#x26;token=5268cb32-33a2-4e2b-874e-a8e894d51410" alt=""><figcaption></figcaption></figure>

Once all the details have been entered, you need to Test the Connection.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDxUSxUEp8vW17bzGemuI%2Fimage.png?alt=media&#x26;token=19e9697b-93df-4d67-9b61-9ec0a5e557cc" alt=""><figcaption></figcaption></figure>

&#x20;

Once the connection has been tested successfully, click to enable the connection:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnUh96rbesizOlrWXfxuT%2Fimage.png?alt=media&#x26;token=b5d6cd59-61f9-4d0a-affc-af51bd53c5aa" alt=""><figcaption></figcaption></figure>

#### Extracting Details from Orchestrator

To get the details required to establish the RPA connection in Enate, log in into UiPath Orchestrator with your username and password - link to [UiPath Orchestrator](https://cloud.uipath.com/portal).&#x20;

Navigate to: Admin -->&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FRF1x2qXscrWox6ymgVG3%2Fimage.png?alt=media&#x26;token=6f4b8230-4170-4b8a-8435-804de73b2952" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F9uK3dRHCBxxuNhnzZPpY%2Fimage.png?alt=media&#x26;token=51139506-bdc3-46b7-a63c-42468c97084a" alt=""><figcaption></figcaption></figure>

DefaultTenant --> Services --> Orchestrator --> API Access

Click on the ellipses on the right-hand side of the orchestrator and select API access.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0eaH9LHbIgaoASw8k5Rl%2Fimage.png?alt=media&#x26;token=d4b51463-5fc0-4203-a493-89a3b713f8af" alt=""><figcaption></figcaption></figure>

&#x20;

In the following pop-up you can find the User Key, Account Logical Name, Tenant logical Name, Client ID information.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVp8A1JRXFijLmR141JY0%2Fimage.png?alt=media&#x26;token=c436f37c-0284-4db0-b818-5405c19e6f22" alt=""><figcaption></figcaption></figure>

### Restart the application engine

Now go to Enate Manager and open the instance to re-start the application engine:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FL4U9DSTyobYRV7EtCHt6%2Fimage.png?alt=media&#x26;token=b9b5c314-c325-4a07-8367-2b9a974a8ab0" alt=""><figcaption></figcaption></figure>

### Open UiPath Assistant

Open UiPath Assistant and navigate to User Profile > Preferences > Orchestrator Settings.

In the Connection Type dropdown, select ‘Service URL’ and then in the resulting Service URL dropdown select ‘<https://cloud.uipath.com/’>.

Then click to 'Sign in'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fz33l1esEE4SBHHgQ5TKo%2Fimage.png?alt=media&#x26;token=bd3a8081-89be-4f49-8de4-ffb0c4dad94e" alt=""><figcaption></figcaption></figure>

Click to 'Open UiPath':

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUs1NgwB3zzfHgjHVOXNR%2Fimage.png?alt=media&#x26;token=d9cd0892-265c-4f26-bd72-0487f916efc8" alt=""><figcaption></figcaption></figure>

Once you are signed in, the Status will now be showing as Connected.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPMtwAi9vJEQur2vUTWTz%2Fimage.png?alt=media&#x26;token=e80352da-d127-49f4-935b-15e402559a39" alt=""><figcaption></figcaption></figure>

### Open UiPath Orchestrator

Now you need to make sure to check that your machine shows up in Cloud Orchestrator. To do this, go back to UiPath Orchestrator and then click on Tenant and Machines.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3DBHiihhHmXHHHJ5CS3M%2Fimage.png?alt=media&#x26;token=634fc484-fffe-466f-b0e6-a1c7e986c9d4" alt=""><figcaption></figcaption></figure>

### Select a Folder

Now you need to select a modern folder to assign a robot account to, to assign a machine to and to create an automation process in.

To select a folder, click on Orchestrator (on the left side), then Tenant and then click on the Folders tab.&#x20;

Here you can either either create a new folder by selecting the New Folder icon or you can use the default ‘Shared’ folder.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fk3Ex81RfeseS0ku59gbs%2Fimage.png?alt=media&#x26;token=60b3be08-09ea-4c1b-b6d4-e01861cb4d64" alt=""><figcaption></figcaption></figure>

### Create a Robot account

The next step is to create a Robot account. You can do this by navigating to the Admin section of UiPath Orchestrator and then selecting:&#x20;

Enate --> Accounts & Groups --> Robot Accounts --> Add Robot Account

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVWFNCyjotVCO8G3dM9yq%2Fimage.png?alt=media&#x26;token=f0adcf6e-e130-47db-8938-631588631979" alt=""><figcaption></figcaption></figure>

In the following pop-up add the name of the Robot Account, select 'Everyone' under the Group Membership options and then click 'Add'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPmcHaLIQ312DN6LU36gc%2Fimage.png?alt=media&#x26;token=76b36f25-6e94-4c83-9014-35850d2c8312" alt=""><figcaption></figcaption></figure>

#### Assign roles

Now we need to assign roles to the robot account. To do this, click on the folder which we created, and then go to Users --> Settings --> Manage access --> Assign Account/Group.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0os4fq3u4X1FMmFB200s%2Fimage.png?alt=media&#x26;token=3ecbb463-5b57-416d-bb62-ba341f594ddb" alt=""><figcaption></figcaption></figure>

Search for the robot account we just added and select it from the drop down.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDUPWTZFAM6veheUe6jvn%2Fimage.png?alt=media&#x26;token=7a18a76c-87a1-4284-b438-b2f6deb97522" alt=""><figcaption></figcaption></figure>

Then add a 'Robot' role to the robot account and click on 'Assign'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVbCJT736oicGUE72lmCS%2Fimage.png?alt=media&#x26;token=4d68b769-143c-463f-a6fb-0f7c2e98d99d" alt=""><figcaption></figcaption></figure>

Once you have done this, the robot account will appear in the modern folder with its roles.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBb2GoSJP2SN3jXLAUilz%2Fimage.png?alt=media&#x26;token=059aa45a-13c9-480e-9773-a6ccf8982f4e" alt=""><figcaption></figcaption></figure>

### Assign Machine to the modern folder

You now need to assign a local machine to the folder. To do this, click on Tenant and then Settings. Click on the ellipses of the folder you just created and hover over 'Settings'. Then click on 'Assign Machines'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FABrbtdq7yIUyV9CeQ9m3%2Fimage.png?alt=media&#x26;token=688338ba-e075-4279-8ce4-14d568479293" alt=""><figcaption></figcaption></figure>

Select the local machine name and click Update.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjnATaglL1Sf2JCfebcNK%2Fimage.png?alt=media&#x26;token=adaab739-e586-40e3-9a36-2eb70e041c08" alt=""><figcaption></figcaption></figure>

Now the local machine will show in the modern folder you created under the Machines tab.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FV6OD0FFUoZYKaWditAM6%2Fimage.png?alt=media&#x26;token=1987f983-2eeb-441c-aa20-7177b6586515" alt=""><figcaption></figcaption></figure>

If a red warning symbol appears, it means that there is no license assigned to the machine. To assign a license, go to the modern folder home screen and click on the Machines tab.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FbTe4TFF9gcSkuoXzDprq%2Fimage.png?alt=media&#x26;token=f3cb28c3-809b-44dc-a719-158e874f10aa" alt=""><figcaption></figcaption></figure>

Click on the ellipses menu and then select 'Edit Machine'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FglW68xdPClOG52SZQEgJ%2Fimage.png?alt=media&#x26;token=8f42ad30-6b06-46fd-a848-94fe3bd133e4" alt=""><figcaption></figcaption></figure>

Here you can update the production license from '0' to '1' and click 'Update'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fx3vZQ0Kf8aRgmztSQIy7%2Fimage.png?alt=media&#x26;token=50a01202-9018-410c-a3dc-51262ffae8c4" alt=""><figcaption></figcaption></figure>

Now the machine is licensed and we can see that the warning symbol has disappeared.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0rXyBbD2akcBy3B7S4kg%2Fimage.png?alt=media&#x26;token=9a7d0654-1f03-440d-ba2a-0b11867612c9" alt=""><figcaption></figcaption></figure>

### Check Bot and Bot Environment Synced

And now when we go to the Robots section (under User Management) in Enate, you can see that the robot you've just created in UiPath Orchestrator is showing in Enate.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FhwoHPci5e59ioGRkWsSa%2Fimage.png?alt=media&#x26;token=1a3565da-9cc4-408b-a869-df882e9a94e2" alt=""><figcaption></figcaption></figure>

### Update robot to run a job/process

In the Unattended Setup section, under the Foreground automated settings section select 'Use a specific Windows user account. Add credentials below'.

In the resulting fields give your Domain\Username according to the following format: enate\firstname.lastname with 'enate' as the domain and you name as the username e.g. enate\rama.verdelli and enter your enterprise password as the password.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fk7buJKVYtl9c0GdL5JHb%2Fimage.png?alt=media&#x26;token=1620a4ff-a0b4-4933-ac18-3c8c6926cbcf" alt=""><figcaption></figcaption></figure>

### Publish the Project in your Machine

The next step is to publish the the UiPath project in your local machine. To do this, go to UiPath Studio, select the desired UiPath project that Enate will trigger based on Action configuration and click 'Publish'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFTThS7XCNjIRzuobYClx%2Fimage.png?alt=media&#x26;token=df7a531d-6583-4318-a04b-106d4eaebdf5" alt=""><figcaption></figcaption></figure>

And then in Package Name enter the name of project you are wanting to publish and click Next.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FN93xGR6X8lvRmT42lRzK%2Fimage.png?alt=media&#x26;token=f21f42f2-3ec0-4c20-ab6c-3c4fae057c09" alt=""><figcaption></figcaption></figure>

Then for the Custom URL click the folder icon and select the folder where you want to save the package and then select 'Publish'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1eKtMpGP3XZeB3hs5CXe%2Fimage.png?alt=media&#x26;token=73db1453-7960-471f-99f1-2a554362068f" alt=""><figcaption></figcaption></figure>

### Upload Package to UiPath Orchestrator

Once the package is published you need to upload it to UiPath Orchestrator. To do this, go to Tenant, select the Packages tab and then click on Upload.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FcnHQEO7UJQ8vu6ZLZzsh%2Fimage.png?alt=media&#x26;token=009867a6-5011-4a67-88bd-039b6953e2d5" alt=""><figcaption></figcaption></figure>

In the resulting pop-up, select the published package from the local folder you have just saved it to and click Upload.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FgS0MxbRFR3j3Kmjjwc1L%2Fimage.png?alt=media&#x26;token=31d13733-a017-4435-a075-da851f246159" alt=""><figcaption></figcaption></figure>

The recently uploaded package should now be visible in the Packages tab.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOfmOgHzj3f3Ussi36CsV%2Fimage.png?alt=media&#x26;token=4e980168-f57c-4a59-8de7-d3a9dd176ff8" alt=""><figcaption></figcaption></figure>

### Create a Process Using the Package

The next step is to create a process using the package you have just published in the previous step.

To do this, navigate to the desired modern folder and then click Automations > Processes > Add Process

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FrExcsNlaxAukq5bBU7JM%2Fimage.png?alt=media&#x26;token=6fbce79b-10cf-4bed-8838-2929ac8b8f9f" alt=""><figcaption></figcaption></figure>

Select the package that was just published in the previous step and click Next.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FB6Ex8phoE25qrDrkDXQA%2Fimage.png?alt=media&#x26;token=69c2334e-8b06-4e66-baca-26d0de05f2b0" alt=""><figcaption></figcaption></figure>

Add a Display name and a description if you want and then click Create.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnRUBUl6B1dscf9RIMI8T%2Fimage.png?alt=media&#x26;token=bbcbab86-d0b8-4de6-8e68-c61c015351e9" alt=""><figcaption></figcaption></figure>

Then click on the play button to start the job manually from Cloud Orchestrator:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZ1TGLXipKCFzdNmIFLo8%2Fimage.png?alt=media&#x26;token=2e0a14eb-16ab-47da-bcc9-f3dd6a1a866c" alt=""><figcaption></figcaption></figure>

In the following screen, enter the same robot account, local machine and hostname as selected in the above steps and click Start.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FHDQUcufJvIdxwSOMpa3N%2Fimage.png?alt=media&#x26;token=9bd52f73-8256-4716-b788-f23b26be3117" alt=""><figcaption></figcaption></figure>

In the Jobs tab you can see that the job is now running.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FM3zm8we28j3I5XVC7VFz%2Fimage.png?alt=media&#x26;token=d98ef12b-50a7-441d-bb40-fda45317295c" alt=""><figcaption></figcaption></figure>

And you can see when the job is completed.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQtYHe3Uw0u2goEFkj18y%2Fimage.png?alt=media&#x26;token=7440b3e3-c3df-4ac7-ac87-0ec51c7ede8d" alt=""><figcaption></figcaption></figure>

Back in Enate, click to edit the robot that got synced:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8K0VMj055EOwnLsMnC3P%2Fimage.png?alt=media&#x26;token=d049b507-d58a-43d9-ba75-0217687e4dc0" alt=""><figcaption></figcaption></figure>

And then click to edit the Bot Farm.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMzLaVOqvslqA2Q9xIW75%2Fimage.png?alt=media&#x26;token=6addf9f6-4f59-4b1d-81ce-b1928a2e7641" alt=""><figcaption></figcaption></figure>

Here you need to click on the Integration Process dropdown and select the job you want the Bot Farm to perform: &#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeNdLKD9hWffzEZ61Rxf5%2Fimage.png?alt=media&#x26;token=33bc9433-8551-4cca-9ca4-8b86356a00bf" alt=""><figcaption></figcaption></figure>

We now need to configure an Action that can be performed by the bot. To do this we need configure the Bot Farm (from Orchestrator) in an Action's General Settings.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FwztCuAyLwAuPRxc9w7tX%2Fimage.png?alt=media&#x26;token=ca6f6f05-8f64-4392-894e-f822e87791d7" alt=""><figcaption></figcaption></figure>

To do this, select to clone the General Settings of the Action and then add the bot farm that we adding in the integration process. You can add the estimated duration for the bot to complete the action if you want.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJk6pFpKjlaJKhKpIYBOI%2Fimage.png?alt=media&#x26;token=c5d5fa75-c216-44a0-834b-040c83582ceb" alt=""><figcaption></figcaption></figure>

We then need to adjust the allocation rules for the Action. To do this, select to clone the Allocation rules and then in the Queue field select the desired Queue (we will add the bot to the Queue in the next step).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fj8CY3O4C7M7xTCfotukd%2Fimage.png?alt=media&#x26;token=4686a386-69c2-45a3-8466-8394245c3c3d" alt=""><figcaption></figcaption></figure>

Set the process live.

### Add bot to Queue

Once the process has been set live, as a Team Leader go to the Queues page, click on edit and then add the robot to the Queue you want it to work from.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FynAeZjsPBam0PdIYt8aI%2Fimage.png?alt=media&#x26;token=27d8a880-7d3f-44de-bee3-df41a81896cf" alt=""><figcaption></figcaption></figure>

When the Case process you have just configured gets launched in Enate Work Manager, and when the Action we have just configured gets created, the integration process will be triggered.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FbEKXtIiTzCuebFJ2UxmH%2Fimage.png?alt=media&#x26;token=01cf706a-8e23-4985-9932-bad5ae57fa18" alt=""><figcaption></figcaption></figure>

When the Action is created and pushed to a Queue that has the desired deep-integrated robot, it sends a message to UiPath Cloud Orchestrator to get a job ready for the selected integration process for the selected robot.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F53SB2buSce7POVZzjlBV%2Fimage.png?alt=media&#x26;token=07140038-1975-4120-96eb-18a12c8b5c20" alt=""><figcaption></figcaption></figure>

You will be able to see when the job triggered from Enate has completed successfully.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFEKzY2Bq5LTxowiyqHuG%2Fimage.png?alt=media&#x26;token=c1f04806-483e-4894-96ad-c3a777e6af98" alt=""><figcaption></figcaption></figure>
