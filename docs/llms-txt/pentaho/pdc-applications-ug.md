# Source: https://docs.pentaho.com/pdc-use/pdc-applications-ug.md

# Applications

Pentaho Data Catalog gives a single location for creating, organizing, curating, and identifying application assets like external applications, groups, and categories to help you understand what type of data is linked from an external application. By organizing external applications into groups and then into categories, you create an applications hierarchy.

The applications hierarchy in Data Catalog helps organize and manage external applications and their interactions with data within the Data Catalog. The primary purpose of the applications hierarchy is to track how external applications use the data. The following are the key functions of the application hierarchy:

* Tracks which applications are using what data, which helps with data governance and optimizing data usage.
* Enables applications to be associated with business terms, providing a clear context of how data is used. This is useful for understanding the impact and usage of data across different applications.
* Shows how schemas are related to applications, indicating which applications predominantly use specific data.

You can use that hierarchy with role-based access control to secure and separate valuable data and metadata and prevent such data from reaching unintended audiences. The role and permissions assigned to you determine how you can interact with the applications. For example, users with the Data\_Steward role can create applications including groups and categories.

## Tour the Applications page

In Data Catalog, the Applications page gives a user-friendly interface for managing and viewing external applications. Click **Applications** in the left navigation menu to open the Applications page. This page is divided into two primary areas:

![Application page areas marked with numbers](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-f4b020498f05172d84280f622ee21f0c5ab10e32%2FPDC%20Applications%20page%20areas%20\(Tour%20the%20Applications%20page\).png?alt=media)

<table><thead><tr><th width="86.77777099609375">Item</th><th width="144.4444580078125">Name (Pane)</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Navigation</td><td><p>Shows the categories, groups, and applications. Navigate the tree of applications to find the one you want to explore on the canvas. In addition, click <strong>Actions</strong> (in area 1) to perform additional functions and features:- <strong>Add New Category</strong></p><ul><li><strong>Add New Group</strong></li><li><strong>Add New Application</strong></li><li><strong>View Table</strong></li><li><strong>View Galaxy</strong></li><li><strong>Import</strong></li><li><strong>Export</strong></li></ul></td></tr><tr><td>2</td><td>Content</td><td>Gives information about the selected asset, where the details provided vary based on the selection. For example, if you select a category, group, or application, the metadata appears in the Content pane.</td></tr></tbody></table>

### Applications navigation pane

On the left Navigation pane, you see a list of external applications organized by category, groups, and application hierarchy. Expand the application tree and click a category, group, or application to view summary information and associated details. In addition, you can enter a keyword in the **Search** box and search for assets, like an application category, group, or application.

When you select an individual asset, the asset name is highlighted in the tree view, and the metadata of that asset is shown in the Content pane. You can view the name of the selected asset and the path in the banner. In addition, select **Actions** to manage assets and import and export the application hierarchy. For more information, see the **Manage Applications** section in the **Administer Pentaho Data Catalog** document. Additionally, you can choose **View Table** or **View Galaxy** to understand the application hierarchy.

### Applications content pane

You can view details about the selected asset in the Content pane in the associated tabs. The details shown depend on the type of resource selected. For example, if you select an application category or an application group, then you can view the summary and custom properties applied to them.

![Content pane on the Applications landing page in Data Catalog](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-16d186bcae705fc04a6f1cec2df819ba7c88c02b%2FApplications%20content%20pane.jpg?alt=media)

The following table identifies the key details available in the Content pane for an application asset:

<table><thead><tr><th width="78.99993896484375">Item</th><th width="146.22222900390625">Name</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Data banner</td><td>Shows the name, path, and type icon identifying the application asset, such as a category, group, or application. The name and type attributes identifying the resource are provided.</td></tr><tr><td>2</td><td><strong>Actions</strong> menu</td><td><p>Click to view actions available for processing, saving, and copying the data, depending on the selected asset type. The actions you can take in the data content area are:- Copy the application path (hierarchy)</p><ul><li>Change to a Galaxy view of the data</li></ul></td></tr><tr><td>3</td><td>Data tabs</td><td><p>Click to view additional information about the application asset:- </p><p></p><ul><li><a href="#summary-tab">Summary</a></li><li><a href="#custom-properties-tab">Custom Properties </a></li><li><a href="#business-terms-tab">Business Terms</a></li><li><a href="#policies-tab">Policies</a></li><li><a href="#reference-data-tab">Reference Data</a></li><li><a href="#data-elements-tab">Data Elements</a></li><li><a href="#comment-tab">Comment</a></li></ul><p>To know more about each tab, see <a href="#applications-hierarchy-view">Applications hierarchy view</a>.</p></td></tr></tbody></table>

## Different views of the application hierarchy

You can choose different views to understand the application hierarchy. On the Applications page, the default view is the hierarchy view. To switch to other views, in the navigation pane, under **Actions**, choose **View Table** to view applications in tabular format and choose **View Galaxy** to view applications in a spatial format.

### Applications hierarchy view

You can create and manage external applications visually and intuitively in the hierarchy view of the Applications page. This view is designed to help organizations define and maintain a common set of external applications and their associated details, ensuring clarity and consistency in data-related discussions. The following options are available on the Applications page.

#### **Application name**

The name of the category, group, or application in Data Catalog. When you hover the mouse pointer on the application name, click the pencil icon to edit this name.

#### **Actions**

A drop-down with the following features:

<table><thead><tr><th width="141.77777099609375">Feature</th><th>Description</th></tr></thead><tbody><tr><td><strong>Copy Path</strong></td><td>Copies the application asset hierarchy.</td></tr><tr><td><strong>View Galaxy</strong></td><td>Takes you to the Galaxy view of the selected application asset. Here, you can see the applications and their related groups and categories. See <a href="pdc-galaxy-view">Galaxy view</a> for more details.</td></tr></tbody></table>

#### **Summary tab**

Gives a summarized view of the selected application asset. In the Summary tab, you can view the following information.

**Note:** The information that is visible depends on the application asset you have selected.

<table><thead><tr><th width="136.22216796875">Name</th><th>Description</th></tr></thead><tbody><tr><td><strong>Description</strong></td><td>Serves as the single and definitive reference for an application asset. You can add or edit the description of the application, group, or category. For example, you should define the purpose of the specified application and what type of data it contains.</td></tr><tr><td><strong>Purpose</strong></td><td>Gives a brief description or explanation of an application asset's purpose or use case. It can help you to understand how data from this application is linked to Data Catalog, what it's intended for, and how it might be relevant. In addition, you can also add or edit the purpose of the application, group, or category.</td></tr><tr><td><strong>Abbreviation</strong> (only for an application)</td><td>Contains a short or commonly used abbreviated name for the application. For example, <em>Customer Relationship Management</em> can be abbreviated as <em>CRM</em>.</td></tr><tr><td><strong>Rating</strong></td><td>Highlights the popularity of the asset by providing an average of all the user ratings. A low rating highlights an issue with the resource, such as incomplete data.</td></tr><tr><td><strong>Properties</strong></td><td><p>Shows the properties of the application, group, or category.</p><ul><li><strong>Vendor:</strong> The name of the company or organization that provides the application.</li><li><strong>Owner:</strong> The individual or team responsible for the application within the organization.</li><li><strong>Contact Name:</strong> The primary point of contact for any queries or issues related to the application.</li><li><strong>Valid Until:</strong> The expiration date or validity period for the application.</li><li><strong>Contact Email:</strong> The email address of the primary contact person.</li><li><strong>Domain:</strong> The specific area or domain within the organization to which the application belongs.</li><li><strong>Custodian:</strong> The person or group responsible for managing and maintaining the application.</li><li><strong>Business Critical:</strong> Indicates whether the application is critical to business operations (true/false).</li><li><strong>Created By:</strong> The user who created the application entry in Data Catalog.</li><li><strong>Updated By:</strong> The user who last updated the application entry in Data Catalog.</li><li><strong>Last Updated:</strong> The date and time when the application data was last updated.</li><li><strong>Application Status</strong> (only for Okta applications): Status of the application, either <strong>Active</strong> or <strong>Inactive</strong>.</li><li><strong>Status:</strong> The current state of the application, such as <strong>Active</strong>, <strong>Inactive</strong>, or <strong>Unknown</strong>.</li></ul></td></tr><tr><td><strong>Custom Properties</strong></td><td>Lists the custom properties associated with the resource. Custom properties refer to user-defined metadata attributes or fields that can be associated with various data assets. For more information, see <a href="../ldc-resource-properties-user-guide-cp#custom-properties">Custom properties</a>.</td></tr><tr><td><strong>Business Terms</strong></td><td>Lists associated business terms for the resource. With the Data Steward role, you can also click <strong>Add Term</strong> to open the Business Terms dialog box and add terms to the resource.</td></tr><tr><td><strong>Tags</strong></td><td>Lists the tags associated with the resource. In addition, you can click and start adding tags like “quality:45” (the key should be unique) to the resource, which helps to identify the resource with tagged keywords.</td></tr><tr><td><strong>Style</strong></td><td><p>Displays the icon, title, and color associated with the application asset. With the data steward role, you can click the <strong>Edit</strong> (pencil) icon to select a different icon, update the title, and change the color. Then you can click <strong>Apply</strong>, the selected icon and color are updated immediately, and the updated title appears in the asset header and in the breadcrumb navigation. You can also choose <strong>Apply to all siblings</strong> to apply the same visual changes to all sibling assets at the same level.<br></p><p>▶️ Watch a guided walkthrough on <a href="https://assets.demos.hitachivantara.com/psl/d4h0ewc">editing icons, titles, and colors in the Style panel</a> in Data Catalog.</p></td></tr></tbody></table>

#### **Custom Properties** tab

You can use custom properties to annotate and categorize the data with additional context-specific information, enhancing the metadata available for data assets within Data Catalog. This tab lists the custom properties and values added to the application, group, or category.

To manage custom properties, select **Manage properties** to open the **Custom Properties** page in the **Management** section. For more information, see [Manage custom properties](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-custom-properties) in [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document.

#### **Business Terms tab**

In the context of applications, business terms are properties of an application (stored in application properties) that denote the general business logic of the application. For example, if the application is related to the finance domain, then it can have business terms assigned like ‘Finance,’ ‘Banking,’ or ‘Accounting.’ In this tab, you can explore the business terms information associated with the application, such as name, parent, and owner.

To add a business term, click **Add Terms** and choose the business term you want to associate with the application. After you add any business term to the application, it creates a relationship between the term and the application. Subsequently, the application appears on the Applications tab of the corresponding business term in [Business Glossary](https://docs.pentaho.com/pdc-use/pdc-business-glossary). You can also click **Delete**, which only removes the association between the application and the business term but does not delete the actual business term.

#### **Policies tab**

In the context of an application, policies and standards are properties of an application (stored in application properties), meaning a set of rules applied to the application. In this tab, you can explore the standards and policies related to the application and additional information, such as name, parent, and owner.

To add a policy, click **Add Policy** and choose the standard and policy you want to link to the application. After you add any policy to the application, it creates a relationship between the policy and the application. Subsequently, the application appears on the **Applications** tab of the corresponding policy in the [Policy](https://docs.pentaho.com/pdc-use/broken-reference) page. You can also click **Delete** which removes the association between the application and policy but does not delete the actual policy.

#### **Reference Data tab**

In the context of an application, this tab lists the reference datasets that contain the respective application information stored. You can explore the reference datasets with additional information such as category, name, status, and version.

To add a reference dataset, click **Add Data Sets** and choose the dataset you want to associate with the application. This creates a relationship between the dataset and the application. Subsequently, the application appears on the **Applications** tab of the respective dataset in Reference Data. You can also click **Delete**, which only removes the association between the application and the dataset but doesn’t delete the actual dataset.

#### **Data Elements tab**

In the context of an application, this tab lists the data elements that contain the selected application information stored. Data assets like folders, schemas, and tables can have associations with the applications, but files and columns can’t have application associations. This tab shows data asset details such as the data source, item name, item type, parent, and associated tags. You can customize the columns and apply filters to refine the list.

To get detailed information, click **View** to view the data element in the Canvas view with a highlighted focus. To add new data elements, click **Add Data Elements** and choose the data element you want to associate with the application. This creates a relationship between the data element and the application. Subsequently, the application appears on the **Applications** tab of the associated data element in the [Data Canvas](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/pdc-data-canvas-explore-your-data). You can also click **Delete**, which only removes the association between the application and the data element but does not delete the actual data element.

#### **Users with Access** (only for Okta applications)

For applications imported through Okta integration, Data Catalog provides an additional tab called **Users with Access**. It displays a list of users who have been granted access to the selected application within the Okta system. The **Users with Access** tab provides key user information, including the first name, last name, and email address of each individual who can access the application. This information is pulled directly from Okta, providing a clear view of application-level access rights. It helps data stewards, business owners, and compliance teams who need to validate user permissions, identify unnecessary access, or audit user roles across the environment.

#### **Comment** tab

The **Comment** tab is a collaborative feature that allows users to discuss and provide feedback on specific data assets within Data Catalog. You can add comments, share suggestions, or ask questions directly in the tab using the provided text box, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then the specific user, or users, are notified of the comment through email and in the Mentions tab on the Data Catalog landing page, prompting them to respond if necessary. For more information, see [Tour of the Home page](https://docs.pentaho.com/pdc-use/ldc-quick-start-user-guide-cp#tour-of-the-home-page).

**Note:** In the Comment tab, you can:

* Tag users who have been configured in Data Catalog.
* Only delete the comments you posted.
* Delete any comment if you are an admin.

### Applications table view

On the Applications page, in the Navigation pane, under **Actions**, when you choose **View Table**, it displays the applications organized by **Category**, **Group**, **Application**, and **All** (irrespective of asset types), including the complete hierarchy in a tabular format. In the table view, you can view key details for each asset, including its name, type (category, group, or application), parent asset, and the dates and times it was created and last updated. Additionally, you can see which user created and last updated each asset.

### Applications galaxy view

In the Navigation pane, under **Actions**, when you choose **View Galaxy**, it shows the applications in the Galaxy view. The galaxy view shows a different visual layout that is useful for exploring relationships and connections between the assets. You can use the Galaxy view feature to view the structure of the data and its details quickly. This feature is especially useful when you want to view information that is not easily visualized using the navigation tree. When you open applications in the galaxy view, you can see the relationships in the data from a bird's eye view and drill down into the data for specific details. To know more about the Galaxy view and its available functions, see [Galaxy view](https://docs.pentaho.com/pdc-use/pdc-galaxy-view).
