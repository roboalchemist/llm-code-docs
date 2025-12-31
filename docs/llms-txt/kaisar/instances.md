# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/ai-solutions/instances.md

# Instances

Manage your deployed AI solution instances.

![Solution Instances](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-30683c17ab8875313a6e9dc0102a1d498f32d4e8%2Finstances_list_view.png?alt=media)

## Overview

The Solution Instances section allows you to manage, monitor, and configure all deployed AI solutions in your organization. Track performance, resource usage, and status of your AI assistants and tools.

## Instances Dashboard

The dashboard displays key metrics at a glance:

**Summary Cards**:

* **Total Instances**: Total number of deployed solution instances
* **Active**: Number of instances currently active
* **Running**: Number of instances currently running
* **Error**: Number of instances experiencing errors

## Instance List View

The instances table shows all deployed solutions with the following information:

**Columns**:

* **Instance Name**: Name and description
* **Category**: Solution category (e.g., Data Analytics, Marketing & Content)
* **Status**: Current status (Active, Running, Error, Stopped)
* **Deployed**: Deployment time
* **Performance**: Request count and success rate
* **Resources**: Agents and models used
* **Actions**: Quick actions menu

**Filtering and Search**:

* Search by instance name
* Filter by Category
* Filter by Status

## Viewing Instance Details

To view detailed information about an instance:

1. Navigate to **AI Solutions** → **Instances**
2. Click on an instance from the list
3. View comprehensive details in the modal dialog

![View Instance](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-ee8c8fd557ff96311858a189689d1842830a197a%2Finstance_details_view.png?alt=media)

**Instance Information**:

**Instance Name**\*

* Descriptive name for the instance
* Example: `BI Assistant - Analytics Team`
* Helper text: "Enter a descriptive name for this instance"

**Solution Template**\*

* ID of the solution template deployed
* Example: `sol-016`
* Helper text: "The ID of the solution template to deploy"

**Description**

* Description of the instance purpose
* Example: "Natural language queries for business data"

**Status**\*

* Current operational status
* Dropdown selection: Active, Running, Stopped, Error
* Example: `Active`

## Managing Instances

### Starting and Stopping

To change instance state:

1. Edit the instance
2. Change Status field (Running ↔ Stopped)
3. Save changes

**Running**: Instance is processing requests **Stopped**: Instance is paused and not consuming compute resources

### Monitoring Performance

**Key Metrics**:

* **Requests**: Total number of requests processed
* **Success Rate**: Percentage of successful requests
* **Uptime**: Percentage of time available

**Performance Analysis**:

* Check error rates for debugging
* Monitor request volume for scaling
* Review uptime for SLA compliance

### Resource Usage

**Agents**:

* Number of active agents in the instance
* Affects concurrency and capability

**Models**:

* Number of AI models loaded
* Affects memory usage and latency

## Best Practices

**Naming Conventions**:

* Use descriptive names (e.g., "Department - Function")
* Include environment (e.g., "Dev - Support Bot")

**Resource Management**:

* Stop unused instances to save costs
* Monitor resource usage regularly
* Scale resources based on demand

**Maintenance**:

* Update solution templates when available
* Review error logs for "Error" status instances
* Archive or delete obsolete instances

## Next Steps

* Browse [Market Place](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/ai-solutions/market-place) for new solutions
* Monitor in [Analytics](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/analytics)
* Configure [Agents](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/organization/agents)
