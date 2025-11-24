# Source: https://infisical.com/docs/documentation/platform/dynamic-secrets/aws-elasticache.md

# AWS ElastiCache

> Learn how to dynamically generate AWS ElastiCache user credentials.

The Infisical AWS ElastiCache dynamic secret allows you to generate AWS ElastiCache credentials on demand based on configured role.

## Prerequisites

2. Create an AWS IAM user with the following permissions:

```json  theme={"dark"}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Action": [
        "elasticache:DescribeUsers",
        "elasticache:ModifyUser",
        "elasticache:CreateUser",
        "elasticache:CreateUserGroup",
        "elasticache:DeleteUser",
        "elasticache:DescribeReplicationGroups",
        "elasticache:DescribeUserGroups",
        "elasticache:ModifyReplicationGroup",
        "elasticache:ModifyUserGroup"
      ],
      "Resource": "arn:aws:elasticache:<region>:<account-id>:user:*"
    }
  ]
}
```

3. Create an access key ID and secret access key for the user you created in the previous step. You will need these to configure the Infisical dynamic secret.

<Note>
  New leases may take up-to a couple of minutes before ElastiCache has the chance to complete their configuration.
  It is recommended to use a retry strategy when establishing new ElastiCache connections.
  This may prevent errors when trying to use a password that isn't yet live on the targeted ElastiCache cluster.

  While a leasing is being created, you will be unable to create new leases for the same dynamic secret.
</Note>

<Note>
  Please ensure that your ElastiCache cluster has transit encryption enabled and set to required. This is required for the dynamic secret to work.
</Note>

## Set up Dynamic Secrets with AWS ElastiCache

<Steps>
  <Step title="Open Secret Overview Dashboard">
    Open the Secret Overview dashboard and select the environment in which you would like to add a dynamic secret.
  </Step>

  <Step title="Click on the 'Add Dynamic Secret' button">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/add-dynamic-secret-button.png" alt="Add Dynamic Secret Button" />
  </Step>

  <Step title="Select AWS ElastiCache">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-modal-aws-elasti-cache.png" alt="Dynamic Secret Modal" />
  </Step>

  <Step title="Provide the inputs for dynamic secret parameters">
    <ParamField path="Secret Name" type="string" required>
      Name by which you want the secret to be referenced
    </ParamField>

    <ParamField path="Default TTL" type="string" required>
      Default time-to-live for a generated secret (it is possible to modify this value after a secret is generated)
    </ParamField>

    <ParamField path="Max TTL" type="string" required>
      Maximum time-to-live for a generated secret.
    </ParamField>

    <ParamField path="Region" type="string" required>
      The region that the ElastiCache cluster is located in. *(e.g. us-east-1)*
    </ParamField>

    <ParamField path="Access Key ID" type="string" required>
      This is the access key ID of the AWS IAM user you created in the prerequisites. This will be used to provision and manage the dynamic secret leases.
    </ParamField>

    <ParamField path="Secret Access Key" type="string" required>
      This is the secret access key of the AWS IAM user you created in the prerequisites. This will be used to provision and manage the dynamic secret leases.
    </ParamField>

    <ParamField path="CA(SSL)" type="string">
      A CA may be required if your DB requires it for incoming connections. This is often the case when connecting to a managed service.
    </ParamField>
  </Step>

  <Step title="(Optional) Modify ElastiCache Statements">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/modify-elasticache-statement.png" alt="Modify ElastiCache Statements Modal" />

    <ParamField path="Username Template" type="string" default="{{randomUsername}}">
      Specifies a template for generating usernames. This field allows customization of how usernames are automatically created.

      Allowed template variables are

      * `{{randomUsername}}`: Random username string
      * `{{unixTimestamp}}`: Current Unix timestamp
      * `{{identity.name}}`: Name of the identity that is generating the secret
      * `{{random N}}`: Random string of N characters

      Allowed template functions are

      * `truncate`: Truncates a string to a specified length
      * `replace`: Replaces a substring with another value

      Examples:

      ```
      {{randomUsername}}                              // 3POnzeFyK9gW2nioK0q2gMjr6CZqsRiX
      {{unixTimestamp}}                               // 17490641580
      {{identity.name}}                               // testuser
      {{random-5}}                                    // x9k2m
      {{truncate identity.name 4}}                    // test
      {{replace identity.name 'user' 'replace'}}      // testreplace
      ```
    </ParamField>

    <ParamField path="Customize ElastiCache Statement" type="string">
      If you want to provide specific privileges for the generated dynamic credentials, you can modify the ElastiCache statement to your needs. This is useful if you want to only give access to a specific resource.
    </ParamField>
  </Step>

  <Step title="Click `Submit`">
    After submitting the form, you will see a dynamic secret created in the dashboard.

    <Note>
      If this step fails, you may have to add the CA certificate.
    </Note>
  </Step>

  <Step title="Generate dynamic secrets">
    Once you've successfully configured the dynamic secret, you're ready to generate on-demand credentials.
    To do this, simply click on the 'Generate' button which appears when hovering over the dynamic secret item.
    Alternatively, you can initiate the creation of a new lease by selecting 'New Lease' from the dynamic secret lease list section.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-generate.png" alt="Dynamic Secret" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-lease-empty.png" alt="Dynamic Secret" />

    When generating these secrets, it's important to specify a Time-to-Live (TTL) duration. This will dictate how long the credentials are valid for.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/provision-lease.png" alt="Provision Lease" />

    <Tip>
      Ensure that the TTL for the lease falls within the maximum TTL defined when configuring the dynamic secret.
    </Tip>

    Once you click the `Submit` button, a new secret lease will be generated and the credentials from it will be shown to you.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/lease-values.png" alt="Provision Lease" />
  </Step>
</Steps>

## Audit or Revoke Leases

Once you have created one or more leases, you will be able to access them by clicking on the respective dynamic secret item on the dashboard.
This will allow you to see the expiration time of the lease or delete a lease before it's set time to live.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/lease-data.png" alt="Provision Lease" />

## Renew Leases

To extend the life of the generated dynamic secret leases past its initial time to live, simply click on the **Renew** button as illustrated below.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-lease-renew.png" alt="Provision Lease" />

<Warning>
  Lease renewals cannot exceed the maximum TTL set when configuring the dynamic secret
</Warning>
