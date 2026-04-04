# Source: https://docs.gitguardian.com/platform/enterprise-administration/scripts-users-teams-sync.md

# User and Team mapping scripts

> Automate user and team management in GitGuardian using scripts and the API for bulk provisioning and synchronization.

## Overview

For efficient and secure user and team management, we **strongly recommend** configuring **SSO** and enabling **SCIM** on GitGuardian:

- **SSO:** Ensures secure access, user provisioning (via Just-In-Time (JIT)) and centralized management ([SAML SSO Configuration](./saml-sso-configuration)).
- **SCIM:** Automates user provisioning and deprovisioning ([SCIM Configuration](./scim-configuration)).

These features streamline integration with your identity provider and enhance overall efficiency.

However, for customers who prefer to map their team structures directly to their version control systems (VCS), such as GitHub and GitLab, we provide **User and Team Mapping Scripts**. These scripts automate user and team synchronization at scale, ensuring consistency across platforms while leveraging the GitGuardian API client library, [py-gitguardian](https://pypi.org/project/pygitguardian/). This solution caters to enterprise customers who require direct alignment between their VCS and GitGuardian environments.

## Key Features

### 1. **User and Team Mapping**

- **Mapping**: Automatically maps GitLab groups or GitHub teams, along with the repositories they own and the users associated with them, to GitGuardian Teams and their respective perimeters. For GitHub, this is achieved by leveraging IDP users when GitHub Enterprise Server is utilized, or alternatively, by analyzing the Organization members as a fallback. However, for Organization members, synchronization will be skipped if their email addresses are hidden by default, as these are required for mapping.
- **Platform Support**: GitHub, GitLab.
- **Automated User Management**: Invites new users and syncs memberships. Does not handle inactive users or their removalâ for this, please use [SCIM](./scim-configuration), which now supports both user provisioning and deprovisioning. For GitHub, the script only maps users who have an email address on their profile or if SAML is configured on GitHub with an Enterprise plan.

### 2. **Permission Handling**

- **Selective Permissions**: Excludes elevated roles (e.g., managers, owners) to prevent over-permissioning.

### 3. **Notifications**

- **Email Alerts**: Option to notify users of changes, invitations, or removal from teams.

### 4. **Logging and Error Handling**

- **Detailed Logs**: Tracks success, failure, and error details using the Python `logging` module.
- **Error Handling**: Provides graceful handling of API errors with appropriate logging.

### 5. **Scalability**

- **Large Dataset Support**: Handles large datasets (1000+ users and teams) with pagination.

### 6. **Customization**

- **Authentication**: Easily configurable using tokens for GitHub.
- **Script Modifications**: Designed for modularity, allowing easy customization to extend functionality.

## Getting Started

Refer to the repository's README file for detailed instructions on configuring and running the script for your platform:

- **GitHub**: [team-mapping-github-gitguardian](https://github.com/GitGuardian/ggtools/tree/main/team-mapping-github-gitguardian)
- **GitLab**: [team-mapping-gitlab-gitguardian](https://github.com/GitGuardian/ggtools/tree/main/team-mapping-gitlab-gitguardian)

## Support

For further assistance, reach out at [support@gitguardian.com](mailto:support@gitguardian.com).
