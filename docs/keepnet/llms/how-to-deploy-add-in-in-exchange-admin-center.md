# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/6.-setup-phishing-reporter/deploy-keepnets-customisable-phishing-report-button/step-2.-deploy-phishing-reporter/how-to-deploy-add-in-in-exchange-admin-center.md

# How to Deploy Add-In in Exchange Admin Center

## Requirements

In order to use the Phishing Reporter add-in in the Exchange environment, your platform must meet the following requirements.

* Exchange 2013 - version (15.0.847.32) or above
* Exchange 2016 - version (15.1.225.42) or above
* Exchange 2019

## Deploy Add-in

To deploy the Phishing Reporter add-in, follow the steps below.

* Log in to the Exchange Admin interface.
* Go to **Exchange Admin Center > Organization > Add-ins (called Apps in some versions)**
* Click the **(+)** button and select **Add** **from** **file**. Install the Phishing Reporter .xml file that you previously downloaded and click **Next**.
* Make sure that these options are selected:
  * Make this add-in available to users in your organization
  * Mandatory is always enabled
  * Users can't disable this add-in.
* Click **Save** to complete the process.

{% hint style="warning" %}
It may take up to 12 hours for the add-in to be displayed on users' email applications. Users may need to relaunch their email applications.
{% endhint %}

✅ **You have now deployed the Phishing Reporter. Next step is to** [**Setup Incident Responder**](https://github.com/ucarozan/keepnet-docs/blob/main/next-generation-product/getting-started/7.-incident-responder-setup) **(only for customers who have purchased the Incident Responder or SOC package)**

## Video Tutorial

{% embed url="<https://youtu.be/92sH456BJQ0>" %}
