# Source: https://firebase.google.com/docs/ml/ios/secure-api-key.md.txt

If your Apple app uses one of Firebase ML's cloud APIs, before you launch your app
in production, you should take some additional steps to prevent unauthorized
API access.

## 1. Reduce the scope of existing API keys

First, configure your existing API keys to disallow access to the Cloud Vision
API:

1. Open the [Credentials](https://console.cloud.google.com/apis/credentials?project=_) page of the
   Google Cloud console. When prompted, select your project.

2. For each existing API key in the list, open the editing view.

3. In the *API restrictions* section, select **Restrict key** , then add to the
   list all of the APIs to which you want the API key to have access. Make sure
   to ***not*** include the Cloud Vision API.

   When you configure an API key's *API restrictions* , you are explicitly
   declaring the APIs to which the key has access. **By default, when the *API
   restrictions* section has *Don't restrict key* selected, an API key can be
   used to access any API that is enabled for the project.**

Now, your existing API keys will not grant access to cloud ML services, but each
key will continue to work for any APIs that you added to its *API restrictions*
list.

Note that if you enable any additional APIs in the future, you must add them to
the *API restrictions* list for the applicable API key.

## 2. Create a new API key for use with Firebase ML

Next, create a new API key for Firebase ML that only allows calls to the
Cloud Vision API:

1. Return to the [Credentials](https://console.cloud.google.com/apis/credentials) page. Be sure your
   Firebase project is still selected.

2. Click **Create credentials \> API key** . Take note of the new API key, then
   click **Restrict key**.

3. In the *API restrictions* section, select **Restrict key** , then add to the
   list ***only*** the Cloud Vision API.

This API key grants access only to the Cloud Vision API and can be used by
Firebase ML to access cloud-based models.

## 3. Recommended: Reduce the Cloud Vision API's quota

To help mitigate the consequences of a compromised key, you should reduce the
Cloud Vision API's per-user quota from its default setting. To do so:

1. Open the [Cloud Vision API Quotas](https://console.cloud.google.com/apis/api/vision.googleapis.com/quotas?project=_) page of the
   Google Cloud console. When prompted, select your project.

2. In the **Requests** section, set the **Requests per minute per user** quota
   to something reasonable for your app. For example, if your app involves
   uploading a picture of a document to get back its text, it's unlikely that a
   user will do that more than once every few seconds, so a quota of 30-40
   would probably be safe.

   Note that in this context "requests per user" refers to requests from a
   single IP address. You might need to consider this if you expect multiple
   users to use your app at the same time from behind a NAT.

## 4. Call Cloud APIs using your Firebase ML API key

Finally, in your app, configure Firebase ML to use your new API key.

Because the Firebase ML API key allows unauthenticated access to the Cloud Vision
API, it's important to keep the key confidential to prevent unauthorized use and
charges to your billing account. To do so, you should refrain from including
your API key in your app binary. Instead, at app runtime, verify that a known
good user is signed in, and only then, retrieve the API key from a server.

Even when these practices are observed, it is possible for an API key to be
compromised. You should take steps to help mitigate the consequences of a
compromised key, such as reducing the API's per-user quota as described above,
implementing key rotation policies, and issuing different keys to different
groups of users.

After your app has safely acquired the API key, when you want to call an
Firebase ML Cloud API, specify the key:

### Swift

    if let cloudVisionKey = getYourApiKey() {  // See note above about securing your API key
        let options = VisionCloudDetectorOptions()
        options.apiKeyOverride = cloudVisionKey
        let cloudDetector = Vision.vision().cloudLandmarkDetector(options: options)
    }

### Objective-C

    NSString *cloudVisionKey = [self getYourApiKey];  // See note above about securing your API key
    if (cloudVisionKey != nil) {
        FIRVisionCloudDetectorOptions *options =
                [[FIRVisionCloudDetectorOptions alloc] init];
        options.APIKeyOverride = cloudVisionKey;
        FIRVisionCloudLandmarkDetector *landmarkDetector =
                [vision cloudLandmarkDetectorWithOptions:options];
    }

In addition, you should follow the general advice in
[Securing an API key](https://cloud.google.com/docs/authentication/api-keys#securing_an_api_key).

## Next steps

See the [launch checklist](https://firebase.google.com/support/guides/launch-checklist) for information on
preparing your app to launch when using other Firebase features.