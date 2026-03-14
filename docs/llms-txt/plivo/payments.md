# Source: https://plivo.com/docs/faq/billing-and-invoices/payments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Payments

> Payment methods, auto-recharge, failed payments, and 3D Secure troubleshooting

Frequently asked questions about payment methods, account recharges, and credits on Plivo.

***

## Payment Methods

<Tabs>
  <Tab title="US + Rest of World">
    ### Accepted payment methods

    | Method            | Availability  | Minimum | Settlement           |
    | ----------------- | ------------- | ------- | -------------------- |
    | Credit Card       | All customers | \$25    | Immediate            |
    | ACH Direct Debit  | US only       | \$25    | 5 business days      |
    | USD Bank Transfer | All customers | —       | Same-day or next-day |

    Accepted cards: Visa, Mastercard, American Express, and Discover. PayPal is not supported.

    A 3% payment gateway fee applies on all card transactions.

    ***

    ### My card payment is failing with 3D Secure / OTP. What should I do?

    Some banks require 3D Secure (3DS) authentication — an additional verification step like an OTP or bank app approval — for online transactions.

    **Troubleshooting steps:**

    1. **Enable pop-ups** — the 3DS verification window opens in a pop-up. Make sure your browser allows pop-ups for the Plivo console.
    2. **Try a different browser** — some browser extensions or privacy settings block the 3DS iframe.
    3. **Check with your bank** — confirm your card is enrolled for 3DS and that online/international transactions are enabled.
    4. **Try a different card** — if the issue persists, use another card from a different issuer.

    If the charge still fails after these steps, contact [Plivo Support](https://support.plivo.com) with the error message shown.

    ***

    ### How do I add a credit card?

    1. Navigate to **Billing** in the Plivo console
    2. Enter card information in the Payment Details section
    3. Click **Add New Card**

    ***

    ### How do I set up ACH Direct Debit (US only)?

    ACH debit requires at least one credit card on file.

    1. Navigate to **Billing** and select bank direct debits
    2. Enter bank account details
    3. Plivo sends a micro-deposit of \$0.01 with a code starting with "SM"
    4. Enter the four digits following "SM" in the console to verify

    Verification typically takes 2-3 days. Maximum 10 verification attempts allowed.

    ***

    ### How do I set up USD Bank Transfer?

    USD Bank Transfer avoids the 3% Payment Gateway Fee charged on credit card payments.

    **Transfer options:**

    * Domestic Wire Transfer: Same-day settlement
    * ACH Transfer: Next-day settlement

    Contact [Plivo Support](https://support.plivo.com) to set up USD Bank Transfer.

    ***

    ### How do I set up wire transfer payments?

    For wire transfers over \$1,000, contact [Plivo Support](https://support.plivo.com) with:

    * Your use case
    * Company details
    * Estimated monthly volume
  </Tab>

  <Tab title="India">
    ### Requirements for India-registered businesses

    | Requirement | Details                                        |
    | ----------- | ---------------------------------------------- |
    | Currency    | INR only                                       |
    | Route Type  | Domestic routes                                |
    | GST         | Required with registration provided in Console |
    | Card Type   | Credit and Debit cards (Indian)                |

    ***

    ### Accepted payment methods

    **Indian Credit/Debit Card:**

    * Minimum: ₹2,000
    * Settlement: Immediate
    * Note: 2% payment gateway fee applies on all card transactions

    ***

    ### GST requirements

    * GST registration details must be entered in the Console
    * 18% GST charged on all invoiced amounts
    * GSTIN must be provided for tax compliance
  </Tab>
</Tabs>

***

## Recharges and Credits

### How do I manually recharge my account?

1. Navigate to **Billing**
2. Enter the recharge amount (minimum \$25 USD or ₹2,000 INR)
3. Complete payment

***

### What is auto-recharge and how does it work?

Auto-recharge automatically adds funds when your balance drops below \$25.

**How it works:**

1. When your balance drops below \$25, Plivo charges your card for the configured recharge amount
2. Choose a recharge amount: $25, $50, $100, $250, $500, or $1,000
3. If a recharge fails, Plivo retries when your balance drops below the threshold again

**Example:** Starting balance $100, recharge amount $100. If a $90 charge reduces the balance to $10 (below $25), auto-recharge triggers and adds $100, resulting in a final balance of \$110.

<Warning>
  **Removing your credit card disables auto-recharge.** If you remove the card on file, auto-recharge stops working and your account may run out of funds. Add a new card and re-enable auto-recharge to resume.
</Warning>

<Note>
  Auto-recharge is not available for India (INR) accounts. INR accounts must recharge manually.
</Note>

***

### How do I configure auto-recharge?

1. Navigate to **Billing**
2. Go to the Auto Recharge section
3. Select a recharge amount ($25, $50, $100, $250, $500, or $1,000)
4. Save

***

### What are monthly recharge limits?

Monthly limits protect against fraudulent activity like SMS pumping or credential leaks.

* The system calculates a recommended limit based on usage
* Limits can be adjusted anytime in the Console
* Some accounts have upper caps based on account history

***

### What balance notifications does Plivo send?

Plivo automatically sends email alerts when your balance drops below $250, $100, and \$10.

**Custom alerts:**

* Configure up to 3 custom threshold amounts
* Add additional notification email addresses via Payment Settings

***

## Related Resources

* [Invoices](/faq/billing-and-invoices/invoices)
* [Taxes](/faq/billing-and-invoices/taxes)
* [Voice Pricing](https://www.plivo.com/pricing/voice/)
* [SMS Pricing](https://www.plivo.com/pricing/sms/)
* [Phone Number Pricing](https://www.plivo.com/virtual-phone-numbers/pricing/)
* [Contact Support](https://support.plivo.com)
