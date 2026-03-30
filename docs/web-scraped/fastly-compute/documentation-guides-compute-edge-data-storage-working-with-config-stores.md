# Source: https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/

Title: Working with config stores | Fastly Documentation

URL Source: https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/

Markdown Content:

1. [Home](https://www.fastly.com/documentation/)
2. [Guides](https://www.fastly.com/documentation/guides/)
3. [Compute](https://www.fastly.com/documentation/guides/compute/)
4. [Edge Data Storage](https://www.fastly.com/documentation/guides/compute/edge-data-storage/)

* English
* 日本語

Config stores are a type of versionless container that allow you to store often repeated data as key-value pairs that can be read from the edge and shared by multiple [Compute services](https://www.fastly.com/documentation/guides/getting-started/services/working-with-compute-services) in your account. Once [linked to a service](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#linking-config-stores-to-a-service), any updates you make to the store are automatically reflected on the service without needing to increment the service's version. Changes immediately impact all service versions, including the active one.

You can also create and work with config stores via the [API](https://www.fastly.com/documentation/reference/api/services/resources/config-store/).

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#prerequisites)Prerequisites
--------------------------------------------------------------------------------------------------------------------------------

Config Store is only available for Fastly's Compute services, not for CDN (VCL-based) services.

Make sure you review the limitations for using edge data stores in the [Compute resource limits](https://docs.fastly.com/products/compute-resource-limits#edge-data-storage-limitations).

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#limitations-and-considerations)Limitations and considerations
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Before working with config stores, keep the following things in mind:

* Config stores can only be used by Compute services, not CDN (VCL-based) services.
* Trials for Compute include one config store with a maximum of 100 entries.
* Paid accounts include a minimum of five config stores (each having a maximum of 500 entries).

When working with config store keys and values, be aware of the following limitations:

* Config store keys are limited to 255 characters and their values are limited to 8,000 characters.
* Keys and their values are case-sensitive.

**WARNING:** Personal information, secrets, or sensitive data should not be included in config stores or incorporated into edge logic. In addition, we do not maintain version histories of your config stores. Our [Compliance and Law FAQ](https://www.fastly.com/trust/faq) describes in detail how Fastly handles personal data privacy.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#creating-a-config-store)Creating a config store
----------------------------------------------------------------------------------------------------------------------------------------------------

Creating a config store requires you to create at least one key-value pair before you associate it with a service. To create a new config store and its key-value pairs, follow these steps:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Config stores**](https://manage.fastly.com/resources/config-stores).
3. Click **Create store**.
4. In the **Store name** field, enter a name for the store and then click **Create**.
5. Click **Add item**.
6. Enter the key and the value in the appropriate fields.
7. Click **Save**.
8. Repeat to add additional key-value pairs as necessary.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#linking-config-stores-to-a-service)Linking config stores to a service
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once you've created a config store, you can link it to one or more services from the Resources controls or from the service configuration for the service, creating a _resource link_. By creating a resource link, any future updates made to the store are automatically reflected on the linked services.

### [](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#creating-a-resource-link-from-the-resources-controls)Creating a resource link from the Resources controls

To link a config store to a service from the Resources controls:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Config stores**](https://manage.fastly.com/resources/config-stores).

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

### [](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#creating-a-resource-link-from-the-service-configuration)Creating a resource link from the service configuration

To link a config store to a service from the service configuration:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. From the [**Home**](https://manage.fastly.com/home) page, select the appropriate service. You can use the search box to search by ID, name, or domain.
3. Click **Edit configuration** and then select the option to clone the active version.
4. Click **Service configuration**.
5. From the **Linked resources** options in the on-page navigation, click **Config stores**.
6. From the **Link Config Store to service** menu, select the config store you want to link to the service. A success message appears once the config store is linked to the service.

Once linked, you can immediately start referencing the config store in your edge logic and [activate the service](https://www.fastly.com/documentation/guides/getting-started/services/working-with-compute-services#editing-and-activating-versions-of-services) when you’re ready.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#referencing-resource-links)Referencing resource links
----------------------------------------------------------------------------------------------------------------------------------------------------------

Once you link a store to a service, that resource link has a unique ID, separate from the service ID and store ID, which you can find by querying the [Resource API](https://www.fastly.com/documentation/reference/api/services/resource/). When referencing the store from your code, use the resource link name or ID, depending on your needs, not the store name. Refer to the [Resource API documentation](https://www.fastly.com/documentation/reference/api/services/resource/) for more information.

**HINT:** It's possible to use the same name for the resource link as for the store itself. For example, you could have a store called `my-store` and also use that same name for the resource link that connects the store to each service. However, if you rename the underlying store, the name of the resource link will not change.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#unlinking-config-stores)Unlinking config stores
----------------------------------------------------------------------------------------------------------------------------------------------------

You can unlink a config store from a service from the service configuration.

To unlink a config store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. From the [**Home**](https://manage.fastly.com/home) page, select the appropriate service. You can use the search box to search by ID, name, or domain.
3. Click **Service configuration**.
4. From the **Resources** options in the on-page navigation, click **Config stores**.
5. Click **Unlink from service** next to the config store you want to unlink from your service.
6. Click **Confirm and unlink**. A new, draft version of the service is created.
7. [Activate the service](https://www.fastly.com/documentation/guides/getting-started/services/working-with-compute-services#editing-and-activating-versions-of-services) to finalize unlinking the config store.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#editing-a-config-store)Editing a config store
--------------------------------------------------------------------------------------------------------------------------------------------------

You can edit the name of a config store as well as the key-value pairs within the store from **Resources**>[**Config stores**](https://manage.fastly.com/resources/config-stores). You can also access this page by clicking **Edit in Resources** when accessing a config store from the service configuration.

To rename a config store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Config stores**](https://manage.fastly.com/resources/config-stores).
3. Click the name of the store you want to edit.
4. From the **Options** menu, click **Edit store name**.
5. Enter a new name for the store.
6. Click **Confirm and rename**.

To add new key-value pairs to a config store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Config stores**](https://manage.fastly.com/resources/config-stores).
3. Click the name of the store you want to edit.
4. Click **Add item**.
5. Enter the key and the value in the appropriate fields.
6. Click **Save**.
7. Repeat to add additional key-value pairs as necessary.

To edit the key-value pairs within a config store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Config stores**](https://manage.fastly.com/resources/config-stores).
3. Click the name of the store you want to edit.
4. Click the pencil ![Image 1: Pencil icon](https://www.fastly.com/documentation/static/9680021d4e04d4ec658b7bbe97a8a944/pencil.png) to the right of the key you want to edit.
5. Edit the key value as necessary.
6. Click **Save**.

To delete the key-value pairs within a config store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Config stores**](https://manage.fastly.com/resources/config-stores).
3. Click the name of the store you want to edit.
4. Click the trash ![Image 2: Trash icon](https://www.fastly.com/documentation/static/bd8eecd5ea8f2d9e87ed0718400db44b/trash.png) to the right of the key you want to edit.
5. Click **Confirm and delete**.

The changes you make will be immediately applied to your configuration including any deployed service versions associated with the config store. If you have custom logic referencing the store or keys, ensure you update them.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#deleting-a-config-store)Deleting a config store
----------------------------------------------------------------------------------------------------------------------------------------------------

You can delete a config store at any time. A config store must be unlinked from any services or an error will appear if you try to delete it.

Deleting a config store also deletes all key-value pairs within the store. If you have custom logic referencing these keys, ensure you update them before deleting the store.

To delete a config store:

1. Log in to the [Fastly control panel](https://manage.fastly.com/).
2. Go to **Resources**>[**Config stores**](https://manage.fastly.com/resources/config-stores).
3. Click the name of the store you want to delete.
4. From the **Options** menu, click **Delete store**.
5. Click **Confirm and delete**.

[](https://www.fastly.com/documentation/guides/compute/edge-data-storage/working-with-config-stores/#related-content)Related content
------------------------------------------------------------------------------------------------------------------------------------

* [Edge Data Storage](https://docs.fastly.com/products/edge-data-storage)
* [Dynamic configuration data for Fastly services](https://www.fastly.com/documentation/guides/concepts/dynamic-config)
* [Edge Data Storage API documentation](https://www.fastly.com/documentation/reference/api/services/resources/)
* [Resource links API documentation](https://www.fastly.com/documentation/reference/api/services/resource/)
