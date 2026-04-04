# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/example-how-to-set-up-a-bot-status-monitor-in-power-automate.md

# Set up a Bot status monitor in Power Automate

## Introduction

This guide will outline the steps involved in configuring a Bot Status monitor in Power Automate. With this flow correctly set up, an email will be automatically generated notifying you of when any of your Bots working in Enate go offline.

## Prerequisites :

* Microsoft Power Automate licensed version.
* Enate instance URL
* Username and password for that instance (user must have Team Leader access)
* RobotFarmGUID (thst you want to receive notifications from). Select GUID from tblRobotFarms where Name = 'Enter-BotFarm-Name'
* Email address of people whom you want to be notified

## **Step 1 : Configure Office 365 Outlook Connector in Power Automate.**

1. Go to Power Automate dashboard ( <https://emea.flow.microsoft.com/> )
2. On left menu bar go to ‘Data’ > ‘Connections’.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8GxrKeqSShVTs0v%2F2.png?generation=1625501505412919\&alt=media)

3\. Click on ‘New Connection’.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8GxrKeqSShVTs0v%2F2.png?generation=1625501505412919\&alt=media)

4\. Choose ‘Office 365 Outlook’

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8Gyrfi6cml2TvIv%2F3.png?generation=1625501505425550\&alt=media)

5\. Click on ‘Create’.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8GzfVxzSmtK67MK%2F4.png?generation=1625501505401507\&alt=media)

6\. Choose a user account and complete the authentication process.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H-JMT0xG-cPijW%2F5.png?generation=1625501505427566\&alt=media)

## **Step 2 : Importing the flow**

1\. Choose the ‘My Flows’ option from the left side menu bar on the dashboard and click on ‘Import’.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H0cctL1iRy3iOn%2F6.png?generation=1625501505395706\&alt=media)

2\. Download the .zip file of the from here:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-Mdw-AG3bn0EJalDr-j-%2F-Mdw07ydztTZ0R3joUYg%2FBot_Status_Monitor.zip?alt=media&token=37fe07bb-e0e3-45a0-8e98-b9493c915cf7>" %}
Bot Status Monitor.zip
{% endfile %}

3\. Upload the provided .zip file into Power Automate.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H1ltNWdrmL3p8s%2F7.png?generation=1625501505394246\&alt=media)

4\. After it has uploaded successfully, click on the ‘Update’ option

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H2iRzzbRFfgEwK%2F8.png?generation=1625501505403322\&alt=media)

5\. Select the ‘Create as new’ option from the dropdown and click on ‘Save’.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H3uylHheB2CTBq%2F9.png?generation=1625501505408060\&alt=media)

6\. Click ‘Select during import’ under Import Setup in the Related Resources field.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H4OHVS9Nq-n_sg%2F10.png?generation=1625501505398505\&alt=media)

7\. Select email account that you connected in step 1 and click on ‘Save, then ‘Import’.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H51de8JKDM7ZuY%2F11.png?generation=1625501505420858\&alt=media)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H6MIyXgKBiXh_1%2F12.png?generation=1625501505398242\&alt=media)

8\. After a successful import, your screen should look like this:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H70MjqbtzMtuBu%2F13.png?generation=1625501505398814\&alt=media)

## **Step 3: Configure Flow**

1\. Go to the ‘My Flows’ option from the left side menu bar on the dashboard. This will show you your Imported project. Then click on the edit button.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H8WLF56KKwQWCj%2F14.png?generation=1625501505392267\&alt=media)

2\. Click on ‘Variable to be initialized’

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8H90p6zIMWxKD14%2F15.png?generation=1625501505398344\&alt=media)

3\. You can then choose which fields to initialize:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8HARt1SKnrOQ-XQ%2F16.png?generation=1625501505393438\&alt=media)

Details of how to initialize the various fields:

1\. **URL**: Enter enate instance URL: Ex: => <https://enate.community/XYZ>

{% hint style="info" %}
N.B. Do not use speech marks ‘/’
{% endhint %}

2\. User Name and Password: Enter the credentials for your chosen URL.

3\. RobotFarmGUID: your can get this from the database. Select GUID from tblRobotFarms where Name = 'Enter-BotFarm-Name'.

&#x20;4\. Email Subject and Header: Enter your Email Subject and header for the notification Email.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8HBOO0mtxnb5bmK%2F17.png?generation=1625501505411984\&alt=media)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8HCxYdHHFGZUei3%2F18.png?generation=1625501505425613\&alt=media)

5\. To Email Addresses: enter the Email addresses which you want to send the notification to, separateing each email address with a semicolon ‘;’ Ex. [deval.example@enate.net;abc@enate.net;xyz@enate.net](mailto:deval.chawda@enate.net;abc@enate.net;xyz@enate.net)

{% hint style="info" %}
Note: Do not use email of people outside of your organization.
{% endhint %}

Click on ‘Save’ and a green confirmation message will appear.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8HDjgbApfEj6eEa%2F19.png?generation=1625501505396925\&alt=media)

6\. Once the green confirmation message has appeared, go back and click ‘Turn on’ to switch on the flow.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8HE2SyRtG4UdQDF%2F20.png?generation=1625501505430674\&alt=media)

This will make the yellow header disappear, telling you that the flow is up and running.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fenate-help%2F-MdrQrg3pU6P6zOSE9SU%2F-MdrR8HFKrEbOfANUwXT%2F21.png?generation=1625501505395416\&alt=media)

Now the flow is running, you should get an email notifying you of every time one of your Bots working in Enate goes offline.

## How to integrate with Power Automate

Check out our Power Automate section for more information about how to integrate it with Enate here:

{% content-ref url="power-automate" %}
[power-automate](https://docs.enate.net/enate-help/integrations/enate-integrations/power-automate)
{% endcontent-ref %}
