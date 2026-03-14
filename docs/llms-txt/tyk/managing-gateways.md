# Source: https://tyk.io/docs/tyk-cloud/environments-deployments/managing-gateways.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Data Planes in Tyk Cloud

> Learn how to manage Data Planes in Tyk Cloud

## Introduction

Cloud Data Planes do all the heavy lifting of actually managing your requests: traffic proxying, access control, data transformation, logging and more.

## Prerequisites

All [user roles](/tyk-cloud/teams-users#assign-user-roles) can edit, deploy, undeploy, restart, redeploy all deployments within a team. Only the Organization Admin and the Team Admin can create or delete deployments.

## Adding a new Cloud Data Plane

Watch our video on setting up a Control Plane and a Cloud Data Plane.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JqXXEDplrr8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

<Note>
  The number of Cloud Data Planes you can add is dependent on your [plan](/tyk-cloud/account-billing#select-a-payment-plan)
</Note>

1. From the Deployments screen click **Add Deployment**
2. Enter a name for the new Gateway
3. Select Cloud Data Plane from the Type drop-down list
4. Select the Bundle Channel and Version
5. (Optional) Enter a [custom domain](/tyk-cloud/using-custom-domains) if required
6. (Optional) Enable [plugins](/tyk-cloud/using-plugins) if required

## Edit Cloud Data Planes

You can edit the following Control Plane settings:

* Change the Gateway name
* Add a [custom domain](/tyk-cloud/using-custom-domains)
* Change the Bundle Channel and Bundle Version
* Enable [plugins](/tyk-cloud/using-plugins)

  <Note>
    The use of custom domains is dependent on your [plan](/tyk-cloud/account-billing#select-a-payment-plan)
  </Note>

To edit an existing Cloud Data Plane:

1. On the Deployments screen, expand the Control Plane and click on the Cloud Data Plane to access the Cloud Data Plane overview screen.
2. Select **Edit** from the Deployed drop-down list

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/cp-edit.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=db4feb26d498df9c1fa5fd5d5451d9ca" alt="Cloud Data Plane drop-down" width="414" height="190" data-path="img/admin/cp-edit.png" />

## Upgrade Cloud Data Planes

There are two ways to upgrade a Control Plane.

### Manual Upgrade

To upgrade an existing Cloud Data Plane:

1. Go to the **Cloud Data Plane settings** using the *Edit Cloud Data Planes* instructions and scroll down to the **Version** section.
2. Select a **Bundle Channel**.

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/cp-edge-upgrade-channel.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=a1cf87e2429a7df755b1b08c0781db98" alt="Bundle channel drop-down" width="1111" height="274" data-path="img/admin/cp-edge-upgrade-channel.png" />

3. Next, select a **Bundle Version**.

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/cp-edge-upgrade-version.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=0b32b37f115e505880b01fda4059bc43" alt="Bundle version drop-down" width="1110" height="476" data-path="img/admin/cp-edge-upgrade-version.png" />

4. To apply your changes, click the **"Save and Re-Deploy"** button located at the top right. After a few seconds, you will be redirected to the overview page of the Control Plane and a **"Deploying"** indicator button will appear.

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/cp-edge-upgrade-deploying.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=662c52fc937659070076923c3376c335" alt="Deploying notification" width="362" height="51" data-path="img/admin/cp-edge-upgrade-deploying.png" />

5. A **"Deployed"** button indicates a successful upgrade.

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/cp-edge-upgrade-deployed.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=f2c6b0713dbcadc298b208447082766a" alt="Deployed notification" width="351" height="53" data-path="img/admin/cp-edge-upgrade-deployed.png" />

### Auto Upgrade

The Auto Upgrade feature is only available for Control Plane deployments. When enabled on a Control Plane, it will automatically upgrade the corresponding data planes related to this control plane. For more information, see the [Tyk Cloud Control Plane Auto Upgrade Documentation](/tyk-cloud/environments-deployments/managing-control-planes).


Built with [Mintlify](https://mintlify.com).