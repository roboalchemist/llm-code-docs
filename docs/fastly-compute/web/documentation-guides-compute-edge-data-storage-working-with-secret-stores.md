# Source: https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/

Title: Working with secret stores | Fastly Documentation

URL Source: https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/

Markdown Content:

1. [Home](https://www.fastly.com/documentation/)
2. [Guides](https://www.fastly.com/documentation/guides/)
3. [Compute](https://www.fastly.com/documentation/guides/compute/)
4. [Edge Data Storage](https://www.fastly.com/documentation/guides/compute/edge-data-storage/)

* English
* 日本語

Secret stores are a type of versionless container that give you a secure location to place credentials so they are available to [Compute services](https://www.fastly.com/documentation/guides/getting-started/services/working-with-compute-services) operating at the Fastly edge. Once [linked to a service](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#linking-secret-stores-to-a-service), any updates you make to the store are automatically reflected on the service without needing to increment the service's version. Changes immediately impact all service versions, including the active one.

You can also create and work with secret stores [via the API](https://www.fastly.com/documentation/reference/api/services/resources/secret-store/).

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#prerequisites)Prerequisites
--------------------------------------------------------------------------------------------------------------------------------

Secret Store is only available for Fastly's Compute services, not for CDN (VCL-based) services.

Make sure you review the limitations for using edge data stores in the [Compute resource limits](https://docs.fastly.com/products/compute-resource-limits#edge-data-storage-limitations).

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#limitations-and-considerations)Limitations and considerations
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Before working with secret stores, keep the following things in mind:

* Trials for Compute include one secret store.
* Paid accounts include a minimum of 10 secrets regardless of the number of stores with additional secrets available for purchase.
* Secrets are limited to 5 secret reads per Compute request. To increase this limit contact [Fastly Support](https://support.fastly.com/).
* Secret stores support a maximum size of 64KB per secret.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#creating-a-secret-store)Creating a secret store
----------------------------------------------------------------------------------------------------------------------------------------------------

Creating a secret store requires you to create at least one key-value pair containing secrets and then associating the store with a service. To create a new secret store and add secrets, follow these steps:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Secret stores**](https://manage.fastly.com/resources/secret-stores).
3. Click **Create store**.
4. In the **Store name** field, enter a name for the store and then click **Create**.
5. Click **Add item**.
6. In the **Key** field, enter the key. **In the**Value**field, enter a value in the text field or click**Upload file** to navigate to a file on your system using the file picker. Alternatively, drag and drop a file directly into the drag and drop area.
7. Click **Save**.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#linking-secret-stores-to-a-service)Linking secret stores to a service
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once you've created a secret store, you can link it to a service from the Resources controls or from the service configuration for the service, creating a _resource link_. By creating a resource link, any future updates made to the store are automatically reflected on the linked services.

### [](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#creating-a-resource-link-from-the-resources-controls)Creating a resource link from the Resources controls

To link a secret store to a service from the **Resources** controls:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Secret stores**](https://manage.fastly.com/resources/secret-stores).

3. Click the name of the store you want to link to a service.

4. From the **Options** menu, click **Link service**.

5. Select the checkbox next to the services you want to link to your store. Use the search box to search for services by name or ID.

6. Click **Next**.

7. From the version menu, select which version of the service to link to. By default, the system will assume you want to clone the most recently active version of your service. Alternatively, you can choose an existing draft version.

8. Select one of the following options to finish linking the store to your service:

    *   **Link only:** links the store to the selected service versions but leaves any cloned or draft versions deactivated so you can activate them at a later time.

    *   **Link and activate:** links the store to the selected service versions and activates those versions at the same time.

A success message appears once the store is linked to the service.

1. Finally, do one of the following:

    *   If you chose **Link only**, click **Finish** to leave the cloned or draft service versions deactivated or click **Activate versions** if you're now ready to activate.
    *   If you chose **Link and activate**, click **Confirm and activate** to activate the cloned or draft service versions linked to the store.

You can immediately start referencing the store in your edge logic.

### [](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#creating-a-resource-link-from-the-service-configuration)Creating a resource link from the service configuration

To link a secret store to a service from the service configuration:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. From the [**Home**](https://manage.fastly.com/home) page, select the appropriate service. You can use the search box to search by ID, name, or domain.
3. Click **Edit configuration** and then select the option to clone the active version.
4. Click **Service configuration**.
5. From the **Linked resources** options in the on-page navigation, click **Secret stores**.
6. From the **Link Secret Store to service** menu, select the secret store you want to link to the service. A success message appears indicating the store is linked to your service.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#unlinking-secret-stores)Unlinking secret stores
----------------------------------------------------------------------------------------------------------------------------------------------------

You can unlink a secret store from a service from the service configuration.

To unlink a secret store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. From the [**Home**](https://manage.fastly.com/home) page, select the appropriate service. You can use the search box to search by ID, name, or domain.
3. Click **Service configuration**.
4. From the **Resources** options in the on-page navigation, click **Secret stores**.
5. Click **Unlink from service** next to the secret store you want to unlink from your service.
6. Click **Confirm and unlink**. A new, draft version of the service is created.
7. [Activate the service](https://www.fastly.com/documentation/guides/getting-started/services/working-with-compute-services#editing-and-activating-versions-of-services) to finalize unlinking the secret store.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#editing-a-secret-store)Editing a secret store
--------------------------------------------------------------------------------------------------------------------------------------------------

You can edit the secrets within the story or add new secrets to the store from **Resources**>[**Secret stores**](https://manage.fastly.com/resources/secret-stores). You can also access this page by clicking **Edit in Resources** when accessing a secret store from the service configuration.

To edit secrets within a store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Secret stores**](https://manage.fastly.com/resources/secret-stores).
3. Click the name of the store you want to edit.
4. Click the pencil ![Image 1: Pencil icon](https://www.fastly.com/documentation/static/9680021d4e04d4ec658b7bbe97a8a944/pencil.png) to the right of the key you want to edit.
5. Edit the key value as necessary. Click **Upload file** to navigate to the file on your system using the file picker. Alternatively, drag and drop your key file directly into the drag and drop area.
6. Click **Save**.

To add new secrets to a secret store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Secret stores**](https://manage.fastly.com/resources/config-stores).
3. Click the name of the store you want to edit.
4. Click **Add item**.
5. Enter the key and the value in the appropriate fields and then click **Save**.
6. Repeat to add additional key-value pairs as necessary.

The changes you make will be immediately applied to your configuration including any deployed service versions associated with the secret store.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#deleting-a-secret-store)Deleting a secret store
----------------------------------------------------------------------------------------------------------------------------------------------------

You can delete a secret store at any time. Before deleting a secret store:

* Unlink the secret store from your services. If the secret store is linked to any service, an error will appear when you try to delete the store.
* Update any custom logic that references the key-value pairs in the secret store. Deleting a secret store also deletes all key-value pairs within the store.

To delete a secret store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Secret stores**](https://manage.fastly.com/resources/secret-stores).
3. Click the name of the store you want to delete.
4. From the **Options** menu, click **Delete store**.
5. Click **Confirm and delete**.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#related-content)Related content
------------------------------------------------------------------------------------------------------------------------------------

* [Edge Data Storage](https://docs.fastly.com/products/edge-data-storage)
* [Dynamic configuration data for Fastly services](https://www.fastly.com/documentation/guides/concepts/dynamic-config)
* [Edge Data Storage API documentation](https://www.fastly.com/documentation/reference/api/services/resources/)
* [Resource links API documentation](https://www.fastly.com/documentation/reference/api/services/resource/)

### On this page

* [Prerequisites](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#prerequisites)
* [Limitations and considerations](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#limitations-and-considerations)
* [Creating a secret store](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#creating-a-secret-store)
* [Linking secret stores to a service](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#linking-secret-stores-to-a-service)
  * [Creating a resource link from the Resources controls](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#creating-a-resource-link-from-the-resources-controls)
  * [Creating a resource link from the service configuration](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#creating-a-resource-link-from-the-service-configuration)

* [Unlinking secret stores](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#unlinking-secret-stores)
* [Editing a secret store](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#editing-a-secret-store)
* [Deleting a secret store](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#deleting-a-secret-store)
* [Related content](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-secret-stores/#related-content)
