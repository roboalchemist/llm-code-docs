# Source: https://firebase.google.com/docs/database/locations.md.txt

When you provision a Realtime Database instance, you must choose a *location* for the
instance. To reduce latency and increase availability, store your data close to
the users and services that need it.

If your project is on the pay-as-you-go Blaze pricing plan, then you can optionally
[create multiple databases](https://firebase.google.com/docs/database/usage/sharding) in your project, each
with its own location setting.

Be aware that once you provision a database instance, you cannot change its
location setting.

> [!NOTE]
> **Note:** The locations of your Realtime Database instances do *not* control the location setting of any other resource in your project, including Cloud Firestore database instances or Cloud Storage buckets.

In the following table, find the supported locations for Realtime Database instances
along with their associated database URL formats.

| **Region name** | **Region description** | **Database URL format** |
|---|---|---|
| `us-central1` | Iowa | `DATABASE_NAME.firebaseio.com` |
| `europe-west1` | Belgium | `DATABASE_NAME.europe-west1.firebasedatabase.app` |
| `asia-southeast1` | Singapore | `DATABASE_NAME.asia-southeast1.firebasedatabase.app` |