# Source: https://docs.axonius.com/docs/justifications.md

# Justifications

Justifications provide clarity on whether an entitlement assignment is appropriately granted or if it was assigned outside of established policies.

Each entitlement assigned to a user (such as groups, roles, or other forms of access) is evaluated by the platform to determine if it is justified. A justified entitlement has a valid, traceable reason for the user to have it.

Functioning as a directory, a justification records the reasoning behind why a specific entitlement was granted to an identity. It continuously tracks all changes to the entitlement's status, including removals, reassignments, and other modifications.

### Viewing Justifications and Justification History

Justifications and the history of changes are viewed on the Asset Profile page of a managed identity or user.

**To view justifications and justification history:**

1. Go the Managed Identities page or the Users page and select a user.

2. Click the entitlement type, such as **Assigned Groups** or **Assigned Roles**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JustificationsAssignedGroupsRoles.png)

3. A table opens with the list of assigned entitlements.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JustificationsTable.png)

<Callout icon="📘" theme="info">
  Note

  This example shows a user assigned to several groups, all marked with "Is Justified: No." This indicates the entitlements were granted within a third-party application without oversight from within the platform.
</Callout>

4. In the Justifications colunn, click **Justifications**. A table showing the justification history for that entitlement is displayed. This table lists all changes to the status of the justification.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JustificationsHistory.png)

## Justification History Table

The system preserves the full historical justification record for an entitlement in the Justifications table even after it has been removed from an identity. This allows for reporting on past access and understanding the original reasoning behind why it was granted.

<Image alt="JustificationsHistory.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JustificationsHistory.png" />

The Justifications table shows the following information about each justification event related to the selected entitlement:

* **Justifications** - The ID of the justification.
* **Justifications: Date** - Timestamp when the justification was recorded in the system.
* **Justifications** - The name of the justification.
* **Justifications Justification: Type** - The type of justification. See [Justification Types](/docs/justification-types) for a list of all justifications.
* **Justifications: Is Valid** - Indicates whether the justification is valid as the currently approved entitlement status. Only the current/latest entry in the justification history can be 'Is Valid'.

### About the "Is Justified" and "Is Valid" Fields

The "Is Justified" field is a boolean value that indicates the status of the entitlement's justification:

* **True** indicates that the entitlement was properly granted, aligning with governance processes. For example, if an entitlement is granted by a rule or an approved access request, it is considered justified.
* **False** indicates that the entitlement was not properly granted and may require revocation. This can occur if an entitlement is manually assigned by an external administrator or if an Access Review results in its rejection.

It's important to note that the definition of a "justified" entitlement in Axonius is not a universal standard; rather, it reflects a deliberate decision made by an authorized person within the organization.

The "Is Valid" field is a component of each justification record, serving to manage its relevance over time. Its primary function is to determine whether a justification should be actively considered when evaluating an entitlement's current status.

Here are its key characteristics:

* **Balancing History and Current Status** - The field allows the system to maintain a complete, long-term history of every event related to an entitlement—even those that are no longer relevant—while ensuring that the final **Is Justified** status reflects the most recent and valid business logic.
* **Evaluation Logic** - Only justifications with **Is Valid** set to `true` are included in the calculation that determines if an entitlement is justified. If an event occurs that supersedes or negates a previous justification, that older justification's **Is Valid** field is changed to `false`.
* **Example** - If a user's entitlement was initially justified by an approved request, but a subsequent Access Review campaign flagged it for removal, the system would create a new justification record for the rejection. This new record would have **Is Valid: true**, while the original request-based justification would be updated to **Is Valid: false**. This preserves the original record for auditing purposes but ensures it no longer influences the entitlement's current status.
* **Rules for Updating** - The general rule is that a new justification invalidates the `Is Valid` status of the previous one. However, an exception exists for scenarios where multiple rules grant the same entitlement, in which case one rule's justification does not invalidate another's.

In essence, the **Is Valid** field acts as a gatekeeper, allowing the platform to accurately determine an entitlement's present state without losing any of the historical data that provides context for why it was granted in the first place.

#### How `Is Justified` and `Is Valid` Work Together

The **Is Justified** and **Is Valid** fields work together to provide a clear, real-time status of an entitlement while maintaining a complete historical record of its lifecycle.

* The **Is Valid** field is a component of an individual justification record. Its purpose is to determine if a particular justification is relevant to the **current** evaluation of an entitlement. A justification marked with `Is Valid: true` is actively considered by the system, whereas a justification with `Is Valid: false` is preserved in the history but is no longer used to determine the entitlement's current status.

* The **Is Justified** field is the final, top-level status of the entitlement itself. It is a boolean value (`true` or `false`) that is calculated by the system. This calculation assesses all the valid justifications associated with that entitlement to arrive at its current status.

**In practice:**

1. When an entitlement is initially granted (e.g., through a rule), a justification record is created with `Is Valid: true`. Consequently, the entitlement's **Is Justified** status is set to `true`.
2. If a new event occurs that invalidates the original justification (e.g., an Access Review rejects the entitlement), the system adds a new justification record. This new record's `Is Valid` field is set to `true`. Simultaneously, the system updates the original justification record's `Is Valid` field to `false`.
3. The system then recalculates the entitlement's **Is Justified** status. Because the original justification is now marked as invalid, it is ignored, and the new, valid justification (the rejection) drives the final outcome, changing the **Is Justified** status to `false`.

In summary, **Is Valid** is a mechanism for maintaining a long-term, searchable history of all events related to a justification while ensuring that only the most recent and relevant justifications are used to determine the real-time **Is Justified** status of an entitlement.

## Applications of Justifications

Justifications have several valuable applications beyond simple tracking:

* **Access Reviews** - By filtering for entitlements that are not justified, customers can streamline the review process and focus on access that lacks proper oversight.
* **Governance Maturity** - Tracking the ratio of rule-based justifications versus in-app justifications helps customers assess their progress toward a complete Identity Governance and Administration (IGA) solution.

## Special Scenarios in Justifications

The following are some special scenarios related to justfications and explain how justifications work in these cases.

### Justification and Auto-Revocation

When an identity no longer meets the conditions of a rule that granted an entitlement, the revocation subsystem is triggered. Instead of immediately removing the entitlement, the system first checks for any other valid justifications. The entitlement is only revoked if no other valid justification exists.

#### When a Rule Grants an Entitlement after an Access Request

If a rule is created to grant an entitlement that was previously obtained through an approved access request, the rule-based justification will invalidate the request-based justification. This behavior ensures that auto-revocation functions correctly and reflects a more deliberate, scalable approach to entitlement management.

#### Forced Revocation of an Entitlement

An entitlement granted by a rule can be overridden through various processes, such as:

* Rejection during an Access Review campaign.
* Manual removal by an administrator.
* Revocation triggered by a workflow or Entitlement Catalog.

In these cases, a new justification is added that invalidates all previous justifications, marking the entitlement as unjustified.