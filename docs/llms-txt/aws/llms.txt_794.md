# Source: https://docs.aws.amazon.com/sms-voice/latest/userguide/llms.txt

# AWS End User Messaging SMS User Guide

> AWS End User Messaging SMS is an application-to-person (A2P) SMS and voice messaging service that provides the global scale, resiliency, and flexibility required to deliver SMS messaging in any web, mobile, or business applications.

- [Best Practices](https://docs.aws.amazon.com/sms-voice/latest/userguide/best-practices.html)
- [Choosing an origination ID](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-number-types.html)
- [Dashboard metrics](https://docs.aws.amazon.com/sms-voice/latest/userguide/view-metrics-dashboard.html)
- [Sending an SMS or voice message](https://docs.aws.amazon.com/sms-voice/latest/userguide/send-sms-voice-message.html)
- [Sending an MMS message](https://docs.aws.amazon.com/sms-voice/latest/userguide/send-mms-message.html)
- [Carrier lookup](https://docs.aws.amazon.com/sms-voice/latest/userguide/carrier-lookup.html)
- [Working with shared resources](https://docs.aws.amazon.com/sms-voice/latest/userguide/shared-resources.html)
- [AWS PrivateLink](https://docs.aws.amazon.com/sms-voice/latest/userguide/vpc-interface-endpoints.html)
- [Quotas](https://docs.aws.amazon.com/sms-voice/latest/userguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/sms-voice/latest/userguide/doc-history.html)

## [What is AWS End User Messaging SMS?](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-sms-mms.html)

- [How does SMS messaging work](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-sms.html): Learn how Short Message Service works using the infrastructure that's already in place for voice calls, operating on the signaling channels of mobile networks.
- [AWS End User Messaging SMS concepts](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-concepts.html): Describes the AWS End User Messaging SMS terminology that you should understand before you start setting up your SMS messaging.


## [Setting up AWS End User Messaging SMS](https://docs.aws.amazon.com/sms-voice/latest/userguide/setting-up.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/sms-voice/latest/userguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Getting started](https://docs.aws.amazon.com/sms-voice/latest/userguide/getting-started.html)

- [First time user tutorial](https://docs.aws.amazon.com/sms-voice/latest/userguide/getting-started-tutorial.html): Learn how to use AWS End User Messaging SMS to send a real or simulated SMS message.
- [Add a verified destination phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/verify-destination-phone-number.html): In AWS End User Messaging SMS, add a destination phone number while you're in the sandbox
- [SMS/MMS and Voice sandbox](https://docs.aws.amazon.com/sms-voice/latest/userguide/sandbox.html): Describes the sandbox in AWS End User Messaging SMS that you use to test your SMS messaging before moving to production.
- [Message part preview](https://docs.aws.amazon.com/sms-voice/latest/userguide/getting-started-mpp.html): Describes SMS message parts in AWS End User Messaging SMS and the billing for those message parts.
- [Simulator phone numbers](https://docs.aws.amazon.com/sms-voice/latest/userguide/test-phone-numbers.html): Learn about simulator phone number and simulator destination phone number.
- [Set a spending limit](https://docs.aws.amazon.com/sms-voice/latest/userguide/spend-limit.html): learn how to limit spending for SMS, MMS, and text to voice sending for each month.


## [SMS and MMS limits and restrictions](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations.html)

- [SMS character limits](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations-character.html): Learn about the messaging limitations when using the GSM 03.38 or Unicode character sets.
- [MMS file types, size and character limits](https://docs.aws.amazon.com/sms-voice/latest/userguide/mms-limitations-character.html): Learn about MMS file size, file type limitations, and maximum number of charters an mms can contain.
- [Message Parts per Second (MPS) limits](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations-mps.html): Learn about the limitations and restrictions that apply to sending SMS and MMS messages using AWS End User Messaging SMS.


## [Phone pools](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool.html)

- [Create a phone pool](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool-create.html): How to create phone pools in AWS End User Messaging SMS.
- [Add a phone number or sender ID](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool-add-number.html): Add a phone number or sender ID to a phone pool.
- [View all phone pools](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool-list.html): How to view your phone pools in AWS End User Messaging SMS using the AWS CLI.
- [Delete a phone pool](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool-delete.html): How to delete your phone pools in AWS End User Messaging SMS.
- [Change a pool''s opt-out list](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool-manage-opt-out-list.html): How to change a phone pool's opt-out list.
- [Update shared routes](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool-shared-routes.html): Enable shared routes to use a shared origination identity to send your message.
- [Using phone pool deletion protection](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool-deletion-protection.html): Use deletion protection to keep from accidentally deleting your resources.
- [Manage tags for phone pools](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool-tags.html): Tags are pairs of keys and values that you can optionally apply to your AWS resources to control access or usage.
- [List shared phone pools](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool-shared.html): How to list all of the phone pools that are shared by AWS RAM using the AWS CLI


## [Phone numbers](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers.html)

### [SMS and MMS country capabilities and limitations](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-support-by-country.html)

Learn about content and country limitations in AWS End User Messaging SMS

- [Supported countries and regions for SMS](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html): This section contains a table of countries and regions along with the origination identities that are supported.
- [Supported countries and regions for MMS](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-mms-by-country.html): Use AWS End User Messaging SMS to send MMS messages to supported countries or regions.
- [Supported countries and regions for voice](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-voice-support-by-country.html): A list countries that support voice calls.

### [Request a phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-request.html)

Learn how to request a phone number for AWS End User Messaging SMS with the console or AWS CLI.

- [Requesting short codes](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-request-short-code.html): Learn how to request a short code by opening a case with Support, and provide the required information.
- [Requesting long codes](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-request-long-code.html): Learn how to request a dedicated long code, open the AWS End User Messaging SMS Console and provide the required information for the request.
- [View a phone number status and capabilities](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-status.html): Learn how to view a phone numbers status and capabilities in the AWS End User Messaging SMS console.
- [Change a phone number's capabilities](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-change-capabilitiy.html): Learn how to change a phone number's capabilities for AWS End User Messaging SMS.
- [Release a phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-delete.html): Release a phone number from your AWS End User Messaging SMS account.
- [Change a phone number's opt-out list](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-manage-opt-out-list.html): Learn how to change the opt-out list used by a phone number.
- [Using deletion protection](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-deletion-protection.html): Use deletion protection to keep from accidentally deleting your phone number.
- [Manage tags a for phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-tags.html): Tags are pairs of keys and values that you can optionally apply to your AWS resources to control access or usage.
- [List shared phone numbers](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-shared.html): Learn how to list all of the phone numbers that are shared by AWS RAM using the AWS CLI


## [Sender IDs](https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id.html)

- [Request a sender ID](https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id-request.html): Learn how to request a sender ID through the AWS End User Messaging SMS console.
- [Request a sender ID through Support](https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id-awssupport-open.html): Learn how to request a sender ID through the Support.
- [Release a sender ID](https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id-release.html): Learn how to release a sender ID through the AWS End User Messaging SMS console.
- [Manage tags a for sender ID](https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id-tags-add.html): Tags are pairs of keys and values that you can optionally apply to your AWS resources to control access or usage.
- [List shared sender IDs](https://docs.aws.amazon.com/sms-voice/latest/userguide/sender-id-shared.html): Learn how to list all of the sender IDs that are shared by AWS RAM using the AWS CLI


## [Registrations](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations.html)

- [Estimated registration times](https://docs.aws.amazon.com/sms-voice/latest/userguide/registration-eta.html): Learn about estimated processing times for different types of registrations in AWS End User Messaging SMS.

### [Manage registrations](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-manage.html)

Learn how to manage your registration forms for an origination identity.

- [Create a new registration using the console](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-create.html): You can use the AWS End User Messaging SMS console to manage registrations for your AWS End User Messaging SMS account.
- [Create a registration using the AWS CLI](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sms-cli.html): Learn how to create a registration using the AWS CLI
- [Check a registration's status](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-status.html): How to check your registration status in AWS End User Messaging SMS.
- [Change a registration's name](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-friendly-name.html): How to rename your registration in AWS End User Messaging SMS.
- [Edit a registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-edit.html): How to edit a registration in AWS End User Messaging SMS.
- [Discard a registration's current version](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-discard.html): How to discard the current version of a registration in AWS End User Messaging SMS
- [Delete a registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-delete.html): How to delete a registration in AWS End User Messaging SMS
- [View a registration associated resources](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-associated-resource.html): How to view resources associated with a registration.

### [Gen-AI Feedback on Registrations](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-genai-feedback.html)

Use AI-powered feedback to review your phone number or sender ID registration before submitting for downstream review.

- [Understanding rejection reasons](https://docs.aws.amazon.com/sms-voice/latest/userguide/understanding-rejection-reasons.html): Learn about common registration rejection reasons and how to resolve them.
- [Get more information on registration issues](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-request-support.html): Learn how to get more information about why your registration was rejected.

### [Registration forms](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-country.html)

Learn how to complete the registration forms for an origination identity.

- [Australia sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-australia.html): How to create sender ID registration for Australia.
- [Belarus sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-belarus.html): How to create sender ID registration for Belarus.
- [China SMS template registration form](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-template-registration.html): Manage your China SMS template registration by opening a request with Support.
- [Egypt sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-egypt.html): How to create sender ID registration for Egypt.

### [India sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sms-senderid-india.html)

How to register a sender ID in India.

- [Register with TRAI and create Telemarketer chains](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sms-senderid-india-register.html): How to register a sender ID with Telecom Regulatory Authority of India (TRAI).
- [India sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sms-senderid-india-support.html): How to register your sender ID in India.
- [Specify the Entity and Template ID values to send messages](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sms-senderid-india-specify-ids.html): How to send messages to India with your sender ID.
- [Understanding template matching issues](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sms-senderid-india-template-issues.html): Learn about why your message was rejected and how to fix it.
- [Indonesia sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-indonesia.html): How to create sender ID registration for Indonesia.
- [Ireland sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-ireland.html): How to create sender ID registration for Ireland.
- [Jordan sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-jordan.html): How to create sender ID registration for Jordan.
- [Kazakhstan sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-kazakhstan.html): How to create sender ID registration for Kazakhstan.
- [Kenya sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-kenya.html): How to create sender ID registration for Kenya.
- [Kuwait sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-kuwait.html): How to create sender ID registration for Kuwait.
- [Philippines sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-philippines.html): How to create sender ID registration for Philippines.
- [Qatar sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-qatar.html): How to create sender ID registration for Qatar.
- [Russia sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-russia.html): How to create sender ID registration for Russia.
- [Saudi Arabia sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-saudi-arabia.html): How to create sender ID registration for Saudi Arabia.

### [Singapore sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sg.html)

How to register a sender ID in Singapore.

- [Singapore Unique Entity Number (UEN)](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sg-uen.html): How to request a Singapore Unique Entity Number (UEN).
- [Singapore sender ID registration form](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sg-form.html): How to complete the your Singapore sender ID registration form.
- [Register a Sender ID with Singapore Network Information Centre (SGNIC)](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sg-sgnic.html): How to register with Singapore Network Information Centre (SGNIC).
- [Singapore sender ID registration frequently asked questions](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sg-faq.html): Frequently asked questions for registering a Singapore sender ID.
- [Sri Lanka sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sri-lanka.html): How to create sender ID registration for Sri Lanka.
- [Thailand sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-thailand.html): How to create sender ID registration for Thailand.
- [Turkey sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-turkey.html): How to create sender ID registration for Turkey.
- [United Arab Emirates sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-united-arab-emirates.html): How to create sender ID registration for United Arab Emirates.

### [United Kingdom sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-uk.html)

How to complete your United Kingdom sender ID registration.

- [United Kingdom registration form](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-uk-form.html): How to complete the your United Kingdom sender ID registration form.
- [Vietnam sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-vietnam.html): How to create sender ID registration for Vietnam.
- [Zambia sender ID registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-zambia.html): How to create sender ID registration for Zambia.

### [Dedicated number registration forms](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-dedicated-number.html)

How to register a dedicated number.

- [Australia](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-australia.html): How to create a dedicated number for Australia.
- [Austria](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-austria.html): How to create a dedicated number for Austria.
- [Chile](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-chile.html): How to create a dedicated number for Chile.
- [Denmark](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-denmark.html): How to create a dedicated number for Chile.
- [Finland](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-finland.html): How to create a dedicated number for Finland.
- [Germany](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-germany.html): How to create a dedicated number for Germany.
- [Hong Kong](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-hong-kong.html): How to create a dedicated number for Hong Kong.
- [Hungary](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-hungary.html): How to create a dedicated number for Hungary.
- [India](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-india.html): How to create a dedicated number for India.
- [Italy](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-italy.html): How to create a dedicated number for Italy.
- [Netherlands](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-netherlands.html): How to create a dedicated number for Netherlands.
- [Norway](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-norway.html): How to create a dedicated number for Norway.
- [Poland](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-poland.html): How to create a dedicated number for Poland.
- [Portugal](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-portugal.html): How to create a dedicated number for Portugal.
- [Spain](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-spain.html): How to create a dedicated number for Spain.
- [Sweden](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-sweden.html): How to create a dedicated number for Sweden.
- [United Kingdom](https://docs.aws.amazon.com/sms-voice/latest/userguide/dedicated-number-united-kingdom.html): How to create a dedicated number for United Kingdom.

### [United States 10DLC registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-10dlc.html)

Learn about the process for how to create and register a 10DLC brand and 10DLC campaign.

- [10DLC registration process](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-10dlc-setup.html): This section describes the process for how to register all 10DLC assets.
- [10DLC brand registration form](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-10dlc-company.html): How to complete the your 10DLC brand registration.
- [Resend a 10DLC brand email authentication](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-10dlc-auth.html): How to check your 10DLC brand two-factor authentication email.
- [10DLC brand vetting form](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-10dlc-vetting.html): How to submit your 10DLC company/brand for vetting.
- [10DLC campaign registration form](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-10dlc-register-campaign.html): After you've registered your company to use a 10DLC, you can register your 10DLC campaign.
- [Associating a long code with a 10DLC campaign](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-10dlc-associate.html): This section describes the process for how to associate 10DLC phone number to a 10DLC campaign.
- [10DLC cross-account access](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-10dlc-configure-cross-account-access.html): Follow these steps if you want any of your other accounts to access 10DLC numbers.

### [United States Toll-free number registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-tfn.html)

Learn how to register a toll-free phone number in the AWS End User Messaging SMS console.

- [US toll-free number registration form](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-tfn-register.html): How to complete the your toll-free phone number registration.
- [Toll-free number registration rejection reasons](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-tfn-rejection-reason.html): Learn about why your registration was rejected and how to fix it.
- [Toll-free number frequently asked questions](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-tfn-register-faq.html): Learn about frequently asked questions on the Toll-free registration process.

### [United States Short Code registration](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-us-short-code.html)

Learn about US Short Code requirements, vetting process, and registration guidelines for SMS campaigns.

- [Prepare for submission](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-us-short-code-prepare.html): Prepare documentation and review compliance requirements before submitting your US Short Code registration.
- [Brand vetting](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-us-short-code-vetting.html): Learn about the brand vetting process required by the US Short Code Registry for SMS campaigns.
- [United States Short Code registration form](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-short-code.html): How to complete the your Short Code registration.


## [Two-way SMS messaging](https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms.html)

- [Set up two-way SMS messaging for a phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms-phone-number.html): Add two-way messaging to a phone number in AWS End User Messaging SMS.
- [Set up two-way SMS messaging for a phone pool](https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms-pool.html): Add two way messaging for a phone pool.
- [IAM policies for Amazon SNS topics](https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms-iam-policy.html): How to add permissions for AWS End User Messaging SMS to access an existing Amazon SNS topic.
- [Topic policies for Amazon SNS topics](https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms-iam-policy-auto.html): Learn how to allow AWS End User Messaging SMS to access an existing Amazon SNS topic.
- [IAM policies for Amazon Connect](https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-connect-iam-policy.html): Learn how to create an IAM role for Amazon Connect to access AWS End User Messaging SMS
- [Example two-way SMS message payload](https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms-payload.html): An example of a two-way SMS message that was received by an Amazon SNS topic.


## [Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html)

- [Required opt-out keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-required.html): Learn what the required opt out keywords are and how they must be respected when a customer sends them.
- [Keyword actions](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-actions.html): Learn what actions can be performed when a customer sends you a message with a keyword.
- [Add a keyword to a phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-manage-phone-number.html): How to add a keyword to a phone number.
- [View the keywords used by a phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-phone-number-list.html): How to view all keywords associated to a phone number.
- [Edit a keyword used by a phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-phone-number-edit.html): Learn how to edit a keyword used by a phone number in the AWS End User Messaging SMS console or AWS CLI.
- [Delete a keyword from a phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-phone-number-delete.html): How to delete a keyword from a phone number.
- [Add a keyword to a phone pool](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-pool-add.html): How to add a keyword to a phone pool.
- [View keywords used by a phone pool](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-pool-list.html): How to view all keywords associated with a phone pool.
- [Edit a keyword in a phone pool](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-pool-edit.html): How to edit a keyword in a phone pool.
- [Delete a keyword from a phone pool](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-pool-delete.html): How to delete a keyword from a phone pool.


## [Configuration sets](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets.html)

- [Create a configuration set](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-create.html): Learn how to create a configuration set in the AWS End User Messaging SMS console and AWS CLI.
- [Edit a configuration set](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-edit.html): How to edit a configuration set in AWS End User Messaging SMS.
- [View all configuration sets](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-view.html): How to view all configuration sets in AWS End User Messaging SMS.
- [Delete a configuration set](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-delete.html): How to delete a configuration set in AWS End User Messaging SMS.
- [Manage tags for a configuration set](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-tags.html): Tags are pairs of keys and values that you can optionally apply to your AWS resources to control access or usage.
- [Edit a configuration set protect configuration](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-edit-protect-configuration.html): How to change a configuration set's protect configuration in AWS End User Messaging SMS.


## [Event destinations](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-event-destinations.html)

- [Event types](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-event-types.html): A list of all event types and their description for SMS, MMS, and voice.
- [Example event data](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-event-format.html): Examples of SMS, MMS and voice events in AWS End User Messaging SMS

### [Set up Amazon CloudWatch event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-cloud-watch.html)

Learn how to setup and use Amazon CloudWatch to log MMS, SMS, or voice events.

- [IAM policy for Amazon CloudWatch](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-cloud-watch-creating-role.html): Learn how to create an IAM policy for CloudWatch logging.
- [Create an Amazon CloudWatch event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-cloud-watch-add.html): Learn how to add CloudWatch logging to an AWS End User Messaging SMS configuration set.
- [Edit an Amazon CloudWatch event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-cloud-watch-edit.html): Learn how to change CloudWatch logging for an AWS End User Messaging SMS configuration set.
- [Delete an Amazon CloudWatch event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-cloud-watch-delete.html): Learn how to remove CloudWatch logging from an AWS End User Messaging SMS configuration set.

### [Set up Amazon Data Firehose event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-kinesis.html)

Learn how to use Amazon Data Firehose to log MMS, SMS, or voice events.

- [IAM policy for Amazon Data Firehose](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-kinesis-creating-role.html): Learn how to create an IAM policy for Amazon Data Firehose logging.
- [Create an Amazon Data Firehose event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-kinesis-add.html): Learn how to add Amazon Data Firehose logging to an AWS End User Messaging SMS configuration set.
- [Edit an Amazon Data Firehose event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-kinesis-edit.html): Learn how to change Amazon Data Firehose logging for an AWS End User Messaging SMS configuration set.
- [Delete an Amazon Data Firehose event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-set-kinesis-delete.html): Learn how to remove Amazon Data Firehose logging from an AWS End User Messaging SMS configuration set.

### [Set up an Amazon SNS event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-sns.html)

Learn how to use Amazon SNS to log MMS, SMS, or voice events.

- [Amazon SNS access policy](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-sns-creating-role.html): Learn how to create an IAM policy for CloudWatch logging.
- [Create an Amazon SNS event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-sns-add.html): Learn how to add Amazon SNS logging to an AWS End User Messaging SMS configuration set.
- [Edit an Amazon SNS event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-sns-edit.html): Learn how to change Amazon SNS logging for an AWS End User Messaging SMS configuration set.
- [Delete an Amazon SNS event destination](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-sns-delete.html): Learn how to delete Amazon SNS logging from an AWS End User Messaging SMS configuration set.


## [Opt-Out lists](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list.html)

- [Required opt-out list keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-keywords.html): Learn about the required opt-out keywords in AWS End User Messaging SMS
- [Self managed opt-outs](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-self-managed.html): By default, when a customer sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS automatically replies with a customizable message.
- [Set up self managed opt-outs](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-managed.html): Use AWS End User Messaging SMS to turn on self managed opt-outs.
- [Create an opt-out list](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-create.html): Learn how to create an opt-out list in AWS End User Messaging SMS
- [View origination identities](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-originators.html): Learn how to view the origination identities that use an opt-out list.
- [View the details of an opt-out list](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-view.html): Learn how to view the details of an opt-out list.
- [Add a destination phone number to an opt-out list](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-add-phone-number.html): Use AWS End User Messaging SMS to add a destination phone number to an opt-out list.
- [Search for a destination phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-search.html): Learn hot to use the AWS End User Messaging SMS console to search for a destination phone numbers in an opt-out list.
- [Remove a destination phone number](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-remove-phone-number.html): Learn how to use AWS End User Messaging SMS to remove a destination phone number from an opt-out list.
- [Delete an opt-out list](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-delete.html): Use AWS End User Messaging SMS to delete an opt-out list.
- [Manage tags for an opt-out list](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-tags.html): Tags are pairs of keys and values that you can optionally apply to your AWS resources to control access or usage.
- [List shared opt-out lists](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-shared.html): How to list all of the opt-out lists that are shared by AWS RAM using the AWS CLI


## [Message feedback](https://docs.aws.amazon.com/sms-voice/latest/userguide/message-feedback.html)

- [Enable message feedback for a configuration set](https://docs.aws.amazon.com/sms-voice/latest/userguide/message-feedback-configuraiton-set-enable.html): Learn how to enable message feedback for a configuration set.
- [Send a message with message feedback](https://docs.aws.amazon.com/sms-voice/latest/userguide/message-feedback-api-enable.html): Learn how to send a message with message feedback enabled.
- [Change a message feedback status record](https://docs.aws.amazon.com/sms-voice/latest/userguide/message-feedback-change-status.html): Learn how to set a message as received or failed with message feedback.


## [Fraud Protection](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect.html)

### [Protect configuration](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-configuration.html)

Use protect configurations to control which destination countries AWS End User Messaging SMS can send your messages to.

- [Create a protect configuration](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-configuration-create.html): Create a protect configuration in AWS End User Messaging SMS.
- [Change country rules](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-configuration-edit-countries.html): Change the countries you can send messages to with a protect configuration.
- [Change association](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-configuration-edit-association.html): Change the association of a protect configuration and configuration set.
- [Delete a protect configuration](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-configuration-delete.html): Delete a protect configuration in AWS End User Messaging SMS.
- [Set up deletion protection](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-configuration-deletion-protection.html): Use deletion protection to prevent accidental deletion of your protect configuration.
- [Rename a protect configuration](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-configuration-change-name.html): Learn how to rename a protect configuration in AWS End User Messaging SMS.
- [Manage tags for a protect configuration](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-configuration-tags.html): Tags are pairs of keys and values that you can optionally apply to your AWS resources to control access or usage.
- [Country rule modes](https://docs.aws.amazon.com/sms-voice/latest/userguide/filter-and-monitor-messages.html): Learn how to use filter and monitor modes in AWS End User Messaging SMS.
- [View protect metrics](https://docs.aws.amazon.com/sms-voice/latest/userguide/filter-and-monitor-messages-monitor.html): Learn how to View filter and monitor mode metrics in AWS End User Messaging SMS.

### [Phone number override rules](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-rule-override.html)

Learn how to use phone number overrides with protect configurations to control which destination phone number AWS End User Messaging SMS can send your messages to.

- [How phone number override rules are processed](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-rule-override-rules-processing.html): Use phone number overrides with protect configurations to control which destination phone number AWS End User Messaging SMS can send your messages to.
- [Create a phone number override rule](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-rule-override-rules-create.html): Learn how to create a country rule override in AWS End User Messaging SMS.
- [Query phone number override rule](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-rule-override-rules-querying.html): Learn how to query country rule overrides.
- [Edit a phone number override rule](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-rule-override-rules-update.html): Learn how to edit phone number override rules in AWS End User Messaging SMS.
- [Delete a phone number override rule](https://docs.aws.amazon.com/sms-voice/latest/userguide/protect-rule-override-rules-delete.html): Learn how to delete phone number override rules in AWS End User Messaging SMS.


## [Understanding SMS billing and usage reports](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-billing.html)

- [Tag AWS End User Messaging SMS resources for billing](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-billing-tag.html): How to tag resources for billing


## [Requesting support](https://docs.aws.amazon.com/sms-voice/latest/userguide/awssupport.html)

- [Requesting a spending quota change](https://docs.aws.amazon.com/sms-voice/latest/userguide/awssupport-spend-threshold.html): To request an increase to your monthly SMS spending quota, open a case with Support, and provide the required information.


## [Security](https://docs.aws.amazon.com/sms-voice/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/sms-voice/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS End User Messaging SMS.

### [Identity and access management](https://docs.aws.amazon.com/sms-voice/latest/userguide/security-iam.html)

How to authenticate requests and manage access your AWS End User Messaging SMS resources.

- [How AWS End User Messaging SMS works with IAM](https://docs.aws.amazon.com/sms-voice/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS End User Messaging SMS, learn what IAM features are available to use with AWS End User Messaging SMS.
- [Identity-based policy examples](https://docs.aws.amazon.com/sms-voice/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS End User Messaging SMS resources.
- [AWS managed policies](https://docs.aws.amazon.com/sms-voice/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS End User Messaging SMS and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/sms-voice/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give AWS End User Messaging SMS access to resources in your AWS account.
- [Troubleshooting](https://docs.aws.amazon.com/sms-voice/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS End User Messaging SMS and IAM.
- [AWS End User Messaging SMS policy actions](https://docs.aws.amazon.com/sms-voice/latest/userguide/permissions-actions.html): Manage AWS End User Messaging SMS access by adding actions to AWS End User Messaging SMS policies for users and resources in your AWS account.
- [Compliance validation](https://docs.aws.amazon.com/sms-voice/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/sms-voice/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS End User Messaging SMS features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/sms-voice/latest/userguide/infrastructure-security.html): Learn how AWS End User Messaging SMS isolates service traffic.
- [Configuration and vulnerability analysis in AWS End User Messaging SMS](https://docs.aws.amazon.com/sms-voice/latest/userguide/vulnerability-analysis-and-management.html): Learn how configuration and vulnerability analysis in AWS End User Messaging SMS.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/sms-voice/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Security best practices](https://docs.aws.amazon.com/sms-voice/latest/userguide/security-best-practices.html): AWS End User Messaging SMS security best practices.
- [SMS protocol security considerations](https://docs.aws.amazon.com/sms-voice/latest/userguide/security-protocol-considerations.html): SMS protocol considerations for security.
- [SMS protocol security best practices](https://docs.aws.amazon.com/sms-voice/latest/userguide/security-protocol-best-practices.html): SMS protocol best practices for security.


## [Monitoring](https://docs.aws.amazon.com/sms-voice/latest/userguide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/sms-voice/latest/userguide/monitoring-cloudwatch.html): You can monitor AWS End User Messaging SMS using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Create CloudWatch Alarms](https://docs.aws.amazon.com/sms-voice/latest/userguide/monitoring-sms-cw.html): Create CloudWatch Alarms to monitor AWS End User Messaging SMS metrics
- [Monitoring spending](https://docs.aws.amazon.com/sms-voice/latest/userguide/monitor-spending.html): Use CloudWatch to monitor the amount of money that you spend when you send SMS or voice messages through AWS End User Messaging SMS.
- [CloudTrail logs](https://docs.aws.amazon.com/sms-voice/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS End User Messaging SMS with AWS CloudTrail.
- [Using EventBridge](https://docs.aws.amazon.com/sms-voice/latest/userguide/monitor-event-bridge.html): Use EventBridge to monitor SMS, MMS, and voice events.
