# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-metadata-similarity-suggestions.md

# Manage metadata similarity suggestions

This section provides step-by-step guidance for running and managing metadata similarity suggestions in Pentaho Data Catalog. The metadata similarity feature uses machine learning to identify and suggest similar tables, columns, and business terms across the data landscape. These suggestions help improve consistency, streamline glossary tagging, and reduce redundancy across datasets. This section helps you to:

* Begin metadata similarity jobs
* Explore and understand similar items suggested
* Take informed actions by approving or rejecting suggested similar items

## Run the metadata similarity process

Perform the following procedure to run the metadata similarity in Data Catalog to identify similar tables, columns, and business terms across different databases:

1. Click **Management** in the left navigation menu.

   The **Manage Your Environment** page opens.
2. In the Metadata Similarity card, click **Configure Similarity**

   The **Metadata Similarity Configuration** page opens.
3. Select the databases for which you want to run metadata similarity and identify similar items.
4. (optional) Select one or more business terms.
5. Click **Apply** to run the metadata similarity process.

   The metadata similarity (Miscellaneous Jobs Worker) process begins.

You have successfully run the metadata similarity process to identify similar tables, columns, and business terms across selected databases.

Once the metadata similarity process is completed, you can view suggestions on the **Similar Items** tab of the respective assets. For more information, see [Review suggested similar items for data assets](#review-suggested-similar-items-for-data-assets) and [Review suggested similar items for business terms](#review-suggested-similar-items-for-business-terms).

## Review suggested similar items for data assets

When you have [run the metadata similarity process](#run-the-metadata-similarity-process), perform the following procedure to view and accept or reject the suggested similar items for the respective data asset.

1. Click **Data Canvas** on the left navigation menu.
2. Select the data asset (table, column, or file) to which you want to view suggested similar items.

   * When you select a table or file, click the **Similar Items** tab.
   * When you select a column, click the **Glossary** tab and then select the **Suggested** pane.\
     The list of Similar Items, including a similarity score and status, appears. It contains items only with a similarity score greater than the default threshold (0.5).

   **Tip:** Higher similarity scores indicate a stronger match based on metadata structure and meaning.

   **Note:** You can also click item to view the respective data asset in focused view.
3. (Optional) You can modify the similarity score in the **Score Threshold** box.
   * Enter a lower score to see more loosely matched items.
   * Enter a higher score to see fewer, more closely matched items.
4. Click **Submit** to apply the filter.
5. In the Similar Items list, review the suggested items and select the checkboxes next to the items:
   * To accept the suggestions, select **Approve**.

     For tables, approving or rejecting a suggestion updates its status in the Similar Items tab. For columns, approving selected terms in the **Glossary** > **Suggested** pane automatically assigns those terms to the column.
   * To discard them, select **Reject**.\
     **CAUTION:** If you reject a suggested item, Pentaho Data Catalog will not include it in future similarity suggestions.
6. (Optional) You can also select the **Show Approved** or **Show Rejected** checkboxes and filter the list to show only respective items.

You have successfully reviewed the suggested items for data assets.

You can also [review the suggested items for business terms](#review-suggested-similar-items-for-business-terms).

## Review suggested similar items for business terms

Once you have [run the metadata similarity process](#run-the-metadata-similarity-process), perform the following procedure to view and accept or reject the suggested similar items for the respective business term.

1. Click **Business Glossary** on the left navigation menu.
2. Select the business term to which you want to view similar items and click **Data Elements** tab.

   The list of Similar Items, including a similarity score and status, appears. It contains items only with a similarity score greater than the default threshold (0.5).

   ![The list of suggested similar items for the selected business terms](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-23d0912f745a5411ed6f9342d3312813181dd1c6%2FSuggested%20Item%20for%20a%20business%20term%20in%20Data%20Catalog.png?alt=media)

   **Tip:** Higher similarity scores indicate a stronger match based on metadata structure and meaning.

   **Note:** You can also click item to view the respective data asset in focused view.
3. (Optional) You can modify the similarity score in the **Score Threshold** box.
   * Enter a lower score to see more loosely matched items.
   * Enter a higher score to see fewer, more closely matched items.
4. Click **Submit** to apply the filter.
5. In the Similar Items list, review the suggested items and select the checkboxes next to the items:

   * To accept the suggestions, select **Approve**. On approval, the associated term is automatically assigned to that column. You can view the assigned column under the **Data Elements** tab.
   * To discard them, select **Reject**.

   **CAUTION:** If you reject a suggested item, Pentaho Data Catalog will not include it in future similarity suggestions.
6. (Optional) You can also select the **Show Approved** or **Show Rejected** checkboxes and filter the list to show only the respective items.

You have successfully reviewed the suggested items for business terms.

You can also [review the suggested items for data assets](#review-suggested-similar-items-for-business-terms).
