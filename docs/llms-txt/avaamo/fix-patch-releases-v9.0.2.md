# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.0.0/fix-patch-releases-v9.0.2.md

# Fix patch releases (v9.0.2)

This article summarizes a list of fix patch releases made in the Avaamo Conversational AI Platform version 9.0.2. The following are some of the key fixes included in this release:

1. [JS errors page: Improved error classification](#js-errors-page-improved-error-classification)
2. [Response handling: Long responses with a disclaimer note](#response-handling-long-responses-with-a-disclaimer-note)
3. [Deprecation – Tag.append](#deprecation-tag.append)

### JS errors page: Improved error classification <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5G4dZl6W7WdeTEQQ8SS6%2FDevelooper%20(2).png?alt=media&#x26;token=ea7bca24-5434-4214-a811-d956d8b3b000" alt="" data-size="line">

* A new **“Type” column** is available in the **JS Errors page** to indicate whether it is an **Error** or a **Warning**.
* This enhancement enables developers to quickly assess the severity and nature of JavaScript issues, facilitating faster debugging and resolution.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FVlPZxMg0XNAu5K411pHx%2FScreenshot%202025-08-25%20at%201.21.55%E2%80%AFPM.png?alt=media&#x26;token=897b71e7-1e64-487c-8b49-5f04733cfa65" alt=""><figcaption></figcaption></figure>

Refer [JS errors](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/js-errors), for more information.

### Response handling: Long responses with a disclaimer note <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXenTTa48f7IueKXbyuzg%2FDevelooper%20(3).png?alt=media&#x26;token=74d895d6-211d-48d4-8cb6-2e518090b9a4" alt="" data-size="line">

* For very long responses, the agent now displays a **disclaimer message** at the end.
* This disclaimer appears only when the **Markdown format** is enabled in the channel. Refer [Enable Markdown Format](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/advanced#enable-markdown-format), for more information.
* This update ensures source citation links are retained even in lengthy responses, addressing the earlier issue of them being hidden.

{% hint style="info" %}
**Note:**&#x20;

* The note message can be `customized` or `disabled` by requesting Avaamo support.
  {% endhint %}

Example of how the disclaimer note is displayed at the end of a long response:

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FQhVsi07XnfCuHrnQQ1rx%2FScreenshot%202025-07-29%20at%204.14.00%E2%80%AFPM.png?alt=media&#x26;token=c6dbbf8e-3164-447e-9105-5cadb03dc04e" alt="" width="375"><figcaption></figcaption></figure></div>

### Deprecation – `Tag.append` <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FulOJh0IsFwIUTUCppSv1%2FDevelooper%20(2).png?alt=media&#x26;token=c4c49596-8bb0-40d8-8f85-8f7aebcff026" alt="" data-size="line">

* The `Tag.append` method is now **deprecated**. This method must be called within an `async` block, which limits its usage.
* Developers should use **`Tag.asyncAppend`**, that can be applied universally without requiring an `async` block. This method provides greater flexibility and simplifies implementation.

Refer [Add tags (JS)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/add-tags-js), for more information.
