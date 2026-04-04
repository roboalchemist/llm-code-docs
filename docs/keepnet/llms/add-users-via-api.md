# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/2.-add-target-users/add-users-via-api.md

# Add Users via API

Using the platform's APIs, target users may be effortlessly migrated. The API endpoints that are required are detailed below.

{% hint style="info" %}
Use your own domain if you are using an on-premise version. e.g. <https://api.PLATFORM\\_DOMAIN/docs/index.html>
{% endhint %}

**Instructions for adding target users using an API**

<mark style="color:green;">**POST**</mark> **​/api​/target-users**

* Go to the Swagger [link](https://api.keepnetlabs.com/docs/index.html).
* Click the **Authorize** button on the top right side of the page.
* Complete the authorization step with the **Client ID** and **Client Secret** key that you created on the platform.
* Make sure that the **api1** option is checked (✓) on the **Scopes** section.
* Then use this endpoint to add a **new target user** to the platform.

{% hint style="info" %}
The most up-to-date format of the body content that you need to use for requesting an API is available on the Swagger interface.
{% endhint %}

**Searching for a user using API**

<mark style="color:green;">**POST**</mark> **​/api​/target-users​/search**

* Go to the Swagger [link](https://api.keepnetlabs.com/docs/index.html).
* Click the **Authorize** button on the top right side of the page.
* Complete the authorization step with the **Client ID** and **Client Secret** key that you created on the platform.
* Make sure that the **api1** option is checked (✓) on the **Scopes** section.
* Then use this endpoint to **search for a target user** on the platform.

{% hint style="info" %}
The most up-to-date format of the body content that you need to use for requesting an API is available on the Swagger interface.
{% endhint %}

**Editing Target Users using API**

<mark style="color:orange;">**PUT**</mark> **​/api​/target-users​/{resourceId}**

* Go to the Swagger [link](https://api.keepnetlabs.com/docs/index.html).
* Click the **Authorize** button on the top right side of the page.
* Complete the authorization step with the **Client ID** and **Client Secret** key that you created on the platform.
* Make sure that the **api1** option is checked (✓) on the **Scopes** section.
* Then use this endpoint to **edit a target user** on the platform.

{% hint style="info" %}
The most up-to-date format of the body content that you need to use for requesting an API is available on the Swagger interface.
{% endhint %}

​✅ **You have now added your first Target Users. Now you need to** [**ensure they are able to receive emails from Keepnet**](https://github.com/ucarozan/keepnet-docs/blob/main/next-generation-product/getting-started/3.-email-deliverability) **successfully ➡️**

### Video Tutorial <a href="#video-tutorial" id="video-tutorial"></a>

{% embed url="<https://youtu.be/S0nN_uE8NjQ>" %}
