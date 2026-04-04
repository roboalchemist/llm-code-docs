# Source: https://documentation.onesignal.com/reference/update-live-activity-api.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Live Activity

> Update or terminate running iOS Live Activities using OneSignal’s Live Activities API. This endpoint enables real-time content updates and activity termination, ensuring dynamic, context-aware user experiences.

## Overview

Update or terminate running iOS Live Activities using our REST API. This endpoint enables real-time content updates and activity termination, ensuring dynamic, context-aware user experiences.

Before using this API, ensure your app is properly configured by following the [Live Activities developer setup](/docs/en/live-activities-developer-setup).

## How to Use this API

1. Select the Live Activity to update by specifying its `activity_id` in the URL. This is set when using the:

* [Start Live Activity API](/reference/start-live-activity)
* [Triggering it in-app](/docs/en/live-activities-developer-setup).
* [`LiveActivities.enter` SDK method](/docs/en/mobile-sdk-reference#enter)

1. Update the state of the Live Activity by setting the `event_updates` parameter to a JSON object that matches the structure of the `ActivityAttributes.ContentState` struct defined in your Live Activity widget extension.

2. When ready to terminate the Live Activity:

* Set the `event` parameter to `end`
* Include a `dismissal_date` if you want the Live Activity to be dismissed in less than 4 hours.
* Set the `dismissal_date` to a time in the past to dismiss the Live Activity immediately. User must have clicked "Allow" for the Live Activity to be removed programmatically.

<Warning>
  Once a Live Activity `activity_id` is ended, you cannot update it. This includes changing the `dismissal_date` or `event` parameter.

  If the Live Activity is not being dismissed immediately, it is either because:

* The `activity_id` has already been ended.
* The user has not clicked "Allow" for the Live Activity to be removed programmatically.
</Warning>

***

## OpenAPI

````yaml POST /apps/{app_id}/live_activities/{activity_id}/notifications
openapi: 3.1.0
info:
  title: api.onesignal.com
  version: '11.6'
servers:
  - url: https://api.onesignal.com
security:
  - {}
paths:
  /apps/{app_id}/live_activities/{activity_id}/notifications:
    post:
      summary: Update Live Activity
      description: >-
        Update or terminate running iOS Live Activities using OneSignal’s Live
        Activities API. This endpoint enables real-time content updates and
        activity termination, ensuring dynamic, context-aware user experiences.
      operationId: update-live-activity-api
      parameters:
        - name: app_id
          in: path
          description: >-
            Your OneSignal App ID in UUID v4 format. See [Keys &
            IDs](/docs/keys-and-ids).
          schema:
            type: string
          required: true
        - name: activity_id
          in: path
          description: >-
            An identifier you set when starting the Live Activity to uniquely
            identify it and associated devices with the event. This value is
            crucial for maintaining a consistent reference to the Live Activity
            across different devices and sessions. Consider using a UUID, CUID,
            or NanoID for this parameter.
          schema:
            type: string
          required: true
        - name: Content-Type
          in: header
          required: true
          schema:
            type: string
            default: application/json
        - name: Authorization
          in: header
          description: >-
            Your App API key with prefix `Key `. See [Keys &
            IDs](/docs/keys-and-ids).
          required: true
          schema:
            type: string
            default: Key YOUR_APP_API_KEY
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - event
                - event_updates
                - name
              properties:
                event:
                  type: string
                  description: >-
                    The action to perform on the Live Activity. Options:`update`
                    - Updates the content of an existing Live Activity without
                    ending it. `end` — Ends the Live Activity and removes it
                    from the user's view. See Apple's developer docs on
                    [Starting and updating Live
                    Activities](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications).
                  enum:
                    - update
                    - end
                event_updates:
                  type: object
                  description: >-
                    The content used to update a running Live Activity. The
                    object must conform to the `ContentState` interface defined
                    within your app's Live Activity. See [Live Activities
                    developer setup](/docs/live-activities-developer-setup).
                  format: json
                name:
                  type: string
                  description: >-
                    An internal name you set to help organize and track
                    messages. Not shown to recipients. Maximum 128 characters.
                contents:
                  type: object
                  description: >-
                    The push message body with [language-specific
                    values](/docs/multi-language-messaging#supported-languages).
                  required:
                    - en
                  properties:
                    en:
                      type: string
                      description: >-
                        The required message language type. See [Supported
                        Languages](/docs/multi-language-messaging#supported-languages).
                stale_date:
                  type: integer
                  description: >-
                    A Unix timestamp (in seconds) that indicates the date the
                    Live Activity is considered outdated. Once this time is
                    reached, the system updates the Live Activity to
                    [`ActivityState.stale`](https://developer.apple.com/documentation/activitykit/activitystate/stale)
                    at which point you can update the Live Activity to indicate
                    that its content is out of date.
                  format: int32
                dismissal_date:
                  type: integer
                  description: >-
                    A Unix timestamp (in seconds) indicating when the Live
                    Activity should be removed from user's device. Use with the
                    `end` event. If not set, the Live Activity will be dismissed
                    automatically after 4 hours. To dismiss the Live Activity
                    immediately, the user must have allowed the Live Activity
                    first. Then you can set a date that’s in the past — for
                    example, `1663177260`. Alternatively, provide a date within
                    a four-hour window to set a custom dismissal date before the
                    default 4 hour period. See [Apple's
                    documentation](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#End-the-Live-Activity-with-a-custom-dismissal-date)
                    for more.
                  format: int32
                priority:
                  type: integer
                  description: >-
                    Set the priority based on the urgency of the message. `10` -
                    High priority. `5` - Normal priority. Apple allows a certain
                    budget of High priority updates per hour. Exceeding the
                    budget may throttle your messages. Apple recommends choosing
                    a mix of priority `5` and `10` to prevent throttling. If
                    your app needs more frequent updates, use
                    `NSSupportsLiveActivitiesFrequentUpdates` entry as directed
                    in [Apple's Developer
                    Docs](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Determine-the-update-frequency).
                  format: int32
                  enum:
                    - 5
                    - 10
                ios_relevance_score:
                  type: number
                  description: >-
                    A value between `0` and `1`. If you start more than one Live
                    Activity for your app, the Live Activity with the highest
                    relevance score appears in the Dynamic Island. If Live
                    Activities have the same relevance score, the system
                    displays the Live Activity that started first. Additionally,
                    the Relevance Score determines the order of your Live
                    Activities on the Lock Screen.
                  format: double
      responses:
        '201':
          description: '201'
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: The ID of the Live Activity update request.
        '400':
          description: '400'
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: array
                    items:
                      type: string
                      description: >-
                        Reason for the message not being started. Usually due to
                        the activity type not being found in the app.
      deprecated: false

````

Built with [Mintlify](https://mintlify.com).
