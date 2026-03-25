# Source: https://docs.port.io/search-and-query/advanced.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/kubernetes-stack/kubernetes/advanced.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/gitlab/advanced.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/gitlab-v2/advanced.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/github/advanced.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-cloud/advanced.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/bitbucket/bitbucket-app/advanced.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/git/azure-devops/advanced.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/azure/resource_templates/advanced.md

# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-cost/kubecost/advanced.md

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/api/advanced.md

# Advanced

The following advanced query parameters are available:

* Delete Dependents
* Create Missing Related Entities

The `delete_dependents` query parameter is used to enable the deletion of dependent Port entities. This is useful when you have two blueprints with a required relation, and the target entity in the relation should be deleted. In this scenario, the delete operation will fail if this flag is set to `false`, if the flag is set to `true`, the source entity will be deleted as well.

* Available at `DELETE` API endpoint of a specific entity.
* Default: `false` (disabled)
* Use case: Deletion of dependent Port entities. Must be enabled if you want to delete a target entity (and its source entities) when the entity's blueprint has required relations.

The `create_missing_related_entities` parameter is used to enable the creation of missing related Port entities. This is useful when you want to create an entity and its related entity in one call, or if you want to create an entity that its related entity does not exist yet.

In both of these scenarios, the resulting *related* entity will be a barebones entity which you can later on update with relevant information as usual.

* Available at `POST`, `PUT`, `PATCH` API endpoints of a specific entity.
* Default: `false` (disabled)
* Use case: Creation of missing related Port entities. Must be enabled, if you want to create a source entity (and its target related entity) even though the target entity doesn't exist.
