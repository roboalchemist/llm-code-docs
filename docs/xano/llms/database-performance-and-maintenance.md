# Source: https://docs.xano.com/the-database/database-performance-and-maintenance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Database Performance And Maintenance

Database performance in Xano is typically dependent on three key areas.

<Steps>
  <Step title="Indexing of large tables">
    As your database table grows in size, queries against that table become more resource intensive. Every time you search for specific records in that table, the table has to go through each record, one by one, to find the matching data.

    We can combat this by using indexing. Like the index in the back of a book, this helps to let the table know where to find the requested information more quickly.

    📖 [**Learn more about indexing**](/the-database/database-performance-and-maintenance/indexing)
  </Step>

  <Step title="Creating efficient queries">
    #### Using Addons

    Addons are an easy way to get related data from multiple tables, such as users and orders. Using addons enables more efficient querying of both tables instead of using two separate queries.

    📖 [**Learn more about addons**](/the-function-stack/functions/database-requests/query-all-records#using-addons)

    #### Pagination

    Access your query settings to adjust pagination when retrieving significant amounts of records at once.
  </Step>

  <Step title="Efficient database design">
    Utilizing proper database design practices is paramount to ensuring your backend is as performant as possible. Even if you are well on your way to deploying your application, don't be afraid to make changes to your database design now to avoid future headaches.

    📖 [**Read our documentation on database design**](/the-database/designing-your-database)
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).