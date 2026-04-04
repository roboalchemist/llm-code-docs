# Source: https://docs.snyk.io/scan-with-snyk/snyk-container/kubernetes-integration/kubernetes-integration-ui-explained/kubernetes-and-the-snyk-priority-score.md

# Kubernetes and the Snyk Priority Score

{% hint style="info" %}
This capability is enabled automatically for all customers using the Kubernetes integration and does not require any additional configuration.
{% endhint %}

All issues in Snyk have a [Priority Score](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/priority-score). This helps determine the relative importance of vulnerabilities, taking into account both the severity of the issue and various other contextual factors.

Similar to the factors contributing to the Priority Score, images imported from the Kubernetes integration also have a number of additional contributing factors.

## How well configured is your workload?

The Kubernetes integration collects information about how workloads are configured, focusing on options that can lead to security issues. Snyk displays this summary on the Project page:

![Project configuration details](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-69907dc2d4b0bc4fba3e13c717c46b21bffd399e%2Fsecure_configuration_info.png?alt=media)

To see the factors taken into consideration for the Priority Score of each vulnerability, hover over the score.

![](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-91fce95685977c2f576568f40ad515bb6f7be665%2Fhover_priority_score.png?alt=media)

The rationale is based on the fact that a vulnerability that is present in a poorly configured workload scores higher than the same vulnerability found in a well-configured workload.

Snyk considers both the nature of the vulnerabilities and the specific issues raised by the configuration. Snyk takes into account the following factors:

| **Configuration**                                                                                   | **Vulnerability properties**                                                                                                  |
| --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Permission issues, for instance running privileged, able to run as root, not dropping capabilities. | CVSSv3 Privileges (PR) vector present in the vulnerability. Weighing based on the impact.                                     |
| Missing memory and/or CPU limits.                                                                   | CVSSv3 Availability (A) vector present in the vulnerability, or CWE includes denial of service. Weighing based on the impact. |
| Not setting a read only root filesystem.                                                            | CWE indicates filesystem access required.                                                                                     |

This scoring system is not intended to be binary. Rather, it’s a risk calculation intended to help you prioritize your efforts.
