# Source: https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/

Title: Working with KV stores | Fastly Documentation

URL Source: https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/

Markdown Content:

1. [Home](https://www.fastly.com/documentation/)
2. [Guides](https://www.fastly.com/documentation/guides/)
3. [Compute](https://www.fastly.com/documentation/guides/compute/)
4. [Edge Data Storage](https://www.fastly.com/documentation/guides/compute/edge-data-storage/)

* English
* 日本語

A KV store is a type of versionless container that allows you to store data in the form of key-value pairs for use in high performance reads and writes at the edge. A single KV store can be associated with multiple [Compute services](https://www.fastly.com/documentation/guides/getting-started/services/working-with-compute-services) in your account.

Once [linked to a service](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#linking-kv-stores-to-a-service), any updates you make to the store are automatically reflected on the service without needing to increment the service's version. Changes immediately impact all service versions, including the active one. Also, because KV stores are stored at the edge, they allow you to offload that data from your origin and keep it closer to your end users.

You can also create and work with KV stores via the [API](https://www.fastly.com/documentation/reference/api/services/resources/kv-store/).

**HINT:** Bulk operations can only be completed via the [API](https://www.fastly.com/documentation/reference/api/services/resources/kv-store-item/#kv-store-upsert-batch).

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#before-you-begin)Before you begin
----------------------------------------------------------------------------------------------------------------------------------

KV Store is only available for Fastly's Compute services, not for CDN (VCL-based) services.

Make sure you review the limitations for using edge data stores in the [Compute resource limits](https://docs.fastly.com/products/compute-resource-limits#edge-data-storage-limitations).

**WARNING:** Personal information, secrets, or sensitive data should not be included in KV stores or incorporated into edge logic. In addition, we do not maintain version histories of your KV stores. Our [Compliance and Law FAQ](https://www.fastly.com/trust/faq) describes in detail how Fastly handles personal data privacy.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#creating-a-kv-store)Creating a KV store
----------------------------------------------------------------------------------------------------------------------------------------

Creating a KV store requires you to create at least one key-value pair before you associate it with a service. To create a new KV store and its key-value pairs, follow these steps:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**KV stores**](https://manage.fastly.com/resources/kv-stores).
3. Click **Create store**.
4. In the **Store name** field, enter a name for the store and then click **Create**.
5. Click **Add item**.
6. Enter the key and the value in the appropriate fields. Click **Upload file** to navigate to the file on your system using the file picker. Alternatively, drag and drop your key file directly into the drag and drop area.
7. Click **Save**.

By default, the web interface displays only the first 1,000 keys in the store. To view more keys, click the **Load more keys** button.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#linking-kv-stores-to-a-service)Linking KV stores to a service
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Once you've created a KV store, you can link it to a service from the Resources controls or from the service configuration for the service, creating a _resource link_. By creating a resource link, any future updates made to the store are automatically reflected on the linked services.

### [](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#creating-a-resource-link-from-the-resources-controls)Creating a resource link from the Resources controls

To link a KV store to a service from the Resources controls:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**KV stores**](https://manage.fastly.com/resources/kv-stores).

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

### [](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#creating-a-resource-link-from-the-service-configuration)Creating a resource link from the service configuration

To link a KV store to a service from the service configuration:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. From the [**Home**](https://manage.fastly.com/home) page, select the appropriate service. You can use the search box to search by ID, name, or domain.
3. Click **Edit configuration** and then select the option to clone the active version.
4. Click **Service configuration**.
5. From the **Linked resources** options in the on-page navigation, click **KV stores**.
6. From the **Link KV Store to service** menu, select the KV store you want to link to the service. A success message appears indicating the store is linked to your service.

Once linked, you can immediately start referencing the KV store in your edge logic and [activate the service](https://www.fastly.com/documentation/guides/getting-started/services/working-with-compute-services#editing-and-activating-versions-of-services) when you’re ready.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#referencing-resource-links)Referencing resource links
------------------------------------------------------------------------------------------------------------------------------------------------------

Once you link a store to a service, that resource link has a unique ID, separate from the service ID and store ID, which you can find by querying the [Resource API](https://www.fastly.com/documentation/reference/api/services/resource/). When referencing the store from your code, use the resource link name or ID, depending on your needs, not the store name. Refer to the [Resource API documentation](https://www.fastly.com/documentation/reference/api/services/resource/) for more information.

**HINT:** It's possible to use the same name for the resource link as for the store itself. For example, you could have a store called `my-store` and also use that same name for the resource link that connects the store to each service. However, if you rename the underlying store, the name of the resource link will not change.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#unlinking-kv-stores)Unlinking KV stores
----------------------------------------------------------------------------------------------------------------------------------------

You can unlink a KV store from a service from the service configuration.

To unlink a KV store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. From the [**Home**](https://manage.fastly.com/home) page, select the appropriate service. You can use the search box to search by ID, name, or domain.
3. Click **Service configuration**.
4. From the **Resources** options in the on-page navigation, click **KV stores**.
5. Click **Unlink from service** next to the KV store you want to unlink from your service.
6. Click **Confirm and unlink**. A new, draft version of the service is created.
7. [Activate the service](https://www.fastly.com/documentation/guides/getting-started/services/working-with-compute-services#editing-and-activating-versions-of-services) to finalize unlinking the KV store.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#editing-a-kv-store)Editing a KV store
--------------------------------------------------------------------------------------------------------------------------------------

You can edit the name of a KV store as well as the key-value pairs within the store from **Resources**>[**KV stores**](https://manage.fastly.com/resources/kv-stores). You can also access this page by clicking **Edit in Resources** when accessing a KV store from the service configuration.

To rename a KV store:

1. Click the name of the store you want to edit.
2. From the **Options** menu, click **Edit store name**.
3. Enter a new name for the store.
4. Click **Confirm and rename**.

To add new key-value pairs to a KV store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**KV stores**](https://manage.fastly.com/resources/kv-stores).
3. Click the name of the store you want to edit.
4. Click **Add item**.
5. Enter the key and the value in the appropriate fields. Click **Upload file** to navigate to the file on your system using the file picker. Alternatively, drag and drop your key file directly into the drag and drop area.
6. Click **Save**.

To edit the key-value pairs within a KV store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**KV stores**](https://manage.fastly.com/resources/kv-stores).
3. Click the name of the store you want to edit.
4. Click the pencil ![Image 1: Pencil icon](https://www.fastly.com/documentation/static/9680021d4e04d4ec658b7bbe97a8a944/pencil.png) to the right of the key you want to edit.
5. Edit the key value as necessary. Click **Upload file** to navigate to the file on your system using the file picker. Alternatively, drag and drop your key file directly into the drag and drop area.
6. Click **Save**.

The changes you make will be immediately applied to your configuration including any deployed service versions associated with the KV store. If you have custom logic referencing the store or keys, ensure you update them.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#deleting-a-kv-store)Deleting a KV store
----------------------------------------------------------------------------------------------------------------------------------------

You can delete a KV store at any time.

Before deleting a KV store:

* Unlink the KV store from your services. If the KV store is linked to any service, an error will appear when you try to delete the store.
* Update any custom logic that references the key-value pairs in the KV store. Deleting a KV store also deletes all key-value pairs within the store.

To delete a KV store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**KV stores**](https://manage.fastly.com/resources/kv-stores).
3. Click the name of the store you want to delete.
4. From the **Options** menu, click **Delete store**.
5. Click **Confirm and delete**.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-kv-stores/#related-content)Related content
--------------------------------------------------------------------------------------------------------------------------------

* [Edge Data Storage](https://docs.fastly.com/products/edge-data-storage)
* [Edge Data Storage API documentation](https://www.fastly.com/documentation/reference/api/services/resources/)
* [Resource links API documentation](https://www.fastly.com/documentation/reference/api/services/resource/)
