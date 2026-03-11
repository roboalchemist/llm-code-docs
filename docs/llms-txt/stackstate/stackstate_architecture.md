# Source: https://archivedocs.stackstate.com/5.1/use/concepts/stackstate_architecture.md

# StackState architecture

## Overview

StackState is built for scale and runs on Kubernetes in your cloud or data center.

In most cases, a single Host Agent is installed on the StackState server to provide Agent-less integration with APIs from multiple sources. Data is gathered and received by one or more Agents and delivered at the Receiver API. From there, all data is put on Kafka. The data is processed by microservices and ends up as Topology in our versioned graph database, called StackGraph. Traces, and some telemetry data, are temporarily stored in Elasticsearch.

A Script and Query Language provides access to all dimensions of the 4T Data Model. They're also used by our own AI Microservices to interface with the 4T Data Model.

REST APIs are available for external services and are also used by our Command Line Interface. Every user interface is kept up to date by WebSocket APIs.

Notifications, tickets, webhooks, and API calls are just a few examples of output data sources to let you respond to situations you observe in StackState.

![StackState architecture and data flow](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-86e96b03e44bedda05aeab600921cc6c36995644%2Fsts-architecture.svg?alt=media)

## Data sources

StackState integrates with external systems to retrieve data. Integrations use [StackState Agent](https://archivedocs.stackstate.com/5.1/setup/agent/about-stackstate-agent) or an associated [integration StackPack](https://archivedocs.stackstate.com/5.1/stackpacks/integrations).

## StackGraph

StackState configuration and topology data are stored in the StackGraph database.

## StackState User Interface and CLI

The StackState User Interface visualizes all collected data in [perspectives](https://archivedocs.stackstate.com/5.1/use/concepts/perspectives). You can also customize your instance of StackState here by adding automation steps, such as event handlers and output to external systems.

You can optionally install the [StackState CLI](https://archivedocs.stackstate.com/5.1/setup/cli) to control your StackState instance directly from the command line.

## Open source

### StackState Agent V3

StackState Agent V3 is open source and available on GitHub:

* Agent - <https://github.com/StackVista/stackstate-agent>
* Agent integrations - <https://github.com/StackVista/stackstate-agent-integrations>

### StackPacks

The StackPacks listed below are open source and available on GitHub:

* Custom Sync StackPack - <https://github.com/StackVista/stackpack-autosync>
* SAP StackPack - <https://github.com/StackVista/stackpack-sap>
* SolarWinds StackPack - <https://github.com/StackVista/stackpack-solarwinds>
* Splunk StackPack - <https://github.com/StackVista/stackpack-splunk>
