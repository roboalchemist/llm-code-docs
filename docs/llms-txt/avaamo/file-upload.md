# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/file-upload.md

# File upload

You can add an input card with an option to upload files to your agent.&#x20;

{% hint style="success" %}
**Key points**:

* You can upload any type of file, however, the maximum limit for each file is 4GB.
* You can upload images of all types and resolutions. There is no restriction on the resolution of the image.
* There is a 191-character limit for all the user-defined text fields.
* For security reasons, by default, you can upload upto 10 files in a span of 60 seconds. The number of files and the frequency or interval within which they can be uploaded is a configurable parameter. Contact Avaamo Support, for further assistance.
* File upload is not supported in the Microsoft Teams channel due to the limitations on the channel's side. See [Microsoft Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information on deploying your agent in the MS Teams channel.&#x20;
  {% endhint %}

## Syntax

The following is the syntax to add an upload option in the card input:

```yaml
"card": {
 "inputs": [{
 "type": "file/file_group",
 "title": "<<upload_title>>",
 "uuid": "<<secure_random_uuid>>",
 *"should_validate": true/false,
 *"image_only": true/false
 },...]
}
* - Indicates optional parameter
… - Indicates one or more parameter
```

<table><thead><tr><th width="185.84132154490462">Attribute</th><th width="447.3895219496286">Description</th><th>Type</th></tr></thead><tbody><tr><td>title</td><td>Indicates the title of file upload.</td><td>String</td></tr><tr><td>type</td><td><p>Indicates if you wish to select a single file or multiple files at a time for uploading: </p><ul><li>file: This option allows you to select a single file</li><li>file_group: This option allows you to select multiple files at a time</li></ul></td><td>String</td></tr><tr><td>should_validate</td><td>Indicates if the user can skip uploading a file or not. By default, the value is set to true.</td><td>Boolean</td></tr><tr><td>uuid</td><td><p>Indicates a secure random UUID that can be used later to access the file uploaded by the user. See Section 4.4 in </p><p><a href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>, for more information. </p><p></p><p>File uploaded name is available in the <a href="https://docs.google.com/document/d/1kLeCPObAeXeon6viGnywY3_9HQxSmfs-YS-xB561Ekg/edit#heading=h.sprg97pwog6">context.last_message</a>.</p><p>Syntax: context.last_message.&#x3C;&#x3C;uuid>></p></td><td>String</td></tr><tr><td>image_only</td><td>Indicates if the file upload must allow uploading of only images or not. Set true to upload only images. By default, the value is false. Currently, this support is only for image file types.</td><td>Boolean</td></tr></tbody></table>

## Supported file types and size

Make a note of the following points related to the supported file types and sizes in the Avaamo Platform:

* You can upload any type of file, however, the maximum limit for each file is 4GB.
* You can upload images of all types and resolutions. There is no restriction on the resolution of the image.
* For security reasons, by default, you can upload upto 10 files in a span of 60 seconds. The number of files and the frequency or interval within which they can be uploaded is a configurable parameter. Contact Avaamo Support, for further assistance.

## Examples

The following examples of file upload are listed:

* [Single file upload](#single-file-upload)
* [Upload images only](#upload-images-only)
* [Access uploaded file and send email](#access-uploaded-file-and-send-email)
* [Upload multiple files](#upload-multiple-files)
* [Making file upload optional](#making-file-upload-optional)

### **Single file upload**&#x20;

The following is a sample JS to provide a file upload option:

```yaml
return {
  "card": {
    "inputs": [
      {
        "type": "file",
        "title": "Upload Profile Pic",
        "uuid": "2e6e7e36-657c-4390-ba06-fa80597871ae"
      }
    ]
  }
}
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FU2k8D0nzJuOjnFKQla78%2Fimage.png?alt=media\&token=a4d5a4f7-3de5-451f-8963-7ea544e67e83)

You can use `context.last_message.<<uuid>>` and `context.last_message.<<uuid>>.name` to access the name and identifier of the file that is uploaded.

### **Upload images only**

The following is a sample JS to provide a file upload option for images only:

```yaml
return {
  "card": {
    "inputs": [
      {
        "type": "file",
        "title": "Upload Profile Pic",
        "uuid": "ab4a6301-8961-430f-9e09-622ce3ca5aa3",
        "image_only": true
      }
    ]
  }
}
```

In the agent, the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FcEbJ5bmYLrRboKvWP863%2Fimage.png?alt=media\&token=daeb4b83-d655-41db-ad3c-96210655012e)

Note that when you click upload, only image file types are enabled for uploading.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Favaamo%2F-LpbpiLTBoXFi_Gj0Sed%2F-LpbqUUKEM8N2eb9Rp66%2F10.png?generation=1569405409918834\&alt=media)

You can use `context.last_message.<<uuid>>.uuid` and `context.last_message.<<uuid>>.name` to access the name and identifier of the file that is uploaded.

### Access the uploaded file and send an email

{% hint style="info" %}
**Note**: You can access the uploaded file only when files are not masked in the agent. See [Information masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking), for more information.
{% endhint %}

Get the **Access Token** from **Agent  -> Configuration -> Settings** page:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Lx_3LI-iCjerMSnRmwo%2F-Lx_5Ncr3_VAP4gLRrcc%2Fjs-file-upload-agent-access-token.png?alt=media&#x26;token=e1576750-afb7-414e-bd28-20f59980fbea" alt=""></div>

Add the following sample JS to access the uploaded file and send it as an email attachment:

```javascript
var access_token = "UoF4VLjeq9uH0dzki3-79gclgRpf8hr9"; // agent access Token
var url = "https://cxx.avaamo.com/files/" + context.last_message.<<uuid>>.uuid + ".json?size=original&access_token=" + access_token;
// here, uuid is the secure random uuid provided at the time of upload. 
// See File upload syntax for more information
try {
    var file_content = await (fetch(url).then(res => res.buffer()));
    var email_sender = await (Email.send({
        to: ["John@avaamo.com"],
        from: ["admin@macpizza.com"],
        subject: "Your Pizza Order",
        body: "Here, is the pic of your pizza baking right now!!! Enjoy.",
        attachments: [{
            filename: context.last_message.<<uuid>.name,
            content: file_content
        }]
    }));
    if (email_sender.status == 'SUCCESS') {
        return "Email Sent";
    } else {
        return "Failed to send email. Kindly try again later.";
    }
} catch (error) {
    return "Sorry, something unexpected happened when processing your request. Please try again later.";
}
```

{% hint style="info" %}
**Note:** The URL in the sample JS provided above is deprecated and is no longer available as of the v8.2.0 release. Instead, use `context.last_message.<<uuid>>.url`. Refer to the sample JS below for accessing the uploaded file and sending it as an email attachment:

```javascript
var access_token = "UoF4VLjeq9uH0dzki3-79gclgRpf8hr9"; // agent access Token
var url=context.last_message.<<uuid>>.url;
// here, uuid is the secure random uuid provided at the time of upload. 
// See File upload syntax for more information
try {
    var file_content = await (fetch(url).then(res => res.buffer()));
    var email_sender = await (Email.send({
        to: ["John@avaamo.com"],
        from: ["admin@macpizza.com"],
        subject: "Your Pizza Order",
        body: "Here, is the pic of your pizza baking right now!!! Enjoy.",
        attachments: [{
            filename: context.last_message.<<uuid>.name,
            content: file_content
        }]
    }));
    if (email_sender.status == 'SUCCESS') {
        return "Email Sent";
    } else {
        return "Failed to send email. Kindly try again later.";
    }
} catch (error) {
    return "Sorry, something unexpected happened when processing your request. Please try again later.";
}
```

{% endhint %}

### Upload multiple files

The following is a sample JS to provide upload multiple files using file upload:

```yaml
return {
  "card": {
    "inputs": [
      {
        "type": "file_group",
        "title": "Upload Passport and address copy",
        "uuid": "5dcf9d7e-8f72-4d3b-94dd-df502c42fbdd"
      }
    ]
  }
}
```

You can use `context.last_message.<<uuid>>` and `context.last_message.<<uuid>>.name` to access the name and identifier of the file that is uploaded.

### Making file upload optional

By default, when you use file upload via card, uploading a file is required. The system validates if the file is uploaded or not when the user clicks **Submit**. However, in certain cases, you can make the file upload optional.&#x20;

The following is a sample JS to show how you can make file upload an optional parameter. Note that you can set "should\_validate" to "false" if you wish to make file uploading optional.

```yaml
return {
  "card": {
    "inputs": [
     {
        "type": "file",
        "title": "Upload File",
        "uuid": "2e6e7e36-657c-4390-ba06-fa80597871ae",
        "should_validate": false
      }
    ]
  }
}
```

In the agent, you can submit the request successfully without uploading the file:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FOJaTZmOBgObqVzrrW7jZ%2Fimage.png?alt=media\&token=e45625d8-4486-4f6c-ae04-ec18ee4ff0ba)

If you have uploaded a file, then you can use `context.last_message.<<uuid>>` and `context.last_message.<<uuid>>.name` to access the name and identifier of the file that is uploaded.

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response)
{% endcontent-ref %}
