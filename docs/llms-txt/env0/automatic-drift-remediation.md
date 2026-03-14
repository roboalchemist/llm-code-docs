# Source: https://docs.envzero.com/guides/admin-guide/environments/drift-detection/automatic-drift-remediation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remediate Drift

> Automatically or manually remediate infrastructure drift in env zero by deploying code or creating pull requests

Drift occurs when the actual state of your infrastructure no longer matches its desired state, which can lead to security, compliance, and reliability risks, as well as increased costs. Complementing env zero's [Drift Detection](/guides/admin-guide/environments/drift-detection) capabilities, Drift Remediation ensures consistency by quickly reconciling drift as part of your infrastructure management workflow - either automatically or with a simple two-click manual action.

## Configuring Automatic Drift Remediation

Activating automatic Drift Remediation offers a hassle-free way to ensure that all detected drifts are immediately corrected, using one of the following options:

* **Disabled**: Selecting this option will disable automatic drift remediation. When drift is detected, you will need to manually review and remediate the differences.
* **Deploy code changes to the cloud (Run env zero deployment)**: If drift is detected, env zero will automatically attempt to remediate it by running an env zero deployment with the latest configuration from your connected version control system (VCS). This option assumes that the desired state is accurately reflected in your code.
* **Create a pull request for manually modified cloud resources**: If drift is detected and it appears that cloud resources were modified manually (outside of env zero), this option will trigger the creation of a pull request in your connected VCS. This pull request will contain the changes necessary to bring your IaC configuration in line with the current cloud state. This allows you to review and approve the changes before they are applied.
* **If the cloud resource was manually changed, create a pull request; otherwise, deploy code changes to the cloud**: This option provides a hybrid approach. If drift is detected and identified as a manual cloud modification, a pull request will be created for review. However, if the drift is not attributed to a manual change, env zero will automatically attempt to remediate it by deploying the latest code from your VCS.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/3656607c4c6ae5ab7d822b512b0dd74f809c3d8c1452177d84e21d97b5e67e7a-image.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=dc9d87e563991078c7ef1964f90464f0" alt="" width="1403" height="686" data-path="images/guides/admin-guide/environments/drift-detection/3656607c4c6ae5ab7d822b512b0dd74f809c3d8c1452177d84e21d97b5e67e7a-image.png" />

The setting can be configured at the project level for all newly created environments or individually at the environment level.

Finally, automatic remediation can also be set to Disabled, allowing you to reconcile drift manually using the ‘Remediate Drift’ button available on the deployment details page. There, you can choose how to resolve the detected discrepancies between your code and the actual infrastructure state. The specific actions available under this button allow you to initiate the reconciliation process:

* **Deploy code changes:**
  * It immediately attempts to apply the configuration defined in your current code/template directly to the live infrastructure, overwriting the detected drift to enforce the state defined by your code.
* **Create a pull request:**
  * It generates a pull request (PR) in your version control system containing the code modifications needed to correct the drift. This allows the fix to be reviewed and approved before being merged and deployed.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/73ccfc413d06789eba8bad9297170865f376f2f950ecad53ab58cf8b7eb96139-image.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=234be4a1ceed2bf27dcbf8d9c26ff147" alt="" width="1556" height="339" data-path="images/guides/admin-guide/environments/drift-detection/73ccfc413d06789eba8bad9297170865f376f2f950ecad53ab58cf8b7eb96139-image.png" />

## Policies and Governance

Importantly, Drift Remediation deployments support all existing env zero policies and governance features. This ensures that any automated remediation action adheres to approval processes, security policies, and compliance requirements.\
For example, you can require approval before applying Automatic Drift Remediation to certain environments.\
See [Approval Policies](/guides/policies-governance/approval-policies) for details on how to configure these rules.

## Scheduling Deployments

In some cases, rather than reacting to drift immediately, you may want to ensure that infrastructure is regularly reconciled with your code.\
[Scheduling](/guides/admin-guide/environments/scheduling) allows you to automate deployments at predefined intervals to maintain alignment with your declared configuration.

Built with [Mintlify](https://mintlify.com).
