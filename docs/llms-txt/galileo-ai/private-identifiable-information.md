# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-guardrail-metrics/private-identifiable-information.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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

<img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/pii-explanation.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=cbc738ba1f8e39ee1f4b5a2eac298083" alt="" data-og-width="1136" width="1136" data-og-height="366" height="366" data-path="images/pii-explanation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/pii-explanation.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=8a733a27809f713b56a9fd270566d281 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/pii-explanation.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=2e20fdd6e9c8c7bbac495d7bc9ebe402 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/pii-explanation.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=253c6477ca89b4fe793da31f5ba09764 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/pii-explanation.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=86c3502df391e16152bf467db703e150 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/pii-explanation.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=60d40a00a295d2cede1361ffee93125c 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/pii-explanation.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=40a550eb0ecff1cd4118186f1cdb886d 2500w" />
