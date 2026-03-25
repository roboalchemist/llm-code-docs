# Source: https://docs.axonius.com/docs/crowdstrike-falcon.md

# CrowdStrike Falcon

## Overview

**CrowdStrike Falcon** is a cloud-native endpoint protection platform that provides next-generation antivirus (NGAV), endpoint detection and response (EDR), managed threat hunting, vulnerability management, and threat intelligence.
The Axonius CrowdStrike Falcon adapter enables visibility into endpoint devices, vulnerabilities, users, roles, alerts, and configuration data to support SaaS Application management, endpoint coverage audits, and incident response workflows.

<Callout icon="📘" theme="info">
  Note

  If you are using CrowdStrike Falcon Identity Protection (formerly Preempt), you need to use the [CrowdStrike Falcon Identity Protection adapter](/docs/preempt).
</Callout>

### Use Cases the Adapter Solves

The **CrowdStrike Falcon** adapter provides insight into endpoint security coverage and device health across the organization. It helps identify endpoints without Falcon agents, outdated agent versions, and devices that may be unmanaged or misconfigured.

By correlating **CrowdStrike Falcon** data with other Axonius data sources, organizations can:

* Audit endpoint protection coverage
* Identify unmanaged or unprotected devices
* Enrich endpoint context with business and ownership data
* Track vulnerabilities and security posture
* Support incident response and remediation workflows

## Types of Assets Fetched

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg" /> Devices |<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Vulnerabilities.svg" /> Aggregated Security Findings | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg" /> Users | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg" /> Roles | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_settings.svg" /> Application Settings | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg" /> SaaS Applications | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Domains_URLs.svg" /> Domains & URLs | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Containers.svg" /> Containers | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg" /> Alerts/Incidents | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Accounts_Tenants.svg" /> Accounts/Tenants

## Before You Begin

### Authentication Methods

The **CrowdStrike Falcon** adapter supports authentication using:

* **Client ID / Client Secret** – Required for connecting the adapter.
* **Username / Password** - Required for fetching **Application Settings**.

### Required Permissions

<Tabs>
  <Tab title="Cyber Assets">
    <Columns layout="auto">
      <Column>
        <strong>Permissions:</strong>

        <ul>
          <li><code>Assets:Read</code></li>
        </ul>
      </Column>
    </Columns>

    <strong> API Permissions </strong>

    <table>
      <thead>
        <tr>
          <th>Scope</th>
          <th>Permission</th>
          <th>Notes</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>Hosts</td>
          <td>Read</td>

          <td />
        </tr>

        <tr>
          <td>Host groups</td>
          <td>Read</td>

          <td />
        </tr>

        <tr>
          <td>IOC Management</td>
          <td>Read</td>

          <td />
        </tr>

        <tr>
          <td>Prevention policies</td>
          <td>Read</td>

          <td />
        </tr>

        <tr>
          <td>Detections</td>
          <td>Read</td>

          <td />
        </tr>

        <tr>
          <td>User Management</td>
          <td>Read</td>

          <td />
        </tr>

        <tr>
          <td>Sensor Update Policies</td>
          <td>Read</td>

          <td />
        </tr>

        <tr>
          <td>Indicators</td>
          <td>Read</td>

          <td>
            Requires CrowdStrike Falcon Intelligence Add-on.
            Used to discover shadow SaaS applications.
          </td>
        </tr>

        <tr>
          <td>Vulnerabilities</td>
          <td>Read</td>

          <td>
            Requires an active CrowdStrike Falcon Vulnerability subscription.
            May assist in discovering shadow SaaS applications.
          </td>
        </tr>
      </tbody>
    </table>
  </Tab>

  <Tab title="SaaS Applications">
    <p>
      To fetch SaaS Applications data the following user permissions are required:
    </p>

    * View Quarantine File settings
    * View Response policies
    * And the following scopes:

    | Scope                   | Permission |
    | :---------------------- | :--------- |
    | Hosts                   | Read       |
    | Host groups             | Read       |
    | IOC Management          | Read       |
    | Prevention policies     | Read       |
    | Sensor update policies  | Write      |
    | Device Control Policies | Read       |
  </Tab>
</Tabs>

## More Information About This Adapter

[Deploying the CrowdStrike Falcon Adapter](/docs/crowdstrike-falcon-deploying-the-adapter)

[CrowdStrike Falcon Additional Permissions](/docs/crowdstrike-falcon-additional-permissions)

[CrowdStrike Falcon Advanced Settings](/docs/crowdstrike-falcon-advanced-settings)

[CrowdStrike Falcon Related Enforcement Actions](/docs/crowdstrike-falcon-related-enforcement-actions)