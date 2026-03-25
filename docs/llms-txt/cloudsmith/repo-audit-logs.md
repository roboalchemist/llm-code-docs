# Source: https://help.cloudsmith.io/docs/repo-audit-logs.md

# Audit Logs

The Repository Audit Log is a timeline view of non-package (but typically administrative) actions that have occurred within the repository, such as creating/modifying repository [Retention Rules](https://help.cloudsmith.io/docs/retention-lifecycle) or creation of an [Entitlement Token](https://help.cloudsmith.io/docs/entitlements).

<Image title="repo-audit-logs.png" alt={1322} align="center" src="https://files.readme.io/1e87b6f90c7bcabb9be54803142924dcd0acfb5f51e69d4adcf56965440f5628-Screenshot_2024-10-18_at_22.32.21.png">
  Repository Audit Logs
</Image>

## 🔐 Audit Log Event Types (Repository)

The following events are logged for repository-level actions, including package changes, key management, entitlement tokens, retention rules, and more.

| **Event**                         | **Identifier**                            | **Description**                                    | **Content Type** |
| --------------------------------- | ----------------------------------------- | -------------------------------------------------- | ---------------- |
| Repository Created                | `repo.created`                            | Created a new repository.                          | Repo             |
| Repository Deleted                | `repo.deleted`                            | Deleted a repository.                              | Repo             |
| EULA Enforcement Enabled          | `repo.eula_enforcement_enabled`           | Enabled EULA enforcement on a repository.          | Repo             |
| EULA Enforcement Disabled         | `repo.eula_enforcement_disabled`          | Disabled EULA enforcement on a repository.         | Repo             |
| Retention Rules Enabled           | `repo.retention_enabled`                  | Enabled retention rules on a repository.           | Repo             |
| Retention Rules Disabled          | `repo.retention_disabled`                 | Disabled retention rules on a repository.          | Repo             |
| Retention Days Updated            | `repo.retention_days_updated`             | Updated 'limit by days' rule for retention.        | Repo             |
| Retention Count Updated           | `repo.retention_count_limit_updated`      | Updated 'limit by count' rule for retention.       | Repo             |
| Retention Size Updated            | `repo.retention_size_limit_updated`       | Updated 'limit by size' rule for retention.        | Repo             |
| Retention Group by Name Updated   | `repo.retention_group_by_name_updated`    | Updated retention rule to group by package name.   | Repo             |
| Retention Group by Format Updated | `repo.retention_group_by_backend_updated` | Updated retention rule to group by package format. | Repo             |
| Retention Group by Type Updated   | `repo.retention_group_by_type_updated`    | Updated retention rule to group by package type.   | Repo             |
| Storage Region Updated            | `repo.storage_region_updated`             | Changed the storage region of a repository.        | Repo             |
| Verify Signatures Enabled         | `repo.verify_signatures_enabled`          | Enabled signature verification for packages.       | Repo             |
| Verify Signatures Disabled        | `repo.verify_signatures_disabled`         | Disabled signature verification for packages.      | Repo             |
| Entitlement Tokens Synced         | `repo.token_synced`                       | Synced entitlement tokens for the repository.      | Repo             |
| Cache Rule Created                | `repo.edge_cache.created`                 | Created a new edge cache rule.                     | Repo             |
| Cache Rule Deleted                | `repo.edge_cache.deleted`                 | Deleted an edge cache rule.                        | Repo             |
| Cache Metadata TTL Updated        | `repo.edge_cache.dynamic_ttl_updated`     | Updated metadata TTL for edge caching.             | Repo             |
| Cache Storage TTL Updated         | `repo.edge_cache.storage_ttl_updated`     | Updated package TTL for edge caching.              | Repo             |
| Entitlement Token Created         | `repo.entitlement.created`                | Created an entitlement token.                      | Repo             |
| Entitlement Token Deleted         | `repo.entitlement.deleted`                | Deleted an entitlement token.                      | Repo             |
| Entitlement Token Enabled         | `repo.entitlement.enabled`                | Enabled an entitlement token.                      | Repo             |
| Entitlement Token Disabled        | `repo.entitlement.disabled`               | Disabled an entitlement token.                     | Repo             |
| Entitlement Token Secret Updated  | `repo.entitlement.secret_updated`         | Updated the secret for an entitlement token.       | Repo             |
| EULA Revision Created             | `repo.eula.created`                       | Created a new EULA revision.                       | Repo             |
| EULA Revision Deleted             | `repo.eula.deleted`                       | Deleted a EULA revision.                           | Repo             |
| EULA Content Updated              | `repo.eula.content_updated`               | Updated the content of a EULA revision.            | Repo             |
| EULA Identifier Updated           | `repo.eula.identifier_updated`            | Updated the identifier of a EULA revision.         | Repo             |
| GPG Key Created                   | `repo.gpg_key.created`                    | Created a GPG key for the repository.              | Repo             |
| GPG Key Deleted                   | `repo.gpg_key.deleted`                    | Deleted a GPG key from the repository.             | Repo             |
| GPG Key Enabled                   | `repo.gpg_key.enabled`                    | Enabled a GPG key.                                 | Repo             |
| GPG Key Disabled                  | `repo.gpg_key.disabled`                   | Disabled a GPG key.                                | Repo             |
| GPG Key Set as Default            | `repo.gpg_key.updated_default`            | Set a GPG key as the default for signing.          | Repo             |
| RSA Key Created                   | `repo.rsa_key.created`                    | Created an RSA key for the repository.             | Repo             |
| RSA Key Deleted                   | `repo.rsa_key.deleted`                    | Deleted an RSA key from the repository.            | Repo             |
| RSA Key Enabled                   | `repo.rsa_key.enabled`                    | Enabled an RSA key.                                | Repo             |
| RSA Key Disabled                  | `repo.rsa_key.disabled`                   | Disabled an RSA key.                               | Repo             |
| RSA Key Set as Default            | `repo.rsa_key.updated_default`            | Set an RSA key as the default for signing.         | Repo             |
| Signature Key Created             | `repo.signature_key.created`              | Created a signature key.                           | Repo             |
| Signature Key Deleted             | `repo.signature_key.deleted`              | Deleted a signature key.                           | Repo             |
| Signature Key Type Changed        | `repo.signature_key.type_changed`         | Changed the type of a repository signature key.    | Repo             |

Please see our documentation on organizational [Audit Logs](https://help.cloudsmith.io/docs/org-audit-logs) for further details on Audit Log contents and searching/filtering Audit logs.