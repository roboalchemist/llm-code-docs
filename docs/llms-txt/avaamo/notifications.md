# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/notifications.md

# Notifications

The **SMS.send** and **Email.send** functions allows the agent to send notifications to the user.

### **SMS.send**

The following is the syntax to send SMS notifications:

```javascript
SMS.send("message", ["phoneNumber1","phoneNumber2",...],*{from_phone: channelPhone});

* - Indicates optional parameter
… - Indicates one or more parameters
```

<table><thead><tr><th width="339">Parameter</th><th>Description</th></tr></thead><tbody><tr><td>message</td><td>Indicates SMS message. The length of the message is according to the standard supported for SMS messages.</td></tr><tr><td>["phoneNumber1”,”phoneNumber2",...]</td><td>Indicates a comma-separated list of phone numbers prefixed with + followed by the country code.</td></tr><tr><td>from_phone</td><td>Indicates the number from which the SMS is sent.</td></tr></tbody></table>

#### **Example**

```javascript
SMS.send("Successfully placed order",["+16503835663", "+919999988888"]);
```

{% code overflow="wrap" %}

```javascript
SMS.send("Successfully placed order", ["+16503835663", "+919999988888"], {from_phone: "+19809890090"});
```

{% endcode %}

### Email.send

The following is the syntax to send Email notifications:

```javascript
Email.send({to: ["<<toMailId_1>>","<<toMailId_2>>",...],
*cc: ["<<ccMailId_1>>","<<ccMailId_2>>",...],
*bcc: ["<<bccMailId_1>>","<<bccMailId_2>>",...],
from: "<<fromMailId>>",
*subject: "<<emailSubject>>",
*body: "<<plainTextMessage>>",
*html:`<<html>>`,
*attachments:[
{filename:"<<filename1>>",content:"<<base64EncodedFormat>>",encoding:"base64"},
{filename:"<<filename2>>",content:"<<base64EncodedFormat>>",encoding:"base64"},
...] });

* - Indicates optional parameter
… - Indicates one or more parameters
```

| **Parameter**                                                                                                                                                                                                                                                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| to: \["<\<toMailId\_1>>",<\<toMailId\_2>>",...]                                                                                                                                                                                                               | Indicates a comma separated list of the recipient email Ids. It is mandatory to specify at-least one recipient email Id.                                                                                                                                                                                                                                                                                                                                    |
| \*cc: \["<\<ccMailId\_1>>","<\<ccMailId\_2>>",...]                                                                                                                                                                                                            | Indicates a comma-separated list of the cc email Ids. This is an optional parameter.                                                                                                                                                                                                                                                                                                                                                                        |
| \*bcc: \["<\<bccMailId\_1>>","<\<bccMailId\_2>>",...]                                                                                                                                                                                                         | Indicates a comma-separated list of the bcc email Ids. This is an optional parameter.                                                                                                                                                                                                                                                                                                                                                                       |
| from: "<\<fromMailId>>"                                                                                                                                                                                                                                       | Indicates the email Id of the sender.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \*subject: "<\<emailSubject>>"                                                                                                                                                                                                                                | Indicates the subject of the email. This is an optional parameter                                                                                                                                                                                                                                                                                                                                                                                           |
| \*body: "<\<plainTextMessage>>"                                                                                                                                                                                                                               | <p>Indicates the body of email message in plain text format. Use can use <strong>html</strong> to send HTML formatted messages in email.</p><p>Note that if you use <strong>body</strong> and <strong>html</strong> both to send an email message, then the message in <strong>html</strong> takes precedence over the message in the <strong>body</strong>.</p>                                                                                            |
| \*html:\`<\<html>>\`                                                                                                                                                                                                                                          | <p>Indicates the body of the email message in HTML format. To embed image attachments, add an HTML tag - <strong>\<img src="cid:<\<contentId>>>"/></strong>.</p><p>Similarly, you can also embed any other files such as text, pdf.</p><p>Note that if you use <strong>body</strong> and <strong>html</strong> both to send an email message, then the message in <strong>html</strong> takes precedence over the message in the <strong>body</strong>.</p> |
| <p>\*attachments:\[{</p><p>filename:"<\<filename1>>",</p><p>content:"<\<base64EncodedFormat>>",</p><p>encoding: "base64"</p><p>},</p><p>{</p><p>filename:"<\<filename2>>",</p><p>content:"<\<base64EncodedFormat>>",</p><p>encoding: "base64"</p><p>},...</p> | <p>Indicates an array of attachments sent in the email. Each attachment must include the following parameters:</p><ul><li><strong>filename</strong>: Name of the file attached.</li><li><strong>content</strong>: Base64 encoded format for the file.</li><li><strong>encoding</strong>: Currently, the supported format is "base64".</li><li>Each attachment size < 10 MB</li></ul>                                                                        |

**Examples:** The following lists a few examples to send email notifications from the agent:

**Plain text message**:

```html
Email.send({
            to: ["john@avaamo.com"],
                from: ["admin@macpizza.com"],
                subject: "Mac Pizza Order Placed Successfully.",
                body: "Thank you for placing order. Your order has been placed successfully and will be delivered soon. Visit Mac Pizza website for more details."
            })
```

**HTML message**:

```html
Email.send({
    from: ["admin@macpizza.com"],
    to: ["john@avaamo.com"],
    subject: "Mac Pizza Order Placed Successfully.",
    html: `<!DOCTYPE html>
<html>
<body>
<h2>Order Details</h2>
<p> Thank you for placing order. Your order has been placed successfully and will be delivered soon. Visit Mac Pizza website for more details.</p>
<table style="width:100%">
 <tr>
 <th>Order Number</th>
 <th>Description</th>
 <th>Price</th>
 </tr>
 <tr>
 <td>b56789</td>
 <td>Cheese Pan Pizza, Regular</td>
 <td>$10</td>
 </tr>
 <tr>
 <td>b8976</td>
 <td>Corn Hand Tossed Pizza, Large</td>
 <td>$20</td>
 </tr>
</table>
<p> Total = $30 </p>
</body>
</html>`
})
```

**Image attachment in the message:**

```
Email.send({
    from: ["admin@macpizza.com"],
    to: ["john@avaamo.com"],
    subject: "Mac Pizza Order Placed Successfully.",
    body: "Thank you for placing order. Your order has been placed successfully and will be delivered soon. Visit Mac Pizza website for more details.",
    attachments: [{
        filename: 'veg-pizza.png',
        content: '<<base64 encoded format>>',
        encoding: 'base64'
    }]
})
```

&#x20;**Image in the email message**:

```
Email.send({
    from: ["admin@macpizza.com"],
    to: ["john@avaamo.com"],
    subject: "Mac Pizza Order Placed Successfully.",
    html: `Embedded image: <img src="cid:uniqubalh"/>.`,
    attachments: [{
        filename: 'veg-pizza.png',
        content: '<<base64 encoded format>>',
        encoding: 'base64'
    }]
})
```
