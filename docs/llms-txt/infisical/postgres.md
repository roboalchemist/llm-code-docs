# Source: https://infisical.com/docs/integrations/app-connections/postgres.md

# PostgreSQL Connection

> Learn how to configure a PostgreSQL Connection for Infisical.

Infisical supports connecting to PostgreSQL using a database role.

## Configure a PostgreSQL Role for Infisical

<Steps>
  <Step title="Create a Role">
    Infisical recommends creating a designated role in your PostgreSQL database for your connection.

    ```SQL  theme={"dark"}
    -- create user role
    CREATE ROLE infisical_role WITH LOGIN PASSWORD 'my-password';

    -- grant login access to the specified database
    GRANT CONNECT ON DATABASE my_database TO infisical_role;
    ```
  </Step>

  <Step title="Grant Relevant Permissions">
    Depending on how you intend to use your PostgreSQL connection, you'll need to grant one or more of the following permissions.

    <Tip>
      To learn more about PostgreSQL's permission system, please visit their [documentation](https://www.postgresql.org/docs/current/sql-grant.html).
    </Tip>

    <Tabs>
      <Tab title="Secret Rotation">
        For Secret Rotations, your Infisical user will require the ability to alter other users' passwords:

        ```SQL  theme={"dark"}
        -- enable permissions to alter login credentials
        ALTER ROLE infisical_role WITH CREATEROLE;
        ```

        <Tip>
          In some configurations, the role performing the rotation must be explicitly granted access to manage each user. To do this, grant the user's role to the rotation role with:

          ```SQL  theme={"dark"}
          -- grant each user role to admin user for password rotation
          GRANT <secret_rotation_user> TO <infisical_role> WITH ADMIN OPTION;
          ```

          Replace `<secret_rotation_user>` with each specific username whose credentials will be rotated, and `<infisical_role>` with the role that will perform the rotation.
        </Tip>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Get Connection Details">
    You'll need the following information to create your PostgreSQL connection:

    * `host` - The hostname or IP address of your PostgreSQL server
    * `port` - The port number your PostgreSQL server is listening on (default: 5432)
    * `database` - The name of the specific database you want to connect to
    * `username` - The role name of the login created in the steps above
    * `password` - The role password of the login created in the steps above
    * `sslCertificate` (optional) - The SSL certificate required for connection (if configured)

    <Note>
      If you are self-hosting Infisical and intend to connect to an internal/private IP address, be sure to set the `ALLOW_INTERNAL_IP_CONNECTIONS` environment variable to `true`.
    </Note>
  </Step>
</Steps>

## Create Connection in Infisical

<Tabs>
  <Tab title="Infisical UI">
    1. Navigate to the **App Connections** page in the desired project.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections Tab" />

    2. Select the **PostgreSQL Connection** option.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/postgres/select-postgres-connection.png" alt="Select PostgreSQL Connection" />

    3. Select the **Username & Password** method option and provide the details obtained from the previous section and press **Connect to PostgreSQL**.

    <Note>
      Optionally, if you'd like Infisical to manage the credentials of this connection, you can enable the Platform Managed Credentials option.
      If enabled, Infisical will update the password of the connection on creation to prevent external access to this database role.
    </Note>

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/postgres/create-username-and-password-method.png" alt="Create PostgreSQL Connection" />

    4. Your **PostgreSQL Connection** is now available for use.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/postgres/username-and-password-connection.png" alt="Assume Role PostgreSQL Connection" />
  </Tab>

  <Tab title="API">
    To create a PostgreSQL Connection, make an API request to the [Create PostgreSQL
    Connection](/api-reference/endpoints/app-connections/postgres/create) API endpoint.

    <Note>
      Optionally, if you'd like Infisical to manage the credentials of this connection, you can set the `isPlatformManagedCredentials` option to `true`.
      If enabled, Infisical will update the password of the connection on creation to prevent external access to this database role.
    </Note>

    ### Sample request

    ```bash Request theme={"dark"}
    curl    --request POST \
    --url https://app.infisical.com/api/v1/app-connections/postgres \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "my-pg-connection",
        "method": "username-and-password",
        "isPlatformManagedCredentials": true,
        "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
        "credentials": {
            "host": "123.4.5.6",
            "port": 5432,
            "database": "default",
            "username": "infisical_role",
            "password": "my-password",
            "sslEnabled": true,
            "sslRejectUnauthorized": true
        },
    }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
        "appConnection": {
            "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "name": "my-pg-connection",
            "projectId": "7ffbb072-2575-495a-b5b0-127f88caef78",
            "version": 1,
            "orgId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "app": "postgres",
            "method": "username-and-password",
            "isPlatformManagedCredentials": true,
            "credentials": {
                "host": "123.4.5.6",
                "port": 5432,
                "database": "default",
                "username": "infisical_role",
                "sslEnabled": true,
                "sslRejectUnauthorized": true
            }
        }
    }
    ```
  </Tab>
</Tabs>
