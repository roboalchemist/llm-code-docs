# Source: https://firebase.google.com/docs/functions/use-cases.md.txt

Cloud Functions gives developers access to Firebase and Google Cloud
events, along with
scalable computing power to run code in response to those events. While it's
expected that Firebase apps will use Cloud Functions in unique ways to meet
their unique requirements, typical use cases might fall into these areas:

- [Notify users when something interesting happens](https://firebase.google.com/docs/functions/use-cases#notify_users_when_something_interesting_happens).
- [Perform database sanitization and maintenance](https://firebase.google.com/docs/functions/use-cases#perform_database_sanitization_and_maintenance).
- [Execute intensive tasks in the cloud instead of in your app](https://firebase.google.com/docs/functions/use-cases#execute_intensive_tasks_in_the_cloud_instead_of_in_your_app).
- [Integrate with third-party services and APIs](https://firebase.google.com/docs/functions/use-cases#integrate_with_third-party_services_and_apis).

Review the use cases and examples for each category that interests
you, and then proceed to our [Get Started](https://firebase.google.com/docs/functions/get-started) tutorial
or to specific how-to guides
for [authentication events](https://firebase.google.com/docs/functions/auth-events),
[analytics events](https://firebase.google.com/docs/functions/analytics-events), and more.

## Notify users when something interesting happens

Developers can use Cloud Functions to keep users engaged and up to date
with relevant information about an app. Consider, for example, an app that
allows users to follow one another's activities in the app. Each time a user
adds themselves as a follower of another user, a write occurs in the
Realtime Database. Then this write event could trigger a function
to create Firebase Cloud Messaging (FCM) notifications to let the appropriate
users know that they have gained new followers.

![Diagram showing the app flow described below](https://firebase.google.com/static/docs/functions/images/notify.png)

1. The function triggers on writes to the Realtime Database path where followers are stored.
2. The function composes a message to send via .
3. sends the notification message to the user's device.

To review working code, see the sample code in GitHub:

- Node.js: [fcm-notifications](https://github.com/firebase/functions-samples/tree/main/Node/fcm-notifications)
- Python: [fcm-notifications](https://github.com/firebase/functions-samples/tree/main/Python/fcm-notifications)

### Other interesting notification use cases

- Send confirmation emails to users subscribing to a newsletter.
- Send a welcome email when a user completes signup.
- Send an SMS confirmation when a user creates a new account.

## Perform database sanitization and maintenance

With Cloud Functions database event handling, you can modify Realtime Database or
Cloud Firestore in response to user behavior, keeping the system in your desired
state. For example, you could monitor write events and change the format
(for example, change to all uppercase) of certain strings in users' messages.
Here's how that could work:

![Diagram showing the app flow described below](https://firebase.google.com/static/docs/functions/images/sanitization.png)

1. The function's database event handler listens for write events on a specific path, and retrieves event data containing the text of a messages.
2. The function processes the text to change strings to uppercase.
3. The function writes the updated text back to the database.

To review working code, see the sample code in GitHub:

- Node.js: [uppercase-rtdb](https://github.com/firebase/functions-samples/tree/main/Node/quickstarts/uppercase-rtdb)
- Python: [uppercase-rtdb](https://github.com/firebase/functions-samples/tree/main/Python/quickstarts/uppercase-rtdb)

### Other database sanitization and maintenance use cases

- Purge a deleted user's content from Realtime Database.
- Limit the number of child nodes in a Firebase database.
- Track the number of elements in a Realtime Database list.
- Copy data from Realtime Database to Google Cloud BigQuery.
- Convert text to emoji.
- Manage computed metadata for database records.

## Execute intensive tasks in the cloud instead of in your app

You can take advantage of Cloud Functions to offload to the Google
cloud resource-intensive work (heavy CPU or networking) instead of running it
on a user's device, improving the responsiveness of your app.
For instance, you could write a function
to listen for image uploads to Cloud Storage, download the image to the instance
running the function, modify it, and upload it back to Cloud Storage. Your
modifications could include resizing, cropping, or converting images with tools
like [sharp](https://www.npmjs.com/package/sharp) or
[Pillow](https://pillow.readthedocs.io/en/stable/).

![Diagram showing the app flow described below](https://firebase.google.com/static/docs/functions/images/intensive.png)

1. A function triggers when an image file is uploaded to Cloud Storage.
2. The function downloads the image and creates a thumbnail version of it.
3. The function writes that thumbnail location to the database, so a client app can find and use it.
4. The function uploads the thumbnail back to Cloud Storage in a new location.
5. The app downloads the thumbnail link.

For a walkthrough of an image processing example, see the guide to
[handling Cloud Storage events](https://firebase.google.com/docs/functions/gcp-storage-events?gen=2nd).

### Other examples of batch jobs in the Firebase cloud

- Periodically delete unused Firebase accounts [Node.js](https://github.com/firebase/functions-samples/tree/main/Node/delete-unused-accounts-cron) \| [Python](https://github.com/firebase/functions-samples/tree/main/Python/delete-unused-accounts-cron).
- Automatically back up uploaded images [Node.js](https://github.com/firebase/functions-samples/tree/main/Node/taskqueues-backup-images) \| [Python](https://github.com/firebase/functions-samples/tree/main/Python/taskqueues-backup-images).
- Send bulk email to users.
- Aggregate and summarize data periodically.
- Process a queue of pending work.

## Integrate with third-party services and APIs

Cloud Functions can help your app work better with other services by
calling and exposing web APIs. For instance, an app used for collaboration on
development could post GitHub commits to a workgroup chat room.

![Diagram showing the app flow described below](https://firebase.google.com/static/docs/functions/images/commit.png)

1. A user pushes commits to a GitHub repo.
2. An HTTPS function triggers via the [GitHub webhook API](https://developer.github.com/webhooks/).
3. The function sends a notification of the commit to a team Slack channel.

### Other ways to integrate with third-party services and APIs

- Use Google [Cloud Vision API](https://cloud.google.com/vision/) to analyze and tag uploaded images.
- Translate messages using Google Translate.
- Use [custom auth](https://firebase.google.com/docs/auth/where-to-start#custom-auth) to sign in users.
- Send a request to a webhook on Realtime Database writes.
- Enable full-text search on Realtime Database elements.
- Process payments from users.
- Create auto-responses to phone calls and SMS messages.
- Create a chatbot using Google Assistant.