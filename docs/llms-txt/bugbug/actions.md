# Source: https://docs.bugbug.io/editing-tests/actions.md

# Actions

When you [manually add steps](https://docs.bugbug.io/editing-tests/manually-creating-the-test), first you need to choose a type of step.

There are two basic types of steps:

* [Actions](#action-types-available-for-a-step)&#x20;
* [Assertions](https://docs.bugbug.io/editing-tests/assertions)

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHTnnoNv67UWK9C7RRp7B%2Fimage.png?alt=media&#x26;token=6e8b54dd-c8a2-4c17-ad11-ff175146b131" alt=""><figcaption></figcaption></figure>

## Action types available for a step

### [**Mouse actions**](#mouse-actions-details)

* [Click ](#click)
* [Double click](#double-click)
* [Right click](#right-click)
* [Hover](#hover)
* [Scroll](#scroll)
* [Drag\&Drop (BETA)](#drag-and-drop-beta)
* [Press mouse button](#press-mouse-button)
* [Release mouse button](#release-mouse-button)

### [**Input actions**](#input-actions-details)

* [Type text](#type-text)
* [Select option](#select-option)
* [Clear input](#clear-input)
* [Change value](#change-value)
* [Upload file](#upload-file)
* [Paste from clipboard](#paste-from-clipboard)

### [**Window actions**](#window-actions-details)

* [Go to URL](#go-to-url)
* [New tab](#new-tab)
* [Close tab](#close-tab)
* [Reload page](#reload-page)

### [**Advanced actions**](#advanced-actions-details)

* [Set variable](#set-variable)
* [Switch context](#switch-context)
* [Run custom JavaScript](#run-custom-javascript)
* [Answer a prompt](#answer-a-prompt)

## Actions - detailed descriptions & tips

### Mouse actions - details

#### Click

When you want to click a specific element.

This is the most common action for navigating the web. This also serves as a "tap" action if you [test mobile resolutions](https://docs.bugbug.io/workflow-tips/mobile-version-testing).

<div align="left"><figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FNJ8hSuAamUD69ZhPywN4%2Fimage.png?alt=media&#x26;token=abb41b9d-20c2-4b10-97be-e42108bc0a99" alt=""><figcaption><p>Click parameters</p></figcaption></figure></div>

Parameter&#x73;*:*

* *Position (default: Smart detection)* - By default, BugBug utilizes its own mechanism to calculate the correct x,y position for clicking on the given element (selector). If you wish, you can modify this parameter and choose where to click (Top Left, Top Center, Top Right, Left, Center, Right, Bottom Left, Bottom Center, Bottom Right).&#x20;
* *Modifier keys (default: None) -* If you need to click with an extra keyboard modifier, it's possible to set it here (Ctrl, Shift, Alt, Meta / Command).

#### Double click&#x20;

When your app has a specific interaction, such as a double-click, for example, to open a file.

#### Right click

When your app has a custom context menu on right-click.

#### Hover

{% hint style="warning" %}
**Important! This action is not recorded automatically. You need to** [**enter "Hover" mode during the recording**](https://docs.bugbug.io/recording-tests-steps/recording-hover)**.**&#x20;
{% endhint %}

Examples when to use it:

* Navigation bar with menus that appear on mouseover
* Cart preview that appears  on hover
* Actions that only appear when you move your mouse over a table row&#x20;

#### Scroll

When you need to force BugBug to scroll to specific coordinates.

Usually, you don't need to add it manually, because BugBug [handles the scroll automatically](https://docs.bugbug.io/preventing-failed-tests/smart-scroll).

#### Drag\&Drop (BETA)

When your app has a slider that is interacted with by a drag-and-drop interaction.

#### Press mouse button

This action will initiate the `mouseDown` event.

You can use it in combination with "hover" and "Release mouse button" to simulate drag & drop from one element to another element.&#x20;

#### Release mouse button

Release the mouse button (`mouseUp`) on a specific element.

### Input actions - details

#### Type text

Type text into `input`, `textarea` or `contenteditable` fields. Simulates keyboard presses, entering characters one by one.

To escape text like {{ }}, you must put it between `{% raw %}` and `{% endraw %}` blocks.

Example:\
This is not a {% raw %}{{not\_a\_variable}}{% endraw %}

#### Select option

Chooses a specific option in a native HTML `select` dropdown (also called "combobox" menu).

#### Clear input

Removes all characters from a text `input` field, `textarea` or `contenteditable` .

#### Change value

Sets a value of any form element. HTML has many form controls, and some of them can be set to a specific value, for example, radio groups. Technically, a JS "change" event is triggered and the value is updated immediately, without typing letter by letter. Use it for typing longer texts.

#### Upload file

Simulates the "choose file" action in a form type `file` for uploading in forms. You can customize the file that will be uploaded.

#### Paste from clipboard

This step simulates the paste action (Ctrl+V) that the user can perform using the keyboard or mouse.

It's useful when you have "*Copy to clipboard*" actions in your app's UI and you want to use the value later in your test scenario.

### Window actions - details

#### Go to URL

Load the given page URL.

The step is marked as *passed* when the browser emits the [`onDOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onDOMContentLoaded) event.

This action doesn't verify the status of the loaded page. If the URL returns an HTTP status different than 200 (OK), for example, 404, but still loads correctly (browser emits the [`onDOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onDOMContentLoaded) event), the step will be marked as "*passed*".&#x20;

Parameters:

* *Password protected* - If your application is behind [basic auth](https://en.wikipedia.org/wiki/Basic_access_authentication), you can add those credentials by enabling this checkbox.\
  \
  ![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F3L9o5R4LQtyhja3Td4TX%2Fimage.png?alt=media\&token=7e934628-4a92-40ac-9b0e-3836b0129602)

#### New tab

Open a new tab and load the given page URL.

This step works similarly to [Go to URL](#go-to-url), but opens in a new tab.

#### Close tab

Close the current, active tab. Focus will be switched to the previous tab.

If the browser has only one active tab, the browser will be closed and the test will be stopped.

#### Reload page

Reload the page. Nothing less, nothing more.

This step is helpful if you expect that the previous step changed something in the app, but your app is not refreshing automatically (i.e., an asynchronous action).&#x20;

### Advanced actions - details

#### **Set variable**

This action can be used to store local variables from tested sources. You can use a selector to find a text value on the tested web application.\
Now you can store any text value from the tested web page in a variable and use it in feature steps. For example, to find out newly registered unique users in your CRM. This variable is also cross-domain.

{% hint style="info" %}
For more detailed information, check out "[Variables during recording](https://docs.bugbug.io/editing-tests/local-variables)".
{% endhint %}

#### **Switch context**

You can use this action for [working with iframes](https://docs.bugbug.io/editing-tests/tabs-and-iframes) or [multiple tabs](https://docs.bugbug.io/editing-tests/tabs-and-iframes).

#### Run custom JavaScript

#### **Answer a prompt**

Accept or decline browser alerts initiated by `alert()`, `confirm()` or provide a custom text answer for a browser `prompt()`.

This action is automatically [recorded](https://docs.bugbug.io/recording-tests-steps), and most of the time you don't need to edit it manually.

* To confirm the window prompt, enter `true` in the answer field.&#x20;
* To reject enter `false`.&#x20;
* For `prompt()` questions, enter a custom text that should be provided as an answer

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUTqZmjEvF703V1Gfo8ld%2FScreen%20Shot%202022-10-24%20at%2017.55.38.png?alt=media&#x26;token=2ee71d2d-3334-4a4a-873f-3be83ab1909e" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F3W3uT0EMTVp1wSNNSvYY%2FScreen%20Shot%202022-10-24%20at%2017.58.39.png?alt=media&#x26;token=8723f786-8fb4-49b4-afcc-eb96e5b7df0f" alt=""><figcaption></figcaption></figure>
