# Source: https://docs.portainer.io/2.33-lts/faqs/getting-started/why-shouldnt-i-give-all-portainer-users-admin-access.md

# Source: https://docs.portainer.io/sts/faqs/getting-started/why-shouldnt-i-give-all-portainer-users-admin-access.md

# Source: https://docs.portainer.io/faqs/getting-started/why-shouldnt-i-give-all-portainer-users-admin-access.md

# Why shouldn’t I give all Portainer users admin access?

Giving every user admin access in Portainer is risky because admins can modify or delete anything, including stacks, registries and production workloads. Instead, use [role-based access](https://docs.portainer.io/admin/user/roles) and assign only the access each person needs.&#x20;

Restricting admin rights prevents accidental changes, limits the impact of mistakes, maintains separation of duties, and improves auditability. Admin access should be reserved for those who manage Portainer itself or handle cluster level configuration. Most users can deploy and manage their own apps without needing admin privileges. Treat admin access as highly privileged and review permissions regularly.
