# Source: https://docs.axonius.com/docs/network-inspector-functionality.md

# Network Inspector Functionality

This topic provides high-level information about the Axonius Network Inspector device functionality.

## Concept Diagram

The following diagram shows the main elements of the Axonius Network Inspector device connections, components, and data flow.

<Image align="center" alt="Axonius Network Inspector device functionality" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/deployment/Network%20Inspector%20Functionality.png" className="border" />

<Callout icon="📘" theme="info">
  **Note**

  For the list of IP addresses and domains assigned to the US and EU, see the <Anchor label="Axonius support page" target="_blank" href="https://support.axonius.com/hc/en-us/articles/35991260012055-Network-Inspector-Requirements">Axonius support page</Anchor> for the Axonius Network Inspector device.
</Callout>

## Server Appliance Ports

The server appliance device includes the following pre-configured ports:

* **Management** – Used for initial configuration and connecting to your network. This port enables the server appliance to connect to the Axonius cloud, allows users to access the web console, and facilitates remote maintenance and updates by the support team.

* **iDRAC** (integrated Dell Remote Access Controller) – Used for device hardware and software support in case of failures.

<Callout icon="📘" theme="info">
  **Note**

  Small Form Factor or mini PC appliances do not have an iDRAC port. When configuring such appliances, ignore all iDRAC configuration instructions.
</Callout>

* **SPAN** (Switched Port Analyzer) – Used for monitoring network traffic via your network switch.