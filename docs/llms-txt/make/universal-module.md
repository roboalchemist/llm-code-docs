# Source: https://developers.make.com/custom-apps-documentation/app-components/modules/universal-module.md

# Universal

A universal module can be used to perform an arbitrary API call to the service's API. It allows the user to specify all parameters of the request while using the app's connection.

Every app using API should have a universal module. An app can have only one universal module.

{% hint style="warning" %}
**Security notice**

As the universal module allows the user to specify the target URL, it's **highly important** that the universal module has to use a **relative path**. Otherwise, a user could point the request to their own custom servers and get access to the access tokens.

**A universal module that doesn't match this condition won't be approved by Make to be used in scenarios.**
{% endhint %}

There are two types of universal modules. Choose one depending on the API you use:

* [REST API](https://developers.make.com/custom-apps-documentation/app-components/modules/universal-module/rest)
* [GraphQL API](https://developers.make.com/custom-apps-documentation/app-components/modules/universal-module/graphql)

## Components

Components of the universal module are the same as for the [action module](https://developers.make.com/custom-apps-documentation/app-components/action#components)**.**

## Available IML variables

You can use all of the IML variables available for [action modules](https://developers.make.com/custom-apps-documentation/app-components/action/components#available-iml-variables) in the universal module, except for the `iterate` directive.

## Universal module in a scenario

When a universal module is used in a scenario, it is recommended to use it together with a **JSON > Create JSON** module. Not only it is much easier to create the structure of JSON for the universal, but also all characters, which are part of JSON definition and should be considered as letters, are escaped.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-4487d31c5d219e14d5181906073866f31c057627%2Funiversalmodule_json.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
