# Source: https://tyk.io/docs/tyk-cloud/environments-deployments/managing-control-planes.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Control Planes in Tyk Cloud

> Learn how to manage Control Planes in Tyk Cloud

## Introduction

Control Planes are situated in your Organization's home region and provide links to an instance of the [Tyk Dashboard](/api-management/dashboard-configuration) and the [Developer Portal](/portal/overview/intro). The Dashboard is where you perform all your API tasks. The developer portal allows your 3rd party developers access to your APIs. Cloud Data Planes are then connected to your Control Planes.

## Prerequisites

All [user roles](/tyk-cloud/teams-users#assign-user-roles) can edit, deploy, undeploy, restart, redeploy all deployments within a team. Only the Organization Admin and the Team Admin can create or delete deployments.

## Adding a new Control Plane

Watch our video on setting up a Control Plane and a Cloud Data Plane.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JqXXEDplrr8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

<Note>
  The number of Control Planes you can add is dependent on your [plan](/tyk-cloud/account-billing#select-a-payment-plan)
</Note>

1. From the Deployments screen click **Add Deployment** (you can also add a Deployment from within an Environment overview)
2. Enter a name for the new Control Plane
3. Select Control Plane from the Type drop-down list
4. Select the Bundle Channel and Version
5. (Optional) Enter a [custom domain](/tyk-cloud/using-custom-domains) if required
6. (Optional) Enable [plugins](/tyk-cloud/using-plugins) if required

## Edit Control Planes

You can edit the following Control Plane settings:

* Change the Control Plane name
* Add a [custom domain](/tyk-cloud/using-custom-domains)
* Change the Bundle Channel and Bundle Version
* Enable [plugins](/tyk-cloud/using-plugins)

  <Note>
    The use of custom domains is dependent on your [plan](/tyk-cloud/account-billing#select-a-payment-plan)
  </Note>

To edit an existing Control Plane:

1. From the Deployments screen, click the **Control Plane Name** from the list
2. Select **Edit** from the Deployed drop-down list

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/cp-edit.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=db4feb26d498df9c1fa5fd5d5451d9ca" alt="Edit drop-down" width="414" height="190" data-path="img/admin/cp-edit.png" />

## Upgrade Cloud Control Planes

There are two ways to upgrade a Control Plane.

### Manual Upgrade

To upgrade an existing Control Plane:

1. Go to the **Control Plane settings** using the *Edit Control Planes* instructions and scroll down to the **Version** section.
2. Select a **Bundle Channel**.

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/cp-edge-upgrade-channel.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=a1cf87e2429a7df755b1b08c0781db98" alt="Bundle channel drop-down" width="1111" height="274" data-path="img/admin/cp-edge-upgrade-channel.png" />

1. Next, select a **Bundle Version**.

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/cp-edge-upgrade-version.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=0b32b37f115e505880b01fda4059bc43" alt="Bundle version drop-down" width="1110" height="476" data-path="img/admin/cp-edge-upgrade-version.png" />

1. To apply your changes, click the **"Save and Re-Deploy"** button located at the top right. After a few seconds, you will be redirected to the overview page of the Control Plane and a **"Deploying"** indicator button will appear.

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/cp-edge-upgrade-deploying.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=662c52fc937659070076923c3376c335" alt="Deploying notification" width="362" height="51" data-path="img/admin/cp-edge-upgrade-deploying.png" />

1. A **"Deployed"** button indicates a successful upgrade.

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/cp-edge-upgrade-deployed.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=f2c6b0713dbcadc298b208447082766a" alt="Deployed notification" width="351" height="53" data-path="img/admin/cp-edge-upgrade-deployed.png" />

### Auto Upgrade

The Auto Upgrade feature enables users to automatically upgrade their deployments to the latest version based on their selected bundle channel (E.g., Latest, LTS) without requiring manual intervention. This feature helps users stay on the latest features and security enhancements by automating the upgrade process according to a scheduled maintenance window.

#### Availability

Auto Upgrade is available for:

* Control Plane deployments
* When enabled on a Control Plane, it will automatically upgrade the corresponding data planes related to this control plane

#### How to Enable Auto Upgrade

You can enable Auto Upgrade when creating a new Control Plane or editing an existing Control Plane.

#### New Control Plane Deployments

1. Navigate to the "Add Deployment" page

2. Fill in the required deployment details

3. In the "Version" section, select your preferred Bundle Channel (Latest or LTS)

4. Select the desired Bundle Version

5. Toggle on the "Auto-upgrade" option

6. Schedule the maintenance window by selecting:

   * **Day**: Choose a day of the week (Monday-Sunday)
   * **Time**: Select an hour (0-23, in UTC timezone)

   <img src="https://mintcdn.com/tyk/WyMyc-aTqiGjdlz9/img/cloud/tyk-cloud-auto-upgrade.png?fit=max&auto=format&n=WyMyc-aTqiGjdlz9&q=85&s=230c514a859a4ff8059c2c2612d2466d" alt="Tyk Cloud Control Plane Auto Upgrade" width="3023" height="1727" data-path="img/cloud/tyk-cloud-auto-upgrade.png" />

7. Complete the deployment creation process

#### Existing Control Plane Deployments

1. Navigate to the deployment dashboard
2. Click "Edit" in the top-right corner
3. In the "Version" section, toggle on "Auto-upgrade"
4. Schedule the maintenance window by selecting the day and time
5. Click "Save and re-deploy"

#### Limitations and Considerations

* **Control Plane Only**: Auto Upgrade can only be enabled on Control Plane deployments
* **Plugin Compatibility**: Auto Upgrade cannot be enabled when plugins are enabled
* **Production Caution**: Not recommended for production environments without prior testing in lower environments
* **UTC Timezone**: All scheduled times are in UTC
* **Bundle Channel**: Upgrades will always follow the selected bundle channel (Latest or LTS)
* **Email Notifications**: Organization and team admins will receive email notifications when auto-upgrades occur

Built with [Mintlify](https://mintlify.com).
