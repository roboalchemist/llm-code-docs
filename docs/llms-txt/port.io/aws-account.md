# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/aws-account.md

# AWS Account

<!-- -->

## AWS::Account::Info[â](#awsaccountinfo "Direct link to AWS::Account::Info")

The following example demonstrates how to ingest AWS account information using a custom resource designed for account resync without AWS Organizations permissions.

Custom Resource for Account Resync

Use `AWS::Account::Info` to resync AWS account data when you do not have organization-level permissions. If you do have AWS Organizations permissions and want to retrieve richer data (e.g., org account metadata, parents, and tags), see the AWS Organizations documentation under [AWS Organizations](/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/aws-organizations/.md).

You can use the following Port blueprint definitions and integration configuration:

**AWS Account blueprint (click to expand)**

Create in Port

```
{
  "identifier": "awsAccount",
  "title": "AWS Account",
  "icon": "AWS",
  "schema": {
    "properties": {},
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {}
}
```

**AWS Account info mapping configuration (click to expand)**

```
resources:
  - kind: AWS::Account::Info
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.Id
          title: .Properties.Name
          blueprint: '"awsAccount"'
```
