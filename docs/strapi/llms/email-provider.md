# Email Provider

Strapi Cloud comes with a basic email provider out of the box. However, it can also be configured to utilize another email provider, if needed.

:::caution
Please be advised that Strapi is unable to provide support for third-party email providers.

:::

:::prerequisites

- A local Strapi project running on `v4.8.2+`.
- Credentials for another email provider (see 

</Tabs>

:::caution
The file structure must match the above path exactly, or the configuration will not be applied to Strapi Cloud.
:::

Each provider will have different configuration settings available. Review the respective entry for that provider in the 

</Tabs>
</TabItem>

</Tabs>
</TabItem>
</Tabs>

:::tip
Before pushing the above changes to GitHub, add environment variables to the Strapi Cloud project to prevent triggering a rebuild and new deployment of the project before the changes are complete.
:::

### Strapi Cloud Configuration

1. Log into Strapi Cloud and click on the corresponding project on the Projects page.
2. Click on the **Settings** tab and choose **Variables** in the left menu.
3. Add the required environment variables specific to the email provider.
4. Click **Save**.

**Example:**

</Tabs>

## Deployment

To deploy the project and utilize another party email provider, push the changes from earlier. This will trigger a rebuild and new deployment of the Strapi Cloud project.

Once the application finishes building, the project will use the new email provider.

:::strapi Custom Provider
If you want to create a custom email provider, please refer to the [Email providers](/cms/features/email#providers) documentation in the CMS Documentation.
:::