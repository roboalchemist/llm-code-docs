# Source: https://documentation.onesignal.com/docs/en/gdpr-compliance.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GDPR & Individual Rights

> OneSignal provides the following solutions to help be GDPR compliant.

If your business operates in any way, shape, or form in the EU, or with citizens of the EU, then you must comply with the General Data Protection Regulation (GDPR) framework. OneSignal can help your activities in the customer engagement space to remain compliant with the GDPR guidelines through purpose built APIs and SDKs. In this section, OneSignal will outline what tools are provided to clients to adhere to the regulation and maintaining individual rights afforded to EU citizen through the GDPR framework.

## The Right to be Informed

<Steps>
  <Step title="What does it mean" icon="question">
    Individuals have the right to be informed about the collection and use of their personal data. It is your responsibility to provide individuals with information including: your purposes for processing their personal data, your retention periods for that personal data, and who it will be shared with. Relevant in the context of using OneSignal for your messaging is informing your users who their information will be shared with.
  </Step>

  <Step title="How to prepare" icon="check">
    OneSignal provides a purpose built SDK with methods that delay the initialization of data collection. If called, you will have the opportunity to inform users of your intent when capturing individual permissions for notifications. For more information on setting up please view our [Handling Personal Data guide](./handling-personal-data). For more information on how OneSignal processes the data of your users please view the [Privacy Policy](https://onesignal.com/privacy_policy).
  </Step>
</Steps>

## The Right of Access

<Steps>
  <Step title="What does it mean" icon="question">
    Individuals have the right to access and receive a copy of their personal data, and other supplementary information. This practice is commonly known as a Subject Access Request (SAR), a process that you must have in place in order to respond to a SAR.
  </Step>

  <Step title="How to prepare" icon="check">
    There are two easy-to-use ways to access individual level data that OneSignal holds on your behalf. First, within the OneSignal application you can search records by a unique identifier to view and export all data in CSV that is held on OneSignal's server. Second, you can call the [`View user` API endpoint](/reference/view-user) to retrieve the same information in JSON format. For detailed understanding of how to export user data please refer to this guide on [Exporting User Data](./exporting-data).

    OneSignal does not automatically collect any PII (Personally Identifiable Information) except for IP Addresses in countries outside the EU. We can disable all IP Address tracking if you wish.

    Any other data that might be considered PII can only be sent to us in the form of tags which you have full control over. Please review our [Handling Personal Data guide](./handling-personal-data) for more details.
  </Step>
</Steps>

## The Right of Rectification

<Steps>
  <Step title="What does it mean" icon="question">
    Individuals have the right to have inaccurate personal data rectified, or completed if it is incomplete. You have up to one calendar month to respond to a request.
  </Step>

  <Step title="How to prepare" icon="check">
    OneSignal provides you with a choice on how to rectify data tied to a personal record either through the online application or by calling OneSignal's purpose built API endpoint. Within the online application simply import data to either amend, add, or delete fields that are attributed to a specific identifier, here is a [guide on how to get started](./import).

    The other method to rectify data for an individual's request is through the [Update user](/reference/update-user) API.

    By using any of these methods you are in a position to rectify data immediately and view the amended record, thus helping to be compliant with this GDPR right by being able to respond within one calendar month.
  </Step>
</Steps>

## The Right to Erasure

<Steps>
  <Step title="What does it mean" icon="question">
    Also known as the "right to be forgotten", this article empowers individuals to request that their personal data be erased. However, this right is not absolute and can only be exercised under certain circumstances such as when the personal data is no longer necessary for the purpose which you originally collected or processed it for.
  </Step>

  <Step title="How to prepare" icon="check">
    We recommend you carefully locate and identify the individual user record that needs to be deleted as the action of deleting devices cannot be undone. It is sensible to use the [Delete user](/reference/delete-user) API endpoint as it processes one request at a time. However, you can delete bulk users within the online application if, for example, you respond to all erasure requests once every week and handle this in a batch. Please view this documentation for more information on [Deleting Users](./delete-users).
  </Step>
</Steps>

## The Right to Restrict Processing

<Steps>
  <Step title="What does it mean" icon="question">
    Individuals have, under certain circumstances, the right to restrict the processing of personal data which effectively means you are limited in how their data can be used within your organization. This right is an alternative to the right of erasure and it is important to note that there are limited number of circumstances in which this applies, for example when the individual contests the accuracy of their personal data and you are verifying the accuracy of the data.
  </Step>

  <Step title="How to prepare" icon="check">
    Following our [Handling Personal Data](./handling-personal-data) practices, you can setup your own application to not send OneSignal [Data Tags](./add-user-data-tags) depending on certain conditions you set within your app.
  </Step>
</Steps>

## The Right to Data Portability

<Steps>
  <Step title="What does it mean" icon="question">
    This right allows individuals to receive the personal data held in a structured, commonly used and machine readable format. Very similar to the Right of Access, it also entitles individuals to have their personal data transmitted between one data controller to another controller.
  </Step>

  <Step title="How to prepare" icon="check">
    OneSignal, as the data processor, will make it easy for you to access and extract data held on a specified individual. Within the online application or through our API, you can generate a CSV export file for a user record or you can access the [View user](/reference/view-user) API to retrieve all data in JSON format.
  </Step>
</Steps>

## The Right to Object

<Steps>
  <Step title="What does it mean" icon="question">
    Individuals have the right to object of processing their personal data at any time. When exercised, you are required to stop processing the data subjects' personal data. This objection may be in relation to all personal data or can relate to a particular purpose you are processing the data for, for example with notifications.
  </Step>

  <Step title="How to prepare" icon="check">
    If this right is exercised by an individual you may need to follow the steps outlined above under "The Right to Restrict Processing" and if the request includes you may also need to follow the recommended steps under "Right to Erasure" as outlined in this article. A combination of these will secure you adhering to this request and, most importantly, being able to respond within the legal time limit of one calendar month.
  </Step>
</Steps>

***

Built with [Mintlify](https://mintlify.com).
