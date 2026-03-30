# Source: https://docs.safetycli.com/safety-docs/safety-cli/installation-and-authentication.md

# Installation and Authentication

## Installation

To scan and secure Python projects, you first need Safety CLI version 3 to be installed on your machine.

{% hint style="info" %}
To check whether Safety CLI 3.x is already installed, open your **terminal** and type:

```
safety --version
```

{% endhint %}

If the safety command is not found, **or your safety version is less than 3.0,** you need to install Safety version 3 using the following command before continuing:

```
pip install safety
```

{% hint style="info" %}
If you already have Safety installed, please use `pip install -U safety`&#x20;
{% endhint %}

## Login Methods

When the installation of Safety version 3 has been confirmed, launch your terminal and authenticate using one of the methods outlined below.

### **Free & Team Customers**

Customers on our Free and Team plans will log in using an email and password defined when you [create your account](https://platform.safetycli.com/register/).

In your **terminal,** type:

```
safety auth login
```

Your default browser will open and you will be asked to authenticate using your Safety username and password. Login via Google is currently supported, and support for additional SSO providers will be added soon.

Once logged in, return to your terminal to verify Safety is authenticated with your account details by typing:

```
safety auth
```

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fdyn3a5051wOzizx3ih1L%2Fimage.png?alt=media&#x26;token=c98a997e-6485-49ae-8402-09dae7d045a3" alt="" width="563"><figcaption><p>1. "safety auth" launches the default browser.</p></figcaption></figure>

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2FdH7aZXBqlUI0YOZnwjy1%2Fimage.png?alt=media&#x26;token=c4846462-7f1b-4929-a124-0c2e63c0b2ab" alt="" width="563"><figcaption><p>2. Browser-based Authentication</p></figcaption></figure>

<figure><img src="https://1428014516-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0ABDwXSDJWM5juLdc6ie%2Fuploads%2Fe9czE5VMpu58M2VooZVA%2Fimage.png?alt=media&#x26;token=f3c52d5f-61a3-4866-bcae-1cf1edbe6448" alt="" width="563"><figcaption><p>"safety auth" triggering browser authentication and successful login</p></figcaption></figure>

### **Enterprise Customers**

Enterprise customers can leverage the method described above or SAML-based authentication, allowing users to be authenticated using organization-specific identities. The latter preserves approved authentication flows and prevents access to anyone not registered in your internal identity platform.

As above, when installation has been confirmed, in your **terminal,** type:

```
safety auth login
```

This will open your browser to authenticate the Safety CLI tool using your work email address and password. If your organization uses SAML authentication, you will be redirected to your corporate login page.

Once logged in, return to your terminal to verify Safety is authenticated with your account details by typing:

```
safety auth
```

If you are unclear as to which method your organization uses, please contact your administrator or email us at <support@safetycli.com>.
