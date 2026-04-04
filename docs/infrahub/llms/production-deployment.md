# Source: https://docs.infrahub.app/guides/production-deployment.md

# How to deploy Infrahub in production

This guide walks you through deploying Infrahub in a production environment with enhanced security, reliability, and maintainability. By following these steps, you'll set up a production-ready Infrahub instance that follows industry best practices.

warning

This page is currently under development. Please use it as a reference checklist when preparing your Infrahub environment for production deployment.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before beginning your production deployment, ensure you have:

* Selected your deployment technology (Docker or Kubernetes)
* Verified your system meets the [hardware requirements](/topics/hardware-requirements.md)
* Administrative access to your deployment environment
* Decided between Community or Enterprise edition based on your support and feature needs
* Access to your organization's identity provider (for SSO configuration)
* A backup strategy and storage location

## Step 1: Create a hardened configuration file[​](#step-1-create-a-hardened-configuration-file "Direct link to Step 1: Create a hardened configuration file")

Production environments require secure configuration settings that differ from development defaults. Create a configuration file that overwrites default values to enhance security.

.env

```
# Environment settings
INFRAHUB_ALLOW_ANONYMOUS_ACCESS=false
INFRAHUB_PRODUCTION=true
INFRAHUB_LOG_LEVEL=INFO

# Security keys & tokens (generate strong unique values)
INFRAHUB_SECURITY_SECRET_KEY=<strong-random-string-at-least-32-chars>
INFRAHUB_INITIAL_ADMIN_PASSWORD=<strong-admin-password>
INFRAHUB_INITIAL_ADMIN_TOKEN=<generate-uuid>  # Generate with: uuidgen
INFRAHUB_INITIAL_AGENT_TOKEN=<generate-uuid>  # Generate with: uuidgen

# Database & message broker security
INFRAHUB_BROKER_PASSWORD=<strong-broker-password>
INFRAHUB_DB_PASSWORD=<strong-database-password>

# TLS & Certificates
INFRAHUB_DB_TLS_ENABLED=true
INFRAHUB_DB_TLS_CA_FILE=/opt/ssl/ca.pem
INFRAHUB_BROKER_TLS_ENABLED=true
INFRAHUB_CACHE_TLS_ENABLED=true
```

warning

Never use default passwords or tokens in production. Generate strong unique values for each environment. You can generate UUIDs using the `uuidgen` command or an online UUID generator.

[Complete configuration reference../reference/configuration](/reference/configuration.md)

## Step 2: Install Infrahub[​](#step-2-install-infrahub "Direct link to Step 2: Install Infrahub")

Install Infrahub using your chosen deployment technology, applying your hardened configuration.

info

For high availability deployments on Kubernetes, use the HA manifest which includes proper replication and resource requests/limits.

[Detailed installation instructions./installation](/guides/installation.md)

success

Navigate to `https://your-server-address` in your browser. You should see the Infrahub login page.

## Step 3: Configure SSO (recommended)[​](#step-3-configure-sso-recommended "Direct link to Step 3: Configure SSO (recommended)")

Connect Infrahub to your organization's identity provider to enhance security and simplify user management.

[Detailed SSO configuration guide./sso](/guides/sso.md)

## Step 4: Set up database backups[​](#step-4-set-up-database-backups "Direct link to Step 4: Set up database backups")

Implement regular database backups to prevent data loss in case of hardware failure or other issues.

[Complete backup and restore guide./database-backup](/guides/database-backup.md)

success

Test your backup and restore process periodically to ensure it works as expected.

## Operations and maintenance[​](#operations-and-maintenance "Direct link to Operations and maintenance")

### Upgrading Infrahub[​](#upgrading-infrahub "Direct link to Upgrading Infrahub")

To upgrade to a new version of Infrahub:

1. Review the release notes for breaking changes
2. Create a full backup of your database
3. Update the container images

danger

Always create a backup before upgrading to ensure you can restore if needed.

[Detailed upgrade procedures./upgrade](/guides/upgrade.md)

## Support options[​](#support-options "Direct link to Support options")

### Community support[​](#community-support "Direct link to Community support")

* GitHub Issues: [github.com/opsmill/infrahub](https://github.com/opsmill/infrahub)
* Discord Community: [discord.gg/infrahub](https://discord.gg/infrahub)
* Documentation: [docs.infrahub.app](https://docs.infrahub.app)

### Enterprise supportEnterprise Edition[​](#enterprise-support "Direct link to enterprise-support")

* 24/7 support with SLA guarantees
* Dedicated support engineer
* Professional services for deployment
* Training and certification programs

Contact <support@opsmill.com> for enterprise support.

## Related resources[​](#related-resources "Direct link to Related resources")

* [Architecture Overview](/topics/architecture.md)
* [Configuration Reference](/reference/configuration.md)
* [API Server Reference](/reference/api-server.md)
