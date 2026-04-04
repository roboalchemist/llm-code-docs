# Source: https://docs.pentaho.com/pentaho-data-mastering/setting-up-business-domains/removing-a-business-domain.md

# Removing a business domain

Remove a business domain when you no longer want to control how the data in that specified category is processed. For example, you might choose to remove one business domain because you want to use a different domain to control the related data elements.

You must have admin privileges to remove a business domain.

Complete the following steps to remove a business domain:

1. &#x20;On the left navigation menu, click **Master Data**. The **Master Data** page opens.
2. In the Business Domains card, click **Business Domains**.

   The Business Domain page opens with the business domains shown in a table.
3. At the end of the row that contains the business domain row that you want to remove, click the more options icon and select **Remove**
4. Click **Remove**.

   The Remove Business Domain confirmation box appears.
5. Click **Remove** to confirm that you want to remove the business domain.

   A confirmation message is displayed at the top of the page and the business domain is removed.

   **Note:** If the user selected the **Local** option while creating the business domain, removing the business domain removes all the data related to that business domain from local tables. However, if the user selected the **External Data Source** option while creating the business domain, removing the business domain removes only the internal Postgres tables for that business domain.
