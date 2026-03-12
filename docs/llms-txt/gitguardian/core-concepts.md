# Source: https://docs.gitguardian.com/public-monitoring/core-concepts.md

# Source: https://docs.gitguardian.com/nhi-governance/core-concepts.md

# Source: https://docs.gitguardian.com/honeytoken/core-concepts.md

# Core concepts

> Introduces honeytokens as decoy credentials that detect unauthorized access, with use cases and recommended placement strategies.

See how Honeytoken works in this brief video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ASOJzMQ82_I?controls=0&modestbranding=1&watchlater=0" title="YouTube video player" frameBorder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>

## What are honeytokens?

GitGuardian Honeytoken allows you to create decoy credentials called âhoneytokensâ that do not allow any access to any actual customer resources or data. Instead, they act as tripwires that reveal information about the attacker (eg. IP Address, User Agent, Location, etc.).

Our honeytokens look just like any other secret to attackers. We designed our honeytokens to be triggered by all types of secret scanners, like open-source projects TruffleHog or Gitleaks, that are often put to wrong use by attackers. This means that if a hacker uses a secret scanner to search for developer secrets, they will trip on the honeytoken, triggering an alert that notifies the security team of a potential security incident.

## Why should you use honeytokens?

Honeytokens are a useful tool for the software development life cycle (SDLC) and software supply chain for several reasons:

1. **An essential function in secrets remediation:** Honeytoken serves as the initial line of defense for users grappling with thousands of secrets incidents. It functions as an alarm system. It provides reassurance and buys valuable time when addressing secrets incidents at scale. Moreover, it acts as a prioritization tool, directing focus to critical incidents, when triggered.
2. **Early detection of security breaches**: By planting honeytokens in your SDLC system and supply chain, you can detect security breaches early on before they cause any real damage. Honeytokens can act as an alarm system that signals the presence of an attacker or malicious activity.
3. **Strengthened supply chain security**: Honeytokens can be used to quickly detect any breaches and identify if a vendor in the supply chain has been compromised. This helps you to strengthen your supply chain security and prevent further damage from occurring.
4. **Complete visibility of monitored codebase**: Honeytokens provide you with a clear view of where they have been deployed, ensuring they were deployed as intended and identifying if they were mistakenly duplicated in several repositories.
5. **Easy deployment at scale**: Honeytokens can be created, deployed, and managed on a large enterprise scale, allowing you to secure thousands of code repositories simultaneously. The integration of Honeytoken in the GitGuardian code security platform ensures that our secret scanning does not generate useless alerts for the deployed honeytokens.
6. **Detection of code leakage**: By placing our honeytokens in code, you can detect if it has been leaked on public GitHub, saving time and resources by providing an easy and quick way to detect code leakage and prevent further data loss.

Read this [blog post](https://blog.gitguardian.com/gitguardian-honeytoken) to learn more about the use cases of our honeytokens.

## Where should you place your honeytokens?

Our honeytokens are tailor-made for deployment in **Version Control Systems (git repositories).** Git repositories are your treasure troves, packed with valuable code essential for your software's functionality. If unauthorized access occurs, it could lead to code theft, tampering, or disruption of your operations.Deploy in all your repositories to detect when your codebase is compromised. Check our detailed [guide](https://blog.gitguardian.com/how-to-secure-your-scm-repositories-with-gitguardian-honeytokens).

Additionally, leverage honeytokens in other critical areas (where your real secrets might be found). Here are some examples:

- Insert them into **[CI/CD tools](https://blog.gitguardian.com/how-to-add-gitguardian-honeytokens-in-ci-cd-pipelines/)** to detect compromised pipelines.
- Plant them in **[Docker images](https://blog.gitguardian.com/how-to-secure-your-container-registries-with-gitguardians-honeytoken/)** or other **internal packages**.
- Place them in [project management tools](https://blog.gitguardian.com/secure-your-productivity-tools-with-gitguardian-honeytoken/) likeÂ **Jira**, internal wikis likeÂ **Confluence**, or messaging tools likeÂ **Slack**.

:::tip

We recommend that each honeytoken be deployed in a unique place. If it appears in several places, then if it gets triggered, you would not be able to identify for sure which place is compromised.

:::
