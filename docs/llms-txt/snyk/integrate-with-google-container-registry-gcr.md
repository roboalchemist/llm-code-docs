# Source: https://docs.snyk.io/scan-with-snyk/snyk-container/container-registry-integrations/integrate-with-google-container-registry-gcr.md

# Integrate with Google Container Registry (GCR)

{% hint style="warning" %}
Google Container Registry (GCR) has been [officially deprecated](https://cloud.google.com/container-registry/docs/release-notes#May_15_2023) by Google and is no longer supported. Google has replaced GCR with the new Google Artifact Registry (GAR). All Snyk customers should **immediately** migrate to the [Snyk GAR integration](https://docs.snyk.io/scan-with-snyk/snyk-container/container-registry-integrations/integrate-with-google-artifact-registry-gar).\
\
Note that Google currently redirects `gcr.io` paths to GAR. Your legacy Snyk GCR integration may continue to work if the credentials provided to Snyk also have the `roles/artifactregistry.reader` and `roles/resourcemanager.projects.list` roles authorized for them. However, this redirect may stop functioning in the future. We strongly recommend that you migrate to the [Snyk GAR integration](https://docs.snyk.io/scan-with-snyk/snyk-container/container-registry-integrations/integrate-with-google-artifact-registry-gar) at the earliest to avoid any unwanted service interruptions.
{% endhint %}

Snyk integrates with Google Container Registry (GCR) so you can import your Projects, monitor your containers for vulnerabilities, and fix vulnerabilities as you work. Snyk tests the Projects you have imported for any known security vulnerabilities at a frequency you control. GCR integration works similarly to other Snyk integrations.

## Enable permissions to access GCR

Enable the [Cloud Resources Manager API](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com?q=cloud%20resource%20manager\&id=16f5d23e-c895-4b9d-88e4-864c1766636f\&project=next-for-integration-testing) for the Google account you plan on integrating with Snyk.

From the relevant project in Google, ensure you have created a service account for this Snyk integration.

To enable GCR permissions:

1. Go to the Google Cloud Platform Console [Credentials](https://console.cloud.google.com/apis/credentials) page, select the Project that you want to integrate with, and then select setting up a new service account key.
2. From the view that opens choose the service account from the dropdown list that you created for this integration and configure a new key for that account with these values:
   * **Service account name** - assign a unique name for the account to help you remember its uses later on.
   * **Role** - Storage Object Viewer (roles/storage.objectViewer)
   * **Service account ID** - leave empty
   * **Key type** - JSON
3. Click **Create** to generate the key for your Project.
4. Copy the entire contents of the JSON file. Save the data you copied to paste it when configuring integration for GCR.

## Configure GCR integration

To configure the GCR integration:

1. Navigate to your Snyk Organization, and navigate to **Integrations** > **GCR**.
2. From the GCR hostname, enter the [registry storage region](https://cloud.google.com/container-registry/docs/pushing-and-pulling) for the images you want to scan in the format region.gcr.io, for example, gcr.io or asia.gcr.io.
3. Paste the entire contents of the JSON key file you created from Google into the JSON key file field in your Snyk account, as shown in the following screenshot.
4. Click **Save**.

Snyk checks the credentials, and when the check is successful, the page reloads with a notification that the connection succeeded.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b8d8b04c86eef46d9c7597852a3a52e28700e3fc%2Fuuid-47cf04cb-248e-5d0f-d35a-f36fbb624614-en.png?alt=media&#x26;token=e4758a14-6b06-4bc5-a7c5-d2949069e74b" alt="GCR account credentials"><figcaption><p>GCR account credentials</p></figcaption></figure>

## Add images from GCR

{% hint style="info" %}
You must be onboarded to your Organization by an administrator and have configured the integration with your GCR repository.
{% endhint %}

Snyk tests and monitors Google Container Registry (GCR) container images by evaluating root folders and custom file locations.

To add images from GAR:

1. In the Snyk Web UI, navigate to the Organization you want to manage.
2. Navigate to **Projects** > **Add Projects**. The list of integrations already configured in your account opens. The view displays all of the available images for the registry to which you connected, grouped by each of your repositories.
3. Select single or multiple images by using any or all of the following methods:
   * Type the name of a single image for import in the **Image Name** field.
   * Select any of the repositories for which you want to import all of the associated images.
   * Expand and collapse repositories to select multiple images across multiple repositories.
4. Click **Add selected repositories**. As the images are imported, a status bar appears at the top of the page. You can continue working while Snyk imports the images.

When the import ends, a notification of success or failure appears at the top of the page. Click **Refresh** to view the **Projects** page with the newly imported images. The images are grouped by repository and linked individually to a detailed **Projects** page.

You can now connect your Git repo to this Project in order to use your Dockerfile for enriched fix advice. For more information, see [Adding your Dockerfile and testing your base image](https://docs.snyk.io/scan-with-snyk/snyk-container/scan-your-dockerfile/detect-vulnerable-base-images-from-your-dockerfile).

GCR files are indicated with a unique icon. You can now filter to view only those Projects.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-cc2aee926271d6bd8742ff652318051390944e5f%2FScreenshot%202023-03-31%20at%2018.06.20.png?alt=media" alt=""><figcaption><p>Examples of GCR Projects</p></figcaption></figure>

{% hint style="info" %}
For application vulnerabilities within container images, any changes to the application will not be reflected with a manual or recurring retest. You must re-import the image. For more information, see [Detecting application vulnerabilities in container images](https://docs.snyk.io/scan-with-snyk/snyk-container/use-snyk-container/detect-application-vulnerabilities-in-container-images).
{% endhint %}
