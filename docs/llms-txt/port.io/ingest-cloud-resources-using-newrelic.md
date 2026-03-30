# Source: https://docs.port.io/guides/all/ingest-cloud-resources-using-newrelic.md

# Ingest Cloud Resources with New Relic

This guide aims to show you how to ingest cloud resources using New Relic to have a comprehensive view of the cloud resources/entities you have from your cloud providers.

## Common Use Cases[â](#common-use-cases "Direct link to Common Use Cases")

* Map your monitored resources from cloud providers in New Relic.
* Enhance visibility of your cloud infrastructure within Port without relying solely on direct integrations.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* You have [installed and set up Port's New Relic integration](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/apm-alerting/newrelic).
* You have entities from cloud providers configured in New Relic. See [New Relic's documentation](https://docs.newrelic.com/docs/infrastructure/) for details on setting up cloud integrations.

## Ingesting cloud resources into Port[â](#ingesting-cloud-resources-into-port "Direct link to Ingesting cloud resources into Port")

We will utilize the `entity` kind in Port's New Relic integration, which provides information on entities monitored in New Relic. Entities are ingested based on their respective infrastructure integration `type`.

**Examples of cloud resources infrastructure integration types**

* `AWSEC2INSTANCE`
* `AWSS3BUCKET`
* `AWSRDSDBINSTANCE`
* `AWSLAMBDAFUNCTION`
* `AWSELBLOADBALANCER`
* `AZUREVIRTUALMACHINE`
* `AZURESQLDATABASE`
* `GCPCOMPUTEINSTANCE`
* `GCPSTORAGEBUCKET`
* `GCPSQLDATABASEINSTANCE`

## Data model setup[â](#data-model-setup "Direct link to Data model setup")

Follow the steps below to set your data model up for ingesting cloud resources from New Relic:

1. Creating the blueprint configuration

After installing the New Relic integration, create the following blueprint configuration in Port:

**New Relic entity cloud resource blueprint (click to expand)**

Create in Port

```
{
  "identifier": "newRelicEntityCloudResource",
  "description": "This blueprint represents a New Relic cloud resource entity.",
  "title": "New Relic Cloud Resource",
  "icon": "NewRelic",
  "schema": {
    "properties": {
      "accountId": {
        "type": "string",
        "title": "Account ID",
        "description": "The New Relic account ID associated with the entity."
      },
      "domain": {
        "type": "string",
        "title": "Domain",
        "description": "The domain of the entity (e.g., INFRA, APM)."
      },
      "type": {
        "type": "string",
        "title": "Entity Type",
        "description": "The type of the entity."
      },
      "infrastructureIntegrationType": {
        "type": "string",
        "title": "Infrastructure Integration Type",
        "description": "The cloud provider integration type."
      },
      "tags": {
        "type": "object",
        "title": "Tags",
        "description": "Tags associated with the entity."
      },
      "reporting": {
        "type": "boolean",
        "title": "Reporting",
        "description": "Indicates if the entity is reporting data."
      },
      "link": {
        "type": "string",
        "title": "Entity Link",
        "description": "A link to the entity in New Relic.",
        "format": "url"
      }
    },
    "required": []
  },
  "relations": {},
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {}
}
```

2. Configuring the integration mapping

Locate the New Relic integration in the [Data Sources page](https://app.getport.io/settings/data-sources) and add the following mapping for cloud resources:

**New Relic `entity` mapping configuration**

```
  - kind: entity
    selector:
      query: 'true'
      entityQueryFilter:
        type IN (  
              # Add the infrastructure integration types you want to ingest
          'AWSEC2INSTANCE',
          'AWSS3BUCKET',
          'AWSRDSDBINSTANCE',
          'AWSLAMBDAFUNCTION',
          'AWSELBLOADBALANCER',
          'AZUREVIRTUALMACHINE',
          'AZURESQLDATABASE',
          'GCPCOMPUTEINSTANCE',
          'GCPSTORAGEBUCKET',
          'GCPSQLDATABASEINSTANCE'
        )
      entityExtraPropertiesQuery: |
        ... on InfrastructureHostEntityOutline {
          infrastructureIntegrationType
          # Include additional properties if needed
        }
    port:
      entity:
        mappings:
          blueprint: '"newRelicEntityCloudResource"'
          identifier: .guid
          title: .name
          properties:
            accountId: .accountId
            domain: .domain
            type: .entityType
            infrastructureIntegrationType: .type
            reporting: .reporting
            link: .permalink
            tags: .tags
```

3. Resyncing Data

After configuring the mapping, click on `Resync` to start ingesting your cloud resources from New Relic into Port.

![](/img/guides/newRelicIngestedData.png)

## More entity types[â](#more-entity-types "Direct link to More entity types")

Based on New Relic's documentation and common integrations, here's a comprehensive list of `infrastructureIntegrationType` values you can include in your mapping:

**Common Infrastructure Integration Types**

* **AWS Integration Types**

  * `AWSEC2INSTANCE`
  * `AWSEBSVOLUME`
  * `AWSS3BUCKET`
  * `AWSRDSDBINSTANCE`
  * `AWSLAMBDAFUNCTION`
  * `AWSELBLOADBALANCER`
  * `AWSDYNAMODBTABLE`
  * `AWSELASTICACHENODE`
  * `AWSREDSHIFTCLUSTER`
  * `AWSKINESISSTREAM`
  * `AWSSNSTOPIC`
  * `AWSSQSQUEUE`
  * `AWSELASTICBEANSTALK`
  * `AWSAUTOSCALINGGROUP`
  * `AWSCLOUDFRONTDISTRIBUTION`
  * `AWSAPIGATEWAY`
  * `AWSECSCLUSTER`
  * `AWSEKSCLUSTER`

* **Azure Integration Types**

  * `AZUREVIRTUALMACHINE`
  * `AZUREVMSCALESET`
  * `AZUREAPPSERVICE`
  * `AZUREFUNCTIONAPP`
  * `AZURESQLDATABASE`
  * `AZURESTORAGEACCOUNT`
  * `AZURECOSMOSDB`
  * `AZUREREDISCACHE`
  * `AZURESERVICEBUSNAMESPACE`
  * `AZUREEVENTHUBNAMESPACE`
  * `AZURELOADBALANCER`
  * `AZUREAPPLICATIONGATEWAY`
  * `AZURECONTAINERINSTANCE`
  * `AZUREKUBERNETESSERVICE`

* **GCP Integration Types**

  * `GCPCOMPUTEINSTANCE`
  * `GCPSTORAGEBUCKET`
  * `GCPCLOUDSQLDATABASE`
  * `GCPFUNCTION`
  * `GCPPUBSUBTOPIC`
  * `GCPBIGQUERYDATASET`
  * `GCPCLOUDSPANNERINSTANCE`
  * `GCPKUBERNETESCLUSTER`
  * `GCPCLOUDRUNSERVICE`

* **Other Integration Types**

  * `APACHEHTTPDSERVER`
  * `NGINXSERVER`
  * `MYSQLDATABASE`
  * `POSTGRESQLDATABASE`
  * `REDISINSTANCE`
  * `DOCKERCONTAINER`
  * `KUBERNETESCLUSTER`
