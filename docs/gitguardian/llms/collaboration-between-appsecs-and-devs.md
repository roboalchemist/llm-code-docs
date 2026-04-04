# Source: https://docs.gitguardian.com/internal-monitoring/core-concepts/collaboration-between-appsecs-and-devs.md

# Collaboration between Application Security and development teams

> Describes the Application Security Shared Responsibility Model and how GitGuardian enables collaboration between security and development teams.

## What is the AppSec Shared Responsibility Model?

Shared responsibility essentially means that security should be owned by various teams acting in collaboration to implement its various layers all along the SDLC:

- Developers are provided with access to the right tools to set up their guardrails and remediate the security issues theyâre the most familiar with, in context.
- Security engineers are responsible for defining and implementing security policies as well as their controls. Sharing responsibility means they can dedicate more time investigating complex or low-assurance findings.
- Platform/Ops can be tasked with ad-hoc responsibilities to make sure security CI/CD controls are correctly configured, or even to take ownership of certain types of vulnerabilities.

## Why do we need it?

Security can no longer be an afterthought or solely addressed once applications start running in production environments.

The everything-as-code approach or the collapse of the Software Development Lifecycle (SDLC) into Source Control Management (source code, CI/CD configurations, policy-as-code, infrastructure-as-code, documentation-as-code) has spawned a whole new range of attack vectors. In turn, this has led to a shift in the priorities of attackers from applications in runtime to the tools that make up the development environments and CI/CD pipelines.

Organizations can only mitigate such threats by addressing security continuously throughout the SDLC, with the help of the developers designing and authoring the code going to production. Our observations show that, on average, organizations run application security programs with one to two security engineers for every 100 developers. In such a configuration, the vulnerabilities introduced in source code outmatch the capacity of security teams to handle them.

Only an **Application Security Shared Responsibility Model**, where developers contribute their fair share, can scale in this new environment.

## How can GitGuardian help your organization achieve it?

### For AppSec teams

GitGuardian aims to:

- Provide AppSec teams with visibility and control over the SCM, DevOps tools and all other components of the SDLC.
- Ease the burden of remediation by pulling developers who own the context closer to the process.

### For development teams

GitGuardian aims to:

- Guide developers throughout the remediation process (feedback collection, steps to follow, etc.) and empower them to resolve incidents by themselves when possible.
- Equip developers with supportive tooling (command-line interface, SDKs, REST API) to implement security guardrails in the environments they are most familiar with.
