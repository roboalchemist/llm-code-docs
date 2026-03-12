# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint.md

# Set up blueprints

[YouTube video player](https://www.youtube.com/embed/ssBKpPiENQA)

<br />

Blueprints are the most basic building block in Port. They are used to represent assets in your organization, and the relationships between them.

Blueprints are comprised of [properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md), which are used to define the structure of the data they represent. Port supports a wide variety of property types, allowing you to model your data in the most accurate way possible.

Blueprints are completely customizable, and support any number of properties. They are created and managed in the [builder page](https://app.getport.io/settings) of the portal.

## Common blueprints[â](#common-blueprints "Direct link to Common blueprints")

Blueprints can be used to represent any asset in your software catalog, some common examples are:

* Microservices
* Packages
* Package versions
* CI jobs
* K8s Clusters
* Cloud accounts
* Cloud environments
* Developer environments
* Service deployment
* Pods
* VMs

Check out our [**live demo**](https://demo.port.io/settings) to see an example of a fleshed-out builder with a variety of blueprints.

## Configure blueprints in Port[â](#configure-blueprints-in-port "Direct link to Configure blueprints in Port")

Port offers a variety of ways to create and edit blueprints:

* UI
* API
* Terraform
* Pulumi

Create in Port

```
{
  "identifier": "myIdentifier",
  "title": "My title",
  "description": "My description",
  "icon": "My icon",
  "calculationProperties": {},
  "schema": {
    "properties": {},
    "required": []
  },
  "relations": {}
}
```

Check out Port's [API reference](/api-reference/port-api.md) to learn more.

#### To edit an existing blueprint:

1. Go to your [Builder page](https://app.port.io/settings/data-model).

2. Expand your desired blueprint by double-clicking on it.

3. Here you can add, remove, or edit this blueprint's [properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md) and [relations](/build-your-software-catalog/customize-integrations/configure-data-model/relate-blueprints/.md).

4. To edit the blueprint's metadata (title, icon, etc.), click on the `...` icon in the top right corner of the blueprint card, and choose `Edit blueprint`.

#### To create a new blueprint:

1. Go to your [Builder page](https://app.getport.io/settings).

2. Click on `+ Blueprint`:

3. Choose a title, icon, and description for your blueprint, then click `Create`.

4. Your blueprint has been created, the next step is to [ingest data into it](/build-your-software-catalog/sync-data-to-catalog/.md).

```
resource "port_blueprint" "myBlueprint" {
  title      = "My blueprint"
  icon       = "My icon"
  identifier = "myIdentifier"
  description = "My description"
  properties {
    string_props = {
      "myProperty" = {
        type  = "string"
        title = "My Property"
      }
      "myUrlProperty" = {
        title  = "URL Property"
        format = "url"
      }
    }
  }
}
```

Full example

For a full example, check the [Terraform-Managed Blueprint Example](/build-your-software-catalog/customize-integrations/configure-data-model/Iac/terraform-managed-blueprint.md) page.

* Python
* TypeScript
* JavaScript
* GO

```
"""A Python Pulumi program"""

impor t pulumi
from port_pulumi import Blueprint

blueprint = Blueprint(
    "myBlueprint",
    identifier="myBlueprint",
    title="My Blueprint",
    icon="My icon",
    description="My description",
    properties=port.BlueprintPropertiesArgs(
        string_props={
            "myStringProp": port.BlueprintPropertiesStringPropsArgs(
                title="My string", required=False
            ),
            "myUrlProp": port.BlueprintPropertiesStringPropsArgs(
                title="My url", required=False, format="url"
            ),
            "myEmailProp": port.BlueprintPropertiesStringPropsArgs(
                title="My email", required=False, format="email"
            ),
            "myUserProp": port.BlueprintPropertiesStringPropsArgs(
                title="My user", required=False, format="user"
            ),
            "myTeamProp": port.BlueprintPropertiesStringPropsArgs(
                title="My team", required=False, format="team"
            ),
            "myDatetimeProp": port.BlueprintPropertiesStringPropsArgs(
                title="My datetime", required=False, format="date-time"
            ),
            "myTimerProp": port.BlueprintPropertiesStringPropsArgs(
                title="My timer", required=False, format="timer"
            ),
            "myYAMLProp": port.BlueprintPropertiesStringPropsArgs(
                title="My yaml", required=False, format="yaml"
            ),
        }
    )
)
```

```
import * as pulumi from "@pulumi/pulumi";
import * as port from "@port-labs/port";

export const blueprint = new port.Blueprint("myBlueprint", {
  identifier: "myBlueprint",
  title: "My Blueprint",
  icon: "My icon",
  description: "My description",
  properties: [
    {
      identifier: "language",
      title: "Language",
      type: "string",
      required: true,
    },
  ],
});
```

```
"use strict";
const pulumi = require("@pulumi/pulumi");
const port = require("@port-labs/port");

const entity = new port.Blueprint("myBlueprint", {
  title: "My Blueprint",
  identifier: "myBlueprint",
  icon: "My icon",
  description: "My description",
  properties: [
    {
      name: "language",
      value: "Node",
    },
  ],
});

exports.title = entity.title;
```

```
package main

import (
	"github.com/port-labs/pulumi-port/sdk/v2/go/port"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		blueprint, err := port.NewBlueprint(ctx, "myBlueprint", &port.BlueprintArgs{
			Identifier: pulumi.String("myBlueprint"),
			Title:      pulumi.String("My Blueprint"),
			Icon:       pulumi.String("My icon"),
			Description: pulumi.String("My description"),
			Properties: port.BlueprintPropertiesArgs{
				StringProps: port.BlueprintPropertiesStringPropsMap{
					"myStringProp": port.BlueprintPropertiesStringPropsArgs{
						Title:    pulumi.String("My string"),
						Required: pulumi.Bool(false),
					},
				},
			},
		})
		ctx.Export("blueprint", blueprint.Title)
		if err != nil {
			return err
		}
		return nil
	})
}
```

Full example

For a full example, check the [Pulumi-Managed Blueprint Example](/build-your-software-catalog/customize-integrations/configure-data-model/Iac/pulumi-managed-blueprint.md) page.

## Blueprint structure[â](#blueprint-structure "Direct link to Blueprint structure")

Each blueprint is represented by a [Json schema](https://json-schema.org/), as shown in the following section:

Create in Port

```
{
  "identifier": "myIdentifier",
  "title": "My title",
  "description": "My description",
  "icon": "My icon",
  "calculationProperties": {},
  "schema": {
    "properties": {
      "myProp1": {
        "type": "my_type",
        "title": "My title"
      },
      "myProp2": {
        "type": "my_special_type",
        "title": "My special title"
      }
    },
    "required": []
  },
  "relations": {}
}
```

### Structure table[â](#structure-table "Direct link to Structure table")

| Field                   | Description                                                                                                                                                                                   | Notes                                                                                                                            |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `identifier`            | The identifier is used for API calls, programmatic access and distinguishing between different blueprints.                                                                                    | **Required**. (Maximum 100 characters)                                                                                           |
| `title`                 | Human-readable name for the blueprint.                                                                                                                                                        | **Required**. (Maximum 100 characters)                                                                                           |
| `description`           | The value is visible as a tooltip to users when hovering over the info icon in the UI.                                                                                                        |                                                                                                                                  |
| `icon`                  | Icon for the blueprint and entities of the blueprint.                                                                                                                                         | See the full icon list [below](#full-icon-list).                                                                                 |
| `calculationProperties` | Contains the properties defined using [calculation properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/calculation-property/.md). | **Required**                                                                                                                     |
| `mirrorProperties`      | Contains the properties defined using [mirror properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/mirror-property.md).            |                                                                                                                                  |
| `schema`                | An object containing two nested fields: `properties` and `required`.                                                                                                                          | **Required**. See the schema structure [here](#schema-object).                                                                   |
| `ownership`             | Defines how ownership of entities is determined.                                                                                                                                              | See the[ownership](https://docs.port.io/sso-rbac/users-and-teams/manage-users-teams#the-ownership-property) section for details. |

Available properties

All available properties are listed in the [properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md) page

### Schema object[â](#schema-object "Direct link to Schema object")

```
"schema": {
    "properties": {},
    "required": []
}
```

| Schema field | Description                                                                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `properties` | See the [`properties`](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md) section for more details. |
| `required`   | A list of the **required** properties, out of the `properties` object list.<br />These are mandatory fields to fill in the UI form.                       |

### Full icon list[â](#full-icon-list "Direct link to Full icon list")

Port provides a wide selection of built-in icons for use in blueprints, properties, actions, action inputs, etc. Enterprise customers can also [upload custom icons](/customize-pages-dashboards-and-plugins/customization.md#custom-icons) to align with their organization's branding.

**Full icon list (click to expand)**

`Actions, Add, AddUser, AI, Airflow, Alert, AmazonEC2, AmazonEKS, AmazonRDS, AmazonS3, Amplication, Ansible, API, APIalt, ApiDocs, APIEndpoint, AppRunner, Apps, Aqua, Argo, ArgoRollouts, Armis, AuditLog, Aws, Azure, AzureAD, AzureDevops, AzurePipline, AzureProvider, Backstage, BadgeAlert, Bar, BitBucket, BitBucketGitops, BlankPage, Blueprint, Bolt, Book, Box, Branch, Bucket, Buddy, Bug, Bulb, Calendar, Catalog, Chat, Checklist, Checkmarx, CICD, CircleCI, Clickup, Clock, ClockLoader, ClosedFolder, Cloud, Cloudflare, CloudFormation, Cluster, Codacy, Code, CodeBlocks, Codecov, Codefresh, Columns, Commit, ConcourseCI, Confluence, Consul, Cookiecutter, Coralogix, Cost, CPlusPlus, CPU, Crossplane, CSharp, Css3, CSV, Customer, Database, Databricks, Datadog, Day2Operation, DBT, DefaultBlueprint, DefaultProperty, Delete, Dependabot, DeployedAt, Deployment, Deployments, Details, DevopsTool, DevTV, Docker, Docs, DownArrow, Download, DrawIO, Drive, DynamicFeed, Dynatrace, Ecs, Edit, ElasticSearch, Emergency, EmptyBox, Environment, Environments, ErrorLogs, EU, Euro, Event, Exporter, Falcosidekick, Figma, Finance, FireHydrant, FitView, Flag, Flagsmith, Fluentd, Fluxcd, Flyway, GCE, General, Git, GitHub, GithubActions, GithubCopilot, GithubGitops, GitIssue, GitLab, GitLabGitops, GitPullRequest, GitSubIcon, GitVersion, GKE, Go, Google, GoogleCloud, GoogleCloudPlatform, GoogleMaps, GPU, Grafana, Graphql, groundcover, GroupBy, HAProxy, HashiCorp, Health, Helm, Help, Home, HourGlass, HourGlassExpired, Html5, Hubspot, Humio, IaC, Infinity, Instance, Istio, Java, Javascript, Jenkins, JFrog, JfrogXray, Jira, Job, Js, JsonEditor, JumpCloudProvider, Jupyter, Kafka, KafkaUI, Key, Kiali, Kibana, KNative, Komodor, Kotlin, Kubecost, Kyverno, Lambda, Lastpass, Launchdarkly, Layers, Learn, LeftArrow, Linear, LineChart, Link, LinkOut, Linux, List, Lock, LogOut, Logz, LucidCharts, Mail, Manager, ManageSearch, Markdown, Matlab, Merge, Metric, Microservice, Microservices, Microsoft, MicrosoftEntraID, Migrate, Miro, Misconfiguration, Mixpanel, MongoDb, Moon, Move, Neo4j, NewPage, NewRelic, Node, NodeJS, Notion, NSQ, Ocean, OctopusDeploy, Okta, OneLogin, Opencost, OpenFolder, OpsGenie, Organization, OutSystems, Package, Pagerduty, Perl, Permissions, Php, Pie, Pipeline, Plug, PlugOff, Port, PostgreSQL, Prometheus, Properties, Pulsar, Pulumi, Python, R, Rancher, React, RedhatOpenshift, Redis, Register, Relation, Reminder, Repeat, Reset, RightArrow, Rocket, Role, Rope, Ruby, SalesForce, Scala, Score, SDK, Search, SendGrid, Sensu, Sentry, Server, Service, Servicenow, Settings, SettingsEthernet, Share, Shield, Sinch, SingleStore, Siren, Slack, Snowflake, SNS, Snyk, SonarCloud, Sonarqube, SonartypeNexusIQ, Sort, Speed, Spinnaker, Spring, SQL, Stack, Stackhawk, StackOverflow, Star, StatusPage, Stonebranch, Stoplight, Store, Stripe, Sun, Supervisor, Support, Swagger, Swift, Sync, Table, Tableau, Team, TeamCity, Template, Terraform, Thanos, Travel, Tribe, Trivy, Twilio, TwoUsers, Typescript, Unavailable, Unleash, Unlock, UpArrow, Updates, Url, USA, User, Users, Version, Vulnerability, Webhook, Widget, Windows, Wiz, Youtrack, Zendesk, Zipkin`
