# Source: https://docs.port.io/guides/all/humanitec-integration.md

# Humanitec Integration

This guide demonstrates how to create a GitHub worklow integration to facilitate the ingestion of Humanitec applications, environments, workloads, resources, resource graphs, pipelines, deployment deltas, deployment sets, secret stores, shared values, value set versions, users, groups into your Port catalog on schedule.

![Humanitec Integration](/img/guides/humanitecEnvironments.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* Empower platform teams to gain visibility and advanced insights into your Humanitec entities including application, environments, users, and groups from Port among other entities.
* Track the status of changes to your Humanitec entities from Port.
* Prepare your Port environment to build useful experiences for Platform Engineering teams with Self Service Actions.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes the following:

* You have a Port account and have completed the [onboarding process](https://docs.port.io/getting-started/overview).
* You have a Humanitec account and a [Service User created](https://developer.humanitec.com/platform-orchestrator/docs/platform-orchestrator/security/service-users/) (You need an Administrator or Manager privilege to create a Service User).
* You have a GitHub account and a repository.

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

As a first step, you need to create blueprint definitions in Port for the Humanitec entities you want to ingest. To do this follow the steps below:

1. Go to the [Builder](https://app.getport.io/settings/data-model/data-model) page in your Port organization.

2. Click on the **+ Blueprint** button at the top of the page.

3. Click on `{...} Edit JSON` button at the top right corner.

4. Copy, paste and save the following blueprints JSON into the editor, repeating the process for each blueprint:

   **Humanitec Application Blueprint (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "humanitecApplication",
     "description": "Humanitec Application",
     "title": "humanitecApplication",
     "icon": "Apps",
     "schema": {
       "properties": {
         "createdAt": {
           "type": "string",
           "title": "Created At",
           "format": "date-time"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {}
   }
   ```

   **Humanitec Environment Blueprint (Click to expand)**

   Create in Port

   ```

   {
     "identifier": "humanitecEnvironment",
     "title": "Humanitec Environment",
     "icon": "Environment",
     "schema": {
       "properties": {
         "type": {
           "title": "Type",
           "icon": "DefaultProperty",
           "type": "string"
         },
         "createdAt": {
           "type": "string",
           "format": "date-time",
           "title": "Creation Date",
           "description": "The date and time when the environment was created."
         },
         "lastDeploymentStatus": {
           "type": "string",
           "title": "Last Deployment Status",
           "description": "The status of the last deployment."
         },
         "lastDeploymentDate": {
           "type": "string",
           "format": "date-time",
           "title": "Last Deployment Date",
           "description": "The date and time of the last time the environment was deployed."
         },
         "lastDeploymentComment": {
           "type": "string",
           "title": "Last Deployment Comment",
           "description": "comment on the last deployment"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "humanitecApplication": {
         "title": "Application",
         "target": "humanitecApplication",
         "required": false,
         "many": false
       }
     }
   }
   ```

   **Humanitec Workload Blueprint (Click to expand)**

   Create in Port

   ```

   {
     "identifier": "humanitecWorkload",
     "title": "Workload",
     "icon": "Cluster",
     "schema": {
       "properties": {
         "class": {
           "title": "Class",
           "description": "The class of the workload",
           "type": "string",
           "icon": "DefaultProperty"
         },
         "driverType": {
           "title": "Driver Type",
           "description": "The driver type of the workload",
           "type": "string",
           "icon": "DefaultProperty"
         },
         "definitionId": {
           "title": "Definition ID",
           "description": "The definition ID of the workload",
           "type": "string",
           "icon": "DefaultProperty"
         },
         "definitionVersionId": {
           "title": "Definition Version ID",
           "description": "The definition version ID of the workload",
           "type": "string",
           "icon": "DefaultProperty"
         },
         "status": {
           "title": "Status",
           "description": "The status of the workload",
           "type": "string",
           "icon": "DefaultProperty"
         },
         "updatedAt": {
           "title": "Update Date",
           "description": "The date and time when the workload was last updated",
           "type": "string",
           "format": "date-time",
           "icon": "DefaultProperty"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "humanitecEnvironment": {
         "title": "Environment",
         "target": "humanitecEnvironment",
         "required": false,
         "many": false
       }
     }
   }
   ```

   **Humanitec Resource Graph Blueprint (Click to expand)**

   Create in Port

   ```

   {
     "identifier": "humanitecResourceGraph",
     "description": "Humanitec Resource Graph",
     "title": "Resource Graph",
     "icon": "Microservice",
     "schema": {
       "properties": {},
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "humanitecResourceGraph": {
         "title": "Resource Graph",
         "target": "humanitecResourceGraph",
         "required": false,
         "many": true
       }
     }
   }
   ```

   **Humanitec Resource Blueprint (Click to expand)**

   Create in Port

   ```

   {
     "identifier": "humanitecResource",
     "title": "Humanitec Resource",
     "icon": "Microservice",
     "schema": {
       "properties": {
         "type": {
           "title": "Type",
           "description": "The type of the resource",
           "type": "string",
           "icon": "DefaultProperty"
         },
         "class": {
           "title": "Class",
           "description": "The class of the resource",
           "type": "string",
           "icon": "DefaultProperty"
         },
         "resource": {
           "title": "Resource",
           "description": "The resource",
           "type": "object",
           "icon": "DefaultProperty"
         },
         "resourceSchema": {
           "title": "Resource Schema",
           "description": "The schema of the resource",
           "type": "object",
           "icon": "DefaultProperty"
         },
         "guresid": {
           "title": "GU Resource ID",
           "description": "The GU resource ID",
           "type": "string",
           "icon": "DefaultProperty"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "humanitecResourceGraph": {
         "title": "Depends On",
         "description": "Resource Graph",
         "target": "humanitecResourceGraph",
         "required": false,
         "many": true
       },
       "humanitecWorkload": {
         "title": "Humanitec Workload",
         "target": "humanitecWorkload",
         "required": false,
         "many": false
       }
     }
   }
   ```

   **Humanitec Secret Stores (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "humanitecSecretStore",
       "title": "Humanitec Secret Store",
       "icon": "Lock",
       "schema": {
         "properties": {
           "primary": {
             "title": "Primary",
             "description": "Whether this is the primary secret store",
             "type": "boolean",
             "icon": "DefaultProperty"
           },
           "createdAt": {
             "title": "Created At",
             "description": "The date and time when the secret store was created",
             "type": "string",
             "format": "date-time",
             "icon": "DefaultProperty"
           },
           "createdBy": {
             "title": "Created By",
             "description": "The user who created the secret store",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "updatedAt": {
             "title": "Updated At",
             "description": "The date and time when the secret store was last updated",
             "type": "string",
             "format": "date-time",
             "icon": "DefaultProperty"
           },
           "updatedBy": {
             "title": "Updated By",
             "description": "The user who last updated the secret store",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "awssm": {
             "title": "AWS Secrets Manager",
             "description": "AWS Secrets Manager configuration",
             "type": "object",
             "icon": "DefaultProperty"
           },
           "azurekv": {
             "title": "Azure Key Vault",
             "description": "Azure Key Vault configuration",
             "type": "object",
             "icon": "DefaultProperty"
           },
           "gcpsm": {
             "title": "Google Cloud Secret Manager",
             "description": "Google Cloud Secret Manager configuration",
             "type": "object",
             "icon": "DefaultProperty"
           },
           "humanitec": {
             "title": "Humanitec",
             "description": "Humanitec secret store configuration",
             "type": "object",
             "icon": "DefaultProperty"
           },
           "vault": {
             "title": "Vault",
             "description": "HashiCorp Vault configuration",
             "type": "object",
             "icon": "DefaultProperty"
           }
         },
         "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "aggregationProperties": {},
       "relations": {}
   }
   ```

   **Humanitec Shared Values (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "humanitecSharedValue",
       "title": "Humanitec Shared Value",
       "icon": "Settings",
       "schema": {
         "properties": {
           "description": {
             "title": "Description",
             "description": "A human friendly description of what the Shared Value is",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "isSecret": {
             "title": "Is Secret",
             "description": "Specified that the Shared Value contains a secret",
             "type": "boolean",
             "icon": "DefaultProperty"
           },
           "secretKey": {
             "title": "Secret Key",
             "description": "Location of the secret value in the secret store",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "secretVersion": {
             "title": "Secret Version",
             "description": "Version of the current secret value as returned by the secret store",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "source": {
             "title": "Source",
             "description": "Source of the value, 'app' for app level, 'env' for app env level",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "value": {
             "title": "Value",
             "description": "The value that will be stored (will be always empty for secrets)",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "createdAt": {
             "title": "Created At",
             "description": "The date and time when the shared value was created",
             "type": "string",
             "format": "date-time",
             "icon": "DefaultProperty"
           },
           "updatedAt": {
             "title": "Updated At",
             "description": "The date and time when the shared value was last updated",
             "type": "string",
             "format": "date-time",
             "icon": "DefaultProperty"
           }
         },
         "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "aggregationProperties": {},
       "relations": {
         "humanitecApplication": {
           "title": "Application",
           "target": "humanitecApplication",
           "required": false,
           "many": false
         },
         "humanitecEnvironment": {
           "title": "Environment",
           "target": "humanitecEnvironment",
           "required": false,
           "many": false
         },
         "humanitecSecretStore": {
           "title": "Secret Store",
           "target": "humanitecSecretStore",
           "required": false,
           "many": false
         }
       }
   }
   ```

   **Humanitec Value Set Versions (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "humanitecValueSetVersion",
       "title": "Humanitec Value Set Version",
       "icon": "Version",
       "schema": {
         "properties": {
           "version": {
             "title": "Version",
             "description": "The version number",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "createdAt": {
             "title": "Created At",
             "description": "The date and time when the value set version was created",
             "type": "string",
             "format": "date-time",
             "icon": "DefaultProperty"
           },
           "createdBy": {
             "title": "Created By",
             "description": "The user who created the value set version",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "comment": {
             "title": "Comment",
             "description": "Comment for the value set version",
             "type": "string",
             "icon": "DefaultProperty"
           }
         },
         "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "aggregationProperties": {},
       "relations": {
         "humanitecApplication": {
           "title": "Application",
           "target": "humanitecApplication",
           "required": false,
           "many": false
         }
       }
   }
   ```

   **Humanitec Deployment Sets (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "humanitecDeploymentSet",
       "title": "Humanitec Deployment Set",
       "icon": "Deployment",
       "schema": {
         "properties": {
           "version": {
             "title": "Version",
             "description": "The version of the deployment set",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "createdAt": {
             "title": "Created At",
             "description": "The date and time when the deployment set was created",
             "type": "string",
             "format": "date-time",
             "icon": "DefaultProperty"
           },
           "createdBy": {
             "title": "Created By",
             "description": "The user who created the deployment set",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "comment": {
             "title": "Comment",
             "description": "Comment for the deployment set",
             "type": "string",
             "icon": "DefaultProperty"
           }
         },
         "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "aggregationProperties": {},
       "relations": {
         "humanitecApplication": {
           "title": "Application",
           "target": "humanitecApplication",
           "required": false,
           "many": false
         }
       }
   }
   ```

   **Humanitec Pipelines (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "humanitecPipeline",
       "title": "Humanitec Pipeline",
       "icon": "Pipeline",
       "schema": {
         "properties": {
           "etag": {
             "title": "ETag",
             "description": "Entity tag for the pipeline",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "name": {
             "title": "Name",
             "description": "The name of the pipeline",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "status": {
             "title": "Status",
             "description": "The status of the pipeline",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "version": {
             "title": "Version",
             "description": "The version of the pipeline",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "createdAt": {
             "title": "Created At",
             "description": "The date and time when the pipeline was created",
             "type": "string",
             "format": "date-time",
             "icon": "DefaultProperty"
           },
           "triggerTypes": {
             "title": "Trigger Types",
             "description": "Types of triggers for the pipeline",
             "type": "array",
             "icon": "DefaultProperty"
           },
           "metadata": {
             "title": "Metadata",
             "description": "Additional metadata for the pipeline",
             "type": "object",
             "icon": "DefaultProperty"
           }
         },
         "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "aggregationProperties": {},
       "relations": {
         "humanitecApplication": {
           "title": "Application",
           "target": "humanitecApplication",
           "required": false,
           "many": false
         }
       }
   }
   ```

   **Humanitec Deployment Deltas (Click to expand)**

   Create in Port

   ```
   {
     "identifier": "humanitecDeploymentDelta",
     "title": "Humanitec Deployment Delta",
     "icon": "Deployment",
     "schema": {
       "properties": {
         "archived": {
           "title": "Archived",
           "description": "Whether the deployment delta is archived",
           "type": "boolean",
           "icon": "DefaultProperty"
         },
         "contributers": {
           "title": "Contributers",
           "description": "The contributers of the deployment delta",
           "type": "array",
           "icon": "DefaultProperty"
         },
         "createdAt": {
           "title": "Created At",
           "description": "The date and time when the deployment delta was created",
           "type": "string",
           "format": "date-time",
           "icon": "DefaultProperty"
         },
         "createdBy": {
           "title": "Created By",
           "description": "The user who created the deployment delta",
           "type": "string",
           "icon": "DefaultProperty"
         },
         "modules": {
           "title": "Modules",
           "description": "The modules for the deployment delta",
           "type": "object",
           "icon": "DefaultProperty"
         },
         "shared": {
           "title": "Shared",
           "description": "The shared for the deployment delta",
           "type": "array",
           "icon": "DefaultProperty"
         }
       },
       "required": []
     },
     "mirrorProperties": {},
     "calculationProperties": {},
     "aggregationProperties": {},
     "relations": {
       "humanitecApplication": {
         "title": "Application",
         "target": "humanitecApplication",
         "required": false,
         "many": false
       },
       "humanitecEnvironment": {
         "title": "Environment",
         "target": "humanitecEnvironment",
         "required": false,
         "many": false
       }
     }
   }
   ```

   **Humanitec Users (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "humanitecUser",
       "title": "Humanitec User",
       "icon": "User",
       "schema": {
         "properties": {
           "email": {
             "title": "Email",
             "description": "The email address of the user",
             "type": "string",
             "icon": "User",
             "format": "user"
           },
           "role": {
             "title": "Role",
             "description": "The role of the user in the organization",
             "type": "string",
             "icon": "Role"
           },
           "invite": {
             "title": "Invite Status",
             "description": "The status of the user's invitation",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "createdAt": {
             "title": "Created At",
             "description": "The date and time when the user was created",
             "type": "string",
             "format": "date-time",
             "icon": "DefaultProperty"
           }
         },
         "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "aggregationProperties": {},
       "relations": {
         "humanitecGroup": {
           "title": "Groups",
           "target": "humanitecGroup",
           "required": false,
           "many": true
         }
       }
   }
   ```

   **Humanitec Groups (Click to expand)**

   Create in Port

   ```
   {
       "identifier": "humanitecGroup",
       "title": "Humanitec Group",
       "icon": "TwoUsers",
       "schema": {
         "properties": {
           "role": {
             "title": "Role",
             "description": "The role of the group in the organization",
             "type": "string",
             "icon": "Role"
           },
           "idp_id": {
             "title": "IDP ID",
             "description": "The identity provider ID",
             "type": "string",
             "icon": "DefaultProperty"
           },
           "createdAt": {
             "title": "Created At",
             "description": "The date and time when the group was created",
             "type": "string",
             "format": "date-time",
             "icon": "DefaultProperty"
           }
         },
         "required": []
       },
       "mirrorProperties": {},
       "calculationProperties": {},
       "aggregationProperties": {},
       "relations": {}
   }
   ```

   Blueprint selection

   You should select the blueprints depending on what you want to track in your Humanitec account.

## Set up the integration[â](#set-up-the-integration "Direct link to Set up the integration")

Fork our [humanitec integration repository](https://github.com/port-labs/humanitec-integration-script.git) to get started.

### Add secrets to your GitHub repository[â](#add-secrets-to-your-github-repository "Direct link to Add secrets to your GitHub repository")

In your GitHub repository, [go to **Settings > Secrets**](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) and add the following secrets:

* `HUMANITEC_API_KEY` - [Humanitec API Key](https://developer.humanitec.com/platform-orchestrator/docs/platform-orchestrator/security/service-users/#generate-an-api-token-from-a-service-user)
* `HUMANITEC_ORG_ID` - [Humanitec Organization ID](https://developer.humanitec.com/concepts/organizations/)
* `PORT_CLIENT_ID` - Your Port `client id` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).
* `PORT_CLIENT_SECRET` - Your Port `client secret` [How to get the credentials](https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/api/#find-your-port-credentials).

### Create the Python files[â](#create-the-python-files "Direct link to Create the Python files")

1. Create the following Python files in a folder named `integration` at the base directory of your GitHub repository:

   * `main.py` - Orchestrates the synchronization of data from Humanitec to Port, ensuring that resource entities are accurately mirrored and updated on your Port catalog.

     Add the following code to the `main.py` file:

     **Main Executable Script (Click to expand)**

     main.py

     ```

     import asyncio
     import argparse
     import time
     import datetime
     from decouple import config  # type: ignore
     import re
     import asyncio
     from loguru import logger
     from clients.humanitec_client import HumanitecClient
     from clients.port_client import PortClient
     import httpx


     class BLUEPRINT:
         APPLICATION = "humanitecApplication"
         ENVIRONMENT = "humanitecEnvironment"
         WORKLOAD = "humanitecWorkload"
         RESOURCE_GRAPH = "humanitecResourceGraph"
         RESOURCE = "humanitecResource"
         SECRET_STORE = "humanitecSecretStore"
         SHARED_VALUE = "humanitecSharedValue"
         VALUE_SET_VERSION = "humanitecValueSetVersion"
         DEPLOYMENT_SET = "humanitecDeploymentSet"
         PIPELINE = "humanitecPipeline"
         DEPLOYMENT_DELTA = "humanitecDeploymentDelta"
         USER = "humanitecUser"
         GROUP = "humanitecGroup"


     class HumanitecExporter:
         def __init__(self, args) -> None:

             timeout = httpx.Timeout(10.0, connect=10.0, read=20.0, write=10.0)
             httpx_async_client = httpx.AsyncClient(timeout=timeout)
             self.port_client = PortClient(
                 args.port_client_id,
                 args.port_client_secret,
                 httpx_async_client=httpx_async_client,
             )
             self.humanitec_client = HumanitecClient(
                 args.org_id,
                 args.api_key,
                 api_url=args.api_url,
                 httpx_async_client=httpx_async_client,
             )

         @staticmethod
         def convert_to_datetime(timestamp: int) -> str:
             converted_datetime = datetime.datetime.fromtimestamp(
                 timestamp / 1000.0, datetime.timezone.utc
             )
             return converted_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

         @staticmethod
         def remove_symbols_and_title_case(input_string: str) -> str:
             cleaned_string = re.sub(r"[^A-Za-z0-9\s]", " ", input_string)
             title_case_string = cleaned_string.title()
             return title_case_string

         async def sync_applications(self) -> None:
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.APPLICATION}")
             applications = await self.humanitec_client.get_all_applications()

             def create_entity(application):
                 return {
                     "identifier": application["id"],
                     "title": self.remove_symbols_and_title_case(application["name"]),
                     "properties": {"createdAt": application["created_at"]},
                     "relations": {},
                 }

             tasks = [
                 self.port_client.upsert_entity(
                     blueprint_id=BLUEPRINT.APPLICATION,
                     entity_object=create_entity(application),
                 )
                 for application in applications
             ]

             await asyncio.gather(*tasks)
             logger.info(f"Finished syncing entities for blueprint {BLUEPRINT.APPLICATION}")

         async def sync_environments(self) -> None:
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.ENVIRONMENT}")
             applications = await self.humanitec_client.get_all_applications()

             def create_entity(application, environment):
                 return {
                     "identifier": f"{application['id']}/{environment['id']}",
                     "title": environment["name"],
                     "properties": {
                         "type": environment["type"],
                         "createdAt": environment["created_at"],
                         "lastDeploymentStatus": environment.get("last_deploy", {}).get(
                             "status"
                         ),
                         "lastDeploymentDate": environment.get("last_deploy", {}).get(
                             "created_at"
                         ),
                         "lastDeploymentComment": environment.get("last_deploy", {}).get(
                             "comment"
                         ),
                     },
                     "relations": {BLUEPRINT.APPLICATION: application["id"]},
                 }

             tasks = [
                 self.port_client.upsert_entity(
                     blueprint_id=BLUEPRINT.ENVIRONMENT,
                     entity_object=create_entity(application, environment),
                 )
                 for application in applications
                 for environments in [
                     await self.humanitec_client.get_all_environments(application)
                 ]
                 for environment in environments
             ]
             await asyncio.gather(*tasks)
             logger.info(f"Finished syncing entities for blueprint {BLUEPRINT.ENVIRONMENT}")

         async def sync_workloads(self):
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.WORKLOAD}")

             def create_workload_entity(resource, application, environment):
                 identifier = f"{application['id']}/{environment['id']}/{resource['res_id'].replace('modules.', '')}"
                 return {
                     "identifier": identifier,
                     "title": self.remove_symbols_and_title_case(
                         resource["res_id"].replace("modules.", "")
                     ),
                     "properties": {
                         "status": resource["status"],
                         "class": resource["class"],
                         "driverType": resource["driver_type"],
                         "definitionVersionId": resource["def_version_id"],
                         "definitionId": resource["def_id"],
                         "updatedAt": resource["updated_at"],
                         "graphResourceID": resource["gu_res_id"],
                     },
                     "relations": {
                         BLUEPRINT.ENVIRONMENT: f"{application['id']}/{environment['id']}",
                     },
                 }

             applications = await self.humanitec_client.get_all_applications()
             for application in applications:
                 environments = await self.humanitec_client.get_all_environments(application)
                 for environment in environments:
                     resources = await self.humanitec_client.get_all_resources(
                         application, environment
                     )
                     resource_group = self.humanitec_client.group_resources_by_type(
                         resources
                     )
                     tasks = [
                         self.port_client.upsert_entity(
                             blueprint_id=BLUEPRINT.WORKLOAD,
                             entity_object=create_workload_entity(resource, application, environment),
                         )
                         for resource in resource_group.get("modules", [])
                         if resource and resource["type"] == "workload"
                     ]
                     await asyncio.gather(*tasks)
             logger.info(f"Finished syncing entities for blueprint {BLUEPRINT.WORKLOAD}")

         async def sync_resource_graphs(self) -> None:
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.RESOURCE_GRAPH}")

             def create_resource_graph_entity(
                 graph_data, include_relations, application, environment
             ):
                 entity = {
                     "identifier": graph_data["guresid"],
                     "title": self.remove_symbols_and_title_case(graph_data["def_id"]),
                     "properties": {
                         "type": graph_data["type"],
                         "class": graph_data["class"],
                         "resourceSchema": graph_data["resource_schema"],
                         "resource": graph_data["resource"],
                     },
                     "relations": {},
                 }
                 if include_relations:

                     entity["relations"] = {
                         BLUEPRINT.RESOURCE_GRAPH: graph_data["depends_on"],
                         BLUEPRINT.ENVIRONMENT: f"{application['id']}/{environment['id']}",
                     }
                 return entity

             applications = await self.humanitec_client.get_all_applications()
             for application in applications:
                 environments = await self.humanitec_client.get_all_environments(application)
                 for environment in environments:
                     graph_nodes = await self.humanitec_client.get_dependency_graph(
                         application, environment
                     )

                     # First pass: Create entities without relations
                     tasks = [
                         self.port_client.upsert_entity(
                             blueprint_id=BLUEPRINT.RESOURCE_GRAPH,
                             entity_object=create_resource_graph_entity(
                                 node, False, application, environment
                             ),
                         )
                         for node in graph_nodes
                     ]
                     await asyncio.gather(*tasks)

                     # Second pass: Update entities with relations
                     tasks = [
                         self.port_client.upsert_entity(
                             blueprint_id=BLUEPRINT.RESOURCE_GRAPH,
                             entity_object=create_resource_graph_entity(
                                 node, True, application, environment
                             ),
                         )
                         for node in graph_nodes
                     ]
                     await asyncio.gather(*tasks)
             logger.info(
                 f"Finished syncing entities for blueprint {BLUEPRINT.RESOURCE_GRAPH}"
             )

         async def enrich_resource_with_graph(self, resource, application, environment):
             try:
                 logger.info("Enriching resource %s with graph", resource["res_id"])
                 data = {
                     "id": resource["res_id"],
                     "type": resource["type"],
                     "resource": resource["resource"],
                 }
                 response = await self.humanitec_client.get_resource_graph(
                     application, environment, [data]
                 )

                 resource.update(
                     {"__resourceGraph": i for i in response if i["type"] == data["type"]}
                 )
                 return resource
             except Exception as e:
                 logger.error(
                     f"Failed to enrich resource {resource['res_id']} with graph: %s", str(e)
                 )
                 return resource

         async def sync_resources(self) -> None:
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.RESOURCE}")

             def create_resource_entity(resource):
                 workload_id = (
                     resource["res_id"].split(".")[1]
                     if resource["res_id"].split(".")[0].startswith("modules")
                     else ""
                 )
                 resource_id = (
                     f"{resource['app_id']}/{resource['env_id']}/{resource['res_id']}"
                 )
                 entity = {
                     "identifier": resource_id,
                     "title": self.remove_symbols_and_title_case(resource["def_id"]),
                     "properties": {
                         "type": resource["type"],
                         "class": resource["class"],
                         "resource": resource["resource"],
                         "status": resource["status"],
                         "updateAt": resource["updated_at"],
                         "driverType": resource["driver_type"],
                     },
                     "relations": {},
                 }
                 if workload_id:
                     workload_id = f"{resource['app_id']}/{resource['env_id']}/{workload_id}"
                     entity["relations"][BLUEPRINT.WORKLOAD] = workload_id
                 return entity

             applications = await self.humanitec_client.get_all_applications()
             for application in applications:
                 environments = await self.humanitec_client.get_all_environments(application)
                 for environment in environments:
                     resources = await self.humanitec_client.get_all_resources(
                         application, environment
                     )

                     entity_tasks = [
                         self.port_client.upsert_entity(
                             blueprint_id=BLUEPRINT.RESOURCE,
                             entity_object=create_resource_entity(resource),
                         )
                         for resource in resources
                     ]
                     await asyncio.gather(*entity_tasks)
                     logger.info(
                         "Upserted resource entities for %s environment", environment["id"]
                     )

             logger.info(f"Finished syncing entities for blueprint {BLUEPRINT.RESOURCE}")

         async def sync_secret_stores(self) -> None:
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.SECRET_STORE}")
             secret_stores = await self.humanitec_client.get_secret_stores()

             def create_secret_store_entity(secret_store):
                 # Determine the secret store type based on which configuration is present
                 secret_store_type = "unknown"
                 if secret_store.get("awssm") is not None:
                     secret_store_type = "AWS Secrets Manager"
                 elif secret_store.get("azurekv") is not None:
                     secret_store_type = "Azure Key Vault"
                 elif secret_store.get("gcpsm") is not None:
                     secret_store_type = "Google Cloud Secret Manager"
                 elif secret_store.get("humanitec") is not None:
                     secret_store_type = "Humanitec"
                 elif secret_store.get("vault") is not None:
                     secret_store_type = "HashiCorp Vault"
                 
                 # Create a title based on the type and ID
                 title = f"{secret_store_type} - {secret_store['id']}"
                 if secret_store.get("primary"):
                     title = f"{title} (Primary)"
                 
                 return {
                     "identifier": secret_store["id"],
                     "title": title,
                     "properties": {
                         "primary": secret_store.get("primary", False),
                         "createdAt": secret_store.get("created_at"),
                         "createdBy": secret_store.get("created_by"),
                         "updatedAt": secret_store.get("updated_at"),
                         "updatedBy": secret_store.get("updated_by"),
                         "awssm": secret_store.get("awssm"),
                         "azurekv": secret_store.get("azurekv"),
                         "gcpsm": secret_store.get("gcpsm"),
                         "humanitec": secret_store.get("humanitec"),
                         "vault": secret_store.get("vault"),
                     },
                     "relations": {},
                 }

             tasks = [
                 self.port_client.upsert_entity(
                     blueprint_id=BLUEPRINT.SECRET_STORE,
                     entity_object=create_secret_store_entity(secret_store),
                 )
                 for secret_store in secret_stores
             ]

             await asyncio.gather(*tasks)
             logger.info(f"Finished syncing entities for blueprint {BLUEPRINT.SECRET_STORE}")

         async def sync_shared_values(self) -> None:
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.SHARED_VALUE}")
             applications = await self.humanitec_client.get_all_applications()

             def create_shared_value_entity(shared_value, application, environment=None):
                 # Create identifier based on source and context
                 if environment:
                     identifier = f"{application['id']}/{environment['id']}/{shared_value['key']}"
                 else:
                     identifier = f"{application['id']}/{shared_value['key']}"
                 
                 
                 # Build relations
                 relations = {BLUEPRINT.APPLICATION: application["id"]}
                 
                 if environment:
                     relations[BLUEPRINT.ENVIRONMENT] = f"{application['id']}/{environment['id']}"
                 
                 # Add secret store relation if present
                 if shared_value.get("secret_store_id"):
                     relations[BLUEPRINT.SECRET_STORE] = shared_value["secret_store_id"]
                 
                 return {
                     "identifier": identifier,
                     "title": shared_value["key"],
                     "properties": {
                         "description": shared_value.get("description"),
                         "isSecret": shared_value.get("is_secret", False),
                         "key": shared_value.get("key"),
                         "secretKey": shared_value.get("secret_key"),
                         "secretVersion": shared_value.get("secret_version"),
                         "source": shared_value.get("source"),
                         "value": shared_value.get("value"),
                         "createdAt": shared_value.get("created_at"),
                         "updatedAt": shared_value.get("updated_at"),
                     },
                     "relations": relations,
                 }

             # Sync app-level shared values
             app_level_tasks = []
             for application in applications:
                 shared_values = await self.humanitec_client.get_shared_values_app_level(application)
                 app_level_tasks.extend([
                     self.port_client.upsert_entity(
                         blueprint_id=BLUEPRINT.SHARED_VALUE,
                         entity_object=create_shared_value_entity(shared_value, application),
                     )
                     for shared_value in shared_values
                 ])

             # Sync environment-level shared values
             env_level_tasks = []
             for application in applications:
                 environments = await self.humanitec_client.get_all_environments(application)
                 for environment in environments:
                     shared_values = await self.humanitec_client.get_shared_values(application, environment)
                     env_level_tasks.extend([
                         self.port_client.upsert_entity(
                             blueprint_id=BLUEPRINT.SHARED_VALUE,
                             entity_object=create_shared_value_entity(shared_value, application, environment),
                         )
                         for shared_value in shared_values
                     ])

             await asyncio.gather(*(app_level_tasks + env_level_tasks))
             logger.info(f"Finished syncing entities for blueprint {BLUEPRINT.SHARED_VALUE}")

         async def sync_value_set_versions(self) -> None:
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.VALUE_SET_VERSION}")
             applications = await self.humanitec_client.get_all_applications()

             def create_value_set_version_entity(value_set_version, application):
                 return {
                     "identifier": f"{application['id']}/{value_set_version['id']}",
                     "title": f"Value Set Version {value_set_version['id']}",
                     "properties": {
                         "version": value_set_version.get("version"),
                         "createdAt": value_set_version.get("created_at"),
                         "createdBy": value_set_version.get("created_by"),
                         "comment": value_set_version.get("comment"),
                     },
                     "relations": {BLUEPRINT.APPLICATION: application["id"]},
                 }

             tasks = []
             for application in applications:
                 value_set_versions = await self.humanitec_client.get_value_set_versions(application)
                 tasks.extend([
                     self.port_client.upsert_entity(
                         blueprint_id=BLUEPRINT.VALUE_SET_VERSION,
                         entity_object=create_value_set_version_entity(value_set_version, application),
                     )
                     for value_set_version in value_set_versions
                 ])

             await asyncio.gather(*tasks)
             logger.info(f"Finished syncing entities for blueprint {BLUEPRINT.VALUE_SET_VERSION}")

         async def sync_deployment_sets(self) -> None:
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.DEPLOYMENT_SET}")
             applications = await self.humanitec_client.get_all_applications()

             def create_deployment_set_entity(deployment_set, application):
                 return {
                     "identifier": f"{application['id']}/{deployment_set['id']}",
                     "title": self.remove_symbols_and_title_case(deployment_set.get("name", deployment_set["id"])),
                     "properties": {
                         "version": deployment_set.get("version"),
                         "createdAt": deployment_set.get("created_at"),
                         "createdBy": deployment_set.get("created_by"),
                         "comment": deployment_set.get("comment"),
                     },
                     "relations": {BLUEPRINT.APPLICATION: application["id"]},
                 }

             tasks = []
             for application in applications:
                 deployment_sets = await self.humanitec_client.get_deployment_sets(application)
                 tasks.extend([
                     self.port_client.upsert_entity(
                         blueprint_id=BLUEPRINT.DEPLOYMENT_SET,
                         entity_object=create_deployment_set_entity(deployment_set, application),
                     )
                     for deployment_set in deployment_sets
                 ])

             await asyncio.gather(*tasks)
             logger.info(f"Finished syncing entities for blueprint {BLUEPRINT.DEPLOYMENT_SET}")

         async def sync_pipelines(self) -> None:
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.PIPELINE}")
             pipelines = await self.humanitec_client.get_pipelines()
             
             # Get cached applications to map pipeline to app names
             applications = await self.humanitec_client.get_all_applications()
             app_map = {app["id"]: app for app in applications}

             def create_pipeline_entity(pipeline):
                 app_id = pipeline.get("app_id")
                 app_name = app_map.get(app_id, {}).get("name", "Unknown App")
                 
                 # Create identifier that includes app context
                 identifier = f"{app_id}/{pipeline['id']}"
                 
                 # Create title that includes app name and pipeline name
                 pipeline_name = pipeline.get("name", pipeline["id"])
                 title = f"{app_name} - {pipeline_name}"
                 
                 return {
                     "identifier": identifier,
                     "title": title,
                     "properties": {
                         "etag": pipeline.get("etag"),
                         "name": pipeline.get("name"),
                         "status": pipeline.get("status"),
                         "version": pipeline.get("version"),
                         "createdAt": pipeline.get("created_at"),
                         "triggerTypes": pipeline.get("trigger_types", []),
                         "metadata": pipeline.get("metadata", {}),
                     },
                     "relations": {
                         BLUEPRINT.APPLICATION: app_id
                     } if app_id else {},
                 }

             tasks = [
                 self.port_client.upsert_entity(
                     blueprint_id=BLUEPRINT.PIPELINE,
                     entity_object=create_pipeline_entity(pipeline),
                 )
                 for pipeline in pipelines
             ]

             await asyncio.gather(*tasks)
             logger.info(f"Finished syncing entities for blueprint {BLUEPRINT.PIPELINE}")

         async def sync_deployment_deltas(self) -> None:
             logger.info(f"Syncing entities for blueprint {BLUEPRINT.DEPLOYMENT_DELTA}")
             applications = await self.humanitec_client.get_all_applications()

             def create_deployment_delta_entity(deployment_delta, application):
                 return {
                     "identifier": f"{application['id']}/{deployment_delta['id']}",
                     "title": self.remove_symbols_and_title_case(deployment_delta.get("name", deployment_delta["id"])),
                     "properties": {
                         "status": deployment_delta.get("status"),
                         "createdAt": deployment_delta.get("created_at"),
                         "createdBy": deployment_delta.get("created_by"),
                         "comment": deployment_delta.get("comment"),
                         "environment": deployment_delta.get("environment"),
                     },
                     "relations": {BLUEPRINT.APPLICATION: application["id"]},
                 }

             tasks = []
             for application in applications:
                 deployment_deltas = await self.humanitec_client.get_deployment_deltas(application)
                 tasks.extend([
                     self.port_client.upsert_entity(
                         blueprint_id=BLUEPRINT.DEPLOYMENT_DELTA,
                         entity_object=create_deployment_delta_entity(deployment_delta, application),
                     )
                     for deployment_delta in deployment_deltas
                 ])

             await asyncio.gather(*tasks)
             logger.info(f"Finished syncing entities for blueprint {BLUEPRINT.DEPLOYMENT_DELTA}")

         async def sync_users_and_groups(self) -> None:
             logger.info(f"Syncing entities for blueprints {BLUEPRINT.USER} and {BLUEPRINT.GROUP}")
             
             all_users, all_groups = await self.humanitec_client.get_users_and_groups()
             
             user_groups = {}
             
             for user in all_users:
                 user_groups[user["id"]] = []
             
             group_tasks = [
                 self.humanitec_client.get_users_in_group(group["id"])
                 for group in all_groups
             ]
             
             group_results = await asyncio.gather(*group_tasks, return_exceptions=True)
             
             for i, result in enumerate(group_results):
                 group_id = all_groups[i]["id"]
                 
                 if isinstance(result, Exception):
                     logger.error(f"Failed to get users for group {group_id}: {str(result)}")
                     continue
                     
                 for user in result:
                     user_id = user["id"]
                     if user_id in user_groups:
                         user_groups[user_id].append(group_id)

             def create_group_entity(group):
                 return {
                     "identifier": group["id"],
                     "title": group["name"],
                     "properties": {
                         "role": group.get("role"),
                         "idp_id": group.get("idp_id"),
                         "createdAt": group.get("created_at"),
                     },
                     "relations": {},
                 }

             def create_user_entity(user):
                 return {
                     "identifier": user["id"],
                     "title": user["name"],
                     "properties": {
                         "email": user.get("email"),
                         "role": user.get("role"),
                         "invite": user.get("invite"),
                         "createdAt": user.get("created_at"),
                     },
                     "relations": {
                         BLUEPRINT.GROUP: user_groups.get(user["id"], [])
                     },
                 }

             group_tasks = [
                 self.port_client.upsert_entity(
                     blueprint_id=BLUEPRINT.GROUP,
                     entity_object=create_group_entity(group),
                 )
                 for group in all_groups
             ]

             user_tasks = [
                 self.port_client.upsert_entity(
                     blueprint_id=BLUEPRINT.USER,
                     entity_object=create_user_entity(user),
                 )
                 for user in all_users
             ]

             await asyncio.gather(*(group_tasks + user_tasks))
             logger.info(f"Finished syncing {len(all_groups)} groups and {len(all_users)} users")

         async def sync_all(self) -> None:
             await self.sync_applications()
             await self.sync_environments()
             await self.sync_workloads()
             await self.sync_resource_graphs()
             await self.sync_resources()
             await self.sync_secret_stores()
             await self.sync_shared_values()
             await self.sync_value_set_versions()
             await self.sync_deployment_sets()
             await self.sync_pipelines()
             await self.sync_deployment_deltas()
             await self.sync_users_and_groups()
             logger.info("Event Finished")

         async def __call__(self, args) -> None:
             await self.sync_all()


     if __name__ == "__main__":

         def validate_args(args):
             required_keys = ["org_id", "api_key", "port_client_id", "port_client_secret"]
             missing_keys = [key for key in required_keys if not getattr(args, key)]

             if missing_keys:
                 logger.error(f"The following keys are required: {', '.join(missing_keys)}")
                 return False
             return True

         parser = argparse.ArgumentParser()
         parser.add_argument(
             "--org-id",
             required=False,
             default=config("ORG_ID", ""),
             type=str,
             help="Humanitec organization ID",
         )
         parser.add_argument(
             "--api-key",
             required=False,
             default=config("API_KEY", ""),
             type=str,
             help="Humanitec API key",
         )
         parser.add_argument(
             "--api-url",
             type=str,
             default=config("API_URL", "https://api.humanitec.com"),
             help="Humanitec API URL",
         )
         parser.add_argument(
             "--port-client-id",
             type=str,
             required=False,
             default=config("PORT_CLIENT_ID", ""),
             help="Port client ID",
         )
         parser.add_argument(
             "--port-client-secret",
             type=str,
             required=False,
             default=config("PORT_CLIENT_SECRET", ""),
             help="Port client secret",
         )
         args = parser.parse_args()
         if not (validate_args(args)):
             import sys

             sys.exit()

         exporter = HumanitecExporter(args)
         asyncio.run(exporter(args))
     ```

   * `config.py` - Contains the configuration constants for the integration, including cache TTL, connection pooling, and other settings.

     Add the following code to the `config.py` file:

     **Config (Click to expand)**

     config.py

     ```

     """
     Configuration constants for the Humanitec integration.
     """

     MAX_RETRY_ATTEMPTS = 5
     DEFAULT_TIMEOUT_SECONDS = 30
     RETRY_DELAY_SECONDS = 1
     USE_EXPONENTIAL_BACKOFF = True
     MAX_RETRY_DELAY_SECONDS = 10

     MAX_CONNECTIONS = 20
     MAX_KEEPALIVE_CONNECTIONS = 10
     KEEPALIVE_EXPIRY = 30

     CACHE_TTL_SECONDS = 300

     LOG_LEVEL = "INFO" 
     ```

   * `requirements.txt` - This file contains the dependencies or necessary external packages need to run the integration

     Add the following code to the `requirements.txt` file:

     **Requirements (Click to expand)**

     requirements.txt

     ```

     python-decouple==3.8
     loguru==0.7.2
     httpx==0.27.0
     loguru==0.7.2
     ```

2. Create the following Python files in a folder named `clients` at the base directory of the `integration` folder:

   * `port_client.py` â Manages authentication and API requests to Port, facilitating the creation and updating of entities within Port's system.

     Add the following code to the `port_client.py` file:

     **Port Client (Click to expand)**

     port\_client.py

     ```

     import httpx
     from typing import Any, Dict, Optional, List
     from loguru import logger
     from .retryable_http_client import RetryableHTTPClient


     class PortClient:
         def __init__(self, client_id: str, client_secret: str, **kwargs) -> None:
             # Inject the retryable HTTP client
             self.http_client = kwargs.get("http_client")
             if not self.http_client:
                 timeout = kwargs.get("timeout", httpx.Timeout(20))
                 self.http_client = RetryableHTTPClient(timeout=timeout)
             
             self.client_id = client_id
             self.client_secret = client_secret
             self.base_url = kwargs.get("base_url", "https://api.port.io/v1")
             self.port_headers = None

         async def send_api_request(
             self,
             method: str,
             endpoint: str,
             headers: Optional[Dict[str, str]] = None,
             json: Optional[Dict[str, Any]] = None,
         ) -> Dict[str, Any]:
             """Send API request using the injected retryable HTTP client."""
             url = f"{self.base_url}{endpoint}"
             response = await self.http_client.request(method, url, headers=headers, json=json)
             return response.json()

         async def get_port_access_token(self) -> str:
             credentials = {"clientId": self.client_id, "clientSecret": self.client_secret}
             endpoint = f"/auth/access_token"
             response = await self.send_api_request("POST", endpoint, json=credentials)
             access_token = response["accessToken"]
             return access_token

         async def get_port_headers(self) -> Dict[str, str]:
             access_token = await self.get_port_access_token()
             port_headers = {"Authorization": f"Bearer {access_token}"}
             return port_headers

         async def upsert_entity(
             self, blueprint_id: str, entity_object: Dict[str, Any]
         ) -> Dict[str, Any]:
             """Upsert a single entity (legacy method for backward compatibility)."""
             endpoint = f"/blueprints/{blueprint_id}/entities?upsert=true&merge=true"
             port_headers = (
                 self.port_headers if self.port_headers else await self.get_port_headers()
             )
             response = await self.send_api_request(
                 "POST", endpoint, headers=port_headers, json=entity_object
             )
             logger.info(response)
             return response

         async def upsert_entities_bulk(
             self, blueprint_id: str, entity_objects: List[Dict[str, Any]]
         ) -> Dict[str, Any]:
             """
             Upsert multiple entities using the bulk endpoint.
             
             Args:
                 blueprint_id: The blueprint identifier
                 entity_objects: List of entity objects to upsert (max 20 per request)
                 
             Returns:
                 Dict containing the response from the bulk operation
                 
             Raises:
                 ValueError: If more than 20 entities are provided
             """
             if len(entity_objects) > 20:
                 raise ValueError(f"Maximum 20 entities allowed per bulk request, got {len(entity_objects)}")
             
             endpoint = f"/blueprints/{blueprint_id}/entities/bulk?upsert=true&merge=true"
             port_headers = (
                 self.port_headers if self.port_headers else await self.get_port_headers()
             )
             
             response = await self.send_api_request(
                 "POST", endpoint, headers=port_headers, json={"entities": entity_objects}
             )
             
             logger.info(f"Bulk upserted {len(entity_objects)} entities for blueprint {blueprint_id}")
             return response

         async def upsert_entities_batched(
             self, blueprint_id: str, entity_objects: List[Dict[str, Any]], batch_size: int = 20
         ) -> List[Dict[str, Any]]:
             """
             Upsert multiple entities in batches using the bulk endpoint.
             
             Args:
                 blueprint_id: The blueprint identifier
                 entity_objects: List of entity objects to upsert
                 batch_size: Number of entities per batch (max 20)
                 
             Returns:
                 List of responses from all batch operations
             """
             if batch_size > 20:
                 batch_size = 20
                 logger.warning(f"Batch size reduced to 20 (maximum allowed)")
             
             responses = []
             total_entities = len(entity_objects)
             
             for i in range(0, total_entities, batch_size):
                 batch = entity_objects[i:i + batch_size]
                 batch_num = (i // batch_size) + 1
                 total_batches = (total_entities + batch_size - 1) // batch_size
                 
                 logger.info(f"Processing batch {batch_num}/{total_batches} with {len(batch)} entities")
                 
                 try:
                     response = await self.upsert_entities_bulk(blueprint_id, batch)
                     responses.append(response)
                     logger.info(f"Successfully processed batch {batch_num}/{total_batches}")
                 except Exception as e:
                     logger.error(f"Failed to process batch {batch_num}/{total_batches}: {e}")
                     raise
             
             logger.info(f"Completed bulk upsert of {total_entities} entities in {len(responses)} batches")
             return responses

         async def close(self):
             """Close the HTTP client."""
             if self.http_client:
                 await self.http_client.close()
     ```

   * `humanitec_client.py` â Handles API interactions with Humanitec, including retrieving data with caching mechanisms to optimize performance.

     Add the following code to the `humanitec_client.py` file:

     **Humanitec Client (Click to expand)**

     humanitec\_client.py

     ```

     import httpx
     from typing import Dict, Any, List, Optional
     from loguru import logger
     from .cache import InMemoryCache
     from .retryable_http_client import RetryableHTTPClient


     class CACHE_KEYS:
         APPLICATION = "APPLICATION_CACHE_KEY"
         ENVIRONMENT = "ENVIRONMENT_CACHE_KEY"
         RESOURCE = "RESOURCE_CACHE_KEY"


     class HumanitecClient:
         def __init__(self, org_id: str, api_token: str, **kwargs) -> None:
             # Inject the retryable HTTP client
             self.http_client = kwargs.get("http_client")
             if not self.http_client:
                 timeout = kwargs.get("timeout", httpx.Timeout(20))
                 self.http_client = RetryableHTTPClient(timeout=timeout)
             
             self.base_url = (
                 f"{kwargs.get('base_url','https://api.humanitec.io')}/orgs/{org_id}/"
             )
             self.api_token = api_token
             self.cache = InMemoryCache()
             self.port_headers = None

         def get_humanitec_headers(self) -> Dict[str, str]:
             humanitec_headers = {
                 "Authorization": f"Bearer {self.api_token}",
                 "Content-Type": "application/json",
             }
             return humanitec_headers

         async def send_api_request(
             self,
             method: str,
             endpoint: str,
             headers: Optional[Dict[str, str]] = None,
             json: Optional[Dict[str, Any] | List[Dict[str, Any]]] = None,
         ) -> Any:
             """Send API request using the injected retryable HTTP client."""
             url = self.base_url + endpoint
             logger.debug(f"Requesting Humanitec data for endpoint: {endpoint}")
             response = await self.http_client.request(method, url, headers=headers, json=json)
             return response.json()

         async def get_all_applications(self) -> List[Dict[str, Any]]:
             if cached_applications := await self.cache.get(CACHE_KEYS.APPLICATION):
                 logger.info(f"Retrieved {len(cached_applications)} applications from cache")
                 return list(cached_applications.values())

             endpoint = "apps"
             humanitec_headers = self.get_humanitec_headers()
             applications: List[Dict[str, Any]] = await self.send_api_request(
                 "GET", endpoint, headers=humanitec_headers
             )

             await self.cache.set(
                 CACHE_KEYS.APPLICATION, {app["id"]: app for app in applications}
             )
             logger.info(f"Received {len(applications)} applications from Humanitec")

             return applications

         async def get_all_environments(self, app) -> List[Dict[str, Any]]:

             try:
                 if cached_environments := await self.cache.get(CACHE_KEYS.ENVIRONMENT):
                     if app_environments := cached_environments.get(app["id"]):
                         logger.info(
                             f"Retrieved {len(app_environments)} environment for {app['id']} from cache"
                         )
                         return list(app_environments.values())

                 logger.info("Fetching environments from Humanitec")

                 endpoint = f"apps/{app['id']}/envs"
                 humanitec_headers = self.get_humanitec_headers()
                 environments: List[Dict[str, Any]] = await self.send_api_request(
                     "GET", endpoint, headers=humanitec_headers
                 )
                 await self.cache.set(
                     CACHE_KEYS.ENVIRONMENT,
                     {
                         app["id"]: {
                             environment["id"]: environment for environment in environments
                         }
                     },
                 )
                 logger.info(f"Received {len(environments)} environments from Humanitec")
                 return environments
             except Exception as e:
                 logger.error(f"Failed to fetch environments from {app['id']}: {str(e)}")
                 return []

         async def get_all_resources(self, app, env) -> List[Dict[str, Any]]:
             try:
                 if cached_resources := await self.cache.get(CACHE_KEYS.RESOURCE):
                     if env_resources := cached_resources.get(app["id"], {}).get(
                         env["id"]
                     ):
                         logger.info(
                             f"Retrieved {len(env_resources)} resources from cache for app {app['id']} and env {env['id']}"
                         )
                         return list(env_resources.values())

                 logger.info("Fetching resources from Humanitec")
                 endpoint = f"apps/{app['id']}/envs/{env['id']}/resources"
                 humanitec_headers = self.get_humanitec_headers()
                 resources: List[Dict[str, Any]] = await self.send_api_request(
                     "GET", endpoint, headers=humanitec_headers
                 )
                 await self.cache.set(
                     CACHE_KEYS.RESOURCE,
                     {
                         app["id"]: {
                             env["id"]: {
                                 resource["gu_res_id"]: resource for resource in resources
                             }
                         }
                     },
                 )
                 logger.info(
                     f"Received {len(resources)} resources for {env['id']} environment in {app['id']}"
                 )
                 return resources
             except Exception as e:
                 logger.error(
                     f"Failed to fetch resources for {env['id']} environment in {app[id]}: {str(e)}"
                 )
                 return []

         async def get_dependency_graph(
             self, app: Dict[str, Any], env: Dict[str, Any]
         ) -> List[Dict[str, Any]]:
             try:
                 if dependency_graph_id := env.get("last_deploy", {}).get("dependency_graph_id"):
                     endpoint = f"apps/{app['id']}/envs/{env['id']}/resources/graphs/{dependency_graph_id}"
                     humanitec_headers = self.get_humanitec_headers()
                     graph = await self.send_api_request(
                         "GET", endpoint, headers=humanitec_headers
                     )
                     nodes = graph["nodes"]
                     logger.info(
                         f"Received {len(nodes)} graph nodes for {env['id']} environment in {app['id']}"
                     )
                     return nodes

                 logger.info(
                     f"No dependency graph found for {env['id']} environment in {app['id']}"
                 )
                 return []
             except Exception as e:
                 logger.error(
                     f"Failed to fetch dependency graphs for {env['id']} environment in {app['id']}: {str(e)}"
                 )
                 return []

         async def get_resource_graph(
             self, app: Dict[str, Any], env: Dict[str, Any], data: List[Dict[str, Any]]
         ) -> Any:
             endpoint = f"apps/{app['id']}/envs/{env['id']}/resources/graph"
             humanitec_headers = self.get_humanitec_headers()
             graph = await self.send_api_request(
                 "POST", endpoint, headers=humanitec_headers, json=data
             )
             return graph

         def group_resources_by_type(
             self, data: List[Dict[str, Any]]
         ) -> Dict[str, List[Dict[str, Any]]]:
             grouped_resources: dict[str, Any] = {}
             for resource in data:
                 workload_id = resource["res_id"].split(".")[0]
                 if workload_id not in grouped_resources:
                     grouped_resources[workload_id] = []
                 grouped_resources[workload_id].append(resource)
             return grouped_resources

         async def get_secret_stores(self) -> List[Dict[str, Any]]:
             """Get all secret stores for the organization."""
             endpoint = "secretstores"
             humanitec_headers = self.get_humanitec_headers()
             secret_stores: List[Dict[str, Any]] = await self.send_api_request(
                 "GET", endpoint, headers=humanitec_headers
             )
             logger.info(f"Received {len(secret_stores)} secret stores from Humanitec")
             return secret_stores

         async def get_shared_values(self, app: Dict[str, Any], env: Dict[str, Any]) -> List[Dict[str, Any]]:
             """Get shared values for a specific environment."""
             endpoint = f"apps/{app['id']}/envs/{env['id']}/values"
             humanitec_headers = self.get_humanitec_headers()
             shared_values: List[Dict[str, Any]] = await self.send_api_request(
                 "GET", endpoint, headers=humanitec_headers
             )
             logger.info(f"Received {len(shared_values)} shared values for {env['id']} environment in {app['id']}")
             return shared_values

         async def get_shared_values_app_level(self, app: Dict[str, Any]) -> List[Dict[str, Any]]:
             """Get shared values at application level."""
             endpoint = f"apps/{app['id']}/values"
             humanitec_headers = self.get_humanitec_headers()
             shared_values: List[Dict[str, Any]] = await self.send_api_request(
                 "GET", endpoint, headers=humanitec_headers
             )
             logger.info(f"Received {len(shared_values)} app-level shared values for {app['id']}")
             return shared_values

         async def get_value_set_versions(self, app: Dict[str, Any]) -> List[Dict[str, Any]]:
             """Get value set versions for an application."""
             endpoint = f"apps/{app['id']}/value-set-versions"
             humanitec_headers = self.get_humanitec_headers()
             value_set_versions: List[Dict[str, Any]] = await self.send_api_request(
                 "GET", endpoint, headers=humanitec_headers
             )
             logger.info(f"Received {len(value_set_versions)} value set versions for {app['id']}")
             return value_set_versions

         async def get_deployment_sets(self, app: Dict[str, Any]) -> List[Dict[str, Any]]:
             """Get deployment sets for an application."""
             endpoint = f"apps/{app['id']}/sets"
             humanitec_headers = self.get_humanitec_headers()
             deployment_sets: List[Dict[str, Any]] = await self.send_api_request(
                 "GET", endpoint, headers=humanitec_headers
             )
             logger.info(f"Received {len(deployment_sets)} deployment sets for {app['id']}")
             return deployment_sets

         async def get_pipelines(self) -> List[Dict[str, Any]]:
             """Get all pipelines in the organization."""
             endpoint = "pipelines"
             humanitec_headers = self.get_humanitec_headers()
             pipelines: List[Dict[str, Any]] = await self.send_api_request(
                 "GET", endpoint, headers=humanitec_headers
             )
             logger.info(f"Received {len(pipelines)} pipelines from Humanitec")
             return pipelines

         async def get_deployment_deltas(self, app: Dict[str, Any]) -> List[Dict[str, Any]]:
             """Get deployment deltas for an application."""
             endpoint = f"apps/{app['id']}/deltas"
             humanitec_headers = self.get_humanitec_headers()
             deployment_deltas: List[Dict[str, Any]] = await self.send_api_request(
                 "GET", endpoint, headers=humanitec_headers
             )
             logger.info(f"Received {len(deployment_deltas)} deployment deltas for {app['id']}")
             return deployment_deltas

         async def get_users_and_groups(self) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
             """Get all users and groups in the organization from a single API call."""
             endpoint = "users"
             humanitec_headers = self.get_humanitec_headers()
             all_entities: List[Dict[str, Any]] = await self.send_api_request(
                 "GET", endpoint, headers=humanitec_headers
             )
             
             users = []
             groups = []
             for entity in all_entities:
                 if entity.get("type") == "user":
                     users.append(entity)
                 elif entity.get("type") == "group":
                     groups.append(entity)
             
             logger.info(f"Received {len(users)} users and {len(groups)} groups from Humanitec")
             return users, groups

         async def get_users_in_group(self, group_id: str) -> List[Dict[str, Any]]:
             """Get all users in a specific group."""
             endpoint = f"groups/{group_id}/users"
             humanitec_headers = self.get_humanitec_headers()
             users: List[Dict[str, Any]] = await self.send_api_request(
                 "GET", endpoint, headers=humanitec_headers
             )
             logger.info(f"Received {len(users)} users in group {group_id}")
             return users

         async def close(self):
             """Close the HTTP client."""
             if self.http_client:
                 await self.http_client.close()
     ```

   * `cache.py` - Provides an in-memory caching mechanism with thread-safe operations for setting, retrieving, and deleting cache entries asynchronously.

     Add the following code to the `cache.py` file:

     **Cache (Click to expand)**

     cache.py

     ```

     import asyncio
     from typing import Dict, Any


     class InMemoryCache:
         def __init__(self):
             self.cache = {}
             self.lock = asyncio.Lock()

         async def set(self, key, data):
             """
             Sets or updates a cache entry with the given key.

             Parameters:
             - key (str): The key to use for the cache entry.
             - data (dict): The data to be cached.
             """
             async with self.lock:
                 if key in self.cache:
                     self.cache[key].update(data)
                 else:
                     self.cache[key] = data
                 return True

         async def get(self, key) -> Dict[str, Any]:
             """
             Retrieves cached data using the given key.

             Parameters:
             - key (str): The key to retrieve from the cache.

             Returns:
             - dict: The cached data associated with the key, or None if not found.
             """
             async with self.lock:
                 return self.cache.get(key, {})

         async def delete(self, key):
             """
             Deletes cached data associated with the given key.

             Parameters:
             - key (str): The key to delete from the cache.

             Returns:
             - bool: True if deletion was successful, False otherwise (key not found).
             """
             async with self.lock:
                 if key in self.cache:
                     del self.cache[key]
                     return True
                 return False
     ```

   * `circuit_breaker.py` - Implements a circuit breaker pattern to handle transient failures in API calls, preventing cascading failures and improving the reliability of the integration.

     Add the following code to the `circuit_breaker.py` file:

     **Circuit Breaker (Click to expand)**

     circuit\_breaker.py

     ```

     import time
     import asyncio
     from typing import Optional, Callable, Any
     from loguru import logger


     class CircuitBreaker:
         """
         Circuit breaker pattern to prevent cascading failures.
         """
         
         def __init__(
             self,
             failure_threshold: int = 5,
             recovery_timeout: float = 60.0,
             expected_exception: type = Exception
         ):
             self.failure_threshold = failure_threshold
             self.recovery_timeout = recovery_timeout
             self.expected_exception = expected_exception
             
             self.failure_count = 0
             self.last_failure_time = None
             self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
             
         def _can_attempt_reset(self) -> bool:
             """Check if enough time has passed to attempt reset."""
             if self.last_failure_time is None:
                 return True
             
             return time.time() - self.last_failure_time >= self.recovery_timeout
         
         def _record_failure(self):
             """Record a failure and potentially open the circuit."""
             self.failure_count += 1
             self.last_failure_time = time.time()
             
             if self.failure_count >= self.failure_threshold:
                 self.state = "OPEN"
                 logger.warning(f"Circuit breaker opened after {self.failure_count} failures")
         
         def _record_success(self):
             """Record a success and reset the circuit."""
             self.failure_count = 0
             self.last_failure_time = None
             if self.state == "HALF_OPEN":
                 self.state = "CLOSED"
                 logger.info("Circuit breaker closed after successful request")
         
         async def call(self, func: Callable, *args, **kwargs) -> Any:
             """
             Execute a function with circuit breaker protection.
             
             Args:
                 func: The function to execute
                 *args: Arguments for the function
                 **kwargs: Keyword arguments for the function
                 
             Returns:
                 The result of the function call
                 
             Raises:
                 Exception: If the circuit is open or the function fails
             """
             if self.state == "OPEN":
                 if self._can_attempt_reset():
                     self.state = "HALF_OPEN"
                     logger.info("Circuit breaker attempting half-open state")
                 else:
                     raise Exception(f"Circuit breaker is OPEN. Last failure: {self.last_failure_time}")
             
             try:
                 result = await func(*args, **kwargs)
                 self._record_success()
                 return result
                 
             except self.expected_exception as e:
                 self._record_failure()
                 raise e
         
         def get_state(self) -> str:
             """Get the current state of the circuit breaker."""
             return self.state
         
         def get_failure_count(self) -> int:
             """Get the current failure count."""
             return self.failure_count 
     ```

   * `retryable_http_client.py` - Provides a retryable HTTP client with exponential backoff and jitter to handle failed API calls due to disonnected HTTP connections.

     Add the following code to the `retryable_http_client.py` file:

     **Retryable HTTP Client (Click to expand)**

     retryable\_http\_client.py

     ```

     import httpx
     import asyncio
     import time
     from typing import Any, Dict, Optional
     from loguru import logger
     from config import (
         MAX_RETRY_ATTEMPTS, 
         DEFAULT_TIMEOUT_SECONDS, 
         RETRY_DELAY_SECONDS,
         USE_EXPONENTIAL_BACKOFF,
         MAX_RETRY_DELAY_SECONDS,
         MAX_CONNECTIONS,
         MAX_KEEPALIVE_CONNECTIONS,
         KEEPALIVE_EXPIRY
     )
     from .circuit_breaker import CircuitBreaker


     class RetryableHTTPClient:
         """
         A wrapper around httpx.AsyncClient that provides automatic retry functionality
         with client recreation on timeout errors.
         """
         
         def __init__(self, timeout: Optional[httpx.Timeout] = None, **kwargs):
             self.timeout = timeout or httpx.Timeout(DEFAULT_TIMEOUT_SECONDS)
             self.max_retries = MAX_RETRY_ATTEMPTS
             self.retry_delay = RETRY_DELAY_SECONDS
             self.use_exponential_backoff = USE_EXPONENTIAL_BACKOFF
             self.max_retry_delay = MAX_RETRY_DELAY_SECONDS
             
             # Connection health monitoring
             self.client_created_at = time.time()
             self.request_count = 0
             self.last_refresh_time = time.time()
             self.refresh_interval = 300  # Refresh client every 5 minutes
             
             # Circuit breaker for additional protection
             self.circuit_breaker = CircuitBreaker(
                 failure_threshold=10,
                 recovery_timeout=120.0,  # 2 minutes
                 expected_exception=(httpx.TimeoutException, httpx.ConnectTimeout, httpx.ReadTimeout)
             )
             
             # Track active requests to prevent premature closure
             self._active_requests = 0
             self._closed = False
             
             # Create client with connection pooling limits
             self.limits = httpx.Limits(
                 max_connections=MAX_CONNECTIONS,
                 max_keepalive_connections=MAX_KEEPALIVE_CONNECTIONS,
                 keepalive_expiry=KEEPALIVE_EXPIRY
             )
             
             self._client = httpx.AsyncClient(
                 timeout=self.timeout,
                 limits=self.limits,
                 **kwargs
             )

         def _should_refresh_client(self) -> bool:
             """Check if the client should be refreshed based on time or request count."""
             current_time = time.time()
             time_since_refresh = current_time - self.last_refresh_time
             
             # Refresh if:
             # 1. More than refresh_interval seconds have passed, OR
             # 2. We've made more than 1000 requests (to prevent connection pool issues)
             return time_since_refresh > self.refresh_interval or self.request_count > 1000

         def _refresh_client_if_needed(self):
             """Refresh the client if it's been running for too long."""
             if self._should_refresh_client():
                 logger.info(f"Refreshing HTTP client after {self.request_count} requests and "
                            f"{time.time() - self.last_refresh_time:.1f}s of operation")
                 self._reconnect_client()
                 self.request_count = 0
                 self.last_refresh_time = time.time()

         def _reconnect_client(self, timeout: Optional[httpx.Timeout] = None):
             """Reconnect the HTTP client by creating a new one."""
             if self._client and not self._closed:
                 try:
                     # Close the old client
                     self._client.close()
                 except Exception:
                     pass  # Ignore errors when closing
             
             new_timeout = timeout or self.timeout
             self._client = httpx.AsyncClient(timeout=new_timeout, limits=self.limits)
             logger.debug("Reconnected HTTP client with fresh connection pool")

         def _calculate_retry_delay(self, attempt: int) -> float:
             """Calculate delay for retry attempt using exponential backoff."""
             if not self.use_exponential_backoff:
                 return self.retry_delay
             
             # Exponential backoff: delay = base_delay * (2^attempt)
             delay = self.retry_delay * (2 ** attempt)
             # Cap the delay at max_retry_delay
             return min(delay, self.max_retry_delay)

         async def _make_request(self, method: str, url: str, headers: Optional[Dict[str, str]] = None, 
                                json: Optional[Any] = None, **kwargs) -> httpx.Response:
             """Internal method to make the actual HTTP request."""
             if self._closed:
                 raise RuntimeError("Cannot send a request, as the client has been closed.")
             
             self._active_requests += 1
             try:
                 return await self._client.request(method, url, headers=headers, json=json, **kwargs)
             finally:
                 self._active_requests -= 1

         async def request(
             self,
             method: str,
             url: str,
             headers: Optional[Dict[str, str]] = None,
             json: Optional[Any] = None,
             **kwargs
         ) -> httpx.Response:
             """
             Make an HTTP request with automatic retry on timeout errors and circuit breaker protection.
             
             Args:
                 method: HTTP method (GET, POST, etc.)
                 url: Request URL
                 headers: Request headers
                 json: JSON payload
                 **kwargs: Additional arguments to pass to httpx.AsyncClient.request
                 
             Returns:
                 httpx.Response: The HTTP response
                 
             Raises:
                 httpx.TimeoutException: If all retry attempts fail due to timeout
                 httpx.HTTPStatusError: For HTTP error responses
                 Exception: For other errors
             """
             if self._closed:
                 raise RuntimeError("Cannot send a request, as the client has been closed.")
             
             # Check if we should refresh the client before making the request
             self._refresh_client_if_needed()
             
             # Use circuit breaker to protect against cascading failures
             async def _request_with_retry():
                 last_exception = None
                 
                 for attempt in range(self.max_retries + 1):
                     try:
                         self.request_count += 1
                         logger.debug(f"Making {method} request to {url} (attempt {attempt + 1}/{self.max_retries + 1})")
                         response = await self._make_request(method, url, headers=headers, json=json, **kwargs)
                         response.raise_for_status()
                         return response
                         
                     except httpx.ConnectTimeout as e:
                         last_exception = e
                         retry_delay = self._calculate_retry_delay(attempt)
                         
                         logger.warning(
                             f"Connection timeout on attempt {attempt + 1}/{self.max_retries + 1} "
                             f"for {method} {url}: {str(e)}. "
                             f"Reconnecting and retrying in {retry_delay:.1f}s..."
                         )
                         
                         if attempt < self.max_retries:
                             # Reconnect the HTTP client for the next attempt
                             self._reconnect_client()
                             # Add exponential backoff delay before retrying
                             await asyncio.sleep(retry_delay)
                         else:
                             logger.error(f"All {self.max_retries + 1} attempts failed for {method} {url}")
                             raise last_exception
                             
                     except (httpx.TimeoutException, httpx.ReadTimeout) as e:
                         last_exception = e
                         retry_delay = self._calculate_retry_delay(attempt)
                         
                         logger.warning(
                             f"Timeout error on attempt {attempt + 1}/{self.max_retries + 1} "
                             f"for {method} {url}: {str(e)}. "
                             f"Retrying in {retry_delay:.1f}s..."
                         )
                         
                         if attempt < self.max_retries:
                             # Add exponential backoff delay before retrying
                             await asyncio.sleep(retry_delay)
                         else:
                             logger.error(f"All {self.max_retries + 1} attempts failed for {method} {url}")
                             raise last_exception
                             
                     except httpx.HTTPStatusError as e:
                         logger.error(f"HTTP error occurred: {e.response.text}")
                         raise
                     except Exception as e:
                         logger.error(f"An error occurred: {str(e)}")
                         raise
             
             return await self.circuit_breaker.call(_request_with_retry)

         async def get(self, url: str, **kwargs) -> httpx.Response:
             """Make a GET request with retry functionality."""
             return await self.request("GET", url, **kwargs)

         async def post(self, url: str, **kwargs) -> httpx.Response:
             """Make a POST request with retry functionality."""
             return await self.request("POST", url, **kwargs)

         async def put(self, url: str, **kwargs) -> httpx.Response:
             """Make a PUT request with retry functionality."""
             return await self.request("PUT", url, **kwargs)

         async def delete(self, url: str, **kwargs) -> httpx.Response:
             """Make a DELETE request with retry functionality."""
             return await self.request("DELETE", url, **kwargs)

         async def close(self):
             """Close the underlying HTTP client only when explicitly requested."""
             if self._client and not self._closed:
                 # Wait for active requests to complete with timeout
                 timeout = 30  # 30 seconds timeout
                 start_time = time.time()
                 
                 while self._active_requests > 0 and (time.time() - start_time) < timeout:
                     logger.debug(f"Waiting for {self._active_requests} active requests to complete before closing")
                     await asyncio.sleep(0.1)
                 
                 if self._active_requests > 0:
                     logger.warning(f"Force closing client with {self._active_requests} active requests after {timeout}s timeout")
                 
                 try:
                     await self._client.aclose()
                     self._closed = True
                     logger.debug("HTTP client closed successfully")
                 except Exception as e:
                     logger.warning(f"Error closing HTTP client: {e}")

         def __enter__(self):
             return self

         def __exit__(self, exc_type, exc_val, exc_tb):
             # Don't create a task for closing in sync context
             pass

         async def __aenter__(self):
             return self

         async def __aexit__(self, exc_type, exc_val, exc_tb):
             # Only close if explicitly requested
             pass 
     ```

### Create the GitHub workflow[â](#create-the-github-workflow "Direct link to Create the GitHub workflow")

Create the file `.github/workflows/humanitec-exporter.yaml` in the `.github/workflows` folder of your repository.

Cron expression

Adjust the cron expression to fit your schedule. By default, the workflow is set to run at 2:00 AM every Monday ('0 2 \* \* 1').

**GitHub Workflow (Click to expand)**

humanitec-exporter.yaml

```
name: Ingest Humanitec Integration Resources

on:
  schedule:
    - cron: '0 2 * * 1'
  workflow_dispatch:

jobs:
  ingest-humanitec-resources: 
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Ingest Entities to Port
        env:
            PORT_CLIENT_ID: ${{ secrets.PORT_CLIENT_ID }}
            PORT_CLIENT_SECRET: ${{ secrets.PORT_CLIENT_SECRET }}
            API_KEY: ${{ secrets.HUMANITEC_API_KEY }}
            ORG_ID: ${{secrets.HUMANITEC_ORG_ID }}    
        run: |
          python integration/main.py
```

## Conclusion[â](#conclusion "Direct link to Conclusion")

Done! Any change that happens to your application, environment, workloads, resources, resource graphs, pipelines, deployment deltas, deployment sets, secret stores, shared values, value set versions, users, groups in Humanitec will be synced to Port on the schedule interval defined in the GitHub workflow.
