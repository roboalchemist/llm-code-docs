# Source: https://docs.pentaho.com/pdc-admin/user-activity-logging-and-dashboard-configuration.md

# User activity logging and dashboard configuration

This guide serves as a technical reference for developers and data engineers building dashboards and analytics solutions with the User Activity Logging system in Pentaho Data Catalog. It outlines the architecture, data schema, event taxonomy, and suggested query and visualization patterns for accessing data from the OpenObserve database via the `/api/observability/logs` endpoint. This logging data can be utilized for observability and auditing.

## System overview

The observability logging subsystem captures granular user and system activities across microservices, enabling rich analytics, auditing, and dashboard insights. It is fully integrated with Data Catalog’s data governance and metadata management components.

The following components constitute the architecture:

* **Frontend**: React-based hooks monitor user interactions and data changes.
* **Backend API**: `/api/observability/logs (POST)` receives structured event payloads.
* **Database Layer**: OpenObserve indexes all logs for real-time and historical analysis.
* **Coverage**: Fully deployed in Business Glossary, Policy, and Applications microservices, detecting creation, modification, deletion, and custom property events.

## **Logging architecture**

Each log event contains a normalized payload that is structured for analysis and visualization in observability dashboards.\
The payload includes the following core elements:

* **Event metadata:** Includes the timestamp, action type, and category.
* **Event details:** Describes the specific asset or field change.
* **User context:** Identifies the user ID, roles, and profile information.
* **Session context:** Captures details about the browser and operating system.
* **Navigation context:** Records the page path and component ID.

This design ensures uniform semantics across all logged actions and allows efficient aggregation for observability dashboards.

## Payload schema

Each log entry follows a standardized JSON structure that defines the format of event data.

### Root structure

```
{
  "level": "info",                    // Always "info" for observability logs
  "message": string,                  // Human-readable activity description
  "event": EventObject,               // Structured event data
  "user_id": string,                  // User identifier
  "user_attributes": UserAttributes,  // User context
  "page_attributes": PageAttributes,  // Navigation context  
  "session_attributes": SessionAttributes // Browser/device context
}
```

### Event object

```

{
  "timestamp": "2025-09-10T22:13:13.778Z", // ISO 8601 timestamp
  "action": string,                         // Event action type
  "category": string,                       // Microservice category
  "details": EventDetails                   // Activity-specific data
}
```

### Event details

```

{
  "id": string,             // Asset unique identifier
  "name": string,           // Asset display name
  "type": string,          // Asset type (e.g., "glossary", "policy", "application")
  "activity": string,      // Human-readable activity description
  "fieldName"?: string,              // Field that was modified (optional)
  "originalValue"?: any,             // Value before change (optional)
  "newValue"?: any,                  // Value after change (optional)
  "relationshipType"?: string,       // For relationship operations (optional)
  "targetTermId"?: string,           // For term relationship operations (optional)
  "importFileName"?: string          // For import operations (optional)
}
```

### User attributes

```
{
  "email": string,
  "roles": string[],
  "firstName": string,
  "lastName": string,
  "owner"?: string,
  "status"?: string
}
```

### Page attributes

```
{
  "id": string,           // React Router location key
  "path": string,         // Current route path (e.g., "/glossary", "/policies")
  "hash": string          // URL hash fragment
}
```

### Session attributes

```
{
  "browser": string,       // Browser name (e.g., "Google Chrome", "Mozilla Firefox")
  "operating_system": string   // OS name (e.g., "Mac OS", "Windows OS", "Linux OS")
}
```

## **Event classification**

Each log event is assigned a category based on the type of asset or operation it records.\
The following table describes the available event categories.

<table><thead><tr><th width="201">Category</th><th>Description</th></tr></thead><tbody><tr><td><strong>Glossary</strong></td><td>Business glossary and terminology assets.</td></tr><tr><td><strong>Policy</strong></td><td>Governance policy assets.</td></tr><tr><td><strong>Applications</strong></td><td>Application and system metadata.</td></tr><tr><td><strong>Entity</strong></td><td>General asset operations.</td></tr><tr><td><strong>Business rules</strong></td><td>Data rule configurations.</td></tr><tr><td><strong>Data collections</strong></td><td>Data-set orchestration activities.</td></tr></tbody></table>

## **Supported actions**

Each log event includes an action that describes the type of operation performed.\
The following table lists the supported actions and their meanings.

<table><thead><tr><th width="201">Action</th><th>Description</th></tr></thead><tbody><tr><td><strong>View</strong></td><td>Viewing or accessing an asset.</td></tr><tr><td><strong>Create</strong></td><td>Creating a new asset or record.</td></tr><tr><td><strong>Update</strong></td><td>Modifying an existing asset.</td></tr><tr><td><strong>Delete</strong></td><td>Removing an asset permanently.</td></tr><tr><td><strong>Run</strong></td><td>Running a specific function or task.</td></tr><tr><td><strong>Start</strong></td><td>Starting a long-running or background process.</td></tr></tbody></table>

## **Activity tracking by hierarchy**

Each hierarchy uses specific activity types that align with its domain.\
Examples include the following:

* **Glossary**: `Create Business Term`, `Update Definition`, `Add Term Relationship`, `Import Terms`
* **Policy**: `Update Purpose`, `Update Effective Range`, `Add Rules`, `Import Policies`
* **Applications**: `Update Owner`, `Add Business Rules`, `Import Applications`

Each operation generates a separate log entry that includes event context and field-level change details recorded from the Data Catalog user interface.

{% hint style="warning" %}
User actions performed through APIs are not logged in this format in version PDC 10.2.9.
{% endhint %}

### **Glossary activities**

User Activity Logging tracks all actions performed on glossary assets, including creation, modification, deletion, and import operations. The following lists describe the supported activity types.

#### **Asset lifecycle operations**

* `Create Business Term` - New business term creation
* `Create Category` - New category creation
* `Create Glossary` - New glossary creation
* `Delete Business Term` - Business term deletion
* `Delete Category` - Category deletion

#### **Field update operations**

* `Update Name` - Asset name changes
* `Update Definition` - Term definition changes
* `Update Description` - Term description changes
* `Update Trust Score` - Data quality scoring
* `Update Knowledge Database` - Knowledge source updates
* `Update Status` - Term lifecycle status (Draft, Accepted, etc.)
* `Update Owner` - Ownership assignment
* `Update Custodian` - Data custodian assignment
* `Update Business Steward` - Business steward assignment
* `Update Domain` - Domain classification
* `Update Sensitivity Level` - Data sensitivity classification
* `Update Abbreviation` - Term abbreviation
* `Update Formula` - Calculation formula
* `Update Business Entity Flag` - Business entity designation
* `Update Critical Data Element Flag` - CDE designation
* `Update Lineage Verification Status` - Data lineage verification
* `Update Quality Score` - Data quality metrics
* `Update Visual Style` - Display styling
* `Update Tags` - Tag management
* `Update Custom Properties` - Bulk custom metadata updates
* `Update Custom Property` - Individual custom property changes

#### **Relationship operations**

* `Add Term Relationship` - Creating term relationships
* `Remove Term Relationship` - Removing term relationships

#### **Import operations**

* `Import Terms` - Bulk term imports
* `Overwrite Term via Import` - Import with data overwrite

### **Policy activities**

User Activity Logging tracks all lifecycle, field-level, and import actions performed on policy assets.\
The following lists describe the supported activity types.

#### **Asset lifecycle operations**

* `Create Policy` - New policy creation
* `Delete Policy` - Policy deletion

#### **Field update operations**

* `Update Name` - Asset name changes
* `Update Definition` - Policy definition text
* `Update Purpose` - Policy purpose/objective
* `Update Scope` - Policy scope and applicability
* `Update Stakeholders` - Policy stakeholders
* `Update Effective Rang`e - Policy effective date range
* `Update Review Date` - Policy review schedule
* `Update Version` - Policy version management
* `Update Owners` - Policy ownership
* `Update Custom Property` - Individual custom property changes

#### **Import operations**

* `Import Policies` - Bulk policy imports
* `Overwrite Policy via Import` - Import with data overwrite

### **Applications activities**

User Activity Logging tracks all lifecycle, field-level, relationship, and import operations performed on application assets. The following lists describe the supported activity types.

#### **Asset lifecycle operations**

* `Create Application` - New application creation
* `Delete Application` - Application deletion

#### **Field update operations**

* `Update Name` - Asset name changes
* `Update Description` - Application description
* `Update Purpose` - Application purpose/function
* `Update Abbreviation` - Application abbreviation
* `Update Owner` - Application ownership
* `Update Critical Data Element Flag` - CDE processing indicator
* `Update Vendor` - Application vendor information
* `Update Valid Until` - Application validity period
* `Update Contact Name` - Technical contact
* `Update Contact Email` - Technical contact email
* `Update Custom Property` - Individual custom property changes

#### **Relationship operations:**

* `Add Application Relationship` - Inter-application relationships
* `Remove Application Relationship` - Relationship removal

#### **Import operations:**

* `Import Applications` - Bulk application imports
* `Overwrite Application via Import` - Import with data overwrite

#### **Common operations** (shared with other microservices)

* `Update Status`,  `Update Domain`,  `Update Custodian`,  `Update Business Steward`
* `Update Rating`,  `Update Visual Style`,  `Update Tags`,  `Update Custom Properties`
* `Add Business Rules`,  `Remove Business Rules`,  `Add Policies`,  `Remove Policies`

### Sample payload examples

Developers can reference the following payloads when building queries or dashboards:

* **the Asset Creation:** Logs newly created glossary or policy assets.
* **Asset Deletion:** Captures asset removal operations.
* **Field Update:** Captures field-level metadata changes (e.g., name, status, tags).
* **Custom Property Updates:** Tracks individual or bulk custom property updates.
* **Import Operations:** Records bulk imports for asset synchronization.

All payloads follow ISO 8601 timestamping and maintain a human-readable message property summarizing the action.

## Analytical query templates

Use the following SQL query templates to create dashboards and visualizations in OpenObserve:

**Top Active Users**

This query lists the users who performed the most actions in a specified period.

```
SELECT user_id, user_attributes.email, COUNT(*) AS activity_count
FROM observability_logs
WHERE timestamp >= '2025-09-01'
GROUP BY user_id, user_attributes.email
ORDER BY activity_count DESC
```

**Activity Volume by Category**

This query shows the total number of events for each asset category.

```
SELECT event.category, COUNT(*) AS event_count
FROM observability_logs
WHERE timestamp >= '2025-09-01'
GROUP BY event.category
```

**Lifecycle Operations**

This query counts the number of assets created and deleted each day.

```
SELECT event.action, DATE(timestamp) AS log_date, COUNT(*) AS count
FROM observability_logs
WHERE event.action IN ('Create', 'Delete')
GROUP BY event.action, DATE(timestamp)
ORDER BY log_date
```

## Log data and governance considerations

User Activity Logging in Data Catalog follows strict data governance and validation standards to ensure audit integrity and operational transparency.\
The following practices apply to all observability logs:

* **Payload validation:** Each log payload is validated upon collection to ensure required fields are present and properly formatted.
* **Field naming conventions:** Field names use dot notation (for example, `event.category`, `user_attributes.email`) to maintain a consistent structure across all microservices.
* **Timestamps:** All timestamps follow the ISO 8601 standard to ensure accurate event ordering and compatibility across time zones.
* **Data minimization:** Personally identifiable information (PII) is limited to operational metadata, such as user names and email addresses.
* **Error handling:** Invalid or incomplete payloads are recorded with warning messages rather than rejected, preserving traceability.

## **Dashboard development recommendations**

You can use observability logs in OpenObserve to build custom dashboards that measure user engagement, governance activity, and operational efficiency.

### Key metrics

The following key metrics are recommended when designing dashboards:

1. **User engagement:** Track the number of user actions over time to identify active users and peak usage periods.
2. **Asset activity:** Monitor how often assets are updated, deleted, or imported to measure data stewardship workload.
3. **Import success rate:** Compare the number of successful import operations to total number of imports to evaluate data synchronization reliability.
4. **Data stewardship participation:** Analyze actions performed by specific roles (for example, Data Steward, Admin) to assess team involvement.
5. **Asset lifecycle trends:** Visualize the flow of assets from creation to modification to retirement to understand data evolution.

### **Implementation coverage summary**

The following table summarizes the current implementation coverage of user activity logging across Data Catalog microservices.

<table><thead><tr><th width="276">Operation Type</th><th>Status</th></tr></thead><tbody><tr><td>Asset Creation</td><td>Complete across all hierarchies</td></tr><tr><td>Asset Deletion</td><td>Complete across all hierarchies</td></tr><tr><td>Field Updates</td><td>Full field-level observability</td></tr><tr><td>Relationship Updates</td><td>Implemented</td></tr><tr><td>Custom Property Management</td><td>Individual and bulk logging implemented</td></tr><tr><td>Import / Bulk Operations</td><td>Fully supported</td></tr><tr><td>Lifecycle Status Changes</td><td>Fully supported</td></tr><tr><td>Ownership and Steward Updates</td><td>Fully supported</td></tr></tbody></table>

All core data governance operations are observable and auditable through OpenObserve, enabling complete visibility into user actions and system changes.

## **Accessing the logs**

You can access user activity logs directly in the OpenObserve interface or by using the API. Perform the following steps to access through the OpenObserve user interface:

1. Go to `https://<PDC hostname>/internal/openobserve/web/`
2. Sign in with your credentials.

   <table data-header-hidden><thead><tr><th width="139">Field</th><th>Value (example)</th></tr></thead><tbody><tr><td><strong>Username</strong></td><td><code>root@example.com</code></td></tr><tr><td><strong>Password</strong></td><td><code>Complexpass#123</code></td></tr><tr><td><strong>Organization</strong></td><td><code>pdc</code></td></tr></tbody></table>

   > **Caution:** These credentials are examples. Use your organization’s secure credentials to access production environments.
3. Open the **`observability_logs`** index to view real-time and historical log data.
4. Use filters or queries to analyze activities by category, action type, or user.

You can now view user and system activity logs in OpenObserve and perform searches or build visual dashboards.
