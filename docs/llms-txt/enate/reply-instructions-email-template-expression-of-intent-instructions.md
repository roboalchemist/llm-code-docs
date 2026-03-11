# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-template-configuration/reply-instructions-email-template-expression-of-intent-instructions.md

# 'Reply Instructions' Email Template - 'Expression of Intent' Instructions

When your Enate system is set to use 'Plus Addressing Only' mode for how it processes and routes emails, your end clients will now see  an additional line auto-inserted into the emails they receive. This line contains guidance on how to best respond to the email, based upon their intention to either start a new business request or continue correesponding on the same item. This is the new line they will see.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FbaE1nEAiZt9taScggZtt%2FEmail%20Intent.png?alt=media&#x26;token=1678b4c4-197d-4bfb-81f9-5eaf98392ddd" alt=""><figcaption></figcaption></figure>

By default, the content will read as follows:

<mark style="color:blue;">'##- For responses related directly to this request, please send a reply email. Please do not adjust any email addresses in this mail. For NEW requests, please create a brand new email instead. -##'</mark>

The intention here is to avoid erroneously creating brand new tickets from incoming emails where the client really intended just to continue correspondence. The note regarding email addresses is to encourage client users to leave Plus Addressing-style email addresses as-is rather than removing or adjusting them when they send a response back in.

### Email Template: 'Reply Instructions'

As part of this new feature, a new 'Reply Instructions' Email template is available within the Email Templates of Builder. This will allow users with the required feature access to specify alternative content that you wish to show to your client users instead of the default.

### How will work manager users and client users see the reply instructions

If the reply instructions are on a *manually written* email, the reply instructions will appear just above the Enate user's signature.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F9AWf7lFrDumg5O93SeLv%2FRepl1.png?alt=media&#x26;token=e3a6da29-ba82-41d8-93d6-295410986afb" alt=""><figcaption></figcaption></figure>

If the email is one which has been *automatically generated* by the system, these reply instructions will appear directly at the top of the email body text.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7w7ldVbiTZQIrJoNeEan%2FRepl2.webp?alt=media&#x26;token=b5e2cb77-965e-4a12-92b3-b627fbcf225f" alt=""><figcaption></figcaption></figure>

## Configuring - How to enable the Reply Instruction template

The 'Reply Instructions' template will only be available to be used when the 'Plus Addressing Only' option is toggled on in the 'General Settings' of Builder. When this option is enabled, users will see a notification message saying that the 'Reply Instructions' template is enabled as well as a link to allow the user to view/ modify it.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F750ZMCbGeX3HZqU6ouQP%2Fimage.png?alt=media&#x26;token=94c30ccc-9014-4c62-9f7b-26f4e3ff8d99" alt=""><figcaption></figcaption></figure>

### How to modify the Reply Instructions template

Builder users can reach the template by either clicking on the link that appears in general settings or by finding it from the template list in the same manner they can find all other Email templates. If users have the ability to edit templates turned on then they can select to edit the template, otherwise users can only view it. If a user clicks to edit the template they will see that the purpose of the template is already set to 'Reply Instructions'. This cannot be changed, however the name of the template can be modified.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnAhCjMI75YXHIqGZNnvF%2Fimage.png?alt=media&#x26;token=9a043477-6179-4044-b9ac-ccc7c32a0ffe" alt=""><figcaption></figcaption></figure>

Users will be presented with default description text and default instruction text in the body of the email. Both of these default texts can be edited.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjxC1UABf6uBfkUqXW9vi%2FDescr.png?alt=media&#x26;token=990461f9-d5d5-4879-b748-04011e42c0f6" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8Eu94ujawjP6NrPClDYA%2FEdit%20Email%20Intent%20template.png?alt=media&#x26;token=8b69b749-df1f-46f5-a436-b0f5caa6baa3" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
It should be noted that only **one** 'Reply Instructions' template can exist in the system and therefore users will not be able to chose reply Instructions as an option in the Purpose drop down when creating other templates.
{% endhint %}

#### Which users can edit the Reply Instructions template

For users to be able to edit the 'Reply Instructions' template they must have the option to edit templates enabled in User Roles. By default, users with 'System Administrators' Builder Role will be able to edit the 'Reply Instructions' default email. Add 'Edit Email Content' to the Builder User Role of other people you wish to have this access.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPfBuFGdWLuoQLkDlRR1w%2FUser%20Roles%20-%20Email%20Template.webp?alt=media&#x26;token=e52161d8-adfd-4a81-908b-fe6f3d50dad6" alt=""><figcaption></figcaption></figure>
