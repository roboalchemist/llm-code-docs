# Source: https://docs.tokens.studio/figma/import/variables/connect-themes-to-imported-variables.md

# Connect Themes to Imported Variables

## Connect Themes to Imported Variables

If you were hoping to import your Variables and use Tokens Studio as your source of truth for maintaining your design decisions, our Themes feature (pro) makes this possible.

The **Themes** feature has a concept of **Groups of Themes**, which allows the plugin to connect to a Variable collection with multiple modes.

{% content-ref url="../../../manage-themes/themes-overview" %}
[themes-overview](https://docs.tokens.studio/manage-themes/themes-overview)
{% endcontent-ref %}

If you have a Pro Licence for Tokens Studio, here are the steps to attach the Imported Variables to Themes, allowing you to use the plugin to update your Variables.

{% hint style="info" %}
The most important thing to pay attention to is the names, so the ID of our Themes can correctly attach to a Variable collection.

Theme Group = Collection \
Theme = Mode
{% endhint %}

The image below shows how **Theme Groups** and **Themes** map to Figma's Variable collections and modes.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FN6RdrBK20GxVRlARRmIO%2FVariables-export-themes-collection-annotated-V2-1.png?alt=media&#x26;token=ab9ab0dc-50c9-4eea-86a5-91111f5bd28f" alt=""><figcaption><p>The Tokens Page in the Plugin with the Themes Menu Open next to a Variable Collection in Figma. <br>The annotations show the relationship between Variable Collection and Theme Group Names as well as Variable Modes and Theme Names. </p></figcaption></figure>

***

### How it Works

Once you Import your Variables Into Tokens Studio, you've taken a "snapshot" of the Variables and their values as Tokens in the Plugin. You need to establish a relationship between the Tokens and the Variables, and Themes are how the Plugin is able to attach the Tokens to Variables across multiple modes and collections.&#x20;

This is the same example used in the Import Variables Guide.&#x20;

{% content-ref url="" %}
[](https://docs.tokens.studio/figma/import/variables)
{% endcontent-ref %}

After the Import is complete, in the Plugin you will see:&#x20;

* Each Variable collection becomes a folder of Token Sets, with the folder name matching the collection name.
* Each Mode within the Variable Collection becomes an individual Token Set, with the Set name matching the Mode name, nested within the folder name matching the collection name.&#x20;
* Each Variable is created as a Design Token with the same name and value.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FeFStwejey8sRDKDZeEea%2FVariables%20to%20Token%20Sets%20-%20Collections%20%2B%20modes%20to%20sets.png?alt=media&#x26;token=be9e1927-4847-4150-a27a-2ec71e9f46c5" alt=""><figcaption><p>Figma Variable Collection beside the Tokens Page in the Plugin. <br>The numbered annotations show the relationship between Variable Collection and Mode names to Token Set names. </p></figcaption></figure>

To attach the Design Tokens in the Plugin to the Variables in Figma, you'll:

1. Create Theme Groups and Themes with names that match the Variable Collections and Modes.&#x20;
2. Attach the Themes with Variables using the Export to Figma feature.
3. Check the connection between your Themes and Variables.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FjUvILuxUWwWde8DdRcjb%2FVariables%20to%20Themes%20Manager%20Modes.png?alt=media&#x26;token=354bb0b1-4e0c-4268-8a52-6040d43b3937" alt=""><figcaption><p>Figma Variable Collection beside the Themes Manager in the Plugin. <br>The numbered annotations show the Theme Group to Collection names. The lettered annotations show the Theme to Mode names. </p></figcaption></figure>

***

### **1. Create Theme Groups and Themes**

When the Plugin completed the import, each Token Set name contains the `collection/mode`, so you will use this to create the `theme-group/theme` names to match.

The easiest way to do this so there is an exact match is to copy the Token Set name.

#### Copy the Token Set Name

1. Right-click on the Token Set Name (left side navigation panel on the Tokens page).
2. Select **Rename**.
   1. The Rename Token Set modal appears with the current name inside the text input.
3. **Select the current name** from the input and copy it using a keyboard shortcut.
   * command + C on a Mac
   * control + C on a PC
4. **Paste the name** in a text editor of your choice.
   * For example `brands/apple` is the full set name in the image below.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F36FNCxYgXgTBYXITmxlO%2Ftoken-set-rightClick-rename-V2-2.png?alt=media&#x26;token=d4c75772-23cf-4cd5-8cba-50bedc627259" alt=""><figcaption><p>Right-click on any Token Set name to open its action menu. Selecting Rename will open a form. You can select the name in the input and copy it for use in the following steps. </p></figcaption></figure>

#### Open the Themes Manager

From the Tokens Page of the Plugin, open the **Themes** dropdown (it doesn't matter what Token Set is showing on the page):

* Select **Manage Themes**
* Select **New Theme**

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FuVaTgN8x3VSKNc6Hy4Ic%2Fthemes-empty-V2-2.png?alt=media&#x26;token=24f3876b-627e-4c79-a146-597691527058" alt=""><figcaption><p>Select the Theme dropdown to open the menu. Select <code>Manage themes</code>to view the Themes Manager. The example on the right shows the Themes Manager before any Themes are created. </p></figcaption></figure>

#### Create a new Theme

From the Themes manager, select the New Theme button.&#x20;

Once the Create Themes form is open:

1. Select **+ add group** from the top left.
   * Paste in the part of the Token Set name that appears before the `/`
   * For example `brands`
2. Select the **Theme name** input and paste the part of the Token Set name that appears after the `/`.
   * For example `apple`
3. Under the inputs is a complete list of all Token Sets.
   * Ensure only Token Set with the name matching the Theme you are creating has the **Status** of **Enabled** (checkmark icon button is highlighted).
   * Ensure **all other Token Sets** have a **Status** of **Disabled** (X icon button is highlighted).
4. Select **Save Theme** to finish.
   * You'll return to the Themes Manager where your new Theme is now listed.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FuKL4YGRj4UQZhhHSbw8V%2FthemesForm-filled-flow-V2-2.png?alt=media&#x26;token=b166f296-0aaa-49ad-91b5-5605083abd4a" alt=""><figcaption><p>After creating the first Theme, it appears in the Themes Manager. The Theme Group, Theme, and number of Sets are shown in the Theme Manger.</p></figcaption></figure>

#### Create additional themes

Now you can repeat this process for the rest of the Token Sets created from your Imported Variables.

In this example, 3 Variable collections were imported with a total of 7 Token Sets.

* `brand` Variable collection has 3 more Token Sets to add.
* `primitive` Variable collection to be created as a Theme Group with 2 Token Sets.
* `theme` Variable collection to be created as a Theme Group with 2 Token Sets.

<figure><img src="broken-reference" alt=""><figcaption><p>Figma Variable Collection beside the Tokens Page in the Plugin. <br>The numbered annotations show the relationship between Variable Collection names and Token Set names. </p></figcaption></figure>

The good news is, if you are creating an additional Theme inside an existing Theme Group, you can select the Theme Group from the form instead of typing it each time.

In this example, the `brands` Theme Group created previously appears in the dropdown while adding the new Theme called `berry.`

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2F6Ghv08ChPTwqjvxx8Mtq%2FthemesForm-select-open-flow-V2-2.png?alt=media&#x26;token=d9a71210-9748-453f-8352-461ad492299a" alt=""><figcaption><p>From the Theme form, the Add Group dropdown shows all Theme Groups previously created. Selecting a Theme Group from the dropdown makes it quick and easy to create additional Themes in the same Group. </p></figcaption></figure>

When all Token Sets have been added into Theme Groups, you are ready to create the connection to the Variables.

In this example, the Themes Manager shows 3 Theme Groups with names that match the imported Variable Collections and Modes.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FH8TBn4bJkVcERpNZK11T%2FVariables%20to%20Themes%20Manager.png?alt=media&#x26;token=75526269-dd13-49d7-93b9-05ca39907505" alt=""><figcaption><p>Figma Variable Collection beside the Themes Manager in the Plugin. <br>The numbered annotations show the Theme Group to Collection names.</p></figcaption></figure>

### **2. Attach Themes with Variables**

You'll use the **Export to Figma feature** to attach your newly created Themes to your Variables in Figma. Once the connection is made, you can use The Plugin to manage your Variables.

This is a quick overview of the steps using this example.

→ [If you'd like a more detailed walkthrough of this process, read the Export to Figma from Themes guide.](https://docs.tokens.studio/figma/export/themes)

Select the **Styles & Variables Button** from the Tokens page.

* Choose the **Export Styles & Variables** option.
* The **Export Options** menu will open, ensure you have:
  * All Variable types selected
  * None of the Style types selected
  * None of the toggles selected under the **Tokens Exported to Figma should** option.
* Select confirm to close the Options menu.&#x20;

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Fe7bfe4P6LGYulpphULC2%2Ftokenspage-stylesVarMenu-export-options-V2-2%201.png?alt=media&#x26;token=9fd9041b-513a-494b-9b14-32d6e826d178" alt=""><figcaption><p>Select the Export Styles and Variables from the Tokens page to configure the Options. </p></figcaption></figure>

You should be looking at the full list of Theme Groups and Themes in your Token Structure.

* Select all Themes within the Theme Groups you just created (checkmark is visible).
* Select **Export to Figma** to complete the action.

{% hint style="info" %}
In this example, there were no Themes previously in our Token Project so all Themes are selected for export. Your project may be different!
{% endhint %}

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2Faf88b9HBx5op0LI1jKbC%2Fexport-variables-options-themes-all-V2-2.png?alt=media&#x26;token=b8deb450-9bf0-400a-af0b-dcd44b966966" alt=""><figcaption><p>After the Export Options are confirmed, all previously created Themes are displayed. In this example, all Themes are selected for Export. </p></figcaption></figure>

### 3. Check connected Themes to Variables

Your Variable collections should now be connected to Tokens Studio!&#x20;

If you navigate back to the Themes manager, you'll see a count of attached Variables for each Theme.

<figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FSqLYsR2u3bYedCAfd00m%2Ftokenspage-themes-manage-variableCount-V2-2.png?alt=media&#x26;token=02c133ec-cad4-416f-bd29-db90af67f8bd" alt=""><figcaption><p>Select the Themes dropdown from the Plugin page to see all Themes created. They are organized by Theme Group. Select Manage Themes to see the count of Sets and Variables attached to each Theme. </p></figcaption></figure>

You can test this by making a change to to a Token from the plugin, and running the **Export to Figma** action again, you should see the matching Variable change in the Figma UI.

If you have unexpected results, here are some additional guides that might be helpful in troubleshooting:

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Export to Figma from Themes</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FTPetIVSWuZKC9ykNmbkB%2Fcard-header-figma-export-themes.png?alt=media&#x26;token=93abe510-7106-4871-b977-e0a9d141d1fc">card-header-figma-export-themes.png</a></td><td><a href="../../export/themes">themes</a></td></tr><tr><td>Export Options</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FXd4p0qnCiV0gU5ShgFSd%2Fcard-header-figma-export-options.png?alt=media&#x26;token=e111be23-de02-4816-aac4-9a35fa5bd124">card-header-figma-export-options.png</a></td><td><a href="../../export/options">options</a></td></tr><tr><td>Import Variables from Figma</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FySgL4m1UesD2QxbziFMV%2Fcard-header-figma-import-variables.png?alt=media&#x26;token=a0765adf-9ad3-4d5f-ab8a-a69649fbd3dc">card-header-figma-import-variables.png</a></td><td><a href=""></a></td></tr><tr><td>Non-local Variables</td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FkPDmDsfoKXFgsIub4LjJ%2Fcard-header-figma-files.png?alt=media&#x26;token=a9f0dd2a-49b0-4816-8aec-1a32a8bbf2bd">card-header-figma-files.png</a></td><td><a href="../../non-local-files">non-local-files</a></td></tr><tr><td>Working with Variables in Tokens Studio. </td><td><a href="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FMqeS1ogOfJU7wHRyILYe%2Fcard-header-figma-variables.png?alt=media&#x26;token=62e99e18-cc17-45de-89ea-97da18143b02">card-header-figma-variables.png</a></td><td><a href="../../variables-overview">variables-overview</a></td></tr></tbody></table>
