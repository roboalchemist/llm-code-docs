# Source: https://docs.asapp.com/reporting/real-time-event-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building a Real-Time Event API

> Learn how to implement ASAPP's real-time event API to receive activity, journey, and queue state updates.

ASAPP provides real-time access to events, enabling customers to power internal use cases.

Typical use cases that benefit from real-time ASAPP events include:

* Tracking the end-user journey through ASAPP
* Supporting workforce management needs
* Integrating with customer-maintained CRM systems

ASAPP's real-time events provide raw data. Batch analytics and reporting handle complex processing, such as aggregation or deduplication.

ASAPP presently supports three real-time event feeds:

1. **Activity**: Agent status change events, for tracking schedule adherence
2. **Journey**: Events denoting milestones in a conversation, for tracking the customer journey
3. **Queue State**: Updates on queues for tracking size and estimated wait times

In order to utilize these available real-time events, a customer will need to configure an API endpoint service under the customer's control. The balance of this document provides information about the high-level tasks a customer will need to accomplish in order to receive real-time events from ASAPP, as well as further information on the events available from ASAPP.

## Architecture Discussion

Upon a customer's request, ASAPP can provide several types of real-time event data.

<Note>
  Note that ASAPP can separately enhance standard real-time events to accommodate specific customer requirements. Such enhancements would usually be specified and implemented as part of ASAPP's regular product development process.
</Note>

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2d5ba1ef-2f1f-b9be-e56a-83915c699934.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=7b18b9056b8a4cde7652c5bf5e597955" alt="Data-ERTAPI-Arch" data-og-width="622" width="622" data-og-height="424" height="424" data-path="image/uuid-2d5ba1ef-2f1f-b9be-e56a-83915c699934.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2d5ba1ef-2f1f-b9be-e56a-83915c699934.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=8caff3b7c89fef1d1d61287a9a733d56 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2d5ba1ef-2f1f-b9be-e56a-83915c699934.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=14bdb167a6c2246faa88192bdc67dc6c 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2d5ba1ef-2f1f-b9be-e56a-83915c699934.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=ca1b2efa0352d7d55ad458da2b47de65 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2d5ba1ef-2f1f-b9be-e56a-83915c699934.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=54e4eb2f1352e8ffce200879c805a5bc 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2d5ba1ef-2f1f-b9be-e56a-83915c699934.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a69cc930af923ecc2554e86dd2301de0 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2d5ba1ef-2f1f-b9be-e56a-83915c699934.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=5a156a55df96b6eabe144168aebf1331 2500w" />
</Frame>

The diagram above provides a high-level view of how a customer-maintained service that receives real-time ASAPP events might be designed; a service that runs on ASAPP-controlled infrastructure will push real-time event data to one or more HTTP endpoints maintained by the customer. For each individual event, the ASAPP service makes one POST request to the endpoint.

ASAPP transmits event data using mTLS-based authentication (See the separate document [Securing Endpoints with Mutual TLS](/reporting/secure-data-retrieval#certificate-configuration) for details).

### Customer Requirements

* The customer must implement a POST API endpoint to handle the event messages.
* The customer and ASAPP must develop the mTLS authentication integration to secure the API endpoint
* All ASAPP real-time "raw" events will post to the same endpoint; the customer is expected to filter the received events to their needs based on name and event type.
* Each ASAPP real-time "processed" reporting feed can be configured to post to one arbitrary endpoint, at the customer's specified preference (i.e., each feed can post to a separate URI, or each can post to the same URI, or any combination required by the customer's use case.)

It should be noted that real-time events do not implement the de-duplication and grouping of ASAPP's batch reporting feeds; rather these real-time events provide building blocks for the customer to aggregate and build on. When making use of ASAPP's real-time events, the customer will be responsible for grouping, de-duplication, and aggregation of related events as required by the customer's particular use case. The events include metadata fields to facilitate such tasks.

### Endpoint Sizing

The endpoint configured by the customer should provisioned with sufficient scale to receive events at the rate generated by the customer's ASAPP implementation. As a rule of thumb, customers can expect:

* A voice call will generate on the order of 100 events per issue
* A text chat will generate on the order of 10 events per issue

So, for example, if the customer's application services 1000 issues per minute, that customer should expect their endpoint to receive 10,000 -- 100,000 messages per minute, or on the order of 1,000 messages per second.

### Endpoint Configuration

ASAPP can configure its service with the following parameters:

* **url:** The destination URL of the customer API endpoint that is set up to handle POST http requests.
* **timeout\_ms:** The number of milliseconds to wait for a HTTP 200 "OK" response before timing out.
* **retries:** The number of times to retry to send a message after a failed delivery.
* **(optional)event\_list:** List of `event_types` to send.

<Note>
  If `event_type` is empty it will default to send all events for this feed.
  List the necessary `event_type` to reduce unnecessary traffic.
</Note>

If the number of retries is exceeded and the customer's API is unable to handle any particular message, that message will be dropped. Real-time information lost in this way will typically be available in historical reporting feeds.

## Real-time Overview

ASAPP's standard real-time events include data representing human interactions and general issue lifecycle information from the ASAPP feeds named `com.asapp.event.activity`, `com.asapp.event.journey`, and `com.asapp.event.queue`.

In the future, when additional event sources are added, the name of the stream will reflect the event source.

## Payload Schema

Each of ASAPP's feeds will deliver a single event's data in a payload comprised of a two-level JSON object. The delivered payload includes:

1. Routing metadata at the top level common to all events.
   *A small set of fields that should always be present for all events, used for routing, filtering, and deduplication.*
2. Metadata common to all events.
   *These fields should usually be present for all events to provide meta-information on the event. Some fields may be omitted if they do not apply to the specific feed.*
3. Data specific to the event feed.
   *Some fields may be omitted but the same total set can be expected for each event of the same origin*
4. Details specific to the event type.

The schema omits null fields -- the customer's API is expected to interpret missing keys as null.

**Versioning**

Minor-versions upgrades to the events are expected to be backwards-compatible; major-version updates typically include an interface-breaking change that may require the customer to update their API in order to take advantage of new features.

## Activity Feed

The agent activity feed provides a series of events for agent login and status changes. ASAPP processes the event data minimally before pushing it into the `activity` feed to:

* Convert internal flags to meaningful human-readable strings
* Filter the feed to include only data fields of potential interest to the customer

<Note>
  ASAPP's `activity` feed does not implement complex event processing (e.g., aggregation based on time windows, groups of events, de-duplication, or system state tracking). Any required aggregation or deduplication should be executed by the customer after receiving `activity` events.
</Note>

### Sample Event JSON

```json  theme={null}
{
  "api_version": "v1.3.0",
  "name": "com.asapp.event.activity",
  "meta_data": {
    "create_time": "2022-06-21T20:10:24.411Z",
    "event_time": "2022-06-21T20:10:24.411Z",
    "session_id": "string",
    "issue_id": "string",
    "company_subdivision": "string",
    "company_id": "string",
    "company_segments": [
      "string"
    ],
    "client_id": "string",
    "client_type": "SMS"
  },
  "data": {
    "rep_id": "string",
    "desk_mode": "UNKNOWN",
    "rep_name": "string",
    "agent_given_name": "string",
    "agent_family_name": "string",
    "agent_display_name": "string",
    "external_rep_id": "string",
    "max_slots": 0,
    "queue_ids": [
      "string"
    ],
    "queue_names": [
      "string"
    ]
  },
  "event_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "event_type": "UNKNOWN",
  "details": {
    "status_updated_ts": "2022-06-21T20:10:24.411Z",
    "status_description": "string",
    "routing_status_updated_ts": "2022-06-21T20:10:24.411Z",
    "routing_status": "UNKNOWN",
    "assignment_load_updated_ts": "2022-06-21T20:10:24.411Z",
    "assigned_customer_ct": 0,
    "previous_routing_status_updated_ts": "2022-06-21T20:10:24.411Z",
    "previous_routing_status": "UNKNOWN",
    "previous_routing_status_duration_sec": 0,
    "previous_routing_status_start_ts": "2022-06-21T20:10:24.411Z",
    "utilization_5_min_updated_ts": "2022-06-21T20:10:24.411Z",
    "utilization_5_min_window_start_ts": "2022-06-21T20:10:24.411Z",
    "utilization_5_min_window_end_ts": "2022-06-21T20:10:24.411Z",
    "utilization_5_min_any_status": {
      "linear_sec": 0,
      "linear_utilized_sec": 0,
      "cumulative_sec": 0,
      "cumulative_utilized_sec": 0
    },
    "utilization_5_min_active": {
      "linear_sec": 0,
      "linear_utilized_sec": 0,
      "cumulative_sec": 0,
      "cumulative_utilized_sec": 0
    },
    "utilization_5_min_away": {
      "linear_sec": 0,
      "linear_utilized_sec": 0,
      "cumulative_sec": 0,
      "cumulative_utilized_sec": 0
    },
    "utilization_5_min_offline": {
      "linear_sec": 0,
      "linear_utilized_sec": 0,
      "cumulative_sec": 0,
      "cumulative_utilized_sec": 0
    },
    "utilization_5_min_wrapping_up": {
      "linear_sec": 0,
      "linear_utilized_sec": 0,
      "cumulative_sec": 0,
      "cumulative_utilized_sec": 0
    }
  }
}
```

### Field Explanations

| Field                   | Description                                                                                                          |
| :---------------------- | :------------------------------------------------------------------------------------------------------------------- |
| api\_version            | Major and minor version of the API, compatible with the base major version                                           |
| name                    | Source of this event stream - use for filtering / routing                                                            |
| event\_type             | Event type within the stream - use for filtering / routing                                                           |
| event\_id               | Unique ID of an event, used to identify identical duplicate events                                                   |
| meta\_data.create\_time | UTC creation time of this message                                                                                    |
| meta\_data.event\_time  | UTC time the event happened within the system - usually some ms before create time                                   |
| meta\_data.session\_id  | Customer-side identifier to link events together based on customer session. May be null for system-generated events. |
| meta\_data.client\_id   | May include client type, device, and version, if present in the event headers                                        |
| data.rep\_id            | Internal ASAPP identifier of an agent                                                                                |
| details                 | These fields vary based on the individual event type - only fields relevant to the event type will be present        |

<Note>
  Adding the `event_list` filter in the configuration allows the receiver of the real-time feed to indicate for which event types they want to receive an Activity message.

  This message will still contain all the fields that have been populated, as the events are being accumulated in the Activity message for that same `rep_id`.

  For example: If the `event_list` contains only `agent_activity_status_updated`, the Activity messages will still contain all the fields (`status_description`, `routing_status`, `previous_routing_status`, `assigned_customer_ct`, `utilization_5_min_active`, etc), but will only be sent whenever the agent status was updated.
</Note>

### Event Types

* `agent_activity_identity_updated`
* `agent_activity_status_updated`
* `agent_activity_capacity_updated`
* `agent_activity_assignment_load_updated`
* `agent_activity_routing_status_updated`
* `agent_activity_previous_routing_status`
* `agent_activity_queue_membership`
* `agent_activity_utilization_5_min`

## Journey Feed

The customer journey feed tracks important events in the customer's interaction with ASAPP. ASAPP processes the event data before pushing it into the `journey` feed to:

* Collect conversation and session events into a single feed of the customer journey
* Add metadata properties to the events to assist with contextualizing the events

<Note>
  This feature is available only for ASAPP Messaging.
</Note>

<Note>
  ASAPP's `journey` feed does not implement aggregation. Any aggregation or deduplication required by the customer's use case will need to be executed by the customer after receiving `journey` events.
</Note>

### Sample Event JSON

```json  theme={null}
{
    "api_version": "string",
    "name": "com.asapp.event.journey",
    "meta_data": {
      "create_time": "2024-08-06T13:57:43.053Z",
      "event_time": "2024-08-06T13:57:43.053Z",
      "session_id": "string",
      "issue_id": "string",
      "company_subdivision": "string",
      "company_id": "string",
      "company_segments": [
        "string"
      ],
      "client_id": "string",
      "client_type": "UNKNOWN"
    },
    "data": {
      "customer_id": "string",
      "opportunity_origin": "UNKNOWN",
      "opportunity_id": "string",
      "queue_id": "string",
      "session_id": "string",
      "session_type": "string",
      "user_id": "string",
      "user_type": "string",
      "session_update_ts": "2024-08-06T13:57:43.053Z",
      "agent_id": "string",
      "agent_name": "string",
      "agent_given_name": "string",
      "agent_family_name": "string",
      "agent_display_name": "string",
      "queue_name": "string",
      "external_agent_id": "string"
    },
    "event_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "event_type": "ISSUE_CREATED",
    "details": {
      "issue_start_ts": "2024-08-06T13:57:43.053Z",
      "intent_code": "string",
      "business_intent_code": "string",
      "flow_node_type": "string",
      "flow_node_name": "string",
      "intent_code_path": "string",
      "business_intent_code_path": "string",
      "flow_name_path": "string",
      "business_flow_name_path": "string",
      "issue_ended_ts": "2024-08-06T13:57:43.053Z",
      "survey_responses": [
        {
          "question": "string",
          "question_category": "string",
          "question_type": "string",
          "answer": "string",
          "ordering": 0
        }
      ],
      "survey_submit_ts": "2024-08-06T13:57:43.053Z",
      "last_flow_action_called_ts": "2024-08-06T13:57:43.053Z",
      "last_flow_action_called_node_name": "string",
      "last_flow_action_called_action_id": "string",
      "last_flow_action_called_version": "string",
      "last_flow_action_called_inputs": {
        "additionalProp1": {
          "value": "string",
          "value_type": "VALUE_TYPE_UNKNOWN"
        },
        "additionalProp2": {
          "value": "string",
          "value_type": "VALUE_TYPE_UNKNOWN"
        },
        "additionalProp3": {
          "value": "string",
          "value_type": "VALUE_TYPE_UNKNOWN"
        }
      },
      "detected_ts": "2024-08-06T13:57:43.053Z",
      "escalated_ts": "2024-08-06T13:57:43.053Z",
      "queued_ts": "2024-08-06T13:57:43.053Z",
      "assigned_ts": "2024-08-06T13:57:43.053Z",
      "abandoned_ts": "2024-08-06T13:57:43.053Z",
      "queued_ms": 0,
      "opportunity_ended_ts": "2024-08-06T13:57:43.053Z",
      "ended_type": "string",
      "assigment_ended_ts": "2024-08-06T13:57:43.053Z",
      "handle_ms": 0,
      "is_ghost_customer": true,
      "last_agent_utterance_ts": "2024-08-06T13:57:43.053Z",
      "agent_utterance_ct": 0,
      "agent_first_response_ms": 0,
      "timeout_ts": "2024-08-06T13:57:43.053Z",
      "last_customer_utterance_ts": "2024-08-06T13:57:43.053Z",
      "customer_utterance_ct": 0,
      "is_resolved": true,
      "customer_ended_ts": "2024-08-06T13:57:43.053Z",
      "customer_params_field_01": "string",
      "customer_params_field_02": "string",
      "customer_params_field_03": "string",
      "customer_params_field_04": "string",
      "customer_params_field_05": "string",
      "customer_params_field_06": "string",
      "customer_params_field_07": "string",
      "customer_params_field_08": "string",
      "customer_params_field_09": "string",
      "customer_params_field_10": "string",
      "customer_params_key_name_01": "string",
      "customer_params_key_name_02": "string",
      "customer_params_key_name_03": "string",
      "customer_params_key_name_04": "string",
      "customer_params_key_name_05": "string",
      "customer_params_key_name_06": "string",
      "customer_params_key_name_07": "string",
      "customer_params_key_name_08": "string",
      "customer_params_key_name_09": "string",
      "customer_params_key_name_10": "string",
      "uploaded_files_list": [
            {
                "file_upload_event_id": "string",
                "file_upload_ts": "2024-10-03T12:30:55.123Z",
                "file_name": "string",
                "file_mime_type": "UNKNOWN",
                "file_size_mb": 0,
                "file_image_width": 0,
                "file_image_height": 0
            }
      ],
      "last_assignment_summary_ts": "2025-10-01T13:03:35.360Z",
      "last_assignment_summary_text": "string",
      "disposition_ts": "2025-10-01T13:03:35.360Z",
      "disposition_fields": [
         {
           "field_type": "UNKNOWN",
           "field_name": "string",
           "field_value": "string"
         }
      ]
    }
  }
```

### Field Explanations

| Field                           | Description                                                                                            |
| :------------------------------ | :----------------------------------------------------------------------------------------------------- |
| api\_version                    | Major and minor version of the API, compatible with the base major version                             |
| name                            | Source of this event stream - use for filtering / routing                                              |
| event\_type                     | Event type within the stream - use for filtering / routing                                             |
| event\_id                       | Unique ID of an event, used to identify identical duplicate events                                     |
| meta\_data.create\_time         | UTC creation time of this message                                                                      |
| meta\_data.event\_time          | UTC time the event happened within the system - usually some ms before create time                     |
| meta\_data.session\_id          | Customer-side identifier to link events together based on customer session                             |
| meta\_data.issue\_id            | ASAPP internal tracking of a conversation - used to tie events together in the ASAPP system            |
| meta\_data.company\_subdivision | Filtering metadata                                                                                     |
| meta\_data.company\_segments    | Filtering metadata                                                                                     |
| meta\_data.client\_id           | May include client type, device, and version                                                           |
| data.customer\_id               | Internal ASAPP identifier of the customer                                                              |
| data.rep\_id                    | Internal ASAPP identifier of an agent. Will be null if no rep is assigned                              |
| data.group\_id                  | Internal ASAPP identifier of a company group or queue. Will be null if not routed to a group of agents |
| details                         | The details of the event. All details are omitted when empty                                           |

### Event Types

* `ISSUE_CREATED`
* `ISSUE_ENDED`
* `INTENT_CHANGE`
* `FIRST_INTENT_UPDATED`
* `INTENT_PATH_UPDATED`
* `NODE_VISITED`
* `LINK_RESOLVED`
* `FLOW_SUCCESS`
* `FLOW_SUCCESS_NEGATED`
* `END_SRS_RESPONSE`
* `SURVEY_SUBMITTED`
* `CONVERSATION_ENDED`
* `CUSTOMER_ENDED`
* `ISSUE_SESSION_UPDATED`
* `DETECTED`
* `OPPORTUNITY_ENDED`
* `OPPORTUNITY_ESCALATED`
* `QUEUED`
* `QUEUE_ABANDONED`
* `TIMED_OUT`
* `TEXT_MESSAGE`
* `FIRST_OPPORTUNITY`
* `QUEUED_DURATION`
* `CUSTOMER_RESPONSE_BY_OPPORTUNITY`
* `ISSUE_OPPORTUNITY_QUEUE_INFO_UPDATED`
* `ASSIGNED`
* `ASSIGNMENT_ENDED`
* `AGENT_RESPONSE_BY_OPPORTUNITY`
* `SUPERVISOR_UTTERANCE_BY_OPPORTUNITY`
* `AGENT_FIRST_RESPONDED`
* `ISSUE_ASSIGNMENT_AGENT_INFO_UPDATED`
* `LAST_FLOW_ACTION_CALLED`
* `JOURNEY_CUSTOMER_PARAMETERS`
* `FILE_UPLOAD_DETECTED`
* `DISPOSITION`
* `LAST_ASSIGNMENT_SUMMARY`

<Note>
  Adding the `event_list` filter in the configuration allows the receiver of the real-time feed to indicate for which event types they want to receive a Journey message.

  This message will still contain all the fields that have been populated, as the events are being accumulated in the Journey message for that same `issue_id`.

  Example: if the `event_list` contains only `SURVEY_SUBMITTED` the Journey messages will still contain all the fields (`issue_start_ts`, `assigned_ts`, `survey_responses`, etc), but will only be sent whenever the survey submitted event happens.
</Note>

## Queue State Feed

The queue state feed provides a set of events describing the state of a queue over the course of time. ASAPP processes the event data before pushing it into the `queue` feed to:

* Collect queue volume, queue time and queue hours events into a single feed of the queue state
* Add metadata properties to the events to assist with contextualizing the events

<Note>
  ASAPP's `queue` feed does not implement aggregation. Any aggregation or deduplication required by the customer's use case will need to be executed by the customer after receiving `queue` events.
</Note>

### Sample Event JSON

```json  theme={null}
{
  "api_version": "string",
  "name": "com.asapp.event.queue",
  "meta_data": {
    "create_time": "2025-10-31T18:03:58.321Z",
    "event_time": "2025-10-31T18:03:58.321Z",
    "session_id": "string",
    "issue_id": "string",
    "company_subdivision": "string",
    "company_id": "string",
    "company_segments": [
      "string"
    ],
    "client_id": "string",
    "client_type": "UNKNOWN"
  },
  "data": {
    "queue_id": "string",
    "queue_name": "string",
    "business_hours_time_zone_offset_minutes": 0,
    "business_hours_time_zone_name": "string",
    "business_hours_start_minutes": [
      0
    ],
    "business_hours_end_minutes": [
      0
    ],
    "holiday_closed_dates": [
      "2025-10-31T18:03:58.321Z"
    ],
    "queue_capping_enabled": true,
    "queue_capping_estimated_wait_time_seconds": 0,
    "queue_capping_size": 0,
    "queue_capping_fallback_size": 0,
    "mitigation_status": "UNKNOWN",
    "queue_availability_last_scheduled_open_ts": "2025-10-31T18:03:58.321Z",
    "queue_availability_last_scheduled_close_ts": "2025-10-31T18:03:58.321Z",
    "queue_availability_next_scheduled_open_ts": "2025-10-31T18:03:58.321Z",
    "queue_availability_next_scheduled_close_ts": "2025-10-31T18:03:58.321Z"
  },
  "event_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "event_type": "UNKNOWN",
  "details": {
    "last_queue_size": 0,
    "last_queue_size_ts": "2025-10-31T18:03:58.321Z",
    "last_queue_size_update_type": "UNKNOWN",
    "estimated_wait_time_updated_ts": "2025-10-31T18:03:58.321Z",
    "estimated_wait_time_seconds": 0,
    "estimated_wait_time_is_available": true,
    "queue_availability_is_closed": true,
    "queue_availability_is_closed_by_business_hours": true,
    "queue_availability_is_closed_by_holiday_settings": true,
    "queue_availability_is_closed_by_estimated_wait_time_cap": true,
    "queue_availability_is_closed_by_size_cap": true,
    "queue_availability_is_closed_by_fallback_size_cap": true,
    "queue_availability_is_closed_by_mitigation": true,
    "queue_availability_is_estimated_wait_time_after_closed_hours": true
  }
}
```

### Field Explanations

For a complete detail of all the fields please refer to the full openapi schema.

| Field                                               | Description                                                                                                                                                    |
| :-------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api\_version                                        | Major and minor version of the API, compatible with the base major version                                                                                     |
| name                                                | Source of this event stream - use for filtering / routing                                                                                                      |
| meta\_data.create\_time                             | UTC creation time of this message                                                                                                                              |
| meta\_data.event\_time                              | UTC time the event happened within the system - usually some ms before create time                                                                             |
| meta\_data.session\_id                              | Customer-side identifier to link events together based on customer session. May be null for system-generated events.                                           |
| meta\_data.issue\_id                                | ASAPP internal tracking of a conversation - used to tie events together in the ASAPP system                                                                    |
| meta\_data.company\_subdivision                     | Filtering metadata                                                                                                                                             |
| meta\_data.company\_id                              | The short name used to uniquely identify the company associated with this event. This will be constant for any feed integration.                               |
| meta\_data.company\_segments                        | Filtering metadata                                                                                                                                             |
| meta\_data.client\_id                               | May include client type, device, and version                                                                                                                   |
| meta\_data.client\_type                             | The lower-cardinality, more general classification of the client used for the customer interaction                                                             |
| data.queue\_id                                      | Internal ASAPP ID for this queue                                                                                                                               |
| data.queue\_name                                    | The name of the queue                                                                                                                                          |
| data.business\_hours\_time\_zone\_offset\_minutes   | The number of minutes offset from UTC for calculating or displaying business hours                                                                             |
| data.business\_hours\_time\_zone\_name              | A time zone name used for display or lookup                                                                                                                    |
| data.business\_hours\_start\_minutes                | A list of offsets (in minutes from Sunday at 0:00) that correspond to the time the queue transitions from closed to open                                       |
| data.business\_hours\_end\_minutes                  | Same as business\_hours\_start\_minutes but for the transition from open to closed                                                                             |
| data.holiday\_closed\_dates                         | A list of dates currently configured as holidays                                                                                                               |
| data.queue\_capping\_enabled                        | Indicates if any queue capping is applied when enqueueing issues                                                                                               |
| data.queue\_capping\_estimated\_wait\_time\_seconds | If the estimated wait time exceeds this threshold (in seconds), the queue will be capped. Zero is no threshold.                                                |
| data.queue\_capping\_size                           | If the queue size is greater than or equal to this threshold, the queue will be capped. Zero is no threshold. This applies independent of estimated wait time. |
| data.queue\_capping\_fallback\_size                 | If there is no estimated wait time and the queue size is greater than or equal to this threshold, the queue will be capped. Zero is no threshold.              |
| event\_id                                           | Unique ID of an event, used to identify identical duplicate events                                                                                             |
| event\_type                                         | Event type within the stream - use for filtering / routing                                                                                                     |
| details.last\_queue\_size                           | The latest size of the queue                                                                                                                                   |
| details.last\_queue\_size\_ts                       | Time when the latest queue size update happened                                                                                                                |
| details.last\_queue\_size\_update\_type             | The reason for the latest queue size change                                                                                                                    |
| details.estimated\_wait\_time\_updated\_ts          | Time when the estimate was last updated                                                                                                                        |
| details.estimated\_wait\_time\_seconds              | The number of seconds a user at the end of the queue can expect to wait                                                                                        |
| details.estimated\_wait\_time\_is\_available        | Indicates if there is enough data to provide an estimate                                                                                                       |

### Event Types

* `queue_info_updated`
* `queue_size_updated`
* `queue_estimated_wait_time_updated`
* `business_hours_settings_updated`
* `holiday_settings_updated`
* `queue_capping_settings_updated`
* `queue_mitigation_updated`
* `queue_availability_updated`
