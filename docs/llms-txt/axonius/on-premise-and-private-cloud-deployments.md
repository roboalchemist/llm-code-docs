# Source: https://docs.axonius.com/docs/on-premise-and-private-cloud-deployments.md

# Axonius Cyber Asset Management: Customer-hosted (on-premises / private cloud)

In on-premises deployments, Axonius is deployed on a virtual appliance that is part of your organization’s internal network.

## How It Works & System Architecture

<Image alt="Axonius Architecture - OnPREm.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Axonius%20Architecture%20-%20OnPREm.png" />

The Axonius solution is deployed as a single virtual appliance. It does not rely on more traditional methods of acquiring data for asset inventories, such as:

* Listening and monitoring network traffic.
* Scanning the network for systems that are online at the time of the scan.
* Installing additional endpoint agents.

To aggregate and correlate asset data, Axonius securely fetches data on periodic and custom discovery cycles from your IT, Security, and Infrastructure solutions using pre-built integrations with hundreds of security and management solutions, known as [adapters](/docs/adapters-list).

Once the virtual appliance is deployed, the solution utilizes adapters to connect to its target data sources. Each adapter requires basic configuration information, including the hostname or IP address of the target system, and the relevant read only access credentials. For example, in the case of Microsoft Active Directory, the solution needs the IP address or hostname of a Domain Controller and a username/password with sufficient privileges to read all relevant objects.

If an adapter needs to connect to a solution on a separate segregated network, a Compute Node virtual machine (VM) can be deployed to relay the information to the Primary Node VM through a dedicated network IP port with all traffic being encrypted across this protocol.

## System Requirements

<Callout icon="📘" theme="info">
  Note

  It is not recommended to use a 32-bit browser. This may lead to browser crashes.
</Callout>

The following requirements apply to Compute and Primary nodes for customer-hosted (on-premises/private cloud) systems for Axonius version 6.1.34 and up:

Axonius requires the following minimum x86\_64 microarchitectures:

* For Intel x86\_64, Axonius requires either:
  * A Sandy Bridge or later Core processor, or
  * A Tiger Lake or later Celeron or Pentium processor.
* For AMD x86\_64, Axonius requires:
  * Axonius only supports Oracle Linux running the Red Hat Compatible Kernel (RHCK). Axonius does not support the Unbreakable Enterprise Kernel (UEK).
* Axonius 6.1.34 and up requires use of the AVX instruction set, available on select Intel and AMD processors.

### Minimum Supported Infrastructure Versions

#### Docker Engine Support

The minimum version for Docker to ensure compatibility with our current container orchestration and security patches:

* Minimum Supported Version: 20.10.18

Recommendation: Environments running versions older than 20.10.18 must be upgraded immediately to avoid service disruptions or unpatched vulnerabilities.

#### Ubuntu Operating System Support

Axonius officially supports the following Ubuntu versions for technical support and testing:

* Official Host Version: Ubuntu 22.04 LTS
* Ubuntu 24.04 LTS Status: Not officially supported at this time.

<br />

For more details on adapters and enforcement actions, see:

* [Adapter List](/docs/adapters-list)
* [Enforcement Center - Action Library](/docs/action-library)
* [Connecting Additional Axonius Collector Nodes](/docs/connecting-additional-axonius-nodes)