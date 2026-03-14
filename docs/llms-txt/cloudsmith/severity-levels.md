# Source: https://help.cloudsmith.io/docs/severity-levels.md

# Severity Levels

When raising a support ticket, customers are prompted to select the severity of the issue they are experiencing. This helps our support team triage and assess the level of impact or importance the issue has on your organization.

At Cloudsmith, we employ a severity (SEV) rating system ranging from 1 to 5, where a lower number signifies a higher severity.

For example:

1. **Critical** : A critical incident with a very high impact. For example, the platform is unavailable or completely unusable for all users.

2. **High**: A major incident with significant impact. For example, a service is down for a subset of users, or a critical function within the platform is not functioning.

3. **Medium**: Moderate application functionality or performance loss, but a workaround is available. For example, delays or intermittent errors when pushing/pulling packages.

4. **Low**: An isolated non-critical issue affecting a small number of users or a subset of non-critical packages. For example, 2FA reset or documentation not matching functionality.

5. **Lowest**: Questions or clarifications around features, feature enablement or general inquiries. No impact on the operation of the platform.

A detailed overview of each severity is also displayed within the following table:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Severity
      </th>

      <th>
        Impact
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Critical
        (SEV 1)
      </td>

      <td>
        • Widespread outage.\
        • Platform completely inoperative.\
        • All organization users severely. impacted and unable to perform normal functions.\
        • No workaround exists.
      </td>

      <td>
        • Broad impact platform outage.\
        • Platform is completely unavailable via UI, CLI, and API.\
        • Unable to push or pull any packages.
      </td>
    </tr>

    <tr>
      <td>
        High\
        (SEV 2)
      </td>

      <td>
        • Major failure or degradation of platform availability or performance.\
        • Platform is available but severely impacted.\
        • Significant impact for multiple users.\
        • Inconvenient workaround or no workaround exists.
      </td>

      <td>
        • Service interruptions to some but not all platform features.\
        • Severe delay or consistent failure in push/pull actions.\
        • Issues are restricted to a single package format.\
        • Platform is unavailable or severely degraded via UI, CLI or API.
      </td>
    </tr>

    <tr>
      <td>
        Medium\
        (SEV 3)
      </td>

      <td>
        • Moderate application functionality or performance loss.\
        • A temporary workaround exists.\
        • Multiple users are impacted in their normal function.
      </td>

      <td>
        • Moderate delay or intermittent failures when performing push/pull actions.\
        • Issue with a single package (i.e. a single docker image).\
        • Packages not fetched from upstream.\
        • Package can be pushed by a user but not via a service account.
      </td>
    </tr>

    <tr>
      <td>
        Low\
        (SEV 4)
      </td>

      <td>
        • Isolated issue, affecting a small number of users or small subset of noncritical packages.\
        • Low impact on operations.\
        • Reasonable workaround is available.
      </td>

      <td>
        • Minor delays or occasional failure with package push/pull actions.\
        • Noncritical functionality impacted.\
        • Functionality does not match documentation.\
        • 2FA reset.
      </td>
    </tr>

    <tr>
      <td>
        Lowest\
        (SEV 5)
      </td>

      <td>
        • No platform impact.\
        • General enquiries.\
        • Feature setup.
      </td>

      <td>
        • Feature request/setup.\
        • Questions regarding functionality. \
        • Beta feature enablement. \
        • Custom domain creation.
      </td>
    </tr>
  </tbody>
</Table>

At Cloudsmith, we understand that our customers are the best judges of how an issue will impact their business. That's why we ask you to select the severity level when submitting a support ticket. However, we reserve the right to make the final determination of the severity level based on the information provided.

Our support team will review the issue, assess the impact on the customer's business, and assign a severity level based on our established guidelines. This helps us ensure that we are providing an appropriate level of support and allocating our resources effectively to address the issue.