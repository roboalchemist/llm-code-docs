# Source: https://upstash.com/docs/redis/howto/importexport.md

# Import/Export Data

## Using Upstash Console

You can use the migration wizard in the
[Upstash console](https://console.upstash.com) to import your Redis to Upstash.
In the database list page, click on the `Import` button, you will see the dialog
like below:

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/import/import.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=99d17377bf60bf21d22b9aa5dd1c9d7e" width="60%" data-og-width="1058" data-og-height="1126" data-path="img/import/import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/import/import.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=102a8daa70a8585410f3efebe2848175 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/import/import.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=a8650496bf4d54db8a1121b5c1027315 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/import/import.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=814e8cd74042ec5e156f3d6183be8f9b 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/import/import.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=f0e55279dcd2aff227cb96dcd87ba536 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/import/import.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=d97cabd9ac40ef4110b991dbb8025f93 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/import/import.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=794c822ee814f035602b468d460eec35 2500w" />
</Frame>

You can move your data from either an Upstash database or a database in another
provider (or on premise).

<Info>
  All the data will be deleted (flushed) in the destination database before the
  migration process starts.
</Info>

## Using upstash-redis-dump

You can also use the
[upstash-redis-dump](https://github.com/upstash/upstash-redis-dump) tool
import/export data from another Redis.

The below is an example how to dump and import data:

```shell  theme={"system"}
$ upstash-redis-dump -db 0 -host eu1-moving-loon-6379.upstash.io -port 6379 -pass PASSWORD -tls > redis.dump
Database 0: 9 keys dumped
```

See [upstash-redis-dump repo](https://github.com/upstash/upstash-redis-dump) for
more information.
