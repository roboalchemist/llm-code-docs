# Source: https://docs.deepconverse.com/product-docs/chatbots/advanced-functionality/channel-specific-functionality/zendesk-sunshine-conversations/how-to-handle-image-and-file-uploads-in-zendesk-sunshine-conversations.md

# How to handle image and file uploads in Zendesk Sunshine Conversations?

When using the Zendesk Sunshine Conversations channel you can accept file and image attachments from customers. This allows supporting use cases such as:

* Returns Automation
* Proof of Purchase Validation
* Product Documentation

Customers can upload file/images at any point in the conversation. These out of bound uploads are maintained in the conversation in Zendesk.

If you would like to accept a file/image upload at a certain point you case use the **Zendesk Sunshine Conversations File Upload** add on. What this does is wait for the user to upload a file and then progress the flow to the next step.

Example flow using the file upload:

![mceclip0.png](https://help.deepconverse.com/hc/article_attachments/8984578218132/mceclip0.png)

#### File Parameters&#x20;

After the user uploads you will have access to the following parameters:

| **Parameter** | **Purpose**                                    |
| ------------- | ---------------------------------------------- |
| fileName      | Name of the file uploaded by the customer      |
| fileUrl       | Media URL hosted by Zendesk                    |
| fileType      | Mime type of the file uploaded by the customer |

For additional details about supported file types and sizes refer to [Sunshine Conversations documentation](https://docs.smooch.io/guide/validating-files/)

### User Experience

Here is the conversation flow in action on Zendesk Sunshine Conversations web widget:

{% embed url="<https://www.loom.com/share/65a1fca7cda34ea292b4a0eaf84f33e3?sid=81025472-1082-44a9-b3e7-9321107846db>" %}
