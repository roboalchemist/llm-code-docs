# Source: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/llms.txt

# Wickr Enterprise Administration Guide

> This is administration documentation for Wickr Enterprise. This Administration Guide describes Wickr Enterprise concepts, and provides instructions on using the various features with both the console and the command line interface.

- [What is Wickr Enterprise?](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/what-is-wickr.html)
- [Getting started](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/getting-started.html)
- [Document history](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/doc-history.html)

## [Super administrator](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/super-administrator.html)

- [Administrator provisioning](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/admin-provisioning.html): Once logged into the super administration panel, you can create network administrators.
- [Network provisioning](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/network-provisioning.html): Once you've created administrators, you can create networks.
- [SSO configuration](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/configuration.html): SSO configuration allows a super administrator to add SSO authentication to a network administrator sign in.
- [Manage Room Bot](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/room-bot.html): The Room Bot allows network administrators to deploy pre-created rooms managed by this bot.
- [Crash report](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/crash-report.html): Super administrators can generate crash reports in case of failures.
- [Lockout](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/lockout.html): Super administrators can unlock network administrator accounts after unsuccessful login attempts on the Lockout tab.
- [Role Based Access Control](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/roles.html): Roles are a group of permissions that can be assigned to a member or an admin by a super administrator.

### [Global Federation](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/global-federation.html)

Global Federation (GF) allows Wickr Enterprise to communicate with other Enterprise deployments as well as Wickr Pro, AWS Wickr, and guest users.

- [Regional domains](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/regional-domains.html): Allow list the following domains to ensure your Wickr network functions correctly.
- [Multitenant Domain Visibility](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/multitenant-domain-visibility.html): Super administrators can hide local domains from lower-level administrators.
- [Self-Signed Certificates](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/self-signed-certificates.html): Super administrators can add self-signed/untrusted certificates in the Wickr admin panel to allow federation between Wickr Enterprise environments.
- [Settings](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/settings.html): Super administrators can allow private IPs for Enterprise deployment (SSO configuration).
- [API access tokens](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/api-token.html): Super administrators can generate an API token that has access to any network and security group within the Enterprise deployment.
- [Appearance](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/appearance.html): Super administrators can manage and customize the appearance of Wickr for their network.


## [Network administrator](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/network-admin.html)

- [Account settings](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/account-settings.html): In the My Account section of the Network administrator console, you can change your first and last names, change your password, or enable 2 Factor Authentication.

### [Dashboard](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/dashboard.html)

Once credentials have been made for a network Administrator, they can login using the same URL as the super administrator.

- [Analytics dashboard](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/analytics-dashboard.html): You can use the analytics dashboard to view how your organization is utilizing Wickr.

### [User](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/user.html)

In the Users section of the Wickr Network Administrator Console, you can view current Wickr users and bots, and modify their details.

### [Team directory](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/directory.html)

If SSO is not enabled on the network, network admins can create individual users.

- [Invite administrators](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/invite-administrators.html): Network administrators can add an existing administrator to a network they manage.
- [Accept network invites](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/network-invites.html): Network administrators can view their invites in the Network drop-down on the upper left of the page.
- [Bulk delete/suspend user](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/bulk-delete-suspend.html): You can bulk delete and bulk suspend Wickr network users in the User section of the Wickr Admin Console for Wickr.
- [Bot management](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/bot-management.html): An administrator can:
- [Guest users](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/guest-users.html): Learn how to enable guest users for your AWS Wickr network.
- [Compliance bot (Data retention)](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/data-retention.html): The data retention service uses the Compliance bot, which is an additional service available within Wickr Enterprise.

### [Network settings](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/network-settings.html)

In the Network Settings section of the Wickr Network Administrator Console, Wickr network name, security groups, and SSO configuration.

- [Network profile](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/network-profile.html): An Administrator can set the name of the network, which is visible to all users within it, and also view the Network ID.

### [Security group](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/security-group.html)

Learn the functions of security groups.

- [General](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/general.html): The General section has the following available options:
- [Messaging](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/messaging.html): The Messaging section has the following available features for users:
- [Calling](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/calling.html): The Calling section has the following available features for users:
- [Security](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/security.html): The Security section has the following available options for administration:
- [Push configuration](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/push-configuration.html): The Push Configuration section has available options for proxy or intermediary networking devices.
- [Federation](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/federation.html): The Federation section has available options for communications internal to the Enterprise deployment and external communications with other Wickr Enterprise, or guest users.
- [Migration to disable certificate pinning](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/disable-certificate-pinning.html)
- [SSO configuration](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/sso-configuration.html): SSO configuration allows an administrator to add SSO authentication to a specific network.
- [Event logging](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/event-logging.html): Event logging changes the default verbosity level for several backend services.
- [Security tags](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/security-tags.html): Security tags are used to classify and organize users to prevent information leakage between classified and unclassified systems.

### [Client configuration](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/client-configuration.html)

Config file or deeplinks created on the Client Configuration screen are the second most important thing an end user needs to successfully register and use Wickr Enterprise.

- [Create a configuration file](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/create-config.html): You can create a new configuration file.
- [Certificate pinning](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/certificate-pinning.html): Certificate pinning is an online application security technique that accepts only authorized pinned certificates for authentication of client-server connections.
- [Wickr Open Access (WOA) configuration](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/wickr-open-access.html): Wickr Open Access (WOA) is an additional layer of network obfuscation that uses various connection methods deployed through our external partner.
- [Default rooms](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/default-rooms.html): When the super administrator has enabled the default room option, network administrators can create rooms managed by a bot.
- [API access](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/api-access.html): An Administrator is able to manage API Tokens.
- [Read receipts](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/read-receipts.html): Read receipts on Wickr are notifications sent to the sender to show when their message has been read.
- [File management](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/file-management.html): Enterprise users can begin to take advantage of the File management feature.
- [Custom TCP calling port](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/custom-tcp-calling-port.html): Learn how to prevent collision when deploying Wickr Enterprise in Low Resource Mode.


## [Data retention](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/data-retention-compliance.html)

- [Installation](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/installation.html): The Wickr Enterprise Compliance Service requires the Wickr IO platform as it is now an integration within that framework.
- [Initial network configuration](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/initial-network-configuration.html): Once the bot-enterprise container is running and have a working deployment of Wickr Enterprise you can begin adding a bot user and completing the setup process.
- [Compliance data location](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/compliance-data-location.html): The compliance bot will save messages and output by default to the following:
- [Compliance container upgrades](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/compliance-container-upgrades.html): If already running the compliance bot within a container, the upgrade process is very simple and will not result in any downtime.
- [Appendix A: Compliance message description](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/compliance-message-description.html): The following table contains a list of JSON fields that will be found in the messages that the compliance bot streams to the received messages file.
- [Appendix B: Compliance output examples](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/compliance-output-examples.html): The following are compliance output examples for different types of messages.


## [Release notes](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/release-notes.html)

### [Infrastructure release notes](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes.html)

Learn about the ongoing updates and improvements to Wickr Enterprise infrastructures with release notes.

- [Infrastructure 6.20](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.20.html): The following release notes include information for infrastructure release 6.20.
- [Infrastructure 6.22](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.22.html): The following release notes include information for infrastructure release 6.22.
- [Infrastructure 6.26](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.26.html): The following release notes include information for infrastructure release 6.26.
- [Infrastructure 6.28](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.28.html): The following release notes include information for infrastructure release 6.28.
- [Infrastructure 6.32](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.32.html): The following release notes include information for infrastructure release 6.32.
- [Infrastructure 6.34](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.34.html): The following release notes include information for infrastructure release 6.34.
- [Infrastructure 6.36](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.36.html): The following release notes include information for infrastructure release 6.36.
- [Infrastructure 6.38](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.38.html): The following release notes include information for infrastructure release 6.38.
- [Infrastructure 6.40](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.40.html): The following release notes include information for infrastructure release 6.40.
- [Infrastructure 6.42](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.42.html): The following release notes include information for infrastructure release 6.42.
- [Infrastructure 6.46](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.46.html): The following release notes include information for infrastructure release 6.46.
- [Infrastructure 6.48](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.48.html): The following release notes include information for infrastructure release 6.48.
- [Infrastructure 6.50](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.50.html): The following release notes include information for infrastructure release 6.50.
- [Infrastructure 6.52](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.52.html): The following release notes include information for infrastructure release 6.52.
- [Infrastructure 6.54](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.54.html): The following release notes include information for infrastructure release 6.54.
- [Infrastructure 6.56](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.56.html): The following release notes include information for infrastructure release 6.56.
- [Infrastructure 6.58](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.58.html): The following release notes include information for infrastructure release 6.58.
- [Infrastructure 6.62](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.62.html): The following release notes include information for infrastructure release 6.62.
- [Infrastructure 6.66](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/infra-release-notes-6.66.html): The following release notes include information for infrastructure release 6.66.

### [Clients release notes](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes.html)

Learn about the ongoing updates and improvements to Wickr Enterprise infrastructures with release notes.

- [Clients 6.22](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.22.html): The following release notes include information for clients release 6.22.
- [Clients 6.26](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.26.html): The following release notes include information for clients release 6.26.
- [Clients 6.28](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.28.html): The following release notes include information for clients release 6.28.
- [Clients 6.32](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.32.html): The following release notes include information for clients release 6.32.
- [Clients 6.34](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.34.html): The following release notes include information for clients release 6.34.
- [Clients 6.36](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.36.html): The following release notes include information for clients release 6.36.
- [Clients 6.38](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.38.html): The following release notes include information for clients release 6.38.
- [Clients 6.40](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.40.html): The following release notes include information for clients release 6.40.
- [Clients 6.42](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.42.html): The following release notes include information for clients release 6.42.
- [Clients 6.46](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.46.html): The following release notes include information for clients release 6.46.
- [Clients 6.48](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.48.html): The following release notes include information for clients release 6.48.
- [Clients 6.50](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.50.html): The following release notes include information for clients release 6.50.
- [Clients 6.52](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.52.html): The following release notes include information for clients release 6.52.
- [Clients 6.54](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.54.html): The following release notes include information for clients release 6.54.
- [Clients 6.56](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.56.html): The following release notes include information for clients release 6.56.
- [Clients 6.58](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.58.html): The following release notes include information for clients release 6.58.
- [Clients 6.62](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.62.html): The following release notes include information for clients release 6.62.
- [Clients 6.66](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/clients-release-notes-6.66.html): The following release notes include information for clients release 6.66.

### [Bots release notes](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/bots-release-notes.html)

Learn about the ongoing updates and improvements to Wickr Enterprise bots with release notes.

- [Bots 6.24](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/bots-release-notes-6.24.html): The following release notes include information for bots release 6.24.
- [Bots 6.32](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/bots-release-notes-6.32.html): The following release notes include information for bots release 6.32.
- [Bots 6.34](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/bots-release-notes-6.34.html): The following release notes include information for bots release 6.34.
