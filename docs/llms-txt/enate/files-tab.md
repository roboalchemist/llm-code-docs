# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/work-item-screens/files-tab.md

# Files Tab

## Overview

The files tab shows all of the files and links that have been added to that work item and its related work items, plus attachments for incoming and outgoing emails.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MTc5Nw==>" %}

Any files/links for the current work item which is open are displayed at the top of the files tab, and any for its related work items are shown in a separated section below this. Items are sorted by the date/time they were uploaded with the most recent at the top.&#x20;

You can see the name of the file, what type of file it is, its size, who uploaded it (and when), plus the reference number and of the work item it was uploaded to. You can also see the [tags ](#tagging-files)and [notes ](#adding-notes-to-files)that have been added to the files.

Various icons help you to identify further information:

* Standard file attachments are denoted with a paperclip icon: <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmYMqgKJ9DuXCL53PugFn%2Fimage.png?alt=media&#x26;token=310b578e-7a11-4891-85ab-3506eca6564e" alt="" data-size="line">
* Links are denoted with a links icon: ![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaccvZVAAP8tP9CW7xbLB%2Fimage.png?alt=media\&token=696ec6dd-46ed-452d-ab06-ecbea8c30808)
* Attachments from incoming emails are denoted with a green email icon: <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fvov9LZHMzNbi2WyLwjZk%2Fimage.png?alt=media&#x26;token=4815f405-f2b9-4b20-83b6-a7c2be842e46" alt="" data-size="line">
* Attachments from outgoing emails are denoted with a blue email icon: <img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fn8qaklJ2nhsDejig2BF1%2Fimage.png?alt=media&#x26;token=b5758a1d-31c3-4521-ad4a-181bf7753c1a" alt="" data-size="line">

All files in the files tab are available to [add as attachments to any outgoing emails](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/attaching-files-to-an-email) and links are available to add to the email body.

{% hint style="info" %}
Please note that when upgrading from versions older than 2022.3, the files attached directly to a work item will all show in the 'Other work items' section without a reference number. Email attachments for this work item's emails *will* show in the 'Current' section however.
{% endhint %}

## Adding Files/Links to a Work Item

If the work item is assigned to you, you can add files and links to a work item in the Files tab. Multiple files can be uploaded at one time. Click the upload links at the top of the tab to upload.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5Jf2BwcDga3ug4ioTVd4%2Fimage.png?alt=media\&token=1db36f90-91ba-4ff7-9d8f-5c7324881e36)

You can also drag and drop files into the files tab to upload them.

{% hint style="info" %}
Note: The maximum size per file is 100.00 MB.&#x20;
{% endhint %}

### File Type restrictions <a href="#tagging-files" id="tagging-files"></a>

By default, all types of files can be uploaded, however filetypes *can* be restricted by specifying acceptable types in the [general settings](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#allowed-file-types) section of Builder.&#x20;

## Tagging Files and Links <a href="#tagging-files-and-links" id="tagging-files-and-links"></a>

Tags can be added to files and links. Tagging is very helpful to add more structure to your files information, and opens up features such as auto-attaching files with certain tags to emails being auto-sent by the system, and to canned responses in mails you're composing. They also allow external automation routines to know which specific files to pick up from a work item.&#x20;

Tagging files is also an important feature for processes which involve automation technology. Example: if a downstream automated Action needs to know which of the files you’ve attached to your Case is the ‘Invoice Confirmation’ file, you can tag the relevant files as such and, no matter the file name, the automation technology would know to select that file based on its tag. Such external automation technology can equally well supply tags as part of uploading documents into Work Items in Enate for further downstream manual / automated use.

The tag titles available to you are [set in Builder](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags). If you're regularly finding that a specific tag is not available to select, make sure to speak to your admin team about getting it added.

You can add a tag to a file by clicking on the '+' icon and then selecting a tag from the resulting list.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVXReQz9C20sb4udydhJF%2Fimage.png?alt=media&#x26;token=602fe6a4-3867-4b26-b40b-61bb28b2f19a" alt=""><figcaption></figcaption></figure>

You can also add tags to multiple files and links at once by selecting one or more items and using the icon which are then displayed in the Files tab header.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFg81XR81PsdWgsqxQ0SU%2Fimage.png?alt=media\&token=47b7cb6a-9956-441c-942e-1714a2abee5e)

Enate can also help with automated tagging of email attachments. Various options are available in the [Marketplace ](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace)section of Enate Builder to enable components (from Enate as well as third party ones) which analyse incoming mail content, including being able to suggest tags for email attachments based on their contents.&#x20;

If your admin has switched on an auto-tagging component, you'll see some extra bits of info in the file tag section, where automated suggestions of tag values for an attachment have been made.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7DjliBUjGYgVVsFAlsVK%2Fimage.png?alt=media&#x26;token=50ad2fe4-77b6-496e-8cb4-4fe37f7fc0b8" alt=""><figcaption></figcaption></figure>

If the technology you're using is confident enough about its tagging suggestion, the tag will appear in green. If you agree with the suggestion, you don't need to do anything, but if disagree with it, you can simply click to change it.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FhrGM2KnQWOm6hWEOWvmT%2Fimage.png?alt=media&#x26;token=8ca78e18-5e32-46ef-aa4e-b11d0247b8c1" alt=""><figcaption></figcaption></figure>

And if the technology was less confident in its tag suggestion, the tag will be highlighted in orange. If you agree with the suggested tag, make sure to confirm it, otherwise change it to your preference. Every time you do this, the technology will learn and get a little bit better at suggesting tags. If you notice that the technology is regularly getting its suggestions wrong, speak to your admin team about modifying the confidence threshold.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FIMxyVCb2WYDXfK5CFCST%2Fimage.png?alt=media&#x26;token=b202cf44-61da-47bf-ae5c-989b964cedc1" alt=""><figcaption></figcaption></figure>

Once tags have been added, the files/links will become available for auto-adding to emails with matching tags, allowing you to ensure that all documents of a relevant type are included with specific emails / email body content.

When a [canned response](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/emails/canned-texts) text is inserted into a manual email or when a new email is auto-created and sent in-process, the system will identify any tags linked to the canned text / email template and will then auto-attach all of that work item’s files which share the same tag. Tags are linked to the canned response / email content as part of system configuration by administrator users in Builder when creating [email templates](https://docs.enate.net/enate-help/builder/builder-2021.1/email-template-configuration).

{% hint style="info" %}
Note: If file tags are not [configured in your system](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags) then this ‘add file tag’ option will not be displayed.
{% endhint %}

## Adding Notes to Files

You can also add notes to files and links to provide a brief description of the content or to provide any other information that might be useful.&#x20;

You can also add notes to multiple files and links at once by selecting one or more items and using the icon which are then displayed in the Files tab header.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUXVe4me5Mn7AGqmEtmQa%2Fimage.png?alt=media\&token=7c06730b-d499-4828-bc7e-78d58984480a)

## Previewing Files

The menu on the right lets you preview an individual file. The preview will open in a new tab.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FdTInKAI18Z8RKC4DDxsP%2Fimage.png?alt=media\&token=395d3020-5805-4e9b-a0e3-edd90351bd33)

{% hint style="info" %}
If the file is not previewable, a confirmation banner will pop up to explain this, and to offer an option to download the file. The file types supported for preview are as follows: **txt**, **pdf**, **jpg**, **jpeg**, **jpe**, **jif**, **jfif**, **jfi**, **png**, **gif**, **web**, **tiff**, **tif**, **heif**,**heic**, **svg**, **svgz**.
{% endhint %}

## Downloading Files

You can download individual files by clicking on the option in the menu on the right.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FTcUK4hSDn8B2DFvlOTZD%2Fimage.png?alt=media\&token=262356ff-ade9-45a1-b5ea-75ad38d334a5)

You can download multiple files at once by selecting the files you wish to download and selecting the option at the top of the screen. These can be downloaded as multiple individual files or as a single compressed ZIP file via the ZIP download option here.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3TEpseIE3pJwc9suEBKD%2Fimage.png?alt=media\&token=217713a4-b82a-4cf6-8b41-c348b68b27e9)

## **Deleting Files/Links**

You can delete files or links individually by clicking on the menu on the right.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fwmg6Aj7ffpIiocroEfCq%2Fimage.png?alt=media\&token=2b22c488-83e1-407f-9134-5344c92a04a6)

You can also delete multiple files/links by selecting the files/links you wish to remove and selecting the delete option at the top of the screen.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FwSfryGedBt7Tlo1SUrWd%2Fimage.png?alt=media\&token=6271abc7-199c-4172-a737-e826760657b7)

## Filtering Files/Links <a href="#drag-and-drop-of-attachments-into-email-section" id="drag-and-drop-of-attachments-into-email-section"></a>

You can filter the files and links being displayed in the files tab by using the filter option at the top. You can filter by: Attachments, Outgoing Email Attachments, Incoming Email Attachments and Links.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzI5mpzWPSZIG7WKdTv1z%2Fimage.png?alt=media\&token=3f0c3b24-b17c-41a6-8725-734fa1534013)

### Freetext File Search

There's also a freetext search available to help you locate individual files or links. You can search based on the various text groups on display - Filename, Tag info and Notes texts.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPjawLOwhfaNmHFicxlnf%2Fimage.png?alt=media\&token=dd4647e9-3f81-4c61-bad1-32b704d4118a)
