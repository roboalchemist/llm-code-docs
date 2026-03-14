# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/uipath/setting-up-enate-and-uipath-orchestrator-synchronization/uipath-synchronization-v4.md

# UiPath Synchronization V4

UiPath Synchronization V4 supports the latest features of UiPath orchestrator. This synchronization majorly covers the modern folders features which can be widely used for orchestration along with its sub folders.&#x20;

{% hint style="info" %}
UiPath Synchronization V4 only works with version 2022.6 and above of Enate.&#x20;
{% endhint %}

See here for more information regarding which version of UiPath in Enate works with which versions of UiPath Orchestrator:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtGJqznyX0FkJ1sb56UE0%2FEnate%20%26%20UiPath%20Orchestrator%20Sync%20Settings.xlsx?alt=media&token=3a1d8504-9e2d-4e65-9e0a-a93865ea9eb8>" %}

## **Steps to synchronize Enate and UiPath Orchestrator V4**

### Create a new RPA Sync Connection in Enate

You do this by going to the [RPA Sync Integration section in Enate Builder](https://docs.enate.net/enate-help/integrations/enate-integrations/uipath/setting-up-enate-and-uipath-orchestrator-synchronization/uipath-synchronization-v4) and selecting the '+' icon  to add a new connection. Enter a Name for the connection and from the Technology dropdown select 'UiPath Synchronisation V4'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0y4YOoY9X4xTUrA1fufi%2Fimage.png?alt=media&#x26;token=4ff5fe79-827c-404d-ba0c-47c363d981e9" alt=""><figcaption></figcaption></figure>

In the following pop-up, fill in the following details:

* URL - URL of the UiPath Orchestrator
* Tenant Name - Tenant name for UiPath Orchestrator
* Username - Username for UiPath Orchestrator
* Password - Password used to access UiPath Orchestrator
* Credential Store Name – name of the credential store, used to store robot credentials

[See below for where you can find these details](#extracting-details-from-orchestrator).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FI9eW5PD4POz9IfdO4KxA%2Fimage.png?alt=media&#x26;token=2c86690b-727f-46f3-bf28-26eb887226c9" alt=""><figcaption></figcaption></figure>

Once all the details have been entered, you need to Test the Connection.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8jcfp9yizYf1UluTWckc%2Fimage.png?alt=media&#x26;token=54c48b1a-6d80-4f07-9867-cd52ffb73467" alt=""><figcaption></figcaption></figure>

&#x20;

Once the connection has been tested successfully, click to enable the connection:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FWyo1L2ES6JpaC2o9mKc6%2Fimage.png?alt=media&#x26;token=8dbd713d-1384-4063-9154-b7fc5ffcedd7" alt=""><figcaption></figcaption></figure>

#### Extracting Details from Orchestrator

Create a user account for your on prem Orchestrator and use these details (URL, username, password, tenant name and credential store name) to establish the RPA connection in Enate.

### Restart the application engine

Now go to Enate Manager and open the instance to re-start the application engine:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FL4U9DSTyobYRV7EtCHt6%2Fimage.png?alt=media&#x26;token=b9b5c314-c325-4a07-8367-2b9a974a8ab0" alt=""><figcaption></figcaption></figure>

### Log in to On Prem Orchestrator

Create a machine template by clicking Tenant and then Machines. Click on Add Machine Template

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfceDXjeMyYKZ2NgjKsNx%2Fimage.png?alt=media&#x26;token=31fe2329-67a1-4257-ac33-c459723fabb5" alt=""><figcaption></figcaption></figure>

Click Provision after entering the Template name and increasing the number of Licenses to at least 1

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqfNwGhp6O8GQteQG2rUn%2Fimage.png?alt=media&#x26;token=f1dbd875-fdf0-405b-b419-8ec376015d47" alt=""><figcaption></figcaption></figure>

Now you need to make sure to check that above created machine shows up in under Tenant -> Machines.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzmM0tAkyBD2U6wT9OIoI%2Fimage.png?alt=media&#x26;token=276602fe-1590-4656-b138-2f1e97e0f902" alt=""><figcaption></figcaption></figure>

### Open UiPath Assistant

Open UiPath Assistant and navigax\`te to User Profile > Preferences > Orchestrator Settings.

In the Connection Type dropdown, select ‘Machine Key’ and then in the Orchestrator URL field enter your organisation's on prem orchestrator URL.

Then click to 'Connect'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFjIoL6wkYVAuQXu0AnSM%2Fimage.png?alt=media&#x26;token=ee164ab0-10ed-4ced-85f8-731fcfe7851b" alt=""><figcaption></figcaption></figure>

Once you are signed in, the Status will now be showing as Connected.

### Open UiPath Orchestrator

Now you need to make sure to check that your machine shows up in&#x20;

Orchestrator. To do this, go back to UiPath Orchestrator and then click on Tenant and Machines.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3DBHiihhHmXHHHJ5CS3M%2Fimage.png?alt=media&#x26;token=634fc484-fffe-466f-b0e6-a1c7e986c9d4" alt=""><figcaption></figcaption></figure>

### Select a Folder

Now you need to select a modern folder to assign a robot account to, to assign a machine to and to create an automation process in.

To select a folder, click on Tenant and then click on the Folders tab.&#x20;

Create a new folder by selecting the New Folder icon.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FiZZLP07lYmRyyawTAkqG%2Fimage.png?alt=media&#x26;token=b9a635e0-1f6b-475b-86fb-3354f26f1f6b" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQzaZIDXD62B7g8aQfcHG%2Fimage.png?alt=media&#x26;token=75b87fc7-f57e-4174-a2dd-944ccf624eff" alt=""><figcaption></figcaption></figure>

### Create a Robot account

The next step is to create a Robot account. You can do this by navigating to Tenant -> Users -> Add Local User

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FadiSgaHvknLcMBv9Qq3I%2Fimage.png?alt=media&#x26;token=cad20f0d-02a5-42c8-b49c-901cb21be455" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8S4cimJJFH4t4yylS8dr%2Fimage.png?alt=media&#x26;token=6f808311-c193-4600-8931-d7467c760c7c" alt=""><figcaption></figcaption></figure>

Click on ‘Unattended Robot’ section on the left side, make sure to enable the toggle ‘Automatically create an unattended robot for this user’ and enter domain\username and password of the account under which this robot runs and click Add.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNUEJCGmyVXj0rUqhj6er%2Fimage.png?alt=media&#x26;token=45ec6b6a-9158-4cf3-819c-162b3c022c7d" alt=""><figcaption></figcaption></figure>

#### Assign roles

Now we need to assign roles to the robot account. To do this, click on the folder which we created, and then go to Users --> Settings --> Manage access --> Assign Account/Group.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8z9czJ5LNxcl2ZlAwjkI%2Fimage.png?alt=media&#x26;token=86a47d30-5cc2-47f2-8bfd-650ba77ccf8a" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqCATQeb8DrJIEuuyRvyC%2Fimage.png?alt=media&#x26;token=d8a5ec17-2853-4f98-b8a7-3b3915b86cba" alt=""><figcaption></figcaption></figure>

Search for the robot account we just added and select it from the drop down. Then add a 'Robot' role to the robot account and click on 'Assign'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FV3gfflBlqDcgC2GCFQ56%2Fimage.png?alt=media&#x26;token=3170f1af-23ab-4341-a756-6cc003112670" alt=""><figcaption></figcaption></figure>

Once you have done this, the robot account will appear in the modern folder with its roles.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FpQs3qhy0BtVib22wxvVx%2Fimage.png?alt=media&#x26;token=0c05eec3-ad15-4414-b47d-e092b90c1feb" alt=""><figcaption></figcaption></figure>

### Assign Machine to the modern folder

You now need to assign a local machine to the folder. Browse to the modern folder created in previous step, navigate to Home -> Machines

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Ft2XAmwNUiHvY8n2FcFsh%2Fimage.png?alt=media&#x26;token=422a8c5b-5c76-4dd9-848e-d2d448c6704e" alt=""><figcaption></figcaption></figure>

Click “Manage Machine in Folder”

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fgi4Tf9N00kFb8cWBJhbt%2Fimage.png?alt=media&#x26;token=c6615e4d-0821-495e-9121-858be127488c" alt=""><figcaption></figcaption></figure>

Search for machine created in previous step, select and click Update

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnpszxGydEGDpW6oHEax4%2Fimage.png?alt=media&#x26;token=063ef89a-2cd9-4548-a454-cce5162ddccf" alt=""><figcaption></figcaption></figure>

Now the local machine will show in the modern folder under the Machines tab.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FuH7UZnUzArP2q2O4z1zm%2Fimage.png?alt=media&#x26;token=7f6dcfee-e880-41e7-ac46-147cee977ec4" alt=""><figcaption></figcaption></figure>

### Check Bot and Bot Environment Synced

And now when we go to the Robots section (under User Management) in Enate, you can see that the robot you've just created in UiPath Orchestrator is showing in Enate.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FYyyDMhCG59n5EYUJWOOt%2Fimage.png?alt=media\&token=5a167ccb-f25e-429b-9ec4-d995750697db)

### Publish the Project in your Machine

The next step is to publish the the UiPath project in your local machine. To do this, go to UiPath Studio, select the desired UiPath project that Enate will trigger based on Action configuration and click 'Publish'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFTThS7XCNjIRzuobYClx%2Fimage.png?alt=media&#x26;token=df7a531d-6583-4318-a04b-106d4eaebdf5" alt=""><figcaption></figcaption></figure>

And then in Package Name enter the name of project you are wanting to publish and click Next.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FN93xGR6X8lvRmT42lRzK%2Fimage.png?alt=media&#x26;token=f21f42f2-3ec0-4c20-ab6c-3c4fae057c09" alt=""><figcaption></figcaption></figure>

Then for the Custom URL click the folder icon and select the folder where you want to save the package and then select 'Publish'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1eKtMpGP3XZeB3hs5CXe%2Fimage.png?alt=media&#x26;token=73db1453-7960-471f-99f1-2a554362068f" alt=""><figcaption></figcaption></figure>

### Upload Package to UiPath Orchestrator

Once the package is published you need to upload it to UiPath Orchestrator. To do this, go to Tenant, select the Packages tab and then click on Upload.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFwSUArL5Oj58UEQ8OWPB%2Fimage.png?alt=media&#x26;token=c884092e-24d3-4471-be4b-162586e90f65" alt=""><figcaption></figcaption></figure>

In the resulting pop-up, select the published package from the local folder you have just saved it to and click Upload.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaFcBjju4XEpVgF15yAtE%2Fimage.png?alt=media&#x26;token=fb3a50a0-700d-40ea-b948-0d64015bef74" alt=""><figcaption></figcaption></figure>

The recently uploaded package should now be visible in the Packages tab.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FYWVmVoZXyjPZKEybn2Um%2Fimage.png?alt=media&#x26;token=0d7b8fe8-6692-458e-bddc-99ec4e786958" alt=""><figcaption></figcaption></figure>

### Create a Process Using the Package

The next step is to create a process using the package you have just published in the previous step.

To do this, navigate to the desired modern folder and then click Automations > Processes > Add Process

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FpvTbGbe0nIElovcvboHB%2Fimage.png?alt=media&#x26;token=68ca8ae2-8bfb-440b-8da6-e31ebe90db77" alt=""><figcaption></figcaption></figure>

Select the package that was just published in the previous step and click Continue.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPlpcOA9hW1m1d9bmB2Xo%2Fimage.png?alt=media&#x26;token=914ab7eb-1001-4a7a-b63a-699754b78893" alt=""><figcaption></figcaption></figure>

Add a Display name and a description if you want and then click Create.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FkMEMIBaUylU97tujWfsC%2Fimage.png?alt=media&#x26;token=8e97c72a-f4c5-432e-9eb1-98c1a8e46e35" alt=""><figcaption></figcaption></figure>

Then click on the play button to start the job manually from on prem Orchestrator:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSd5EBV3WDrcH2RKzq3Tq%2Fimage.png?alt=media&#x26;token=7b19405a-2f6f-441f-a9a5-8118d73e7d00" alt=""><figcaption></figcaption></figure>

In the following screen, enter the same robot account, local machine and hostname as selected in the above steps and click Start.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FAD3dD8j0Fgd8W60su8X0%2Fimage.png?alt=media&#x26;token=4d6db12e-9f15-4a02-ad37-2abc1be9d909" alt=""><figcaption></figcaption></figure>

In the Jobs tab you can see that the job is now running.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjliSV9ZC1tvyuGsabePS%2Fimage.png?alt=media&#x26;token=7afa8825-df2b-4efc-947a-707e42956b21" alt=""><figcaption></figcaption></figure>

And you can see when the job is completed.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FYawyKSL4vo00arfgbiw0%2Fimage.png?alt=media&#x26;token=68981fbf-2d61-4d06-98f0-a63a64581a25" alt=""><figcaption></figcaption></figure>

Back in Enate, click to edit the robot that got synced:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4cDaGueLE5EBO4fp6JJS%2Fimage.png?alt=media\&token=ee5a603d-a9a8-4f34-bb02-dc88e3451166)

And then click to edit the Bot Farm.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6Ii44EInYbCVHt0kGCl9%2Fimage.png?alt=media&#x26;token=20dbe9f1-3e6d-4359-9afc-1685aaf9bbcf" alt=""><figcaption></figcaption></figure>

Here you need to click on the Integration Process dropdown and select the job you want the Bot Farm to perform:&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXYQLQiaqTM0iuTbVtKIQ%2Fimage.png?alt=media&#x26;token=66d92c96-00be-4462-bd7f-253a73ba5fce" alt=""><figcaption></figcaption></figure>

We now need to configure an Action that can be performed by the bot. To do this we need configure the Bot Farm (from Orchestrator) in an Action's General Settings.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FSv24wIT3Q5MmMfjKDdaL%2Fimage.png?alt=media&#x26;token=60294c1f-61c8-401f-bdcc-a34e12039930" alt=""><figcaption></figcaption></figure>

To do this, select to clone the General Settings of the Action and then add the bot farm that we adding in the integration process. You can add the estimated duration for the bot to complete the action if you want.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fk1meZMbZM3O2TwcBCAU1%2Fimage.png?alt=media&#x26;token=5af3a86a-ac34-483d-9adc-c0235990fdaf" alt=""><figcaption></figcaption></figure>

We then need to adjust the allocation rules for the Action. To do this, select to clone the Allocation rules and then in the Queue field select the desired Queue (we will add the bot to the Queue in the next step).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfOQH3VFOS57cfnxGZgbo%2Fimage.png?alt=media&#x26;token=0ab0481f-170e-4252-ad58-3937e3e1d973" alt=""><figcaption></figcaption></figure>

Set the process live.

### Add bot to Queue

Once the process has been set live, as a Team Leader go to the Queues page, click on edit and then add the robot to the Queue you want it to work from.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FuyKDTGL7gPltISNT2Tp3%2Fimage.png?alt=media&#x26;token=eff77b4f-ac1d-457e-8c54-82ee382e523b" alt=""><figcaption></figcaption></figure>

When the Case process you have just configured gets launched in Enate Work Manager, and when the Action we have just configured gets created, the integration process will be triggered.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0yqtKE4xCdOC7JcltcTI%2Fimage.png?alt=media&#x26;token=c9767439-34f0-4886-88fc-e1278deed83a" alt=""><figcaption></figcaption></figure>

When the Action is created and pushed to a Queue that has the desired deep-integrated robot, it sends a message to UiPath Orchestrator to get a job ready for the selected integration process for the selected robot.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FWak3c3OegqBPCmZr3OeN%2Fimage.png?alt=media&#x26;token=281ec7f7-9ada-4094-b30d-92742fb419ce" alt=""><figcaption></figcaption></figure>

You will be able to see when the job triggered from Enate has completed successfully.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1Z7V6NvDAFPw12dOZChs%2Fimage.png?alt=media&#x26;token=ec3112ad-5dce-426e-9429-32976b8de5ec" alt=""><figcaption></figcaption></figure>
