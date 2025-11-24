# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/private-identifiable-information.md

# Private Identifiable Information

> Understand Galileo's PII Metric

***Definition:*** Identify PII spans within a sample (both input and output). The current model detects the following precisely defined categories:

* **Account Information**: Bank account numbers, Bank Identification Code (BIC) and International Bank Account Number (IBAN).

* **Address**: A physical address. Must contain at least a street name and number, and may contain extra elements such as city, zip code, state, etc.

* **Credit Card**: Credit card number (can be full or last 4 digits), Card Verification Value (CVV) and expiration date.

* **Date of Birth**: This represents the day, month and year a person was born. The context should make it clear that it's someone's birthdate.

* **Email**: An email address.

* **Name**: A person's full name. It must consist of at least a first and last name to be considered PII.

* **Network Information**: IPv4, IPv6 and MAC addresses.

* **Password**: A password.

* **Phone Number**: A phone number.

* **Social Security Number (SSN)**: A US Social Security Number.

* **Username**: A username.

***Calculation:*** We leverage a Small Language Model (SLM) trained on proprietary datasets.

***Usefulness:*** Automatically identify PII occurrences in any part of the workflow (user input, chains, model output, etc), and respond accordingly by implementing guardrails or other preventative measures.

**Explainability:** To highlight which parts of the text were detected as PII, click on the <Icon icon="eye" /> icon next to the PII metric value. The type of PII detected along with the model's confidence will be shown on the input or output text.

![](https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/pii-explanation.png)
