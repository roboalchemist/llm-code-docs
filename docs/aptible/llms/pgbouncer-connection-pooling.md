# Source: https://www.aptible.com/docs/how-to-guides/database-guides/pgbouncer-connection-pooling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying PgBouncer on Aptible

> How to deploy PgBouncer on Aptible

PgBouncer is a lightweight connection pooler for PostgreSQL which helps reduce resource usage and overhead by managing database connections.
This guide provides a overview on how you can get started with PgBouncer on Aptible and [Dockerfile Deploy](https://www.aptible.com/docs/core-concepts/apps/deploying-apps/image/deploying-with-git/overview#deploying-with-git).

<Steps>
  <Step title="Setting Up PgBouncer">
    <Accordion title="Gather Database Variables">
      To successfully use and configure PgBouncer, you'll need to have a PostgreSQL database you want to pool connections for. From that database, you'll need to know the following:

      * PostgreSQL username
      * PostgreSQL password
      * PostgreSQL host
      * PostgreSQL port
      * PostgreSQL database name
        These values can be retrieved from the [Database Credentials](https://www.aptible.com/docs/core-concepts/managed-databases/connecting-databases/database-credentials#overview) in the UI, and will be used to set configuration variables later in the guide.
        For example:

      ```
      If the Database Credentials were
      postgresql://aptible:very_secure_password@db-aptible-docs-example-1000.aptible.in:4000/db

      PostgreSQL username      = 'aptible'
      PostgreSQL password      = 'very_secure_password'
      PostgreSQL host          = 'db-aptible-docs-example-1000.aptible.in'
      PostgreSQL port          = 4000
      PostgreSQL database name = 'db'
      ```
    </Accordion>

    <Accordion title="Create your PgBouncer Application">
      Through the UI or CLI, create the PgBouncer application, and set a few variables:

      ```
        aptible apps:create pgbouncer
        aptible config:set --app pgbouncer \
        POSTGRESQL_USERNAME='aptible' \
        POSTGRESQL_PASSWORD=$PASSWORD \
        POSTGRESQL_DATABASE='db' \
        POSTGRESQL_HOST='$DB_HOSTNAME' \
        POSTGRESQL_PORT='$DB_PORT' \
        PGBOUNCER_DATABASE='db' \
        PGBOUNCER_SERVER_TLS_SSLMODE='require' \
        PGBOUNCER_AUTH_USER='aptible' \
        PGBOUNCER_AUTH_QUERY='SELECT uname, phash FROM user_lookup($1)' \
        IDLE_TIMEOUT=2400 \
        PGBOUNCER_CLIENT_TLS_SSLMODE='require' \
        PGBOUNCER_CLIENT_TLS_KEY_FILE='/opt/bitnami/pgbouncer/certs/pgbouncer.key' \
        PGBOUNCER_CLIENT_TLS_CERT_FILE='/opt/bitnami/pgbouncer/certs/pgbouncer.crt' \
      ```

      Note that you'll need to fill out a few variables with the Database Credentials you previously gathered. We're also assuming the certificate and key you're using to authenticate will be saved as `pgbouncer.crt` and `pgbouncer.key`.
    </Accordion>

    <Accordion title="Generate a Certificate and Key for SSL Authentication">
      Since databases on Aptible require SSL, you'll also need to provide an authentication certificate and key. These can be self-signed and created using `openssl`.

      1. Generate a Root Certificate and Key

      ```
      openssl req -x509 \ 
              -sha256 -days 365 \
              -nodes \
              -newkey rsa:2048 \
              -subj "/CN=app-$APP_ID.on-aptible.com/C=US/L=San Fransisco" \
              -keyout rootCA.key -out rootCA.crt
      ```

      This creates a rootCA.key and rootCA.crt in your current directory. `-subj "/CN=app-$APP_ID.on-aptible.com/C=US/L=San Francisco"` is modifiable — notably, the Common Name, `/CN`, should match the TCP endpoint you've created for the pgbouncer App.
      If you're using a default endpoint, you can fill in \$APP\_ID with your Application's ID.

      2. Using the Root Certificate and key, create the authentication certificate and private key:

      ```
      openssl genrsa -out pgbouncer.key 2048
      openssl req -new -key pgbouncer.key -out pgbouncer.csr
      openssl x509 -req \
            -in pgbouncer.csr \
            -CA rootCA.crt -CAkey rootCA.key \
            -CAcreateserial -out pgbouncer.crt \
            -days 365 \
            -sha256
      ```
    </Accordion>
  </Step>

  <Step title="Create the Dockerfile">
    For a basic implementation, the Dockerfile is quite short:

    ```
    FROM bitnami/pgbouncer:latest
    COPY pgbouncer.key /opt/bitnami/pgbouncer/certs/pgbouncer.key
    COPY pgbouncer.crt /opt/bitnami/pgbouncer/certs/pgbouncer.crt
    ```

    We're using the PgBouncer image as a base, and then copying a certificate-key pair for TLS authentication to where PgBouncer expects them to be.
    This means that your git repository needs to contain three files: the Dockerfile, `pgbouncer.key`, and `pgbouncer.crt`.
  </Step>

  <Step title="Deploy using Git Push">
    Now you're ready to deploy. Since we're working from a Dockerfile, follow the steps in [Deploying with Git](https://www.aptible.com/docs/core-concepts/apps/deploying-apps/image/deploying-with-git/overview) to push your repository to your app's Git Remote to trigger a deploy.
  </Step>

  <Step title="Make an Endpoint for PgBouncer">
    This is commonly done by creating a TCP endpoint.

    ```
    aptible endpoints:tcp:create --app pgbouncer cmd --internal
    ```

    Instead of connecting to your database directly, you should configure your resources to connect to PgBouncer using the TCP endpoint.
  </Step>

  <Step title="Celebrate!">
    At this point, PgBouncer should be deployed. If you run into any issues, or have any questions, don't hesitate to reach out to [Aptible Support](https://app.aptible.com/support)
  </Step>
</Steps>
