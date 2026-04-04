# Source: https://infisical.com/docs/documentation/platform/dynamic-secrets/snowflake.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Snowflake

> Learn how to dynamically generate Snowflake user credentials.

Infisical's Snowflake dynamic secrets allow you to generate Snowflake user credentials on demand.

## Snowflake Prerequisites

<Note>
  Infisical requires a Snowflake user in your account with the USERADMIN role.
  This user will act as a service account for Infisical and facilitate the
  creation of new users as needed.
</Note>

<Steps>
  <Step title="Navigate to Snowflake's User Dashboard and press the '+ User' button">
        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/snowflake/dynamic-secret-snowflake-users-page.png"
          alt="Snowflake User
    Dashboard"
        />
  </Step>

  <Step title="Create a Snowflake user with the USERADMIN role for Infisical">
    <Warning>
      Be sure to uncheck "Force user to change password on first time login"
    </Warning>

        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/snowflake/dynamic-secret-snowflake-create-service-user.png"
          alt="Snowflake Create Service
    User"
        />
  </Step>

  <Step title="Click on the Account Menu in the bottom left and take note of your Account and Organization identifiers">
        <img
          src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/snowflake/dynamic-secret-snowflake-identifiers.png"
          alt="Snowflake Account And Organization
    Identifiers"
        />
  </Step>
</Steps>

## Set up Dynamic Secrets with Snowflake

<Steps>
  <Step title="Open the Secret Overview Dashboard">
    Open the Secret Overview dashboard and select the environment in which you would like to add a dynamic secret.
  </Step>

  <Step title="Click on the 'Add Dynamic Secret' button">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/add-dynamic-secret-button.png" alt="Add Dynamic Secret Button" />
  </Step>

  <Step title="Select the Snowflake option in the grid list">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/snowflake/dynamic-secret-snowflake-modal.png" alt="Dynamic Secret Modal" />
  </Step>

  <Step title="Provide the required parameters for the Snowflake dynamic secret">
    <ParamField path="Secret Name" type="string" required>
      The name you want to reference this secret by
    </ParamField>

    <ParamField path="Default TTL" type="string" required>
      Default time-to-live for a generated secret (it is possible to modify this value when generating a secret)
    </ParamField>

    <ParamField path="Max TTL" type="string" required>
      Maximum time-to-live for a generated secret
    </ParamField>

    <ParamField path="Account Identifier" type="string" required>
      Snowflake account identifier
    </ParamField>

    <ParamField path="Organization Identifier" type="string" required>
      Snowflake organization identifier
    </ParamField>

    <ParamField path="User" type="string" required>
      Username of the Infisical Service User
    </ParamField>

    <ParamField path="Password" type="string" required>
      Password of the Infisical Service User
    </ParamField>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/snowflake/dynamic-secret-snowflake-setup-modal.png" alt="Dynamic Secret Setup Modal" />
  </Step>

  <Step title="(Optional) Modify SQL Statements">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/snowflake/dynamic-secret-snowflake-sql-statements.png" alt="Modify SQL Statements Modal" />

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

    <ParamField path="Customize Statement" type="string">
      If you want to provide specific privileges for the generated dynamic credentials, you can modify the SQL
      statement to your needs.
    </ParamField>
  </Step>

  <Step title="Click 'Submit'">
    After submitting the form, you will see a dynamic secret created in the dashboard.
  </Step>

  <Step title="Generate dynamic secrets">
    Once you've successfully configured the dynamic secret, you're ready to generate on-demand credentials.
    To do this, simply click on the 'Generate' button which appears when hovering over the dynamic secret item.
    Alternatively, you can initiate the creation of a new lease by selecting 'New Lease' from the dynamic secret
    lease list section.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-generate.png" alt="Dynamic Secret" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-lease-empty.png" alt="Dynamic Secret" />

    When generating these secrets, it's important to specify a Time-to-Live (TTL) duration. This will dictate how
    long the credentials are valid for.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/provision-lease.png" alt="Provision Lease" />

    <Tip>
      Ensure that the TTL for the lease falls within the maximum TTL defined when configuring the dynamic secret in
      step 4.
    </Tip>

    Once you click the `Submit` button, a new secret lease will be generated and the credentials for it will be
    shown to you.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/lease-values.png" alt="Provision Lease" />
  </Step>
</Steps>

## Audit or Revoke Leases

Once you have created one or more leases, you will be able to access them by clicking on the respective dynamic secret item on the dashboard.
This will allow you to see the lease details and delete the lease ahead of its expiration time.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/lease-data.png" alt="Provision Lease" />

## Renew Leases

To extend the life of the generated dynamic secret lease past its initial time to live, simply click on the **Renew** button as illustrated below.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-lease-renew.png" alt="Provision Lease" />

<Warning>
  Lease renewals cannot exceed the maximum TTL set when configuring the dynamic
  secret.
</Warning>
