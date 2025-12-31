# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-buttons.md

# Add buttons

You can add different types of buttons to [Quick reply](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#quick-reply), [Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#card), [Carousel](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#carousel), and [ListView](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/..#list-view) responses.&#x20;

* For each button, specify the button caption.&#x20;
* Additionally, depending on the button type, specify message, node number, URL, or HTML code, as required. You can add the following types of buttons:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FvPKmnyxkJ0PDw2yTfSEm%2F6.3-fb-camera-effect-response.png?alt=media&#x26;token=33415b60-903c-43a3-8e42-a6ed74ed40ba" alt=""><figcaption></figcaption></figure>

* [Call](#call)
* [Location](#location)
* [Date](#date)
* [Post message](#post-message)
* [Goto node](#goto-node)
* [Webpage](#webpage)
* [Webview (URL)](#webview-url)
* [Webview (HTML)](#webview-html)

### Call

Allows you to create a link to a phone number. You must specify a complete phone number with a country code.

**Supported in**: Card, Carousel, List view

**Example**: The following is an example of the **Call** button in the **Card** response:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Mjj7cNxv1CsUOZA3I5j%2F-Mjj9vI54sC2jKF8JkqS%2Fcall-info-number.png?alt=media\&token=f794725f-ccb2-49f9-b578-1b234ad4da84)

Post a query as specified in the intent to trigger the response. Click the **Call** button to create a link to a phone number. This creates the call link and tells the browser how to use the number.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FJDUsvSIkwcKGdV40Psgm%2Fimage.png?alt=media\&token=c2939c2a-ebb8-4541-862d-290a0944a1d3)

You can use `context.last_message` to get the phone number specified in the **Call** button.&#x20;

### Location

Displays the current location of the agent.

**Supported in**: Quick reply, Card, Carousel, and ListView

**Example**: The following is an example of the **Location** button in the **Quick reply** response:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO2-WSuJa0jQ6BB9sNV%2F-MO4rBOjzH52e1VZAIOD%2Fdialog-skill-quick-reply.png?alt=media\&token=ef363b41-2e21-41fb-a911-9c61c9a275a9)

Post a query as specified in the intent to trigger the response. Click the **Location** button to display the current agent location.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F8SkUZVU39tlaN1XliaEq%2Fimage.png?alt=media\&token=b0bf671b-0389-4a79-bd67-5718e00fa587)

When the users click the **Location** button, the details of latitude and longitude along with complete address is available in `context.last_message` that can be used for further processing.&#x20;

```javascript
{
      "lat": "12.9736704",
      "lon": "77.549568",
      "title": "",
      "description": "Vijayanagar, South Zone, Bengaluru, Bangalore North, Bangalore Urban, Karnataka, 560040, India"
}
```

In the next node after the Location node, you can create an intent with a wildcard (training phrases intent without any training phrases) and in the post-processing perform necessary validations using latitude and longitude.&#x20;

**Example**: In the pizza agent, you can validate the location,  check for the nearby delivery stations, and update the delivery time.

{% hint style="info" %}
**Notes**:&#x20;

* The Location button in Quick replies is deprecated by Facebook. See <https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies#locations>, for more information.
* The Location button is not supported in the Microsoft Teams channel due to the limitation on the channel's side. See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.
  {% endhint %}

### Date

Displays a date picker.&#x20;

**Supported in**: Quick reply, Card, Carousel, and ListView

**Example**: The following is an example of a **Date** button in the **Quick reply** response:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO7FJqIePTJFF-ScB4P%2F-MO7H6Y61pwUSIl-2H8o%2Fdialog-add-button-date.png?alt=media\&token=38b9b760-53a8-4cef-ba30-193a4d0b2b45)

Post a query such as specified in the intent to trigger the response. Click the **Date of Birth** button to display a date picker:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FUs9g95g3J52CX3wWlfDm%2Fimage.png?alt=media\&token=a0929663-66ac-4b71-b76f-863a3f354a5e)

You can use `context.last_message` to get the date selected by the user.

{% hint style="info" %}
**Note**: The Date button is not supported in the Microsoft Teams channel due to the limitation on the channel's side. See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.
{% endhint %}

### Post message

Post the specified message in the agent.

**Supported in**: Quick reply, Card, Carousel, and ListView

**Example**: The following is a sample example of the **Post message** button in the **Quick reply** response:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO7FJqIePTJFF-ScB4P%2F-MO7ID0Fe0fjALV3Tr4Z%2Fdialog-add-button-post-message.png?alt=media\&token=26584d8b-2001-401a-a4d8-d3e462b5ebe9)

Post a query as specified in the intent to trigger the response. Click any of the buttons to post a message as specified in the response:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fcan6bSx5NHU7R0cHUaF2%2Fimage.png?alt=media\&token=217f9630-e855-4998-a198-064ed17657e1)

### Goto node

Transfers the flow to the specified node number.

**Supported in**: Quick reply, Card, Carousel, and ListView

**Example**: The following is a sample example of the **Goto node** button in the **Quick reply** response:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO7FJqIePTJFF-ScB4P%2F-MO7IhPrOumcz2rGiIVG%2Fdialog-add-button-goto-node.png?alt=media\&token=cb27c3f4-e476-488c-8fc9-99031cf615b5)

Post a query as specified in the intent to trigger the response. Click any of the buttons to Goto the respective node:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2ljljNeb8b2Ws5BAtIO0%2Fimage.png?alt=media\&token=9586d31d-c088-44d3-8d27-dcd4cc58ee1b)

### Webpage

Navigates to the specified URL in a new browser tab.&#x20;

**Supported in**: Card, Carousel, and ListView

**Supported channels**: Web, Facebook&#x20;

Example: The following is a sample example of **Webpage** button in **ListView** response:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MO7FJqIePTJFF-ScB4P%2F-MO7J3epLyn2fnOQKU5W%2Fdialog-add-button-webpage.png?alt=media\&token=1b2d2601-12e7-4bfc-90a8-8377ce1cc7a7)

Post a query as specified in the intent to trigger the response. Click the "Know more..." button to navigate to the specified URL:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXtHht9RD5ilDPWC6TUrP%2Fimage.png?alt=media\&token=e5e2d027-0c43-4a1e-9798-5502a817e9d5)

{% hint style="info" %}
**Note**: Ensure that you have whitelisted all the URLs that are rendered inside the Team's web view or Task Module in the Teams App. See [Microsoft teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information.
{% endhint %}

### Webview (URL)

Navigates to the specified URL in the web view of the agent.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* The URL must be accessible without any privacy and security restrictions from the agent.
* The link you are using must be allowed to be opened in an iframe.
* Ensure that you have whitelisted all the URLs that are rendered inside the Team's web view or Task Module in the Teams App. See [Microsoft teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information.
  {% endhint %}

**Supported in**: Card, Carousel, and ListView

**Supported channels**: Web, Facebook

**Example**: See [Webpage](#webpage), except that the URL is displayed in the web-view, all other settings remain similar.

### Webview (HTML)

Displays the HTML in the web view of the agent. When you add a Webview button, you can choose the following types of views:

* **Compact**: Displays a small compact view in the agent window.
* **Tall**: Displays a view slightly bigger than the compact view in the agent window.
* **Full**: Displays a view as big as the agent window.

**Supported in**: Card, Carousel, and ListView

**Supported channels**: Web, Facebook &#x20;

**Example**: The following is a sample example of the Webview (HTML) button in ListView response:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LwMc9fq67gZ5RcaeYhI%2F-LwMlXnFWt7T9MLiDtRY%2Fjs-custom-skill-web-view.png?alt=media&#x26;token=4cee6f4e-1892-479b-8f70-64c19cff2709" alt=""></div>

Post a query as specified in the intent to trigger the response. Click the "Know more..." button to view the HTML content:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FDLhJyPoUcCXAoQGjs2Nf%2Fimage.png?alt=media\&token=6a928038-ad08-4a02-97f1-e7e4de37960c)

See [Create custom HTML web views](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/create-custom-html-web-views), for a complete example.

{% hint style="info" %}
**Notes**:&#x20;

* Currently, Compact, Tall, and Full view are not supported in the Microsoft Teams channel due to the limitations on the channel's side. See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.
* Webview (HTML) supports upto 65000 characters. If you have a requirement to use a larger HTML, then it is recommended to use [Webview (URL) ](#webview-url)option.&#x20;
* Specify HTML in the proper standard format. Include all the required elements such as HTML, HEAD, TITLE, and BODY. The "title" tag is displayed in the popup title. If you wish to omit the "title" tag, then it is still recommended to include an empty "title" tag, so that it adheres to proper HTML standards.
* In case you wish to embed a video in your card input, then you can host it and use it as a "href".  If you want to create a frame you can use the below code:\
  \
  `<iframe src="<<hosted file location>>" width="800" height= "500"  frameborder="0" allow="autoplay; fullscreen"  allowfullscreen></iframe>`
  {% endhint %}
