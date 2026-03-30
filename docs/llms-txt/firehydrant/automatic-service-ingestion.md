# Source: https://docs.firehydrant.com/docs/automatic-service-ingestion.md

# Automatic Service Ingestion

Aside from adding components [manually via UI](https://docs.firehydrant.com/docs/service-catalog-basics), [importing from 3rd-party providers](https://docs.firehydrant.com/docs/import-and-link-components), or managing [via API](https://docs.firehydrant.com/docs/ingesting-via-api), FireHydrant also provides a service ingestion process to automate synchronizing your Service Catalog.

After you set up service ingestion as described below, FireHydrant will search for and ingest updates to your YAML file every hour. You can also manually force an update.

## Prerequisites

FireHydrant currently supports two methods of automatic service ingestion:

* Reading a YAML file from your repository to ingest new services automatically. To do this, you must first have [GitHub integration with FireHydrant configured](https://docs.firehydrant.com/docs/github-integration).
* Via API. If done via API, you will need:
  * An [API Key](https://docs.firehydrant.com/docs/api-keys)
  * An external system or mechanism that will make API calls to FireHydrant with service catalog data in the appropriate format

## via Repository YAML

To get started:

1. Click on **Catalog** in the navigation at the top and then go to **Catalog settings** on the left.
2. Click **+ Create catalog setting** to add service ingestion details.

<Image alt="Catalog ingestion settings" align="center" width="650px" src="https://files.readme.io/444cc34-image.png">
  Catalog ingestion settings
</Image>

3. On this page, fill in details about the new ingestion mechanism:
   1.  **Name** - A name for this ingestion
   2. **Description** - A description, if desired
   3. **Provider** - Choose GitHub here. The other option is **API Only**, which [you can learn about here](#via-api).
   4. **Format** - The data format that will be sent to FireHydrant. At this time, FireHydrant supports [Backstage](https://backstage.io/docs/features/software-catalog/descriptor-format/)\* and [Opslevel](https://docs.opslevel.com/docs/opslevel-yml) formats.

<Image alt="Example target settings" align="center" width="400px" src="https://files.readme.io/6931807-image.png">
  Example target settings
</Image>

4. Once you've picked GitHub as the provider, an additional section, **Targets**, will appear below with the following fields for each target:
   1. **Type** - Either GitHub or GitHubScan. Choose GitHub if you want to read a single YAML file from a single repository or GitHubScan if you want to read a YAML file from multiple repositories. Usually, Backstage users will use GitHub, while Opslevel users will use GitHubScan.
   2. **Repository/Repositories (GitHub and GitHubScan)** - The repository (for GitHub) or repositories (GitHubScan) from which to read the YAML file(s).
   3. **Reference (GitHub only)** - The name of a specific branch or SHA of a commit from which to read the YAML file.
   4. **Path (GitHub and GitHubScan)** - The file path within the repository/repositories for the YAML\*\*.
5. If necessary, add more targets and repeat step #4 above.
6. Click "Create setting."

After you configure these settings, FireHydrant ingests your services according to the YAMLs you've specified. After completing the process, you can view your ingested services from the **Services** subpage in the FireHydrant UI.

> 📘 Notes
>
> \*For Backstage YAML, we currently only support `kind: Component`. See [Backstage docs](https://backstage.io/docs/features/software-catalog/descriptor-format/) for more examples of Backstage YAML and entity formatting.
>
> \*\*Supports glob pattern matching.

## via API

FireHydrant has a [robust API](https://developers.firehydrant.com/#/Z) through which most operations within FireHydrant are possible. This method enables you to make webhook calls to an endpoint that accepts body data in the same formats as above.

To reiterate, there are two prerequisites:

* You need an [API key](https://docs.firehydrant.com/docs/api-keys) to make API calls to FireHydrant
* This method relies on an external system that will make API calls to FireHydrant to send catalog data

If the above prerequisites are met, then you can configure this with the following steps:

1. Click on **Catalog** in the navigation at the top and then go to **Catalog settings** on the left.
2. Click **+ Create catalog setting** to add service ingestion details.
3.  On this page, fill in the following details:
   1. **Name** - A name for this ingestion
   2. **Description** - A description, if desired
   3. **Provider** - Choose "API Only" here. The other option is **GitHub**, which was covered in the previous section.
   4. **Format** - The data format that will be sent to FireHydrant. At this time, FireHydrant supports [Backstage](https://backstage.io/docs/features/software-catalog/descriptor-format/) and [Opslevel](https://docs.opslevel.com/docs/opslevel-yml) formats.
4. Click **Create setting**.
5. Next, you are returned to the Catalog settings page. The catalog you just added will appear in the list on this page - click on it to return to this catalog setting's page, where you can see the API endpoint for posting your data. Copy this API endpoint.
6. Make API requests to this endpoint at recurring intervals to keep the FireHydrant catalog up-to-date. You can base your cURL request for service ingestion on the following example. Note that this example uses a Backstage Component definition. To send OpsLevel or effx formats, change your request format accordingly.

```curl Example cURL
curl --location --request POST 'https://api.firehydrant.io/v1/catalogs/<CATALOG ID>/ingest' \
  --header 'Authorization: Bearer <YOUR BEARER TOKEN>' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "encoding": "application/json",
    "data": {
      "apiVersion": "backstage.io/v1alpha1",
      "kind": "Component",
      "metadata": {
        "namespace": "Spongebob",
        "name": "Component Service",
        "description": "I am a Backstage service component",
        "annotations": {
          "pagerduty.com/service-id": "EXAMPLE",
          "backstage.io/source-location": "url:https://github.com/octocat/Hello-World"
        },
        "labels": {
          "third-party": "true"
        }
      },
      "spec": {
        "type": "service",
        "lifecycle": "experimental",
        "owner": "team-name",
        "system": "whats-a-system",
        "links": [
          {
            "url": "https://admin.example-org.com/",
            "title": "Admin Dashboard",
            "icon": "dashboard"
          }
        ]
      }
    }
  }'
```

## Editing or updating service details

Any service details defined in the `.yaml` file or sent in via API will be controlled via those means. This is to maintain a source of truth for your Service Catalog. Fields you can edit from within the FireHydrant UI contain information specific to FireHydrant behavior and cannot be defined externally in the `.yaml` file or in the API request body.