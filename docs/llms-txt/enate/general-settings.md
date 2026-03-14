# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings.md

# General Settings

As part of [system-level settings](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings), the following general settings can be configured:

{% hint style="info" %}
Changes you make to general settings will only take effect after logging out and logging back in again.
{% endhint %}

## **Keep with user**

This setting can determine if items which are set to longer-term pauses, or upon re-opening, should default to assigning back to the last user to perform any activity on it.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FsofQZ7KgJaxkhTB0vvWg%2Fimage.png?alt=media&#x26;token=8f138b42-fbf0-4799-90da-bfdc5c589c82" alt=""><figcaption></figcaption></figure>

## Show Time Tracker

This setting will enable the display of the elapsed time tracker card on Work Items. Not enabling this setting, means elapsed time will still be tracked but service agents will not see the time tracker display.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5UZybNOcgTcFxgoxgKO0%2Fimage.png?alt=media&#x26;token=879696a9-5ddf-4982-bde3-5bddbe1da20d" alt=""><figcaption></figcaption></figure>

## **Display Expected Times in Time Tracker**

This setting allows the expected amount of time it should take to carry out an activity to be displayed in the the Time Tracker card for Work Items in Work Manager.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4GdFZovoqZCegdc5HDH8%2Fimage.png?alt=media&#x26;token=0f9c6288-30c6-46fc-983f-3469c7129e5d" alt=""><figcaption></figcaption></figure>

## Show Effort Estimation

This setting enable users use Effort Estimation on Work Items, allowing better planning of resource requirements.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVMcxiDCkuzE09khmHgQ6%2Fimage.png?alt=media&#x26;token=975d7bb3-223d-4354-90a5-a27b4f023eba" alt=""><figcaption></figcaption></figure>

## **Email or Note Required on Ticket in Order to Resolve**

This setting allows you to specify if Tickets will require a resolution email / note to be added to a Ticket before it can be marked as ‘Resolved’. Note that upon an upgrade, this setting is ticked to maintain the previous behaviour.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FHaSGtmrdeInceXK9l315%2Fimage.png?alt=media&#x26;token=a97d24f2-dbb5-43d4-9bfc-ae0c821a573d" alt=""><figcaption></figcaption></figure>

## **Show Parent Company**

This allows you to more easily manage your companies by creating a nested company structure where a parent company can maintain multiple child companies.&#x20;

A parent company can have multiple child companies, but a child company can only have one parent company. A parent company cannot have its own parent company and a child company cannot be set as a parent company. Please note that a company cannot be both a Supplier and a Parent Company.&#x20;

Additionally, a Work Manager user will be able to start work items for both parent and child companies for a parent company contact; however they will only be to start a work item for a child company for a child company contact.&#x20;

The Contacts Card in Work Manager for work items running against a parent company will show the contacts of that parent company, but will not show any child company contacts, however work items running against a child company will show the contacts of that child company as well as of the parent company.

Once a parent company has been set, you can edit or remove it IF there are no running work items with contacts that are scoped to the current parent company. If this is the case, you will only be able to change the parent company once all of these work items have closed and there are no more running work items with contacts that are scoped to the current parent company.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZXEc3EdbTnZiLNAmleMa%2Fimage.png?alt=media&#x26;token=1256d41b-41de-44da-ba36-3a9bce3f71e4" alt=""><figcaption></figcaption></figure>

## **Enable Automatic Contact Creation**

This setting allow contacts to be auto-created when an incoming email has been received from an unknown email address. This setting is set to ON by default. Note that the company set to an auto-created contact will depend on the [contact scope setting](#contact-scope) you have set. If it is set to 'Global', or 'Global and Local', the auto-created contact will have a Global scope. If it is set to 'Local', the auto-created contact will have a Local scope.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvbyUc7ZJtadlAfknMLvQ%2Fimage.png?alt=media&#x26;token=7261acb9-745b-466c-a861-9db50eb9f8b1" alt=""><figcaption></figcaption></figure>

## Employee Availability Insights

This option allows Agent users to provide data around their daily time spent outside of Enate (for things like meetings, training etc.), to give Line Managers greater visibility of availability, helping with workforce scheduling and more efficient resource allocation.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXh83V88AqVCw3xLsLVaj%2Fimage.png?alt=media&#x26;token=ff15cf33-264f-4a07-8cb2-51ff12529d87" alt=""><figcaption></figcaption></figure>

## Show Process Group Information

This setting lets you decide if you want to show or hide process group information in both Builder and Work Manager.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5dfaPfkxOOjTk86tJuds%2Fimage.png?alt=media&#x26;token=6a4246bf-66aa-4086-8e33-de38d9102a56" alt=""><figcaption></figcaption></figure>

If the setting is off, all process group labels and fields will be hidden.

{% hint style="info" %}
Note that if a user tries to switch off the option after having added process group information, they will not be able to switch it off.
{% endhint %}

## Work Item Plus Addressing

When new emails arrive into Enate, the system analyses the email to determine whether it’s a brand new request or related to an existing one, and then determines how to proceed.

The Work Item 'Plus Addressing' setting is where you decide how you would like your incoming emails to be processed. The options are as follows:

* **Plus Addressing OFF** - Plus Addressing is completely disabled and emails are matched using the standard email processing rules only (i.e. those not used in Plus Addressing).
* **Mixed** **Mode** - Plus Addressing is enabled and emails are matched using both plus addressing AND the standard processing rules standard email processing rules.
* **Plus Addressing Only** - Plus Addressing is enabled and emails are matched using plus addressing ONLY.

Check out our dedicated Email Processing options article here:

{% content-ref url="../email-mailbox-configuration/incoming-emails-processing-logic" %}
[incoming-emails-processing-logic](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic)
{% endcontent-ref %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUCUP0heWJPB4mQzhYK8Y%2Fimage.png?alt=media&#x26;token=d98b452e-68b7-4e70-a2f3-ecdb86aee9b5" alt=""><figcaption></figcaption></figure>

#### Match by Work Item Reference in Email Subject or Body\*

*\*Note: This option is only available for older clients who may previously have been using this approach in earlier product versions. This method is not available for any new setups going forward, and clients who have this option are encouraged to switch if OFF as an approach to use in the long term.*

*Additionally, this option is only available for older clients if **Mixed Mode** or **Plus Addressing OFF** have been toggled on.*

This setting enables matching based on the Work Item reference in the email subject or body.

{% hint style="warning" %}
Caution: Existing clients who have this option available in General Settings are strongly encouraged to switch this option OFF, as it could lead to data breaches if incorrect or irrelevant work item references numbers are present in an incoming email subject or body.
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBv8l55tZXxhzAyHpefZf%2Fimage.png?alt=media&#x26;token=b677bb5d-1c2b-49a3-b786-639dcc1df126" alt=""><figcaption></figcaption></figure>

### Hide Work Item Matching Data in Email Addresses

Enabling this option will add a 'Reply To' header for outbound emails where work item matching data will NOT display as plus addresses in the 'From' address.&#x20;

The impact of this is that if the setting is enabled, instead of seeing emails with&#x20;

'*<jane.smith+12345-T@acmecorp.org>*' in the from field, it will instead show simply as&#x20;

&#x20;'*<jane.smith@acmecorp.org>*'.

{% hint style="info" %}
Note that this option is only available if some form of plus addressing is enabled (i.e. either Mixed Mode or Plus Addressing Only mode have been selected) and it is set to off by default.
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FIzpJAFT49hTWinw3Igw7%2Fimage.png?alt=media&#x26;token=4381607c-eaf8-4064-a85b-60ae9ae0ae11" alt=""><figcaption></figcaption></figure>

#### **Further** information about how Enate matches emails

See here for more information about how Enate processes incoming emails:

{% content-ref url="../email-mailbox-configuration/incoming-emails-processing-logic" %}
[incoming-emails-processing-logic](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic)
{% endcontent-ref %}

## **Enable WebSocket Integration**

This setting allows you to take advantage of WebSockets to improve performance. If WebSockets are not supported, you should disable this option to revert back to a fallback method.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fkz2YEpxgEn7coU4d0fOr%2Fimage.png?alt=media&#x26;token=28eef4a0-ec02-4093-8a66-dc70e1944059" alt=""><figcaption></figcaption></figure>

## **Allowed File Types**

Here you can specify the file types that you want your platform to accept. Leaving the box blank means that all file types will be accepted. The following file types will be set as default:

* txt
* pdf
* xls
* xlsx
* doc
* docx

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FLSoOKPWVpXP7s5QrukZv%2Fimage.png?alt=media&#x26;token=a88b9fc2-6697-4e81-8bf2-77c8be41d45c" alt=""><figcaption></figcaption></figure>

## **Unmonitored Email Address**

The email you supply here will override the default outgoing email address on communications which cannot be responded to.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0GVzCOAI1pjUL2eoe1QK%2Fimage.png?alt=media&#x26;token=009cf67f-ccb9-44a6-b03d-9e74eb201ed1" alt=""><figcaption></figcaption></figure>

## Maximum Email Size

This setting determines the maximum size allowed for outgoing emails. Users won't be able to send, schedule, or save as a draft emails that exceed this limit.

{% hint style="info" %}
Please note that the validation of the email size occurs as part of saving the email, not at the sent time. So if a 25MB email has been scheduled and then the maximum email size gets reduced in Builder to 10MB, the scheduled email will still be sent as it conformed to the size allowance configured when it was scheduled.
{% endhint %}

Additionally, it is recommended that you configure the limit to 30% less than what you want your end-users to write as as an extra buffer to accommodate encoding etc. e.g. if you want the maximum size of 100MB, we would recommend setting the limit to 70MB.&#x20;

{% hint style="info" %}
Note that the maximum email size allowed by Enate is 100MB. Also note that the size limit will not be applicable to system-generated emails, such as Request Acknowledgement emails.
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FEfKz0KMve8Vp4aCvJOgQ%2Fimage.png?alt=media&#x26;token=108ef211-e3b7-4732-b925-fd84eba88efb" alt=""><figcaption></figcaption></figure>

## **Maximum File Upload Size**

This setting determines the maximum size of a file that can be uploaded to a Work Item or Email in Enate Work Manager, with the absolute maximum file size setting available being 100MB.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fj8twvUQeLns2u1JBJIJf%2Fimage.png?alt=media&#x26;token=f682561f-2f41-4633-969b-44620aa1987f" alt=""><figcaption></figcaption></figure>

## **Automated Failure Retry Pattern / Polling Frequency**

This lets you set:

* **The** **number of times the system will automatically retry to send an email** as well as the...&#x20;
* **The number of times your mailboxes are polled when checking to see if there are any emails to be processed**.&#x20;

Use the slider to adjust the frequency. This can be set up to a maximum of 10 times.&#x20;

You will see the time intervals that the system will automatically retry to send the email or poll a mailbox which increase exponentially with each retry.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fkk3bmbVDwn3HA2SwxgjM%2Fimage.png?alt=media&#x26;token=553a44b8-8918-4451-8e94-a80926ce70ff" alt=""><figcaption></figcaption></figure>

Once the system has retried sending an email 10 times, it will no longer retry sending it automatically, but you can still retry sending the email manually, i.e. by clicking the 'Retry' icon.

## **Contact Scope**

This lets you change the scope of your external contacts to either Global, Local or Global and Local.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FWKkzdpAODqZY04hw1tT1%2Fimage.png?alt=media&#x26;token=181bdde5-7bec-47ab-b5aa-708078f9f7e9" alt=""><figcaption></figcaption></figure>

### Global&#x20;

* Setting the contact scope to Global means that all the external contacts are scoped to Global/All Companies and those contacts can access/create work items of All the Companies.&#x20;
* Contact Creation in Work Manager : All the contacts created via Quick Find search or contact card in work item and Bulk creation are by default scoped to Global/All Companies.

{% hint style="info" %}
Please note that selecting this option will clear the company relationship from every external contact.
{% endhint %}

### Local

* Setting the contact scope to Local means that all the external contacts are scoped to a particular company and those contacts can access/create work items of the particular scoped company.&#x20;
* Contact Creation in Work Manager : All the contacts created via Quick Find search or contact card in work item and Bulk creation provides an option to set the scope of the contact to particular company.&#x20;
* Search from Contact Card: users in Work Manager will only be able to search for external contacts belonging to companies which the contact has associated to.&#x20;
* Scope Change in Work Manager : Any locally scoped contact can be changed to a different company when the contact has no active work items associated. If the contact has associated work items the contact should be removed from the work items to change the scope successfully.

{% hint style="info" %}
Please note that it is only possible to set the scope to Local if all existing external contacts have a company associated with them. This can be achieved by editing them in the Contact Management view in Work Manager.
{% endhint %}

### Global and Local&#x20;

* This setting lets you set some external contacts to Local and some to Global. This means that you can assign some external contacts with a company (and therefore users in work manager will only be able to create and work items for these 'local' external contact for the particular company that the external contact is associated with), and you can assign some external contacts as 'Global', so users in work manager will be able to create work items for all companies for these 'Global' external contacts.&#x20;
* Contact Creation in Work Manager : All the contacts created via Quick Find search or contact card in work item and Bulk creation provides an option to set the scope of the contact to particular company or set the scope to Global/All Companies.&#x20;
* Search from Contact Card: users in Work Manager will be able to search for all external contacts which are associated to company to which work item is associated and all other global external contacts.&#x20;
* Scope Change in Work Manager : Any locally scoped contact can be changed to Global and any globally scoped contact cannot be changed to a particular company if the contact has associated to work items of multiple companies, in this case the contact should be removed from the work items of other companies.

### Contact Scope vs. Permissions

It is important to take the user permissions settings you have created when setting Local / Global Contact scoping:&#x20;

{% hint style="info" %}
**Please note: Locally-scoped contacts are visible only to users with permission on specific companies or parent companies, while Global contacts are visible to all users.**
{% endhint %}

## Privacy Policy

This setting allows you to add a link displaying your company's privacy policy to the Enate login page.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FdJQDgii20XHCfBHWEvXs%2Fimage.png?alt=media&#x26;token=7d6a6ee7-7476-436e-a933-6a7e7544419d" alt=""><figcaption></figcaption></figure>

## Additional BCC Address

This option can be used at a system level for sending a hidden email copy of all outgoing emails sent by the system to an address for tracking or archiving.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCCsYsFIp84jZzSqvaHBO%2Fimage.png?alt=media&#x26;token=fa01f9e0-e8f0-4c61-b2db-6c6016ebd3cc" alt=""><figcaption></figcaption></figure>

Multiple email addresses can be specified, using a ',' comma separator in between.

## Override 'To' Address

Populate this field if you wish to redirect all outgoing emails to this email address / list of addresses, overriding the original recipients.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fvm9kfRnJM5hVSdF0VZxr%2Fimage.png?alt=media&#x26;token=a36c4ebb-f61d-4248-a8cb-cf0a3a877966" alt=""><figcaption></figcaption></figure>

Multiple email addresses can be specified, using a ',' comma separator in between.

{% hint style="warning" %}
NOTE: This setting **should not** be used in live production environments, as it will prevent emails from reaching their intended recipients.
{% endhint %}

## Override 'CC' Address

Populate this field if you wish to replace all CC recipients on outgoing emails with this email address / list of email addresses.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FS9v66wPP40xMpnl5A2eq%2Fimage.png?alt=media&#x26;token=19228b20-adcf-4de5-a28f-f2f14ffa4821" alt=""><figcaption></figcaption></figure>

Multiple email addresses can be specified, using a ',' comma separator in between.

{% hint style="warning" %}
NOTE: This setting **should not** be used in live production environments, as it will prevent emails from reaching their intended recipients.
{% endhint %}

## Override 'BCC' Address

Populate this field if you wish to replace all BCC recipients in outgoing emails with this email address / list of addresses.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1HEsfmb1yhwhXtE0DP29%2Fimage.png?alt=media&#x26;token=e6fa3f07-6a2c-4a60-8d65-ae37025813e1" alt=""><figcaption></figcaption></figure>

Multiple email addresses can be specified, using a ',' comma separator in between.

{% hint style="warning" %}
This setting **should not** be used in live production environments, as it will prevent emails from reaching their intended recipients.
{% endhint %}

## Maximum Session Duration

This option allows you to set the time the system will wait before logging out log out users after a period of activity (e.g if the active session timeout is set to 30 minutes, then though you are active, you will be logged out after 30 minutes). The maximum time you can set is 23:59:00 hours. If you leave this option blank, it will default to zero, meaning that no time has been set and the session does not expire for a still active user.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FqBvfiZcIENFscbR9ICBV%2Fimage.png?alt=media&#x26;token=9463f0f9-cb4e-4f0f-8e9a-2a699873aad4" alt=""><figcaption></figcaption></figure>

## Maximum Idle Duration

This option allows you to set the maximum time that user can remain inactive before the system will automatically log them out. (e.g if the idle session timeout is set to 15 minutes, you will be logged out if your account is idle for 15 minutes). The maximum time you can set is 23:59:00 hours.&#x20;

{% hint style="warning" %}
**If this value is set to blank it will default to zero, i.e. user sessions do not expire.** **For security reasons, it is NOT recommended that this value be set to blank.**
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUEwgfcFYPa1j4wbLirHq%2Fimage.png?alt=media&#x26;token=176a3473-178b-4056-b027-750641a9426c" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**NOTE: For security reasons, it is NOT recommended that this value be set to blank.**
{% endhint %}

## Company Logo

This option allows you to set your company that will appear alongside the login section on the initial login screen.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fag8xC5bwRkQSDkPWGj8f%2Fimage.png?alt=media&#x26;token=9f7cd631-5924-49fa-b189-c1103595b2b4" alt=""><figcaption></figcaption></figure>

## Header Logo

This option allows you to set the header logo that appears in the top left corner of the Work Manager and Builder screens.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FI2ggBJFNzydwKP76TGp1%2Fimage.png?alt=media&#x26;token=81296c8c-57bc-4eda-a952-4b16ad9c5e99" alt=""><figcaption></figcaption></figure>

## Favorite Logo

This option allows you to set the logo to use as the browser tab icon for all of your Enate tabs.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FY5g6In5ojII35NzXXb7N%2Fimage.png?alt=media&#x26;token=b300a2db-ef80-4baa-9af5-a7071ce0e2ba" alt=""><figcaption></figcaption></figure>
