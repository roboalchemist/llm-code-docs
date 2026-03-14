# Source: https://docs.gitguardian.com/public-monitoring/remediate/remediation-overview.md

# Source: https://docs.gitguardian.com/internal-monitoring/remediate/remediation-overview.md

# Secret Remediation Overview

> GitGuardian's remediation philosophy and recommended six-step approach for addressing secret incidents while maintaining operational continuity.

## The GitGuardian Remediation Philosophy

At GitGuardian, we believe effective secret remediation requires a balanced approach that prioritizes security while maintaining operational continuity. Our philosophy centers on **informed decision-making** rather than panic-driven responses.

### Core Principles

1. **Assess before Acting** - Understand the full impact of a secret exposure before taking remediation steps
2. **Maintain Operations** - Ensure your systems remain functional throughout the remediation process
3. **Leverage Platform Insights** - Use GitGuardian's investigation tools and NHI governance data to make informed decisions
4. **Collaborate Effectively** - Involve the right stakeholders at the right time for efficient remediation

## Understanding Remediation Context

### Internal vs. External Incidents

**Internal incidents** occur within your monitored repositories and typically allow for more controlled remediation:
- You have full control over the codebase and deployment process
- You can coordinate with development teams for planned updates
- You can leverage Secrets Manager integrations for seamless transitions

**External incidents** (like public GitHub leaks) require faster response:
- The secret is potentially visible to attackers immediately
- Limited control over all copies of the exposed secret
- May require emergency revocation procedures

### Impact Assessment Framework

Before beginning remediation, evaluate:

- **Scope of Access**: What resources does this secret protect?
- **Privilege Level**: Can this secret access sensitive data or critical systems?
- **Usage Patterns**: How frequently is this secret used? By which services?
- **Blast Radius**: What would happen if we revoke this secret immediately?

GitGuardian provides insights through:
- [Incident investigation tools](./investigate-incidents.md)
- [NHI governance mapping](/nhi-governance/discover-your-nhis#exploration-map)
- Historical usage patterns and context

## The GitGuardian Remediation Approach

Our recommended methodology follows a **secure-first approach** that ensures operational continuity while implementing proper secret management:

### 1. Assess before acting
- Review the secret's scope and privileges
- Identify dependent systems and services
- Understand potential operational impact of revocation

### 2. Secure Storage
- Store the secret properly in a secret manager or secure vault
- Use GitGuardian's [push-to-vault feature](#secrets-manager-integrations) when available
- Ensure proper access controls and rotation policies

### 3. Update Code
- Modify applications to retrieve secrets from secure storage
- Update deployment configurations and environment variables
- Implement proper secret management practices

### 4. Test & Deploy
- Perform thorough non-regression testing
- Deploy changes to production environments
- Monitor applications to ensure proper functionality

### 5. Rotate & Revoke
- Generate new credentials through the appropriate service
- Update the new credentials in your secret manager
- Revoke the compromised secret to prevent unauthorized access

### 6. Monitor & Verify
- Check access logs for signs of unauthorized usage
- Verify that all dependent systems are functioning properly
- Document the incident and lessons learned

## Platform Capabilities for Remediation

### Secrets Manager Integrations

GitGuardian integrates with popular secret managers through **[ggscout](/ggscout-docs/home)**:
- **Push-to-vault**: Seamlessly move exposed secrets to secure storage
- **Synchronization**: Keep track of secrets across multiple managers
- **Automated workflows**: Streamline the secure storage process

[Learn more about Secrets Manager integrations](../integrate-sources/secrets-managers-integrations/overview.md)

### Revocation Features

For supported secret types, GitGuardian can help with:
- **Automated revocation**: Direct integration with service providers
- **Guided revocation**: Step-by-step instructions for manual processes
- **Revocation verification**: Confirmation that credentials have been properly disabled

### Collaboration Tools

Effective remediation often requires team coordination:
- **Incident sharing**: Grant access to relevant stakeholders
- **Feedback collection**: Gather input from developers and security teams
- **Assignment and tracking**: Ensure accountability and progress monitoring

[Learn more about collaboration features](../../platform/collaboration-and-sharing/incident-permissions-and-sharing.md)

## Choosing Your Remediation Approach

Different situations require different approaches. The key is matching your response to the specific circumstances:

### By incident type
- **Real-time incidents**: Engage with developers while context is fresh
- **Historical incidents**: Systematic investigation and prioritization required  
- **Public exposures**: Balance urgency with proper assessment
- **Bulk remediation**: Coordinate across teams with structured processes

### By risk level
- **Critical secrets**: May require emergency response procedures
- **Standard secrets**: Follow the secure-first approach
- **Low-risk secrets**: Can often be handled through standard processes

### By organizational context
- **Single team**: Direct developer engagement possible
- **Multiple teams**: Coordination and communication essential
- **Large scale**: Structured processes and automation needed

## Next Steps

Ready to start remediating? Choose the guide that fits your situation:

- **[Remediation Scenarios](./remediation-scenarios/overview.md)** - Comprehensive workflows for different situations
- **[Investigation Guide](./investigate-incidents.md)** - Thorough assessment techniques
- **[Platform Features](./remediate-incidents.md)** - GitGuardian tools for collaboration and automation
- **[Prioritization Guide](./prioritize-incidents.md)** - Focus on the most important incidents first

> **Remember**: Effective remediation is about making informed decisions, not just moving quickly. Take the time to understand the impact and choose the right approach for your specific situation.
