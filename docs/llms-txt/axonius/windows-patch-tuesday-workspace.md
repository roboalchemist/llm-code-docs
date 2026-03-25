# Source: https://docs.axonius.com/docs/windows-patch-tuesday-workspace.md

# Windows Patch Tuesday Workspace

Windows Patch Tuesday Workspace monitors the patch currency of all Windows clients and servers. This workspace identifies lagging devices, critical vulnerabilities, and unsupported systems. This helps teams prioritize updates, close exposure gaps, and maintain a secure, resilient environment.

### The Challenge

Organizations often struggle to efficiently identify and track Windows devices with outdated operating system builds and patches. Without a built-in mechanism to automatically flag these devices, teams are forced to rely on time-consuming, manual workarounds. This results in:

* Substantial human effort consumed in tracking regular Windows "Patch Tuesday" releases
* Delays in identifying and patching vulnerable systems
* Increased risk exposure to known exploits
* Difficulties in consistently adhering to patch policies for compliance and audits
* Overwhelming amount of work, containing numerous, potential distractions

### Our Solution

Axonius Windows Patch Tuesday automatically flags Windows devices whose OS doesn't match the latest vendor patch data, eliminating the need for manual comparison. By providing a centralized, consolidated, real-time view of the organization's patching posture, Axonius empowers security and IT teams to:

* Quickly identify and prioritize devices requiring critical security updates, thus reducing attack surface
* Enhance operational efficiency
* Ensure consistent adherence to security controls and regulatory requirements

### Recommended Adapter Categories

To see valuable data in this workspace, we recommend you connect adapters from the following categories:

* Directory Services
* EDR/EPP
* MDM/EMM
* RMM
* Configuration and Patch Management

## Workspace Assets and Modules

<Callout icon="📘" theme="info">
  **Note**

  Each workspace has its own use-case-focused navigation menu on the left. The assets and modules available from this menu depend upon your access configuration.
</Callout>

You can access the following assets directly from this workspace:

* [Devices](/docs/devices-page)
* [Aggregated Security Findings](/docs/vulnerabilities).

See [Using Workspaces](/docs/workspaces) to learn how to generally access, navigate, and use workspaces.

## Use Cases this Workspace Helps You Fulfill

The Windows Patch Tuesday's Home page displays charts and KPIs of special interest, divided into functional areas that help you focus on specific use-case information.

### General Patching Posture Picture

The **Overview** section displays the total counts of active Windows devices in your environment, highlighting the proportions of Clients and Server devices, and the relative health status of each category - how many clients/servers are up-to-date and how many are lagging.

These charts provide a simple, straightforward view of your patch currency status, helping you see where you currently stand and understand what to expect in the near future.

### Identifying Risks Quickly

Comprehensive, up-to-date patching posture data help you recognize risks ahead of time, prioritize remediation or patching efforts, and ensure your teams focus on the highest-impact issues.

To achieve that, this workspace shows devices requiring immediate attention due to heightened risk or unsupported status. The data is based on different Exposures and Software-related criteria - CVE score, any CISA known exploited vulnerabilities, and EOL/EOS/EoES status.

### Exploring Missing Patches in Context

The Patch Backlog Heatmap maps all Windows Server/Client devices by their distribution type against the number of missing patches. For each distribution type (such as Windows Server 2016, Windows Server 2019, etc.), the chart shows how many patches behind the latest version each device group is, and the overall numbers of affected devices. This helps you detect clusters of lagging servers and asses your overall patch hygiene.