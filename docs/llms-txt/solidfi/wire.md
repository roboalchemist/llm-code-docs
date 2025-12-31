# Source: https://docs.solidfi.com/payments/wire.md

# Wire

> A guide to Wires

Wires are direct transfers between banks. International wires (and in some cases, domestic wires) usually have intermediary/correspondent banks, which serve as third-party banks that help process and settle transactions. Unlike Intra Account transactions, Wire transactions go through multiple states in their lifecycle before the transaction finally settles:

* Originated: when a transaction is created.
* Pending: when a transaction is waiting to be sent to the bank.
* Clearing: when a transaction has been sent to the bank in the FedWire/MT103 file or via an API.
* Cleared: when the bank has processed the transaction and given Solid the IMAD/OMAD number. The IMAD/OMAD number is a unique number used to locate the transaction if required.
* Settled: when a transaction is marked as settled to indicate the completion of the wire transaction.
* Returned: when the originated wire transaction is returned by the RDFI.

### 1. Domestic Wire

Steps to originate a Domestic Wire transaction:

<Steps>
  <Step title="Create Counterparty">
    Via the Dashboard or the API, [Create a Counterparty](/v2/api-reference/counterparties/create-a-counterparty) with the beneficiary account details in the `domestic_wire` sub-object.
  </Step>

  <Step title="Originate a Domestic Wire Transaction">
    Via the Dashboard or the API, [Originate a Domestic Wire](/v2/api-reference/transactions/originate-a-domestic-wire)
  </Step>

  <Step title="Pass Parameters">
    Pass the necessary parameters (originating sub\_account\_id, counterparty\_id, amount) and other optional parameters as needed.

    ```
    {
      "sub_account_id": "sub_bda1e562657c41e553104b10aad3fe70",
      "counterparty_id": "ctp_8e5541c8a9e50c3af3b0daacf9175130",
      "amount": "25000.00",
      "description": "Invoice 123-9088-2 ",
      "external_reference_id": "123-9088-2"
    }
    ```
  </Step>
</Steps>

<Check>Congratulations, you have now successfully Originated a Domestic Wire transaction!</Check>

### 2. International Wire

Steps to originate an International Wire transaction:

<Steps>
  <Step title="Create Counterparty">
    Via the Dashboard or the API, [Create a Counterparty](/v2/api-reference/counterparties/create-a-counterparty) with the beneficiary account details in the `international_wire` sub-object.
  </Step>

  <Step title="Originate an International Wire Transaction">
    Via the Dashboard or the API, [Originate an International Wire](/v2/api-reference/transactions/originate-an-international-wire)
  </Step>

  <Step title="Pass Parameters">
    Pass the necessary parameters (originating sub\_account\_id, counterparty\_id, amount) and other optional parameters as needed.

    ```
    {
      "sub_account_id": "sub_bda1e562657c41e553104b10aad3fe70",
      "counterparty_id": "ctp_8e5541c8a9e50c3af3b0daacf9175130",
      "amount": "250000.00",
      "description": "Offshore Dev 123-9088-2 ",
      "external_reference_id": "123-9088-2"
    }
    ```
  </Step>
</Steps>

<Check>Congratulations, you have now successfully Originated an International Wire transaction!</Check>

### 3. Wire Cut-off Times

**Originating Wires (both Domestic and International)**: The cut-off time for originating Wires on the same day is 12 pm PT.

**Receiving Wires (both Domestic and International)**: Incoming Wires received by the partner bank before 4 pm PT are made available on the same day.
