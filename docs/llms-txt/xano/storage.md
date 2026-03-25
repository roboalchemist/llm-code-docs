# Source: https://docs.xano.com/the-database/database-performance-and-maintenance/storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Database Storage Explained

<Info>
  Database storage uses high-performance solid-state drives (SSD). This storage is used only for the database schema, the metadata of each database record, and the indexes on the metadata. Any media references in the database records would be metadata only as the actual binary of this media is stored in separate media storage.
</Info>

### Explaining Database Usage

In Xano, your data is stored in a PostgreSQL database, which allows for incredibly powerful structure, scalability, and speed. In your dashboard, you have the ability to see exactly how much of your database storage is occupied, to help guide you in making decisions about what data to keep, or if it’s time to upgrade your instance with more storage to suit your needs.

Database storage is different from file storage. Think of a folder on your computer that you delete a file inside of. When you do this, your computer doesn’t immediately destroy the data – that file is hidden from you, marked as inaccessible, and the storage that file occupies is now marked as available. Your computer then calculates the available storage, taking this newly available space into account. This all happens in real time.

Now, in terms of a database, where your Xano data is stored, deleting a row does not immediately remove this row from your storage. This approach is required to ensure that things like versioning and backups can still continue to function, and to account for anything else that may still be accessing that data. Eventually, that data will not be relevant to any operation, and the space it occupies must then be reclaimed for reuse by new rows. This is something that occurs on your workspace at regular intervals with scheduled maintenance.

#### I deleted some records, but my storage is still the same. What’s going on?

As stated above, when records are removed, to support certain Xano features, as well as by design on the PostgreSQL database, that space is not immediately going to be marked as available and computed in your storage statistics – however, eventually the space those records were occupying will be reused when adding new records. In addition, it’s important to remember when considering this that a database table with 1000 records, that has had 999 of them deleted, is not the same in terms of structure or storage requirements as a brand new table with only one record.

#### My storage usage doesn’t seem to be updating.

Your storage statistics are updated at regular intervals throughout the day, and are not real-time. We’d love to be able to offer more control over data architecture and maintenance in the future, and if that’s something you are looking for, make sure to let us know on our feature request board.

#### What is actually taking up database storage?

There are several different components that make up your Xano database, and they can all contribute to database storage.

This includes:

* Database table schema<br />*What fields you've set and the settings that accompany them*
* Records<br />*This is your actual data that you are storing in your database.*
* [Indexing](/the-database/database-performance-and-maintenance/indexing)<br />*Some indexes are auto-generated and required to maintain your table. Others are manually added by you, and can take up a varying amount of space.*
* [Request History](/maintenance-monitoring-and-logging/request-history)<br />*When you make requests to your Xano APIs or run background tasks, this history is logged on a 24-hour rolling cycle. Sometimes, if you have an exceptional amount of history, this will be reflected as used database storage, as it is stored in a similar fashion to your database records behind the scenes.*


Built with [Mintlify](https://mintlify.com).