# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-connectors-detail.md

# Email Connectors

## Adding an Email Connector <a href="#a-adding-an-email-connector" id="a-adding-an-email-connector"></a>

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTUwMTU2Mg==>" %}

To add a new email connector click on the ‘+’ icon at the top right of the Email Connectors page, select 'Email Connector' and fill out the details in the resulting popup.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MjYcgu3KLUdqczIShVr%2F-MjYdXGN6ojpcKv89Iyu%2FEmail%20Connector%20%2B%20icon.gif?alt=media\&token=2bbfd467-30fe-4cb2-ad68-f65ff0751a39)

The attributes to configure are:

| **Attribute**                 | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Email Connector Name          | Your Enate-friendly name – you can enter anything you like here as a name.                                                                                                                                                                                                                                                                                                                                                          |
| Email Service                 | <p>List of available email Services which can be used for email connectors. Options available are:</p><ul><li>Gmail (POP3)</li><li>Gmail (IMAP)</li><li>Office 365 (POP3)</li><li>Office 365 (IMAP)</li><li>Office 365 (Graph)</li><li>Other - if you select the ‘Other’ option for Email Service, you will need to specify the incoming and/or outgoing email server information, including server address, port and SSL</li></ul> |
| Username                      | The email address / username                                                                                                                                                                                                                                                                                                                                                                                                        |
| Password                      | The email address password. Maximum of 50 characters.                                                                                                                                                                                                                                                                                                                                                                               |
| Primary Email Address         | The email address of your connector. If you have multiple email addresses linked to the same mailbox, you must note the primary email address.                                                                                                                                                                                                                                                                                      |
| Can access additional mailbox | If you want to access an additional mailbox which has the same login information as this, tick the box and add the mailbox name here                                                                                                                                                                                                                                                                                                |
| Use for                       | <p>Options are:</p><ul><li>Incoming: Emails create new Tickets / Cases or link to existing.</li><li>Outgoing: Mails can be sent OUT from the system via this mailbox. If you want to reference this email connector in e.g. ‘from email address’ settings etc. within Ticket/Case configuration, you must set it as ‘outgoing/ both’ for this to work.</li><li>Both</li></ul>                                                       |

### Setting a Fallback Email Route <a href="#e-default-email-connector-for-outgoing-emails" id="e-default-email-connector-for-outgoing-emails"></a>

You must also set a fallback email route for the primary email address of each email mailbox in your system.

This will ensure that any mails arriving to that connector which don't get handled by the various email routes configured will at least be handled by this fallback and will kick off the Case or Ticket it routes to.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FE2oxSFRCM3166iJJh03u%2FFallback-Email-Connector.gif?alt=media&#x26;token=88784e32-6561-4a4e-9bd4-08ac9ca185bb" alt=""><figcaption></figcaption></figure>

When setting a fallback route you must define the work item that should be created for an email coming into that connector (if not picked up by any other email routes), i.e. the specific Ticket or Case.

You can also choose whether you want to send automatic emails (such as request acknowledgement emails) to the work item's contact when a work item has been created via the fallback route by selecting the 'Send Automated Emails' option.&#x20;

You can also choose whether you want your fallback email route to only create work items in [test mode](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/test-mode) by selecting the 'Only create work in test mode' option.

#### Behaviour After Upgrade to v2022.5

After your system has been upgraded to v2022.5, Email Connectors which do not yet have a fallback route defined will still work, and as such would still potentially allow some incoming emails to be unprocessed if they are not picked up by any of the existing email routes. **However, you should be aware of the following when configuring Email Connectors after upgrade:**

{% hint style="warning" %}

* **Any NEW Connectors which you create MUST have a fallback route specified in order to be saved and set live.**
* **Any EXISTING Connectors which you EDIT MUST also have a fallback route specified in order for you to save your changes. The Save option will be disabled until you have specified a fallback route.**
  {% endhint %}

#### Auto-Selection of Fallback Routes during Upgrade

During the upgrade to 2022.5, Enate will assess all the existing Email Routes for each Connector in your system attempt to automatically set one of these for each Connector as its fallback route. In order to qualify as an acceptable fallback route, the email route must meet the following criteria:

* Its email must match the primary email address or be set as a catch-all '\*' wildcard.
* No additional Routing Rules must exist for the Email Route.
* It must have a Ticket or Case route already defined for it.
* It must already be the last route in the ordered set of Routes for that Connector.
* It must already be Enabled.

If an Email Route for a connector meets the above criteria, its route settings will be added to the Connector (displaying in the Connector details popup), and certain aspects of the Route's configuration will become locked down, in order to ensure it remains as the fallback route. See [section below](#how-fallback-routes-subsequently-display-in-routes-section) for details of this.

#### How Fallback Routes Subsequently Display in 'Routes' Section

Whether it be as a result of auto-selecting during upgrade, or manual definition of the email route afterwards within the Connector, the email routes which have been specified will then show in your Email routes section with some specific impacts.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7U7Q7CYQ1HVAjBAb8u3B%2Fimage.png?alt=media&#x26;token=209412eb-02c1-4449-bb2d-814c27502a42" alt=""><figcaption></figcaption></figure>

Details of this are as follows:

* These routes will always display at the foot of the Email Routes list
* The Routing Rule will be set to read-only
* The Email Connector will be set to read-only
* The 'Enable' setting is set to ON, and is read-only

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0JBRc0GeaZ604jNYwu6E%2Fimage.png?alt=media&#x26;token=7df6ce67-c19a-4c7e-8925-1efc80d10c76" alt=""><figcaption></figcaption></figure>

### Testing a Connector & Setting it Live

Once you have configured the required information you must then test the connection. To do this, click on the 'Test Connection' button.

Once the connection has been tested successfully, you can then enable the connector by switching on the 'Enable' toggle.

{% hint style="info" %}
The connection will not run with unless 'Enable' is switched on.
{% endhint %}

## Editing an Email Connector

You can edit an email connector by clicking on the ellipsis and choosing 'Edit'.

When editing an email connector, you are also able to see its activity history by clicking on the Show Activity button. You can see when the email connector was created and by who, as well as if any edits have been made to the email connector, when they were made and by who.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpg6LWUc3pHK4L_bbl%2F-MWpgrKCSmVrcOtWe-rU%2Fimage.png?alt=media\&token=04995eed-c963-4f53-ad1f-e992d88492e9)

## Default Email Connector for Outgoing emails <a href="#e-default-email-connector-for-outgoing-emails" id="e-default-email-connector-for-outgoing-emails"></a>

The system has a default outgoing email Connector called ‘System Default SMTP Gateway’ for standard system activities e.g. User Welcome emails etc.

## Outgoing Email Authentication <a href="#outgoing-email-authentication" id="outgoing-email-authentication"></a>

Depending on the Email service you chose, you will have different Authentication Methods available to chose from. You can find the differnet Authentication Methods below:

#### **What authentication methods are avaiable if you choose Office 365 (SMTP Relay) as your Email Service?**

If you configure your outgoing email connector's **Email Service** as 'Office 365 (SMTP Relay)', you will be able to chose either '**Authentication Certificate'** or '**None**' as your Authentication Method.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FlILRQoOXdqRKGKWWuGyt%2Fimage.png?alt=media&#x26;token=482caad1-edba-4ba2-81c6-98debdc58531" alt=""><figcaption></figcaption></figure>

#### What do you do if you choose 'Authentication Certificate' for your Authentication method when using Office 365 (SMTP Relay) as your Email Service

If you chose the **Authentication Certificate** option, you will be presented with a file box where you can either drag and drop your **.pfx** file, or browse your files for it. Additionally there will also be a **Certification Password** box to add your connector's **Certificate Password**.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fnd0w0liE33ehl81ChMDe%2Fimage.png?alt=media&#x26;token=376b7793-2865-4611-bf4a-3a968095ce39" alt=""><figcaption></figcaption></figure>

#### **What are the authentication options if you choose Gmail (SMTP) as your Email Service?**

If you use Gmail (SMTP) as your Email Service, you can **only use Username and Password** as your Authentication Method.

<figure><img src="https://docs.enate.net/enate-help/~gitbook/image?url=https%3A%2F%2F3859925423-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MWYnDNwe3Cuo4zlGbs5-887967055%252Fuploads%252FqD3TyLMcmEj20tNSi6rC%252Fimage.png%3Falt%3Dmedia%26token%3D3ca203a1-1a6f-4cff-ab39-73d60fd6c08e&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=1c59c232&#x26;sv=2" alt=""><figcaption></figcaption></figure>

#### What are the Authenication Methods avaiable when choosing 'Other' as your Email Service?

If you configure your outgoing email connector to use 'Other' as its **Email Service**, you will be able to chose from **None**, **Username and Password** or **Authentication Certificate** as your **Authentication Method**.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F32bLdAMtgZrI31YibgL4%2Fimage.png?alt=media&#x26;token=e547f211-50dd-49b5-a0b9-c553ead8fd9b" alt=""><figcaption></figcaption></figure>

#### What to do if you choose 'Username & Password' as the Authentication method with 'Other' is set as the Email Service

If you choose **Username and Password** as your **Authentication Method**, you will be required to fill out your **Connector's Username** and you **Connector's Password**.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FWB0DYBRx9bAmtvc08149%2Fimage.png?alt=media&#x26;token=9d5be23c-5271-4caf-9574-656a2a08e29c" alt=""><figcaption></figcaption></figure>

#### What to do if you choose 'Authentication Certificate' as the Authentication Method with 'Other' is set as the Email Service

If you choose the **Authentication Certificate** option, you will be presented with a file box where you can either drag and drop your **.pfx** file, or browse your files for it. Additionally, there will also be a **Certification Password** box where you will be able to configure your connector's configuration password.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMqKNwbCJgifQYF1bdX57%2Fimage.png?alt=media&#x26;token=e92a9e1d-f9b6-4e1c-97bd-710585c45766" alt=""><figcaption></figcaption></figure>

## Automatic disablement of email connectors

There are some scenarios in which an email connector may be automatically disabled, as follows:

* If client secret authentication for Office 365 integration is expired, then after multiple attempts (defined in Builder), Enate disables the connector automatically.
* If the mail server does not respond to Enate API calls to poll, after multiple attempts (defined in Builder), Enate disables the connector automatically.
* For non Graph API connectors, if the Password expires Enate disables the connector automatically.
