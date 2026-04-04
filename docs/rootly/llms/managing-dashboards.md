# Source: https://docs.rootly.com/metrics/managing-dashboards.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Dashboards

> Create, customize, share, and operationalize dashboards to understand incident performance across your organization.

Dashboards are where operational data becomes decision-making context.

In Rootly, dashboards allow you to transform raw incident data into structured, visual insights across teams, services, severities, time periods, and operational layers. Whether you're tracking executive-level reliability metrics or drilling into team-level performance, dashboards give you flexible control over how performance is measured and communicated.

You can access dashboards by navigating to **Metrics**.

***

# Overview

Every dashboard in Rootly is defined by three core dimensions:

1. **Ownership** — who controls it
2. **Permissions** — who can modify or manage it
3. **Visibility** — who can access it (internally or publicly)

Understanding these dimensions helps you design dashboards intentionally — not just visually, but operationally.

***

# Dashboard Ownership & Visibility

## Ownership Types

Dashboards are owned either by a **user** or by the **organization**.

### Personal Dashboards

Personal dashboards are owned by an individual user.

They are ideal for:

* Exploratory analysis
* Individual reporting workflows
* Temporary or experimental views
* Personal operational tracking

By default:

* You are the **Manager**
* No one else has access unless explicitly shared

***

### Organization Dashboards

Organization dashboards are owned at the team level.

They are appropriate when:

* Multiple teams rely on the same metrics
* Dashboards support recurring reporting (weekly reviews, exec syncs)
* Standardized views are required across departments

Organization dashboards can be shared broadly across your Rootly account.

***

## Public Dashboards

Any dashboard (Personal or Organization) can optionally be made **Public**.

When public access is enabled:

* A view-only link is generated
* Authentication is not required
* External stakeholders can access performance data

<Callout icon="sparkles" color="#7748F6">
  **Public access is a visibility layer — not ownership**

  Public dashboards do not change who manages or edits the dashboard. They simply allow view-only access via a shareable link.
</Callout>

<Callout icon="eye-slash" color="#FFC107">
  **Public dashboards may be disabled**

  Some organizations disable public dashboard access. If you do not see the public toggle, contact your administrator.
</Callout>

***

# Creating a Dashboard

To create a new dashboard:

1. Navigate to **Metrics**
2. Click **+ Create Dashboard**
3. Configure the dashboard settings

Dashboards are designed to be flexible but opinionated — providing sensible defaults while allowing advanced customization.

***

## Configuration Options

When creating a dashboard, you can define:

* **Name** (must be unique within your organization)
* **Description**
* **Icon**
* **Color theme**
* **Date range**
* **Period grouping**
* **Auto-refresh behavior**

### Default Values

If you create a dashboard without customizing every field, Rootly applies the following defaults:

* Icon: 📊
* Date range: **Last 30 Days**
* Period: **Day**
* Auto-refresh: **Disabled**
* Color: Randomly selected from the supported palette

<Callout icon="palette" color="#FFFFFF">
  **Color system**

  Dashboard colors are selected from a predefined palette to ensure visual consistency across your organization.
</Callout>

***

## Period Grouping

Metrics can be grouped by:

* Day
* Week
* Month
* Quarter
* Year

Choosing the correct period grouping is not cosmetic — it affects how trends are interpreted.

For example:

* **Day** is useful for short-term incident spikes
* **Month or Quarter** is better for leadership-level reporting

***

# Personalizing Dashboard Views

Each user can personalize how they view a dashboard — without affecting other users.

You can adjust:

* Date range
* Period grouping
* Team filters
* Service filters

These preferences are saved **per user, per dashboard**.

<Callout icon="user-cog" color="#7748F6">
  **View preferences are private**

  Changing filters or date ranges does not modify the dashboard globally. Other viewers will not see your changes.
</Callout>

***

# Sharing & Permissions

To share a dashboard:

1. Open the dashboard
2. Click **Share**
3. Assign permission levels

## Permission Levels

Permissions are hierarchical:

* **Viewer**
  * Can view data only

* **Editor**
  * Can view and modify panels
  * Inherits Viewer permissions

* **Manager**
  * Can view, edit, share, and delete
  * Inherits Editor permissions

<Callout icon="shield-check" color="#FFC107">
  **Permission hierarchy matters**

  Editors automatically inherit Viewer permissions. Managers inherit both Viewer and Editor capabilities.
</Callout>

***

# Setting a Default Dashboard

You can designate one dashboard as your default.

This dashboard will automatically open when navigating to **Metrics**.

To set a default:

1. Open the dashboard
2. Click **⋯**
3. Select **Set default**

<Note>
  You can only have one default dashboard per team. Setting a new default replaces the previous one.
</Note>

***

# Duplicating Dashboards

Duplicating a dashboard is useful when:

* Creating team-specific variants
* Running quarterly comparisons
* Testing new panel configurations safely

To duplicate:

1. Open the dashboard
2. Click **⋯**
3. Select **Duplicate**

Duplicated dashboards:

* Include all panels and configurations
* Are created as **Personal dashboards**
* Do not inherit sharing permissions
* Are automatically renamed with a date suffix

***

# Exporting Dashboards & Panels

Dashboards and panels can be exported for reporting and distribution.

## Entire Dashboard

* **PDF export**

## Individual Panels

From the panel menu:

* CSV
* JSON
* PDF
* PNG (charts only)
* JPG (charts only)

Exports allow teams to distribute insights outside of Rootly while preserving data fidelity.

***

# Auto-Refresh Behavior

Dashboards support auto-refresh, but data is cached.

<Callout icon="clock" color="#7748F6">
  **Auto-refresh is not real-time**

  Changes to underlying data may take 15–20 minutes to appear due to caching layers and refresh intervals.
</Callout>

***

# Deleting Dashboards

To delete:

1. Navigate to **Metrics**
2. Open the **⋯** menu
3. Select **Delete**

<Callout icon="triangle-exclamation" color="#FFC107">
  **Deletion is not user-recoverable**

  Dashboards use soft deletion internally, but there is no self-serve recovery mechanism. Duplicate important dashboards before deleting.
</Callout>

***

# Best Practices

Designing dashboards is not just about metrics — it’s about operational clarity.

## 1. Separate Strategic vs Tactical Dashboards

* Tactical dashboards: Short date ranges, high granularity
* Strategic dashboards: Monthly or quarterly grouping

Avoid mixing both purposes in one dashboard.

***

## 2. Limit Panel Density

Too many panels reduce clarity.

Instead:

* Create multiple focused dashboards
* Duplicate and specialize dashboards
* Use descriptive naming conventions

Example:

* 🚨 Critical Incidents — Last 30 Days
* 📈 Reliability Trends — Quarterly

***

## 3. Use Organization Dashboards for Standardization

If a dashboard is referenced in:

* Weekly reviews
* Executive reporting
* Post-incident retros

It should likely be an **Organization dashboard**.

***

## 4. Configure Public Links Intentionally

Public dashboards are powerful, but:

* Ensure sensitive data is not exposed
* Confirm intended filters are applied
* Validate before distributing externally

***

# Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Why must dashboard names be unique?" icon="fingerprint">
    Dashboard names must be unique within your organization (excluding deleted dashboards) to prevent confusion and maintain clarity in shared environments.

    If you receive a validation error, simply choose a different name.
  </Accordion>

  <Accordion title="Can I restrict who edits panels but still allow viewing?" icon="user-lock">
    Yes. Assign users as **Viewers** to grant read-only access.

    Only Editors and Managers can modify panel configurations.
  </Accordion>

  <Accordion title="Does duplicating copy sharing permissions?" icon="copy">
    No. Duplicated dashboards start as Personal dashboards owned by the duplicating user.

    Sharing must be configured separately.
  </Accordion>

  <Accordion title="How many default dashboards can I have?" icon="house">
    You can have one default dashboard per team context. Setting a new default replaces the previous one.
  </Accordion>

  <Accordion title="What happens if I enable auto-refresh?" icon="rotate">
    The dashboard will refresh automatically at set intervals, but underlying data may still be subject to caching delays (up to \~15–20 minutes).
  </Accordion>
</AccordionGroup>

***

Dashboards are most effective when they reflect how your organization thinks about reliability. Design them intentionally, share them responsibly, and revisit them periodically as your operational maturity evolves.


Built with [Mintlify](https://mintlify.com).