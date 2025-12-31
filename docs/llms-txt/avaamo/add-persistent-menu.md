# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-persistent-menu.md

# Persistent menu

A **Persistent menu** allows you to specify menu options that are always available to the user. Having a persistent menu easily communicates the basic capabilities of your agent for first-time and returning users. This is an optional configuration.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can configure an agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.
* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

There are two panels in the **Persistent menu** page, the right panel is a preview of how the configuration is displayed in your agent and the left panel is where you can configure details.  In the right panel, you can select options on how you wish to display the menu options in the agent:

* **Expanded**: By default, the menu option is expanded in the agent. However, the user can collapse the menu options in the agent, if required.
* **Always Expanded**: By default, the menu option is expanded and always stays expanded in the agent. The user cannot collapse the menu options.
* **Collapsed**: By default, the menu option is collapsed in the agent. However, the user can expand the menu options in the agent, if required.

## **Configure persistent menu**

* In the **Agent** page, navigate to the **Configure -> Persistent menu** option in the left navigation menu.
* You can add multiple menu options using **Add action**. The following types are supported:
  * [Web page (In-app)](#web-page-in-app)
  * [Web page (External Browser)](#web-page-external-browser)
  * [Deeplink](#deeplink)
  * [Post message](#post-message)

### Web page (In-app)

Use this when you wish for navigating to the specified URL and to open the menu in the agent chat widget.&#x20;

{% hint style="success" %}
**Key points**:

* Specify complete URL
* This is applicable only when the agent is deployed on the Web channel.
* Select **Append user identity** if you wish to append the encrypted JWT token of user details in the URL. See [Append user identity](#append-user-identity), for more information.
  {% endhint %}

**Example**: Consider that you wish to create a persistent menu "Help" that navigates to the specified URL and opens the menu in the agent chat widget:

* For this use case, the following sample HTML is created and hosted in a publically accessible URL

{% code overflow="wrap" %}

```html
<!doctype html>

<html lang="en">

<head>
  <meta charset="utf-8">

  <title>Help Menu</title>
  <meta name="description" content="Help Menu">
  <meta name="author" content="Avaamo">

  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

  <style>
    body {
      margin: 12px;
      padding: 12px;
      font-family: 'Open Sans', sans-serif;
    }

    .header {
      display: flex;
    }

    .profile-img {
      width: 60px;
      height: 60px;
      border-radius: 100%;
      margin: 24px;
      border: solid 3px red;
    }

    .list-item-header {
      margin-bottom: 10px;
      font-size: 16px;
    }

    .list-item {
      cursor: pointer;
      font-size: 14px;
      padding-bottom: 10px;
      color: gray;
    }

    .list-item:hover {
      color: red;
    }

    hr {
      display: block;
      height: 1px;
      border: 0;
      border-top: 1px solid #ccc;
      margin: 1em 0;
      padding: 0;
    }
    
  </style>

</head>

<body class="w3-container w3-animate-bottom">
  <div>
    <a onclick="closeWebView()" href="#" style="text-decoration: none; color: red;">
      < <span style="color: black;">Back</span> </a>
  </div>
  <div>
    <div class="header">
      <img class="profile-img" src="https://i.pinimg.com/originals/2e/19/4e/2e194e71dbfe491c225185560df57f27.jpg"
        alt="agent">
      <div>
        <h1>Hi, I'm Mac</h1>
        <p style="font-size: 14px;">I'm your MacPizza virtual assistant here to help! Here are some things you can ask me...</p>
      </div>
    </div>
    <hr />
    <div>
      <h5 class="list-item-header">About MacPizza</h5>
      <div class="list-item" onclick="onMessageClick('How do I work?')">"How do I work?"</div>
      <div class="list-item" onclick="onMessageClick('Am I safe and secure?')">"Am I safe and secure?"</div>
    </div>
    <hr />
    <div>
      <h5 class="list-item-header">Book an order</h5>
      <div class="list-item" onclick="onMessageClick('I want to book a flight to Tokyo')">"I want order pizza"</div>
      <div class="list-item" onclick="onMessageClick('Can I pre-order a vegetarian meal?')">"Can I pre-order a
        vegan pizza?"</div>
    </div>
    <hr />
    <div>
      <h5 class="list-item-header">Order status</h5>
      <div class="list-item" onclick="onMessageClick('Is my flight on time?')">"Is my order on time?"</div>
      <div class="list-item" onclick="onMessageClick('Is there any new COVID-19 travel advisories?')">"Is there any new
        vegan pizza?"</div>
    </div>
    <hr />
    <div>
      <h5 class="list-item-header">Change or cancel a order</h5>
      <div class="list-item" onclick="onMessageClick('I want to cancel my flight')">"I want to cancel my order"</div>
      <div class="list-item" onclick="onMessageClick('I want to change the name on my flight')">"I want to change the
        toppings on my order"</div>
    </div>
    <hr />
  </div>

  <script>
    function onMessageClick(msg) {
      window.parent.postMessage({ hidden_content: null, message: msg, fn: "postMessage" }, "*")
      closeWebView();
    }
    function closeWebView() {
      window.parent.postMessage({ fn: "closeWebView"}, "*")
    }
  </script>
</body>

</html>
```

{% endcode %}

* In-order to render the **Help** menu, the following Custom CSS is configured in the Agent -> Channels -> Web -> Theme section. See [Configure web channel](https://docs.avaamo.com/user-guide/how-to/build-agents/deploy/web-channel/configure-web-channel#custom-css), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MdRGJtxxOOWYgDe6BPg%2F-MdRO5kCwjLAlI1PhwbB%2F5.7-persistent-menu-in-app-custom-css.png?alt=media\&token=65612148-e928-47e6-832f-b6d75d7f91e3)

The following is the Custom CSS used in this example:

{% code overflow="wrap" %}

```css
.webview_container .modal-dialog.tall {
	height: 100% !important;
}

#avm_chat_window_91a4602e-a8fb-4928-acac-c6a177217df1 .botMenu__menu__item:first-child{
	position: fixed;
	bottom: 2px;
	left: 4px;
	border-radius: 50%;
	padding: 10px 13px;
	font-weight: bold;
	color: transparent;
	width: 15px;
	height: 15px;
}

#avm_chat_window_91a4602e-a8fb-4928-acac-c6a177217df1 .botMenu__menu__item:first-child:hover{
	background-color: #f17375;
	color: transparent;
}

#avm_chat_window_91a4602e-a8fb-4928-acac-c6a177217df1 .botMenu__menu__item:last-child{
	position: fixed;
	top: 11px;
	left: 11px;
	padding: 10px 13px;
	color: #f17375;
}

#avm_chat_window_91a4602e-a8fb-4928-acac-c6a177217df1 .botMenu__menu__item:last-child:hover{
	background-color: #f17375;
	color: white;
}

#avm_chat_window_91a4602e-a8fb-4928-acac-c6a177217df1  .botMenu__menu{
	padding: 0;
}
#avm_chat_window_91a4602e-a8fb-4928-acac-c6a177217df1  .txt-common.editor{
	padding-left: 45px;
}

#avm_chat_window_91a4602e-a8fb-4928-acac-c6a177217df1  .botMenu__menu__item:first-child:before{
	content: '?';
	color: #f17375;
}

#avm_chat_window_91a4602e-a8fb-4928-acac-c6a177217df1  .botMenu__menu__item:first-child:hover:before{
	content: '?';
	color: white;
}

#avm_chat_window_91a4602e-a8fb-4928-acac-c6a177217df1  .nav-bar.messages_nav-bar {
	background-color: #fff;
	color: #F17375;
	text-align: center;
}

.avaamo_popup__close {
	color: #F17375 !important;
}

.avaamo_popup__close:hover {
	color: #F17375 !important;
}

.webview_container button.close {
	display: none !important;
}

#avm_chat_window_91a4602e-a8fb-4928-acac-c6a177217df1  .nav-bar h2 {
	font-weight: bold;
}

```

{% endcode %}

* Navigate to **Configuration -> Persistent menu** and specify the following details:
  * Name: Help
  * Type: Web page (In-app)
  * Link: <\<link of the HTML that is publically hosted>>

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MdROfcQGMfLD3LTD8Qc%2F-MdRPGAKmLUQ-LZY_OIl%2F5.7-persistent-menu-in-app.png?alt=media\&token=1b131c02-48fa-4cb7-8702-e391d7df1d5b)

* Click **Save** to save the persistent menu details.&#x20;
* Click the agent widget icon at the bottom-right corner to test the agent.
* Click the **Persistent menu** in the agent typing text area.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FQVZIF1dM7L6qqrqMdXEP%2Fimage.png?alt=media\&token=a9e3ae4e-6850-46f0-ad7f-983150216a7f)

* In the **Persistent menu,** click `Help`  link.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FDG7Ex9HQBOLhzy8KKxKL%2Fimage.png?alt=media\&token=9f5e2121-ceaf-4d22-a376-4e1dbcdf7218)

* You can view the Help menu displayed in the agent chat widget:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FYZp5YtadCESH0Dl2Muvy%2Fimage.png?alt=media\&token=c06429da-ab48-4a29-983f-a5555a9a643f)

### Web page (External Browser)

Use this option for navigating to the specific URL in a new browser tab.&#x20;

{% hint style="success" %}
**Key points**:

* Specify complete URL
* This is applicable only when the agent is deployed on the Web or Facebook channel.
* Select **Append user identity** if you wish to append the encrypted JWT token of user details in the URL. See [Append user identity](#append-user-identity), for more information.
  {% endhint %}

**Example**: Consider that you wish to create a persistent menu that navigates to the home page of the MacPizza website:

* Navigate to **Configuration -> Persistent menu** and specify the following details:
  * Name: MacPizza - Home
  * Type: Web page (External Browser)
  * Link: <https://macpizza.com/>

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MdQUuUToQ8X_ZEEmGKo%2F-MdQVM-EDLanZ-hjcjfG%2F5.7-persistent-menu-external-browser-setup.png?alt=media\&token=12704665-ca64-4c58-9d78-a7c336050f82)

* Click **Save** to save the persistent menu details.&#x20;
* Click the agent widget icon at the bottom-right corner to test the agent.
* Click the **Persistent menu** in the agent typing text area.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2MeDIhCVFI4WB4AdDwJ9%2Fimage.png?alt=media\&token=6de4712c-df0e-430e-993a-c46660479713)

* In the **Persistent menu,** click `MacPizza - Home`  link.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fu6nIWZZ94Fkn7r7AfHbH%2Fimage.png?alt=media\&token=cf16856b-d2bc-46d0-ace8-160f9e79204f)

* The specified URL is opened in a new browser tab.

### Deeplink

Currently, deep links can be used only to navigate to a specific node in the flow in the Persistent menu. See [Flow control](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control), for more information.

Use `avaamo:#messages/hidden/%23goto_node_<skill_key>>.<<intent_key>>/new/<<message>>`, for navigation to a different node in the conversation flow.

**Example**: Consider that you wish to create a persistent menu that navigates to a specific node in the flow:

* Navigate to **Configuration -> Persistent menu** and specify the following details:
  * Name: Register me
  * Type: Deep Link
  * Link: `avaamo:#messages/hidden/%23goto_node_register_skill.start/new/Registration-Begin`

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MdQlkNMmAkZIAhebcbx%2F-MdQmEjPgceEloOzXL7o%2F5.7-persistent-menu-deep-link.png?alt=media\&token=624c820d-7b14-4e2e-8d1d-cb651fe3d2cd)

* Click **Save** to save the persistent menu details.&#x20;
* Click the agent widget icon at the bottom-right corner to test the agent.
* Click the **Persistent menu** in the agent typing text area.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FI5RrRRnuMjS5ae7ajc3c%2Fimage.png?alt=media\&token=093a3d4a-c67e-46ce-89db-d3ff7118f8df)

* In the **Persistent menu,** click `Register me`  link.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbFzWxZRsmYDSIGhPWMJY%2Fimage.png?alt=media\&token=e72df9e7-3231-4b08-aff9-a5fbd9168ab0)

* The flow navigates to the specified node in the persistent menu:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fyp5HAAR5WdHWTPfLKRNh%2Fimage.png?alt=media\&token=e090f418-e485-478f-9d25-9e4e6078e4e7)

* You can also click the eye icon to view if the menu option has navigated to the desired skill and intent key:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FxTZfdwWwrx0EINmehPAX%2Fimage.png?alt=media\&token=63bf5118-283b-4c4a-94b4-19872f79492a)

### Post message

Use this to post a specific message to the agent.

**Example**: Consider that you wish to create a persistent menu that posts a message in the agent:

* Navigate to **Configuration -> Persistent menu** and specify the following details:
  * Name: Order pizza&#x20;
  * Type: Post message
  * Link: I want to order pizza

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MdQtxCohyAVM09xziQD%2F-MdQulM1iLufjvrfA6Eg%2F5.7-persistent-menu-post-message.png?alt=media\&token=6954431e-5466-433e-b1db-a426ecdb28f5)

See [Flow control](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/flow-control), for more details on goto node.

* Click **Save** to save the persistent menu details.&#x20;
* Click the agent widget icon at the bottom-right corner to test the agent.
* Click the **Persistent menu** in the agent typing text area.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2f3U9pSEs7t7QBc1VaNY%2Fimage.png?alt=media\&token=6a10bce5-9ee5-48e6-aa07-4ff8bbede33b)

* In the **Persistent menu,** click `Order Pizza`  link.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7W9KbJXjSvehhEmTFCwe%2Fimage.png?alt=media\&token=dfa32ca8-f334-4b4b-8ec0-95eee33d8e33)

* You can see the message is posted in the agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FM1qOTl3QW8PSwZPJma2u%2Fimage.png?alt=media\&token=5791a639-5775-4161-8b33-024649c6347d)

{% hint style="info" %}
**Note**:&#x20;

* The following notification messages are displayed in the persistent menu. Note that these are applicable only if you are using the Facebook channel to deploy your agents.&#x20;

<img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-McwSNMhRJyg2eqpzq6C%2F-McwTQK0i1aPnFO4m-sT%2F5.7-rn-persistent-menu.png?alt=media&#x26;token=ddc31a98-9719-4a17-bf61-aad5658b56a2" alt="" data-size="original">&#x20;

The "number of persistent menu items" restriction is due to the limitations of Facebook messenger See [call\_to\_actions in the properties section](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/persistent-menu#properties), for more information.
{% endhint %}

## Append user identity

The **JWT** is generated for passing a unique user identifier, first name, last name, email/phone (if available), and other optional user information that the agent can use to enhance its interaction with the user. See [JWT](https://jwt.io/), for more information on how to encode user payload with the secret key using the HS256 algorithm:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MgFZC1EzqSRWbq-ZFfP%2F-MgFaGAplTJ3ATIVzz4I%2Fpersistent-menu-append-user-identity-jwt.png?alt=media\&token=9e6ee51f-e284-44bc-b611-cbe666a92a1b)

* The following is a sample user payload. Currently, only the following properties can be extracted from the JWT token - uuid, first\_nam&#x65;*,* last\_name, email, and timetoken.

  ```javascript
  {
    "uuid": "dashboard_admin_test_user_368",
    "first_name": "John",
    "last_name": "Washington",
    "email": "",
    "phone": null,
    "time_token": 1628070417
  }
  ```

**Example**: Consider that you wish to create a persistent menu that navigates to the home page of the MacPizza website and append the encrypted JWT token of user details in the URL.

* Navigate to **Configuration -> Persistent menu** and specify the following details:
  * Name: MacPizza - Home
  * Type: Web page (External Browser)
  * Link: <https://macpizza.com/>
  * Check the "Append user identity" check box.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MgFP63mc0667fBI7nu6%2F-MgFY9XjnkGJGJTLf-Px%2Fpersistent-menu-append-user-identity.png?alt=media\&token=feb0956c-8f3a-4e28-94c3-55c310317fad)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fda14mEfOp3aq3OW6cryh%2Fimage.png?alt=media\&token=a77edd29-d787-4b66-a3ee-96fd1b26453c)

* In the **Persistent menu,** click `MacPizza - Home`  link.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FIfIZOoXWN0XHT9eYrq9N%2Fimage.png?alt=media\&token=698b7e52-d144-4f89-a34d-1f50d8691b48)

* The specified URL is opened in a new browser tab and the encrypted JWT token is passed in the **user\_jwt\_token** URL parameter.

## Persistent Menu Compliance

Persistent menu is supported only in the following channels:

* [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel)
* [Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps)
* [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps)
* [Facebook (except Deeplink)](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel)
