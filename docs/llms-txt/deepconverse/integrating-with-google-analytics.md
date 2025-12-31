# Source: https://docs.deepconverse.com/product-docs/analytics/integrating-with-google-analytics.md

# Integrating with Google Analytics

When you use the DeepConverse chat widget you can also integrate it seamlessly with Google Analytics. This allows you to use your existing GA property and track events and user interactions happening in the chatbot.&#x20;

You can set the Google Analytics property in the **Features > Miscellaneous** section of your chatbot (shown below)

{% hint style="warning" %}
This feature requires **Google Analytics 4**&#x20;
{% endhint %}

<figure><img src="https://help.deepconverse.com/hc/article_attachments/5915083177492/mceclip0.png" alt=""><figcaption></figcaption></figure>

&#x20;

We list out the events that are tracked with different interactions in the chatbot.

| **Event Name**      | **Event Label** | **Description**                                           |
| ------------------- | --------------- | --------------------------------------------------------- |
| Open Bot            |                 | Fired when user clicks on chat bubble to open chatbot     |
| Setting Clicked     |                 | Fired when user clicks on Settings icon                   |
| Minimize Bot        |                 | Fired when user minimized chatbot                         |
| Close Bot           |                 | Fired when user closes chatbot                            |
| Close Preview       |                 | Fired when user closes the chatbot bubble text            |
| User Clicked        | Button Text     | Fired when user clicks on a quick reply button            |
| Enlarge Image       |                 | Fired when user clicks to enlarge an image                |
| Confirm End Chat    |                 | Fired when user clicks confirm end chat                   |
| Continue Chat       |                 | Fired when a user clicks on Continue chat                 |
| Download Transcript |                 | Fired when user clicks Download Transcript                |
| Input Submitted     | User Input Text | Fired when user types something into the chatbot text box |

&#x20;

### Google Analytics View

You will be able to see the events show up in Google Analytics. Now you use these events to filter and segment users and create views based on them.

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2Fok8TMQ2XTxaTmaAjJqWA%2Fimage.png?alt=media&#x26;token=cbb1e711-4a89-490d-ad15-439f799500b7" alt=""><figcaption></figcaption></figure>
