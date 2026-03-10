# Source: https://www.elastic.co/docs/deploy-manage/users-roles

﻿---
title: Users and roles
description: To prevent unauthorized access to your Elastic resources, you need a way to identify users and validate that a user is who they claim to be (authentication),...
url: https://www.elastic.co/docs/deploy-manage/users-roles
products:
  - Elastic Cloud Serverless
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Users and roles
To prevent unauthorized access to your Elastic resources, you need a way to identify users and validate that a user is who they claim to be (*authentication*), and control what data users can access and what tasks they can perform (*authorization*).
The methods that you use to authenticate users and control access depends on the way Elastic is deployed.
<note>
  Preventing unauthorized access is only one element of a complete security strategy. To secure your Elastic environment, you can also do the following:
  - Restrict the nodes and clients that can connect to the cluster using [network security](https://www.elastic.co/docs/deploy-manage/security/network-security) policies.
  - Take steps to maintain your data integrity and confidentiality by [encrypting HTTP and inter-node communications](https://www.elastic.co/docs/deploy-manage/security/secure-cluster-communications), as well as [encrypting your data at rest](https://www.elastic.co/docs/deploy-manage/security/data-security).
  - Maintain an [audit trail](https://www.elastic.co/docs/deploy-manage/security/logging-configuration/security-event-audit-logging) for security-related events.
  - Control access to dashboards and other saved objects in your UI using [Kibana spaces](https://www.elastic.co/docs/deploy-manage/manage-spaces).
  - Connect your cluster to a [remote cluster](https://www.elastic.co/docs/deploy-manage/remote-clusters) to enable cross-cluster replication and search.
  - Manage [API keys](https://www.elastic.co/docs/deploy-manage/api-keys) used for programmatic access to Elastic.
</note>


## Cloud organization level

<applies-to>
  - Elastic Cloud Serverless: Generally available
  - Elastic Cloud Hosted: Generally available
</applies-to>

If you’re using Elastic Cloud, then you can perform the following tasks to control access to your Cloud organization, your Cloud Hosted deployments, and your Cloud Serverless projects:
- [Invite users to join your organization](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-organization/manage-users)
- Assign [user roles and privileges](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-organization/user-roles):
  - Manage organization-level roles and high-level access to deployments and projects.
- Assign project-level roles and [create custom roles](https://www.elastic.co/docs/deploy-manage/users-roles/serverless-custom-roles). <applies-to>Elastic Cloud Hosted: Unavailable</applies-to>
- Configure [SAML single sign-on](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-organization/configure-saml-authentication) for your organization

<tip>
  For Elastic Cloud Hosted deployments, you can configure SSO at the organization level, the deployment level, or both. Refer to [Cloud organization users](/docs/deploy-manage/users-roles/cloud-organization#organization-deployment-sso) for more information.
</tip>

Elastic Cloud Hosted deployments can also use [cluster-level authentication and authorization](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth). Cluster-level auth features are not available for Elastic Cloud Serverless.
<admonition title="Granular data access control in Serverless">
  Elastic Cloud Serverless centralizes user management with [Cloud organization-level roles](/docs/deploy-manage/users-roles/cloud-organization/user-roles#ec_organization_level_roles). You can configure [document- and field-level access control](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/controlling-access-at-document-field-level) in Elastic Cloud Serverless projects as a part of a project-level custom role.
</admonition>


## Orchestrator level

<applies-to>
  - Elastic Cloud Enterprise: Generally available
</applies-to>

Control access to your Elastic Cloud Enterprise [orchestrator](https://www.elastic.co/docs/deploy-manage/deploy/cloud-enterprise/deploy-an-orchestrator) and deployments.
- [Manage passwords for default users](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-enterprise-orchestrator/manage-system-passwords)
- [Manage orchestrator users and roles](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-enterprise-orchestrator/manage-users-roles):
  - [Using native users](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-enterprise-orchestrator/native-user-authentication)
- By integrating with external authentication providers:
  - [Active Directory](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-enterprise-orchestrator/active-directory)
- [LDAP](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-enterprise-orchestrator/ldap)
- [SAML](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-enterprise-orchestrator/saml)
- [Configure single sign-on to deployments](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-enterprise-orchestrator/configure-sso-for-deployments) for orchestrator users
  <tip>
  For Elastic Cloud Enterprise deployments, you can configure SSO at the orchestrator level, the deployment level, or both.
  </tip>

Elastic Cloud Enterprise deployments can also use [cluster-level authentication and authorization](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth).
<note>
  You can't manage users and roles for Elastic Cloud on Kubernetes clusters at the orchestrator level. Elastic Cloud on Kubernetes deployments use cluster-level authentication and authorization only.
</note>


## Project level

<applies-to>
  - Elastic Cloud Serverless: Generally available
</applies-to>

As an extension of the [predefined cloud resource access roles](/docs/deploy-manage/users-roles/cloud-organization/user-roles#ec_instance_access_roles) offered for Serverless projects, you can create custom roles at the project level to provide more granular control, and provide users with only the access they need within specific projects. You can also use custom roles to apply [document and field-level security](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/controlling-access-at-document-field-level) at the project level.
[Learn more about custom roles for Elastic Cloud Serverless projects](https://www.elastic.co/docs/deploy-manage/users-roles/serverless-custom-roles).

## Cluster or deployment level

<applies-to>
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
</applies-to>

Set up authentication and authorization at the cluster or deployment level, and learn about the underlying security technologies that Elasticsearch uses to authenticate and authorize requests internally and across services.

### User authentication

Set up methods to identify users to the Elasticsearch cluster.
Key tasks for managing user authentication include:
- [Managing default users](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/built-in-users)
- [Managing users natively](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/native)
- [Integrating with external authentication providers](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/external-authentication)

You can also learn the basics of Elasticsearch authentication, learn about accounts used to communicate within an Elasticsearch cluster and across services, and perform advanced tasks.
[View all user authentication docs](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/user-authentication)

### User authorization

After a user is authenticated, use role-based access control to determine whether the user behind an incoming request is allowed to execute the request.
Key tasks for managing user authorization include:
- Assigning [built-in roles](https://www.elastic.co/docs/reference/elasticsearch/roles) or [defining your own](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/defining-roles)
- [Mapping users and groups to roles](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/mapping-users-groups-to-roles)
- [Setting up field- and document-level security](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/controlling-access-at-document-field-level)

You can also learn the basics of Elasticsearch authorization, and perform advanced tasks.
<tip>
  User roles are also used to control access to [Kibana spaces](https://www.elastic.co/docs/deploy-manage/manage-spaces).
</tip>

[View all user authorization docs](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/user-roles)