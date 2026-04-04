# Source: https://developers.make.com/api-documentation/authentication/create-authentication-token.md

# Creating API token

Make API uses authentication tokens to authenticate requests. You must include your authentication token in the headers of all requests that you send to the API.

Generate and manage API tokens from your profile in the Make interface.

{% hint style="warning" %}
If you have access to multiple Make zones, generate separate tokens for each of them.
{% endhint %}

{% stepper %}
{% step %}
Sign in to Make and click your avatar at the bottom-left corner of the page.
{% endstep %}

{% step %}
Click **Profile**.
{% endstep %}

{% step %}
Open the **API** tab.

![Choose API](https://636730569-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLXp8X1eBwkwrLIWrN9cg%2Fuploads%2Fgit-blob-b7cbaecb7bfc716c4b0a85862f475272ce56432c%2Fintro-steps-1.png?alt=media)
{% endstep %}

{% step %}
Click **Add token**.

![Add token](https://636730569-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FLXp8X1eBwkwrLIWrN9cg%2Fuploads%2Fgit-blob-89842cb56dd532f906d475c25604a2736dbf10d5%2Fintro-steps-2.png?alt=media)
{% endstep %}

{% step %}
In the **Add token** dialog, do the following:

* **Label**: type a custom name for your token that will help you recognize what the token is used for
* **Scopes**: select the scopes you need for working with API resources. For more information about scopes, refer to [Make roles and API scopes](https://developers.make.com/api-documentation/authentication/api-scopes-overview).
  {% endstep %}

{% step %}
Click **Save**.
{% endstep %}
{% endstepper %}

Make generates your token. Copy it and store it in a safe place.

{% hint style="warning" %}
**Do not share your token with anyone!**

Once you leave the **Profile** section, parts of your token will be hidden for security reasons. You won't be able to see or copy your token again.
{% endhint %}

With an active token, you are ready to make API calls. For more details, refer to the [Getting started](https://developers.make.com/api-documentation/getting-started) section.
