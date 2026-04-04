# Source: https://docs.socket.dev/docs/scim.md

# SCIM

SCIM, or System for Cross-domain Identity Management allows for the automation of user provisioning for your Socket organization.

*Available only to Enterprise organizations*

# Overview

SCIM automates user provisioning, updates, and deactivation in Linear directly from your identity provider, removing the overhead of manual account management and ensuring continuous alignment with your organizational directory.

# Configure

## Enable

1. Navigate to <Anchor label="Settings > SCIM" target="_blank" href="http://socket.dev/dashboard/settings/security/scim">Settings > SCIM</Anchor>
2. Click on "Configure"
3. Choose your identity provider
4. Follow the instructions for you identity provider

If the connection was successful, you should now see in the Socket SCIM settings page an "active" label with a green dot and you should see the list of all the SCIM groups pushed to Socket. If you don't see the "active" label, try following the instructions again or contact support.

Note: finishing this configuration also syncs all the new SCIM members to your organization.

# Role syncing

By default, all new SCIM groups will have the "member" role. This means any user that is part of this SCIM group will now have an account created (if not already) with the "member" role.

However, if the user was added previously by other methods (like email invitation, organization link or VCS) they will keep the previous role. SCIM sync will not override any previous member roles. If you want to override them just remove the member from the org and trigger a new sync from your identity provider.

In the Socket SCIM settings page you can change the role mapping for each SCIM group. This will take effect immediately. Note: if a user is a member of multiple groups they will be assigned the most permissive role in this order: "admin", "member" and "contributor". (for example a user with "admin" and "member" roles will have be assigned the "admin" role).

# Manual invitations

You can still invite members to your organization through other methods like email invitation, organization links and VCS.

# Disabling SCIM

If you want to disable SCIM, just click on "Configure" and delete the SCIM connection.

Note: this will remove all members of the org that were added via SCIM, except the "owner" of the organization. This member will never be deleted.