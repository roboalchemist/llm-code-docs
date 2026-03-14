# Source: https://docs.statsig.com/access-management/scim/concepts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM Concepts

<br />

Our SCIM implementation represents both Statsig users at the Organization level and
Project level with their associated roles. There are two major resources in our SCIM
implementation: Users and Groups.

## Users

Users in SCIM correspond to Statsig users at the Organization level.
Users that are part of the Statsig Organization and have the organization email domain will be recognized as SCIM users.
Each user has the following attributes:

* First name
* Last name
* Email address (main identifier, must be unique within the IdP)
* Statsig ID (used by the IDP to identify the user in the Statsig SCIM API)

## Groups

Groups in SCIM represent Statsig Projects with specific roles.
For example, a Project named "Project A" with a role of "Admin" would be represented as a group in SCIM.
The group name for this example project would be `Statsig-ProjectA-Admin`.

### Team x Role Groups

Team x Role Groups are a special type of group that represent Statsig Teams with specific roles.
For example, a Team named "Team A" with a role of "Admin" would be represented as a group in SCIM.
The group name for this example team would be `Statsig-ProjectName-TeamA-Admin`.

Important notes about groups:

* We do not allow project level deletion via SCIM, we do support team level deletion.
* We currently do not support updating group names via SCIM.

### General Mapping Between SCIM and Statsig

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/okta-statsig-group.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=4973eb6281f7c2b4d9178b23d4a99e09" alt="Mapping diagram showing Okta group synced to Statsig project and team roles via SCIM" width="1680" height="1180" data-path="images/okta_scim_steps/okta-statsig-group.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).