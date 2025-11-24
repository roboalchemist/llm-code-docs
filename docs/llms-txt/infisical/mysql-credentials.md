# Source: https://infisical.com/docs/documentation/platform/secret-rotation/mysql-credentials.md

# MySQL Credentials Rotation

> Learn how to automatically rotate MySQL credentials.

## Prerequisites

1. Create a [MySQL Connection](/integrations/app-connections/mysql) with the required **Secret Rotation** permissions
2. Create two designated database users for Infisical to rotate the credentials for. Be sure to grant each user login permissions for the desired database with the necessary privileges their use case will require.

   An example creation statement might look like:

   ```SQL  theme={"dark"}
   -- create user roles
   CREATE USER 'infisical_user_1'@'%' IDENTIFIED BY 'temporary_password';
   CREATE USER 'infisical_user_2'@'%' IDENTIFIED BY 'temporary_password';

   -- grant all privileges
   GRANT ALL PRIVILEGES ON my_database.* TO 'infisical_user_1'@'%';
   GRANT ALL PRIVILEGES ON my_database.* TO 'infisical_user_2'@'%';

   -- apply the privilege changes
   FLUSH PRIVILEGES;
   ```

   <Tip>
     To learn more about the MySQL permission system, please visit their [documentation](https://dev.mysql.com/doc/refman/8.4/en/grant.html).
   </Tip>
3. Ensure your network security policies allow incoming requests from Infisical to this rotation provider, if network restrictions apply.

## Create a MySQL Credentials Rotation in Infisical

<Tabs>
  <Tab title="Infisical UI">
    1. Navigate to your Secret Manager Project's Dashboard and select **Add Secret Rotation** from the actions dropdown.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/generic/add-secret-rotation.png" alt="Secret Manager Dashboard" />

    2. Select the **MySQL Credentials** option.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/mysql-credentials/select-mysql-credentials-option.png" alt="Select MySQL Credentials" />

    3. Select the **MySQL Connection** to use and configure the rotation behavior. Then click **Next**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/mysql-credentials/mysql-credentials-configuration.png" alt="Rotation Configuration" />

       * **MySQL Connection** - the connection that will perform the rotation of the configured database user credentials.
       * **Rotation Interval** - the interval, in days, that once elapsed will trigger a rotation.
       * **Rotate At** - the local time of day when rotation should occur once the interval has elapsed.
       * **Auto-Rotation Enabled** - whether secrets should automatically be rotated once the rotation interval has elapsed. Disable this option to manually rotate secrets or pause secret rotation.

    4. Input the usernames of the database users created above that will be used for rotation. Then click **Next**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/mysql-credentials/mysql-credentials-parameters.png" alt="Rotation Parameters" />

       * **Database Username 1** - the username of the first user that will be used for rotation.
       * **Database Username 2** - the username of the second user that will be used for rotation.

    5. Specify the secret names that the active credentials should be mapped to. Then click **Next**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/mysql-credentials/mysql-credentials-secrets-mapping.png" alt="Rotation Secrets Mapping" />

       * **Username** - the name of the secret that the active username will be mapped to.
       * **Password** - the name of the secret that the active password will be mapped to.

    6. Give your rotation a name and description (optional). Then click **Next**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/mysql-credentials/mysql-credentials-details.png" alt="Rotation Details" />

       * **Name** - the name of the secret rotation configuration. Must be slug-friendly.
       * **Description** (optional) - a description of this rotation configuration.

    7. Review your configuration, then click **Create Secret Rotation**.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/mysql-credentials/mysql-credentials-confirm.png" alt="Rotation Review" />

    8. Your **MySQL Credentials** are now available for use via the mapped secrets.
       <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/secret-rotations-v2/mysql-credentials/mysql-credentials-created.png" alt="Rotation Created" />
  </Tab>

  <Tab title="API">
    To create a MySQL Credentials Rotation, make an API request to the [Create MySQL Credentials Rotation](/api-reference/endpoints/secret-rotations/mysql-credentials/create) API endpoint.

    ### Sample request

    ```bash Request theme={"dark"}
    curl --request POST \
    --url https://us.infisical.com/api/v2/secret-rotations/mysql-credentials \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "my-mysql-rotation",
        "projectId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "description": "my database credentials rotation",
        "connectionId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "environment": "dev",
        "secretPath": "/",
        "isAutoRotationEnabled": true,
        "rotationInterval": 30,
        "rotateAtUtc": {
            "hours": 0,
            "minutes": 0
        },
        "parameters": {
            "username1": "infisical_user_1",
            "username2": "infisical_user_2"
        },
        "secretsMapping": {
            "username": "MYSQL_USERNAME",
            "password": "MYSQL_PASSWORD"
        }
    }'
    ```

    ### Sample response

    ```bash Response theme={"dark"}
    {
        "secretRotation": {
            "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "name": "my-mysql-rotation",
            "description": "my database credentials rotation",
            "secretsMapping": {
                "username": "MYSQL_USERNAME",
                "password": "MYSQL_PASSWORD"
            },
            "isAutoRotationEnabled": true,
            "activeIndex": 0,
            "folderId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "connectionId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "rotationInterval": 30,
            "rotationStatus": "success",
            "lastRotationAttemptedAt": "2023-11-07T05:31:56Z",
            "lastRotatedAt": "2023-11-07T05:31:56Z",
            "lastRotationJobId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "nextRotationAt": "2023-11-07T05:31:56Z",
            "connection": {
                "app": "mysql",
                "name": "my-mysql-connection",
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
            },
            "environment": {
                "slug": "dev",
                "name": "Development",
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
            },
            "projectId": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
            "folder": {
                "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
                "path": "/"
            },
            "rotateAtUtc": {
                "hours": 0,
                "minutes": 0
            },
            "lastRotationMessage": null,
            "type": "mysql-credentials",
            "parameters": {
                "username1": "infisical_user_1",
                "username2": "infisical_user_2"
            }
        }
    }
    ```
  </Tab>
</Tabs>
