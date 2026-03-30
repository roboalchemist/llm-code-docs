# Content History

The Content History feature, in the 

</IdentityCard>

## Usage

**Path to use the feature:**  Content Manager <br/> From the edit view of a content type: click  (top right corner) then  **Content History**.

### Browsing Content History

With Content History, you can browse your content through:

- The main view on the left, which lists the fields and their content for the version selected in the sidebar on the right.
- The sidebar on the right, which lists the total number of versions available, and for each version:
  - the date and time when the version was created,
  - the user who created it,
  - and whether its status is Draft, Modified, or Published (see [Draft & Publish](/cms/features/draft-and-publish) for more information about document statuses).

:::note
The main view of Content History clearly states whether a field was inexistent, deleted, or renamed in other versions of the content-type. Fields that are unknown for the selected version will be displayed under an _Unknown fields_ heading below the other fields.
:::

### Restoring a previous version

You can choose to restore a previous version of a document. When restoring a version, the content of this version will override the content of the current draft version. The document switches to the Modified status and you will then be able to publish the content whenever you want (see [Publishing a draft](/cms/features/draft-and-publish#publishing-a-draft)).

1. Browse the Content History and select a version via the sidebar on the right.
2. Click the **Restore** button.
3. In the _Confirmation_ window, click **Restore**.  

:::note
If the [Internationalization (i18n)](/cms/features/internationalization) feature is enabled for the content-type, restoring a version with a unique field (i.e. a field whose content is the same for all locales) will restore the content of this field for all locales.
:::