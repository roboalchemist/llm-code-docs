# Source: https://docs.sinch.com/ia-conversational/untitled-8/bot-message.md

# Bot message

To design your conversational flow, you can use multiple components, like text messages, buttons and carousels. Depending on the channel you publish the bot to (Facebook Messenger, web, Slack, Telegram, ...), these will be shown slightly differently.

{% hint style="info" %}
**Character limits**

When you're building your flows, our platform gives you advice on how many characters you can use in buttons, text messages, etc.

​![](https://firebasestorage.googleapis.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-M1_neKsEEUw6wdropeT%2F-M1_odGl6kgprl2B86zM%2Fimage.png?alt=media\&token=78726eee-3830-42b4-a149-0f1c1c3b6684)​

For Facebook Messenger, these are hard limits, meaning that if you're adding a button label longer than 20 characters, it will be cut off and shown with "..." For example: the label "hello I am a button click me" will be shown as "hello I am a button..."
{% endhint %}

{% hint style="info" %}
For all other channels, the character limit is based on best practices. We recommend using less characters than the limit, but it's not mandatory.
{% endhint %}

## Text Messages <a href="#text" id="text"></a>

Text messages are the most simple components. Most channels will show them as 'text bubbles'.

## Buttons <a href="#buttons" id="buttons"></a>

Buttons are a useful way to guide the conversation by giving the user a limited set of options. You can add a maximum of three buttons to a message.

### Button types <a href="#button-types" id="button-types"></a>

#### Next bot dialog <a href="#next-bot-dialog" id="next-bot-dialog"></a>

For each button, you need to define a next dialog state. Optionally, you can add key-value combinations to a button. These will set variables depending on which button the user has clicked. These variables can then later be used to route dialog states, do an API call or render specific text.

#### URL <a href="#url" id="url"></a>

You can link a button to an external URL.

#### Call <a href="#call" id="call"></a>

This button will initiate a call if the user is using a mobile device.

#### Webview <a href="#webview" id="webview"></a>

This button will open a webview (or a new browser window depending on the channel) with the configured URL as target.

The parameters you configure for this button will be JSON stringified and appended to the URL as a Base64 encoded string. It is possible to decode this string using the `atob` JavaScript function.

## Media <a href="#media" id="media"></a>

With the Media template, you can enable the bot to send files to your users.

{% hint style="warning" %}
If you upload the file directly in the platform, there is a file size limit of 10 MB. If you use a direct URL to the file, there is no file size limit.

​![](https://firebasestorage.googleapis.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MRUA1-jfsQMKFUW1UgA%2F-MRUAQmVfC0rawpgtBg6%2Fimage.png?alt=media\&token=21f112e2-f731-468c-90d9-5efee876f884)
{% endhint %}

**​Images**

All typical image types, such as jpg, png and gif are supported on our platform.

#### Video <a href="#video" id="video"></a>

Videos are available in the Emulator, web widget and Facebook channel. The following video formats are supported:

* mp4
* ogv
* webm

A nice feature of Facebook Messenger is that people can share a video with their friends by clicking the button on the right side of the video:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LLTwINdA-k01sAajhSX%2F-LLTwJKNgjL7aMhqnglA%2Fvideo%20messenger.png?alt=media)

{% hint style="warning" %}
Are you having trouble adding an external video to your bot? Check out [this](https://docs.chatlayer.ai/tips-and-best-practices/solving-bot-issues/3.-media-upload-not-working) article.
{% endhint %}

**Audio**

The audio widget is available in the Emulator, the web widget and Facebook Messenger. Currently we only support MP3 as an audio format.

### ​![](https://firebasestorage.googleapis.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LLTwINdA-k01sAajhSX%2F-LLTwJKPmRgeNs9TA5u2%2Fmessenger%20audio.png?generation=1535969952855086\&alt=media)​ <a href="#undefined" id="undefined"></a>

#### Files <a href="#files" id="files"></a>

File attachments are available in Facebook Messenger. Currently, only PDF is supported.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LLTwINdA-k01sAajhSX%2F-LLTwJKRh_qOHTpZs70J%2Fattachment.png?alt=media)

{% hint style="info" %}
We recommend media files shared on Facebook Messenger to be below 5 MB in size, as Facebook seems to have trouble in handling files larges with acceptable performance.
{% endhint %}

## Quick replies <a href="#quick-replies" id="quick-replies"></a>

Quick replies behave similarly to buttons. They are shown horizontally next to each other in a scrollable container. This means that you can add as many quick replies as you think necessary.

#### Payloads <a href="#payloads" id="payloads"></a>

For each quick reply, you need to define a next dialog state. Optionally, you can add key-value combinations. These will set variables depending on which button the user has clicked. These variables can then later be used to route dialog states, do an API call or render specific text.

#### URL <a href="#url-1" id="url-1"></a>

Quick replies only support next dialog states, no links to external websites. You can use a button for that.

#### Icon <a href="#icon" id="icon"></a>

Optionally, you can add an icon to a quick reply by specifying its URL.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LLTwINdA-k01sAajhSX%2F-LLTwJKTb_8IfdZj-Ld9%2Fquickrelies.png?alt=media)

#### Location <a href="#location" id="location"></a>

This button will save your location to a defined variable. Make sure to set the language for all location related data.

## Carousel <a href="#carousel" id="carousel"></a>

Carousels are a way to visualize options by using images. Each option can have up to three buttons with separate actions, but this is not required. These buttons are the same buttons as in the button template and use the same properties like payloads and URL, with the addition of an extra share button.

{% hint style="info" %}
Facebook has renamed the 'Carousel' template to 'Generic Template'. You can read more about their guidelines for Generic Templates [here](https://developers.facebook.com/docs/messenger-platform/send-messages/template/generic).
{% endhint %}

#### Share button <a href="#share-button" id="share-button"></a>

The share button opens a sharing-dialog in Facebook Messenger, enabling people to share message bubbles (aka carousel cards) with their friends.

When a new user receives a message bubble, he can share it with his friends by tapping the same share button. When tapping the postback button, the user is send to the start page of the bot.

You can only use share button in generic templates items (previously called carousels) and only items with maximum one url can be shared by Facebook. It is not possible to change the button title: Facebook Messenger will translate the button to the user's preferred language profile setting.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LLTwINdA-k01sAajhSX%2F-LLTwJKVzShk3Y7meASp%2Fcarousel.png?alt=media)

## List <a href="#list" id="list"></a>

The List Template is a template that allows you to present a list of items, shown vertically.

Each item may shown a button that can be used as a call-to-action (postback). You can also provide a URL that opens when an item is tapped.

Each list template message can also have up to one global button that will show below the item list.

### List styles <a href="#list-styles" id="list-styles"></a>

Lists can be shown in two different ways: Large and Compact.

#### Large <a href="#large" id="large"></a>

Large lists show the first item with a cover image and text overlay. This is useful if you want to make the first item stand out over the other items.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LLTwINdA-k01sAajhSX%2F-LLTwJKXmBQxe0crxOg7%2Flist%20template.png?alt=media)

#### Compact <a href="#compact" id="compact"></a>

Compact lists show each item in the same way. This is useful for presenting a list of items where no item is shown more prominently.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LLTwINdA-k01sAajhSX%2F-LLTwJKZWVwNUi1O0xTs%2Flist%20template%20compact.png?alt=media)

## File upload <a href="#file-upload" id="file-upload"></a>

Use the file upload template to let users upload a file directly from their device to your bot.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-M3L63O1_lCPCmfdqyUK%2F-M3LuOrQ9lQqyVA8Ak3p%2Fimage.png?alt=media\&token=2efa2689-ae81-492e-9e24-5b666688c271)

Configuring the File Upload as shown above will show an Upload button in the conversation:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-M3L63O1_lCPCmfdqyUK%2F-M3LukpL2-eh7WBMg5h1%2Fimage.png?alt=media\&token=d32aee90-41b1-44f6-863a-a8db92300237)

If the upload failed because there was a problem with the connection, or the file the user chose was bigger than 10 MB, the bot will go to the "failed upload" bot dialog.

The URL where the uploaded file is stored can be found under the `{uploadedFileUrl}` variable in the user's session. You can reuse this variable to show the file that the user uploaded by using the [Media](https://docs.chatlayer.ai/bot-answers/dialog-state/message-components#attachments) template. Alternatively, you can retrieve the URL with an [API plugin](https://docs.chatlayer.ai/integrations/custom-back-end-integrations) to store the files on your servers.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-M3L63O1_lCPCmfdqyUK%2F-M3Lv7RSad1WBybBk6fL%2Fimage.png?alt=media\&token=786fe358-10fe-4974-a37a-b59d25f7c49c)

## Rich text <a href="#rich-text" id="rich-text"></a>

Rich text allows you to go beyond text messages and style your text the way you want it. You can also add weblinks using the rich text editor.

{% hint style="warning" %}
Rich text is only visible in the Chat Widget channel. The other channels do not support this type of text.
{% endhint %}

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MJXFE7Uify2nmmX8UzW%2F-MJXc2k8-uGN9vJ_TbP6%2Fimage.png?alt=media\&token=530e3629-e937-4192-a48e-a6d7a2f62668)

The rich text editor allows you to use the following styles:

* Paragraph
* Heading 1
* Heading 2
* Heading 3
* Heading 4
* Bulleted list
* Ordered list (= numbered list)

And format the text in the following ways:

* **Bold**
* *Italic*
* Underline

You can also add hyperlinks (weblinks) that either go to an external page or to a specific place in your conversation.Inserting a link using rich text

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWYVhNNRbTnSKA7OTmX%2F-MWYW53C8upHR8BjUtKU%2Fimage.png?alt=media\&token=8daa73e9-1f07-4227-87bd-25cd2f285a6d)

To hyperlink a word or sentence, select it and then click the chain icon on the right below. A popup will appear where you can put in the link address. Then click 'save'.
