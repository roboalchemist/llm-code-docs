# Source: https://docs.jfrog.com/artifactory/docs/distribution-task-maintenance.md

# Distribution Task Maintenance

Use REST APIs to perform the following distribution task maintenance procedures:

* [Generate Maintenance Execution Token](/reference/generatemaintenanceexecutiontoken) – Generates a time-limited encrypted token required to execute a maintenance action.
* [Execute Maintenance Action](/reference/executemaintenanceaction) – Executes a maintenance action using a previously generated token. Two action types are supported:
  * Unlock stuck tasks: Unlocks all stuck distribution tasks.
  * Stop all tasks: Stops all running distribution tasks.
* [Get Stuck Distributions](/reference/getstuckdistributions): Returns a list of all stuck distributions that need to be unlocked.
* [Distribute by Last Days](/reference/distributebylastdays): Redistributes all Release Bundle versions within a defined time period to a specified Edge node.

<Callout icon="✅" theme="okay">
  **Tip**

  JFrog Distribution 2.32.0 and later contains an auto-recovery mechanism that detects and frees stuck distribution tasks. To activate it, open the [Distribution application config YAML file](/installation/docs/distribution-application-config-yaml-file), and in the `internal.monitoring` section, change the value of the `stuck-tasks-auto-recovery-enabled` property to `true`.
</Callout>