# Source: https://infisical.com/docs/integrations/app-connections/mssql.md

# Source: https://infisical.com/docs/documentation/platform/dynamic-secrets/mssql.md

# MS SQL

> Learn how to dynamically generate MS SQL database user credentials.

The Infisical MS SQL dynamic secret allows you to generate Microsoft SQL server database credentials on demand based on configured role.

## Prerequisite

Create a user with the required permission in your SQL instance. This user will be used to create new accounts on-demand.

## Set up Dynamic Secrets with MS SQL

<Steps>
  <Step title="Open Secret Overview Dashboard">
    Open the Secret Overview dashboard and select the environment in which you would like to add a dynamic secret.
  </Step>

  <Step title="Click on the 'Add Dynamic Secret' button">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/add-dynamic-secret-button.png" alt="Add Dynamic Secret Button" />
  </Step>

  <Step title="Select `SQL Database`">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-modal.png" alt="Dynamic Secret Modal" />
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

    <ParamField path="Metadata" type="list" required>
      List of key/value metadata pairs
    </ParamField>

    <ParamField path="Service" type="string" required>
      Choose the service you want to generate dynamic secrets for. This must be selected as **MS SQL**.
    </ParamField>

    <ParamField path="Host" type="string" required>
      Database host
    </ParamField>

    <ParamField path="Port" type="number" required>
      Database port
    </ParamField>

    <ParamField path="User" type="string" required>
      Username that will be used to create dynamic secrets
    </ParamField>

    <ParamField path="Password" type="string" required>
      Password that will be used to create dynamic secrets
    </ParamField>

    <ParamField path="Database Name" type="string" required>
      Name of the database for which you want to create dynamic secrets
    </ParamField>

    <ParamField path="CA(SSL)" type="string">
      A CA may be required if your DB requires it for incoming connections. AWS RDS instances with default settings will requires a CA which can be downloaded [here](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.CertificatesAllRegions).
    </ParamField>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-setup-modal-mssql.png" alt="Dynamic Secret Setup Modal" />
  </Step>

  <Step title="(Optional) Modify SQL Statements">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/modify-sql-statements-mssql.png" alt="Modify SQL Statements Modal" />

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
This will allow you to see the expiration time of the lease or delete the lease before it's set time to live.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/lease-data.png" alt="Provision Lease" />

## Renew Leases

To extend the life of the generated dynamic secret leases past its initial time to live, simply click on the **Renew** button as illustrated below.
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-lease-renew.png" alt="Provision Lease" />

<Warning>
  Lease renewals cannot exceed the maximum TTL set when configuring the dynamic
  secret
</Warning>
