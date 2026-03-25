# Source: https://docs.pentaho.com/pdia-data-integration/pentaho-data-integration-plugins/salesforce-bulk-operations-plugin.md

# Salesforce Bulk Operations Plugin

## Overview

Salesforce Bulk Operation (SFBO) Plugin enables users to perform bulk operations on Salesforce objects. It supports INSERT, UPDATE, UPSERT, and DELETE actions using Salesforce Bulk API 2.0. This plugin is designed for efficient and scalable data integration with Salesforce, offering significantly faster performance compared to traditional SOAP-based steps.

## Installation

### Pre-Installation

* Ensure that you have access to the [Support Portal](https://support.pentaho.com/hc/en-us/categories/200568085-Downloads). Reach out to your Pentaho Support representative if you do not have access.
* Ensure that any Pentaho Data Integration (PDI) tools (pan, kitchen, Carte, Spoon) and Pentaho Server are fully shut down before beginning the installation.

### Installation Instructions

{% stepper %}
{% step %}

### Download the Plugin

* Visit the Download section in the Pentaho Support portal
  * [Download for PDI 10.2](https://support.pentaho.com/hc/en-us/articles/28937520396173-Pentaho-10-2-GA-Release)&#x20;
  * [Download for PDI 11.0](https://support.pentaho.com/hc/en-us/articles/42133683854093-Pentaho-11-0-GA-Release)
* Download the zip file: `plugins/Salesforce Bulk Operation/salesforce-bulk-plugin-<version>-<build>-dist.zip.`&#x20;
  {% endstep %}

{% step %}

### Extract the files&#x20;

Unzip the dowloaded file
{% endstep %}

{% step %}

### Run the Installer

* Execute the appropriate script based on your operating system:
  * `install.sh` for Linux/macOS
  * `install.bat` for Windows
* Accept the End User License Agreement (EULA) when prompted
* Choose Installation Path
  * For PDI/Spoon: `<PENTAHO_HOME>/data-integration/plugins`
  * For Pentaho Server: `<PENTAHO_HOME>/pentaho-server/pentaho-solutions/system/kettle/plugins`
  * **Note**: `<PENTAHO_HOME>` is the absolute path of the folder where you have installed Pentaho
    {% endstep %}
    {% endstepper %}

### Post-installation Steps

* Restart PDI and/or Pentaho Server after installation.
* Sample transformations are included in the `plugin release` folder for reference.

## Further Details

See [Salesforce Bulk Operations](https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/salesforce-bulk-operation).
