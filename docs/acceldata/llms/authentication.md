# Source: https://docs.acceldata.io/api/authentication.md

# Source: https://docs.acceldata.io/documentation/authentication.md

# Authentication

ADOC enforces platform-wide access control using **Role-Based Access Control (RBAC)**. This ensures that users can only access features they are explicitly permitted to use. Permissions are controlled through roles, which are assigned at both application and feature levels.

RBAC in ADOC applies to both the **Admin Central** and **Data Observability** applications, each of which includes its own set of features and supported roles.

## ADOC Applications

There are two core applications in ADOC where roles apply independently:

1. Admin Central
    1. Focuses on administrative and configuration functions.
    2. Accessible via the (settings) icon.
    3. Used to manage users, roles, authentication, and other platform-wide configurations.

2. Data Observability
    1. Contains all observability features—pipelines, alerts, reliability tools, policies, and lineage.
    2. Where most day-to-day monitoring and management activities take place.

## Role Types by Application

Each application supports a different set of roles:

- **Admin Central Roles**
- **Data Observability Roles**

Users may be assigned different roles for each application independently.

## Features, Categories & Permissions

Features are grouped into functional categories, such as:

- Administration
- Alerts
- Compute
- Reliability
- General
- Pipeline

Each feature can have one or more of the following permission levels:

- **Create** – Users can add new entities (e.g., a new asset, pipeline, or user).
- **Modify** – Users can update existing items.
- **View** – Users can only see the feature and its contents but cannot change anything.

## Viewing User Roles

To check the roles assigned to a user:

- Navigate to **User Management**.  Click on a specific user to open their **Detail View**.
- You’ll see their assigned roles for both **Admin Central** and **Data Observability**.
- Roles can be directly edited here by platform admins.

Note You can view the exact feature-wise permissions assigned to each role by navigating to the **Tenant Roles** or **Domain Roles** section in **User Management**. Permissions are grouped by feature category and shown with their corresponding **Create**, **Modify**, and **View** access.