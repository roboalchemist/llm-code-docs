# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel/facebook-messenger-compliance.md

# Facebook Messenger compliance

Facebook Messenger offers several content templates to display information in a conversational UI. It is important to understand the specifications of these templates so that conversation flows can be more quickly and accurately translated to the Messenger chatbot UI.

### **Text bubble**

Used for simple text and conversations. Can be used to display the largest blocks of text for all content types:

* Upto 640 characters, which is by far the largest text container.
* No support for rich text such as bolding, italics, color, etc.
* No URL linking within the text bubble (except for tel #s). However, you can add up to 3 link buttons to the bottom of the text message.
* Each text message can contain a max of 640 characters
* Upto 3 buttons can be added to a text message

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M719VpBXiLePY2oQg0Z%2F-M71NwLJ_VuT53V4N94U%2Ffb-messenger-text.png?alt=media\&token=dd467079-abad-442f-ad2c-7c5e4050312c)

See [Text responses](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#text), for more information on building text response in your agent.

### **Cards & Carousels**

{% hint style="info" %}
**Note**: See [Generic Template Reference](https://developers.facebook.com/docs/messenger-platform/reference/templates/generic), for more information on limitations from the Facebook Messenger.
{% endhint %}

For displaying products and services and a quick summary:

* Allows for an image
* The title has an 80 character limit
* The subtitle has an 80 character limit
* Buttons is limited to 3
* Up to 5 carousel items allowed

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M719VpBXiLePY2oQg0Z%2F-M71O9lpICJk-pFQQXDq%2Ffb-messenger-card.png?alt=media\&token=24bcde17-5e15-4625-ad2d-d2a4696c97bf)

See [Card](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#card) and [Carousel](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#carousel) response, for more information on building card and carousel response in your agent.

### **List Template**

Good for showing FAQs and items that require more text than offered in cards (80 vs 20 characters). See [ListView](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#listview) response, for more information on building ListView response in your agent.

Currently, ListView is displayed as [Carousel ](#cards-and-carousels)in the Facebook Messenger channel, since ListView is not supported in FB Messenger.

### **Quick Replies**

A very space-efficient and quick way to move through flows.&#x20;

* Button title has a 20 character limit. Beyond 20 characters, the button title gets truncated.
* After a button is clicked it disappears
* You can have upto 10 quick reply buttons
* Note that the Location button in Quick replies is deprecated by Facebook. See <https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies#locations>, for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M719VpBXiLePY2oQg0Z%2F-M71OvjXuAs97xQNgvcv%2Ffb-messenger-quick-replies.png?alt=media\&token=13715424-f2ef-4540-bb6c-d5cac601ebf7)

See [Quick reply](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses#quick-reply) response, for more information on building a Quick reply response in your agent.

### **Persistent menu**

A **Persistent menu** allows you to specify menu options that are always available to the user. Having a persistent menu easily communicates the basic capabilities of your agent for first-time and returning users.

* Menu items are limited to 3 for the top level, and 5 items for any submenus.
* The title is limited to 30 characters
* You can have at most 3 hierarchical levels of menu\_item in total

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M719VpBXiLePY2oQg0Z%2F-M71PWsyRbtLDu8gf1yL%2Ffb-messenger-persistent-menu.png?alt=media\&token=a25a8be2-f5da-40c6-a154-87ea6c0bb149)

See [Add persistent menu](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-persistent-menu), for more information.

### **Webview**

Using webviews, you can augment your agent's user experience with features that might be difficult to offer using only message bubbles.

* A good way to handle lots of text
* Ability to link to a website
* Scrolls
* Rich formatting (its a webpage)

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M719VpBXiLePY2oQg0Z%2F-M71Pj1DvQtY_MC7Wzw2%2Ffb-messenger-webview.png?alt=media\&token=49e50b7a-9b0e-4963-84ed-77a7ea753bd7)

See [WebView](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/add-buttons#webview-url), for more information.
