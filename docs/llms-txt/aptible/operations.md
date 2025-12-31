# Source: https://www.aptible.com/docs/core-concepts/architecture/operations.md

# Operations

> Learn more about operations work on Aptible - with minimal downtime and rollbacks

# Overview

An operation is performed and recorded for all changes made to resources, environments, and stacks. As operations are performed, operation logs are outputted and stored within Aptible. Operations are designed with reliability in mind - with minimal downtime and automatic rollbacks.

A collective record of operations is referred to as [activity](/core-concepts/observability/activity).

# Type of Operations

* `backup`: Creates a [database backup](/core-concepts/managed-databases/managing-databases/database-backups)
* `configure`: Sets the [configuration](/core-concepts/apps/deploying-apps/configuration) for an app
* `copy`: Creates a cross-region copy [database backup](/core-concepts/managed-databases/managing-databases/database-backups#cross-region-copy-backups)
* `deploy`: [Deploys a Docker image](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) for an app
* `deprovision`: Stops all running [containers](/core-concepts/architecture/containers/overview) and deletes the resources
* `execute`: Creates an [ephemeral SSH session](/core-concepts/apps/connecting-to-apps/ssh-sessions) for an app
* `logs`: Streams [logs](/core-concepts/observability/logs/overview) to CLI
* `modify`: Modifies a [database](/core-concepts/managed-databases/overview) volume type (gp3, gp2, standard) or provisioned IOPS (if gp3)
* `provision`: Provisions a new [database](/core-concepts/managed-databases/overview), [log drain](/core-concepts/observability/logs/log-drains/overview), or [metric drain](/core-concepts/observability/metrics/metrics-drains/overview)
* `purge`: Deletes a [database backup](/core-concepts/managed-databases/managing-databases/database-backups)
* `rebuild`: Rebuilds the Docker [image](/core-concepts/apps/deploying-apps/image/overview) for an app and deploys the app with the newly built image
* `reload`: Restarts the [database](/core-concepts/managed-databases/overview) in place (does not alter size)
* `replicate`: Creates a [replica](/core-concepts/managed-databases/managing-databases/replication-clustering) for databases that support replication.
* `renew`: Renews a certificate for an [app endpoint using Managed HTTPS](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview).
* `restart`: Restarts an [app](/core-concepts/apps/overview) or [database](/core-concepts/managed-databases/overview)
* `restore`: Restores a [database backup](/core-concepts/managed-databases/managing-databases/database-backups) into a new database
* `scale`: Scales a [service](/core-concepts/apps/deploying-apps/services) for an app
* `scan`: Generates a [security scan](/core-concepts/security-compliance/security-scans) for an app

# Operation Logs

For all operations performed, Aptible collects operation logs. These logs are retained only for active resources.

# Activity Dashboard

<img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5-app-ui.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=b056c313e87dd846dde0bc8aaf1fb3a1" alt="" data-og-width="2560" width="2560" data-og-height="1280" height="1280" data-path="images/5-app-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5-app-ui.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=f83ddf57cabd3c4339c3bbb9ad6f0491 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5-app-ui.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=a972084e881fb1448a7f08fdc2a30f06 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5-app-ui.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=f84f089638f4edf484ca5f08e10eeab4 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5-app-ui.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=a503f7c3153528517ab3ca8eb361d0cf 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5-app-ui.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=08399c46ca0b4e171f73cfbe4394b864 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5-app-ui.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=6d7ea7d7d47908e00b3f10d52a2c41cd 2500w" />

The Activity dashboard provides a real-time view of operations for active resources in the last seven days. Through the Activity page, you can:

* View operations for resources you have access to
* Search operations by resource name, operation type, and user
* View operation logs for debugging purposes

<Tip> Troubleshooting with our team? Link the Aptible Support team to the logs for the operation you are having trouble with. </Tip>

# Activity Reports

Activity Reports provide historical data of all operations in a given environment, including operations executed on resources that were later deleted. These reports are generated on a weekly basis for each environment, and they can be accessed for the duration of the environment's existence. All Activity Reports for an Environment are accessible for the lifetime of the Environment.

# Minimal downtime operations

To further mitigate the impact of failures, Aptible Operations are designed to be interruptible at any stage whenever possible.

In particular, when deploying a web application, Aptible performs [Zero-Downtime Deployment](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview#zero-downtime-deployment). This ensures that if the Operation is interrupted at any time and for any reason, it still won't take your application down.

When downtime is inevitable (such as when resizing a Database volume or redeploying a Database to a bigger instance), Aptible optimizes for minimal downtime.

For example, when redeploying a Database to another instance, Aptible must perform the following steps:

* Shut down the old Database [Container](/core-concepts/architecture/containers/overview).
* Unmount and then detach the Database volume from the instance the Database was originally scheduled on.
* Attach then remount the Database volume on the instance the Database is being re-scheduled on.
* Start the new Database Container.

When performing this Operation, Aptible will minimize downtime by ensuring that all preconditions are in place to start the new Database Container on the new instance before shutting down the old Database Container. In particular, Aptible will ensure the new instance is available and has pre-pulled the Docker image for your Database.

# Operation Rollbacks

Aptible was designed with reliability in mind. To this extent, Aptible provides automatic rollbacks for failed operations. Users can also manually rollback an operation should they need to.

### Automatic Rollbacks

All Aptible operations are designed to support automatic rollbacks in the event of a failure (with the exception of a handful of trivial operations with no side effects (such as launching [Ephemeral SSH Sessions](/core-concepts/apps/connecting-to-apps/ssh-sessions)).

When a failure occurs, and an automatic rollback is initiated, a message will be displayed within the operation logs. The logs will indicate whether the rollback succeeded (i.e., everything was restored back to the way it was before the Operation) or failed (some changes could not be undone).

<Warning> Some side-effects of deployments cannot be rolled back by Aptible. In particular, database migrations performed in [`before_release`](/core-concepts/apps/deploying-apps/releases/aptible-yml#before-release) commands cannot be rolled back (unless you design your migrations to roll back on failure, of course!). We strongly recommend designing your database migrations so that they are backwards compatible across at least one release. This is a very good idea in general (not just on Aptible), and a best practice for zero-downtime deployments (see [Concurrent Releases](/core-concepts/apps/deploying-apps/releases/overview#concurrent-releases) for more information). </Warning>

### Manual Rollbacks

A rollback can be manually initiated within the Aptible CLI by using the [`aptible operation:cancel`](/reference/aptible-cli/cli-commands/cli-operation-cancel) command.

# FAQ

<AccordionGroup>
  <Accordion title="How do I access Operation Logs?">
    Operation Logs can be accessed in the following ways:

    * Within the Aptible Dashboard:
      * Within the resource summary by:
        * Navigating to the respective resource
        * Selecting the Activity tab
          <img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Downloading-operation-logs-2.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=247ccd8bc573aa6cd19ed6430b5d6276" alt="" data-og-width="2800" width="2800" data-og-height="2000" height="2000" data-path="images/Downloading-operation-logs-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Downloading-operation-logs-2.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=1bf646d3bc4db6497a7babb29bf1e6cf 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Downloading-operation-logs-2.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=65d3b0840c5ac982e8a84d39894edd01 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Downloading-operation-logs-2.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=070ed8c98262ea073582fea35c75d8ca 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Downloading-operation-logs-2.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=acfb03abea58d42dfb0ad73ef3b4318b 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Downloading-operation-logs-2.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=1f428db3f5512b4fdf933077f363e39d 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Downloading-operation-logs-2.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=e4e31ea164a9f48a100609c342dbb245 2500w" />
      * Within the Activity dashboard by:
        * Navigating to the Activity page
        * Selecting the Logs button for the respective operation
          * Note: This page only shows operations performed in the last 7 days.
    * Within the Aptible CLI by using the [`aptible operation:logs`](/reference/aptible-cli/cli-commands/cli-operation-logs) command
      * Note: This command only shows operations performed in the last 90 days.
  </Accordion>

  <Accordion title="How do I access Activity Reports?">
    Activity Reports can be downloaded in CSV format within the Aptible Dashboard by:

    * Selecting the respective Environment
    * Selecting the **Activity Reports** tab

        <img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Activity_Reports.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=340af39557cf152c9ba2985e7ef71328" alt="Activity reports" data-og-width="2800" width="2800" data-og-height="2000" height="2000" data-path="images/App_UI_Activity_Reports.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Activity_Reports.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=1b62c99730e3214bfbc958b93f3296de 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Activity_Reports.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=a3cfaf078e221412e1b1a2f3fdcbd3e6 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Activity_Reports.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=2e603c313de868ccc9a6f652d6fa118e 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Activity_Reports.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=1503d88811f970cbfbb76b20f3d6c4d6 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Activity_Reports.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=00b99629750c148e5343b0af9e125ab1 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/App_UI_Activity_Reports.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=17d99ad7038fdb9442bf441592efc813 2500w" />
  </Accordion>

  <Accordion title="Why do Operation Failures happen?">
    Reliability is a top priority at Aptible in general and for Aptible in particular. That said, occasional failures during Operations are inevitable and may be caused by the following:

    * Failing third-party services: Aptible strives to minimize dependencies on the critical path to deploying an [App](/core-concepts/apps/overview) or restarting a [Database](/core-concepts/managed-databases/managing-databases/overview), but Aptible nonetheless depends on a number of third-party services. Notably, Aptible depends on AWS EC2, AWS S3, AWS ELB, and the Docker Hub (with a failover or Quay.io and vice-versa). These can occasionally fail and when they do, they may cause Aptible Operations to fail.

    * Crashing instances: Aptible is built on a fleet of Linux instances running Docker. Like any other software, Linux and Docker have bugs and may occasionally crash. Here again, when they do, Aptible operations may fail
  </Accordion>
</AccordionGroup>
