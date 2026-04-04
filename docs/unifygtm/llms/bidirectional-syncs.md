# Source: https://docs.unifygtm.com/reference/integrations/salesforce/bidirectional-syncs.md

# Source: https://docs.unifygtm.com/reference/integrations/hubspot/bidirectional-syncs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unifygtm.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How Bidirectional Syncs Work

> An in-depth explanation of how syncs work between HubSpot and Unify.

# Overview

Unify can create and update HubSpot records in response to Play runs and
sequence enrollments. This page summarizes the rules used to determine when and
how to create or update records in HubSpot.

# Overwriting data

Unify takes a very conservative approach to overwriting existing HubSpot data in
order to make data loss impossible. This approach is based around only a few
simple rules:

* **Creating new records:** When Unify is creating a new HubSpot record, it will
  fill in all properties that are enabled for writing in the field mapping or
  default values.

* **Updating existing records:** Unify will inspect whether the field is empty
  or not. If the field already has a value, it will only be updated if it is a
  Unify-specific field. These fields are prefixed with "Unify" and can be found [here](/reference/integrations/hubspot/field-mappings#available-fields).

These rules apply regardless of how the record was originally created (e.g., by
Unify or externally). If you're looking for more fine-grained control, you can
also limit the permissions granted to the Unify integration user in HubSpot.

# Duplicate prevention

Duplicates are strictly prevented within Unify. When creating new HubSpot
records, Unify will only ever create one record. If there is already an existing
HubSpot record of the same type, Unify will always update it rather than
creating a new one.

However, duplicates are a common problem in HubSpot and may already exist in
your HubSpot instance. In addition, users or other integrations may accidentally
create new duplicates over time.

In order to accommodate this reality, Unify follows specific rules to ensure
predictable behavior when updating duplicated HubSpot records. While Unify
cannot de-duplicate your HubSpot, it will *never* make the problem worse, and
in some situations may be able to help clarify the “source of truth” record.

### Contacts

If there is an existing contact that matches the Unify person being written, it
will be updated. Matches are determined based on email address. If there are no
matches, a new contact will be created.

If there are multiple contacts that match the Unify person, only one will be
updated. Specifically, the contact that was most recently modified within
HubSpot is the one that will be updated.

### Companies

HubSpot companies are written by Unify whenever a contact is created or updated.
They are also written if a HubSpot sync action runs within a Play that is
running on companies.

If there is an existing company that matches the Unify company being written, it
will be updated. Matches are determined based on the domain of the company
website. Domains are normalized, so URLs that redirect to different domains will
not result in duplicates. If there are no matches, a new company will be
created.

If there are multiple companies that match the Unify company, only one will be
updated. Specifically, the company that was most recently modified within
HubSpot will be updated.

### Email Messages

Unify does not update existing email messages in HubSpot; only emails sent
through Unify or received in response to those emails will be written to
HubSpot.

Email messages are written to HubSpot for all emails sent as a part of Unify
sequences if the corresponding person already exists in HubSpot. This means
that in order to write email messages for sequence enrollments, you should
ensure that the person already exists in HubSpot or that you include a Play
action to sync them to HubSpot.
