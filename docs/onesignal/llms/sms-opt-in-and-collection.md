# Source: https://documentation.onesignal.com/docs/en/sms-opt-in-and-collection.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS opt-in and collection

> Build compliant SMS opt-in forms and collect phone numbers for marketing.

Building an engaged audience is crucial for any SMS marketing strategy and it starts with acquiring your user's phone number.

OneSignal offers user-friendly and effective forms for your users to opt in or double opt-in to SMS messaging. Each method caters to different user preferences and regulatory requirements:

1. Log-in collection opt-in form
2. Coupon code promotional opt-in form
3. Promotional double opt-in form
4. Promotional text-to-subscribe
5. Promotional text-to-subscribe via advertisement

**Deciding between opt in and double opt-in?**

Which form to use depends on your goals and objectives, your target audience, the nature of your business, and local regulations.

Opt in is faster and easier to implement and can lead to a higher volume of phone numbers. Users can also immediately start to receive text messages.

Double opt-in requires users to also confirm their subscription via SMS, which may lead to drop-off. However, double opt-in can help improve the quality of your contact list by reducing invalid numbers. It can also increase engagement rates and lower spam complaints by weeding out low-intent audiences, so you're reaching the people who really want to hear from you.

## Use OneSignal Lookup & Verify to validate phone numbers

To help keep user data clean and ensure phone numbers are valid, OneSignal offers a way to set up one-time verification codes and run checks on phone numbers.

**Verify APIs** allows you to send one time passwords for authentication purposes. [More on setting up Verify](./sms-verify)

**Lookup API** allows you to query information on a phone number to verify users, prevent fraud, and enhance user authentication. The API provides accurate information about phone number type, carrier, country, and reachability, as well as phone number ownership, contact consent validity, and SIM card changes, without impacting user experience.

## Example opt-in flows

<Info>
  For all of these examples, you can check out a working demo available on [GitHub](https://github.com/OneSignalDevelopers/signup-form-examples), take a look for inspiration.
</Info>

To create a new SMS subscription record, call the [Create user](/reference/create-user) endpoint.

Expected response from this endpoint:

* `200` - success, a subscription record has been created
* `202` - subscription record was already created

### Log-in collection opt-in form

In your sign-up flows, you can collect phone numbers. Make sure to include consent boxes, that are 'un-ticked' by default.

<Frame caption="Log-in Collection Opt-in">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/72f9ca5ec5f79911956d91378c575732d9cbc15a52f925ba28ce1cf61d0c9a3f-Desktop_-_71.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=4e4924af3c50b003ac726eab0df20ab2" width="833" height="893" data-path="images/docs/72f9ca5ec5f79911956d91378c575732d9cbc15a52f925ba28ce1cf61d0c9a3f-Desktop_-_71.png" />
</Frame>

### Coupon code promotional opt-in form

A coupon code promotional opt-in is a standard way to incentivize a customer to provide you with their phone number. It's a great choice for Desktop and Mobile experiences. Because the recipients opts in only by providing their phone number, this would not be considered best practice is some locations that require a double opt-in flow.

<Frame caption="Coupon Code Promotional Opt-in">
  <img src="https://files.readme.io/32db2662db127555a0178a73a82e75203057d9dcd456780ac62ee4b3f4429b78-SMS_Coupon_Code.gif" />
</Frame>

<Info>
  This method for SMS collection only accounts for one form of opt-in consent. To improve account verification and follow best practices, you might want to consider implementing a Double Opt-in collection methodology like one of the options below.
</Info>

### Promotional double opt-in form

This option is a standard Double Opt-in flow. It works great for both Desktop and Mobile experiences. It does require turning on the Double Opt-in Prompt in Settings and setting up a keyword reply.

<Frame caption="Promotional Double Opt-in">
  <img src="https://files.readme.io/8b36a78bb9a307570e2b81c0d57892215ff76f9f3c5e069313a0c49d2adc6b11-SMS_Double_Opt_In_Desktop.gif" />
</Frame>

This flow includes 4 steps:

1. Phone number collection
2. OneSignal will text the `Send Message Prompt` template
3. OneSignal receives the keyword reply
4. OneSignal sends keyword reply template, and marks the recipient as 'subscribed'

**Requirements**: For this method to work you will need to:

1. Ensure all message replies are properly syncing to OneSignal.
2. Turn on `Send Message Prompt` and select a template
3. Set up a Keyword reply with a response template.

### Promotional Text-to-Subscribe

This option has been shown to provide a higher rate, but it should only be implemented to display on obile devices, not desktop devices.

<Frame caption="Promotional Text-to-Subscribe">
  <img src="https://files.readme.io/bcc57cfb017a50d38ef48a21eab69bac47bd4af590d7bd41332e767a028d602b-Text_to_Subscribe.gif" />
</Frame>

Text-to-subscribe works as a double opt-in flow because there are two opportunities for the person to consent to subscribe to marketing messages: 1. When they click the first button, and 2. When they send the pre-populated text to the provided number.

The experience provides a clickable link that opens the recipient's SMS app with a pre-populated message.

You can build a clickable link using [URI Encoding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) to generate the link. In general, you'll end up building a clickable link similar to the one below:

<CodeGroup>
  ```html HTML theme={null}
  <div class="modal" id="smsLinkModal">
    <p>Click below to subscribe via SMS:</p>
     <a href="sms:+123456789?&body=Send%20this%20message%20to%20subscribe%20to%20marketing%20messages%20and%20receive%2015%25%20off!%20%5BRef%3A15off%5D">
        Click here to text us!
    </a>
  </div>
  ```
</CodeGroup>

In this example URL:

* The `sms:+123456789` parameter specifies that it's an SMS link and includes the phone number.
* The `?&body=` parameter is used to include a pre-filled message.
* The text Send this message to subscribe to marketing messages and receive 15% off! \[Ref:15off] is URL-encoded to ensure special characters are correctly interpreted by web browsers and mobile devices. For example:

  * `%20` is used for spaces
  * `%25` is used for the percent symbol (%)
  * `%5B` and `%5D` are used for square brackets `[` and `]`
  * `%3A` is used for the colon `:`

### Promotional text-to-subscribe via advertisement

This option is great for TV ads, posters, or other forms of media. Tell your customer to text a text-to-subscribe keyword to one of your Sender Identities.

<Frame caption="Promotional Text to Subscribe via Advertisement">
  <img src="https://files.readme.io/8d4f4a3e728f17e40a632750e3eff7dce8cf14b976f8f669e146eefd63eb1228-From_Advertisement.gif" />
</Frame>

***

## Making sure your opt-in flows are compliant

Sending SMS messages is subject to regulatory oversight. In your opt-in flows, we recommend following these compliance steps:

1. **Always include your business name:** As shown in the examples, your business name should be included in every SMS message, especially in the first interaction.
2. **Opt-in language:** Make it clear that users are opting in to receive messages from your business.
3. **Opt-out instructions:** Provide easy opt-out options with every message (e.g., "Reply STOP to unsubscribe").
4. **Message and data rates:** Always include a disclaimer that standard message and data rates may apply.
5. **Consent not a condition of purchase:** Include this disclaimer to comply with regulations and ensure transparency.
6. **Link to terms and privacy policy:** When appropriate, include a link to your Terms of Service or Privacy Policy, especially in the initial subscription messages.
7. **Identify the message purpose:** When appropriate, explain the types of messages you expect to send.

By following these guidelines, you'll ensure that your SMS campaigns are compliant with industry standards and regulations, while also maintaining clarity and trust with your customers. Learn more at [SMS Regulatory Compliance](./sms-regulatory-compliance).

***

## Managing your double opt-in prompts

If you would like to send a SMS to each new SMS subscription added. You can turn on the `Send Message Prompt` setting by navigating to **SMS Settings > Consent Management**. This will automatically send the template selected to all new SMS subscriptions created through the API or SDKs. Subscriptions added via the CSV Importer will not receive a message prompt.

The send message prompt will send from your default Sender Identity. It's recommended to use a Messaging Service that you have set up for transactional sending to ensure that these messages are sent in a timely manner.

### Text-to-subscribe keywords

Add a keyword reply to complete the double opt flow. For example, you might use a generic text-to-subscribe keyword, a special code, or a keyword like `Y` or `Subscribe`.

Keywords can be any alpha-numeric value. All incoming messages will be checked for keywords, if the message has many words, we check the first word, last word, and any words between parentheses, e.g. `(summer sale)`.

**Requirement**: Ensure that you have set up your SMS replies to automatically sync to OneSignal.

### Bypassing the prompt

If you want to use Double Opt-in in some scenarios but not 100% of the time. You can bypass the `Send Message Prompt` by setting the API parameter `send_double_opt_in_prompt` to `false`.

***

## Send a contact card to brand your sender

You can send your subscribers a contact card (also known as a vCard or VCF file) so they can save your business as a contact on their phone. Once a subscriber downloads and saves your contact card, future messages from you will display with your branded contact name and info instead of just a phone number. This also helps ensure your messages don't land in the "Unknown Senders" inbox on iOS, which can significantly improve visibility and engagement.

### How it works

A contact card is a `.vcf` file that contains your business name, phone number, logo, and other contact details. You send it as an MMS message by including a publicly hosted URL to the `.vcf` file in the media field of your SMS message. When the subscriber receives it, they'll see a prompt to download and save the contact.

### Step 1: Create your VCF file

Create a `.vcf` (vCard) file with your business contact information. A VCF file is a standard format that includes fields for:

* Business/display name
* Phone number (use the same number as your SMS sender identity)
* Company name
* Logo/photo (optional but recommended)

You can create a VCF file using:

* An online vCard generator (such as vcardmaker.com, vcard.me, or similar tools)
* A text editor — the VCF format is a simple plain-text format

Here's a minimal example:

```text  theme={null}
BEGIN:VCARD
VERSION:3.0
FN:Your Business Name
ORG:Your Business Name
TEL;TYPE=CELL:+15551234567
END:VCARD
```

### Step 2: Host your VCF file at a public URL

The VCF file needs to be accessible via a public URL. You can host it using:

* Your own web server or CDN (e.g., upload to your website at something like `https://yourdomain.com/contact.vcf`)
* A cloud storage service like AWS S3, Google Cloud Storage, or similar, with public read access enabled
* Any file hosting service that provides a direct download link to the raw file

Make sure the URL points directly to the `.vcf` file (not a download page or preview).

### Step 3: Send the contact card via SMS

1. In the OneSignal dashboard, create a new SMS message.
2. In the **Media URL** field, paste the public URL to your hosted `.vcf` file (e.g., `https://yourdomain.com/yourcompany-contact.vcf`).
3. Add a message body encouraging the subscriber to save your contact — for example: "Save our contact to always know it's us! Tap the attachment to add us to your contacts."
4. Send the message to your subscribers.

<Note>
  Sending a contact card uses the media URL field, which means the message will be sent as MMS and will be charged at MMS rates. Check your plan details for MMS pricing.
</Note>

<Tip>
  Consider sending your contact card as part of your welcome flow when a new subscriber opts in. This way, all future messages will appear branded from the start.
</Tip>

***

Built with [Mintlify](https://mintlify.com).
