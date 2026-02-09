# Source: https://infisical.com/docs/documentation/platform/external-migrations/envkey.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating from EnvKey to Infisical

> Learn how to migrate secrets from EnvKey to Infisical.

## Migrating from EnvKey

<Steps>
  <Step title="Open the EnvKey dashboard and go to My Org">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/external-migrations/envkey-dashboard.png" alt="EnvKey Dashboard" />
  </Step>

  <Step title="Export your EnvKey organization">
    Go to Import/Export on the top right corner, Click on Export Org and save the exported file.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/external-migrations/envkey-export.png" alt="Export organization" />
  </Step>

  <Step title="Obtain EnvKey encryption key">
    Click on copy to copy the encryption key and save it.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/external-migrations/envkey-copy-encryption-key.png" alt="Copy encryption key" />
  </Step>

  <Step title="Navigate to Infisical external migrations">
    Open the Infisical dashboard and go to Organization Settings > External Migrations.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/external-migrations/infisical-external-migration-dashboard.png" alt="Infisical Organization settings" />
  </Step>

  <Step title="Select the EnvKey platform">
    Select the EnvKey platform and click on Next.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/external-migrations/infisical-import-envkey-modal.png" alt="Select EnvKey platform" />
  </Step>

  <Step title="Upload the exported file from EnvKey">
    Upload the exported file from EnvKey, paste the encryption key and click Import data.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/external-migrations/infisical-import-envkey.png" alt="Infisical Import EnvKey" />
  </Step>
</Steps>

<Note>
  It may take several minutes to complete the migration. You will receive an email when the migration is complete, or if there were any errors during the migration process.
</Note>

## Talk to our team

To make the migration process even more seamless, you can [schedule a meeting with our team](https://infisical.cal.com/vlad/migration-from-envkey-to-infisical) to learn more about how Infisical compares to EnvKey and discuss unique needs of your organization. You are also welcome to email us at [support@infisical.com](mailto:support@infisical.com) to ask any questions or get any technical help.
