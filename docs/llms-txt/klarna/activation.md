# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/sap-commerce-cloud/payments/activation.md

# Activation of SAP Commerce Cloud Add-on

## This guide helps you activate Klarna Payments by setting up configurations and credentials in the SAP Commerce Backoffice.

### Prerequisites

Before you start, ensure:

- The `klarnapaymentaddon` is successfully installed.
- You have access to the SAP Commerce Backoffice.
- Credentials from the Klarna Merchant Portal, including **API username**, **API password**, and **Public Key ID**.

### Steps to Activate Klarna Payments

#### Step 1: Create a Klarna Payments configuration

**1.** Navigate to Klarna Payment Configuration: Go to **SAP Commerce Backoffice** → **Klarna** → **Klarna Payments Config**.


![Navigate to Klarna Payment Configuration](Activation_of_SAP_Commerce_Cloud_Add-on_1737037256971.png)
*Navigate to Klarna Payment Configuration*

**2.** Create a new Klarna configuration: Select the option to create a new Klarna configuration.


![Create a New Klarna Configuration](Activation_of_SAP_Commerce_Cloud_Add-on_1737037796619.png)
*Create a New Klarna Configuration*

**3.** Fill in mandatory fields:

- **Code:** A unique identifier for the configuration.
- **Enable Klarna Payments:** Toggle to enable the feature.
- **Email for Failure Notifications:** Email for receiving alerts.
- *Click **Next** to proceed.*


![Fill in the Klarna Payments Specific Fields](Activation_of_SAP_Commerce_Cloud_Add-on_1737037867953.png)
*Fill in the Klarna Payments Specific Fields*

**4.** Provide additional details:

- Enable **AutoCapture** (optional).
- Enable **Extra Merchant Data (EMD)** (optional).
- Set **Merchant Reference 2** and optional color customization for the Klarna interface.


![Fill in the Klarna Payments Specific Fields 2](Activation_of_SAP_Commerce_Cloud_Add-on_1737037970190.png)
*Fill in the Klarna Payments Specific Fields 2*

#### Step 2: Create credential data

**1. Navigate to Klarna Activation:** In the Backoffice, go to **Klarna** → **Klarna Activation**. **2. Add a new credential:** Click the **+** icon below the Klarna Activation section.


![Klarna Activation](Activation_of_SAP_Commerce_Cloud_Add-on_1737039726935.png)
*Klarna Activation*

**3. Fill in mandatory fields:**

- **Code:** Identifier for the credentials.
- **Client ID, API Username, and API Password:** Retrieved from the Klarna Merchant Portal.


![Create new credential](Activation_of_SAP_Commerce_Cloud_Add-on_1737040297543.png)
*Create new credential*

**4. Provide additional details:**

- Region (e.g., EUROPE, NORTH_AMERICA).
- Supported **Markets**.
- Enable **VCN** if applicable.
- **Public Key ID:** For encrypting VCN data.


![Credential additional details](Activation_of_SAP_Commerce_Cloud_Add-on_1737040358173.png)
*Credential additional details*

#### Step 3: Map credentials and Klarna Payments configuration

**1.** Navigate to Klarna Common Configuration: Go to **Klarna** → **Klarna Common Configuration**.


![Common Configuration](Activation_of_SAP_Commerce_Cloud_Add-on_1737040563865.png)
*Common Configuration*

**2.** Create a mapping:

- Click the **+** icon to create a new mapping.
- Fill in details such as **Code**, **Active**, and **Environment** (TEST or LIVE).


![Mapping credentials](Activation_of_SAP_Commerce_Cloud_Add-on_1737041144962.png)
*Mapping credentials*

**3.** Link Klarna credentials and payment configuration:

- Select the Klarna credentials created in Step 2.
- Associate the Klarna Payments configuration created in Step 1.


![Mapping details](Activation_of_SAP_Commerce_Cloud_Add-on_1737041223904.png)
*Mapping details*

### Klarna Payments Configuration Fields

| **Attribute** | **Mandatory** | **Description** |
|----|----|----|
| Klarna API Username | Yes | Generated in Klarna Merchant Portal. |
| Klarna API Password | Yes | Generated in Klarna Merchant Portal. |
| Region | Yes | Choose from EUROPE, NORTH_AMERICA, or OCEANIA. |
| Markets | Yes | Countries supported under the selected region. |
| Environment | Yes | TEST (playground) or LIVE (production). |
| AutoCapture | No | Enables auto capturing during order placement (not relevant if VCN is enabled). |
| Enable VCN | No | Toggles VCN-based settlement. |
| Public Key ID | No | RSA public key provided in JWK format for VCN settlement. Recommended: 4096-bit RSA keypair. |

**Tips for an Optimal User Experience** Ensure the Klarna Payments iframe is visible and text is legible by using a consistent minimum width for checkout and billing pages. This enhances the experience for mobile users.

### <span>Setting Up Virtual Card Numbers (VCN)</span>

#### Steps to Enable VCN

##### Step 1: Enable VCN in Klarna Configuration

1.  **Access Klarna Activation:**
    - Navigate to **SAP Commerce Backoffice** → **Klarna** → **Klarna Activation**.
2.  **Enable VCN:**
    - Select the **Enable VCN** option.

##### Step 2: Generate a 4096-bit RSA Key Pair

**1.** Open a terminal and run the following commands:

``` bash
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:4096
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

**2.** This will create two files:

- `private_key.pem` (Private key)
- `public_key.pem` (Public key)

##### Step 3: Configure Klarna with RSA Keys

1.  In **Klarna Activation**, set the **Public Key ID** using the contents of `public_key.pem`.
2.  Example `public_key.pem` file contents:

``` text
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAoNYG7l2G8nZa+22oBYZk
tV228lw3UE9WO4oxfknJtKEdHn84x55ULt8KQTh9NVtdeKC8nTfTgyvMt/GNCa18
xuZV/lGYDftKt85hbV5EjOum+StAIufEXvlBX7nMOMc1KyWm9kp2kbqd88mFIX63
KV94OoNEXcNatRDFYR+qz53+ifadDQtQ1slVNStdroCZDJ1+LxtBy9V+BdmsBK1E
RLsKh/JLXyWE24FJKV+z00s7TQkdWW/5ET12OGQYZsWo1yqgi9HplNvrisve8vWP
xaL4m8iZ3I/9yYdg7yANQbTxSJcbbRCgaaagPo30CNxeqU6qafY5g8vY3E52CoXH
DdO4UslX1qcuYIDhqaDzey6W+b8m755xLi+rqQyM4PBWL0J0dM3FVid8+4YKILex
3AKBFciqRCMHSOGaEeyrXKTjlAsghr9RS8PifvQRrL440cHzqw2vX0DvpjSWcmUJ
tW4wUq5RNSsobrxnVmoV6fj1z67Q/1P+l5Ie+oowdahR5ztVqJlO+2PNoX4I5VDs
/Pkz3f8wWVc3Mp2oNT244o+/NIiyRfPFaJJx7JAgrcvZt2nFAmY4QApXLFJCpgEM
wYucE4AH4gJKsh3KZbxRERrrO72bL2rxvWqBp/0h7DcMsV9sQs4BvxxIl6CF506F
ThzmclaKLBAyd5LALiXiPfkCAwEAAQ==
-----END PUBLIC KEY-----
```


![VCN](Activation_of_SAP_Commerce_Cloud_Add-on_1737040358173.png)
*VCN*

**<em>Important Notes on PCI Compliance</em>**

- **Do not save decrypted PCI data (e.g., VCN or CVV) on servers.**
- Ensure **PCI-DSS compliance** by securely handling card data.
- Collaborate with partners, Payment Service Providers (PSP), and Acquirers for secure data management.
- Delete any historical decrypted PCI data, regardless of its validity.

#### Verifying VCN Data in Backoffice

**1. Access the Order**

- Navigate to **Order** in the SAP Commerce Backoffice.
- Search for the specific order number.


![Verifying VCN in order](Activation_of_SAP_Commerce_Cloud_Add-on_1737044434610.png)
*Verifying VCN in order*

**2. View Order Details**

- Click the order number.
- Go to the **Payment & Delivery** section.
- Select **Payment Information** to view the VCN details.


![VCN Details](Activation_of_SAP_Commerce_Cloud_Add-on_1737044466859.png)
*VCN Details*
<em>Important!</em>

- VCNs are **one-time use cards** tied to individual orders.
- Merchants are responsible for securely managing the cards.
- Avoid storing decrypted PCI data in production environments.

### Verifying Klarna Order IDs in Backoffice

#### Steps to Verify Klarna Orders

1.  **Log in to SAP Commerce Backoffice.**
2.  **Navigate to Orders:**
    - Click **Orders** in the left-side menu.
3.  **Search for a Specific Order:**
    - Enter the order number in the search bar.
    - Open the order by clicking its entry in the results.

#### Viewing Klarna-Specific Details

**1. Verify Klarna Order ID:**

- Go to the **Properties** tab of the order.
- Locate and confirm the **Klarna Order ID**.


![Verify Klarna Order ID](Activation_of_SAP_Commerce_Cloud_Add-on_1737044767442.png)
*Verify Klarna Order ID*

**2. Check Payment Transactions:**

- Go to the **Administration** tab.


![Verify Payment Transactions](Activation_of_SAP_Commerce_Cloud_Add-on_1737044812412.png)
*Verify Payment Transactions*

- Look for the transaction type `KLARNA`*`ORDER_PLACED`* *to verify Klarna-specific transactions*


![KLARNA_ORDER_PLACE](Activation_of_SAP_Commerce_Cloud_Add-on_1737044884697.png)
*KLARNA_ORDER_PLACE*

### Configuring Extra Merchant Data (EMD)

The **Extra Merchant Data (EMD)** feature allows merchants to send additional customer information to Klarna, such as alternative delivery addresses and reservation details. By default, only logged-in customer information is sent.

#### Steps to Enable EMD in SAP Commerce Backoffice

1.  **Navigate to the Backoffice:**
    - Open **SAP Commerce Backoffice**.
    - Go to **Klarna** → **Klarna Payments Configuration**.
2.  **Enable the EMD Option:**
    - Locate the **Enable EMD** setting in the Klarna Payments configuration.
    - Toggle the option to enable it.


![Enable EMD](Activation_of_SAP_Commerce_Cloud_Add-on_1737045598452.png)
*Enable EMD*

#### Configuring EMD in Code

To extend the EMD functionality beyond the default behavior:

1.  **Open the KPCreditSessionPopulator.java File:** Locate the file in your SAP Commerce extension codebase.
2.  **Use the `addAttachment` Method:**
    - This method is exposed for configuring EMD data.
    - Replace `yourDataObject` with the required data (e.g., customer preferences or reservation details).
    - Example usage: `addAttachment("additionalData", yourDataObject);`
3.  **Compile and Deploy the Changes:** Build your extension and deploy it to the SAP Commerce environment.

**Best Practices for EMD and Order Verification**

- Use the **addAttachment** method to ensure relevant EMD fields are properly configured for Klarna Payments.
- Regularly monitor orders in Backoffice to ensure accurate mappings between Klarna and SAP Commerce configurations.

### Appendix

#### <span>Extension Model and Classes</span>

|  |  |  |
|----|----|----|
| **Model** | **OOB Model** | **Attributes** |
| BaseStore | BaseStore | klarnaPayConfig |
| AbstractOrder | AbstractOrder | kpIdentifier kpAnonymousGUID kpOrderId kpFraudStatus isKpPendingOrder isKpAuthorised isKpFraudRiskStopped |
| KPPaymentInfo | InvoicePaymentInfo | paymentOption finalizeRequired description authToken isVCNUsed vcnBrand vcnCSC vcnValidToYear vcnValidToMonth vcnHolder vcnPan vcnCVV |

##### <span>Classes extended from OOB SAP (Hybris) Commerce platform</span>

|  |  |
|----|----|
| **Class** | **OOB Class** |
| KPPaymentMethodCheckoutStepController | PaymentMethodCheckoutStepController |
| KPSummaryCheckoutStepController | AbstractCheckoutStepController |
| KlarnaResponsiveSummaryCheckoutStepValidator | AbstractCheckoutStepValidator |
| KlarnaSummaryCheckoutStepValidator | AbstractCheckoutStepValidator |
| KPAddressPopulator | AddressPopulator |
| KPOrderPopulator | AbstractOrderPopulator |
| KlarnaEventPublishingSubmitOrderStrategy | SubmitOrderStrategy |
| KPPaymentTypeCheckoutStepController | AbstractCheckoutStepController |

#### <span>Klarna Payment Method Reference</span>

|  |  |  |
|----|----|----|
| **Use Case** | **Class** | **Method** |
| Create/Update payment session | DefaultKPPaymentFacade | getORcreateORUpdateSession |
| Authorize Payment | DefaultKPPaymentFacade | getPaymentAuthorization |
| Create Klarna Order | DefaultKPPaymentCheckoutFacade | saveKlarnaOrderId |
| Cancel Klarna Order | KPOrderConfirmationController | orderConfirmation |

#### <span>KlarnapaymentAPI Method Reference</span>

|                            |           |                                    |
|----------------------------|-----------|------------------------------------|
| **Use Case**               | **Class** | **Method**                         |
| Get Klarna Payment session | Client    | newPaymentsSessionsApi             |
| Authorize Payment          | Client    | newPaymentsOrdersApi               |
| Get Klarna Order by ID     | Client    | newOrderManagementOrdersApi        |
| Create payment Settlement  | Client    | newVirtualCreditCardSettlementsApi |
| Delete Auth                |           | newPaymentsOrdersApi               |
| Capture Payment            |           | newOrderManagementCapturesApi      |