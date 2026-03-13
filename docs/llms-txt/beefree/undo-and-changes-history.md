# Source: https://docs.beefree.io/beefree-sdk/server-side-configurations/server-side-options/undo-and-changes-history.md

# Undo & Changes history

## Overview <a href="#overview" id="overview"></a>

Your users will have the ability to rewind and fast-forward to any point in their recent edit history. Once *Undo* is enabled in the [Beefree SDK Console](https://developers.beefree.io/), the application immediately begins tracking changes. Behind the scenes, this is accomplished via a new callback event – [called onChange](https://docs.beefree.io/beefree-sdk/getting-started/tracking-message-changes) – which can also be used “stand-alone” without enabling *Undo*. No client-side configuration is required to use this feature. Continue reading to learn how to activate and use *Undo*. And if you can’t wait to try it yourself, you can immediately do so at [beefree.io](https://beefree.io/templates/)

### How it works <a href="#how-it-works" id="how-it-works"></a>

When changes are detected, a compact *Undo* widget displays in the bottom left corner of the stage:

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2Fxf8GT9xEafFOleM02v5t%2Fundo_widget-1024x327.png?alt=media&#x26;token=9f4e1a1a-aac5-43f5-8fa2-2141b62cefdd" alt=""><figcaption></figcaption></figure>

The widget displays 3 actions:

* **Undo and Redo arrows** that offer the classic pattern to move back and forth between changes.
* **A history icon** that expands a timeline of the latest changes:

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FQ4mgU0JEwQhGVYeQnwuv%2F2undo_timeline-1024x954.jpeg?alt=media&#x26;token=bc503d24-bddf-42e0-b341-e8a47bda9bd4" alt=""><figcaption></figcaption></figure>

### **Timeline**

The timeline allows the user to browse through the most recent changes.

All the steps display:

* An icon to identify the content element type (an image, text, etc.)
* A description of what changed, giving the new property value (if any)
* The exact time it happened

All these details provide enough information for users to understand what modification was applied, and, if desired, rewind the message to that state:

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FjKQbkYjqQGDiSntyRYoB%2F3history-browse-1024x868.jpeg?alt=media&#x26;token=5b12166b-ada8-4321-9070-4f2f752e4b90" alt=""><figcaption></figcaption></figure>

When the user selects a previous step, the content or row that triggered the history record displays as the selected item, providing further context.

The timeline for more recent changes is still available, allowing the user to move forward without losing any changes:

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FNracszYDXctGjIPlA73Y%2F4history-rewind-1024x923.jpeg?alt=media&#x26;token=bddcad14-91dc-42a1-97ca-7ee1d0340fad" alt=""><figcaption></figcaption></figure>

The *Undo* widget currently displays the last 15 edits in the timeline, but users can always rewind to the *Message opened* state to undo all changes since the message was initially opened in the builder.

We are also doing additional testing to see if the number of recent edits can be increased beyond 15 without negatively impacting the browser’s performance. We will update this section if the number is increased.

The last saved edits are only available at the session level, so they reset every time the builder is loaded. If you need to provide a complete message history, you can build a custom one based on the *onSave* and *onChange* events (see below).

## Activating the Widget

The Undo option is available at the application level in the [Beefree SDK Console](https://developers.beefree.io/). Select your application from the list and open the *Application configuration* in the bottom-right.\
The option to enable this widget is available in the *Services* list:

<figure><img src="https://806400411-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8c7XIQHfAtM23Dp3ozIC%2Fuploads%2FVuDAAk4nzZOBKfCnxFg4%2F5enableUNDO-300x42.png?alt=media&#x26;token=6182695b-bfd3-484f-9e61-cb3818462984" alt=""><figcaption></figcaption></figure>

The widget uses the [onChange callback](https://docs.beefree.io/beefree-sdk/getting-started/tracking-message-changes) information to work. However, it doesn’t need a client-side configuration for the callback: once *Undo* is enabled, the application starts tracking changes even if the [*trackChanges* parameter](https://docs.beefree.io/beefree-sdk/getting-started/tracking-message-changes) is not set in [*beeConfig*](https://docs.beefree.io/beefree-sdk/getting-started/readme/installation/configuration-parameters).
