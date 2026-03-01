# Source: https://docs.curator.interworks.com/site_administration/backend_administrators/overview.md

# Source: https://docs.curator.interworks.com/setup/authentication/overview.md

# Source: https://docs.curator.interworks.com/creating_integrations/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Overview of creating and managing integrations with external platforms in Curator

## Overview

Integrations connect Curator to your business intelligence platforms, allowing
you to embed dashboards, synchronize users, and centralize analytics access.

### What are Integrations?

Integrations (also called "Connections") allow Curator to communicate with external BI platforms. Once configured,
these connections enable you to:

* **Embed visualizations**: Add dashboards and reports from your BI platforms directly to Curator
  by selecting dropdown options
* **Synchronize users**: Keep user access and permissions in sync between Curator and your BI platforms
* **Monitor health**: Automatically detect connection issues and receive email alerts when problems occur
* **Automate tasks**: Schedule data refreshes, run scripts, and execute platform-specific commands

### How Connections Work

Each connection stores the server details and authentication credentials needed to communicate with the external
platform. Curator securely encrypts sensitive information and continuously monitors connection health to ensure
reliable access to your analytics. Follow the platform-specific setup guides to create and configure the
connection to your BI tool.

### Supported Platforms

Curator supports integrations with the following platforms:

* [Tableau Cloud](/creating_integrations/tableau_connection/tableau_cloud_setup)
* [Tableau Server](/creating_integrations/tableau_connection/creating_a_connection)
* [Power BI](/creating_integrations/power_bi_connection/azure_app_setup)
* [ThoughtSpot](/creating_integrations/thoughtspot_connection/integrating_thoughtspot_with_curator)
* [Sigma Computing](/creating_integrations/sigma_connection/creating_a_sigma_connection)
