# Source: https://docs.gitguardian.com/secrets-detection/core-concepts/secure-secrets-management.md

# Secure secrets management

> Discusses the challenges of secure secrets management in the SDLC and the role of automated detection and remediation.

## Managing secrets in the SDLC

### There's no silver bullet

Secrets are so widely used in DevOps environments that there simply canât be a one-size-fits-all for managing them. We have development secrets used by developers, build secrets, application secrets, infrastructure secrets, etc.

Even for the most mature DevSecOps organizations or teams, secrets management is very difficult to master, because it is a matter of striking a right balance between security and accessibility. This second point is very important for one simple reason: in modern development teams, secrets are required by everyone. Making it hard to use secrets will inevitably lead to the bypassing of the protective layers in place, and lead to practices such as hardcoding them.

In practice, it is easy to see that there is a gap between theory and practice when it comes to handling and sharing credentials in a team, a department, or an organization. For example, the organization may pay for a cloud-based secrets manager, a vault, or maybe even for a dedicated team to administrate these tools, which makes it falsely think it has solved this problem. But under further scrutiny, it would realize that the long-lived credentials are also stored on the devsâ local machines for convenience.

### Find your way to secure secrets management

There are various ways with which secrets can be managed in the software development lifecycle. You should explore the following options with infrastructure and engineering teams before deciding which one is the right approach for your organization:

- ~~Hardcoded in source code and templates~~ (please, don't.)
- Grouping secrets in common, unencrypted configuration files, such as `.env` (outside of the git repository)
- Encrypting secrets in a GitOps or sealed secrets approach, with decryption key stored in a vault
- Storing secrets in a vault and distributing them through a secrets management service
- Generating dynamic secrets, through a complex secrets management infrastructure

## The problem of hardcoded secrets

### Are hardcoded secrets a vulnerability?

[OWASP](https://owasp.org), the Open Web Application Security Project foundation that works to improve the security of software, lists hardcoded secrets as one of its famous list of the [Top 10 Web Application Security Risks](https://owasp.org/Top10). The vulnerability ranked #2 in the latest edition published in 2021, under the [Cryptographic Failures (A02:2021)](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/) entry.

MITRE, famous for its [ATT&CK](https://attack.mitre.org) knowledge base of adversary tactics and techniques, also lists the use of hardcoded credentials in its [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/archive/2022/2022_cwe_top25.html). The vulnerability ranked #15 in the 2022 edition, under [CWE-798 âÂ Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html).

### What makes hardcoded secrets different?

Hardcoded secrets is a unique vulnerability in source code when compared to other vulnerabilities found through static or dynamic analysis. Regardless of whether the code is compiled and in runtime or not, hardcoded secrets represent a risk in themselves. Attackers who gain initial access to a repository can traverse all its branches and commit history to look for valid secrets. It does not matter if a secret is found on the deployed main branch or a short-lived bugfix branch, as long as it is valid and gives access to a resource (e.g. a server, a database, a third-party API).

### Secrets sprawl is a pervasive problem

Developers write code with the best of intentions, but they still end up compromising credentials and sensitive data. With 6 million secrets exposed on public GitHub in 2021 and a lot more in the private repositories, our research in the [State of Secrets Sprawl 2022 report](https://www.gitguardian.com/state-of-secrets-sprawl-report-2022) shows that this problem is much more common than developers and security engineers think.

## The solution: automated detection and remediation

Detecting secrets in source code is like finding needles in a haystack: there are a lot more sticks than there are needles, and you donât know how many needles might be in the haystack. In the case of secrets, you donât even know what all the needles look like!

A high-performing automated scanner will be able to achieve:

- A low number of false alerts raised. We call this **high precision**. Precision answers the question: "What is the percentage of the secrets that you detect that are actual secrets?". This question is legitimate, especially in a context where security teams have to deal with alert-fatigue.
- A low number of secrets missed. This is what we call **high recall**. Considering that a single undetected credential can have a big impact for an organization, some organizations prefer to triage more false alerts but make sure they donât miss a secret.

Balancing the equation to ensure that the algorithm captures as many secrets as possible without flagging too many false results is an intricate and extremely difficult challenge GitGuardian takes care of for its users. GitGuardian builds and maintains a secrets detection engine with more than 350 specific types of secrets covered in addition to support for generic and custom patterns.
