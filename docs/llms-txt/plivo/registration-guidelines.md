# Source: https://plivo.com/docs/messaging/a2p-10dlc/registration-guidelines.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 10DLC Registration Guidelines

> Requirements, fees, and common rejection reasons for 10DLC brand and campaign registration

Before you can send application-to-person (A2P) text messages over long codes in the US, you must register with The Campaign Registry (TCR), the agency that carriers use to vet businesses. To register through Plivo (or even directly with TCR) you must provide information about your company (brand) and use cases (campaigns), and if you're a reseller you must also provide brand and campaign information about each customer on whose behalf you send text messages. Follow the instructions here to minimize the possibility of your brand or campaign registrations being rejected.

<Frame>
  <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/10DLC-Registration-Guidelines-by-Plivo-(1).mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=04d11b991dafd32dd08a6293cce2d925" data-path="images/10DLC-Registration-Guidelines-by-Plivo-(1).mp4" />
</Frame>

View the presentation <a href="https://plivo-docs-upload.s3.us-west-1.amazonaws.com/10DLC%2BRegistration%2BGuidelines%2Bby%2BPlivo.pdf" target="_blank">
here</a>

## Brand registration

Whether you're registering from the [10DLC page](https://cx.plivo.com/home) of the Plivo console or using the [10DLC API](/messaging/api/10dlc/profile/), here are some things to keep in mind as you provide information.

* The values you enter for **company name** and **tax ID number (EIN)** must exactly match the values on your tax registration document. If the document specifies "Yourbusiness, Inc." you can't simply say "Yourbusiness."
* Provide a secure **website** that represents your business. Registrations without a website, those that use websites that lack an SSL certificate to support the HTTPS protocol, and those whose websites display boilerplate content or templates are likely to be rejected. The website should include About Us, Contact Us, Terms & Conditions and Privacy Policy pages. A website without these pages will not be considered compliant.
* Provide a working **phone number** — preferably, the same one mentioned on your website's contact or support page. Plivo or TCR may attempt to verify the authenticity of this phone number.
* Provide a working **email address** — preferably, the same one mentioned on your website's contact or support page. A personal email address from a provider like Gmail or Yahoo or one from a disposable domain is likely to result in your brand registration being rejected.

You must provide a unique contact address, email address, and phone number for each registration. TCR prohibits using the same contact information for multiple brands. Brands found in violation of this policy may be deactivated by Plivo or TCR.

Brand registrations are typically approved or rejected within a few days. Contact Plivo support if your brand is still in pending status after one week.

## Campaign registration

Once you've registered your brand you can register campaigns, which you can think of as use cases.

Each campaign must be an appropriate use case for the brand with which it is associated. For example, a pharmaceutical company should not try to create a campaign for food delivery messaging. TCR and carriers may reject campaign registrations that they deem unrelated to or not consistent with the brand.

[Certain use cases are never allowed](/messaging/concepts/us-messaging-best-practices#things-to-avoid-in-content-creation), including

* deceptive marketing
* fraud/scam
* SHAFT (sex, hate, alcohol, firearms, and tobacco)
* cannabis promotion/sale
* debt relief
* high-risk financial services
* third-party lead generation services
* gambling
* real estate

No campaign that falls into any of these disallowed categories will be approved.

### Campaign type

Campaigns must be categorized into any of [10 standard campaign types](/messaging/a2p-10dlc/quickstart#10dlc-campaign-types), or specified as mixed — a combination of two to five standard use cases.

### Campaign description

For each campaign, provide a detailed description that includes the brand name, use case, and the type of messages you'll send.

<table>
  <thead>
    <tr>
      <th width="30%">Good Example</th>
      <th>Bad Example</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ABC LLC uses this campaign to provide real-time delivery notifications to customers regarding packages they ordered on [https://www.abc-llc.com](https://www.abc-llc.com).
      </td>

      <td>
        "Using for delivery notification" — Lacks brand name and the type of messages going out
      </td>
    </tr>

    <tr>
      <td>
        ABC LLC uses this campaign to send followup customer care messages to subscribers who have opted in through a webform and want to sell their vehicle.
      </td>

      <td>
        "Customer outreach campaign" — Lacks brand name and type of messages going out
      </td>
    </tr>
  </tbody>
</table>

### Message flow

Also known as call to action (CTA), the message flow describes how a customer opts in to a campaign, thereby giving consent to the sender to send messages. A compliant CTA should include the following:

* Brand Information — name of brand sending these texts
* Message frequency — for example, "You may receive up to two messages a week" or "Message frequency varies" or "Message will be sent when a user registers or changes password"
* Pricing disclosure — for example, "Message and data rates may apply"
* Link to your Terms & Conditions page
* Link to your Privacy Policy
* Privacy Policy **must have a no-sharing clause** that states subscriber information will not be shared with 3rd parties for their direct marketing purposes. For example, "No mobile information will be shared with third parties/affiliates for marketing/promotional purposes. All the above categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties."
* Opt-in consent mechanism — the opt-in method and action taken by the user to subscribe

Opt-in methods may be web form, texting a keyword, paper form, verbal or mixed.

* **Web form**: Website visitors submit a form agreeing to receive your texts. Specify the link to the form in the CTA. The web form should include opt-in language, links to your company's Terms & Conditions and Privacy Policy pages, expected message frequency, pricing, HELP and OPT OUT information. Here's an example of a compliant form with all the required details. A check box is recommended to collect consent for Web opt-in due to regulations prohibiting forced opt-in by carriers.

<Frame>
    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/consent2.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=70a501c417071b915d81f8f5e3f5c4f5" alt="img" width="932" height="938" data-path="images/consent2.png" />
</Frame>

<table>
  <thead>
    <tr>
      <th width="30%">
        Good Example
      </th>

      <th>
        Bad Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ABC LLC: Customers opt in by subscribing to our weekly newsletter from our website, [https://abc-llc.com](https://abc-llc.com), where they indicate that they would like to receive texts about upcoming shows. Instructions about how to opt out are sent alongside the text messages. Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe and HELP for assistance. Terms & Conditions: \<link> Privacy Policy: \<link>
      </td>

      <td>
        "Customers opt in by subscribing to our weekly newsletter, where they indicate that they would like to receive texts about upcoming shows" — missing brand name, opt-in consent mechanism, links to Terms & Conditions and Privacy Policy, message frequency and pricing disclosure, HELP and OPT-OUT information
      </td>
    </tr>

    <tr>
      <td>
        Danceabc: Customers visit our website [https://www.danceabc.com/](https://www.danceabc.com/) and click on "Register For Class" which redirects them to our registration form [https://www.danceabc.com/enroll](https://www.danceabc.com/enroll). While filling this form they can check a box "Receive Text Message Notifications" (below the Cell # field in CONTACT #1 section) to opt-in to receive these alerts. Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe and HELP for assistance. Terms & Conditions: \<link> Privacy Policy: \<link>
      </td>

      <td>
        "Customers opt in by enrolling for a dance class online" — missing brand name, link to webform, Terms & Conditions and Privacy Policy, message frequency, pricing disclosure, HELP and OPT-OUT information
      </td>
    </tr>
  </tbody>
</table>

* **Keyword**: Customers text a keyword or phrase to join your message list. Mention the opt-in keyword, number, how the number is advertised and add a link to an image of the advertisement. Ad should contain opt-in language, links to the Terms & Conditions and Privacy Policy pages, expected message frequency, pricing, HELP and OPT OUT information.

<table>
  <thead>
    <tr>
      <th width="30%">
        Good Example
      </th>

      <th>
        Bad Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ABC LLC: Consumers opt in by texting START to (202) 555-3456, as mentioned on our website's Contact Us information at [https://abc-llc.com/contact](https://abc-llc.com/contact). Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe and HELP for assistance. Terms & Conditions: \<link> Privacy Policy: \<link>
      </td>

      <td>
        "Consumers opt-in by text and provide consent to receive these messages" — missing brand name, text keyword and number, how the number is advertised for subscribers, links to Terms & Conditions and Privacy Policy, message frequency, pricing disclosure, HELP and OPT-OUT information
      </td>
    </tr>

    <tr>
      <td>
        On arriving at Ovlip LLC managed parking locations, the customers find printed signage that asks them to text "555" to our phone number +13456548977 to avail parking services.\<link to an image of advertisement> Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe and HELP for assistance. Privacy Policy: \<link> Terms of Use: \<link>
      </td>

      <td>
        "Customers message phone number at garage and to operate gate system, we then send gate code to customer." — missing brand name, text keyword and number, how the number is advertised for subscribers, links to Terms & Conditions and Privacy Policy, message frequency, pricing disclosure, HELP and OPT-OUT information
      </td>
    </tr>
  </tbody>
</table>

* **Paper form**: Consumers provide phone numbers and express consent on a paper form. Put a copy of the paper form on a web page and include a link to that page in the CTA. The form should contain opt-in language, links to the Terms & Conditions and Privacy Policy pages, expected message frequency, pricing, HELP and OPT OUT information.

<table>
  <thead>
    <tr>
      <th width="30%">
        Good Example
      </th>

      <th>
        Bad Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ABC LLC: Upon hire, employees sign an employment contract wherein they provide consent to receive scheduling messages as a part of their contract. \<link to image of paper form> Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe and HELP for assistance. Terms & Conditions: \<link> Privacy Policy: \<link>
      </td>

      <td>
        "ABC LLC: Upon hire, employees sign an employment contract wherein they provide consent to receive scheduling messages as a part of their contract" — missing links to a copy of paper form, Terms & Conditions and Privacy Policy, message frequency, pricing disclosure, HELP and OPT OUT information
      </td>
    </tr>

    <tr>
      <td>
        ABC Clinic: Subscribers opt in by signing the paperform during their first visit to our clinic where they consent to receive texts from us. \<link to image of paper form> Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe and HELP for assistance. Terms & Conditions: \<link> Privacy Policy: \<link>
      </td>

      <td>
        "Subscribers opt in by signing the paper form during their first visit to our clinic" — missing brand name, copy of paper form on a shared link, Terms & Conditions and Privacy Policy, message frequency, pricing disclosure, HELP and OPT OUT information
      </td>
    </tr>
  </tbody>
</table>

* **Verbal**: Customers provide a verbal consent to receive texts. The phone number, time stamp and voice record of consent needs to be stored on a recorded line. A good practice is the implementation of double opt-in, as an additional layer of consent that will be easier saved and stored.

<table>
  <thead>
    <tr>
      <th width="30%">
        Good Example
      </th>

      <th>
        Bad Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ABC Clinic: Consumers opt in by calling us at (202) 555-3456 to book an appointment. During this call, our staff seeks consent from them to send appointment reminders via text. An initial sms is then sent notifying subscribers that they will receive appointment reminders by sms with opt-out instructions (double opt-in). Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe and HELP for assistance. Terms & Conditions: \<link> Privacy Policy: \<link>
      </td>

      <td>
        "Consumers opt in by booking an appointment" — missing brand name, channel and details of opt-in flow, links to Terms & Conditions and Privacy Policy, message frequency, pricing disclosure, HELP and OPT-OUT information
      </td>
    </tr>

    <tr>
      <td>
        Ovlip LLC: Consumers visit the dealership and provide their contact information. During this visit, our staff seeks verbal consent from them to send customer care and marketing messages via text. An initial sms is then sent notifying they have subscribed to receive sms alerts and asking them to Reply "Yes" for confirmation (double opt-in). Only consumers who reply "Yes" are sent text. Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe and HELP for assistance. Terms & Conditions: \<link> Privacy Policy: \<link>
      </td>

      <td>
        "Ovlip LLC: Consumers visit the dealership and provide their contact information. During this visit, our staff seeks verbal consent from them to send customer care and marketing messages via text. An initial sms is then sent notifying they have subscribed to receive sms alerts and asking them to Reply "Yes" for confirmation (double opt-in). Only consumers who reply 'Yes' are sent text." — missing links to Terms & Conditions and Privacy Policy, message frequency, pricing disclosure, HELP and OPT-OUT information
      </td>
    </tr>
  </tbody>
</table>

* **Mixed**: A combination of two or more opt-in methods - web forms, keywords, verbal, paper forms

<table>
  <thead>
    <tr>
      <th width="30%">
        Good Example
      </th>

      <th>
        Bad Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ABC School: Subscribers opt in by visiting our website and registering for a dance class by clicking on "Book" and submitting the enrollment form at [https://abcschool.com/enroll.jspx](https://abcschool.com/enroll.jspx) with their name, address, and contact details. Alternatively they can opt in at our studio, where they sign a paper copy of our online enrollment form. Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe and HELP for assistance. Terms & Conditions: \<link> Privacy Policy: \<link>
      </td>

      <td>
        "Subscribers enroll for a dance class and provide consent to receive text notification" — missing brand name, opt-in mechanism, links to Terms & Conditions and Privacy Policy, message frequency, pricing disclosure, HELP and OPT-OUT information
      </td>
    </tr>

    <tr>
      <td>
        Ovlip LLC: Subscribers opt in by visiting our website and submitting the "Contact Us" webform at [https://ovlipllc.com/contact](https://ovlipllc.com/contact) with their name and contact number. Alternatively they can opt-in by texting "START" to number +16785678766 (as mentioned on our website). Subscribers may receive upto 2 messages per week. Message and data rates may apply. Reply STOP to unsubscribe and HELP for assistance. Terms & Conditions: \<link> Privacy Policy: \<link>
      </td>

      <td>
        "Subscribers opt-in by text or webform" — missing brand name, opt-in mechanism, links to Terms & Conditions and Privacy Policy, message frequency, pricing disclosure, HELP and OPT-OUT information
      </td>
    </tr>
  </tbody>
</table>

### Sample message

You must provide sample messages that are indicative of the actual messages you're sending. They should adhere to [A2P best practices](/messaging/concepts/us-messaging-best-practices/) and must contain your brand name and opt-out instructions.
