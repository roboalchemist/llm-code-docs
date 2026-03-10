# Source: https://docs.aws.amazon.com/securityagent/latest/userguide/llms.txt

# AWS Security Agent User Guide

- [What is AWS Security Agent?](https://docs.aws.amazon.com/securityagent/latest/userguide/what-is.html)
- [How AWS Security Agent works](https://docs.aws.amazon.com/securityagent/latest/userguide/how-it-works.html)
- [Quickstart: Run a penetration test](https://docs.aws.amazon.com/securityagent/latest/userguide/quickstart.html)
- [AWS Security Agent capabilities](https://docs.aws.amazon.com/securityagent/latest/userguide/agent-capabilities.html)
- [Log in to the AWS Security Agent Web App](https://docs.aws.amazon.com/securityagent/latest/userguide/login-web-app.html)
- [Understand the resource hierarchy and lifecycle](https://docs.aws.amazon.com/securityagent/latest/userguide/understand-lifecycle.html)
- [Review code security findings in GitHub](https://docs.aws.amazon.com/securityagent/latest/userguide/review-code-findings-github.html)
- [Service Quotas](https://docs.aws.amazon.com/securityagent/latest/userguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/securityagent/latest/userguide/doc-history.html)

## [Configure AWS Security Agent](https://docs.aws.amazon.com/securityagent/latest/userguide/setup-agent.html)

- [Set up AWS Security Agent](https://docs.aws.amazon.com/securityagent/latest/userguide/setup-security-agent.html): Configure AWS Security Agent for your organization by creating your first Agent Space and establishing how users will access the web application.
- [Create an Agent Space](https://docs.aws.amazon.com/securityagent/latest/userguide/create-agent-space.html): Create Agent Spaces to secure applications or projects in your organization.
- [Enable penetration test](https://docs.aws.amazon.com/securityagent/latest/userguide/enable-penetration-test.html): Configure AWS Security Agent to run autonomous penetration tests on your applications.
- [Enable code review capability for a GitHub repository](https://docs.aws.amazon.com/securityagent/latest/userguide/enable-code-review.html): Configure AWS Security Agent to automatically review pull requests in your connected GitHub repositories.
- [Manage security requirements](https://docs.aws.amazon.com/securityagent/latest/userguide/security-requirements.html): Configure security requirements that AWS Security Agent uses to analyze your applications during design reviews and code reviews.
- [Connect AWS Security Agent to GitHub repositories](https://docs.aws.amazon.com/securityagent/latest/userguide/connect-github.html): Connect your AWS Security Agent to GitHub repositories to enable code review and penetration testing capabilities.
- [Remove a GitHub integration](https://docs.aws.amazon.com/securityagent/latest/userguide/remove-github.html): Remove a GitHub integration when you no longer need AWS Security Agent to access repositories from a specific GitHub organization or user account.
- [Create an IAM Role for AWS Security Agent](https://docs.aws.amazon.com/securityagent/latest/userguide/create-iam-role.html): AWS Security Agent uses IAM Roles in three ways:
- [Connect agent to private VPC resources](https://docs.aws.amazon.com/securityagent/latest/userguide/connect-agent-vpc.html): If the application you want to run a penetration test on is not available on the public internet, you need to provide AWS Security Agent with a VPC configuration.
- [Enable users to start remediation of penetration test findings](https://docs.aws.amazon.com/securityagent/latest/userguide/enable-remediate-findings.html): In the AWS Management Console, you can enable the code remediation feature that allows users to remediate findings in the penetration test web app.
- [Provide agent resources from an S3 bucket](https://docs.aws.amazon.com/securityagent/latest/userguide/enable-s3-bucket.html): You can grant AWS Security Agent access to resources in an S3 bucket, such as API documents, threat model documents, and source code that support penetration testing.
- [Enable an application domain for penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/enable-test-domain.html): Before you can run a penetration test on an application, you need to add a target domain and verify ownership.
- [Grant users access to the AWS Security Agent web app](https://docs.aws.amazon.com/securityagent/latest/userguide/grant-user-access.html): AWS Security Agent provides two methods for users to access the web application, depending on how you configured your Agent Space during setup.
- [Troubleshooting](https://docs.aws.amazon.com/securityagent/latest/userguide/troubleshooting.html): Find solutions to commonly seen errors when using AWS Security Agent.


## [Create a design review](https://docs.aws.amazon.com/securityagent/latest/userguide/perform-design-review.html)

- [Review findings from a design review](https://docs.aws.amazon.com/securityagent/latest/userguide/review-design-findings.html): Review findings help you understand which security requirements are met, which need attention, and what actions to take to improve your designâs security posture before implementation begins.


## [Create a penetration test](https://docs.aws.amazon.com/securityagent/latest/userguide/perform-penetration-test.html)

- [Review findings from a penetration test](https://docs.aws.amazon.com/securityagent/latest/userguide/review-penetration-findings.html): Monitor pentest execution in real time on the Penetration Test Logs page after AWS Security Agent starts a pentest.
- [Provide authentication credentials for penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/provide-testing-credentials.html): Provide credentials to enable AWS Security Agent to test authenticated areas of your web applications.
- [Remediate a penetration test finding](https://docs.aws.amazon.com/securityagent/latest/userguide/remediate-finding.html): When viewing the findings for a penetration test, you can request AWS Security Agent attempt to remediate a finding.


## [Security](https://docs.aws.amazon.com/securityagent/latest/userguide/security.html)

- [Security Considerations](https://docs.aws.amazon.com/securityagent/latest/userguide/security-guidance.html): AWS Security Agent is a frontier agent that proactively secures your applications throughout the development lifecycle across all your environments.
- [AWS managed policies](https://docs.aws.amazon.com/securityagent/latest/userguide/security-iam-awsmanpol.html): An AWS managed policy is a standalone policy that is created and administered by AWS.
- [Data protection](https://docs.aws.amazon.com/securityagent/latest/userguide/data-protection.html): The AWS shared responsibility model applies to data protection in AWS Security Agent.

### [Identity and access management](https://docs.aws.amazon.com/securityagent/latest/userguide/security-iam.html)

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources.

- [How AWS Security Agent works with IAM](https://docs.aws.amazon.com/securityagent/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Security Agent, learn what IAM features are available to use with AWS Security Agent.
- [AWS Security Agent identity-based policy examples](https://docs.aws.amazon.com/securityagent/latest/userguide/security-iam-id-based-policy-examples.html): By default, IAM users and roles donât have permission to create or modify AWS Security Agent resources.
- [Troubleshooting AWS Security Agent identity and access](https://docs.aws.amazon.com/securityagent/latest/userguide/security-iam-troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Security Agent and IAM.
- [Incident response](https://docs.aws.amazon.com/securityagent/latest/userguide/incident-response.html): AWS Security Agent is a proactive security testing service designed to identify and prevent vulnerabilities before they can be exploited.
- [Compliance validation](https://docs.aws.amazon.com/securityagent/latest/userguide/compliance-validation.html): To learn whether an AWS service is within the scope of specific compliance programs, see AWS services in Scope by Compliance Program and choose the compliance program that you are interested in.
- [Resilience](https://docs.aws.amazon.com/securityagent/latest/userguide/resilience.html)
- [Infrastructure security](https://docs.aws.amazon.com/securityagent/latest/userguide/infrastructure-security.html): As a managed service, AWS Security Agent is protected by AWS global network security.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/securityagent/latest/userguide/configuration-vulnerability-analysis.html): Configuration and IT controls are a shared responsibility between AWS and you, our customer.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/securityagent/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesnât have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Security best practices](https://docs.aws.amazon.com/securityagent/latest/userguide/security-best-practices.html): AWS Security Agent provides a number of security features to consider as you develop and implement your own security policies.
- [IAM actions and resources migration](https://docs.aws.amazon.com/securityagent/latest/userguide/security-iam-migration.html): AWS Security Agent is a frontier agent that proactively secures your applications throughout the development lifecycle across all your environments.
