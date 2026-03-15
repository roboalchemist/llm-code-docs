# Source: https://docs.instabug.com/product-guides-and-integrations/integrations/azure-devops.md

# Azure DevOps

{% hint style="info" %}
We only support one-way sync integration with Azure DevOps — changing statuses or assignees on Azure DevOps won't reflect on Luciq.
{% endhint %}

Forward your bug reports to your Azure DevOps workspace by following these simple steps.

{% stepper %}
{% step %}

#### Navigate to Integrations

Open Luciq's Settings and go to the Integrations page. Click *Create* on the Azure DevOps integration.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FXJCpn5p42pxJMU7lmicL%2Fimage.png?alt=media&#x26;token=857fb1af-2a7f-4474-bc1c-677e2245cece" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Fill integration form

In the integration form, you'll need to provide:

* PAT Token
* Organization URL

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FfcUgds0FBqb9OkIQWZQL%2Fimage.png?alt=media&#x26;token=5d884d91-c452-4411-87d1-a871e05b258d" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Create a PAT Token (Personal Access Token)

To create a new PAT Token in Azure DevOps:

* Head over to Azure DevOps.
* Click on User Settings from the menu.
* Choose "Personal Access Token", or navigate to this URL:\
  <https://dev.azure.com/{ORGANIZATION}/\\_usersSettings/tokens>

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FHUsIM2QgRlKA0vTvUdqa%2Fimage.png?alt=media&#x26;token=50f21615-b76e-4053-8c07-a6c5127aee44" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Configure the token

Click on New Token, ensuring the new token has either full access or read-and-write access to work items.
{% endstep %}

{% step %}

#### Enter credentials in Luciq

Fill in your PAT Token and Organization URL in the integration form.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FeqcEaTrlLOHUPZSNkyAV%2Fimage.png?alt=media&#x26;token=0e539143-9525-4ca6-a73a-475b6d18181e" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Test and create

Test the connection and create your integration.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FLHh68ZQMJciuNpAJLL7V%2Fimage.png?alt=media&#x26;token=766dd278-9e58-4610-bd16-991198f7190f" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Configure forwarding and rules

From the final page you can:

* Choose automatic forwarding of all bug reports or forward manually.
* Set Rules & Alerts based on conditions before forwarding.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F1Uhk4kzIHOfchy2HTLB0%2Fimage.png?alt=media&#x26;token=2eb7f45d-d5ce-4d66-8039-9a1e4637610d" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}
