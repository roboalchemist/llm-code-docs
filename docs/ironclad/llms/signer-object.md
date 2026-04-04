# Source: https://clickwrap-developer.ironcladapp.com/docs/signer-object.md

# Signer Object

A Signer in Ironclad Clickwrap refers to the counterparty accepting the contract. Signer objects in Ironclad are uniquely identified by the `signer_id`, which can be any string but are most commonly one of the following:

* Email address
* User ID
* Account UUID

# Creating a New Signer

Signer objects are automatically created in Ironclad Clickwrap whenever a new `signer_id` is passed with an acceptance. The new Signer object will contain any `custom_data` attributes sent with the acceptance.

## Default Properties

Ironclad has a few reserved `custom_data` properties for signer attributes that are recommended and will appear conveniently in certain in-app locations throughout the Ironclad UI. These are indicated below:

* first\_name, last\_name OR name (equivalent)
* company\_name
* title
* email (important for clickwrap notification acceptance email)
* mobile\_number

## Custom Properties

Signer objects can also include **any** custom property keys you’d like, and you will be able to use them as filters to  locate the relevant Signer records.

# Updating Existing Signers

Importantly, if you pass an existing `signer_id` with an acceptance, the existing Signer object will be associated to the record, but by default its attributes **will not** be overwritten by the new `custom_data`.

To update existing Signer objects, you can do so at any time by sending an ‘updated’ event to Ironclad. See [here](https://clickwrap-developer.ironcladapp.com/docs/loading-a-clickwrap-101#sending-acceptance-with-custom-data) for more information.

## Counterparty as an Entity

When your counterparty is an entity rather than an individual, it is often best practice to supply a unique account id as the `signer_id`. This way the Signer is generally applicable to the entire counterparty corporation rather than tied to an individual who might not be with the company forever. In addition, if the counterparty entity ever changes its legal name, you can send an ‘updated’ event to Ironclad and update how the counterparty’s name will appear in the records.

## Clickwrap Acceptance Confirmation Email

If an email address is specified on the Signer object (as either the `signer_id` or in the email field), then this can be used to send an acceptance confirmation email from Ironclad to the counterparty at the time of acceptance. Click [here]() for more information on sending a confirmation email to your counterparty signers.