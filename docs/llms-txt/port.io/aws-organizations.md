# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/aws-organizations.md

# AWS Organizations

<!-- -->

## AWS::Organizations::Account[â](#awsorganizationsaccount "Direct link to AWS::Organizations::Account")

The following example demonstrates how to ingest your AWS Organizations accounts to Port.

#### Organizations Account supported actions[â](#organizations-account-supported-actions "Direct link to Organizations Account supported actions")

The table below summarizes the available actions for ingesting AWS Organizations Account resources in Port:

| Action                                                                                                                  | Description                                                   | Type     | Required AWS Permission             |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | -------- | ----------------------------------- |
| [ListAccountsAction](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)               | Discover organization accounts and retrieve account metadata. | Default  | `organizations:ListAccounts`        |
| [ListTagsForResourceAction](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListTagsForResource.html) | Retrieve tags for the specified account.                      | Optional | `organizations:ListTagsForResource` |
| [ListParentsAction](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListParents.html)                 | Retrieve parent information for the specified account.        | Optional | `organizations:ListParents`         |

Optional Properties Note

Properties of optional actions will not appear in the response unless you explicitly include the action that provides them in your configuration.

You can use the following Port blueprint definitions and integration configuration:

**Organizations Account blueprint (click to expand)**

Create in Port

```
{
  "identifier": "awsOrganizationAccount",
  "description": "This blueprint represents an AWS Organizations Account in our software catalog",
  "title": "Organizations Account",
  "icon": "AWS",
  "schema": {
    "properties": {
      "arn": {
        "type": "string",
        "title": "ARN"
      },
      "email": {
        "type": "string",
        "title": "Email"
      },
      "status": {
        "type": "string",
        "title": "Status"
      },
      "joinedTimestamp": {
        "type": "string",
        "title": "Joined Timestamp"
      },
      "joinedMethod": {
        "type": "string",
        "title": "Joined Method"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {}
}
```

**Organizations Account mapping configuration (click to expand)**

```
resources:
  - kind: AWS::Organizations::Account
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .Properties.Id
          title: .Properties.AccountName
          blueprint: '"awsOrganizationAccount"'
          properties:
            arn: .Properties.Arn
            email: .Properties.Email
            status: .Properties.Status
            joinedTimestamp: .Properties.JoinedTimestamp
            joinedMethod: .Properties.JoinedMethod
```

For more details about Organizations accounts, refer to the [AWS Organizations API documentation](https://docs.aws.amazon.com/organizations/latest/APIReference/Welcome.html).
