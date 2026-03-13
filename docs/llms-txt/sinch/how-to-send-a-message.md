# Source: https://docs.sinch.com/send-a-message/how-to-send-a-message.md

# How to Send a Message

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
