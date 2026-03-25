# Source: https://docs.gitguardian.com/nhi-governance/improve-your-posture.md

# Assess and improve your NHI security posture

> NHI Governance security policies to assess your posture, including checks for leaked, reused, duplicated, and long-lived secrets.

Our security policies are informed by the **[OWASP Top 10 for NHIs](https://owasp.org/www-project-non-human-identities-top-10/2025/)**, a comprehensive framework that highlights the most critical security risks they pose.

We support the following policies:

- **Publicly Leaked Secrets**: These are secrets that have been exposed publicly, identified through our public monitoring services. Such exposure can allow unauthorized parties to access sensitive systems, posing significant security threats.
- **Internally Leaked Secrets**: Secrets that have been inadvertently exposed within your internal perimeter can be detected through our private monitoring services. These internal leaks can be just as harmful as public ones, especially if internal defenses are breached.
- **Cross-Environment Secrets**: A secret that is found in multiple environments, like both production and staging, can risk exposing sensitive production-level access to less secure environments. Ensuring each environment has distinct secrets helps maintain security boundaries.
- **Reused Secrets**: When a secret is used by multiple entities, it increases the risk of compromise. If one entity is breached, others using the same secret can also be jeopardized. Ensuring unique secrets for each use case reduces this risk.
- **Duplicated Secrets**: Having the same secret stored in multiple vaults or paths can complicate management and increase the chance of using outdated or unrevoked credentials. It is crucial to maintain a single source of truth to manage secrets effectively.
- **Long-Lived Secrets**: Secrets that exist beyond a given lifespan (by default one year) without renewal are vulnerable to misuse. Regularly updating these secrets helps minimize the risk of prolonged exposure to potential threats.

In the inventory details, selecting a breach policy will visually highlight the locations of the issues on the exploration map.

![Breached Policies](/img/nhi-governance/breached-policies.png)

Note that new policies will be supported shortly.
