# Source: https://docs.portainer.io/2.33-lts/faqs/upgrading/why-do-my-users-no-longer-have-access-after-upgrading-to-be-from-ce.md

# Source: https://docs.portainer.io/sts/faqs/upgrading/why-do-my-users-no-longer-have-access-after-upgrading-to-be-from-ce.md

# Source: https://docs.portainer.io/faqs/upgrading/why-do-my-users-no-longer-have-access-after-upgrading-to-be-from-ce.md

# Why do my users no longer have access after upgrading to BE from CE?

When upgrading from Portainer Community Edition (CE) to Business Edition (BE), we perform a number of actions on the Portainer database to provide the additional functionality available in Business Edition. One of the BE-exclusive features is Role-based Access Control (RBAC), which provides a more powerful user permission experience.

For security reasons, when the upgrade to BE is performed, any existing users with the **Standard User** role (ie, any users that are not administrators) are assigned to the **Read-Only User** role. This can of course be changed per-environment [after the upgrade](https://docs.portainer.io/faqs/upgrading/broken-reference).
