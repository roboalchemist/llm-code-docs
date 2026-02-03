# Source: https://docs.snyk.io/snyk-api/api-endpoints-index-and-tips/scenarios-for-using-the-snyk-api.md

# Scenarios for using the Snyk API

The Snyk API scenarios identify procedures you can use to accomplish tasks with Snyk applications using the API. The scenarios listed on this page are grouped in Snyk processes and provided in a [repository](https://github.com/snyk-playground/cx-tools/tree/main/scripts) or on the user docs site. Links are included.

If you have issues when using these procedures, contact your Technical Success Manager or Solutions Engineer, or [submit a ticket](https://support.snyk.io) to Snyk support.

## Manage Snyk Organization structure

### Create multiple new Organizations that all have the same settings in a given Group

Scenario: [create-multiple-orgs-and-copy-settings](https://github.com/snyk-playground/cx-tools/blob/main/scripts/create-multiple-orgs-and-copy-settings.md) (complete procedure)

**Endpoints used:**\
[Create a new organization](https://docs.snyk.io/reference/organizations-v1#org)\
[View organization settings](https://docs.snyk.io/reference/organizations-v1#org-orgid-settings-1)\
[Update organization settings](https://docs.snyk.io/reference/organizations-v1#org-orgid-settings)\
[Clone an integration with settings and credentials](https://docs.snyk.io/reference/integrations-v1#org-orgid-integrations-integrationid-clone)

### Assign all users in a given list to all the Organizations a company has (all Organizations in a Group)

Scenario: [assign-users-to-all-orgs](https://github.com/snyk-playground/cx-tools/blob/main/scripts/assign-users-to-all-orgs.md) (complete procedure)

**Endpoints used:**\
[List all members in a group](https://docs.snyk.io/reference/groups-v1#group-groupid-members)\
[Invite users](https://docs.snyk.io/reference/organizations-v1#org-orgid-invite)

### Add users to organizations at scale ahead of the first login

Scenario: [Provision users to Orgs via API](https://docs.snyk.io/snyk-platform-administration/user-management-with-the-api/provision-users-to-organizations-using-the-api)

**Endpoint used:**\
[Provision a user to the organization](https://docs.snyk.io/reference/organizations-v1#org-orgid-provision)

## Import and set up Snyk Projects

### Identify and import new repositories only

Scenario: [Identify-and-import-new-repos](https://github.com/snyk-playground/cx-tools/blob/main/scripts/Identify-and-import-new-repos.md) (complete procedure)

**Endpoints used:**\
[Get targets by org ID](https://docs.snyk.io/reference/targets#orgs-org_id-targets)\
[Import targets](https://docs.snyk.io/reference/import-projects-v1#org-orgid-integrations-integrationid-import)

### Import fresh container images

Scenario: [import-new-container-images](https://github.com/snyk-playground/cx-tools/blob/main/scripts/import-new-container-images.md) (complete procedure)

**Endpoints used:**\
[List all projects for an Org with the given Org ID](https://docs.snyk.io/reference/projects#orgs-org_id-projects)\
[Import targets](https://docs.snyk.io/reference/import-projects-v1#org-orgid-integrations-integrationid-import)\
[Get import job details](https://docs.snyk.io/reference/import-projects-v1#org-orgid-integrations-integrationid-import-jobid)\
[Delete a project](https://docs.snyk.io/reference/projects-v1#org-orgid-project-projectid-2)

### Detect new Projects (files) in repositories and import them into a Target in Snyk on a regular basis

Scenario: [Identify-and-import-new-repos](https://github.com/snyk-playground/cx-tools/blob/main/scripts/Identify-and-import-new-repos.md) (complete procedure)

**Endpoint used:**\
[Get targets by org ID](https://docs.snyk.io/reference/targets#orgs-org_id-targets)\
[Import targets](https://docs.snyk.io/reference/import-projects-v1#org-orgid-integrations-integrationid-import)

## Manage Snyk Projects

### Tag all Projects in Snyk

Scenario: [Tag projects in Snyk](https://github.com/snyk-playground/cx-tools/blob/main/scripts/tag-snyk-projects.md) (complete procedure)

**Endpoints used:**\
[List all Projects for an Org with the given Org ID](https://docs.snyk.io/reference/projects#orgs-org_id-projects)

### Move Projects from one Organization to another

Scenario: [Move projects between organizations](https://github.com/snyk-playground/cx-tools/blob/main/scripts/move-projects.md) (complete procedure)

{% hint style="info" %}
The API token used must have Group Admin access.\
If you are moving between Organizations in different Groups, you must use a personal API token with Group Admin permissions in both Groups. Service Accounts cannot move projects between Organizations in different Groups.

Historical data for reporting will be lost.
{% endhint %}

**Endpoints used:**\
[Move project to a different organization](https://docs.snyk.io/reference/projects-v1#org-orgid-project-projectid-move)

## Integrate with SCMs

### Rotate or change your Broker token for any reason

Scenario: [Broker-token-rotation](https://github.com/snyk-playground/cx-tools/blob/main/scripts/broker-token-rotation.md) (complete procedure)

**Endpoints used:**\
[List all the organizations a user belongs to](https://docs.snyk.io/reference/organizations-v1#orgs) (group admin only)\
[Add new integration](https://docs.snyk.io/reference/integrations-v1#org-orgid-integrations)\
[Update existing integration](https://docs.snyk.io/reference/integrations-v1#org-orgid-integrations-integrationid) (to enable Broker)

### For a specific event or time, disable all interactions (pull requests, tests) from Snyk to the code base (source control management repository)

Scenario: [disable-all-interaction-from-snyk](https://github.com/snyk-playground/cx-tools/blob/main/scripts/disable-all-interaction-from-snyk.md) (complete procedure)

**Endpoints used alternative 1: Get integrations from different organizations and then update the settings for each integration**\
[List](https://docs.snyk.io/reference/integrations-v1#org-orgid-integrations-1) (integrations)\
[Update](https://docs.snyk.io/reference/integrations-v1#org-orgid-integrations-integrationid-settings) (integration settings)\
[Update existing integration](https://docs.snyk.io/reference/integrations-v1#org-orgid-integrations-integrationid)

**Endpoints used alternative 2:** **Webhooks approach: remove the Snyk webhook by getting the Webhook Id and using it to delete the webhook**\
[List webhooks](https://docs.snyk.io/reference/webhooks-v1#org-orgid-webhooks-1)\
[Delete a webhook](https://docs.snyk.io/reference/webhooks-v1#org-orgid-webhooks-webhookid-1)\
[Create a webhook](https://docs.snyk.io/reference/webhooks-v1#org-orgid-webhooks)

## Retrieve and manage issues

### Retrieve a Project snapshot for every Project in a given Group

Scenario: [Retrieve-project-snapshots](https://github.com/snyk-playground/cx-tools/blob/main/scripts/retrieve-projects-snapshots.md) (complete procedure)

**Endpoints used:**\
[List all organizations in a group](https://docs.snyk.io/reference/groups-v1#group-groupid-orgs)\
[Get list of latest issues](https://docs.snyk.io/reference/reporting-api-v1#reporting-issues-latest)

### Find all Projects affected by a vulnerability

Scenario: [find-all-projects-affected-by-a-vuln.md](https://github.com/snyk-playground/cx-tools/blob/main/scripts/find-all-projects-affected-by-a-vuln.md) (complete procedure)

**Endpoints used:**\
[Get list of issues](https://docs.snyk.io/reference/reporting-api-v1#reporting-issues)\
[List all organizations in a group](https://docs.snyk.io/reference/groups-v1#group-groupid-orgs)\
[List all projects for an Org with the given Org ID](https://docs.snyk.io/reference/projects#orgs-org_id-projects)

### Bulk ignore issues

Scenario: [bulk-ignore-issues](https://github.com/snyk-playground/cx-tools/blob/main/scripts/bulk-ignore-issues.md) (complete procedure)

**Endpoints used:**\
[List all projects for an Org with the given Org ID](https://docs.snyk.io/reference/projects#orgs-org_id-projects)\
[Get list of latest issues](https://docs.snyk.io/reference/reporting-api-v1#reporting-issues-latest) (To get all issues but Code)\
[Get issues by org ID](https://docs.snyk.io/reference/issues#orgs-org_id-issues) (To get all Code issues)

### List all issues including Snyk Code issues in all the Projects in an Organization

Scenario: [list-all-issues-for-a-snyk-org](https://github.com/snyk-playground/cx-tools/blob/main/scripts/list-all-issues-for-a-snyk-org.md) (complete procedure)

**Endpoints used:**\
[List all projects for an Org with the given Org ID](https://docs.snyk.io/reference/projects#orgs-org_id-projects)\
[List all aggregated issues](https://docs.snyk.io/reference/projects-v1#org-orgid-project-projectid-aggregated-issues) (no Code)\
[Get issues by org ID](https://docs.snyk.io/reference/issues#orgs-org_id-issues) Note that as of April, 2025, you can retrieve Snyk Code issues using this endpoint. It has the primary file path and primary region in the `source_location` data in `representations` in `coordinates` for an issue.\
REST experimental [Get a Snyk Code issue by its ID](https://apidocs.snyk.io/?version=2022-04-06%7Eexperimental#get-/orgs/-org_id-/issues/detail/code/-issue_id-)\
[Retrieve ignore](https://docs.snyk.io/reference/ignores-v1#org-orgid-project-projectid-ignore-issueid-2)
