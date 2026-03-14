# Source: https://doc.keepnetlabs.com/next-generation-product/platform/phishing-reporter/phishing-reporter-deployment/how-to-deploy-the-add-in-in-exchange-admin-center.md

# How to Deploy the Add-in in Exchange Admin Center

## Requirements

In order to use the Phishing Reporter add-in in the Exchange environment, your platform must meet the following requirements.

* Exchange 2013 - version (15.0.847.32) or above
* Exchange 2016 - version (15.1.225.42) or above
* Exchange 2019

## Deploy Add-in

To deploy the Phishing Reporter add-in, follow the steps below.

* Log in to the Microsoft 365 Admin interface.
* Go to **Microsoft 365 Admin Center > Settings > Integrated Apps > Add-ins**.
  * If you have Exchange 2013 or a different Exchange Admin interface, you can try **Exchange** **Admin Center > Organization > Apps.** You may also search the 'add-ins' word to find the related place.
* Click the **(+)** button and select **Add** **from** **file**. Install the Phishing Reporter .xml file that you previously downloaded and click **Next**.
* Make sure that these options are selected:
  * Make this add-in available to users in your organization
  * Mandatory is always enabled
  * Users can't disable this add-in.
* Click **Save** to complete the process.

{% hint style="warning" %}
It may take up to 12 hours for the add-in to be displayed on users' email applications. Users may need to relaunch their email applications.
{% endhint %}

## Uninstall the Add-in

To uninstall the Phishing Reporter add-in from Exchange Admin Center user accounts, follow these steps:

* Log in to the Microsoft 365 Admin Center.
* Go to **Microsoft 365 Admin Center > Settings > Integrated Apps > Add-ins**.
  * If you have Exchange 2013 or a different Exchange Admin interface, you can try **Exchange Admin Center > Organization > Apps**. You may also search the 'add-ins' word to find the related place.
* Click the add-in you want to uninstall.
* Click the **trash** **bin** **icon** and then click **Yes** to complete the process.

{% hint style="warning" %}
It may take up to 12 hours for the add-in to be uninstalled. Users may need to relaunch email applications.​
{% endhint %}

## Video Tutorial

{% embed url="<https://youtu.be/92sH456BJQ0>" %}
