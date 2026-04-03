# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfigmanager.md.txt

# ProjectConfigManager class

Manages (gets and updates) the current project config.

**Signature:**  

    export declare class ProjectConfigManager 

## Methods

|                                                                                         Method                                                                                         | Modifiers |                Description                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------|
| [getProjectConfig()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfigmanager.md#projectconfigmanagergetprojectconfig)                           |           | Get the project configuration.             |
| [updateProjectConfig(projectConfigOptions)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfigmanager.md#projectconfigmanagerupdateprojectconfig) |           | Updates an existing project configuration. |

## ProjectConfigManager.getProjectConfig()

Get the project configuration.

**Signature:**  

    getProjectConfig(): Promise<ProjectConfig>;

**Returns:**

Promise\<[ProjectConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfig.md#projectconfig_class)\>

A promise fulfilled with the project configuration.

## ProjectConfigManager.updateProjectConfig()

Updates an existing project configuration.

**Signature:**  

    updateProjectConfig(projectConfigOptions: UpdateProjectConfigRequest): Promise<ProjectConfig>;

### Parameters

|      Parameter       |                                                                                    Type                                                                                    |               Description                |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| projectConfigOptions | [UpdateProjectConfigRequest](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.updateprojectconfigrequest.md#updateprojectconfigrequest_interface) | The properties to update on the project. |

**Returns:**

Promise\<[ProjectConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfig.md#projectconfig_class)\>

A promise fulfilled with the updated project config.