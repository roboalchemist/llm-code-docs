# Source: https://infisical.com/docs/documentation/platform/dynamic-secrets/vertica.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vertica

> Learn how to dynamically generate Vertica database users.

The Infisical Vertica dynamic secret allows you to generate Vertica database credentials on demand based on configured role.

## Prerequisite

Create a user with the required permission in your Vertica instance. This user will be used to create new accounts on-demand.

## Set up Dynamic Secrets with Vertica

<Steps>
  <Step title="Open Secret Overview Dashboard">
    Open the Secret Overview dashboard and select the environment in which you would like to add a dynamic secret.
  </Step>

  <Step title="Click on the 'Add Dynamic Secret' button">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/add-dynamic-secret-button.png" alt="Add Dynamic Secret Button" />
  </Step>

  <Step title="Select `Vertica`">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/vertica/dynamic-secret-modal-vertica.png" alt="Dynamic Secret Modal" />
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

    <ParamField path="Gateway" type="string">
      Select a gateway for private cluster access. If not specified, the Internet Gateway will be used.
    </ParamField>

    <ParamField path="Host" type="string" required>
      Vertica database host
    </ParamField>

    <ParamField path="Port" type="number" required>
      Vertica database port (default: 5433)
    </ParamField>

    <ParamField path="Database" type="string" required>
      Name of the Vertica database for which you want to create dynamic secrets
    </ParamField>

    <ParamField path="User" type="string" required>
      Username that will be used to create dynamic secrets
    </ParamField>

    <ParamField path="Password" type="string" required>
      Password that will be used to create dynamic secrets
    </ParamField>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/vertica/dynamic-secret-setup-modal-vertica.png" alt="Dynamic Secret Setup Modal" />
  </Step>

  <Step title="(Optional) Modify SQL Statements">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/vertica/modify-sql-statements-vertica.png" alt="Modify SQL Statements Modal" />

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

    <ParamField path="Creation Statement" type="string">
      Customize the SQL statement used to create new users. Default creates a user with basic schema permissions.
    </ParamField>

    <ParamField path="Revocation Statement" type="string">
      Customize the SQL statement used to revoke users. Default revokes a user.
    </ParamField>
  </Step>

  <Step title="(Optional) Configure Password Requirements">
    <ParamField path="Password Length" type="number" default="48">
      Length of generated passwords (1-250 characters)
    </ParamField>

    <ParamField path="Character Requirements" type="object">
      Minimum required character counts:

      * **Lowercase Count**: Minimum lowercase letters (default: 1)
      * **Uppercase Count**: Minimum uppercase letters (default: 1)
      * **Digit Count**: Minimum digits (default: 1)
      * **Symbol Count**: Minimum symbols (default: 0)
    </ParamField>

    <ParamField path="Allowed Symbols" type="string" default="-_.~!*">
      Symbols allowed in generated passwords
    </ParamField>
  </Step>

  <Step title="Click 'Submit'">
    After submitting the form, you will see a dynamic secret created in the dashboard.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/vertica/dynamic-secret-vertica.png" alt="Dynamic Secret" />
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
This will allow you to see the expiration time of the lease or delete the lease before its set time to live.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/lease-data.png" alt="Provision Lease" />

## Renew Leases

To extend the life of the generated dynamic secret leases past its initial time to live, simply click on the **Renew** button as illustrated below.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-lease-renew.png" alt="Provision Lease" />

<Warning>
  Lease renewals cannot exceed the maximum TTL set when configuring the dynamic secret
</Warning>
