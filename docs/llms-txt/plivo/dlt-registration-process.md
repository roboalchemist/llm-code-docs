# Source: https://plivo.com/docs/messaging/concepts/dlt-registration-process.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DLT Registration Process for Sending SMS to India

> Register entities, headers, and templates on DLT for India SMS

The Telecom Regulatory Authority of India (TRAI) has mandated all entities that want to send SMS to register their organizations, headers, and templates along with required consent information, on distributed ledger technology (DLT) platforms to curb unsolicited commercial communication (UCC).

Please note that only Indian entities (those registered locally in India) are eligible to register on the DLT platform.

**Here's how to do that:**

### **Step 1 — Get unique Entity ID**

Register on any of the DLT platforms below by filling in the required information to get a temporary ID. After verification of your documents, the operator will provide you with a unique Entity ID.

* Videocon ([https://smartping.live/entity/register-with](https://smartping.live/entity/register-with))
* Vodafone Idea Limited ([https://www.vilpower.in](https://www.vilpower.in))
* Airtel ([https://dltconnect.airtel.in/signup/](https://dltconnect.airtel.in/signup/))
* Jio ([https://trueconnect.jio.com/#/](https://trueconnect.jio.com/#/))

#### Note:

* According to customer feedback so far, Jio seems to have a shorter and easier registration process than the others.
* Please share your reference number/temporary ID/unique Entity ID and registered entity name with us once you have registered on any of the DLT platforms.

### **Step 2 — Register headers**

Once you get your unique Entity ID, register your headers in the DLT platforms.

#### **To add headers**

* After the registration is complete, you can add your headers (sender ID) under the Headers tab in the dashboard. Please refer to the attached guide for the header registration process.
* There are two types of Headers to choose from — Promotional and Others.
* For sending promotional campaigns, such as offers, discounts, and promotions, you need to choose a 6-digit numeric sender ID, which will be prefixed with your industry
* For sending transactional campaigns, such as updates and notifications, you can choose your preferred header name. Add your preferred header name in the text box and state the reason for choosing it in the description box below.

Your header name should match your entity name. If the header name is different, please justify the discrepency and include your mobile number in the description box. The mobile number will help the DLT support team to contact you in case they have questions.

#### Note:

* Only entities with registered headers can send SMS messages. Please contact us once your headers have been approved.
* Headers (sender names) are case-sensitive, so ABCDEF and abcdef, for example, are two different sender names and can be registered separately.

### **Step 3 — Register consent templates**

After you've registered your business and headers (sender IDs), the next step in the DLT registration process is to add consent templates.

**Consent templates and registering guidelines**

A consent template is a standard message that's sent to users to get their consent to receive communications from enterprises.\*\*\*\*

* Template Name: Choose whatever you like
* Brand Name: A product or trade name
* Scope of Consent: Description of the content you plan to send to users. Examples:
  * We would like to send communication regarding marketing offers and events to our registered customers
  * ABC Solutions needs your consent to send you messages about your account information and activity and our best offers
  * We will send you updates, transactions, recommendations of our services and products to our registered customers

#### **Dos for consent templates**

* Choose a relevant short name to the template to help you choose the right consent templates when you associate them with content templates in promotional or service categories.
* Brand name should be relevant to details mentioned in scope of content.
* The scope of content and your intent should be clear and relevant to the mentioned brand.
* If you want to offer opt-out information, include complete information. Example: “To opt out, send STOP to 5555555”

#### **Don’ts for consent templates**

* Don't use generic names for templates, such as "template1."
* Don't mention invalid or irrelevant names or popular brand names. Operators will treat these as invalid templates.
* Don't enter an actual message sent to the customer.
* Don't enter short messages like "consent" or "SMS to customers."
* Don't use variables in the scope of consent, as variables are applicable only to content templates.

After filling in the details in the three fields you can submit the template for approval. There is no limitation on the number of consent templates you can create.

After consent templates are approved by the registrar, you can link them to content templates in promotional or service categories, as shown here:

### **How to register a consent template in a DLT portal**

#### **For Jio DLT platform:**

* Select Template > Consent Registration.
* Add a template name and your brand name.
* Add Template Consent, which is the standard message that is added to your T\&C or any other document informing them about their consent to receive communications from respective enterprise.
* After adding your consent template, add a list of consented customers.
* For adding phone numbers, select Customers’ Consent > Bulk Upload.

### **Content templates and registration guidelines**

After you've registered consent templates, the next step in the DLT registration process is to add content templates.

#### **How to add content templates**

There are four types of content templates: transaction, service implicit, service explicit, and promotional.

**Transactional**

Any message that contains a one-time password (OTP) required to complete a banking or credit or debit card transaction initiated by a bank customer is considered transactional. Here are some examples of this type of content, along with examples of the template formats that would create them.

**Actual Message**

**Template Format**

234567 is the OTP for txn of inr 57.75 at Izaak payment services PVT with your sbi card xx3931. OTP is valid for 10 mins. pls do not share with anyone

\{#var#} is the OTP for txn of inr \{#var#} at \{#var#} with your sbi card\{#var#}. OTP is valid for \{#var#}. pls do not share with anyone

234567 is your OTP for fund transfer for the amount Rs.6,000 to Raja. OTP valid for 8 minutes. Do not share this OTP with anyone.

\{#var#} is your OTP for fund transfer for the amount \{#var#} to \{#var#}. OTP valid for 8 minutes. Do not share this OTP with anyone.

234567 is OTP for your eComm Txn for the amount Rs.25,000 OTP valid for 8 minutes. Do not share this OTP with anyone.

\{#var#} is OTP for your eComm Txn for the amount \{#var#} OTP valid for 8 minutes. Do not share this OTP with anyone

#### **Service-implicit**

Any message arising out of customers' actions or their existing relationship with the enterprise, and that is not promotional, is considered a service-implicit message. These include:

* Confirmation messages of net banking and credit/debit card transactions
* Product purchase confirmation and delivery status from ecommerce websites
* Customer is making payments through a payment wallet for an ecommerce website or mobile app, and an OTP is sent to complete the transaction
* OTPs required for ecommerce websites, app logins, social media apps, authentication and verification links, securities trading, demat account operations, KYC, and ewallet registration
* Messages from TSP/ISP
* Periodic balance info, bill generation, bill dispatch, due date reminders, recharge confirmation (DTH, cable, prepaid electricity recharge, etc.)
* Delivery notifications, updates, and periodic upgrades
* Messages from retail stores related to invoices and warranties
* Messages from schools, such as attendance and transport alerts
* Messages from hospitals, clinics, pharmacies, radiologists, and pathologists about registration, appointments, discharge, and reports
* Confirmatory messages from app-based services
* Government/DOT/TRAI mandated messages
* Service updates from car workshops, repair shops, and gadgets service centers
* Directory services such as Justdial and Yellow Pages
* Day-end and month-end settlement alerts to securities and demat account holders

**Actual Message**

**Template Format**

Thank you for using EMI Facility on your XXXX Bank Credit Card 4\*\*\*1234 EMI request for Rs. 89000.00 executed on 01/07/2019

Thank you for using EMI Facility on your IDBI Bank Credit Card \{#var#} EMI request for \{#var#} executed on \{#var#}

XXX BANK - Your new bill for BESCOM Bangalore - account 0123456000 for Rs 4339.00 could not get scheduled because the auto-pay limit is less than the bill amount.

XXX BANK - Your new bill for \{#var#} - account \{#var#} for Rs \{#var#} could not get scheduled because the auto-pay limit is less than the bill amount.

Account: 123456 is your Pansoi account verification code.

Account: \{#var#} is your Pansoi account verification code

#### **Service-explicit**

Service-explicit messages require explicit consent from customers that has been verified directly from the recipient in a robust and verifiable manner and recorded by the consent registrar. This category includes any service messages that don’t fall under the service-implicit category.

Customer consent templates must be linked to content templates in the service-explicit category.

Examples include messages to the existing customers recommending or promoting products or services.

**Actual Message**

**Template Format**

Your Rs.500 exclusive voucher is ready. Redeem it on purchase of Rs.1,000 at M\&M. Use code 654321001. Valid till 31 Mar 2021! T\&C.

Your Rs.\{#var#} exclusive voucher is ready. Redeem it on purchase of Rs.\{#var#} at M\&M. Use code \{#var#}. Valid till \{#var#}! T\&C.

To best serve you and others, please click on mosl.co/ywq8FBJpAn to share your meeting experience with your Ojas Insurance representative

To best serve you and others, please click on \{#var#} to share your meeting experience with \{#var#}

Baba Finserv personal loans need minimal documentation. Meet your financial needs in one click: [http://m.BabajFin.in/Iphr8tFE](http://m.BabajFin.in/Iphr8tFE)

Baba Finserv personal loans need minimal documentation. Meet your financial needs in one click: \{#var#}.

#### **Promotional**

These are any messages with an intention to promote or sell products, goods, or services. Service content mixed with promotional content is treated as promotional. These messages are sent to customers after performing the preference and consent scrubbing function.

Customer consent templates must be linked to content templates in the promotional category.

Examples:

**Actual Message**

**Template Format**

Lifetime free bank credit card with vouchers from LensKart, Pepperfry, Grabon worth Rs.3000. SMS “apply” to 5676766. TnC apply

Lifetime free bank credit card with vouchers from LensKart, Pepperfry, Grabon worth Rs.\{#var#}. SMS “\{#var#}” to 5676766. TnC apply

Pay just Rs 640\* pm & get Rs 83,333 for 120 months or payout of Rs 1,00,00,000 with LIC (Life Insurance Cover) for your family. [http://px2.in/pAD4Tls](http://px2.in/pAD4Tls)

Pay just Rs \{#var#} pm & get Rs \{#var#} for \{#var#} months or payout of Rs \{#var#} with LIC (Life Insurance Cover) for your family. \{#var#}

You can win Rs 20,000 in fantasy cricket! Use code 542321. Install Badger app now to win. Click [https://abc.com](https://abc.com)

You can win Rs \{#var#} in fantasy cricket! Use code \{#var#}. Install Badger app now to win. Click \{#var#}

### **Content template validation**

* Use of two or more spaces before, after, or between words is not advisable.
* All special characters are allowed.
* The variable format in text is \{#var#}, which is case-sensitive. You can also insert a variable by clicking the insert variable radio button.
* Transactional and service content should always have some variable content.
* Promotional content can have completely fixed content or some variable content.
* There is no limitation on the number of variables per message.
* Values such as dates, amounts, account numbers, names, and OTPs must be inserted using variables.

#### **Dos for content templates**

* Use the promotional category for communications intended to be sent only from numerical sender IDs.
* Only banking enterprises should use the transactional category for OTP messages during fund transfers, online payments, and merchant transactions.
* Choose relevant and recognizable names for content templates.
* Use the message type as “TEXT” for all general messages and “Unicode” for regional messages.
* Use variable \{#var#} insertion for values such as dates, amounts, account numbers, names, and OTPs.
* Make sure your CTAs are whitelisted, including:
  * **URLs:** any link/URL used in an SMS; WhatsApp links; APK links
  * **Numbers used for calls or messages (including mobile, landline, and toll-free)**
  * **Email addresses**

#### **Don’ts for content templates**

* Don’t use the same content template with multiple headers.
* Don’t make header selections against irrelevant templates.
* Don’t select the transactional content types for nonbanking enterprises.
* Don’t use double spaces in templates. Check for this using a tool like Notepad++ before template submission.
* Don’t use templates with fewer than six characters or with only variable insertion.
* Don’t use any URLs that have not been whitelisted; if a value is not whitelisted under your brand, your **messages will fail** to be delivered.

### **How to register a content template in a DLT portal**

#### **For Jio DLT platform**

* Select Template > Content Template Registration
* Choose template type as SMS
* Choose your content type — English or other languages
* Select a Category from the drop-down list
* Select Consent ID from the drop-down list
* Choose a type of communication — Promotional / Transactional / Service-Inferred / Service-Explicit
* Select Header from the drop-down list
* Add the template content in the "template content" text box and click Submit.

***

## Linking DLT to Plivo Console

After completing your DLT registration and receiving approvals, link your DLT credentials to Plivo to start sending messages to India.

### Add your DLT Entity ID

1. Log in to the [Plivo Console](https://console.plivo.com/)
2. Navigate to **Messaging** > **Compliance**
3. Enter your **DLT Entity ID** (provided by the DLT platform after entity verification)
4. Click **Save**

### Map DLT templates to Plivo

Once your Entity ID is linked, map your approved DLT content templates:

1. In the Plivo Console, go to **Messaging** > **Compliance** > **DLT Templates**
2. Add each approved template by entering:
   * **Template ID** — the unique ID assigned by the DLT platform
   * **Template content** — must exactly match the approved DLT template, including variables (`{#var#}`)
   * **Header** — the sender ID (header) associated with this template
3. Click **Save** for each template

<Note>
  The template content in Plivo must be an exact match of the DLT-approved template. Any mismatch — including extra spaces, different capitalization, or missing variables — causes message delivery failures.
</Note>

***

## Troubleshooting DLT Registration

### My content template was rejected by the DLT platform

Common reasons for template rejection:

| Issue                         | Fix                                                                                                              |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Incorrect variable format     | Use `{#var#}` exactly — it is case-sensitive                                                                     |
| Double spaces in template     | Remove extra whitespace between words; use a text editor like Notepad++ to check                                 |
| Template too short            | Templates must have at least six characters beyond variables                                                     |
| Only variables, no fixed text | Include meaningful fixed text alongside variables                                                                |
| URL not whitelisted           | Whitelist all URLs, email addresses, and phone numbers used in the template under your brand on the DLT platform |

### My header (sender ID) was not approved

* Header names must closely match your registered entity name. If different, provide justification in the description field.
* Headers are **case-sensitive** — `ABCDEF` and `abcdef` are treated as separate headers.
* Include your mobile number in the description so the DLT support team can contact you if needed.
* Promotional headers must be 6-digit numeric sender IDs prefixed with your industry code.

### Messages are failing after DLT registration

If your DLT registration is complete but messages are not delivering:

1. **Template ID mismatch** — Verify the Template ID in the Plivo Console matches the one approved on the DLT platform exactly.
2. **Content scrubbing mismatch** — The message body sent via the Plivo API must match the registered template structure. Variable portions must align with `{#var#}` placeholders.
3. **Header not mapped** — Ensure the sender ID used in your API request matches a header registered and approved on the DLT platform.
4. **Consent not registered** — For service-explicit and promotional messages, verify consent templates are linked to your content templates on the DLT platform.

### My Entity ID verification is delayed

Entity ID verification timelines vary by DLT platform. To expedite:

* Ensure all required documents (business registration, PAN, GST certificate) are uploaded correctly
* Check for any pending clarifications on the DLT platform dashboard
* Contact the DLT platform support directly:
  * **Jio TrueConnect:** [trueconnect.jio.com](https://trueconnect.jio.com)
  * **Airtel DLT:** [dltconnect.airtel.in](https://dltconnect.airtel.in)
  * **Vodafone Idea (VIL):** [vilpower.in](https://www.vilpower.in)
  * **Videocon (Smartping):** [smartping.live](https://smartping.live)
