# Source: https://docs.jit.io/docs/connect-jit-with-your-gitlab-account.md

# Connect Jit with your GitLab account

## Background

As part of Jit’s security approach, our tool operates entirely within the SCM environment, ensuring that no code is ever transmitted to our cloud servers. This design significantly minimizes risks and potential vulnerabilities, enhancing the security of your code. Our approach is both novel and unique within the ASPM landscape. However, it may introduce a few additional steps during the onboarding process. These additional steps are reflected in the following onboarding instructions and are essential to maintaining our high-security standards.

## Getting Started with GitLab Integration

Welcome to the new GitLab onboarding flow! This guide will walk you through setting up your GitLab integration with Jit in a secure and efficient manner. Our approach ensures minimal manual work while maintaining visibility throughout the process.

This onboarding process features a simplified setup with streamlined steps, prioritizes security by limiting token permissions, and ensures centralized management without touching your CI/CD or pulling your code to the cloud.

## Prerequisites

Before starting, ensure the following:

* **Paid GitLab Plan:** Integration is supported only for paid plans.
* **Permissions:** Although the application doesn't require permission from the group owner, you'll need them to complete certain configuration tasks, so please ensure you have group owner permissions

## First step of onboarding - Choose the integration method

### Confirm prerequisites

First, confirm whether your GitLab account has a paid plan and that you have permission from the group owner. If you have both, you can proceed.

### Choose the Integration Method

From this point, there are two integration options available:

**Fastest:** Selecting the Fastest method grants Jit group owner-level access, enabling the quickest and most seamless integration with minimal manual steps. For detailed instructions for this method, click [here](https://docs.jit.io/v4.7.1/docs/fastest).

**Fast:** Gives Jit maintainer-level access to your GitLab projects. This requires some manual setup but allows you to limit the permissions granted. For detailed instructions for this method, click [here](https://docs.jit.io/v4.7.1/docs/fast).

## Supporting Multiple GitLab Groups

Jit supports connecting multiple GitLab groups to a single tenant using a Personal Access Token (PAT).\
This allows organizations that manage repositories across several GitLab groups to maintain unified security visibility.

### How it works

* GitLab integration is based on a Personal Access Token (PAT).
* A single PAT can be used to access multiple groups, as long as the token owner has permissions for all of them.
* All accessible repositories are discovered and managed under the same Jit tenant.

### Requirements

* **Token scope:** The PAT must include the `api` scope.
* **Access level:** The user generating the token must have access to all GitLab groups that should be connected.

### Automation and permissions

* **Owner-level PAT (recommended):**\
  Allows full automation, including webhook creation.
* **Maintainer-level PAT:**\
  Repository access is supported, but webhook creation may be limited due to GitLab permission constraints.

### Managing Resources & Organizations

Once multiple organizations are connected, you can manage them centrally from the **Resource Management** modal.

### View the resources

1. Open Settings → **Manage Resources**
2. Use the dropdown menu to select a specific Organization

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8e4c8368e79de2851f7c6cfac274003d9b9f6448eac2948c221b49c052192030-image.png",
        null,
        null
      ],
      "align": "center",
      "sizing": "600px"
    }
  ]
}
[/block]