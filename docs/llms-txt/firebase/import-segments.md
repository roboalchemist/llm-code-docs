# Source: https://firebase.google.com/docs/projects/import-segments.md.txt

Firebase provides tools to tailor a user's experience by targeting groups of users through Firebase services such as[Remote Config](https://firebase.google.com/docs/remote-config),[Cloud Messaging](https://firebase.google.com/docs/cloud-messaging), and[In-App Messaging](https://firebase.google.com/docs/in-app-messaging). Using a linked[BigQuery](https://cloud.google.com/bigquery/)account, you can import segments you may have identified outside Firebase to create targeted experiences with Firebase services.

## Set up imported segments

You can import data for your segments into Firebase using Google Cloud[BigQuery](https://cloud.google.com/bigquery/). BigQuery provides several ways to[load data](https://cloud.google.com/bigquery/docs/loading-data), so you are free to choose what works best for your configuration.

![Imported segments dataflow](https://firebase.google.com/docs/projects/images/imported_segments_dataflow.png)

Once the integration is enabled:

- Firebase creates a dataset in BigQuery that you own, but Firebase has read access to.
- Firebase periodically ingests the data, making your updated segments available in theFirebaseconsole for targeting.
- Firebase only has read access to this data. Firebase keeps a copy of this data in its internal storage.
- Any data that is deleted from the BigQuery data set is also deleted from Firebase data storage.

### Enable BigQuery import

1. Go to the[BigQuery integration](https://console.firebase.google.com/project/_/settings/integrations/bigquery)page in theFirebaseconsole.
2. If you haven't previously set up BigQuery integration, follow the on-screen instructions to enable BigQuery.![Integrations screen in the <span class=](https://firebase.google.com/docs/projects/images/enable_bigquery.png)Firebaseconsole"\>
3. Enable the**Imported Segments** toggle.![The imported segments toggle in the inactivated state](https://firebase.google.com/docs/projects/images/enable_imported_segments.png)

When you enable importing segments from BigQuery:

- Firebase automatically creates a new BigQuery[data set](https://cloud.google.com/bigquery/docs/datasets)named`firebase_imported_segments`. This dataset contains empty[tables](https://cloud.google.com/bigquery/docs/tables-intro)named`SegmentMemberships`and`SegmentMetadata`.
- The dataset 'firebase_imported_segments' is also be shared with a Firebase service account with the domain`@gcp-sa-firebasesegmentation.iam.gserviceaccount.com`.
- Firebase runs a job at least every 12 hours to read from this dataset, and may import more frequently than 12 hours.

### Import data into BigQuery

You can use any supported mechanism to[load your data](https://cloud.google.com/bigquery/docs/loading-data)into BigQuery to populate the`SegmentMemberships`and`SegmentMetadata`tables. The data must follow the[schema](https://cloud.google.com/bigquery/docs/schemas)described below:  

### SegmentMemberships

    [
      {
        "name": "instance_id",
        "type": "STRING"
      },
      {
        "name": "segment_labels",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "update_time",
        "type": "TIMESTAMP"
       }
    ]

**instance_id** : The[Firebase installation ID](https://firebase.google.com/docs/projects/manage-installations)for a specific app install. You'll need to[retrieve the installation ID](https://firebase.google.com/docs/projects/manage-installations#retrieve_client_identifiers)for each app install that you want to include in a segment, and use those values to populate this field.

**segment_labels** : The segments that devices (`"instance_id"`) are included in. These don't have to be human-friendly and can be short to reduce BigQuery storage usage. There must be a corresponding entry in the`SegmentMetadata`table for each`"segment_labels"`used here. Note this is plural, whereas the`SegmentMetadata`table has`"segment_label"`.

**update_time**: Currently not used by Firebase, but can be used to delete older segment memberships from BigQuery that aren't used anymore.

### SegmentMetadata

    [
       {
          "name": "segment_label",
          "type": "STRING"
       },
       {
          "name": "display_name",
          "type": "STRING"
       }
    ]

**segment_label** : Identifies a particular segment. There must be an entry in this table for every segment listed in the`SegmentMemberships`table. Note this is singular, whereas the SegmentMemberships table has`"segment_labels"`.

**display_name** : A human-readable, UI-friendly name for the segment. This is used to label your segment in theFirebaseconsole.

### Set up billing for BigQuery

If you are trying out the new feature for an app with very few installations, you may only need to set up the[BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox).

However, if you are using this for a production app with many users, you must set up[billing for BigQuery usage](https://cloud.google.com/bigquery/pricing)to pay for storage as well as the mechanism used to load data into BigQuery. You will not be charged for any reads initiated by Firebase.

### Deactivate the integration

To deactivate this integration, go to the[BigQuery integration](https://console.firebase.google.com/project/_/settings/integrations/bigquery)page in theFirebaseconsole and deactivate the**Custom segments**toggle.
| **Caution:** Disabling this integration will delete any Firebase copies of imported segment data in its storage for your project and deactivate the data ingestion job. This may impact any Firebase services using imported segments for targeting.**This does not delete any data from Big Query.**You are still responsible for any data in BigQuery, including storage costs.

## Use imported segments

Once the data is ingested, it will be available in theFirebaseconsole for targeting with services such as Remote Config or In-App Messaging. This works just like targeting with properties orGoogle Analyticsaudiences.

![Example of using imported segments with the notification composer](https://firebase.google.com/docs/projects/images/use_segments_with_notifications.png)

You can use "Imported segment(s)" as one of the targetable attributes and segments you imported will be available for selection. They also include an estimate of the number of app instances that belong to each segment.

An estimate of the number of instances that match the entire targeting criteria is also available. This is updated as you make any changes to the targeting criteria.

## Use cases

There are a number of ways you might use imported segments to create targeted user experiences. This section outlines some common scenarios where you might wish to use this feature.

### Send notifications to a group of users

Imagine you have an app that allows in-app purchases with a shopping cart. You might also use custom-built or third-party analytics solutions (ones not powered byGoogle Analytics) to collect various metrics associated with user behavior in your app. Using these metrics, you could identify a group of users who have added items to the cart, but not completed checkout.

Now imagine you want to useFirebase Cloud Messagingto send a notification to these users to remind them they have items in their cart. You can create a segment called "incomplete-checkout" and include these users, identified by theirFirebaseinstallation ID, and upload it to BigQuery to share with Firebase.

Once Firebase ingests this data, it is available in the Notifications composer where you can create a new notification campaign targeting "incomplete-checkout" to send a message nudging the users to complete checkout.

### Configure an app for a subset of users

Suppose you use an in-house analytics solution that indicates some users are having trouble navigating the app. To help those users, you want to configure the app behavior for these users to include a short tutorial video.

You can incorporateRemote Configin your app and use a parameter, named something like "needs_help", in your app to[conditionally show](https://firebase.google.com/docs/remote-config/use-cases#test_new_functionality_on_a_limited_testing_group)the tutorial video.

Using your analytics data, create a segment named "troubled-users" and include appropriate users, identified byFirebaseinstallation ID. Then upload this segment and its members to BigQuery to share with Firebase.

Once Firebase ingests this data, it is made available in theRemote Configconsole as a targetable segment. You can then create a condition targeting "troubled-users" and set the "needs_help" parameter to true for this condition and false by default. Once this config is published, the app shows the tutorial video only to users in the "troubled-users" segment.

### Follow user journeys across devices

Imagine you built a restaurant-review app using Firebase andGoogle Analytics. Using metrics collected, you find users often access the app from both a mobile device and a tablet. You also discover that your users prefer to write reviews on the tablet, while they may read reviews from any device.

Some users start writing a review on their phone and give up, possibly due to the smaller form factor. You decide to send a notification to such users on their tablets prompting them to finish their reviews.

To do this, you could set an internally-generated reviewerId as the UserId usingGoogle Analyticsfor signed-in users and trigger an event to identify cancelled reviews. You can then export your app'sGoogle Analyticsdata to BigQuery.

By analyzing this data in BigQuery, you can identify theFirebaseinstallation ID of tablets for users who didn't finish writing a review on their phone. You can name this group "tablets-of-users-who-cancelled-on-phone" and upload the segment to BigQuery to share the list of members with Firebase.

Once Firebase ingests this data, it is available in the Notifications composer as a targetable segment. You can then create a new notifications campaign targeting "tablets-of-users-who-cancelled-on-phone" to send a message nudging these users to complete their review on their tablets.