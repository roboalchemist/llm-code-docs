# Source: https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# System inventory

A system inventory is a resource that contains information about the hardware and software assets within an IT infrastructure. Keeping an inventory of all assets helps organizations maximize the visibility of hardware and software in their environment. An up-to-date system inventory is essential for maintaining good IT hygiene within an enterprise network.

Wazuh agents collect system information from monitored endpoints and forward it to the Wazuh server to maintain a centralized system inventory. This information is processed on the Wazuh server and then sent to the Wazuh indexer, where it is stored as global state data. The Wazuh Syscollector module on the Wazuh agent collects hardware, operating system, installed software, network interfaces, port, running processes, browser extensions, services, users and groups information from each agent. The Wazuh agent can also collect data about Windows updates from Windows endpoints. You can configure what kind of information you want the Syscollector module to collect or ignore.

Users can generate system inventory reports from the Wazuh dashboard, which can be valuable resources during threat hunting and IT hygiene exercises. The information contained in the report can be used to identify unwanted applications, processes, services, and malicious artifacts.

> ##### Contents
> 
> * [How it works](how-it-works.md)
> * [Configuration](configuration.md)
>   * [Wazuh agent configuration](configuration.md#wazuh-agent-configuration)
>   * [Wazuh manager configuration](configuration.md#wazuh-manager-configuration)
> * [Viewing system inventory data](viewing-system-inventory-data.md)
>   * [Dashboard](viewing-system-inventory-data.md#dashboard)
>   * [System](viewing-system-inventory-data.md#system)
>   * [Software](viewing-system-inventory-data.md#software)
>   * [Processes](viewing-system-inventory-data.md#processes)
>   * [Network](viewing-system-inventory-data.md#network)
>   * [Identity](viewing-system-inventory-data.md#identity)
>   * [Services](viewing-system-inventory-data.md#services)
>   * [Query the agent inventory data](viewing-system-inventory-data.md#query-the-agent-inventory-data)
> * [Generating system inventory reports](generating-system-inventory-reports.md)
>   * [IT Hygiene report](generating-system-inventory-reports.md#it-hygiene-report)
>   * [Property-specific report](generating-system-inventory-reports.md#property-specific-report)
> * [Available inventory fields](available-inventory-fields.md)
>   * [Hardware](available-inventory-fields.md#hardware)
>   * [Operating system](available-inventory-fields.md#operating-system)
>   * [Packages](available-inventory-fields.md#packages)
>   * [Networks](available-inventory-fields.md#networks)
>   * [Ports](available-inventory-fields.md#ports)
>   * [Processes](available-inventory-fields.md#processes)
>   * [Windows updates](available-inventory-fields.md#windows-updates)
>   * [Users](available-inventory-fields.md#users)
>   * [Groups](available-inventory-fields.md#groups)
>   * [Services](available-inventory-fields.md#services)
>   * [Browser extensions](available-inventory-fields.md#browser-extensions)
> * [Compatibility matrix](compatibility-matrix.md)
> * [Using Syscollector information to trigger alerts](using-syscollector-information-to-trigger-alerts.md)
>   * [Create a custom rule that uses the built-in Syscollector rule 221](using-syscollector-information-to-trigger-alerts.md#create-a-custom-rule-that-uses-the-built-in-syscollector-rule-221)
>   * [New searchable fields on the Wazuh dashboard](using-syscollector-information-to-trigger-alerts.md#new-searchable-fields-on-the-wazuh-dashboard)
> * [Use cases](use-cases.md)
>   * [Use case 1. Resource monitoring](use-cases.md#use-case-1-resource-monitoring)
>   * [Use case 2: Vulnerability management](use-cases.md#use-case-2-vulnerability-management)
> * [Osquery](osquery.md)
>   * [How it works](osquery.md#how-it-works)
>   * [Configuration](osquery.md#configuration)
>   * [Alert examples](osquery.md#alert-examples)
