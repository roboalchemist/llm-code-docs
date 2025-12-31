# Source: https://docs.deepconverse.com/product-docs/chatbots/localization.md

# Localization

You can export the text content used in the chatbot for translating it into other languages. DeepConverse makes it easy for you to export it to a Google Sheet for collaborative editing and sharing. Once you are ready with the translations and the locales for your site you can import it back into DeepConverse.&#x20;

### Exporting Translations

To export translations navigate to the chatbot that you would like to export.

On the chatbot page click Actions > Export/Import Translations.

![](https://help.deepconverse.com/hc/article_attachments/7611009322516/mceclip0.png)

In the open form click Submit if you would like to export to a new sheet, or enter the Sheet Key and Worksheet Title for the sheet you would like to update.&#x20;

*Once the export is completed the sheet will be shared with your email.*

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2Fs0I5fuXxX4f9SUminS0V%2Fimage.png?alt=media&#x26;token=cf65a433-c432-4805-9bb2-af9ab7c07ba0" alt=""><figcaption></figcaption></figure>

**Prefill Auto Translation**&#x20;

This allows you to prefill the sheet with Google Translate values if the translation does not exist.

Here is an example of how the exported translations would look like.

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FV4cRzEQtk8A05j3lK4yx%2Fimage.png?alt=media&#x26;token=3d35a16a-3959-4466-abaa-433f7b17ef55" alt=""><figcaption></figcaption></figure>

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FR9wOO1rXIpEcuHPo96f4%2Fimage.png?alt=media&#x26;token=78d78dc1-2a26-40f1-84ec-51c561d349d1" alt=""><figcaption></figcaption></figure>

### Adding Translations&#x20;

Once you have exported the text into the Google Sheet you can add additional columns each representing a locale that you would like to target.&#x20;

Add the corresponding translation for that row in the cell.

Here is an example of how **French (fr)** is added into the sheet.

***Tip***: You can use the [GOOGLETRANSLATE](https://support.google.com/docs/answer/3093331?hl=en) function already available in Google Sheets for quick translations

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FWjxwkKVmBp057R3bh3TY%2Fimage.png?alt=media&#x26;token=9f0b1ca3-9589-4211-a4fe-1f5e65e81479" alt=""><figcaption></figcaption></figure>

### Importing Translations&#x20;

On the chatbot page click Actions > Export/Import Translations.

Select **Import** as the operation

Enter the **Sheet Key** and the **Worksheet Title**&#x20;

&#x20;

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FKRsUUO7cMQFlPRi6hrZn%2Fimage.png?alt=media&#x26;token=85f4b9da-d2de-438a-88ea-7d2f038d3407" alt=""><figcaption></figcaption></figure>

**Notes**:

1. Locales in the Google Sheet should match the locales you use in your production/deployment environments for the translations to get picked up.
2. If a text doesn't have the the corresponding language translation then it will default to using text from 'en\_us' as the fallback

<br>
