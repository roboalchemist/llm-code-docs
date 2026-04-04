# Source: https://docs.upsun.com/administration/web/configure-project.md

# Configure a project

Each project has settings that apply to everything within that project, including all its environments.
You can only see and update settings for projects where you are a [Project Admin](https://docs.upsun.com../users.md).
To access the settings, click Settings **Settings** from the main project page.

The settings are divided into several sections.

## General

The **General** section shows you the project's region and allows you to update the project name and [timezone](https://docs.upsun.com../../projects/change-project-timezone.md).

![configure project](https://docs.upsun.com/images/console/settings-general.png "1.0")

## Access

The **Access** section allows you to [manage user access to the project](https://docs.upsun.com../users.md).

<!-- The **Access** section allows you to [manage user access](https://docs.upsun.com../users.md),
and [teams access](https://docs.upsun.com../teams.md) to a project. -->

![Project configure icon](https://docs.upsun.com/images/console/settings-access-users.png "0.7")

## Certificates

The **Certificates** section shows a list of your project's TLS certificates.
To see details about a certificate or delete one, click **Edit **.
See how to [add custom certificates](https://docs.upsun.com../../domains/steps/tls.md).

![A list of certificates in a project](https://docs.upsun.com/images/management-console/settings-certificates.png "0.7")

## Domains

The **Domains** section allows you to manage the domains where your project is accessible.
See how to [set up your domain](https://docs.upsun.com../../domains/steps.md).

![project domain](https://docs.upsun.com/images/management-console/settings-domains.png "0.7")

## Deploy Key

The **Deploy Key** section shows you the public SSH key you can add to your private repositories.
Adding it lets Upsun access the repositories during the build process.
This is useful if you want to reuse some code components across multiple projects and manage those components as dependencies of your project.

![Project deploy key](https://docs.upsun.com/images/management-console/settings-deploy-key.png "0.7")

## Integrations

The **Integrations** section allows you to manage all of your [integrations](https://docs.upsun.com../../integrations.md).

![Integrations](https://docs.upsun.com/images/management-console/settings-integrations.png "0.7")

## Variables

The **Variables** section allows you to manage all project-wide [variables](https://docs.upsun.com../../development/variables.md).

![Project variables](https://docs.upsun.com/images/management-console/settings-variables-project.png "0.7")

