# Source: https://developers.make.com/custom-apps-documentation/best-practices/modules/module-types.md

# Module types

## Module types <a href="#module-types" id="module-types"></a>

Modules should be associated with the correct type depending on their functionality.

Detailed descriptions of different types of modules can be found in our [modules](https://developers.make.com/custom-apps-documentation/app-components/modules) documentation as well as in the [best practices guide to module descriptions](https://developers.make.com/custom-apps-documentation/best-practices/naming-conventions/modules/module-descriptions).

{% tabs %}
{% tab title="Incorrect" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-1cef3549c32ceca351911f5db00a236be51edec5%2Fincorrect_moduletype.png?alt=media" alt="" width="196"></div>

{% hint style="info" %}
The List campaigns module in this example is incorrectly identified as an Action module.
{% endhint %}
{% endtab %}

{% tab title="Correct" %}

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-612181a228666ef1b4e5baddc498218df26ccf0f%2Fcorrect_moduletype.png?alt=media" alt="" width="196"></div>

{% hint style="info" %}
The List campaigns module in this example is correctly identified as a Search module.
{% endhint %}
{% endtab %}
{% endtabs %}

## Universal modules

Each app should have a universal module. This module allows users to use API endpoints that are not supported, using their connection created to the app.

More about universal modules can be found in our [modules](https://developers.make.com/custom-apps-documentation/app-components/modules/universal-module) documentation.

Make sure the universal module has the:

* correct label and description,
* correct `url` which starts with the [base URL](https://developers.make.com/custom-apps-documentation/app-components/base/base-url), and
* correct connection.
