# Source: https://posthog.com/docs/data-warehouse/sources/redshift.md

# Source: https://posthog.com/docs/cdp/batch-exports/redshift.md

# Source: https://posthog.com/docs/cdp/sources/redshift.md

# Linking Redshift as a source - Docs

The Redshift connector can link your database tables to PostHog.

To link Redshift:

1.  Go to the [Data pipeline page](https://app.posthog.com/data-management/sources) and the sources tab in PostHog
2.  Click **New source** and select Redshift
3.  Enter your database connection details:
    -   **Host:** The hostname or IP of your Redshift cluster like `my-cluster.abc123.us-east-1.redshift.amazonaws.com`.
    -   **Port:** The port your Redshift cluster is listening on. The default is `5439`.
    -   **Database:** The name of the database you want like `analytics_db`.
    -   **User:** The username with the necessary permissions to access the database.
    -   **Password:** The password for the user.
    -   **Schema:** The schema for your database where your tables are located. The default is `public`.
4.  Click **Next**

The data warehouse then starts syncing your Redshift data. You can see details and progress in the [sources tab](https://app.posthog.com/data-management/sources).

> **Permissions:** The Redshift source only requires read permissions on the schemas and tables you intend to sync.

#### Inbound IP addresses

We use a set of IP addresses to access your instance. To ensure this connector works, add these IPs to your inbound security rules:

| US | EU |
| --- | --- |
| 44.205.89.55 | 3.75.65.221 |
| 44.208.188.173 | 18.197.246.42 |
| 52.4.194.122 | 3.120.223.253 |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better