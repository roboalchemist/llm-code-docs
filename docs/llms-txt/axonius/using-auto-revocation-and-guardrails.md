# Source: https://docs.axonius.com/docs/using-auto-revocation-and-guardrails.md

# Using Automatic Revocation and Guardrails

Use automatic revocation when [creating a rule](https://docs.axonius.com/axonius-help-docs/docs/creating-a-rule) to ensure permissions or access rights granted to a user are **automatically revoked** when the conditions for that permission no longer apply. This enhances security and ensures that users don’t retain access to resources they shouldn’t have anymore. Rules in Axonius use queries within Axonius to determine the granting of entitlements. A rule grants entitlements to the identities that match the query parameters.

How automatic revocation works:

* A rule or permission is granted to a user based that meets the query requirements, such as their role, their group, or admin level. Automatic revocation ensures that if any of these conditions change (e.g., the user leaves the company or their role changes), the permission is automatically revoked.
* When the rule query is run and assets that previously matched the query parameters are no longer returned, i.e. they don't match the query parameters that define what identities are granted the permissions, auto revocation will revoke the permissions granted by that rule.

**Common Use Cases**:

* **User Role Changes**: If a user's role changes (e.g., from "admin" to "user"), permissions specific to the previous role will be automatically revoked.
* **Project Completion**: If a user has permissions granted for a specific project (such as an outside consultant), once the project is completed or they are reassigned, the permissions are revoked.
* **Attribute Changes**: If a user’s attributes change (e.g., a department transfer, a change in clearance level), permissions associated with the old attributes are revoked automatically.

## The Revocation Window

The revocation window is a configurable, specific period of time after a permission's justification from a rule with auto-revocation is removed. If, within this timeframe, all other justifications for the same permission for the same identity also become invalid, the system will automatically revoke the permission. This automatic revocation occurs even if the rules providing those other justifications do not have auto-revocation enabled themselves.

The revocation window protects the user since there may be other reasons the user should still have the permission or the other rule with auto revocation enabled was inaccurate.

### An Example Using the Revocation Window

Suppose you have a certain permission granted to you for two different reasons (Rule A and Rule B).

* **Rule A has auto-revocation:** If the reason for Rule A granting you the permission is no longer valid, Rule A's "justification" for that permission is automatically removed. However, you still have the permission because Rule B's justification is still valid.
* **Rule B does not have auto-revocation:** Even if the reason for Rule B granting you the permission becomes invalid, the permission remains.
* **At some later time, the justification of Rule B becomes invalid.** Since Rule B does not have auto-revocation, the permission wouldn't normally be automatically revoked.

However, the revocation window allows the system to look back in time for a short period. If the justification from Rule A was removed recently (within the justification window time frame), then when Rule B's justification also becomes invalid, the system sees that both original reasons for granting you the permission are now gone. Because Rule A's removal happened within the revocation window, the system will automatically revoke the permission when Rule B becomes invalid, even though Rule B itself doesn't have auto-revocation enabled.

The revocation window allows the system to consider the recent auto-revocation of one rule's justification when evaluating whether to revoke a permission based on another rule that lacks auto-revocation. It helps catch scenarios where all supporting reasons for a permission have recently disappeared.

## Guardrails

When leveraging auto-revocation, guardrails are essential mechanisms that inject intelligence and context into the automated removal of permissions. They act as safety nets, preventing unintended disruptions to critical access by ensuring that auto-revocation respects practical operational needs, compliance mandates, and the necessity of maintaining access for specific individuals or groups.

Guardrails function by applying context-sensitive constraints to the auto-revocation process. This means the system doesn't blindly revoke access based solely on the expiration of a rule. Instead, guardrails consider factors like the user's role, the criticality of the resource, or membership in protected groups.

For example, suppose there is a rule that broadly grants access to a core service for all users. If this rule is configured for auto-revocation, a guardrail can be implemented to recognize and exempt critical roles, such as administrators. Even if the rule's conditions for general users are no longer met and auto-revocation would typically trigger, the guardrail would prevent the revocation from affecting administrators. This ensures they retain uninterrupted access to manage the service, even as access is automatically removed for other users according to the rule's lifecycle.

Guardrails ensure that automation enhances security and efficiency without compromising essential access and without risking operational stability or security oversight.