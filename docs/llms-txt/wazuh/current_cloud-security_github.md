# Source: https://documentation.wazuh.com/current/cloud-security/github/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Monitoring GitHub

GitHub is a cloud-based platform that provides version control and collaboration tools for software development projects. It offers an API that enables developers to interact with it programmatically. GitHub provides an audit logging feature that records events as they occur within an organization. Organizations can leverage the audit log to track changes and monitor user activities, therefore enhancing transparency.

This section describes how to monitor GitHub audit logs for your organization. Wazuh can monitor the following GitHub activities:

- Access to your organization or repository settings.
- Changes in repository permissions.
- User addition or removal in an organization, repository, or team.
- Changes in members privilege.
- Changes to permissions of a GitHub App.
- Git events such as cloning, fetching, and pushing.

> ##### Contents
> 
> * [Monitoring GitHub audit logs](monitoring-github-activity.md)
>   * [Requirements for monitoring GitHub audit logs](monitoring-github-activity.md#requirements-for-monitoring-github-audit-logs)
>   * [Configure Wazuh to pull GitHub logs](monitoring-github-activity.md#configure-wazuh-to-pull-github-logs)
>   * [Use case](monitoring-github-activity.md#use-case)
