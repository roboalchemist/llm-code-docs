# Source: https://docs.rootly.com/api-reference/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Changelog

> Track the latest changes and updates to the Rootly API

## Unreleased

* **fix:** pagination stability across 26 API v1 controllers by adding deterministic sorting tiebreakers (created\_at, id) to prevent duplicate records across pages
* **breaking:** default sort order changed from descending to ascending for 16 endpoints: causes, custom\_fields, environments, form\_fields, form\_field\_placements, form\_field\_placement\_conditions, functionalities, genius\_tasks, genius\_workflows, groups, incident\_roles, incident\_types, services, severities, catalog\_entities, catalog\_fields. Use `sort=-position` to restore previous behavior.
* **fix:** custom\_forms endpoint now defaults to `created_at` sort (previously used non-existent `position` column)

## December 2025

### December 5, 2025

* **feat:** add assignee to shifts include options and deprecate user field
* **feat:** add incident alerts to incident API response

### December 3, 2025

* **feat:** add created\_by field to Incident AI API

## November 2025

### November 26, 2025

* **feat:** add mitigation\_message, resolution\_message, and cancellation\_message to incident update API

### November 7, 2025

* **fix:** remove timestamps from routing rule target serializer

### November 6, 2025

* **feat:** make slack\_channel nullable in schedules API

### November 4, 2025

* **feat:** add slack\_channel field to schedule endpoint

## October 2025

### October 30, 2025

* **feat:** return UUID for custom\_field\_id in workflow custom field selections API

### October 29, 2025

* **feat:** make scheduled\_for and scheduled\_until fields not required, with auto defaults

### October 28, 2025

* **fix:** add rules back to alert routes API schema
* **feat:** support large position values in API

### October 14, 2025

* **feat:** add additional information fields to Users API
* **feat:** add auto\_add\_members\_when\_attached field to Teams API

### October 10, 2025

* **feat:** add project schedules support to schedules API

### October 7, 2025

* **feat:** add schedule rotation serializer with enhanced rotation details
* **fix:** alert sources API schema validation errors

### October 6, 2025

* **fix:** add alert deduplication fields to alert serializer

### October 3, 2025

* **fix:** missing shifts in API response due to duplicate shift IDs by generating deterministic UUIDs

### October 2, 2025

* **fix:** timezone handling in escalation policy business\_hours API

### October 1, 2025

* **feat:** include substatus name with ID for incidents API
* **feat:** update schedule rotations API to support schedule rotation members
* **fix:** shifts API to return all shifts including duplicates by ID
* **fix:** shift start time to respect API query time range

## September 2025

### September 30, 2025

* **feat:** implement SAML authentication API endpoints for status pages
* **feat:** add email-based heartbeat pinging support
* **fix:** postmortem template update from API

### September 26, 2025

* **fix:** correct turn start for hourly rotations crossing DST

### September 25, 2025

* **fix:** schedule members being null in API response

### September 16, 2025

* **feat:** add assignee\_id and assignee\_type to shift serializer
* **perf:** fix N+1 queries in API alerts index endpoint

### September 12, 2025

* **fix:** search filters not working in heartbeats API

### September 11, 2025

* **feat:** add content\_raw field for markdown type post\_mortem\_templates
* **fix:** missing rate limit headers in API responses

### September 10, 2025

* **feat:** add IANA timezone format support to User API serializer
* **fix:** alert acknowledge/resolve endpoints to validate status transitions

### September 9, 2025

* **feat:** add alert\_description field to heartbeats API

### September 6, 2025

* **feat:** add comprehensive API support for SAML authentication configuration

### September 5, 2025

* **fix:** schedule\_rotation\_users API uses shift rendering v2 if enabled

### September 4, 2025

* **feat:** add alert field values to alerts using API

### September 3, 2025

* **fix:** return 400 for ActionDispatch::Http::Parameters::ParseError

## August 2025

### August 27, 2025

* **feat:** added event sourcing for remote MCP source

### August 22, 2025

* **feat:** Alert Routes API endpoints

### August 12, 2025

* **feat:** add non editable form fields option in forms API

### August 7, 2025

* **fix:** undefined reference to current\_user.role in API responses

### August 6, 2025

* **feat:** allow owner/admin to manage UserNotificationRule for team members via API

### August 4, 2025

* **fix:** relax minimum escalation path restriction for Terraform
* **feat:** add alert events to alerts serializer

## July 2025

### July 31, 2025

* **feat:** add custom fields and incident roles as columns in Table metrics panel API

### July 28, 2025

* **feat:** alert deduplication configuration, timeline events, and API endpoints

### July 23, 2025

* **feat:** email verification API endpoints

### July 22, 2025

* **fix:** include destination in alert routing rule API response
* **fix:** rotation start/end timestamps now returned in UTC
* **feat:** add disable auto adding members to incident channel feature in groups API

## June 2025

### June 4, 2025

* **fix:** user\_ids\[] filtering on /v1/shifts endpoint
* **feat:** slug field to status pages API serializer and schema

### June 2, 2025

* **feat:** services API now accepts owner\_group\_ids parameter
* **refactor:** create reusable user response schema
* **fix:** action items schema for assigned\_to field
* **fix:** ensure user contact info is created for correct user

## May 2025

### May 30, 2025

* **fix:** delete prior sourceable when updating attributes from the API

### May 28, 2025

* **feat:** remove verification attributes from email/phone number APIs
* **feat:** remove primary attribute from user email addresses API
* **feat:** add case-insensitive target\_type normalization

### May 27, 2025

* **feat:** add RESTful API endpoints for user phone numbers and email addresses

### May 26, 2025

* **feat:** add API support for advanced conditions in alert grouping

### May 15, 2025

* **feat:** allow automated invite of external emails into Slack incident channels
* **docs:** update API schema

### May 5, 2025

* **feat:** add new escalate targets to public API schemas

## April 2025

### April 30, 2025

* **feat:** ability to filter alerts by status via API

### April 29, 2025

* **feat:** return API timestamps in seconds

### April 21, 2025

* **feat:** allow internal API endpoint to accept a user\_id parameter

### April 18, 2025

* **fix:** API issue with assigning multiple users to role
* **feat:** include initial\_delay in API serializer

### April 15, 2025

* **fix:** allow owner\_group\_ids parameter in API requests
* **perf:** updated pagination method to accept count for large collections

### April 14, 2025

* **perf:** updated API pagination method to avoid extra count call

### April 9, 2025

* **fix:** add missing urgency rules to alert source serializer

### April 8, 2025

* **feat:** add email source settings to disable threaded emails

### April 4, 2025

* **fix:** typo in alert routes API

### April 3, 2025

* **feat:** team and organization API keys

## March 2025

### March 31, 2025

* **refactor:** single paginate method for database queries and search
* **fix:** API key search in audit logs section

### March 28, 2025

* **feat:** support resolution rule in alert source API

### March 26, 2025

* **refactor:** consistent pagination for search and database queries
* **fix:** specify required fields in routing rule schema
* **fix:** change routing rule schema to conform to OpenAPI standards
* **fix:** prevent crash from invalid SQL queries
* **fix:** allow creating alert events with Rootly bot as user

### March 25, 2025

* **feat:** create/update/delete alert "note" events
* **feat:** specify whether field can be computed in API schema

### March 21, 2025

* **refactor:** updated alert params filtering for API controller

### March 20, 2025

* **fix:** alert routing API issues

### March 17, 2025

* **feat:** add API support for alert routes
* **docs:** fix incorrect paging strategy options
* **fix:** create cached Slack channel if necessary
* **feat:** filter schedules and escalation policies by name
* **fix:** validate and hydrate Slack channel targets
* **fix:** return 422 for invalid record exceptions
* **fix:** prevent duplicate active\_times when updating rotation

### March 14, 2025

* **feat:** add business hours support to escalation policy API
* **fix:** schedule rotation update should return errors
* **fix:** respect requested escalation level position (breaking change)
* **fix:** replace urgency rules when updating source (breaking change)
* **fix:** do not prevent deletion of schedule rotations (breaking change)
* **fix:** prevent duplicate schedule rotation active times

### March 13, 2025

* **fix:** support for escalation level paging strategy

### March 11, 2025

* **feat:** expose sub-status configuration on teams API

## February 2025

### February 26, 2025

* **fix:** API alert sources webhooks endpoint URL

### February 25, 2025

* **fix:** alert sources tags and operationId API schema
* **feat:** add API support to mark alerts as noise

### February 17, 2025

* **feat:** track last updated user for schedule rotations
* **feat:** track last updated user for schedule rotation users

### February 12, 2025

* **feat:** API support for new escalation policy target type "team"

## January 2025

### January 31, 2025

* **docs:** add note about admin\_ids to groups API schema

### January 30, 2025

* **feat:** API support for group admin\_ids

### January 17, 2025

* **fix:** schedules slack\_user\_group API schema

### January 10, 2025

* **feat:** API support for alert source urgency id and alert template

### January 7, 2025

* **feat:** API support for email alert creation

## December 2024

### December 13, 2024

* **refactor:** update escalation policy levels controller

### December 2, 2024

* **fix:** handle undocumented PagerDuty API schema

## October 2024

### October 23, 2024

* **feat:** on-call shift calendar subscription

### October 16, 2024

* **docs:** improve API documentation

### October 14, 2024

* **feat:** handle "mitigated" status for workflow tasks when sub-status enabled
* **feat:** add "Update Incident Status Timestamp" task to API schema

### October 10, 2024

* **feat:** allow sub\_status\_id for /v1/incidents/:id endpoint

### October 1, 2024

* **feat:** add missing API schema attribute for Terraform compatibility

### September 25, 2024

* **feat:** API support for sub-statuses

### September 16, 2024

* **feat:** expose alert urgency to POST api.rootly.com/v1/alerts

### September 10, 2024

* **feat:** add alert notification target on alert updates

### September 4, 2024

* **feat:** add API support for alert groups

### August 30, 2024

* **feat:** add API support for alert urgency

### August 29, 2024

* **feat:** add schedule rotation attributes to OpenAPI schema for Terraform compatibility
* **feat:** add escalation policy path API support

### August 26, 2024

* **docs:** fix /v1/incidents/{incident_id}/alerts documentation

### July 19, 2024

* **fix:** escalation policy OpenAPI schema and add service\_ids, group\_ids

### July 2, 2024

* **fix:** /api/v1/dashboards/:id returning 404 when shared publicly

***


Built with [Mintlify](https://mintlify.com).