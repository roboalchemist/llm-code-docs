# Source: https://docs.pentaho.com/pdia-data-integration/pentaho-data-integration-plugins/kafka-plugin.md

# Kafka Plugin

## Overview

Pentaho Kafka Plugin is designed to enable seamless integration with Apache Kafka for streaming and batch data operations. It supports real-time data ingestion and publishing to Kafka topics, making it ideal for scalable, event-driven architectures.

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
* Download the zip files:&#x20;
  * `Plugins/Kafka/streaming-kafka-plugin-<version>-<build>-dist.zip`
  * `Plugins/Kafka/kafka-job-plugins-<version>-<build-dist.zip`
    {% endstep %}

{% step %}

### Extract the files&#x20;

Unzip both of the dowloaded files
{% endstep %}

{% step %}

### Run the Installers (for both unzipped files)

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

See [Kafka Offset Job Entry](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/kafka-offset), [Kafka Consumer Step](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-consumer), [Kafka Producer Step](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kafka-producer).
