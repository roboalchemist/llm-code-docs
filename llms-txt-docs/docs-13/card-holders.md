# Source: https://docs.solidfi.com/general/card-holders.md

# Card Holders

> A guide to Card Holders

The card holder, a person authorized to use the card, can only be issued a card after successfully passing the necessary OFAC check. This check and other checks (as mandated by the bank per the CIP requirements) are essential in screening and verifying the card holder.

The platform allows for flexibility in the types of card holders, depending on the type of card issued. This adaptability caters to various account holder needs and enhances the user experience.

For example

* In the case of a business spend card, the business is the account holder, and the cardholder is the person(employee) who is authorized to use the business spend card. 
* In the case of a teen card, the parent is the account holder, and the card holder is the child who is authorized to use the card.
* In a typical personal checking account and debit card setup, the account holder is also the card holder.

FinTechs can create both card holder and cards using Solid APIs:

* [Create a Card Holder API](/v2/api-reference/card-holders/create-a-card-holder)
* [Create a Card API](/v2/api-reference/cards/create-a-card)

For more, see the [Card Issuance Guide](/card-issuance/introduction).

<Frame caption="Card Holder hierarchy" type="glass">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/solidfi/images/Card-Holders.svg" />
</Frame>
