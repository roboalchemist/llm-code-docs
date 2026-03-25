# Source: https://docs.pentaho.com/pdc-use/pdc-policies-and-standards-ug.md

# Policies and standards

You can use the Pentaho Data Catalog policy manager to configure and enforce policies and standards, so that your data is consistent and meets the level of quality that is necessary for your business. For example, a policy governing the collection of customer data might include the following conditions:

* A customer's data must contain an active customer identifier with it
* A customer's data must contain consent to use it for a given business purpose
* A customer's data must be deleted upon request or at the end of a predefined period

In this example, the policy has a standard outlining that applications collecting customer data must provide consent forms, and the standard is linked to the SalesForce application.

## Tour the Policy page

In Pentaho Data Catalog, the Policy page provides a user-friendly interface for managing and viewing policies and standards. Click **Policy** in the left navigation menu to open the Policy page. This page is divided into two primary areas:

![](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-fb10e7e5f3da34f305171f3a056f96028cc3de6e%2FPDC%20Policy%20page%20areas%20\(Tour%20the%20Policy%20page\).png?alt=media)

<table><thead><tr><th width="80.111083984375">Item</th><th width="125.22222900390625">Name (Pane)</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Navigation</td><td><p>Shows the policies and standards. Navigate the tree to find what you want to explore. In addition, click <strong>Actions</strong> to perform additional functions and features:</p><ul><li><strong>Add New Policy</strong></li><li><strong>Add New Standard</strong></li><li><strong>View Table</strong></li><li><strong>View Galaxy</strong></li><li><strong>Import</strong></li><li><strong>Export</strong></li></ul></td></tr><tr><td>2</td><td>Content</td><td>Gives information about the selected asset, where the details provided vary based on the selection. For example, if you select a policy or standard, the metadata appears in the Content pane.</td></tr></tbody></table>

### Policy navigation pane

On the left Navigation pane, you see a hierarchy of policies and standards. Expand the policy tree and click a child policy or standard to view summary information and associated details. In addition, you can enter a keyword in the **Search** box and search for policies or standards.

When you select an individual asset, the asset name is highlighted in the tree view, and the metadata of that asset is shown in the Content pane. You can view the name of the selected asset and the path in the banner. In addition, select **Actions** to manage assets and import and export the application hierarchy. For more information, see [**Manage policies and standards**](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-policies-and-standards-cp) in [**Administer Pentaho Data Catalog**](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/). Additionally, you can choose **View Table** or **View Galaxy** to understand the policy hierarchy.

### Policy content page

You can view details about the selected policy or standard in the Content pane in the associated tabs. The details shown depend on the type of asset selected.

![](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-65c006e2cfd591cdf703e150ac89568ea744095f%2FPDC%20Policy%20page%20Content%20pane%20UG.png?alt=media)

<table><thead><tr><th width="80.111083984375">Item</th><th width="144.11114501953125">Name</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Data banner</td><td>Shows the name, path, and type icon identifying a policy or standard.</td></tr><tr><td>2</td><td><strong>Actions</strong> menu</td><td><p>Click to view actions available for the asset. The actions you can take are:</p><ul><li>Copy the path (hierarchy)</li><li>Change to a Galaxy view of the data</li></ul></td></tr><tr><td>3</td><td>Data tabs</td><td><p>Click to view additional information about the asset:</p><ul><li><a href="#summary-tab">Summary</a></li><li><a href="#custom-properties-tab">Custom Properties </a></li><li><a href="#business-terms-tab">Business Terms</a></li><li><a href="#comment-tab">Comment</a></li><li>Data Elements</li><li><a href="#applications-tab">Applications</a></li><li><a href="#rules-tab">Rules</a></li></ul><p>To know more about each tab, see <a href="#policy-hierarchy-view">Policy hierarchy view</a>. For standards, the additional tabs available are:</p></td></tr></tbody></table>

## Different views of the policy hierarchy

You can choose different views to better understand the policy hierarchy. On the Policy page, the default view is the hierarchy view. To switch to other views, on the navigation pane, under **Actions**, choose **View Table** to view policies in tabular format or choose **View Galaxy** to view policies in a spatial format.

### Policy hierarchy view

You can create and manage external policies visually and intuitively in the hierarchy view of the Policy page. This view is designed to help organizations define and maintain a common set of policies and their associated standards. The following options are available on the Policy page.

#### **Policy or Standard name**

The name of the policy in Data Catalog. When you hover the mouse pointer on the policy name, click the pencil icon to edit the name. In addition, you can view the time stamp of the last update below the policy name.

#### **Actions**

A menu with the following features:

<table><thead><tr><th width="154">Feature</th><th>Description</th></tr></thead><tbody><tr><td><strong>Copy Path</strong></td><td>Copies the asset hierarchy.</td></tr><tr><td><strong>View Galaxy</strong></td><td>Takes you to the Galaxy view of the selected asset. Here, you can see the policies and their related standards. See<a href="pdc-galaxy-view">Galaxy view</a> for more details.</td></tr></tbody></table>

#### **Summary tab**

Gives a summarized view of the selected policy or standard asset. In the Summary tab, you can view the following information.

**Note:** The information that is visible depends on whether you have selected a policy or a standard.

<table><thead><tr><th width="152.88885498046875">Name</th><th>Description</th></tr></thead><tbody><tr><td><strong>Definition</strong></td><td>A brief explanation of a policy or standard. Users with the Business Steward role can add or edit the description of the policy or standard.</td></tr><tr><td><strong>Purpose</strong></td><td>The policy or standard’s purpose or use case, to help other users understand how it is used.</td></tr><tr><td><strong>Scope</strong></td><td>The boundaries of a policy or standard, including what it covers, what it doesn't cover, and what decisions it applies to.</td></tr><tr><td><strong>Stakeholders</strong></td><td>The users that have an interest in the policy or standard or its outcomes.</td></tr><tr><td><strong>Rating</strong></td><td>Highlights the popularity of the policy or standard by providing an average of all the user ratings. A low rating highlights an issue with the resource, such as incomplete data.</td></tr><tr><td><strong>Properties</strong></td><td><p>Displays <a href="https://hv-eng.atlassian.net/wiki/spaces/PDC/pages/edit-v2/32815120390#Built-in-properties">built-in properties</a> of the policy or standard. Built-in properties are system-defined metadata attributes that provide standardized information about governance, ownership, classification, and status.</p><p><strong>Mandatory built-in properties</strong></p><p></p><ul><li><strong>Sensitivity</strong>: Metadata attributes, like <strong>High</strong>, <strong>Medium</strong>, and <strong>Low</strong>, that identify the sensitivity of the resource.</li><li><strong>Domain</strong>: The specific area or domain within the organization to which the policy or standard belongs.</li><li><strong>Status</strong>: The current state of the policy or standard, such as <strong>Draft</strong>, <strong>Review</strong>, <strong>Accepted</strong>, or <strong>Deprecated</strong>.</li><li><strong>Created By</strong>: The user who created the policy or standard entry in Data Catalog.</li><li><strong>Updated By</strong>: The user who last updated the policy or standard entry in Data Catalog.</li><li><strong>Last Updated</strong>: The date and time when the policy or standard data was last updated.</li></ul><p><strong>Non-mandatory built-in properties</strong></p><ul><li><strong>Effective From-Until</strong>: The date that the policy or standard goes into effect and the date that it expires.</li><li><strong>Policy Review Date or Standard Review Date</strong>: The date to review the policy or standard.</li><li><strong>Policy version or Standard version</strong>: The version for the policy or standard.</li><li><strong>Custodian</strong>: The user responsible for managing and maintaining the policy or standard.</li><li><strong>Business Steward</strong>: The business steward responsible for the policy or standard.</li><li><strong>Owners</strong>: The user or users who own the policy or standard.</li></ul><p><strong>Note</strong>: For glossaries and policies, administrators can manage the visibility of selected built-in properties. For more information, see <a href="https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-properties#enable-or-disable-built-in-properties">Enable or disable built-in properties</a>.</p></td></tr><tr><td><strong>Custom Properties</strong></td><td>Lists the custom properties associated with the resource. Custom properties refer to user-defined metadata attributes or fields that can be associated with various data assets. For more information, see <a href="../ldc-resource-properties-user-guide-cp#custom-properties">Custom properties</a>.</td></tr><tr><td><strong>Tags</strong></td><td>Lists the tags that are linked to the policy or standard. You can also add your own tags,which assist in identifying the resource using specific keywords.</td></tr><tr><td><strong>Style</strong></td><td>Displays the icon, title, and color associated with the policy or standard. With the business steward role, you can click the <strong>Edit</strong> (pencil) icon to select a different icon, update the title, and change the color. Then you can click <strong>Apply</strong>, the selected icon and color are updated immediately, and the updated title appears in the asset header and in the breadcrumb navigation. You can also choose <strong>Apply to all siblings</strong> to apply the same visual changes to all sibling assets at the same level.<br><br>▶️ Watch a guided walkthrough on <a href="https://assets.demos.hitachivantara.com/psl/d4h0ewc">editing icons, titles, and colors in the Style panel</a> in Data Catalog.</td></tr></tbody></table>

#### **Custom Properties** tab

You can use custom properties to annotate and categorize the data with additional context-specific information, enhancing the metadata available for data assets within Data Catalog. This tab lists the custom properties and values added to the policy or standard.

To manage custom properties, select **Manage properties** to open the **Custom Properties** page in the **Management** section. For more information, see [Manage custom properties](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-custom-properties) in [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document.

#### **Business Terms tab**

In the context of policies and standards, business terms identify the general business context of the policy or standard. For example, if the policy or standard is related to the finance domain, then it can have business terms assigned like ‘Finance,’ ‘Banking,’ or ‘Accounting.’ In this tab, you can explore the business terms information associated with the policy or standard, such as name, parent, and owner.

To add a business term, click **Add Terms** and choose the business term you want to associate with the policy or standard. After you add any business term to the policy or standard, it creates a relationship between the term and the policy or standard. Subsequently, the policy or standard appears on the **Policies** tab of the corresponding business term in [Business Glossary](https://docs.pentaho.com/pdc-use/pdc-business-glossary). You can also click **Delete**, which only removes the association between the policy or standard and the business term but does not delete the actual business term.

#### **Comment tab**

The **Comment** tab is a collaborative feature that allows users to discuss and provide feedback on specific data assets within Data Catalog. You can add comments, share suggestions, or ask questions directly in the tab using the provided text box, which includes basic formatting options like bold, italic, and bullet points. In addition, you can tag other users by mentioning them with the "@" symbol followed by their username. Then the specific user, or users, are notified of the comment through email and in the Mentions tab on the Data Catalog landing page, prompting them to respond if necessary. For more information, see [Tour of the Home page](https://docs.pentaho.com/pdc-use/ldc-quick-start-user-guide-cp#tour-of-the-home-page).

**Note:** In the Comment tab, you can:

* Tag users who have been configured in Data Catalog.
* Only delete the comments you posted.
* Delete any comment if you are an admin.

#### **Applications tab**

For a standard, the **Applications** tab contains the linked applications and additional information associated with each application.

To add an application. click **Add Applications** and choose the application you want to link to the standard. Subsequently, the standard and the parent policy appear on the **Policies** tab of the corresponding application on the Applications page. Users with permission can click **Delete**, which removes the association between the application and the standard but does not delete the actual application.

#### **Rules tab**

For a standard, the **Rules** tab contains the linked rule definitions and additional information associated with each rule definition.

To add a rule definition. click **Add Rule definition(s)** and choose the rule you want to link to the standard. Users with permission can click **Delete**, which only removes the association between the rule definition and the standard but does not delete the actual rule definition.

### Policy table view

In the Navigation pane, under **Actions**, when you choose **View Table**, it displays the policies and standards. The information is organized by Name, Type, Parent, Domain, Owner, and Tags. In the table view, you can view key details for each asset, including any custom properties, and the dates and times it was created and last updated. Additionally, you can see which user created and last updated each asset. You can use tabs at the top to view just policies or just standards, or you can view them all in one table by clicking **All**.

You can also filter the display or use the **Actions** button to add a new policy or standard, import, or export. You can click **View Hierarchy** to return to the Hierarchy view.

### Policy galaxy view

In the Navigation pane, under **Actions**, when you choose **View Table**, it displays the policies and standards. In the table view, you can view key details for each asset, including any custom properties, and the dates and times it was created and last updated. Additionally, you can see which user created and last updated each asset. You can use tabs at the top to view just policies or just standards, or you can view them all in one table by clicking **All**.

You can also filter the display or use the **Actions** button to add a new policy or standard, import, or export. You can click **View Hierarchy** to return to the Hierarchy view.
