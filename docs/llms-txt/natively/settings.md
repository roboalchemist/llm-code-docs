# Source: https://docs.buildnatively.com/natively-platform/settings.md

# Settings

## General App Info

### App Name

The name of your application. Will be displayed on a device.

### App Url

The URL of your website that runs inside of your application.

{% hint style="info" %}
If your app is password protected (and it's not displayed in the app), please use the following formatting for your URL\
https\://{username}:{password}@yourwebsiteurl.com (example: <https://roman:123456@yourwebsiteurl.com>)
{% endhint %}

### External App Schemes

These app schemes will allow to open external apps from yours. \
Write the scheme in the input and click the 'Add' button.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FTdJktCxGbsOVoOnQoXn3%2Fexternal_app_scheme.png?alt=media&#x26;token=8b7d06a8-0233-472b-8b46-6a6cc5e851cb" alt=""><figcaption></figcaption></figure>

### Internal URLs

Keep trusted third-party domains (like your own Help Center) inside your app’s primary view. This removes the "browser" UI (navigation bars) and makes external content feel like a native part of your app.

By default, Natively will open external domains in an In-App Browser to protect the user's session. However, you can force specific external URLs to open within your app’s primary view (without the navigation bar or "Close" ison) by using the whitelist.

How to whitelist a domain:

1. Navigate to your Natively Dashboard.
2. Go to Settings.
3. Locate the Internal URLs section.
4. Add the domains you want to keep internal (e.g., `*.example.com`).

When to use this:

* If your app logic spans multiple subdomains (e.g., `app.example.com` and `auth.example.com`).
* If you use a third-party service that must stay within your app context.

Examples:

* \*.example.com matches app.example.com
* example.\*.com matches example.dev.com
* *\*.\**.example.com matches api.dev.example.com

\
Write the URL/Domain in the input and click the 'Add' button.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FcgBeDw3sc6YvyPd7T0gw%2Finternal_urls.png?alt=media&#x26;token=cad5fc96-bef7-4d73-9268-7e5ae02b6c89" alt=""><figcaption></figcaption></figure>

## iPad support \[Only for iOS]

* Select devices that you want to be supported
* iPhone, iPad or both
* **Android** tablets are supported by default

{% hint style="info" %}
If your previously submitted version included iPad support, it's crucial to keep this setting consistent in subsequent builds.
{% endhint %}

## Reload WebView \[Advanced]

Reload the WebView after a period in the background or screen lock, or manually trigger a reload.

1. Enable the feature, set time interval (seconds), save, and rebuild.
2. Manual reload:

&#x20;      2.1. Bubble: "Natively - Reload WebView" action.&#x20;

&#x20;      2.2. JS SDK: window\.natively.reloadWebview();
