# Source: https://www.aptible.com/docs/how-to-guides/app-guides/deploy-preview-app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to deploy a preview app to Aptible using Github Actions

## Overview

This guide offers step-by-step instructions for implementing and customizing GitHub workflows to deploy preview apps on the Aptible platform. The workflows described in this documentation are included in this [example repository](https://github.com/aptible/deploy-demo-preview-example/tree/main/.github/workflows), are ready for production, and can be adapted to suit your specific deployment requirements and integration needs.

### Preview Deployment (preview\.yml)

The preview\.yml workflow automatically deploys a preview app for every pull request, enabling reviewers to test the changes introduced in the PR in a separate app in a selected Aptible environment.

**What this workflow does:**

1. Triggers automatically when pull requests are created or updated with new commits
2. Creates a PostgreSQL database and a Redis database for the preview app
3. Configures a new Aptible app configured with the necessary environment variables to connect to the databases from the previous step
4. Builds and pushes a Docker image tagged with the PR number
5. Deploys the application to Aptible using the image built in the previous step
6. Creates an HTTPS endpoint for accessing the preview app

### Preview Cleanup (deprovision\_preview\.yml)

The `deprovision_preview.yml` workflow handles the cleanup of preview resources when a pull request is closed.

**What this workflow does:**

1. Triggers when a pull request is closed (merged or rejected).
2. Deprovisions the Aptible app and endpoint associated with the PR.
3. Deprovisions the PostgreSQL and Redis databases created for the preview.

### Prerequisites

To deploy to Aptible via Git, you must have a public SSH key associated with your account. We recommend creating a robot user to manage your deployment:

1. Create a "Robots" [custom role](/core-concepts/security-compliance/access-permissions) in your Aptible [organization](/core-concepts/security-compliance/access-permissions), and grant it "Full Visibility" and "Deployment" [permissions](/core-concepts/security-compliance/access-permissions) for the [environment](/core-concepts/architecture/environments) where you will be deploying.
2. Invite a new robot user with a valid email address (for example, `deploy@yourdomain.com`) to the `Robots` role.
3. Sign out of your Aptible account, accept the invitation from the robot user's email address, and set a password for the robot's Aptible account.
4. Generate a new SSH key pair to be used by the robot user, and don't set a password: `ssh-keygen -t ed25519 -C "your_email@example.com"`
5. Register the [SSH Public Key](/core-concepts/security-compliance/authentication/ssh-keys) with Aptible for the robot user.

### Configuring the Environment

Add the following [secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets#using-encrypted-secrets-in-a-workflow) in Github:

* APTIBLE\_ROBOT\_PASSWORD: Password for your Aptible robot account
* DOCKERHUB\_USERNAME: Your Docker Hub username
* DOCKERHUB\_TOKEN: Access token for Docker Hub
* DOCKERHUB\_PASSWORD: Your Docker Hub password

Add the following [variable](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables) in Github

* APTIBLE\_ROBOT\_USERNAME: Email address of your Aptible robot account

### Update the workflows and add them to your repository

1. Update the environment variables:
   1. Replace `preview-apps` with your Aptible environment name.
   2. Replace `aptible/deploy-demo-app` with your Docker image name.
   3. Adjust the app name pattern if needed.
2. Modify the database type, version, and name pattern as needed for your application.
3. Update the tagging strategy if required in the `Build and Push Docker images` step.
4. You can customize the workflow further by using different [<u>event types to trigger</u>](https://docs.github.com/en/actions/reference/events-that-trigger-workflows) the workflows. The [<u>push</u>](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#push) and [<u>pull\_request</u>](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#pull_request) event documentation, in particular, includes practical examples for everyday use cases.
