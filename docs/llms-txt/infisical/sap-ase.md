# Source: https://infisical.com/docs/documentation/platform/dynamic-secrets/sap-ase.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SAP ASE

> Learn how to dynamically generate SAP ASE database account credentials.

The Infisical SAP ASE dynamic secret allows you to generate SAP ASE database credentials on demand.

## Prerequisite

* Infisical requires that you have a user in your SAP ASE instance, configured with the appropriate permissions. This user will facilitate the creation of new accounts as needed.
  Ensure the user possesses privileges for creating, dropping, and granting permissions to roles for it to be able to create dynamic secrets.
  The user used for authentication must have access to the `master` database. You can use the `sa` user for this purpose or create a new user with the necessary permissions.

* The SAP ASE instance should be reachable by Infisical.

## Set up Dynamic Secrets with SAP ASE

<Steps>
  <Step title="Open Secret Overview Dashboard">
    Open the Secret Overview dashboard and select the environment in which you would like to add a dynamic secret.
  </Step>

  <Step title="Click on the 'Add Dynamic Secret' button">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/add-dynamic-secret-button.png" alt="Add Dynamic Secret Button" />
  </Step>

  <Step title="Select SAP ASE">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/sap-ase/dynamic-secret-sap-ase-modal.png" alt="Dynamic Secret Modal" />
  </Step>

  <Step title="Provide the inputs for dynamic secret parameters">
    <ParamField path="Secret Name" type="string" required>
      Name by which you want the secret to be referenced
    </ParamField>

    <ParamField path="Default TTL" type="string" required>
      Default time-to-live for a generated secret (it is possible to modify this value when a secret is generate)
    </ParamField>

    <ParamField path="Max TTL" type="string" required>
      The maximum time-to-live for a generated secret
    </ParamField>

    <ParamField path="Host" type="string" required>
      Your SAP ASE instance host (IP or domain)
    </ParamField>

    <ParamField path="Port" type="number" required>
      Your SAP ASE instance port. On default SAP ASE instances this is usually `5000`.
    </ParamField>

    <ParamField path="Database" type="number" required>
      The database name that you want to generate credentials for. This database must exist on the SAP ASE instance.
      Please note that the user/password used for authentication must have access to this database, **and** the `master` database.
    </ParamField>

    <ParamField path="User" type="string" required>
      Username that will be used to create dynamic secrets
    </ParamField>

    <ParamField path="Password" type="string" required>
      Password that will be used to create dynamic secrets
    </ParamField>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/sap-ase/dynamic-secret-sap-ase-setup-modal.png" alt="Dynamic Secret Setup Modal" />
  </Step>

  <Step title="(Optional) Modify SAP SQL Statements">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/sap-ase/dynamic-secret-sap-ase-statements.png" alt="Modify SQL Statements Modal" />

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
      If you want to provide specific privileges for the generated dynamic credentials, you can modify the SQL statement to your needs.

      <Warning>
        Due to SAP ASE limitations, the attached SQL statements are not executed as a transaction.
      </Warning>
    </ParamField>
  </Step>

  <Step title="Click 'Submit'">
    After submitting the form, you will see a dynamic secret created in the dashboard.
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
      Ensure that the TTL for the lease falls within the maximum TTL defined when configuring the dynamic secret in step 4.
    </Tip>

    Once you click the `Submit` button, a new secret lease will be generated and the credentials for it will be shown to you.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/lease-values.png" alt="Provision Lease" />
  </Step>
</Steps>

## Audit or Revoke Leases

Once you have created one or more leases, you will be able to access them by clicking on the respective dynamic secret item on the dashboard.
This will allow you see the lease details and delete the lease ahead of its expiration time.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/lease-data.png" alt="Provision Lease" />

## Renew Leases

To extend the life of the generated dynamic secret lease past its initial time to live, simply click on the **Renew** as illustrated below.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-lease-renew.png" alt="Provision Lease" />

<Warning>
  Lease renewals cannot exceed the maximum TTL set when configuring the dynamic
  secret.
</Warning>
