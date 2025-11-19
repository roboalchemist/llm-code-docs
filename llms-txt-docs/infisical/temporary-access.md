# Source: https://infisical.com/docs/documentation/platform/access-controls/temporary-access.md

# Temporary Access

> Learn how to set up timed access to sensitive resources for user and machine identities.

Certain environments and secrets are so sensitive that it is recommended to not give any user permanent access to those. For such use cases, Infisical supports the functionality of **Temporary Access** provisioning.

To provision temporary access through Web UI:

1. Click on the `Edit` button next to the set of roles for user or identities.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/edit-role.png" alt="Edit User Role" />

2. Click `Permanent` next to the role or specific privilege that you want to make temporary.

3. Specify the duration of remporary access (e.g., `1m`, `2h`, `3d`).
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/configure-temporary-access.png" alt="Configure temp access" />

4. Click `Grant`.

5. Click the corresponding `Save` button to enable remporary access.
   <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/access-controls/temporary-access.png" alt="Temporary Access" />

<Note>
  Every user and machine identity should always have at least one permanent role attached to it.
</Note>
