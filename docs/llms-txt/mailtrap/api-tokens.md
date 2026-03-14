# Source: https://docs.mailtrap.io/developers/account-management/api-tokens.md

# Source: https://docs.mailtrap.io/email-sandbox/setup/api-tokens.md

# Source: https://docs.mailtrap.io/email-api-smtp/setup/api-tokens.md

# API Tokens

#### Add and manage tokens manually

{% stepper %}
{% step %}
Navigate to **Settings** in the menu on the left and select **API Tokens**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dfe523503ba601dfe5dcc1648b09fcede7bc5112%2Fapi-tokens-add-token.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
To add a new token, click the **Add Token** button in the upper right corner.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-dfe523503ba601dfe5dcc1648b09fcede7bc5112%2Fapi-tokens-add-token.png?alt=media" alt="" width="563"></div>
{% endstep %}

{% step %}
**Type the token name** into the designated field.&#x20;

It’s perfectly fine to have a custom name for the API token, as it’s only for your reference, regardless of the use case.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FlpA9pLUncYMLdgSmAeKK%2FScreenshot%202025-12-16%20at%2016.19.22.png?alt=media&#x26;token=db12e0a4-70a9-4c7e-ba86-03015e19afdd" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Assign permissions** by checking the boxes in the corresponding access level columns. Note that you must have admin permissions on a particular domain to send emails with this token.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-aad9698d90812d10b8afa0226ddf5fcafd66d19f%2Fapi-tokens-permissions-editor.png?alt=media" alt="" width="375"></div>
{% endstep %}

{% step %}
Click the **Save** button and preview the new token under the **API Tokens** main menu.

<figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FbJoeiyZ94WGz0p0AdGh3%2FScreenshot%202025-12-16%20at%2016.20.39.png?alt=media&#x26;token=f400948a-2bd0-4232-bc85-5d9d61e23475" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

#### Auto-created token per domain

When you create a domain, a token is automatically created and named based on the following formula: \[domain name] + \[token] + \[token ID].

For example, if you add the example.com domain, the token for that domain will be named example.com token 1234. By default, the automatically generated token gets Domain Admin Mailtrap for the given domain.

{% hint style="info" %}
You need to edit permissions for the automatically generated token to allow for authorization on other domains.
{% endhint %}

### Where to find tokens?

Select **Settings** in the left menu, then API Tokens. You’ll see all active tokens, their creator, and their access level.&#x20;

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2FIjRHg8ZYMhuIFtktQHkC%2Fimage.png?alt=media&#x26;token=7596f750-f75e-4e47-a126-99a9c5d30615" alt="" width="563"><figcaption></figcaption></figure></div>

The automatically assigned token per domain is under the Integration tab in Sending Domains. Choose the desired stream, click Integrate, and toggle the switch to API. You'll see the endpoint (Host) and your API Token.

### Reset token

Go to **Settings** > **API Tokens**, click the three-dot menu icon next to the token you want to reset, and click **Reset API Token**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3762cde4a3322e8764196f336b594df6f4ec68c5%2Fapi-tokens-reset-menu-option.png?alt=media" alt="" width="563"></div>

Confirm your choice by clicking on the corresponding button.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-25e07ca7578551e8334f73700b5026fa96047780%2Fapi-tokens-reset-confirmation.png?alt=media" alt="" width="563"></div>

{% hint style="success" %}
**Tip:** The three-dot menu icon next to the token also allows you to copy a token to your clipboard.
{% endhint %}

{% hint style="warning" %}
**Important notes:**

* After clicking the Reset credentials or Reset API Token buttons, the existing token becomes invalid after 12 hours. So, you have a 12-hour window to update all apps that use the old API token. Once the old token expires, some parts of your application will not work properly unless you've updated the token. All expired tokens get deleted from your account within 24 hours after expiration.
* After the API token is reset and expired, a new token is created. The token ID is added to the token name the same way it's done for automatically generated tokens, e.g., mailtrap.example token 4231.
  {% endhint %}

### Edit permissions

As mentioned earlier, click the menu icon at the far right of a token and select **Edit permissions**.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-532af5c8cd0d2effab0678823088ef476173c267%2Fapi-tokens-edit-permissions-option.png?alt=media" alt="" width="563"></div>

Click on the corresponding boxes to add or remove token permissions. Then, confirm your selection with the **Save** button.

### Delete token

To delete a token, click a three-dot menu icon and choose the **Delete** **token** option.

<div align="left" data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-51692fed552abdb850f55a54a7bca58cbe023465%2Fapi-tokens-delete-menu-option.png?alt=media" alt="" width="563"></div>

Confirm the action by clicking the **Confirm** button.

<div data-with-frame="true"><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-738ea005c1db709ef926c8698ffc7e1a4bbe85b9%2Fapi-tokens-delete-confirmation.png?alt=media" alt=""></div>

{% hint style="warning" %}
**Important:** Keep in mind that a token is deleted immediately, and you can't delete the last token per domain.
{% endhint %}
