# Source: https://docs.infrahub.app/emma.md

# Welcome to Emma

Emma is an experimental AI-powered assistant designed to help you interact with Infrahub, OpsMill's next-generation infrastructure management platform. Emma helps you manage infrastructure schemas and data through an intuitive web interface.

![Emma Homepage](/assets/images/home_page-688ffc9365ffba7db2bec7b3ee5c6c4f.png)

Experimental Software

Emma is experimental by design and may not work as expected. She tests out new ideas before her big brother Otto gets involved and implements them in Infrahub.

## What Emma can do[​](#what-emma-can-do "Direct link to What Emma can do")

Emma provides powerful tools for infrastructure management:

### 🏗️ **Schema management**[​](#️-schema-management "Direct link to ️-schema-management")

* **[AI Schema Builder](/emma/features/schema-builder.md)** - Create schemas using natural language descriptions
* **[Schema Library](https://docs.infrahub.app/schema-library)** - Browse and use community-validated schemas
* **[Schema Loader](/emma/features/schema-management.md)** - Load schemas into your Infrahub instance
* **[Schema Visualizer](/emma/features/schema-management.md)** - Visual representation of schema relationships

### 📊 **Data operations**[​](#-data-operations "Direct link to -data-operations")

* **[Data Import](/emma/features/data-import-export.md)** - Import CSV data into Infrahub with intelligent mapping
* **[Data Export](/emma/features/data-import-export.md)** - Export Infrahub data to CSV for analysis and backup

### 🔬 **Experimental features**[​](#-experimental-features "Direct link to -experimental-features")

* **Query Builder** - Interactive GraphQL query interface (feature flag required)
* **Template Builder** - Create and manage infrastructure templates (feature flag required)

## Quick start[​](#quick-start "Direct link to Quick start")

Ready to get started? Choose your preferred installation method:

### 🚀 **Fastest setup**[​](#-fastest-setup "Direct link to -fastest-setup")

Use the one-command quickstart to get Emma and Infrahub running together:

```
curl https://infrahub.opsmill.io/latest-emma | docker compose -f - up -d
```

Then open [Emma](http://localhost:8501) and [Infrahub](http://localhost:8000) in your browser.

### 📚 **Full installation guide**[​](#-full-installation-guide "Direct link to -full-installation-guide")

For detailed installation instructions, including local development setup and production deployments, see the **[Installation Guide](/emma/getting-started/installation.md)**.

## Documentation structure[​](#documentation-structure "Direct link to Documentation structure")

### 🚀 Getting started[​](#-getting-started "Direct link to 🚀 Getting started")

Perfect for new users:

* **[Installation](/emma/getting-started/installation.md)** - Set up Emma in various environments
* **[Configuration](/emma/getting-started/configuration.md)** - Configure Emma and connect to Infrahub
* **[First Steps](/emma/getting-started/first-steps.md)** - Your first experience with Emma

### ⚙️ Features[​](#️-features "Direct link to ⚙️ Features")

Deep dives into Emma's capabilities:

* **[AI Schema Builder](/emma/features/schema-builder.md)** - AI-powered schema creation
* **[Data Import & Export](/emma/features/data-import-export.md)** - Comprehensive data management
* **[Schema Management](/emma/features/schema-management.md)** - Complete schema lifecycle
* **[Schema Library](https://docs.infrahub.app/schema-library)** - Community schema collection

### 📖 Guides[​](#-guides "Direct link to 📖 Guides")

Step-by-step tutorials:

* **[Building Your First Schema](/emma/guides/building-your-first-schema.md)** - Complete walkthrough

### 📚 Reference[​](#-reference "Direct link to 📚 Reference")

Complete reference materials:

* **[Configuration Reference](/emma/reference/configuration.md)** - All configuration options
* **[Feature Flags](/emma/reference/feature-flags.md)** - Experimental feature management
* **[Troubleshooting](/emma/reference/troubleshooting.md)** - Solutions to common issues

## Common use cases[​](#common-use-cases "Direct link to Common use cases")

### Infrastructure modeling[​](#infrastructure-modeling "Direct link to Infrastructure modeling")

Start with Emma's Schema Library to model your infrastructure:

1. Browse [pre-built schemas](https://docs.infrahub.app/schema-library) for common components
2. Use the [AI Schema Builder](/emma/features/schema-builder.md) for custom requirements
3. [Load schemas](/emma/features/schema-management.md) into your Infrahub instance
4. [Visualize relationships](/emma/features/schema-management.md) to understand your model

### Data migration[​](#data-migration "Direct link to Data migration")

Migrate from existing systems using Emma's data tools:

1. Export data from your current systems to CSV
2. Use Emma's [Data Importer](/emma/features/data-import-export.md) to map and load data
3. Validate and clean data during the import process
4. Export data for backup and integration with other tools

### Schema development[​](#schema-development "Direct link to Schema development")

Develop and iterate on infrastructure schemas:

1. [Plan your schema](/emma/guides/building-your-first-schema.md) requirements
2. Use AI assistance to generate initial schema definitions
3. Test and refine schemas with sample data
4. Share schemas with your team through the library

## Getting help[​](#getting-help "Direct link to Getting help")

### 📖 Documentation[​](#-documentation "Direct link to 📖 Documentation")

This documentation covers everything you need to know about Emma. Use the navigation menu to explore topics in detail.

### 🐛 Issues and support[​](#-issues-and-support "Direct link to 🐛 Issues and support")

* **Bug Reports**: [GitHub Issues](https://github.com/opsmill/emma/issues)
* **General Questions**: [OpsMill Discord Community](https://discord.gg/opsmill)

### 🔗 Related resources[​](#-related-resources "Direct link to 🔗 Related resources")

* **[Infrahub Documentation](https://docs.infrahub.app)** - Complete Infrahub documentation
* **[Schema Library Repository](https://docs.infrahub.app/schema-library)** - Community schema collection
* **[OpsMill Website](https://opsmill.com)** - Learn more about OpsMill

## Next steps[​](#next-steps "Direct link to Next steps")

1. **New to Emma?** Start with the [Installation Guide](/emma/getting-started/installation.md)
2. **Ready to build?** Try [Building Your First Schema](/emma/guides/building-your-first-schema.md)
3. **Need schemas?** Explore the [Schema Library](https://docs.infrahub.app/schema-library)
4. **Have data to import?** Check out [Data Import & Export](/emma/features/data-import-export.md)

Emma is designed to make infrastructure management more accessible and efficient. Whether you're modeling a basic network or a complex multi-cloud environment, Emma provides the tools you need to succeed.

Happy infrastructure modeling!
