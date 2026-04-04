# Source: https://docs.infrahub.app/integrations.md

# Infrahub Integrations

Infrahub integrates with a wide range of infrastructure management and automation tools to help you synchronize data, automate workflows, and manage your infrastructure. This page provides an overview of all available integrations and their capabilities.

## Network automation and validation platforms[​](#network-automation-and-validation-platforms "Direct link to Network automation and validation platforms")

### Ansible[​](#ansible "Direct link to Ansible")

The OpsMill Infrahub Ansible Collection provides modules and plugins to seamlessly interact with Infrahub through Ansible. This integration enables you to define and enforce the desired state of your infrastructure using Ansible playbooks.

**Key capabilities:**

* Dynamic inventory from Infrahub GraphQL data
* Node creation, updates, and deletion
* Branch management and manipulation
* GraphQL queries and lookup operations
* Artifact retrieval and management

[Ansible Documentation/ansible](/ansible.md)

### Kriten[​](#kriten "Direct link to Kriten")

Kriten is an API-first automation engine that transforms containerized scripts into secure REST API endpoints. The integration with Infrahub creates a powerful automation pipeline that separates data modeling from task execution, enabling secure cross-domain automation.

**Key capabilities:**

* Webhook-triggered automation from Infrahub events
* Automatic API generation from containerized scripts
* Enterprise-grade security with RBAC and audit trails
* Support for synchronous and asynchronous job execution
* Multi-language script support for diverse automation needs

[Infrahub-Kriten Integrationhttps://opsmill.com/blog/infrahub-kriten-integration/](https://opsmill.com/blog/infrahub-kriten-integration/)

### Netpicker[​](#netpicker "Direct link to Netpicker")

Netpicker provides network testing and compliance validation capabilities that integrate with Infrahub as a source of truth. This integration enables automated compliance checking by comparing live device configurations against Infrahub data.

**Key capabilities:**

* Device interface compliance validation
* Configuration drift detection between Infrahub and live devices
* Automated assertion-based testing for network infrastructure
* Integration with pytest frameworks for network testing workflows

[NetPicker Infrahub Integrationhttps://github.com/netpicker/pytests-for-networking/blob/main/Integrations/Infrahub/infrahub.py](https://github.com/netpicker/pytests-for-networking/blob/main/Integrations/Infrahub/infrahub.py)

### Nornir[​](#nornir "Direct link to Nornir")

A Nornir plugin that allows Infrahub to serve as an inventory source for Nornir-based network automation workflows. This integration simplifies network automation by providing structured data directly from your Infrahub instance.

**Key capabilities:**

* Inventory management with GraphQL-based host and group data
* Artifact management for configuration templates and files
* Host-specific artifact regeneration
* Bulk artifact generation across multiple devices

[Nornir Documentation/nornir](/nornir.md)

## Data synchronization with Infrahub Sync[​](#data-synchronization-with-infrahub-sync "Direct link to Data synchronization with Infrahub Sync")

Infrahub Sync is a versatile Python package that synchronizes data between source systems and Infrahub. Built on `diffsync`, it provides flexible and efficient data synchronization across different network management platforms.

[Infrahub Sync Overview/sync](/sync.md)

### Network management systems[​](#network-management-systems "Direct link to Network management systems")

#### LibreNMS[​](#librenms "Direct link to LibreNMS")

Integrates with the open-source LibreNMS network monitoring system to import device and monitoring data into Infrahub for centralized infrastructure management.

[LibreNMS Adapter/sync/adapters/librenms](/sync/adapters/librenms.md)

#### Observium[​](#observium "Direct link to Observium")

Connects with Observium network monitoring platform to synchronize device discovery and performance data with Infrahub for comprehensive network visibility.

[Observium Adapter/sync/adapters/observium](/sync/adapters/observium.md)

### Infrastructure documentation systems[​](#infrastructure-documentation-systems "Direct link to Infrastructure documentation systems")

#### Nautobot[​](#nautobot "Direct link to Nautobot")

Synchronizes data from Nautobot, an open-source network source of truth platform. Supports both Nautobot v1 and v2 data models with flexible schema mapping.

**Key data synchronized:**

* Device and platform information
* Location and site hierarchies
* Manufacturer and hardware data
* Tags and custom attributes

[Nautobot Adapter/sync/adapters/nautobot](/sync/adapters/nautobot.md)

#### Netbox[​](#netbox "Direct link to Netbox")

Imports infrastructure data from NetBox, the popular open-source IPAM and DCIM tool, into Infrahub while maintaining data relationships and hierarchies.

**Key data synchronized:**

* Device inventory and rack layouts
* IP address management (IPAM) data
* Location hierarchies (regions, sites, racks)
* Circuit and connection documentation

[Netbox Adapter/sync/adapters/netbox](/sync/adapters/netbox.md)

#### Peering manager[​](#peering-manager "Direct link to Peering manager")

Bi-directional synchronization with Peering Manager for comprehensive BGP session and interconnection management.

**Key data synchronized:**

* BGP communities and routing policies
* Peering session configurations
* Internet exchange point (IXP) data
* AS (Autonomous System) information

[Peering Manager Adapter/sync/adapters/peering-manager](/sync/adapters/peering-manager.md)

### Network data collection[​](#network-data-collection "Direct link to Network data collection")

#### IP Fabric[​](#ip-fabric "Direct link to IP Fabric")

Synchronizes network discovery data from IP Fabric's network discovery and validation platform into Infrahub. IP Fabric provides automatic network discovery and advanced analytics through SSH/Telnet connectivity.

**Key data synchronized:**

* Device inventory with hardware details
* Network topology and relationships
* Platform and software version data

[IP Fabric Adapter/sync/adapters/ipfabric](/sync/adapters/ipfabric.md)

#### Slurp'it[​](#slurpit "Direct link to Slurp'it")

Integrates with Slurp'it network data collection platform to import structured network configuration and operational data into Infrahub.

**Key data synchronized:**

* Device vendor and model information
* Network configuration templates
* Routing table and interface data
* Custom planning and operational data

[Slurp'It Adapter/sync/adapters/slurpit](/sync/adapters/slurpit.md)
