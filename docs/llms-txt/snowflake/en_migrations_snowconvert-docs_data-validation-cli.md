# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/data-validation-cli/index.md

# Snowflake Data Validation - Documentation Index

Welcome to the Snowflake Data Validation CLI documentation. The Snowflake Data Validation CLI (`snowflake-data-validation` or `sdv`) is a comprehensive command-line tool for validating data migrations between source databases (SQL Server, Teradata, Amazon Redshift, Snowflake) and Snowflake. It provides multi-level validation strategies to ensure data consistency and quality, including Snowflake-to-Snowflake validation for cross-account or cross-region migrations.

## Documentation roadmap

### 1. Command References by Database Dialect

**Choose your source database for dialect-specific commands:**

* **[SQL Server Commands Reference](sqlserver_commands.md)** - Complete SQL Server command documentation
* **[Teradata Commands Reference](teradata_commands.md)** - Complete Teradata command documentation
* **[Amazon Redshift Commands Reference](redshift_commands.md)** - Complete Redshift command documentation
* **[Snowflake Commands Reference](snowflake_commands.md)** - Complete Snowflake-to-Snowflake command documentation

Each command reference includes:

* Detailed syntax and options for all commands
* Connection configuration specifics
* Complete examples
* Troubleshooting tips
* Best practices for that platform

---

### 2. CLI Usage Guide - Comprehensive Reference

**[Start here for complete documentation.](CLI_USAGE_GUIDE.md)**

A comprehensive, customer-facing guide covering all aspects of the CLI tool.

**Contents:**

* Complete installation instructions
* Detailed command reference for all source databases
* In-depth configuration file reference with all options explained
* Complete configuration examples
* Advanced usage patterns
* Troubleshooting guide

**Best for:**

* First-time users getting started
* Users needing detailed explanations of configuration options
* Troubleshooting issues
* Understanding all available features

---

### 3. Quick Reference Guide - Fast Lookup

**[Use this for quick lookups and reminders.](CLI_QUICK_REFERENCE.md)**

A concise reference guide with essential information in an easy-to-scan format.

**Contents:**

* Command syntax at a glance
* Quick configuration templates
* Table configuration patterns
* Common CLI options reference
* Performance tips
* Common issues and quick fixes

**Best for:**

* Experienced users who need quick reminders
* Looking up specific syntax
* Quick configuration templates
* Performance optimization tips

---

### 4. Configuration Examples - Ready-to-Use configurations

**[Copy and adapt these real-world examples.](CONFIGURATION_EXAMPLES.md)**

A collection of ready-to-use configuration file examples for various scenarios.

**Contents:**

* 16+ complete configuration examples
* SQL Server configurations
* Teradata configurations
* Redshift configurations
* Snowflake-to-Snowflake configurations
* Scenario-based examples (dev, staging, production, PII-compliant, etc.)
* Tips for adapting examples
* Security best practices

**Best for:**

* Jump-starting your configuration
* Finding a configuration similar to your use case
* Learning by example
* Best practices for different scenarios

---

## Quick Navigation by Task

### The following sections provide quick references to the documentation for specific tasks

#### Get Started

1. Follow installation instructions in [CLI Usage Guide](CLI_USAGE_GUIDE.md)
2. Copy an example from [Configuration Examples](CONFIGURATION_EXAMPLES.md)
3. Run your first validation using the [Quick Reference](CLI_QUICK_REFERENCE.md)

#### Understand All Options

→ [CLI Usage Guide - Configuration File Reference](CLI_USAGE_GUIDE.md)

#### Find a Command

→ [Quick Reference - Common Commands](CLI_QUICK_REFERENCE.md)

#### Create a Configuration File

→ [Configuration Examples](CONFIGURATION_EXAMPLES.md) (pick the closest match to your scenario)

#### Troubleshoot an Issue

→ [CLI Usage Guide - Troubleshooting](CLI_USAGE_GUIDE.md)

#### Optimize Performance

→ [Quick Reference - Performance Tips](CLI_QUICK_REFERENCE.md)

#### Validate Large Tables

→ [CLI Usage Guide - Working with Large Tables](CLI_USAGE_GUIDE.md)

#### Understand Connection Options

→ [CLI Usage Guide - Connection Configuration](CLI_USAGE_GUIDE.md)

#### Set Up Validation Levels

→ [CLI Usage Guide - Validation Configuration](CLI_USAGE_GUIDE.md)

#### Configure Table-Specific Settings

→ [CLI Usage Guide - Table Configuration](CLI_USAGE_GUIDE.md)

#### Configure View Validation

→ [CLI Usage Guide - View Configuration](CLI_USAGE_GUIDE.md)

#### View Validation Examples

→ [Configuration Examples - View Validation](CONFIGURATION_EXAMPLES.md)

---

## Documentation by Source Database

The following sections provide quick references to the documentation for specific source databases.

### SQL Server Users

**Essential Reading:**

1. **[SQL Server Commands Reference](sqlserver_commands.md)** - Complete command reference
2. [Quick Reference - SQL Server Connection](CLI_QUICK_REFERENCE.md)
3. [CLI Usage Guide - SQL Server Commands](CLI_USAGE_GUIDE.md)
4. [Configuration Examples - SQL Server Examples](CONFIGURATION_EXAMPLES.md)

**Key Examples:**

* [Example 1: Minimal SQL Server Configuration](CONFIGURATION_EXAMPLES.md)
* [Example 2: Production SQL Server with SSL/TLS](CONFIGURATION_EXAMPLES.md)
* [Example 3: SQL Server Incremental Validation](CONFIGURATION_EXAMPLES.md)
* [Example 4: SQL Server with Column Mappings](CONFIGURATION_EXAMPLES.md)

### Teradata Users

**Essential Reading:**

1. **[Teradata Commands Reference](teradata_commands.md)** - Complete command reference
2. [Quick Reference - Teradata Connection](CLI_QUICK_REFERENCE.md)
3. [CLI Usage Guide - Teradata Commands](CLI_USAGE_GUIDE.md)
4. [Configuration Examples - Teradata Examples](CONFIGURATION_EXAMPLES.md)

**Key Examples:**

* [Example 5: Basic Teradata Configuration](CONFIGURATION_EXAMPLES.md)
* [Example 6: Teradata Large-Scale Migration](CONFIGURATION_EXAMPLES.md)
* [Example 7: Teradata Multi-Schema Validation](CONFIGURATION_EXAMPLES.md)

### Amazon Redshift Users

**Essential Reading:**

1. **[Amazon Redshift Commands Reference](redshift_commands.md)** - Complete command reference
2. [Quick Reference - Redshift Connection](CLI_QUICK_REFERENCE.md)
3. [CLI Usage Guide - Redshift Commands](CLI_USAGE_GUIDE.md)
4. [Configuration Examples - Redshift Examples](CONFIGURATION_EXAMPLES.md)

**Key Examples:**

* [Example 8: Basic Redshift Configuration](CONFIGURATION_EXAMPLES.md)
* [Example 9: Redshift Data Lake Migration](CONFIGURATION_EXAMPLES.md)
* [Example 10: Redshift with Complex Filtering](CONFIGURATION_EXAMPLES.md)

---

## Documentation by Use Case

### Development Environment

* [Configuration Example 11: Development Environment - Fast Validation](CONFIGURATION_EXAMPLES.md)
* [Quick Reference - Common Commands](CLI_QUICK_REFERENCE.md)

### Staging Environment

* [Configuration Example 12: Staging Environment - Comprehensive Testing](CONFIGURATION_EXAMPLES.md)
* [CLI Usage Guide - Advanced Usage](CLI_USAGE_GUIDE.md)

### Production Environment

* [Configuration Example 13: Production - Maximum Performance](CONFIGURATION_EXAMPLES.md)
* [CLI Usage Guide - Working with Large Tables](CLI_USAGE_GUIDE.md)
* [Quick Reference - Performance Tips](CLI_QUICK_REFERENCE.md)

### PII/Compliance Requirements

* [Configuration Example 14: PII-Compliant Validation](CONFIGURATION_EXAMPLES.md)
* [CLI Usage Guide - Table Configuration](CLI_USAGE_GUIDE.md)

### Migration Cutover

* [Configuration Example 15: Migration Cutover Validation](CONFIGURATION_EXAMPLES.md)
* [CLI Usage Guide - Advanced Usage](CLI_USAGE_GUIDE.md)

### Continuous/Incremental Validation

* [Configuration Example 16: Continuous Validation - Daily Incremental](CONFIGURATION_EXAMPLES.md)
* [CLI Usage Guide - Advanced Usage](CLI_USAGE_GUIDE.md)

### View Validation

Validate database views alongside or separately from tables. Views are materialized into temporary tables for comparison.

* [CLI Usage Guide - View Configuration](CLI_USAGE_GUIDE.md)
* [Configuration Examples - View Validation](CONFIGURATION_EXAMPLES.md)
* [Quick Reference - View Configuration](CLI_QUICK_REFERENCE.md)

**Key Features:**

* Validate views with the same options as tables (column selection, filtering, column mappings)
* Support for target database/schema/name overrides
* Views are automatically materialized for accurate comparison

### Snowflake-to-Snowflake Validation

Validate data between different Snowflake accounts, regions, or databases.

**Essential Reading:**

1. **[Snowflake Commands Reference](snowflake_commands.md)** - Complete command reference
2. [CLI Usage Guide - Snowflake Commands](CLI_USAGE_GUIDE.md)
3. [Configuration Examples - Snowflake Examples](CONFIGURATION_EXAMPLES.md)

**Key Features:**

* Cross-account validation with separate source and target credentials
* IPC mode for direct connection parameter specification
* Source-only validation with Parquet file export for offline comparison
* Same validation capabilities as other source platforms (schema, metrics, row-level)

---

## Configuration Reference

The following sections provide quick references to the documentation for specific configuration scenarios.

### Quick Config Template

→ [Quick Reference - Configuration Template](CLI_QUICK_REFERENCE.md)

### Complete Field Reference

→ [CLI Usage Guide - Configuration File Reference](CLI_USAGE_GUIDE.md)

### Real-World Examples

→ [Configuration Examples](CONFIGURATION_EXAMPLES.md)

---

## Common Workflows

The following sections provide quick references to the documentation for common workflows.

### First-Time Setup Workflow

1. Install the CLI

   * → [CLI Usage Guide - Installation](CLI_USAGE_GUIDE.md)
2. Generate configuration template

   * → [Quick Reference - Get Templates](CLI_QUICK_REFERENCE.md)
3. Copy and modify an example

   * → [Configuration Examples](CONFIGURATION_EXAMPLES.md)
4. Run validation

   * → [Quick Reference - Run Validation](CLI_QUICK_REFERENCE.md)
5. Review results

   * → [CLI Usage Guide - Validation Reports](CLI_USAGE_GUIDE.md)

### Troubleshooting Workflow

1. Check error message

   * → [CLI Usage Guide - Troubleshooting](CLI_USAGE_GUIDE.md)
2. Review configuration

   * → [Quick Reference - Configuration Template](CLI_QUICK_REFERENCE.md)
3. Enable debug logging

   * → [CLI Usage Guide - Logging Configuration](CLI_USAGE_GUIDE.md)
4. Review logs

   * → [CLI Usage Guide - Troubleshooting](CLI_USAGE_GUIDE.md)
5. Adjust configuration

   * → [Configuration Examples](CONFIGURATION_EXAMPLES.md)

### Performance Optimization Workflow

1. Review performance tips

   * → [Quick Reference - Performance Tips](CLI_QUICK_REFERENCE.md)
2. Enable chunking

   * → [CLI Usage Guide - Working with Large Tables](CLI_USAGE_GUIDE.md)
3. Adjust thread count

   * → [CLI Usage Guide - Global Configuration](CLI_USAGE_GUIDE.md)
4. Add filters

   * → [CLI Usage Guide - Table Configuration](CLI_USAGE_GUIDE.md)
5. Test with examples

   * → [Configuration Examples - Production](CONFIGURATION_EXAMPLES.md)

---

## Feature Matrix

| Feature | Command Refs | Quick Reference | Usage Guide | Examples |
| --- | --- | --- | --- | --- |
| Installation |  | ✓ | ✓✓✓ |  |
| Command Syntax | ✓✓✓ | ✓✓✓ | ✓✓ |  |
| Configuration | ✓ | ✓✓ | ✓✓✓ | ✓✓✓ |
| Connection Setup | ✓✓✓ | ✓ | ✓✓✓ | ✓✓✓ |
| Table Config |  | ✓✓ | ✓✓✓ | ✓✓✓ |
| View Config |  | ✓✓ | ✓✓✓ | ✓✓✓ |
| Validation Levels |  | ✓ | ✓✓✓ | ✓✓ |
| Performance |  | ✓✓✓ | ✓✓ | ✓✓ |
| Troubleshooting | ✓✓✓ | ✓✓ | ✓✓✓ |  |
| Examples | ✓✓ | ✓ | ✓✓ | ✓✓✓ |

Legend: ✓ = Covered, ✓✓ = Good Coverage, ✓✓✓ = Comprehensive Coverage

---

## Learning Path

### Beginner Path

1. **Day 1: Understanding the Tool**

   * Read the [Main Project Repository](https://github.com/snowflake-eng/migrations-data-validation)
   * Skim [CLI Usage Guide - Overview](CLI_USAGE_GUIDE.md)
   * Review [Quick Reference](CLI_QUICK_REFERENCE.md)
2. **Day 2: First Validation**

   * Follow [CLI Usage Guide - Quick Start](CLI_USAGE_GUIDE.md)
   * Copy [Configuration Example 1 or 5 or 8](CONFIGURATION_EXAMPLES.md)
   * Run your first validation
3. **Day 3: Configuration Mastery**

   * Read [CLI Usage Guide - Configuration Reference](CLI_USAGE_GUIDE.md)
   * Review multiple [Configuration Examples](CONFIGURATION_EXAMPLES.md)
   * Customize configuration for your needs

### Intermediate Path

1. **Optimize Performance**

   * [CLI Usage Guide - Working with Large Tables](CLI_USAGE_GUIDE.md)
   * [Quick Reference - Performance Tips](CLI_QUICK_REFERENCE.md)
2. **Advanced Features**

   * [CLI Usage Guide - Advanced Usage](CLI_USAGE_GUIDE.md)
   * [Configuration Examples - Scenario-Based](CONFIGURATION_EXAMPLES.md)
3. **CI/CD Integration**

   * [CLI Usage Guide - CI/CD Integration](CLI_USAGE_GUIDE.md)
   * [Configuration Examples - Continuous Validation](CONFIGURATION_EXAMPLES.md)

### Expert Path

1. **Custom Templates**

   * [CLI Usage Guide - Using Custom Query Templates](CLI_USAGE_GUIDE.md)
2. **Async Workflows**

   * [CLI Usage Guide - Asynchronous Validation Workflow](CLI_USAGE_GUIDE.md)
3. **Production Deployment**

   * [Configuration Example 13 & 15](CONFIGURATION_EXAMPLES.md)

---

## Search Tips

### Finding Information Quickly

**For Commands:**

* Look in [Quick Reference](CLI_QUICK_REFERENCE.md) first
* For details, see [CLI Usage Guide - CLI Commands](CLI_USAGE_GUIDE.md)

**For Configuration:**

* Start with [Quick Reference - Configuration Template](CLI_QUICK_REFERENCE.md)
* For full details, see [CLI Usage Guide - Configuration Reference](CLI_USAGE_GUIDE.md)
* For examples, see [Configuration Examples](CONFIGURATION_EXAMPLES.md)

**For Errors:**

* Check [CLI Usage Guide - Troubleshooting](CLI_USAGE_GUIDE.md)
* Review [Quick Reference - Common Issues](CLI_QUICK_REFERENCE.md)

---

## Additional Support

If you cannot find what you need in these documents:

Email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
