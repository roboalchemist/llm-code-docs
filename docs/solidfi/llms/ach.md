# Source: https://docs.solidfi.com/payments/ach.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ACH

> A guide to ACH

Automated Clearing House (ACH) payment is a Push & Pull payment method supported by the Solid platform. An ACH payment occurs when the transaction originator instructs the ACH network to push money to or pull money from an external bank in the US. Unlike Intra Account transactions, ACH transactions go through multiple states in their lifecycle before the transaction finally settles:

* Originated: when an ACH transaction is created.
* Pending: when a transaction is waiting to be sent to the bank.
* Clearing: when a transaction has been sent to the bank in the NACHA file.
* Cleared: when the bank has processed the transaction and given Solid the production trace number. The trace number is a unique number used to locate the transaction if required.
* Settled: when a transaction is marked as settled to indicate the completion of the ACH transaction.
* Returned: When the originating ACH transaction is returned by the RDFI.

While ACH transactions can be somewhat complex, understanding the possible types of ACH transactions is essential. See scenatios below on originating outgoing (push/pull) and receiving incoming (push/pull) ACH transactions.

### 1. Originating ACH Transactions

<AccordionGroup>
  <Accordion title="1a: Originate an ACH Push">
    Sub Account Holder 1 at Partner Bank A wants to push \$100 via ACH to Person 2 at Bank B. In this example, Sub Account Holder 1 is originating the ACH transaction at Partner Bank A, instructing the bank (via Solid's technology) to:<br />
    Debit \$100 from Sub Account Holder 1's Sub Account at Partner Bank A<br />
    Credit \$100 to Person 2's Account at Bank B<br />
    Message: Outgoing<br />
    Method: ACH<br />
    Type: Push<br />
    ODFI (Originating Depository Financial Institution): Partner Bank A<br />
    RDFI (Receiving Depository Financial Institution): Bank B
  </Accordion>

  <Accordion title="1b: Originate an ACH Pull">
    Sub Account Holder 1 (Utility Company) at Partner Bank A wants to pull \$100 via ACH from Person 2 at Bank B. In this example, Sub Account Holder 1 (Utility Company) is originating the ACH transaction at Partner Bank A, instructing the bank (via Solid's technology) to:<br />
    Credit \$100 to Sub Account Holder 1's Sub Account at Partner Bank A<br />
    Debit \$100 from Person 2's Account at Bank B<br />
    Message: Outgoing<br />
    Method: ACH<br />
    Type: Pull<br />
    ODFI (Originating Depository Financial Institution): Partner Bank A<br />
    RDFI (Receiving Depository Financial Institution): Bank B<br />
  </Accordion>
</AccordionGroup>

<Tip>Note that ACH payments can only originate from a Sub Account, not from a Master Account.</Tip>

Steps to originate an ACH payment transaction:

<Steps>
  <Step title="Create Counterparty">
    Via the Dashboard or the API, [Create a Counterparty](/v2/api-reference/counterparties/create-a-counterparty) with the beneficiary account details in the `ach` sub-object.
  </Step>

  <Step title="Originate an ACH Payment Transaction">
    Via the Dashboard or the API, [Originate an ACH Push](/v2/api-reference/transactions/originate-an-ach-push) (where money is pushed to an external Bank Account) or [Originate an ACH Pull](/v2/api-reference/transactions/originate-an-ach-pull) (where money is pulled from an external Bank Account)
  </Step>

  <Step title="Pass Parameters">
    Pass the necessary parameters (originating sub\_account\_id, counterparty\_id, amount) and other optional parameters as needed.

    ```
    {
      "sub_account_id": "sub_bda1e562657c41e553104b10aad3fe70",
      "counterparty_id": "ctp_8e5541c8a9e50c3af3b0daacf9175130",
      "amount": "500.00",
      "description": "May Rent",
      "same_day": "true",
      "effective_date": "2024-04-05",
      "company_entry_description": "Payment",
      "external_reference_id": "123-9088-2"
    }
    ```
  </Step>
</Steps>

<Check>Congratulations, you have now successfully Originated an ACH payment transaction!</Check>

### 2. Receiving ACH Transactions

ACH Transactions received in the Sub Account with an incoming message include essential instructions such as amount, credit/debit, method, and type. Transactions are received via ACH Payment webhooks.

<AccordionGroup>
  <Accordion title="2a: Receiving an ACH Push">
    Person 2 at Bank B wants to push \$100 via ACH to Sub Account Holder 1 at Partner Bank A. In this example, Person 2 is originating the ACH transaction at Bank B, instructing the bank to:<br />
    Debit \$100 from Person 2's Account at Bank B<br />
    Credit \$100 to Sub Account Holder 1's Account at Partner Bank A<br />
    Message: Incoming<br />
    Method: ACH<br />
    Type: Push<br />
    ODFI (Originating Depository Financial Institution): Bank B<br />
    RDFI (Receiving Depository Financial Institution): Partner Bank A
  </Accordion>

  <Accordion title="2b: Receiving an ACH Pull">
    Utility Company at Bank B wants to pull \$100 from via ACH from Sub Account Holder 1 at Partner Bank A. In this example, Utility Company is originating the ACH transaction at Bank B, instructing the bank to:<br />
    Credit \$100 to Utility Company's Account at Bank B<br />
    Debit \$100 from Sub Account Holder 1's Account at Partner Bank A<br />
    Message: Incoming<br />
    Method: ACH<br />
    Type: Pull<br />
    ODFI (Originating Depository Financial Institution): Bank B<br />
    RDFI (Receiving Depository Financial Institution): Partner Bank A<br />
  </Accordion>
</AccordionGroup>

### 3. ACH Cut-off Times

Below are the cut-off times for originating ACH Credit & Debit Transactions (basically, [1a and 1b](/payments/ach#1-originating-ach-transactions)) on banking days.

* 5:15 am PT
* 8:15 am PT
* 12:15 pm PT
* 4:15 pm PT

<Note>For same-day ACH, transfers must be sent before the 12:15 pm cut-off. Anything sent after that will be treated as a next-day ACH.
If you are receiving ACH Credit and debit Transactions (basically, [2a and 2b](/payments/ach#2-receiving-ach-transactions)), we will credit the funds to and debit from Master Account / Sub Account as soon as the RDFI receives the ACH instruction.</Note>

### 4. ACH Returns & Reversals

Next, we dive into the different scenarios surrounding ACH Returns and Reversals.<br />

But first, let's understand the financial institutions (FIs) involved in an ACH transaction:

* ODFI (Originating Depository Financial Institution)
* RDFI (Receiving Depository Financial Institution)

Most banks can do both, meaning they can act as ODFI (that originates the ACH transaction on behalf of their Account Holder) and RDFI (that receives the ACH transaction intended for their Account Holder).

**ACH Returns**<br />
ACH Return is filed by the RDFI to return an ACH payment that was previously originated by an ODFI. ACH Returns are filed in the following scenarios:

<AccordionGroup>
  <Accordion title="1. Not Sufficient Funds (NSF)">
    If the bank account at the RDFI does not have sufficient funds to cover the debited amount, an automatic ACH Return is filed by the RDFI and sent to the Automated Clearing House (ACH), which then notifies the ODFI.<br />
    In [2b](/payments/ach#2-receiving-ach-transactions), if Sub Account Holder 1's account at Partner Bank A does not have sufficient funds to cover the debited amount, the RDFI (Partner Bank A) files an automatic ACH return.
  </Accordion>

  <Accordion title="2. Unauthorized Transaction">
    If the account holder at the RDFI requests a return to the payment due to an unauthorized ACH Debit transaction, an ACH Return is filed by the RDFI and sent to the Automated Clearing House (ACH), which then notifies the ODFI. Solid must receive the request to file the return within 24 hours.<br />
    In [2b](/payments/ach#2-receiving-ach-transactions), if Sub Account Holder 1's account at Partner Bank A does not have sufficient funds to cover the debited amount, the RDFI (Partner Bank A) files an automatic ACH return.
  </Accordion>

  <Accordion title="3. Incorrect Account">
    If the bank account at the RDFI is either invalid, closed, or does not exist, an automatic ACH Return is filed by the RDFI and sent to the Automated Clearing House (ACH), which then notifies the ODFI.<br />
    In [2b](/payments/ach#2-receiving-ach-transactions), if Sub Account Holder 1's account at Partner Bank A is either invalid, closed or does not exist, the RDFI (Partner Bank A) files an automatic ACH return.
  </Accordion>
</AccordionGroup>

See a list of [ACH Return Codes](https://uploads-ssl.webflow.com/66633a8deaa98cd86b9f0eb3/66980f78467135c36869e194_ACH-Return-Codes.pdf).

**ACH Reversals**<br />
The ODFI files an ACH Reversal to reverse the ACH payment that the ODFI previously originated, most likely due to an error (such as an incorrect amount, duplicate transaction, or incorrect account). ACH Reversals are filed in the following scenarios:

<AccordionGroup>
  <Accordion title="1. Incorrect Amount">
    If an incorrect dollar amount was credited to or debited from another bank account, the ODFI can file an attempt to reverse the transaction and send it to the Automated Clearing House (ACH), which then notifies the RDFI. Solid must receive the request to file the return within 24 hours.<br />
    In [1a](/payments/ach#1-originating-ach-transactions), if Person 2's Account at Bank B was credited with an incorrect dollar amount, then Partner Bank A (the ODFI) can file an attempt to reverse the transaction. 
  </Accordion>

  <Accordion title="2. Duplicate Transaction">
    If a duplicate transaction of the same dollar amount was credited to or debited from another bank account, the ODFI can file an attempt to reverse the transaction and send it to the Automated Clearing House (ACH), which then notifies the RDFI. Solid must receive the request to file the return within 24 hours.<br />
    In [1a](/payments/ach#1-originating-ach-transactions), if Person 2's Account at Bank B was credited with a duplicate transaction of the same dollar amount, then Partner Bank A (the ODFI) can file an attempt to reverse the transaction. 
  </Accordion>

  <Accordion title="3. Incorrect Account">
    If the ODFI sends a payment to an incorrect account, the ODFI can file an attempt to reverse the transaction and send it to the Automated Clearing House (ACH), which notifies the RDFI. Solid must receive the request to file the return within 24 hours.<br />
    In [1a](/payments/ach#1-originating-ach-transactions), if Person 2's Account at Bank B was incorrect, then Partner Bank A (the ODFI) can file an attempt to reverse the transaction. 
  </Accordion>
</AccordionGroup>

<Warning>ACH Reversals are not guaranteed to be honored by the RDFI, as the funds have already been debited or credited and may not exist in the account at the RDFI. The RDFI has 48 hours to respond to the ACH Reversal request.</Warning>
