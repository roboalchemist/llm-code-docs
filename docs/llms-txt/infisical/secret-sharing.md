# Source: https://infisical.com/docs/documentation/platform/secret-sharing.md

# Secret Sharing

> Learn how to share time & view-count bound secrets securely with anyone on the internet.

Developers frequently need to share secrets with team members, contractors, or other third parties, which can be risky due to potential leaks or misuse.
Infisical offers a secure solution for sharing secrets over the internet in a time and view-count bound manner. It is possible to share secrets without signing up via [share.infisical.com](https://share.infisical.com) or via Infisical Dashboard (which has more advanced functionality).

## Sharing a Secret

<Steps>
  <Step title="Navigate to the 'Secret Sharing' page and click 'Share Secret'">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-sharing/overview.png" alt="Secret Sharing" />
  </Step>

  <Step title="Configure Secret Share">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-sharing/create-new-secret.png" alt="Configure Secret" />

    * **Name (optional):** A friendly name for the shared secret.

    * **Your Secret:** The secret content.

    * **Password (optional):** A password which will be required when viewing the secret.

    * **Limit access to people within organization:** Only lets people within your organization view the secret. Enabling this feature requires secret viewers to log into Infisical.

    * **Expires In:** The time it'll take for the secret to expire.

    * **Max Views:** How many times the secret can be viewed before it's destroyed.

    * **Authorized Emails (optional):** Emails which are authorized to view this secret. Enabling this feature requires secret viewers to log into Infisical. Each email will receive the shared secret link in their inbox after creation.
  </Step>

  <Step title="Copy Link and Share Secret">
    After creating the shared secret, its link will be displayed. Share this with the intended recipients.

    <Info>
      If no organization or email restrictions are set, anyone with this link can view the secret before it expires.
    </Info>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-sharing/copy-url.png" alt="Copy URL" />
  </Step>

  <Step title="Access Shared Secret">
    Visiting the secret link will display its contents.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-sharing/public-view.png" alt="Access Shared Secret" />
  </Step>
</Steps>

## Deleting a Shared Secret

To delete a shared secret, click the **Trash Can** icon on the relevant shared secret row in the [**Secret Sharing**](https://app.infisical.com/organization/secret-sharing?selectedTab=share-secret) page.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-sharing/delete-secret.png" alt="Delete Secret" />

## FAQ

<AccordionGroup>
  <Accordion title="Can secrets be changed after they are shared?">
    No, secrets cannot be changed after they've been created. This is to ensure that secrets are not tampered with.
  </Accordion>
</AccordionGroup>
