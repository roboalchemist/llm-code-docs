# Source: https://docs.solidfi.com/payments/intra-account.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Intra Account

> A guide to Intra Account (On-Us)

Intra Account is a Push & Pull payment method supported by the Solid platform. Money movement between Sub Accounts are basically Intra Account (On-Us) transactions.

Steps to originate an Intra Account (On-Us) payment transaction:

<Steps>
  <Step title="Create Counterparty">
    Via the Dashboard or the API, [Create a Counterparty](/v2/api-reference/counterparties/create-a-counterparty) with the beneficiary account details in the `intra_account` sub-object.
  </Step>

  <Step title="Originate an Intra Account (On-Us) Transaction">
    Via the Dashboard or the API, [Originate an Intra Account Push](/v2/api-reference/transactions/originate-an-intra-account-push) (where money is pushed to another Sub Account) or [Originate an Intra Account Pull](/v2/api-reference/transactions/originate-an-intra-account-pull) (where money is pulled from another Sub Account)
  </Step>

  <Step title="Pass Parameters">
    Pass the necessary parameters (originating sub\_account\_id, counterparty\_id, amount) and other optional parameters as needed.

    ```
    {
      "sub_account_id": "sub_bda1e562657c41e553104b10aad3fe70",
      "counterparty_id": "ctp_8e5541c8a9e50c3af3b0daacf9175130",
      "amount": "4570.00",
      "description": "May Salary",
      "external_reference_id": "123-9088-2"
    }
    ```
  </Step>
</Steps>

<Check>Congratulations, you have now successfully Originated an Intra Account (On-Us) transaction!</Check>

**Settlement Time**: Instant
