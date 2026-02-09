# Source: https://herd.laravel.com/docs/macos/herd-pro-services/typesense.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Typesense

# Set up Typesense for Laravel Scout

Typesense is a lightning-fast open source search engine for your application, working perfectly with [Laravel Scout](https://laravel.com/docs/11.x/scout). It allows you to add a search engine with great relevancy, typo correction, and more to your application by simply adding the `Searchable` Trait to a model.

Herd makes setting up a Typesense service super easy:

<Frame>
  <img alt="Screenshot of Typesense settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6b7debd8169c3ebfcfb5d569b3169fcd" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-typesense.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2291761b846bffb9a4bcfad2a6e21b29 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3e059c0376b8da624bf71b551934d323 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=199d15ad073422f7b1eb49004370a803 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=edeb7dd47dc8a1dca86dd4106bca2ae4 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3dcd71dcf83ab6adeea2cde987ccaa5c 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4486a86a1d5d1c82e57994c3537bfcd3 2500w" />
</Frame>

## Connecting from your Laravel application

Like with all Herd services, you can configure the port as well as the service name of your Typesense instance and then add the following environment variables to your `.env` file.

```env  theme={null}
SCOUT_DRIVER=typesense
TYPESENSE_API_KEY=LARAVEL-HERD
TYPESENSE_HOST=localhost
```

If you're using a different port, you can simply copy the connections details from the right side of the service settings. The Typesense detail view also gives you a quick access to the logs of the service.

<Frame>
  <img alt="Typesense settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5728acbd0db1ce3847e1c9a6f755101a" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_typesense.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ebb7a81a12337b341c29947c0b1e2dc6 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f10a221d926c83f96cdddbf9415d5b05 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=838305f6a6d47a34f9a1b6e316b767bf 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f39d158a7fa27f76e370d5802a536cf5 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=27db1815b4abd32d437cd373bd8a4601 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=660fd2aea294ad1b570ee210aa6fc1eb 2500w" />
</Frame>

When using the Typesense with Laravel Scout you will need to install the Typesense PHP SDK via the Composer package manager:

```bash  theme={null}
composer require typesense/typesense-php
```

You can find additional information about using Laravel Scout with Typesense in the [Laravel documentation](https://laravel.com/docs/11.x/scout#typesense)

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service   | Version |
| --------- | ------- |
| Typesense | 0.26    |
