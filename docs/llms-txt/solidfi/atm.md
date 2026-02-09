# Source: https://docs.solidfi.com/card-issuance/atm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ATM

> A guide to Automated Teller Machines (ATM).

Cards issued on Solid allow cash withdrawals at ATMs. The ATM feature must be enabled, the PIN must be set, and the entered PIN must match the set PIN when entering an ATM. You can also authorize or decline ATM transactions in real time.

### 1. PIN

A Card PIN, or Personal Identification Number, is a 4-digit code unique to each solid-issued card. It ensures that the cardholder is making the transaction. The Card PIN could be required at an ATM or at certain point-of-sale (POS) devices, where it must be entered to complete the transaction.

By default, the card does not have a PIN set. A new PIN can be set by calling the Set a New PIN API.

### 2. ATM Transactions

ATM PIN transactions involve the cardholder using their card to withdraw cash by verifying the transaction using a secret PIN. Here is how the process works:

1. Card Insertion: The cardholder inserts the card into the ATM's card reader,
2. PIN Entry: The cardholder enters their secret PIN on the keypad to authenticate the transaction. This is a security measure to ensure that the person using the card is the legitimate cardholder.
3. Authorization: The ATM communicates with the bank or financial institution that issued the debit card to seek transaction authorization.
4. Transaction Approval or Decline: After PIN verification, the transaction is either approved, with funds deducted from the cardholder's account or declined due to insufficient funds or other issues.

### 3. ATM Access & Locations

Solid has partnered with MoneyPass® to provide surcharge-free ATM access when a Solid issued card is used. MoneyPass® has over 37,000 ATMs nationwide to offer easy access to the funds in the associated account. The FinTech program is responsible for the MoneyPass® transaction fee (refer to the provided fee schedule).

If the Solid issued card is used at an ATM outside of the MoneyPass® network, the fee is disclosed to the end-user at the ATM before the transaction.

You can find MoneyPass® ATMs by searching your zip code on their [ATM locator website](https://www.moneypass.com/index.html). Alternatively, your end user can download the MoneyPass® ATM Locator app, available on the app store. Solid also provides a List all ATM API to list ten nearby MoneyPass® ATMs.

ATM access can be enabled or disabled for the card. By default, it is enabled ("atm\_enabled": true). When Creating a Card or Updating a Card, set "atm\_enabled": false to restrict ATM access.
