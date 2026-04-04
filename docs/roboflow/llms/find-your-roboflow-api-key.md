# Source: https://docs.roboflow.com/developer/authentication/find-your-roboflow-api-key.md

# Find Your Roboflow API Key

**You can find your API Key at** [**app.roboflow.com/settings/api**](https://app.roboflow.com/settings/api)

***

There are two kinds of API key:

* **Private API Keys**: used by Roboflow API and [Roboflow Infernece](https://inference.roboflow.com/)
* **Public / Publishable API Key**: Used by `inference.js` , our JavaScript inference SDK

API keys are scoped to a Workspace, which means you must use the API key associated with a workspace to access that Workspace's private projects.

<figure><img src="https://1284666567-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fe5GEiPeDoFksvZv1vH3A%2Fuploads%2FhibQvL0THiVIE25hgBl4%2Fimage.png?alt=media&#x26;token=8e883d16-32da-4cd2-a560-8245f3e1c6ee" alt=""><figcaption></figcaption></figure>

Click "Generate New Key" to issue a new key, or copy a key you have already created.

{% hint style="success" %}
Be sure to keep your private API key secret. Treat it like a password; it grants the bearer access to your workspace's data and models.
{% endhint %}

If you ever accidentally expose your key to someone who isn't authorized to access your workspace, click "Roll API Key", which will disable previous API key and create a new one.

### Multiple API Keys

Workspaces on Enterprise plans can create multiple API keys, allowing them to isolate environments and instantly revoke access for specific deployments or personnel without disrupting their entire production workflow.

<figure><img src="https://1284666567-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fe5GEiPeDoFksvZv1vH3A%2Fuploads%2FCz7wQYzwIxy5pdC4KiYo%2Fimage.png?alt=media&#x26;token=92b8601b-4d29-4ad5-98cd-b24230ee2c83" alt=""><figcaption><p>Multiple API Key options for Enterprise Workspaces</p></figcaption></figure>

We also offer [scoped-api-keys](https://docs.roboflow.com/developer/authentication/scoped-api-keys "mention") as an Add-on to our Enterprise customers.
