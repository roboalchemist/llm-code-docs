# Configuration settings

System admins for both self-hosted and Cloud Mattermost deployments can
manage Mattermost configuration using the System Console by selecting
the **Product** [\|product-list\|](##SUBST##|product-list|) menu and
selecting **System Console**.

:::: note
::: title
Note
:::

- In self-hosted Mattermost deployments, configuration settings are
  maintained in the `config.json` configuration file, located in the
  `mattermost/config` directory, or
  `stored in the database </administration-guide/configure/configuration-in-your-database>`{.interpreted-text
  role="doc"}. System admins managing self-hosted deployments can also
  modify the `config.json` file directly using a text editor.
- Mattermost requires write permissions to the `config.json` file;
  otherwise, configuration changes made within the System Console will
  have no effect.
::::

::: {.toctree maxdepth="1" hidden="" titlesonly=""}
Self-hosted workspace edition and license settings
\</administration-guide/configure/self-hosted-account-settings\> Cloud
workspace subscription, billing, and account settings
\</administration-guide/configure/cloud-billing-account-settings\>
Reporting configuration settings
\</administration-guide/configure/reporting-configuration-settings\>
User management configuration settings
\</administration-guide/configure/user-management-configuration-settings\>
System attributes \</administration-guide/configure/system-attributes\>
Environment configuration settings
\</administration-guide/configure/environment-configuration-settings\>
Site configuration settings
\</administration-guide/configure/site-configuration-settings\>
Authentication configuration settings
\</administration-guide/configure/authentication-configuration-settings\>
Plugins configuration settings
\</administration-guide/configure/plugins-configuration-settings\>
Integrations configuration settings
\</administration-guide/configure/integrations-configuration-settings\>
Compliance configuration settings
\</administration-guide/configure/compliance-configuration-settings\>
Experimental configuration settings
\</administration-guide/configure/experimental-configuration-settings\>
Deprecated configuration settings
\</administration-guide/configure/deprecated-configuration-settings\>
Bleve search \</administration-guide/configure/bleve-search\>
:::

Mattermost configuration settings are organized into the following
categories within the System Console:

- `Self-hosted workspace edition and license settings </administration-guide/configure/self-hosted-account-settings>`{.interpreted-text
  role="doc"}
- `Cloud workspace subscription, billing, and account settings</administration-guide/configure/cloud-billing-account-settings>`{.interpreted-text
  role="doc"}
- `Reporting configuration settings </administration-guide/configure/reporting-configuration-settings>`{.interpreted-text
  role="doc"}
- `User management configuration settings </administration-guide/configure/user-management-configuration-settings>`{.interpreted-text
  role="doc"}
- `System attributes </administration-guide/configure/system-attributes>`{.interpreted-text
  role="doc"}
- `Environment configuration settings </administration-guide/configure/environment-configuration-settings>`{.interpreted-text
  role="doc"}
- `Site configuration settings </administration-guide/configure/site-configuration-settings>`{.interpreted-text
  role="doc"}
- `Authentication configuration settings </administration-guide/configure/authentication-configuration-settings>`{.interpreted-text
  role="doc"}
- `Plugins configuration settings </administration-guide/configure/plugins-configuration-settings>`{.interpreted-text
  role="doc"}
- `Integrations configuration settings </administration-guide/configure/integrations-configuration-settings>`{.interpreted-text
  role="doc"}
- `Compliance configuration settings </administration-guide/configure/compliance-configuration-settings>`{.interpreted-text
  role="doc"}
- `Experimental configuration settings </administration-guide/configure/experimental-configuration-settings>`{.interpreted-text
  role="doc"}
- `Deprecated configuration settings </administration-guide/configure/deprecated-configuration-settings>`{.interpreted-text
  role="doc"}
- `Bleve search </administration-guide/configure/bleve-search>`{.interpreted-text
  role="doc"}

## Configuration in database

Self-hosted system configuration can be stored in the database. This
changes the Mattermost binary from reading the default `config.json`
file to reading the configuration settings stored within a configuration
table in the database. See the
`Mattermost database configuration </administration-guide/configure/configuration-in-your-database>`{.interpreted-text
role="doc"} documentation for migration details.

## Environment variables

You can use
`environment variables </administration-guide/configure/environment-variables>`{.interpreted-text
role="doc"} to manage Mattermost configuration for self-hosted
deployments. Environment variables override settings in `config.json`.
If a change to a setting in `config.json` requires a restart to take
effect, then changes to the corresponding environment variable also
require a server restart.

## Configuration reload

In self-hosted deployments, the "config watcher", the mechanism that
automatically reloads the `config.json` file, has been deprecated in
favor of the
`mmctl config reload <administration-guide/manage/mmctl-command-line-tool:mmctl config reload>`{.interpreted-text
role="ref"} command that you must run to apply configuration changes
you\'ve made. This improves configuration performance and robustness.

## Deprecated configuration settings

See the
`deprecated configuration settings documentation </administration-guide/configure/deprecated-configuration-settings>`{.interpreted-text
role="doc"} for details on all deprecated Mattermost configuration
settings that are no longer supported.
