# Source: https://infisical.com/docs/documentation/platform/identities/auth-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Machine Identity Auth Templates

> Learn how to use auth templates to standardize authentication configurations for machine identities.

## Concept

Machine Identity Auth Templates allow you to create reusable authentication configurations that can be applied across multiple machine identities. This feature helps standardize authentication setups, reduces configuration drift, and simplifies identity management at scale.

Instead of manually configuring authentication settings for each identity, you can create templates with predefined authentication parameters and apply them to multiple identities. This ensures consistency and reduces the likelihood of configuration errors.

Key Benefits:

* **Standardization**: Ensure consistent authentication configurations across identities
* **Efficiency**: Reduce time spent configuring individual identities
* **Governance**: Centrally manage and update authentication parameters
* **Scalability**: Easily apply proven configurations to new identities

## Managing Auth Templates

Auth templates are managed in **Organization Settings > Access Control > Identities** under the **Identity Auth Templates** section.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/identities/auth-templates/templates-section.png" alt="Identity Auth Templates Section" />

### Creating a Template

<Steps>
  <Step title="Navigate to Auth Templates">
    In your organization settings, go to **Access Control > Identities** and scroll down to the **Identity Auth Templates** section.
  </Step>

  <Step title="Create a new template">
    Click **Create Template** to open the template creation modal.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/identities/auth-templates/create-template-button.png" alt="Create Template Button" />

    Select the authentication method you want to create a template for (currently supports LDAP Auth).
  </Step>

  <Step title="Configure template settings">
    Fill in the template configuration based on your chosen authentication method.

    <Tabs>
      <Tab title="LDAP Auth Template">
        **For LDAP Auth templates**, configure the following fields:

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/identities/auth-templates/ldap-template.png" alt="LDAP Auth Template" />

        * **Template Name**: A descriptive name for your template
        * **URL**: The LDAP server to connect to such as `ldap://ldap.your-org.com`, `ldaps://ldap.myorg.com:636` *(for connection over SSL/TLS)*, etc.
        * **Bind DN**: The DN to bind to the LDAP server with.
        * **Bind Pass**: The password to bind to the LDAP server with.
        * **Search Base / DN**: Base DN under which to perform user search such as `ou=Users,dc=acme,dc=com`.
        * **CA Certificate**: The CA certificate to use when verifying the LDAP server certificate. This field is optional but recommended.

        <Note>
          You can read more about LDAP Auth configuration in the [LDAP Auth documentation](/documentation/platform/identities/ldap-auth/general).
        </Note>
      </Tab>
    </Tabs>
  </Step>
</Steps>

### Using Templates

Once created, templates can be applied when configuring authentication methods for machine identities. When adding an auth method to an identity, you'll have the option to select from available templates or configure manually.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/identities/auth-templates/machine-identity-page.png" alt="Attach Template" />
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/identities/auth-templates/attach-template-form.png" alt="Attach Template Form" />

### Managing Template Usage

You can view which identities are using a specific template by clicking **View Usages** in the template's dropdown menu.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/identities/auth-templates/template-usages.png" alt="Template Usages" />
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/identities/auth-templates/template-usages-modal.png" alt="Template Usages Modal" />

## FAQ

<AccordionGroup>
  <Accordion title="Can I modify a template after it's been applied to identities?">
    Yes, you can edit existing templates. After editing a template, changes to templates will automatically update identities that are already using them.
  </Accordion>

  <Accordion title="What happens if I delete a template that's in use?">
    If you delete a template that's currently being used by identities, those identities will continue to function with their existing configuration. However, the link to the template will be broken, and you won't be able to use the template for new identities.
  </Accordion>

  <Accordion title="Can I see which identities are using a specific template?">
    Yes, click **View Usages** in the template's dropdown menu to see all identities currently using that template.
  </Accordion>

  <Accordion title="Do templates support all authentication methods?">
    Currently, auth templates support LDAP Auth. Support for additional authentication methods will be added in future releases.
  </Accordion>
</AccordionGroup>
