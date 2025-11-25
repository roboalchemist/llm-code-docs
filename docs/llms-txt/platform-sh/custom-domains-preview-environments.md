# Source: https://docs.upsun.com/domains/steps/custom-domains-preview-environments.md

# Set up a custom domain on a preview environment

[Preview environments](https://docs.upsun.com/glossary.md#preview-environment) in your project can't use the custom domain [set up on your production environment](https://docs.upsun.com../steps.md).
By default and for each preview environment,
Upsun automatically replaces the custom production domain
with an automatically generated URL.

If you don't want to use these default URLs,
you can add a custom domain to each of your preview environments
(`staging` or `development` [environment types](https://docs.upsun.com/glossary.md#environment-type)).

To do so, no need to modify your [routes configuration](https://docs.upsun.com../../define-routes.md).
When you add a new custom domain for a preview environment,
just attach it to the custom production domain it replaces.
If you have multiple custom production domains,
you need to select which one you're replacing.

**Example**: 

You have two environments, a production environment and a staging environment.
You’ve added the ``example.com`` custom domain to your production environment.

You want to add the ``staging.example.com`` custom domain to your staging environment.
To do so, you need to attach the new ``staging.example.com`` custom domain
to its corresponding custom production domain ``example.com``.
You can then access your staging environment through ``staging.example.com``,
and still access your production environment through ``example.com``.

If you have multiple custom domains on your production environment,
when you set up a custom domain on a preview environment,
you don't need to update your [routes configuration](https://docs.upsun.com../../define-routes.md) either.
Upsun automatically figures out the routing of your preview environment
based on the following elements:

- The custom production domains in your existing [routes configuration](https://docs.upsun.com../../define-routes.md)
- The custom domains for preview environments attached to each of those custom production domains

## Before you start

You need:

- A production environment with at least one custom domain already set up
- At least one preview (staging or development) environment
- Optional: The [Upsun CLI](https://docs.upsun.com../../administration/cli.md) (v4.8.0+)

To prevent abuse, by default you can add custom domains to up to 5 preview environments per project only.
This limit doesn't include the production environment,
and you can increase it without charge.
To do so, [contact Support](https://docs.upsun.com/learn/overview/get-support.md).

**Note**: 

If you delete a custom production domain,
all of the attached custom domains for preview environments are deleted too.
You need to rebuild the affected preview environments for the deletion to be complete.

## Add a custom domain to a preview environment

To add a custom domain to a preview environment, follow these steps:

 - [Configure your DNS provider](https://docs.upsun.com/domains/steps.md#2-configure-your-dns-provider).
In particular, make sure your DNS record points to the target of your preview environment.
**Note**: 

Using the target of your production environment to configure your DNS provider is technically possible,
but Upsun recommends using the target of your preview environment as a best practice.

 - Run a command similar to the following:

```bash {}
upsun domain:add staging.example.com --environment <STAGING_ENVIRONMENT_ID> --attach <PRODUCTION_CUSTOM_DOMAIN_TO_ATTACH>
```

 - Get the target for your preview environment. 
To do so, navigate to your preview environment and click **Settings Settings**. 
Select the **Domains** tab. 
In the **Configure your domain** section, copy the content of the **CNAME record** field. 
Save it for later use at step 7.

 - Click **Add domain**.

 - Name the custom domain for your preview environment.

 - Attach the custom domain for your preview environment to the desired production custom domain.

 - Click **Add**.

 - Click **Okay**.

 - [Configure your DNS provider](https://docs.upsun.com/domains/steps.md#2-configure-your-dns-provider). 
In particular, make sure your DNS record points to the target of your preview environment.

**Note**: 

Using the target of your production environment to configure your DNS provider is technically possible,
but Upsun recommends using the target of your preview environment as a best practice.

**Note**: 

You can’t update a custom domain when it’s used on a preview environment.
You can only delete it and create a new one as a replacement.

### Example

You've added the `mysite.com` custom domain to your production environment.
You now want to add the `mydev.com` custom domain to a preview environment called `Dev`.

To do so, follow these steps:

 - Get the target for ``Dev``. 
To do so, navigate to ``Dev`` and click **Settings Settings**. 
Select the **Domains** tab. 
In the **Configure your domain** section, copy the content of the **CNAME record** field. 
Save it for later use at step 7.

 - Click **Add domain**.

 - Enter ``mydev.com`` as a name for the custom domain you want to add to ``Dev``.

 - Select ``mysite.com`` as the production custom domain you want to attach ``mydev.com`` to.

 - Click **Add**. 

 - Click **Okay**.

 - [Configure your DNS provider](https://docs.upsun.com/domains/steps.md#2-configure-your-dns-provider). 
In particular, make sure your DNS record points to ``Dev``’s target.

In the above example, the `Dev` environment needs to exist
for you to add the `mydev.com` custom domain successfully.
If the `Dev` environment is later removed,
the `mydev.com` custom domain is removed too.

## List the custom domains of a preview environment

 - Navigate to your preview environment and click **Settings Settings**.
 - Select the **Domains** tab. 
All the custom domains for your preview environment are displayed.

## Get a specific custom domain used on a preview environment

 - Navigate to your preview environment and click **Settings Settings**. 
 - Select the **Domains** tab. 
All the custom domains for the selected environment are displayed.
 - To see which actions you can perform on a displayed custom domain,
click **More More** next to it.

## Remove a custom domain from a preview environment

 - Navigate to your preview environment and click **Settings Settings**.
 - Select the **Domains** tab. 
All the custom domains for the selected environment are displayed.
 - Click **More More** on the custom domain you want to delete.
 - Click **Delete**.
 - Click **Yes, delete**.


