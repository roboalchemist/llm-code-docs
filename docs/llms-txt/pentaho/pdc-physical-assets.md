# Source: https://docs.pentaho.com/pdc-use/pdc-physical-assets.md

# Physical Assets

In edge environments, IoT machines generate a vast number of data points. Still, only a select few are usually used for analytics, while the remaining data points often remain siloed and underutilized. As a part of the Pentaho +, Pentaho Edge is designed to acquire, ingest, process, and analyze operation technology (OT) assets data close to its source, typically in Industrial Internet of Things (IIoT) or edge environments. You can ingest all generated OT assets data into the Physical Assets section of Pentaho Data Catalog, which serves as a centralized platform for discovering, organizing, and governing data assets.

Using Physical Assets, you can:

* Integrate edge-generated data and metadata with enterprise-wide systems, ensuring consistency and accessibility for analytics workflows.
* Provide a unified, centralized repository for OT assets and data points, eliminating silos and enabling seamless access to all relevant data in one place.
* Visualize all OT assets data points, including those not used in analytics, and to provide a comprehensive view of the data ecosystem.
* Easily navigate and understand the relationships between devices, services, locations, and machines as OT assets data points are organized logically into a hierarchical structure.
* Discover and retrieve the exact data needed for analysis and decision-making since all data points are indexed and categorized under the Physical Assets.
* Enrich the data points by providing additional context and improving the understanding of their purpose and relevance.
* Trace the origin and transformation of data points using the lineage feature.
* Prepare industrial data with contextualizationby adding relevant information, business glossary, polices, applications, data elements along with time, location, or source, to raw data simplifing your IT-OT integration journey.

## Physical Assets components

In Data Catalog, the Physical Assets section contains operational technology (OT) assets and data points in an organized and structured manner, including components such as device services (protocols), locations, devices, and data point (tags) values, and is displayed in a tree structure to easily locate, understand, and analyze relevant data points.

![Asset Hierarchy Components](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-4ad029b821b08014104e44c025c2a7a6cbc2f5c8%2FAsset%20Hierarchy%20Components_Updated%3DGUID-71788F25-E879-43BF-B00C-9BBE5312E901%3D1%3Den%3DLow.png?alt=media)

<table><thead><tr><th width="80.33331298828125">Item</th><th width="146.4444580078125">Physical Asset Component</th><th width="308.8887939453125">Description</th><th>Example</th></tr></thead><tbody><tr><td>1</td><td>Device Service</td><td>The specific service or functionality provided by a device within the OT ecosystem.</td><td>‘Device-service:DataCenter_Sustainability’</td></tr><tr><td>2</td><td>Location</td><td>The physical or logical place where the device or its service is deployed, which can be a factory floor, a specific room, a geographical area, or even a virtual location within a system.</td><td>Americas, EMEA, or “Factory A, Line 3"</td></tr><tr><td>3</td><td>Device</td><td>The specific equipment or machinery associated with the device or service, which represents the physical asset within which the device operates or interacts.</td><td>Temperature sensor in cold storage, HVAC unit, or a robotic arm in assembly line</td></tr><tr><td>4</td><td>Value</td><td>The actual data or metric captured, generated, or transmitted by the device, which is typically a measurable quantity or status used for monitoring, analysis, or decision-making.</td><td>"75°C" as the temperature value from a sensor or "120 RPM" as the speed value from a motor</td></tr></tbody></table>

## Tour the Physical Assets page

In Data Catalog, the Physical Assets page provides a user-friendly interface for managing and viewing OT assets. To access and explore the Physical Assets page, in the left navigation menu, click **Physical Assets**. This page is divided into two primary areas, the navigation and content pane.

![Asset Hierarchy Landing Page](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-9383892be0f1b9c069ca08fbefc4ebb752bfecd1%2FAsset%20Hierarchy%20Landing%20Page%3DGUID-C760B745-865F-4DF0-9F16-1120C08BA455%3D1%3Den%3DLow.jpg?alt=media)

### Physical Assets navigation pane

On the left navigation pane, you see the list of physical assets components such as device services, locations, machines, and values in a hierarchical tree structure. You can explore this hierarchy to locate specific physical assets for further analysis. You can choose **View Table** or **View Galaxy** under **Actions** to understand the physical assets hierarchy. Additionally, you can manage physical assets using the following options available under **Actions**:

* [Add New Device](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-physical-assets#add-a-new-device-locally-to-data-catalog)
* [Add New Value](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-physical-assets#add-a-new-value-locally-to-data-catalog)
* [Import](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-physical-assets#import-physical-assets)
* [Export](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-physical-assets#export-physical-assets)

For more information, see the [Manage physical assets](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-physical-assets) section in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document.

### Physical assets content pane

You can view detailed information about the selected physical assets, including metadata specific to the chosen component. For instance, when a device profile is selected, the content pane shows its associated metadata, where you can clearly understand the data attributes and context.

The following table identifies the key details available in the content pane for an physical asset:

![Physical Assets Content Pane](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-84f861a05171fce1143a9cb88f348af90a7c6764%2FOT%20Asset%20Hierarchy%20Content%20Pane%3DGUID-DF3FAA75-3D48-489F-97E7-D403AECA00F7%3D1%3Den%3DLow.jpg?alt=media)

<table><thead><tr><th width="77.88885498046875">Item</th><th width="125">Name</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Data banner</td><td>Shows the name, path, and type icon identifying the physical assets, such as a device profile, location, device, or value. With these details, you can get clear context about the asset's position within the hierarchy and its classification. The name and type attributes identifying the resource are provided.</td></tr><tr><td>2</td><td>Actions drop-down</td><td>Shows a menu of actionable options tailored to the selected physical asset type. You can perform tasks such as copying the application path (hierarchy) to reference the asset’s location or switching to a Galaxy view to alternately visualize the data.</td></tr><tr><td>3</td><td>Data tabs</td><td><p>Get access to detailed information and metadata related to the selected physical assets through the following tabs:</p><ul><li><a href="#summary-tab">Summary</a></li><li><a href="#custom-properties-tab">Custom Properties</a></li><li><a href="#data-elements-tab">Data Elements</a></li><li><a href="#comment-tab">Comment</a></li><li><a href="#business-terms-tab">Business Terms</a></li><li><a href="#reference-data-tab">Reference Data</a></li><li><a href="#applications-tab">Applications</a></li><li><a href="#policies-tab">Policies</a></li></ul><p>On each tab, you can get insights into specific attributes or relationships of the physical assets, which can help to analyze and understand the data. To know more about each tab, see the <a href="#physical-assets-hierarchy-view">Physical assets hierarchy view</a>.</p></td></tr></tbody></table>

## Different views of the Physical Assets

In the Physical Assets section of Data Catalog, you can choose different views of the physical assets and explore and understand the data structure in ways that best suit your needs. By default, you see the physical assets hierarchy view in a tree-structured representation. Here, you can explore physical assets like device services (protocols), device profiles (data points), locations, devices, and values by following clear parent-child relationships and understanding how physical assets components are interconnected contextually.

You can also switch to Table View or Galaxy View by selecting the **View Table** or **View Galaxy** option under **Actions** in the navigation pane. In the table view, you see the physical assets in a tabular layout or a detailed spreadsheet-like format, which helps to analyze data attributes and compare multiple assets efficiently. In Galaxy view, you can visualize physical assets in a spatial format, where you can identify relationships and patterns between assets, making it ideal for gaining a broader, more interconnected perspective of your data.

### Physical assets hierarchy view

You can manage physical assets visually and intuitively in the hierarchy view of the Physical Assets page Data Catalog. In this view, organizations can sync physical assets and maintain their associated details, ensuring clarity and consistency in data-related discussions. The following options are available on the Physical Assets page.

#### **Physical assets component name**

The name of the physical assets component, such as a device profile (protocol), location, device, or data point value. With this, you can quickly identify and understand the specific physical asset you are working with.

#### **Actions**

A drop-down with the following features:

<table><thead><tr><th width="132.888916015625">Feature</th><th>Description</th></tr></thead><tbody><tr><td><strong>Copy Path</strong></td><td>Copies the hierarchical path of the physical assets component for quick reference or to share it with others.</td></tr><tr><td><strong>View Galaxy</strong></td><td>Takes you to the Galaxy view of the selected physical asset. Here, you can see the physical assets components and their related assets. See <a href="pdc-galaxy-view">Galaxy view</a> for more details.</td></tr></tbody></table>

#### **Summary tab**

Gives a summarized view of the selected physical asset component. In the Summary tab, you can view the following information.

**Note:** The information that is visible depends on the physical asset component you have selected.

<table><thead><tr><th width="136.22216796875">Name</th><th>Description</th></tr></thead><tbody><tr><td><strong>Description</strong></td><td>A concise explanation of what the physical asset component represents within the hierarchy. It describes the physical asset component's role, characteristics, or functionality in the operational technology ecosystem. For example, for a device or system, the definition might outline its purpose, key features, or how it contributes to the overall operation. Additionally, you can add or edit the description of the physical asset component.</td></tr><tr><td><strong>Purpose</strong></td><td>Specifies the primary objective or intended use of the physical asset. It explains why the asset exists within the system and what goals it is meant to achieve. For instance, this can include details about how the asset supports a particular process, delivers value, or contributes to achieving specific operational outcomes. Additionally, you can add or edit the purpose of the physical asset component.</td></tr><tr><td><strong>Rating</strong></td><td>Highlights the popularity of the physical asset component by providing an average of all the user ratings. A low rating highlights an issue with the resource, such as incomplete data.</td></tr><tr><td><strong>Properties</strong></td><td><p>Shows the physical asset data points that are being monitored in Pentaho Edge. Along with these data points, you can also see the following information.</p><ul><li><strong>Domain</strong>: The specific area or domain to which the physical asset component belongs.</li><li><strong>Business Steward</strong>: The individual or team responsible for the governance, oversight, and maintenance of the physical asset component.</li><li><strong>Status</strong>: The current state or lifecycle stage of the physical asset component, such as "Accepted," "Draft," or "Deprecated," to better understand the readiness or usability of the asset within the system.</li><li><strong>Created By</strong>: The user or system that created the physical asset component in Data Catalog.</li><li><strong>Updated By</strong>: The user or system that last updated the physical asset component in Data Catalog.</li><li><strong>Last Updated</strong>: The date and time when the physical asset component was last updated.</li></ul></td></tr><tr><td><strong>Custom Properties</strong></td><td>Lists the custom properties associated with the resource. Custom properties refer to user-defined metadata attributes or fields that can be associated with various data assets. For more information, see <a href="../ldc-resource-properties-user-guide-cp#custom-properties">Custom properties</a>.</td></tr><tr><td><strong>Tags</strong></td><td>Lists the tags associated with the resource. In addition, you can click and start adding tags like “quality:45” (the key should be unique) to the resource, which helps to identify the resource with tagged keywords.</td></tr><tr><td><strong>Style</strong></td><td><p>Displays the icon, title, and color associated with the physical asset. With the data steward role, you can click the <strong>Edit</strong> (pencil) icon to select a different icon, update the title, and change the color. Then you can click <strong>Apply</strong>, the selected icon and color are updated immediately, and the updated title appears in the asset header and in the breadcrumb navigation. You can also choose <strong>Apply to all siblings</strong> to apply the same visual changes to all sibling assets at the same level.<br></p><p>▶️ Watch a guided walkthrough on <a href="https://assets.demos.hitachivantara.com/psl/d4h0ewc">editing icons, titles, and colors in the Style panel</a> in Data Catalog.</p></td></tr></tbody></table>

#### Custom Properties tab

You can use custom properties to annotate and categorize the physical asset component with additional context-specific information, enhancing the metadata available for data assets within Data Catalog. This tab lists the custom properties and values added to the physical asset component. You can apply filters to refine the list.

To manage custom properties, select **Manage properties** to open the **Custom Properties** page in the **Management** section. For more information, see [Manage custom properties](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-custom-properties) in [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document.

#### **Data Elements tab**

The **Data Elements** tab shows a detailed view of the data elements associated with a selected physical asset component. This tab shows data asset details such as the data source, item name, item type, parent, and associated tags which help you to understand the data structure, maintain metadata, and perform actions like adding, viewing, or deleting data elements. You can also apply filters to refine the list.

To add new data elements, click **Add Data Elements** and choose the data element you want to associate with the component. To get detailed information, click **View** to see the data element in the canvas view with a highlighted focus. You can also click **Delete**, which only removes the association between the component and the data element but does not delete the actual data element.

#### **Comment tab**

The **Comment** tab is a collaborative feature, where users can discuss and give feedback on specific data assets within Data Catalog. You can add comments, share suggestions, or ask questions directly in the tab using the provided text box, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then, the specific user or users are notified of the comment through email and in the Mentions tab on the Data Catalog landing page, prompting them to respond if necessary. For more information, see [Tour of the Home page](https://docs.pentaho.com/pdc-use/ldc-quick-start-user-guide-cp#tour-of-the-home-page).

**Note:** In the Comment tab, you can:

* Tag users who have been configured in Data Catalog.
* Only delete the comments you posted.
* Delete any comment if you are an admin.

#### **Business Terms tab**

In the **Business Terms** tab, you can associate physical assets with relevant business terms to define and categorize physical asset components, ensuring consistency across the organization. It shows the names of associated terms, their parent categories, and the owners responsible for them. You can also apply filters to refine the list.

To add a business term, click **Add Terms** and choose the business term you want to associate with the physical asset component. After you add any business term to the physical asset component, it creates a relationship between the term and the physical asset component. To get detailed information, click on the term to view the business term in the canvas view with a highlighted focus. You can also click **Delete**, which only removes the association between the component and the business term but does not delete the actual business term in Data Catalog.

#### **Reference Data tab**

The **Reference Data** tab lists the reference datasets that are associated with the respective physical asset components. By linking physical assets with authoritative reference datasets, you can ensure consistency and give additional context, which helps to standardize data usage, maintain version control, and enhance the quality of analytics and decision-making. You can also apply filters to refine the list.

To add a reference dataset, click **Add Data Sets** and choose the dataset you want to associate with the physical asset component. This creates a relationship between the dataset and the physical asset component. To get detailed information, click on the data set name to view the data set in the canvas view with a highlighted focus. You can also click **Delete**, which only removes the association between the component and the dataset but doesn’t delete the actual dataset in Data Catalog.

#### **Applications tab**

For a standard, the **Applications** tab contains the third-party or external applications associated with the physical asset component and additional information associated with each application. By linking third-party applications and physical asset components, you can understand how external applications interact with specific physical assets and the relationship between data and external systems to better assess its purpose and relevance. You can also apply filters to refine the list.

To add an application, click **Add Applications** and choose the application you want to link to the physical asset component. You can also click **Delete**, which removes the association between the application and the standard but does not delete the actual application in Data Catalog.

#### **Policies tab**

In the context of an physical asset component, policies and standards are properties of an physical asset component, meaning a set of rules applied to the component. In **Policies** tab, you can explore the standards and policies related to the component and additional information, such as name, parent, and owner. By linking policies and standards with physical assets, you can give clarity on the policies and standards governing data usage and management and reduce the risk of non-compliance. You can also apply filters to refine the list.

To add a policy, click **Add Policy** and choose the standard and policy you want to link to the component. After you add any policy to the component, it creates a relationship between the policy and the component. You can also click **Delete**, which removes the association between the component and policy but does not delete the actual policy in Data Catalog.

### Physical assets table view

In Data Catalog, the table view is an alternative to the default hierarchical tree view. On the Physical Assets page, in the navigation pane, under **Actions**, when you choose **View Table**, it shows the physical asset components such as **Device Profile**, **Location**, **Device**, **Value**, and **All** (irrespective of asset types), including the complete hierarchy in a tabular format.

In the table view, you can click **Edit** and update:

* The physical asset name or add a business steward who owns the data.
* Tags with relevant keywords or identifiers to categorize and identify the physical asset.
* Custom properties to include additional metadata tailored to their specific business needs.

Additionally, you can apply filters to refine the list and manage columns using the settings feature and can perform the following actions in the table view:

* [**Add New Device**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-physical-assets#add-a-new-device-locally-to-data-catalog)
* [**Add New Value**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-physical-assets#add-a-new-value-locally-to-data-catalog)
* [**Import physical assets**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-physical-assets#import-physical-assets)
* [**Export physical assets**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-physical-assets#export-physical-assets)

To learn more about these additional actions, see [Manage physical assets](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-physical-assets) section in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document.

### Physical assets galaxy view

In the navigation pane, under **Actions**, when you choose **View Galaxy**, it shows the physical asset components in the galaxy view. In Data Catalog, the galaxy view shows a different visual layout that is useful for exploring relationships and connections between machines, datasets, policies, business contexts, and applications. You can use the galaxy view feature to view the structure of the data and its details quickly. This feature is especially useful when you want to view information that is not easily visualized using the navigation tree. When you open physical assets in the galaxy view, you can see the relationships in the data from a bird's-eye view and drill down into the data for specific details. To learn more about the galaxy view and its available functions, see [Galaxy view](https://docs.pentaho.com/pdc-use/pdc-galaxy-view).

![](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-a80760af290e33fb79dbf9d763fe4425e6258fe3%2FAsset%20Hierarchy%20Galaxy%20View.jpg?alt=media)
