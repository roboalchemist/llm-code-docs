# Source: https://infisical.com/docs/documentation/platform/dynamic-secrets/elastic-search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Elasticsearch

> Learn how to dynamically generate Elasticsearch user credentials.

The Infisical Elasticsearch dynamic secret allows you to generate Elasticsearch credentials on demand based on configured role.

## Prerequisites

1. Create a role with at least `manage_security` and `monitor` permissions.
2. Assign the newly created role to your API key or user that you'll use later in the dynamic secret configuration.

<Note>
  For testing purposes, you can also use a highly privileged role like
  `superuser`, that will have full control over the cluster. This is not
  recommended in production environments following the principle of least
  privilege.
</Note>

## Set up Dynamic Secrets with Elasticsearch

<Steps>
  <Step title="Open Secret Overview Dashboard">
    Open the Secret Overview dashboard and select the environment in which you would like to add a dynamic secret.
  </Step>

  <Step title="Click on the 'Add Dynamic Secret' button">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/add-dynamic-secret-button.png" alt="Add Dynamic Secret Button" />
  </Step>

  <Step title="Select 'Elasticsearch'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-modal-elastic-search.png" alt="Dynamic Secret Modal" />
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

    <ParamField path="Host" type="string" required>
      Your Elasticsearch host. This is the endpoint that your instance runs on. *(Example: [https://your-cluster-ip](https://your-cluster-ip))*
    </ParamField>

    <ParamField path="Port" type="string" required>
      The port that your Elasticsearch instance is running on. *(Example: 9200)*
    </ParamField>

    <ParamField path="Roles" type="string[]" required>
      The roles that the new user that is created when a lease is provisioned will
      be assigned to. This is a required field. This defaults to `superuser`, which
      is highly privileged. It is recommended to create a new role with the least
      privileges required for the lease.
    </ParamField>

    <ParamField path="Authentication Method" type="API Key | Username/Password" required>
      Select the authentication method you want to use to connect to your Elasticsearch instance.
    </ParamField>

    <ParamField path="Username" type="string" required>
      The username of the user that will be used to provision new dynamic secret
      leases. Only required if you selected the `Username/Password` authentication
      method.
    </ParamField>

    <ParamField path="Password" type="string" required>
      The password of the user that will be used to provision new dynamic secret
      leases. Only required if you selected the `Username/Password` authentication
      method.
    </ParamField>

    <ParamField path="API Key ID" required>
      The ID of the API key that will be used to provision new dynamic secret
      leases. Only required if you selected the `API Key` authentication method.
    </ParamField>

    <ParamField path="API Key" required>
      The API key that will be used to provision new dynamic secret leases. Only
      required if you selected the `API Key` authentication method.
    </ParamField>

    <ParamField path="CA(SSL)" type="string">
      A CA may be required if your DB requires it for incoming connections. This is often the case when connecting to a managed service.
    </ParamField>

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

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-input-modal-elastic-search.png" alt="Dynamic Secret Setup Modal" />
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

    When generating these secrets, it's important to specify a Time-to-Live (TTL) duration. This will dictate  how long the credentials are valid for.

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
  Lease renewals cannot exceed the maximum TTL set when configuring the dynamic
  secret
</Warning>
