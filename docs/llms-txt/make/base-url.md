# Source: https://developers.make.com/custom-apps-documentation/app-components/base/base-url.md

# Source: https://developers.make.com/custom-apps-documentation/best-practices/base/base-url.md

# Base URL

[Base URL](https://developers.make.com/custom-apps-documentation/app-components/base/base-url) is the main URL to a web service that should be used for every module and remote procedure in an app, for example: `https://mywebservice.com/api/v1.`

{% hint style="info" %}
Make sure that the base URL is a **production** **endpoint** with a domain that belongs to the app itself.

Apps with development or staging URLs, or apps with a domain belonging to a cloud computing service, will not be approved.
{% endhint %}

When the service has a different domain for each user, the domain should be requested in the connection and then the value should be used in the Base tab.

## Correct Base URL examples

{% tabs %}
{% tab title="Correct" %}
An example from the Mailerlite app:

```javascript
{
    "baseUrl": "https://api.mailerlite.com/api/v2"
}
```

{% endtab %}

{% tab title="Correct (different domain)" %}
An example from the Freshsales app:

```javascript
{
    "baseUrl": "https://{{connection.domain}}.freshsales.io"
}
```

{% endtab %}
{% endtabs %}

## Incorrect Base URL examples

{% tabs %}
{% tab title="Incorrect (different domain)" %}

```javascript
{
    "baseUrl": "https://mydomain.freshsales.io"
}
```

{% hint style="info" %}
The "mydomain" should be a variable used from the Connection.
{% endhint %}
{% endtab %}

{% tab title="Incorrect (app will not be approved)" %}

```javascript
{
    "baseUrl": "https://mailerlite.heroku.com/development"
}
```

{% endtab %}
{% endtabs %}

## Using the Base URL <a href="#using-the-base-url" id="using-the-base-url"></a>

All of the modules should build on top of the `baseURL` from the Base section (starting with a forward slash `/`). It is very unlikely that a single module will need to have a completely different URL than the rest.

{% tabs %}
{% tab title="Incorrect" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-eec3078b92f7d173af53654ec70c3fbeff9c5c77%2Fbaseurl_incorrect.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The underlined part, which is the same for each module, should be in the Base tab.
{% endhint %}
{% endtab %}

{% tab title="Correct" %}

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-a748a6d69a52772f2ded77b91ed1656fac56fe54%2Fbaseurl_correct.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Modules "url" should start with forward slash `/`
{% endhint %}
{% endtab %}
{% endtabs %}
