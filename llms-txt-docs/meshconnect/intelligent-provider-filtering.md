# Source: https://docs.meshconnect.com/advanced/intelligent-provider-filtering.md

# Intelligent Provider Filtering in Mesh Link

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
