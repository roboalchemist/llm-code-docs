# Source: https://docs.solidfi.com/general/account-holders.md

# Account Holders

> A guide to Account Holders

The account holder is a person or business that owns the account. The account holder needs to be fully verified as per the bank's CIP requirement before creating an account for the account holder.

There are two types of account holders.

1. Master Account Holder: The master account holder, typically a business and often the FinTech itself, is the entity that owns the master account. This role is of significant importance as the master account holder and the master account are provisioned by Solid at the time of onboarding, tailored to the specific needs of FinTech. For more details, refer to the [Master Accounts Guide](/accounts/master-accounts).

2. Sub Account Holder: The sub account holder can be a person or a business, depending on the FinTech's use case. The sub account holder owns the sub account and the funds in it. FinTechs can create both a sub account holder and sub account using Solid APIs.

* Create a [Sub Account Holder API](/v2/api-reference/sub-account-holders/create-a-sub-account-holder)
* Create a [Sub Account API](/v2/api-reference/sub-accounts/create-a-sub-account)

For more, see the [Sub Accounts Guide](/accounts/sub-accounts).

<Frame caption="Account Holder hierarchy" type="glass">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/solidfi/images/Account-Holders.svg" />
</Frame>
