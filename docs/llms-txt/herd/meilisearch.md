# Source: https://herd.laravel.com/docs/macos/herd-pro-services/meilisearch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Meilisearch

# Set up Meilisearch for Laravel Scout

Meilisearch is a powerful search engine for your application, working perfectly with [Laravel Scout](https://laravel.com/docs/11.x/scout). It allows you to add a search engine with great relevancy, typo correction, and more to your application by simply adding the `Searchable` Trait to a model.

<Frame>
  <img alt="Screenshot of Meilisearch settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d72a51d32be226143441c1c7131394eb" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-meilisearch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fbf39ee7d84da13575e0f360578d03d8 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f64bf3ae0c341c344e1d6ef15787dc8c 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6f6ec069040b592f1fa21bc10e317e70 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1aa732268f504cc88209783dfa9d3bc3 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ea57beac79d36d70c81565ae63eb3b27 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a62cf4652288af214cc9d8c0f0bd3837 2500w" />
</Frame>

## Connecting from your Laravel application

Like with all Herd services, you can configure the port as well as the service name of your Meilisearch instance and add the following environment variables to your `.env` file.

```env  theme={null}
SCOUT_DRIVER=meilisearch
MEILISEARCH_HOST=http://127.0.0.1:7700
MEILISEARCH_KEY=LARAVEL-HERD
```

When using the Meilisearch driver you will need to install the Meilisearch PHP SDK via the composer package manager:

```bash  theme={null}
composer require meilisearch/meilisearch-php http-interop/http-factory-guzzle
```

You can find additional information about using Laravel Scout with Meilisearch in the [Laravel documentation](https://laravel.com/docs/11.x/scout#meilisearch).

## Using Meilisearch

You can open the Meilisearch Dashboard or the logs of the service from the right side of the service details.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=381dca368dda29b60cba76b48aa21eb9" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_meilisearch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=7af381cf85755ee911f9f9d1420f3150 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e926ed5200b2a4ca8c9d699b85530ed3 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=85a35336e1de5316ed945062be005677 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f894923f1e871379cf3c1d60da521490 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=093b93ebe27c6daeb0e43603f8461de6 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f8929586252d29a2d922302c6f510259 2500w" />
</Frame>

## Dashboard

The Meilisearch dashboard is accessible via `http://locahost:port` or by using the dashboard button in the services list.

<Frame>
  <img alt="Screenshot of the Meilisearch dashboard" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=85fa215d160b130a895cc6cbac189730" data-og-width="2882" width="2882" data-og-height="1984" height="1984" data-path="images/docs/setup-meilisearch-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f5ac4eaac05f1a5d0aaafa87c8cb690b 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a70c9edd4940c1fe8a53a165a605ab79 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=45fd6912e718756273e695f65bc2f808 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=bbd2d08612ba0642e367cd6a7923bab2 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9ed554fb54ba45d2ab0ea7fe867cd644 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=70ecd49107d885f68fd866369901d802 2500w" />
</Frame>

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service     | Version |
| ----------- | ------- |
| Meilisearch | 1.9.0   |
