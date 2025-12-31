# Source: https://docs.replit.com/replitai/connectors-for-organizations.md

# Connectors for Organizations

> Centralize and manage app connectors across Teams and Enterprise Workspaces with admin controls, scoped permissions, and auditability.

Connectors for Organizations bring centralized, admin-managed connections to Teams and Enterprise Workspaces.

## Overview

Connectors in Teams and Enterprise accounts allow admins to set up and manage connections once, then make them available to apps across the organization. This removes repetitive setup for builders, improves security for IT, and standardizes access to tools like Notion, GitHub, Google, Outlook, Dropbox, Salesforce, and more.

## Key capabilities

* Centralized management: Admin setup and approval for organization-wide connections
* Role-based access controls: Enforce scoped, least-privilege permissions
* Visibility and auditability: Track which apps use which services
* Bring your own OAuth: Use organization-owned OAuth clients with custom scopes
* Bring your own OAuth (BYO OAuth): Use organization-owned OAuth clients with custom scopes \[Enterprise organizations only]
* Per-app consent and easy revocation

## How it works

1. Admin sets up a service once using organization credentials
2. Admin approves which teams can use the connector
3. Members build with that service by asking Agent
4. Admins can monitor which members and apps use which services

## Security and governance

* Scoped access with least-privilege permissions
* Credentials and tokens managed by the platform, not individual apps
* Centralized revocation and rotation without code changes

## Setup and management

1. Enable new connectors for the organization
   1. Navigate to the "Integrations" page from your organization’s home page
   2. Click "Enable new connector" in the top right
   3. Select the service you want to enable for your organization
   4. Enable the connector using default configs
   * Enterprise only: Create an OAuth connector using custom configs (for example, Drive scopes `.../auth/drive.file`, `.../auth/drive.install`)
   5. Click "Submit"

2. Configure RBAC
   1. After enabling a connector, click "Manage"
   2. Grant access to a specific group

3. Modify connectors
   * After enabling a connector, click "Manage"
   * Deleting a connector removes connections for all users in the organization
   * Edit the scopes of a custom connector as needed

## Plan controls

* Only Enterprise organizations can create custom OAuth clients; Teams are restricted to Replit defaults
* Only Enterprise organizations can set access controls on API keys; on Teams, API keys are available to all Members and Admins

## Roadmap

We are expanding Connectors for Organizations to support:

* Databases and warehouses as connector types
* Webhook events for event-driven workflows
* Deeper admin experience with permissions, assignments, and analytics
