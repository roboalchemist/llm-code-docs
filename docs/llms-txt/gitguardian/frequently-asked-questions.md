# Source: https://docs.gitguardian.com/honeytoken/frequently-asked-questions.md

# Frequently Asked Questions

> Common questions about GitGuardian honeytokens, including how they differ from honeypots, supported types, and deployment best practices.

### What is the difference between a honeytoken and a traditional honeypot?

A honeypot is a decoy system or network that is set up to simulate vulnerabilities, lure attackers, and detect or deflect their malicious activities. It's a trap that is designed to deceive attackers and redirect them away from the actual network. The honeypot can be a physical or virtual system, and it can be set up with vulnerable applications or services to attract attackers. The goal of a honeypot is to identify and study attackers' tactics, techniques, and procedures (TTPs) to help organizations better defend against real attacks.

On the other hand, **a honeytoken is a piece of dummy credential that is deliberately placed in your SDLC to detect unauthorized access or malicious activity**. The goal of honeytokens is to provide an early warning of an attack, indicating that an attacker has gained access to the system or is attempting to access the false credential.

Honeytokens do offer some unique benefits over traditional honeypots:

1. **Precision**: Honeytokens are highly precise. They can be deployed with specific and customized information, such as a unique username or a fake file name, which makes it easier to detect exactly what is being targeted. Traditional honeypots, on the other hand, require attackers to engage with a broader system, making it more difficult to pinpoint the specific vulnerability that is being exploited.
2. **Simplicity**: Honeytokens are relatively simple to implement and maintain. They require fewer resources to deploy and monitor than traditional honeypots, which can be time-consuming and costly to set up and maintain.
3. **Scalability**: Honeytokens can be easily scaled to different parts of an organizationâs supply chain, allowing them to be deployed more broadly and monitored more effectively. Traditional honeypots can be more difficult to scale, as they require more resources and may not be as precise as honeytokens.
4. **Early detection**: Honeytokens can help organizations detect attacks earlier in the attack lifecycle. Since honeytokens are designed to detect unauthorized access attempts, they can alert organizations to potential security breaches before attackers are able to execute their attacks fully.

Overall, honeytokens are a useful addition to an organization's security toolkit, as they offer specific benefits that traditional honeypots may not provide.

### Is it easy for an attacker to recognize a honeytoken?

To automate their attacks, attackers often use secrets scanning tools that can quickly scan and identify secrets in a system. It's highly unlikely that an attacker would inspect each secret manually, as this would be an extremely time-consuming and inefficient process.

It can be difficult for an attacker to recognize a honeytoken like a dummy AWS credential if it is properly implemented and hidden within a system. Since we are using actual AWS keys as honeytokens, attackers have no way of discovering them.

### How are honeytokens triggered?

When an attacker tries to use a honeytoken, the login attempt is logged in AWS, giving us detailed information about the attack. This triggers an alert in GitGuardian's system, letting you know that someone has accessed the honeytoken along with valuable info about the attack.

### Why should you choose the GitGuardian Honeytoken SaaS version instead of using open-source projects?

GitGuardian's Honeytoken SaaS version offers a number of benefits over open-source alternatives. For example, GitGuardian offers a more user-friendly interface and dashboard for easy honeytoken management. You can also monitor their deployment, in particular in the codebase, thanks to the synergy with our Secret Detection capabilities.

GitGuardian's Honeytoken is specifically designed to detect code leakage by instantly alerting you if a honeytoken you've placed in your code is found on public GitHub. Our solution creates easily recognizable events that tag exposed honeytokens as "Publicly Exposed," so you can quickly identify which repo and honeytoken have been compromised and take swift action to safeguard your sensitive data. This ability sets GitGuardian apart from its competitors.

It is much easier to roll out the solution. You donât have to spend time and effort on installation. You can also get expert support and guidance from the GitGuardian team.
