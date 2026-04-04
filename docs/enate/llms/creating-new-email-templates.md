# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-template-configuration/creating-new-email-templates.md

# Creating New Email Templates

## Creating a New Email Template <a href="#a-creating-a-new-email-template" id="a-creating-a-new-email-template"></a>

There are a number of different attributes which can be defined when creating / editing Email Templates.

### Info Tab <a href="#info-tab" id="info-tab"></a>

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpjfJOiDTYYDeMu8R9%2Fimage.png?alt=media\&token=887eb5b0-6cd8-42de-b3e2-668a59455de4)

The Info tab is used for defining the key information of the template:

* Name: In addition to a friendly name for subsequent selection
* ‘Purpose’ dropdown determines what the template can be used for (this is the type of template as defined above). Please note: This is set permanently when you are creating the template and cannot be modified subsequently.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpjk_TAhsGnwuNol5o%2Fimage.png?alt=media\&token=7e1b1429-8e88-4583-9426-4850778b56bb)

* Description of the template
* Subject of the email.
* Email Body – The contents of the email, along with rich text formatting.

#### System fields <a href="#system-fields" id="system-fields"></a>

System fields can be inserted into the Subject and the HTML Body. They take the form of the field name surrounded by square brackets e.g. \[customerName]. Only fields recognized by the system will be replaced, to avoid false matches on the email e.g. \[this text would remain in the email].

Note: This tab provides the English (default) version of the email content, with definitions for alternate languages definable on the ‘Translation’ tab.

### Files/Links Tab <a href="#files-tab" id="files-tab"></a>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FH3rqszSYUcZSDlQX6kaS%2Fimage.png?alt=media&#x26;token=7fba6b4f-b25f-4088-8247-9cc59b004d87" alt=""><figcaption></figcaption></figure>

The Files/Links tab defines attachments that will be added to an email by default when this template is used.

{% hint style="info" %}
If files are attached to a template, they should be provided for each language used.&#x20;
{% endhint %}

The tags functionality allows the auto-adding of files or links to an email based on their tag if the tag matches the variable set in the email template.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4ZqWGkhnXhsATRFUhTgW%2Fimage.png?alt=media&#x26;token=dc1dcc22-49fc-4a9d-a23f-0ae38840d46a" alt=""><figcaption></figcaption></figure>

Links will be injected anywhere in email body text that the 'Hyperlinks' variable, available in the info tab, has been added.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBOL67zKvBhDSH6zaV1gK%2Fimage.png?alt=media&#x26;token=8820411c-0c6d-41e0-8702-a4f543bc3b64" alt=""><figcaption></figcaption></figure>

### Translation Tab <a href="#translation-tab" id="translation-tab"></a>

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpk25znqj0jcv62Zml%2Fimage.png?alt=media\&token=04a53985-0127-435d-bdd8-caed586cfe72)

The content for each language is provided on this tab. If content for a language is not provided, the system will either use the regional default language or will fall back to English.

If a link is added to the translated email template, you will be prompted to verify the link. \\

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MeipoLrky204T8-Ppa_%2F-MeiprI5yiE2VfJhTfcH%2Fimage.png?alt=media\&token=58f07f62-f740-4a07-88a2-5cb3c9b4757d)

You can verify the link by highlighting the text you want to act as the hyperlink, clicking on the 'Insert Link' icon and then entering the URL to link to.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MeipoLrky204T8-Ppa_%2F-MeiqIVZKwyFHGAC91L_%2Fimage.png?alt=media\&token=747d993c-c034-4aa0-8f29-33db8754e360)

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpk8EURC7YJ-pYb_vD%2Fimage.png?alt=media\&token=64f27c03-f7dc-413b-9a55-143cefe5a93c)

## Localizing Email Template Names <a href="#d-email-template-names-are-localisable" id="d-email-template-names-are-localisable"></a>

Please note that email template names can be set in multiple languages in the [Localisation ](https://docs.enate.net/enate-help/builder/builder-2021.1/adding-localisations)section of Builder, allowing users working in that language to choose the template with a name set in this language.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWpkEJwYILxcgGNkggr%2Fimage.png?alt=media\&token=ffd9733d-32c7-42c7-bfcb-2123181b95e0)
