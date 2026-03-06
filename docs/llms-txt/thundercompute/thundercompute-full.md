# Thundercompute Documentation

Source: https://www.thundercompute.com/docs/llms-full.txt

---

# Add SSH key to instance
Source: https://www.thundercompute.com/docs/api-reference/instances/add-ssh-key-to-instance

https://api.thundercompute.com:8443/openapi.json post /instances/{id}/add_key
Add an SSH key to an existing instance. If public_key is provided in the request body, it will be added to authorized_keys. If no public_key is provided, a new key pair will be generated and the private key returned.



# Create instance
Source: https://www.thundercompute.com/docs/api-reference/instances/create-instance

https://api.thundercompute.com:8443/openapi.json post /instances/create
Create a new compute instance



# Delete instance
Source: https://www.thundercompute.com/docs/api-reference/instances/delete-instance

https://api.thundercompute.com:8443/openapi.json post /instances/{id}/delete
Delete a compute instance by ID



# List instances
Source: https://www.thundercompute.com/docs/api-reference/instances/list-instances

https://api.thundercompute.com:8443/openapi.json get /instances/list
Get a list of user's compute instances



# Modify instance
Source: https://www.thundercompute.com/docs/api-reference/instances/modify-instance

https://api.thundercompute.com:8443/openapi.json post /instances/{id}/modify
Modify a running compute instance's resources



# Create a snapshot
Source: https://www.thundercompute.com/docs/api-reference/snapshots/create-a-snapshot

https://api.thundercompute.com:8443/openapi.json post /snapshots/create
Create a new snapshot from a running instance



# Delete a snapshot
Source: https://www.thundercompute.com/docs/api-reference/snapshots/delete-a-snapshot

https://api.thundercompute.com:8443/openapi.json delete /snapshots/{id}
Delete a snapshot by ID



# List snapshots
Source: https://www.thundercompute.com/docs/api-reference/snapshots/list-snapshots

https://api.thundercompute.com:8443/openapi.json get /snapshots/list
Get a list of all snapshots for the authenticated user's organization



# Add an SSH key
Source: https://www.thundercompute.com/docs/api-reference/ssh-keys/add-an-ssh-key

https://api.thundercompute.com:8443/openapi.json post /keys/add
Add a new SSH public key to the authenticated user's organization



# Delete an SSH key
Source: https://www.thundercompute.com/docs/api-reference/ssh-keys/delete-an-ssh-key

https://api.thundercompute.com:8443/openapi.json delete /keys/{id}
Delete an SSH key by ID



# List SSH keys
Source: https://www.thundercompute.com/docs/api-reference/ssh-keys/list-ssh-keys

https://api.thundercompute.com:8443/openapi.json get /keys/list
Get a list of all SSH keys for the authenticated user's organization



# Get current pricing
Source: https://www.thundercompute.com/docs/api-reference/utilities/get-current-pricing

https://api.thundercompute.com:8443/openapi.json get /pricing
Retrieve current hourly pricing information for compute resources



# Get thunder templates
Source: https://www.thundercompute.com/docs/api-reference/utilities/get-thunder-templates

https://api.thundercompute.com:8443/openapi.json get /thunder-templates
Get available thunder templates for instance creation



# Billing
Source: https://www.thundercompute.com/docs/billing

Understand Thunder Compute's usage-based billing, payment methods, billing alerts, current rates, and tips for saving on GPU cloud costs.

## Payment Options

There are **two ways to pay** for Thunder Compute:

### Option 1: Auto-Pay

Set up auto-pay by saving a credit card in the Stripe customer portal. Open it from [console.thundercompute.com/settings/billing](https://console.thundercompute.com/settings/billing) by clicking "manage billing".

### Option 2: Preload Credit

Add credit directly to your account as an alternative to auto-pay. This credit never expires and will be used before any saved payment method.

**Order of payment**

1. Any preloaded credit you've added
2. Charges to your saved payment method

You can switch between options or use both—set up auto-pay anytime, even if you started with preloaded credit.

## Billing Alerts

* **Instance reminders:** We'll email you about any running instances so you're never caught off guard.
* **Threshold charges:** As your usage grows, we'll bill your card at preset checkpoints (which rise over time) to prevent runaway bills.

## Our rates

All compute resources are billed per minute only while your instances run. Rates and promotions are subject to change without notice. For current rates, see our [pricing page](https://www.thundercompute.com/pricing).

## Credit Terms

* **Preloaded credit** does not expire and will be used before charging your saved card.
* **Promotional credit** can be revoked at our discretion.
* **Refunds:** Credit is non-refundable.

## Money-Saving Tips

While Thunder Compute is already the cheapest GPU cloud platform, there are a few strategies we recommend to reduce your bill:

* Delete instances when you're done with them to stop billing.
* Right‑size new workloads with `tnr create --gpu`, `--vcpus`, and related flags so you only pay for what you use.

We think this balances a smooth experience with strong verification—but if you have feedback or questions, please hop into our [Discord](https://discord.com/invite/nwuETS9jJK). We're always happy to improve!


# Data Processing Addendum
Source: https://www.thundercompute.com/docs/guides/data-processing-addendum

Our Data Processing Addendum outlining data handling and privacy terms.

## Sample Agreement

Data Processing Agreement

## Using this DPA

This DPA has 2 parts: (1) the Key Terms on this Cover Page and (2) the Common Paper DPA Standard Terms Version 1 posted at commonpaper.com/standards/data-processing-agreement/1.1 (“DPA Standard Terms”), which is incorporated by reference. If there is any inconsistency between the parts of the DPA, the Cover Page will control over the DPA Standard Terms. Capitalized and highlighted words have the meanings given on the Cover Page. However, if the Cover Page omits or does not define a highlighted word, the default meaning will be “none” or “not applicable” and the correlating clause, sentence, or section does not apply to this Agreement. All other capitalized words have the meanings given in the DPA Standard Terms or the Agreement. A copy of the DPA Standard Terms is attached for convenience only.

## Key Terms

The key legal terms of the DPA are as follows:

| Term                      | Details                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| Agreement                 | Reference to sales contract will be set when sending agreement                                 |
| Approved Subprocessors    | [https://www.thundercompute.com/sub-processors](https://www.thundercompute.com/sub-processors) |
| Provider Security Contact | `support@thundercompute.com`                                                                   |
| Security Policy           | As defined in the Agreement.                                                                   |

### Service Provider Relationship

To the extent California Consumer Privacy Act, Cal. Civ. Code § 1798.100 et seq (“CCPA”) applies, the parties acknowledge and agree that Provider is a service provider and is receiving Personal Data from Customer to provide the Service as agreed in the Agreement and detailed below (see Nature and Purpose of Processing), which constitutes a limited and specified business purpose. Provider will not sell or share any Personal Data provided by Customer under the Agreement. In addition, Provider will not retain, use, or disclose any Personal Data provided by Customer under the Agreement except as necessary for providing the Service for Customer, as stated in the Agreement, or as permitted by Applicable Data Protection Laws. Provider certifies that it understands the restrictions of this paragraph and will comply with all Applicable Data Protection Laws. Provider will notify Customer if it can no longer meet its obligations under the CCPA.

## Restricted Transfers

### Governing Member State

* EEA Transfers: Ireland
* UK Transfers: England and Wales

## Annex I(A) List of Parties

### Data Exporter

* Name: the Customer signing this DPA
* Activities relevant to transfer: See Annex I(B)
* Role: Controller

### Data Importer

* Name: the Provider signing this DPA
* Contact person: Carl Peterson, CEO
* Address: 887 w marietta st nw, Suite N105, Georgia 30318, USA
* Activities relevant to transfer: See Annex I(B)
* Role: Processor

## Annex I(B) Description of Transfer and Processing Activities

### Service

The Service is: GPU cloud computing with on-demand cloud instances, backed by physical servers, in addition to data storage.

### Categories of Data Subjects

* Customer's employees

### Categories of Personal Data

* Name
* Contact information such as email, phone number, or address
* Financial information such as bank account numbers
* Transactional information such as account information or purchases
* User activity and analysis such as device information or IP address
* Location information

### Special Category Data

Is special category data (as defined in Article 9 of the GDPR) Processed? No

### Frequency of Transfer

Continuous

### Nature and Purpose of Processing

* Receiving data, including collection, accessing, retrieval, recording, and data entry
* Holding data, including storage, organization, and structuring
* Using data, including analysis, consultation, testing, automated decision making, and profiling
* Updating data, including correcting, adaption, alteration, alignment, and combination
* Protecting data, including restricting, encrypting, and security testing
* Sharing data, including disclosure, dissemination, allowing access, or otherwise making available
* Returning data to the data exporter or data subject
* Erasing data, including destruction and deletion

### Duration of Processing

Provider will process Customer Personal Data as long as required (i) to conduct the Processing activities instructed in Section 2.2(a)-(d) of the Standard Terms; or (ii) by Applicable Laws.

## Annex I(C)

### Competent Supervisory Authority

The supervisory authority will be the supervisory authority of the data exporter, as determined in accordance with Clause 13 of the EEA SCCs or the relevant provision of the UK Addendum.

## Annex II

### Technical and Organizational Security Measures

See Security Policy

Provider and Customer have not changed the DPA Standard Terms except for the details on the Cover Page above. By signing this Cover Page, each party agrees to enter into this DPA as of the last date of signature below.

## Signatures

| Field                | Provider (Thunder Compute) | Customer |
| -------------------- | -------------------------- | -------- |
| Signature            |                            |          |
| Print Name           |                            |          |
| Title                |                            |          |
| Legal Notice Address | `carl@thundercompute.com`  |          |
| Date                 |                            |          |

## 1. Processor and Subprocessor Relationships

### 1.1 Provider as Processor

In situations where Customer is a Controller of the Customer Personal Data, Provider will be deemed a Processor that is Processing Personal Data on behalf of Customer.

### 1.2 Provider as Subprocessor

In situations where Customer is a Processor of the Customer Personal Data, Provider will be deemed a Subprocessor of the Customer Personal Data.

## 2. Processing

### 2.1 Processing Details

Annex I(B) on the Cover Page describes the subject matter, nature, purpose, and duration of this Processing, as well as the Categories of Personal Data collected and Categories of Data Subjects.

### 2.2 Processing Instructions

Customer instructs Provider to Process Customer Personal Data: (a) to provide and maintain the Service; (b) as may be further specified through Customer’s use of the Service; (c) as documented in the Agreement; and (d) as documented in any other written instructions given by Customer and acknowledged by Provider about Processing Customer Personal Data under this DPA. Provider will abide by these instructions unless prohibited from doing so by Applicable Laws. Provider will immediately inform Customer if it is unable to follow the Processing instructions. Customer has given and will only give instructions that comply with Applicable Laws.

### 2.3 Processing by Provider

Provider will only Process Customer Personal Data in accordance with this DPA, including the details in the Cover Page. If Provider updates the Service to update existing or include new products, features, or functionality, Provider may change the Categories of Data Subjects, Categories of Personal Data, Special Category Data, Special Category Data Restrictions or Safeguards, Frequency of Transfer, Nature and Purpose of Processing, and Duration of Processing as needed to reflect the updates by notifying Customer of the updates and changes.

### 2.4 Customer Processing

Where Customer is a Processor and Provider is a Subprocessor, Customer will comply with all Applicable Laws that apply to Customer’s Processing of Customer Personal Data. Customer’s agreement with its Controller will similarly require Customer to comply with all Applicable Laws that apply to Customer as a Processor. In addition, Customer will comply with the Subprocessor requirements in Customer’s agreement with its Controller.

### 2.5 Consent to Processing

Customer has complied with and will continue to comply with all Applicable Data Protection Laws concerning its provision of Customer Personal Data to Provider and/or the Service, including making all disclosures, obtaining all consents, providing adequate choice, and implementing relevant safeguards required under Applicable Data Protection Laws.

### 2.6 Subprocessors

1. Provider will not provide, transfer, or hand over any Customer Personal Data to a Subprocessor unless Customer has approved the Subprocessor. The current list of Approved Subprocessors includes the identities of the Subprocessors, their country of location, and their anticipated Processing tasks. Provider will inform Customer at least 10 business days in advance and in writing of any intended changes to the Approved Subprocessors whether by addition or replacement of a Subprocessor, which allows Customer to have enough time to object to the changes before the Provider begins using the new Subprocessor(s). Provider will give Customer the information necessary to allow Customer to exercise its right to object to the change to Approved Subprocessors. Customer has 30 days after notice of a change to the Approved Subprocessors to object, otherwise Customer will be deemed to accept the changes. If Customer objects to the change within 30 days of notice, Customer and Provider will cooperate in good faith to resolve Customer’s objection or concern.
2. When engaging a Subprocessor, Provider will have a written agreement with the Subprocessor that ensures the Subprocessor only accesses and uses Customer Personal Data (i) to the extent required to perform the obligations subcontracted to it, and (ii) consistent with the terms of Agreement.
3. If the GDPR applies to the Processing of Customer Personal Data, (i) the data protection obligations described in this DPA (as referred to in Article 28(3) of the GDPR, if applicable) are also imposed on the Subprocessor, and (ii) Provider’s agreement with the Subprocessor will incorporate these obligations, including details about how Provider and its Subprocessor will coordinate to respond to inquiries or requests about the Processing of Customer Personal Data. In addition, Provider will share, at Customer’s request, a copy of its agreements (including any amendments) with its Subprocessors. To the extent necessary to protect business secrets or other confidential information, including personal data, Provider may redact the text of its agreement with its Subprocessor prior to sharing a copy.
4. Provider remains fully liable for all obligations subcontracted to its Subprocessors, including the acts and omissions of its Subprocessors in Processing Customer Personal Data. Provider will notify Customer of any failure by its Subprocessors to fulfill a material obligation about Customer Personal Data under the agreement between Provider and the Subprocessor.

## 3. Restricted Transfers

### 3.1 Authorization

Customer agrees that Provider may transfer Customer Personal Data outside the EEA, the United Kingdom, or other relevant geographic territory as necessary to provide the Service. If Provider transfers Customer Personal Data to a territory for which the European Commission or other relevant supervisory authority has not issued an adequacy decision, Provider will implement appropriate safeguards for the transfer of Customer Personal Data to that territory consistent with Applicable Data Protection Laws.

### 3.2 Ex-EEA Transfers

Customer and Provider agree that if the GDPR protects the transfer of Customer Personal Data, the transfer is from Customer from within the EEA to Provider outside of the EEA, and the transfer is not governed by an adequacy decision made by the European Commission, then by entering into this DPA, Customer and Provider are deemed to have signed the EEA SCCs and their Annexes, which are incorporated by reference. Any such transfer is made pursuant to the EEA SCCs, which are completed as follows:

1. Module Two (Controller to Processor) of the EEA SCCs apply when Customer is a Controller and Provider is Processing Customer Personal Data for Customer as a Processor.
2. Module Three (Processor to Sub-Processor) of the EEA SCCs apply when Customer is a Processor and Provider is Processing Customer Personal Data on behalf of Customer as a Subprocessor.
3. For each module, the following applies (when applicable):
   * The optional docking clause in Clause 7 does not apply;
   * In Clause 9, Option 2 (general written authorization) applies, and the minimum time period for prior notice of Subprocessor changes is 10 business days;
   * In Clause 11, the optional language does not apply;
   * All square brackets in Clause 13 are removed;
   * In Clause 17 (Option 1), the EEA SCCs will be governed by the laws of Governing Member State;
   * In Clause 18(b), disputes will be resolved in the courts of the Governing Member State; and
   * The Cover Page to this DPA contains the information required in Annex I, Annex II, and Annex III of the EEA SCCs.

### 3.3 Ex-UK Transfers

Customer and Provider agree that if the UK GDPR protects the transfer of Customer Personal Data, the transfer is from Customer from within the United Kingdom to Provider outside of the United Kingdom, and the transfer is not governed by an adequacy decision made by the United Kingdom Secretary of State, then by entering into this DPA, Customer and Provider are deemed to have signed the UK Addendum and their Annexes, which are incorporated by reference. Any such transfer is made pursuant to the UK Addendum, which is completed as follows:

1. Section 3.2 of this DPA contains the information required in Table 2 of the UK Addendum.
2. Table 4 of the UK Addendum is modified as follows: Neither party may end the UK Addendum as set out in Section 19 of the UK Addendum; to the extent ICO issues a revised Approved Addendum under Section ‎18 of the UK Addendum, the parties will work in good faith to revise this DPA accordingly.
3. The Cover Page contains the information required by Annex 1A, Annex 1B, Annex II, and Annex III of the UK Addendum.

### 3.4 Other International Transfers

For Personal Data transfers where Swiss law (and not the law in any EEA member state or the United Kingdom) applies to the international nature of the transfer, references to the GDPR in Clause 4 of the EEA SCCs are, to the extent legally required, amended to refer to the Swiss Federal Data Protection Act or its successor instead, and the concept of supervisory authority will include the Swiss Federal Data Protection and Information Commissioner.

## 4. Security Incident Response

Upon becoming aware of any Security Incident, Provider will: (a) notify Customer without undue delay when feasible, but no later than 72 hours after becoming aware of the Security Incident; (b) provide timely information about the Security Incident as it becomes known or as is reasonably requested by Customer; and (c) promptly take reasonable steps to contain and investigate the Security Incident. Provider’s notification of or response to a Security Incident as required by this DPA will not be construed as an acknowledgment by Provider of any fault or liability for the Security Incident.

## 5. Audit & Reports

### 5.1 Audit Rights

Provider will give Customer all information reasonably necessary to demonstrate its compliance with this DPA and Provider will allow for and contribute to audits, including inspections by Customer, to assess Provider’s compliance with this DPA. However, Provider may restrict access to data or information if Customer’s access to the information would negatively impact Provider’s intellectual property rights, confidentiality obligations, or other obligations under Applicable Laws. Customer acknowledges and agrees that it will only exercise its audit rights under this DPA and any audit rights granted by Applicable Data Protection Laws by instructing Provider to comply with the reporting and due diligence requirements below. Provider will maintain records of its compliance with this DPA for 3 years after the DPA ends.

### 5.2 Security Reports

Customer acknowledges that Provider is regularly audited against the standards defined in the Security Policy by independent third-party auditors. Upon written request, Provider will give Customer, on a confidential basis, a summary copy of its then-current Report so that Customer can verify Provider’s compliance with the standards defined in the Security Policy.

### 5.3 Security Due Diligence

In addition to the Report, Provider will respond to reasonable requests for information made by Customer to confirm Provider’s compliance with this DPA, including responses to information security, due diligence, and audit questionnaires, or by giving additional information about its information security program. All such requests must be in writing and made to the Provider Security Contact and may only be made once a year.

## 6. Coordination & Cooperation

### 6.1 Response to Inquiries

If Provider receives any inquiry or request from anyone else about the Processing of Customer Personal Data, Provider will notify Customer about the request and Provider will not respond to the request without Customer’s prior consent. Examples of these kinds of inquiries and requests include a judicial or administrative or regulatory agency order about Customer Personal Data where notifying Customer is not prohibited by Applicable Law, or a request from a data subject. If allowed by Applicable Law, Provider will follow Customer’s reasonable instructions about these requests, including providing status updates and other information reasonably requested by Customer. If a data subject makes a valid request under Applicable Data Protection Laws to delete or opt out of Customer’s giving of Customer Personal Data to Provider, Provider will assist Customer in fulfilling the request according to the Applicable Data Protection Law. Provider will cooperate with and provide reasonable assistance to Customer, at Customer’s expense, in any legal response or other procedural action taken by Customer in response to a third-party request about Provider’s Processing of Customer Personal Data under this DPA.

### 6.2 DPIAs and DTIAs

If required by Applicable Data Protection Laws, Provider will reasonably assist Customer in conducting any mandated data protection impact assessments or data transfer impact assessments and consultations with relevant data protection authorities, taking into consideration the nature of the Processing and Customer Personal Data.

## 7. Deletion of Customer Personal Data

### 7.1 Deletion by Customer

Provider will enable Customer to delete Customer Personal Data in a manner consistent with the functionality of the Services. Provider will comply with this instruction as soon as reasonably practicable except where further storage of Customer Personal Data is required by Applicable Law.

### 7.2 Deletion at DPA Expiration

1. After the DPA expires, Provider will return or delete Customer Personal Data at Customer’s instruction unless further storage of Customer Personal Data is required or authorized by Applicable Law. If return or destruction is impracticable or prohibited by Applicable Laws, Provider will make reasonable efforts to prevent additional Processing of Customer Personal Data and will continue to protect the Customer Personal Data remaining in its possession, custody, or control. For example, Applicable Laws may require Provider to continue hosting or Processing Customer Personal Data.
2. If Customer and Provider have entered the EEA SCCs or the UK Addendum as part of this DPA, Provider will only give Customer the certification of deletion of Personal Data described in Clause 8.1(d) and Clause 8.5 of the EEA SCCs if Customer asks for one.

## 8. Limitation of Liability

### 8.1 Liability Caps and Damages Waiver

To the maximum extent permitted under Applicable Data Protection Laws, each party’s total cumulative liability to the other party arising out of or related to this DPA will be subject to the waivers, exclusions, and limitations of liability stated in the Agreement.

### 8.2 Related-Party Claims

Any claims made against Provider or its Affiliates arising out of or related to this DPA may only be brought by the Customer entity that is a party to the Agreement.

### 8.3 Exceptions

This DPA does not limit any liability to an individual about the individual’s data protection rights under Applicable Data Protection Laws. In addition, this DPA does not limit any liability between the parties for violations of the EEA SCCs or UK Addendum.

## 9. Conflicts Between Documents

This DPA forms part of and supplements the Agreement. If there is any inconsistency between this DPA, the Agreement, or any of their parts, the part listed earlier will control over the part listed later for that inconsistency: (1) the EEA SCCs or the UK Addendum, (2) this DPA, and then (3) the Agreement.

## 10. Term of Agreement

This DPA will start when Provider and Customer agree to a Cover Page for the DPA and sign or electronically accept the Agreement and will continue until the Agreement expires or is terminated. However, Provider and Customer will each remain subject to the obligations in this DPA and Applicable Data Protection Laws until Customer stops transferring Customer Personal Data to Provider and Provider stops Processing Customer Personal Data.

## 11. Definitions

### 11.1 Applicable Laws

“Applicable Laws” means the laws, rules, regulations, court orders, and other binding requirements of a relevant government authority that apply to or govern a party.

### 11.2 Applicable Data Protection Laws

“Applicable Data Protection Laws” means the Applicable Laws that govern how the Service may process or use an individual’s personal information, personal data, personally identifiable information, or other similar term.

### 11.3 Controller

“Controller” will have the meaning(s) given in the Applicable Data Protection Laws for the company that determines the purpose and extent of Processing Personal Data.

### 11.4 Cover Page

“Cover Page” means a document that is signed or electronically accepted by the parties that incorporates these DPA Standard Terms and identifies Provider, Customer, and the subject matter and details of the data processing.

### 11.5 Customer Personal Data

“Customer Personal Data” means Personal Data that Customer uploads or provides to Provider as part of the Service and that is governed by this DPA.

### 11.6 DPA

“DPA” means these DPA Standard Terms, the Cover Page between Provider and Customer, and the policies and documents referenced in or attached to the Cover Page.

### 11.7 EEA SCCs

“EEA SCCs” means the standard contractual clauses annexed to the European Commission's Implementing Decision 2021/914 of 4 June 2021 on standard contractual clauses for the transfer of personal data to third countries pursuant to Regulation (EU) 2016/679 of the European Parliament and of the European Council.

### 11.8 European Economic Area (EEA)

“European Economic Area” or “EEA” means the member states of the European Union, Norway, Iceland, and Liechtenstein.

### 11.9 GDPR

“GDPR” means European Union Regulation 2016/679 as implemented by local law in the relevant EEA member nation.

### 11.10 Personal Data

“Personal Data” will have the meaning(s) given in the Applicable Data Protection Laws for personal information, personal data, or other similar term.

### 11.11 Processing

“Processing” or “Process” will have the meaning(s) given in the Applicable Data Protection Laws for any use of, or performance of a computer operation on, Personal Data, including by automatic methods.

### 11.12 Processor

“Processor” will have the meaning(s) given in the Applicable Data Protection Laws for the company that Processes Personal Data on behalf of the Controller.

### 11.13 Report

“Report” means audit reports prepared by another company according to the standards defined in the Security Policy on behalf of Provider.

### 11.14 Restricted Transfer

“Restricted Transfer” means (a) where the GDPR applies, a transfer of personal data from the EEA to a country outside of the EEA which is not subject to an adequacy determination by the European Commission; and (b) where the UK GDPR applies, a transfer of personal data from the United Kingdom to any other country which is not subject to adequacy regulations adopted pursuant to Section 17A of the United Kingdom Data Protection Act 2018.

### 11.15 Security Incident

“Security Incident” means a Personal Data Breach as defined in Article 4 of the GDPR.

### 11.16 Service

“Service” means the product and/or services described in the Agreement.

### 11.17 Special Category Data

"Special Category Data” will have the meaning given in Article 9 of the GDPR.

### 11.18 Subprocessor

“Subprocessor” will have the meaning(s) given in the Applicable Data Protection Laws for a company that, with the approval and acceptance of Controller, assists the Processor in Processing Personal Data on behalf of the Controller.

### 11.19 UK GDPR

“UK GDPR” means European Union Regulation 2016/679 as implemented by section 3 of the United Kingdom’s European Union (Withdrawal) Act of 2018 in the United Kingdom.

### 11.20 UK Addendum

“UK Addendum” means the international data transfer addendum to the EEA SCCs issued by the Information Commissioner for Parties making Restricted Transfers under S119A(1) Data Protection Act 2018.


# Self-host Deepseek R1
Source: https://www.thundercompute.com/docs/guides/deepseek-r1-running-locally-on-thunder-compute

5-minute guide. Run Deepseek R1 on your hardware.

# Easily Run DeepSeek R1 on Thunder Compute

Looking for the **cheapest way to run DeepSeek R1** or just want to **try DeepSeek R1** without buying hardware? Thunder Compute lets you spin up pay‑per‑minute A100 GPUs so you only pay for the time you use. Follow the steps below to get the model running in minutes.

> **Quick reminder:** Make sure your Thunder Compute account is set up. If not, start with our [Quickstart Guide](/vscode/quickstart).

If you prefer video instructions, watch this overview:

<iframe title="YouTube video player" />

## Step 1: Create a Cost‑Effective GPU Instance

Open your CLI and launch an 80 GB A100 GPU (perfect for the 70B variant):

```bash theme={null}
tnr create --gpu "a100xl" --template "ollama"
```

For details on instance templates, see our [templates guide](/guides/using-instance-templates).

## Step 2: Check Status and Connect

Verify the instance is running:

```bash theme={null}
tnr status
```

<img alt="Instance creation in CLI" />

Connect with its ID:

```bash theme={null}
tnr connect <instance-id>
```

## Step 3: Start the Ollama Server

Inside the instance, start Ollama:

```bash theme={null}
start-ollama
```

If you run into issues, check our [troubleshooting guide](/troubleshooting).

Wait about 30 seconds for the web UI to load.

<img alt="Ollama server startup" />

## Step 4: Access the Web UI and Load DeepSeek R1

1. Visit `http://localhost:8080` in your browser.
2. Choose **DeepSeek R1** from the dropdown. On an 80 GB A100, pick the **70B** variant for peak performance.

<img alt="Web UI with model selection" />

## Step 5: Run DeepSeek R1

Type a prompt in the web interface. For example:

> *"If the concepts of rCUDA were applied at scale, overcoming latency, what would it mean for the cost of GPUs on cloud providers?"*

The model will think through the answer and respond. A full reply can take up to 200 seconds.

<img alt="Model response in progress" />

## Conclusion

That's the **cheapest way to run DeepSeek R1** and a quick way to **try DeepSeek R1** on Thunder Compute. Explore more guides:

* [Using Docker on Thunder Compute](/guides/using-docker-on-thundercompute)
* [Using Instance Templates](/guides/using-instance-templates)
* [Running Jupyter notebooks](/guides/running-jupyter-notebooks-on-thunder-compute)

Happy building!


# Run GPT‑OSS 120B on Thunder Compute
Source: https://www.thundercompute.com/docs/guides/gpt-oss-running-locally-on-thunder-compute

A guide to setting up and running GPT‑OSS 120B affordably on Thunder Compute.

# Run GPT‑OSS 120B on Thunder Compute

Looking for the **cheapest way to self‑host GPT‑OSS 120B** or just want to **try it out** without buying hardware? Thunder Compute lets you spin up pay‑per‑minute NVIDIA A100 GPUs, so you only pay for what you use. Follow the steps below to get the model running in minutes.

> **Prerequisite:** Ensure your Thunder Compute account is ready. If not, start with our [Quickstart Guide](/vscode/quickstart).

## Step 1 — Create a Cost‑Effective Prototyping‑Mode GPU Instance

Launch an 80 GB A100 instance (large enough to host the full 120 B model):

```bash theme={null}
tnr create \
  --gpu a100xl \
  --vcpus 4 \
  --mode prototyping \
  --disk-size-gb 200 \
  --template "ollama"
```

This command starts a lower‑cost [prototyping‑mode](/prototyping-vs-production#prototyping-mode) instance with:

* **GPU:** A100 80 GB
* **vCPUs:** 4
* **Storage:** 200 GB (from the *Ollama* template)

> The GPU, vCPU Count, and Mode ([Prototyping](/prototyping-vs-production#prototyping-mode) / [Production](/prototyping-vs-production#production-mode)), can be changed later if your requirements change, and the amount of storage can be increased if needed.

For details on templates, see the [Instance Templates guide](/guides/using-instance-templates).

## Step 2 — Check Status and Connect

Verify that the instance is running, it can take a minute to spin up:

```bash theme={null}
tnr status
```

<img alt="Instance status output" />

Connect to the instance:

```bash theme={null}
tnr connect <instance‑id>
```

## Step 3 — Start Ollama and Download the Model

Inside the instance, start Ollama (this also launches OpenWebUI and a Cloudflare tunnel):

```bash theme={null}
start-ollama
```

While the UI is initializing, download the model, here we are downloading the 120B variant of GPT‑OSS, but any models can be downloaded from the [Ollama Model Library](https://ollama.com/library):

```bash theme={null}
ollama pull gpt-oss:120b
```

> **Tip:** If you encounter issues, consult the [troubleshooting guide](/troubleshooting).

Give the UI about 60 seconds to finish loading.

<img alt="Ollama status output" />

## Step 4 — Access the Web UI and Select the Model

1. Open `http://localhost:8080` in your browser.
2. Choose **gpt-oss:120b** from the model dropdown.

<img alt="OpenWebUI model selection" />

## Step 5 — Run GPT‑OSS 120B

Enter a prompt in the web interface, for example:

> *“Tell a tale of a seaman who found the treasure of the clouds by following the sound of thunder.”*

## Conclusion

That's it—the **cheapest way to run GPT‑OSS 120B** on Thunder Compute. For more, check out:

* [Using Docker on Thunder Compute](/guides/using-docker-on-thundercompute)
* [Using Instance Templates](/guides/using-instance-templates)
* [Running Jupyter Notebooks](/guides/running-jupyter-notebooks-on-thunder-compute)

Happy building!


# Install MCP Server
Source: https://www.thundercompute.com/docs/guides/mcp-server-for-managing-gpus

Install the Mintlify MCP server to host Thunder Compute docs locally. Enables AI tools like Cursor to provide instant answers based on documentation.

## TL;DR

```
# 1 – install the docs bundle
npx @mintlify/mcp@latest add thundercompute

# 2 – start the server
node ~/.mcp/thundercompute/src/index.js
```

Your **Thunder Compute MCP** server is now live at [**http://localhost:5001**](http://localhost:5001) and ready for any AI client.

## Connect in Cursor

1. Open **Cursor → Settings → Docs**.
2. **Add Source** → `http://localhost:5001`.
3. Ask something like *"How do I submit a batch to Thunder Compute?"*.

## Update docs

Run the install command again whenever you need the latest release:

```
npx @mintlify/mcp@latest add thundercompute
```


# Thunder Compute Referral Program
Source: https://www.thundercompute.com/docs/guides/referral-program

Earn credits by referring friends to Thunder Compute. Get 3% of every dollar your referrals spend on GPU instances with our lifetime rewards program.

**Refer a friend, earn credit.** Share your unique referral link and receive credits every time someone you refer spends on Thunder Compute GPUs.

<Note>
  This program is currently in beta. Terms may evolve as we improve the program based on user feedback.
</Note>

## How It Works

Our referral program rewards you with **3% of every dollar** your referrals spend on GPU instances. Here's what you need to know:

* **Reward Rate:** 3% of all spending by referred users
* **Duration:** Lifetime rewards for each referred customer
* **Credits:** Paid out in Thunder Compute credits (non-transferable)
* **Tracking:** Credits apply to paid, consumed compute resources. These typically post within minutes of a finalized invoice for consumed compute.

We created this program as a way to give back to our community. Rather than paying advertisers, we want to reward you for your contribution to Thunder Compute.

By referring even a medium-size startup you can often receive thousands of dollars of free compute.

## Getting Started

### 1. Find Your Referral Link

1. Sign in to the [Thunder Compute Console](https://console.thundercompute.com/)
2. Navigate to **Settings › General**
3. Copy your unique referral link
4. Share it anywhere—social media, tutorials, blog posts, or direct messages

### 2. Share and Earn

Once someone creates a new account using your link and starts using GPU instances, you'll automatically earn 3% of their payments as credits.

## Eligibility Requirements

### For Referrers

* Active Thunder Compute account in good standing
* No restrictions on sharing methods or platforms

### For Referrals

* Must create a **new account** via your referral link
* Existing accounts that sign up through referral links are not eligible
* Self-referrals and duplicate accounts are prohibited

<Warning>
  Credits are non-transferable and cannot be converted to cash. They can only be used for Thunder Compute services.
</Warning>

## Program Rules

### Fair Use Policy

We maintain strict anti-fraud measures to ensure program integrity:

* Creating fake accounts is prohibited
* Self-referrals will result in credit removal
* Violating Thunder Compute's Terms & Conditions may lead to account suspension
* All referral activity is monitored for suspicious patterns

### Program Changes

Thunder Compute reserves the right to:

* Modify reward rates or eligibility requirements
* Update program terms with advance notice
* Discontinue the program if necessary

We'll announce any changes through email notifications and documentation updates.

## Frequently Asked Questions

**Q: When do I receive my referral credits?**
A: Credits are typically added to your account within minutes of your referral's successful invoice.

**Q: Is there a limit to how much I can earn?**
A: No, there's no cap on referral earnings. The more successful referrals you make, the more you earn.

**Q: Can I refer existing Thunder Compute users?**
A: No, only new users who create accounts through your referral link are eligible.

**Q: What counts as a qualifying payment?**
A: Only direct card payments for GPU instances qualify for referral rewards. Usage on free or referral credits do not qualify.

## Need Help?

Have questions about referral eligibility, credit posting, or the program in general? Contact our support team:

* **Discord:** Join our [community server](https://discord.com/invite/nwuETS9jJK)

Thank you for giving back to the Thunder Compute community!


# Jupyter Notebooks
Source: https://www.thundercompute.com/docs/guides/running-jupyter-notebooks-on-thunder-compute

Launch notebooks on cloud GPUs. Develop locally.

## Prerequisites for a Jupyter Notebook with Cloud GPU

* VSCode installed
* Thunder Compute extension installed in VSCode, Cursor, or Windsurf
* Jupyter Notebook extension installed in VSCode, Cursor, or Windsurf

## Steps to Launch Your Notebook

### 1. Connect to a Thunder Compute cloud GPU in VSCode

Follow the instructions in our [quickstart](/vscode/quickstart) guide to set and connect to a remote instance in VSCode.

### 2. Install the Jupyter extension in your cloud workspace

Open the Extensions panel and install the Jupyter extension inside your Thunder Compute instance.

### 3. Verify GPU availability inside the notebook

Create a Jupyter Notebook, which is now connected to a Thunder Compute instance with GPU capabilities. To confirm that the GPU is accessible, run the following in a notebook cell:

```
import torch
print(torch.cuda.is_available())
```

If everything is set up correctly, the output should be:

```
True
```

You now have a Jupyter Notebook running on a Thunder Compute cloud GPU, a fast and low-cost alternative to Colab for indie developers, researchers, and data scientists.


# Speeding Up Snapshots
Source: https://www.thundercompute.com/docs/guides/speeding-up-snapshots

Optimizing snapshot creation and restoration.

The size of your instance's disk directly affects how long snapshots take to create and restore.

This guide focuses on simple, high-impact steps to reduce snapshot size and speed up restores. We’ll expand this guide as more snapshot features ship.

## Quick Wins

1. **Keep your instance disk lean**: Remove large, transient files before snapshotting.
2. **Exclude non-essential data**: Use `.thunderignore` to skip caches, build outputs, and generated assets.

## .thunderignore Files for Exclusion

Often, you may want to exclude certain heavy files, cache directories, or generated files from a snapshot. You can do this using a `.thunderignore` file. This will help speed up snapshot creation and restoration.

1. Create a `.thunderignore` file in the `/` directory of your instance.
2. Add all paths you would like to ignore (absolute paths or relative to `/`). Patterns are supported - the syntax for these is the same as [`filepath.Match`](https://pkg.go.dev/path/filepath#Match) in Go. Patterns are matched against paths, not just basenames, so use `/` to anchor from the root (for example, `/data/*.parquet`). `*` and `?` are supported; `**` is not special and is treated literally. Blank lines are ignored, and lines starting with `#` are treated as comments.
3. Create your snapshot. The `.thunderignore` file is included in the snapshot so your exclusions persist on restore.

<Tip>
  Start by excluding caches, build outputs, and temporary files. You’ll usually see the biggest size reductions there.
</Tip>

<Note>
  Make sure you don’t exclude anything required to run your workloads after restore, such as model weights or datasets you actually need.
</Note>

Example `.thunderignore`:

```
# Caches and build artifacts
.cache/*
*.tmp

# Large data
/data/*.parquet
/models/*.pt

# Common language build outputs
/node_modules/*
/dist/*
/target/*
```


# Stopping Instances
Source: https://www.thundercompute.com/docs/guides/stopping-instances

Pause your work and save costs using the snapshot workaround.

## The Workflow

Thunder Compute does not have a native "Stop" feature for instances. Fortunately, you can achieve the same result by using snapshots.

To "stop" an instance, follow these three steps:

1. **Create a snapshot:** This saves the current state of the running instance.

2. **Delete the instance:** Once snapshot creation is underway, you can safely delete the running instance.

3. **Restore the snapshot:** Create a new instance by using your saved Snapshot as the template.

### 1. Create a Snapshot

First, capture the current state of your running instance. You can trigger this through any of our supported interfaces:

**Guides:** [VS Code](https://www.thundercompute.com/docs/vscode/operations/snapshots#create-a-snapshot) | [CLI](https://www.thundercompute.com/docs/cli/operations/snapshots#create-a-snapshot) | [Console](https://www.thundercompute.com/docs/console/operations/snapshots#create-a-snapshot)

### 2. Delete the Running Instance

Once the snapshot is initiated, delete the instance.

**Guides:** [VS Code](/vscode/operations/deleting-instances#delete-an-instance) | [CLI](/cli/operations/deleting-instances#delete-an-instance) | [Console](/console/operations/deleting-instances#delete-an-instance)

<Tip>
  You can delete your instance immediately after triggering the snapshot.
</Tip>

### 3. Restore from Snapshot

When you are ready to resume, create a new instance using your snapshot as the base.

**Guides:** [VS Code](/vscode/operations/snapshots#restore-from-a-snapshot) | [CLI](/cli/operations/snapshots#restore-from-a-snapshot) | [Console](/console/operations/snapshots#restore-from-a-snapshot)

***

## Important Notes

<Warning>
  The time required to create and restore snapshots varies based on the size of the snapshot.
</Warning>

* **Cost Efficiency:** You only pay for the snapshot storage while the instance is deleted; significantly cheaper than keeping an instance running.


# Using Docker
Source: https://www.thundercompute.com/docs/guides/using-docker-on-thundercompute

Experimental Docker support on Thunder Compute.

## Disclaimer: Docker support is experimental

Docker has experimental support inside Thunder Compute instances. Because Thunder Compute instances
are themselves containers, running Docker on Thunder Compute is like running Docker inside of
Docker. To get this to work, our instances come with a modified version of `dockerd`, and there are
certain situations when it might not work exactly like the official Docker (eg, advanced
networking features).

# Installing and running Docker

1. `apt update`
2. `apt install docker.io`
3. Start `dockerd` in the background: `nohup dockerd &`
4. Start your container with the `--device nvidia.com/gpu=all` flag in order to expose GPUs. For example: `docker run -it --rm --device nvidia.com/gpu=all ubuntu:latest`.

   Some tutorials will tell you to use `--runtime=nvidia` or `--gpus=all`. These are outdated options and are not supported in Thunder Compute. `--device nvidia.com/gpu=all` is the only supported way to add a GPU to a docker container.

# Known issues

* Docker Compose does not work.
* The container network is not isolated. This means that even ports you don't list with `-p` will be available, and could potentially conflict with other processes or containers.
* Sometimes when the container is destroyed, the processes in it will not be properly killed. This can cause e.g. port conflicts if you then try to start the same container again. You can use standard tools like `ps aux` and `kill` to find and stop any remaining container processes.

If you run into issues, please [contact us](https://www.thundercompute.com/contact/).


# Use Instance Templates for AI
Source: https://www.thundercompute.com/docs/guides/using-instance-templates

Quickly deploy LLMs (Ollama) and AI image generators (ComfyUI) on Thunder Compute using pre-configured instance templates. Get started fast.

Thunder Compute gives indie developers, researchers and data scientists instant access to **affordable cloud GPUs**. Our pre-configured **instance templates** set up popular AI stacks automatically, so you can **run LLMs** or **generate AI images** in minutes.

## AI Templates on Cheap Cloud GPUs

We currently offer:

* **Ollama** – launches an Ollama server for open-source large language models
* **ComfyUI** – installs ComfyUI for fast AI-image generation workflows

## Deploy a Template

1. **Create an instance**

```bash theme={null}
# Launch an Ollama instance
tnr create --template ollama

# Launch ComfyUI
tnr create --template comfy-ui
```

2. **Connect to the instance**

```bash theme={null}
tnr connect 0   # replace 0 with your instance ID
```

<Note>
  Port forwarding is handled automatically when you connect. The `-t` flag is unnecessary.
</Note>

3. **Start the service**

```bash theme={null}
# Ollama
start-ollama

# ComfyUI
start-comfyui
```

Required ports forward to your local machine automatically.

## Template Details

### Ollama Template

* Forwards port **11434**
* Access the API at `http://localhost:11434`
* Ready for popular Ollama models

### ComfyUI Template

* Forwards port **8188**
* Mounts the `ComfyUI` directory to your Mac or Linux host
* UI at `http://localhost:8188`
* Includes common nodes and extensions

## Need Help?

Encounter problems or have questions? Reach out to our support team any time.


# Weights & Biases
Source: https://www.thundercompute.com/docs/guides/weights-and-biases

Track, debug, and optimize GPU-heavy workloads on Thunder Compute instances using Weights & Biases (wandb).

Weights & Biases (wandb) is an experiment tracking and model management platform that’s particularly useful when training large models on Cloud GPUs. It helps you:

* Track training runs, hyperparameters, and metrics
* Monitor GPU/CPU utilization in real time
* Version datasets and model checkpoints
* Run large-scale hyperparameter sweeps across many GPU instances

On Thunder Compute, wandb helps you monitor GPU utilization, identify bottlenecks, and track training metrics.

***

## Prerequisites

* A Thunder Compute GPU instance created and connected
* Python environment set up on your instance
* A Weights & Biases account ([https://wandb.ai/site](https://wandb.ai/site))

***

## Installation

Install wandb on your Thunder Compute instance:

```bash theme={null}
pip install wandb
```

Or add to a `requirements.txt`:

```bash theme={null}
echo "wandb" >> requirements.txt
pip install -r requirements.txt
```

***

## Authentication

Authenticate with:

```bash theme={null}
wandb login
```

Or via environment variable:

```bash theme={null}
export WANDB_API_KEY="your_api_key"
wandb login --relogin
```

You will see the following below:

```
wandb: Logging into wandb.ai. (Learn how to deploy a W&B server locally: https://wandb.me/wandb-server)
wandb: You can find your API key in your browser here: https://wandb.ai/authorize?ref=models
wandb: Paste an API key from your profile and hit enter, or press ctrl+c to quit:
```

Enter your API key which can be found on the homepage of wandb.ai after you create an account, once entered you will see:

```
wandb: No netrc file found, creating one.
wandb: Appending key for api.wandb.ai to your netrc file: /home/ubuntu/.netrc
wandb: Currently logged in as: username (entity-name) to https://api.wandb.ai. Use `wandb login --relogin` to force relogin
```

<Note>
  For shared or production Thunder instances, environment variables or secret
  managers are preferred over pasting API keys directly.
</Note>

***

## Getting Started

Follow these steps to run your first wandb experiment on your Thunder Compute instance.

### Step 1 — Create a Training File

Create a new Python file on your instance:

```bash theme={null}
nano train.py
```

Or create a new file within your IDE connected over SSH.

### Step 2 — Paste Minimal Working Example

Copy this minimal example into your `train.py` file:

```python theme={null}
import wandb
import time

# Initialize wandb
wandb.init(
    project="thunder-resnet",
    name="quick-test",
    config={
        "learning_rate": 0.001,
        "batch_size": 32,
        "epochs": 5,
    },
)

# Simple training loop simulation
for epoch in range(5):
    # Simulate training metrics
    train_loss = 1.0 / (epoch + 1)
    train_acc = 0.5 + epoch * 0.1

    # Log metrics to wandb
    wandb.log({
        "epoch": epoch,
        "train/loss": train_loss,
        "train/accuracy": train_acc,
    })

    time.sleep(0.5)  # Simulate work

wandb.finish()
```

### Step 3 — Run the Script

Execute your training script:

```bash theme={null}
python train.py
```

### Step 4 — Expected Output

You should see output similar to:

```
wandb: Currently logged in as: your-username (entity-name) to https://api.wandb.ai. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.23.0
wandb: Run data is saved locally in /home/ubuntu/wandb/run-20251120_135726-abcd
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run quick-test
wandb: ⭐️ View project at https://wandb.ai/entity-name/thunder-resnet
wandb: 🚀 View run at https://wandb.ai/entity-name/thunder-resnet/runs/abcd
wandb:
wandb: Run history:
wandb:          epoch ▁▃▅▆█
wandb: train/accuracy ▁▃▅▆█
wandb:     train/loss █▄▂▁▁
wandb:
wandb: Run summary:
wandb:          epoch 4
wandb: train/accuracy 0.9
wandb:     train/loss 0.2
wandb:
wandb: 🚀 View run quick-test at: https://wandb.ai/entity-name/thunder-resnet/runs/abcd
wandb: ⭐️ View project at: https://wandb.ai/entity-name/thunder-resnet
wandb: Synced 4 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20251120_135726-abcd/logs
```

### Step 5 — View Your Results

1. **View your dashboard**: Click the link in the output or visit [https://wandb.ai](https://wandb.ai) and navigate to your project
2. **View in Table view**: Go to **(Project Name)** > **Projects** > **thunder-resnet** > **Table** to see all your runs in a tabular format
3. **Compare runs**: Run the script multiple times with different configurations to compare results
4. **Add artifacts**: See the [Model Checkpointing with Weights & Biases Artifacts](#model-checkpointing-with-weights--biases-artifacts) section to version checkpoints and datasets
5. **Scale to multi-GPU**: Check out [Distributed Training](#distributed-training-ddp-lightning-deepspeed) for multi-GPU setups
6. **Run sweeps**: Use [Hyperparameter Sweeps](#hyperparameter-sweeps-multi‑gpu-multi‑instance) for automated hyperparameter search

***

## Viewing Results

1. Visit [https://wandb.ai/site](https://wandb.ai/site)
2. Select your project
3. Explore:
   * Metrics charts
   * GPU utilization
   * Model checkpoints
   * Dataset artifacts
   * Sweep dashboards

***

## Core Concepts for Cloud GPU Workloads

When using remote GPUs, these wandb features matter most:

1. **Run tracking** — metrics, hyperparameters, logs
2. **GPU/system monitoring** — GPU utilization, power, memory, CPU load
3. **Artifacts** — versioned checkpoints and datasets
4. **Sweeps** — distributed hyperparameter search
5. **Groups & jobs** — organize multi-GPU/distributed training

***

## Basic Usage

### Initialize a Run

```python theme={null}
import wandb

wandb.init(
    project="my-thunder-project",
    name="baseline-resnet50",
    config={
        "learning_rate": 3e-4,
        "batch_size": 64,
        "epochs": 20,
        "optimizer": "adamw",
        "precision": "fp16",
    },
)
```

### Log Metrics

```python theme={null}
wandb.log({
    "train/loss": loss,
    "train/accuracy": acc,
    "step": step,
})
```

### Best Logging Practices

* Log every **N steps** (e.g., 10–50) to minimize overhead
* Avoid logging huge tensors every step
* Use artifacts for large files

***

## GPU & System Monitoring

Wandb automatically collects:

* GPU utilization
* GPU memory usage
* GPU temperature and power
* CPU usage
* RAM usage
* Disk and network I/O

Use these graphs to diagnose:

* **GPU-bound** workloads
* **Data-bound** workloads
* **Bottlenecks** due to I/O or preprocessing
* **Too-small batch sizes**

### Improving GPU Utilization

* Increase batch size until GPU memory is near capacity
* Use **mixed precision** (`torch.cuda.amp`)
* Increase dataloader workers
* Preload/augment data on the GPU
* Reduce unnecessary synchronizations

***

## Model Checkpointing with Weights & Biases Artifacts

When you train on Thunder Compute GPU instances, it's important that your model checkpoints are **not** tied to a single machine. Weights & Biases Artifacts provide a simple way to:

* Persist checkpoints even if the instance is deleted
* Move checkpoints between different Thunder instances (or GPU types)
* Share models with your team
* Reproduce and resume long-running training jobs

This section provides a walkthrough of how to do checkpointing with wandb.

***

### Why use Artifacts for checkpoints?

Saving checkpoints only to the local filesystem is risky:

* Thunder instances may be stopped or recreated
* You may want to resume training on a *different* GPU (A100 → H100)
* Your team may need to reuse your model
* You may want versioned, reproducible training history

Artifacts solve this by storing checkpoints in W\&B's managed, versioned storage.

***

### Step 1 — Save a checkpoint locally during training

Inside your real training loop, periodically save a checkpoint.\
For real projects (PyTorch):

```python theme={null}
import torch

# ... inside your training loop ...
if (epoch + 1) % 5 == 0:
    ckpt_path = f"checkpoints/model_epoch_{epoch+1}.pt"
    torch.save(model.state_dict(), ckpt_path)
```

> It is best practice to save checkpoints inside a dedicated `checkpoints/` folder.

***

### Step 2 — Log the checkpoint as a W\&B Artifact

Right after saving your file:

```python theme={null}
import wandb

artifact = wandb.Artifact(
    name=f"resnet50-epoch-{epoch+1}",
    type="model",
    metadata={
        "epoch": epoch + 1,
        "val_loss": float(val_loss),
        "val_accuracy": float(val_acc),
    },
)

artifact.add_file(ckpt_path)
wandb.log_artifact(artifact)
```

This uploads your checkpoint to W\&B and keeps a permanent copy.

***

### Step 3 — View & manage checkpoints in the W\&B UI

1. Go to your wandb project
2. Open the **Artifacts** tab
3. Click your model artifact
4. You can now:
   * View version history (v0, v1, v2…)
   * Open the metrics/metadata
   * Download the checkpoint
   * Use it as an input for new runs

***

### Step 4 — Restore a checkpoint on another Thunder instance

On a fresh machine:

```python theme={null}
import wandb
import torch

run = wandb.init(project="my-thunder-project", job_type="restore")

artifact = run.use_artifact(
    "wato/my-thunder-project/resnet50-epoch-10:latest",
    type="model",
)
artifact_dir = artifact.download()

checkpoint = torch.load(f"{artifact_dir}/model_epoch_10.pt", map_location="cuda")
model.load_state_dict(checkpoint)
model.to("cuda")
```

You now have the exact model weights from your previous run — even if the original instance is gone.

***

### Step 5 — Resume training

```python theme={null}
model.load_state_dict(checkpoint)
model.to("cuda")

optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)

start_epoch = 10
for epoch in range(start_epoch, config.epochs):
    train_one_epoch(...)
    validate(...)
    wandb.log({"epoch": epoch})
```

***

### Example: Adding Checkpointing to a Minimal `train.py`

Here is a working example using the simple training script from the Getting Started section.

This example simulates a checkpoint file (JSON), but the workflow is identical for real model weights.

```python theme={null}
import wandb
import time
import json
import os

# Initialize wandb
wandb.init(
    project="thunder-resnet",
    name="quick-test",
    config={
        "learning_rate": 0.001,
        "batch_size": 32,
        "epochs": 5,
    },
)

os.makedirs("checkpoints", exist_ok=True)

for epoch in range(5):
    # Simulate training metrics
    train_loss = 1.0 / (epoch + 1)
    train_acc = 0.5 + epoch * 0.1

    # Log metrics to wandb
    wandb.log({
        "epoch": epoch,
        "train/loss": train_loss,
        "train/accuracy": train_acc,
    })

    # ---- Checkpointing Example ----
    # In a real project this would be torch.save(model.state_dict(), ...)
    checkpoint_path = f"checkpoints/epoch_{epoch}.json"
    with open(checkpoint_path, "w") as f:
        json.dump({
            "epoch": epoch,
            "train_loss": train_loss,
            "train_accuracy": train_acc,
        }, f)

    # Log checkpoint as an artifact
    artifact = wandb.Artifact(
        name=f"quick-test-epoch-{epoch}",
        type="model",
        metadata={
            "epoch": epoch,
            "train_loss": train_loss,
            "train_accuracy": train_acc
        },
    )
    artifact.add_file(checkpoint_path)
    wandb.log_artifact(artifact)
    # --------------------------------

    time.sleep(0.5)

wandb.finish()
```

This example demonstrates:

* how checkpoint files are created
* how they are logged as Artifacts
* how each epoch becomes a tracked, versioned checkpoint

These appear in the **Artifacts** tab of your project.

***

### Quick Reference: Other Artifact Types

Artifacts aren't just for model checkpoints. You can also version datasets:

```python theme={null}
# Logging a Dataset
dataset = wandb.Artifact("imagenet-subset", type="dataset")
dataset.add_dir("data/imagenet_subset")
wandb.log_artifact(dataset)
```

***

## Hyperparameter Sweeps (Multi‑GPU, Multi‑Instance)

Sweeps allow large-scale hyperparameter search across many Thunder Compute instances.

### Step 1 — Create `sweep.yaml`

```yaml theme={null}
program: train.py
project: thunder-resnet
method: bayes

metric:
  name: val/accuracy
  goal: maximize

parameters:
  learning_rate:
    min: 0.00001
    max: 0.001
  batch_size:
    values: [32, 64, 128]
  weight_decay:
    min: 0.0
    max: 0.1
  augment:
    values: ["none", "light", "heavy"]
```

Output:

```
wandb: Creating sweep from: sweep.yaml
wandb: Creating sweep with ID: fgbkmk3q
wandb: View sweep at: https://wandb.ai/entity-name/thunder-resnet/sweeps/fgbkmk3q
wandb: Run sweep agent with: wandb agent entity-name/thunder-resnet/fgbkmk3q
```

### Step 2 — Initialize the sweep:

```bash theme={null}
wandb sweep sweep.yaml
```

### Step 3 — Run agents on Thunder GPU instances:

```bash theme={null}
wandb agent <entity>/<project>/<sweep_id>
```

Each agent pulls new hyperparameters and launches a run automatically.

***

## Distributed Training (DDP, Lightning, DeepSpeed)

### PyTorch DDP Example

```python theme={null}
wandb.init(
    project="thunder-ddp",
    group="llama7b-a100x4",
    job_type="training",
)
```

Set run names per rank:

```python theme={null}
wandb.run.name = f"gpu-{rank}"
```

### PyTorch Lightning Example

```python theme={null}
from lightning.pytorch import Trainer
from lightning.pytorch.loggers import WandbLogger

wandb_logger = WandbLogger(project="thunder-lightning-demo")

trainer = Trainer(
    logger=wandb_logger,
    accelerator="gpu",
    devices=4,
    strategy="ddp",
    max_epochs=50,
)

trainer.fit(model)
```

Lightning automatically:

* Logs metrics and gradients
* Tracks checkpoints
* Handles multi-GPU logging

***

## Offline Mode (Air‑Gapped or Firewalled Environments)

Thunder instances may have intermittent or restricted internet access.

### Run in offline mode:

```bash theme={null}
export WANDB_MODE=offline
python train.py
```

### Sync later:

```bash theme={null}
wandb sync /path/to/wandb/run-folder
```

### Fully disable wandb:

```bash theme={null}
export WANDB_MODE=disabled
```

***

## Best Practices for Thunder Compute GPU Instances

### Run Management

* Use meaningful run names that include dataset + model + GPU type
* Log all hyperparameters in `wandb.config`
* Track system metrics to diagnose bottlenecks
* Organize multi-GPU runs using `group`
* Reduce logging overhead by batching logs

### Artifacts & Checkpointing

* Use meaningful artifact names (e.g. `llama7b-a100-epoch20`)
* Attach useful metadata (epoch, val metrics, dataset version)
* Log fewer but higher-quality checkpoints
* Always use artifacts for long or expensive runs
* Use `use_artifact(...).download()` to restore weights anywhere
* Use artifacts for datasets and checkpoints

### Experimentation

* Use sweeps for expensive experiments
* Compare runs systematically using the dashboard
* Monitor GPU utilization to optimize batch sizes

***

## Troubleshooting

### Authentication Issues

```bash theme={null}
wandb login --relogin
```

### GPU Metrics Not Showing

* Ensure `nvidia-smi` works inside the environment
* Use GPU-enabled containers (`--gpus all`)
* Call `wandb.init()` early

### Connection Issues

* Verify outbound internet access
* Firewalls must allow connections to `*.wandb.ai`
* Use offline mode if required

### Large File Uploads

* Always use artifacts for multi-GB files
* Compress large checkpoints
* Prune old versions

***

## Need Help?

* W\&B Docs: [https://docs.wandb.ai](https://docs.wandb.ai)
* Thunder Compute Discord: [https://discord.com/invite/nwuETS9jJK](https://discord.com/invite/nwuETS9jJK)
* Email support: `support@thundercompute.com`


# Prototyping vs Production
Source: https://www.thundercompute.com/docs/prototyping-vs-production

Choose between optimized development pricing and full compatibility for your workloads

Thunder Compute offers two modes for running instances.

| Feature                   | Prototyping        | Production              |
| ------------------------- | ------------------ | ----------------------- |
| Cost                      | Lower              | Higher                  |
| Compatibility             | Most ML workloads  | Full CUDA compatibility |
| GPUs                      | A6000, A100, H100  | A100, H100              |
| Multi-GPU                 | H100: up to 2 GPUs | Up to 8 GPUs            |
| Graphics (OpenGL, Vulkan) | No                 | Yes                     |

## Prototyping Mode

<Note>
  Prototyping mode is currently in beta and exclusively available on Thunder Compute.
</Note>

Prototyping mode applies CUDA-level optimizations to maximize GPU utilization, significantly reducing costs for AI/ML development workflows.

### Supported Software

* **PyTorch**: Fully supported (downgrading from the pre-installed version may cause issues)
* **TensorFlow**
* **JAX**
* **Jupyter Notebooks**
* **Model Serving**: ComfyUI, Ollama, VLLM, and others
* **Fine Tuning**: Unsloth and others

### Unsupported Workloads

* Graphics workloads (OpenGL, Vulkan, FFMPEG)
* Custom CUDA kernels (may exhibit unpredictable behavior)
* Hardware-specific profiling tools

<Tip>
  If you encounter issues with an unsupported workload, switch to production mode with [modify](/vscode/operations/modifying-instances) for full compatibility.
</Tip>

## Production Mode

Production mode provisions a standard virtual machine with full CUDA compatibility and predictable performance.

### When to Choose Production

* Long-running training jobs
* Multi-GPU workloads (up to 8 GPUs)
* Graphics workloads (OpenGL, Vulkan, FFMPEG)
* Custom CUDA kernels
* Workloads requiring accurate hardware metrics

## Switching Between Modes

[Modify existing instances](/vscode/operations/modifying-instances) to switch between prototyping and production mode. This also lets you change GPU type, vCPUs, and RAM. Storage can be expanded but not reduced.

## Learn More

* [Technical Specifications](/technical-specs) - Hardware, networking, and storage details


# Restrictions
Source: https://www.thundercompute.com/docs/restrictions

Usage restrictions, geographic availability, and prohibited activities on Thunder Compute

## Prohibited Activities

### Cryptocurrency Mining

Mining, staking, or otherwise interacting with cryptocurrency is strictly prohibited on Thunder Compute. If cryptocurrency-related activity is detected:

* The associated account is immediately banned
* Any billing credit is revoked
* The account is billed for the full amount of usage

## Geographic Availability

### B2B Requirements

Thunder Compute is only available for B2B customers and requires a VAT ID (or similar) in the following countries:

* United Arab Emirates
* Angola
* Bahrain
* Brazil
* Switzerland
* Côte d’Ivoire (Ivory Coast)
* Colombia
* Algeria
* Georgia
* Iraq
* Jordan
* Kazakhstan
* South Korea (Republic of Korea)
* Kuwait
* Morocco
* North Macedonia
* Oman
* Paraguay
* Qatar
* Saudi Arabia
* Tunisia
* Turkey (Türkiye)
* Tanzania
* Ukraine
* Uganda
* Uzbekistan
* Yemen
* India
* Moldova (Republic of Moldova)

### Restricted Countries

Thunder Compute is not currently available in the following countries:

* Belarus
* China
* Cuba
* Indonesia
* Iran
* Kenya
* North Korea
* Malaysia
* Mexico
* Nigeria
* Russia
* Sudan
* Syria
* Uruguay

If you're located in one of these countries and need access to Thunder Compute, please contact us to discuss potential alternatives.

## Usage Guidelines

### Acceptable Use

Thunder Compute instances are intended for legitimate computational workloads, particularly:

* AI/ML development and training
* Scientific computing
* Data processing and analysis
* Software development and testing

We have a strict one-account-per-user policy.

### Resource Usage

Users must comply with fair use policies and avoid activities that:

* Violate terms of service
* Engage in illegal or unethical activities

## Support

If you have questions about restrictions or need clarification on acceptable use, contact our support team.


# Technical Specifications
Source: https://www.thundercompute.com/docs/technical-specs

Hardware specifications, networking details, and pre-installed software for Thunder Compute instances

## Instance Infrastructure

### Hardware Specifications

* **GPU Options**:
  * A6000 48GB (Prototyping only)
  * A100 80GB (Both modes)
  * H100 80GB (Both modes)
* **Memory**: 18 vCPUs and 90GB RAM per GPU (Production mode, Prototyping is fully customizable)
* **Location**: Canada (Quebec)

### Pre-installed Software

* **CUDA**: Version 13.0
* **CUDA Driver**: Version 580
* **PyTorch**: Version 2.9.0+cu128
* **JupyterLab**: Pre-installed
* Additional scientific Python libraries (NumPy, Pandas, etc.)

<Warning>
  Do not attempt to reinstall CUDA. If compatibility issues arise, upgrade your other dependencies (e.g., PyTorch) rather than downgrading CUDA.
</Warning>

## Networking

* **Egress/Ingress**: 7 Gbps
* **IP Address**: Dynamic

### Port Access

* **Public URLs (CLI)**: Use `tnr ports forward` to expose HTTP services at `https://<uuid>-<port>.thundercompute.net` with automatic HTTPS and DDoS protection. See [Port Forwarding](/cli/operations/port-forwarding) for details.
* **Local tunneling (CLI)**: Use `tnr connect <instance_id> -t <port>` to tunnel ports to your local machine
* **VS Code**: Use the built-in [port forwarding](https://code.visualstudio.com/docs/debugtest/port-forwarding) feature


# Troubleshooting
Source: https://www.thundercompute.com/docs/troubleshooting

Troubleshoot common Thunder Compute errors. Find solutions for connection issues, function errors, SSH problems, and access logs. Get support via Discord.

## Common solutions

1. Reconnect to the instance with `ctrl + d` and `tnr connect <instance_id>`
2. Upgrade tnr. Depending on your install method, you may have to use `pip install tnr --upgrade` or re-download the binary from the website
3. Back up any important data, then delete and recreate the instance.

## Common errors

### Function not implemented

A common error you may encounter is some variant of "This function is not implemented." What this means is that your program touches a portion of the CUDA API that we do not currently support. Check our [Prototyping vs Production](/prototyping-vs-production) guide for supported features, and if you encounter this, please contact us.

### SSH errors

If you encounter SSH-related errors (like `Error reading SSH protocol banner` or permission issues), first retry the command.

For quick fixes, back up critical data and recreate the instance. Instances cannot be stopped or restarted.

For persistent SSH issues, see our [SSH on Thunder Compute guide](/cli/operations/ssh) for alternative connection methods.

## Recommended Guides

To help prevent common issues and get the most out of Thunder Compute, we recommend these guides:

* [Using Docker](/guides/using-docker-on-thundercompute) - Learn about GPU-enabled containers and troubleshooting Docker issues
* [Using Instance Templates](/guides/using-instance-templates) - Use pre-configured environments to minimize setup issues

## Production mode as a last resort

If you continue to experience compatibility issues or errors that cannot be resolved through the above methods, consider switching to production mode by [modifying your existing instance](/vscode/operations/modifying-instances). Production mode provides maximum stability and reliability with all low-level optimizations disabled, ensuring complete compatibility for workloads that encounter persistent issues in the prototyping tier.

## Support

The fastest way to get support is to join [our discord](https://discord.com/invite/nwuETS9jJK). Our founding team will personally respond to help you as quickly as possible.


# Authentication
Source: https://www.thundercompute.com/docs/vscode/operations/authentication

Log in to Thunder Compute and manage your API tokens

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/authentication">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/authentication">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/authentication">
    Web interface
  </QuickstartCard>
</Columns>

## Log In

The extension may prompt you to log in automatically when you first install it.

If not, open the command palette with `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) and run:

```
Thunder Compute: Login
```

Your browser will open automatically to complete authentication via OAuth.

## Log Out

Open the command palette and run:

```
Thunder Compute: Logout
```

## Managing API Tokens

API tokens authenticate your CLI and extension access. You can manage them in the [console](https://console.thundercompute.com/settings?tab=tokens).

* **Generate tokens**: Create new tokens for each device or use case
* **Revoke tokens**: Remove access for specific tokens without affecting others
* **Token persistence**: Tokens never expire unless manually revoked

<Note>
  Use unique tokens for each device so you can revoke access individually if needed.
</Note>

## Adding a Payment Method

Before creating instances, you need a payment method on file. Visit the [billing settings](https://console.thundercompute.com/settings/billing) to add a credit card.


# Connecting to Instances
Source: https://www.thundercompute.com/docs/vscode/operations/connecting-to-instances

SSH into your Thunder Compute instances

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/connecting-to-instances">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/connecting-to-instances">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/connecting-to-instances">
    Web interface
  </QuickstartCard>
</Columns>

## Connect to an Instance

1. Open the Thunder Compute sidebar panel
2. Find your running instance in the list
3. Click the **Connect** button (the icon with two arrows pointing toward each other)

A new VSCode window opens connected to your instance. You can browse files, edit code, and run terminals as if working locally.

<Note>
  If connecting fails, make sure you have the [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension installed.
</Note>

## Exposing Services

To expose web servers, Jupyter notebooks, or other services running on your instance, use a [Cloudflare Tunnel](/technical-specs#port-access).

## Using Standard SSH

If you prefer using your own SSH client, Thunder Compute is compatible with standard SSH tools.

Need to manage saved keys or copy a raw SSH command? See [SSH on Thunder Compute](/vscode/operations/ssh) for the manual workflow.


# Creating Instances
Source: https://www.thundercompute.com/docs/vscode/operations/creating-instances

Launch new Thunder Compute instances with your preferred configuration

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/creating-instances">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/creating-instances">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/creating-instances">
    Web interface
  </QuickstartCard>
</Columns>

## Create an Instance

1. Open the Thunder Compute sidebar panel
2. Click the **Create Instance** button (or the `+` icon)
3. A configuration window will open—select your options from the dropdown menus
4. Click **Create**

## Configuration Options

The extension provides the same options as the CLI:

* **Mode**: Prototyping or Production
* **GPU Type**: A6000, A100, H100 (availability depends on mode)
* **GPU Count**: 1 GPU for most prototyping GPUs; H100 prototyping supports 1-2 GPUs. Production supports 1-8.
* **vCPUs**: Options vary by GPU type and count (prototyping only)
* **Disk Size**: 100GB to 400GB (prototyping) or 1000GB (production)
* **Template**: Base, Ollama, ComfyUI, and more

## Mode Selection

Choose between optimized development pricing or full compatibility:

* **Prototyping** (default): Lower cost with CUDA-level optimizations. Best for development.
* **Production**: Standard VM with full compatibility. Best for long-running jobs and production workloads.

See [Prototyping vs Production](/prototyping-vs-production) for details on each mode.

## GPU Options

| GPU   | VRAM | Availability     |
| ----- | ---- | ---------------- |
| A6000 | 48GB | Prototyping only |
| A100  | 80GB | Both modes       |
| H100  | 80GB | Both modes       |

## Templates

Templates pre-configure your instance for common AI workflows:

| Template   | Description                     |
| ---------- | ------------------------------- |
| `base`     | Ubuntu with PyTorch + CUDA      |
| `ollama`   | Ollama server environment       |
| `comfy-ui` | ComfyUI for AI image generation |

See [Using Instance Templates](/guides/using-instance-templates) for more details.

## Restore from Snapshot

When creating a new instance, select your snapshot from the template dropdown instead of a template.


# Deleting Instances
Source: https://www.thundercompute.com/docs/vscode/operations/deleting-instances

Remove Thunder Compute instances and free up resources

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/deleting-instances">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/deleting-instances">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/deleting-instances">
    Web interface
  </QuickstartCard>
</Columns>

## Delete an Instance

<Warning>
  Deleting an instance permanently removes it and all associated data. This action cannot be undone. Consider [creating a snapshot](/vscode/operations/snapshots) first to back up your environment.
</Warning>

1. Open the Thunder Compute sidebar panel
2. Find the instance you want to delete
3. Click the delete button (trash icon) next to the instance
4. Confirm the deletion in the dialog

## Before Deleting

Before deleting an instance, make sure to:

1. **Download important files**: Use the VSCode file explorer to save any outputs, models, or data you need
2. **Create a snapshot**: If you want to restore your environment later, [create a snapshot](/vscode/operations/snapshots) first
3. **Push code to GitHub**: Commit and push any code changes to a remote repository

## Billing

Billing stops immediately when an instance is deleted. You are charged only for the time the instance was running.

Check your usage and billing details in the [console billing settings](https://console.thundercompute.com/settings/billing).


# File Transfers
Source: https://www.thundercompute.com/docs/vscode/operations/file-transfers

Copy files between your local machine and Thunder Compute instances

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/file-transfers">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/file-transfers">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/file-transfers">
    Web interface
  </QuickstartCard>
</Columns>

## Upload Files

1. Connect to your instance using the Connect button
2. In the new window, open the file explorer (sidebar)
3. Drag and drop files from your local machine into the explorer

## Download Files

1. Right-click on a file in the remote file explorer
2. Select **Download** to save it locally

## Alternative: Integrated Terminal

You can also use `scp` directly in the integrated terminal if you have the CLI installed locally.

## Best Practices

* **Compress large transfers**: Zip files before transferring to reduce time
* **Use cloud storage for big files**: For datasets over a few GB, upload to cloud storage and download directly to your instance
* **Back up important outputs**: Always download critical results before deleting an instance


# Modifying Instances
Source: https://www.thundercompute.com/docs/vscode/operations/modifying-instances

Change the resources of a running Thunder Compute instance

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/modifying-instances">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/modifying-instances">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/modifying-instances">
    Web interface
  </QuickstartCard>
</Columns>

## Modify an Instance

1. Open the Thunder Compute sidebar panel
2. Right-click on a running instance
3. Select **Modify Instance**
4. A configuration window will open—adjust the resources
5. Click **Save**

## What Can Be Modified

| Resource  | Can Modify?   | Notes                                                |
| --------- | ------------- | ---------------------------------------------------- |
| GPU Type  | Yes           |                                                      |
| GPU Count | Yes           |                                                      |
| vCPUs     | Yes           | Prototyping mode only                                |
| RAM       | Yes           | Scales with vCPUs (prototyping) or GPUs (production) |
| Mode      | Yes           | Switch between prototyping and production            |
| Disk Size | Increase only | Cannot shrink disk                                   |

<Note>
  RAM is automatically determined based on your configuration:

  * **Prototyping mode**: 8GB per vCPU
  * **Production mode**: 90GB per GPU
</Note>


# Monitoring Instances
Source: https://www.thundercompute.com/docs/vscode/operations/monitoring-instances

View the status of your Thunder Compute instances

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/monitoring-instances">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/monitoring-instances">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/monitoring-instances">
    Web interface
  </QuickstartCard>
</Columns>

## View Instances

Open the Thunder Compute sidebar panel to see all your instances. Each instance shows:

* Status indicator (running, creating, etc.)
* GPU type and count
* Instance ID

Click on an instance to see more details or connect to it.

## Refresh Status

Click the refresh button at the top of the panel to update the instance list.

## Instance States

| Status      | Description                                |
| ----------- | ------------------------------------------ |
| `RUNNING`   | Instance is active and ready to use        |
| `CREATING`  | Instance is being provisioned              |
| `RESTORING` | Instance is being restored from a snapshot |
| `DELETING`  | Instance is being removed                  |

## Benchmarking Notes

When measuring performance in **prototyping mode**, note that hardware-level metrics (temperature, wattage, utilization) may not be accurate due to CUDA-level optimizations. Use application-level metrics like iterations per second for reliable comparisons.

For accurate hardware metrics, use **production mode** instances.


# Port Forwarding
Source: https://www.thundercompute.com/docs/vscode/operations/port-forwarding

Expose HTTP services running on your instance to the internet

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/port-forwarding">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/port-forwarding">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/port-forwarding">
    Web interface
  </QuickstartCard>
</Columns>

## Port Forwarding

Public port forwarding with automatic HTTPS and DDoS protection is currently only available through the [CLI](/cli/operations/port-forwarding).

For local port forwarding while developing, you can use VS Code's built-in [port forwarding feature](https://code.visualstudio.com/docs/debugtest/port-forwarding) when connected to your instance.


# Snapshots
Source: https://www.thundercompute.com/docs/vscode/operations/snapshots

Save and restore the state of your Thunder Compute instances

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/snapshots">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/snapshots">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/snapshots">
    Web interface
  </QuickstartCard>
</Columns>

## Create a Snapshot

1. Open the Thunder Compute sidebar panel.
2. Right click the running instance.
3. Select **Create Snapshot**.
4. Name the new snapshot.

<img alt="Step by step on creating a snapshot" />

Snapshotting happens in the background—you can continue using your instance immediately. The snapshot captures the exact state at the moment you initiated it.

## View Snapshots

Your snapshots appear in the Thunder Compute panel below your instances.

## Restore from a Snapshot

1. Create a new instance.
2. Open the template menu.
3. Select your snapshot.

<img alt="Step by step on restoring a snapshot" />

<Note>
  Restoring from a snapshot can take up to 8 minutes per 100GB of data.
</Note>

## Delete a Snapshot

1. Open the Thunder Compute sidebar panel.
2. Right click the snapshot.
3. Select **Delete Snapshot**.

<img alt="Step by step on deleting a snapshot" />

## Best Practices

1. **Name snapshots descriptively**: Include the project, date, or purpose (e.g., `llama-finetuned-jan2026`)

2. **Clean up unused snapshots**: To minimize your bill, remove snapshots you no longer need.

## Snapshots vs External Backups

Snapshots are great for quickly restoring your environment, but they’re meant for convenience rather than long-term data security. We do not provide explicit guarantees about snapshot durability. For long-term data preservation, consider using:

* **GitHub** for code and configuration
* **Local downloads** for important outputs
* **Cloud storage** (R2, Google Drive) for large files

To learn about optimizing the a snapshot for faster creation and restoration, refer to our [Speeding Up Snapshots](/guides/speeding-up-snapshots) guide.


# SSH on Thunder Compute
Source: https://www.thundercompute.com/docs/vscode/operations/ssh

Use saved SSH keys to sign in to Thunder Compute instances when you need manual SSH access.

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/operations/ssh">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/operations/ssh">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/operations/ssh">
    Web interface
  </QuickstartCard>
</Columns>

<Warning>
  Manually SSHing is an advanced escape hatch. Thunder Compute already handles SSH, port forwarding, and key rotation through the **CLI**, **VS Code extension**, and **console**. Stick to the standard connect flows unless you have existing infrastructure that relies on raw SSH.
</Warning>

## Save an SSH key

The VS Code extension uses the same saved keys as the console. Open [Authentication → SSH Keys (Advanced)](https://console.thundercompute.com/settings/ssh) in the console to add or remove organization keys.

Saved keys live at the org level, so everyone on your team can reuse them when creating instances.

## Attach a key when creating an instance

The create-instance dialog in the VS Code extension lets you pick any key from your saved list. New windows reuse it automatically.

Instances include the selected public key in `authorized_keys` at boot. You can add keys later via the [Add SSH key to instance](/api-reference/instances/add-ssh-key-to-instance) API endpoint.

## SSH manually

1. Find the instance IP and SSH port from the instance details in the Thunder Compute sidebar, or run `tnr status` in a terminal.

2. From your local machine, run SSH with the private key that matches the saved public key, the reported port, and the `ubuntu` user:

   ```bash theme={null}
   ssh -i ~/.ssh/id_ed25519 -p <port> ubuntu@<instance-ip>
   ```

   Replace `~/.ssh/id_ed25519` with your private key path. Substitute `<port>` with the value from instance details. Most images use the `ubuntu` user; check your template if it differs.

3. Optional: use the command with JetBrains Gateway or any remote-SSH client.

## Quick troubleshooting

* **Permission denied:** make sure you are connecting as `ubuntu`, using the `-p <port>` from instance details, and that the matching private key exists locally.
* **Connection timed out:** re-check that you copied the correct port; the IP stays stable, but the exposed port can change if the instance is cycled.
* **Host verification failed:** remove the old entry from `~/.ssh/known_hosts` and retry. New IPs will change fingerprints.
* **Still stuck?** Double-check the IP, port, and key, or send a message in [Discord](https://discord.gg/thundercompute) with the SSH output.


# Quickstart
Source: https://www.thundercompute.com/docs/vscode/quickstart

Get started with Thunder Compute using VSCode, Cursor, or Windsurf

<Columns>
  <QuickstartCard title="VS Code" icon="window" href="/vscode/quickstart">
    Editor extension
  </QuickstartCard>

  <QuickstartCard title="CLI" icon="terminal" href="/cli/quickstart">
    Command line
  </QuickstartCard>

  <QuickstartCard title="Console" icon="browser" href="/console/quickstart">
    Web interface
  </QuickstartCard>
</Columns>

## Installation

Click the following links to access the Thunder Compute extension:

* [VSCode extension](vscode:extension/ThunderCompute.thunder-compute)
* [Cursor extension](cursor:extension/ThunderCompute.thunder-compute)
* [Windsurf extension](windsurf:extension/ThunderCompute.thunder-compute)

You must have already installed the corresponding editor for each link to work.

## Authentication

You may be automatically prompted to login. If not, open the command palette with `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) and run `Thunder Compute: Login`.

Your browser will open automatically to complete authentication.

## Add a Payment Method

In the console, [add a payment method](https://console.thundercompute.com/settings/billing) to your account.

## Using The Extension

You can create instances through the [console](https://console.thundercompute.com) or directly through the extension like so:

<img alt="Create Instance" />

Click on the `Connect` button next to your instance, shaped like two arrows pointing towards each other.

<img alt="Connect to Instance" />

<Note>
  If connecting to the instance fails, check that you have the remote-ssh extension installed on your editor.
</Note>

A new window will open connected to your instance. You can drag files you need into the file explorer, run notebooks, scripts, and more as if they were on your local machine.

<img alt="SSH View" />

That's it! You're now ready to use Thunder Compute.

## Next Steps

* Learn about [Prototyping vs Production](/prototyping-vs-production) to choose the right mode for your workload
* Explore [Technical Specifications](/technical-specs) for hardware, networking, and storage details
* Learn how to [transfer files](/vscode/operations/file-transfers), [create snapshots](/vscode/operations/snapshots), and more in the Operations section
* Learn how to [Run a Jupyter Notebook](/guides/running-jupyter-notebooks-on-thunder-compute)


# Add SSH key to instance
Source: https://www.thundercompute.com/docs/api-reference/instances/add-ssh-key-to-instance

https://api.thundercompute.com:8443/openapi.json post /instances/{id}/add_key
Add an SSH key to an existing instance. If public_key is provided in the request body, it will be added to authorized_keys. If no public_key is provided, a new key pair will be generated and the private key returned.



# Create instance
Source: https://www.thundercompute.com/docs/api-reference/instances/create-instance

https://api.thundercompute.com:8443/openapi.json post /instances/create
Create a new compute instance



# Delete instance
Source: https://www.thundercompute.com/docs/api-reference/instances/delete-instance

https://api.thundercompute.com:8443/openapi.json post /instances/{id}/delete
Delete a compute instance by ID



# List instances
Source: https://www.thundercompute.com/docs/api-reference/instances/list-instances

https://api.thundercompute.com:8443/openapi.json get /instances/list
Get a list of user's compute instances



# Modify instance
Source: https://www.thundercompute.com/docs/api-reference/instances/modify-instance

https://api.thundercompute.com:8443/openapi.json post /instances/{id}/modify
Modify a running compute instance's resources



# Create a snapshot
Source: https://www.thundercompute.com/docs/api-reference/snapshots/create-a-snapshot

https://api.thundercompute.com:8443/openapi.json post /snapshots/create
Create a new snapshot from a running instance



# Delete a snapshot
Source: https://www.thundercompute.com/docs/api-reference/snapshots/delete-a-snapshot

https://api.thundercompute.com:8443/openapi.json delete /snapshots/{id}
Delete a snapshot by ID



# List snapshots
Source: https://www.thundercompute.com/docs/api-reference/snapshots/list-snapshots

https://api.thundercompute.com:8443/openapi.json get /snapshots/list
Get a list of all snapshots for the authenticated user's organization



# Add an SSH key
Source: https://www.thundercompute.com/docs/api-reference/ssh-keys/add-an-ssh-key

https://api.thundercompute.com:8443/openapi.json post /keys/add
Add a new SSH public key to the authenticated user's organization



# Delete an SSH key
Source: https://www.thundercompute.com/docs/api-reference/ssh-keys/delete-an-ssh-key

https://api.thundercompute.com:8443/openapi.json delete /keys/{id}
Delete an SSH key by ID



# List SSH keys
Source: https://www.thundercompute.com/docs/api-reference/ssh-keys/list-ssh-keys

https://api.thundercompute.com:8443/openapi.json get /keys/list
Get a list of all SSH keys for the authenticated user's organization



# Get current pricing
Source: https://www.thundercompute.com/docs/api-reference/utilities/get-current-pricing

https://api.thundercompute.com:8443/openapi.json get /pricing
Retrieve current hourly pricing information for compute resources



# Get thunder templates
Source: https://www.thundercompute.com/docs/api-reference/utilities/get-thunder-templates

https://api.thundercompute.com:8443/openapi.json get /thunder-templates
Get available thunder templates for instance creation



# Billing
Source: https://www.thundercompute.com/docs/billing

Understand Thunder Compute's usage-based billing, payment methods, billing alerts, current rates, and tips for saving on GPU cloud costs.

## Payment Options

There are **two ways to pay** for Thunder Compute:

### Option 1: Auto-Pay

Set up auto-pay by saving a credit card in the Stripe customer portal. Open it from [console.thundercompute.com/settings/billing](https://console.thundercompute.com/settings/billing) by clicking "manage billing".

### Option 2: Preload Credit

Add credit directly to your account as an alternative to auto-pay. This credit never expires and will be used before any saved payment method.

**Order of payment**

1. Any preloaded credit you've added
2. Charges to your saved payment method

You can switch between options or use both—set up auto-pay anytime, even if you started with preloaded credit.

## Billing Alerts

* **Instance reminders:** We'll email you about any running instances so you're never caught off guard.
* **Threshold charges:** As your usage grows, we'll bill your card at preset checkpoints (which rise over time) to prevent runaway bills.

## Our rates

All compute resources are billed per minute only while your instances run. Rates and promotions are subject to change without notice. For current rates, see our [pricing page](https://www.thundercompute.com/pricing).

## Credit Terms

* **Preloaded credit** does not expire and will be used before charging your saved card.
* **Promotional credit** can be revoked at our discretion.
* **Refunds:** Credit is non-refundable.

## Money-Saving Tips

While Thunder Compute is already the cheapest GPU cloud platform, there are a few strategies we recommend to reduce your bill:

* Delete instances when you're done with them to stop billing.
* Right‑size new workloads with `tnr create --gpu`, `--vcpus`, and related flags so you only pay for what you use.

We think this balances a smooth experience with strong verification—but if you have feedback or questions, please hop into our [Discord](https://discord.com/invite/nwuETS9jJK). We're always happy to improve!


# Data Processing Addendum
Source: https://www.thundercompute.com/docs/guides/data-processing-addendum

Our Data Processing Addendum outlining data handling and privacy terms.

## Sample Agreement

Data Processing Agreement

## Using this DPA

This DPA has 2 parts: (1) the Key Terms on this Cover Page and (2) the Common Paper DPA Standard Terms Version 1 posted at commonpaper.com/standards/data-processing-agreement/1.1 (“DPA Standard Terms”), which is incorporated by reference. If there is any inconsistency between the parts of the DPA, the Cover Page will control over the DPA Standard Terms. Capitalized and highlighted words have the meanings given on the Cover Page. However, if the Cover Page omits or does not define a highlighted word, the default meaning will be “none” or “not applicable” and the correlating clause, sentence, or section does not apply to this Agreement. All other capitalized words have the meanings given in the DPA Standard Terms or the Agreement. A copy of the DPA Standard Terms is attached for convenience only.

## Key Terms

The key legal terms of the DPA are as follows:

| Term                      | Details                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| Agreement                 | Reference to sales contract will be set when sending agreement                                 |
| Approved Subprocessors    | [https://www.thundercompute.com/sub-processors](https://www.thundercompute.com/sub-processors) |
| Provider Security Contact | `support@thundercompute.com`                                                                   |
| Security Policy           | As defined in the Agreement.                                                                   |

### Service Provider Relationship

To the extent California Consumer Privacy Act, Cal. Civ. Code § 1798.100 et seq (“CCPA”) applies, the parties acknowledge and agree that Provider is a service provider and is receiving Personal Data from Customer to provide the Service as agreed in the Agreement and detailed below (see Nature and Purpose of Processing), which constitutes a limited and specified business purpose. Provider will not sell or share any Personal Data provided by Customer under the Agreement. In addition, Provider will not retain, use, or disclose any Personal Data provided by Customer under the Agreement except as necessary for providing the Service for Customer, as stated in the Agreement, or as permitted by Applicable Data Protection Laws. Provider certifies that it understands the restrictions of this paragraph and will comply with all Applicable Data Protection Laws. Provider will notify Customer if it can no longer meet its obligations under the CCPA.

## Restricted Transfers

### Governing Member State

* EEA Transfers: Ireland
* UK Transfers: England and Wales

## Annex I(A) List of Parties

### Data Exporter

* Name: the Customer signing this DPA
* Activities relevant to transfer: See Annex I(B)
* Role: Controller

### Data Importer

* Name: the Provider signing this DPA
* Contact person: Carl Peterson, CEO
* Address: 887 w marietta st nw, Suite N105, Georgia 30318, USA
* Activities relevant to transfer: See Annex I(B)
* Role: Processor

## Annex I(B) Description of Transfer and Processing Activities

### Service

The Service is: GPU cloud computing with on-demand cloud instances, backed by physical servers, in addition to data storage.

### Categories of Data Subjects

* Customer's employees

### Categories of Personal Data

* Name
* Contact information such as email, phone number, or address
* Financial information such as bank account numbers
* Transactional information such as account information or purchases
* User activity and analysis such as device information or IP address
* Location information

### Special Category Data

Is special category data (as defined in Article 9 of the GDPR) Processed? No

### Frequency of Transfer

Continuous

### Nature and Purpose of Processing

* Receiving data, including collection, accessing, retrieval, recording, and data entry
* Holding data, including storage, organization, and structuring
* Using data, including analysis, consultation, testing, automated decision making, and profiling
* Updating data, including correcting, adaption, alteration, alignment, and combination
* Protecting data, including restricting, encrypting, and security testing
* Sharing data, including disclosure, dissemination, allowing access, or otherwise making available
* Returning data to the data exporter or data subject
* Erasing data, including destruction and deletion

### Duration of Processing

Provider will process Customer Personal Data as long as required (i) to conduct the Processing activities instructed in Section 2.2(a)-(d) of the Standard Terms; or (ii) by Applicable Laws.

## Annex I(C)

### Competent Supervisory Authority

The supervisory authority will be the supervisory authority of the data exporter, as determined in accordance with Clause 13 of the EEA SCCs or the relevant provision of the UK Addendum.

## Annex II

### Technical and Organizational Security Measures

See Security Policy

Provider and Customer have not changed the DPA Standard Terms except for the details on the Cover Page above. By signing this Cover Page, each party agrees to enter into this DPA as of the last date of signature below.

## Signatures

| Field                | Provider (Thunder Compute) | Customer |
| -------------------- | -------------------------- | -------- |
| Signature            |                            |          |
| Print Name           |                            |          |
| Title                |                            |          |
| Legal Notice Address | `carl@thundercompute.com`  |          |
| Date                 |                            |          |

## 1. Processor and Subprocessor Relationships

### 1.1 Provider as Processor

In situations where Customer is a Controller of the Customer Personal Data, Provider will be deemed a Processor that is Processing Personal Data on behalf of Customer.

### 1.2 Provider as Subprocessor

In situations where Customer is a Processor of the Customer Personal Data, Provider will be deemed a Subprocessor of the Customer Personal Data.

## 2. Processing

### 2.1 Processing Details

Annex I(B) on the Cover Page describes the subject matter, nature, purpose, and duration of this Processing, as well as the Categories of Personal Data collected and Categories of Data Subjects.

### 2.2 Processing Instructions

Customer instructs Provider to Process Customer Personal Data: (a) to provide and maintain the Service; (b) as may be further specified through Customer’s use of the Service; (c) as documented in the Agreement; and (d) as documented in any other written instructions given by Customer and acknowledged by Provider about Processing Customer Personal Data under this DPA. Provider will abide by these instructions unless prohibited from doing so by Applicable Laws. Provider will immediately inform Customer if it is unable to follow the Processing instructions. Customer has given and will only give instructions that comply with Applicable Laws.

### 2.3 Processing by Provider

Provider will only Process Customer Personal Data in accordance with this DPA, including the details in the Cover Page. If Provider updates the Service to update existing or include new products, features, or functionality, Provider may change the Categories of Data Subjects, Categories of Personal Data, Special Category Data, Special Category Data Restrictions or Safeguards, Frequency of Transfer, Nature and Purpose of Processing, and Duration of Processing as needed to reflect the updates by notifying Customer of the updates and changes.

### 2.4 Customer Processing

Where Customer is a Processor and Provider is a Subprocessor, Customer will comply with all Applicable Laws that apply to Customer’s Processing of Customer Personal Data. Customer’s agreement with its Controller will similarly require Customer to comply with all Applicable Laws that apply to Customer as a Processor. In addition, Customer will comply with the Subprocessor requirements in Customer’s agreement with its Controller.

### 2.5 Consent to Processing

Customer has complied with and will continue to comply with all Applicable Data Protection Laws concerning its provision of Customer Personal Data to Provider and/or the Service, including making all disclosures, obtaining all consents, providing adequate choice, and implementing relevant safeguards required under Applicable Data Protection Laws.

### 2.6 Subprocessors

1. Provider will not provide, transfer, or hand over any Customer Personal Data to a Subprocessor unless Customer has approved the Subprocessor. The current list of Approved Subprocessors includes the identities of the Subprocessors, their country of location, and their anticipated Processing tasks. Provider will inform Customer at least 10 business days in advance and in writing of any intended changes to the Approved Subprocessors whether by addition or replacement of a Subprocessor, which allows Customer to have enough time to object to the changes before the Provider begins using the new Subprocessor(s). Provider will give Customer the information necessary to allow Customer to exercise its right to object to the change to Approved Subprocessors. Customer has 30 days after notice of a change to the Approved Subprocessors to object, otherwise Customer will be deemed to accept the changes. If Customer objects to the change within 30 days of notice, Customer and Provider will cooperate in good faith to resolve Customer’s objection or concern.
2. When engaging a Subprocessor, Provider will have a written agreement with the Subprocessor that ensures the Subprocessor only accesses and uses Customer Personal Data (i) to the extent required to perform the obligations subcontracted to it, and (ii) consistent with the terms of Agreement.
3. If the GDPR applies to the Processing of Customer Personal Data, (i) the data protection obligations described in this DPA (as referred to in Article 28(3) of the GDPR, if applicable) are also imposed on the Subprocessor, and (ii) Provider’s agreement with the Subprocessor will incorporate these obligations, including details about how Provider and its Subprocessor will coordinate to respond to inquiries or requests about the Processing of Customer Personal Data. In addition, Provider will share, at Customer’s request, a copy of its agreements (including any amendments) with its Subprocessors. To the extent necessary to protect business secrets or other confidential information, including personal data, Provider may redact the text of its agreement with its Subprocessor prior to sharing a copy.
4. Provider remains fully liable for all obligations subcontracted to its Subprocessors, including the acts and omissions of its Subprocessors in Processing Customer Personal Data. Provider will notify Customer of any failure by its Subprocessors to fulfill a material obligation about Customer Personal Data under the agreement between Provider and the Subprocessor.

## 3. Restricted Transfers

### 3.1 Authorization

Customer agrees that Provider may transfer Customer Personal Data outside the EEA, the United Kingdom, or other relevant geographic territory as necessary to provide the Service. If Provider transfers Customer Personal Data to a territory for which the European Commission or other relevant supervisory authority has not issued an adequacy decision, Provider will implement appropriate safeguards for the transfer of Customer Personal Data to that territory consistent with Applicable Data Protection Laws.

### 3.2 Ex-EEA Transfers

Customer and Provider agree that if the GDPR protects the transfer of Customer Personal Data, the transfer is from Customer from within the EEA to Provider outside of the EEA, and the transfer is not governed by an adequacy decision made by the European Commission, then by entering into this DPA, Customer and Provider are deemed to have signed the EEA SCCs and their Annexes, which are incorporated by reference. Any such transfer is made pursuant to the EEA SCCs, which are completed as follows:

1. Module Two (Controller to Processor) of the EEA SCCs apply when Customer is a Controller and Provider is Processing Customer Personal Data for Customer as a Processor.
2. Module Three (Processor to Sub-Processor) of the EEA SCCs apply when Customer is a Processor and Provider is Processing Customer Personal Data on behalf of Customer as a Subprocessor.
3. For each module, the following applies (when applicable):
   * The optional docking clause in Clause 7 does not apply;
   * In Clause 9, Option 2 (general written authorization) applies, and the minimum time period for prior notice of Subprocessor changes is 10 business days;
   * In Clause 11, the optional language does not apply;
   * All square brackets in Clause 13 are removed;
   * In Clause 17 (Option 1), the EEA SCCs will be governed by the laws of Governing Member State;
   * In Clause 18(b), disputes will be resolved in the courts of the Governing Member State; and
   * The Cover Page to this DPA contains the information required in Annex I, Annex II, and Annex III of the EEA SCCs.

### 3.3 Ex-UK Transfers

Customer and Provider agree that if the UK GDPR protects the transfer of Customer Personal Data, the transfer is from Customer from within the United Kingdom to Provider outside of the United Kingdom, and the transfer is not governed by an adequacy decision made by the United Kingdom Secretary of State, then by entering into this DPA, Customer and Provider are deemed to have signed the UK Addendum and their Annexes, which are incorporated by reference. Any such transfer is made pursuant to the UK Addendum, which is completed as follows:

1. Section 3.2 of this DPA contains the information required in Table 2 of the UK Addendum.
2. Table 4 of the UK Addendum is modified as follows: Neither party may end the UK Addendum as set out in Section 19 of the UK Addendum; to the extent ICO issues a revised Approved Addendum under Section ‎18 of the UK Addendum, the parties will work in good faith to revise this DPA accordingly.
3. The Cover Page contains the information required by Annex 1A, Annex 1B, Annex II, and Annex III of the UK Addendum.

### 3.4 Other International Transfers

For Personal Data transfers where Swiss law (and not the law in any EEA member state or the United Kingdom) applies to the international nature of the transfer, references to the GDPR in Clause 4 of the EEA SCCs are, to the extent legally required, amended to refer to the Swiss Federal Data Protection Act or its successor instead, and the concept of supervisory authority will include the Swiss Federal Data Protection and Information Commissioner.

## 4. Security Incident Response

Upon becoming aware of any Security Incident, Provider will: (a) notify Customer without undue delay when feasible, but no later than 72 hours after becoming aware of the Security Incident; (b) provide timely information about the Security Incident as it becomes known or as is reasonably requested by Customer; and (c) promptly take reasonable steps to contain and investigate the Security Incident. Provider’s notification of or response to a Security Incident as required by this DPA will not be construed as an acknowledgment by Provider of any fault or liability for the Security Incident.

## 5. Audit & Reports

### 5.1 Audit Rights

Provider will give Customer all information reasonably necessary to demonstrate its compliance with this DPA and Provider will allow for and contribute to audits, including inspections by Customer, to assess Provider’s compliance with this DPA. However, Provider may restrict access to data or information if Customer’s access to the information would negatively impact Provider’s intellectual property rights, confidentiality obligations, or other obligations under Applicable Laws. Customer acknowledges and agrees that it will only exercise its audit rights under this DPA and any audit rights granted by Applicable Data Protection Laws by instructing Provider to comply with the reporting and due diligence requirements below. Provider will maintain records of its compliance with this DPA for 3 years after the DPA ends.

### 5.2 Security Reports

Customer acknowledges that Provider is regularly audited against the standards defined in the Security Policy by independent third-party auditors. Upon written request, Provider will give Customer, on a confidential basis, a summary copy of its then-current Report so that Customer can verify Provider’s compliance with the standards defined in the Security Policy.

### 5.3 Security Due Diligence

In addition to the Report, Provider will respond to reasonable requests for information made by Customer to confirm Provider’s compliance with this DPA, including responses to information security, due diligence, and audit questionnaires, or by giving additional information about its information security program. All such requests must be in writing and made to the Provider Security Contact and may only be made once a year.

## 6. Coordination & Cooperation

### 6.1 Response to Inquiries

If Provider receives any inquiry or request from anyone else about the Processing of Customer Personal Data, Provider will notify Customer about the request and Provider will not respond to the request without Customer’s prior consent. Examples of these kinds of inquiries and requests include a judicial or administrative or regulatory agency order about Customer Personal Data where notifying Customer is not prohibited by Applicable Law, or a request from a data subject. If allowed by Applicable Law, Provider will follow Customer’s reasonable instructions about these requests, including providing status updates and other information reasonably requested by Customer. If a data subject makes a valid request under Applicable Data Protection Laws to delete or opt out of Customer’s giving of Customer Personal Data to Provider, Provider will assist Customer in fulfilling the request according to the Applicable Data Protection Law. Provider will cooperate with and provide reasonable assistance to Customer, at Customer’s expense, in any legal response or other procedural action taken by Customer in response to a third-party request about Provider’s Processing of Customer Personal Data under this DPA.

### 6.2 DPIAs and DTIAs

If required by Applicable Data Protection Laws, Provider will reasonably assist Customer in conducting any mandated data protection impact assessments or data transfer impact assessments and consultations with relevant data protection authorities, taking into consideration the nature of the Processing and Customer Personal Data.

## 7. Deletion of Customer Personal Data

### 7.1 Deletion by Customer

Provider will enable Customer to delete Customer Personal Data in a manner consistent with the functionality of the Services. Provider will comply with this instruction as soon as reasonably practicable except where further storage of Customer Personal Data is required by Applicable Law.

### 7.2 Deletion at DPA Expiration

1. After the DPA expires, Provider will return or delete Customer Personal Data at Customer’s instruction unless further storage of Customer Personal Data is required or authorized by Applicable Law. If return or destruction is impracticable or prohibited by Applicable Laws, Provider will make reasonable efforts to prevent additional Processing of Customer Personal Data and will continue to protect the Customer Personal Data remaining in its possession, custody, or control. For example, Applicable Laws may require Provider to continue hosting or Processing Customer Personal Data.
2. If Customer and Provider have entered the EEA SCCs or the UK Addendum as part of this DPA, Provider will only give Customer the certification of deletion of Personal Data described in Clause 8.1(d) and Clause 8.5 of the EEA SCCs if Customer asks for one.

## 8. Limitation of Liability

### 8.1 Liability Caps and Damages Waiver

To the maximum extent permitted under Applicable Data Protection Laws, each party’s total cumulative liability to the other party arising out of or related to this DPA will be subject to the waivers, exclusions, and limitations of liability stated in the Agreement.

### 8.2 Related-Party Claims

Any claims made against Provider or its Affiliates arising out of or related to this DPA may only be brought by the Customer entity that is a party to the Agreement.

### 8.3 Exceptions

This DPA does not limit any liability to an individual about the individual’s data protection rights under Applicable Data Protection Laws. In addition, this DPA does not limit any liability between the parties for violations of the EEA SCCs or UK Addendum.

## 9. Conflicts Between Documents

This DPA forms part of and supplements the Agreement. If there is any inconsistency between this DPA, the Agreement, or any of their parts, the part listed earlier will control over the part listed later for that inconsistency: (1) the EEA SCCs or the UK Addendum, (2) this DPA, and then (3) the Agreement.

## 10. Term of Agreement

This DPA will start when Provider and Customer agree to a Cover Page for the DPA and sign or electronically accept the Agreement and will continue until the Agreement expires or is terminated. However, Provider and Customer will each remain subject to the obligations in this DPA and Applicable Data Protection Laws until Customer stops transferring Customer Personal Data to Provider and Provider stops Processing Customer Personal Data.

## 11. Definitions

### 11.1 Applicable Laws

“Applicable Laws” means the laws, rules, regulations, court orders, and other binding requirements of a relevant government authority that apply to or govern a party.

### 11.2 Applicable Data Protection Laws

“Applicable Data Protection Laws” means the Applicable Laws that govern how the Service may process or use an individual’s personal information, personal data, personally identifiable information, or other similar term.

### 11.3 Controller

“Controller” will have the meaning(s) given in the Applicable Data Protection Laws for the company that determines the purpose and extent of Processing Personal Data.

### 11.4 Cover Page

“Cover Page” means a document that is signed or electronically accepted by the parties that incorporates these DPA Standard Terms and identifies Provider, Customer, and the subject matter and details of the data processing.

### 11.5 Customer Personal Data

“Customer Personal Data” means Personal Data that Customer uploads or provides to Provider as part of the Service and that is governed by this DPA.

### 11.6 DPA

“DPA” means these DPA Standard Terms, the Cover Page between Provider and Customer, and the policies and documents referenced in or attached to the Cover Page.

### 11.7 EEA SCCs

“EEA SCCs” means the standard contractual clauses annexed to the European Commission's Implementing Decision 2021/914 of 4 June 2021 on standard contractual clauses for the transfer of personal data to third countries pursuant to Regulation (EU) 2016/679 of the European Parliament and of the European Council.

### 11.8 European Economic Area (EEA)

“European Economic Area” or “EEA” means the member states of the European Union, Norway, Iceland, and Liechtenstein.

### 11.9 GDPR

“GDPR” means European Union Regulation 2016/679 as implemented by local law in the relevant EEA member nation.

### 11.10 Personal Data

“Personal Data” will have the meaning(s) given in the Applicable Data Protection Laws for personal information, personal data, or other similar term.

### 11.11 Processing

“Processing” or “Process” will have the meaning(s) given in the Applicable Data Protection Laws for any use of, or performance of a computer operation on, Personal Data, including by automatic methods.

### 11.12 Processor

“Processor” will have the meaning(s) given in the Applicable Data Protection Laws for the company that Processes Personal Data on behalf of the Controller.

### 11.13 Report

“Report” means audit reports prepared by another company according to the standards defined in the Security Policy on behalf of Provider.

### 11.14 Restricted Transfer

“Restricted Transfer” means (a) where the GDPR applies, a transfer of personal data from the EEA to a country outside of the EEA which is not subject to an adequacy determination by the European Commission; and (b) where the UK GDPR applies, a transfer of personal data from the United Kingdom to any other country which is not subject to adequacy regulations adopted pursuant to Section 17A of the United Kingdom Data Protection Act 2018.

### 11.15 Security Incident

“Security Incident” means a Personal Data Breach as defined in Article 4 of the GDPR.

### 11.16 Service

“Service” means the product and/or services described in the Agreement.

### 11.17 Special Category Data

"Special Category Data” will have the meaning given in Article 9 of the GDPR.

### 11.18 Subprocessor

“Subprocessor” will have the meaning(s) given in the Applicable Data Protection Laws for a company that, with the approval and acceptance of Controller, assists the Processor in Processing Personal Data on behalf of the Controller.

### 11.19 UK GDPR

“UK GDPR” means European Union Regulation 2016/679 as implemented by section 3 of the United Kingdom’s European Union (Withdrawal) Act of 2018 in the United Kingdom.

### 11.20 UK Addendum

“UK Addendum” means the international data transfer addendum to the EEA SCCs issued by the Information Commissioner for Parties making Restricted Transfers under S119A(1) Data Protection Act 2018.


# Install MCP Server
Source: https://www.thundercompute.com/docs/guides/mcp-server-for-managing-gpus

Install the Mintlify MCP server to host Thunder Compute docs locally. Enables AI tools like Cursor to provide instant answers based on documentation.

## TL;DR

```
# 1 – install the docs bundle
npx @mintlify/mcp@latest add thundercompute

# 2 – start the server
node ~/.mcp/thundercompute/src/index.js
```

Your **Thunder Compute MCP** server is now live at [**http://localhost:5001**](http://localhost:5001) and ready for any AI client.

## Connect in Cursor

1. Open **Cursor → Settings → Docs**.
2. **Add Source** → `http://localhost:5001`.
3. Ask something like *"How do I submit a batch to Thunder Compute?"*.

## Update docs

Run the install command again whenever you need the latest release:

```
npx @mintlify/mcp@latest add thundercompute
```


# Thunder Compute Referral Program
Source: https://www.thundercompute.com/docs/guides/referral-program

Earn credits by referring friends to Thunder Compute. Get 3% of every dollar your referrals spend on GPU instances with our lifetime rewards program.

**Refer a friend, earn credit.** Share your unique referral link and receive credits every time someone you refer spends on Thunder Compute GPUs.

<Note>
  This program is currently in beta. Terms may evolve as we improve the program based on user feedback.
</Note>

## How It Works

Our referral program rewards you with **3% of every dollar** your referrals spend on GPU instances. Here's what you need to know:

* **Reward Rate:** 3% of all spending by referred users
* **Duration:** Lifetime rewards for each referred customer
* **Credits:** Paid out in Thunder Compute credits (non-transferable)
* **Tracking:** Credits apply to paid, consumed compute resources. These typically post within minutes of a finalized invoice for consumed compute.

We created this program as a way to give back to our community. Rather than paying advertisers, we want to reward you for your contribution to Thunder Compute.

By referring even a medium-size startup you can often receive thousands of dollars of free compute.

## Getting Started

### 1. Find Your Referral Link

1. Sign in to the [Thunder Compute Console](https://console.thundercompute.com/)
2. Navigate to **Settings › General**
3. Copy your unique referral link
4. Share it anywhere—social media, tutorials, blog posts, or direct messages

### 2. Share and Earn

Once someone creates a new account using your link and starts using GPU instances, you'll automatically earn 3% of their payments as credits.

## Eligibility Requirements

### For Referrers

* Active Thunder Compute account in good standing
* No restrictions on sharing methods or platforms

### For Referrals

* Must create a **new account** via your referral link
* Existing accounts that sign up through referral links are not eligible
* Self-referrals and duplicate accounts are prohibited

<Warning>
  Credits are non-transferable and cannot be converted to cash. They can only be used for Thunder Compute services.
</Warning>

## Program Rules

### Fair Use Policy

We maintain strict anti-fraud measures to ensure program integrity:

* Creating fake accounts is prohibited
* Self-referrals will result in credit removal
* Violating Thunder Compute's Terms & Conditions may lead to account suspension
* All referral activity is monitored for suspicious patterns

### Program Changes

Thunder Compute reserves the right to:

* Modify reward rates or eligibility requirements
* Update program terms with advance notice
* Discontinue the program if necessary

We'll announce any changes through email notifications and documentation updates.

## Frequently Asked Questions

**Q: When do I receive my referral credits?**
A: Credits are typically added to your account within minutes of your referral's successful invoice.

**Q: Is there a limit to how much I can earn?**
A: No, there's no cap on referral earnings. The more successful referrals you make, the more you earn.

**Q: Can I refer existing Thunder Compute users?**
A: No, only new users who create accounts through your referral link are eligible.

**Q: What counts as a qualifying payment?**
A: Only direct card payments for GPU instances qualify for referral rewards. Usage on free or referral credits do not qualify.

## Need Help?

Have questions about referral eligibility, credit posting, or the program in general? Contact our support team:

* **Discord:** Join our [community server](https://discord.com/invite/nwuETS9jJK)

Thank you for giving back to the Thunder Compute community!


# Weights & Biases
Source: https://www.thundercompute.com/docs/guides/weights-and-biases

Track, debug, and optimize GPU-heavy workloads on Thunder Compute instances using Weights & Biases (wandb).

Weights & Biases (wandb) is an experiment tracking and model management platform that’s particularly useful when training large models on Cloud GPUs. It helps you:

* Track training runs, hyperparameters, and metrics
* Monitor GPU/CPU utilization in real time
* Version datasets and model checkpoints
* Run large-scale hyperparameter sweeps across many GPU instances

On Thunder Compute, wandb helps you monitor GPU utilization, identify bottlenecks, and track training metrics.

***

## Prerequisites

* A Thunder Compute GPU instance created and connected
* Python environment set up on your instance
* A Weights & Biases account ([https://wandb.ai/site](https://wandb.ai/site))

***

## Installation

Install wandb on your Thunder Compute instance:

```bash theme={null}
pip install wandb
```

Or add to a `requirements.txt`:

```bash theme={null}
echo "wandb" >> requirements.txt
pip install -r requirements.txt
```

***

## Authentication

Authenticate with:

```bash theme={null}
wandb login
```

Or via environment variable:

```bash theme={null}
export WANDB_API_KEY="your_api_key"
wandb login --relogin
```

You will see the following below:

```
wandb: Logging into wandb.ai. (Learn how to deploy a W&B server locally: https://wandb.me/wandb-server)
wandb: You can find your API key in your browser here: https://wandb.ai/authorize?ref=models
wandb: Paste an API key from your profile and hit enter, or press ctrl+c to quit:
```

Enter your API key which can be found on the homepage of wandb.ai after you create an account, once entered you will see:

```
wandb: No netrc file found, creating one.
wandb: Appending key for api.wandb.ai to your netrc file: /home/ubuntu/.netrc
wandb: Currently logged in as: username (entity-name) to https://api.wandb.ai. Use `wandb login --relogin` to force relogin
```

<Note>
  For shared or production Thunder instances, environment variables or secret
  managers are preferred over pasting API keys directly.
</Note>

***

## Getting Started

Follow these steps to run your first wandb experiment on your Thunder Compute instance.

### Step 1 — Create a Training File

Create a new Python file on your instance:

```bash theme={null}
nano train.py
```

Or create a new file within your IDE connected over SSH.

### Step 2 — Paste Minimal Working Example

Copy this minimal example into your `train.py` file:

```python theme={null}
import wandb
import time

# Initialize wandb
wandb.init(
    project="thunder-resnet",
    name="quick-test",
    config={
        "learning_rate": 0.001,
        "batch_size": 32,
        "epochs": 5,
    },
)

# Simple training loop simulation
for epoch in range(5):
    # Simulate training metrics
    train_loss = 1.0 / (epoch + 1)
    train_acc = 0.5 + epoch * 0.1

    # Log metrics to wandb
    wandb.log({
        "epoch": epoch,
        "train/loss": train_loss,
        "train/accuracy": train_acc,
    })

    time.sleep(0.5)  # Simulate work

wandb.finish()
```

### Step 3 — Run the Script

Execute your training script:

```bash theme={null}
python train.py
```

### Step 4 — Expected Output

You should see output similar to:

```
wandb: Currently logged in as: your-username (entity-name) to https://api.wandb.ai. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.23.0
wandb: Run data is saved locally in /home/ubuntu/wandb/run-20251120_135726-abcd
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run quick-test
wandb: ⭐️ View project at https://wandb.ai/entity-name/thunder-resnet
wandb: 🚀 View run at https://wandb.ai/entity-name/thunder-resnet/runs/abcd
wandb:
wandb: Run history:
wandb:          epoch ▁▃▅▆█
wandb: train/accuracy ▁▃▅▆█
wandb:     train/loss █▄▂▁▁
wandb:
wandb: Run summary:
wandb:          epoch 4
wandb: train/accuracy 0.9
wandb:     train/loss 0.2
wandb:
wandb: 🚀 View run quick-test at: https://wandb.ai/entity-name/thunder-resnet/runs/abcd
wandb: ⭐️ View project at: https://wandb.ai/entity-name/thunder-resnet
wandb: Synced 4 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20251120_135726-abcd/logs
```

### Step 5 — View Your Results

1. **View your dashboard**: Click the link in the output or visit [https://wandb.ai](https://wandb.ai) and navigate to your project
2. **View in Table view**: Go to **(Project Name)** > **Projects** > **thunder-resnet** > **Table** to see all your runs in a tabular format
3. **Compare runs**: Run the script multiple times with different configurations to compare results
4. **Add artifacts**: See the [Model Checkpointing with Weights & Biases Artifacts](#model-checkpointing-with-weights--biases-artifacts) section to version checkpoints and datasets
5. **Scale to multi-GPU**: Check out [Distributed Training](#distributed-training-ddp-lightning-deepspeed) for multi-GPU setups
6. **Run sweeps**: Use [Hyperparameter Sweeps](#hyperparameter-sweeps-multi‑gpu-multi‑instance) for automated hyperparameter search

***

## Viewing Results

1. Visit [https://wandb.ai/site](https://wandb.ai/site)
2. Select your project
3. Explore:
   * Metrics charts
   * GPU utilization
   * Model checkpoints
   * Dataset artifacts
   * Sweep dashboards

***

## Core Concepts for Cloud GPU Workloads

When using remote GPUs, these wandb features matter most:

1. **Run tracking** — metrics, hyperparameters, logs
2. **GPU/system monitoring** — GPU utilization, power, memory, CPU load
3. **Artifacts** — versioned checkpoints and datasets
4. **Sweeps** — distributed hyperparameter search
5. **Groups & jobs** — organize multi-GPU/distributed training

***

## Basic Usage

### Initialize a Run

```python theme={null}
import wandb

wandb.init(
    project="my-thunder-project",
    name="baseline-resnet50",
    config={
        "learning_rate": 3e-4,
        "batch_size": 64,
        "epochs": 20,
        "optimizer": "adamw",
        "precision": "fp16",
    },
)
```

### Log Metrics

```python theme={null}
wandb.log({
    "train/loss": loss,
    "train/accuracy": acc,
    "step": step,
})
```

### Best Logging Practices

* Log every **N steps** (e.g., 10–50) to minimize overhead
* Avoid logging huge tensors every step
* Use artifacts for large files

***

## GPU & System Monitoring

Wandb automatically collects:

* GPU utilization
* GPU memory usage
* GPU temperature and power
* CPU usage
* RAM usage
* Disk and network I/O

Use these graphs to diagnose:

* **GPU-bound** workloads
* **Data-bound** workloads
* **Bottlenecks** due to I/O or preprocessing
* **Too-small batch sizes**

### Improving GPU Utilization

* Increase batch size until GPU memory is near capacity
* Use **mixed precision** (`torch.cuda.amp`)
* Increase dataloader workers
* Preload/augment data on the GPU
* Reduce unnecessary synchronizations

***

## Model Checkpointing with Weights & Biases Artifacts

When you train on Thunder Compute GPU instances, it's important that your model checkpoints are **not** tied to a single machine. Weights & Biases Artifacts provide a simple way to:

* Persist checkpoints even if the instance is deleted
* Move checkpoints between different Thunder instances (or GPU types)
* Share models with your team
* Reproduce and resume long-running training jobs

This section provides a walkthrough of how to do checkpointing with wandb.

***

### Why use Artifacts for checkpoints?

Saving checkpoints only to the local filesystem is risky:

* Thunder instances may be stopped or recreated
* You may want to resume training on a *different* GPU (A100 → H100)
* Your team may need to reuse your model
* You may want versioned, reproducible training history

Artifacts solve this by storing checkpoints in W\&B's managed, versioned storage.

***

### Step 1 — Save a checkpoint locally during training

Inside your real training loop, periodically save a checkpoint.\
For real projects (PyTorch):

```python theme={null}
import torch

# ... inside your training loop ...
if (epoch + 1) % 5 == 0:
    ckpt_path = f"checkpoints/model_epoch_{epoch+1}.pt"
    torch.save(model.state_dict(), ckpt_path)
```

> It is best practice to save checkpoints inside a dedicated `checkpoints/` folder.

***

### Step 2 — Log the checkpoint as a W\&B Artifact

Right after saving your file:

```python theme={null}
import wandb

artifact = wandb.Artifact(
    name=f"resnet50-epoch-{epoch+1}",
    type="model",
    metadata={
        "epoch": epoch + 1,
        "val_loss": float(val_loss),
        "val_accuracy": float(val_acc),
    },
)

artifact.add_file(ckpt_path)
wandb.log_artifact(artifact)
```

This uploads your checkpoint to W\&B and keeps a permanent copy.

***

### Step 3 — View & manage checkpoints in the W\&B UI

1. Go to your wandb project
2. Open the **Artifacts** tab
3. Click your model artifact
4. You can now:
   * View version history (v0, v1, v2…)
   * Open the metrics/metadata
   * Download the checkpoint
   * Use it as an input for new runs

***

### Step 4 — Restore a checkpoint on another Thunder instance

On a fresh machine:

```python theme={null}
import wandb
import torch

run = wandb.init(project="my-thunder-project", job_type="restore")

artifact = run.use_artifact(
    "wato/my-thunder-project/resnet50-epoch-10:latest",
    type="model",
)
artifact_dir = artifact.download()

checkpoint = torch.load(f"{artifact_dir}/model_epoch_10.pt", map_location="cuda")
model.load_state_dict(checkpoint)
model.to("cuda")
```

You now have the exact model weights from your previous run — even if the original instance is gone.

***

### Step 5 — Resume training

```python theme={null}
model.load_state_dict(checkpoint)
model.to("cuda")

optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)

start_epoch = 10
for epoch in range(start_epoch, config.epochs):
    train_one_epoch(...)
    validate(...)
    wandb.log({"epoch": epoch})
```

***

### Example: Adding Checkpointing to a Minimal `train.py`

Here is a working example using the simple training script from the Getting Started section.

This example simulates a checkpoint file (JSON), but the workflow is identical for real model weights.

```python theme={null}
import wandb
import time
import json
import os

# Initialize wandb
wandb.init(
    project="thunder-resnet",
    name="quick-test",
    config={
        "learning_rate": 0.001,
        "batch_size": 32,
        "epochs": 5,
    },
)

os.makedirs("checkpoints", exist_ok=True)

for epoch in range(5):
    # Simulate training metrics
    train_loss = 1.0 / (epoch + 1)
    train_acc = 0.5 + epoch * 0.1

    # Log metrics to wandb
    wandb.log({
        "epoch": epoch,
        "train/loss": train_loss,
        "train/accuracy": train_acc,
    })

    # ---- Checkpointing Example ----
    # In a real project this would be torch.save(model.state_dict(), ...)
    checkpoint_path = f"checkpoints/epoch_{epoch}.json"
    with open(checkpoint_path, "w") as f:
        json.dump({
            "epoch": epoch,
            "train_loss": train_loss,
            "train_accuracy": train_acc,
        }, f)

    # Log checkpoint as an artifact
    artifact = wandb.Artifact(
        name=f"quick-test-epoch-{epoch}",
        type="model",
        metadata={
            "epoch": epoch,
            "train_loss": train_loss,
            "train_accuracy": train_acc
        },
    )
    artifact.add_file(checkpoint_path)
    wandb.log_artifact(artifact)
    # --------------------------------

    time.sleep(0.5)

wandb.finish()
```

This example demonstrates:

* how checkpoint files are created
* how they are logged as Artifacts
* how each epoch becomes a tracked, versioned checkpoint

These appear in the **Artifacts** tab of your project.

***

### Quick Reference: Other Artifact Types

Artifacts aren't just for model checkpoints. You can also version datasets:

```python theme={null}
# Logging a Dataset
dataset = wandb.Artifact("imagenet-subset", type="dataset")
dataset.add_dir("data/imagenet_subset")
wandb.log_artifact(dataset)
```

***

## Hyperparameter Sweeps (Multi‑GPU, Multi‑Instance)

Sweeps allow large-scale hyperparameter search across many Thunder Compute instances.

### Step 1 — Create `sweep.yaml`

```yaml theme={null}
program: train.py
project: thunder-resnet
method: bayes

metric:
  name: val/accuracy
  goal: maximize

parameters:
  learning_rate:
    min: 0.00001
    max: 0.001
  batch_size:
    values: [32, 64, 128]
  weight_decay:
    min: 0.0
    max: 0.1
  augment:
    values: ["none", "light", "heavy"]
```

Output:

```
wandb: Creating sweep from: sweep.yaml
wandb: Creating sweep with ID: fgbkmk3q
wandb: View sweep at: https://wandb.ai/entity-name/thunder-resnet/sweeps/fgbkmk3q
wandb: Run sweep agent with: wandb agent entity-name/thunder-resnet/fgbkmk3q
```

### Step 2 — Initialize the sweep:

```bash theme={null}
wandb sweep sweep.yaml
```

### Step 3 — Run agents on Thunder GPU instances:

```bash theme={null}
wandb agent <entity>/<project>/<sweep_id>
```

Each agent pulls new hyperparameters and launches a run automatically.

***

## Distributed Training (DDP, Lightning, DeepSpeed)

### PyTorch DDP Example

```python theme={null}
wandb.init(
    project="thunder-ddp",
    group="llama7b-a100x4",
    job_type="training",
)
```

Set run names per rank:

```python theme={null}
wandb.run.name = f"gpu-{rank}"
```

### PyTorch Lightning Example

```python theme={null}
from lightning.pytorch import Trainer
from lightning.pytorch.loggers import WandbLogger

wandb_logger = WandbLogger(project="thunder-lightning-demo")

trainer = Trainer(
    logger=wandb_logger,
    accelerator="gpu",
    devices=4,
    strategy="ddp",
    max_epochs=50,
)

trainer.fit(model)
```

Lightning automatically:

* Logs metrics and gradients
* Tracks checkpoints
* Handles multi-GPU logging

***

## Offline Mode (Air‑Gapped or Firewalled Environments)

Thunder instances may have intermittent or restricted internet access.

### Run in offline mode:

```bash theme={null}
export WANDB_MODE=offline
python train.py
```

### Sync later:

```bash theme={null}
wandb sync /path/to/wandb/run-folder
```

### Fully disable wandb:

```bash theme={null}
export WANDB_MODE=disabled
```

***

## Best Practices for Thunder Compute GPU Instances

### Run Management

* Use meaningful run names that include dataset + model + GPU type
* Log all hyperparameters in `wandb.config`
* Track system metrics to diagnose bottlenecks
* Organize multi-GPU runs using `group`
* Reduce logging overhead by batching logs

### Artifacts & Checkpointing

* Use meaningful artifact names (e.g. `llama7b-a100-epoch20`)
* Attach useful metadata (epoch, val metrics, dataset version)
* Log fewer but higher-quality checkpoints
* Always use artifacts for long or expensive runs
* Use `use_artifact(...).download()` to restore weights anywhere
* Use artifacts for datasets and checkpoints

### Experimentation

* Use sweeps for expensive experiments
* Compare runs systematically using the dashboard
* Monitor GPU utilization to optimize batch sizes

***

## Troubleshooting

### Authentication Issues

```bash theme={null}
wandb login --relogin
```

### GPU Metrics Not Showing

* Ensure `nvidia-smi` works inside the environment
* Use GPU-enabled containers (`--gpus all`)
* Call `wandb.init()` early

### Connection Issues

* Verify outbound internet access
* Firewalls must allow connections to `*.wandb.ai`
* Use offline mode if required

### Large File Uploads

* Always use artifacts for multi-GB files
* Compress large checkpoints
* Prune old versions

***

## Need Help?

* W\&B Docs: [https://docs.wandb.ai](https://docs.wandb.ai)
* Thunder Compute Discord: [https://discord.com/invite/nwuETS9jJK](https://discord.com/invite/nwuETS9jJK)
* Email support: `support@thundercompute.com`


# Restrictions
Source: https://www.thundercompute.com/docs/restrictions

Usage restrictions, geographic availability, and prohibited activities on Thunder Compute

## Prohibited Activities

### Cryptocurrency Mining

Mining, staking, or otherwise interacting with cryptocurrency is strictly prohibited on Thunder Compute. If cryptocurrency-related activity is detected:

* The associated account is immediately banned
* Any billing credit is revoked
* The account is billed for the full amount of usage

## Geographic Availability

### B2B Requirements

Thunder Compute is only available for B2B customers and requires a VAT ID (or similar) in the following countries:

* United Arab Emirates
* Angola
* Bahrain
* Brazil
* Switzerland
* Côte d’Ivoire (Ivory Coast)
* Colombia
* Algeria
* Georgia
* Iraq
* Jordan
* Kazakhstan
* South Korea (Republic of Korea)
* Kuwait
* Morocco
* North Macedonia
* Oman
* Paraguay
* Qatar
* Saudi Arabia
* Tunisia
* Turkey (Türkiye)
* Tanzania
* Ukraine
* Uganda
* Uzbekistan
* Yemen
* India
* Moldova (Republic of Moldova)

### Restricted Countries

Thunder Compute is not currently available in the following countries:

* Belarus
* China
* Cuba
* Indonesia
* Iran
* Kenya
* North Korea
* Malaysia
* Mexico
* Nigeria
* Russia
* Sudan
* Syria
* Uruguay

If you're located in one of these countries and need access to Thunder Compute, please contact us to discuss potential alternatives.

## Usage Guidelines

### Acceptable Use

Thunder Compute instances are intended for legitimate computational workloads, particularly:

* AI/ML development and training
* Scientific computing
* Data processing and analysis
* Software development and testing

We have a strict one-account-per-user policy.

### Resource Usage

Users must comply with fair use policies and avoid activities that:

* Violate terms of service
* Engage in illegal or unethical activities

## Support

If you have questions about restrictions or need clarification on acceptable use, contact our support team.


# Troubleshooting
Source: https://www.thundercompute.com/docs/troubleshooting

Troubleshoot common Thunder Compute errors. Find solutions for connection issues, function errors, SSH problems, and access logs. Get support via Discord.

## Common solutions

1. Reconnect to the instance with `ctrl + d` and `tnr connect <instance_id>`
2. Upgrade tnr. Depending on your install method, you may have to use `pip install tnr --upgrade` or re-download the binary from the website
3. Back up any important data, then delete and recreate the instance.

## Common errors

### Function not implemented

A common error you may encounter is some variant of "This function is not implemented." What this means is that your program touches a portion of the CUDA API that we do not currently support. Check our [Prototyping vs Production](/prototyping-vs-production) guide for supported features, and if you encounter this, please contact us.

### SSH errors

If you encounter SSH-related errors (like `Error reading SSH protocol banner` or permission issues), first retry the command.

For quick fixes, back up critical data and recreate the instance. Instances cannot be stopped or restarted.

For persistent SSH issues, see our [SSH on Thunder Compute guide](/cli/operations/ssh) for alternative connection methods.

## Recommended Guides

To help prevent common issues and get the most out of Thunder Compute, we recommend these guides:

* [Using Docker](/guides/using-docker-on-thundercompute) - Learn about GPU-enabled containers and troubleshooting Docker issues
* [Using Instance Templates](/guides/using-instance-templates) - Use pre-configured environments to minimize setup issues

## Production mode as a last resort

If you continue to experience compatibility issues or errors that cannot be resolved through the above methods, consider switching to production mode by [modifying your existing instance](/vscode/operations/modifying-instances). Production mode provides maximum stability and reliability with all low-level optimizations disabled, ensuring complete compatibility for workloads that encounter persistent issues in the prototyping tier.

## Support

The fastest way to get support is to join [our discord](https://discord.com/invite/nwuETS9jJK). Our founding team will personally respond to help you as quickly as possible.


