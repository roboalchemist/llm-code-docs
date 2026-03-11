# Source: https://tyk.io/docs/tyk-cloud/environments-deployments/managing-environments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Environments in Tyk Cloud

> Learn how to manage Environments in Tyk Cloud

## Introduction

Environments are used to group your [Control Plane](/tyk-cloud#glossary) and [Cloud Data Planes](/tyk-cloud#glossary) into logical groups. For example you may want to create environments that reflect different departments of your organization.

<Note>
  The number of Environments you can create is determined by your [plan](/tyk-cloud/account-billing#select-a-payment-plan)
</Note>

## Prerequisites

The following [user roles](/tyk-cloud/teams-users#assign-user-roles) can perform Environment Admin tasks:

* Org Admin
* Team Admin

You should also have created a team to assign to any new environment.

## Adding a New Environment

1. From the Environments screen, click **Add Environment**
2. Select the team you want to assign to the Environment
3. Give your new Environment a name
4. Click **Create**

## Editing an Existing Environment

An Org Admin can perform the following:

* Rename an Environment
* Delete an Environment

1. Click the environment Name from your list

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/tyk-cloud-edit-env.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=6b3d156a45076a913bc91116aac032dd" alt="Edit Environment Name" width="1077" height="298" data-path="img/admin/tyk-cloud-edit-env.png" />

2. Click Edit

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/tyk-cloud-env-screen.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=d3605b1c0725f68e0f739ae5e97ef5a2" alt="Env Edit Screen" width="1076" height="412" data-path="img/admin/tyk-cloud-env-screen.png" />

3. You can now rename the environment, or delete it from your organization

<img src="https://mintcdn.com/tyk/KUyxLx5tNlKCB02w/img/admin/tyk-cloud-rename-delete.png?fit=max&auto=format&n=KUyxLx5tNlKCB02w&q=85&s=f71d52b7bde0e9779727ee1d0e80d22d" alt="Delete or Rename Env" width="1077" height="531" data-path="img/admin/tyk-cloud-rename-delete.png" />

<Warning>
  Deleting an environment will also delete all the Control Planes and Cloud Data Planes associated with it
</Warning>


Built with [Mintlify](https://mintlify.com).