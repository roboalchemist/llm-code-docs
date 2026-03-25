# Sinch Documentation

Source: https://docs.sinch.com/llms-full.txt

---

# Introduction

> Detailed documentation for the **Sinch Latam WEB messaging platform**. Discover how to use our features, learn about types of deliveries, reporting, and much more.\
> \ <mark style="color:$danger;">**IMPORTANT:**</mark> This site is for our LATAM customers – if you are interested in the Global Sinch Documentation then please visit our Global Sinch Developer Documentation site: <https://developers.sinch.com&#x20>;

## Supported Languages:

[Spanish - LATAM](https://support-latam.wavy.global/) \
[Portuguese](https://docs.wavy.global/)

##


# Glossary

Learn more about important terms in our platform

## **A**

**Account or Customer ID**

Usually, each customer number has an account identifier; this number is also referred to as Customer ID.

## **API**

API, or Application Programming Interface, is a set of [routines](https://en.wikipedia.org/wiki/Subroutine) and standards established by a [software](https://en.wikipedia.org/wiki/Software) for the use of its features by applications that do not intend to involve themselves with the software’s [implementation](https://en.wikipedia.org/wiki/Software_implementation) details, but only use its services.

## **B**

### **Blocklist**

Unlike the Whitelist, the Blocklist are numbers that the company adds and classifies as numbers that may not receive messages. E.g.: numbers from competitors.

## **C**

### **Carrier**

You are also the customer of a Carrier! By Carrier we mean the Service Provider that holds the number in question. I.e., if I have a TIM number, then the Carrier of my MSISDN is TIM.

### **Closed Session?**

A closed session is when more than 24 hours have passed from the user’s last contact or when there has been no contact from the user.

This way, in order for the company to open the session with the user once again, it needs to actively trigger an HSM, for example.

### **Conversion Rate**

Conversion rate (used especially by international customers) is the formula used to measure the number of messages sent and received VS the delivery volume. When there is a decrease in the DR, customers are directly affected in the conversion rate, and it may direct traffic to another SMS broker that has a better conversion rate.

## **D**

### **Deploy**

A Deploy is every update, release or new version of a feature. It can be under approval or in production, and all deploys improve or remove a certain feature.

### **DR or DLR (Delivery Report)**

DR, or Delivery Report, is the successful delivery confirmation status at the carrier. If the MT was successfully delivered, the DR will confirm the time of delivery of this SMS to the user. Note that if, at the time the SMS is sent, the device is turned off or has no signal, the DR time will be delayed.

## **F**

### **FTP**

FTP or File Transfer Protocol is a form of transferring files. It can refer to both the protocol and the program that implements said protocol. Transferring data in computer networks usually involves transferring files and accessing remote file systems (source: Wikipedia). This system is often used at Sinch for uploading large batches. Each platform (WA or SMS) must respect a pre-established format.

## **L**

### **LA**

LA, or Large Account, is a short number (up to digits) that is used to send the SMS. The numbers belong to the carriers and may only be used by approved partners.

## **M**

### **MO**

MO, or Mobile Originated, is every message that originates from a device to the company in question. It is used in the case of questions and answers via messages, when user confirmation is required.

### **MSISDN**

You certainly own an MSISDN! A Mobile Station International Subscriber Directory Number, or MSISDN, is a number that exclusively identifies a subscription to a GSM or UMTS mobile network. To make it even simpler, it is your cell phone number. In technical terms, all numbers of a carrier are referred to as MSISDNs. So, whenever you read MSISDN, you already know it refers to the cell phone number in question.

### **MT**

MT, or Mobile Terminated, is every message that is destined for the user’s device. I.e., the company sends a message to the number in question.

## **O**

### **Open Session**

When we initiate a contact or the user initiates the contact organically, we start counting it as an open session, as the company has 24 hours after the user’s interaction as a channel “open” for communication.

It also means, in the case of WhatsApp, that the company can send the user any MT and not just HSM (which requires approval from Facebook) like when the session is closed.

### **Opt-in**

Opt-in is the permission given by the user for a company to contact them through a given channel. This permission can be, for instance, through the website of the company itself, via email or SMS.

### **Opt-out**

Opt-out is when the user chooses to no longer receive messages from that contact through a given channel. When a user opts out of a contact list, our system blocks any delivery attempts that may occur to the user from that contact.

## **S**

### **Subaccount**

Within Sinch, we have an architecture that enables our customers to use the same number to serve multiple purposes.

Within an Account, you can have multiple Subaccounts with customized “departments” and settings, where you can trigger many different options such as service, CRM, Request Status, among others.

Each subaccount can have its own users and webhook, this enables the optimization of a customer’s number.

## **V**

### **VPN**

A VPN, or Virtual Private Network, is a private communications network built on a public communications network (such as the [Internet](https://en.wikipedia.org/wiki/Internet)). Data traffic is carried by the public network using standard [protocols](https://en.wikipedia.org/wiki/Communication_protocol), not necessarily secure. In summary, it creates a secure and encrypted connection, that can be considered a tunnel, between your computer and a server operated by the VPN service.

## **W**

### **WhatsApp Template**

A template used to send active messages to your customers. Every template must be approved by WhatsApp prior to its usage – this way, they ensure that you are following their guidelines for allowed content.

### **Webhook**

A webhook is the information bridge between our Sinch system and the company that owns the Webhook.

This bridge is done through a URL where information passes between our system and the system desired by our customer.

### **Whitelist**

Users on the Whitelist are users that the company adds and classifies as users that may receive messages. This does not mean that said user has given permission at any time.


# Sinch | Latam Messaging Documentation

Empowering our customers to create valuable experiences through technology.

## ​Sinch Latam Messaging Platform​

### Let’s begin!

Welcome to our documentation!

Know some of the main sessions of our platform:

## Initial Sessions

* ​[**Login, Language & Menu**](https://docs-latam.messaging.sinch.com/getting-started-menu/sinch-messaging-platform/login-language-and-menu)​
* ​[**Account** **& Settings**](https://docs-latam.messaging.sinch.com/getting-started-menu/sinch-messaging-platform/account-and-settings)​
* ​[**Dashboard**](https://docs-latam.messaging.sinch.com/getting-started-menu/sinch-messaging-platform/dashboard)**​**
* **​**[**Reports**](https://docs-latam.messaging.sinch.com/reports)**​**
* **​**[**Campaigns**](https://docs-latam.messaging.sinch.com/send-a-message/campaigns)**​**
* ​[**Contacts**](https://docs-latam.messaging.sinch.com/getting-started-menu/sinch-messaging-platform/contacts)**​**
* **​**[**Groups**](https://docs-latam.messaging.sinch.com/getting-started-menu/sinch-messaging-platform/groups)**​**

### How to Send a Message

* **​**[**How** **to Send a Message**](#how-to-send-a-message)​
* **​**[**How to Set Up a File**](https://docs-latam.messaging.sinch.com/send-a-message/how-to-set-up-a-file)​
* **​**[**Campaigns**](https://docs-latam.messaging.sinch.com/send-a-message/campaigns)**​**
* **​**[**Correlation ID**](https://docs-latam.messaging.sinch.com/send-a-message/correlation-id)​
* **​**[**Tracking Sent Messages**](https://docs-latam.messaging.sinch.com/send-a-message/tracking-sent-messages)**​**

### Reports

* **​**[**Viewing & Exporting Reports – Consolidated & Detailed**](https://docs-latam.messaging.sinch.com/reports/viewing-and-exporting-reports)​​
* **​**[**WhatsApp Lists**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/whatsapp-lists-via-api)​

### Permissions

* **​**[**Subaccounts & Users**](https://docs-latam.messaging.sinch.com/permission/subaccounts-and-users)**​**

### SMS Menu

* **​**[**SMS Template**](https://docs.wavy.global/sms/template-sms)**​**
* **​**[**SMS Bot**](https://docs-latam.messaging.sinch.com/sms/sms-bot)**​**

### WhatsApp Menu

* **​**[**WhatsApp Guidelines**](https://docs-latam.messaging.sinch.com/whatsapp/whatsapp-guidelines)​
* **​**[**HSM – What Is It?**](https://docs-latam.messaging.sinch.com/whatsapp/template)​
* **​**[**Registering an HSM**](https://docs-latam.messaging.sinch.com/whatsapp/registering-a-template)​
* ​[**WhatsApp Account Settings**](https://docs-latam.messaging.sinch.com/whatsapp/whatsapp-account-settings)​​
* **​**[**Webhook**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/webhook)**​**

### Technical Documentation - APIs & Integrations

**APIs & Integrations**

* **​**[**Introduction - Types of Integration**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/introduction-integrations)​
* **​**[**SMS API**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/sms-api)**​**
* **​**[**Email API**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/email-api)​
* **​**[**Fallback API**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/fallback-api)​
* **​**[**WhatsApp API**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/whatsapp-api)​​
* **​**[**WhatsApp Lists via API**​](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/whatsapp-lists-via-api)
* **​**[**WhatsApp Messaging via FTP**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/whatsapp-messaging-via-sftp)​
* **​**[**Campaigns API**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/campaigns-api)​
* **​**[**TTL - Time to Live**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/untitled-2)​
* **​**[**Webhook**](https://docs-latam.messaging.sinch.com/technical-documentation/api-and-integrations/webhook)**​**

####


# Login, Language & Menu

Learn more about the initial browsing of our platform

### **Login**

![messaging.sinch.global](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlGYdBZT1FF2BKlnKLx%2F0.png?generation=1633455871254871\&alt=media)

This is our home screen. There you can log in or access our website by clicking [**What is Sinch?**](https://latam.sinch.com/)

Login: Can be done using your **email** or **username**

If you have forgotten your password, click on **I forgot my password** and enter your email in the following step.

You can also change your password by [**clicking here**](https://messaging.wavy.global/password). You will receive an email to register your new password.

**Language**

In the upper right corner, you can choose between the 3 available languages for Sinch Messaging: **Portuguese BR** (🇧🇷), **Spanish** (🇪🇸) or **English** (🇬🇧)

![language](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FTNd31RlwFHS2SBh3ITYw%2Fimage.png?alt=media\&token=90649ce3-c802-43c1-b496-6b8d7fb52e39)

### **Menu**

On the left side menu, you can find the main sessions within the platform:

![left side menu](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FHuh7LDECEuaw2ybaDGB1%2Fimage.png?alt=media\&token=04a18220-800c-410e-bd24-5964cc796b76)

### **New Message**

* **SMS PLANS** (Available only for **Pre-Paid** Customers);
* Home;
* Messaging;
* Flow Builder;
* Solutions;
* WhatsApp (Available only for Contract customers);
* Settings;
* Help;

### **Messaging**

* Messages sent;
* Campaigns;
* Reports;
* SMS templates;
* Blocklists;
* Contacts;
* Groups;

### **Flow Builder**

* SMS Bot;

### **WhatsApp**

* Account;
* Inner panel;
* Templates;
* Dashboard;

### **Warm Up**

* Start;
* Track;

### **Settings**

* My account;
* Subaccounts and users;

{% embed url="<https://docs.wavy.global/getting-started/wavy-messaging-platform>" %}


# Account & Settings

Access credentials and basic settings, email, and password

**Clicking your username in the top right menu, you can access your account information:**

{% hint style="success" %}

* Your credentials
* Name
* Email
* Password
  {% endhint %}

## **My Profile**

![my profile](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FcGf9wDpWLu2YhpyKhDfk%2Fimage.png?alt=media\&token=1b653336-623f-4109-8c77-a79f043b494d)

## **Your Credentials**

Your account details: Your username, Customer, Subaccount, and your Authentication token.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FtPkGhYvZPlLBUZeDjVpe%2Fimage.png?alt=media\&token=ea785ab0-981d-428e-9dcf-9a3e00be25fa)

{% hint style="info" %}
**Your Credentials are**:&#x20;

• The Customer you belong to&#x20;

• The Subaccount you are associated with&#x20;

• Your Authentication Token
{% endhint %}

## **Name, Email, and Password**

![For illustration purposes only. In this session, you will see your data in email and username.](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlGYkz_dXFqM8mgJ4y4%2F2.png?generation=1633455903137573\&alt=media)

{% hint style="info" %}
You can change your profile name, email and password.
{% endhint %}

​


# Contacts

Learn how to edit, delete or create new contacts.

## Contact List

Under contacts, you can find your whole customer base that has already been imported into the platform.

#### Adding a New Contact

{% hint style="info" %}
Click the **+ single contact** button in the **contacts** menu and fill out the form; fields with a **\*** are required. **You can choose to add this new contact to an existing group.** Click **save**. There you go! Your new contact has been created. Or you can **import multiple contacts** at once by uploading a spreadsheet.
{% endhint %}

#### Adding a single contact:

1. ![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fp7Fq90scb3PuA3cjSII2%2Fimage.png?alt=media\&token=5f8cc548-d00f-4a6a-991f-4114e24b29d2)&#x20;
2.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FEGDyCMQSV8sTVPtwXqp6%2Fimage.png?alt=media\&token=cbedf50c-ed5d-47b3-877f-645f83543db3)

#### 3. Fill out the fields below for creating your contact.

### Adding bulk contacts:

Click on Import Contacts:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FnVrET2La7QJZxFxFyTXO%2Fimage.png?alt=media\&token=89a32b22-2dac-4660-a8dc-d56657700672)

Click on download template and fill in the spreadsheet according to the template. Save in CSV format and then upload to platform.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FWAa7yJiPv8YBMqt9i73c%2Fimage.png?alt=media\&token=e84886ba-caae-4022-badf-e09d20fc6de7)

### Editing a Contact

In the "actions" column, you can edit the information of each contact.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FGJMXVzqW7eTU77hIizEl%2Fimage.png?alt=media\&token=7e2556a8-efc6-4d00-98bb-ba86f8adfe34)


# Groups

You can create groups with your contacts and target selective triggers at certain people. This way, you only send what your customer wishes to view.

{% hint style="danger" %}

### We are not referring to WhatsApp groups, only groups of people for deliveries.

{% endhint %}

### How to Create a Group

{% hint style="info" %}

* Click **+ Group**
* Enter name and description
* Click **Create**
  {% endhint %}

###

### Editing a Group and Adding Members

By clicking on **Actions > Edit**, you can edit the group’s name and description.

By clicking on **Delete Group**, you delete it from your list.

To add members, switch the tab.


# Send a fast message

To send SMS more quickly and simply, use the "quick send" available in the "New message" menu

Click on new message and then select quick sms:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FsnKOyZUSgGv4sWytwXVu%2Fimage.png?alt=media\&token=c606ad82-7b36-4f85-9be6-1bb9ba5f4115)

### Recipients:

You can choose to add phone numbers manually or upload your customer base to the platform, just click on upload file.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FGYPlwJjisZIxyp5nL5WM%2Fimage.png?alt=media\&token=4c4447c5-b790-4a90-a55f-777d2cbfb098)

{% hint style="info" %}
**If you choose to upload a file, the platform provides the format in which your customer base must be.**
{% endhint %}

### **Content:**

Add the content of your message; you will have 160 characters to describe your message.

{% hint style="warning" %}
**If you use accentuations, each character that has an accent is counted as two characters, reducing the number of words you can use.**
{% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F2qRCVScTAqSeagGz6fiT%2Fimage.png?alt=media\&token=00a23ba7-3824-452d-8744-1d21e3e18467)

In order for you not to forget to remove the accentuation, the platform provides the following button:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FHjy4rCxZzBuYZqt3gMsU%2Fimage.png?alt=media\&token=be0af7b2-6021-46fa-9f8b-306264374d7b)

{% hint style="danger" %}
If you wish to send a link in your SMS, you need to submit it for review by our team. You can access our [**Service Center**](https://servicecenter.wavy.global/) for this.
{% endhint %}

## Sending a Message

You can choose to immediately send your message or program your delivery for any date

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FjEZPSWH1iRqUczyrKQ16%2Fimage.png?alt=media\&token=73511ca1-ccf2-4daf-9aba-1726e8395094)

There you go! If everything is correct, your messages will be sent successfully.


# How to Send a Message

Learn how to send SMS, WhatsApp, and WhatsApp Group messages through our platform!

## **Steps for Sending Messages**

To send a new message, you need to go through a few steps:

* [ ] Subaccount and recipients;
* [ ] Content;
* [ ] Campaign;
* [ ] Programming;
* [ ] Summary;
* [ ] Sending;

Click the **New Message** button

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FRvxDbgITxFr8f1d4OJxo%2Fimage.png?alt=media\&token=e16286a6-283d-423f-b653-c94dd3070c19)

{% hint style="info" %}
Choose the delivery **channel**

Even if you do not have all contracted features, out platform lists the other products by default.
{% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FlPKOlkG1NX5lZc019tVw%2Fimage.png?alt=media\&token=888f7a42-a3c9-4c31-983c-53f14e58d522)

## **New Message**

### **Subaccount and Recipients**

Subaccount and recipients are the first setup steps for sending your message. These settings are done for both SMS and WhatsApp message deliveries.

* [ ] Select the **subaccount** that will trigger your message;
* [ ] Choose the **recipients**: Import contacts via file, select already registered contacts, select already registered groups, or enter phone number;
* [ ] In case of "delivery by file," you need to note if you require **assistance with the country code** or not;
* [ ] **Upload your file**
* [ ] In case of "delivery by file," you can **download** our template
* [ ] **Proceed** - This option is only available after setting the recipients

Selecting the subaccount that will trigger the message, at the top of your screen you have the subaccount that is sending the message:

{% hint style="warning" %}
**To change the subaccount that will send the message, just click the down arrow.**
{% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FUzRioVljFF8Ylyrw6zYb%2Fimage.png?alt=media\&token=794e5978-dfb0-4a8f-942a-14904d6103b2)

### **Recipients**

{% hint style="warning" %}
**Recipients can be included in 4 ways**

* **Importing contacts:** Upload a file of up to 15MB with the numbers of your recipients; you can add dynamic field columns to customize the messag&#x65;**. (You can download the example template).**
* **Contacts:** Select already registered contacts.
* **Groups:** Select already registered groups.
* **Phone number:** manually enter the numbers of your recipients.

Always consider the format: country code + area code + number, e.g.:

**5511900000000**

**You can also choose to be assisted with the country code; in this case, we will add the country code to the numbers in your file.**

**You can only use one function per delivery.**
{% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FziaphwstoBVHTpfgeWOu%2Fimage.png?alt=media\&token=95036a15-22f1-403f-92b5-2a0377cad552)

### **Assistance with the Country Code**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FXAQ3VA0SsPNeqVTCN4KA%2Fimage.png?alt=media\&token=54845688-6141-45c7-bf42-5e8f6ec8f64f)

{% hint style="danger" %}
**ATTENTION**:

* If the numbers in the file already have the corresponding country code, nothing will be added.
* For now, we only add the calling code of one country at a time; if your trigger is for various countries, do triggers separately.
* The use of country codes is only available for delivery by file.
  {% endhint %}

### **SMS Content**

Set the content to be received by the recipients. For SMS, you can choose between **Text** or [**SMS**](https://docs.wavy.global/sms/template-sms%22%20/l%20%22enviar-sms-com-templates%22%20/t%20%22_blank) [**Template**](https://docs.wavy.global/sms/template-sms%22%20/l%20%22enviar-sms-com-templates%22%20/t%20%22_blank). Also learn about delivery via [**SMS Bot**](https://docs.wavy.global/sms/bot-sms).

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FgPLwHDV2cGowqc6utH2o%2Fimage.png?alt=media\&token=b475db46-3699-46cf-893f-4ff4bbb6513a)

{% hint style="warning" %}

* **Text**: enter the content you wish to send and preview how your message will look on the right side of the screen.
* You can select to send it as **FLASH SMS** - a pop-up message that shows up even if the user’s mobile phone is locked.
* **SMS Template:** select a previously created template. To learn more, refer to [**SMS Template**](https://docs.wavy.global/sms/template-sms) and learn how to create a message template.
  {% endhint %}

### **Character Number Rules**

In the case of SMS, carriers have a few rules regarding the number of characters in messages, such as the ones listed below, so **PAY ATTENTION** when planning your content in [**Messaging**](https://messaging.wavy.global/%22%20/t%20%22_blank).

### **Accents and Special Characters**

Messages containing **only** characters shown in the table below are charged for every 160 characters. If the message has **one or more** characters that are not shown in the table below, it is charged for every 70 characters, as per the carriers’ network protocol specification.

| ​     | ​  | ​ | ​ | ​ | ​ | ​ | ​  | ​  | ​ | ​ | ​  |
| ----- | -- | - | - | - | - | - | -- | -- | - | - | -- |
| Space | (  | 0 | 8 | @ | H | P | X  | \` | h | p | x  |
| !     | )  | 1 | 9 | A | I | Q | Y  | a  | i | q | y  |
| “     | \* | 2 | : | B | J | R | Z  | b  | j | r | z  |
| #     | +  | 3 | ; | C | K | S | {  | c  | k | s | \~ |
| $     | ,  | 4 | < | D | L | T | \\ | d  | l | t | ​  |
| %     | -  | 5 | = | E | M | U | }  | e  | m | u | ​  |
| &     | .  | 6 | > | F | N | V | ^  | f  | n | v | ​  |
| ‘     | /  | 7 | ? | G | O | W | \_ | g  | o | w | ​  |

### **Notes:**

• The enabling of accents and special characters must be requested from support. • If the target carrier does not accept accents and special characters (Oi and Sercomtel), our platform automatically replaces them for our customers, such as: á to a, é to e, etc.

### **Long Texts (Concatenation)**

The protocol used in the carriers’ network has the limits of 70 or 160 characters, for messages with or without **special characters**, respectively. But you can send longer messages by using concatenation, where the device regroups messages upon receiving them.

It is worth noting that, despite showing up in the device as a single long message, messages still pass through carriers’ network individually, and in this case, we still charge and are charged individually for every 63 or 160 characters (depending on the **characters** used). Reminding that, when using concatenation, part of the characters (70 or 160) are used by the header, as it is through the header that we identify that one message is linked to another.

It is also worth highlighting that, every time messages are concatenated, the carrier deduces a few characters from the second message; thus, the second message, instead of having 160 or 70 characters, has 153 or 63 characters available for use by the user while being sent.

### **Customers Who Use SMS for Marketing**

In the case of customers who use the platform for sending Marketing SMS, the number of characters is also deduced from the header and footer, as both identifications are **mandatory** for this type of content.

**Header**: In this case, the header is the 'reference' of the subaccount used in the trigger.

**Footer**: this is the opt-out message, where the recipient has the choice to opt out of receiving this type of content.

### **Campaign**

Campaigns help you to organize your messages and compare them to each other in reports.

{% hint style="warning" %}
You can set up Campaigns in 3 ways:

* No campaign
* Select an existing campaign
* Create a new campaign
  {% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FzliVDmxcERyfZpgUmUou%2Fimage.png?alt=media\&token=854a22a6-950c-4627-8338-99cf0e348427)

### **Programming**

{% hint style="info" %}
Your message can be programmed in 2 ways:

* **Immediate delivery:** Choose the date and time.
* **Delivery in parts:** Set partitions, and start and end date and time.
  {% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FbGIAiUi7MpBhjke4vofp%2Fimage.png?alt=media\&token=5e5dbe9d-8bec-4fc1-a13e-297e4e23a6be)

{% hint style="danger" %}
If you choose to **deliver in parts** set the percentage of each part with the total sum of **100%**

Delivery in parts helps to prevent overwhelming your call center if you are sending something that leads the consumer to contact your company.
{% endhint %}

### **Summary**

{% hint style="info" %}
In the summary of your message, you can see the following information:

* Type of message;
* Total messages;
* Number of recipients;
* Programming;
* Campaign (If you have selected delivery with no campaign, only "- " will be displayed);
  {% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F8FgZThtFX79MHTYDg0dy%2Fimage.png?alt=media\&token=e6fec400-f170-440b-9413-d175d9a11f49)

{% hint style="danger" %}
After clicking **send message**, a new confirmation screen is displayed, and you can choose to send it or not.
{% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FoYrUX5jxNevzVEQB5Lnn%2Fimage.png?alt=media\&token=cccd2338-93b9-44d0-b053-5b5b657be643)

### **Delivery**

After the message is sent, you will be directed to the **messages sent** screen, where you can track the message’s status.

You will have the following information in the **messages sent** scree&#x6E;**:**

* **ID:** Whenever a message is sent, the platform generates an id for its delivery;
* **Subaccount:** It points out the subaccount that has triggered the message;
* **File name:** If you used a customer base to send your message, the name of the file you uploaded to the platform shows up in this field;
* **Type:** You will see information about what type of delivery was done, in this case: SMS or WhatsApp;
* **Total:** Total recipients contained in the message;
* **Status:** You will have 3 message statuses: **-** **Green:** Message sent successfully. **- Purple:** Message in queue to be triggered. **- Red:** Message with error.
* **Created on:** Date and time the message was sent.
* **Actions:** By clicking the 3 dots, you can cancel the delivery of your message, if you have chosen to program the message for another date, and by clicking the eye you can view the message that has been sent.

{% hint style="success" %}
**​**[**Learn more about the messages sent screen, statuses, and track the delivery of your messages.**](https://docs.wavy.global/enviar-uma-mensagem/mensagens)**​**
{% endhint %}

​


# How to Set Up a File

You can upload your customer base to the platform; see how to use variables and correctly set up your files.

{% hint style="info" %}
**Requirement: Your contact file can be in XLSX, CSV, or TXT and should have a maximum of 15 MB.**
{% endhint %}

## **How to Set Up an XLSX File**

To set up the file on Excel or Google Spreadsheet, you should follow a few guidelines:

* The **first row** consists of a **header;**
* The **first column** must have the title **destination** and the **contact numbers;**
* The **remaining columns** are filled by **placeholders or variables** that can be used in the body of the message or HSM variables;
* **One of the columns** may be used as **Correlation ID** (with the title **correlationid**) for identifying customers by reports;

Example of an .xlsx file: [**XLSX File**](https://messaging2.movile.com/assets/files/valid.xlsx)**​**

Example:

| destination   | name   | info | correlationid |
| ------------- | ------ | ---- | ------------- |
| 5511987654321 | André  | Wavy | campaign\_X   |
| 5511912345678 | Mozart | Wavy | campaign\_Y   |

{% hint style="info" %}
Tip: to prevent conflicts or issues, we suggest clearing the table formatting. In order to clear it on Excel, select the entire table and click **Clear** / **Clear all formats**. Then select the first column (destination), right click and select **Format Cells**, select **Numbers** and set **0 decimal places**.
{% endhint %}

![Excel: Clear / Clear all formats](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlG_O7bibM5YjgS4hXH%2F0.gif?generation=1633456330333299\&alt=media)

![Excel: First column / Format Cells / Numbers \[decimal places = 0](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlG_O7cniJJ5FsPEAOC%2F1.gif?generation=1633456330742539\&alt=media)

![Google Spreadsheet: Format / Clear formatting](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlG_O7dlvdUMbMxA1An%2F2.gif?generation=1633456330300490\&alt=media)

## **How to Set Up a CSV File**

To set up the file on Excel or Google Spreadsheet, follow the same procedure above for the XLSX file and save in CSV.

Example of a .csv file: [**CSV File**](https://messaging2.movile.com/assets/files/valid.csv)**​**

![Excel: Save as / File Format CSV](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlG_O7e8qCOWxXmPUJ9%2F3.gif?generation=1633456329927880\&alt=media)

![Google Spreadsheet: Download as / Comma-separated values](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGXR5MHTjAi_S-wv5u%2F-MlG_O7fYZXbBOmwogGF%2F4.gif?generation=1633456330136359\&alt=media)

## **How to Set Up a TXT File**

To set up a TXT file, just fill out the first line of the file with the following information: destination: reserved for all phone numbers separated by ";" the other "columns" of the file. Example of a .txt file: [**TXT File**](https://messaging2.movile.com/assets/files/valid.txt)


# Mapped errors

Possible errors you may encounter when uploading your customer base.

### **Tips:**&#x20;

To better understand the error in a file, the Messaging platform started to indicate what is wrong and on which line of your file.

When uploading a file with some type of error, the message below will appear with a hyperlink.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FirL2CVbNIin7egb2XUGe%2Fimage.png?alt=media&#x26;token=9de4e497-e1f9-4417-9dd2-98f64ff0b0f4" alt=""><figcaption></figcaption></figure>

When you click on ![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FImwT1pyxL08ELpIKC7P1%2Fimage.png?alt=media\&token=a1f7e16e-5948-47cb-a7dc-cc5d4829b177), you will be redirected to a .txt file (depending on the browser, it will open in a separate tab) and you will see the information like this:

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FkH6X6w2zhOdxLK5zpipL%2Fimage.png?alt=media&#x26;token=d5b7c47f-40a3-4296-a423-b54104c7240a" alt=""><figcaption></figcaption></figure>

To make it easier to understand these errors, take this file into account:

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FLVxkGqNQjE99URPkMnJn%2Fimage.png?alt=media&#x26;token=c5b75ea7-7452-41f1-bf7c-56677f61a9f9" alt=""><figcaption></figcaption></figure>

This way, it becomes easier to understand where the problem is! If you have any doubts about interpreting this information, do not hesitate to call our Support Team.

However, it is important to know that we have an error that occurs before the file is uploaded, which is Encoding, which is the error below.

### Error sending the file related to formatting&#x20;

**Error message:** The file must be written with UTF-8 characters. Please check and correct the type before trying again.&#x20;

It is mandatory that the file is written with UTF-8 characters. You need to correct it before trying again.


# Campaigns

Learn how reviewing message deliveries through a campaign works.

### **Sending Messages with a Campaign**

Campaigns help you to organize your messages and compare them to each other.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FLqbLSlxgkQATyX0C9gpw%2Fimage.png?alt=media\&token=7a549fe3-0ef1-49b8-b384-665b2584e1bd)

{% hint style="info" %}
You can set up Campaigns in 3 ways:

* No campaign
* Select an existing campaign
* Create a new campaign
  {% endhint %}

{% hint style="success" %}
If you have already sent a message with a campaign, you can send new messages using an existing campaign.
{% endhint %}

### **Analyzing Campaigns**

By sending a message with a campaign, we can then filter in the reports and analyze campaign data, delivery percentage, reading percentage, and other information.


# Correlation ID

Sending the correlation id in order to better identify messages sent.

The “correlation ID” information will **not** be included in the message text, it will be hidden and used subsequently by the customer to identify the message sent.

* In order for it to work, a column must be included in the file intended for the correlation ID.

| destination    | name   | info    | ... | correlationid |
| -------------- | ------ | ------- | --- | ------------- |
| 55199999999999 | Wavy   | company | ​   | campaign\_X   |
| 55199999999999 | Movile | company | ​   | campaign\_X   |
| 55199999999999 | 1B     | company | ​   | campaign\_X   |

{% hint style="warning" %}
**Note:** All rows of the Correlation ID column must be filled.
{% endhint %}

### **Names that Will Be Interpreted as correlation ID:**

"correlationid", "correlationId", "CorrelationId", "CorrelationID", "correlationID", "Correlationid", "CORRELATIONID","correlation\_id", "correlation\_Id", "Correlation\_Id", "Correlation\_ID", "correlation\_ID", "Correlation\_id", "CORRELATION\_ID"


# Tracking Sent Messages

Learn more about the Messages sent screen, programmed messages, status, and more.

## **Messages Menu**

When you trigger a message, it enters a queue in our system to be delivered to your user. After sending a message, you are redirected to the **Messages** menu.

To find the sent messages menu, on the left side of the screen, expand the messaging menu and click on messages sent:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FGIlAb9kaB8aKBBqRtxS4%2Fimage.png?alt=media\&token=78247949-64bd-45bc-aceb-4751aac9fdb1)

After opening the messages sent screen, you can use filters to search within the platform for specific messages:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FcZRANChLmVIz8GthrrRE%2Fimage.png?alt=media\&token=d5dc0928-caea-4cd6-b293-abad1ba77875)

Filtering by **Status**, you can track only messages that have already been sent, or those that are still being processed by the platform, for instance.

Filtering by **ID**, you can search specifically for a batch of sent messages, but this requires you to know the **ID** of the messages you have triggered. Whenever a new trigger is done, the platform generates a new batch for your messages, it is the first field listed under sent messages.

Filtering by **Type**, if you have contracted SMS and WhatsApp, you can filter by one type of message or by the other.

{% hint style="info" %}
If you have done a trigger by file, you can also find the message through the **file name** column
{% endhint %}

### **Message Status**

{% hint style="info" %}

* **Programmed:** Your message has been programmed and will be processed at the set time.
* **Processing:** The message is ready to enter the delivery queue.
* **Sending:** The messages are being sent to the delivery queue.
* **Cancelled:** The delivery of the programmed message has been cancelled.
* **Error:** An error has occurred while sending the message.
* **Sent:** The message has entered the user delivery queue.
* **Blocked Time:** The message has been set to be delivered at a time that is not allowed by the subaccount
  {% endhint %}

### **Previewing a Message Sent**

You can preview a message sent under the actions menu.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FCmkuCdpGLxGfvNPsmCLq%2Fimage.png?alt=media\&token=cc58ee4a-54dc-4c85-b842-6dcb78be342e)

{% hint style="info" %}
**Previewing the message, you can see**

* **The message’s content;**
* **The delivery channel;**
* **Number of messages sent;**
* **When it was sent;**
* **Which user and subaccount has triggered the delivery;**
  {% endhint %}

## **Words Not Allowed in SMS Deliveries**

Following the guidelines of our services and in order to protect end users from inappropriate content, some words or links need to be enabled by our Support team. If your message has not been sent because it **contains a link** or **a specific term** that can sound ambiguous in certain cases, contact us by accessing [**servicecenter.wavy.global**](https://servicecenter.wavy.global/) informing the link or term to be sent, and our team will review it and clear it for your future deliveries.


# Cancelling a Message

Learn how to cancel the delivery of your message.

Currently through Messaging you can only cancel messages that have been programmed and whose status is as shown in the image below:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F1FI7qNTPEruQCJqVvj1l%2Fimage.png?alt=media\&token=745382de-26ab-4294-9fc7-04e2f84de2fd)

When the status of your message is **'Sent,'** even if the trigger is split into batches, you can only cancel it by contacting our **Customer Service** team through the link: [**Service Center**](https://servicecenter.wavy.global/).


# Character Limit Setting

You can ask the Support team to set a character limitation, where 1500 characters is the maximum a message can be. This setting is done per subaccount.

Once this configuration is done, it looks like this:

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FOzYyUSGClkconWWHFx9d%2Fimage.png?alt=media&#x26;token=406f6ea2-b8e7-4d29-9e22-60f4c3369b4b" alt=""><figcaption></figcaption></figure>

If the user hovers the mouse over the (new) configured information, the following message appears:

> Contagem de caracteres configurada pelo admin da sua conta.

For those who choose to use a template, the configuration also appears:

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FbWhaQ4tb0FiyvJemOMhj%2Fimage.png?alt=media&#x26;token=c7ca9666-6844-4ffb-aa7e-eaee49fef44f" alt=""><figcaption></figcaption></figure>

And when you go to shoot, in case your account has some character configuration limitation, this message will appear in yellow:

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FvOPh9byuUhaFZZjX0cP5%2Fimage.png?alt=media&#x26;token=a3f473e2-8ae3-4b6a-90bc-683b45a8d3fe" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
ATTENTION!!!

When using a template with a variable, this yellow box will appear informing that this account is configured. If you want to know which text limitation, just select the TEXT option to see this information.
{% endhint %}

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FOyM1HfEpMNfWqFuusfX7%2Fimage.png?alt=media&#x26;token=9d3f5c06-7d45-407b-bd21-a3e488f801ea" alt=""><figcaption></figcaption></figure>

An important factor is that even having configured the character limitation, when using a template with a variable and this variable will exceed the limitation, the message will be sent in full.&#x20;

It is understood that at the level of customer experience, it is necessary that the message be delivered in full.&#x20;

The warning in the yellow box serves precisely to warn of this behavior and to review the content or content of the file that will be used.


# MM2: New Report: Chat (MT + MO)

Report Chat (MT+MO) is the new SMS report from MM2, where we consolidate the information of MT + MO in one single place.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FohOqzOFPWUJMbETSd1Jq%2Fimage.png?alt=media&#x26;token=f53537a6-4ddd-4250-9513-48c0f3f1686a" alt=""><figcaption><p>image1</p></figcaption></figure>

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FRrUnNJorhc64WK2eB5aS%2Fimage.png?alt=media&#x26;token=e716414b-2d83-402e-8e7a-302e1995dd15" alt=""><figcaption><p>image 2</p></figcaption></figure>

Report Chat (MT+MO) is the new SMS report from MM2, where we consolidate the information of MT + MO in one single place.

## How is it works?

<mark style="color:red;">**2.1**</mark> The idea of this report is consolidate the message sent (MT) and message received (MO) information in one unique place, in an ordered way. You can use these filters + calendary (to get the period of information that you need) and then, click into APPLY

<mark style="color:red;">**2.2**</mark> Correlation ID: It is a specific field that can be added to your customer base indicating a registration number or protocol, this data does not appear in your SMS.&#x20;

<mark style="color:red;">**2.3**</mark> Type (MT/MO): if it is MT or MO message&#x20;

<mark style="color:red;">**2.4**</mark> Campaign: name of the campaign (if it exists)&#x20;

<mark style="color:red;">**2.5**</mark> Message: the content of the message&#x20;

<mark style="color:red;">**2.6**</mark> Select All: bring all the information&#x20;

<mark style="color:red;">**2.7**</mark> Phone: if you want to search some specific phone number (must fill it up with complete number)&#x20;

<mark style="color:red;">**2.8**</mark> Calendar: select the period to see your data

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FT7fD8SuL4XhmokilB8AZ%2Fimage.png?alt=media&#x26;token=5abc8501-9c02-4a9e-9644-5a73125b218a" alt=""><figcaption></figcaption></figure>

2. **Go to side Menu > Reports > SMS > Chat (MT+MO)**

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FCRjdrNhPHZ39c2TOgjCn%2Fimage.png?alt=media&#x26;token=26fea8ab-dfa1-46aa-880e-5917508fb943" alt=""><figcaption></figcaption></figure>

As you can see, you will be able to identify what is MT and what is MO, in an orderly way (starting with the oldest to the newest) Another thing our customers will be able to do is to answer a specific MO. If he choose to do this, he will redirect to Fast SMS. After sending it, he will return on Report screen (first page).

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FNRD8OxhsMMzDxKp292Iw%2Fimage.png?alt=media&#x26;token=6c8d9aa4-cc30-48c7-a998-f29982599d6a" alt=""><figcaption></figcaption></figure>

On this page, we bring the phone number (coming from the MO) that the customer decided to answer.


# SMS Report > RCS

SMS Report > RCS On the Messaging platform, it is now possible to send SMS converted into RCS.&#x20;

To gain access, talk to your **Account Executive** and ask our [**team for help**](https://docs-latam.messaging.sinch.com/support) in configuring your account!

Once you have this configuration and have taken shots, the best way to monitor the success of your campaign will be to view the report, right?&#x20;

Well, here is a brief guide to what you need to know!&#x20;

**New Columns:** find out what this report has to offer

Here we list the new columns:&#x20;

**Read:** containing only YES/NO \
**Read at:** containing date and time it was opened \
**Billing type:** indicating whether the message is Basic / Single and in cases where it only has a dash (-), it means that we are talking about an SMS message. \
**Sent as SMS (if there was a fallback to SMS):** Yes/No \
**Message parts:** number of parts that were sent&#x20;

### Understanding your MTs&#x20;

You will see your MTs that were converted as RCS only.&#x20;

### Viewing MOs&#x20;

Here you will see the MOs that interacted in the messages sent and converted to RCS only.

This is because the MOs of users who received the fallback SMS will be treated as “common MO”, without having any type of identification that indicates that the message was from the **SMS flow -> RCS.**&#x20;

To identify these MOs, it will be necessary to go to the SMS report and look at the MT that was associated with the MO, or the customer/subaccount of the MO, to find out if it is from a subaccount configured to send as SMS -> RCS.


# Viewing & Exporting Reports

### Reports

Under Reports, you can see how your triggers perform.

To access the reports tab, on your left-side menu, expand the messaging menu and then click on **Reports:**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FioN70akvrJPELMUANbZc%2Fimage.png?alt=media\&token=a05a39bb-5bf7-44c2-a80c-e5e7cbf46962)

Select the channel **(WhatsApp or SMS)** you wish to view and filter according to your needs. Even if you do not have SSM or WhatsApp contracted, just switch the tab between them:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FfNcodFsjFqbUDsRg7lMP%2Fimage.png?alt=media\&token=2ba617b4-19b7-4a96-93b4-79355d0190eb)

The first filter you need to apply for your search to be correctly extracted is the date filter. You can search up to the last 90 days of deliveries by the platform:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FsoWIa5zoeNXxkyZ33Ie4%2Fimage.png?alt=media\&token=91aa2104-d333-4b67-b58e-94e10233d2c7)

{% hint style="info" %}
By default, the platform only shows the results of the last 7 days.
{% endhint %}

You can make your search cleaner by using the other filters, namely:

* MTs (The messages you send to your customers);
* MOs (The messages your customer sends to your company);
* Subaccount that triggered the messages;
* User;
* Campaign;
* Type of content;
* Status;

### Consolidated & Detailed

{% hint style="info" %}

* **Consolidated report** is the overview; you track your results according to the date filter set on the platform, and the result is shown as a percentage.
* **Detailed report** shows the content that was sent, and you can filter by phone number; you can also track whether messages were successfully delivered or if for some reason there was an error.
  {% endhint %}

### Consolidated:

After applying the due filters, first the platform will bring you a chart view; by running your cursor over the peaks, you can see the number of messages that were delivered on that day and the number of messages that had errors:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F2SobrjIF2s8rP4ravTPv%2Fimage.png?alt=media\&token=d25c2bca-bcf3-41c5-bdae-a9f10722c79d)

### Consolidated report

Underneath you can view some more information:

* **Total messages:** Number of messages that have been triggered on this platform.
* **Sent:** Number of messages that have been sent by the platform; in this status, it is important to note that when a message is sent, it doesn’t mean that it has been delivered.
* **Delivered:** Number of messages that have been delivered by the platform during the period set on the date filter.
* **Read:** Number of messages that have been read by devices; this field depends on the end user having their read receipt enabled.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FcNF4S4XSzWCAQW2ZXSXJ%2Fimage.png?alt=media\&token=fa26a9a3-ecf8-406f-b109-e845b5c3d3ee)

Scrolling down to the bottom of the page, you can track the delivery percentage per days:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FNh2j5YObM00ZMzMvkF1s%2Fimage.png?alt=media\&token=c53be9cf-e7c9-4859-a0a8-c59ff15f258d)

### Detailed Report

The detailed report has the same fields as the consolidated report; however, it has one extra field and also one other type of data view.

To access your detailed report, just switch the platform’s tab:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FPSi1wSTN5ndcPRceqY0i%2Fimage.png?alt=media\&token=5c153abb-d7e4-4ecd-ab8b-0f1005127200)

The first filter to be set is the date filter on the top of the screen:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fubqdo9jHk9MEqjAABesY%2Fimage.png?alt=media\&token=fbeb7842-bde7-4da2-b984-2c12aef7b887)

You can search messages up to the last 90 days (this is a platform default).

You can make your search cleaner by using the other filters, namely:

* MTs (The messages you send to your customers);
* MOs (The messages your customer sends to your company);
* Subaccount that triggered the messages;
* User;
* Campaign;
* Type of content;
* Status;
* Contact or phone number: Imagine a user reporting that they have not received your communication? You can add the customer’s phone number in this field and understand what happened to the message’s delivery.

## Exporting Your Report

After selecting the channel and filters, click **apply** and you will have access to the information on your screen. To export, click the desired format and **export**

{% hint style="warning" %}
By clicking export, the file will be processed and you will be able to access it clicking on:

**See exported reports**
{% endhint %}

**To export a report, just click on the button:**

Export in: CSV or XLSX.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FKDbcXAvMVfqwNg1uvXdr%2Fimage.png?alt=media\&token=fd77c2b2-93c1-401d-bb24-960a0d1ac451)

Or you can also use the button: Export to PDF,

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F9Fuc8fsHqLFRQ8AEUaqn%2Fimage.png?alt=media\&token=8dd8491e-772e-4b43-a623-9285790b84f4)

{% hint style="info" %}
Under exported reports, you have the history of all reports requested and you can see the user and subaccount that made the request. You can download or see reports that are still being processed or cases of export errors.
{% endhint %}

​


# New WhatsApp Conversation report

### What are the new concepts&#x20;

In view of Whatsapp's new business model, based on conversations and no longer on the number of templates sent (in effect since February/2022), our report has been updated to reflect these changes.&#x20;

Now there is the concept of conversation, which is a fixed 24-hour session always initiated with the proactive sending of the first message by the company or when the company responds to the contact initiated by the user.&#x20;

There are two types of conversations: those that are initiated by the user (your customers), called "user initiated conversations", and those that are initiated by the company (you), called "business initiated conversations".&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FJ9zIEWjplQlhh6Uu8lg9%2Fimage.png?alt=media\&token=d21e1c2a-83ef-4142-aabb-387ee1c7d95e)

In the "Detailed Messages (MT)" report screen we have added 2 new filters: the Conversation ID and the Conversation Type (to see who started the conversation: business / user / free entry point).

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FDi3Av0wVkF2L6IV0sHHg%2Fimage.png?alt=media\&token=79dfc491-6872-419c-b15f-18f941ec5957)

By applying the on-screen filters and extracting your detailed message (MT) report, you will see 3 new columns: Conversation ID **(1)**, Conversation Type **(2)** and Conversation Expiration Date. \
&#x20;

**(1)** Filtering by conversation ID, you can see how many messages belong to the same conversation, i.e. the same ID. Remembering that the session is now fixed (24h), that is, for each completed session I will have a conversation ID. \
&#x20;\
\&#xNAN;**(2)** Conversation Type: can be Business Initiated, User Initiated and Free Entry Point. \
&#x20;\
\- **Business Initiated:** the company initiates a conversation by sending a message to the user/customer \
&#x20;\
\- **User Initiated:** the user initiates a conversation by sending a message to the business/company and the company responds \
&#x20;\
\- **Free Entry Point:** conversations from Click to Whatsapp Ads and Facebook CTA are not charged. \
&#x20;\
In addition to adding new filters and information to the "Detailed Messages (MT)" report, we also created two new reports: Consolidated and Detailed Conversations. \
&#x20;\
1\. **View All conversations:** number of conversations that were Business Initiated and User Initiated \
2\. **View Free Conversations:** number of conversations that refer to Free Entry Point and Free Tier \
3\. **View Paid Conversations:** number of conversations that were Business Initiated and User Initiated&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FfdAt2Kw4wpKXhbS2NtGC%2Fimage.png?alt=media\&token=cd429e2b-1010-4d64-9f89-6c6a2268fbbb)

Another new concept is the Free Tier, where every month, the first thousand conversations will be free (for each WABA ID – WhatsApp Business Account), and can be initiated by both the company and the user. It is important to emphasize that even if the conpany has several WhatsApp numbers created in the same WABA, the limit of free conversations will still be 1.000 (and not 1.000 per number). &#x20;


# Getting to know the new reports

### Detailed Message Reporting (MT): What's Changed?&#x20;

In addition to the filters you already know, we added 2 new filters (Conversation ID and Conversation Type):

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F1Ntyo0Ya3BZRYXpKRaA1%2Fimage.png?alt=media\&token=16e81cf5-8010-43e9-962d-dd036f043499)

When doing your report extraction according to the filters you want, you will come across 3 new columns (Conversation ID, Conversation Type and Conversation Expiration Date).

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FDAX5GAcSU1vWBoISwZif%2Fimage.png?alt=media\&token=b1457c03-50af-448f-a4bc-f049296250b9)

In other words, you will be able to identify:

* all messages referring to a given conversation ID;
* will know if that message is part of a conversation that was initiated by your customer or by you (company)
* you will know if that conversation has already expired or if it is still open, viewing the expiration date and time (remembering that the fixed session time is 24h)

### Conversations Report (New!)

With the new Whatsapp conversation model, you will be able to extract consolidated and detailed reports from your campaigns.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fw9oO317ymN0hCbXHtl6h%2Fimage.png?alt=media\&token=51895487-326f-440b-b65a-1194e9bf1176)

### Report - Consolidated Conversations&#x20;

By filling in the date (period), sub-account or campaign name filters, you will see these 3 graphs: All conversations, Free conversations and Paid conversations. At the end, a consolidated of these data. \
**Important to know** that the data is updated hourly. If you don't find the data you are looking for, you should try to generate the report again within 1h. \
&#x20;\
Chart of All Conversations: according to your filter, you will see the consolidated of all conversations initiated by the company (Business Initiated) and how many were initiated by the customer (User Initiated). What makes this visualization different from the Paid Conversations graph is that it is taken into account here: \
&#x20;\
&#x20;\
**Business Initiated =** Business Initiated paid + Business Initiated free tier  \
**User Initiated =** User Initiated paid + User Initiated free tier + Free entry point&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FgZcHEAXZrVuuYFKcqhWq%2Fimage.png?alt=media\&token=9c0a1229-1e67-40e8-90c3-55e5bb9b36f9)

**Free Conversations Graph:** according to your filter, you will see how many are related to the Free Tier (benefit provided for each WABA) and how many are related to the Free entry point.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F9U5lpfGSmk4KTrvXy8bD%2Fimage.png?alt=media\&token=81f44636-5a79-4133-8aa3-f7499ddb219c)

**Paid Conversations Graph:** according to your filter, you will see the total number of conversations and know how many of them were initiated by the company (Business Initiated) and how many were initiated by the customer (User Initiated).

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FgMXozEYvybDcfSFoWGVa%2Fimage.png?alt=media\&token=aeaa022a-f264-4fd3-bc1d-d9c6b3641e41)

Report - Detailed Conversations&#x20;

Here you can filter, in addition to the campaign period, also by sub-account, campaign name, conversation ID, conversation type (if it was Business Initiated, User Initiated or Free entry point) or by destination (phone number with area code).&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FnyAqEGNndmXK53FKzO5k%2Fimage.png?alt=media\&token=ef9d9cf5-63fe-4966-8136-e5a14cb8a9c5)

After performing the search, you will find a report with all this information filled in, in addition to the date/time of the expiry of the conversation. You will be able to export your report in PDF, CSV or XLSX format.


# Saved Reports

To make the extraction and analyses done from report data, you can now save report templates in order to accelerate your work routine.

After selecting the desired filters, click on "Save template,"

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FLs4k2fCLVJRxPMWiTnTn%2Fimage.png?alt=media\&token=488a77c6-01cc-4cac-9b4d-c4d3c98f3401)

enter a name for this report template (e.g.: monthly report of deliveries by subaccount).

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FHdtuSE0HmXXlgouRv3w7%2Fimage.png?alt=media\&token=7f683f20-2555-40d4-83de-0f31d2f42895)

To access saved reports, click on "Saved report templates" and search for the template name and enter the date from which you wish to view data.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FUBt8saK6DtrwJHq9nmOM%2Fimage.png?alt=media\&token=f86dd491-82ad-4b0c-ac16-d04225598520)

**Reminder that you are saving report filters; dates may be different at each new export.**


# WhatsApp Lists

### Opt-out&#x20;

With the Opt-out list, you can extract information of all users who have opted out of receiving messages through the channel. When a user opts out of a contact list, our system blocks any attempts that may occur to send a message to this user.&#x20;

&#x20;

### How Do I Extract a List?&#x20;

To extract a list, sign in to Messaging with your login and password and follow the steps below:&#x20;

1 - Click “Reports” in the menu on the left of your screen; &#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Faxo8tiKsNSQhsK3a2c1n%2Fimage.png?alt=media\&token=c22040ea-0dc7-412a-862d-7ae21eda5003)

### &#x20;Reports&#x20;

2 - Click “Lists” under the reports tab, choose which list you want and click export. At the bottom of the page, you will have a message; just click view:&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fdcmrz4swOkJFov2OfEur%2Fimage.png?alt=media\&token=7989651e-c08d-43be-88df-d21e81ce8b3e)

&#x20;

### Lists&#x20;

3 - You will be redirected to a page will all reports requested by your user and a new report will be on this list; choose which of them you wish to extract and click “Download”.&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FlpQc9liRn5TXf7q1siIM%2Fimage.png?alt=media\&token=34419e0b-4435-4e37-ac45-4b725c712359)

&#x20;


# Billing Report


# System User Role

## What is this new feature?

Before we explain about the feature, we need to **understand the problem that we are solving**. When you have to create a chatbot integrated to MM2, you must create an account on MM2 to link this to a chatbot, on Chatlayer. If this person who has created this bot **leaves the company**, this chatbot usually is <mark style="color:red;">**desactivate**</mark> due to this event.

So, thinking in **avoid this bad experience** happen always that someone leaves the company (and to guarantee more security in our process), we have decided to **create the** <mark style="color:red;">**System User Role**</mark>. This new feature intend to prevent this issue from happening, become able to <mark style="color:red;">**create safe users to use on your chatbots.**</mark>

## Activating the System User Role

Go to Settings > My Account > Account Settings

<mark style="color:red;">**2.1**</mark> - You can see the new tab called System User.&#x20;

{% hint style="danger" %}
Only the customer **Admin** and the **Developer role** can be able to set up this new configuration.
{% endhint %}

<mark style="color:red;">**2.2**</mark> - Button to "**Create System User**".

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FcohEwmlI9r0mqrFcqeUm%2Fimage.png?alt=media&#x26;token=87e565e2-44ef-425e-b962-d00cbc0f3d5b" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**2.3**</mark> - Once you click on the button to create a new system user, it will open a pop up where you can select the subaccount + username.

<mark style="color:red;">**2.4**</mark> - It is important to know that you can only create a system user for each subaccount.

{% hint style="info" %}
The **Username** can be whatever you want.
{% endhint %}

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FTVuZEz6rrWTTzZTk0hbo%2Fimage.png?alt=media&#x26;token=3c23813e-f82f-4ee4-961d-5c09e4118600" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**2.5 -**</mark> After you define the subaccount and the username, you will click on <mark style="color:red;">**Generate Token**</mark>.&#x20;

It will appear this pop up, so pay attention to take note of this token because it will not be displayed again. In case you forget to take a note, you will have to generate a new token.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FxCogAnABtlH3H0XHtRWm%2Fimage.png?alt=media&#x26;token=d35f5df7-d0fa-4871-9842-bae499896260" alt=""><figcaption></figcaption></figure>

In this screen, you can see all the system users you have created.

<mark style="color:red;">**2.6 -**</mark> You can see who user has created.

<mark style="color:red;">**2.7 -**</mark> All the informations that belongs to the system user.

<mark style="color:red;">**2.8 -**</mark> You will be able to see just the end of the token.

<mark style="color:red;">**2.9 -**</mark> The date and the time of this creation.

<mark style="color:red;">**2.9.1 -**</mark> If it is active or inactive.

<mark style="color:red;">**2.9.2 -**</mark> More Actions (Deactive or Generate a new Token)

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FQC8wc9JrnAL034oS2zIO%2Fimage.png?alt=media&#x26;token=2df34f0e-38c0-4744-a008-b2477720642a" alt=""><figcaption></figcaption></figure>

## Deactivating the System User Role

Go to Actions > Click on … > Deactivate.

<mark style="color:red;">**3.1**</mark> Once you click on Actions and choose to deactivate the System User, it will open a pop up to confirm your choice.&#x20;

<mark style="color:red;">**3.2**</mark> After doing this, you will see the Status column updated. In case you want to activate it again, just go to Actions.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F55rhC0MVRPr5sbaXaUMU%2Fimage.png?alt=media&#x26;token=7f798f7a-0d49-4f90-a77f-cb42143bd6bc" alt=""><figcaption></figcaption></figure>

## Generate a new token

Go to Actions > Click on … > Generate a new token.

<mark style="color:red;">**4.1 -**</mark> Once you click on Actions and choose to Generate a new token, it will open a pop up to ensure your understanding about the risk of doing this (just in case you have configured in an API).

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FoUG56raTaSVKZhWdi59y%2Fimage.png?alt=media&#x26;token=dae3e3c8-7934-4872-ab88-b274d58657c0" alt=""><figcaption></figcaption></figure>

## Webhook Configuration: prepare to Chatlayer integration

Go to Settings > Webhook.

5.1 This configuration is the same of usual.

The only exception is that if your chatbot is not so active into sending messages and not expecting to receive organic MO (mainly after so much time without any interaction), you will have to configure another Answer (MO) to accept **Subaccount Null**.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FCAL7C454ai4orMqo6WmT%2Fimage.png?alt=media&#x26;token=760ae06d-90a4-4325-9d7b-ed9934a15860" alt=""><figcaption></figcaption></figure>

## Update Chatlayer with System User

Go to Chatlayer > Configure Wavy WhatsApp Channel

<mark style="color:red;">**6.1**</mark> This configuration is the same of usual.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FXfU0W5LjksBHr6vUwti3%2Fimage.png?alt=media&#x26;token=320565f8-e443-4e88-9ee8-549fa917ea15" alt=""><figcaption></figcaption></figure>


# Managing Customers | Subaccounts

{% hint style="danger" %}
**Prerequisites:**&#x20;

* **In order for you to use this feature, our support team must have previously linked your accounts.**&#x20;
* **Administrator permission.**&#x20;
* **As an administrator, you will already have all the accounts | subaccounts linked to your user. A**
* **fter the configuration is applied to your users, they will be able to freely browse the configured accounts.**&#x20;
* **It is important to pay attention when taking a shot, making sure you are using the correct environment.**
  {% endhint %}

To carry out the configuration, you must access the following in the left side menu:&#x20;

**Settings > Subaccounts and Users > Switch tab to Users**


# Permission Levels

Today the platform has different levels for viewing features that are tied to user permission. See below which levels are those:

### **User**

Can send messages and access the report of messages it has sent. Can view some other information that is shared within the subaccount to which it belongs, such as templates, groups, and contacts.

### **Analyst**

Has access to everything that has been triggered from its subaccount, such as messages, reports, templates, and contacts.

### ​**Manager**

This profile has access to all data that is in the subaccounts of its account, i.e., it is a more macro profile that has information on everything, but does not yet have permission to edit and create new subaccounts and users.

### ​**Customer Administrator**

The customer administrator profile, in addition to having all data available on everything within its account, such as reports, templates, groups, and contacts, among others, it can also create and edit new subaccounts and users, as per [this](https://docs.wavy.global/permissoes/subcontas-e-usuarios) guide.

### ​**Data Analyst**

Can extract reports from the entire account, but cannot have access to any other features or trigger any messages.

### ​Resale Administrator

Has access to all resale customer features (reports, deliveries, and visibility of subaccount and user settings).


# Subaccounts & Users

Learn how to manage subaccounts and users within the platform.

## What is a Subaccount?

Within Wavy, we have an architecture where our customer can use the same number to serve multiple purposes.

Within an Account, you can have multiple Subaccounts with customized “departments” and settings, where you can trigger multiple different things, such as service, CRM, Request status, among others

![Sinch Structure: Account and Subaccount](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGb9wIBDCgL4DPdczn%2F0.png?generation=1633456795944564\&alt=media)

Each subaccount can have its own users and webhook; this enables the optimization of a customer number.

{% hint style="warning" %}
**Only users with an Administrator profile can create subaccounts**
{% endhint %}

## Subaccounts Menu

{% hint style="info" %}
**Subaccounts Menu**

Within our platform, access the “Subaccounts & Users” menu. In this session you can:

* See all existing subaccounts in your main account
* See users belonging to subaccounts
* Create a new subaccount or user: Creating Subaccounts and Users depends on your user profile. Only the **Administrator** profile can create and manage subaccounts and users

**See** [**user profiles**](https://docs.wavy.global/permissoes/subcontas-e-usuarios#perfis-de-usuario) **to understand the permissions of this and other sessions**
{% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Ftm5exBo3GvkUUmylzCtR%2Fimage.png?alt=media\&token=a0ed7465-da85-48a1-9173-81933bf406c5)

### Subaccount Settings

{% hint style="info" %}
**Within a Subaccount**

When you select a subaccount, having an Administrator profile, you can:

* Edit the Subaccount’s name and reference;
* See the list of users linked to this subaccount;
* Edit users of the subaccount;
* Set LAs;
  {% endhint %}

### ​Creating a Subaccount

Creating a new subaccount for your users is simple: after accessing the settings menu > Subaccounts & users, just click on **Create Subaccount:**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FBoXtMrch6v0n8NYO1OCv%2Fimage.png?alt=media\&token=b0b256e6-1520-4630-b6e3-a383f98063d9)

The platform requests that you add some information:

* Name;
* Reference name (It is the name used in our databank)

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FPE5iNRQJtMjYDxeanL3F%2Fimage.png?alt=media\&token=8e9c0469-c370-414e-9d61-2936f84d3533)

### Adding Users

{% hint style="warning" %}
**Only users with an Administrator profile can create new users**
{% endhint %}

Access the settings menu > Subaccounts & users:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FZYjhTGPOZr6xdz6qZCMm%2Fimage.png?alt=media\&token=189feed3-a394-4657-8901-fb1b6f9aeba5)

Switch the subaccounts menu to **Users:**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FaVjqprX2F5iyaHiVoBdM%2Fimage.png?alt=media\&token=e9bfdde7-051c-4844-aa68-e81a1828fb82)

On this screen, you can see all users already registered on the platform. If you need to make any changes, such as email address, subaccount to which a user reports, name, or surname, just click the pencil that is under the actions tab:

![pencil](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FgZ56Z30xZB7p4B1cHfqo%2Fimage.png?alt=media\&token=b3e75884-daef-4543-95b7-cdb0d1bb221d)

To create new users on the platform, use the button: **Create user.**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FQxeZOLWGZwNsxolSnwJT%2Fimage.png?alt=media\&token=f7119eb0-f16b-4764-89df-482525d17e0a)

{% hint style="info" %}
**Adding a User**

By clicking on **add user,** you will enter the registration screen for your new user; fill it out with:

* Name (required);
* Surname (required);
* Username
* Email (Must be a valid email, and you can only use corporate email addresses, you cannot use @gmail.com, for instance);
* Country code;
* Phone number;
* Set the subaccount to which it belongs (required);
* ​[User profile](https://docs.wavy.global/permissoes/subcontas-e-usuarios#perfis-de-usuario): IMPORTANT – each profile grants different permissions
  {% endhint %}

### User Profiles

{% hint style="info" %}

### **Resale Administrator**

#### **Resale administrator:** Has access to all resale customer features (reports, deliveries, and visibility of subaccount and user settings)

{% endhint %}

{% hint style="info" %}

### **Data Analyst**

**Data analyst:** Can extract reports from the entire account, but cannot have access to any other features or trigger any messages.
{% endhint %}

{% hint style="info" %}

### **Manager**

**Manager:** This profile has access to all data that is in the subaccounts of its account, i.e., it is a more macro profile that has information on everything, but does not yet have permission to edit and create new subaccounts and users.
{% endhint %}

{% hint style="info" %}

### **Administrator**

**Administrator**: The administrator profile, in addition to having all data available on everything within its account, such as reports, templates, groups, and contacts, among others, it can also create and edit new subaccounts and users.
{% endhint %}

{% hint style="info" %}

### **User**

**User:** Can send messages and access the report of messages it has sent. Can view some other information that is shared within the subaccount to which it belongs, such as templates, groups, and contacts.
{% endhint %}

{% hint style="info" %}

### **Analyst**

**Analyst**: Has access to everything that has been triggered from its subaccount, such as messages, reports, templates, groups, and contacts.
{% endhint %}


# IP Restriction

Insert IPs that your users can use to access the messaging platform.

## What is this new feature?

IP Restriction is a new feature flag from MM2, that allows you to define which IP can access your messaging platform. Once you activated, all IP is blocked until you define which IP is allowed.

## Activating this feature flag

Go to Settings > My Account > IP Restriction

In this area, you can activate the IP Restriction feature. It is important to know that once activated, you will block all the users instantly. You will be blocked the next time you try to login (so the Admin can also include herself/himself on the list). We recommend that you first add the allowed IPs so then activate the feature.

{% hint style="danger" %}
Only the customer Admin can set up this configuration for him/her and for all users under this customer.
{% endhint %}

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F1jLNMfDJy6zWR9UPlurD%2Fimage.png?alt=media&#x26;token=caae5117-b6c1-4adb-b78e-e33e3aec8fdf" alt=""><figcaption></figcaption></figure>

Click on the **+Add button** to insert all IPs will be allowed to access messaging platform. Here you going to insert the email under the customer that has an account on **messaging + IP allowed.**

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FSBFP2tRMX2JH1D0iEELJ%2Fimage.png?alt=media&#x26;token=fdbe4e93-9ab8-4fb8-a706-2b908c02f404" alt=""><figcaption></figcaption></figure>

You can add as many IPs as you like, and you can edit them too.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FpEAbf8bmWrSegBLWA9Ef%2Fimage.png?alt=media&#x26;token=3534a7aa-f3c7-418a-ba4b-69691d745895" alt=""><figcaption></figcaption></figure>

## Message Error if you are not in the allowed list

If you are not in the allowed list, you will find this message the next time you try to login into the platform. To solve this problem, you can ask to your Admin to include your IP on the list or open a ticket for support to add manuall&#x79;**.**

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FxVfp2ibCNuUkgrrUpc58%2Fimage.png?alt=media&#x26;token=ce695a2d-d682-4754-afa6-969b51395896" alt=""><figcaption></figcaption></figure>


# Two-step Verification

An extra layer of security for your environment.

A autenticação de dois fatores, ou 2FA, é uma camada extra de proteção usada para garantir a segurança das contas online além de apenas um nome de usuário e senha.

{% hint style="danger" %}
By enabling this function, all users will be required to perform two-step authentication to login to the tool.
{% endhint %}

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F9ZxupaatBLK3wOHoDZ0k%2Fimage.png?alt=media&#x26;token=c0ad2114-5689-44ef-b088-35ea0085bafa" alt=""><figcaption></figcaption></figure>

## How to enable 2-Step Verification for your account?

Two-Step Verification (2FA) is a feature that only the customer admin can view and enable for all users.&#x20;

To enable the feature, follow these steps:&#x20;

1. Access your messaging account, make sure you are using an administrator account.&#x20;
2. In your left side menu search for settings > My account.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FtXNzqMPajG8nS3p3I1RW%2Fimage.png?alt=media&#x26;token=4f636032-9438-49ea-b1f6-e31e4a542968" alt=""><figcaption></figcaption></figure>

3. When accessing the above configuration, you will have access to the new configuration: Account Settings.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FdKU69lIXLmvwg180VC8H%2Fimage.png?alt=media&#x26;token=c9131c7d-6c70-4553-b02a-99effe9d6c51" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The "i" next to two factor authentication shows information about what two-step configuration is.
{% endhint %}

4. By enabling the function, all users will have two-factor authentication.

## First Setup

After accessing the Messaging tool, fill in your login credentials and password, when clicking login, a pop-up will open on the screen asking you to configure the verification. The message brings the user some more information on how two-step verification works on the account.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FDeH0m2Bbf8HE8l3yPSMk%2Fimage.png?alt=media&#x26;token=15f4b1f2-c574-4321-a0ff-9bca5cfbe25f" alt=""><figcaption></figcaption></figure>

After clicking on the next button in the previous message, it will be mandatory that you configure the phone that will be used as a security key and click on the recaptcha button (you are not a robot).

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fv31kiNpBK0MaSrzQXZga%2Fimage.png?alt=media&#x26;token=ee350953-aab1-4a7b-8eea-32aa9a9ab46a" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
**Informações importantes:**

1. **Ao inserir seu telefone na etapa acima, lembre-se de colocar o seu código do país + DDD + Número de telefone + Marcar eu não sou um robô.**
2. **Após a primeira configuração, você poderá escolher entre duas chaves de segurança: número de telefone ou email cadastrado.**
3. **Todos os usuários obrigatoriamente farão essa configuração uma vez.**&#x20;
   {% endhint %}

After adding your phone number as in the previous image, we will send you a token via SMS to your number. You have 180 seconds to receive this information and enter it in the "TOKEN" field. After adding the code, the tool clicks on validate token.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FAw0TnvgdpohPdzMvF6Nf%2Fimage.png?alt=media&#x26;token=e8638582-6a41-4afa-a80e-e1c1386b28eb" alt=""><figcaption></figcaption></figure>

Ready! You will now have access to Messaging.

## What to do after the first setup?

Now that you have configured your access in two steps, every time you log in to the platform, you will see a pop-up on the screen where you: First you need to mark the field that you are not a robot to release the buttons. With the buttons released you need to choose between receiving your token by email or by sms.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FlaECOxrT2dOHJCUn1lQI%2Fimage.png?alt=media&#x26;token=b6d147de-9193-460c-85c9-a6de2c00e865" alt=""><figcaption></figcaption></figure>

## I need to change my registered phone number

{% hint style="info" %}
This setting is only visible to users with two-step verification enabled.
{% endhint %}

You will need to access your account and search for the field my profile, this field is in the upper right corner of your screen:

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FKCicYNF4QH3yq7JnZca3%2Fimage.png?alt=media&#x26;token=8b64d0e8-78f1-4d3c-bce6-9a3fb8071b9f" alt=""><figcaption></figcaption></figure>

In this field, you can see a new configuration called phone.&#x20;

1. To change your phone, you must choose the country code + ddd + phone number, with the information filled in, click on save.&#x20;
2. When performing the previous step, a pop-up will open on your screen and you will be able to perform the configuration.&#x20;
3. In the telephone area you also see the number registered today.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FJ2K9VzH6UvZj4qfqGYIW%2Fimage.png?alt=media&#x26;token=49196476-d301-4675-aebd-660ddb830ac5" alt=""><figcaption></figcaption></figure>


# SMS Template

Learn how to create an SMS message template.

### Templates for SMS Messages&#x20;

Under Messaging, you can create and save SMS message templates for future deliveries! Add dynamic fields and customize your message. &#x20;

### How to Create SMS Templates&#x20;

{% hint style="warning" %}
IMPORTANT&#x20;

Attention when creating new SMS templates: You cannot edit or delete created templates.&#x20;
{% endhint %}

In your left-side menu, expand the Messaging tab:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FWH63lroz88WdKGYX9Lqk%2Fimage.png?alt=media\&token=825b6159-65b2-46be-945a-7bd8c01d077e)

You will be redirected to a screen where you can view all templates that have been created in the platform. If this is your first template, click at the top of the screen on: Create template.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fwwse4kvwpopAz4KBUcyr%2Fimage.png?alt=media\&token=d07f1979-c7a0-4783-880c-286832781439)

First, you need to add a name to your template:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FoaVKty8waTukrBEfyWUw%2Fimage.png?alt=media\&token=327987a7-f25d-487e-a895-03f38d2b5d2a)

Then, you can start typing the text of your message; you can use emojis (not accepted in all devices) and also variables:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FpFWYDhbOMHm9fbVDJqBv%2Fimage.png?alt=media\&token=8b6250e9-f962-4c7d-b382-850b2059e4e8)

When we use variables in our message, they show up between curly brackets {{1}}; you can change this field for the name of your customers if you upload to our platform, or for any default word. Variables (dynamic fields) are only filled at the time of sending your message.

1. Remember that, fi you use accentuations in your message, the number of characters used doubles.&#x20;
2. You can use the button: Remove accents from words, to avoid forgetting any.&#x20;
3. As with SMS, you will have 160 characters to type your message.&#x20;

You will always be able to preview your message on the right side of your screen:&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FtXLV295eZcOfxj38EmYP%2Fimage.png?alt=media\&token=315c7bc6-2f71-4792-952b-05f7e70dae71)

On the bottom of the screen, click Create message, and your template will be ready for use.

### Sending SMS with Templates&#x20;

In the content of the SMS, you can type free text or select one among created templates. &#x20;

First, click on new message:&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FmgMns007T3IUNgptBGSh%2Fimage.png?alt=media\&token=97a883ed-5aed-4b7f-ad6e-023e9fb3d707)

Then select the SMS option:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Ff7k7mhhHm8QatacAw4Jz%2Fimage.png?alt=media\&token=4bb97a33-8b1c-44f8-86a4-137fe2c43d1b)

Upload your customer base to the platform or choose how to trigger your message.&#x20;

If you use the upload a file option, the platform will read the header of your file as a variable (dynamic fields), and you can change any field between curly brackets {{}} for those words.&#x20;

#### Delivery By File:&#x20;

Variables are the last words that show up on this screen:&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FnsATw2N1unzh43H6z1iL%2Fimage.png?alt=media\&token=f72bad1a-a261-4571-b187-0fad7181f92f)

After clicking Advance, you can choose the Template option:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FpAp2StKfXXsFfFxoyC4i%2Fimage.png?alt=media\&token=8b321a3f-8c50-41c9-b81b-314864acdf5f)

The platform will request the name of your template under: Choose a template, just enter the name of the template you have created:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FPkgGe6dLn2F2UFIiTl2G%2Fimage.png?alt=media\&token=444a8866-9fbe-47a2-bb17-e04fce92f8ab)

Then, you will view the text of your message:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fo8Py3hsfDVHmERMsp2Sg%2Fimage.png?alt=media\&token=f4fb0697-75af-4e20-b0c6-c55bc58e7907)

You can choose to send the message as a flash-sms, but not all carriers accept this type of delivery. The message appears as a pop-up on the screen of your end user’s phone.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FsXZ7dyDlvIN3iH4kVQkF%2Fimage.png?alt=media\&token=ba199ffb-b5bb-47d3-afca-f9b0dfd85588)

And lastly, you add variables (dynamic fields) to your message. You can choose to fill out the field with a column of your customer base (referring to customers by name, for instance), or add a default message:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FGGaYCiq97h4xVWsSF0Qi%2Fimage.png?alt=media\&token=dd797efc-835e-4282-a89d-c693cefcdc4a)

If you opt for the file column feature, you can choose among all columns that are in your file:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FoIh5qW08BdM65VJ7Qd7C%2Fimage.png?alt=media\&token=fb4f730e-b5ac-446d-a437-1d4d433680cd)

You will have an entry field for each of the variables your message has; you will only be directed to the next screen after filling out all of them:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FBf74E4HsrrQBau6nKUNt%2Fimage.png?alt=media\&token=ef25b6c0-d651-4052-8e37-2232fb1ed9a5)

Your message will be shown on the right side of your screen, so that you can follow the progress.&#x20;

Then, just click advance and send your message as usual, choosing the campaign, time of delivery, and summary.&#x20;


# SMS BOT

Learn more about SMS message bots

### **What is a BOT?**

BOTS are robots structured through an intelligence to automate and standardize human care in a pre-determined task or exercise.

### **Example of a BOT?**

On the platform itself, you can view and use a few BOT templates to collect users’ Opt-in via SMS or perform NPS searches, but BOTS can be used for many other purposes according to your business.

### **How Does an SMS BOT Work?**

The SMS BOT works actively, i.e., you need to send a message with the desired BOT to start it all.

After sending the message, the BOT records and acts in the messages replied to by the recipients for up to 7 days; after that, you need to send a new message from the same BOT or a different BOT so that recipients that have not interacted can reply.

(If a user is in the middle of the flow and you send them a new BOT, the previous flow will be interrupted and the user will go to the flow of the new BOT).

Below we have a few terms that are used when we talk about building an SMS BOT:

* Steps are the different messages that make up the BOT’S flow and can be sent or not to recipients according to the replies received by the BOT.
* Message Text is the text that the person will actually receive in the message, in that step.
* Replies are Keywords that the BOT recognizes in the replies it received from users and through which it triggers new messages or performs actions in the flow.
* Mnemonics or Synonyms are different spellings for a same reply that a step accepts. For example, if a step accepts the reply YES, you can set up the BOT to recognize different ways of spelling YES, such as Y, Sin, Yeah, Si, Yup, Yea, etc.
* "Name on Report" is the way in which different mnemonics are grouped to be recorded in reports. You can determine the name you wish for a group of Mnemonics accepted in one of the replies of a step of the BOT’S flow to be recorded in the reports.

### **How to Build an SMS BOT?**

To create an SMS BOT, just access **messaging** with your login and password and follow the step by step below:

1. Expand the **Flow Builder** option under the menu on the left of the screen and click on “SMS BOT”:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F6mVBXGDP5CQkRftAPBKf%2Fimage.png?alt=media\&token=4d3de940-70b6-4522-bb8b-bc1168b7e5d6)

2\. To create a new BOT, click the “+New SMS BOT” button, which is in the upper right corner of the screen

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FPYWyqNTaU3ksjFhPAOOt%2Fimage.png?alt=media\&token=ed182ed6-22c2-48f5-8c87-d5423424e581)

3\. Then you will see a screen such as the one shown in the image below, where you can use templates for NPS Searches, Opt-in, and create a new BOT with the flow you want:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fh4uD6xffiNy2f4yK6GZl%2Fimage.png?alt=media\&token=696e9219-7f33-4e71-a31e-fc5c1e1cbecb)

4\. By clicking to create a blank flow, you can make a few settings such as: **adding a step and the replies expected from users.**

* **You will have 70 characters to set up your messages.**
* **Remember not to use accentuations.**

***To the side, you can view a drawing of how the decision tree is looking for the bot you are creating.***

6\. Create a new step and give it a name. Then include the question that will be sent via SMS in the field “Message text”.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FOCH4OJkWywpVTooHwKxF%2Fimage.png?alt=media\&token=e11ce31d-c07d-4dd0-8a64-661b4eaa7b09)

In the “replies” field, you must include potential user replies.

In the “Terms for reports” field, you must include an intuitive name that will show up in the report on that reply.

In the “Actions” field, you must include which action the bot should take if the user’s reply is the one included above.

**7.** After these steps, you can include as many steps as you deem necessary for your BOT to fulfill its purpose.

It is very important that, after building the entire desired flow, you click the button “Create” on the lower right corner of your screen to save your BOT.

{% hint style="warning" %}
**Important: It is still not possible to change an SMS BOT after it is created, therefore, if you need to edit an SMS BOT, you must create a NEW SMS BOT based on the existing BOT.**
{% endhint %}


# RCS (Native)

RCS is a channel developed by Google with native integration into Android, eliminating the need for users to install a separate messaging app. It allows for the sending of text, images, GIFs, videos, files, audio, interactive buttons, and even product carousels to individuals or groups of users.

### **Before you start, make sure everything is already configured** <a href="#id-17.rcsnative-pure-beforeyoustart-makesureeverythingisalreadyconfigurated" id="id-17.rcsnative-pure-beforeyoustart-makesureeverythingisalreadyconfigurated"></a>

Once you have contracted RCS, the Provisioning team will assist you throughout the process, handling all necessary configurations to ensure that everything is ready for use!

### **How to send a RCS message** <a href="#id-17.rcsnative-pure-stepbystep-howtosendarcsmessage" id="id-17.rcsnative-pure-stepbystep-howtosendarcsmessage"></a>

### **Go on New Message > New Channels > RCS**

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FzJSqA8MgOGK3xF1u0rbT%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2013.40.07.png?alt=media&#x26;token=8fce5821-fab9-40e4-bece-d2f64d62cf7c" alt=""><figcaption></figcaption></figure>

### **Upload/choose your audience**

You can upload a file (maximum of 105 mb) or choose from Saved Files, Contacts, Groups of Contacts or even send for a few individual numbers.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FlmGeTGIk0yy8lLzUz1nd%2F5.png?alt=media&#x26;token=6527d18c-25e4-4ed3-91d5-82ba32e045a9" alt=""><figcaption></figcaption></figure>

### RCS Content Creation <a href="#id-17.rcsnative-pure-stepbystep-howtosendarcsmessage" id="id-17.rcsnative-pure-stepbystep-howtosendarcsmessage"></a>

There are 3 types of content creation: Simple Text, Rich card and Carousel.

### **Simple Text** <a href="#id-17.rcsnative-pure-02.1.simpletext" id="id-17.rcsnative-pure-02.1.simpletext"></a>

If you choose to create a simple text, you will be able to create and send only text to your final users, without any media. \
It is important to emphasize that within this transmission, we can create content of both Basic and Single types.

**Rule for Basic:**

* write up to 160 characters&#x20;

**Rule for Single:**

* text that exceeds more than 160 characters
* usage of the button

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FjYwzI8ygyqLSm4v2GELq%2F6.png?alt=media&#x26;token=37ea9359-5229-4992-9b4e-9aefda002a8a" alt=""><figcaption></figcaption></figure>

Within Simple Text, you will be able to add up to **10 buttons** (Buttons are not mandatory). There are 2 types: \
\
**Actions** → you can add Phone number or a redirect to a Website\
**Quick Answers** → buttons of select something

### **Rich Card** <a href="#id-17.rcsnative-pure-02.2.richcard" id="id-17.rcsnative-pure-02.2.richcard"></a>

It is a message with media content. Media and Message body are mandatory.

<table data-header-hidden><thead><tr><th width="136"></th><th width="526"></th></tr></thead><tbody><tr><td><strong>Image</strong></td><td>Up to 2MB</td></tr><tr><td><strong>Video</strong></td><td>Up to 10MB</td></tr><tr><td><strong>URL (website button)</strong></td><td>URL length limit is 2048 characters</td></tr></tbody></table>

You can choose between Short / Medium / Tall for media high.\
In Rich card, you can add up to 4 buttons (optional).

<div><figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F6IA7hzKyBLfM5cXLQfhA%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2014.09.26.png?alt=media&#x26;token=806b54df-e6fd-4300-b04a-424105b11efd" alt=""><figcaption></figcaption></figure> <figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FjI9R3ZejtDEbGnxmQGZd%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2014.09.47.png?alt=media&#x26;token=704bb6b6-83b5-4b62-bc81-d5ed9238a508" alt=""><figcaption></figcaption></figure></div>

### **Carousel**  <a href="#id-17.rcsnative-pure-02.3.carousel" id="id-17.rcsnative-pure-02.3.carousel"></a>

Carousel is a set of rich cards to compose your message. Maximum of 10 rich cards.

<table><thead><tr><th width="143"></th><th width="512"></th></tr></thead><tbody><tr><td><strong>Image</strong></td><td>Up to 1MB</td></tr><tr><td><strong>Video</strong></td><td>Up to 5MB</td></tr><tr><td><strong>URL</strong></td><td>URL length limit is 2048 characters</td></tr></tbody></table>

You can also choose between Short / Medium / Tall for media high.\
In Carousel, you can add up to 2 buttons (optional) of Actions and up to 10 of Quick Answers.

You can move your rich cards in Preview, you can drag and change cards disposal and even delete some if you don't like it.

<div><figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fu9PMd1o4zEOWTrw3P596%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2014.15.01.png?alt=media&#x26;token=d907cd00-1048-4753-aefb-7ab0e092b71a" alt=""><figcaption></figcaption></figure> <figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FzYdjBUisFHClp3HRZqS9%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2014.15.19.png?alt=media&#x26;token=32689272-05fd-4f13-af0c-c93dcd0fc093" alt=""><figcaption></figcaption></figure></div>

### **Define a campaign** <a href="#id-17.rcsnative-pure-3.defineacampaign" id="id-17.rcsnative-pure-3.defineacampaign"></a>

After creating your content, you can choose your campaign.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fr4i9TeOfnpSd9BiTluy0%2F9.png?alt=media&#x26;token=e586bf29-b1a7-4af5-a594-1b42758a576b" alt=""><figcaption></figcaption></figure>

### **Schedule your message** <a href="#id-17.rcsnative-pure-4.choosewhenthemessagewillbesent" id="id-17.rcsnative-pure-4.choosewhenthemessagewillbesent"></a>

Define when you will send your message.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FOWxeLaVd2VdxALkLgesX%2F10.png?alt=media&#x26;token=84ef8067-d46d-4c1e-833b-653a28b034d4" alt=""><figcaption></figcaption></figure>

### **Everything is ready. Let's go to your summary!** <a href="#id-17.rcsnative-pure-5.everythingisready-payattentiontoyoursummary" id="id-17.rcsnative-pure-5.everythingisready-payattentiontoyoursummary"></a>

All information consolidated before you send your message.

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FKduc1KJcJDYpGjEwcmzI%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2014.35.38.png?alt=media&#x26;token=9f2c7814-4b2a-4e47-a64e-be4c6b86b783" alt=""><figcaption></figcaption></figure>

### **Once you click to send your message, you will be redirect to this page:** <a href="#id-17.rcsnative-pure-6.onceyouclicktosendyourmessage-youwillberedirecttothispage" id="id-17.rcsnative-pure-6.onceyouclicktosendyourmessage-youwillberedirecttothispage"></a>

<figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FPlePhPLOf65flzgvVbJa%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2014.38.55.png?alt=media&#x26;token=864cea9b-fc78-4332-b811-f05702539c4b" alt=""><figcaption></figcaption></figure>

### **Report**  <a href="#id-17.rcsnative-pure-7.report-directlyinsinchdashboard" id="id-17.rcsnative-pure-7.report-directlyinsinchdashboard"></a>

The current report for RCS is available only in Sinch Dashboard. The data you will have access to includes: Total messages per month, main sending errors, and messages delivered/read/failed.

<div><figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FkFWHuBnF6guQPPBjJOt0%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2015.01.15.png?alt=media&#x26;token=20a1b8c8-a44f-4328-a40d-a3f15d5f4544" alt=""><figcaption></figcaption></figure> <figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FWGxZVnemvhsE7VNWAfmo%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2015.01.27.png?alt=media&#x26;token=b4e3699f-c892-4bb0-9649-0b450ea18071" alt=""><figcaption></figcaption></figure> <figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FXDfdDYtCZ98tWuAQvbWS%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2015.01.36.png?alt=media&#x26;token=1552f1a7-1ded-41fa-8691-908881bb42a0" alt=""><figcaption></figcaption></figure> <figure><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F5601RlMCovyjd72FoP5N%2FCaptura%20de%20Tela%202024-09-03%20a%CC%80s%2015.01.44.png?alt=media&#x26;token=0d314c7d-9655-4486-9a6c-b3f1a1a42b5a" alt=""><figcaption></figcaption></figure></div>


# WhatsApp Embedded Signup

The embedded signup flow simplifies the current WhatsApp signup process, reducing the onboarding period from days to minutes.

Before you start using WhatsApp, sending and receiving messages from your customers, you first need to sign up for a Facebook account, a WhatsApp account, and link a phone number to these accounts in addition to being approved by Facebook itself.

Don’t worry, just follow this guide to set up your WhatsApp account from scratch in just a few minutes within the Messaging platform. If your company already has a Business Manager or WABA, this process will be even simpler.


# Prerequisites

The embedded signup flow simplifies the current WhatsApp signup process, reducing the onboarding period from days to minutes.

Please have all necessary resources at hand to proceed with the embedded signup

### A Facebook Account.

During the embedded signup process, you must log in to your personal or professional Facebook account. If you do not yet have one, use the following link to create one: <https://www.facebook.com/>

{% hint style="info" %}
Facebook does not allow recently created Facebook accounts to go through the embedded signup flow, therefore your account must have been created at least 1 day prior.
{% endhint %}

## Business Manager

It is Facebook’s business management platform for companies that includes all Facebook services and applications (Ad accounts, Pages, Apps, Employees, etc.).

Your Business Manager will be created on the Messaging Platform, and the following information will be required for such:

* [ ] A name for your Business Manager. We suggest using your company name
* [ ] Company’s corporate name
* [ ] Business phone number
* [ ] Company’s website
* [ ] Your business email address
* [ ] Country
* [ ] Corporate address
* [ ] City
* [ ] State
* [ ] Zip Code
* [ ] Time Zone

### Creating a WABA

The WABA, WhatsApp Business Account, is a WhatsApp account within which Phone Numbers (or “Verified Accounts”) will be created

Your WABA will be created on the Messaging Platform, and the following information will be required for such:

* [ ] A name for your WABA (WhatsApp Business Manager). We suggest using your company name
* [ ] A name for your account on WhatsApp Business. This is the name your customers will see; we suggest using your company name
* [ ] Your company’s category, such as: "vehicles," "education," "entertainment," "hospitality," among others.

### New Phone Number

This is the number that will be used on the Messaging platform to send messages to your customers.

{% hint style="info" %}
Watch out because this number cannot be registered to an existing WhatsApp account, whether it is a WhatsApp Business or WhatsApp personal account.

During the WhatsApp signup process, you will receive an SMS or a phone call
{% endhint %}

* [ ] A new mobile phone number!

{% hint style="warning" %}
If you already have a WhatsApp number linked to the account you wish to activate, you will have to delete said account so we can move forward with the process.
{% endhint %}


# Registering your WhatsApp Number

The embedded signup flow simplifies the current WhatsApp signup process, reducing the onboarding period from days to minutes.

Now that you have put together all required information during the 1st step, in order to follow through with the embedded signup of the previous step, it’s time to create your WhatsApp account on Messaging!

## Access your Messaging Account

Access the login page at [https://messaging.sinch.global/](https://messaging.wavy.global/) and enter your access information on the login page.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FNpukfN48xgZUaxmprwLg%2Fimage.png?alt=media\&token=890ecd45-b44a-46fe-9f54-c1335c32749d)

## Begin the Activation Process of your WhatsApp Number

Click "ACTIVATE MY NUMBER" on the upper left corner

![Main page](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGcvfi2kfQvxNmDHmj%2F1.png?generation=1633457257670250\&alt=media)

### Log In to your Facebook Account

!\[Graphical user interface, application, Teams

Description automatically generated]\(<https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGcvfxk6Us_ilrmyZ3%2F16.jpeg?generation=1633457257697725\\&alt=media>)

{% hint style="info" %}
Grab the information requested in the first step

* [ ] To create ur Business Manager
* [ ] Company’s corporate name
* [ ] Business contact number
* [ ] Company’s website
* [ ] Your business email address
* [ ] Country
* [ ] Corporate address
* [ ] City
* [ ] State
* [ ] Zip Code
* [ ] Time Zone
* [ ] To Create your WABA
* [ ] name for your WABA
* [ ] name for your account on WhatsApp Business.
* [ ] Company’s category
* [ ] New phone number
* [ ] Phone number
  {% endhint %}

### Create or Select a Business Manager

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGcvfySDmOyRkcvYDS%2F17.jpeg?generation=1633457257692391\&alt=media)

After creating a BM and having your account verified by Facebook, it is time to create a WhatsApp Business Manager (WABA)

### Create or Select a WABA

![Create or select an existing WABA](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGcvfzqFWCG9_X5hW2%2F18.jpeg?generation=1633457257699042\&alt=media)

{% hint style="info" %}
Before completing your signup process, you can change the display name as many times as you wish. After signing up, you must wait 30 days between requests to change the display name and must follow the embedded signup flow once again; we discourage changing the display name after approval.
{% endhint %}

### Add a New Phone Number

Enter your desired number and the PIN sent to verify said number

{% hint style="info" %}

* Each number is linked to a WABA; choose the WABA to which you wish to link your new number wisely, as the WABA number cannot be migrated after registration
* Each WABA can have up to 25 numbers linked; if you wish to extend this limit, contact Facebook support
  {% endhint %}


# Verifying your Company on Business Manager

The embedded signup flow simplifies the current WhatsApp signup process, reducing the onboarding period from days to minutes.

Now that your signup has been submitted for approval by Facebook

You can begin your limited trial period using your business account, your WhatsApp Business profile that you created, and your WhatsApp Business number to send a **limited number of messages** to a **limited number of WhatsApp users. For more information on your trial period, access:** [**https://www.facebook.com/business/help/2640149499569241**](https://www.facebook.com/business/help/2640149499569241)**​**

**To send more messages** and to actually be able to use our service, **you need to verify your company.**

## Follow the Step by Step Below to Verify Your Company:

In order to have a WhatsApp Business account, you must also be a verified company on Facebook, and this is a step between you as a company and Facebook. Company verification is important to inform if the Business Manager account belongs to a company or organization that actually exists.

We will help you to understand Facebook’s requirements and follow all steps to verify your Company’s account.

Access your company’s business page on Facebook, at the following link: <https://business.facebook.com/>​

### **Click the Business Settings Symbol**

![](broken-reference)

### Click Security Center > Account verification > Start verification

![Start your company’s verification](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGczBnANyTf9XUt8hF%2F1.png?generation=1633457272481813\&alt=media)

### Start Verification, Enter Your Business Details and Click Next

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGczBocIFAzVkXY2I-%2F2.png?generation=1633457272494640\&alt=media)

Select the corresponding business type from the suggestions list or select 'none of these‘ if none of the options fit your company.

* [ ] Follow the instructions to confirm your business details.
* [ ] Choose how you want to receive your verification code: phone call or email.
* [ ] Depending on your location, the phone verification option may be unavailable, therefore Facebook will send your code via email.
* [ ] Add your verification code.

#### If none of the options fit your business type and you have selected ‘none of these,’ you will be required to upload additional documents

* [ ] Proof of business registration: it can be articles of incorporation, a business license, business tax registration, etc.
* [ ] Proof of business address and phone number: it can be an electricity bill, phone bill, bank statement, articles of incorporation, etc.
* [ ] Your tie to this business: something that proves that you are an official representative of this company.

{% hint style="info" %}
Important: After completing your business verification, it will NOT be possible to change your company’s corporate name, address, business phone number, website, or tax identification number
{% endhint %}

## Congratulations! You Have Completed the Account Verification Request Step :)

Now you just have to wait for Facebook to review your request and reply. Once your account is verified, you will receive a notification on your account and also through the email account linked to Facebook:

!\[Graphical user interface

Description automatically generated]\(<https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGczBx2gxbluhcWxEN%2F11.png?generation=1633457272492683\\&alt=media>)

You can also check if your Company’s account has been verified in two other ways on Facebook:

Access "Business settings > Business Information"

!\[Graphical user interface, application

Description automatically generated]\(<https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGczByU6XbD5DcSYmP%2F12.png?generation=1633457272645156\\&alt=media>)

​

Or access "Business Settings > Business Information"

!\[Graphical user interface, text, application

Description automatically generated]\(<https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGczBzkKmpaGeSKhzz%2F13.png?generation=1633457272527106\\&alt=media>)

​

With a verified Facebook account, your Company can now use our solution normally.

{% hint style="info" %}
If you have any questions left, please contact our support team at: <https://servicecenter.sinch.global/>
{% endhint %}


# Potential Errors During the Embedded Signup Flow

The embedded signup flow simplifies the current WhatsApp signup process, reducing the onboarding period from days to minutes.

In some situations, companies may not be able to send messages after completing the embedded signup flow. The following checklist helps to solve messaging problems:

1. Check that a valid payment method has been attached to the WhatsApp business account. Otherwise, sending message templates will fail.
2. Verify that the 30-day period of unverified trial experience has expired. If this has happened, the company will need to verify the phone number before you can send messages again. For more information, see Phone numbers.
3. Check that the trial experience has not already been granted to another phone number on the same WhatsApp business account. In this case, the number must go through the verification processes to be able to send messages.

### See also below for the most common list of possible errors and their solutions during the embedded registration flow.

<table><thead><tr><th width="252.76057268095758">Error</th><th width="221.52023692003954">Description</th><th>Solution</th></tr></thead><tbody><tr><td><p></p><p><strong>An error occurred while processing this request. Please try again later.</strong></p></td><td>Business account creation could have failed due to various reasons, please contact Support for further assistance.</td><td><p>Use an active Facebook account or contact Support for resolution.</p><p></p></td></tr><tr><td><p><strong>You have reached the limit for the number of Businesses you can create at this time.</strong></p><p></p></td><td><p>There is a limit to the number of Business Accounts that you can create.</p><p></p></td><td><p>Please use an existing Business Account.</p><p></p></td></tr><tr><td><p><strong>Your Facebook account is too new to create a business account. Try again in an hour.</strong></p><p></p></td><td><p>New Facebook accounts have to wait for some time to create a Business Manager account.</p><p></p></td><td>Use an existing active Facebook account or wait for a few hours before using your new account. The new Facebook account can be actively used during the wait period.</td></tr><tr><td><strong>We limit how often you can post, comment or do other things in a given amount of time in order to help protect the community from spam. You can try again later.</strong></td><td><p>Your Facebook account was been flagged because of suspicious behavior.</p><p></p></td><td><p>Use an existing, active Facebook account with no prior issues.</p><p></p></td></tr><tr><td><p><strong>You’re no longer allowed to use Facebook Products to advertise. You can’t run ads, manage advertising assets or create new ad or business accounts.</strong></p><p></p></td><td><p>You are unable to create new Business Manager accounts due to previous suspicious behavior.</p><p></p></td><td><p>Use an existing, active Facebook account with no prior issues.</p><p></p></td></tr><tr><td><p><strong>The name you chose for your business isn’t valid. Consider using xxx.</strong></p><p></p></td><td><p>Invalid business name.</p><p></p></td><td>Add a valid name that matches the name of your business.</td></tr><tr><td><p><strong>A user can only create one business user at a time</strong></p><p></p></td><td><p>You can only create a single Business Account within a given time period.</p><p></p></td><td><p>Use an existing Business Account to onboard.</p><p></p></td></tr></tbody></table>


# Human Assistance Policy

* It is mandatory that the path for your customer to obtain human assistance is clear, within WhatsApp.
* Ways to escalate to Human assistance **accepted within WhatsApp’s policy**:
  * **Human Referral within the channel** (we suggest this one, as it makes your customer’s life easier.)
  * **A message clarifying the ways your customer can contact a Human:** Directing them to a phone number, email or web form to open a ticket or directing them to a Physical store.
* E.g.: Hello, to speak to one of our agents please call: XXXXXX
* E.g.: Hello, to speak to one of our agents please email: XXXXXX

[**https://www.whatsapp.com/policies/business-policy/**](https://www.whatsapp.com/policies/business-policy/)

**Note: Failure to comply with this policy will impact the quality of your channel and, if not resolved, it can impact your tier (causing it to be downgraded).**


# WhatsApp Guidelines

Important concepts for WhatsApp business accounts.

### **Introduction - WhatsApp for Business**

{% hint style="info" %}
**WhatsApp:** It is a new technology for the B-to-B market.
{% endhint %}

{% hint style="warning" %}
**Attention:**

Very few companies had access to beginning tests in the year 2017. Despite being announced to the market in August, **still all use cases undergo approval by WhatsApp** – once approved, your company is one of the few that can communicate with their customers through this channel. As it is a new channel and technology, you will need patience and organization within your company so that communications are done as best as possible and always placing your customer at the center.
{% endhint %}

{% hint style="success" %}
**Support**

You will always have the **support** of your **account executive** and the New Business team, specialized in WhatsApp.
{% endhint %}

## **Important Terms**

### **Facebook Business Manager**

It is Facebook’s business management platform. It houses Sinch (company)’s general Facebook account as well as those of our customers. It includes all Facebook services and applications (Ad accounts, Pages, Apps, Employees, etc.). The Business Manager is referred to by an ID that we need to receive from each of our customers - the BM ID (Business Manager ID) - in order to set up the customer’s WhatsApp account (WABA)

### **WABA**

WhatsApp Business Account (WABA) – Account of each Sinch

&#x20;customer on WhatsApp, within which the Phone Numbers (or “Verified Accounts”) will be created

### **Phone Numbers**

Each number is created within a WABA, as a “Verified Account.” After it has been created and installed, WhatsApp can give our customer a GREEN badge, for “Verified Account,” or keep it with the GRAY badge, for “Business Account.” This is a decision of WhatsApp.

### **Container**

Each WhatsApp number requires a technology solution that is linked to (servers.)

## **Expressly Forbidden Actions**

{% hint style="danger" %}
**Messages of a Promotional or Advertising Nature**
{% endhint %}

Actively sending messages about **Sales; Marketing; Promotions.** (Any actions of a spamming nature are forbidden).

{% hint style="danger" %}
**Invasive Messages (Spamming Nature)**
{% endhint %}

In addition to the messages mentioned above, there are infinite messages that can be of a **spamming nature**, and aggressive; thus, **it requires the explicit opt-in for WhatsApp** from the end customer. (There is a section exclusively to discuss opt-ins in this manual).

If you wish to communicate promotions through other channels where information can be requested through WhatsApp, this is fine. (As long as your customer pulls up your WhatsApp and requests it; the chat must be initiated by the end customer). For everything you do in this channel, always keep in mind that the end customer is who decides if you are helping, informing, or bothering them. Thus, we suggest a communication that is always centered on the end consumer. (We have a section discussing this).

### Opt-In

{% hint style="warning" %}
Requesting your customer’s **opt-in before** **sending** them an active message is **mandatory**.
{% endhint %}

**Good Practices**

* When requesting a customer’s Opt-In, we suggest including the WhatsApp number field for them to fill out, so you can also ensure the accuracy of the data. Avoiding sending messages to a phone number that does not belong to a customer.
* Sending an SMS with a click to WhatsApp.

​

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F6ANND9RtkBsTbLzp5Ika%2Fimage.png?alt=media\&token=96af9d27-d52a-41b9-9640-9ec1192d8359)

* Sending a mass email collecting opt-ins.
* Collecting the customer’s opt-in on your website or app.
* Training all PAs to collect opt-ins on the calls.

**Important:** Collect their opt-in and **take the chance** to update this customer’s WA mobile number (one of the greatest issues we face today are outdated bases).

A few examples and closing remarks.

{% hint style="info" %}
**When a customer’s their Opt-In, we suggest including the WhatsApp number field for them to fill out, so you can also ensure the accuracy of the data. (avoiding sending messages to a phone number that does not belong to a customer).**
{% endhint %}

{% hint style="warning" %}
The **WhatsApp** logo should appear near the opt-in field. The examples above are from Ingresso Rápido and Netflix respectively
{% endhint %}

### **Opt-Out**

{% hint style="warning" %}
Give your customer the **option** to **say they do not wish to receive** a certain type of message.

This is also a way to improve your content and adapt to your customer’s interests.
{% endhint %}

{% hint style="info" %}
Suggestion of what should be included in your HSM.
{% endhint %}

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FGQK6O27HOIGXp3j0AuyQ%2Fimage.png?alt=media\&token=b13477db-877c-4f96-9ec0-bc626abcfc66)

{% hint style="danger" %}
**It is extremely important that the Opt-Out happens, abiding by the user’s wish to no longer receive any messages.**
{% endhint %}

We have recently added a new feature to the opt-out mechanic, consisting in the possibility to send automatic replies to users when they opt out or back in.

When users opt out, these automatic replies are sent to them from replies that we set by default, but you can also choose customized response sentences, if the customer requests for our support.

Important: Sending automatic messages is customizable and therefore, when a user sends an “exit,” for example, by default we will send the automatic reply, but it is also possible not to send it, if the customer has such a setting.

Another point of attention is that automatic replies do not prevent the customer from replying to a user’s MO. Therefore, it is possible that a user will receive two messages, one with the automatic reply and the other with the “I don’t understand” from the customer’s bot. So, the ideal is for the customer’s bot to identify messages with the “exit” text, for instance, and not reply to the user in cases of opting out or back in.

### **Replies to Users Opting Out**

When a user begins the opting out process with one of the keywords: "**Sair,**" "**Salir,**" "**Exit,**" "**Stop,**" or "**Detener,**" we can send a corresponding automatic reply for each language. Our replies, by default, are:

"**Sair**" (BR): "Seu pedido para sair da conversa foi atendido. Favor enviar #voltar para retornar!"

“**Salir**” or “**Detener**”: "Tu solicitud de abandonar la conversación se cumplió. ¡Envíe #volver para regresar!"

“**Exit**” or “**Stop**”: "Your request to leave the conversation was accomplished. Please send #start to come back!"

### **Replies to Users Opting Back In**

It is also possible for a user to wish to opt back in and begin receiving messages again. For that, they must send one of the keywords: "#voltar," “#receber,” “#recibir,” “#volver,” or “#start.” We can also send automatic replies in this case, corresponding to each language. Our replies, by default, are:

"**#volta**r" or “**#receber**”: "Seu pedido para sair da conversa foi atendido. Favor enviar #voltar para retornar!"

“**#recibir**” or “**#volver**”: "Tu solicitud de abandonar la conversación se cumplió. ¡Envíe #volver para regresar!"

“**#start**”: "Your request to leave the conversation was accomplished. Please send #start to come back!"

### **WhatsApp - Customer Focus**

{% hint style="info" %}
**WhatsApp** is very concerned about the privacy of its users and their right to be contacted or not by a certain business/ brand through their channel.
{% endhint %}

This is why all actions done in this channel must always have the end customer in mind and the purpose of being useful to the end consumer.

In addition to the **actions you are expressly forbidden** from actively doing (specific section discussing this), there are **invasive actions** and actions that do not generate benefits to the consumer or actions that are repetitive and bothersome.

For this reason, the customer is who decides if you are helping, informing, or bothering them. The customer can always block you if your communication makes no sense to them or if you are being very insistent. The way that **WhatsApp measures** if you are focusing on the end customer and their wellbeing, without being intrusive, is to monitor your **block rate,** i.e., the % of people to which you have been sending messages who have been blocking you. (Unfortunately, your block rate is an information to which we do not have access; WhatsApp notifies Sinch when it starts to go up and can even block your number if it stays high and going up).

{% hint style="danger" %}
Your **block rate** is also related to the accuracy of your base. This is why you should collect **opt-ins** on your website, when purchasing new products; this way, in addition to their opt-in, you ensure your customer’s WhatsApp number is the one you are using.
{% endhint %}

{% hint style="info" %}
**Inform Your Customer that You Have an Official WhatsApp Number**

It is extremely important that you relay your number to your customer. The fact that your customer knows you will communicate with them through WhatsApp and especially that it will be through a verified number is security to both parties.

You can evidence it in all email signatures, on your website, on all purchase receipts. You can even use this to obtain your customer’s opt-in, asking them to send #I want to receive messages to your number.
{% endhint %}

{% hint style="warning" %}
**Avoid Fraud**: Informing your customer that you will now communicate with them through an official number and teaching them to identify that the number is official as shown in the figure below generates trust and prevents your company from being plagiarized, or offering fake discounts, promotions, or even stealing data from your customers.
{% endhint %}

## **Service via WhatsApp**

{% hint style="success" %}
Implementing bots in your WhatsApp channel to handle the most searched topics by users, making it easier to solve problems and reducing the amount of direct service. Transferring to the human assistance platform if the issue is not resolved with Artificial Intelligence only.
{% endhint %}

{% hint style="success" %}
Through WhatsApp, you can assist your customers more quickly, using service platforms exclusive to this channel. On this platform, you can Interact with your customers, answering questions, relaying clear and objective information, and providing necessary support. You can also enrich your conversation by sending files (pdf, images).
{% endhint %}

{% hint style="success" %}
Assisting multiple customers at once, improving efficiency, customer satisfaction, and decreasing service costs.
{% endhint %}

## **WhatsApp Guidelines**

Download the WhatsApp for Business guidelines below:

{% file src="<https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FwpS7M5fBo7uzhpjDRIdN%2FWhatsApp%20Business%20Solution%20PR%20and%20Marketing%20Guidelines.pdf?alt=media&token=f0409f0d-c261-4bb3-b512-cc6e175e06a6>" %}


# Instructions & Good Practices

In this document, we will introduce you to some good practices for using the platform, this way you can enjoy our platform to the fullest.


# Channel Rules

A few factors influence your WhatsApp number’s message deliverability and sending limits. Important indicators are as follows:

## **WhatsApp Number Status:**

WhatsApp splits a number’s status into 5 categories:

* **Offline:** The number is not connected to WhatsApp;
* **Pending:** The number has not yet been integrated and approved;
* **Connected:** The number is online and functioning normally;
* **Flagged:** This is a warning sign. When its quality reaches a low quality rating, the number is moved to a flagged status;

When the quality rating reaches a low state **(red)**, the phone number is moved to a Flagged status.

If the message rating improves to a high **(green)** or medium **(yellow)** state within 7 days, the phone number will return to a Connected status.

If the quality rating does not improve within 7 days, the number will return to a Connected status, but with a lower messaging limit imposed on it.

* **Restricted:** Phone numbers that reach their messaging limit are moved to a restricted status. While restricted, the number will be unable to send any notification messages until the 24-hour window for sending messages is reset. They can still respond to any messages initiated by users.

## **Block Rate & Quality Rating**

For companies that use WhatsApp as their communication channel, it is worth paying attention to two variables: the quality rating and messaging limit. These indicators represent the satisfaction level of end customers and may impact the deliverability of messages sent by the company.

**Block Rate**

WhatsApp allows for the end customer to decide if the company is relevant or not through the “**block**” or “**flag as spam**” features.

A Block Rate is when the end customer blocks your brand’s number on WhatsApp or reports your message as spam.

When interaction with the brand is negative and the customer manifests their dissatisfaction, the block rate impacts the **quality rating** of its messages, and may reduce the deliverability of future messages.

The main reasons for a block are:

* **Lack of opt-in** or consent to privacy policies.
* **Frequency**: Number of messages sent to the same person.
* **Response time**: Delay in service, whether human or bot.
* **Lack of service or resolution in the channel**: a customer wishes to resolve a certain issue in the channel and there is no service.

Some factors that can cause a negative experience are:

• Bad experience with the bot; • The end customer contacts the company regarding subject X and the company insists on talking about subject Y; • Lack of or delay in transferring the conversation to another channel or agent; • Unmet need.

## **Influence of Templates (HSM)**

A Template (**previously HSM**) needs to be submitted for prior approval by WhatsApp, and this does not prevent the account from being flagged for poor quality or having a high block rate.

Examples of HSMs that could cause a block rate (even if previously approved):

* Open Session / New way;
* Vague messages;
* Request for personal information;
* Poor customer base;

## **Quality Rating**

The quality rating shows how messages have been received by customers within the last 24 hours. Three different statuses are displayed:

* **High (green):** Positive engagements;
* **Medium (yellow):** Engagement on alert
* **Low (red):** Poor engagement (**must revise template/bot/base**).

A phone number can display two specific statuses related to messaging limits and quality: [**Flagged**](https://docs.wavy.global/whatsapp/instrucoes-e-boas-praticas/regras-do-canal#status-do-numero-do-whatsapp) and [**Restricted**](https://docs.wavy.global/whatsapp/instrucoes-e-boas-praticas/regras-do-canal#status-do-numero-do-whatsapp).


# Learn More About Tiers

The indicators shown on [Channel Rules](https://docs-latam.messaging.sinch.com/whatsapp/instructions-and-good-practices/channel-rules) influence your message sending limitation.

The message deliverability limitations determine to how many unique users your company can send messages daily. This includes new chats and existing chats with users.

Your message limit does **NOT** restrict the number of messages your company can send, only the amount of users who can receive them.

It does also NOT apply to messages sent in reply to a message initiated by the user within a 24-hour period.

## **Understanding the Tiers**

Upon registering its phone number, a company begins at **Level 1**, which has a limit of **1,000** messages sent **every 24 hours**.

* **Tier 1** - Allows you to send messages to 1,000 unique users every 24h.
* **Tier 2** - Allows you to send messages to 10,000 unique users every 24h.
* **Tier 3** - Allows you to send messages to 100,000 unique users every 24h.

A number that is in Tier 3 **can drop to a lower tier due to poor quality.**

## **How to Upgrade Your Tier?**

A company’s phone number will be upgraded to the following level if:

1. Its quality rating is not too low.
2. The cumulative number of users to whom it sends notifications adds up to twice the current message limit within a 7-day period. A company will be upgraded from Level 1 to Level 2 when it sends messages to a total of 2,000 users within a 7-day period, for instance.

The minimum amount of time in which this change can occur is **48 hours after the 1st trigger**.

A few possible scenarios below:

**Scenario 1:** Every number begins at tier 1. The company will move up to the following level once it sends messages to a total of 2,000 users within a 7-day period, for example, and has a good quality rating.

![Scenario 1](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGelOpGGK_hRcfivfS%2F0.png?generation=1633457739744324\&alt=media)

**​Scenario 2:** A low quality level (Red) causes the number’s status to change from Connected to Flagged.

During its Flagged period, the number had good quality (Green/Yellow) in its deliveries. After the 7-day period, the customer goes up to the next Tier.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FaFHsvvf7DDHmn99Q32eK%2Fimage.png?alt=media\&token=6c935f48-5d93-4c41-abb3-d5773ae0cee9)

**Scenario 3:** A low quality level (**Red**) causes the number’s status to change from Connected to Flagged.

​

![Scenario 3](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGelOrU0lmC4wLXStr%2F2.png?generation=1633457739751866\&alt=media)

During its Flagged period, the number continues to have poor quality (red). After the 7-day period, the customer goes back to the previous Tier, which allows their company to send a smaller number of messages.


# Good Practices

In order to maintain a high quality and be able to upgrade your tier, we recommend some good practices:

* Always check if your messages follow the [WhatsApp Business Policy](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR1ec4FMqKNTvk3K6ZQ7jzrKhrZjqVl9JF8nheX_gnjSt5io8Jrj2hbBJXE).
* Only send messages to users who have accepted to receive messages from your company. Carefully check your base:
* Quality base: Your base needs to be recent and have a WhatsApp opt-in. (Users who have interacted with the brand in less than 4 months, preferably having specifically opted in to this channel. The amount of phone numbers required depends on which tier you wish to reach.)
* Create highly personalized messages that are useful for users.
* Avoid sending overly vague introductory or welcome messages.
* Take frequency into account: avoid sending too many messages per day to customers. Be careful when preparing informative messages, being mindful of content optimization and conciseness.

## **It Is Important to Always Observe Channel Restrictions;**

* Sending spam, fraud, or unsolicited publicity (consent) is forbidden;
* Do not create games involving competition or luck;
* Tobacco items and related paraphernalia;
* Alcohol;
* Unsafe ingestible supplements;
* Animals: businesses may not transact in the sale of any animals;
* Adult products or services;
* Weapons, ammunition, or explosives;
* Illegal products or services;
* Drugs, whether prescription, recreational, or otherwise;
* Medical and healthcare products;
* Body parts and fluids;
* Items or products with overtly sexualized positioning;
* Real money gambling services;
* Dating services;
* Products or items that facilitate and/or encourage unauthorized access to digital media;
* Digital and subscription services, including links to or processing of any subscription sales, renewals, or upgrades;
* Real, virtual, or fake currency;
* Third-party infringement.

**For more information:** [**https://www.whatsapp.com/policies/commerce-policy/**](https://www.whatsapp.com/policies/commerce-policy/)​

## **Be Mindful of Your End Customer’s Needs:**

* Having your customer’s confirmation (opt-in) is the first step to preventing an increase in your block rate;
* Draft, publish and make available your Privacy Policy.
* The customer is the center of the entire operation and must see value in every interaction on WhatsApp;
* Paying attention to the communication guideline is essential (message frequency and quality of each message’s content);
* Human referral: the assistance transfer done by your company’s bot or team should be easy and transparent so that the end customer will always have the solution they seek in the channel.
* Opt-out: Always let your customer know that they can always enter EXIT to stop receiving messages, in all templates you actively send them. (this prevents blocks and values your customer’s freedom.)
* Keep your bot in line with the WA guidelines;
* Make sure your messages follow the [WhatsApp Business Policy](https://www.whatsapp.com/legal/business-policy/).
* Periodically check the quality of your solution;
* Do not send content that goes against the [WA Commerce Policy](https://www.whatsapp.com/policies/commerce-policy/).

## **Creating Templates**

Words that should be avoided when creating templates:

**Always watch out for:**

* Abusive content;
* Formatting errors;
* Grammar mistakes;
* Allow your customer to let you know that they are not the customer you think, e.g.: "I am not Caroline"
* Conduct A/B message tests to better explore your best-performing messages.

## **Human Assistance**

* It is mandatory that the path for your customer to obtain human assistance is clear, within WhatsApp.
* Ways to escalate to human assistance accepted within WhatsApp’s policy:
* Human Referral within the channel (we suggest this one, as it makes your customer’s life easier.)
* A message clarifying the ways your customer can contact a Human: Directing them to a phone number, email or web form to open a ticket or directing them to a Physical store.

**E.g.**: Hello, to speak to one of our agents please call: XXXXXX

**E.g.**: Hello, to speak to one of our agents please email: XXXXXX

**For more information:** [**https://www.whatsapp.com/policies/business-policy/**](https://www.whatsapp.com/policies/business-policy/)

**NOTE:** Failure to comply with this policy will impact the quality of your channel and, if not resolved, it can impact your tier (causing it to be downgraded).


# WA Template - What Is It?

Learn how WhatsApp’s Message Template works.

**WhatsApp templates**, or message templates, are formats for common reusable messages that can be sent by a business through our Messaging platform.

Every template **must be approved** by WhatsApp before being used – this way they can ensure you are following the guidelines for allowed content.

Before submitting your Template for approval, remember that it needs to contain the entire message you wish to send.

You can add dynamic fields (variables) to your message, which you can replace with keywords when it’s time to send, such as: names, businesses, addresses, or with default words that make sense in your text.

## [​Click Here for Tips on Creating Your Template](https://docs-latam.messaging.sinch.com/whatsapp/registering-a-template)​

The flow for registering and requesting a new Template is done directly on the Wavy Messaging platform.

See below how to register a template.


# Registering a Template

Creating a WhatsApp message template. Learn how to register your template.

Templates

We will teach you how to follow this process in a few steps and in a straightforward manner!

{% hint style="success" %}
Registering WhatsApp Templates has never been easier!
{% endhint %}

**If you have any questions** about Templates (also known as HSMs) access: [WA Template WA – What Is It?](https://docs.wavy.global/whatsapp/template)​

## Checking Templates:

In the "**Templates**" menu under Messaging, you can check all templates that have already been submitted for Facebook’s approval and also create and submit new templates for review.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FxFTC3k1YybRM7P8U35uS%2Fimage.png?alt=media\&token=b4885dbd-10e5-4cd8-ba6c-c5c88268d015)

You will be directed to a page where you can view all templates that have been created. If you haven’t yet created any templates, the screen will appear blank.

You have the following information:

1. **Template name:** Name that was chosen during its creation.
2. **Type of message:** There are more than 10 message options (account update, warning, appointment, payment, etc.).
3. **Preview:** You can view the text of your message.
4. **Languages and approval status:** Language chosen for your template and its approval status on Facebook. There are three approval statuses: Under review, Denied, Approved.
5. **Actions:** Option to view your template completely on the creation screen.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FkqJdtk1Mi6FtnAIS6Oq3%2Fimage.png?alt=media\&token=d7477953-5387-4425-b3f7-96b7be4cf4d5)

**Template approval depends exclusively on Facebook, and you cannot edit or resubmit for review a template that has been rejected by Facebook.**

## New Template

Creating a new template is simple. Remember that all templates are reviewed before being approved; the time for this approval varies, so make sure not to create your template the moment you want to send a message.

To create a new template, on your left-side menu, click on: **WhatsApp > Templates** and then **Create Template:**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FbO0mJ9Md626LvPOfv0Qv%2Fimage.png?alt=media\&token=42944529-a06c-44eb-83f7-5132b9d7887c)

In a new platform update, we added a feature where we send suggestions of templates that also need to be approved, but that you can use as a base:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F1h9oqBVJKGstet21d7Ic%2Fimage.png?alt=media\&token=6f8ef0db-96b5-4161-87dd-03ab6e9da829)

### Template Name

All templates need a name. It should always be entirely in lower-case letters; you can use numbers and underscores (\_) as spacers. Special characters are not accepted.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F8sGJuX1Fm87YEoE135BI%2Fimage.png?alt=media\&token=9ffd6ea2-bc8e-478d-9f00-b3179649f67e)

### Template Categories

**Attention!!!**

As of **June 1, 2023**, Meta will apply changes to the WhatsApp Business Platform business model globally.

The main changes will be:

1. Update of conversation categories
2. Cost update by category by Target
3. Free entry point via click to WhatsApp or Facebook page will have a free 72h window - currently it is 24 hours.
4. The first 1,000 free conversations of each WABA are now valid for User-initiated conversations/Service conversations only, and no longer the first any 1,000 conversations.

{% hint style="info" %}
**Pay attention when registering and choose the most appropriate category for your message. There are currently 4 template categories:**

* **Utility Conversations:** Facilitate a specific, agreed-upon request or transaction, or update a customer on an ongoing transaction, including post-purchase notifications and recurring billing statements
* **Authentication Conversations:** Allow enterprises to authenticate users with one-time passwords, potentially at multiple stages of the login process (e.g., account verification, account recovery, integrity challenges)
* **Marketing Conversations:** Include promotions or offers, informational updates or invitations for customers to respond / take action. Any conversation that does not qualify as utility or authentication is a marketing conversation.
  {% endhint %}

{% hint style="info" %}
**NOTE:** There is a fourth new category, where it is not used to create a template, which is Service Conversations - all user initiated conversations will be categorized as Service Conversations, which help customers resolve queries.
{% endhint %}

### Language

WhatsApp will not translate messages for your company. All translations of message templates must be entered by you in the same format as shown below. When creating a template, you will specify the language in which you wish your message template to be displayed using the language field.

### Body of the Message

In order to structure the message of your template, you can set the texts in the following fields:

**Header (optional):** title of your message, where you can enter a text or media, which can be a Picture, document, location, or video. If you choose the text option, your text will only show up in the preview once you start typing the body of your message; using text, you can use up to 60 characters.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FHczh5OJ4edxjMw1ODwmp%2FHeader.gif?alt=media\&token=033b4de7-2b74-458f-ab17-2a5f35db5a3c)

**Body (required):** The body of your message is where you type the text that will be sent to your customer. You can add emojis, use bold, strikethrough, and italic formats, and also use placeholders (variables). Variables are numbers that appear between curly brackets {{1}}; you can use these fields as dynamic fields and change what is between curly brackets for a default word or use the header of a file to fill out the field. **Your text can contain up to 1024 characters.**

If your placeholder (variable) is edited to something other than numbers between the “curly brackets,” a warning is displayed with instructions for use: they must always be in ascending order. For example: {{1}}, {{2}}, {{3}}.

* After finishing your template, you will be required to tell the platform what you wish to enter in this field.

![variable](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGfVMU7AdcqeTlcRDl%2F9.gif?generation=1633457932825516\&alt=media)

**Footer (optional):** The footer is optional. You can add a few words of gratitude, for instance, you can only add text contents and use up to 60 characters. It will show on the right side in your preview in a lighter shade of gray.

![foote](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGfVMVVGuRV8LcBHid%2F10.gif?generation=1633457932809041\&alt=media)

**Buttons (optional):** There are 2 types of buttons that can be used; however, you can only use one or the other.

The buttons are: **Actions:** You can direct your customer to a phone call or a website chosen by you:

![action buttons](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGfVMWGle1m1zsBo08%2F11.gif?generation=1633457932815318\&alt=media)

**Quick replies:** Usually used with **yes** or **no.**

![quick replies](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGfVMXOwfBvn12vPh3%2F12.gif?generation=1633457932867567\&alt=media)

**Important:** The text formatting in each field is distinct. **Header:** It is bold at the start of the message; if you have chosen a media header, a preview of your picture will appear. The media is only attached once your message is triggered to customers. **Body of the message:** The body of your message appears in a light shade according to your settings data. **Footer:** It appears in a lighter shade of gray at the end of your message. **Buttons:** They appear at the endo f your message for the user to click.

![preview](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGfVMYqzALHzLFxSeY%2F13.png?generation=1633457932812881\&alt=media)

After reviewing your template, click create on the bottom of your screen. Your template will be submitted for review by Facebook; the estimated time for reply is up to **5 days**.

![create template](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGfVMZ-KZdjXvH7GmG%2F14.gif?generation=1633457932945653\&alt=media)

After submitting your template for approval, you will see 3 status types: **Green:** Template approved and ready for use. **Blue:** Your template is under review. **Red:** Your template has been denied.

**If a template is denied, it cannot be resubmitted for review. You must create a new template and request a new review.**

After the status of your template changes to "**ready for use,"** just go to the "**New message**" menu, search for the name of your template and send your message.

## General Tips for Creating Templates

**Tips for creating your template**

* **Give clear names to your templates**, which refer to the content of your message and explain the context in which it will be sent, with only lower-case letters, numbers, and underscores (spacers).
* **Choose the correct category for your template.**
* The content should be **clear, brief, and to the point.**
* **Find out if there are specific moments of your operation for which you can create default templates that can be reused.**
* When your message is written, you should consider the fact that the team in charge of approvals does not know the context in which they are inserted.
* **Read your template out loud** and notice how it sounds.
* **Pay attention to your HSM formatting.** Dynamic fields must be according to standards, and the message cannot contain any typos or grammar mistakes.
* **In order to reopen a session with your user, mention what you had been previously talking about.**
* **Do not induce your customer to remain in the flow.**

### Formatting

**Issues with formatting lead to a template being rejected.** Pay attention and make sure your text is according to acceptance standards.

* **Dynamic fields** must be numbers between two curly brackets and surrounded by information that clearly indicate what will be inserted there;
* **We cannot** use line breaks, tab, or consecutive spaces.
* **Grammar mistakes and typos will cause your template to be rejected.** Slang and informal language are accepted, but you should note that they will **not always** make sense for the team in charge of approvals.

### Formatting Examples

| Correct Formatting                                                                       | Incorrect Formatting                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Hello, {{1}}! How are you? This is your flight ticket number: {{2}}.**                 | <p><strong>{{1}}</strong></p><p><strong>How are you? Below are your ticket details:</strong></p>                                                                                                             |
| **Your flight to the city of {{3}} is scheduled for {{4}}, at {{5}}. Have a nice trip!** | <p><strong>{{2}}</strong></p><p><strong>{{3}}</strong></p><p><strong>Make sure to write down your flight details so you don’t forget:</strong></p><p><strong>{{4}}</strong></p><p><strong>{{5}}</strong></p> |

### Template Rejected? What Could Be the Reason?

**You are not allowed to send promotional content** i.e., all types of offers that **have not been requested by the customer.** There are certain words that lead FB’s approval team to believe that a template is promotional, even when its content does not have that intentio&#x6E;**:**

**Price reductions/changes**

* Promotion;
* Promotional;
* Promo;
* Offer;
* Proposal;
* Sale;
* Discount;
* Bargain;
* Deal;
* Advantage;
* Clearance;
* Steal;
* Markdown;

**Advertising and news**

* Ad
* Advertising
* Propaganda
* Commercial
* Release
* Limited edition
* Promote
* Publicity
* Opportunity

**Gratuities**

* Sample
* Coupon
* Lottery
* Gift
* Surprise
* Freebie
* Giveaway

### Examples of Rejected Messages

| ​                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Did you know you have a pre-approved loan of {{1}}? You can pay it back in up to {{2}} installments, and the money is credited to your account within 24 hours after approval! Don’t miss it! This offer is available until {{3}}.**                  |
| ​                                                                                                                                                                                                                                                       |
| **Hi, {{1}}! How are you? We have great news! You are only one click away from contracting your loan. Just reply to this message and we can help you!**                                                                                                 |
| ​                                                                                                                                                                                                                                                       |
| **This is the Digital Assistant speaking on behalf of {{2}} store. We noticed you are interested in {{3}}, at the {{4}} portal. How about simulating a loan, scheduling a test drive, or speeding up your used car review? Just click the link: {{5}}** |
| ​                                                                                                                                                                                                                                                       |
| <p><strong>We have news for you! In order to check it out for free and get ready to increase your sales, enter:</strong></p><p><strong>1 - to see the {{3}} collection;</strong></p><p><strong>2 - to receive the {{2}} catalog.</strong></p>           |
| ​                                                                                                                                                                                                                                                       |
| **We have a proposal for you! Can we chat here right now?**                                                                                                                                                                                             |

## Opening a Session

A session is the 24-hour period from the moment you receive a message from your user. That is, **only MOs (messages sent by your customer) open a session.**

You must send a template to start the conversation and, from the moment your user replies, the session is open and you can directly communicate with them without requiring a new template. You can send free texts, pictures, attachments, videos.

## A Few Expressly Forbidden Actions

#### **Messages of a promotional, advertising, or invasive nature (spam)**

Message templates regarding **Sales; Marketing; Promotions.** Any actions of a spamming nature are forbidden. For everything you do in this channel, always keep in mind that the end customer is who decides if you are helping, informing, or bothering them. Thus, we suggest a communication that is always centered on the end consumer.

## **Template Suggestions**

**1: General information (very similar to collecting an opt-in in the channel)**

Hello! We would like to inform you that this is the official channel for XXXXX. You can use this channel to XXXXXXX.

Click the "Yes, I want it!" button to begin receiving messages or "Exit" if you are not interested: Buttons: Yes, I want it! / Exit

**2: Assistance for people who wish to purchase products / services, ensure their opt-in is collected on the actual website, and when the base is less than 3 days old.**

Hello, we noticed you have signed up for our website. We would like to let you know that this is our WhatsApp channel, and we can answer any questions you may have here.

Click the "Yes, I want it!" button to learn more or "Exit" if you are not interested:

Buttons: Yes, I want it! / Exit

**3: Bank slips / invoices**

Hello, this is the official channel for the XXX company for information on invoices payable or overdue / order status / account status. Click the "Yes, I want it!" button to begin receiving messages or "Exit" if you are not interested:

Buttons: Yes, I want it! / Exit

**4: Order status**

Hello, this is the official channel for XXXX for information and order statuses. Click the "Yes, I want it!" button to begin receiving messages or "Exit" if you are not interested:

Buttons: Yes, I want it! / Exit

**5: Consigned credit / Loans**

Hello, this is the official channel for XXXX, here you can ask any questions and learn more about XXXXXXX. Click the "Yes, I want it!" button to learn more or "Exit" if you are not interested:

Buttons: Yes, I want it! / Exit

### **Automatic Replies:**

**EXIT:**

Your request to leave the conversation was accomplished. Please send #start to come back!

**#START:**

Your request to return to this conversation was accomplished! Welcome back!

**YES:**

**1: General information (very similar to collecting an opt-in in the channel)**

Thank you, you will receive this information here, stay tuned.

**2: Assistance for people who wish to purchase products / services, ensure their opt-in is collected on the actual website, and when the base is less than 3 days old.**

Thank you, we will contact you soon to answer your questions

Thank you, send a Hi to begin your assistance

**3: Bank slips / invoices**

Thank you, you will receive this information here, stay tuned.

**4: Order status**

Thank you, you will receive the status of your order(s) here, stay tuned.

**5: Consigned credit / Loans**

Thank you, we will contact you through the channel soon to better assist you.

It’s great having you here. We will always keep you informed through this channel, and whenever you need us, just let us know


# Deleting a WA Template

You can delete a template that has been approved, is under approval, or has been denied by WhatsApp through the Messaging platform.

**How To:** On the template list, click the trash can and await the 30 days of confirmation by WhatsApp to create a new template with the same name as the one you deleted. You cannot send a template after it has been deleted.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FrMu2DuExkHBk2fHoMjRt%2Fimage.png?alt=media\&token=94cdcc2c-8ca8-41de-8128-b5ed3a74e280)


# WhatsApp Account Settings

Learn how and what you can change in your WhatsApp profile

{% hint style="info" %}
After all the process of creating a WhatsApp account, it is possible to carry out all the management of WhatsApp information within the Sinch Messaging platform.
{% endhint %}

## **Editing Your WhatsApp Profile**

{% hint style="danger" %}
**BE CAREFUL! Changes will be made instantaneously!**
{% endhint %}

{% hint style="success" %}
**What you are allowed to change:**

* Your Company’s industry
* Status
* Description
* Address
* Website
* Facebook or Instagram page
* Email
* Picture
  {% endhint %}

{% hint style="danger" %}
**What you are not allowed to change:**

* Your Company’s name;
* Phone number;
  {% endhint %}

## **How to Manage Your WhatsApp Account:**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F2nMqqtaztaq3p7EOsB9X%2Fimage.png?alt=media\&token=0a72d50c-cb57-4874-b2a5-93059d1356ff)

### **Account on Mobile Device:**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGfztvemHQdHon0qo9%2F1.png?generation=1633458061296789\&alt=media)


# WhatsApp Dashboard

Learn more details about your WhatsApp Dashboard

## **WhatsApp Dashboard**

This is where you see general and detailed information on messages triggered to WhatsApp

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FPAf2uBWYT5W6do3puNpY%2Fimage.png?alt=media\&token=7a423a74-f453-45c7-be38-8ba47299dfb8)

### **Field descriptions**

* Total messages: This is where you can view the total number of messages sent and received within a selected period.
* Date filter: It is located on the upper right corner; just select the period you wish to filter.
* Total MTs: Total number of messages sent.
* Sent: Messages that have left for delivery on the platform.
* Sent with open session: These are the messages that have been sent and delivered to devices, where the end user replied to your message.
* Sent with closed session: These are messages that have been sent and delivered to devices, but your end user did not reply to your message.
* Delivered: Messages that have been sent and delivered to devices.
* Read: Number of messages according to the stipulated filter that have been read by your end users; a point of attention is that we only have this status if your end user has the read receipt enabled.
* Total MOs: Number of messages your end users have sent to your company.
* Session-opening MOs: Number of users who contacted your company, without any interaction from you.
* Under Open Sessions Now you have the data of live open sessions.

### **Overview**

To access this field, just switch the tab on your screen:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FsuYcW5Iuh7Q0yLrI8Ec5%2Fimage.png?alt=media\&token=60a78619-b606-4f38-8140-7ca64b157c69)

{% hint style="info" %}
**Overview**

This is where you can filter your charts to better review your triggers

View

* Time
* Day of the Month
* Month

Charts

* Total MTs
* Sent
* Delivered
* Read
* Total MOs

Additionally, you can also filter by **Campaigns, Subaccounts and Users.**
{% endhint %}


# Tech Providers - What is it and how does it work?

The Tech Provider refers to companies that need, in a legitimate way, to access commercial data from other organizations to offer services or functionalities to them. Here, we can understand it as Reseller companies.

No app claimed by a company can be used by other companies until the verification as a Tech Provider is completed. Account Admins can finalize the verification process for the company to be recognized as a Tech Provider. Once verified, any app claimed by the customer can be used by another customer of this reseller.

## How does it work?

If you are a Reseller company, it is necessary to have an ISV (Independent Software Vendor) registration directly in Meta's BM (Business Manager). The administrative part of the process is first carried out in your BM, either by you or you can request support from our Support team.

Once this is done, you can proceed with the Embedded SignUp process. Remember that if it is necessary to create other customers on the Messaging platform (MM2), you should contact our Provisioning team (Support)!

## How to do it: step by step

1. You (Reseller) must have access to the BM as an Admin and be an ISV.
2. It is necessary to have an app within this BM (to learn more about how it works, see [here](https://developers.facebook.com/docs/development/create-an-app/)). As a Reseller (ISV), it is required that this BM be verified by Meta.
3. Make sure your app is in "live" mode and not in development mode. If this is not set up this way, you will receive an error in the embedded signup process. The app is created by default in development mode, and you can switch the mode on the app's page.
4. Once everything is set correctly in the app, it is important that you are connected to our Sinch app. If you don't have it, go to the left sidebar of the BM, click on Partner Solutions, and then click to create a Partner Solution. Next, you should define a name for the solution (internal) and add the Sinch AppID in the Partner app ID field. The Partner app ID varies based on the BM to which we will connect the number (to access this partner app ID, contact our support and inform them that you are going through the Tech Provider process on your own).
5. After you follow these steps, we at Sinch must accept the partnership solution request on the partnership solutions page of our app! Once accepted, just continue with the embedded signup process. If you need to create more customers in your reseller or need support in this process, simply reach out to our Provisioning team (Support)!


# Planning your bot

Before you start building your bot on our platform, there are a few strategic steps to consider. From defining the use cases to crafting a bot personality – here's how to get started.

## **1. Define the bot's goal** <a href="#id-6f63" id="id-6f63"></a>

Before you can start building your bot, you need to know **why** **you are building it**. What is the goal here? If you want to automate an existing service, what is the current experience like, and how could a bot help you improve it?

Make sure to look at your business and marketing goals: if one of your goals is to increase customer satisfaction, you may want to add a bot to your customer support team and let it handle the most common FAQs, so your team has more time to focus on the complex cases.

## 2. Define the bot use cases <a href="#id-9f38" id="id-9f38"></a>

After figuring out the why of your bot, it’s **time for the what**. What is your bot going to do exactly? How will it help the user? We cannot stress how important it is to figure this out **before** **you start building your bot**, as you cannot build something that isn't defined yet.

Here are some good use case examples:

* Book a table at a restaurant
* Play a song
* Find specific products
* Recommend new products
* Get directions
* Book a flight
* Show local promotions
* Process returns

## 3. Understand your tech <a href="#d127" id="d127"></a>

Know that you know the why and the what of your bot, it’s important to understand the where: **where will your bot live?** Will it be integrated with WhatsApp? Can customers engage with it via SMS, Facebook Messenger or on the company website? **What are the restrictions of each channel?** A bot that talks to your users via SMS won’t be able to use as many characters as a bot that only communicates via web. So make sure you understand your tech and its limitations.

> Our platform allows you to easily connect your bot to multiple channels and all your back-end databases. That's how you provide your users with a truly delightful experience.

## 4. Know your user <a href="#id-948d" id="id-948d"></a>

In order to design an experience that feels personal, you need to make it personal. **Who is this user that will engage with your bot?** Remember, there is no such thing as a universal user! It’s important to know what users want and how they are feeling during the conversation.

* What’s their backstory?
* Their challenges?
* Their motivations?
* How familiar are they with your business and using bots in general?

## 5. Craft your bot personality <a href="#eb7b" id="eb7b"></a>

How can you make sure that your users connect with your bot and that the conversation is engaging and representative of real human interaction? By giving your bot a **clear** **personality**.

If you can, use your company branding as a starting point and build on it. You can read more about how to design your bot’s personality [**here**](https://chatbotslife.com/how-to-design-your-chatbots-personality-free-download-dd9eeccffbb9).

## 6. Script your happy flow <a href="#d5fb" id="d5fb"></a>

Now that you have a clear picture of who’s communicating (your bot persona and your user ID) and what they’re talking about (your use cases), it’s time to write the **dialogues**.

**A ‘happy flow’ is** **a dialogue where everything runs the way it’s supposed to run**. The conversation is natural and smooth, and the user reaches their goal in as little steps as possible. Many conversation designers start with the happy flow because it’s the flow of least resistance. It takes the least amount of effort to script because it doesn’t include many of the inconvenient complexities that can occur.

But they will, and you need to be ready for when they do.

> **A great way to script a natural conversation is by creating a sample dialog**. Have two people sit back-to-back and improvise a conversation around a use case, with one person playing the user and the other playing the bot. Record their conversation or take notes to see which parts of the dialog still need a bit more work.

## 7. Script for edge cases <a href="#id-06e9" id="id-06e9"></a>

While our AI technology is very good, it is not yet capable of understanding every user utterance well enough in order to reply in a correct way — no matter how well the script is written, in tricky situations, it will most likely fail. So after writing the happy flows, write out the most likely ways a user might go off track and how you’re going to deal with that. The sample dialog should help those pain points, as will user testing.

What if a user asks your bot how it’s doing? What if they tell the bot they don’t like it? What if they want another suggestion? What happens if the user wants to book a table for two, but one person is allergic to gluten and the other one doesn’t eat fish?

You can find these kind of questions as prebuilt intents in our platform's NLP section. These intens are predefined and come with their own expressions, which means you can use them straight away!

Always make to strategically guide the user back to an existing flow, like in the example below:![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MMLXDBCFeefGMWius7I%2F-MMLZSwhq6g3ne3-TL3M%2Fimage.png?alt=media\&token=65476735-3ebd-405a-9f0f-16fd90b78c47)A good answer to an out-of-scope question that puts the user back on track

## Time to start building <a href="#time-to-start-building" id="time-to-start-building"></a>

Now that you've done all the groundwork, it's time to build your bot. Continue to our next tutorial: [Creating a new bot/tutorials/tutorial-getting-started](https://docs.chatlayer.ai/tutorials/tutorial-getting-started)

​


# Creating a new bot

*Are you working on an existing project? Then you don't need to set up a new one. Feel free to skip ahead to the next tutorial:* [Adding content to your bot/tutorials/tutorial-adding-content](https://docs.chatlayer.ai/tutorials/tutorial-adding-content)

## Creating a new bot <a href="#creating-a-new-bot" id="creating-a-new-bot"></a>

What better way to learn how to build a bot than building one! To help you get started, we'll go through a bot-building tutorial together. In this tutorial, you will create a bot called Choo Choo: a digital assistant that can help people book train tickets.

{% hint style="warning" %}
To get started, you need a Chatlayer account. **Don't have an account yet?** [Create a trial account here](https://chatlayer.ai/try-now/)**.** Have a problem with your account? Contact our support team [here](mailto:support@chatlayer.ai).
{% endhint %}

1.Go to <https://app.chatlayer.ai/> and log in using your credentials

2\. To build a new bot, click the blue `+ Add bot` button:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGtSWzaQln1DHqbTDJ%2F-MkGtYkFkZ-E07BxtJ63%2Fimage.png?alt=media\&token=bb7eac66-47f1-403d-b130-20ee6a26570b)

3\. Choose "Start from scratch". You can add template bots to your account later

<div align="center"><img src="https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FzwNGl7eJPFCnIqd2Qi9E%2Fimage.png?alt=media&#x26;token=c31fc342-eb52-4155-8667-3e7d25ef3af6" alt=""></div>

4\. Now enter `Choo Choo + your first name` as the name of the bot, so you can easily find it again after

5\. Then select your primary language. This is the language that your bot will use. If you'd like to create a multilingual bot, you can add extra languages.

6\. Now click `Create` to create your new bot!

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FiCNOGZn4Iy6iUEBAJheo%2Fimage.png?alt=media\&token=99aea785-4a22-4178-ad4b-872572c683aa)

## Creating bot dialogs <a href="#creating-bot-dialogs" id="creating-bot-dialogs"></a>

1.In the menu on the left, click on Bot dialogs

2\. Then go to the Generalflow by clicking the green flow icon:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGtSWzaQln1DHqbTDJ%2F-MkGtstupWqpA_B3LB38%2Fimage.png?alt=media\&token=facd58a8-b045-4cb4-b9e5-a452bde0ca30)

{% hint style="info" %}
**Flows** are a way to group bot dialogs that are about the same topic or use case. You will learn more about them later.
{% endhint %}

3\. In the 'general' flow, you will see an overview of all the bot dialogs that are part of this flow. When creating a new bot, you always start with a few predefined dialogs:

* Not understood
* Introduction
* Offloading open
* Offloading closed
* Bot disabled
* Error occurred
* ...

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGtSWzaQln1DHqbTDJ%2F-MkGtz69wusVWRNC4orB%2Fimage.png?alt=media\&token=2b392ab7-673b-426a-b6ab-368992253415)

{% hint style="info" %}
To navigate the screen, you can zoom in or out by using the scrolling wheel, or with your trackpad. You can also click and drag to move through the dialog tree.
{% endhint %}

## Step 1: Adding an introduction <a href="#step-1-adding-an-introduction" id="step-1-adding-an-introduction"></a>

The first thing you'll need to do is create an introduction. This is the first message your users will see, the dialog your bot will use to introduce itself and help users understand its functionalities. Introductions are an important way to set the proper expectations of a bot.

* You can edit the introduction by clicking the `introduction` bot dialog.

{% hint style="info" %}
**What is a bot dialog?** A bot dialog is a something that the bot will say or do when triggered by a user [intent](https://docs.chatlayer.ai/understanding-users/natural-language-processing-nlp#intent) or user message. This can be anything: from a message to a user to connecting to an external system, giving a message back and jumping to a different dialog in the flow. We will come back to the [four different types](https://docs.chatlayer.ai/bot-answers/dialog-state) of bot dialogs.
{% endhint %}

{% hint style="warning" %}
Chatlayer.ai supports multiple media types. Depending on the channel your bot will use (Facebook, Slack, Skype, Google Home, ...) these will be rendered slightly differently. For now that is not a problem, but check out [this page](https://docs.chatlayer.ai/channels/multi-channel/) when you start building your 'real' bot.
{% endhint %}

Since this is our first bot and our first message, let's start with a simple text message:

* Delete the predefined greeting message by selecting the following text:

> Hello. Please configure the introduction dialog state with a meaningful message.

* Replace it with the following text:

> Hello there, I'm Choo Choo, your digital assistant

* Click on `Text` in the section 'Add bot message' to add a second message and enter the following text:

> How can I help you today?

The result will be:

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FzErRIbDRlAaz8qGaymqZ%2Fimage.png?alt=media\&token=b64c1a9c-b721-4ea7-b7ff-b6062b99a6a7)

Just like in normal conversations, your users will find it odd if your bot always replies with the exact same message. That's why we support random messages. A random message means that the different messages will be alternated, so sometimes the first message will show, sometimes the second one.

In the Text Message block, you can add multiple versions of the same message. The bot will randomly pick one of these messages to show to the user, making your dialogue more natural and human-like.

* To add a random message, click on `+ Add random message` and enter the following text:*"What can I do for you?"*

Tip: you can add as many random messages as you like.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MTonj9dhkngmb4YfuD6%2F-MTp8yVHh7mRlG-262u-%2Fimage.png?alt=media\&token=6a8468c1-fe76-41dc-ab71-503ae83adf27)

* Click on `Save` to save your `introduction` bot dialog.

## Step 2: Testing your greeting <a href="#step-2-testing-your-greeting" id="step-2-testing-your-greeting"></a>

Time to check if we configured everything correctly. You can test your bot by using our built-in emulator.

* Click on the Emulator icon in the lower right corner to test your bot:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGtSWzaQln1DHqbTDJ%2F-MkGuuHsF2WqAfMVtLQa%2Fimage.png?alt=media\&token=ff295c92-3daf-48bc-a966-eff6640bb805)

If you have configured everything correctly, Choo Choo will now start the conversation with the introduction you just created. *PS: You can ignore the debug button on the left for now, though this will be useful a little later, when you want to debug more complicated flows.*

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGtSWzaQln1DHqbTDJ%2F-MkGv8qHhUPXH7lELdb_%2Fimage.png?alt=media\&token=d62ebbd8-503a-4e15-8aed-01d26274b919)

Congrats, you just created your first bot dialog! 🥳

## Lesson recap <a href="#lesson-recap" id="lesson-recap"></a>

You now have the done the following:

* Created your own tutorial bot
* Changed the introduction message
  * Added a new message and a random message

You should now know:

* How to change a bot message
* What the emulator is, and how to check your bot message in the emulator

In the [next tutorial](https://docs.chatlayer.ai/tutorials/tutorial-adding-content), you will learn to set up questions which the user may ask the bot, and how to create a bot response.


# Adding content to your bot

In the previous tutorial, we created a new bot and added a greeting. Now it's time to add some more content. We will start with some basic bot responses to frequently asked questions from users.

## The basics of bot building <a href="#the-basics-of-bot-building" id="the-basics-of-bot-building"></a>

In this lesson, we are going to add intents to our Choo Choo bot. We will learn about the NLP engine, how to update the NLP in your bot, and how to link intents and messages.

## The NLP engine <a href="#the-nlp-engine" id="the-nlp-engine"></a>

Before we create some more dialogs, we'd like to tell you about the NLP engine first. You see, the Natural Language Processing (NLP) engine is the underlying algorithm that allows the bot to understand what the user is saying. And as each language has its own words and grammar, we have a separate NLP engine for each language!

> Understanding language isn't easy: it takes us humans about 6 years and hundreds of examples to understand the most common 20,000 words. It's not so different for computers either. To train an NLP engine, we need huge amounts of data. Luckily, we rely on pre-trained models that have a lot of smarts built in already.

## Step 3: Adding an intent <a href="#step-3-adding-an-intent" id="step-3-adding-an-intent"></a>

An intent is a specific question from your user or an action they can do. Users will type their question in the bot, which can be recognised by the NLP engine and linked to an intent. For example: an intent can be a question, a statement, an answer to a question, or a greeting. Each intent can be expressed in many different ways, which is why we call them **expressions**.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MMLfRKntn78RIWIaRVc%2F-MMLhtEtPGu04ZiKva0K%2FUntitled-1.png?alt=media\&token=8002aa84-62dd-49d0-81e7-c24ca47686ac)

In the example above, the user intent is "How do I sign up for a free trial?". This is then recognised by the NLP engine, which triggers the correct response.

Here are some more examples of intents and expressions:

* **Intent: book train ticket** Expressions:
  * I want to book a train ticket
  * I need to go from Antwerp to Brussels
  * Can I order a ticket here?
* **Intent: who are you?** Expressions:
  * What is your name?
  * What can you do?
  * What should I call you?
* **Intent: yes** Expressions:
  * Looks good
  * Yes
  * Ok, confirm
* **Intent: I want to speak to a human** Expressions:
  * Can I speak to a real person?
  * human please
  * I want to talk to a human

For this tutorial, we want to give Choo Choo the ability to answer basic questions about itself. To get started, we will create an intent for the question: `Who are you?`

* On the left side of the screen in the navigation menu, click on `NLP` to navigate to the NLP module. Click the `Intents` submenu.

The NLP menu

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGvLhwGB21_S9e9PXt%2Fimage.png?alt=media\&token=ca534e84-78f8-49d7-b754-df6dedea15e1)

* Click on `Add Intent` and name it `who are you`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGvU5y_2CuizhTLXI5%2Fimage.png?alt=media\&token=f3ce5eb7-f2d3-44f4-a57b-eb199d99203c)

* Click on `Create`
* Now you see that the intent is successfully created, without any expressions added to it (that is what the '0' means below the language)

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MTpDBTkDjv_iNirTsD0%2F-MTpMyT4l1QZp__fbVRH%2Fimage.png?alt=media\&token=2c0f2655-64b8-4011-bada-ac3c314b451e)

## Step 4: Adding expressions <a href="#step-4-adding-expressions" id="step-4-adding-expressions"></a>

Now we have to make sure the NLP recognises this intent. We do this by adding expressions. Expressions are different ways your users will express one intent. In botbuilding, as in real life, there are more ways to say something or ask a question.

{% hint style="info" %}
Expressions are another word for what is sometimes called 'Utterances'
{% endhint %}

The more expressions you add to an Intent, the more accurately it will be recognised. It is crucial for an intent to have a wide variety of expressions to give accurate results. The more expression you can think of, the better the result of the NLP will be and the 'smarter' your bot will appear.

* Select the `who are you` intent in the **Intents** pane on the left hand side
* The **Expressions** pane will open in the right. Click on `Add Expression`
* Enter `Who are you?` in the open text field
* Click on `Create`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGvezDjMYOxHfNKeHa%2Fimage.png?alt=media\&token=f5dbc509-c670-4e7e-959d-7cade2784d0e)

Add some more expressions by clicking `Add Expression`:

* What is your name?
* Can I know your name?
* Tell me more about yourself
* Please, I'd like to know who I am talking to
* How should I call you?
* Who is Choo Choo?
* Tell me what your name is
* Who are ya?
* What do people call you?
* Are you a train?
* Do you have a name?

{% hint style="info" %}
After you have finished your first expression, press Shift + Enter to save that Expression and immediately add a new one
{% endhint %}

This will result in the following screen:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGw2QlGzo2yVENGcU1%2Fimage.png?alt=media\&token=c802326d-460e-4e66-a65a-5c9cebc74bbf)

Again, the more expressions you have, the more accurate your bot will be able to respond. Later on we'll see how we can make sure that our bot gets smarter over time; by looking at actual user input once the bot has been made public.

Let's try adding another intent and expressions:

Add another intent, like `Greeting` and add some expressions:

* Hi
* Hello
* Hey
* Hi there
* Good morning

We have defined two intents now: who are you & greeting.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGw8lRwZ0SGxDiG01p%2Fimage.png?alt=media\&token=7b49d96a-b497-4fbf-9687-adc3f2ad1f54)

However, if we were now to say 'Good morning' to the bot emulator, nothing will happen. That is because the NLP is not trained yet, and the intent is not yet linked to a bot dialog. We will work on that in the next steps.

## Step 5: Training the model <a href="#step-5-training-the-model" id="step-5-training-the-model"></a>

To update the bot, we now need to re-train the NLP. Updating the NLP means that the newly added intents and expressions will be recognised by the bot so we can use them in a conversation.

{% hint style="info" %}
To successfully train the NLP, you need to have at least two intents with a minimum of 5 expressions each.
{% endhint %}

* Click the `Update NLP` button in the top right corner of the screen:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LM6YZRQL3d1aj7P433Y%2F-LM6pLiFLy6DJ3kAACH5%2Fimage.png?alt=media\&token=bf3b849b-497d-4351-abfd-9aa2959cdd32)

Select the language you used to add the expressions. You can view the status of the NLP update for each language by clicking on the Update NLP icon.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGwEH13mHjwe97F7Ak%2Fimage.png?alt=media\&token=16f3d14e-4a09-48b0-ba28-45824c232729)

Click on `Update` to start the training. This can take a couple of minutes to one hour depending on the size of your chatbot. The more complex, the longer it'll take.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGvEPIdg7XsPFNQqST%2F-MkGwSqHxCVYb7No4T1M%2Fimage.png?alt=media\&token=357dd3c1-6dd9-4a70-8b42-b38337b9530e)

That was a great first step to use the 'Greeting' and 'How are you' intent. The next step is to link these intents in the bot dialogs.

## Step 6: Linking the intent and defining a response <a href="#step-6-linking-the-intent-and-defining-a-response" id="step-6-linking-the-intent-and-defining-a-response"></a>

You have now taught the NLP to understand your intents and expressions, congrats! The only thing left to do is teaching Choo Choo how to respond. This means we are going to choose what the response (or flow) should be for each intent. You can do this by adding a new Bot dialog.

* Click on Bot Dialogs menu item in the navigation pane
* Open the General flow
* Click on the grey button on top `+ Bot message`
* Enter `who are you` as the name
* Choose the `introduction` dialog state as the parent (in the Settings tab)
* Link the intent to the bot dialog in the bot dialog NLP tab as follows:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGwZV_yaoD3OeX7q88%2F-MkGx-k-YWMcDYuMfw2y%2Fimage.png?alt=media\&token=cb5c4390-8a4d-47ff-b612-d55091eb9862)

* Go to `Bot Message` tab and add a text message that says:

> I am Choo Choo, your personal assistant for booking train tickets

Your screen should look like this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGwZV_yaoD3OeX7q88%2F-MkGx7LadIEUWwl8Zmy-%2Fimage.png?alt=media\&token=61f43605-73dc-47cf-8d1f-32a43af39afd)

* Click on `Create`
* This will result in the folowing overview in the flow:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MMGJDynLKF2rk_VX1en%2F-MMGLSNh8OIL0boHToUU%2Fimage.png?alt=media\&token=2af6f418-fdd7-4393-8884-afeb1f2622bb)

The image below means that a certain intent is linked to that bot dialog.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MTpQO-OQuFYJUtB4w02%2F-MTpZtA9-iJ0Gz1fQsxW%2Fimage.png?alt=media\&token=d965d756-f802-44a3-8275-222946b316f3)

If you now say 'Who are you' in the emulator, you immediately get the response that is typed in the 'Who are you' bot dialog.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGwZV_yaoD3OeX7q88%2F-MkGxDxHjCKSswPByq6q%2Fimage.png?alt=media\&token=6d1d4026-145c-4a26-898f-7a8833446957)

We have defined the `introduction` bot dialog as the parent dialog state in the `who are you` bot dialog. Parent bot dialogs do not limit or define the possible flow of the dialogue. They are a visual tool to structure the conversational flow and keep an overview, which makes it easier to create complex conversational flows. Bot dialogs can be reached from any point in the conversation by linking a bot dialog to an intent, although you can restrict them too by using Contexts. This mimics the way humans talk, jumping from one subject to another.

## Step 7: Testing your bot <a href="#step-7-testing-your-bot" id="step-7-testing-your-bot"></a>

Time to Choo Choo! Click on `Test your bot` at the bottom right to test your conversational flow. To get a feel of your bot's performance, ask the same question a couple times, including different ways of asking the question that are different to the expression you used to train. If a question is not correctly recognized, you'll have to go back to the `NLP` tab, add the questions as an expression, and retrain the NLP model. You can do this as many times as needed, the model will just keep on improving.

{% hint style="info" %}
The 'Test your bot' feature is also referred to as the 'emulator'.
{% endhint %}

## Lesson recap <a href="#lesson-recap" id="lesson-recap"></a>

Now, you have a bot with the following configuration:

* 2 intents ('Greeting' and 'Who are you') and their expressions
* A bot message 'Who are you', with the intent 'Who are you' and four text messages in it.

You should now be familiar with:

* Adding an intent to a bot dialog
* Creating intents and expressions
* Training the NLP to use these intents and expressions
* Adding multiple text messages in one bot message
* Testing your intent and messages in the emulator

If any of these topics are difficult for you, revisit them in the tutorial or search on the page in the top right search bar to learn more about a topic.

In the next tutorial we'll be gathering user input. Choo Choo will ask the user for input, needed for booking a train ticket.


# Detecting information in expressions

In the previous tutorial, you learned about intents and expressions. In this section, we'll cover another important part of bot building: entities.

You will learn how to detect valuable information, mentioned by a user in an intent, using **contextual entities**. Entities are important pieces of information that are extracted from an expression.

There are four types of entities. You can find more information about them here: [Entities/understanding-users/natural-language-processing-nlp/synonym-entities](https://docs.chatlayer.ai/understanding-users/natural-language-processing-nlp/synonym-entities)

In this tutorial we will focus on one entity type: contextual entities. Contextual entities use machine learning to identify entities in sentences by learning what type of word your entity is, where it's placed in the sentence, and what the specific context is.

You want to store these contextual entities in a separate variable so you can re-use them later on. Read more about the difference between entities and variables [here](https://docs.chatlayer.ai/understanding-users/natural-language-processing-nlp/synonym-entities#the-difference-between-entities-variables-and-values). In the next tutorial, you will learn how you can ask explicitly for missing information.

Let's say we have an intent that tells us the user wants to book a train ticket. A few different expressions could be:

* I want a train ticket
* I need a ticket
* Can I book a train ticket here?

This assures the bot dialog, linked to the corresponding intent, to be triggered when the user says one of these expressions.

But what would happen if the user says:

* I want a train ticket to **Amsterdam**
* I need to go to **Antwerp tomorrow**
* Can I book a train ticket to **Brussels** please?

These expressions contain valuable information. We want to make sure we capture that information, in this case the destination and time, and save it as **entities**. We then have expressions with an entity in them.

We are now going to create a new intent with some expressions for booking a train ticket. Some of these expressions will contain a contextual entity, but some will not.

## Step 9: Creating contextual entities <a href="#step-9-creating-contextual-entities" id="step-9-creating-contextual-entities"></a>

Not all users will immediately mention their destination, so let's make sure we train our intent without those specific entities as well:

* Go to `NLP` > `Intents`
* Click on `Add Intent`
* Add a new intent called `book train ticket`
* Add some simple expressions, like:
  * I want a train ticket
  * I need a ticket
  * Can I book a train ticket, please?

{% hint style="info" %}
If you have trouble doing this, please read the [previous tutorial](https://docs.chatlayer.ai/tutorials/tutorial-adding-content).
{% endhint %}

Next, it's time to add a contextual entity.

* Go to `Intents` and select your `book train ticket` intent
* Click on `+ Add expression` to create a new expression
* Enter an expression that contains an entity, for example:

> I want to book a ticket from Brussels to Paris

* Select `Brussels` in this sentence

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGxjU95gXOWRIT-00A%2F-MkGxxv8SOeFMIFvsE7c%2Fimage.png?alt=media\&token=004b7ae3-6de6-400a-b0d8-39ff6e062252)

* Click on the '+ entity' icon in the bottom right of the expression box to create a new contextual entity for 'Brussels'

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGxjU95gXOWRIT-00A%2F-MkGyCH7wsvcaDFBmzaV%2Fimage.png?alt=media\&token=24d67668-28c8-4bac-8527-8cbde0db440a)

* Brussels is the location the user wants to depart from, so we will name this entity `origin`
* Type `origin` in the `Create new entity` field and click on 'Create new entity' to confirm

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGxjU95gXOWRIT-00A%2F-MkGyJxX0IFrM96GU68X%2Fimage.png?alt=media\&token=77862567-721f-4704-917a-95eefc1eafcc)

* Brussels will be added to the list of possible values for the @origin variable
* Do the same thing for `Paris` as a 'destination' entity

You will then have the following set-up for this expression:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGxjU95gXOWRIT-00A%2F-MkGyV2A2i5z-N9Bjko2%2Fimage.png?alt=media\&token=4ad66920-83d0-4a9b-935e-0a823ab6fa23)

We now save added the expression 'I want to book a ticket from @origin to @destination', where 'Brussels' is a value for @origin and 'Paris' is a value for the entity @destination.

* Add some other values to the 'origin' and 'destination' entities in the expression field. These will be saved for all future expressions. You can add these in the 'Create new value' box and pressing enter.
* Add more expressions that contain the entities **origin** and **destination**

Once you have added more Entity values, these will also show up in the menu `Entities` > `Contextual Entities`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MTtSJzh0IZmA5tu3CIt%2F-MTtUS1oKy_IOQmi5o0r%2Fimage.png?alt=media\&token=8db10598-73a6-4d7f-9c52-359dfe861b2d)

* Now, let's add some more expressions to our `Book train ticket` intent. Some ideas for expressions:

  * Can I book a train from Cologne to Brussels?
  * I need to be in Rotterdam
  * I need a train to London
  * I want to travel to Lyon
  * I want to buy a ticket from Moscow to Vladivostok
  * I need a ticket from New York to Baltimore

  ​

{% hint style="info" %}
When typing a new expression, you can add entities and entity values in two ways:

1. Typing @ and then the name of the entity, for example @origin. You can add a new value in the box below with 'Create new value'
2. Selecting an entity value and clicking the +entity value button. For example, select 'Cologne', click the +button. This will result in 'Cologne' being changed into @origin and 'Cologne' will be a value of @origin
   {% endhint %}

* Make sure you retrain the NLP model by clicking the `Update NLP` button in the right upper corner.

This will now result some expressions for the `Book train ticket` intent, and entity values, like so:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkGzbGNWNnq3K523Ulr%2F-MkGzyb8SE__tYj3dfE0%2Fimage.png?alt=media\&token=39186f8a-7c8f-4d85-9303-cb1a0653322c)

To make it easier for you to add new expressions fast, we have built the expressions generator. Head over to [this page](https://docs.chatlayer.ai/understanding-users/expression-generator) for more information.

## Step 10: Testing contextual entities <a href="#step-10-testing-contextual-entities" id="step-10-testing-contextual-entities"></a>

After we have retrained our model, let's see if its good enough to recognise the destination entity.

* Go to `NLP` >`Test` to open the testing console
* Write 'I would like to go to Brussels from Amsterdam' as the expression to be tested
* Click on `Test`

You'll see that the entity gets recognized with a 99.93% confidence. The results will be different based on your training set. If the entity is not recognized correctly, you can add it here as a training expression immediately by clicking `+Add expression`.

{% hint style="warning" %}
Make sure you retrain the NLP model before testing newly added expressions
{% endhint %}

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH0Xc2j9da2v7Beyly%2F-MkH15--aKH17tP9HGHH%2Fimage.png?alt=media\&token=ad4d3c89-61ee-49c2-bdbf-cd49bc93d818)

Now we know how to add intents, create expressions and entities, however we still need to create a conversation so the user can talk to Choo Choo and our bot replies accordingly. Let's add some bot messages in the next step.

## Step 11: Using variables in messages <a href="#step-11-using-variables-in-messages" id="step-11-using-variables-in-messages"></a>

When a user says something containing an entity, and the entity is successfully detected, our tool will automatically store the entity as a **variable** for that specific user.

At the moment, when you test your bot, the user is stuck after giving the information about the ticket:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH0Xc2j9da2v7Beyly%2F-MkH1CUu58sorl5kmWxV%2Fimage.png?alt=media\&token=d1af8e0a-8938-43be-8ba4-d12ec80c81cd)

However, we do see some positive items, namely that the 'origin' and 'destination' are stored correctly as variables. You can see this by opening the debugger by clicking 'Debugger' (with the magnifying glass icon) in the emulator. In the 'Debugger' tab, you can scroll down and you see this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU2TVa1AuMzEh_EOnYY%2F-MU2VeSiba5oLsepO84p%2Fimage.png?alt=media\&token=44d3181f-b11c-4dd4-bc4d-55fc1fa86aeb)

So even though the sentence did give an error message, these entities are correctly recognized in the user input. This means the variable 'origin' is now saved with a variable value 'Brussels' and the variable 'destination' with the value 'Paris'. Also, in the ''NLP Result' tab we see that the intent was recognised correctly, that's great! Let's now work on removing that error message first.

The error message is caused by the fact that the intent `Book train ticket` does not have a bot dialog linked to it. So even though it is correctly recognised, we are not telling the bot what to do when that intent is recognised.

We can change that by adding a new Bot message:

* In the menu Bot dialogs, open the 'General' flow, create a bot dialog of the type 'Bot message' `book train ticket`. Open the 'NLP' tab, and choose the `Book train ticket` intent in the 'Intent' dropdown.
* In the 'Settings' tab, name the bot message `Book train ticket`
* Add a new text message with the text "So you want to go to `{destination}`, I can help you with that!"
* Click `Create` to save this bot message.

{% hint style="info" %}
To reuse the variable later on in the conversation, you can put it in between curly brackets like this: `{variable_name}`

When writing this message to the users, Chatlayer will automatically substitute `{variable_name}` with the value of the variable. If the variable is empty, an empty space will be shown.
{% endhint %}

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH0Xc2j9da2v7Beyly%2F-MkH1PrdzbeTf9tu68sF%2Fimage.png?alt=media\&token=7c8f42e4-4d7b-4558-b519-2fd051b6e447)

We have now linked the `Book train ticket` to this bot message, great job! This means that, when a user says something that triggers the `Book train ticket` intent, this bot message will show.

## Step 12: Testing entities in the emulator <a href="#step-12-testing-entities-in-the-emulator" id="step-12-testing-entities-in-the-emulator"></a>

Now that we have linked everything, we are ready to test if everything is configured correctly by using the emulator.

* Open the emulator (the `Test your bot` tool on the bottom right)
* If needed, clear the last conversation by clicking 'Clear conversation' on the top right. This starts a new conversation
* Enter "I want to go to Amsterdam" and click on submit
* Open the debugger

In the tab 'NLP Result' you can now see if the entity was recognized correctly:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH3SXFOwX2uPCsNuP2%2F-MkH4NrTG2-cY0ooVsXM%2Fimage.png?alt=media\&token=c8010d53-7fad-4041-979f-7d2925f1f0d6)

{% hint style="info" %}
When creating new bot dialogs, you don't need to re-train the NLP
{% endhint %}

If you do not get the result as stated above, please check the following items in your bot:

* If your entity is recognised by the NLP but doesn't show up in with `{destination}` it did not pass the threshold of 80%. Try adding that value to your entity and re-train your model, or choose another destination
* If you get 'Sorry I didn't understand that', double check if your intent is linked to the Bot message and this is saved correctly.
* If your intent or expression is not recognised, try re-training your NLP again.

Now we already have a great start with linking the intent and giving a response to the expression the user says. However, we want more information from the user. Let's add more expressions and entities.

## Step 13: Multiple entities in one expression <a href="#step-13-multiple-entities-in-one-expression" id="step-13-multiple-entities-in-one-expression"></a>

You can add as many entities as you want to one expression. For Choo Choo, we want to more information from the user than just the destination and origin, to give a complete train-booking experience. Let's add more contextual entities!

* Go to the `Expressions` menu
* Click 'Add Expression'
* Select the `Book train ticket` intent

Create the following expression:

* I want to go from **Antwerp** to **Brussels** **tomorrow** at **9am** in **first** **class**

And create the following entities:

* origin: Antwerp
* destination: Brussels
* departure-date: tomorrow
* departure-time: 9am
* class: first class

*If you are having trouble adding these, scroll back to step 9 in this tutorial to read all about it.*

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH3SXFOwX2uPCsNuP2%2F-MkH525pu7JX-S69BFna%2Fimage.png?alt=media\&token=bf9e6fe8-55f3-472b-a331-de6789211512)

#### Additional suggestions for expressions <a href="#additional-suggestions-for-expressions" id="additional-suggestions-for-expressions"></a>

* I need to be in Paris next Thursday
* I need to be in New York on Friday
* I want to go to Brussels on Monday
* Friday I want to go from Antwerp to Amsterdam
* I want to travel in second class from Ghent to Brussel on Friday
* I want to travel in first class from Antwerp to Aalst on Thursday
* I like to book a first class ticket from Aalst to Brussels at nine o'clock
* Tomorrow I want to go from Antwerp to Brussels on the train from 9:00 in first class

{% hint style="info" %}
Keep in mind that NLP techniques are probabilistic in nature. When you try to capture five expressions in one sentence, it might not be able to recognise all of them correctly. As a general rule of thumb, you can start to expect reasonable results for one entity when the NLP was given at least 30 expression to learn from.
{% endhint %}

Add more expressions with the new contextual entities to the intent. Ensure you have around 20 expressions for `Book train ticket` in total.

## Step 14: Missing entities <a href="#step-14-missing-entities" id="step-14-missing-entities"></a>

Let's test out your newly created expressions:

Update the wording in the `book train ticket` dialog to correctly display the entities:

*I need a ticket from Antwerp to Brussels tomorrow at 9am in first class*

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH7g-t2PdP1Gsu3XVv%2F-MkH8YKAwriN4PC7GJ0n%2Fimage.png?alt=media\&token=c5e2d9cc-b3f7-450b-9324-4ecd2380ec50)

{% hint style="warning" %}
If you try to update your NLP and you get an error message about 5 example entities, it means you need to add more entity values to some of your newly created entities. To do so, go to NLP > Entities > Contextual entities and make sure that that entity has at least 5 values.
{% endhint %}

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH7g-t2PdP1Gsu3XVv%2F-MkH9WVdq97GEU-ttmps%2Fimage.png?alt=media\&token=dac2c47a-3e4b-4dd9-81d0-ca0d8f301738)

Uh oh, this isn't really what we expected. As you can see, not all variables were recognized correctly. So, what's the issue? Lets have a look at the NLP results in the debugger:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MkH7g-t2PdP1Gsu3XVv%2F-MkH9TzgUC7RuJYHHDo7%2Fimage.png?alt=media\&token=677387f2-a43a-4d3c-ada8-d28cb0906025)

`origin`, `destination`, `time_departure` and `class` were found correctly, but only `time_departure` and `class` have a confidence score higher than 80%. `Origin` and `destination` score much lower, so they weren't processed as variables.

{% hint style="info" %}
In the [NLP treshold settings](https://docs.chatlayer.ai/understanding-users/natural-language-processing-nlp/settings) of our bot, we put a threshold of 80%, so anything underneath that won't be recognized correctly.
{% endhint %}

How can you fix this issue? By adding more expressions! Try adding more expressions and retrain your NLP model to see if the variables now show up correctly in the bot. You can also choose to lower the NLP score, but be careful as this can impact the overal accuracy of your bot in the long run.

## Lesson recap <a href="#lesson-recap" id="lesson-recap"></a>

Your bot now has the following configuration:

* 3 intents with around 35 expressions in total
* 5 contextual entities
* A bot message, linked to the `Book train ticket` intent, confirming the user input in the message

You now know how to:

* Create contextual entities and entity values
* Use variables in a bot message
* Use multiple contextual entities in an expression
* Test your input in the debugger

Not every user will give all the entities you need. In the [next tutorial](https://docs.chatlayer.ai/tutorials/tutorial-request-and-use-information-using-input-plugins), you will learn how to check if a user has already provided certain information, and ask for what's missing.


# Asking user info through input validation

You have now built the basic version of the Choo Choo bot, great! Next up is working with input validation. Often, the bot can grab information from expressions, using input validation.

To complete our Choo Choo bot, we need to ask the following information from the user:

1. Origin
2. Destination
3. Departure date
4. Departure time
5. Class

This works great when the users says, for example:

* **Tomorrow**, I need to go from **Amsterdam** to **Brussels** at **2pm** in **second** class

But right now, our bot can only detect this information when the user gives all this information in a single sentence. Of course, in a lot of cases, this will not always be the case, so we 'll need to ask this information from the user. The dialog to ask for this info is called the **Input Validation dialog**.

## Step 15: working with input validation <a href="#step-15-working-with-input-validation" id="step-15-working-with-input-validation"></a>

Until now, we have only worked with the bot dialog type `Bot Message`. One of the other [four bot dialogs](https://docs.chatlayer.ai/bot-answers/dialog-state) types is `Input validation`. With an input validation, you can ask specific information from a user and save the answer directly in a variable. Let's start with origin and destination.

#### Text input  <a href="#text-input" id="text-input"></a>

We are going to create new input validations. This can be done in the main flow overview with the green `+Input validation` button, but can also be created directly in another bot dialog.

* Open the `book train ticket` bot dialog
* Change your bot message text here to: 'So I have a request for a train ticket'.
* In the Bot Message tab, scroll down to `Go to`
* Type `destination` in the Go to field, and click `Create Input Validation 'destination'`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU4leF2pmBkjy6PCJVw%2F-MU4srj_NrF2syL8B7F_%2Fimage.png?alt=media\&token=8e5df79b-0576-4192-852f-ce29143f1121)

{% hint style="info" %}
In every bot dialog, there is a `Go to` option. This means that the conversation flow will automatically go to that next bot dialog if the current one is finished, or if that specific input is given. With the current set-up, the bot will automatically go to the input validation if the first bot message for the `Book train ticket` intent is finished.
{% endhint %}

* Save the `book train ticket` bot dialog

You can see that the newly created dialog turns red. This means it's not finished yet. Let's finish it so it turns green:

* Open the newly created `destination` input validation
* In the `Input Validation` tab, under 'Question', add a new text message "Where do you want to go?"
* In the 'Save user input as 'pane, select `Any` as the format type under 'Check if response matches'

{% hint style="info" %}
Input validation can automatically detect certain types of data, like dates, addresses, numbers, hours, currencies, ... This will convert the users response into a more structured format.

In this example, we just want to know the city of destination, which can take on any format. So, we'll use input type 'Any' which will accept any value as valid input.

You can find more info about plugin parser types [here](https://docs.chatlayer.ai/bot-answers/dialog-state/user-input-bot-dialog#input-types).
{% endhint %}

* Type `destination` as the variable. The input from each user will be saved under this variable name.
* Type `Confirm booking` in the 'Go to' field. Because the `Confirm booking` bot dialog doesn't exist, you get the option to create a new one. Pick `Create Bot Message 'Confirm booking'`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU8OCrKsJiXKw6ZyzoN%2F-MU9PxMzC40ywMyeD4w2%2Fimage.png?alt=media\&token=b695b616-96da-4336-b98e-e942715121dc)

The end result should look like this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU8OCrKsJiXKw6ZyzoN%2F-MU9QJfEHny2q0nOk8sW%2Fimage.png?alt=media\&token=1281cc2e-4b70-45db-aa0c-06debd0a8cf7)

#### NLP & input plugin <a href="#nlp-and-input-plugin" id="nlp-and-input-plugin"></a>

You want to make sure your users don't get stuck in a loop where the bot keeps asking them for input. That's why we make sure that if an intent is detected in the answer to the input plugin, users automatically leave the input plugin and go to the relevant part of the conversation.

Our Choo Choo bot doesn't have a mature NLP model yet, which increases the likelihood of false intent matches. So for now, it's best to select the 'Disable NLP' checkbox in the input plugin.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU8OCrKsJiXKw6ZyzoN%2F-MU9RU4aotcmUFmvmEzD%2Fimage.png?alt=media\&token=9e826e3d-52d0-45b2-8db1-4625e8bd4843)

Once created you will see the following flow:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU8OCrKsJiXKw6ZyzoN%2F-MU9QXlqXRcX8GeSljhF%2Fimage.png?alt=media\&token=c029f2cb-07e9-48e9-8cc6-3f7b6a97df8d)

{% hint style="warning" %}
The parent-child relation between dialog state nodes is only a visual representation, it has no functional meaning. Always link your bot dialogs using Go to's.
{% endhint %}

#### Using user input in text messages <a href="#using-user-input-in-text-messages" id="using-user-input-in-text-messages"></a>

As can be seen in the image above, the bot message is red. This means it is not completed yet. Let's complete it so it will turn grey (the colour of all Bot messages). All the session variables are stored in the user session. To access a variable in any displayed text, you can put the variable name between curly brackets.

* Open the `Confirm booking` bot dialog
* Enter a new text message `Okay you want to go to {destination}. We can do that.`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU8OCrKsJiXKw6ZyzoN%2F-MU9R7gO9zO9mEKiJJ_q%2Fimage.png?alt=media\&token=7448e6a2-1e7b-4720-b837-df740fcd01d7)

Time for a test!

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MU9RkNyhP4QN1UQ6dwH%2F-MU9UbuO_rOONaD01OtC%2Fimage.png?alt=media\&token=533ba19f-6984-4b36-9afd-11daac9c3d4c)

{% hint style="info" %}
If you forget to define the 'Go to' and you test your conversation flow, the flow will just stop. The conversation will only continue if you correctly set the 'Go to' for each dialog state.
{% endhint %}

That looks great! If you are getting a message with empty spaces in the first bot message ('So I have a request for a train ticket'), make sure you have changed that bot message accordingly for our newest set-up. If the destination is not captured correctly, make sure that you save the variable as 'destination' in the Input validation and you use '{destination}' in the bot message.

## Step 16: Completing the booking flow with the remaining input validations <a href="#step-16-completing-the-booking-flow-with-the-remaining-input-validations" id="step-16-completing-the-booking-flow-with-the-remaining-input-validations"></a>

Repeat the previous steps for the the other pieces of information you'd like to get from your users:

* Origin: Where are you leaving from?
* Departure time: At what time do you want to leave?
* Departure date: Which day would you like to take the train?

This means you need to create three extra Input Validations, just like the `destination`Input Validation. You can change the current `destination`Input Validation to make sure the `origin` is asked next:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWO1Zdl3Cz7ul2TcJKE%2F-MWO33qVHR2oxFRZoKe1%2Fimage.png?alt=media\&token=d7db512e-ae66-4b71-9633-15908a9ce843)

Create the Input Validation. Save the variable under 'origin' and choose 'Check if response matches > any'. Once this is created you will see this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWO1Zdl3Cz7ul2TcJKE%2F-MWO3SNlz9WclAYqUiEx%2Fimage.png?alt=media\&token=bffe583d-696a-4e58-aa38-a8906bc653fe)

This is because the `Confirm booking`Bot Message still has `destination` as parent. No worries, this will be fixed later. Add 'Where are you leaving from?' as text in the Input validation and save the input under 'origin' variable. Make sure that the next Input Validation after this one will be `departure time.`

* Now, create the other Input Validations:
  * 'departure-time' variable, with text: 'At what time do you want to leave?'. Save under 'Check if response matches > any'. Go to: departure date. Disable the NLP.
  * 'departure-date' variable, with text: 'Which day do you want to take the train?'. Save under 'Check if response matches > any'. Go to: confirm booking. Disable the NLP.

Make sure all of these input validations follow a consecutive flow, and end up in the `Confirm booking` bot dialog:

1. `Book train ticket`
2. `Destination`
3. `Origin`
4. `Departure time`
5. `Departure date`
6. `Confirm booking`

{% hint style="info" %}
You will see, once you open `departure date` Input validation, that the go to is `confirm booking` but this does not show in the flow overview. That is because the parent of `confirm booking` is still destination. You can change this by opening `confirm booking` > Setting tab > change parent to `departure date`.
{% endhint %}

This means the end result will look like the following:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWO6M8HjaakuDW7YtVO%2F-MWO7ksNgYfl1JK1enjS%2Fimage.png?alt=media\&token=2ede2494-82eb-4a78-9444-1d0cf30fad98)

If any of your bot dialogs are red - check if the bot dialog is complete with a text and saved under the correct variable. If you do not have a consecutive flow, please check if all parents are set correctly and the go-tos in the dialogs are saved correctly.

We now have a great train booking flow! Try it out a couple of times.

In the emulator with the debugger tab you can see if the variables are saved correctly. In this tab you can see all the variables stored in that specific session. If you scroll down you can see something like this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWOYSBxsXVVKc1L5Irj%2F-MWOYxfyqkQOrZpuiUTs%2Fimage.png?alt=media\&token=fb4fccb1-9c6e-4d26-95c9-b8cf05e743aa)

This is a great start when you need to debug. Here you can see if you made a typo in a certain variable or if the user input is correctly stored in the variable.

## Step 17: Combining user input with buttons <a href="#step-17-combining-user-input-with-buttons" id="step-17-combining-user-input-with-buttons"></a>

In the tutorial above, we requested user input by sending a text message. However, in an `input validation`, we can also ask for the user's input by click, but it is also possible to use buttons, lists, carousels and other UI components to support user input as text or clicks.

This is especially useful and user friendly to have when there are only a few options to choose from, as described [here](https://docs.chatlayer.ai/tips-and-best-practices/chatbot-checklist) in the Conversation Design Chatbot Checklist.

Let's use buttons to request the user their preferred train class.

* In the `Departure date` input validation, type `Class` in the Go to field and create a new input validation
* Under Question, add Buttons
* Enter the text message: "Which class do you want to travel in?"
* Add two buttons, choose the Go to option, "First class" and "Second class," both going to the `Confirm booking` bot dialog
* In both buttons add a variable `class` and value `first` and `second`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWO8Gz9pphhnIm1m8oP%2F-MWOU3azKsdwgVasGI4e%2Fimage.png?alt=media\&token=0a95a8e9-ee60-428f-9bcd-1205add5a7d7)

* Select format type `Any`, enter `class` as variable, and go to `Confirm booking`

{% hint style="info" %}
It's important to use an identical variable name for the input variable, the NLP entity and the button variable.
{% endhint %}

Depending on the user input, different actions will be executed:

1. If a user writes an expression that contains an entity that matches with the variable in an input validation, this input validation is skipped. This way we can avoid asking things from the user which they've already said.
   * For example: when the user says `I need a first class train ticket` which belongs to intent `book train ticket` and includes an entity `class`, the 'class' variable is stored in the user session with a value 'first' and the input validation 'class' is skipped because the value for the input variable is already available in the user session.
2. When the user is asked to give his preferred train class and he says 'first', this value will be added in the input variable 'class' in the user session.
3. When the user clicks the button 'First class', the value 'first' will be added to the variable 'class' in the user session.

This gives a lot of freedom to the user; no matter where they give their input (in an input validation, expression, or button) this is all saved in the correct variable.

Try it out in the emulator!

## Step 18: Finishing up <a href="#step-18-finishing-up" id="step-18-finishing-up"></a>

Now that you have all this extra information, it's time to show all the data you've gathered in the input validations to the user:

* Open the `Confirm booking` bot dialog
* Replace the existing text message with "I have a train ticket for you from {origin} to {destination} on {departure-date} at {departure-time}h, in {class} class."
* Change the parent to `class`

Now test your newly created bot to see if it works!

If you run into any issues,

## Lesson recap <a href="#lesson-recap" id="lesson-recap"></a>

Now, you have a bot with:

* A flow to book a train ticket with 2 bot messages and 5 input validations
* The ability to recognize both variables given in expressions or via input validations
* A final bot message summarizing all variables given by the user

You should now be familiar with:

* Creating an input validation and storing the user input in a variable
* Creating a button and storing the input from the button click in a variable
* Linking bot dialogs to each other with the go to option in a bot dialog, and creating a new bot dialog from the go to option
* Changing the parent of a bot dialog
* Using the debugger tab to see how user input is stored

In the [next tutorial](https://docs.chatlayer.ai/tutorials/tutorial-conditional-flow-navigation), you will learn how you can steer the conversation in a certain direction based on known variables.


# Flow navigation with variables

In this final tutorial we will look at how to use user information and base different conversational flows on that.

## Step 19: Go to bot dialog <a href="#step-19-go-to-bot-dialog" id="step-19-go-to-bot-dialog"></a>

The `Go To` bot dialog enables the bot to redirect the user to a bot dialog, depending on conditions of the session variables. You can define conditions with operators like `equals`, `greater than`, `smaller than`, etc. You can also combine multiple conditions with `AND` and `OR`.

Consider the following scenario where the user asks the bot the following:

> I want to book a train from Paris to London in first class please.

We already have a lot of information in this expression. Let's say we now want to show a different message for first class tickets, seeing there are more facilities in first than in second class.

* Create a `Go To` bot dialog with the name `class redirect`
* Add a condition with the '+' sign next to 'If'
* Choose a Go To condition saying 'if class equals first' > go to `selected first class` bot message

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWilwM5mQ2H9tRMW7II%2F-MWioj71pr2qc11MtkJu%2Fimage.png?alt=media\&token=7e3e9c46-c49f-433c-aae3-6dea4d76ac14)

* Open another condition with the '+' sign, next to 'Else if' and do the same for second class.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWilwM5mQ2H9tRMW7II%2F-MWip29QLnjOmbTzBCJA%2Fimage.png?alt=media\&token=e9eee233-66d6-492b-a5a6-c36255ea5979)

* If the user has selected no class at all, we want to redirect the user to the bot dialog `class,` which we already created. Here, the traveler will be asked explicitly in which class they want to travel.
* Make sure the parent of this Go To is the `departure date`Input Validation.
* Configure the Go To like this:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWilwM5mQ2H9tRMW7II%2F-MWivdYdBIGoSCNu7NeM%2Fimage.png?alt=media\&token=b3cd38ec-8931-4e58-8a39-754418258d19)

## Step 20: First class options <a href="#step-20-first-class-options" id="step-20-first-class-options"></a>

* Open `selected first class` bot dialog. We are going to create buttons and save that information in a variable. Click on 'buttons' and create similar buttons as in the `class` Input Validation, to ask the user if they want a window seat. Make sure to save this to a variable. Add a Go To that redirects the user to `confirm booking.`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWilwM5mQ2H9tRMW7II%2F-MWitMFqou0syZEVlT4e%2Fimage.png?alt=media\&token=090ea0c9-ab58-401e-bb83-87a9d96458ee)

## Step 21: Final touches <a href="#step-21-final-touches" id="step-21-final-touches"></a>

* Open `selected second class` bot dialog. Add a text message saying 'Second class confirmed' and go to `confirm booking`
* In the `departure date` Input Validation, change the Go To to `class redirect`
* Open the `class` Input Validation. Change buttons so that both choices are redirected to the Go To `class redirect`. Change the parent to `class redirect`

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWilwM5mQ2H9tRMW7II%2F-MWiwDMYqj8COMy4ChoL%2Fimage.png?alt=media\&token=75cc48f7-ca7b-4350-abfa-479ce593f279)

What we have now done, is that in `class redirect` we check if the class has already been given in the expression by the user. If that is the case, we confirm second class or give extra options for first class. If class has not been given yet, the user can choose this in the `class` Input Validation. If the user chooses their class in the Input Validation, then they are redirected to the class options.

Let's test this new functionality in the emulator:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MWixY5tBqI3mO5AlzMA%2F-MWiyL__jl2G4FBAaMmq%2Fimage.png?alt=media\&token=14e8ed11-d088-4e59-bc92-4b78b2aefbc3)

​

That looks great! If something is not working correctly, double check the Go Tos in the bot dialogs. Sometimes the parent is changed, but the Go Tos not and that can cause issues.

## Lesson recap <a href="#lesson-recap" id="lesson-recap"></a>

That was it! You have completed Choo Choo, great job!

You should now be comfortable with the basics of bot building on the Chatlayer platform:

* Creating Bot Messages
* Asking for user input in Input Validations
* Creating intents and expressions
* Using contextual entities
* Using a Go To to steer the conversation

Make sure to check out the rest of the documentation as well.

Good luck with building your own bot! If you have any questions, please do not hesitate to contact us at <support@chatlayer.ai>.


# Bot dialogs

## Flows <a href="#flows" id="flows"></a>

You can think of flows as a folder in which you can put bot dialogs that are related to the same topic.

{% hint style="info" %}
Keep in mind that flows, just like the connections between dialog states, are simply a way of organizing your bot. They do not restrict the movement of users across your bot.

* Users can jump from one flow to another by using intents
* Bot builders can set-up a next bot dialog to another flow
  {% endhint %}

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LRkkwO6qeoGYk9PS2b2%2F-LRklhazZ52KdyiUXcb5%2Fimage.png?alt=media\&token=085bd477-99bb-4a23-a37f-b118768ca6b3)

Some tips on choosing how to group flows:

* Group all flows that have a functional relation. In our Choo Choo example, you could group all bot dialogs that are meant to help book a ticket, all general questions about trains, and all support flows (e.g. "I lost my bag on the train")
* Reserve one flow for general questions, such as your offloading settings and the dialog for when your bot doesn't understand

## Bot dialog flow builder <a href="#bot-dialog-flow-builder" id="bot-dialog-flow-builder"></a>

### Bot dialog types <a href="#bot-dialog-types" id="bot-dialog-types"></a>

There are 4 kinds of bot dialogs, each with its own colour and functionalities:

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LR7fnSIfSEa3UlK1beX%2F-LR7ww3XTl-35ge-lFNe%2Fimage.png?alt=media\&token=56ebe60d-1561-4222-9a3e-d06914cf969a)

* **​**[**Bot message**](https://docs.chatlayer.ai/bot-answers/dialog-state/message-components)​
  * Any message a bot is sending to a user is what we call a bot message. This includes text messages, buttons, quick replies, etc.
* **​**[**Go to**](https://docs.chatlayer.ai/bot-answers/dialog-state/plugins)​
  * If you want to add rules to determine where a user is guided to, based on the value of a variable, you can do it with this bot dialog type.
* **​**[**Action**](https://docs.chatlayer.ai/bot-answers/dialog-state/action-bot-dialog)**​**
  * Actions allow you to configure the settings of a user session, such as the language that will be used to reply to your user, or the offloading of a user.
* **​**[**Input validation**](https://docs.chatlayer.ai/bot-answers/dialog-state/user-input-bot-dialog)​
  * Use this bot dialog type to gather input from your users.

Every bot dialog type has its own settings and NLP tab, which stays the same throughout the different types.

### Bot dialogs menu <a href="#bot-dialogs-menu" id="bot-dialogs-menu"></a>

Our platform offers two different views of your dialog states, where you can configure what the bot will answer to a user.

* **The flow view**: a visual representation of all your dialog states, where you can easily see which bot dialogs are related to each other.
* **The table view**: the same information about your dialog states as in the flow view, but shown in a table, making it easier to filter, search and sort the dialog states.

### Flow view <a href="#flow-view" id="flow-view"></a>

The flow view shows your flows like a tree. This view is helpful to see how your flows are constructed. The parent child relations between bot dialogs visually organises the bot dialog states. Changing the parent child relation will not change the way your conversation flows work: it is purely for organising the bot dialogs in a logical matter. The user is only redirected by intent recognition or clicks on UI components such as buttons and quick replies.

### Table view <a href="#table-view" id="table-view"></a>

View your bot dialog states as a table, which is helpful for searching, filtering and sorting dialog states.

## Bot Dialog Settings <a href="#bot-dialog-settings" id="bot-dialog-settings"></a>

### Bot Dialog ID <a href="#bot-dialog-id" id="bot-dialog-id"></a>

This is the ID associated with the dialog state. You can use this to debug your bot using the Emulator.

### Bot dialog Name <a href="#bot-dialog-name" id="bot-dialog-name"></a>

The name for a specific dialog state. This is also the label that is shown in the tree view, the list view or the translations module. You can enter any name you want and change it as often as you like.

### &#x20;Bot Dialog Label <a href="#bot-dialog-label" id="bot-dialog-label"></a>

You may use this field as a custom identifier for your bot dialog when integrating solutions through the Webhook Channel API .

For example: say you want to store the number of times some specific bot dialog ( eg. `Greeting Message` ) has been triggered. You have added a custom label to that bot dialog ( eg. `messages_greeting`).

Now if you delete the `Greeting Message` and recreate it, its unique identifier on our side will change, but you could still add `messages_greeting` as the custom label again.

If you use this custom label in your system to check if the bot dialog has been triggered then nothing on your side needs to be changed, just make sure the label of the recreated bot dialog is the same as the label of the bot dialog you deleted.

### Flow <a href="#flow" id="flow"></a>

The bot dialog flow determines in which flow the bot dialog you are editing (or creating) will be stored.

### Parent bot dialog <a href="#parent-bot-dialog" id="parent-bot-dialog"></a>

The Parent Dialog State can be used to visually organise your dialog states. Changing the Parent Dialog State will not restrict the conversation flows: it is purely for organising the dialog states in a visual way on the canvas.

You can only choose a parent that is present in the flow you have selected.

## Bot dialog NLP settings <a href="#bot-dialog-nlp-settings" id="bot-dialog-nlp-settings"></a>

### Intent <a href="#intent" id="intent"></a>

Every bot dialog can be linked to an Intent. When a user is entering free-form text, it is analysed by the NLP model. If the model recognises an intent with a high enough accuracy (above the threshold), the user will get the bot dialog coupled to that intent. Multiple bot dialogs can reuse the same intent by using different `Context` settings. A dialog state can only be linked to one Intent.

### Required context <a href="#required-context" id="required-context"></a>

Input contexts give more information about when exactly an intent can be used. If you specify an input context and the linked intent is recognised, the bot will check if the input context is active and act accordingly: combine multiple required contexts for sub flows in flows.

To set a required context for a certain bot dialog, type the name of your context in the `Search or create required context` field. If it doesn't exist, a new context will be created. An existing context will be reused. You can also click on the available contexts in order to select one.

* If the required context is not active, this dialog state will not be shown, even though the intent linked to it was recognised.
* If the required context is active, the dialog state will be shown.

To learn more about using context, see our [Context concepts documentation](https://docs.chatlayer.ai/understanding-users/using-context).

## Default bot dialogs <a href="#default-bot-dialogs" id="default-bot-dialogs"></a>

Every bot, when created, has a set of standard bot dialogs.

### Bot Disabled <a href="#bot-disabled" id="bot-disabled"></a>

The Bot Disabled bot dialog will only be triggered if you explicitly disable your bot. You can do this in the 'Settings > Bot' page. Let's say you want to disable the bot for 1 day, then you can show a message like 'At this moment I can not help you further, please contact our support service through \<email> or call us on \<phone> if you have any questions' in that bot dialog.

### Error occurred <a href="#error-occurred" id="error-occurred"></a>

The error occurred bot dialog will be triggered if an API integration fails to complete a certain request. For example, let's say you perform an API call to an external system from an API Action bot dialog to retrieve details about a product. If the external API throws an error, the conversation will automatically be redirected to the Error Occurred bot dialog.

### Not understood <a href="#not-understood" id="not-understood"></a>

Whenever an intent is not recognized above your [threshold](https://docs.chatlayer.ai/understanding-users/natural-language-processing-nlp/settings), the bot will refer to 'not understood'. Please find more information on how to configure different 'not understood' options [here](https://docs.chatlayer.ai/tips-and-best-practices/not-understood-bot-dialog).

​

The other system bot dialogs are specifically related to our Offloading feature (redirecting your users from the bot to a human). You can find more information about them in our [documentation](https://docs.chatlayer.ai/integrations/human-offloading-live-chat#human-handover-bot-dialogs.).


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


# Go To

Go To enables your bot to redirect the user to a bot dialog state depending on the conditions of the session variables.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2F9yg17OeUeyJbJLPx4Mj2%2Fimage.png?alt=media\&token=108badec-7312-43c3-9ae8-63107334f910)

{% hint style="warning" %}
The order of the conditional items determines their priority. If a conditional item is met, other conditional items will not be taken into account.
{% endhint %}


# Input Validation

An `input validation` dialog state can be used to get information from the user. When the user gives information, the bot will first check if the info corresponds to an already known variable. Variables can be known already for various reasons:

* The user has answered this question before
* A previous entity was detected with the same variable name
* The user is authenticated and the variable was automatically set

If the `variable` has a `value` already, the bot will automatically go to the next bot dialog specified in the `Next bot dialog` dropdown list.

If the `variable` does not have a `value` yet, the bot will ask the question written in the input validation dialog.

## Invalid input

When a user gives an answer that's invalid (for example, when the bot asks for an email address and the user replies with 'chicken') the bot needs to let the user know their answer was invalid. To do so, you can create a message to be displayed for when input validation fails once, and another message for when the input fails 3 times.&#x20;

For example: the first time an input fails, the error message could simply be "Sorry, I didn't get that. Can you try again?" or "Sorry, that doesn't seem to be a valid date. Can you try the DD-MM-YYYY format?". When the user fails to give valid input 3 times in a row, the error message could be "Sorry, I can't seem to understand. Please contact our support team at \[tel number]". Another option is for your bot to redirect the user to a live agent.

## Settings

### Disable NLP

Users are able to leave the input validation if an intent is recognized. For bots with a very small NLP model, this might trigger a false positive. The 'disable NLP' checkbox allows you to disable the NLP model while in the input validation, which makes sure that whatever the user says gets saved as input.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FMFmd3L5uZ6YGwe4pJBag%2Fimage.png?alt=media\&token=a7e6b906-39ef-49bd-ac1a-35d164b89bce)

### Always past - always future

Our platform parses user's expressions to match a default date format. If the date you ask should always be in the present or future, you can use these options. A user saying “Thursday” for example will be either mapped to last or next Thursday.

### Input types

Input plugins automatically validate and extract different input types based on the type setting. The type parser is responsible for extracting the data from the user's input. For example: if the input-plugin has a type of **date** and the user's input-sentence was 'I need to be in Paris *in two days*' the input plugin parser will extract the date definition from this input which results in 'in two days'. The parser will convert this into a date representation, DD-MM-YYYY, and the result will be stored in the user session.

#### Any

The 'Any' input type will accept all string values as an input. It is important to know that intents and entities are processed before parsers. This can be useful for automatically extracting certain pieces of a sentence as an answer to a question. We've got a great example of this in our tutorial [here](https://docs-latam.messaging.sinch.com/ia-conversational/untitled-8/broken-reference).

#### Date

The Date input parser type will try to parse the response as a date. Sentences like 'next week Monday' are automatically converted to a DD-MM-YYYY date object. Supported formats (also in other supported NLP languages) are:

* 22-04-2018
* 22-04
* 22 apr
* 22 april 18
* twenty two April 2018
* yesterday
* today
* now
* last night
* tomorrow, tmr
* in two weeks
* in 3 days
* next Monday
* next week Friday
* last/past Monday
* last/past week
* within/in 5/five days
* Friday/Fri

#### Location

The location parser will send the user's input to a Google Geocoding API service. When a correct address or location is recognized, the Chatlayer platform will automatically create an object that contains all relevant geo-data.&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FLBgmTCYDt63nQiAHRC6G%2Fimage.png?alt=media\&token=d2d6d7f6-9e9d-4565-aa8d-0060d7859b23)

Look at the bot dialog above. When the user answers the question "Where do you work?" with a valid location, this information will be stored as a `user_work_location` variable (you can rename this variable if needed).&#x20;

Below is an example that shows how the `user_work_location` variable would be stored when the user responds with 'Chatlayer.ai':

```javascript
{
    fullAddress: "Oudeleeuwenrui 39, 2000 Antwerpen, Belgium",
    latitude: 51.227317,
    longitude: 4.409155999999999,
    streetNumber: "39",
    streetName: "Oudeleeuwenrui",
    city: "Antwerpen",
    country: "Belgium",
    zipcode: "2000",
}
```

{% hint style="info" %}
To show the address as a full address (street, street number, zipcode and city) you need to add some extra information to the variable: `.fullAddress`

So in the example above, the bot can display the entire location by using the following variable:`{user_work_location.fullAddress}`
{% endhint %}

A bot message containing the following info:

`Thank you, shall I send your package to {user_work_location.fullAddress}?`

Will display the following message to the user:

`Thank you, shall I send your package to Oudeleeuwenrui 39, 2000 Antwerpen, Belgium?`

#### Number

Number will parse any number the user has given.

#### Hours

This input type will parse and validate timestamps.

#### Currency

This input type will parse and validate currencies.

#### E-mail

This input type will parse and validate email addresses.

#### Postal code

This input type will parse and validate zip codes. Note: currently we only support Belgian zip codes.

#### **Image**

The image format type allows you to check if a user has uploaded an image or other file (such as pdf). Currently, this is only possible in the Facebook Messenger, WhatsApp, Instagram, RCS, MMS, Telegram and Instagram channels. If the bot user uploads a file, the URL to that file will be saved under the variable you save the response to.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FfIXahKBnQ4KxFImK9H1D%2Fimage.png?alt=media\&token=9a0ab99b-3e26-4762-828d-9a68e5089ebb)

The image will be saved as an array. If you chose {img} as variable, this means that you should use {img\[0]} to retrieve the URL for the first saved image.&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fi7HoJBOzklHVugh3KfDh%2Fimage.png?alt=media\&token=1a4eded6-a0af-4c37-87df-c3f80c264863)

For the chat widget (web channel), we recommend using the [file upload](https://docs-latam.messaging.sinch.com/ia-conversational/untitled-8/broken-reference) template.

#### Language

This input type will parse and validate NLP supported languages.

* English: (en-us): 'engels', 'English', 'en', 'anglais'
* Dutch (nl-nl): 'nederlands', 'Dutch', 'ned', 'nl', 'vlaams', 'hollands', 'be', 'ned', 'néerlandais', 'belgisch'
* French (fr-fr): 'French', 'français', 'frans', 'fr', 'francais'
* Chinese (zh-cn): 'Chinese', 'cn', 'zh', 'chinees'
* Spanish (es-es): 'Spanish', 'español', 'es', 'spaans'
* Italian (it-it): 'Italian', 'italiaans', 'italiano', 'it
* German (de-de): 'German', 'duits', 'de', 'deutsch
* Japanese (ja-jp): 'Japanese', 'japans', 'jp', '日本の
* Brazil Portugese (pt-br): 'Brazil Portugese', 'Portugese', 'portugees', 'braziliaans portugees', 'português'

#### **Voice message**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fly84J1rWoAhefWWEYLEk%2Fimage.png?alt=media\&token=2290f213-b384-4f53-9b54-60dcdfd303c7)

Use the Voice message input type to save whatever is said to the bot in a voice channel as text. You can configure the maximum duration of this voice message, and how long it takes for the bot to regard the message as "complete".


# Action

## Clear Session <a href="#clear-session" id="clear-session"></a>

Often, at the end of a flow, an API backend call will be configured to, for example, save a train ticket in the ticket ordering system. Afterwards users should be able to book a new ticket to a different location.

You can achieve this with the 'clear session' action. This action removes the values of set session variables. This is useful when a user asks to correct a value, or to start over and delete all variables.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-LV37Zkd0k6v1aYEycFQ%2F-LV3aGDou1TkM9YA4Oo_%2Fimage.png?alt=media\&token=707756be-6db6-46fa-82a2-73dd3b290fb1)

## Send to offload provider <a href="#send-to-offload-provider" id="send-to-offload-provider"></a>

A user that reaches this action will be offloaded to a human customer support agent. For this to work, you need to enable offloading.

Depending on your selected offloading provider, additional configuration may be required.

## API <a href="#api" id="api"></a>

This action can be used to integrate back-end services into your bot. More details can be found in [our tutorial](https://docs.chatlayer.ai/integrations/custom-back-end-integrations).

## Code <a href="#code" id="code"></a>

The code editor allows developers to quickly build custom logic on top of the bot by writing their own Javascript code blocks. Typically, the code editor is used to perform requests to external systems, or to do operations with variables.

You can find more information about the code editor here: [Code Editor/integrations/code-action](https://docs.chatlayer.ai/integrations/code-action)

There are also two tutorials in which we show you how the code editor can be used:

[Retrieving data from Airtable (GET)/integrations/code-action/retrieving-data-from-airtable-get](https://docs.chatlayer.ai/integrations/code-action/retrieving-data-from-airtable-get)

[Sending data to Airtable (POST)/integrations/code-action/airtable](https://docs.chatlayer.ai/integrations/code-action/airtable)

## iframe <a href="#iframe" id="iframe"></a>

An iframe is a custom element that can be used to show a different web page in the chat conversation. It can also be used to communicate with the parent window using the [postMessage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage).

Have a look at this basic example:

```
<!DOCTYPE html><html lang="en">	<head>		<meta charset="UTF-8">		</head>		<body>			<button onClick="window.parent.postMessage(JSON.stringify({target:'CL_API',type:'SEND_MESSAGE', payload:{text: 'You clicked the button'} }),'*')">         SEND_MESSAGE        </button>		</body></html>
```

If this block of code is hosted and embedded within our iframe plugin, it will send the user a chat message when they click the button.

The postMessage API can also handle `UPDATE_SESSION` and `GO_TO_DIALOGSTATE` events.

## JSON Builder <a href="#json-builder" id="json-builder"></a>

If your bot is published on the [Webhook API](https://docs.chatlayer.ai/channels/webhook-api) channel, you can use the JSON Builder action to send messages to the conversation that don't need to result in an actual message to the user. Typically, it's used to send information about the user or bot conversation to the website the bot is published on.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-M1dw5eMqNDrpjDngOe6%2F-M1dx9mzFppiXljhS6k-%2Fimage.png?alt=media\&token=3ef5dcd0-6d98-4e2d-9d95-631beacaa858)

### Website window events  <a href="#website-window-events" id="website-window-events"></a>

**You can use the JSON builder action** **in combination with the webwidget channel** to receive window events on your webpage. These events will contain the data as configured in your JSON builder action.

Here's an example: Configure your JSON builder action to send a **language** key, with a variable retrieved from the session, and the "Send config to parent window" toggled on.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-MKa3vnvkdS2-AigosWt%2F-MKa57sjNNmEoWB6CO2l%2Fimage.png?alt=media\&token=c4e9711d-7541-4f47-8ff3-4db02a33cd6b)

Your widget will trigger an event for that configuration to its parent window as a MessageEvent. The MessageEvent will contain a \`data\` field which contains the stringified result of the JSON builder configuration. Here's an example on how to listen to these events:

```
// Chatlayer JSON Builder Event Handlerwindow.addEventListener('message', (event) => {    const data = event && event.data && JSON.parse(event.data) || {}    const { type, payload } = data    if (type !== 'CL_DISPATCH_EVENT') return;    console.log('Chatlayer language received: ' + payload.language)})
```

[<br>](https://docs.chatlayer.ai/bot-answers/dialog-state/user-input-bot-dialog)


# Publishing & platform URLs FAQ

In one of our previous platform updates, we have released a new version of Chatlayer that makes handling the live and draft versions of your bot much easier. Older customers may still know [cms.staging.chatlayer.ai](http://cms.staging.chatlayer.ai/) instead of [app.chatlayer.ai](http://app.chatlayer.ai/).

We’re introducing the [app.chatlayer.ai](http://app.chatlayer.ai/) URL that unifies everything that’s used to be on the [cms.staging.chatlayer.ai](http://cms.staging.chatlayer.ai/) and the [cms.chatlayer.ai](http://cms.chatlayer.ai/) URLs.

## Why are we changing this?  <a href="#why-are-we-changing-this" id="why-are-we-changing-this"></a>

We’ve received a few support tickets by customers accidentally making changes to their live bots when they wanted to do so in the staging environment. And we get it, it’s too easy to make mistakes in a URL! We also think it’s quite a hassle to remember which URL hosts which environment, especially if you’re a new Chatlayer user.

## So, what has changed? <a href="#so-what-has-changed" id="so-what-has-changed"></a>

### Chatlayer URL <a href="#chatlayer-url" id="chatlayer-url"></a>

Instead of having a separate URL for Staging & Production, we now have 1 URL for everything: [app.chatlayer.ai](http://app.chatlayer.ai/). You can manage both the live & draft versions of your bot through this URL.

Now when you open a bot on [app.chatlayer.ai](http://app.chatlayer.ai/), it will open the DRAFT version of that bot. Go to the 'publish' tab to, well, publish your bot.

### Publishing a bot <a href="#publishing-a-bot" id="publishing-a-bot"></a>

We’ve renamed the “Versioning” tab to “Publish”. When you’re ready to publish a newer version of the bot, just click the “Publish” button and follow the steps in the platform.

### Editing your LIVE bot <a href="#editing-your-live-bot" id="editing-your-live-bot"></a>

We recommend against changing the LIVE version of the bot directly. However, in some cases, if you need to make some quick changes without publishing an entirely new version, it can be useful. To change the LIVE version of the bot, go to the “Publish” page. On this page, look for the LIVE version of the bot on the right and click the “Open live mode” button.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-M_LPm53LdLDWkj791F3%2F-M_LPtni7NlT8gxJXdef%2Fimage.png?alt=media\&token=0ef3c7f7-9a50-4f01-834e-1bb6d605bc0b)

### Channels <a href="#channels" id="channels"></a>

Your bot can still connect to draft and live channels separately, exactly like you’re doing now in the Staging and Production environments. However, we want to give a better overview, so we’re consolidating all your channels into one single table.

![](https://gblobscdn.gitbook.com/assets%2F-LLTwFwbOqJj4dDhg8Ju%2F-M_LPm53LdLDWkj791F3%2F-M_LPx6AcFoMlCRoqEY8%2Fimage.png?alt=media\&token=e685e52b-43b0-4946-b3d2-dd1f69fec2eb)

### Conversations <a href="#conversations" id="conversations"></a>

Only one small change on the conversations page: both LIVE and DRAFT conversations are now visible within the same table. You can filter in this table to show either one.

### Bot export <a href="#bot-export" id="bot-export"></a>

When you export a bot, you can now choose between exporting the LIVE or DRAFT version of that bot.

## What is not changing? <a href="#what-is-not-changing" id="what-is-not-changing"></a>

Your workflow will remain the same: you can publish a new version of the bot from draft to live whenever it’s ready.

The Chatlayer API URLs will not change.

## FAQ <a href="#faq" id="faq"></a>

* Am I losing my staging environment?

No, the databases and infrastructure between the staging and production environments have been the same for over a year already. We are just merging the URLs. Your workflow remains the same: you can publish a new version from draft to live whenever it’s ready.

* Will the old URLs (using ‘cms’) still work?

The ‘cms’ URLs will continue to work for now. At some point in the future we will redirect them to [app.chatlayer.ai](http://app.chatlayer.ai/) URLs. There will be no change to the URLs that you use in your APIs.

* What do I have to change to my account or bot?

Nothing! Your workflow will remain the same: you can publish a new version of the bot from draft to live whenever it’s ready. The Chatlayer API URLs will not change.

* Will there be any downtime of the bots during or after the release?

We have been secretly preparing for this release for a long time, so in the background, everything has been merged already. This means that this change isn’t actually a really big one. Hence, we do not expect any downtime during or after the release of your bot.

* What will happen to the analytics dashboard?

If you have a live version of your bot, we will show you the stats from that live version. If you don’t, we will show some sample data in the analytics dashboard.

* What should I do if I still have questions?

If you have any questions about your bot specifically, feel free to [reach out to us](http://support.chatlayer.ai/).


# Latam Messaging Technical Documentation regarding API & Integrations

API & Integrations

Welcome to our technical documentation for developers!​

Here you’ll find everything you need to integrate your business to our messaging platform.

**API & Integrations Menu.**

**API & Integrations**

* **​**[**Introduction – Types of Integration**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/introducao)​
* ​[**Atlas API**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/atlas-api)**​**
* **​**[**SMS API**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/sms-api)**​**
* **​**[**Email API**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/e-mail-api)​
* **​**[**Fallback API**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/fallback-api)​
* **​**[**WhatsApp API**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/whatsapp-api)​
* **​**[**WhatsApp Groups API**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/grupos-de-whatsapp-api)​
* **​**[**WhatsApp Lists via API**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/listas-whatsapp-via-api)​
* **​**[**WhatsApp Messaging via FTP**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/envio-whatsapp-via-ftp)​
* **​**[**Campaigns API**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/campanhas-api)​
* **​**[**TTL - Time to Live**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/ttl-time-to-live)​
* **​**[**Webhook**](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/webhook%22%20/t%20%22_blank)**​**

​


# Introduction - Integrations

Welcome to our documentation for developers

&#x20;Here you will find everything you need to integrate your company to our messaging platform.&#x20;

### Types of Integration&#x20;

You can integrate through the following methods:&#x20;

| ​                | ​                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HTTPS API**    | Allows you to send and receive messages and statuses through HTTPS protocol using the GET or POST methods                                                                                                                                                                                                                                                                   |
| **SMPP API**     | Specific protocol for exchanging SMS messages; it allows you to maintain an active connection with our SMPP server and is suitable for customers whose traffic is over 5 million messages per month                                                                                                                                                                         |
| **SFTP API**     | Protocol used to transfer files; it is suitable for mass messaging (bulk). The files are transferred by the customer to our servers and are immediately processed                                                                                                                                                                                                           |
| **Websphere MQ** | Used to transfer messages between Websphere MQ servers; it is suitable for customers whose traffic is over 30 million messages per month, especially financial banks where the customer already has this system in operation for internal messages. This integration option has an environment setup and maintenance fee, priced at R$50,000.00 and R$2,000.00 respectively |

### API & Integrations Menu.&#x20;

{% hint style="info" %}
API & Integrations&#x20;

* ​[Introduction – Types of Integration​ ](https://doc-messaging.wavy.global/#introduction)
* ​[SMS API​](https://doc-messaging.wavy.global/#sms-api)&#x20;
* ​[WhatsApp API​](https://doc-messaging.wavy.global/#whatsapp-api)&#x20;
* ​[WhatsApp Lists via API​ ](https://doc-messaging.wavy.global/#whatsapp-lists-via-api)
* ​[WhatsApp Messaging via FTP​](https://doc-messaging.wavy.global/#api-sftp-whatsapp)&#x20;
* ​[Campaigns API​](https://doc-messaging.wavy.global/#campaigns-api)&#x20;
  {% endhint %}


# SMS API

Technical Documentation: SMS API.

## Important Terms

### **Important Terms**

| ​             | ​                              | ​                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MT**        | Mobile Terminated              | Term used for messages that have the user (device) as destination. I.e., **messages originating from your company**, destined for the user (device)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **MO**        | Mobile Originated              | Term used for messages that have your company as destination. I.e., **messages originating from the user** (device). It is used, for instance, in question and answer flows via SMS, when confirmation is required from the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Response**  | Synchronous response from Wavy | The immediate response to a request made in our API, where we inform whether the message has been accepted by our platform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Callback**  | Sent status                    | The first sent status we return, where we inform whether the message has been delivered **to the carrier**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **LA**        | Short Code                     | A short 5- or 6-digit number, used for sending and receiving SMS messages. They are appointed by carriers to approved integrators (Wavy) and have antifraud and antispam rules                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **DR or DLR** | Delivery Receipt               | <p>The second sent status we return, where we inform whether the message was delivered <strong>to the device</strong>. The carriers send this information to Wavy, and we relay it to the customer. Delivery time varies: for example, if the device was turned off at the time the message was sent and the user turned it back on 2 hours later, this DLR status will be delivered to the customer with a 2-hour delay.</p><p><strong>•</strong> This receipt of delivery to the device will only exist in cases where the message has been successfully delivered to the carrier, i.e., the first status (callback) was successful.</p><p><strong>•</strong> It is very important to highlight that unfortunately carriers Oi and Sercomtel do not have this functionality, that is, they do not give us information on delivery to the device. Messages sent to numbers from those carriers will only have information on delivery to the carrier (callback)</p> |

## Message Flow

Simplified Flow: MT, Callback, DLR, MO

!\[Diagram

Description automatically generated]\(<https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGhsmOlT1CwS5Md1dR%2F-MlGj-fPMNPcZsbwy1u5%2F0.png?generation=1633458858387845\\&alt=media>)

## HTTPS API

This API allows you to automatize both single and bulk message requests and the retrieval of sent statuses through queries. It uses HTTP protocol with TLS and accepts the GET method with query string parameters and the POST method with [JSON](http://json.org/) parameters.

### Authentication

To send messages and run queries in our API, you need to authenticate using a combination of either username or email and a token.

| Field                   | Details                                                                                                                                                                                                                                                                                                                         | Data Type |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **UserName**            | Your username or email                                                                                                                                                                                                                                                                                                          | String    |
| **AuthenticationToken** | Your authentication token. Check [here](https://messaging.movile.com/messaging/user/api_configuration) and read username descriptions below.                                                                                                                                                                                    | String    |
| Type                    | Details                                                                                                                                                                                                                                                                                                                         | ​         |
| **Administrator**       | Admin user for your company; it is used for creating/editing/deactivating subaccounts and other users, and it can view reports of the entire company. This user does not send messages, whether through the portal or via API integration.                                                                                      | ​         |
| **User**                | User used for sending messages via API and portal; it can view reports specific to its subaccount. A user is always related to a single subaccount. A subaccount can have multiple users. Each subaccount is a cost center in our platform; messages are broken down in reports and financially by subaccount, and not by user. | ​         |
| **templateID**          | SMS template identifier. The text of the message will be retrieved and it should first be created through the Messaging Portal.                                                                                                                                                                                                 | Long      |
| **templateName**        | SMS template name. It may not be exclusive, resulting in an error if more than one template is found for the user’s access level. The text of the message will be retrieved and it should first be created through the Messaging Portal                                                                                         | String    |

### Connection Details

| ​                  | ​                                                            |
| ------------------ | ------------------------------------------------------------ |
| **Hostname**       | api-messaging.wavy.global                                    |
| **APIs**           | Single messages /v1/send-sms Bulk messages /v1/send-bulk-sms |
| **Port**           | 443 (https)                                                  |
| **Protocol**       | HTTPS (TLS encryption)                                       |
| **Authentication** | username + token                                             |
| **Portal**         | messaging.wavy.global                                        |

### Encoding

The encoding standard used is UTF-8, all message contents must follow this standard.

You can escape characters if you wish or encode using HTTP format.

You can see some encoding examples to the side

***“messageText”:“A combinação foi perfeita :)”***

Or you can escape characters if you so wish:

***“messageText”:“A combina\u00e7\u00e3o foi perfeita :)”***

***​***

## Sending Messages (MT)

### Sending with GET Method - Individual

curl -X POST \\

&#x20;<https://api-messaging.wavy.global/v1/send-sms> \\

&#x20;-H 'authenticationtoken: \<authenticationtoken>' \\

&#x20;-H 'username: \<username>' \\

&#x20;-H 'content-type: application/json' \\

&#x20;-d '{"destination": "5511900000000" , "messageText": "linha\nquebrada"}'

​

After sending a message, you will receive a JSON informing the id that was generated for that message (Synchronous response from Wavy):

\[

&#x20;{

&#x20;"id":"9cb87d36-79af-11e5-89f3-1b0591cdf807",

&#x20;"correlationId":"myId"

&#x20;}

]

Via GET method, you can send a message by relaying all parameters as a query string.

### URL for Single Messages with GET Method

GET <https://api-messaging.wavy.global/v1/send-sms?destination=>..

Via POST method, you can send a message by relaying all parameters in the body.

### URL for Single Messages with POST Method

POST <https://api-messaging.wavy.global/v1/send-sms> - Content-Type: application/json

### Request Parameters

**\* Required field**

| Field                | Details                                                                                                                                                                                                                                                                                                                                                                                                                                        | Type       |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **destination\***    | Phone number to which the message will be sent (**including country code**). E.g.: 5511900000000                                                                                                                                                                                                                                                                                                                                               | String     |
| **messageText\***    | Text of the message to be sent (max 1280 chars).                                                                                                                                                                                                                                                                                                                                                                                               | String     |
| **correlationId**    | A unique ID set by you to match the sent statuses (callback and DLR). This parameter is optional, and you can use the ID generated by Wavy for this purpose (max 64 chars).                                                                                                                                                                                                                                                                    | String     |
| **extraInfo**        | Any extra information you wish to add to your message (max 255 chars).                                                                                                                                                                                                                                                                                                                                                                         | String     |
| **timeWindow**       | Messages will only be sent during the specified time. For example, if you set a \[11, 12, 18] window, messages will be sent between 11:00 and 11:59 A.M., 12:00 and 12:59 P.M., and 6:00 and 6:59 PM. This parameter must be set in the root of the JSON object                                                                                                                                                                                | Integer\[] |
| **expiresAt**        | Your message will not be sent after this date. The format used is [Unix time](https://en.wikipedia.org/wiki/Unix_time) . Note: The expiresAt, expiresInMinutes and expiresDate field are mutually exclusive (use one of them only)                                                                                                                                                                                                             | Long       |
| **expiresInMinutes** | Your message will expire after the time set in this field. The time starts counting as soon as your message is received by Wavy. Note: The expiresAt, expiresInMinutes and expiresDate fields are mutually exclusive (use one of them only)                                                                                                                                                                                                    | Long       |
| **expiresDate**      | Your message will not be sent after this date. This field accepts the following format yyyy-MM-dd’T'HH:mm:ss. Note: The expiresAt, expiresInMinutes and expiresDate fields are mutually exclusive (use one of them only)                                                                                                                                                                                                                       | String     |
| **scheduledAt**      | Your message will not be sent after this date. IMPORTANT! You can only schedule a period longer than 30 minutes, as it is processed by a differentiated flow from non-scheduled messages. The format used is [Unix time](https://en.wikipedia.org/wiki/Unix_time). The expiresAt, expiresInMinutes and expiresDate fields are mutually exclusive (use one of them only)                                                                        | Long       |
| **delayedInMinutes** | How many minutes after the request is made your message will be sent. The expiresAt, expiresInMinutes and expiresDate fields are mutually exclusive (use one of them only)                                                                                                                                                                                                                                                                     | Long       |
| **scheduledDate**    | Your message will not be sent before this date. This field supports the format yyyy-MM-dd’T'HH:mm:ss. Note: The expiresAt, expiresInMinutes and expiresDate fields are mutually exclusive (use one of them only)                                                                                                                                                                                                                               | String     |
| **timeZone**         | Specifies the time zone into be used directly in the fields: expiresDate, scheduledDate and timeWindow (which will be modified in case dynamic time zones are used, such as daylight saving time). If the time zone is not included in your request, the system will check the user’s time zone - if included - or the time zone of the user’s country as a last resort. If neither of these options are present, the system will use UTC time | String     |
| **campaignAlias**    | Identification for a previously created campaign. [Click here](https://messaging.movile.com/messaging/master) to register a new campaign; this parameter must be set in the root of the JSON object                                                                                                                                                                                                                                            | String     |
| **flashSMS**         | Flash SMS; use this option to send a pop-up message to a user’s phone. To send a Flash message, set parameter to true.                                                                                                                                                                                                                                                                                                                         | Boolean    |
| **flowId**           | Bot flow identifier. The text of your message will come from the selected flow                                                                                                                                                                                                                                                                                                                                                                 | String     |
| **subAccount**       | Subaccount reference. It can only be used by Admin users                                                                                                                                                                                                                                                                                                                                                                                       | String     |
| **params**           | Map of placeholders that will be replaced in the text of your message. If one or more parameters are incorrect, your message will be flagged as invalid, but delivery will not be cancelled. You must send the flowId to use parameters                                                                                                                                                                                                        | Map        |

**For every user, there is a unique authentication token**

### Messaging via POST Method - Single or Bulk

curl --request POST \\

&#x20;\--url <https://api-messaging.wavy.global/v1/send-bulk-sms> \\

&#x20;\--header 'authenticationtoken: \<Authentication Token>' \\

&#x20;\--header 'username:\<Movile Messaging User>' \\

&#x20;\--header 'content-type: application/json' \\

&#x20;\--data "{ "messages":\[{ "destination":"5519999999999", "messageText":"First message" }, { "destination":"5519999999999" }, { "destination":"5519999999999" }], "defaultValues":{"messageText":"Default message" }}"

​

**There is a 1000-message limit per request**

After sending a message, a JSON object will be returned with the UUID for the batch and individual messages:

​

&#x20;{

&#x20;"id": "ce528d70-013b-11e7-98f2-e27c463c8809",

&#x20;"messages": \[

&#x20;{

&#x20;"id": "ce528d71-013b-11e7-98f2-e27c463c8809"

&#x20;},

&#x20;{

&#x20;"id": "ce528d72-013b-11e7-98f2-e27c463c8809"

&#x20;}

&#x20;]

}

Allows you to send bulk or individual messages by relaying parameters in a JSON object. There is a 1000-message limit per request

### HTTP Request via POST Method

Example of JSON for Bulk messaging:

Example 1:

{

&#x20;"messages":\[

&#x20;{

&#x20;"destination":"5519900001111",

&#x20;"messageText":"First message"

&#x20;},

&#x20;{

&#x20;"destination":"5519900002222"

&#x20;},

&#x20;{

&#x20;"destination":"5519900003333"

&#x20;}

&#x20;],

&#x20;"defaultValues":{

&#x20;"messageText":"Default message"

&#x20;}

}

Example 2:

{

&#x20;"messages":\[

&#x20;{

&#x20;"destination":"5519900001111",

&#x20;"messageText":"First message"

&#x20;},

&#x20;{

&#x20;"destination":"5519900002222"

&#x20;}

&#x20;],

&#x20;"timeZone":"America/Sao\_Paulo",

&#x20;"scheduledDate": "2017-01-28T02:30:43",

&#x20;"timeWindow": \[12, 15, 20],

&#x20;"defaultValues":{

&#x20;"messageText":"Default message"

&#x20;}

}

Example 3:

{

&#x20;"messages":\[

&#x20;{

&#x20;"destination":"5519900001111"

&#x20;},

&#x20;{

&#x20;"destination":"5519900002222"

&#x20;}

&#x20;],

&#x20;"defaultValues":{

&#x20;"messageText":"Default message",

&#x20;"flashSMS":"true"

&#x20;}

}

Example 4, with flowId and params:

{

&#x20;"messages":\[

&#x20;{

&#x20;"destination":"5519900001111",

&#x20;"params": {

&#x20;"param1": "other\_value1",

&#x20;"param2": "other\_value2"

&#x20;}

&#x20;},

&#x20;{

&#x20;"destination":"5519900002222"

&#x20;}

&#x20;],

&#x20;"defaultValues":{

&#x20;"params": {

&#x20;"param1": "value1",

&#x20;"param2": "value2"

&#x20;}

&#x20;},

&#x20;"flowId": "14f8142d-e731-4971-8220-5a76a12c413f"

}

Example 5, with templateId/templateName (possible with either or both) and parameters:

{

&#x20;"messages":\[

&#x20;{

&#x20;"destination":"5519900001111",

&#x20;"params": {

&#x20;"param1": "other\_value1",

&#x20;"param2": "other\_value2"

&#x20;}

&#x20;},

&#x20;{

&#x20;"destination":"5519900002222"

&#x20;}

&#x20;],

&#x20;"defaultValues":{

&#x20;"params": {

&#x20;"param1": "value1",

&#x20;"param2": "value2"

&#x20;}

&#x20;},

&#x20;"templateId": 0,

&#x20;"templateName": 'name'

}

​

## HTTP Status Code Response

Most common HTTP status codes:

| Group   | Description           |
| ------- | --------------------- |
| **2xx** | Success               |
| **4xx** | Client Error          |
| **5xx** | Server Error          |
| Code    | Description           |
| **200** | Success               |
| **400** | Bad Request           |
| **401** | Unauthorized          |
| **403** | Forbidden             |
| **404** | Not Found             |
| **429** | Too Many Requests     |
| **500** | Internal Server Error |
| **503** | Service Unavailable   |
| **504** | Gateway Timeout       |

Maximum limit is 700 requests per second per IP.

## Sent Status (Callback and DLR)

There are two ways of obtaining message sent statuses, namely:

* Webhook - Receive statuses in a webserver of your company (recommended)

As soon as we deliver your message to the carrier, or as soon as the carrier informs us whether it has delivered your message to the device, this information is relayed to you instantaneously.

* Query API - Make query requests in our sms-status API.

Statuses are available for 3 days and can be retrieved using the UUID that Wavy returned upon receiving the message from your company or the ID that your company received after delivering your message to Wavy.

The downside to this option Note in the examples above, some “destination” fields do not have a “messageText” directly attributed to them; in these cases, the text of your message will be the “messageText” within “defaultValues.” This function is useful when you need to send the same message to several different numbers of running queries instead of webhooks is that you will make query requests for an ID that might not have been delivered to the carrier or the device yet; in this case, a series of unnecessary requests will be made. For example, if a user had their device turned off when you sent them a message and they turned it back on 2 hours later, you will be requesting this ID countless times during two hours. And if you use a webhook, this information would be sent to you as soon as it was delivered to the device, without any empty requests.

Status queries have a rate-limit of 1 request per second per IP address. Requests beyond this limit are responded to with HTTP status code 429.

### Statuses via Webhook (Delivery to Your Webservice)

In order to set the delivery of Callbacks and DRs (if you have questions about these terms, check the [Important Terms](http://doc-messaging.movile.com/pt.html#termos-importantes) tab), first you need to log in to [Wavy Messaging](https://www.messaging.wavy.global/) in API settings; in the settings form, you can provide the URLs to which sent statuses (Callbacks) and device confirmation statuses (DRs) will be sent

After including your webhook in the portal above, your settings will be replicated to our platform within 10 minutes, and we will call your URL when the following actions occur:

| Action                                                      | Return status sent         |
| ----------------------------------------------------------- | -------------------------- |
| After a message is delivered or not to the carrier          | Sent status API (callback) |
| When a message is delivered or not to the customer’s device | Delivery Report API (DRs)  |

Example of JSON sent status (callback - delivery to the carrier)

POST <https://example.com/callback/>

Content-Type: application/json

​

{

&#x20;"id":"f9c100ff-aed0-4456-898c-e57d754c439c",

&#x20;"correlationId":"client-id",

&#x20;"carrierId":1,

&#x20;"carrierName":"VIVO",

&#x20;"destination":"5511900009999",

&#x20;"sentStatusCode":2,

&#x20;"sentStatus":"SENT\_SUCCESS",

&#x20;"sentAt":1266660300000,

&#x20;"sentDate":"2010-02-20T10:05:00Z",

&#x20;"campaignId":"64",

&#x20;"extraInfo":"",

}

### JSON response fields in Callbacks (sent status)

| Field              | Description                                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------- |
| **id**             | Message UUID generated                                                                                                |
| **correlationId**  | Your identification for this message                                                                                  |
| **carrierId**      | Carrier identifier                                                                                                    |
| **carrierName**    | Carrier name                                                                                                          |
| **destination**    | Phone number to which your message was sent                                                                           |
| **sentStatusCode** | Status code generated by Wavy for your message indicating its sent status. Refer to status codes for more information |
| **sentStatus**     | Sent status description. Refer to status codes for more information                                                   |
| **sentAt**         | Time the message was sent, the format used is Unix\_time                                                              |
| **sentDate**       | Date the message was sent. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                             |
| **campaignId**     | Campaign identifier, if any                                                                                           |
| **extraInfo**      | Any extra information added by the customer when sending the message                                                  |

### JSON response fields in Delivery Reports (DRs)

| Field                   | Description                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **id**                  | Message UUID generated                                                                                                     |
| **correlationId**       | Your identification for this message                                                                                       |
| **carrierId**           | Carrier identifier                                                                                                         |
| **carrierName**         | Carrier name                                                                                                               |
| **destination**         | Phone number to which your message was sent                                                                                |
| **sentStatusCode**      | Status code generated by Wavy for your message indicating its sent status. Refer to status codes for more information      |
| **sentStatus**          | Sent status description. Refer to status codes for more information                                                        |
| **sentAt**              | Time the message was sent, the format used is Unix\_time                                                                   |
| **sentDate**            | Date the message was sent. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                  |
| **deliveredStatusCode** | Status code generated by Wavy for your message indicating its delivered status. Refer to status codes for more information |
| **deliveredStatus**     | Delivered status description. Refer to status codes for more information                                                   |
| **deliveredAt**         | Time of delivery, the format used is Unix\_time                                                                            |
| **deliveredDate**       | Date the message was sent. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                  |
| **campaignId**          | Campaign identifier, if any                                                                                                |
| **extraInfo**           | Any extra information added by the customer when sending the message                                                       |

### Status Query via HTTP Request

To check the status of the your last sent messages, you need to make a POST request to the URL below by sending the UUID(s) and/or correlationId(s) obtained in the sent response:

POST <https://api-messaging.wavy.global/v1/sms/status/search>

{ "ids": \["918F3591-9AD6-11E7-9C9B-E255B01A8B1A","234F3591-6AD6-11E7-9C9B-E255B01A8B1A"], "correlationIds": \["2468"] }

You can also obtain only the statuses that have not yet been requested:

GET <https://api-messaging.wavy.global/v1/sms/status/list>

Note that this endpoint only returns statuses that haven’t yet been returned by this endpoint.

### Response

JSON response fields:

| Field                   | Details                                                                                                       | Type   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- | ------ |
| **id**                  | UUID generated in the request for the message                                                                 | String |
| **correlationId**       | Same correlationId as in the request                                                                          | String |
| **carrierId**           | Carrier ID; for more information, refer to error codes                                                        | Long   |
| **carrierName**         | Carrier name                                                                                                  | String |
| **destination**         | Phone number to which your message was sent                                                                   | String |
| **sentStatusCode**      | Sent status code. Refer to Sent Status Codes for more information                                             | Long   |
| **sentStatus**          | Sent status. Refer to Sent Status Codes for more information                                                  | String |
| **sentStatusAt**        | When the message was sent. It is an Epoch Date                                                                | Long   |
| **sentStatusDate**      | When the message was sent. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone (ISO 8601)      | String |
| **deliveredStatusCode** | Delivered status code. Refer to Delivered Status Codes for more information                                   | Long   |
| **deliveredStatus**     | Delivered status. Refer to Delivered Status Codes for more information                                        | String |
| **deliveredAt**         | When the message was delivered. It is an Epoch Date                                                           | Long   |
| **deliveredDate**       | When the message was delivered. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone (ISO 8601) | String |
| **campaignId**          | Campaign Identifier                                                                                           | Long   |
| **extraInfo**           | Any extra information set by the user when the message was sent                                               | String |

Example of JSON Delivery Report (DR or DLR - Delivery to the user’s device)

{

&#x20;"id":"8f5af680-973e-11e4-ad43-4ee58e9a13a6",

&#x20;"correlationId":"myId",

&#x20;"carrierId":5,

&#x20;"carrierName":"TIM",

&#x20;"destination":"5519900001111",

&#x20;"sentStatusCode":2,

&#x20;"sentStatus":"SENT\_SUCCESS",

&#x20;"sentStatusAt":1420732929252,

&#x20;"sentStatusDate":"2015-01-08T16:02:09Z",

&#x20;"deliveredStatusCode":4,

&#x20;"deliveredStatus":"DELIVERED\_SUCCESS",

&#x20;"deliveredAt":1420732954000,

&#x20;"deliveredDate":"2015-01-08T16:02:34Z",

&#x20;"campaignId":1234

}

## User Response (MO)

The MO API allows you to automatize the process of retrieving messages sent by customers in response to the messages you have sent them. All requests use the GET method, and responses are sent in JSON format. IMPORTANT! MO receipt is enabled by default only for LAs 27182 and 28149; if you need to receive messages through other Las, you need to contact support for evaluation.

You can also set it so that MOs are forwarded as they arrive to an API of the customer; this is the most efficient manner, as you don’t have to make any calls, just handle messages as they arrive. For this setting to be made, you need to open a ticket with our support team at <customer.service@wavy.global> relaying the url that will receive MOs. We are able to send MOs via both GET method (query string) and POST method (JSON)

Example of JSON sent to your API (POST method)

{

&#x20;"id": "25950050-7362-11e6-be62-001b7843e7d4",

&#x20;"subAccount": "iFoodMarketing",

&#x20;"campaignAlias": "iFoodPromo",

&#x20;"carrierId": 1,

&#x20;"carrierName": "VIVO",

&#x20;"source": "5516981562820",

&#x20;"shortCode": "28128",

&#x20;"messageText": "I want pizza",

&#x20;"receivedAt": 1473088405588,

&#x20;"receivedDate": "2016-09-05T12:13:25Z",

&#x20;"mt": {

&#x20;"id": "8be584fd-2554-439b-9ba9-aab507278992",

&#x20;"correlationId": "1876",

&#x20;"username": "iFoodCS",

&#x20;"email": "<customer.support@ifood.com>"

&#x20;}

&#x20;}

​

Each request made will return MOs received during the last 3 days, up to a limit of 1,000 MOs. For previous dates or larger amounts, please contact our support team at <customer.service@wavy.global>

The behavior of the MO query list will be different for each authenticated user due to each user’s permission level.

We recommend the method of sending MOs to an API; every MO sent will automatically be sent to an API, thus all responses can be handled immediately after receipt

| Profile           | Permission                                                                                                                                                                                                                                                       |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Regular**       | each request made in the MO API will only return MOs that correspond to the subaccount the user belongs to. A regular user is not able to retrieve MOs from other subaccounts.                                                                                   |
| **Administrator** | the default behavior for the administrator user is to retrieve all MOs from all subaccounts. If an admin wishes to retrieve MOs from only one subaccount, they need to specify the subaccount in the subAccount parameter with the id of the desired subaccount. |

### Default MO Response Format

Example of JSON response to a Wavy API call:

{

&#x20;"total": 1,

&#x20;"start": "2016-09-04T11:12:41Z",

&#x20;"end": "2016-09-08T11:17:39.113Z",

&#x20;"messages": \[

&#x20;{

&#x20;"id": "25950050-7362-11e6-be62-001b7843e7d4",

&#x20;"subAccount": "iFoodMarketing",

&#x20;"campaignAlias": "iFoodPromo",

&#x20;"carrierId": 1,

&#x20;"carrierName": "VIVO",

&#x20;"source": "5516981562820",

&#x20;"shortCode": "28128",

&#x20;"messageText": "I want pizza",

&#x20;"receivedAt": 1473088405588,

&#x20;"receivedDate": "2016-09-05T12:13:25Z",

&#x20;"mt": {

&#x20;"id": "8be584fd-2554-439b-9ba9-aab507278992",

&#x20;"correlationId": "1876",

&#x20;"username": "iFoodCS",

&#x20;"email": "<customer.support@ifood.com>"

&#x20;}

&#x20;},

&#x20;{

&#x20;"id": "d3afc42a-1fd9-49ff-8b8b-34299c070ef3",

&#x20;"subAccount": "iFoodMarketing",

&#x20;"campaignAlias": "iFoodPromo",

&#x20;"carrierId": 5,

&#x20;"carrierName": "TIM",

&#x20;"source": "5519987565020",

&#x20;"shortCode": "28128",

&#x20;"messageText": "Is my burger arriving?",

&#x20;"receivedAt": 1473088405588,

&#x20;"receivedDate": "2016-09-05T12:13:25Z",

&#x20;"mt": {

&#x20;"id": "302db832-3527-4e3c-b57b-6a481644d88b",

&#x20;"correlationId": "1893",

&#x20;"username": "iFoodCS",

&#x20;"email": "<customer.support@ifood.com>"

&#x20;}

&#x20;}

&#x20;]

}

Both list and search requests return a JSON object with the following fields:

| Field        | Details                                     | Type    |
| ------------ | ------------------------------------------- | ------- |
| **total**    | Total number of MOs returned by the request | Integer |
| **start**    | Minimum query limit                         | String  |
| **end**      | Maximum query limit                         | String  |
| **messages** | List of objects                             | List    |

### **Each message in the messages field has the following structure:**

| Field             | Details                                                                                       | Type    |
| ----------------- | --------------------------------------------------------------------------------------------- | ------- |
| **id**            | Message ID                                                                                    | String  |
| **subAccount**    | subaccount responsible for sending the message that generated the response                    | String  |
| **carrierId**     | Carrier ID                                                                                    | Integer |
| **carrierName**   | Carrier name                                                                                  | String  |
| **source**        | Phone number that sent the response message                                                   | String  |
| **shortCode**     | Shortcode of the message that originated the response and through which the response was sent | String  |
| **messageText**   | Text of the response message                                                                  | String  |
| **receivedAt**    | Time of receipt                                                                               | Long    |
| **receivedDate**  | Date and time of receipt in UTC format                                                        | String  |
| **campaignAlias** | Alias of the campaign that originated the response                                            | String  |
| **mt**            | Original MT that generated the response                                                       | MT      |

### **MTs have the following structure:**

| Field             | Details                                             | Type   |
| ----------------- | --------------------------------------------------- | ------ |
| **id**            | MT ID                                               | String |
| **correlationId** | CorrelationID sent in the MT                        | String |
| **username**      | Username of the user responsible for sending the MT | String |
| **email**         | Email of the user responsible for sending the MT    | String |

### List MO Request

The List will return all MOs received since the last call according to the default response described above. Once this call is made, it will be consumed and will not return following calls.

As a regular user, to retrieve all MOs from a subaccount, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/list>

As an administrator user, to retrieve ALL MOs from ALL subaccounts, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/list>

As an administrator user, to retrieve MOs from a subaccount with the reference “referencia\_subconta”, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/list?subAccount=referencia\\_subconta>

### Search MO Request

The search request will return each MO received within a given period of time. You must set the start and end parameters to specify a time period, using the ISO-8601 format. START by default is set for 5 days prior to the current date, and END by default is set for the current date. You cannot retrieve MOs prior to 5 days.

As a regular user, to retrieve all MOs from a subaccount, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/search>

As an administrator user, to retrieve ALL MOs from ALL subaccounts, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/search>

As an administrator user, to retrieve MOs from a subaccount with the reference “referencia\_subconta”, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/search?subAccount=referencia\\_subconta>

Search with set START and END parameters:

GET <https://api-messaging.wavy.global/v1/sms/receive/search?start=2016-09-12T00:00:00\\&end=2016-09-15T00:00:00>

Only with START specified (using default END, current date)

GET <https://api-messaging.wavy.globalv1/sms/receive/search?start=2016-09-12T00:00:00>

Only with END specified (using default START, 5 days prior to the current date)

GET <https://api-messaging.wavy.global/v1/sms/receive/search?end=2016-09-15T00:00:00>

Using default values for START and END and specifying the subaccount

GET <https://api-messaging.wavy.global/v1/sms/receive/search?subAccount=iFoodMarketing>

## Sent Status Codes

There are **two status levels** that are sent independently.

**1 - First Status (sent\_status - Sent Status = Callback)**

Status of delivery **to the carrier**, this is the first status we return, and all carriers have it.

| Code    | Message                                  | Meaning                                                                                                                                                                                                                         |
| ------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**   | **SENT\_SUCCESS**                        | Successfully delivered to the carrier (This is the status to be considered for billing purposes.)                                                                                                                               |
| **101** | **EXPIRED**                              | Expired before being delivered to the device                                                                                                                                                                                    |
| **102** | **CARRIER\_COMMUNICATION\_ERROR**        | Communication error with the carrier                                                                                                                                                                                            |
| **103** | **REJECTED\_BY\_CARRIER**                | The carrier has rejected the message                                                                                                                                                                                            |
| **201** | **NO\_CREDIT**                           | The message limit set by your company’s administrator, for your account or subaccount, has been exceeded. Or, if your company uses the pre-paid credit model, it has run out.                                                   |
| **202** | **INVALID\_DESTINATION\_NUMBER**         | The destination number is invalid (Not a valid mobile number).                                                                                                                                                                  |
| **203** | **BLACKLISTED**                          | The destination number is blacklisted and has been manually entered by your company.                                                                                                                                            |
| **204** | **DESTINATION\_BLOCKED\_BY\_OPTOUT**     | The destination number has opted out and no longer wishes to receive messages from this subaccount. (This status is specifically for mobile marketing accounts).                                                                |
| **205** | **DESTINATION\_MESSAGE\_LIMIT\_REACHED** | The destination number has already received the maximum number of messages that one company can send, within a period of time. (This status is specifically for Mobile Marketing accounts, and this is a rule set by carriers). |
| **207** | **INVALID\_MESSAGE\_TEXT**               | The text of your message contains words that are not accepted by the carrier. These words can be profanity, or, if yours is a Mobile Marketing account, they can be major brands.                                               |
| **301** | **INTERNAL\_ERROR**                      | An error occurred in Wavy’s platform.                                                                                                                                                                                           |

**2 - Second Status (delivered\_status - Delivery Report Callback)**

Status of delivery to **the device**, this is the second status we return and it only exists for cases where the first status above was successful, i.e., the message was successfully delivered to the carrier. In this status, we inform whether the message has been delivered to the device. Carriers Oi and Sercomtel do not have this second status level; for those carriers, the first status, i.e., whether the carrier has accepted your message, is the maximum information there is.

| Code    | Message                | Meaning                                                                                                                                                                                                                                                                                                                                                        |
| ------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **4**   | **DELIVERED\_SUCCESS** | Successfully delivered to the device.                                                                                                                                                                                                                                                                                                                          |
| **104** | **NOT\_DELIVERED**     | The carrier has accepted the message, but was unable to deliver it to the device. Potential causes: Device is off or has no signal for a given period of time (usually 24 hours, but for some carriers, such as Vivo, this retry period is 8 hours). Number is valid, but inactive (some carriers only return this kind of error in this second status level). |

## SMPP API

All services provided by Wavy must necessarily be encrypted, and the [SMPP](http://doc-messaging.movile.com/pt.html#termos-importantes) protocol does not have native encryption. In this case, we provide two options for integration:

### Option 1 - SMPP over TLS + IP whitelist (**Recommended option**)

This is the option we recommend. If your system does not have this functionality, click [HERE](http://doc-messaging.movile.com/pt.html#proxy-tls) to get help in setting up a TLS proxy.

In addition to the encryption to be done by TLS, access will only be authorized for the public IP of your server. (We accept multiple IPs and ranges) This information must be sent to the email address <customer.service@wavy.global>

If you need to allow outgoing traffic in your firewall, we recommend allowing any destination IP on port 2444; if not possible, you must include rules with the following allowances: 200.219.220.8:2444 200.219.220.193:2444 200.189.169.8:2444 189.36.59.86:2444 45.236.179.18:2444 45.236.179.19:2444

​

### Option 2 - SMPP over VPN

Encryption and access granting will be done through VPN.

If you choose this option, set up VPNs using the peers and hosts below, already including the phase 1 and 2 proposals you wish. Please send the completed VPN form for your company to <customer.service@wavy.global>

peer 200.155.0.250 hosts 200.219.220.8 and 200.219.220.193 port 2443

peer 200.143.57.150 hosts 200.189.169.8 and 189.36.59.86 port 2443

peer 45.236.178.12 hosts 45.236.179.18 and 45.236.179.19 port 2443

For high availability and load balancing reasons, you are required to set the **2** **VPNs**, as well as use the smpp-messaging.wavy.global.com domain as your SMPP client’s destination, instead of IPs.

​

## Connection Details

| Information                     | Details                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hostname**                    | smpp-messaging.wavy.global When setting your SMPP system, you must use the domain as destination, instead of IPs. This domain has 4 entry proxies with round robin DNS and health check, and multiple backend servers. Based on the volume of messages your company will transmit, we will increase the number of binds (connections) allowed simultaneously. |
| **Port**                        | 2444 (SMPP over TLS) or 2443 (VPN)                                                                                                                                                                                                                                                                                                                            |
| **SMPP Version**                | 3.4                                                                                                                                                                                                                                                                                                                                                           |
| **Bind Count**                  | Minimum of 4. Setting at least 4 binds is required to obtain high availability and load balancing.                                                                                                                                                                                                                                                            |
| **Character Encoding**          | GSM7 - Default (data\_coding = 0) (GSM3.38 extended table is not supported by carriers.) LATIN1 (data\_coding = 1) UCS2 (data\_coding=8). **Attention:** Check character and billing details [HERE](http://doc-messaging.movile.com/pt.html#characters).                                                                                                      |
| **Flash SMS**                   | Supported data\_coding=0x10 for GSM7 and data\_coding 0x18 for UCS2 When we receive flashSMS messages from our customers, they are sent to carriers as flashSMS; if the carrier does not support flashSMS, it is delivered as a normal SMS message.                                                                                                           |
| **Enquire-link**                | Minimum: 30 seconds / Maximum: 59 seconds.                                                                                                                                                                                                                                                                                                                    |
| **Concatenation**               | UDH 8-bit and 16-bit are supported / [UDH Headers](https://en.wikipedia.org/wiki/Concatenated_SMS).                                                                                                                                                                                                                                                           |
| **Default addr\_ton**           | 1                                                                                                                                                                                                                                                                                                                                                             |
| **Default addr\_npi**           | 1                                                                                                                                                                                                                                                                                                                                                             |
| **window size**                 | 10                                                                                                                                                                                                                                                                                                                                                            |
| **2way**                        | Supported                                                                                                                                                                                                                                                                                                                                                     |
| **SMPP bind type**              | Transceiver (Recommended). Separate transmit/receiver binds are also accepted.                                                                                                                                                                                                                                                                                |
| **SMPP system\_type**           | MovileSMSC                                                                                                                                                                                                                                                                                                                                                    |
| **SMPP source addr (senderID)** | When your service requires user responses (MO), the source address **must** match the system\_id, i.e., username. When your service does not require MOs, you can use anything in this field.                                                                                                                                                                 |
| **Max MO throughput**           | 80 per bind                                                                                                                                                                                                                                                                                                                                                   |
| **Max MT throughput**           | 80 per bind                                                                                                                                                                                                                                                                                                                                                   |
| **Server Timezone**             | UTC                                                                                                                                                                                                                                                                                                                                                           |
| **ID Format**                   | UUID                                                                                                                                                                                                                                                                                                                                                          |
| **Default validity\_period**    | 24 hours                                                                                                                                                                                                                                                                                                                                                      |

​

## Sent Status (Callback and DLR)

**1 - First Status (sent\_status - Sent Status = Callback)**

Status of delivery **to the carrier**, this is the first status we return, and all carriers have it.

| stat        | err | TLV (0x1403) | TLV (0x1404)                         | Meaning                                                                                                                                                                                                                         |
| ----------- | --- | ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ACCEPTD** | 000 | 2            | SENT\_SUCCESS                        | Successfully delivered to the carrier **(This is the status to be considered for billing purposes.)**                                                                                                                           |
| **EXPIRED** | 101 | 101          | EXPIRED                              | Expired before being delivered to the device.                                                                                                                                                                                   |
| **REJECTD** | 102 | 102          | CARRIER\_COMMUNICATION\_ERROR        | Communication error with the carrier.                                                                                                                                                                                           |
| **REJECTD** | 103 | 103          | REJECTED\_BY\_CARRIER                | The carrier has rejected the message.                                                                                                                                                                                           |
| **REJECTD** | 201 | 201          | NO\_CREDIT                           | The message limit set by your company’s administrator, for your account or subaccount, has been exceeded. Or, if your company uses the pre-paid credit model, it has run out.                                                   |
| **REJECTD** | 202 | 202          | INVALID\_DESTINATION\_NUMBER         | The destination number is invalid (Not a valid mobile number).                                                                                                                                                                  |
| **REJECTD** | 203 | 203          | BLACKLISTED                          | The destination number is blacklisted and has been manually entered by your company.                                                                                                                                            |
| **REJECTD** | 204 | 204          | DESTINATION\_BLOCKED\_BY\_OPTOUT     | The destination number has opted out and no longer wishes to receive messages from this subaccount. (This status is specifically for mobile marketing accounts).                                                                |
| **REJECTD** | 205 | 205          | DESTINATION\_MESSAGE\_LIMIT\_REACHED | The destination number has already received the maximum number of messages that one company can send, within a period of time. (This status is specifically for Mobile Marketing accounts, and this is a rule set by carriers). |
| **REJECTD** | 207 | 207          | INVALID\_MESSAGE\_TEXT               | The text of your message contains words that are not accepted by the carrier. These words can be profanity, or, if yours is a Mobile Marketing account, they can be major brands.                                               |
| **REJECTD** | 301 | 301          | INTERNAL\_ERROR                      | An error occurred in Wavy’s platform.                                                                                                                                                                                           |
| **UNKNOWN** | 301 | 301          | INTERNAL\_ERROR                      | An error occurred in Wavy’s platform.                                                                                                                                                                                           |

**2 - Second Status (delivered\_status - Delivery Report Callback)**

Status of delivery to **the device**, this is the second status we return and it only exists for cases where the first status above was successful, i.e., the message was successfully delivered to the carrier. In this status, we inform whether the message has been delivered to the device. Carriers Oi and Sercomtel do not have this second status level; for those carriers, the first status, i.e., whether the carrier has accepted your message, is the maximum information there is.

| stat        | err | TLV (0x1403) | TLV (0x1404)  | TLV (0x1405) | TLV (0x1406)       | Meaning                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | --- | ------------ | ------------- | ------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DELIVRD** | 000 | 2            | SENT\_SUCCESS | 4            | DELIVERED\_SUCCESS | Successfully delivered to the device.                                                                                                                                                                                                                                                                                                                          |
| **UNDELIV** | 104 | 2            | SENT\_SUCCESS | 104          | NOT\_DELIVERED     | The carrier has accepted the message, but was unable to deliver it to the device. Potential causes: Device is off or has no signal for a given period of time (usually 24 hours, but for some carriers, such as Vivo, this retry period is 8 hours). Number is valid, but inactive (some carriers only return this kind of error in this second status level). |

Statuses of delivery to the device, carrier, and MOs are queued if a connectivity problem occurs, but the time period is 8h; after this, you will no longer be able to obtain statuses through SMPP.

## TLS Proxy - Linux

The proxy is required if your connection is not made via VPN. As previously explained, the SMPP protocol does not have native TLS encryption; in this case we suggest the proxy below:

### HAProxy

### Installing the HAProxy

**Debian-Like**

In Debian-like distributions through the repository: sudo apt-get install haproxy

**RedHat-Like**

As there is currently no HAProxy package with TLS support already in the repository, you can download it from the official website: <http://www.haproxy.org/>

To the side, you will find a script for installation

sudo yum install wget gcc pcre-static pcre-devel -y

​

wget <http://www.haproxy.org/download/1.6/src/haproxy-1.6.3.tar.gz> -O \~/haproxy.tar.gz

tar xzvf \~/haproxy.tar.gz -C \~/

​

cd \~/haproxy-1.6.3

make TARGET=linux2628 USE\_LINUX\_TPROXY=1 USE\_ZLIB=1 USE\_REGPARM=1 USE\_OPENSSL=1 USE\_PCRE=1

sudo make install

sudo cp /usr/local/sbin/haproxy /usr/sbin/

sudo cp \~/haproxy-1.6.3/examples/haproxy.init /etc/init.d/haproxy

sudo chmod 755 /etc/init.d/haproxy

sudo mkdir -p /etc/haproxy

sudo mkdir -p /run/haproxy

sudo mkdir -p /var/lib/haproxy

sudo touch /var/lib/haproxy/stats

​

sudo useradd -r haproxy

sudo haproxy -vv

Setting up haproxy

global

&#x20;\# local2.\* /var/log/haproxy.log

&#x20;log 127.0.0.1 local2

​

&#x20;chroot /var/lib/haproxy

&#x20;pidfile /var/run/haproxy.pid

&#x20;ssl-server-verify none

&#x20;maxconn 4000

&#x20;user haproxy

&#x20;group haproxy

&#x20;daemon

&#x20;\# turn on stats unix socket

&#x20;stats socket /var/lib/haproxy/stats

​

resolvers dns

&#x20;nameserver google 8.8.8.8:53

&#x20;hold valid 1s

​

defaults

&#x20;log global

&#x20;option redispatch

&#x20;retries 3

&#x20;timeout http-request 10s

&#x20;timeout queue 1m

&#x20;timeout connect 10s

&#x20;timeout client 1m

&#x20;timeout server 1m

&#x20;timeout http-keep-alive 10s

&#x20;timeout check 10s

&#x20;maxconn 3000

​

frontend movile

&#x20;bind \*:2444

&#x20;mode tcp

&#x20;option tcplog

&#x20;use\_backend movile

​

backend movile

&#x20;mode tcp

&#x20;server smpp-messaging.movile.com smpp-messaging.wavy.global.com:2444 ssl resolvers dns check inter 15000

* Installing haproxy servers (red-hat / centos):

$sudo yum install -y openssl-devel haproxy

* Installing haproxy servers (debian / ubuntu)

$sudo apt-get install -y openssl-devel haproxy

* After installing, replace the entire content of the /etc/haproxy/haproxy.cfg file with the content to the side ->

**IMPORTANT:** Set your system (SMPP client) to use 127.0.0.1:2444 as destination address

## TLS Proxy - Windows

Setting up nginx

worker\_processes 2;

​

events {

&#x20;worker\_connections 1024;

}

​

stream {

&#x20;resolver 8.8.8.8 valid=1s;

&#x20;map $remote\_addr $backend {

&#x20;default smpp-messaging.wavy.global.com;

&#x20;}

&#x20;server {

&#x20;listen 2444;

&#x20;proxy\_pass $backend:2444;

&#x20;proxy\_ssl on;

&#x20;}

}

You can use nginx as a TLS proxy in Windows servers to encrypt the data

Download the version below (it is important to use this version, as older versions only resolve the name in the first request)

​<http://nginx.org/download/nginx-1.12.1.zip>​

Extract the .zip file to the desired location and replace the content of the conf/nginx.conf file with the data to the side

## SFTP API

### Connection Details

| ​                  | ​                                                            |
| ------------------ | ------------------------------------------------------------ |
| **Hostname**       | ftp-messaging.wavy.global                                    |
| **Port**           | 2222                                                         |
| **Protocol**       | SFTP (transfer over ssh, providing client-server encryption) |
| **Authentication** | username + password (provided by support)                    |
| **Portal**         | messaging.wavy.global                                        |

Your IPs must be allowed in Wavy’s firewalls. If you need to allow outgoing traffic in the firewall for port 2222, you must allow the DNS, or IPs 200.219.220.54, 200.189.169.53 and 45.236.179.22

## Sending Messages via SFTP

To trigger messages via SFTP, you need to generate a TXT file, with formatting following the example below:

**number;text;correlationId(optional);** **5511900000000;message 1;;** **5519900000000;message 2;;** **5521900000000;message 3;;** **EOF**

The name of the file to be sent must have the following format:

\<SUBACCOUNT\_ID>.\<DATE(YYYYMMDD)>.\<SEQUENCE> or \<SUBACCOUNT\_REFERENCE\_NAME>.\<DATE(YYYYMMDD)>.\<SEQUENCE>

Subaccounts (projects) can be created by the customer themself in the portal. If the nomenclature above is not followed, the messages will be sent by the customer’s default subaccount.

**Example:**

3486.20170101.01.txt or PROJECT1.20170101.01.txt

It is important to follow the set nomenclature so the messages can be discounted from the correct subaccount.

Afterwards, the file must be sent to the sftp server in the upload directory. The file will be moved to the success directory after it is done; if any error occurs, the file will be moved to the error directory.

## Number Validation API

API for validating phone numbers, where we return the current carrier of queried numbers (including ported numbers), or whether the number is invalid, i.e., it is not a mobile number.

IMPORTANT: Number lookup queries have a differentiated fee from SMS deliveries; before running a query, check with the head of the commercial team

### Authentication

To send messages and run queries in our API, you need to authenticate using a combination of username or email and a token.

| Field               | Details                                                                     | Data Type |
| ------------------- | --------------------------------------------------------------------------- | --------- |
| UserName            | Your username or email                                                      | String    |
| AuthenticationToken | Your authentication token. Check here and read username descriptions below. | String    |

### Connection Details

| ​                  | ​                         |
| ------------------ | ------------------------- |
| **Hostname**       | api-messaging.wavy.global |
| **APIs**           | /v1/carrier/lookup        |
| **Port**           | 443 (https)               |
| **Protocol**       | HTTPS (TLS encryption)    |
| **Authentication** | username + token          |
| **Portal**         | messaging.wavy.global     |

​

## HTTP Request via POST Method

curl --request POST \\

&#x20;\--url <https://api-messaging.wavy.global/v1/carrier/lookup> \\

&#x20;\--header 'authenticationtoken: \<authenticationtoken>' \\

&#x20;\--header 'username: \<username>' \\

&#x20;\--header 'Content-Type: application/json' \\

&#x20;\--data '{

&#x20;"destinations": \["+55(19)997712322", "5519997712322", "2312312"]

}'

POST <https://api-messaging.wavy.global/v1/carrier/lookup> Content-Type: application/json

To run a query, just add a json to the request body with the number array. You can run a query using the +55(19)999999999 and 5519999999999 formats

### Query Response

Call response in JSON format

{

&#x20;"id": "aadb5130-7dd7-11e7-baac-a6aabe61edb5",

&#x20;"destinations": \[

&#x20;{

&#x20;"destination": "5519997712322",

&#x20;"active": true,

&#x20;"carrier": {

&#x20;"name": "VIVO",

&#x20;"countryCode": "BR"

&#x20;}

&#x20;},

&#x20;{

&#x20;"destination": "5519997712322",

&#x20;"active": true,

&#x20;"carrier": {

&#x20;"name": "VIVO",

&#x20;"countryCode": "BR"

&#x20;}

&#x20;},

&#x20;{

&#x20;"destination": "2312312",

&#x20;"active": false,

&#x20;"carrier": {

&#x20;"name": "UNKNOWN"

&#x20;}

&#x20;}

&#x20;]

}

The last number in the example is an invalid number to shown now the query returns the JSON in such cases.

The batch query response will contain a JSON file with individual information on each queried number:

| Field            | Details                                                                                                                                | Type                  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **id**           | UUID generated for this batch                                                                                                          | String                |
| **destinations** | This field is an array with the responses of the individual batch queries, it contains the id and correlationId of each queried number | IndividualResponse\[] |
| **destination**  | Queried phone number                                                                                                                   | Long                  |
| **active**       | number's status with the carrier (currently only checks whether the number belongs to the carrier, not active / in use)                | Boolean               |
| **carrier**      | Carrier and country to which the queried number belongs                                                                                | array\[]              |
| **name**         | Carrier name                                                                                                                           | String                |
| **countryCode**  | Country Code                                                                                                                           | String                |

## Accents & Special Characters

Messages containing **only** characters in the table below are charged for every 160 characters. If your message has **one or more** characters that are not in the table below, you will be charged for every 70 characters, as specified in the protocol of the carriers’ network.

| ​     | ​  | ​ | ​ | ​ | ​ | ​ | ​  | ​  | ​ | ​ | ​  |
| ----- | -- | - | - | - | - | - | -- | -- | - | - | -- |
| Space | (  | 0 | 8 | @ | H | P | X  | \` | h | p | x  |
| !     | )  | 1 | 9 | A | I | Q | Y  | a  | i | q | y  |
| “     | \* | 2 | : | B | J | R | Z  | b  | j | r | z  |
| #     | +  | 3 | ; | C | K | S | {  | c  | k | s | \~ |
| $     | ,  | 4 | < | D | L | T | \\ | d  | l | t | ​  |
| %     | -  | 5 | = | E | M | U | }  | e  | m | u | ​  |
| &     | .  | 6 | > | F | N | V | ^  | f  | n | v | ​  |
| ‘     | /  | 7 | ? | G | O | W | \_ | g  | o | w | ​  |

Notes:

• Please request our support team to enable the use of accents and special characters.

• If the destination carrier does not accept accents and characters (Sercomtel), our platform automatically replaces them for our customers, such as: á to a, é to e, etc.

## Long Texts (Concatenation)

The protocol used in the carriers’ network has 70- or 160-character limits for messages with or without **special characters**, respectively. But you can send longer messages using concatenation, where the device regroups messages upon receipt.

For customers integrated via HTTPS, SFTP, or MQ, there are no additional indicators in order to activate concatenation, just send the long message text in a single request.

For customers integrated via SMPP, you must use the concatenation feature with indicators in the header (UDH), [LINK](https://en.wikipedia.org/wiki/Concatenated_SMS).

It is worth noting that, despite appearing on the device as a single long message, messages still travel through carriers’ networks individually, and, in this case, we continue being charged and charging individually for every 63 or 160 characters (depending on the **characters** used). Reminding that, when you use concatenation, part of the characters (70 or 160) are used by the header header.

Note: In cases of carriers that do not support the concatenation feature (e.g.: Sercomtel), Wavy sends the messages separately, without concatenating, and includes order indicators automatically for our customers. E.g.:

​


# Email API

Technical Documentation: Email API.

## Email API

This API allows you to automatize both single and bulk message requests and the retrieval of sent status through its endpoints. It uses HTTP protocol with TLS and accepts GET requests with query string parameters and POST requests with [JSON](http://json.org/%22%20/t%20%22_blank) parameters.

## User Authentication

In order to successfully use our API, you are required to present a valid username - or email - and the associated token authentication. While creating the request, you have to provide the following parameters on the headers:

| Field               | Details                                                                                                                         | Data Type |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------- |
| UserName            | Your username or email                                                                                                          | String    |
| AuthenticationToken | Your authentication token. Get yours [here](https://messaging.movile.com/messaging/user/api_configuration%22%20/t%20%22_blank)​ | String    |

## Connection Details

| ​                  | ​                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------- |
| **Hostname**       | api-messaging.wavy.global                                                                    |
| **APIs**           | SendEmail /v1/email/send SearchEmail /v1/email/status/search ListEmail /v1/email/status/list |
| **Port**           | 443 (https)                                                                                  |
| **Protocol**       | HTTPS (TLS encryption)                                                                       |
| **Authentication** | username + token                                                                             |

## SendEmail

## SendEmail request

​

curl --request POST \\

&#x20;\--url <https://api-messaging.wavy.global/v1/email/send> \\

&#x20;\--header 'authenticationtoken: \<authenticationtoken>' \\

&#x20;\--header 'content-type: application/json' \\

&#x20;\--header 'username: \<username>' \\

&#x20;\--data '{

&#x20;"fromEmail": "<notification@movile.com>",

&#x20;"fromName": "Notifications",

&#x20;"replyTo": "<replyTo@movile.com>",

&#x20;"subject": "Marketing e-mail",

&#x20;"campaignAlias": "MyCampaign",

&#x20;"recipients": \[{

&#x20;"correlationId": "1234",

&#x20;"emailAddress": "<recipient-1@wavy.global>",

&#x20;"emailName": "Recipient-1",

&#x20;"extraInfo": "Extra e-mail info1",

&#x20;"substitutionData": {

&#x20;"name": "Recipient-1"

&#x20;}

&#x20;},

&#x20;{

&#x20;"correlationId": "567",

&#x20;"emailAddress": "<recipient-2@wavy.global>",

&#x20;"emailName": "Recipient-2",

&#x20;"extraInfo": "Extra e-mail info2"

&#x20;}

&#x20;],

&#x20;"emailHtml": "\<html> Hi, {{name}}, this is the email HTML body \</html>",

&#x20;"emailText": "Email text body",

&#x20;"substitutionData": {

&#x20;"name": "Recipient-1"

&#x20;},

&#x20;"attachments": \[{

&#x20;"data": "Q29uZ3JhdHVsYX2FuIGJhc2U2NCBkZWNvZGUh",

&#x20;"name": "billing.pdf",

&#x20;"type": "application/pdf"

&#x20;}]

}'

​

POST <https://api-messaging.wavy.global/v1/email/send> Content-Type: application/json

The request body must contain a JSON object in which information are enveloped with the following fields. Fields with a \* are required.

| Field            | Details                                                                                                                                                                                                                                                                                                          | Type   |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| fromEmail\*      | Email sender’s address. E.g. <notification@domain.com>                                                                                                                                                                                                                                                           | String |
| fromName\*       | Email sender’s name. E.g. Notification.                                                                                                                                                                                                                                                                          | String |
| replyTo          | Email address used to compose the email’s “Reply-To” header.                                                                                                                                                                                                                                                     | String |
| subject          | Email subject line.                                                                                                                                                                                                                                                                                              | String |
| campaignAlias    | Campaign name.                                                                                                                                                                                                                                                                                                   | String |
| recipients\*     | Array of recipients.                                                                                                                                                                                                                                                                                             | ​      |
| correlationId    | Identifier generated by the customer.                                                                                                                                                                                                                                                                            | String |
| emailAddress\*   | Valid email address of a recipient.                                                                                                                                                                                                                                                                              | String |
| emailName        | Name of the recipient, associated with the emailAddress                                                                                                                                                                                                                                                          | String |
| extraInfo        | Any extra info set by the user when the email was sent.                                                                                                                                                                                                                                                          | String |
| emailHTML        | HTML content for the email’s text/html MIME part.                                                                                                                                                                                                                                                                | String |
| emailText        | Text content for the email’s text/plain MIME part.                                                                                                                                                                                                                                                               | String |
| substitutionData | Mapping of tags, within {{}} marks, that should be replaced on html body.                                                                                                                                                                                                                                        | ​      |
| attachments      | Array of attachment files.                                                                                                                                                                                                                                                                                       | ​      |
| data             | The content of the attachment as a Base64 encoded string. The string should not contain \r\n line breaks.                                                                                                                                                                                                        | String |
| name             | The filename of the attachment (for example, document.pdf).                                                                                                                                                                                                                                                      | String |
| type             | The MIME type of the attachment; e.g., text/plain, image/jpeg, audio/mp3, video/mp4, application/msword, application/pdf, etc., including the charset parameter (ex: text/html; charset=“UTF-8”) if needed. The value will apply as-is to the Content-Type header of the generated MIME part for the attachment. | String |

## SendEmail response

{

&#x20;"id": "abcd-1234-efgh-5678-ijkl-9999",

&#x20;"recipients": \[

&#x20;{

&#x20;"correlationId": "5678",

&#x20;"id": "9i9j9k9l-5e6f7g8h-0i0j0k0l-1a2b3c4d"

&#x20;},

&#x20;{

&#x20;"correlationId": "5678",

&#x20;"id": "9i9j9k9l-5e6f7g8h-0i0j0k0l-1a2b3c4d"

&#x20;}

&#x20;]

}

The response body will contain a JSON object with tracking information related to the email request:

| Field         | Details                                                                   | Type   |
| ------------- | ------------------------------------------------------------------------- | ------ |
| id            | UUID generated for this email request.                                    | String |
| correlationId | The same correlationId from the request.                                  | String |
| recipients    | Tag corresponding to an id and correlationId for every request recipient. | ​      |

## SearchEmailStatus request

Example:

{

&#x20;"correlationIds": \["1234", "5678", "7890"],

&#x20;"ids": \["1234-5678-9asd-fghj", "qwer-1234-asdf-0987",

&#x20;"zxcv-4567-ghjk-6789"],

&#x20;"startDate": "2017-04-27T10:00:00Z",

&#x20;"endDate": "2017-04-28T10:00:00Z"

}

POST <https://api-messaging.wavy.global/v1/email/status/search> Content-Type: application/json

Retrieves information on a previously sente mail, given its IDs, correlationIds, and a date interval.

| Field          | Details                                                                                                                                                               | Type   |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| ids\*          | UUID generated for this email. Must correspond to the respective correlationId.                                                                                       | String |
| correlationIds | The same correlationId from the request. Must correspond to the respective id.                                                                                        | String |
| startDate      | Start date for search interval. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601%22%20/t%20%22_blank)​ | String |
| endDate        | End date to search interval. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601%22%20/t%20%22_blank)​    | String |

## ListEmailStatus request

POST <https://api-messaging.wavy.global/v1/email/status/list> Content-Type: application/json

Retrieves information on a previously sente mail, considering its user and token. This method returns all emails that haven’t yet been checked.

## List and Search EmailStatus response

\[{

&#x20;"recipient": {

&#x20;"id": "1234-5678-9asd-fghj",

&#x20;"correlationId": "1234",

&#x20;"emailAddress": "<recipient-1@movile.com>",

&#x20;"emailName": "Recipient-1",

&#x20;"extraInfo": "Extra e-mail info1"

&#x20;},

&#x20;"fromEmail": "<notificaction@movile.com>",

&#x20;"fromName": "Notifications",

&#x20;"createdAt": 12345678910,

&#x20;"createdDate": "2017-04-28T13:10:10.336Z",

&#x20;"sent": true,

&#x20;"sentStatusCode": 2,

&#x20;"sentStatus": "SENT\_SUCCESS",

&#x20;"sentAt": 9638527410,

&#x20;"sentDate": "2017-04-28T13:10:10.336Z",

&#x20;"delivered": true,

&#x20;"deliveredStatusCode": 2,

&#x20;"deliveredStatus": "SENT\_SUCCESS",

&#x20;"deliveredAt": 9876543210,

&#x20;"deliveredDate": "2017-04-28T13:10:10.336Z",

&#x20;"opened": true,

&#x20;"openedAt": 9638527410,

&#x20;"openedDate": "2017-04-28T13:10:10.336Z",

&#x20;"clicked": true,

&#x20;"clickedAt": 741258963,

&#x20;"clickedDate": "2017-04-28T13:10:10.336Z",

&#x20;"campaignId": 1,

&#x20;"campaignAlias": "demo1"

}, {

&#x20;"recipient": {

&#x20;"id": "qwer-1234-asdf-0987",

&#x20;"correlationId": "5678",

&#x20;"emailAddress": "<recipient-1@movile.com>",

&#x20;"emailName": "Recipient-1",

&#x20;"extraInfo": "Extra e-mail info1"

&#x20;},

&#x20;"fromEmail": "<notificaction@movile.com>",

&#x20;"fromName": "Notifications",

&#x20;"createdAt": 12345678910,

&#x20;"createdDate": "2017-04-28T13:10:10.336Z",

&#x20;"sent": true,

&#x20;"sentStatusCode": 2,

&#x20;"sentStatus": "SENT\_SUCCESS",

&#x20;"sentAt": 9876543210,

&#x20;"sentDate": "2017-04-28T13:10:10.336Z",

&#x20;"delivered": true,

&#x20;"deliveredStatusCode": 2,

&#x20;"deliveredStatus": "SENT\_SUCCESS",

&#x20;"deliveredAt": 9876543210,

&#x20;"deliveredDate": "2017-04-28T13:10:10.336Z",

&#x20;"opened": true,

&#x20;"openedAt": 9638527410,

&#x20;"openedDate": "2017-04-28T13:10:10.336Z",

&#x20;"clicked": true,

&#x20;"clickedAt": 741258963,

&#x20;"clickedDate": "2017-04-28T13:10:10.336Z",

&#x20;"campaignId": 1,

&#x20;"campaignAlias": "demo1"

}, {

&#x20;"recipient": {

&#x20;"id": "zxcv-4567-ghjk-6789",

&#x20;"correlationId": "0987",

&#x20;"emailAddress": "<recipient-1@movile.com>",

&#x20;"emailName": "Recipient-1",

&#x20;"extraInfo": "Extra e-mail info1"

&#x20;},

&#x20;"fromEmail": "<notificaction@movile.com>",

&#x20;"fromName": "Notifications",

&#x20;"createdAt": 12345678910,

&#x20;"createdDate": "2017-04-28T13:10:10.336Z",

&#x20;"sent": true,

&#x20;"sentStatusCode": 2,

&#x20;"sentStatus": "SENT\_SUCCESS",

&#x20;"sentAt": 9876543210,

&#x20;"sentDate": "2017-04-28T13:10:10.336Z",

&#x20;"delivered": true,

&#x20;"deliveredStatusCode": 2,

&#x20;"deliveredStatus": "SENT\_SUCCESS",

&#x20;"deliveredAt": 9876543210,

&#x20;"deliveredDate": "2017-04-28T13:10:10.336Z",

&#x20;"opened": true,

&#x20;"openedAt": 9638527410,

&#x20;"openedDate": "2017-04-28T13:10:10.336Z",

&#x20;"clicked": true,

&#x20;"clickedAt": 741258963,

&#x20;"clickedDate": "2017-04-28T13:10:10.336Z",

&#x20;"campaignId": 1,

&#x20;"campaignAlias": "demo1"

}]

Retrieves information on a previously sent email, considering its user and token. This method returns all emails not previously queried.

| Field               | Details                                                                                                                                                        | Type    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| emailStatus         | Block for each email information.                                                                                                                              | ​       |
| recipient           | Block for recipient email information.                                                                                                                         | ​       |
| id                  | The same id from the request.                                                                                                                                  | ​       |
| correlationId       | The same correlationId from the request.                                                                                                                       | ​       |
| emailAddress        | Email address of the recipient.                                                                                                                                | ​       |
| emailName           | Name of the recipient, associated with the emailAddress.                                                                                                       | ​       |
| extraInfo           | Any extra information.                                                                                                                                         | ​       |
| fromEmail           | Email sender’s address. E.g. <notification@domain.com>                                                                                                         | ​       |
| fromName            | Email sender’s name. E.g. Notification, Not reply, etc.                                                                                                        | ​       |
| createdAt           | When the email was created. It is an Epoch Date.                                                                                                               | Long    |
| createdDate         | When the message was created. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601)​                | ​       |
| sent                | Flag indicating if the email was sent.                                                                                                                         | Boolean |
| sentStatusCode      | Sent status code. Check Sent Status Codes for more information.                                                                                                | Long    |
| sentStatus          | Sent status.                                                                                                                                                   | String  |
| sentAt              | When the email was sent. It is an Epoch Date.                                                                                                                  | Long    |
| sentDate            | When the email was sent. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601)​                     | ​       |
| delivered           | Flag indicating if the email was delivered to the recipient.                                                                                                   | Boolean |
| deliveredStatusCode | Delivered status code. Check Delivered Status Codes for more information.                                                                                      | Long    |
| deliveredStatus     | Delivered status.                                                                                                                                              | String  |
| deliveredAt         | When the email was delivered. It is an Epoch Date.                                                                                                             | Long    |
| deliveredDate       | When the email was delivered. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601)​                | ​       |
| open                | Flag indicating if the email was opened by the recipient.                                                                                                      | Boolean |
| openedAt            | When the email was opened. It is an Epoch Date.                                                                                                                | Long    |
| openedDate          | When the email was opened. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601)​                   | ​       |
| clicked             | Flag indicating if the email was clicked by the recipient.                                                                                                     | Boolean |
| clickedAt           | When the email was clicked. It is an Epoch Date.                                                                                                               | Long    |
| clickedDate         | When the email was clicked by the recipient. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601)​ | ​       |
| campaignId          | Campaign identifier.                                                                                                                                           | Long    |
| campaignAlias       | Campaign name.                                                                                                                                                 | String  |

## Status Codes

## Sent Status Codes

A sent status code represents the status of a message that goes through our system and is sent to the carrier.

### Success codes

| ​ | ​             | ​                         |
| - | ------------- | ------------------------- |
| 2 | SENT\_SUCCESS | Sent to Wavy successfully |

### Wavy error codes

| ​   | ​               | ​                   |
| --- | --------------- | ------------------- |
| 301 | INTERNAL\_ERROR | Wavy internal error |

## Delivered Status Codes

A delivered status code represents the status report we receive from the server about the email.

### Success codes

| ​ | ​                  | ​                                |
| - | ------------------ | -------------------------------- |
| 3 | DELIVERED\_SUCCESS | Delivered to server successfully |

### Carrier error codes

| ​   | ​              | ​                                                |
| --- | -------------- | ------------------------------------------------ |
| 103 | NOT\_DELIVERED | Email accepted but has not delivered the e-mail. |

## Opened Status Codes

An opened status code represents the email opened by the customer.

### Success codes

| ​ | ​               | ​                                |
| - | --------------- | -------------------------------- |
| 4 | OPENED\_SUCCESS | Delivered to server successfully |

### Carrier error codes

| ​   | ​           | ​                                                 |
| --- | ----------- | ------------------------------------------------- |
| 104 | NOT\_OPENED | Email accepted but has not opened by the customer |

## Clicked Status Codes

A clicked status code represents the status report when the customer clicked over the email. |||| |–|–|–| |5|CLICKED\_SUCCESS|Clicked by the customer successfully|

### Carrier error codes

| ​   | ​            | ​                                                  |
| --- | ------------ | -------------------------------------------------- |
| 104 | NOT\_CLICKED | Email accepted but has not clicked by the customer |


# Fallback API

hnical Documentation: Fallback API

This API allows you to automatize messaging using many different channels (SMS, email and voice) in the fallback system (messaging is structured in steps and, if one of those steps fails, the following specified step will be executed).

It uses HTTP protocol with TLS and accepts the POST method with parameters via [JSON](http://json.org/).

## Authentication

To send messages and run queries in our API, it is necessary to authenticate using a combination of either username or email and a token.

| Field               | Details                                                                                                                                      | Data Type |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| UserName            | Your username or email                                                                                                                       | String    |
| AuthenticationToken | Your authentication token. Check [here](https://messaging.movile.com/messaging/user/api_configuration) and read username descriptions below. | String    |

## Connection Details

| ​                  | ​                                 |
| ------------------ | --------------------------------- |
| **Hostname**       | api-messaging.wavy.global         |
| **APIs**           | Individual messages /v1/omni/send |
| **Port**           | 443 (https)                       |
| **Protocol**       | HTTPS (TLS encryption)            |
| **Authentication** | username + token                  |
| **Portal**         | messaging.wavy.global             |

## Encoding

The encoding standard used is UTF-8, all message contents must follow this standard.

You can escape characters if you wish or encode using HTTP format

You can see some encoding examples to the side

***“messageText”:“A combinação foi perfeita :)”***

Or you can escape characters if you wish:

***“messageText”:“A combina\u00e7\u00e3o foi perfeita :)”***

## Messaging via POST Method

```
curl --request POST \
 --url 'http://{{channel-api-base-url}}/v1/omni/send' \
 --header 'authenticationtoken: 56xdJ3zs_ses51KyGM1b8py1CxCsba2sTT334hrs' \
 --header 'content-type: application/json' \
 --header 'username: bruno.azenha@movile.com' \
 --data '{
 "contacts":
 [
 {
 "contactInfo": {
 "phone1": "5516981562829",
 "phone2": "5516981562829",
 "email": "azenha.bruno@gmail.com",
 "recipientName": "Bruno Azenha"
 }
 },
 {
 "contactInfo": {
 "phone1": "0",
 "phone2": "5511982994265",
 "email": "bruno.farias@movile.com",
 "recipientName": "Bruno Farias"
 }
 }
 ],
 "template":
 {
 "campaignAlias": "Campaign Alias",
 "steps":
 [
 {
 "type": "MT",
 "destinationField": "phone1",
 "messageText": "First message.",
 "flashSms": false
 },
 {
 "type": "VOICE",
 "destinationField": "phone2",
 "ttsMessage": "This is the third message",
 "timeout": 3
 },
 {
 "type": "MT",
 "destinationField": "phone1",
 "messageText": "Second Message as Flash",
 "flashSms": true
 },
 {
 "type": "EMAIL",
 "destinationField": "email",
 "recipientName": "recipientName",
 "subject": "Third message",
 "replyTo": "reply.to@domain.com",
 "fromEmail": "email@domain.com",
 "fromName": "Your name",
 "emailText": "Email content as simple plain text",
 "emailHtml": "Email content as HTML"
 }
 ]
 }
}'
```

POST <https://api-messaging.wavy.global/v1/omni/send> Content-Type: application/json

The request body must contain the JSON object with information according to the fields below:

\* Required field

| Field                | Details                                                                                      | Type     |
| -------------------- | -------------------------------------------------------------------------------------------- | -------- |
| **contacts\***       | Array of contacts to which delivery attempts will be made                                    | Array\[] |
| **contactInfo\***    | Text of the message that will be sent                                                        | String   |
| **phone**            | Phone number to which the message will be sent (including country code). E.g.: 5511900000000 | Long     |
| **email**            | Email of the recipient                                                                       | String   |
| **emailName**        | ​                                                                                            | ​        |
| **template\***       | Template with information on the flow that will be executed                                  | Array\[] |
| **campaignAlias**    | Fallback identification                                                                      | String   |
| **Steps\***          | Steps to be executed when sending                                                            | Array\[] |
| **type\***           | Type of message (Email, MT, Voice)                                                           | String   |
| **destinationField** | Information created in the contactInfo field should be relayed                               | String   |
| **subject\***        | Used when sending emails, subject of the email to be sent                                    | String   |
| **fromEmail\***      | Source email                                                                                 | String   |
| **emailHTML\***      | HTML content to be relayed in the body of the email                                          | String   |
| **messageText**      | Content of the message for sending SMS                                                       | String   |
| **ttsMessage**       | Check phone\*\*\*\*\*\*                                                                      | ​        |

**IMPORTANT!**

**For each username, there is a unique authentication token**

## Request responses

The response to bulk messaging will contain a JSON file with the information required for tracking, an id will be created for the entire batch and an individual id and correlationId will be created for each message:

| Field | Details                     | Type   |
| ----- | --------------------------- | ------ |
| id    | UUID generated for messages | String |


# WhatsApp API

## WhatsApp API

Technical Documentation: WhatsApp API

### WhatsApp API

This documentation provides information on how your application can send WhatsApp messages via API using the Wavy Messaging platform.

Here you will also find information on **Webhooks,** which are HTTP call returns set by the user that are triggered by specific events. Whenever a trigger event occurs, Wavy’s API will collect the data and immediately send a notification (HTTP request) to the URL chosen by our customer, updating the status of messages sent or letting you know when you receive a message.

Wavy Messaging’s API allows you to send single or bulk messages.

The API has REST integration, using HTTP protocol with TLS, supporting the POST method with parameters sent in JSON format.

### **Prerequisites**

1. To use Wavy Messaging’s API, first you need to have an active account on the Wavy Messaging platform. Refer to our documentation on [Account & Settings](https://docs.wavy.global/getting-started/wavy-messaging-platform/conta-e-configuracoes) for more information on how to follow this procedure.
2. You must also have a valid username and token associated with this account. Learn how to create your username in our [Adding Users](https://docs.wavy.global/permissoes/subcontas-e-usuarios#adicionar-usuarios) guide.
3. With the above credentials, you can already start using Wavy Messaging’s API.

​

### **Connection Details**

| ​                  | ​                         |
| ------------------ | ------------------------- |
| **Hostname**       | api-messaging.wavy.global |
| **Port**           | 443 (https)               |
| **Protocol**       | HTTPS (TLS encryption)    |
| **Authentication** | username + token          |
| **Encoding**       | UTF-8                     |

## **Making Calls to Wavy Messaging’s API**

To make your first calls, we recommend using the “[Postman](https://www.postman.com/downloads/)” application with requests in JSON format instead of starting out already writing code in other languages.

**Note: In order to send test messages, you need to have an approved message template in your WhatsApp Business account. Refer to our documentation on** [**Creating WhatsApp Message Templates**](https://docs.wavy.global/whatsapp/cadastro-de-template) **to create your first templates.**

If you do not yet have any approved message templates, you can still send test messages as long as the recipient interacts with the source number. This way, a customer service window will be activated. It allows you to send any type of message within a 24-hour window. If your message arrives, it means your request to Wavy Messaging’s API was successful. If not, check your Webhook for notifications that could indicate any issues.

**Messages:**

Calls to Wavy Messaging’s API are sent to <https://api-messaging.wavy.global/v1/whatsapp/send> in POST format regardless of message type, but the content of the JSON message’s body varies for each type of message.

The authentication fields in the header will also follow the same format regardless of message type:

POST /v1/whatsapp/send HTTP/1.1 Host: api-messaging.movile.com UserName: user\_name AuthenticationToken: aaaaaa-bbbbbbbbbbbbbXXXXX12 Content-Type: application/json

### **Sending a Template**

### **Destinations**

| **Name**         | Required | Description                                     |
| ---------------- | -------- | ----------------------------------------------- |
| **destinations** | Yes      | Details on sent and destination identifiers     |
| **message**      | Yes      | Details on the MESSAGE object that will be sent |

### **Destination**

| Name              | Required | ​ | Description                                                                                                                                                       |
| ----------------- | -------- | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **correlationId** | No       | ​ | Id set by the customer that will be returned in the message status (callback). You can use this id to track sent messages in a customized manner.                 |
| **destination**   | Yes      | ​ | Phone number that will receive the message (country code (55 for Brazil) and area code are required). Examples: 5519900001111, +5519900001111, +55(19) 900001111. |

### **Message**

| Name         | ​ | Required | ​ | Description                                                                                                                                           |
| ------------ | - | -------- | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ttl**      | ​ | No       | ​ | Time to live in days. It sets the maximum number of days in which the message should be delivered. Valid from 1 to 30. Default value is 7 if not set. |
| **template** | ​ | Yes      | ​ | Details on the TEMPLATE object that will be sent                                                                                                      |

### **Template**

| **Name**         | ​ | Required                                            | ​ | Description                                                                                                                                                                                                           |
| ---------------- | - | --------------------------------------------------- | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **namespace**    | ​ | Yes                                                 | ​ | ID of the namespace that will be used. **NOTE:** The namespace and element\_name parameters must match the Business Manager with which the source number is associated, otherwise the message will fail when sending. |
| **elementName**  | ​ | Yes                                                 | ​ | Name of the registered and approved template.                                                                                                                                                                         |
| **header**       | ​ | Yes, when the Template has parameters in the header | ​ | Header objects with their parameters                                                                                                                                                                                  |
| **languageCode** | ​ | Yes                                                 | ​ | Name of the registered and approved template.                                                                                                                                                                         |

### **Header**

| **Name**    | Required | Description                                                                                             |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------- |
| **title**   | Optional | Title must have no more than 60 characters                                                              |
| **element** | Yes      | <p>Options:</p><p>text (default),</p><p>image,</p><p>audio,</p><p>document,</p><p>hsm,</p><p>video.</p> |

### **Element**

| **Name**    | ​ | Required | ​ | Description                               |
| ----------- | - | -------- | - | ----------------------------------------- |
| **url**     | ​ | Yes      | ​ | Media URL. Use only with HTTP/HTTPS URLs. |
| **type**    | ​ | Yes      | ​ | Type of media (JPEG, MP3, PDF, etc.)      |
| **caption** | ​ | Yes      | ​ | Name of media                             |

​

## **Webhooks**

Webhooks (or callbacks) are HTTP call returns set by the user that are triggered by specific events. Whenever a trigger event occurs, Wavy’s API will collect the data and immediately send a notification (HTTP request) to the URL chosen by the customer updating the status of messages sent or letting you know when you receive a message.

When your customer sends you a message, Wavy Messaging’s API will send a POST HTTP request notification to the **Webhook**’s URL with the details.

It is important that your **Webhook** returns a 200 OK HTTPS response to notifications (within 200 ms or asynchronously). Otherwise, Wavy Messaging’s API will consider this notification to have failed and will try again after some delay.

**Important: The URL where you will receive Webhooks must be set up by our support team.**

### **General Format of a Webhook**

| **Name**     | Object Content                 |
| ------------ | ------------------------------ |
| **messages** | Incoming message notifications |
| **statuses** | Message status updates         |

### Status

| Status                 | Description                           | WhatsApp Equivalent for Mobile Devices |
| ---------------------- | ------------------------------------- | -------------------------------------- |
| **SENT\_SUCCESS**      | Message received by WhatsApp’s server | One check mark                         |
| **DELIVERED\_SUCCESS** | Message delivered to the recipient    | Two check marks                        |
| **READ\_SUCCESS**      | Message read by the recipient         | Two blue check marks                   |

### Errors

| **HTTP Code** | **Description**                              |
| ------------- | -------------------------------------------- |
| **2xx**       | **Success**                                  |
| **200**       | **Success (OK)**                             |
| **201**       | **Successfully Created (For POST requests)** |
| **302**       | **Found**                                    |
| **4xx**       | **Client Errors**                            |
| **400**       | **Bad Request**                              |
| **401**       | **Unauthorized**                             |
| **403**       | **Forbidden**                                |
| **404**       | **Not Found**                                |
| **405**       | **Method Not Allowed**                       |
| **412**       | **Precondition Failed**                      |
| **420**       | **Message is Rate Limited**                  |
| **429**       | **Too Many Requests**                        |
| **5xx**       | **Server Errors**                            |
| **500**       | **Internal Server Error**                    |
| **504**       | **Timeout**                                  |

### Other Statuses

| Sent Code | Delivery Code | Status                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------- | ------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 102       | ​             | CARRIER COMMUNICATION ERROR      | Error in uploading media to WhatsApp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 103       | ​             | REJECTED\_BY\_CARRIER            | A databank error has occurred                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2         | 101           | EXPIRED                          | Message expired                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 2         | 104           | NOT\_DELIVERED                   | <p>Potential Causes:</p><p>Limit reached -too many attempts to send messages, or failure to send message because the destination phone number is part of an experiment, or the template structure does not exist, or failure to send message because the destination number is outside the 24h service window to receive messages freely, or an error occurred when uploading media (unknown error),</p><p>or failure to send message because your account is ineligible on Facebook Business Manager,</p><p>or there was a temporary upload failure. Please try again later.</p> |
| 202       | ​             | INVALID\_DESTINATION\_NUMBER     | Invalid WhatsApp contact                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 204       | ​             | DESTINATION\_BLOCKED\_BY\_OPTOUT | Destination blocked by Opt-Out                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 206       | ​             | INVALID\_MESSAGE\_LENGTH         | Message is too long                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 207       | ​             | INVALID\_MESSAGE\_TEXT           | Invalid parameter value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 209       | ​             | INVALID\_CONTENT                 | Invalid type of UNKNOWN message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 210       | ​             | INVALID\_SESSION                 | Session or service window is not open and no fallback Template is set up                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 311       | ​             | INTERNAL\_ERROR                  | Unable to verify WhatsApp API contacts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### **Messages (MO)**

When a customer sends you a message, Wavy Messaging’s API will send a POST HTTP request to the **Webhook’s URL with the details**.

It is important that your **Webhook** returns a 200 OK HTTPS response to notifications (within 200 ms or asynchronously). Otherwise, Wavy Messaging’s API will consider this notification to have failed and will try again after some delay.

**Important: The URL where you will receive Webhooks must be set up by our support team.**

## Common HTTP Status Code Responses

### Successful Request Response (200)

{

&#x20;"Id": "5efc3581-b8e8-11e7-9895-a6aabe61edb5",

&#x20;"destination": \[{

&#x20;"id": "5efc3581-b8e8-11e7-9895-a6aabe61edb5",

&#x20;"correlationId": "MyCorrelationId",

&#x20;"destination": "5519900001111."

}]

}

If your request is successfully run, a list of destinations with the generated uuids will be returned:

### Authentication Error Response (401)

{

&#x20;"errorCode": 401,

&#x20;"errorMessage": "Authentication Error: No user was found with this combination of username and Authentication token."

}

If a problem occurs with authentication, the following message will be returned:

### Status Update Callback

Example

{

&#x20;"total": 1,

&#x20;"data": \[

&#x20;{

&#x20;"id": "8995c40f-1c3a-48d0-98ee-bbc603622a91",

&#x20;"correlationId": "...",

&#x20;"destination": "5519900000000",

&#x20;"origin": "5519900000000",

&#x20;"campaignId": 100,

&#x20;"campaignAlias": "...",

&#x20;"flowId": "...",

&#x20;"extraInfo": "...",

&#x20;"sent": true,

&#x20;"sentStatusCode": 1,

&#x20;"sentStatus": "sent status",

&#x20;"sentDate": "2017-12-18T17:09:31.891Z",

&#x20;"sentAt": 1513616971891,

&#x20;"delivered": true,

&#x20;"deliveredStatusCode": 1,

&#x20;"deliveredStatus": "delivered status",

&#x20;"deliveredDate": "2017-12-18T17:09:31.891Z",

&#x20;"deliveredAt": 1513616971891,

&#x20;"read": true,

&#x20;"readDate": "2017-12-18T17:09:31.891Z",

&#x20;"readAt": 1513616971891,

&#x20;"updatedDate": "2017-12-18T17:09:31.891Z",

&#x20;"updatedAt": 1513616971891

&#x20;}

&#x20;],

&#x20;"clientInfo": {

&#x20;"customerId": 42,

&#x20;"subAccountId": 1291,

&#x20;"userId": 1

&#x20;}

}

For every status update of sent messages (receipt of delivery to the end user, message read, etc.), a callback/webhook is sent. Callbacks are sent in bulk.

Important: The endpoint that the webhook will use to send statuses must be set up by our support and operations team.

The return format will have the following description:

| Field          | Details                          | Type       |
| -------------- | -------------------------------- | ---------- |
| **total**      | Number of callbacks in the call. | String     |
| **data**       | List of Callbacks.               | Data\[]    |
| **clientInfo** | Client information.              | ClientInfo |

### Data:

| Field                   | Details                                                                                                                                                              | Type    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **id**                  | Last message id.                                                                                                                                                     | String  |
| **correlationId**       | Unique ID set by you to compare to the message status (Callback and DLR). This parameter is optional, and you can use the ID generated by Wavy Messaging to compare. | String  |
| **destination**         | Phone number to which your message was sent (including country code). E.g.: 5511900000000.                                                                           | String  |
| **origin**              | Phone number that identifies the WhatsApp Account (including country code). E.g.: 5511900000000.                                                                     | String  |
| **campaignId**          | Previously set campaignID.                                                                                                                                           | String  |
| **campaignAlias**       | Previously set campaign alias.                                                                                                                                       | String  |
| **extraInfo**           | Extra information sent with the original message.                                                                                                                    | String  |
| **sent**                | Indicates whether the message has been sent.                                                                                                                         | Boolean |
| **sentStatusCode**      | Status Code generated by Wavy Messaging for the message indicating its sent status.                                                                                  | Number  |
| **sentStatus**          | Sent status description.                                                                                                                                             | Boolean |
| **sentDate**            | Date the message was sent. Format: yyyy-MM-dd’T'HH:mm:ssZ.                                                                                                           | String  |
| **sentAt**              | Time the message was sent, using Unix\_time format                                                                                                                   | Number  |
| **delivered**           | Indicates whether the message has been delivered to its destination.                                                                                                 | Boolean |
| **deliveredStatusCode** | Status Code generated by Wavy Messaging indicating whether the message has been delivered.                                                                           | Number  |
| **deliveredStatus**     | Delivered status description.                                                                                                                                        | String  |
| **deliveredDate**       | Date the message was delivered. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                                                       | String  |
| **deliveredAt**         | Time the message was delivered, using Unix\_time format                                                                                                              | Number  |
| **read**                | Indicates whether the message has been read by the recipient.                                                                                                        | Boolean |
| **readDate**            | Date the message was read. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                                                            | String  |
| **readAt**              | Time the message was read, using Unix\_time format                                                                                                                   | String  |
| **updatedDate**         | Date the message status was updated. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                                                  | String  |
| **updatedAt**           | Time the message status was updated, using Unix\_time format                                                                                                         | String  |

### ClientInfo

| Field            | Details                    | Type   |
| ---------------- | -------------------------- | ------ |
| **customerId**   | Customer identification.   | Number |
| **subAccountId** | Subaccount identification. | Number |
| **userId**       | User identification.       | Number |

### Status

Statuses that can be sent in the callback:

| Status                                  | Sent Code | Delivery Code | Meaning                                                                                                                                               |
| --------------------------------------- | --------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CARRIER\_COMMUNICATION\_ERROR**       | 102       | ​             | Error in uploading media to WhatsApp.                                                                                                                 |
| **REJECTED\_BY\_CARRIER**               | 103       | ​             | A databank error has occurred.                                                                                                                        |
| **SENT\_SUCCESS**                       | 2         | ​             | ​                                                                                                                                                     |
| **EXPIRED**                             | 2         | 101           | Message expired.                                                                                                                                      |
| ​                                       | ​         | ​             | Failure to send message because it is too old.                                                                                                        |
| **NOT\_DELIVERED**                      | 2         | 104           | Limit reached - too many attempts to send messages.                                                                                                   |
| ​                                       | ​         | ​             | Failure to send message because this user’s phone number is part of an experiment.                                                                    |
| ​                                       | ​         | ​             | Structure unavailable: Customer unable to display HSM.                                                                                                |
| ​                                       | ​         | ​             | Failure to send message because you are outside the support window for freely messaging this user. Please use a valid HSM notification or reconsider. |
| ​                                       | ​         | ​             | Error uploading media (unknown error).                                                                                                                |
| ​                                       | ​         | ​             | Failure to send message because your account is ineligible. Please verify your WhatsApp Business account.                                             |
| ​                                       | ​         | ​             | Temporary upload failure. Please try again later.                                                                                                     |
| **DELIVERED\_SUCCESS**                  | 2         | 4             | ​                                                                                                                                                     |
| **READ\_SUCCESS**                       | 2         | 5             | ​                                                                                                                                                     |
| **INVALID\_DESTINATION\_NUMBER**        | 202       | ​             | Invalid WhatsApp contact.                                                                                                                             |
| **DESTINATION\_BLOCKED\_BY\_OPTOUT**    | 204       | ​             | Destination blocked by Opt-Out.                                                                                                                       |
| **INVALID\_MESSAGE\_LENGTH**            | 206       | ​             | Message is too long.                                                                                                                                  |
| **INVALID\_MESSAGE\_TEXT**              | 207       | ​             | Invalid parameter value.                                                                                                                              |
| **INVALID\_CONTENT**                    | 209       | ​             | Invalid type of UNKNOWN message.                                                                                                                      |
| **INVALID\_SESSION**                    | 210       | ​             | Session is not open and no fallback HSM is set up.                                                                                                    |
| **DESTINATION\_BLOCKED\_BY\_OPTIN**     | 211       | ​             | ​                                                                                                                                                     |
| **DESTINATION\_BLOCKED\_BY\_WHITELIST** | 212       | ​             | ​                                                                                                                                                     |
| **INTERNAL\_ERROR**                     | 311       | ​             | Unable to verify WhatsApp API contacts.                                                                                                               |

### MO (Messages Sent by the End User to the WhatsApp Account)

Text message example:

{

&#x20;"total": 1,

&#x20;"data": \[

&#x20;{

&#x20;"id": "ce425ffe-bc62-421f-9261-e6819a5eab43",

&#x20;"source": "5519900000000",

&#x20;"origin": "5519900000000",

&#x20;"userProfile": {

&#x20;"name": "username"

&#x20;},

&#x20;"campaignId": 100,

&#x20;"correlationId": "...",

&#x20;"campaignAlias": "...",

&#x20;"flowId": "....",

&#x20;"extraInfo": "...",

&#x20;"message": {

&#x20;"type": "TEXT",

"messageText": "Hello, this is a user message."

&#x20;},

&#x20;"receivedAt": 1513616971473,

&#x20;"receivedDate": "2017-12-18T17:09:31.473Z"

&#x20;}

&#x20;]

}

Extra Info example:

{

&#x20;"segmentation\_list":\[

&#x20;{

&#x20;"id":26,

&#x20;"customerId":42,

&#x20;"subAccountId":0,

&#x20;"name":"Movile WhatsApp Segmentation List",

&#x20;"active":true

&#x20;},

&#x20;{

&#x20;"id":27,

&#x20;"customerId":43,

&#x20;"subAccountId":0,

&#x20;"name":"Movile WhatsApp Segmentation List 2",

&#x20;"active":true

&#x20;}

&#x20;]

}

Media message example

{

&#x20;"total": 1,

&#x20;"data": \[

&#x20;{

&#x20;"id": "ce425ffe-bc62-421f-9261-e6819a5eab43",

&#x20;"source": "5519900000000",

&#x20;"origin": "5519900000000",

&#x20;"userProfile": {

&#x20;"name": "username"

&#x20;},

&#x20;"campaignId": 100,

&#x20;"correlationId": "...",

&#x20;"campaignAlias": "...",

&#x20;"flowId": "....",

&#x20;"extraInfo": "...",

&#x20;"message": {

&#x20;"type": "IMAGE",

&#x20;"mediaUrl": "https\://...",

&#x20;"mimeType": "image/jpg",

&#x20;"caption": "..."

&#x20;},

&#x20;"receivedAt": 1513616971473,

&#x20;"receivedDate": "2017-12-18T17:09:31.473Z"

&#x20;}

&#x20;]

}

Location message example:

{

&#x20;"total": 1,

&#x20;"data": \[

&#x20;{

&#x20;"id": "ce425ffe-bc62-421f-9261-e6819a5eab43",

&#x20;"source": "5519900000000",

&#x20;"origin": "5519900000000",

&#x20;"userProfile": {

&#x20;"name": "username"

&#x20;},

&#x20;"campaignId": 100,

&#x20;"correlationId": "...",

&#x20;"campaignAlias": "...",

&#x20;"flowId": "....",

&#x20;"extraInfo": "...",

&#x20;"message": {

&#x20;"location": {

&#x20;"geoPoint": "-22.894180,-47.047960",

&#x20;"name": "Wavy",

&#x20;"address": "Av. Cel. Silva Telles"

&#x20;}

&#x20;},

&#x20;"receivedAt": 1513616971473,

&#x20;"receivedDate": "2017-12-18T17:09:31.473Z"

&#x20;}

&#x20;]

}

Contact message example:

{

&#x20;"total": 1,

&#x20;"data": \[

&#x20;{

&#x20;"id": "ce425ffe-bc62-421f-9261-e6819a5eab43",

&#x20;"source": "5519900000000",

&#x20;"origin": "5519900000000",

&#x20;"userProfile": {

&#x20;"name": "username"

&#x20;},

&#x20;"campaignId": 100,

&#x20;"correlationId": "...",

&#x20;"campaignAlias": "...",

&#x20;"flowId": "....",

&#x20;"extraInfo": "...",

&#x20;"message": {

&#x20;"contacts":\[

&#x20;{

&#x20;"addresses":\[

&#x20;{

&#x20;"city":"Menlo Park",

&#x20;"country":"United States",

&#x20;"country\_code":"us",

&#x20;"state":"CA",

&#x20;"street":"1 Hacker Way",

&#x20;"type":"HOME",

&#x20;"zip":"94025"

&#x20;},

&#x20;{

&#x20;"city":"Menlo Park",

&#x20;"country":"United States",

&#x20;"country\_code":"us",

&#x20;"state":"CA",

&#x20;"street":"200 Jefferson Dr",

&#x20;"type":"WORK",

&#x20;"zip":"94025"

&#x20;}

&#x20;],

&#x20;"birthday":"2012-08-18",

&#x20;"emails":\[

&#x20;{

&#x20;"email":"<test@fb.com>",

&#x20;"type":"WORK"

&#x20;},

&#x20;{

&#x20;"email":"<test@whatsapp.com>",

&#x20;"type":"WORK"

&#x20;}

&#x20;],

&#x20;"name":{

&#x20;"first\_name":"John",

&#x20;"formatted\_name":"John Smith",

&#x20;"last\_name":"Smith"

&#x20;},

&#x20;"org":{

&#x20;"company":"WhatsApp",

&#x20;"department":"Design",

&#x20;"title":"Manager"

&#x20;},

&#x20;"phones":\[

&#x20;{

&#x20;"phone":"+1 (940) 555-1234",

&#x20;"type":"HOME"

&#x20;},

&#x20;{

&#x20;"phone":"+1 (650) 555-1234",

&#x20;"type":"WORK",

&#x20;"wa\_id":"16505551234"

&#x20;}

&#x20;],

&#x20;"urls":\[

&#x20;{

&#x20;"url":"<https://www.fb.com>",

&#x20;"type":"WORK"

&#x20;}

&#x20;]

&#x20;}

&#x20;]

&#x20;},

&#x20;"receivedAt": 1513616971473,

&#x20;"receivedDate": "2017-12-18T17:09:31.473Z"

&#x20;}

&#x20;]

}

For each reply from the end user (MO or Mobile Originated), a callback/webhook is sent. These MOs are sent in bulk.

Important: The endpoint that the webhook will use to send statuses must be set up by our support and operations team.

The return format will have the following description:

| Field             | Details                                                                                                                                                              | Type        |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **total**         | Number of callbacks for the call.                                                                                                                                    | String      |
| **data**          | List of Mobile Originated (MO) messages.                                                                                                                             | Data\[]     |
| Field             | Details                                                                                                                                                              | Type        |
| **id**            | Last message identification                                                                                                                                          | String      |
| **source**        | Sender’s phone number                                                                                                                                                | String      |
| **origin**        | Phone number that identifies the WhatsApp Account (including country code). E.g.: 5511900000000.                                                                     | String      |
| **userProfile**   | Profile of the user who sent the message                                                                                                                             | UserProfile |
| **correlationId** | Unique ID set by you to compare to the message status (Callback and DLR). This parameter is optional, and you can use the ID generated by Wavy Messaging to compare. | String      |
| **campaignId**    | Previously set campaignID.                                                                                                                                           | String      |
| **campaignAlias** | Previously set campaign alias.                                                                                                                                       | String      |
| **message**       | MO message.                                                                                                                                                          | message     |
| **receivedAt**    | Date the message was received. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                                                        | String      |
| **receivedDate**  | Date the message was received, using Unix\_time format                                                                                                               | String      |
| **extraInfo**     | Extra information related to the message. Format: **Json**                                                                                                           | String      |

### **MO Flow Control - Segmentation Lists**

The message will have a list of segmentation lists in the extraInfo field. Our partners use it to direct messages to certain flows. The key name is **segmentation\_lists** and it contains a list of **SegmentationList**.

| Field            | Details                      | Type    |
| ---------------- | ---------------------------- | ------- |
| **id**           | Segmentation list identifier | Integer |
| **customerId**   | Customer identifier          | Integer |
| **subAccountId** | Subaccount identifier        | Integer |
| **name**         | Name of segmentation list    | String  |
| **active**       | Status of segmentation list  | Boolean |

### Message:

| Field           | Details                                                               | Type       |
| --------------- | --------------------------------------------------------------------- | ---------- |
| **type**        | Type of message sent to the end user: TEXT - IMAGE - AUDIO - DOCUMENT | String     |
| **messageText** | Text message (MO) sent by the end user.                               | String     |
| **waGroupId**   | Group to which the message was sent.                                  | String     |
| **mediaUrl**    | Url to download media sent by the end user.                           | String     |
| **mimeType**    | Mime type of the file sent by the end user.                           | String     |
| **caption**     | Media label sent by the end user.                                     | String     |
| **location**    | Location sent by the end user.                                        | Location   |
| **contacts**    | Contacts sent by the end user.                                        | Contact\[] |

### UserProfile:

| Field    | Required | Details           | Type   |
| -------- | -------- | ----------------- | ------ |
| **name** | No       | User profile name | String |

### Location:

| Field        | Details                                                     | Type   |
| ------------ | ----------------------------------------------------------- | ------ |
| **name**     | Location name.                                              | String |
| **address**  | Location address.                                           | String |
| **geoPoint** | Geopoint sent by the end user. Format: “latitude,longitude” | String |

### Contact:

| Field         | Required | Details                                    | Type       |
| ------------- | -------- | ------------------------------------------ | ---------- |
| **addresses** | No       | Full address(es) of the contact.           | Address\[] |
| **birthday**  | No       | Birthday in YYYY-MM-DD format.             | String     |
| **emails**    | No       | Email address(es) of the contact.          | Email\[]   |
| **name**      | No       | Full name of the contact.                  | Name       |
| **org**       | No       | Information of the contact’s organization. | Org        |
| **phones**    | No       | Phone number(s) of the contact.            | Phone\[]   |
| **urls**      | No       | URL(s) of the contact.                     | Url\[]     |

### Address:

| Field             | Required | Details                             | Type   |
| ----------------- | -------- | ----------------------------------- | ------ |
| **street**        | No       | Street name and number.             | String |
| **city**          | No       | City name.                          | String |
| **state**         | No       | State abbreviation.                 | String |
| **zip**           | No       | Zip code.                           | String |
| **country**       | No       | Full country name.                  | String |
| **country\_code** | No       | Country abbreviation (Two letters). | String |
| **type**          | No       | Default Values: HOME, WORK.         | String |

### Email:

| Field     | Required | Details                     | Type   |
| --------- | -------- | --------------------------- | ------ |
| **email** | No       | Email address.              | String |
| **type**  | No       | Default Values: HOME, WORK. | String |

### Name:

| Field               | Required | Details                           | Type   |
| ------------------- | -------- | --------------------------------- | ------ |
| **first\_name**     | No       | First name.                       | String |
| **last\_name**      | No       | Last name.                        | String |
| **middle\_name**    | No       | Middle name.                      | String |
| **name\_suffix**    | No       | Name suffix.                      | String |
| **name\_prefix**    | No       | Name prefix.                      | String |
| **formatted\_name** | No       | Full name as it normally appears. | String |

### Org:

| Field          | Required | Details                             | Type   |
| -------------- | -------- | ----------------------------------- | ------ |
| **company**    | No       | Name of the contact’s organization. | String |
| **department** | No       | Name of the contact’s department.   | String |
| **title**      | No       | Contact’s corporate title.          | String |

### Phone:

| Field      | Required | Details                                         | Type   |
| ---------- | -------- | ----------------------------------------------- | ------ |
| **phone**  | No       | Formatted phone number.                         | String |
| **type**   | No       | Default values: CELL, MAIN, IPHONE, HOME, WORK. | String |
| **wa\_id** | No       | WhatsApp identifier.                            | String |

### Url:

| Field     | Required | Details                     | Type   |
| --------- | -------- | --------------------------- | ------ |
| **phone** | No       | URL of the contact.         | String |
| **type**  | No       | Default values: HOME, WORK. | String |

For objects containing a type field, the listed values are simply considered default values that can be seen; however, you can set the field to any descriptive value you choose.

## WhatsApp SFTP API

#### Connection Details

| ​                  | ​                                                            |
| ------------------ | ------------------------------------------------------------ |
| **Hostname**       | ftp-messaging.wavy.global                                    |
| **Port**           | 2222                                                         |
| **Protocol**       | SFTP (transfer over ssh, providing client-server encryption) |
| **Authentication** | username + password (provided by support)                    |

Your IPs must be allowed in Movile’s firewalls. If you need to allow outgoing traffic in the firewall for port 2222, you must allow the DNS, or IPs 200.219.220.54, 200.189.169.53 and 45.236.179.22

### Sending Messages via SFTP

To trigger messages via FTP, you need to generate a file with formatting following the example below: HSM Message:

**2018-10-16;10:00;20:00;HSM;chatclub\_welcome;pt\_BR;DETERMINISTIC;name|company** **phone;name;company** **551999999999;Name1;Wavy** **551999999999;Name2;Movile**

| 1st Line                                                |
| ------------------------------------------------------- |
| Send date (for scheduling cases)                        |
| Start send time (for scheduling cases)                  |
| End send time (for scheduling cases)                    |
| Message type must be: **HSM**                           |
| HSM name (elementName)                                  |
| HSM language (languageLocale)                           |
| HSM language Deterministic or Fallback (languagePolicy) |
| name of HSM parameters                                  |

### **Notes for the First Line:**

1 - Parameter names must match the column names

2 - Information that will not be used may be left blank, however you should keep the semicolon as separation. Example of a case where we did not use scheduling (the first fields are between semicolons and have no information within): ; ; ; HSM;chatclub\_welcome;pt\_BR;DETERMINISTIC;name|company

3 - By default, the languagePolicy will be Deterministic.

4 - The names of HSM parameters should be separated by “ | ” and not by “ ; ”

| 2nd Line                               |
| -------------------------------------- |
| Column names                           |
| 3rd and Remaining Lines:               |
| Recipient and values of HSM parameters |

### Consulting Lists via API

### Request

Using GET, you can make a request by sending all parameters in the query string

<http://api-messaging.wavy.global/v1/list/{listType}?customerId={customerId}\\&subAccountId={subAccountId}>

| List Type                       | Value relayed in {listType} |
| ------------------------------- | --------------------------- |
| **Whatsapp OPT-OUT List**       | OPTOUT                      |
| **Whatsapp OPT-IN List**        | OPTIN                       |
| **Whatsapp Blacklist**          | BLACKLIST                   |
| **Whatsapp Whitelist (for MT)** | WHITELIST                   |

The ***customerId*** parameter is required, while ***subAccountId*** is optional.

Attention: the ’{‘ and ’}‘ curly brackets must also be replaced. For example, “{listType}” becomes “OPTIN”.

You should also relay the following headers:

| Header                  | Value               |
| ----------------------- | ------------------- |
| **Content-Type**        | application/json    |
| **authenticationToken** | Messaging1 token    |
| **userName**            | Messaging1 username |

### Response

If successful, if there is any data related to the customerId and subAccountId, the request will return a JSON with 3 attributes:

| Attribute   | Value                                                                                                |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| **success** | true                                                                                                 |
| **status**  | 200                                                                                                  |
| **data**    | Link to download a csv file containing the “source” and “createdAt” fields of all destinations found |

The “createdAt” column is in the **America/Sao\_Paulo time zone**, UTC-3 or UTC-2 in Daylight Saving Time

If there is no associated data, only a similar JSON will be returned, but without the data field, which means no issues occurred with the request, but there weren’t any data related to the parameters relayed.

Response example:

{

&#x20;"success": true,

&#x20;"status": 200,

&#x20;"data": "<https://chatclub-cdn.wavy.global/2019/02/12/f2b8effb-d0bc-4327-86c2-48fedcb01b1b/list-42-4330544192402746957.csv>"

}

### Consulting Open Sessions via API

### Request

To consult open sessions through our API, you need to make a GET request to the following URL:

GET <http://api-messaging.wavy.global/v1/session?customerId={customerId}\\&subAccountId={subAccountId}>

The ***customerId*** parameter is required, while ***subAccountId*** is optional.

Attention: The ’{‘ and ’}‘ curly brackets must also be replaced. For example, “={customerId}” becomes “=42”.

You should also relay the following headers:

| Header                  | Value            |
| ----------------------- | ---------------- |
| **Content-Type**        | application/json |
| **authenticationToken** | Token            |
| **userName**            | Username         |

Username and token can be obtained through our platform: <https://messaging.wavy.global>

### Response

If successful, if there are any open sessions for the customerId and subAccountId, the request will return a JSON with the following attribute:

| Attribute     | Value                                                                                                           |
| ------------- | --------------------------------------------------------------------------------------------------------------- |
| **file\_url** | Link to download a csv file containing the “source” and “session\_created\_at” fields of all destinations found |

If there are no data associated with the ***customerId*** and ***subAccountId***, the returned file will be empty, containing only the header.

Response example:

{

&#x20;"file\_url": "<https://chatclub-cdn.wavy.global/2019/02/13/633e33fc-3a3f-4ca5-a8b0-4b747fb67137/5bd46e2b-5990-4681-9b29-98ab6598960e>"

}


# WhatsApp Groups API

This documentation provides the information you need for integration with the Wavy Messaging platform for managing groups through the Wavy WhatsApp Integration. The API has REST integration, using the HTTP protocol with TLS, supporting the POST method with parameters sent in JSON format.

### Authentication

In order to successfully use our API, you are required to present a valid user name - or email - and the associated authentication token. While creating the request, you have to provide the following parameters on the headers:

| Field                   | Details                                                                                                                                                     | Data Type |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **userName**            | Name or email valid for authentication on Wavy Messaging.                                                                                                   | String    |
| **authenticationToken** | Authentication token generated by our platform. Find it here or consult the support. [here](https://messaging.movile.com/messaging/user/api_configuration)​ | String    |

### Connection Details

| ​                  | ​                         |
| ------------------ | ------------------------- |
| **Hostname**       | api-messaging.wavy.global |
| **Port**           | 443 (https)               |
| **Protocol**       | HTTPS (TLS encryption)    |
| **Authentication** | username + token          |
| **Encoding**       | UTF-8                     |

### Sending Messages to Groups

When sending messages to groups, the request is similar to that of direct messages. Only the Destination object needs to be adapted.

POST <https://api-messaging.wavy.global/v1/whatsapp/send>

The request body must contain the same fields as in [Sending Text Messages](http://doc-messaging.movile.com/pt.html#envio-de-mensagens-de-texto).

Group delivery example

```
{
 "destinations": [{
 "destination": "5519900000000-1513616971",
 "recipientType": "group"
 }],
 "message": {
 "messageText": "Test message"
 }
 }
```

### &#x20;Group MO

Group MOs contain the same fields as [Regular MOs](http://doc-messaging.movile.com/pt.html#mo-mensagens-enviadas-pelo-usu-rio-final-para-a-conta-do-whatsapp) with the addition of waGroupId indicating to which group the message was sent, as shown in the example.

Be careful if you are replying automatically to direct messages sent to your WhatsApp account. If the waGroupId field is ignored, **the MO can be mistaken for a direct message instead of a group message**, and you will reply with a direct message. This way you run the risk of being charged for an HSM every time the user sends you a group message if the waGroupId field is not treated correctly.

Group message example:

```
{
 "total": 1,
 "data": [
 {
 "source": "5419900000000",
 "origin": "5419900000000",
​
 "...",
​
 "message": {
 "type": "TEXT",
 "messageText": "Hello",
 "waGroupId": "5519900000000-1553784379"
 },
​
 "..."
 }
 ]
}
```

### Creating Groups

Create a group by providing it with a subject or title, which is the name that will appear on the chat list. In response, you will receive a group ID you will use to send messages to the group, manage the group, etc.

**Unused Groups**: If you have many unused groups associated with your account, you may encounter an error (due to too many groups created). You can simply clear the groups you are no longer using by leaving them.

#### Request

Example

```
{
 "subject": "group-subject"
 }
```

&#x20;POST <https://api-messaging.wavy.global/v1/whatsapp/groups>

The request body must contain a JSON object with the following fields:

| Field   | Required | Details                                          | Type   |
| ------- | -------- | ------------------------------------------------ | ------ |
| subject | Yes      | Group subject or title, limited to 25 characters | String |

#### Response

Response example

```
 {
 "groups": [{
 "creation_time": 1513616971,
 "id": "5519900000000-1513616971"
 }]
 }
```

The response to a request to create a group returns a group ID that you will use to send messages to the group, manage the group, etc. If you need to obtain the group ID at another time, see the [Consulting All Groups section](http://doc-messaging.movile.com/pt.html#consulta-de-todos-os-grupos).

The following fields are returned in a successful response:

| Field          | Details                                                                                                                                  | Type    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| creation\_time | Time of creation                                                                                                                         | Integer |
| id             | Group identified for the recently created group. It must be used to uniquely identify groups in later requests, where group\_id is used. | String  |

### Consulting All Groups

Retrieve all groups in which the customer is a participant.

#### Request

GET <https://api-messaging.wavy.global/v1/whatsapp/groups>

#### Response

Response example

```
 {
 "groups": [{
 "id": "5519900000000-1513616971"
 }]
 }
```

The response returns the group IDs for all groups in which the customer is a participant. You can obtain more information on the group, such as list of participants and the group subject, using the call described in the [Consulting Group Information section](http://doc-messaging.movile.com/pt.html#consulta-a-informa-es-de-grupo).

The following fields are returned in a successful response. If there are no groups, a JSON array of empty groups is returned.

| Field  | Details                                     | Type   |
| ------ | ------------------------------------------- | ------ |
| **id** | List of groups the customer participates in | String |

### Consulting Group Information

Use this call to obtain information on the group, including participant Ids, and group subject. To obtain the group icon, see the [Consulting a Group Icon section](http://doc-messaging.movile.com/pt.html#consulta-a-cone-de-grupo).

#### Request

GET <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id>

#### Response

Response example

```
{
 "groups": [{
 "admins": [
 "5519900000000"
 ],
 "creation_time": 1513616971,
 "creator": "5519900000000",
 "id": "5519900000000-1513616971",
 "participants": [
 "5519900000000"
 ],
 "subject": "group-subject"
 }]
 }
```

&#x20;The following fields are returned in a successful response:

| Field              | Details                                                                                                                                                                                                                                                                                                             | Type      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **admins**         | Group administrators. Lists the IDs of the group creator and any added administrators as described in the [Adding Administrators section](http://doc-messaging.movile.com/pt.html#adi-o-de-administradores).                                                                                                        | String\[] |
| **creation\_time** | Time of group creation                                                                                                                                                                                                                                                                                              | Int       |
| **creator**        | Group creator ID                                                                                                                                                                                                                                                                                                    | String    |
| **id**             | Group ID                                                                                                                                                                                                                                                                                                            | String    |
| **participants**   | Group participants. It is an array with the IDs of all group participants. Initially, it will only be the group creator. Invite users to the group creating an invite link, as described in the [Creating a Group Invite Link section](http://doc-messaging.movile.com/pt.html#cria-o-de-link-de-convite-de-grupo). | String\[] |
| **subject**        | Group subject                                                                                                                                                                                                                                                                                                       | String    |

### Updating Group Information

Updating information means setting a new group subject.

#### Request

Example

```
 {
 "subject": "new-group-subject"
 }
```

PUT <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id>

The request body must contain a JSON object with the following fields:

| Field       | Required | Details                                                          | Type   |
| ----------- | -------- | ---------------------------------------------------------------- | ------ |
| **subject** | Yes      | Update the group subject to this value, limited to 25 characters | String |

#### Response

A successful response will return a 200 OK status and null or {}. If the group is not found, the response will be 404 Not Found.

### Creating a Group Invite Link

You cannot directly add participants to the group. Participants can only be invited to the group. Create a link that participants can use to join your group.

#### Request

GET <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id/invite>

#### Response

Response example

```
{
 "groups": [{
 "link": "group-invite-link"
 }]
 }
```

&#x20;The following fields are returned in a successful response:

| Field | Details           | Type   |
| ----- | ----------------- | ------ |
| link  | Group invite link | String |

Once you have a link to invite participants to the group, send the link in a text message. When a user clicks the message, they will be invited to the group.

### Deleting an Invite Link

#### Request

DELETE <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id/invite>

#### Response

A successful response will return a 200 OK status and null or {}.

### Removing Group Members

#### Request

Example

```
 {
 "waIds": [
 "5519900000000",
 "5519900000000"
 ]
 }
```

DELETE <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id/participants>

The request body must contain a JSON object with the following fields:

| Field | Required | Details                                              | Type      |
| ----- | -------- | ---------------------------------------------------- | --------- |
| waIds | Yes      | Numbers of participants to be removed from the group | String\[] |

#### Response

A successful response will return a 200 OK status and null or {}. If the phone number is not found, the response will be 400 Bad Request.

### Leaving a Group

Leaving a group means you will remove yourself from the list of group participants. The Group will continue to exist with the remaining participants.

#### Request

POST <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id/leave>

#### Response

A successful response will return a 200 OK status and null or {}. If the phone number is not found, the response will be 400 Bad Request.

### Setting a Group Icon

#### Request

Example

```
curl -X POST \
 https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id/icon \
 -H 'authenticationToken: <authenticationtoken>'
 -H 'username: <username>' \
 -H 'Content-Type: image/jpeg' \
 --data-binary @your-file-path​
```

POST <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id/icon> Content-Type: image/jpeg or other appropriate type

binary-image-content

In order to set a group icon, you have to upload an image from its binary content. The Content-Type header must match the image’s MIME type.

#### Response

A successful response will return a 200 OK status and null or {}.

### Consulting a Group Icon

#### Request

GET <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id/icon>

#### Response

Response example

```
{
 "type": "URL",
 "mimeType": "image/jpeg",
 "fileName": "groupIcon.jpeg",
 "extraData": {
 "public": true,
 "Content-Type": "image/jpeg",
 "Content-Length": "2500"
 },
 "data": "https://chatclub-cdn.wavy.global/2019/03/25/ce425ffe-bc62-421f-9261-e6819a5eab43/groupIcon.jpeg"
}
```

A successful response will return a 200 OK and a JSON object with the following fields. If the group does not have an associated icon, the response will be 404 Not Found.

| Field         | Details          | Type   |
| ------------- | ---------------- | ------ |
| **type**      | Data field type  | String |
| **mimeType**  | File MIME type   | String |
| **fileName**  | File name        | String |
| **extraData** | File information | String |
| **data**      | File             | String |

### Removing a Group Icon

#### Request

DELETE <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id/icon>

#### Response

A successful response will return a 200 OK status and null or {}. If the group does not have an associated icon, the response will be 404 Not Found.

### Adding Administrators

By default, the only administrator of a group is its creator. More administrators can be added as long as they are already group participants. To consult the participants of a group, follow the instructions in [Consulting Group Information](http://doc-messaging.movile.com/pt.html#consulta-a-informa-es-de-grupo)​

#### Request

Example

```
 {
 "waIds": [
 "5519900000000",
 "5519900000000"
 ]
 }
```

PATCH <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id/admins>

The request body must contain a JSON object with the following fields:

| Field     | Required | Details                                                | Type      |
| --------- | -------- | ------------------------------------------------------ | --------- |
| **waIds** | Yes      | Numbers of participants who will become administrators | String\[] |

#### Response

A successful response will return a 200 OK status and null or {}. If the phone number is not found, the response will be 400 Bad Request.

### Removing Administrators

Administrators can be removed so as to become regular group participants. To consult the administrators of a group, follow the instructions in [Consulting Group Information](http://doc-messaging.movile.com/pt.html#consulta-a-informa-es-de-grupo).

#### Request

Example

```
 {
 "waIds": [
 "5519900000000"
 ]
 }

```

DELETE <https://api-messaging.wavy.global/v1/whatsapp/groups/your-group-id/admins>

The request body must contain a JSON object with the following fields:

| Field | Required | Details                                                          | Type      |
| ----- | -------- | ---------------------------------------------------------------- | --------- |
| waIds | Yes      | Phone numbers of the participants who will become administrators | String\[] |

#### Response

A successful response will return a 200 OK status and null or {}. If the phone number is not found, the response will be 400 Bad Request.


# Listing Message Templates

Request <https://apigw.wavy.global/api/v1/whatsapp_message_templates?page=1&page_size=999> **The request can contain the following parameters in the query string**

| Field         | Required | Description                                                         |
| ------------- | -------- | ------------------------------------------------------------------- |
| page          | no       | Page index beginning at 1                                           |
| page\_size    | no       | Page results. 10 by default                                         |
| element\_name | no       | Search for templates containing element\_name as part of their name |

## Response Example

```
{
 "data" : [
 {
 "message_type" : "RESERVATION_UPDATE",
 "customer_id" : 6364,
 "messages" : [
 {
 "buttons_type" : null,
 "id" : 33732,
 "buttons" : {
 "payload" : null
 },
 "language" : "EN",
 "last_modified" : "2020-06-04T14:52:39.674403",
 "placeholders" : ["data"],
 "header" : "",
 "text" : "Hello, you have an appointment with us for *{{1}}*.\nReply *YES* to confirm or *NO* to cancel.",
 "header_type" : "none",
 "status" : "approved",
 "footer" : ""
 }
 ],
 "sub_account_id" : 11486,
 "last_modified" : "2020-06-04T14:52:39.665449",
 "id" : 22045,
 "element_name" : "appointment_reminder_datetime",
 "namespace" : "whatsapp:hsm:ecommerce:movile",
 "template_type" : "header_footer",
 "languages" : ["EN"]
 },
 {
 "messages" : [
 {
 "status" : "approved",
 "footer" : "",
 "text" : "You have an appointment with us!",
 "header_type" : "none",
 "header" : "",
 "language" : "EN",
 "placeholders" : [],
 "last_modified" : "2020-06-02T18:46:01.386517",
 "buttons" : {
 "payload" : null
 },
 "id" : 33649,
 "buttons_type" : null
 }
 ],
 "sub_account_id" : 11486,
 "customer_id" : 6364,
 "message_type" : "RESERVATION_UPDATE",
 "template_type" : "header_footer",
 "languages" : ["EN"],
 "namespace" : "whatsapp:hsm:ecommerce:movile",
 "id" : 21964,
 "element_name" : "appointment_reminder",
 "last_modified" : "2020-06-02T18:46:01.384862"
 }
 ]
}
​
```

&#x20;

The response returns a list of message templates with the following fields

| Field                       | Details                                                                                                                                                                                                                                                                                                                                                                                                 | Tipo      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| languages                   | Languages this template is available in                                                                                                                                                                                                                                                                                                                                                                 | \[String] |
| namespace                   | Template namespace. Must be used in the messaging API                                                                                                                                                                                                                                                                                                                                                   | String    |
| element\_name               | Template name. Must be used in the messaging API                                                                                                                                                                                                                                                                                                                                                        | String    |
| message\_type               | <p>Template category type. Possible values are</p><p>ACCOUNT\_UPDATE, PAYMENT\_UPDATE, PERSONAL\_FINANCE\_UPDATE, SHIPPING\_UPDATE, RESERVATION\_UPDATE, ISSUE\_RESOLUTION, APPOINTMENT\_UPDATE, TRANSPORTATION\_UPDATE, TICKET\_UPDATE, ALERT\_UPDATE, AUTO\_REPLY</p>                                                                                                                                 | String    |
| template\_type              | <p>Template type. Possible values are</p><p>header\_footer or body\_only</p>                                                                                                                                                                                                                                                                                                                            | String    |
| messages\[]                 | List containing information on each template translation. The size of this list is equivalent to the number of supported languages in languages                                                                                                                                                                                                                                                         | \[Object] |
| messages\[].status          | <p>Template status. Possible values are:</p><p>in\_analysis, approved, disapproved, error</p><p>In order for a template to be approved, its content must follow Facebook’s guidelines.</p><p>​<a href="https://developers.facebook.com/docs/whatsapp/message-templates/guidelines"><https://developers.facebook.com/docs/whatsapp/message-templates/guidelines></a>​</p>                                | String    |
| messages\[].header\_type    | <p>Header type. Possible values are</p><p>video, location, text, document, image or none</p>                                                                                                                                                                                                                                                                                                            | String    |
| messages\[].header          | Text contained in the text header. Only used when header\_type = text                                                                                                                                                                                                                                                                                                                                   | String    |
| messages\[].text            | Text contained in the body                                                                                                                                                                                                                                                                                                                                                                              | String    |
| messages\[].footer          | Text contained in the footer                                                                                                                                                                                                                                                                                                                                                                            | String    |
| messages\[].buttons\_type   | <p>Button type. Possible values are</p><p>quick\_reply or call\_to\_action</p>                                                                                                                                                                                                                                                                                                                          | String    |
| messages\[].placeholders    | Description of placeholders present in the body text, represented as {{1}}, {{2}}, etc. in the text field                                                                                                                                                                                                                                                                                               | \[String] |
| messages\[].buttons.payload | <p>Button content in JSON format serialized as a string.</p><p>Quick reply buttons will be in {"payload": \[{"text": "button text"}]} format</p><p>Call-to-action buttons will be in</p><p>{"payload": \[{"url": "https:wavy.global/en", "text": "Access our website", "type": "url"}, {"text": "Call us", "type": "phone\_number", "country\_code": "55", "phone\_number": "11900000000"}]} format</p> | String    |

## Message Template Examples

Template with a text header, body and footer:

Template with an image header, body and no footer:

Template with 2 parameters:


# WhatsApp Interactive API

## Interactive Messages

To send interactive messages we will follow the standard of other types of messages that can be seen [here](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/whatsapp-api#whatsapp-api).

#### Message

| Field       | Required | Details                                 | Type                |
| ----------- | -------- | --------------------------------------- | ------------------- |
| interactive | Yes      | Field used to send interactive messages | Interactive Message |

#### Interactive Message

| Field                  | Required                                         | Details                                                                                 | Type              |
| ---------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------- | ----------------- |
| messageInteractiveType | Yes                                              | Type of interactive message. Available options: LIST and REPLY\_BUTTON                  | String            |
| header                 | No                                               | Header content                                                                          | Header            |
| body                   | Yes                                              | Main text                                                                               | Body              |
| footer                 | No                                               | Footer content                                                                          | Footer            |
| listAction             | When the messageInteractiveType is LIST          | Contains parameters of a list message                                                   | ListAction        |
| replyButtonAction      | When the messageInteractiveType is REPLY\_BUTTON | Contains parameters of a reply button message                                           | ReplyButtonAction |
| alternativeText        | No                                               | Text that will be sent if the user’s mobile phone does not support interactive messages | String            |

#### Header

If the message has a header, **exactly one of the fields below must be filled**.

If the message type is LIST only the text field is accepted.

| Field    | Details                                                                    | Type     |
| -------- | -------------------------------------------------------------------------- | -------- |
| text     | Header text. Maximum 60 characters. Allows the use of emojis and markdown. | String   |
| document | Complex Document object.                                                   | Document |
| video    | Complex Video object.                                                      | Video    |
| image    | Complex Image object.                                                      | Image    |
| location | Complex Location object.                                                   | Location |

**Image**

| Field | Required | Details                                                                                          | Type   |
| ----- | -------- | ------------------------------------------------------------------------------------------------ | ------ |
| type  | Yes      | Type/extension of the image that will be sent in the message. Available options: JPG, JPEG, PNG. | String |
| url   | Yes      | URL of the content (image) that will be sent.                                                    | String |

**Video**

| Field | Required | Details                                                                               | Type   |
| ----- | -------- | ------------------------------------------------------------------------------------- | ------ |
| type  | Yes      | Type/extension of the video that will be sent in the message. Available options: MP4. | String |
| url   | Yes      | URL of the content (video) that will be sent.                                         | String |

**Document**

| Field | Required | Details                                                                                  | Type   |
| ----- | -------- | ---------------------------------------------------------------------------------------- | ------ |
| type  | Yes      | Type/extension of the document that will be sent in the message. Available options: PDF. | String |
| url   | Yes      | URL of the content (document) that will be sent.                                         | String |

**Location**

| Field    | Required | Details                                       | Type   |
| -------- | -------- | --------------------------------------------- | ------ |
| name     | No       | Location name.                                | String |
| address  | No       | Location address.                             | String |
| geoPoint | Yes      | Coordinates in the format: latitude,longitude | String |

#### Body/Footer

| Field | Required | Details                                                                                                                  | Type   |
| ----- | -------- | ------------------------------------------------------------------------------------------------------------------------ | ------ |
| text  | Yes      | Cannot be an empty string. Allows for emojis and markdown. Body: Maximum 1024 characters. Footer: Maximum 60 characters. | String |

#### ListAction

| Field    | Required | Details                                           | Type       |
| -------- | -------- | ------------------------------------------------- | ---------- |
| button   | Yes      | Content to be written inside the button.          | String     |
| sections | Yes      | List of sections. Must have at least one section. | Section\[] |

**Section**

| Field | Required | Details                                                                   | Type   |
| ----- | -------- | ------------------------------------------------------------------------- | ------ |
| rows  | Yes      | List rows. Must have at least one row and at most 10 adding all sections. | Row\[] |

**Row**

| Field       | Required | Details         | Type   |
| ----------- | -------- | --------------- | ------ |
| identifier  | Yes      | Row identifier  | String |
| title       | Yes      | Row title       | String |
| description | No       | Row description | String |

#### ReplyButtonAction

| Field   | Required | Details                      | Type      |
| ------- | -------- | ---------------------------- | --------- |
| buttons | Yes      | List with 1, 2, or 3 Buttons | Button\[] |

**Button**

| Field | Required | Details          | Type  |
| ----- | -------- | ---------------- | ----- |
| reply | Yes      | Button structure | Reply |

**Reply**

| Field   | Required | Details                                                             | Type   |
| ------- | -------- | ------------------------------------------------------------------- | ------ |
| title   | Yes      | Text to be written inside the button. Maximum 20 characters.        | String |
| payload | Yes      | Information to be returned in the callback. Maximum 256 characters. | String |

### Request Examples

**LIST**

```
{
 "destinations": [
 {
 "correlationId": "MyCorrelationId",
 "destination": "5519900001111"
 }
 ],
 "message": {
 "interactive": {
 "messageInteractiveType": "LIST",
 "header": {
 "text": "Sample text"
 },
 "body": {
 "text": "Main message text"
 },
 "footer": {
 "text": "Footer text"
 },
 "listAction": {
 "button": "button text",
 "sections": [
 {
 "rows": [
 {
 "identifier": "9ab8d65e-d389-4123-b97b-702e658cc9e4",
 "title": "August 7, 11:00",
 "description": "Saturday, August 7, 2021. 11:00AM"
 },
 {
 "identifier": "2051afef-e000-47d0-99a5-7d96c17968b2",
 "title": "August 7, 15:00",
 "description": "Saturday, August 7, 2021. 3:00PM"
 },
 {
 "identifier": "55baac93-a513-45d0-ad9e-2e2271861fc8",
 "title": "August 9, 11:00",
 "description": "Monday, August 9, 2021. 11:00AM"
 },
 {
 "identifier": "e2703f03-689c-4d1e-b0e9-4045d6687605",
 "title": "August 9, 15:00",
 "description": "Monday, August 9, 2021. 4:00PM"
 }
 ]
 }
 ]
 },
 "alternativeText": "Simple message text"
 }
 }
}
```

**REPLY\_BUTTON**

```
{
 "destinations": [
 {
 "correlationId": "MyCorrelationId",
 "destination": "5519900001111"
 }
 ],
 "message": {
 "interactive": {
 "messageInteractiveType": "REPLY_BUTTON",
 "header": {
 "text": "Sample text",
 "image": {
 "type": "JPG",
 "url": "http://...jpg"
 },
 "video": {
 "type": "MP4",
 "url": "http://...mp4"
 },
 "document": {
 "type": "PDF",
 "url": "http://...pdf"
 },
 "location": {
 "geoPoint": "-22.894180,-47.047960",
 "name": "Wavy",
 "address": "Av. Cel. Silva Telles"
 }
 },
 "body": {
 "text": "Main message text"
 },
 "footer": {
 "text": "Footer text"
 },
 "replyButtonAction": {
 "buttons": [
 {
 "reply": {
 "title": "Display Text 1",
 "payload": "callback_payload_1"
 }
 },
 {
 "reply": {
 "title": "Display Text 2",
 "payload": "callback_payload_2"
 }
 }
 ],
 },
 "alternativeText": "Simple message text"
 }
 }
}
```

## Interactive Message Callback

#### Callback

| Field      | Details                                                  | Type       |
| ---------- | -------------------------------------------------------- | ---------- |
| total      | Number of callbacks in this request                      | Long       |
| data       | List of messages sent by the user                        | Data\[]    |
| clientInfo | Information of the client that is receiving the messages | ClientInfo |

#### Data

| Field         | Details                                                                                           | Type        |
| ------------- | ------------------------------------------------------------------------------------------------- | ----------- |
| id            | Message identifier                                                                                | String      |
| source        | Phone number of who sent the message                                                              | String      |
| origin        | Phone number of the WhatsApp Account that received the message                                    | String      |
| userProfile   | User profile who sent the message                                                                 | UserProfile |
| correlationId | Unique ID sent by the customer when sending the message to be returned in the callback. Optional. | String      |
| campaignId    | Campaign related to the message                                                                   | String      |
| campaignAlias | Alias of the campaign related to the message                                                      | String      |
| message       | Message received                                                                                  | Message     |
| receivedDate  | Date the message was received. Format: yyyy-MM-dd’T'HH:mm:ssZ                                     | String      |
| receivedAt    | Date the message was received, using Unix\_time format                                            | Long        |
| extraInfo     | Extra information related to the message. Format: Json                                            | String      |
| session       | Session information                                                                               | Session     |

#### UserProfile

| Field      | Details           | Type   |
| ---------- | ----------------- | ------ |
| name       | WhatsApp username | String |
| whatsAppId | User phone number | String |

#### Session

| Field     | Details                            | Type   |
| --------- | ---------------------------------- | ------ |
| sessionId | Id of this user’s session          | String |
| createdAt | Creation timestamp of this session | Long   |

#### Message

| Field           | Details                                                                                                 | Type                |
| --------------- | ------------------------------------------------------------------------------------------------------- | ------------------- |
| type            | Type of message sent by the user: TEXT - IMAGE - AUDIO - DOCUMENT - STICKER - BUTTON - ORDER            | String              |
| **messageText** | Text of the message sent by the user. For list replies, it is the same as the rowTitle the user clicked | String              |
| mediaUrl        | Url to download media sent by the user                                                                  | String              |
| mimeType        | Mime type of the file sent by the user                                                                  | String              |
| caption         | Label of media sent by the user                                                                         | String              |
| location        | Location sent by the user                                                                               | Location            |
| contacts        | List of contacts sent by the user                                                                       | Contact\[]          |
| interactive     | Fields related to interactive messages                                                                  | ReceivedInteractive |

#### ReceivedInteractive

| Field       | Details                                                           | Type        |
| ----------- | ----------------------------------------------------------------- | ----------- |
| type        | Type of interactive message. Can be: LIST\_REPLY or BUTTON\_REPLY | String      |
| listReply   | List reply (LIST)                                                 | ListReply   |
| buttonReply | Button reply (REPLY\_BUTTON)                                      | ButtonReply |

**ListReply**

| Field         | Details                                 | Type   |
| ------------- | --------------------------------------- | ------ |
| rowIdentifier | Identifier of the row the user selected | String |
| rowTitle      | Title of the row the user selected      | String |

**ButtonReply**

| Field   | Details                                     | Type   |
| ------- | ------------------------------------------- | ------ |
| payload | Text set at the time of sending the message | String |
| title   | Title of the button the user clicked        | String |

#### ClientInfo

| Field        | Details                                               | Type |
| ------------ | ----------------------------------------------------- | ---- |
| customerId   | customerId of the customer who receives the message   | Long |
| subAccountId | subAccountId of the customer who receives the message | Long |
| userId       | userId of the customer who receives the message       | Long |


# WhatsApp Lists via API

Technical Documentation: WhatsApp Lists via API

### **Consulting Lists via API**

**OPT IN/OUT & BLACK/WHITE LIST**

**API - Possible list request types:**

* OPT IN
* OPT OUT
* BLACK LIST
* WHITE LIST
* OPEN SESSIONS

**Request**

You need to make a GET request to the URL ***<http://api-messaging.wavy.global/v1/list/{listType}?customerId={customerId}\\&subAccountId={subAccountId}>***.

| List Type                       | Value relayed in listType |
| ------------------------------- | ------------------------- |
| **WhatsApp OPT-OUT List**       | OPTOUT                    |
| **WhatsApp OPT-IN List**        | OPTIN                     |
| **WhatsApp Blacklist**          | BLACKLIST                 |
| **WhatsApp Whitelist (for MT)** | WHITELIST                 |

The ***customerId*** parameter is required, while ***subAccountId*** is optional. You should also relay the following headers:

| ​                       | ​                   |
| ----------------------- | ------------------- |
| **Content-Type**        | application/json    |
| **authenticationToken** | Messaging1 token    |
| **userName**            | Messaging1 username |

**Response**

If successful, if there is any data related to the customerId and subAccountId (if specified), the request will return a JSON with 3 attributes:

| ​           | ​                                                                                                    |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| **success** | true                                                                                                 |
| **status**  | 200                                                                                                  |
| **data**    | Link to download a csv file containing the “source” and “createdAt” fields of all destinations found |

**If there is no associated data, only a similar JSON will be returned, but without the data field, which means no issues occurred with the request, but there weren’t any data related to the parameters relayed.**

**​**


# WhatsApp Messaging via SFTP

Here is the WhatsApp messaging via FTP process.

#### Connection Details <a href="#connection-details" id="connection-details"></a>

|                    |                                                              |
| ------------------ | ------------------------------------------------------------ |
| **Hostname**       | ftp-messaging.wavy.global                                    |
| **Port**           | 2222                                                         |
| **Protocol**       | SFTP (transfer over ssh, providing client-server encryption) |
| **Authentication** | username + password (supplied by our tech support)           |

<mark style="color:red;">**It is necessary to add your IPs to our firewalls authorized IPs list!**</mark>

If it is necessary to get firewall allowance for the port 2222, you must allow the DNS, or the IPs 200.219.220.54 and 45.236.179.22

**This document is intended as a guide for messages sent through the new WhatsApp messaging via FTP format**

* The file format was based on sending an SMS file via FTP.
* Sending HSMs will be possible in this first version.

**To trigger messages via FTP, you must generate a file with the formatting in the example below:**

**HSM Message:**

```
2018-10-16;10:00;20:00;HSM;chatclub_welcome;EN;DETERMINISTIC;name|company
phone;name;company
551999999999;Name1;Sinch
551999999999;Name2;Sinch
```

| 1st line:                                               |
| ------------------------------------------------------- |
| Send date (for scheduling cases)                        |
| Start send time (for scheduling cases)                  |
| End send time (for scheduling cases)                    |
| Message type must be: **HSM**                           |
| HSM name (elementName)                                  |
| HSM language (languageLocale)                           |
| HSM language Deterministic or Fallback (languagePolicy) |
| name of HSM parameters                                  |

**Notes for the first line:**

1. Parameter names must match the column names
2. Information that will not be used may be left blank, **however** you should keep the semicolon as separation. Example of a case where we did not use scheduling (the first fields are between semicolons and have no information within): ; ; ; HSM;chatclub\_welcome;pt\_BR;DETERMINISTIC;name|company
3. By default, the languagePolicy will be **Deterministic.**
4. The names of HSM parameters should be separated by **" | " and not by " ; "**

| 2nd line:                              |
| -------------------------------------- |
| Column names                           |
| 3rd and remaining lines:               |
| Recipient and values of HSM parameters |

**​**


# Campaigns API

Technical Documentation: Campaigns API

## Authentication

Authentication for queries via API has a standard format, and you must provide a valid username (email) associated with authentication token (see how to access your data). You must add the following headers to the request:

| Field             | Details                                                                                                                                              | Data Type |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| UserName          | Valid e-mail subscribed in ChatClub Platform.                                                                                                        | String    |
| AutenticaçãoToken | Authentication token generated by our platform. Find it [here](https://messaging.movile.com/messaging/user/api_configuration)​ or check our support. | String    |

## Connection Details

| **Hostname**       | apigw\.wavy.global     |
| ------------------ | ---------------------- |
| **Port**           | 443 (https)            |
| **Protocol**       | HTTPS (TLS encryption) |
| **Authentication** | username + token       |
| **Encoding**       | UTF-8                  |

## Listing Campaigns

List of campaigns already registered in the platform. You can page results or filter by campaign name.

GET <https://apigw.wavy.global/api/v1/campaigns>

### QueryString Parameters

\* Required field

| Field      | Details                                            | Type    |
| ---------- | -------------------------------------------------- | ------- |
| name       | Campaign’s name to be used as a filter for listing | String  |
| page       | Page to be listed                                  | Integer |
| page\_size | Total campaigns per page                           | Integer |

Positive response

HEADERS:

```
page-number: 1
per-page: 10
total: 2
total-pages: 1
```

### Informing the total number of campaigns there are and Displaying right below:

```
{
 "status": {
 "error": false
 },
 "campaigns": [
 {
 "name": "My first campaign",
 "id": 1,
 "alias": "first"
 },
 {
 "name": "My second campaign",
 "id": 2,
 "alias": "second"
 }
 ]
}
```

### Showing

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGhsmOlT1CwS5Md1dR%2F-MlGmR-L9lp46KD_pyzt%2F0.gif?generation=1633459749638643\&alt=media)

## Requesting for a Campaign

Requests for the data of a campaign by registration ID

You need to know the registration ID in advance

GET <https://apigw.wavy.global/api/v1/campaign/{id}>

## Creating a Campaign

Example of campaign creation:

Creating a new campaign with name and alias. The campaign alias should be a simple name to make it easier to use with the API. It is recommended to be short and do not use special characters.

POST <https://apigw.wavy.global/api/v1/campaigns>

### JSON Parameters

\* Required field

| Field  | Details                                   | Type   |
| ------ | ----------------------------------------- | ------ |
| name\* | Campaign name                             | String |
| alias  | Campaign identifier to be used in the API | String |

`Call`

```

{
 "campaign" : {
 "name": "My Campaign2019",
 "alias": "mycampaign2019"
 }
 }
Response
{
 "status": {
 "error": false
 },
 "campaign": {
 "name": "My Campaign",
 "id": 1234,
 "alias": "mycampaign"
 }
}
```

!\[Graphical user interface

Description automatically generated]\(<https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGhsmOlT1CwS5Md1dR%2F-MlGmR-MEovVYrF_1GGM%2F1.gif?generation=1633459749638737\\&alt=media>)

## Changing a Campaign

Changing a campaign by modifying its name and/or alias.

PUT <https://apigw.wavy.global/api/v1/campaigns/{id}>

You must include the {id} of the campaign you wish to change

### JSON Parameters

\* Required field

| Field  | Details                                   | Type   |
| ------ | ----------------------------------------- | ------ |
| name\* | Campaign name                             | String |
| alias  | Campaign identifier to be used in the API | String |

Call

```
{
 "campaign" : {
 "name": "My Campaign",
 "alias": "mycampaign"
 }
 }
Response
{
 "status": {
 "error": false
 },
 "campaign": {
 "name": "My Campaign",
 "id": 1234,
 "alias": "mycampaign"
 }
}

```

## Deleting a Campaign

Deleting a campaign by its ID.

DELETE <https://apigw.wavy.global/api/v1/campaigns/{id}>

You must include the {id} of the campaign you wish to change


# TTL - Time to Live

Messaging with TTL (Time to Live - The HSM’s lifespan before being delivered)

## Messaging with TTL (Time to Live - The HSM’s lifespan before being delivered)

**Feature Description:**

### From v2.21.3 **(**[**https://developers.facebook.com/docs/whatsapp/changelog#app**](https://developers.facebook.com/docs/whatsapp/changelog#app)**) onwards**, you can inform the TTL (in days) for the delivery of your messages to expire (i.e., their Time to Live).

* Companies can use this to ensure messages aren’t delivered on dates later than what was set.
* Currently, TTL **can only be set for HSM messages (**[**access HSM information**](https://docs.wavy.global/whatsapp/hsm-template)**).**
* If a message is not delivered to the customer before the period set as limit, i.e. it expires, then the message will no longer be delivered.
* A status notification (CallBack) will be sent by WA.
* The status notification can be sent to our customers so long as it is configured.

{% hint style="warning" %}
**IMPORTANT: setting a TTL has the following limitations:**

* Only HSM messages
* minimum 1 day (24 hours) from the time the message is sent
* maximum 30 days
* default 7 days. (Currently, this value can be altered)
* the TTL is effective from the moment your message is sent, that is, if a message is scheduled, the TTL will be attributed by adding the value to the date when it was triggered.
* If a message receives a value of less than 1 day or greater than 30 days, our platform will, at the time of delivery, attribute values within the permitted limit.
* This behavior has been implemented to prevent us from having issues when delivering messages, as, if there is an attempt to deliver a message that does not observe the minimum and maximum TTL values, this message will be denied by the container.
  {% endhint %}

## Call for Messaging via **FTP with TTL**

Messaging exampl&#x65;**:** 2019-01-18;11:0;11:15;HSM;chatclub\_welcome;pt\_BR;DETERMINISTIC;name|company;**2** phone;name;company 5519998873499;mozart;wavy 5519981794226;diego;wavy The information that represents the **TTL** is at the end of the first line, after the **HSM** parameter&#x73;**.**

This information will be an **INTEGER** that is represented in number of days. That is, we will have a 2-day **TTL**. This means that, after 2 days from the date and time the message is sent, if the recipient has not received the message, this message **WILL NO LONGER BE DELIVERED.**

## **Call for Messaging via API with TTL**

```
{
 "destinations": [{
 "correlationId": "MyCorrelationId",
 "destination": "5519900001111"
 }],
 "message": {
 "ttl": 1,
 "hsm": {
 "namespace": "namespace",
 "elementName": "elementName",
 "parameters":[
 "MyParam1",
 "MyParam2"
 ]
 }
 }
 }
```


# Webhook

## **Webhook**

### **How Do Webhooks Work?**

When we trigger a message from our platform, we receive in return some information; this information can be shared with our customers and directed for other support channels to take any actions.

For instance, we can trigger an HSM from our platform and, if the customer replies with an MO, we can send the information to the webhook of a support channel, where a human conversation is initiated between agent and user.

### **How do I Set Up My Webhook?**

Today, to set up your webhook, just open a ticket through our portal with Wavy’s Customer Service at [Service Center](https://service.sinch.com) and we will help you with your setup.

### **Technical Information**

It is important that this webhook has an HTTPS connection, as this formo f connection is the most secure way to transfer data between computer networks on the internet.


# Glossary - Status Page Components

<table><thead><tr><th width="161.5" align="center">Field</th><th align="center">Description</th></tr></thead><tbody><tr><td align="center"><strong>SMPP</strong></td><td align="center">Specific protocol made to exchange SMS messages, it permits a active connection with the SMPP servers, it is recommended to the clients that have 5 millions or more messages per month The instability in this component affects in general form the sending and receiving of messages trough your API SMPP.</td></tr><tr><td align="center"><strong>Web service API</strong></td><td align="center">This API permits that you automatize the sending messages requisitions, unique or in lot, and the recovery of the sending status trough consultations. She utilizes the HTTP protocol with TLS and accepts the GET methods, with the passage of parameters in the query string or POST with parameters in JSON The instability in this service affects in general form the sending and receiving of SMS trought the API.</td></tr><tr><td align="center"><strong>Web Interface</strong></td><td align="center">This component refers at your platform <a href="https://messaging.wavy.global">Messaging</a>. The instability in this service can affects the sending and receiving of SMS and Whatsapp messages trough our platform.</td></tr><tr><td align="center"><strong>Webhook DLR (delivery to handset)</strong></td><td align="center">The instability in this component directly affects the delivery to handset status in your Webhook.</td></tr><tr><td align="center"><strong>SMPP DLR (delivery to handset)</strong></td><td align="center">The instability in this component directly affects the delivery to handset status in your API SMPP.</td></tr><tr><td align="center"><strong>SMPP Callback (delivery to carrier)</strong></td><td align="center">The instability in this component directly affects the delivery to carrier status in your Webhook.</td></tr><tr><td align="center"><strong>Webhook Callback (delivery to carrier)</strong></td><td align="center">The instability in this component directly affects the delivery to handset status in your API SMPP.</td></tr><tr><td align="center"><strong>Carrier</strong></td><td align="center">The instability in the carrier is linked whit the service outage provided by the carrier, when this happens we can expect delays on the sending and in the receiving of messages, we inform the carrier about the delay and we stabilize our messages rows in our side, this instability and your resolution time can vary from carrier to carrier.</td></tr><tr><td align="center"><strong>Internal Queues MT</strong></td><td align="center">The instability in this integration is linked directly with the sending of messages trough Whatsapp, when this happens, we can expect delays in the delivery of that message, until the message row is gradually emptied.</td></tr><tr><td align="center"><strong>Internal Queues (MO)</strong></td><td align="center">The instability in this integration is linked directly with the receiving  of messages trough Whatsapp, when this happens, we can expect delays in the receiving of that message, until the message row is gradually emptied.</td></tr></tbody></table>


# Components status page

This part of the documentation is intended to explain what each of the components of our status page (https\://status.wavy.global) do when they have instabilities.


# Integrations

Here are the articles in this section:

{% content-ref url="integrations/smpp" %}
[smpp](https://docs-latam.messaging.sinch.com/status-page/components-status-page/integrations/smpp)
{% endcontent-ref %}

{% content-ref url="integrations/web-service-api" %}
[web-service-api](https://docs-latam.messaging.sinch.com/status-page/components-status-page/integrations/web-service-api)
{% endcontent-ref %}

{% content-ref url="integrations/web-interface" %}
[web-interface](https://docs-latam.messaging.sinch.com/status-page/components-status-page/integrations/web-interface)
{% endcontent-ref %}


# SMPP

Specific protocol made to exchange SMS messages, it permits a active connection with the SMPP servers, it is recommended to the clients that have 5 millions or more messages per month

The instability in this component affects in general form the sending and receiving of messages trough your API SMPP&#x20;


# Web service API

This API permits that you automatize the sending messages requisitions, unique or in lot, and the recovery of the sending status trough consultations. She utilizes the HTTP protocol with TLS and accepts the GET methods, with the passage of parameters in the query string or POST with parameters in JSON

The instability in this service affects in general form the sending and receiving of SMS trought the API


# Web Interface

This component refers at your platform <https://messaging2.movile.com/>

The instability in this service can affects the sending and receiving of SMS and Whatsapp messages trough our platform


# Callback / Delivery Report

Here are the articles in this section:

{% content-ref url="callback-delivery-report/webhook-dlr-delivery-to-handset" %}
[webhook-dlr-delivery-to-handset](https://docs-latam.messaging.sinch.com/status-page/components-status-page/callback-delivery-report/webhook-dlr-delivery-to-handset)
{% endcontent-ref %}

{% content-ref url="callback-delivery-report/smpp-dlr-delivery-to-handset" %}
[smpp-dlr-delivery-to-handset](https://docs-latam.messaging.sinch.com/status-page/components-status-page/callback-delivery-report/smpp-dlr-delivery-to-handset)
{% endcontent-ref %}

{% content-ref url="callback-delivery-report/smpp-callback-delivery-to-carrier" %}
[smpp-callback-delivery-to-carrier](https://docs-latam.messaging.sinch.com/status-page/components-status-page/callback-delivery-report/smpp-callback-delivery-to-carrier)
{% endcontent-ref %}

{% content-ref url="callback-delivery-report/webhook-callback-delivery-to-carrier" %}
[webhook-callback-delivery-to-carrier](https://docs-latam.messaging.sinch.com/status-page/components-status-page/callback-delivery-report/webhook-callback-delivery-to-carrier)
{% endcontent-ref %}


# Webhook DLR (delivery to handset)

The instability in this component directly affects the delivery to handset status in your Webhook


# SMPP DLR (delivery to handset)

The instability in this component directly affects the delivery to handset status in your API SMPP


# SMPP Callback (delivery to carrier)

&#x20;The instability in this component directly affects the delivery to carrier status in your Webhook


# Webhook Callback (delivery to carrier)

The instability in this component directly affects the delivery to handset status in your API SMPP


# OPERATORS

The instability in the carrier is linked whit the service outage provided by the carrier, when this happens we can expect delays on the sending and in the receiving of messages, we inform the carrier about the delay and we stabilize our messages rows in our side, this instability and your resolution time can vary from carrier to carrier


# WhatsApp Sending messages to the user (MT)

Here are the articles in this section:

{% content-ref url="whatsapp-sending-messages-to-the-user-mt/internal-queues-mt" %}
[internal-queues-mt](https://docs-latam.messaging.sinch.com/status-page/components-status-page/whatsapp-sending-messages-to-the-user-mt/internal-queues-mt)
{% endcontent-ref %}


# Internal Queues MT

The instability in this integration is linked directly with the sending of messages trough Whatsapp, when this happens, we can expect delays in the delivery of that message, until the message row is gradually emptied


# WhatsApp Receiving User Messages (MO)

Here are the articles in this section:

{% content-ref url="whatsapp-receiving-user-messages-mo/internal-queues-mo" %}
[internal-queues-mo](https://docs-latam.messaging.sinch.com/status-page/components-status-page/whatsapp-receiving-user-messages-mo/internal-queues-mo)
{% endcontent-ref %}


# Internal Queues (MO)

The instability in this integration is linked directly with the receiving  of messages trough Whatsapp, when this happens, we can expect delays in the receiving of that message, until the message row is gradually emptied


