# Source: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/spcs-execute-sql.md

# Snowpark Container Services: SQL execution

Your application container can connect to Snowflake and execute SQL. This topic describes how container code obtains the required information to connect to Snowflake, including authentication credentials, the database and schema context of the service, and the warehouse used to run SQL statements.

## Credential configuration options

Snowflake recommends that application containers use Snowflake-provided credentials to authenticate to Snowflake when executing SQL. Although it is possible to use other credentials by connecting through an external access integration (EAI), connecting through an EAI treats the service as if it were running outside Snowflake and connecting to Snowflake over the internet.

You have three options to connect to Snowflake from a service container:

* **Use Snowflake-provided service user credentials:** Snowflake provides every service with credentials, which are referred to as service credentials. A service uses these credentials to connect to Snowflake as the service user.
* **Use Snowflake-provided caller credentials (caller’s rights):** When you configure your service with caller’s rights, Snowflake also provides credentials for the service to connect to Snowflake as the calling user.
* **Use other credentials:** In this case, you use an external access integration (EAI) that allows your service to connect to Snowflake’s internet endpoint by using valid authentication credentials. This option requires an administrator to create the EAI, and then grant the USAGE privilege on the integration to the service owner role.

  > **Note:**
  >
  > If you use external access integrations to access Snowflake, you might send potentially sensitive information over the internet.

For examples of code that uses various Snowflake drivers to connect to Snowflake, see [Snowflake Connection Samples](https://github.com/Snowflake-Labs/sf-samples/tree/main/samples/spcs/sf-connection).

### Using Snowflake-provided service user credentials

When you use Snowflake-provided service credentials, be aware of the following effects:

* Every object in Snowflake has an *owner role*, which is the role that is used to create the object. A service’s owner role determines the capabilities that the service is allowed when it interacts with Snowflake. These capabilities include executing SQL, accessing stages, and performing service-to-service networking.
* When you create a service, Snowflake also creates a service user that is specific to that service. That service user has access to only two roles: the service owner role and the ‘PUBLIC’ role. The default role for the service user is the service owner role.

When you start a service, including job services, Snowflake performs several actions. In each of your application containers, Snowflake enables the container code to use drivers for connecting to Snowflake and executing SQL, which is similar to any other code on your computer connecting to Snowflake. The following list shows the actions that Snowflake performs when you start a service:

* Provides credentials (an OAuth token) in the container in a file that is named `/snowflake/session/token`. The container code uses
  these credentials to authenticate as the service user. This OAuth token can’t be used outside Snowpark Container Services
* Sets the following environment variables for you to configure a Snowflake client in your service code:

  * SNOWFLAKE_ACCOUNT: This variable is set to the [account locator](../../user-guide/admin-account-identifier.md) for the Snowflake account that the service is currently running under.
  * SNOWFLAKE_HOST: This variable provides the hostname that is used to connect to Snowflake.

When you create a connection to Snowflake as the service user, container code must use SNOWFLAKE_HOST, SNOWFLAKE_ACCOUNT, and the OAuth token. The OAuth token can’t be used without also using SNOWFLAKE_HOST.

**Example**

In [Tutorial 2](tutorials/tutorial-2.md) (see `main.py`), the code reads the environment variables as shown in the following example:

```python
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_HOST = os.getenv('SNOWFLAKE_HOST')
```

The code passes these variables to a connection creation code for the Snowflake client of choice. The container uses these
credentials to create a new session, with the service’s owner role as the session’s primary role, to run queries. The following example
shows the minimum code that you need to create a Snowflake connection in Python:

```python
def get_login_token():
  with open('/snowflake/session/token', 'r') as f:
    return f.read()

conn = snowflake.connector.connect(
  host = os.getenv('SNOWFLAKE_HOST'),
  account = os.getenv('SNOWFLAKE_ACCOUNT'),
  token = get_login_token(),
  authenticator = 'oauth'
)
```

Be aware of the following details about this OAuth token:

* Snowflake refreshes the content of the `/snowflake/session/token` file every few minutes. Every token is valid
  for up to one hour. After a container connects to Snowflake successfully, the
  expiration time doesn’t apply to the connection, as is the case with any sessions that users create directly.
* This OAuth token is valid only within the specific Snowflake service. You can’t copy the OAuth token and use it outside
  the service.
* If you use the OAuth token to connect, it creates a new session. The OAuth token is not associated with any existing SQL session.

  > **Note:**
  >
  > A significant difference between executing stored procedures and executing a service is that stored procedures run in
  > the same session as the SQL that runs the procedures. But every time a container establishes a new connection, you create a new
  > session.

To view the queries issued by a specific service user, you can use the ACCOUNTADMIN role to view the
[query history](../../user-guide/ui-snowsight-activity.md).
The user name of the service user appears in the following forms:

* For a service created before the 8.35 server release, the service user name is of the format `SF$SERVICE$unique-id`.
* For a service created after the 8.35 server release, the service user name is the same as the service name.

> **Note:**
>
> A service’s owner role is the role that created the service. You can define one or more service roles to manage access to the endpoints that the service exposes. For more information, see [Managing service-related privileges](working-with-services.md).

### About using Snowflake-provided caller credentials (caller’s rights)

In certain application scenarios, you might need to execute
queries by using the context of the end user rather than the service user as explained in the preceding section. The caller’s rights feature is used in this context.

For example, suppose that you create a service that exposes a public endpoint for a web application that displays a dashboard that uses data stored
in Snowflake. You grant other users in your Snowflake account access to the dashboard by granting them the
[service role](working-with-services.md). When a user signs in, the dashboard displays only the data that user
is authorized to access.

However, because containers by default execute queries by using the service user and the service’s owner role,
the dashboard shows the data that the service’s owner role has access to, regardless of which end user
connected to the endpoint. As a result, the dashboard isn’t limited to the data the end user is authorized to access, allowing the signed-in user to see data they shouldn’t have access to.

To limit the dashboard to show only data that is accessible to the signed in user, the application containers
must execute SQL by using privileges granted to the end user. You can enable this by using caller’s
rights in the application.

> **Note:**
>
> * The caller’s rights feature is supported only when [accessing a service](working-with-services.md) using network ingress. The feature isn’t available when using a service function to access the service.
> * The caller’s rights feature is currently not supported in a Snowflake Native App ([apps with containers](../native-apps/native-apps-about.md)).

#### Configure caller’s rights for your service

Configuring caller’s rights for your application is a two-step procedure.

1. In the [service specification](specification-reference.md), set the `executeAsCaller` to `true`, in as shown in the following specification fragment:

   ```yaml
   spec:
     containers:
     ...
   capabilities:
     securityContext:
       executeAsCaller: true
   ```

   This setting tells Snowflake that the application intends to use caller’s rights and causes Snowflake to insert the `Sf-Context-Current-User-Token` header in every incoming request before sending the request to the application container. This user token facilitates query execution as the calling user. If not specified, `executeAsCaller` defaults to `false`.

   Specifying the `executeAsCaller` option doesn’t affect the service’s ability to execute queries as the service user and service’s owner role. With `executeAsCaller` enabled, the service has the option to connect to Snowflake both as a calling user and as a service user.
2. To establish a Snowflake connection on behalf of the calling user, update your application code to create a login token that includes both the OAuth token that Snowflake provided to the service and the user token from the `Sf-Context-Current-User-Token` header.

   The login token must follow this format: `<service-oauth-token>.<Sf-Context-Current-User-Token>`.

   This update is demonstrated in the following Python code fragment:

   ```python
   # Environment variables below will be automatically populated by Snowflake.
   SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
   SNOWFLAKE_HOST = os.getenv("SNOWFLAKE_HOST")

   def get_login_token():
       with open("/snowflake/session/token", "r") as f:
           return f.read()

   def get_connection_params(ingress_user_token = None):
       # start a Snowflake session as ingress user
       # (if user token header provided)
       if ingress_user_token:
           logger.info("Creating a session on behalf of the current user.")
           token = get_login_token() + "." + ingress_user_token
       else:
           logger.info("Creating a session as the service user.")
           token = get_login_token()

       return {
           "account": SNOWFLAKE_ACCOUNT,
           "host": SNOWFLAKE_HOST,
           "authenticator": "oauth",
           "token": token
       }

   def run_query(request, query):
       ingress_user_token = request.headers.get('Sf-Context-Current-User-Token')
       # ingress_user_token is None if header not present
       connection_params = get_connection_params(ingress_user_token)
       with Session.builder.configs(connection_params).create() as session:
         # use the session to execute a query.
   ```

In the example above:

* The `get_login_token` function reads the file where Snowflake copied the OAuth token for the container to use.
* The `get_connection_params` function constructs a token by concatenating the OAuth token and the user token from the
  `Sf-Context-Current-User-Token` header. The function includes this token in a dictionary of parameters that the application uses to
  connect to Snowflake.

> **Note:**
>
> When a service uses caller’s rights, it can connect to Snowflake as multiple users. You are responsible for managing access to resources that aren’t managed by Snowflake.
>
> For example, in Streamlit apps, the `st.connection` object automatically caches the connection by using `st.cache_resource` in the global state, making it accessible across Streamlit sessions that are started by different users. When you use caller’s rights, consider using `st.session_state` to store connections on a per-session basis to avoid sharing connections between users.

For an example with step-by-step instructions, see [Create a service with caller’s rights enabled](tutorials/advanced/tutorial-7-callers-rights.md).

#### Accessing a service with caller’s rights configured

*Configuring caller’s rights* means that your service is establishing a Snowflake connection on behalf of the caller. How you log in to the
service’s ingress endpoints, either programmatically or by using a browser, remains the same. After log in, the following behaviors and options apply:

* **Accessing a public endpoint using a browser:** After you log into an endpoint, the service establishes a connection to Snowflake on behalf
  of the calling user using the default role of the user. If there is no default role configured for the user, the PUBLIC role is used.
* **Accessing a public endpoint programmatically:** When [logging into an endpoint programmatically](../../user-guide/oauth-custom.md) using JWT token, you can optionally set the `scope` parameter to specify the role to activate

Currently, after a service establishes a caller’s right connection to Snowflake on behalf of the caller, switching roles is not supported. If your application needs to use different roles to access different objects, you must change the user’s default secondary roles property.

* To set up the user to have all secondary roles active by default, use the [ALTER USER](../../sql-reference/sql/alter-user.md) command to set the [DEFAULT_SECONDARY_ROLES](../../sql-reference/sql/create-user.md) property of the user to (‘ALL’), as shown in the following example:

```sqlexample
ALTER USER my_user SET DEFAULT_SECONDARY_ROLES = ( 'ALL' );
```

#### Managing caller grants to a service

When a service creates a caller’s rights session, the session operates as the calling user, *not* as the service user. When an operation is performed by using this session, Snowflake applies a sequence of two permissions checks:

1. The first permissions check is performed as if the user created the session directly. This check is part of the normal permission checks that Snowflake performs
   for the user.
2. The second permissions check verifies that the service is allowed to perform the operation on behalf of a user. Snowflake verifies this by
   ensuring that the service’s owner role was granted the necessary caller grants.

In a caller’s rights session, both the normal permission check and the service owner role’s caller grants check must allow the
operation; this is referred to as [restricted caller’s rights](../restricted-callers-rights.md). By default the service has no permission to do anything on behalf of a user. You must explicitly grant caller grants to
the service so it can run with the caller’s privileges.

For example, suppose a user `U1` uses a role `R1` that has the SELECT privilege on the table `T1`. When `U1` logs into the public endpoint of your
service (`example_service`), which is configured to use the caller’s rights, the service then establishes a connection with Snowflake on
behalf of `U1`.

To allow the service to query table `T1` on behalf of `U1`, you need to grant the service’s owner role the following privileges:

* Privileges to resolve the table’s name, by granting a caller grant that allows the service to run with the USAGE privilege on the database and schema for that table.
* Privileges to use a warehouse to execute queries by granting a caller grant that allows the service to run with the USAGE privilege on a warehouse.
* Privileges to query the table by granting a caller grant that allows the service to run with the SELECT privilege on table `T1`.

The following example shows how to grant the service’s owner role with these privileges:

```sqlexample
-- Permissions to resolve the table's name.
GRANT CALLER USAGE ON DATABASE <db_name> TO ROLE <service_owner_role>;
GRANT CALLER USAGE ON SCHEMA <schema_name> TO ROLE <service_owner_role>;
-- Permissions to use a warehouse
GRANT CALLER USAGE ON WAREHOUSE <warehouse_name> TO ROLE <service_owner_role>;
-- Permissions to query the table.
GRANT CALLER SELECT ON TABLE T1 TO ROLE <service_owner_role>;
```

Any role in your account that has the global MANAGE CALLER GRANT privilege can grant caller grants. For more information about caller grants, see [GRANT CALLER](../../sql-reference/sql/grant-caller.md) and [Restricted caller’s rights](../restricted-callers-rights.md).

#### Example

For an example of a service that uses the caller’s rights feature when executing SQL queries on behalf of users, see [Create a service with caller’s rights enabled](tutorials/advanced/tutorial-7-callers-rights.md).

### Connect to Snowflake by using other credentials

You can use other forms of authentication to connect to Snowflake, not just the Snowflake-provided OAuth token. To do this, you create an external access integration (EAI) that enables your container to connect to Snowflake as if the container is running outside Snowflake and connecting through the internet. When you connect this way, you don’t need to configure the host that is used by the client.

> **Note:**
>
> Because these connections traverse an EAI, Snowflake authentication also enforces network policies. If your business requires network policies, connecting with other credentials isn’t supported.

For example, the following connection specifies the username and password to authenticate:

```python
conn = snowflake.connector.connect(
  account = '<acct-name>',
  user = '<user-name>',
  password = '<password>'
)
```

To use a default hostname, you need external access integration with a network rule that allows access from your service to the
Snowflake internet hostname for your account. For example, if your account name is `MYACCOUNT` in the organization `MYORG`, the hostname is
`myorg-myaccount.snowflakecomputing.com`. For more information, see [Configure service egress](service-network-communications.md). [Privatelink](../../user-guide/private-connectivity-inbound.md) hostnames are not supported

* Create a network rule that matches your account’s Snowflake API hostname:

  ```sqlexample
  CREATE OR REPLACE NETWORK RULE snowflake_egress_access
    MODE = EGRESS
    TYPE = HOST_PORT
    VALUE_LIST = ('myorg-myaccount.snowflakecomputing.com');
  ```

* Create an integration that uses the preceding network rule:

  ```sqlexample
  CREATE EXTERNAL ACCESS INTEGRATION snowflake_egress_access_integration
    ALLOWED_NETWORK_RULES = (snowflake_egress_access)
    ENABLED = TRUE;
  ```

## Configuration of the database and schema context for executing SQL

In addition to providing credentials, Snowflake also provides the database and schema context in which the service is created. The container code can use this information to execute SQL in the same database and schema context as the service.

This section explains two concepts:

* The logic Snowflake uses to determine the database and schema in which to create your service.
* The method through which Snowflake conveys this information to your containers, thus enabling the container code to execute
  SQL in the same database and schema context.

Snowflake uses the service name to determine the database and schema in which to create a service:

* Example 1: In the following CREATE SERVICE and EXECUTE JOB SERVICE commands, the service name does not explicitly specify a database and schema name. Snowflake creates the service and the job service in the current database and schema.

  ```sqlexample
  -- Create a service.
  CREATE SERVICE test_service IN COMPUTE POOL ...

  -- Execute a job service.
  EXECUTE JOB SERVICE
    IN COMPUTE POOL tutorial_compute_pool
    NAME = example_job_service ...
  ```

* Example 2: In the following CREATE SERVICE and EXECUTE JOB SERVICE commands, the service name includes a database and schema name. Snowflake creates the service and job service in the specified database (`test_db`) and schema (`test_schema`), regardless of the current schema.

  ```sqlexample
  -- Create a service.
  CREATE SERVICE test_db.test_schema.test_service IN COMPUTE POOL ...

  -- Execute a job service.
  EXECUTE JOB SERVICE
    IN COMPUTE POOL tutorial_compute_pool
    NAME = test_db.test_schema.example_job_service ...
  ```

When Snowflake starts a service, it provides the database and schema information to the running containers using the
following environment variables:

* SNOWFLAKE_DATABASE
* SNOWFLAKE_SCHEMA

Your container code can use environment variables in the connection code to determine which database and schema to use, as
shown in this example:

```python
conn = snowflake.connector.connect(
  host = os.getenv('SNOWFLAKE_HOST'),
  account = os.getenv('SNOWFLAKE_ACCOUNT'),
  token = get_login_token(),
  authenticator = 'oauth',
  database = os.getenv('SNOWFLAKE_DATABASE'),
  schema = os.getenv('SNOWFLAKE_SCHEMA')
)
```

**Example**

In [Tutorial 2](tutorials/tutorial-2.md), you create a Snowflake job service that connects with Snowflake and executes SQL statements.
The following steps summarize how the tutorial code uses the environment variables:

1. In the common setup (see the [Common Setup](tutorials/common-setup.md) section), you create resources, including a
   database and a schema. You also set the current database and schema for the session:

   ```sqlexample
   USE DATABASE tutorial_db;
   ...
   USE SCHEMA data_schema;
   ```

2. After you create a job service (by running EXECUTE JOB SERVICE), Snowflake starts the container and sets the following environment variables in
   the container to the current database and schema of the session:

   * SNOWFLAKE_DATABASE is set to “TUTORIAL_DB”
   * SNOWFLAKE_SCHEMA is set to “DATA_SCHEMA”
3. The job code (see `main.py` in Tutorial 2) reads these environment variables:

   ```python
   SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE')
   SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')
   ```

4. The job code sets the database and schema as the context in which to execute the SQL statements (`run_job()` function
   in `main.py`):

   ```sqljson
   {
      "account": SNOWFLAKE_ACCOUNT,
      "host": SNOWFLAKE_HOST,
      "authenticator": "oauth",
      "token": get_login_token(),
      "warehouse": SNOWFLAKE_WAREHOUSE,
      "database": SNOWFLAKE_DATABASE,
      "schema": SNOWFLAKE_SCHEMA
   }
   ...
   ```

   > **Note:**
   >
   > SNOWFLAKE_ACCOUNT, SNOWFLAKE_HOST, SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA are environment variables that Snowflake generates for the application container, but SNOWFLAKE_WAREHOUSE is not (the Tutorial 2 application code created this variable because Snowflake does not pass a warehouse name to a container).

## Specifying the warehouse for your container

If your service connects to Snowflake to execute a query in a Snowflake warehouse, you have the following options to specify a warehouse:

* **Specify a warehouse in your application code.** Specify a warehouse as part of the connection configuration when starting a Snowflake session to run queries in your code. For an example, see [Tutorial 2](tutorials/tutorial-2.md).
* **Specify a default warehouse when creating a service.** Specify the optional QUERY_WAREHOUSE
  parameter in the
  [CREATE SERVICE](../../sql-reference/sql/create-service.md) or [EXECUTE JOB SERVICE](../../sql-reference/sql/execute-job-service.md)
  command to provide a default warehouse. If your application code doesn’t provide a warehouse
  as part of connection configuration, Snowflake uses the default warehouse. Use the
  [ALTER SERVICE](../../sql-reference/sql/alter-service.md) command to change the default warehouse.

  > **Note:**
  >
  > The warehouse specified using the QUERY_WAREHOUSE parameter is the default only for the
  > service user.
  > When the service connects to Snowflake on behalf of another user — in the context of
  > caller’s rights scenario,
  > Snowflake uses the user’s default warehouse.

If you specify a warehouse by using both methods, the warehouse that is specified in the application code is used.

## Access service user query history

You can find queries executed by your service as the service user by filtering the [QUERY_HISTORY view](../../sql-reference/account-usage/query_history.md) or [QUERY_HISTORY](../../sql-reference/functions/query_history.md) function where `user_type` is SNOWFLAKE_SERVICE.

**Example 1:** Fetch queries run by a service.

```sqlexample
SELECT *
FROM snowflake.account_usage.query_history
WHERE user_type = 'SNOWFLAKE_SERVICE'
AND user_name = '<service_name>'
AND user_database_name = '<service_db_name>'
AND user_schema_name = '<service_schema_name>'
order by start_time;
```

In the WHERE clause:

* `user_name = '<service_name>'`: You specify the service name as the user name because a service executes queries as the service user, and the service user’s name is the same as the service name.
* `user_type = 'SNOWFLAKE_SERVICE'` and `user_name = '<service_name>'`: This limits the query result to retrieve only queries executed by a service.
* `user_database_name` and `user_schema_name`: For a service user, these are the service’s database and schema.

You can get the same results by calling the QUERY_HISTORY function.

```sqlexample
SELECT *
FROM TABLE(<service_db_name>.information_schema.query_history())
WHERE user_database_name = '<service_db_name>'
AND user_schema_name = '<service_schema_name>'
AND user_type = 'SNOWFLAKE_SERVICE'
AND user_name = '<service_name>'
order by start_time;
```

In the WHERE clause:

* `user_type = 'SNOWFLAKE_SERVICE'` and `user_name = '<service_name>'` limit the query result to retrieve only queries executed by a service.
* `user_database_name` and `user_schema_name` names (for a service user) are the service’s database and schema.

**Example 2:** Fetch queries run by services and the corresponding service information.

```sqlexample
SELECT query_history.*, services.*
FROM snowflake.account_usage.query_history
JOIN snowflake.account_usage.services
ON query_history.user_name = services.service_name
AND query_history.user_schema_id = services.service_schema_id
AND query_history.user_type = 'SNOWFLAKE_SERVICE'
```

The query joins the QUERY_HISTORY and SERVICES views to retrieve information about the queries and services that executed the queries. Note the following:

* For queries run by services, the `query_history.user_name` is the service user’s name, which is the same as the service name.
* The query joins the views using the schema IDs (not schema name) to ensure you refer to the same schema, because if you drop and recreate a schema, the schema ID changes but the name remains the same.

You can add optional filters to the query. For example:

* Filter `query_history` to retrieve only services that executed specific queries.
* Filter `services` to retrieve only queries executed by specific services.

**Example 3:** For every service, fetch service user information.

```sqlexample
SELECT services.*, users.*
FROM snowflake.account_usage.users
JOIN snowflake.account_usage.services
ON users.name = services.service_name
AND users.schema_id = services.service_schema_id
AND users.type = 'SNOWFLAKE_SERVICE'
```

The query join SERVICES and USERS views in the ACCOUNT_USAGE schema to retrieve services and service user information. Note the following:

* When a service runs queries, it runs the queries as service user and the service user’s name is the same as the service name. Therefore, you specify the join condition: `users.name = services.service_name`.
* Service names are unique only within a schema. Therefore, the query specifies the join condition (`users.schema_id = services.service_schema_id`) to ensure each service user is matched against the specific service they belong to (and not any other same-named service running in different schemas).
