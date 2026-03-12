# Source: https://help.cloudsmith.io/docs/manage-a-repository.md

# Repositories

Comprehensive guide to managing a Cloudsmith Repository

<HTMLBlock>
  {`
  <div class="cs-headline">A Repository, or repo, is a storage location for software packages and containers. 
  </div>
  `}
</HTMLBlock>

Cloudsmith provides polyglot repositories that can contain packages of all support types. You can create an unlimited number of repositories; providing you with the flexibility to suit any use-case.

> 📘
>
> At Cloudsmith we use "repository" as a general term. We also refer to "registry" and "feed" in line with the format's specific nomenclature.

## Repository Controls

Cloudsmith provides comprehensive controls to allow you to secure, monitor and control the packages inside each repository.

Use the top menu items to access the controls available:

<Image title="repositories.png" alt={1323} align="center" width="80%" src="https://files.readme.io/c70462e33e7074bce138a83187c3c99f7a05025268e34d0eb09522c76714285c-Screenshot_2024-10-18_at_22.21.48.png">
  Repository Settings
</Image>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Control
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        [Packages](https://help.cloudsmith.io/docs/repository-packages)
      </td>

      <td>
        A list of all uploaded packages and artifacts.
      </td>
    </tr>

    <tr>
      <td>
        [Package Groups](https://help.cloudsmith.io/docs/package-groups)
      </td>

      <td>
        A list of grouped packages by name (ignoring version/distro info)
      </td>
    </tr>

    <tr>
      <td>
        [Audit Logs](https://help.cloudsmith.io/docs/repo-audit-logs)  (Beta)
      </td>

      <td>
        A log of repository events
      </td>
    </tr>

    <tr>
      <td>
        [Client Logs](https://help.cloudsmith.io/docs/download-logs)
      </td>

      <td>
        View access logs for this repository
      </td>
    </tr>

    <tr>
      <td>
        [Client Statistics](https://help.cloudsmith.io/docs/statistics)
      </td>

      <td>
        See all the statistics gathered about your packages - downloads, bandwidth usage, etc.
      </td>
    </tr>

    <tr>
      <td>
        <span class="nobr">[License Compliance](https://help.cloudsmith.io/docs/license-compliance)</span>
      </td>

      <td>
        View and edit all licenses for packages in the repository
      </td>
    </tr>

    <tr>
      <td>
        [Package Logs](https://help.cloudsmith.io/docs/event-logs)
      </td>

      <td>
        View logs of package events for this repository
      </td>
    </tr>

    <tr>
      <td>
        [Security Scanning](https://help.cloudsmith.io/docs/security-scanning)
      </td>

      <td>
        Security Scanning for artifacts and Docker images
      </td>
    </tr>

    <tr>
      <td>
        [Signing Keys](https://help.cloudsmith.io/docs/signing-keys)
      </td>

      <td>
        GPG and RSA signing keys
      </td>
    </tr>

    <tr>
      <td>
        [Main Settings](https://help.cloudsmith.io/docs/repository-settings)
      </td>

      <td>
        Change the Name, Permissions, Visibility and if needed, delete the repository.
      </td>
    </tr>

    <tr>
      <td>
        [Access Controls](https://help.cloudsmith.io/docs/access-controls)
      </td>

      <td>
        Manage teams and user access to this repository
      </td>
    </tr>

    <tr>
      <td>
        [Custom Domains](https://help.cloudsmith.io/docs/custom-domains)
      </td>

      <td>
        Setup domain configuration to support your named endpoint. [Contact us](https://help.cloudsmith.io/docs/contact-us) for help!
      </td>
    </tr>

    <tr>
      <td>
        [Edge Caching](https://help.cloudsmith.io/docs/repository-edge-caching)
      </td>

      <td>
        Configure and manage edge caching rules
      </td>
    </tr>

    <tr>
      <td>
        [Entitlement Tokens](https://help.cloudsmith.io/docs/entitlements)
      </td>

      <td>
        Manage entitlement tokens for external, read-only access to private repositories.
      </td>
    </tr>

    <tr>
      <td>
        [EULA Enforcement](https://help.cloudsmith.io/docs/eula)
      </td>

      <td>
        Manage End-User License Agreement enforcement
      </td>
    </tr>

    <tr>
      <td>
        [Geo/IP Rules](https://help.cloudsmith.io/docs/geoip-restriction)
      </td>

      <td>
        Manage download permissions by IP and/or Geographic area
      </td>
    </tr>

    <tr>
      <td>
        [Retention Rules](https://help.cloudsmith.io/docs/retention-lifecycle)
      </td>

      <td>
        Manage the size of your repositories with retention settings
      </td>
    </tr>

    <tr>
      <td>
        [Upstream Proxying](https://help.cloudsmith.io/docs/proxying)
      </td>

      <td>
        Configure upstream sources for this repository
      </td>
    </tr>

    <tr>
      <td>
        [Webhooks](https://help.cloudsmith.io/docs/webhooks)
      </td>

      <td>
        Create and configure webhooks to allow external tools/systems to see your Cloudsmith events
      </td>
    </tr>
  </tbody>
</Table>