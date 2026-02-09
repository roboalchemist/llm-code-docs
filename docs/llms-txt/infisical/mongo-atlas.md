# Source: https://infisical.com/docs/documentation/platform/dynamic-secrets/mongo-atlas.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mongo Atlas

> Learn how to dynamically generate Mongo Atlas Database user credentials.

The Infisical Mongo Atlas dynamic secret allows you to generate Mongo Atlas Database credentials on demand based on configured role.

## Prerequisite

Create a project scoped API Key with the required permission in your Mongo Atlas following the [official doc](https://www.mongodb.com/docs/atlas/configure-api-access/#grant-programmatic-access-to-a-project).

<Info>The API Key must have permission to manage users in the project.</Info>

## Set up Dynamic Secrets with Mongo Atlas

<Steps>
  <Step title="Open Secret Overview Dashboard">
    Open the Secret Overview dashboard and select the environment in which you would like to add a dynamic secret.
  </Step>

  <Step title="Click on the 'Add Dynamic Secret' button">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/add-dynamic-secret-button.png" alt="Add Dynamic Secret Button" />
  </Step>

  <Step title="Select Mongo Atlas">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-atlas-modal.png" alt="Dynamic Secret Modal" />
  </Step>

  <Step title="Provide the inputs for dynamic secret parameters">
    <ParamField path="Secret Name" type="string" required>
      Name by which you want the secret to be referenced
    </ParamField>

    <ParamField path="Default TTL" type="string" required>
      Default time-to-live for a generated secret (it is possible to modify this value after a secret is generated)
    </ParamField>

    <ParamField path="Max TTL" type="string" required>
      Maximum time-to-live for a generated secret
    </ParamField>

    <ParamField path="Admin public key" type="string" required>
      The public key of your generated Atlas API Key. This acts as a username.
    </ParamField>

    <ParamField path="Admin private key" type="string" required>
      The private key of your generated Atlas API Key. This acts as a password.
    </ParamField>

    <ParamField path="Group ID" type="number" required>
      Unique 24-hexadecimal digit string that identifies your project. This is same as project id
    </ParamField>

    <ParamField path="Roles" type="string" required>
      List that provides the pairings of one role with one applicable database.

      * **Database Name**: Database to which the user is granted access privileges.
      * **Collection**: Collection on which this role applies.
      * **Role Name**: Human-readable label that identifies a group of privileges assigned to a database user. This value can either be a built-in role or a custom role.
        * Enum: `atlasAdmin` `backup` `clusterMonitor` `dbAdmin` `dbAdminAnyDatabase` `enableSharding` `read` `readAnyDatabase` `readWrite` `readWriteAnyDatabase` `<a custom role name>`.
    </ParamField>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-modal-atlas.png" alt="Dynamic Secret Setup Modal" />
  </Step>

  <Step title="(Optional) Modify Access Scope">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/advanced-option-atlas.png" alt="Modify Scope Modal" />

    <ParamField path="Username Template" type="string" default="{{randomUsername}}">
      Specifies a template for generating usernames. This field allows customization of how usernames are automatically created.

      Allowed template variables are:

      * `{{randomUsername}}`: Random username string.
      * `{{unixTimestamp}}`: Current Unix timestamp at the time of lease creation.
      * `{{identity.name}}`: Name of the identity that is generating the lease.
      * `{{dynamicSecret.name}}`: Name of the associated dynamic secret.
      * `{{dynamicSecret.type}}`: Type of the associated dynamic secret.
      * `{{random N}}`: Random string of N characters.

      Allowed template functions are:

      * `truncate`: Truncates a string to a specified length.
      * `replace`: Replaces a substring with another value.
      * `uppercase`: Converts a string to uppercase.
      * `lowercase`: Converts a string to lowercase.

      Examples:

      ```yaml  theme={"dark"}
      {{ randomUsername }}                                            // 3POnzeFyK9gW2nioK0q2gMjr6CZqsRiX
      {{ unixTimestamp }}                                             // 17490641580
      {{ identity.name }}                                             // <identity-name>
      {{ random 5 }}                                                  // x9K2m
      {{ truncate identity.name 4 }}                                  // test
      {{ replace identity.name '<identity-name>' 'new-value' }}       // new-value
      ```
    </ParamField>

    <ParamField path="Customize Scope" type="string">
      List that contains clusters, MongoDB Atlas Data Lakes, and MongoDB Atlas Streams Instances that this database user can access. If omitted, MongoDB Cloud grants the database user access to all the clusters, MongoDB Atlas Data Lakes, and MongoDB Atlas Streams Instances in the project.

      * **Label**: Human-readable label that identifies the cluster or MongoDB Atlas Data Lake that this database user can access.
      * **Type**: Category of resource that this database user can access.
    </ParamField>
  </Step>

  <Step title="Click 'Submit'">
    After submitting the form, you will see a dynamic secret created in the dashboard.

    <Note>
      If this step fails, you may have to add the CA certificate.
    </Note>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret.png" alt="Dynamic Secret" />
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

    Once you click the `Submit` button, a new secret lease will be generated and the credentials for it will be shown to you.

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
  Lease renewals cannot exceed the maximum TTL set when configuring the dynamic
  secret
</Warning>
