# Source: https://docs.solidfi.com/payments/check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Check

> A guide to Checks

Check is a paper document that delivers funds from one account to another (usually at different banks), via the Check Clearing House.

The Check has information such as Payor, Payee, Date, Amount, Memo, and Signature.

* The Payor writes the information on the Check issued by the Payor's Bank.
* The Payee deposits the Check that is issued by the Payee's Bank.

Using the information on the Check (such as the Payor's Account Number and Routing Number and amount), the Check authorizes the Payee's Bank (ODFI) to pull the funds from the Payor's Bank (RDFI) account and deposit them into the Payee's Bank Account.

Solid's Payment capabilities support both – 

* issuing and mailing a physical check ([Originate a Check Send](/v2/api-reference/transactions/originate-a-check-send)) on behalf of the Payor
* depositing a check ([Originate a Check Deposit](/v2/api-reference/transactions/originate-a-check-deposit))
