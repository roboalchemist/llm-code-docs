# Source: https://docs.axonius.com/docs/saas-deployment.md

# Axonius-hosted (SaaS)

In Axonius-hosted (SaaS) deployments, Axonius is deployed on an AWS EC2 instance that is fully separated from other customers’ environments. The AWS EC2 instance can be hosted on any of the available Amazon EC2 Regions, and is automatically backed up to allow restoration in case of failure.

## How It Works & System Architecture

<Image alt="Axonius Architecture - AX_Hosted.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Axonius%20Architecture%20-%20AX_Hosted.png" />

To aggregate and correlate asset data, Axonius securely fetches data from your IT, Security, and business solutions using pre-built integrations with hundreds of security and management solutions, known as [adapters](/docs/adapters-list).

Since the Axonius-hosted (SaaS) instance resides in the cloud and is not part of your organization's internal network, you must install the Axonius Gateway to connect to adapter sources that are only accessible by an internal network. The [Axonius Gateway](/docs/installing-axonius-tunnel) enables you to establish a secure link between an internal network and the Axonius-hosted (SaaS) instance.

Axonius fetches data on periodic and custom discovery cycles from configured adapters. During these discovery cycles, the Axonius Gateway is used as a VPN to pull asset data from the sources of the adapters that are part of your organization’s internal network.

The Axonius Gateway is a container that is installed on an on-premises server you provision that can access the internet via TCP port 443 from the Gateway server either by direct connection or by HTTPS proxy. Once the Axonius Gateway is installed, it initiates a connection from the on-premises container to the Axonius-hosted (SaaS) instance. After this connection is established, bi-directional communication is enabled on the top of that Gateway, using the VPN protocol.

To connect adapters that are accessible to the internet, such as other SaaS solutions, configuring and installing the Axonius Gateway is not required.

### Trust Center

More information and aspects regarding our security program can be found in in [Axonius Trust Center](https://trust.axonius.com/). This presents general information regarding security standards, certifications and other security data items.

### Third Party IP Allowlisting

For third party services to which Axonius is connecting  that require IP Allowlisting information, you will need to provide the Public IP Address of your Axonius instance. This is where outbound traffic will be originating from. Please contact Axonius Support if you require assistance confirming the Public IP Address

### Hardware requirements for the Axonius Gateway server:

* An An Intel x86\_64 architecture processor
* At least 1 GB of free disk space
* At least 1 GB of RAM dedicated to the gateway container
* The EC2 instance size for a gateway server deployed in AWS should be t3.small.

For more details about  adapters and enforcement actions, see:

* [Axonius Gateway](/docs/installing-axonius-tunnel)
* [Adapter List](/docs/adapters-list)
* [Enforcement Center - Action Library](/docs/action-library)