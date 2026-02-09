# Source: https://docs.lunary.ai/docs/more/security/GDPR.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GDPR compliance guide

The [General Data Protection Regulation (GDPR)](https://gdpr.eu/) represents a set of regulations on privacy and security, established and enacted by the European Union (EU). It mandates responsibilities for organizations globally, provided they process or gather data concerning individuals within the EU.

It is advisable to delve into the complete GDPR docs and consult with a legal expert to understand your specific responsibilities. Non-compliance with GDPR can lead to significant repercussions.

## What data is protected under GDPR?

Under GDPR, personal data is safeguarded, encompassing any details that can identify an individual either directly or indirectly. This includes, but is not limited to, names, email addresses, geographical data, ethnic background, gender, biometric details, religious convictions, internet cookies, and political views.

## What is the impact of GDPR on observability?

The primary guideline is to avoid gathering, storing, or utilizing any personal data without a valid justification, such as:

* The individual has provided explicit, clear consent for data processing (for instance, they have subscribed to your marketing emails).

* The processing is essential for the formation of a contract with someone (for example, conducting a background investigation is necessary).

* The processing is required to fulfill a legal duty (for example, responding to a court order in your area).

* The data needs to be processed to protect someone's life (in such cases, the circumstances will be evident).

* The processing is necessary to execute a task that serves the public interest or an official duty (for example, if you operate a private waste collection service).

* You possess a valid interest in processing an individual's personal data. This basis for processing is notably adaptable, yet the "fundamental rights and freedoms of the data subject" take precedence over your interests, particularly in the case of minors.

### You must acquire "Unambiguous Consent"

Specific guidelines exist regarding the definition of consent:

* Consent must be "freely given, specific, informed and unambiguous"

* Consent requests must be "clearly distinguishable from the other matters" and conveyed in "clear and plain language"

* At any time, data subjects are allowed to revoke their consent, and it's your responsibility to respect this choice

* Only with a parent's permission can children under the age of 13 provide consent

* Documentary proof of consent must be maintained by you

Therefore, if your product tracks users through Lunary, it's crucial to directly request their consent for this data usage and clearly detail how it will be employed at the time they register for your service.

### Data must be handled securely

It's mandatory to ensure data security through the adoption of "appropriate technical and organizational measures."

This encompasses technical strategies (such as data encryption) and organizational tactics (such as conducting staff training and restricting access to sensitive data).

In the event of a data breach, you are obligated to inform the affected individuals within 72 hours to avoid penalties. (However, this requirement for notification can be bypassed if technological protections, like encryption, are employed to make the data inaccessible to unauthorized parties.)

### You should not transfer EU users' personal data outside the EU

For those who have chosen to self-host Lunary on servers located outside the EU while handling data from EU users, it's advised to anonymize the personal data of such users.

Similarly, for users of Lunary Cloud, anonymizing personal data of EU users is also recommended.

## How to set Lunary up for GDPR compliance

The obligations under GDPR vary based on the manner in which your organization handles personal data. Entities can function as data controllers, data processors, or fulfill both roles simultaneously. [Data controllers](https://gdpr-info.eu/art-24-gdpr/) are responsible for collecting data from their end users and determining the purposes and means of processing that data. On the other hand, [data processors](https://gdpr-info.eu/art-28-gdpr/) are entities that process personal data on the instructions of another business.

You will be using Lunary in one of three ways:

1. Hosted and managed by us on Lunary Cloud
2. Hosted and managed by us on a region of your choice with the Dedicated option
3. Self-hosted by you on a private cloud or your own infrastructure

If you are using Lunary Cloud or then Lunary is the Data Processor and you are the Data Controller.

If you are self-hosting Lunary then you are both the Data Processor and the Data Controller because you are responsible for your Lunary instance.

### Step 1: Choose how to host Lunary

We recommend using Lunary Cloud for GDPR compliance. If self-hosting, the steps will depend on where you're hosting your data.

### Step 2: Deploy Lunary

If using Lunary Cloud, simply follow the steps in the onboarding process to start sending events. Read our [getting started guide](/docs/get-started) for more information on sending logs to Lunary.

Setting up Lunary on your own infrastructure is simple, and our team is here to assist with any issues that arise. Begin by consulting our [self-hosting guide](/docs/more/self-hosting/docker).

### Step 3: Security configuration

Our SDKs used with Lunary Cloud utilize HTTPS to ensure the security of data during transmission. When self-hosting Lunary, we strongly recommend using HTTPS as well to secure data transmission.

It is highly advised to restrict access to Lunary and its underlying infrastructure strictly to individuals who have authorization and a legitimate need to interact with the data, this includes links to shared dashboards.

### Step 4: Configure consent

Given that Lunary inherently collects data, which may include personal information, it's imperative to establish a method for obtaining consent for such data collection. This requirement aligns with the GDPR's [right to be informed](https://gdpr-info.eu/issues/right-to-be-informed/).

The consent form should clearly specify which categories of personal data are being gathered and the tools utilized for this collection:

* If you are using Lunary Cloud you should identify Lunary as a tool
* If you are self-hosting you can either not list a tool or provide a generic description such as "Monitoring".

If a user opts out then you must stop data capturing and processing. Here are some ways Lunary makes this possible:

* If Lunary has been initialized, call `lunary.opt_out()` in Python or `lunary.optOut()` in JS.

* Do not load the Lunary SDK.

* Do not initialize the Lunary SDK by setting an empty Public Key / Project ID.

## Complying with 'right to be forgotten' requests

Users should have the capability to demand the deletion of their data. The method through which you accommodate such requests is at your discretion. For instance, you might choose to receive these requests through email or by a form.

You can remove a user from a Lunary instance via the Lunary user interface. To do this:

* Select "Users" from the sidebar menu
* Search and click on the concerned user
* Click "Delete" to remove them and all their associated data from Lunary.
