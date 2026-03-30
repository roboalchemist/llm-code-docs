# Source: https://docs.gitguardian.com/self-hosting/installation/databases/postgres-azure.md

# Azure Database: PostgreSQL on Azure

> Configure Azure Database for PostgreSQL as the database backend for GitGuardian self-hosted.

## Introduction

To deploy the GitGuardian app, a PostgreSQL instance is required. This page is
dedicated to helping you set up PostgreSQL on Azure using Azure Database for PostgreSQL (Flexible Server).

## High-Availability

Azure Database for PostgreSQL Flexible Server provides built-in high availability with zone-redundant deployment. This ensures automatic failover and minimal downtime during maintenance or outages. For more details, see [High availability in Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-high-availability).

## Installation

### From the Azure Portal

To create a PostgreSQL instance from the Azure Portal, we recommend following the
[official documentation](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-server-portal).

We recommend you use the 'Production' configuration for high availability and security.

You need to set the following fields:

- Ensure `High availability` is set to `Zone redundant` for production workloads.
- Set the `Authentication method` to `Password authentication`.
- Set the `Admin username` to your liking or keep the default `azureuser`.
- Set the `Password` or auto-generate it. You must save this value as it
  is required to configure the GitGuardian application.

### Using Terraform

To create a PostgreSQL instance using Terraform, you need the following resources:

- [azurerm_postgresql_flexible_server](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_flexible_server)

In addition to the fields required by Terraform, we require the following fields
to be set:

- `administrator_login=<POSTGRES_USERNAME>`: username for the admin user.
- `administrator_password=<POSTGRES_PASSWORD>`: password for the admin user.
- `high_availability.mode="ZoneRedundant"`: enables high availability.
- `version`: set to a supported PostgreSQL version (e.g., `16`).

## Plugins installation (like pgvector)

To install a plugin on Azure Database for PostgreSQL, your admin user can enable supported extensions directly. For more information, see [PostgreSQL extensions in Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-extensions).

This elevated privilege is only needed for plugin installation; the user configured in the GitGuardian application does not require it.
