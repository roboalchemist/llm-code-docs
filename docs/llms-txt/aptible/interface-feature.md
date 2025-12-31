# Source: https://www.aptible.com/docs/reference/interface-feature.md

# Interface Feature Availability Matrix

There are three supported methods for managing resources on Aptible:

* [The Aptible Dashboard](/reference/dashboard)
* The [Aptible CLI](/reference/aptible-cli/cli-commands/overview) client
* The [Aptible Terraform Provider](https://registry.terraform.io/providers/aptible/aptible)

Currently, not every action is supported by every interface. This matrix describes which actions are supported by which interfaces.

## Key

* ✅ - Supported

* 🔶 - Partial Support

* ❌ - Not Supported

* 🚧 - In Progress

* N/A - Not Applicable

## Matrix

|                                   |              Web             | CLI | Terraform       |
| :-------------------------------: | :--------------------------: | :-: | --------------- |
|    **User Account Management**    |               ✅              |  ❌  | ❌               |
|    **Organization Management**    |               ✅              |  ❌  | ❌               |
|   **Dedicated Stack Management**  |                              |     |                 |
|               Create              | 🔶 (can request first stack) |  ❌  | ❌               |
|                List               |               ✅              |  ❌  | ✅ (data source) |
|            Deprovision            |               ❌              |  ❌  | ❌               |
|     **Environment Management**    |                              |     |                 |
|               Create              |               ✅              |  ❌  | ✅               |
|                List               |               ✅              |  ✅  | ✅ (data source) |
|               Delete              |               ✅              |  ❌  | ✅               |
|               Rename              |               ✅              |  ✅  | ✅               |
|    Set Backup Retention Policy    |               ✅              |  ✅  | ✅               |
|         Get CA Certificate        |               ❌              |  ✅  | ❌               |
|         **App Management**        |                              |     |                 |
|               Create              |               ✅              |  ✅  | ✅               |
|                List               |               ✅              |  ✅  | N/A             |
|            Deprovision            |               ✅              |  ✅  | ✅               |
|               Rename              |               ✅              |  ✅  | ✅               |
|               Deploy              |               ✅              |  ✅  | ✅               |
|        Update Configuration       |               ✅              |  ✅  | ✅               |
|         Get Configuration         |               ✅              |  ✅  | ✅               |
|            SSH/Execute            |              N/A             |  ✅  | N/A             |
|              Rebuild              |               ❌              |  ✅  | N/A             |
|              Restart              |               ✅              |  ✅  | N/A             |
|               Scale               |               ✅              |  ✅  | ✅               |
|            Autoscaling            |               ✅              |  ✅  | ✅               |
|     Change Container Profiles     |               ✅              |  ✅  | ✅               |
|      **Database Management**      |                              |     |                 |
|               Create              |     🔶 (limited versions)    |  ✅  | ✅               |
|                List               |               ✅              |  ✅  | N/A             |
|            Deprovision            |               ✅              |  ✅  | ✅               |
|               Rename              |               ✅              |  ✅  | ✅               |
|               Modify              |               ❌              |  ✅  | ❌               |
|               Reload              |               ❌              |  ✅  | N/A             |
|           Restart/Scale           |               ✅              |  ✅  | ✅               |
|     Change Container Profiles     |               ✅              |  ❌  | ✅               |
|          Get Credentials          |               ✅              |  ✅  | ✅               |
|          Create Replicas          |               ❌              |  ✅  | ✅               |
|               Tunnel              |              N/A             |  ✅  | ❌               |
|   **Database Backup Management**  |                              |     |                 |
|               Create              |               ✅              |  ✅  | N/A             |
|                List               |               ✅              |  ✅  | N/A             |
|               Delete              |               ✅              |  ✅  | N/A             |
|              Restore              |               ✅              |  ✅  | N/A             |
|          Disable backups          |               ✅              |  ❌  | ✅               |
|      **Endpoint Management**      |                              |     |                 |
|               Create              |               ✅              |  ✅  | ✅               |
|                List               |               ✅              |  ✅  | N/A             |
|            Deprovision            |               ✅              |  ✅  | ✅               |
|               Modify              |               ✅              |  ✅  | ✅               |
|            IP Filtering           |               ✅              |  ✅  | ✅               |
|        Custom Certificates        |               ✅              |  ✅  | ❌               |
| **Custom Certificate Management** |                              |     |                 |
|               Create              |               ✅              |  ❌  | ❌               |
|                List               |               ✅              |  ❌  | N/A             |
|               Delete              |               ✅              |  ❌  | ❌               |
|      **Log Drain Management**     |                              |     |                 |
|               Create              |               ✅              |  ✅  | ✅               |
|                List               |               ✅              |  ✅  | N/A             |
|            Deprovision            |               ✅              |  ✅  | ✅               |
|    **Metric Drain Management**    |                              |     |                 |
|               Create              |               ✅              |  ✅  | ✅               |
|                List               |               ✅              |  ✅  | N/A             |
|            Deprovision            |               ✅              |  ✅  | ✅               |
|      **Operation Management**     |                              |     |                 |
|                List               |               ✅              |  ❌  | N/A             |
|               Cancel              |               ❌              |  ✅  | N/A             |
|                Logs               |               ✅              |  ✅  | N/A             |
|               Follow              |              N/A             |  ✅  | N/A             |
