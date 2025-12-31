# Source: https://docs.unifygtm.com/reference/integrations/salesforce/bidirectional-syncs.md

# How Bidirectional Syncs Work

> An in-depth explanation of how syncs work between Salesforce and Unify.

# Overview

Unify can create and update Salesforce records in response to Play runs and
sequence enrollments. This page summarizes the rules used to determine when and
how to create or update records in Salesforce.

# Overwriting data

Unify takes a very conservative approach to overwriting existing Salesforce
data in order to make data loss impossible. This approach is based around only
a few simple rules:

* **Creating new records:** When Unify is creating a new Salesforce record, it
  will fill in all fields that are enabled for writing in the field mapping or
  default values.

* **Updating existing records:** Unify will inspect whether the field is empty
  or not. If the field is empty, it will be updated with the new value. If the
  field already has a value, it will only be updated if it is a Unify-specific
  field. These fields are prefixed with "Unify" and can be found [here](/reference/integrations/salesforce/field-mappings#available-fields).

These rules apply regardless of how the record was originally created (e.g., by
Unify or externally). If you're looking for more fine-grained control, you can
also limit the permissions granted to the Unify integration user in Salesforce.

# Duplicate prevention

Duplicates are strictly prevented within Unify. When creating new Salesforce
records, Unify will only ever create one record. If there is already an existing
Salesforce record of the same type, Unify will always update it rather than
creating a new one.

However, duplicates are a common problem in Salesforce and may already exist in
your Salesforce instance. In addition, users or other integrations may
accidentally create new duplicates over time.

In order to accommodate this reality, Unify follows specific rules to ensure
predictable behavior when updating duplicated Salesforce records. While Unify
cannot de-duplicate your Salesforce, it will *never* make the problem worse, and
in some situations may be able to help clarify the “source of truth” record.

### Contacts

Salesforce contacts are written by Unify if **Create new records as Contacts & Accounts**
is selected. In addition, contacts are sometimes created in place of leads if
the person being written to Salesforce *already exists* as a contact. Unify
cannot create a lead in this situation due to Salesforce’s
[contact duplicate rules](https://help.salesforce.com/s/articleView?language=en_US\&id=sf.duplicate_rules_standard_contact_rule.htm\&type=5).

In both situations, if there is an existing contact that matches the Unify
person being written, it will be updated. Matches are determined based on email
address. If there are no matches, a new contact will be created.

If there are multiple contacts that match the Unify person, only one will be
updated. Specifically, the contact that was most recently modified within
Salesforce is the one that will be updated.

### Accounts

Salesforce accounts are written by Unify whenever a contact is created or
updated. They are also written if a Salesforce sync action runs within a Play
that is running on companies.

If there is an existing account that matches the Unify company being written, it
will be updated. Matches are determined based on the domain of the company
website. Domains are normalized, so URLs that redirect to different domains will
not result in duplicates. If there are no matches, a new account will be
created.

If there are multiple accounts that match the Unify company, only one will be
updated. Specifically:

* If one account has more associated contacts than the other(s), that one will
  be updated
* Otherwise, the account that was most recently modified within Salesforce will
  be updated

### Leads

Salesforce leads are written by Unify when **Create new records as Leads** is
selected.

If there is an existing lead that matches the Unify company being written, it
will be updated. Matches are determined based on email address. If there are no
matches, a new lead will be created.

If there are multiple leads that match the Unify person, only one will be
updated. Specifically, the lead that was most recently modified within
Salesforce is the one that will be updated.

### Email Messages

Unify writes to the email message object in Salesforce, which is the recommended
approach for syncing email data to Salesforce. In order to write records of this
object type, the *Enhanced Email* feature must be enabled in Salesforce. This is
typically enabled by default.

Unify does not update existing email messages in Salesforce; only emails sent
through Unify or received in response to those emails will be written to
Salesforce. Unify uses the standard **Universal Message ID** to deduplicate
email messages if they are simultaneously being written by another integration.

Email messages are written to Salesforce for all emails sent as a part of Unify
sequences if the corresponding person already exists in Salesforce. This means
that in order to write email messages for sequence enrollments, you should
ensure that the person already exists in Salesforce or that you include a Play
action to sync them to Salesforce.
