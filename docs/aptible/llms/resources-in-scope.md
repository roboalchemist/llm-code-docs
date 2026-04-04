# Source: https://www.aptible.com/docs/core-concepts/security-compliance/security-compliance-dashboard/resources-in-scope.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Resources in Scope

Aptible considers any containerized apps, databases, and their associated endpoints across different Aptible environments hosted on your Shared and Dedicated Stacks and users with access to these workloads. Aptible tests each resource for various security controls Aptible has identified as per our [division of responsibilities](https://www.aptible.com/secured-by-aptible).

Aptible splits security controls across different categories that pertain to various pieces of an organization’s overall security posture. These categories include:

* Access Management
* Auditing
* Business Continuity
* Encryption
* Network Protection
* Platform Security
* Vulnerability Management

Every control tests for security safeguard implementation for specific resources in scope. For example, the *Multi-factor Authentication* control tests for the activation and enforcement of [MFA/2FA](/core-concepts/security-compliance/authentication/password-authentication#2-factor-authentication-2fa) on the account level, whereas a control like *Cross-region backups* is applied on the database level, testing whether or not you’ve enabled the auto-creation of [geographically redundant copy of each database backup](/core-concepts/managed-databases/managing-databases/database-backups) for disaster recovery purposes.

You can see resources in scope by clicking on a control of interest.

<img src="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/c30c447-compliance-visibility-resources.jpeg?fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=68a0dee200d0a9c2a4eade0f6a83f6c4" alt="Image" data-og-width="3060" width="3060" data-og-height="1842" height="1842" data-path="images/c30c447-compliance-visibility-resources.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/c30c447-compliance-visibility-resources.jpeg?w=280&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=922d481beb7f071a41f70b019656c32d 280w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/c30c447-compliance-visibility-resources.jpeg?w=560&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=95f29d7d1c414aa223dd8453cce6c3d8 560w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/c30c447-compliance-visibility-resources.jpeg?w=840&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=dceb59faad2e480efe17593a8286d587 840w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/c30c447-compliance-visibility-resources.jpeg?w=1100&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=47fd5ce4b0feeadad152da5dfac66c62 1100w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/c30c447-compliance-visibility-resources.jpeg?w=1650&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=73568b58bd924575385ce8ebfa6314df 1650w, https://mintcdn.com/aptible/2c_c-XH-dAzVOaDu/images/c30c447-compliance-visibility-resources.jpeg?w=2500&fit=max&auto=format&n=2c_c-XH-dAzVOaDu&q=85&s=fe7b88f84cd8dc4ca1a224501f0ab032 2500w" />
