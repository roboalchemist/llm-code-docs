# Nomic Documentation

Source: https://docs.nomic.ai/platform/account/security-and-rbac

Nomic Atlas implements organization-level and dataset-level role-based access controls (RBAC).

## Organization Role-Based Access Controls​

Every Atlas user belongs to one or more organizations. Every user in an organization has one of the following roles and associated permissions.

## Dataset Role-Based Access Controls​

Users within an organization perform actions on their own organizations' datasets. The dataset's creator and the organization's owner and admins are all admins on the dataset. Dataset admins can grant users in the organization the following roles and permissions.

Organization-level roles supersede dataset-level roles. For example, all organization owners and admins
automatically have full-access to all datasets.

## Default Organization Roles on Datasets​

## API Key Scoping​

You can create Nomic API keys scoped with different permissions levels using our API Key admin endpoints.

By default, API keys are scoped to an organization. Additionally, API keys can also be scoped to a specific dataset or a specific user.

If only key_name is provided in the request for creating an API key, the key will be scoped to the user's current organization.

To scope an API key to a specific organization by ID, set key_scope = "ORGANIZATION" and key_target_id with the UUID of the organization in the API key creation request.

To scope an API key to a specific dataset, set key_scope = "DATASET" and key_target_id with the UUID of the dataset in the API key creation request.

To scope an API key to a specific user, set key_scope = "USER" in the API key creation request.

## Who can see my datasets?​

When you create a dataset, you can toggle it as public or restricted in your dataset's page settings.

Public datasets are accessible by anyone with a link in your Atlas deployment.

Restricted datasets are only accessible by authenticated individuals in your organization.

Atlas Client Restricted Map Example

```
from nomic import AtlasDatasetdataset = AtlasDataset(    'my_organization/dataset_name',     is_public=False)dataset.add_data(private_data)atlas_map = dataset.create_index(    indexed_field='your_field_to_embed',)
```

## Creating datasets in organizations​

You can create datasets under any organization you are apart of by specifying an organization_slug prefix in the dataset identifier.

```
organization_slug
```

For example, we can create a dataset in the sterling-cooper organization called my-dataset by specifying sterling-cooper/my-dataset
as the dataset identifier.

```
sterling-cooper
```

```
my-dataset
```

```
sterling-cooper/my-dataset
```

- Organization Role-Based Access Controls
- Dataset Role-Based Access Controls
- Default Organization Roles on Datasets
- API Key Scoping
- Who can see my datasets?
- Creating datasets in organizations
