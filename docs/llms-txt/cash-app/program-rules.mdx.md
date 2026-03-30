# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/partnerships/program-rules.mdx

***

## stoplight-id: 5459315f74833

# Program Rules

Last update: October 1, 2025

## Introduction

Block has established these Program Rules to provide a common set of rules governing a Merchant's use of Cash App Pay, establish the minimum obligations of Merchants using Cash App Pay, and provide a common payment experience for all Merchants using Cash App Pay.

These Rules may be modified by Block at its discretion to ensure the effective operation of Cash App Pay. By using Cash App Pay, Merchants agree to be bound by these Program Rules.

## Program Rules List

Here is the list of topics covered under these Program Rules. You can use the page links or the left-hand navigation to see these topics.

* [Use of Cash App Pay](#use-of-cash-app-pay)
* [Merchant Eligibility](#merchant-eligibility)
* [Payment Limits and Liability](#payment-limits-and-liability)
* [Disputes and Disputed Payments](#disputes-and-disputed-payments)
* [Use of Cash App Marks](#use-of-cash-app-marks)
* [Customer Support](#customer-support)
* [Fees, Taxes, and Incentives](#fees-taxes-and-incentives)
* [Confidentiality and Privacy](#confidentiality-and-privacy)
* [Information Security](#information-security)
* [Enforcement](#enforcement)

## Definitions

Capitalized terms used throughout these Program Rules shall have the following meanings, unless otherwise noted. If the singular is used in these Rules, it means the plural, and the plural means the singular.

| Term                                | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Applicable Data Protection Laws** | All applicable federal, state and local laws, rules and regulations of any applicable jurisdiction governing the processing of Personal Information or that otherwise relates to data protection, data security, or Data Security Breach notification obligations for Personal Information.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Applicable Laws**                 | All federal, state and local laws or regulations, network rules, and other legal requirements applicable to Cash App Pay in the respective jurisdictions in which Cash App Pay is provided, including without limitation, money transmission, anti-money laundering, anti-terrorist financing, sanctions (including those administered by the U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC)), privacy, information security, consumer protection, anti-bribery, and anti-corruption laws.                                                                                                                                                                                                          |
| **Block**                           | Block, Inc., and all of its subsidiaries and affiliates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Block Services**                  | Cash App, CAP, the CAP API, and any other Block mobile applications, websites, cloud-based solutions, software, developer kits, APIs, documents, or other Block products and services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **CAP Brand Guidelines**            | The Cash App Brand Guidelines available at [Cash App Pay Assets](/cash-app-pay-partner-api/guides/resources/cash-app-pay-assets).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **CAP Marks**                       | The Cash App logos and trademark assets set forth in the CAP Brand Guidelines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Cash App**                        | The Cash App application-based financial platform through which Customers can send peer-to-peer payments, store funds, order physical and virtual debit cards, purchase and store bitcoin, pay Merchants using Cash App Pay, and obtain financial rewards using products or services featured within the application.                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Cash App Account**                | A Cash App account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Cash App Balance**                | The funds a Customer has in their Cash App Account that are available for new transactions and are not subject to pending transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Cash App Pay (CAP)**              | The program made available by Block via the Cash App API that enables Merchants to obtain a Customer's authorization to use the Customer's Cash App Account as a payment method for Transactions with participating Merchants.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Cash App Pay API (CAP API)**      | The Application Program Interface (API) made available by Block to Merchants that enables Merchants to offer Cash App Pay as a Payment method for Customers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Cash App Privacy Notice**         | The Cash App [Privacy Notice](https://cash.app/legal/us/en-us/privacy), as amended by Block from time to time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Customer**                        | A user who has a Cash App Account and uses Cash App Pay to make one or more Payments to a Merchant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Data Security Breach**            | Any breach of confidentiality or other event that compromises the security, confidentiality, or integrity of Personal Information or other Restricted Information (as defined in the Confidentiality Section below), including any loss, misuse, or unauthorized access, disclosure, alteration, destruction or acquisition of Personal Information or other Restricted Information.                                                                                                                                                                                                                                                                                                                                           |
| **Developer Portal**                | The developer documentation available at [Cash App Pay Partner API](/cash-app-pay-partner-api/guides/welcome).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Dispute**                         | Any dispute, complaint, or error alleged by a Customer regarding a Transaction or Goods.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Goods**                           | The goods or services offered, sold, or distributed by a Merchant to a Customer that used Cash App Pay to make the Payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Liability**                       | Any and all damages (including lost profits or savings, indirect, consequential, special, exemplary, punitive, or incidental), penalties, fines, expenses and costs (including reasonable fees and expenses of legal and other advisers).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Linked Financial Instrument**     | The external bank account, debit card, credit card or other payment instrument, in each instance, linked to the Customer's Cash App Account, as permitted and enabled by Block.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Merchant**                        | A person or entity that accepts Cash App Pay in connection with Customers' Payment for Goods or to make donations. Merchants may enter into agreements with PSPs for the purpose of offering Cash App Pay to Customers, and must register, either directly or indirectly via their PSP, with Block and utilize the Cash App Pay API to process Cash App Pay Transactions for Customers. A Merchant may have one or more stores, websites, outlets, branches, or other commercial venues.                                                                                                                                                                                                                                       |
| **Merchant Use Policy (MUP)**       | The current Cash App Pay [Merchant Use Policy](/cash-app-pay-partner-api/guides/partnerships/merchant-use-policy), as amended by Block from time to time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **On File**                         | An arrangement between a Merchant and the Customer via the Merchant's Website(s), under which the Customer authorizes the use of the Cash App Pay for future Payments in one or both of the following forms:<br />• **Customer Initiated Transactions (CIT)** - A Transaction where the Customer is present on the Merchant's Website and actively initiates each Transaction without needing to log into their Cash App Account; and/or<br />• **Merchant Initiated Transactions (MIT)** - A Transaction where the Merchant initiates the Transaction without the Customer being present. MITs may include (A) one-time payments (such as capture amounts), or (B) automatic recurring payments on a fixed or variable basis. |
| **Payment**                         | A type of Transaction that uses Cash App Pay to send funds from a Customer to a Merchant to purchase Goods or to make donations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Payment Service Provider (PSP)**  | A person or entity that offers payment processing and settlement services to facilitate the purchase of, or payment of bills for, goods or services through clearance and settlement systems by agreements with other persons or entities, including Merchants. To offer Cash App Pay as a clearance and settlement system to Merchants, PSPs must enter into Cash App Pay-related service agreements with Block. Where a Merchant uses its integration with Afterpay to enable Cash App Pay via [Cash App Afterpay](/cash-app-afterpay/guides/welcome/getting-started), then Afterpay is the applicable Merchant's PSP.                                                                                                       |
| **Personal Information**            | Any information that identifies or can be used to identify, directly or indirectly, contact, or locate the individual person to whom such information pertains, and any other information subject to or governed by Applicable Data Protection Laws.<br /><br />Personal Information includes, without limitation, unique identifiers such as names, physical addresses, CashTags, photographs, government issued identification numbers, date of birth, place of birth, phone numbers, IP addresses, email addresses, and /or any other content containing Personal Information made available to Merchants in connection with the provision of Cash App Pay.                                                                 |
| **Personnel**                       | Employees, including employees of affiliates, subcontractors, and agents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Program Rules (Rules)**           | These Cash App Pay Program Rules which, along with other applicable documents and agreements, govern the use of the Cash App Pay API and the offering of Cash App Pay to Customers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Refund**                          | A type of Transaction that uses Cash App Pay to send funds from a Merchant to a Customer to refund an earlier corresponding Payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Taxes**                           | Include any and all present or future taxes, charges, fees, levies, or other assessments, including, without limitation, income, telecommunications, value-added, goods and services tax or similar taxes, gross receipts, excise, real or personal property, sales, withholding, social security, occupation, use, severance, environmental, license, net worth, payroll, employment, franchise, transfer and recording taxes, fees and charges, imposed by any domestic or foreign taxing authority.                                                                                                                                                                                                                         |
| **Transaction**                     | Money movement initiated via or processed through Cash App Pay.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Unauthorized Payment**            | Fraudulent or otherwise unauthorized Payment that: (1) arises from theft or unauthorized use of a Customer's Cash App Account or financial information related to Customer's credit card, debit card, external banking account or other user credentials, (2) occurs in an environment hosted by Block, and (3) Merchant reasonably believed the Payment was authorized and not fraudulent.                                                                                                                                                                                                                                                                                                                                    |
| **Website**                         | Website, mobile and web application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Use of Cash App Pay

Use of Cash App Pay (CAP) is entirely at Block's discretion. Block may impose limits or conditions on the use of CAP by any Merchant, Payment Service Provider (PSP), or other person, or discontinue the service at any time for any reason without notice.

CAP may only be used for purposes expressly authorized by Block. CAP may be used only to facilitate Transactions using Cash App in accordance with these Program Rules (Rules) and the Cash App Pay Merchant Use Policy (MUP). Merchants must not initiate, accept payment for, or otherwise engage in unlawful or illegal Transactions. Merchants must not violate the Rules or do anything to cause anyone else to violate these Rules. Merchants will comply with and will ensure that their Personnel comply with the Rules and will be responsible for any breach of the Rules by their Personnel.

These Rules govern Merchants' use of CAP and the Cash App Pay API (CAP API). Merchants may enter into agreements with PSPs for the purpose of offering CAP to Customers, and must register, either directly or indirectly via their PSP, with Block and utilize the CAP API to process Transactions for Customers. A Merchant may have one or more stores, Websites, outlets, branches, or other commercial venues. These Rules do not constitute a contract, promise, or agreement with any third party. A Merchant's right to use CAP may not be assigned or transferred without prior written consent from Block. Block may, in its sole discretion, disable Merchant's use of CAP at any time.

In relation to each Transaction, Merchant represents and warrants to Block that:

* Merchant does not know of or have any reason to suspect fraud or suspicious activity relating to the Transaction;
* The Transaction represents a bona fide sale by Merchant to the Customer in the ordinary course of Merchant's business;
* The purchase and Merchant's terms and conditions associated with the Transaction, as well as the Goods or donations involved in the Transaction, comply with Applicable Law;
* The Goods or donations duly comply and conform with all terms, conditions, and any warranties (express or implied) applicable to the Transaction;
* In relation to Goods that are goods: (a) the Customer has or will have title to the Goods listed and clear of all encumbrances, licenses, and claims; and (b) the Goods at the time they were delivered to the Customer were of a merchantable and acceptable quality;
* In relation to Goods that are services: (a) the Goods have been or will be provided with due care and skill; and (b) the Goods will be delivered within the agreed time frame or within a reasonable time frame if no time has been agreed for the provision of the Goods; and
* In relation to Transactions for donations, you will utilize donations received via CAP in a manner consistent with Merchant's terms and conditions and Applicable Law.

Merchants will not, will not attempt to, and will not permit anyone else to:
(1) copy, reproduce, alter, modify, create derivative works, publicly display, republish, upload, post, transmit, resell or replicate any Block Services, in whole or in part, or any other materials made available to a PSP or Merchant in connection with CAP;
(2) decompile, disassemble, reverse engineer or otherwise deconstruct any Block Services or related component; or
(3) bypass or circumvent any security features for any Block Services, or otherwise alter any Block Services, including any copyright, trademark or other proprietary right.

### Changes

Block may revise, amend, modify, or otherwise change these Rules in its sole discretion, at any time and for any reason. The most up-to-date version of the Rules will be available on the Developer Portal and/or Block's website. Merchants should review these Terms from time to time for updates and changes that may impact them.

Block will have sole discretion in the interpretation and enforcement of these Rules.

### Waivers

Block's failure to require strict adherence with any provision of these Rules on any occasion will not constitute a waiver of Block's right to require adherence with that or any other provisions of these Rules.

## Merchant Eligibility

### Overview

CAP is only available to Merchants located in the United States, and all Transactions must occur entirely within the United States.

Block reserves the right to inquire about and take any corrective action it deems appropriate if it believes or suspects that any Merchant or Transaction violates the MUP, these Rules, or is otherwise illegal or unsuitable, or to disable any Transaction or Merchant for any reason it deems prudent. Block may also report any illegal or abusive activity in accordance with Applicable Laws.

### New features

As Block introduces new features related to CAP, certain features may be available only in certain regions or only to certain types of Merchants. Any such restrictions will be listed in these Rules.

### Merchant registration

All PSPs will register each Merchant with Block through the CAP API prior to initiating a Payment. Merchants with multiple locations, that are part of a franchise or chain, or that otherwise require identification with a brand or another entity may be required to provide their PSP with additional details to facilitate registration.

### On File

Merchant may only enable use of On File with Block's prior authorization. Block may withdraw this authorization at any time in its sole discretion. Block may restrict or prohibit any type or sub-type of CIT or MIT in its sole discretion. Each use of On File must comply with the Customer's prior On File authorization, any limits set by Block, and all Applicable Laws. Merchant must provide Block with sufficient information (such as metadata) as Block requires from time to time to: (1) allow Block to determine if a Transaction is a CIT or MIT and (2) for MITs, show the Customer's authorization.

When a Customer authorizes use of On File for future Payments, Block will issue a token to Merchant to be stored against that Customer's account with Merchant. Merchant may only use the token to initiate transactions that are consistent with the Customer's authorization. Merchant may not use any token for a Customer who has cancelled their On File authorization. A Customer may cancel their authorization either directly with Block or through Merchant's Website(s) or terms. Merchant must promptly notify PSP and Block if a Customer cancels On File authorization or if Merchant cancels the Customer's On File authorization. Merchant must ensure that the Customer can easily cancel their On File authorization at any time, via a clearly accessible option on Merchant's Website(s) or in Merchant's checkout flow.

To the fullest extent permitted by law, Merchant agrees to promptly reimburse Block from and for all claims, liabilities, losses, damages, costs and expenses Block incurs directly or indirectly from, or in connection with, any actual or alleged data breach, system failure, or unauthorized access to or use of Merchant's On File system where the Customer has elected to save or store their Cash App Account details with Merchant.

### Compliance

By utilizing CAP, Merchants agree to comply with and will ensure that all of its Personnel comply with all Applicable Laws.

Merchants will maintain all necessary licenses, permits, approvals and registrations from all applicable state, local and federal regulatory and governmental authorities. Transactions must be lawful in all of the following jurisdictions: (1) where the Customer resides, (2) where Merchant resides, and (3) where the Transaction occurs.

#### Information Requests and Investigations

Block may request information from Merchants in order to investigate Disputes; to validate adherence to, or to investigate violations of, these Rules, the MUP or other agreements; to respond to requests from law enforcement, regulatory, or other governmental entities; and for other routine business needs. Merchants will, at any time requested by Block, provide information related to CAP activities or otherwise facilitate collection and transmission of the requested information to Block. Requests will be sent to the contact information provided by Merchant at the time of registration with CAP or as otherwise provided to Block. Merchant will promptly notify Block of updated contact information in the event of a change of relevant Personnel.

Merchants will respond to and comply with Block's requests within a commercially reasonable timeframe not to exceed 10 business days.

#### Termination of a Merchant as a Result of Compliance Concerns

If Block determines, in its sole discretion, that a Merchant is submitting Transactions that violate these Rules, the MUP, or any Applicable Laws, Block may decline any Transaction or series of Transactions, suspend Merchant's participation in CAP until Merchant resolves its violations, subject to a resolution that is sufficient in Block's sole discretion, and/or terminate or decline to allow a Merchant to participate in CAP. Block may, in its sole discretion, provide Merchant the opportunity to cure violations prior to suspending or terminating Merchant's participation in CAP.

## Payment Limits and Liability

### Limits

Block implements Customer, Transaction, and velocity limits at its discretion for risk and compliance purposes. These limits may affect a Merchant's ability to process Transactions or a Customer's ability to make a Payment using CAP. Block may change these limits at any time and in its sole discretion.

### Liability

Merchants are responsible to Block for any Transaction submitted to CAP whether or not the Customer returns the underlying Goods to Merchant.

Block will only be liable to a Merchant for lost or misdirected funds for Transactions, and only if the loss or misdirection is caused solely and directly by Block. In such a case, Block will be liable only up to the authorization amount of the lost or misdirected Payment. Block will not be liable for any indirect, incidental, consequential, special, punitive, or other damages, and Block will not be liable to any third parties as a result of any lost or misdirected Payment.

## Disputes and Disputed Payments

### Refunds

Merchant will disclose its return/cancellation policy on its Websites. Merchant's policies and agreements (including applicable return/cancellation policy, complaints policy, treating customers fairly policy, and information security policies) with Customers will comply with Applicable Laws. Merchant will consider any Customer's request for a Refund in good faith and in accordance with Merchant's policies and Applicable Laws. A Refund will not exceed the total amount of the applicable Transaction. Merchant will not accept cash or any other consideration from Customer in exchange for issuing a Refund. Merchant will not give cash refunds in connection with a Transaction unless required by Applicable Laws. Please see Cash App Pay's Technical Guide on Refunds for more information regarding Refunds.

### Merchant expectations

Merchants will make a good faith attempt to promptly resolve any issues associated with a Transaction and to minimize the number of Disputes. Merchants are expected to be a Customer's first point of contact for issues, grievances, and other Customer support issues related to a Transaction, except as otherwise provided in these Rules.

### Errors related to Transactions

Only Customers can file Disputes. If a Customer believes there is an error related to a Transactions or has questions regarding a Transaction, Customer may:

* For Payments originating from Customer's Linked Financial Instrument, Customer must either (1) contact their issuing financial institution, or (2) contact Block via the procedure set forth in the Cash App Terms of Service.
* For Payments originating from Customer's Cash App Balance, Customers must follow the procedure set forth in the Cash App Terms of Service.

### Dispute liability and review

#### Unauthorized Payments

Block will assume Liability on behalf of Merchants for all Unauthorized Payments.

Block may restrict, suspend, or terminate a Merchant's use of CAP if Block, in its sole discretion, suspects Merchant of enabling or otherwise failing to prevent Unauthorized Payments, and Block reserves all rights to seek recovery from Merchant in such cases. Merchant will provide all information as reasonably requested by Block to facilitate Block's investigation of potential Unauthorized Payments.

#### Disputes

Except as required by Applicable Law (including Block's obligations under the Electronic Funds Transfer Act and Regulation E), Merchant will be liable for any Dispute resolved in the Customer's favor where such Dispute did not arise from an Unauthorized Payment. Merchant will receive notice of these Disputes via their PSP and will have the opportunity to provide supporting evidence for rebuttal. Merchants will respond to and handle Disputes in accordance with Cash App Pay's Technical Guide on Disputes.

If Merchant, whether directly or indirectly via a PSP, provides evidence to contest a Dispute, the Dispute will be reviewed and adjudicated by either Block or the Customer's financial institution, depending on where the Dispute was filed.

All Dispute adjudication decisions are final and may not be appealed.

### Dispute and risk monitoring

Block monitors all Dispute activity and notifies PSPs when any Merchant to whom they provide CAP-related services has excessive Dispute volumes. Once a PSP is notified of and provides notice to Merchant of excessive Disputes, Merchants will work to reduce their Dispute activity, including promptly responding to customer inquiries and operating as Customer's first point of contact with respect to Disputes. Block may, in its sole discretion, restrict Merchant's ability to use CAP if Merchant fails to take appropriate steps to reduce Dispute activity.

Block reserves the right to impose additional requirements or penalties on Merchants that have excessive Dispute volumes, including, but not limited to, increased reserve requirements, additional fee downgrades, liability shifting for Unauthorized Payments, and/or otherwise limiting, restricting, suspending, or terminating a Merchant's access to CAP. Further, Block will monitor Transactions for suspicious behavior and fraud claims brought against Merchants.

## Use of Cash App Marks

Merchants shall use commercially reasonable efforts to treat CAP equally to any other payment methods offered at their points of sale and on their Websites. This includes equal or better logo placement and position within any point of sale or Website, as well as equal or better treatment in any payment flow, terms and conditions, marketing or advertising materials, or fee structure. Further, Merchants shall endeavor to not indicate a preference for any payment type over CAP.

Block grants Merchant a non-exclusive, non-transferable, revocable and royalty free license to use and reproduce the CAP Marks solely within the U.S. and solely in connection with Merchant's display of CAP on its Websites or in-store(s) (as applicable), and checkout page, and as permitted under these Rules and any other written directions Block may issue from time to time including any use guidelines. Merchants must immediately discontinue, modify or change the use or display of the CAP Marks whenever instructed by PSP or Block.

Merchant's use of CAP Marks must adhere to the CAP Brand Guidelines. Block is the exclusive owner of the "Block", "Cash App", "Cash App Pay", and the CAP Marks. Merchant will not use the CAP Marks to indicate endorsement or affiliation with Block or Cash App without Block's prior express written consent. Merchant will not use the CAP Marks in any way that dilutes the goodwill or reputation of Block or any of its affiliates, brands, or programs. All use of the CAP Marks will inure for the benefit of Block.

## Customer Support

Block will provide Customers with customer support for technical issues related to Payments made or attempted with CAP.

Merchants will provide Customers with customer support for all other issues, including, but not limited to, Customers' inquiries related to the Goods or donations.

If Merchants need to direct Customers to contact Block to resolve an issue, they can instruct Customers to reach Cash App customer support directly in Cash App or by calling +1(800) 969-1940.

## Fees, Taxes, and Incentives

### Fees and Taxes

#### Transaction fees

Merchants will pay a fee for each Transactions in accordance with the terms of the applicable service agreement between Merchant and the PSP or Block.

#### No surcharges

Unless required by Applicable Laws, Merchants may not charge Customers a surcharge, convenience fee, or any other fee, or otherwise increase the price of any Goods, for accepting CAP as a payment method.

#### Taxes

Merchants are responsible and liable, as required under Applicable Law, for determining and paying any and all Taxes required to be assessed, incurred, collected, paid, or withheld for their use of CAP. Merchants are also responsible and liable for:

* Determining whether Taxes apply to their sale of Goods, Payments received, donations received, and any other transactions arising from or out of their use of CAP; and
* Calculating, collecting, reporting or remitting any Taxes to the appropriate tax and revenue authorities. Block specifically disclaims any liability for such Taxes.

### Incentives

Block may (unilaterally or in partnership with Merchant) offer incentives for Customers to use CAP or otherwise market or promote the use of CAP. Such incentives, marketing activities, or promotions are offered at Block's discretion, are not guaranteed, and may be discontinued, suspended, or modified by Block at any time.

## Confidentiality and Privacy

By offering or using CAP, Merchant represents, warrants, and covenants that it is and will remain in compliance with all Applicable Data Protection Laws and will process all Personal Information in compliance with all Applicable Data Protection Laws. Where necessary, Merchant will provide any necessary disclosures and/or obtain any necessary consents to provide Personal Information to Block.

Merchant must ensure all Restricted Information is kept strictly confidential and used only in connection with Payments or as otherwise provided for in these Rules or permitted by Block. Merchants will, upon request from Block, return or destroy any Restricted Information in its possession or control. "Restricted Information" includes any of the following:

* Any information transmitted by Block to a PSP or Merchant in connection with any Transaction,
* Any Cash App Account or Customer's Personal Information provided by Block to a PSP or Merchant,
* Any other information subject to or governed by Applicable Data Protection Laws, and
* Any non-public information shared by Block during discussions or negotiations related to CAP including, without limitation, proprietary technical information regarding CAP; information regarding Cash App's customers or customer base; product roadmap, marketing plans and strategies, market research, and other market information; costs, fees, and other financial data; and any other data of a confidential or proprietary nature.

Further, unless required by Applicable Laws, Merchant may not disclose to any third party or use any Cash App Account or Customer Personal Information other than to complete a Transaction, to resolve a Transaction-related Dispute, to perform risk evaluation and fraud prevention, or to provide an enhanced customer experience by providing access to transaction histories, receipts, and notifications. Block may use Restricted Information or Transaction-related information it receives from a Merchant to process  Transactions and as otherwise permitted under the Cash App Privacy Notice.

If Merchant is served with a court order, subpoena, civil investigative demand, or similar legal process compelling disclosure of Customer Personal Information, Merchant will promptly notify Block (and in any event within 48 hours)  and cooperate in good faith with Block in the event Block opposes disclosure. Merchant will limit the scope of such disclosure to what is strictly required by Applicable Laws.

Cash App Customer Personal Information and Cash App Account data is the proprietary information of Block. Block and Merchant are not providing or making available any Personal Information to the other for any consideration, and any such provision of Personal Information to the other shall not constitute a "sale" of Personal Information under any Applicable Data Protection Laws.

## Information Security

Block requires all Merchants interacting with CAP data to follow best practices for securing financial and Customer Personal Information data. This includes, but is not limited to:

* Implementing multi-factor authentication and role-based access controls and granting Personnel the least privilege necessary for job function
* Reviewing access controls periodically and disabling Personnel access upon departure
* Encrypting all data transmitted with the CAP API in transit
* Encrypting all data received from the CAP API at rest
* Conducting routine security audits and penetration tests of systems interacting with CAP data and credentials
* Implementing logging for access to CAP data
* Installing software security patches and updates in a timely manner
* Securing access to CAP data and credentials
* Rotating certificates and API keys for interacting with the CAP API on a routine basis
* Implementing controls designed to prevent intrusion or unauthorized access to Merchant's systems and Personal Information, including virus protection software, firewalls, intrusion prevention technologies and other measures designed to ensure appropriate levels of access are restricted to authorized Personnel
* Personnel training and controls, such as communication of all applicable security policies and confidentiality obligations, background checks (as permitted by Applicable Data Protection Laws), user authentication, security awareness training, and disciplinary processes
* Written confidentiality agreements governing access to Restricted Information by Personnel
* Controls designed to ensure the physical safety and security of Merchant's facilities, including, without limitation, records of access

Detailed requirements for information security are available on the Developer Portal. Block may revise, amend, modify, or otherwise change information security requirements at any time and for any reason. Merchants should, either directly or indirectly via their PSP, implement these requirements as soon as possible when updated to ensure the safety of Cash App Customers' data and finances.

In the event a Merchant determines that there has been any actual or suspected Data Security Breach, Merchant shall, without undue delay (and in any event within 48 hours), notify Block (via email to [breachnotifications@block.xyz](mailto:breachnotifications@block.xyz) , which may be updated from time to time) of the actual or suspected Data Security Breach. Merchant shall promptly initiate an investigation into the circumstances surrounding such Data Security Breach and shall reasonably cooperate with Block in remedying and addressing any such Data Security Breach.

## Enforcement

### General Enforcement

If Merchant is in breach of these Rules or any CAP-related agreements or terms, Block may take a number of actions at any time in its sole discretion. These include, but are not limited to:

* Assessing fee downgrades or other financial penalties
* Limiting Merchant's access to CAP
* Suspending or terminating Merchant's account or Merchant's access to and use of CAP
* Refusing to provide CAP services to Merchant in the future
* Reporting Merchant to the appropriate legal authorities
* Contacting Customers who have purchased Goods from a Merchant using CAP
* Other legal action

Except in circumstances described below where Block is permitted to terminate or suspend Merchant's CAP services immediately, prior to taking any action, Block will: (1) provide a Merchant with notice of the breach and, when practical, provide reasonable advance notice and an opportunity to cure, and (2) use reasonable efforts to attempt to resolve the matter in good faith. Merchant will use reasonable efforts to resolve any breach in good faith. Failure to cure the breach will result in termination of a Merchant's ability to use or offer CAP.

### Immediate Enforcement

Block may terminate or suspend a Merchant's use of CAP immediately (or for such other date as notified to Merchant) if:

* Merchant breaches these Program Rules or any CAP-related agreements and such breach is incapable of remedy;
* Merchant breaches the MUP;
* Merchant experiences a Data Security Breach;
* Block reasonably believes Merchant is engaging or has engaged in fraudulent activity or conduct; or
* Block is required to do so by any regulatory authority or in order to comply with Applicable Laws (including any change in Applicable Laws).
