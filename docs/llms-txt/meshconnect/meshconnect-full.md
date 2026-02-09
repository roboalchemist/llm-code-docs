# Meshconnect Documentation

Source: https://docs.meshconnect.com/llms-full.txt

---

# Best UX Practices & Examples
Source: https://docs.meshconnect.com/advanced/best-ux-practices



Mesh provides a faster, safer, and more reliable way for users to move funds from exchanges and wallets directly into your platform. By replacing error-prone QR codes and manual address entry with a seamless, embedded flow, you can significantly increase conversion and user satisfaction.

**Key Advantages:**

* **Fast and Easy:** One-click payments and deposits from Binance, Coinbase, MetaMask, and 300+ other sources.
* **Error-Free:** Prevents wrong addresses, wrong networks, and address poisoning scams.
* **Higher Conversion:** Reduces user drop-off compared to manual flows.
* **Customer-Friendly:** A familiar, secure connection process, similar to linking an account with Plaid or PayPal.

***

### **Placement Best Practices**

How you present the Mesh option in your UI is critical for adoption.

* **Prioritize the Embedded Flow:** Place the "Pay with Crypto" or "Deposit with Crypto" button prominently in your checkout or wallet UI, above any manual QR code options.
* **Use QR Codes as a Backup:** Maintain the manual/QR code option as a secondary choice for users who prefer it.
* **Use Action-Oriented Labels:** Highlight Mesh as the recommended option with labels like **Smart Pay**, **Easy Deposit**, or **Instant Transfer**.
* **Lead with Trusted Brands:** Instead of "Pay with Mesh," use the logos of top exchanges and wallets your users trust, like Binance, Coinbase, and MetaMask.

***

### **The User Journey: A Phased Approach**

The goal is to move users from a simple first-time setup to a frictionless, one-click experience.

#### **1. First-Time User Experience (Smart Pay / Smart Deposit)**

For a new user connecting an account, the flow is simple and builds trust.

* The user selects "Pay with Crypto" or "Deposit from Exchange/Wallet."
* Mesh securely authenticates their account once.
* The user chooses an asset, previews the transaction, and confirms.

This is equivalent to adding a card to Apple Pay: a small, one-time setup that unlocks a seamless experience for all future use.

**📸 Example (Payment Use Case): A "Pay with Crypto" button in a checkout flow.**

<img alt="Pay With Crypto Pn" title="Pay With Crypto Pn" />

**📸 Example (Deposit Use Case): "Deposit from Wallet" with trusted brand options.**

<img alt="deposit" />

<img alt="deposit1" />

<img alt="deposit2" />

#### **2. Returning User Experience (Easy Pay / Easy Deposit)**

This is where the power of Mesh becomes clear. Once an account is connected, returning users get a one-click experience.

* You use the stored `auth_token` to initialize Mesh.
* The user is taken **directly to the confirmation screen**, skipping the login steps.
* You can create dedicated, personalized buttons like **"Pay with your Binance account"** or **"Deposit from MetaMask."**

**📸 Example: A personalized deposit button for a return user.**

<img alt="returnUserDeposit" />

#### **3. Power User Experience (Fast Pay / Fast Deposit)**

For frequent users, you can create an even faster flow by pre-selecting the token and network.

* The `linkToken` is configured with a single, pre-defined asset.
* The user is taken directly into the transfer flow, bypassing all selection steps.
* This is ideal for high-frequency use cases like iGaming platforms.

<img alt="FastDeposit" title="" />

***

### **Key Feature for Payments: SmartFunding**

For all use cases, enabling SmartFunding is the most effective way to maximize conversion.

* **What it is:** SmartFunding allows users to complete a payment even if they don't have enough of the required token by **auto-converting** their other assets in the background.
* **Why it's critical for payments:** It prevents transaction failures due to insufficient funds of a specific asset, turning a potential "failed payment" into a successful one.

***

### **Technical Integration Tips**

* **Token Management:** Always store and refresh the user's `auth_token` to enable the "Easy Pay/Deposit" return user experience.
* \*\*Use \*\*`integrationId`**s:** Deep-link directly to specific providers (e.g., Binance, Coinbase) to create shortcuts in your UI.
* **Support Multi-Asset Arrays:** In your `linkToken` request, pass an array of all the tokens/networks you support to give users maximum flexibility.

***

### **Business Impact**

By adopting this UX strategy, our partners see measurable improvements:

* **Higher Conversion Rates (20-30% lift):** Users complete payments and deposits more often.
* **Increased Volume:** Faster flows encourage more frequent and larger transactions.
* **Reduced Support Tickets:** Eliminates user errors like sending to the wrong address or network.
* **Stronger Retention (2-6x repeat conversions):** Account-linked flows keep users engaged on your platform.


# Configuring Transfer Options
Source: https://docs.meshconnect.com/advanced/configuring-transfer-options



The `transferOptions` object is the core of any payment or deposit flow in Mesh. By passing this object in your server-side `POST /api/v1/linktoken` request, you can precisely control the user's experience in the Link UI, from the assets they can transfer to the fees they are charged.

# Core Components of `transferOptions`

| Parameter        | Type   | Description                                                                           |
| :--------------- | :----- | :------------------------------------------------------------------------------------ |
| `toAddresses`    | Array  | **Required.** An array of objects defining the destination for the funds.             |
| `transferType`   | String | The type of transfer, either `payment` or `deposit`.                                  |
| `fundingOptions` | Object | An object to enable features like SmartFunding.                                       |
| `transactionId`  | String | A unique identifier for the transaction from your system, crucial for reconciliation. |
| `ClientFee`      | Number | A decimal representing a fee you can add to the transaction (e.g., `0.025` for 2.5%). |

***

# **`Configuring Destination Addresses (toAddresses)`**

The `toAddresses` array is the most critical part of the configuration. Each object in this array defines a specific asset, network, and destination address.

* **Key Requirement:** You must use the Mesh-specific Unique Identifier (`NetworkId`) for each network. You can find these by calling the `GET /api/v1/transfers/managed/networks` endpoint.

# **Single Address (Streamlined UX)**

Providing a single object in the `toAddresses` array creates the most direct user experience. The Link UI will skip the asset and network selection screens, taking the user directly to the amount and confirmation steps.

**Example:**

```
"transferOptions": {
  "toAddresses": [
    {
      "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
      "symbol": "ETH",
      "address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"
    }
  ]
}
```

# **Multiple Addresses (Flexibility)**

To give your users more choice, you can provide an array with multiple destination objects. This will allow the user to select their preferred asset and network within the Link UI.

**Example:**

```
"transferOptions": {
  "toAddresses": [
    {
      "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
      "symbol": "ETH",
      "address": "0xYourAddress..."
    },
    {
      "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
      "symbol": "USDC",
      "address": "0xYourAddress..."
    },
    {
      "networkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
      "symbol": "MATIC",
      "address": "0xYourAddress..."
    }
  ]
}
```

***

# **Configuring a Specific Amount**

For payment use cases, you can pre-fill the amount the user needs to send.

* **Amount in Crypto:** To specify an amount in a specific cryptocurrency, add the `Amount` key to an object within the `toAddresses` array.
* **Amount in Fiat:** To specify an amount in fiat (e.g., USD) that will be converted to the crypto equivalent at the time of the transaction, add the `AmountInFiat` key directly within the `transferOptions` object.

**`Example (AmountInFiat):`**

```
"transferOptions": {
  "toAddresses": [
    {
      "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
      "symbol": "ETH",
      "address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"
    }
  ],
  "AmountInFiat": 10,
  "TransactionId": "YOUR_UNIQUE_TRANSACTION_ID"
}
```

***

# **Enabling SmartFunding**

To maximize conversion, we strongly recommend enabling SmartFunding. This allows users to complete a payment even if they don't have enough of the required asset by auto-converting their other tokens.

* **How to Enable:** Set `enabled: true` within the `fundingOptions` object.

**Example:**

```
"transferOptions": {
  "toAddresses": [ /* ... */ ],
  "AmountInFiat": 10,
  "fundingOptions": {
    "enabled": true
  }
}
```


# Intelligent Provider Filtering in Mesh Link
Source: https://docs.meshconnect.com/advanced/intelligent-provider-filtering



Mesh automatically applies intelligent filtering during Link initialization to ensure users only see compatible, compliant, and viable providers (wallets, exchanges, brokers). This improves success rates, avoids regulatory blockers, and enhances user experience.

Below is a complete breakdown of the filters we apply, categorized by use case and user type.

## **1. Token & Network Compatibility**

**Applies to: All clients**

Mesh only displays providers that support the exact asset and network combination requested in the transfer.

**How it works:**

* If a user selects USDC on Solana, only providers that support USDC *on Solana* will be shown.
* If the selected token or network is not supported by a provider, that provider is excluded.

**Why this matters:**

Prevents failed transfers due to unsupported configurations and ensures a seamless experience.

## **2. Travel Rule Filters – VASP ID Requirement**

**Applies to: Custodial platforms (e.g. neobanks, exchanges, fintechs)**

In certain jurisdictions, Coinbase requires the sending platform to provide a valid **VASP ID**. If Mesh does not have a VASP ID on file for your client and the user is in a restricted country, **Coinbase will not appear**.

**Countries affected:**

AE, AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IS, IT, JE, KR, LI, LT, LU, LV, MT, NL, NO, NZ, PL, PT, RO, SE, SG, SI, SK

**Logic:**

* IP address is in an affected country
* Mesh does not have a VASP ID for your client

  → Coinbase is excluded from the provider list

## **3. Travel Rule Filters – Wallet Ownership Verification**

**Applies to: Self-custody wallets (e.g. MetaMask, Zengo, Trust Wallet)**

When a user is connecting via a self-hosted wallet, Coinbase enforces wallet ownership verification in certain jurisdictions. Because self-custody wallets cannot provide ownership proof, Mesh filters Coinbase out in these scenarios.

**Logic:**

* If the **transfer amount exceeds 1000 EUR** and the user's IP is in one of the following countries, Coinbase will **not be shown**: **AE, AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IS, IT, JE, KR, LI, LT, LU, LV, MT, NL, NO, NZ, PL, PT, RO, SE, SG, SI, SK**
* If the user's IP is in one of the following **Southeast and East Asian countries**, Coinbase will also be **filtered regardless of amount**: **SG (Singapore), HK (Hong Kong), PH (Philippines), KR (South Korea)**

This enforcement is based on Coinbase's jurisdiction-specific compliance policies and is dynamically applied by Mesh at runtime.

## **4. Travel Rule Filters – Use Case Restrictions**

**Applies to: Gaming platforms using custodial or exchange accounts**

Some providers restrict transfers based on the **type of platform** initiating the request.

**Example:**

* **Binance (Japan):** Does not allow Japanese accounts to transfer to gaming platforms.

  → If a user is on a gaming platform and their IP is in Japan, Binance will not be shown.

Mesh applies this logic automatically when the client metadata indicates the platform is categorized as “gaming.”

## **5. Broker Geography Restrictions**

**Applies to: All clients**

Mesh enforces IP-based restrictions at the provider level to reflect each broker’s supported regions.

**Rules:**

* **Binance:** Not shown to users with IPs in **US, Canada, or Netherlands**
* **Robinhood:** Only shown to users with **US IPs**; filtered out otherwise

These rules are enforced directly based on provider policies and automatically reflected in the Link session.

## **Summary**

| **Filter Type**             | **Applies To**       | **Example Outcome**                               |
| --------------------------- | -------------------- | ------------------------------------------------- |
| Token/Network Compatibility | All clients          | Only show providers that support USDT on Arbitrum |
| Coinbase VASP ID            | Custodial clients    | Coinbase not shown if no VASP ID for client in DE |
| Coinbase Wallet Ownership   | Self-custody wallets | Coinbase hidden for >1000 EUR from FR via Zengo   |
| Broker Geography            | All clients          | Binance not shown to user in US                   |
| Use Case Travel Rule        | Gaming platforms     | Binance filtered for JP IPs on gaming platform    |

If you need help validating provider coverage for specific asset/network combinations or regions, please reach out to your Mesh account manager or visit the [Mesh Developer Docs](https://docs.meshconnect.com/).


# Enabling Multi-Language Support for Link
Source: https://docs.meshconnect.com/advanced/language

This guide explains how to configure Mesh Link to support multiple languages, allowing you to provide a localized experience for your users.

This guide explains how to configure Mesh Link to support multiple languages, allowing you to provide a localized experience for your users.

# Understanding Language Configuration with `language`

The `language` parameter, which you set during Mesh Link initialization, is the key to displaying Link in your user's preferred language. This parameter allows you to:

* **Automatically match the user's device/browser language**, or
* **Specify a particular language.**

# Key Parameter: `language`

You'll use the `language` parameter when initializing Mesh Link via your SDK (Web, iOS, Android, or React Native).

## **Possible Values:**

* **`<BCP 47 code>`**: A specific language code enumerated as the 2 digit language identifier (eg. “**`fr-`**” for French) and the 2 digit region identifier (eg. “**`-CA`**” for Canada), combined as “**`fr-CA`**".  Alternatively, the SDK will accept an input of only the language (eg. “**`fr`**”).
* If the indicated language (eg. “**`fr-`**”) is followed by a region code (eg. “**`-CA`**”) that is not recognized or supported for that language, Link will fall back to the default translation for that language, if available (eg. “**`fr-FR`**”). If no translation for the language is available, Link will default to "**`en-US`**" (English, US).
* If you do not provide a value for the parameter, or if you provide a value for a language that is not supported, Link will default to "**`en-US`**" (English, US).
* **`system`**: Link will detect the default language on the user’s browser and/or device and display Link in that language. If it is an unsupported value, it will fallback to another locale for that language, or it will fallback to the global default of **`en-US`**.

# Implementation

## **Initialize Link with `language`**

When you initialize Link in your application, use the **`language`** parameter to specify the desired language behavior.

### **Web SDK**

```jsx theme={null}
const connection = createLink({
        ...
        language: 'en-US'
        ...
      })
```

### **Android SDK**

```kotlin theme={null}
val configuration = LinkConfiguration(
    token = "linkToken",
    language = "en-US")
```

### **iOS SDK**

```swift theme={null}
let settings = LinkSettings(language: "en-US")
let configuration = LinkConfiguration(
    linkToken: linkToken,
    settings: settings,
    ...
    )
```

### **React native SDK**

```jsx theme={null}
<LinkConnect settings={{language: 'en-US'}} ... />
```

# Testing Your Implementation

Thoroughly test your implementation to ensure a seamless experience for your users:

* Verify that Link displays correctly in the languages you intend to support.
* Please notify your Mesh support person if you see any words or phrases that you believe are incorrectly translated if you see any layout issues (for example with right-to-left languages or character-based languages).

# Currently supported languages

<aside>
  🤝🏽

  **If you need a language that is not shown as supported below, please notify your Mesh team member to request it be added.**
</aside>

| **Status**               | **Language**                   | **Region**                                    | **Locale code** |
| ------------------------ | ------------------------------ | --------------------------------------------- | --------------- |
| <span>**live**</span>    | English                        | United States <span>**global default**</span> | **`en-US`**     |
| <span>**live**</span>    | Spanish                        | United States <span>**es default**</span>     | **`es-US`**     |
| <span>**live**</span>    | Russian                        | Russia                                        | **`ru-RU`**     |
| <span>**live**</span>    | French                         | France <span>**fr default**</span>            | **`fr-FR`**     |
| <span>**live**</span>    | Chinese/Mandarin (Simplified)  | China <span>**zh default**</span>             | **`zh-CN`**     |
| <span>**live**</span>    | Turkish                        | Turkey                                        | **`tr-TR`**     |
| <span>**live**</span>    | Polish                         | Poland                                        | **`pl-PL`**     |
| <span>**live**</span>    | Japanese                       | Japan                                         | **`ja-JP`**     |
| <span>**live**</span>    | German                         | Germany                                       | **`de-DE`**     |
| <span>**live**</span>    | Finnish                        | Finland                                       | **`fi-FI`**     |
| <span>**live**</span>    | Hindi                          | India                                         | **`hi-IN`**     |
| <span>**live**</span>    | Portuguese                     | Portugal <span>**pt default**</span>          | **`pt-PT`**     |
| <span>**live**</span>    | Vietnamese                     | Vietnam                                       | **`vi-VN`**     |
| <span>**live**</span>    | system                         |                                               | **`system`**    |
| <span>**backlog**</span> | Arabic                         | Egypt                                         | **`ar-EG`**     |
| <span>**backlog**</span> | Chinese/Mandarin (Traditional) | United States                                 | **`zh-US`**     |
| <span>**backlog**</span> | Chinese                        | Hong Kong                                     | **`zh-HK`**     |
| <span>**backlog**</span> | Chinese                        | Taiwan                                        | **`zh-TW`**     |
| <span>**backlog**</span> | Czech                          | Czech Republic                                | **`cs-CZ`**     |
| <span>**backlog**</span> | Danish                         | Denmark                                       | **`da-DK`**     |
| <span>**backlog**</span> | Dutch, Flemish                 | Belgium                                       | **`nl-NL`**     |
| <span>**backlog**</span> | English                        | Australia                                     | **`en-AU`**     |
| <span>**backlog**</span> | English                        | India                                         | **`en-IN`**     |
| <span>**backlog**</span> | English                        | United Kingdom                                | **`en-GB`**     |
| <span>**backlog**</span> | French                         | Canada                                        | **`fr-CA`**     |
| <span>**backlog**</span> | Greek, Modern (1453–)          | Greece                                        | **`el-GR`**     |
| <span>**backlog**</span> | Hebrew                         | Israel                                        | **`he-IL`**     |
| <span>**backlog**</span> | Hungarian                      | Hungary                                       | **`hu-HU`**     |
| <span>**backlog**</span> | Indonesian                     | Indonesia                                     | **`id-ID`**     |
| <span>**backlog**</span> | Italian                        | Italy                                         | **`it-IT`**     |
| <span>**backlog**</span> | Korean                         | South Korea                                   | **`ko-KR`**     |
| <span>**backlog**</span> | Norwegian                      | Norway                                        | **`no-NO`**     |
| <span>**backlog**</span> | Portuguese                     | Brazil                                        | **`pt-BR`**     |
| <span>**backlog**</span> | Slovak                         | Slovakia                                      | **`sk-SK`**     |
| <span>**backlog**</span> | Spanish, Castilian             | Spain                                         | **`es-ES`**     |
| <span>**backlog**</span> | Swedish                        | Sweden                                        | **`sv-SE`**     |
| <span>**backlog**</span> | Thai                           | Thailand                                      | **`th-TH`**     |


# Mesh Link SDK Events
Source: https://docs.meshconnect.com/advanced/link-ui-events



## Overview

Mesh Link UI offers an event tracking system, allowing you to gain insights into user interactions within the Link UI. These events can be used for analytics and understanding user behavior. The event data can be obtained directly from the SDKs and includes various user actions, such as initiating a connection, completing authentication, completing an asset transfer, or encountering errors.

The way in which these events are captured and transmitted varies slightly across different platforms (Web, iOS, Android, and React Native). For detailed instructions, see the page for your specific platform.

# SDK Callback Functions

| **SDK callback function**      | **Description of callback function**                                                                                                                                                                                                                                     | **Payload details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`onIntegrationConnected()`** | A callback function that allows you (Mesh client) to run specific business logic when the user has successfully completed connecting an account.                                                                                                                         | • **`accessToken`**: the access and refresh tokens to the connected account with some basic metadata about the account and tokens.<br />• **`brokerBrandInfo`**: links to icons and logos for the connected integration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **`onTransferFinished()`**     | A callback function that allows you (Mesh client) to run specific business logic when the user has  successfully completed a transfer.                                                                                                                                   | • **`status`**: pending / succeeded / failed<br />• **`txId`**: A unique client identifier<br />• **`transferId`**: A unique Mesh identifier<br />• **`txHash?`**: A unique blockchain identifier<br />• **`fromAddress`**: Address transfer is sent from<br />• **`toAddress`**: Address transfer is sent to<br />• **`symbol`**: Symbol of asset being transferred<br />• **`amount`**: Amount being transferred<br />• **`amountInFiat`**: Fiat equivalent of transfer amount<br />• **`totalAmountInFiat`**: Total amount transferred, including transfer-related fees<br />• **`networkId`**: Selected network identifier<br />• **`networkName`**: Selected network name<br />• **`refundAddress`**: The address that the user can receive back to |
| **`onExit()`**                 | A callback function that allows you (Mesh client) to run specific business logic when the user has exited Link at some point.                                                                                                                                            | • **`errorMessage`**: Descriptive error message, if applicable<br />• **`summary`**: // optional<br />• **`page`**: the page the user was on when they exited<br />• **`selectedIntegration`**: Name and Id of integration<br />• **`transfer`**: previewId and other details about the transfer preview                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **`onEvent()`**                | A general callback function that allows you (Mesh client) to run specific business logic in more granular scenarios, like when the user exits Link from specific parts in the user journey.<br />The events that can be used in this callback function are listed below. | Different payload structure for different events                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

# SDK Events

| **SDK Event Type**                        | **Description of Occurrence**                                                                                                                                                                                                                                   | **Payload Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`pageLoaded`**                          | Triggered when the first page is fully loaded. The first page the user sees may differ based on use case.                                                                                                                                                       | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`methodSelected`**                      | Triggered on HomePage when the user selects a particular method for their flow.                                                                                                                                                                                 | • **`method`**: The selected method type ('embedded' / 'manual' / 'buy')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **`close`**                               | Triggered when the user exits the Mesh Link modal.                                                                                                                                                                                                              | • **`page`**: the page the user was on when they exited.<br />• Note: In the context of a transfer flow, `page: 'transferExecutedPage'` would indicate the full flow was successful because the user exited from the Success page. And if the page is anything else, then the flow was not successfully completed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **`integrationSelected`**                 | Triggered when a user selects an integration from the catalog list.                                                                                                                                                                                             | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• **`userSearched?`**: true/false if the user searched selected this integration from search results or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **`legalTermsViewed`**                    | Triggered if a user views the terms of use page in Link.                                                                                                                                                                                                        | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`credentialsEntered`**                  | Triggered when a user submits exchange login credentials.                                                                                                                                                                                                       | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`integrationMfaRequired`**              | Triggered when the user is prompted to enter MFA in an exchange authentication flow.                                                                                                                                                                            | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`integrationMfaEntered`**               | Triggered when the user enters their MFA code in an exchange authentication flow.                                                                                                                                                                               | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`integrationOAuthStarted`**             | Triggered when an exchange’s OAuth window is launched in authentication flow.                                                                                                                                                                                   | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`integrationAccountSelectionRequired`** | Triggered if user is prompted to select a specific account within linked exchange.                                                                                                                                                                              | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`integrationConnected`**                | Triggered when a user successfully connects to an integration.                                                                                                                                                                                                  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• \*\*`accessToken`\*\*payload: The access token to the user account and relevant metadata about the integration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **`integrationConnectionError`**          | Triggered when there is an error in connecting to an integration.                                                                                                                                                                                               | • **`errorMessage`**: Descriptive error message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **`transferStarted`**                     | Triggered when the user begins the transfer flow. This means they have successfully connected an account and have moved on to either configuring or previewing their transfer. It does NOT mean they have initiated a transfer of assets.                       | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **`transferAssetSelected`**               | Triggered when the user selects an asset to transfer. This does not relate to assets used for funding operations. This is about the asset being transferred.                                                                                                    | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• **`symbol`**: Currency symbol                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **`transferNetworkSelected`**             | Triggered when the user selects a network to transfer on.                                                                                                                                                                                                       | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• **`symbol`**: Currency symbol<br />• **`networkId`**: Selected network identifier<br />• **`networkName`**: Selected network name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **`transferAmountEntered`**               | Triggered when the user enters an amount to transfer.                                                                                                                                                                                                           | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• **`symbol`**: Currency symbol<br />• **`networkId`**: Selected network identifier<br />• **`networkName`**: Selected network name<br />• **`amount`**: Amount the user enters for transfer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **`transferNoEligibleAssets`**            | Triggered when there are no assets in the user’s account eligible for the transfer, or Mesh cannot use the assets in the account to fund the transfer.                                                                                                          | • **`arrayOfTokensHeld`**: A list of tokens held in the user’s account<br />   • **`symbol`**: Currency symbol<br />   • **`amount`**: Amount of holding<br />   • **`amountInFiat`**: Amount of holding in fiat<br />   • **`ineligibilityReason`**: Why the token is ineligible.<br />• **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• **`noAssetsType`**:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **`transferConfigureError`**              | This may happen if the session linkToken expires during the configuration flow of a transfer. Very rare.                                                                                                                                                        | • **`errorMessage`**: Descriptive error message.<br />• **`requestId`**:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **`transferPreviewed`**                   | Triggered when a user previews the details of a pending transfer.                                                                                                                                                                                               | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• **`symbol`**: Currency symbol<br />• **`networkId`**: Selected network identifier<br />• **`networkName`**: Selected network name<br />• **`amount`**: Crypto amount of the transfer<br />• **`amountInFiat`** (optional): Amount in fiat currency<br />• **`fiatCurrency`**: fiat currency symbol for the **`amountInFiat`** value.<br />• **`toAddress`**: Destination address<br />• **`fees`**:<br />    • `institutionTransferFee`<br />    • `estimatedNetworkGasFee`<br />    • `customClientFee`<br />• **`fiatPurchaseStrategy`**: an enumeration of a fiat funding option used to fund this transaction plus any applicable `tradingFee`.<br />• **`cryptocurrencyFundingOptionType`**: an enumeration of any funding options used to fund this transactionplus any applicable `cryptocurrencyConversionFee` or `depositFee`.<br />• **`previewId`**: Unique ID for the preview |
| **`transferPreviewError`**                | Triggered when there is an error in building a transfer preview.                                                                                                                                                                                                | • **`errorMessage`**: Descriptive error message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **`linkTransferQRGenerated`**             | Triggered when the user lands on the Manual QR screen.                                                                                                                                                                                                          | • **`token`** (optional): Token symbol for the transfer<br />• **`network`** (optional): Network being used<br />• **`toAddress`** (optional): Destination address<br />• **`qrUrl`** (optional): Generated QR code URL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **`fundingOptionsViewed`**                | Triggered when the user views the funding options page.                                                                                                                                                                                                         | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`fundingOptionsUpdated`**               | Triggered when the user makes updates to the selected funding options and clicks save (ie. saves a new funding strategy).                                                                                                                                       | No additional payload. When a user saves a new funding strategy, it would build a new Preview, which would fire a new **`transferPreviewed`** event with new funding options enumerated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **`transferInitiated`**                   | Triggered when the user clicks to Proceed from the Preview screen. This will send a request to transfer to the exchange or wallet, which the user then needs to approve (via 2FA for exchange, or signing for wallet).                                          | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• **`symbol`**: Currency symbol<br />• **`networkId`**: Selected network identifier<br />• **`networkName`**: Selected network name<br />• **`amount`**: Crypto amount of the transfer<br />• **`amountInFiat`** (optional): Amount in fiat currency<br />• **`fiatCurrency`**: fiat currency symbol for the **`amountInFiat`** value.<br />• **`toAddress`**: Destination address<br />• **`fees`**:<br />    • `institutionTransferFee`<br />    • `estimatedNetworkGasFee`<br />    • `customClientFee`<br />• **`fiatPurchaseStrategy`**: an enumeration of a fiat funding option used to fund this transaction plus any applicable `tradingFee`.<br />• **`cryptocurrencyFundingOptionType`**: an enumeration of any funding options used to fund this transactionplus any applicable `cryptocurrencyConversionFee` or `depositFee`.                                                   |
| **`executeFundingStep`**                  | Triggered when there is a success or error on a funding operation before a transfer.                                                                                                                                                                            | • **`fundingOptionType`**: The operation that has completed or failed.<br />• **`status`**: Outcome of the funding operation.<br />• **`errorMessage`**: Descriptive error message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **`gasIncreaseWarning`**                  | Triggered after funding operations and before initiation of transfer if the cost of gas has gone higher than the buffered estimate shown to the user on the Preview page.                                                                                       | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`transferMfaRequired`**                 | Triggered when the user is prompted to enter an MFA code to perform an exchange transfer.                                                                                                                                                                       | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`transferMfaEntered`**                  | Triggered when the user submits their MFA code to perform an exchange transfer.                                                                                                                                                                                 | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`transferKycRequired`**                 | Triggered when the user has not completed KYC in the linked account, is prompted to do so before being able to transfer assets.                                                                                                                                 | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`transferExecuted`**                    | Do not use. Obsolete.                                                                                                                                                                                                                                           | Do not use. Obsolete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **`transferCompleted`**                   | Triggered when the user views the Success page at the conclusion of the transfer flow.<br />It is recommended to use the **`onTransferFinished()`** callback function to properly handle the user experience returning to your app after a successful transfer. | **`transferFinished`** payload:<br />• **`status`**: pending / succeeded / failed<br />• **`txId`**: A unique client identifier<br />• **`transferId`**: A unique Mesh identifier<br />• **`txHash?`**: A unique blockchain identifier<br />• **`fromAddress`**: Address transfer is sent from<br />• **`toAddress`**: Address transfer is sent to<br />• **`symbol`**: Symbol of asset being transferred<br />• **`amount`**: Amount being transferred<br />• **`amountInFiat`**: Fiat equivalent of transfer amount<br />• **`totalAmountInFiat`**: Total amount transferred, including transfer-related fees<br />• **`networkId`**: Selected network identifier<br />• **`networkName`**: Selected network name<br />• **`refundAddress`**: The address that the user can receive back to                                                                                                                                                                                                                                                                             |
| **`transferExecutionError`**              | Triggered when there is an error in executing a transfer.                                                                                                                                                                                                       | • **`errorMessage`**: Descriptive error message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **`seeWhatHappenedClicked`**              | Triggered when the user clicks the See what happened link on the Transfer Success screen                                                                                                                                                                        | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`connectionUnavailable`**               | Triggered when a timeout occurs when attempting to open a wallet on mobile, most likely because the DeFi wallet app is not installed on the device.                                                                                                             | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• **`reason`**: string                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **`connectionDeclined`**                  | Triggered when the user rejects a connection request in their wallet, or some error causes an auto-rejection.                                                                                                                                                   | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• **`reason`**: string.<br />• **`networkId`**: Selected network identifier<br />• **`networkName`**: Selected network name<br />• **`toAddress`**: Address transfer is sent to.<br />• **`errorMessage`**: Descriptive error message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **`transferDeclined`**                    | Triggered when the user rejects the transfer request in their wallet, or some error causes an auto-rejection.                                                                                                                                                   | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.<br />• **`integrationName`**: Name of the selected integration.<br />• **`reason`**: string<br />• **`networkId`**: Selected network identifier<br />• **`networkName`**: Selected network name<br />• **`toAddress`**: Address transfer is sent to<br />• **`symbol`**: Symbol of asset being transferred<br />• **`amount`**: Amount being transferred<br />• **`status`**: pending / succeeded / failed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **`walletMessageSigned`**                 | Triggered when a user signs a message in their wallet to verify ownership.                                                                                                                                                                                      | • **`address`**: wallet address that signed the message<br />• **`isVerified`**: true / false indicator of whether the user has signed the exact message sent for signature from this address<br />• **`message`**: Message that was signed<br />• **`signedMessageHash`**: The hash of the message signed by the wallet<br />• **`timeStamp`**: Time stamp of when the signature happened                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **`verifyDonePage`**                      | Triggered when the user views the Success page after successfully completing the wallet verification flow.                                                                                                                                                      | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`verifyWalletRejected`**                | Triggered when the user rejects the message signature request in their wallet, or some error causes an auto-rejection.                                                                                                                                          | No additional payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **`done`**                                | Triggered when the user exits Link after successfully completing a read-only account connection flow (ie. for Mesh Verify) or after successfully completing the wallet verification flow (ie. for Mesh Verify).                                                 | • **`page`**: the page the user was on when they exited.<br />• Note: In wallet verification (ie. Mesh Verify) flow, `page: verifyDonePage` would indicate successful completion of the flow. And in a read-only (ie Mesh Portfolio) flow, `page: integrationConnectedPage` would indicate successful completion of the flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **`registerTransferError`**               | Shown when we are unable to receive the transfer hash from a self-custody wallet at the conclusion of a transfer flow.                                                                                                                                          | • **`errorMessage`**: Descriptive error message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |


# Mesh Managed Tokens (MMT)
Source: https://docs.meshconnect.com/advanced/mesh-managed-tokens

This guide explains how to implement Mesh Managed Tokens (MMT), our recommended approach for handling user authentication to create a secure and seamless return user experience.

# Overview

Mesh’s Managed Tokens system (MMT) is a service designed to simplify how clients manage user authentication tokens. Rather than requiring clients to handle the lifecycle of access and refresh tokens for each integration, MMT securely stores and manages tokens on behalf of the client. Clients receive a persistent `TokenId` that can be used to interact with exchange brokers via Mesh APIs without needing to refresh or re-authenticate.

***

## Benefits

* **Simplified Token Lifecycle**: Clients do not need to handle the storage or refresh logic for tokens directly.
* **Streamlined UX**: End-users can skip repetitive authentication steps, enhancing the embedded experience.
* **Persistent Access** (where supported): For broker integrations that provide long-lived or refreshable tokens (e.g., Coinbase), the same `TokenId` remains valid indefinitely. For integrations with expiring tokens (e.g., Binance), users may still need to re-authenticate, but the `TokenId` remains unchanged, allowing clients to reuse it without needing to update backend storage.
* **Seamless Re-authentication**: When a token expires (e.g., Binance), Mesh Link will prompt the user to re-authenticate. Once complete, the same `TokenId` is revalidated and continues to work as before—reducing backend complexity for clients.
* **Integration-Agnostic**: Works across different auth methods (OAuth, credentials-based) with no added client-side complexity.

***

## Security Considerations

While MMT streamlines token handling and unlocks powerful functionality, it also requires thoughtful security practices given its expanded role in managing user access. Mesh has designed the system with robust safeguards to ensure token integrity and data protection, including:

* **Encrypted Storage**: All tokens are encrypted at rest using modern encryption standards.
* **Scoped Access**: Each `TokenId` is tied to the permission scope (read or write) associated with the API key. Unauthorized operations (e.g., calling a write endpoint with a read-scoped token) will be rejected.
* **Client-Level Isolation**: Each `TokenId` is also scoped to a specific `clientId`. Even if the same end user connects the same integration account across multiple client apps, the tokens are isolated and not shared across clients.
* **User-Level Isolation**: Each `TokenId` is unique to a specific `EndUserId` and integration.
* **Token Revocation**: Clients can revoke a `TokenId`, permanently disabling access and triggering a secure deletion process. There is no path to restore a revoked token.

***

# How to Implement MMT

## 1. Enable Token Management for Your Client

Ensure MMT is enabled for your `clientId` by contacting your Mesh Customer Success representative.

Once enabled, all authentication flows will return a `TokenId` in place of a raw access token.

***

## 2. Obtain a `TokenId`

When a user authenticates with their exchange or wallet account, you will receive the SDK event `integrationConnected`, which contains an object like this:

```json theme={null}

{
  "accountTokens": [
    {
      "account": {
        "accountName": "Coinbase wallets",
        "fund": 0.90
      },
      "tokenId": "dc16b40f-746c-4701-xxxx-ac37eccc766d"
    }
  ]
}

```

Save the `tokenId` for future use with Mesh APIs.

***

## 3. Reuse TokenIds with Mesh SDK

You can pass existing `TokenId` (or multiple, if available) into the Mesh Link SDK to skip re-authentication and launch users directly into the transfer or portfolio flow.

**SDK Setup Example:**

```jsx theme={null}
javascript
CopyEdit
const link = new MeshLink({
  clientId: "<your-client-id>",
  linkToken: "<link-token>",
  accountTokens: [
    {
      tokenId: "dc16b40f-746c-4701-xxxx-ac37eccc766d",
      type: "Coinbase"
    }
  ]
});

```

This enables seamless repeat usage without forcing the user to re-authenticate.

If the associated token is still valid, users will skip auth and land in the desired experience. If the token has expired (e.g., Binance), Link will prompt the user to re-authenticate and automatically reactivate the same `TokenId` upon success.

***

### 4. Token Lifecycle and Behavior

| Scenario                                                           | Result                                                                                                              |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **Same user reconnects with same integration**                     | Returns same `TokenId`                                                                                              |
| **Different user connects to same integration**                    | Returns a new `TokenId`                                                                                             |
| **Same user connects with different scopes (e.g., read vs write)** | Returns distinct `TokenId`s per scope                                                                               |
| **Write endpoint called using read-only `TokenId`**                | API returns a scope mismatch error                                                                                  |
| **Token revoked by client**                                        | Associated access is permanently disabled and Mesh also deletes the token physically, without any way to restore it |

***

## Supported Integrations (as of today)

* **Coinbase** (OAuth)
* **Binance** (Username/Password)
* *Note: connections with self-custody wallets are maintained on subsequent sessions without the need for handling tokens (unless the user actively kills the connection in their wallet app). This means the same smooth return user journey is achieved for wallet transactions.*

For testing with sandbox accounts, see [our sandbox guide](https://docs.meshconnect.com/guides/digital-asset-managed-transfers-with-sdk-integration-guide).

***

## Key Takeaways

* The `TokenId` is a powerful abstraction. It should be stored and transmitted securely.
* MMT is backward-compatible with all Mesh API endpoints that accept `AuthToken`.
* Always ensure scope consistency when re-using a `TokenId`.

***


# Paylinks
Source: https://docs.meshconnect.com/advanced/paylinks



# Introduction

This document explains how to use Paylinks, which allows merchants to redirect customers to a pre-built page for completing payments or asset transfers. This approach simplifies the payment process by eliminating the need for merchants to integrate the Mesh SDK directly into their systems.

Paylinks is a feature that enables clients to externalize the Link functionality to a Mesh-hosted webpage.  Instead of integrating the Mesh SDK directly into their application, merchants can generate a Paylink URL and redirect their customers to this URL.  The customer can then complete the payment or transfer process on the Mesh-hosted page.

This approach is particularly useful in several scenarios:

* **Simplified Integration:** For merchants who want to quickly enable payment functionality without extensive development work.
* **Third-Party Platforms:** When integrating with platforms where direct SDK integration is not feasible or desirable.
* **Specific Use Cases:** Situations where a simple redirect-based payment flow is preferred.

# Prerequisites

Before using Paylinks, ensure you have the following:

* Mesh Client ID and Client Secret

# Implementation

## 1. Generate a Paylink URL

To create a Paylink, send a `linkToken` request to the Mesh API. This will generate a URL that you can then provide to your customer.

* **Method:** `POST`

* **URL:** `https://integration-api.meshconnect.com/api/v1/linkToken`

* **Headers:**
  * `X-Client-Id`: Your Mesh Client ID. This identifies your application to the Mesh API.
  * `X-Client-Secret`: Your Mesh Client Secret. This is a secret key used to authenticate your requests to the Mesh API.
    Include these headers in your request to authorize it.

* **Body:** The request body needs to be in JSON format and include the following information:
  * `userId`: A unique identifier for the user making the payment or transfer. This should be a value that identifies the user in your system.
  * `transferOptions`: This object contains the details of the transaction:
    * `toAddresses`: An array of one or more recipient addresses. For each recipient, provide:
      * `symbol`: The symbol of the asset being transferred (e.g., "ETH", "BTC").
      * `networkId`: The ID of the blockchain network being used for the transfer.
      * `address`: The blockchain address of the recipient.
    * `isInclusiveFeeEnabled`: A boolean value that specifies whether the transaction fee is included in the transfer amount. Set to `true` if the amount your user enters includes the fee, `false` otherwise.
    * `transferType`: The type of transfer. Use "deposit" if the user is sending funds to your platform, "payment" if the user is paying for something.
    * `transactionId`: A unique identifier for this transaction in your system. This allows you to track the transaction and reconcile it later.
    * `fundingOptions`: An object indicating if SmartFunding is enabled
    * `generatePayLink`: Set this value to `true`. This tells the Mesh API to generate a Paylink URL in the response. **This is required to ensure Paylinks works.**

**Important:** You **must** provide a `transactionId` in your request body when `generatePayLink` is set to `true`. If it is not provided, the API will return an error. The `transactionId` should be a unique string generated by your system for each transaction. This ID is used to correlate the Paylink transaction with your internal records. For example, you could use an order ID, a payment ID, or a unique hash. This value should be unique and persistent so you can reliably look up the transaction in your database.

**Example Request (JSON):**

```json theme={null}
{
  "userId": "USER_IDENTIFIER_123",
  "transferOptions": {
    "amountInFiat": "100.00",
    "toAddresses": [
      {
        "symbol": "ETH",
        "networkId": "NETWORK_ID_GOES_HERE",
        "address": "0xRecipientAddressGoesHere"
      }
    ],
    "generatePayLink": true,
    "isInclusiveFeeEnabled": false,
    "transferType": "payment",
    "transactionId": "YOUR_TRANSACTION_ID",
    "fundingOptions": {
      "enabled": true
    }
  }
}
```

Replace the placeholder values (e.g., `USER_IDENTIFIER_123`, `NETWORK_ID_GOES_HERE`) with actual data

## 2. Retrieve the Paylink URL from the Response

After sending the `linkToken` request, the API will respond with a JSON object. If the request was successful, the response will contain a `paymentLink` field.

**Example Response (JSON):**

```json theme={null}
{
  "content": {},
  "linkToken": "aHR0cHM6Ly93ZWlubWVzaGNvbm5lY3QuY29tL2lyYi1pZnJhk...",
  "paymentLink": "https://paylink.meshconnect.com?linkToken=aHR0cHM6Ly...",
  "status": "ok",
  "message": "",
  "errorType": ""
}
```

The `paymentLink` value is the URL that you will provide to your customer.

## 3. Redirect Your Customer to the Paylink URL

Redirect your customer to the URL provided in the `paymentLink` field. This can be done in several ways, depending on your application (e.g., using a redirect in your web server code, or providing the link in an email or message).

Once the user clicks the link, they will be taken to a Mesh-hosted page where they can complete the payment or transfer.

# Error States

This section describes potential errors that your customers may encounter when using Paylinks, and how to handle them:

* **Paylink was already used**: This error occurs when a user attempts to use the same Paylink URL more than once. Paylinks are designed to be used only once for security reasons.
  * **Merchant Action**: When this happens, your user will need to initiate a new payment or transfer and obtain a new Paylink. You should provide clear messaging to the user explaining that the Paylink can only be used once and that they need to generate a new one.
* **Previous Paylink was unused, but expired**: This error occurs when a user tries to use a Paylink that has expired. Paylinks are typically valid for a limited time (e.g., 30 minutes).
  * **Merchant Action**: Similar to the previous error, your user will need to generate a new Paylink. Inform them that the previous link has expired and they should start the payment or transfer process again.

**Recommended User Experience**: In both cases, it is strongly recommended that you redirect the user back to the payment initiation page on your site where they can click a button (e.g., "Pay" or "Transfer") to generate a new Paylink. This will provide a seamless experience for the user and allow them to complete their transaction.


# Managing Sub-Clients
Source: https://docs.meshconnect.com/advanced/sub-client-branding



## **What are Sub-Clients?**

If your product is used directly by end-users, this section is likely not relevant to you. However, if your product is embedded within other platforms (e.g., you are a Payment Service Provider powering payments for multiple retailers), then Sub-Clients are critical.

A **Sub-Client** represents the specific merchant or platform where your product is embedded. Registering them allows you to:

* **Ensure Consistent Branding:** Display the specific retailer's name and logo in the Mesh Link modal, creating a seamless experience for the end-user.
* **Maintain Compliance:** Mesh requires visibility into the legal entity associated with each transaction for compliance purposes.

### **How to Register a Sub-Client**

You can register and manage sub-clients in two ways: via the Mesh Dashboard or programmatically via the Account Management API.

### **Option 1: Via the Mesh Dashboard**

1. Notify your Mesh representative to enable this functionality for your account.
2. Navigate to **Account** > **Link Configuration** > **Clients** tab.
3. Click **"Add a client"**.
4. Enter the Business Legal Name, Display Name, Callback URL(s), and upload the relevant icon.
5. Click **Save**.

### **Option 2: Via the Account Management API**

For high-volume or automated setups, you can use our **Account Management API** to create, update, and delete sub-clients programmatically.

To use this API, you must first generate a dedicated API key and configure security settings.

1. **Generate an API Key:**
   * Go to **Account** > **API Keys**.
   * In the new **Account Management API Keys** section, click to generate a new key.
   * Use this key to authenticate your requests to the `https://admin-api.meshconnect.com` endpoints.
2. **Configure IP Whitelisting (Security Requirement):**
   * To enhance security, access to the Account Management API is restricted to pre-approved IP addresses.
   * Go to the **Account Management API Whitelisted IPs** section in your dashboard.
   * Add the specific IP address ranges from which your servers will make API calls.
   * **Note:** Initially, you can configure these IPs without enforcement. Once your configuration is tested and ready, we will enable the filtering to strictly enforce these rules.

### **Using a Sub-Client in a Transaction**

Once a sub-client is registered (via Dashboard or API), you will receive a unique `subClientId`.

To apply the sub-client's branding and settings to a transaction, simply pass this ID in your `linkToken` request:

JSON

`{
  "subClientId": "your_sub_client_id_here",
  "transferOptions": { ... }
}`

This ensures the Link modal automatically renders with the correct branding for that specific merchant. You can test this flow in our interactive demos by selecting a registered client from the "Sub-client" dropdown.


# Verifying Self-Hosted Wallets
Source: https://docs.meshconnect.com/advanced/verifying-self-hosted-wallets

Using Mesh Verify for wallet verification

### Background on self-hosted wallet Travel Rule guidelines

Travel Rule regulations have long-existed in traditional financial markets as a way for regulators to enforce laws pertaining to the movement of money (eg. anti-money laundering, terrorist financing, sanctions, etc.). In short, regulated financial institutions are responsible for knowing who they are receiving assets from, and where they’re sending assets to. The crypto world has long-awaited clear Travel Rule guidelines for crypto, and on July 4th the European Banking Authority (EBA) released their final guidelines. Other global regulatory regimes are likely to follow soon as well. This guide dives into detail around Mesh’s support for verifying ownership of a self-hosted wallet.

### How does wallet verification work?

The nature of self-hosted wallets is that they don’t know who the user is. In other words, a user doesn’t KYC with MetaMask like they would with Coinbase or another centralized exchange. So verifying ownership of a self-hosted wallet is not about receiving user information from that wallet. Instead, it is about confirming that the user you know is in control of the wallet in question. Additionally, verification pertains to an address (ie. 0x31…cF98), not a wallet app (ie. MetaMask). Keep in mind that a user can interact with the same wallet (ie. address) from multiple wallet apps, and can also interact with multiple wallets from within the same wallet app.

The EBA specifies that one acceptable method of verifying ownership of a self-hosted wallet is having the user sign a self-attestation of ownership (ie. a message) in that wallet. The message doesn’t have to be anything specific, but the message the user signs must be the exact message requested by you. A message signature is an off-chain event (ie. it’s completely gasless), but is also fully verifiable with the combination of the signedMessageHash, the address, and message.

### Invoking wallet verification in Mesh Link

* Wallet verification can be completely independent of a transfer (ie. the user only connects their wallet and signs the message), or can be used in combination with a transfer (ie. the user connects their wallet, signs a message, and then continues to the transfer).
* In the request to `/api/v1/linktoken` to invoke the Mesh Link modal, there is a parameter called `verifyWalletOptions`. To have the user sign a message, you must:
  1. Select a `verificationMethods` (as of now the only option is `signedMessage`). We may also have other options in the future.
  2. Add a `message`. We recommend keeping this short. Do not include any PII in this message (ie. do not include a user name). If this is left blank, a generic message will be added.
* This will only impact the user experience for self-hosted wallets (ie. MetaMask, Trust Wallet, etc.). This will not change anything about the experience for centralized exchanges (ie. Binance, Coinbase, etc.).
* After connecting their wallet, the user will then be prompted to sign a message. As with connection requests and transfer requests, the user will not have to configure anything manually. Mesh will send the signature request, with the message, to the wallet app, and will open the wallet app on the user’s screen. All the user has to do is review it and sign it.

### What you’ll receive back from Mesh after a successful signature

After the user signs the message in their wallet, you will receive the SDK event: `walletMessageSigned` back from Mesh with the following payload:

* `signedMessageHash`
* `message`
* `address`
* `timeStamp`
* `isVerified` (boolean)

This data can be stored on your side for audit purposes, as well as to improve the return user experience within your UX.

**NOTE**: this is the only time that the `signedMessageHash` data will be provided, Mesh does not retain this data.


# Generate Auth token
Source: https://docs.meshconnect.com/api-reference/account-management/auth-token/generate-auth-token

https://admin-api.meshconnect.com/swagger/AdminAPI/swagger.json post /admin/api/v1/Token
Get a short lived token for initializing request calls for Registered client API.



# Get Main Client callback urls
Source: https://docs.meshconnect.com/api-reference/account-management/main-clients/get-main-client-callback-urls

https://admin-api.meshconnect.com/swagger/AdminAPI/swagger.json get /admin/api/v1/Client/callbackUrls
Get information about Main Client Allowed Link URLs.



# Update Main Client callback urls
Source: https://docs.meshconnect.com/api-reference/account-management/main-clients/update-main-client-callback-urls

https://admin-api.meshconnect.com/swagger/AdminAPI/swagger.json post /admin/api/v1/Client/callbackUrls
Update information about Main Client Allowed Link URLs. Allowed Link URLs of Main Client will only be used for those Registered clients,
that don't have any Allowed Link URLs specified.



# Add new Registered client
Source: https://docs.meshconnect.com/api-reference/account-management/registered-clients/add-new-registered-client

https://admin-api.meshconnect.com/swagger/AdminAPI/swagger.json post /admin/api/v1/SubClient
Create new Registered client with specified data. Client will be created without Logo URL.
In order to specify a Logo URL, send separate Update Registered Logo request along with id of just created client.



# Delete Registered client
Source: https://docs.meshconnect.com/api-reference/account-management/registered-clients/delete-registered-client

https://admin-api.meshconnect.com/swagger/AdminAPI/swagger.json delete /admin/api/v1/SubClient/{id}
Delete Registered client by id.



# Get all Registered clients
Source: https://docs.meshconnect.com/api-reference/account-management/registered-clients/get-all-registered-clients

https://admin-api.meshconnect.com/swagger/AdminAPI/swagger.json get /admin/api/v1/SubClient
Get information about all Registered clients.



# Get Registered client
Source: https://docs.meshconnect.com/api-reference/account-management/registered-clients/get-registered-client

https://admin-api.meshconnect.com/swagger/AdminAPI/swagger.json get /admin/api/v1/SubClient/{id}
Get information about the Registered client of specified identifier.



# Remove Registered client Logo
Source: https://docs.meshconnect.com/api-reference/account-management/registered-clients/remove-registered-client-logo

https://admin-api.meshconnect.com/swagger/AdminAPI/swagger.json delete /admin/api/v1/SubClient/{id}/logo
Remove logo of Registered client.



# Update Registered client
Source: https://docs.meshconnect.com/api-reference/account-management/registered-clients/update-registered-client

https://admin-api.meshconnect.com/swagger/AdminAPI/swagger.json put /admin/api/v1/SubClient/{id}
Update information about already Registered client by client id. This request does not support updating client Logo URL.
In order to update a Logo URL, send separate Update Registered Logo request along with id of the client.



# Update Registered client Logo
Source: https://docs.meshconnect.com/api-reference/account-management/registered-clients/update-registered-client-logo

https://admin-api.meshconnect.com/swagger/AdminAPI/swagger.json post /admin/api/v1/SubClient/{id}/logo
Adds or update a logo for Registered client.
Allowed file extensions are ".png", ".jpg", ".jpeg".
Allowed file MIME types are "image/png", "image/jpeg", "image/jpg".
Maximum file size is 5MB.
Upload logo as form data with key 'logoFile'.



# Get account balance
Source: https://docs.meshconnect.com/api-reference/balance/get-account-balance

post /api/v1/balance/get
Get real-time account fiat balances.



# Get aggregated portfolio fiat balances
Source: https://docs.meshconnect.com/api-reference/balance/get-aggregated-portfolio-fiat-balances

get /api/v1/balance/portfolio
Get cached aggregated fiat balances from all connected integrations.



# Get health status
Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/get-health-status

get /api/v1/status
Get the list of supported institutions and their health statuses.



# Get Link token with parameters
Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters

post /api/v1/linktoken
Get a short lived, one-time use token for initializing a Link session using the client-side SDKs



# Refresh auth token
Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/refresh-auth-token

post /api/v1/token/refresh
Refresh auth token of the connected institution.
Some institutions do not require tokens to be refreshed.
            
The following institutions require custom flows:
            
WeBull: AuthToken should be provided along with the RefreshToken
            
Vanguard: security settings may activate MFA, requiring user action.
If MFA is triggered, a second refresh request should be sent.
Second request should contain MFA code and access token obtained from initial response



# Remove connection
Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/remove-connection

delete /api/v1/account
Remove connection to the financial institution and erase all related data completely.



# Retrieve the list of all available integrations.
Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/retrieve-the-list-of-all-available-integrations

get /api/v1/integrations
Returns a list of integrations with details including the integration ID, name, type,
DeFi wallet provider ID, and categories.



# Get deposit address
Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-deposit-address

post /api/v1/transfers/managed/address/get
Get or generate a cryptocurrency deposit address that can be used to transfer assets to the financial institution



# Get integrations
Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-integrations

get /api/v1/transfers/managed/integrations
**Get supported integrations list.**


---
Get the list of all integrations supported by Mesh to perform transfers, including which tokens and networks are supported.



# Get deposit addresses
Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-list-of-deposit-addresses

post /api/v1/transfers/managed/address/list
Get or generate a cryptocurrency deposit address that can be used to transfer assets to the financial institution



# Get networks
Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-networks

get /api/v1/transfers/managed/networks
**Get supported networks list.**


---
Get the list of all networks supported by Mesh to perform transfers, including which tokens and integrations are supported.



The response always includes validation data:
- `addressPattern`: The regex pattern for validating addresses on this network
- `contractAddress`: For each token, the contract address (if applicable) to enable ERC20 contract address validation



# Get supported tokens list
Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-supported-tokens-list

get /api/v1/transfers/managed/tokens
Get the list of all tokens supported by Mesh to perform transfers, including which networks and integrations are supported.



# Get transfers initiated by Mesh
Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-transfers-initiated-by-mesh

get /api/v1/transfers/managed/mesh
Get cryptocurrency transfers initiated by Mesh on exchanges or self-custody wallets.



# Get aggregated portfolio
Source: https://docs.meshconnect.com/api-reference/portfolio/get-aggregated-portfolio

get /api/v1/holdings/portfolio
Get the aggregated portfolio of the user containing market values.



# Get holdings.
Source: https://docs.meshconnect.com/api-reference/portfolio/get-holdings

post /api/v1/holdings/get
Obtain assets from the connected investment account. Performs realtime API call to the underlying integration.



# Get holdings values.
Source: https://docs.meshconnect.com/api-reference/portfolio/get-holdings-values

post /api/v1/holdings/value
Obtain assets from the connected investment account and return total value and performance.
Performs realtime API call to the underlying integration.



# Get deposit address
Source: https://docs.meshconnect.com/api-reference/transfers/get-deposit-address

post /api/v1/transfers/address/get
Get or generate a cryptocurrency deposit address that can be used to transfer assets to the financial institution



# Get details of asset
Source: https://docs.meshconnect.com/api-reference/transfers/get-details-of-asset

post /api/v1/transfers/symbol/details
Get details of the asset for deposit or withdrawal. For example, several exchanges support same tokens over multiple
blockchains, and thus require the name of chain to be supplied for transfers. This endpoint allows getting such details.



# Get transfer details
Source: https://docs.meshconnect.com/api-reference/transfers/get-transfer-details

post /api/v1/transfers/details
Get details of a specific transfer (withdrawals or deposits) executed from an exchange.
Only supports Exchange integrations.



# Get transfer history
Source: https://docs.meshconnect.com/api-reference/transfers/get-transfer-history

post /api/v1/transfers/list
Get entire history of cryptocurrency transfers (withdrawals or deposits) executed from an exchange.
Only supports Exchange integrations.



# Verify account identity.
Source: https://docs.meshconnect.com/api-reference/verify/verify

post /api/v1/exchange/verify
Returns basic profile data of the user's exchange account.
Available data varies by exchange and linked account.



# Get wallet verifications for user and address.
Source: https://docs.meshconnect.com/api-reference/verify/wallet

get /api/v1/wallets/verify



# Manual
Source: https://docs.meshconnect.com/manual



This guide provides a step-by-step walkthrough for integrating the Mesh SDK across all supported platforms. The core flow is the same everywhere: your secure backend creates a linkToken, which your client-side application then uses to open the Link UI.

## Setting up your developer dashboard (team members, API keys, and Link customization)

* Go to [Account > Team](https://dashboard.meshconnect.com/company/team) to add team members. New team members can be invited with varying permission sets to ensure you control access to only what’s needed on a per-member basis.

<img alt="Image1 Pn" />

* Go to [Account > API keys](https://dashboard.meshconnect.com/company/keys) to add callback URLs (where the Mesh SDK will be allowed to render) and to generate your production or sandbox API keys (you’ll have to complete a business verification check before being able to generate production keys).

<img alt="Image2 Pn" />

* Go to [Account > Link configuration](https://dashboard.meshconnect.com/company/link) to customize the Link SDK for your branding and other needs.

<img alt="Image3 Pn" />

## Create Link Token (Backend)

This first step is a mandatory server-side operation and is the same for all client platforms. The Link UI is always initialized with a linkToken, which must be generated from your backend to protect your apiSecret.

**🔒 Security First**
Never expose your `X-Client-Secret` in a client-side application. The `/api/v1/linktoken` endpoint must always be called from a secure server environment.

Make a `POST` request from your backend to the appropriate Mesh API endpoint:

Sandbox: [https://sandbox-integration-api.meshconnect.com](https://sandbox-integration-api.meshconnect.com/api/v1/linktoken)

Production: [https://integration-api.meshconnect.com](https://integration-api.meshconnect.com)

**Example** `cURL` **request from your backend**

```
curl --request POST \
     --url https://integration-api.meshconnect.com/api/v1/linktoken \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'X-Client-Id: YOUR_CLIENT_ID' \
     --header 'X-Client-Secret: YOUR_CLIENT_SECRET' \
     --data '{
        "userId": "example_user123",
  		"restrictMultipleAccounts": true,
  		"transferOptions": {
    		"transactionId": "example_tx123",
    		"transferType": "payment", // payment or deposit
    		// Enable SmartFunding
    		"fundingOptions": {
      			"enabled": true
    		},
    	"isInclusiveFeeEnabled": false,
    	"toAddresses": [
      		{
        		"symbol": "USDT",
        		"address": "0x314838D6783865908456257c0b07Ea4Bc272cF98", 
        		"networkId": "18fa36b0-88a8-43ca-83db-9a874e0a2288",
        		"amount": 99.99 // pass an amount when enabling SmartFunding
      		}
    	]
      }'
```

The API will respond with a linkToken that you can then send to your client application.

## Configuring the Link Token

The `linkToken` is a powerful tool that allows you to tailor the Link UI for your specific use case. By passing different parameters in the body of your `POST /api/v1/linktoken` request, you can control the entire user journey.

#### **Setting up a Transfer**

If you want the user to transfer assets, you must include the `transferOptions` object in your request body. This object contains all the necessary details for the transaction.

#### Finding the `networkId`

The `networkId` is a required field that tells Mesh which blockchain to use for the transfer. You can retrieve a complete list of all supported networks and their corresponding `networkId` values by making a `GET` request to our [transfers/managed/networks](https://docs.meshconnect.com/api-reference/managed-transfers/get-networks) endpoint.

#### **Configuring Destination Addresses (**`toAddresses`**)**

This array tells Mesh where the user can send their funds.

* **Single Address (Streamlined UX):** If your user has already selected a token and network in your app, or if you only accept one specific asset, you can pass a single object in the `toAddresses` array. This provides the most direct user experience, as Link will skip the asset and network selection screens.
* **Multiple Addresses (Recommended for Flexibility):** For greater flexibility and potentially higher conversion, we recommend passing an array of all possible tokens and networks that you accept. This allows the user to choose their preferred asset within the Link UI.

#### **Enabling SmartFunding**

To maximize conversion and increase average transfer size, you should always enable SmartFunding.

* **How to Enable:** Set `enabled: true` within the `fundingOptions` object inside `transferOptions`.
* **Why it's important:** SmartFunding allows users to complete a payment even if they don't have enough of the target asset by auto-converting their other available tokens. This is a key feature for ensuring a successful transaction.

```
"transferOptions": {
  "toAddresses": [
    // ... your single or multiple addresses here
  ],
  "fundingOptions": {
    "enabled": true
  }
}
```

#### **Controlling the User Flow**

You can control where the user lands when the Link UI opens.

* **Go to Catalog:** By default, if you only provide a `userId`, the user will see the full catalog of supported exchanges and wallets.
* **Go Straight to an Integration:** To bypass the catalog and send the user directly to a specific institution (e.g., Coinbase), include the `integrationId` in your `linkToken` request.

#### **Using Paylinks**

If you want to simplify your integration and avoid using the client-side SDKs, you can use Paylinks. This feature generates a unique, Mesh-hosted URL that you can redirect your customers to.

* **How to Enable:** Set `"generatePayLink": true` inside your `transferOptions`.
* **Learn More:** For a detailed guide on this feature, please see our [**Paylinks**](/advanced/paylinks) Documentation.

## Open Link UI (Client-Side)

Once your client application receives the linkToken, you can use it to initialize and open the Link UI.

**Installation**

<Tabs>
  <Tab title="Web">
    ```bash theme={null}
    npm install --save @meshconnect/web-link-sdk 
    ```
  </Tab>

  <Tab title="iOS">
    Add the LinkSDK package in your project's Package Dependencies or download the LinkSDK.xcframework.
  </Tab>

  <Tab title="Android">
    In your build.gradle file:

    ```groovy theme={null}
    dependencies { implementation 'com.meshconnect:link:2.0.0' } 
    ```
  </Tab>

  <Tab title="React Native">
    ```bash theme={null}
    npm install --save @meshconnect/react-native-link-sdk

    # Also ensure react-native-webview is installed
    npm install --save react-native-webview
    ```
  </Tab>

  <Tab title="Flutter">
    Add to your `pubspec.yaml`:

    ```yaml theme={null}
    dependencies:
      mesh_sdk_flutter: <latest_version>
    ```

    Then add localization delegates to your `MaterialApp`:

    ```dart theme={null}
    import 'package:mesh_sdk_flutter/mesh_sdk_flutter.dart';

    MaterialApp(
      localizationsDelegates: [
        ...MeshLocalizations.localizationsDelegates,
      ],
    );
    ```
  </Tab>
</Tabs>

**Code Implementation**

<Tabs>
  <Tab title="Web">
    ```jsx theme={null}
    import { createLink } from "@meshconnect/web-link-sdk";

    // Initialize the Link connection with your callbacks
    const meshLink = createLink({
      clientId: "YOUR_CLIENT_ID",
      onIntegrationConnected: (payload) => { /* Handle success */ },
      onExit: (error) => { /* Handle exit */ },
      onTransferFinished: (payload) => { /* Handle transfer result */ }
    });

    // Use the linkToken from your server to open the UI
    meshLink.openLink("YOUR_LINK_TOKEN");
    ```
  </Tab>

  <Tab title="iOS">
    ```swift theme={null}
    // Create a configuration with the linkToken and callbacks
    let configuration = LinkConfiguration(
    linkToken: "YOUR_LINK_TOKEN",
    onIntegrationConnected: { linkPayload in /* Handle success */ },
    onTransferFinished: { transferPayload in /* Handle transfer result */ },
    onExit: { /* Handle exit */ }
    )

    // Create a handler and present the UI
    let result = configuration.createHandler()
    switch result {
    case .failure(let error):
        print(error)
    case .success(let handler):
        handler.present(in: self)
    }
    ```
  </Tab>

  <Tab title="Android">
    ```kotlin theme={null}
    // Register a launcher to handle the result from the Link flow
    private val linkLauncher = registerForActivityResult(LinkContract()) { result ->
    when (result) {
    is LinkSuccess -> {
    // Handle successful connection or transfer
    handlePayloads(result.payloads)
    }
    is LinkExit -> {
    // Handle user exit or error
    // result.errorMessage will contain details
    }
    }
    }

    // Launch the Link UI with the linkToken from your server
    linkLauncher.launch("YOUR_LINK_TOKEN")
    ```
  </Tab>

  <Tab title="React Native">
    ```jsx theme={null}
    import React from 'react';
    import { LinkConnect } from '@meshconnect/react-native-link-sdk';

    export const App = () => {
      return (
        <LinkConnect
          linkToken={"YOUR_LINK_TOKEN"}
          onIntegrationConnected={(payload) => { /* Handle success */ }}
          onTransferFinished={(payload) => { /* Handle transfer result */ }}
          onExit={(err) => { /* Handle exit */ }}
        />
      );
    };
    ```
  </Tab>

  <Tab title="Flutter">
    ```dart theme={null}
    import 'package:mesh_sdk_flutter/mesh_sdk_flutter.dart';

    Future<void> openMeshLink(String linkToken) async {
      final result = await MeshSdk.show(
        context,
        configuration: MeshConfiguration(
          linkToken: linkToken,
          onIntegrationConnected: (integration) { /* Handle success */ },
          onTransferFinished: (transfer) { /* Handle transfer result */ },
          onExit: (error) { /* Handle exit */ },
        ),
      );

      switch (result) {
        case MeshSuccess():
          // Handle success
        case MeshError():
          // Handle error: result.type
      }
    }
    ```
  </Tab>
</Tabs>

### Handle Events

Your application needs to respond to events to know the outcome of a user's session. This happens in two places: on the client-side from the SDK, and on the server-side from webhooks.

**From Link UI (Client-Side)** The client-side SDK provides immediate feedback about the user's interaction. Please see the [Mesh Link SDK events](/advanced/link-ui-events) guide for full details on callback functions and events emitted from Mesh’s SDKs.

<Tabs>
  <Tab title="Web">
    The `createLink` function takes callbacks as arguments:

    * `onIntegrationConnected`: Called on a successful account connection. The payload contains the accessToken.
    * `onTransferFinished`: Called when a transfer is complete (either success or failure).
    * `onExit`: Called when the user closes the UI.
  </Tab>

  <Tab title="iOS">
    The `LinkConfiguration` object takes callbacks:

    * `onIntegrationConnected`: Called on successful connection.
    * `onTransferFinished`: Called when a transfer is complete.
    * `onExit`: Called when the user closes the UI.
  </Tab>

  <Tab title="Android">
    The `registerForActivityResult` callback provides a result object:

    * `LinkSuccess`: Contains a list of payloads, including AccessTokenPayload for connections and TransferFinishedSuccessPayload for successful transfers.
    * `LinkExit`: Indicates the user closed the UI. The errorMessage property will contain details if an error occurred.
  </Tab>

  <Tab title="React Native">
    The `<LinkConnect>` component accepts props for callbacks:

    * `onIntegrationConnected`: Called on successful connection.
    * `onTransferFinished`: Called when a transfer is complete.
    * `onExit`: Called when the user closes the UI.
  </Tab>

  <Tab title="Flutter">
    The `MeshConfiguration` object accepts callbacks:

    * `onIntegrationConnected`: Called on successful connection.
    * `onTransferFinished`: Called when a transfer is complete.
    * `onExit`: Called when the user closes the UI.
    * `onEvent`: Called for various UI events.

    The `MeshSdk.show()` method returns a `MeshResult` that can be `MeshSuccess` or `MeshError`.
  </Tab>
</Tabs>

**From Webhooks (Server-Side)**
Webhooks are the definitive source of truth for the status of a transfer. While the client-side onTransferFinished event provides immediate feedback, a webhook from Mesh ensures your backend is notified of the final state (succeeded or failed), even if the user closes the app.

**Retrieving Historical Data**

To retrieve a history of past transfers and their final statuses, you can also use the `GET /v1/transfers/managed/mesh` endpoint. This is useful for reconciliation or auditing purposes after a transfer has already completed. You can find the API reference for this endpoint [**here**](https://docs.meshconnect.com/api-reference/managed-transfers/get-transfers-initiated-by-mesh).

**➡️ Learn More**
For detailed information on webhook security, payload structure, and how to respond to events, see the [webhooks](/testing/webhooks) guide.

To get more information about our SDKs, refer to the respective Github repository:

| [Web](https://github.com/FrontFin/mesh-web-sdk) | [Android](https://github.com/FrontFin/mesh-android-sdk) | [iOS](https://github.com/FrontFin/mesh-ios-sdk) | [React Native](https://github.com/FrontFin/mesh-react-native-sdk) | [Flutter](https://github.com/FrontFin/mesh-flutter-sdk) |
| :---------------------------------------------: | :-----------------------------------------------------: | :---------------------------------------------: | :---------------------------------------------------------------: | :-----------------------------------------------------: |

## Productionize

When you are ready to move from testing to production, follow these steps:

**Switch API Keys**: In your Mesh Dashboard, generate Production API keys and use them in your backend environment variables.

**Update API Endpoint**: Change the base URL in your backend from the sandbox endpoint to the production endpoint ([https://integration-api.meshconnect.com](https://integration-api.meshconnect.com)).

**Configure Production Webhooks**: In the Mesh Dashboard, add your production webhook URL to receive real-time transfer status updates.

**Add Allowed Callback URLs**: Ensure your production domain (e.g., [https://yourapp.com](https://yourapp.com)) is added to the "Allowed callback URLs" list in your dashboard settings to allow the Link SDK to load correctly.


# Overview
Source: https://docs.meshconnect.com/overview



Mesh is a global crypto payments network that connects exchanges, wallets, and payment providers, allowing merchants to accept crypto payments and stablecoin conversions easily. It streamlines payments, reduces fees, and offers instant settlement through a suite of APIs and client-side SDKs.

The core of the Mesh experience is **Mesh Link**, a collection of client-side SDKs that provide a user-friendly interface for your users to interact with their crypto exchanges and self-custody wallets. It handles credential validation, multi-factor authentication, and error handling for every integration we support. This allows you to build embedded experiences where users can transfer digital assets from centralized exchanges or self-custody wallets without ever needing to leave your application to copy and paste an address.

***

## ✨ Capabilities

Mesh is a flexible platform designed to support a variety of use cases through its core product offerings.

### **Pay**

Configure Link to facilitate cryptocurrency payments within your application. You can define accepted payment assets, amounts, and apply fees for processing. SmartFunding enables automatic conversion of the assets the user has into your payment token of choice.

### **Deposit**

Enable your users to deposit crypto into specified addresses. You can define single or multiple deposit options and create a seamless experience for returning users by saving their connection information.

### **Verify**

Confirm ownership of the accounts your users’ interact with.

* **For Exchanges**: Retrieve basic profile data to get user information directly from their connected exchange account.
* **For Wallets**: Provide an embedded, gasless wallet verification by having users sign a message to proving they’re in control of a certain address.

***

## 🧱 Basics of a Mesh integration

**Foundational elements**

* **Backend**: You request a linkToken which will be used to initialize the Mesh Link SDK. The parameters passed configure the user's experience in that session. These are single use, so you'll be requesting a new linktoken for every user session.
* **Frontend**: Download and install the Mesh SDK. This is a modal that overlays your app and facilitates the UX of the entire user journey.

**The **[**Manual**](manual)** that follows will provide more detail on the basics of building your integration with Mesh**

* Inviting team members to collaborate in your Mesh developer account
* Generating API keys and managing permissions
* Configuring the Link SDK for your branding and other needs
* Configuring the linkToken request to create the appropriate user flow
* Configuring the SDK initialization to support language and return users
* Listening for SDK events to properly handle the end of the user journey
* Subscribing to webhooks for real-time transfer status updates
* Enabling a seamless return-user experience with token management.
* General best practices

***


# null
Source: https://docs.meshconnect.com/supported-tokens



# Mesh Network & Token Support

## Quick Overview

**24 Networks** • **\~120 Unique Tokens** • **233 Wallets** • **8 Major Exchanges**

## Supported Networks

### Major EVM Networks

| **Network**     | **Tokens** | **Available Assets**                                                                                                                                                                                                                                         |
| --------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ethereum**    | **43**     | AAVE, APE, ARB, BLUR, BUSD, CAKE, CRO, DAI, DEXE, ENA, ETH, FDUSD, FTM, GRT, IMX, INJ, LDO, LEO, LINK, MANA, MATIC, MKR, MNT, PAXG, PYUSD, QNT, RLUSD, RNDR, SAND, SHIB, SNX, TUSD, UNI, USD1, USDC, USDD, USDP, USDT, VIRTUAL, WBTC, WETH, USDG, EURC, WLFI |
| **Polygon**     | **6**      | POL, USDC, USDT, DAI, MATIC, WMATIC                                                                                                                                                                                                                          |
| **BSC**         | **11**     | BNB, USDC, USDT, CAKE, FDUSD, WBNB, LTC, DEXE, FORM, USD1, WLFI                                                                                                                                                                                              |
| **Arbitrum**    | **7**      | ETH, USDC, USDT, DAI, ARB, PYUSD, WETH                                                                                                                                                                                                                       |
| **Optimism**    | **7**      | ETH, USDC, USDT, DAI, OP, SNX, WETH                                                                                                                                                                                                                          |
| **Base**        | **5**      | ETH, USDC, VIRTUAL, WETH, EURC                                                                                                                                                                                                                               |
| **Avalanche C** | **6**      | AVAX, USDC, USDT, DAI, WAVAX, EURC                                                                                                                                                                                                                           |
| **Blast**       | **3**      | BLAST, ETH, WETH                                                                                                                                                                                                                                             |
| **HyperEVM**    | **2**      | HYPE, USDC                                                                                                                                                                                                                                                   |
| **SEI**         | **2**      | SEI, USDC                                                                                                                                                                                                                                                    |
| **Monad**       | **5**      | MON, ETH, USD1, USDC, USDT                                                                                                                                                                                                                                   |

### Non-EVM Networks

| **Network** | **Tokens** | **Available Assets**                                                    |
| ----------- | ---------- | ----------------------------------------------------------------------- |
| **Solana**  | 10         | SOL, USDC, USDT, BONK, WIF, PENGU, JTO, PYUSD, FDUSD, TRUMP, USDG, EURC |

### Exchange-Only Networks

| **Network**     | **Tokens** | **Available Assets** |
| --------------- | ---------- | -------------------- |
| **Bitcoin**     | 1          | BTC                  |
| **Tron**        | 3          | TRX, USDC, USDT      |
| **Litecoin**    | 1          | LTC                  |
| **Dogecoin**    | 1          | DOGE                 |
| **Ripple**      | 1          | XRP                  |
| **Aptos**       | 3          | APT, USDC, USDT      |
| **Cardano**     | 1          | ADA                  |
| **Stellar**     | 3          | XLM, USDC, EURC      |
| **Sui**         | 3          | SUI, USDC, FDUSD     |
| **TON**         | 2          | TON, USDT            |
| **Sonic**       | 2          | S, EURC              |
| **Injective**   | 1          | INJ                  |
| **Avalanche X** | 1          | AVAX                 |

### Test Networks (Wallets only)

| **Wallet** | **Testnet**   | **Native Token** | **Stablecoin** | **Get Tokens**    |
| ---------- | ------------- | ---------------- | -------------- | ----------------- |
| MetaMask   | Sepolia       | SEPOLIAETH       | PYUSD, USDG    | sepoliafaucet.com |
| Phantom    | Solana Devnet | DEVNETSOL        | PYUSD, USDG    | faucet.solana.com |

## Stablecoin Coverage

| **Stablecoin** | **Networks**          | **Coverage**                                                                                                  |
| -------------- | --------------------- | ------------------------------------------------------------------------------------------------------------- |
| **USDC**       | 12 networks           | Ethereum, Polygon, BSC, Arbitrum, Optimism, Base, Avalanche, Solana, Tron, Aptos, Stellar, Sui, HyperEVM, SEI |
| **USDT**       | 11 networks           | Ethereum, Polygon, BSC, Arbitrum, Optimism, Avalanche, Solana, Tron, Aptos, Sui, TON                          |
| **DAI**        | 5 networks            | Ethereum, Polygon, Arbitrum, Optimism, Avalanche                                                              |
| **FDUSD**      | 4 networks            | Ethereum, BSC, Solana, Sui                                                                                    |
| **PYUSD**      | 3 networks + testnets | Ethereum, Arbitrum, Solana (+ Sepolia, Solana Devnet)                                                         |
| **USD1**       | 2 networks            | Ethereum, BSC                                                                                                 |
| **TUSD**       | 1 network             | Ethereum                                                                                                      |
| **USDP**       | 1 network             | Ethereum                                                                                                      |
| **USDD**       | 1 network             | Ethereum                                                                                                      |
| **RLUSD**      | 1 network             | Ethereum                                                                                                      |
| **USDG**       | 2 networks            | Ethereum, Solana                                                                                              |
| **USDH**       | 1 network             | HyperEVM                                                                                                      |

## Exchange Integration

| **Exchange**            | **Networks** | **Tokens** | **Focus**               |
| ----------------------- | ------------ | ---------- | ----------------------- |
| **Coinbase**            | 14           | 44+        | US Market Leader + EMEA |
| **Binance**             | 17           | 58+        | Global Coverage         |
| **Kraken**              | 13           | 33+        | US Market Leader        |
| **Bitfinex**            | 12           | 33         | Global Coverage         |
| **Paribu**              | 11           | 42         | Turkey/EMEA             |
| **BtcTurk**             | 10           | 36         | Turkey/EMEA             |
| **Robinhood**           | 8            | 14         | US Retail               |
| **ByBit** - Coming Soon | TBD          | TBD        | Global Coverage         |
| **OKX** - Coming Soon   | TBD          | TBD        | Global Coverage         |

## Wallet Support

### Full Integration (EVM Chains)

* MetaMask
* Coinbase Wallet
* Trust Wallet
* Binance Wallet
* Exodus
* Rainbow
* **+227 more Web3 wallet integrations**

### Solana Wallets

* Phantom
* Trust Wallet
* Exodus
* Solflare
* 1Inch Wallet

For detailed token lists and specific integration details, please refer to the complete API documentation at [docs.meshconnect.com](https://docs.meshconnect.com/).

*Last updated: October 21, 2025*


# null
Source: https://docs.meshconnect.com/testing/error-dictionary



## Possible Ineligibility Reasons

Here are the reasons why holdings cannot be transferred in some cases.

## Configure Transfer Errors

| Error Code                      | Description                                                                                                                                                                | Level Found |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| NoEligibleNetworks              | None of the networks supported by Source and Target accounts can be used for the transfer. Individual reasons specifying why a particular network cannot be used may vary. | Holdings    |
| SymbolDoesNotMatch              | The symbol that was requested for the transfer is different from the holding’s symbol                                                                                      | Holdings    |
| NotSupportedForTransferByTarget | None of the networks for that token are eligible to transfer TO the source. This is often due to the **client** not supporting the token for transfer.                     | Holdings    |
| NotSupportedForTransferBySource | None of the networks for that token are eligible to transfer FROM the source. This is often due to **Mesh or the integration** not supporting the token for transfer.      | Holdings    |
| AmountNotSufficient             | The (amount to be transferred + the gas fee) is more than the available balance                                                                                            | Network     |
| NoTargetNetworkFound            | Target addresses/institution do not contain the corresponding network, so this network cannot be used for the transfer                                                     | Network     |
| GasFeeAssetBalanceNotEnough     | The amount of the asset is sufficient, but there’s not enough balance of the gas fee’s asset (e.g. not enough ETH to send USDC)                                            | Network     |

## Preview Transfer Errors

Statuses:

* Succeeded
* Failed

### Error messages (when status = failed)

| Error Code                                         | Error Message                                                                                                                                                                                                               |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NetworkIdMissing                                   | (TransferToAddress.NetworkId) field was not provided.                                                                                                                                                                       |
| AddressMissing                                     | (TransferToAddress.Address) field was not provided.                                                                                                                                                                         |
| SymbolMissing                                      | (TransferToAddress.Symbol) field was not provided.                                                                                                                                                                          |
| UnsupportedSymbolByNetwork                         | Network does not currently support the requested symbol.                                                                                                                                                                    |
| InvalidAddressPattern                              | Target address does not match network '' address pattern.                                                                                                                                                                   |
| NetworkNotFound                                    | Network not found.                                                                                                                                                                                                          |
| NetworkDisabled                                    | Network '' is currently disabled and cannot be used.                                                                                                                                                                        |
| InsufficientFunds                                  | Insufficient '' funds.                                                                                                                                                                                                      |
| InsufficientFeeFunds                               | Insufficient '' funds for transfer fees.                                                                                                                                                                                    |
| EmptyWalletSymbolBalance                           | Source wallet '' balance is empty.                                                                                                                                                                                          |
| KycRequired                                        | The provided '' account requires KYC to be completed to perform transfers.                                                                                                                                                  |
| DepositAmountTooLow                                | The requested amount is lower than the minimum amount that can be accepted by the target institution.                                                                                                                       |
| WrongPreviewRequestFromAuthTokenMissing            | (PreviewTransferRequest.FromAuthToken) is a mandatory field and should be provided.                                                                                                                                         |
| WrongPreviewRequestNoSymbol                        | (PreviewTransferRequest.Symbol) is a mandatory field and should be provided.                                                                                                                                                |
| WrongPreviewRequestInvalidToAuthToken              | (PreviewTransferRequest.ToAuthToken) is invalid.                                                                                                                                                                            |
| WrongPreviewRequestToData                          | Either (PreviewTransferRequest.ToAuthToken) with (PreviewTransferRequest.ToType) or (PreviewTransferRequest.ToAddress) should be provided.                                                                                  |
| WrongPreviewRequestAmount                          | Both (PreviewTransferRequest.AmountInFiat) and (PreviewTransferRequest.Amount) can not be provided.                                                                                                                         |
| WrongPreviewRequestNoAmount                        | Either (PreviewTransferRequest.AmountInFiat) or (PreviewTransferRequest.Amount) should be provided.                                                                                                                         |
| WrongPreviewRequestUnsupportedSymbolBySourceWallet | Symbol to transfer not supported by the source wallet over the requested network.                                                                                                                                           |
| WrongPreviewRequestUnsupportedSymbolByTargetWallet | Symbol to transfer not supported by the target wallet over the requested network.                                                                                                                                           |
| WrongPreviewRequestNetwork                         | Requested network is not supported by the source wallet.                                                                                                                                                                    |
| PriceNotFound                                      | Could not fetch '' price.                                                                                                                                                                                                   |
| AmountMoreThanWithdrawMaximum                      | Could not preview the transfer. The requested amount (previewRequest.Amount) (requestDto.Request.Symbol) is greater than the maximum allowed amount (minimumMaximumAmount.WithdrawMaximumAmount requestDto.Request.Symbol). |
| AmountLessThanWithdrawMinimum                      | Could not preview the transfer. The requested amount (previewRequest.Amount) (requestDto.Request.Symbol) is below the minimum allowable threshold (minimumMaximumAmount.WithdrawMinimumAmount requestDto.Request.Symbol).   |

## Execute Transfer Errors

Statuses:

* Succeeded
* Failed
* MfaRequired
* EmailConfirmationRequired
* DeviceConfirmationRequired
* MfaFailed
* AddressWhitelistRequired

### Error messages (when status = failed)

| Error Code           | Error Message                         |
| -------------------- | ------------------------------------- |
| PreviewExpired       | The preview is expired.               |
| TransferIsRequested  | The transfer is already requested.    |
| PreviewNotFound      | Could not find the preview.           |
| AddressNotRegistered | The target address is not registered. |


# Sandbox
Source: https://docs.meshconnect.com/testing/sandbox

Learn about the Sandbox environment, its features, limitations, and how to use it for API testing.

## What is the Sandbox?

The Sandbox is a dedicated testing environment that allows you to integrate and interact with our APIs in a safe and controlled manner. It is designed to mirror the Production environment but uses **mocked data** for exchange integrations and **testnet funds** for wallet transactions, ensuring a realistic experience without risking real assets.

### Key Features of the Sandbox

* **Isolated from Production:** Prevents any interference with your live application.
* **Mocked Exchange Data:** Simulates responses from centralized exchanges for testing API calls and transfer flows.
* **On-Chain Wallet Testing:** Supports the **Sepolia testnet** for validating real on-chain transactions with self-custody wallets.
* **Dedicated API Endpoint:** Access the Sandbox API at: `https://sandbox-integration-api.meshconnect.com`.

***

Mesh Sandbox now supports Defi Wallet **transfers using browser extension wallets** for applicable testnet scenarios. This allows developers to test end-to-end flows involving DeFi wallets directly within the Sandbox environment.

### **Supported Browser Extension Wallets & Networks**

* **MetaMask → Sepolia (Ethereum Testnet)**

  Use MetaMask on Sepolia network to test SEPOLIAETH/PYUSD/USDG transfers on Sandbox Environment

* **Phantom → Solana Devnet**

  Use Phantom on SolanaDevnet network to test DEVNETSOL/PYUSD/USDG transfers on Sandbox Environment

These capabilities enable comprehensive testing of token movement and wallet behavior without interacting with mainnet environments.

***

## **How to Test in the Sandbox: A Step-by-Step Guide**

> **‼️ Important: For Development & Testing Only**
>
> The Sandbox environment and Sandbox API keys are designed exclusively for your development and testing phases. **Never** use the Sandbox API endpoint or Sandbox keys in your live production application. Your production application must use your Production API keys and the production endpoint.

#### **Step 1: Get Your Sandbox API Keys**

Before you begin, you must generate API keys specifically for the Sandbox.

1. Go to **Account > API keys** in your Mesh Dashboard.
2. Generate a new key in the **"Sandbox"** section. Remember to store your `Client Secret` securely.

#### **Step 2: Test a Centralized Exchange (CEX) Transfer**

This flow uses mocked data to simulate a transfer from an exchange like Coinbase or Binance.

1. ****`Generate a linkToken:`**** From your backend, make a `POST` request to the Sandbox endpoint (`https://sandbox-integration-api.meshconnect.com/api/v1/linktoken`). Include a `transferOptions` object specifying a destination address.
2. **Initialize the Link SDK:** Pass the `linkToken` to your client-side SDK to open the Link UI.
3. **Select an Exchange:** In the Link UI, choose any supported exchange. You can use any credentials (e.g., "user123"/"pass123") as the data is mocked.
4. **Complete the Transfer:** Follow the on-screen prompts to initiate and confirm the transfer.
5. **Verify the Webhook:** After completing the flow, you should receive a webhook notification with a `succeeded` status for the simulated transfer.

#### **Step 3: Test a Self-Custody Wallet Transfer (On-Chain)**

This flow uses the **Sepolia testnet** to validate a real on-chain transaction without risking actual funds.

1. **Get Sepolia ETH:** To perform a testnet transaction, you need testnet tokens. You can get free Sepolia ETH from a public faucet. A reliable option is the Google Cloud Faucet: [https://cloud.google.com/application/web3/faucet/ethereum/sepolia](https://cloud.google.com/application/web3/faucet/ethereum/sepolia). Send these funds to a test wallet that you control, such as a test MetaMask account.
2. ****`Generate a linkToken:`**** From your backend, make a `POST` request to the Sandbox endpoint. In the `transferOptions`, specify the Sepolia network and a destination address you own.
   * **Token:** Sepolia ETH
   * **Network:** Sepolia
3. **Initialize the Link SDK:** Pass the `linkToken` to your client-side SDK.
4. **Select a Supported Wallet:** In the Link UI, choose one of the supported testnet wallets, such as **MetaMask** or **Rainbow**. Connect the test wallet that holds your Sepolia ETH.
5. **Confirm the Transaction:** You will be prompted by your wallet to sign and approve the on-chain transaction.
6. **Verify the Webhook & On-Chain Transaction:** You will receive a webhook notification once the transaction is confirmed on the Sepolia network. You can also verify this by checking a Sepolia block explorer.

***

### **Limitations of the Sandbox**

* **Mocked Integrations:** All CEX integrations return simulated responses; no real transactions occur.
* **Hardcoded Prices:** Asset prices are hardcoded and do not reflect real market values.
* **Limited Wallet Support:** On-chain testing is currently limited to the Sepolia testnet and a specific set of wallets (MetaMask, Rainbow).

***

## Frequently Asked Questions

<Accordion title="🔹 Can I perform real transactions in the Sandbox?">
  No, the Sandbox does not process real transactions. All payments, asset movements, and third-party API calls return mocked responses for testing purposes.
</Accordion>

<Accordion title="🔹 Does the Sandbox have the same API as Production?">
  Yes, the Sandbox API follows the same structure and endpoints as the Production API, but the responses are simulated.
</Accordion>

<Accordion title="🔹 Are Testnets supported?">
  Currently, Sepolia network is supported for Metamask and Rainbow. Please read more about how to set them up in your sandbox in this [Guide](/guides/quickstart-testnet-sandbox).
</Accordion>

<Accordion title="🔹 Are all exchange integrations supported in the Sandbox the same as in Production?">
  No, the Sandbox API supports Coinbase, Binance, and Robinhood.
</Accordion>

<Accordion title="🔹 How can I allow users to bypass authentication when they return to use Mesh again?">
  * To enable a seamless return experience without prompting users to authenticate again, you can pass a valid `accessToken` into the `createLink()` function when connecting an account via the Mesh Web SDK.
  * If you provide a valid `accessToken`, users will not need to reauthenticate.
  * If you pass **`no integrationId and no accessToken`**, the catalog will open, but users will be required to authenticate again when selecting an already linked integration.
  * **Important:** You must securely store and manage the `accessToken` on your side. For best practices on handling authentication tokens, refer to our guide: [Handling Auth Tokens](https://docs.meshconnect.com/guides/handling-auth-tokens#handling-auth-tokens).
</Accordion>


# Testnets
Source: https://docs.meshconnect.com/testing/testnets



# What It Is

Mesh now supports testnet transactions in our sandbox environment, allowing developers to validate on-chain transactions without risking real funds.

<aside>
  ℹ️

  Currently, we only support the **Sepolia testnet** and **Sepolia ETH** test tokens.
</aside>

# Why It's Important

Previously, our sandbox environment did not support wallet transactions, requiring customers to use real funds for testing. With testnets, developers can now configure transfers using Sepolia testnet and obtain test tokens from a [faucet](https://cloud.google.com/application/web3/faucet/ethereum/sepolia), ensuring a risk-free and seamless integration experience.

## What Are Testnets and Test Tokens?

* **Testnets** are blockchain networks used for testing purposes, replicating mainnet functionality without real economic consequences.
* **Test Tokens** are tokens issued on testnets that simulate real assets, allowing developers to conduct transactions, test smart contracts, and validate integrations before deploying on the mainnet.

By enabling testnet support, we remove a major barrier to integration, speeding up contract signing and reducing implementation friction for prospective PSP clients.

# How to Use It

1. Reference our updated sandbox documentation: [Sandbox Documentation](https://docs.meshconnect.com/guides/sandbox)
2. Access our demo environment: [Mesh Demo Environment](https://dashboard.meshconnect.com/demos/mesh-deposit)
3. Configure a transfer using the following:
   * **Token:** Sepolia ETH

   * **Network:** Sepolia
4. **Obtaining testnet tokens:** There are two ways in which customers can obtain testnet tokens:
   **Acquire test tokens from a faucet**: Customers can obtain Sepolia ETH from a public faucet for testing. e.g. [https://cloud.google.com/application/web3/faucet/ethereum/sepolia](https://cloud.google.com/application/web3/faucet/ethereum/sepolia)

## Additional Notes

* Expanding testnet coverage is part of our future roadmap.
  * Please reach out to product with any additional testnet expansion request.
* Currently, only MetaMask and Rainbow wallets are supported
  * Please reach out to product to enable additional wallet support
* Sales and CS teams should proactively inform customers about this feature to accelerate integration timelines.
* For further assistance, customers should reach out to their assigned CS representative.

## Reference Docs

[https://docs.meshconnect.com/guides/sandbox](https://docs.meshconnect.com/guides/sandbox)


# null
Source: https://docs.meshconnect.com/testing/troubleshooting-link



## Link UI is not displaying in your webpage

**Symptoms:**

* When initializing the Link UI, you see a grey box instead of the Link UI
* An error in the browser's console that says `Refused to frame 'https://web.meshconnect.com/' because an ancestor violates the following Content Security Policy directive...`

![CORS Error](https://files.readme.io/c063393-cors_error.png)

**Causes:**

* When using the Link Web SDK in your page, Mesh SDK loads the Link UI using an iFrame component. Due to security reasons, we allow loading the Link UI only on a predefined set of URLs.
* If you are using a Content Security Policy (CSP) directives on your website, they might block loading an external iFrame into your page.

**Troubleshooting:**

* [ ] &#x20;Add your website's URL to the list of **Allowed Link URLs** in our [dashboard](https://dashboard.meshconnect.com/company/keys).
* [ ] &#x20;Add the following CSP directives to your site:\
  `frame-src: *.meshconnect.com`

# Unable to connect an OAuth integration

**Symptoms:**

* When authenticating on a third party integration's side (e.g., Coinbase or Gemini), the user gets stuck on a page displaying a loading spinner

**Causes:**

* Ad-blocking software is not officially supported with Link UI, and some ad-blockers have been known to cause issues with Link.
* Some browsers have built-in ad-blocking service (Brave Browser) which prevents Link UI from using the browser's storage.

**Troubleshooting:**

* [ ] &#x20;Disable all ad-blockers in your browser


# Transfer Webhooks
Source: https://docs.meshconnect.com/testing/webhooks



If your business relies on transfer status updates to make business decisions (releasing inventory, dispersing funds, etc.), then polling Mesh’s managed transfers endpoint is an inefficient and ineffective solution. Mesh offers webhooks to solve this problem. A webhook is a callback function that allows lightweight, event-driven communication between 2 systems. The events that trigger communications from Mesh’s webhooks are updates to transfer statuses. Instead of polling a Mesh endpoint, you can provide Mesh (via the Dashboard) with a unique callback URL which will automatically receive transfer status updates as Mesh learns about them.

## Secure Data Transmission

* Mesh uses HMAC (Hash-based Message Authentication Code)
* When clients register their Webhook URI, they receive a Secret from Mesh which will be used in signing the request.
* Mesh signs each webhook request using a secret key. The receiver can verify the signature using the same secret key to ensure the data has not been tampered with.
* Mesh will include a signature header (e.g., **`X-Mesh-Signature-256`**) that the receiver can use to validate the integrity and authenticity of the payload.

This is the function we use for creating HMAC signature that is used in the request header:

```csharp theme={null}
 public string GenerateHmacSignature(string payload, string webhookSecret)
    {
        using var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(webhookSecret));
        byte[] hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(payload));
        return Convert.ToBase64String(hash);
    }
```

# Whitelist IP

All the webhook calls from Mesh side will come from this static IP:

```bash theme={null}
20.22.113.37
```

## Webhook Event Model

The webhook payload contains the core information related to a transfer update, and also includes additional fields specific to the webhook event.

### Transfer data

* **`TransferId`** (`Guid`): The unique identifier of the transfer related to this event.
* **`Timestamp`** (`long`): The timestamp indicating when the event occurred.
* **`TransferStatus`** (`string`): The status of the transfer at the time of the event. This is an enumeration representing various possible states of the transfer.
* **`TransactionId`** (`string`): The unique identifier for the transaction associated with the transfer.
* **`TxHash`** (`string`): The unique identifier for the blockchain transaction associated with the transfer.
* **`UserId`** (`string`): The unique identifier of the user associated with the transfer.
* **`Token`** (`string`): The token associated with the transfer.
* **`Chain`** (`string`): The chain associated with the transfer.
* **`SourceAmount`** (`decimal?`): The amount of token that has left the source account.
* **`SourceAccountProvider`** (`string`): The account provider that has been used to send the token.
* **`DestinationAmount`** (`decimal?`): The amount of token that has received by the destination account.
* **`DestinationAddress`** (`string`): The destination account address.
* **`RefundAddress`** (`string`): The refund address (optional).

### Webhook call data

* **`EventId`** (`Guid`): A unique identifier for the event. This event identifies each message sent to clients. This ID will remain same even in case of retries.
* **`Id`** (`Guid`): A unique identifier for the webhook event. This is considered as SentID, there maybe multiple retries for any event pushed into the queue. For each try for sending a specific event there is a different Id.
* **`SentTimestamp`** (`long`): The timestamp indicating when the webhook event was sent.

### Payload

The payload format is JSON. Here is an example of payload.

```json theme={null}
{
  "Id": "358c6ab7-4518-416b-9266-c680fda3a8dd",
  "EventId": "56713e70-be74-4a37-0036-08da97f5941a",
  "SentTimestamp": 1720532648,
  "UserId": "user_id_provided_by_client",
  "TransactionId": "transaction_id_provided_by_client",
  "TransferId": "dd4063e5-f317-441c-3f07-08dc7353b6f8",
  "TransferStatus": "Pending",
  "TxHash": "0x7d4ec1ce50952a377452c95fdf5a787ff551f08c0343093f866c84f57c473495",
  "Chain":"Ethereum",
  "Token":"ETH",
  "DestinationAddress":"0x0Ff0000f0A0f0000F0F000000000ffFf00f0F0f0",
  "SourceAccountProvider" :"Binance",
  "SourceAmount":0.004786046226555188,
  "DestinationAmount":0.004786046226555188,
  "RefundAddress": "0x0Ff0000f0A0f0000F0F000000000ffFf00f0F0f0",
  "Timestamp": 1715175519038
}
```

### Transfer Status Values

* **`pending`**: The transfer has been initiated via Mesh, but has not yet reached a final state. Mesh does not yet have a Transfer Hash for this transfer.
* **`succeeded`**: A final state that indicates the transfer was successfully delivered to the destination address. Mesh has a Transfer Hash for this transfer.
* **`failed`**: A final state that indicates the transfer has failed. No transfer hash available.

### Create and register your callback URI

* Create an endpoint that can receive a POST request with application/json content.
* Go to [Account —> API Keys](https://dashboard.meshconnect.com/company/keys) in your Mesh Dashboard.
* Scroll down to “Production Transfer Webhook URI” and “Sandbox Transfer Webhook URI”

<img alt="Register Webhook" />

* When registering an endpoint, you’ll be prompted to store your secret key, as you won’t be able to view it again.

<img alt="Register Webhook" />

* You can only save one production URI and one Sandbox URI, but you can deactivate one and save a new one at any time.

<img alt="Register Webhook" />

### How to respond to a Mesh webhook event

* Please respond with a **`200`** response in \< 200ms to confirm receipt of the event.
* If Mesh does not receive a **`200`** response in \< 200ms, the webhook will retry (you will receive the event again with all duplicate information except for a different **`Id`**).


