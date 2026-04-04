# Source: https://docs.luciq.ai/product-guides-and-integrations/integrations/store-integrations.md

# Store Integrations

To integrate your App Store or Play Store account, you'll need to navigate to the settings page in the side navigation bar.

Depending on the OS of the current application, you'll find the relevant store integration.

<figure><img src="https://files.readme.io/5f1777e7b51546c14a971a906401ef4a182eff5a99560b337a5120817be0e0c5-store-integration-5.png" alt=""><figcaption></figcaption></figure>

### iOS - App Store

#### Create Integration

1. To integrate with the App Store, first generate an API Key with “App Manager“ access.\
   After generating the key, enter your Key ID and Issuer ID, then upload your .p8 file.

<figure><img src="https://files.readme.io/b1eaf73-image.png" alt=""><figcaption></figcaption></figure>

2. **Choose Bundle ID:** We'll fetch all bundle IDs associated with the created Key ID.

<figure><img src="https://files.readme.io/2653c5eaca2febb020c1edfe4c7323ec92553cdab03e8ee4d271bfb72b1eb245-store-integration-15.png" alt=""><figcaption></figcaption></figure>

3. You now have a successful connection.

<figure><img src="https://files.readme.io/5735241fbcebea23666b7c75bc2540113f53911d527075e6e866c1a896bc73ed-store-integration-10.png" alt=""><figcaption></figcaption></figure>

#### How to generate an API Key for App Store Connect?

1. Log in to [App Store Connect](https://appstoreconnect.apple.com/).
2. Select Users and Access, and then select the Integrations tab.
3. Click Generate API Key or the Add (+) button.
4. Enter a name for the key. The name is for your reference only and is not part of the key itself.
5. Under Access, select the **App Manager or Admin** role for the key
6. Click Generate.

The new key's name, key ID, download link, and other information will appear on the page. The private key is available for download a single time. You can check Apple's documentation for it [here](https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api).

<figure><img src="https://files.readme.io/ad8ab12-image.png" alt="App Store Connect Dashboard"><figcaption><p><em>App Store Connect Dashboard</em></p></figcaption></figure>

{% hint style="info" %}

#### How we prioritize the security of your integration?

* **API Key Management**: We follow best practices for safeguarding API keys, including secure storage by encrypting your key and only decrypting it at runtime.
* **Data Encryption**: We use industry-standard encryption for data transmitted between Luciq and App Store Connect to keep your information secure during transit.
  {% endhint %}

#### Edit Integration

1. After creating the integration successfully, you can edit the integration by choosing another bundle ID associated with the Key ID by clicking on the pencil icon.

<figure><img src="https://files.readme.io/5735241fbcebea23666b7c75bc2540113f53911d527075e6e866c1a896bc73ed-store-integration-10.png" alt=""><figcaption></figcaption></figure>

2. Choose the new Bundle ID.

<figure><img src="https://files.readme.io/0997453bc17d28684d6b2539c3cd326d6152eb3b005ef9b77e26d53c89c15552-store-integration-11.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
You will not be able to edit the key details.
{% endhint %}

#### Delete Integration

You can delete the Bundle ID associated with our dashboard and we won’t be able to fetch any details from the store for this Bundle ID.

<figure><img src="https://files.readme.io/fb4ae63bc0695156013b47683094eef8919725333acd9ed7fd3eed544654affc-store-integration-4.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Deleting this integration will not delete the key from the dashboard. The key will be permanently deleted once all integrations using this key are deleted.
{% endhint %}

### Android - Google Play

{% hint style="info" %}

#### You can refer to Google’s guide on getting started with Google Play Developer [API](https://developers.google.com/android-publisher/getting_started)

{% endhint %}

#### Create Integration

1. **Create a Google Cloud Project**. You can skip this step if you already have a Google Cloud Project you want to use.\
   Otherwise, you can create a project in the [Google Cloud Console](https://console.cloud.google.com/projectcreate).<br>

   <figure><img src="https://files.readme.io/793574d-image.png" alt=""><figcaption></figcaption></figure>
2. **Enable the Google Play Developer API for your Google Cloud Project**
   1. Go to the Google Play Developer API [page](https://console.developers.google.com/apis/api/androidpublisher.googleapis.com/) in Google Cloud Console.
   2. Click **Enable**<br>

      <figure><img src="https://files.readme.io/2326a42-image.png" alt=""><figcaption></figcaption></figure>
3. **Set up a service account** with appropriate Google Play Console permissions to access the Google Play Developer API. You can create a [service account](https://developers.google.com/accounts/docs/OAuth2ServiceAccount) from the Google Play Console.
   1. In the Google Cloud Console, go to [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
   2. Click "Create service account" and follow the steps.

      <figure><img src="https://files.readme.io/0502be0cc085827f85be4b5a190edf487b7f5f46b4ec3b5be2741227da914ab1-image.png" alt=""><figcaption></figcaption></figure>

      <figure><img src="https://files.readme.io/83cd9b1523b9cd83cb65dd351791bc073a8269c881f886a516e8891a117e8c38-image.png" alt=""><figcaption></figcaption></figure>
   3. Go to the [Users & Permissions](https://play.google.com/console/users-and-permissions) page on the Google Play Console.
   4. Click "Invite new users".

      <figure><img src="https://files.readme.io/55590269ac082cad2a88b2e3291892ba15d15c296f7606e8e2c6a0cc3954b40e-image.png" alt=""><figcaption></figcaption></figure>
   5. Put an email address for your service account in the email address field and grant the necessary rights to perform actions.
   6. You'll need to allow the Release to production, exclude devices, and use Play App Signing permission to be able to use rollout management .
   7. Click "Invite user".
4. **Generate a key**
   1. **Create a new key**: After you've granted permissions, click on the service account name and then select the "Keys" tab. Click the "Create new key" button.

      <figure><img src="https://files.readme.io/f5edb60c7f5d4119596056657ea337d34fbd8ffc7f3da8c093bc413cf6a3a1fc-image.png" alt=""><figcaption></figcaption></figure>
   2. Select "JSON" as the key type and click "Create".

      <figure><img src="https://files.readme.io/fbe83858e125fc43a52c980c0237e6c16d0b55fbd4c98f3e89c88073b091c4bb-image.png" alt=""><figcaption></figcaption></figure>
   3. Download Service account key file: Your service account key file should start downloading; you’ll need to upload that key on our dashboard.
5. **Upload key to Luciq**.
   1. To integrate a Play Store account with Luciq, you'll need to navigate to the settings page in the side navigation bar.
   2. Click on "Connect app".

      <figure><img src="https://files.readme.io/26d0307240413d3901c7ab6e28b6347fb90c4704cb0562ff3055a4c5cdfd594d-store-integration-3.png" alt=""><figcaption></figcaption></figure>
   3. You’ll need to upload the Package name and Key in the Luciq dashboard.

      <figure><img src="https://files.readme.io/a94418b-image.png" alt=""><figcaption></figcaption></figure>
6. Now you have a successful connection!

   <figure><img src="https://files.readme.io/a1e14f1df032da2f2357f2a068bb8a6e47536aff0f5a5184acb8fd1fa9a07ede-store-integration-6.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}

## How we prioritize the security of your integration

* **API Key Management**: We follow best practices for safeguarding API keys, including secure storage by encrypting your key and only decrypting it at runtime
* **Data Encryption**: We use industry-standard encryption for data transmitted between Luciq and the Play Store Console to keep your information secure during transit.
  {% endhint %}

#### Edit Integration

1. After creating the integration successfully, you can edit the integration by entering another package name associated with the Key ID by clicking on the pencil icon.

<figure><img src="https://files.readme.io/a1e14f1df032da2f2357f2a068bb8a6e47536aff0f5a5184acb8fd1fa9a07ede-store-integration-6.png" alt=""><figcaption></figcaption></figure>

2. Enter the other package name.

<figure><img src="https://files.readme.io/aafccee-image.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
You will not be able to edit the key details.
{% endhint %}

#### Delete Integration

You can also delete the package name associated with the Luciq dashboard, and we won’t be able to fetch any details from the store for this package name.

<figure><img src="https://files.readme.io/78b4d7d-image.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Deleting this integration will not delete the key from the dashboard. The key will be permanently deleted once all integrations using this key are deleted.
{% endhint %}
