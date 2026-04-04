# Source: https://firebase.google.com/docs/cloud-messaging/ios/live-activity.md.txt

<br />

With the Firebase Cloud Messaging [HTTP v1
API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages/send), you can remotely send,
update, and end live activity notifications on iOS devices. Note that you need
iOS 16.1 to use live activity and iOS 17.2 to remotely start a live activity
notification.

## Before you begin

Before you get started with live activity on Firebase Cloud Messaging, follow the
instructions in [Set up a Firebase Cloud Messaging client app on Apple
platforms](https://firebase.google.com/docs/cloud-messaging/ios/client) to create and add
Firebase Cloud Messaging to your client app.

## Start a live activity

To start a live activity remotely using Firebase Cloud Messaging, you need to
obtain a [push-to-start
token](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Start-new-Live-Activities-with-ActivityKit-push-notifications)
from Apple. You will also need the [FCM registration
token](https://firebase.google.com/docs/cloud-messaging/ios/client#access_the_registration_token) for the
target app.

To construct a [payload that starts a live
activity](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Construct-the-payload-that-starts-a-Live-Activity),
fill in the
[`apns.payload`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#ApnsConfig) field
from the following code sample to remotely start a live activity using
FCM.  

### REST


```json
{
"message": {
  "token": "<var translate="no">FCM_TOKEN</var>",
  "apns": {
    "live_activity_token": "<var translate="no">LIVE_ACTIVITY_PUSH_TO_START_TOKEN</var>",
    "headers": {
      "apns-priority": "10"
    },
    "payload": {
      "aps": {
        "timestamp": TIMESTAMP,
        "event": "start",
        "content-state": {
          "demo": 1
        },
        "attributes-type": "DemoAttributes",
        "attributes": {
          "demoAttribute": 1
        },
        "alert": {
          "title": "test title",
          "body": "test body"
        }
      }
    }
  }
}
}
```

<br />

### cURL


```bash
curl -X POST -H "Authorization: Bearer <var translate="no">OAUTH2_ACCESS_TOKEN</var>" -H "Content-Type: application/json" -d '{
"message": {
"token": "<var translate="no">FCM_TOKEN</var>",
"apns": {
  "live_activity_token": "<var translate="no">LIVE_ACTIVITY_PUSH_TO_START_TOKEN</var>",
  "headers": {
    "apns-priority": "10"
  },
  "payload": {
    "aps": {
      "timestamp": <var translate="no">TIMESTAMP</var>,
      "event": "start",
      "content-state": {
        "demo": 1
      },
      "attributes-type": "DemoAttributes",
      "attributes": {
        "demoAttribute": 1
      },
      "alert": {
        "title": "test title",
        "body": "test body"
      }
    }
  }
}
}
}' https://fcm.googleapis.com/v1/projects/YOUR_PROJECT_ID/messages:send
```

<br />

[Run](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages/send?apix=true&apix_params=%7B%22parent%22:%22projects/%3Cproject_number%3E%22,%22resource%22:%7B%22message%22:%7B%22token%22:%22%3Cfcm_token:test%3E%22,%22apns%22:%7B%22live_activity_token%22:%22%3Clive_activity_push_to_start_token%3E%22,%22headers%22:%7B%22apns-priority%22:%2210%22%7D,%22payload%22:%7B%22aps%22:%7B%22timestamp%22:%22%3Ctimestamp%3E%22,%22event%22:%22start%22,%22content-state%22:%7B%22demo%22:1%7D,%22attributes-type%22:%22DemoAttributes%22,%22attributes%22:%7B%22demoAttribute%22:1%7D,%22alert%22:%7B%22title%22:%22test+title%22,%22body%22:%22test+body%22%7D%7D%7D%7D%7D%7D%7D)

Click **Run** to try the sample in the **API Explorer**.

## Update a live activity

To update a live activity remotely using Firebase Cloud Messaging, you need to
obtain a [push
token](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Start-a-Live-Activity-that-supports-push-updates-to-push-tokens)
from Apple. You will also need the [FCM registration
token](https://firebase.google.com/docs/cloud-messaging/ios/client#access_the_registration_token) for the
target app.

To construct a [payload that updates a Live
Activity](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Construct-the-ActivityKit-remote-push-notification-payload),
fill in the
[`apns.payload`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#ApnsConfig) field
from the following code sample to remotely update a live activity using
FCM.  

### REST


```json
{
"message": {
  "token": "<var translate="no">FCM_TOKEN</var>",
  "apns": {
    "live_activity_token": "<var translate="no">LIVE_ACTIVITY_PUSH_TOKEN</var>",
    "headers": {
      "apns-priority": "10"
    },
    "payload": {
      "aps": {
        "timestamp": TIMESTAMP,
        "event": "update",
        "content-state": {
          "test1": 100,
          "test2": "demo"
        },
        "alert": {
          "title": "test title",
          "body": "test body"
        }
      }
    }
  }
}
}
```

<br />

### cURL


```bash
curl -X POST -H "Authorization: Bearer <var translate="no">OAUTH2_ACCESS_TOKEN</var>" -H "Content-Type: application/json" -d '{
"message": {
"token": "<var translate="no">FCM_TOKEN</var>",
"apns": {
  "live_activity_token": "<var translate="no">LIVE_ACTIVITY_PUSH_TOKEN</var>",
  "headers": {
    "apns-priority": "10"
  },
  "payload": {
    "aps": {
      "timestamp": <var translate="no">TIMESTAMP</var>,
      "event": "update",
      "content-state": {
        "test1": 100,
        "test2": "demo"
      },
      "alert": {
        "title": "test title",
        "body": "test body"
      }
    }
  }
}
}
}' https://fcm.googleapis.com/v1/projects/YOUR_PROJECT_ID/messages:send
```

<br />

[Run](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages/send?apix=true&apix_params=%7B%22parent%22:%22projects/%3Cproject_number%3E%22,%22resource%22:%7B%22message%22:%7B%22token%22:%22%3Cfcm_token:test%3E%22,%22apns%22:%7B%22live_activity_token%22:%22%3Clive_activity_push_token%3E%22,%22headers%22:%7B%22apns-priority%22:%2210%22%7D,%22payload%22:%7B%22aps%22:%7B%22timestamp%22:%22%3Ctimestamp%3E%22,%22event%22:%22update%22,%22content-state%22:%7B%22test1%22:100,%22test2%22:%22demo%22%7D,%22alert%22:%7B%22title%22:%22test+title%22,%22body%22:%22test+body%22%7D%7D%7D%7D%7D%7D%7D)

Click **Run** to try the sample in the **API Explorer**.

## End a live activity

To end a live activity using Firebase Cloud Messaging, you need to obtain a [push
token](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Start-a-Live-Activity-that-supports-push-updates-to-push-tokens)
from Apple. You will also need the [FCM registration
token](https://firebase.google.com/docs/cloud-messaging/ios/client#access_the_registration_token)
for the target app.

To construct [a payload that ends a live
activity](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Construct-the-ActivityKit-remote-push-notification-payload),
fill in the
[`apns.payload`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#ApnsConfig) field
from the following code sample to remotely end a live activity using
FCM.  

### REST


```json
{
"message": {
  "token": "<var translate="no">FCM_TOKEN</var>",
  "apns": {
    "live_activity_token": "<var translate="no">LIVE_ACTIVITY_PUSH_TOKEN</var>",
    "headers": {
      "apns-priority": "10"
    },
    "payload": {
      "aps": {
        "timestamp": TIMESTAMP,
        "dismissal-date": DISMISSAL_DATE,
        "event": "end",
        "content-state": {
          "test1": 100,
          "test2": "demo"
        },
        "alert": {
          "title": "test title",
          "body": "test body"
        }
      }
    }
  }
}
}
```

<br />

### cURL


```bash
curl -X POST -H "Authorization: Bearer <var translate="no">OAUTH2_ACCESS_TOKEN</var>" -H "Content-Type: application/json" -d '{
"message": {
"token": "<var translate="no">FCM_TOKEN</var>",
"apns": {
  "live_activity_token": "<var translate="no">LIVE_ACTIVITY_PUSH_TOKEN</var>",
  "headers": {
    "apns-priority": "10"
  },
  "payload": {
    "aps": {
      "timestamp": <var translate="no">TIMESTAMP</var>,
      "dismissal-date": <var translate="no">DISMISSAL_DATE</var>,
      "event": "end",
      "content-state": {
        "test1": 100,
        "test2": "demo"
      },
      "alert": {
        "title": "test title",
        "body": "test body"
      }
    }
  }
}
}
}' https://fcm.googleapis.com/v1/projects/YOUR_PROJECT_ID/messages:send
```

<br />

[Run](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages/send?apix=true&apix_params=%7B%22parent%22:%22projects/%3Cproject_number%3E%22,%22resource%22:%7B%22message%22:%7B%22token%22:%22%3Cfcm_token:test%3E%22,%22apns%22:%7B%22live_activity_token%22:%22%3Clive_activity_push_token%3E%22,%22headers%22:%7B%22apns-priority%22:%2210%22%7D,%22payload%22:%7B%22aps%22:%7B%22timestamp%22:%22%3Ctimestamp%3E%22,%22dismissal-date%22:%22%3Cdismissal_date%3E%22,%22event%22:%22end%22,%22content-state%22:%7B%22test1%22:100,%22test2%22:%22demo%22%7D,%22alert%22:%7B%22title%22:%22test+title%22,%22body%22:%22test+body%22%7D%7D%7D%7D%7D%7D%7D)

Click **Run** to try the sample in the **API Explorer**.