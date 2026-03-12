# Source: https://docs.snowflake.com/en/developer-guide/node-js/nodejs-driver-connect.md

# Managing connections

To execute statements against Snowflake, you first need to establish a connection. The Snowflake Node.js Driver lets you
establish connections as follows:

* Create a single connection
* Create a pool of connections
* Connect through a proxy
* Connect through an authenticated proxy

> **Important:**
>
> Beginning with Snowflake version 8.24, network administrators have the option to require multi-factor authentication (MFA) for all connections to Snowflake. If your administrator decides to enable this feature, you must configure your client or driver to use MFA when connecting to Snowflake. For more information, see the following resources:
>
> * [8.24 release notes](../../release-notes/2024/8_24.md)
> * [Multi-factor authentication (MFA)](../../user-guide/security-mfa.md)
> * [Troubleshooting service users authentication issues with Snowflake MFA](https://community.snowflake.com/s/article/Troubleshooting-service-users-authentication-issues-with-Snowflake-MFA) Knowledge Base article

## Creating a single connection

To create a single connection to Snowflake:

1. Call `snowflake.createConnection` to create a new `Connection` object, and pass in a JavaScript object that
   specifies the [connection options](nodejs-driver-options.md).
2. Using the `Connection` object, call the `connect` method to establish a connection.

   > **Note:**
   >
   > If you set the `authenticator` option to `EXTERNALBROWSER` (in order to use
   > [browser-based SSO](nodejs-driver-authenticate.md)) or `https://<okta_account_name>.okta.com`
   > (in order to use [native SSO through Okta](nodejs-driver-authenticate.md)), call the `connectAsync` method, rather than
   > the `connect` method.

   To handle connection errors, pass in a callback function that has the following signature:

   ```javascript
   function(err, conn)
   ```

   where:

   * `err` is a JavaScript `Error` object.
   * `conn` is the current `Connection` object.

   If an error occurs during connection, the `connect` method passes an `Error` object to your callback function.
   You can use this object in your callback function to get details about the error. If you need information about the current
   `Connection` object, you can use the `conn` argument passed to your callback function.

The following example establishes a connection and uses a password for authentication. To use other authentication methods, see
[Authentication options](nodejs-driver-options.md).

> ```javascript
> // Load the Snowflake Node.js driver.
> var snowflake = require('snowflake-sdk');
> ```
>
> ```javascript
> // Create a Connection object that we can use later to connect.
> var connection = snowflake.createConnection({
>     account: account,
>     username: user,
>     password: password,
>     application: application
>   });
> ```
>
> ```javascript
> // Try to connect to Snowflake, and check whether the connection was successful.
> connection.connect(
>     function(err, conn) {
>         if (err) {
>             console.error('Unable to connect: ' + err.message);
>             }
>         else {
>             console.log('Successfully connected to Snowflake.');
>             // Optional: store the connection ID.
>             connection_ID = conn.getId();
>             }
>     }
> );
> ```

When creating a connection, you can set the connection options as described
in [Options Reference](nodejs-driver-options.md).

## Verifying that a connection is ready to receive queries

Before submitting Snowflake queries, you can use the `connection.isValidAsync()` method (in version 1.6.23 and later)
to ensure the connection is up
and ready to execute requests on Snowflake. The method returns `true` if the connection is ready or `false` otherwise.

```javascript
// Create a Connection object and connect to Snowflake
// ..

// Verify if connection is still valid for sending queries over it
const isConnectionValid = await connection.isValidAsync();

// Do further actions based on the value (true or false) of isConnectionValid
```

## Creating a connection pool

Instead of creating a connection each time your client application needs to access Snowflake, you can define a
cache of Snowflake connections to reuse as needed. Connection pooling usually reduces the lag time to
make a connection. However, it can slow down client failover to an alternative DNS when a DNS problem occurs.

To create a connection pool:

1. Call `snowflake.createPool(connectionOptions, poolOptions)` to create a new `ConnectionPool` object, and
   pass in two JavaScript objects that specify the [connection options](nodejs-driver-options.md)
   and pool options.

   > **Note:**
   >
   > The Snowflake Node.js Driver uses the open-source [node-pool](https://github.com/coopernurse/node-pool) library for implementing connection pools. For information about
   > the supported `poolOptions`, see the description of the `opts` argument in the
   > [node-pool library documentation](https://github.com/coopernurse/node-pool/blob/master/README.md).
2. With the `ConnectionPool` object, call the `use` function to execute statements for a single connection
   in the connection pool.

   To handle connection errors, pass in a callback function that has the following signature:

   ```javascript
   function(err, stmt, rows)
   ```

   where:

   * `err` is a JavaScript `Error` object.
   * `stmt` is an object with information about the SQL statement that was executed, including the literal
     text of the statement.
   * `rows` is an array containing the “result set” of the statement.

   If an error occurs while executing the statement, the `connect` method passes an `Error` object to your callback function.
   You can use this object in your callback function to get details about the error.

The following example creates a connection pool that supports a maximum of ten active connections. It uses a password
for authentication. To use other authentication methods, see [Authentication options](nodejs-driver-options.md).

> ```javascript
> // Create the connection pool instance
> const connectionPool = snowflake.createPool(
>     // connection options
>     {
>       account: account,
>       username: user,
>       password: password
>     },
>     // pool options
>     {
>       max: 10, // specifies the maximum number of connections in the pool
>       min: 0   // specifies the minimum number of connections in the pool
>     }
> );
> ```

The following example uses the `connectionPool.use` method to execute a SQL statement using the connections in the pool.
The `clientConnection.execute` method specifies the SQL statement to execute and defines a callback function.

> ```javascript
> // Use the connection pool and execute a statement
> connectionPool.use(async (clientConnection) =>
> {
>     const statement = await clientConnection.execute({
>         sqlText: 'select 1;',
>         complete: function (err, stmt, rows)
>         {
>             var stream = stmt.streamRows();
>             stream.on('data', function (row)
>             {
>                 console.log(row);
>             });
>             stream.on('end', function (row)
>             {
>                 console.log('All rows consumed');
>             });
>         }
>     });
> });
> ```

When creating a connection pool, you can set the connection options as described
in [Options Reference](nodejs-driver-options.md).

### Handling idle connections

With the default setting of the node-pool’s `evictionRunIntervalMillis` option set to 0, idle connection eviction checks are not run. If you have a longer running application, this behavior can lead to terminated connections lingering around in the connection pool, which when the driver acquires them and tries to send a query over them to Snowflake, causes an error.

To address this behavior in a long-running application, you could consider the following ways to handle it:

* Create the Snowflake `ConnectionPool` with an enabled evictor.

  You can add the `evictionRunIntervalMillis` option to the pool options, as shown in the following example:

  ```javascript
  const pool = snowflake.createPool(
      {
        account: account,
        username: username,

        //rest of the connection options

      },
      {
        evictionRunIntervalMillis: 60000 // default = 0, off
        idleTimeoutMillis: 60000, // default = 30000
        max: 2,
        min: 0,
      },
  );
  ```

  This example runs the evictor every minute and evicts any connections that are idle for more than one minute. You can also tweak `numTestsPerEvictionRun` (default: 3) to change the number of resources checked during each eviction run.

  See the node-pool library [documentation](https://github.com/coopernurse/node-pool/blob/master/README.md) for details and more options.
* Keep existing connections alive in the pool

  If you need to keep a connection alive more frequently than every hour, you can add the following to the pool options:

  * `clientSessionKeepAlive: true`
  * `clientSessionKeepAliveHeartbeatFrequency: n`, where `n` is between 900 (15m) and 3600 (1h) seconds (default: 3600).

  The following example sends a keep-alive heartbeat every 15 minutes to keep the connection alive even if no other activity, such as a query from a client, occurs.

  ```javascript
  const pool = snowflake.createPool(
      {
        account: account,
        username: username,

        // rest of the connection options

        clientSessionKeepAlive: true,  // default = false
        clientSessionKeepAliveHeartbeatFrequency: 900 // default = 3600
      },
      {
        max: 2,
        min: 0,
      },
  );
  ```

  You can also use the `clientSessionKeepAlive` option without using pooled connections.

  For more information about the session keep-alive, see [Node.js options reference](nodejs-driver-options.md).

## Connecting through a proxy

You can connect to Snowflake through a proxy, by supplying the details as connection options when creating a `Connection` object.

The following example shows how to connect to a proxy using HTTP:

```javascript
var connection = snowflake.createConnection({
      account: "account",
      username: "user",
      password: "password",
      proxyHost: "localhost",
      proxyPort: 3128,
});
```

Beginning with version 1.15.0, the Snowflake Node.js driver fully supports the `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` environment variables in addition to their corresponding connection parameters.

By default, the new `useEnvProxy` global configuration setting is set to `true`, which enables support for the environment variables.

With the ability to set these proxies both in the `Connection` object and in the environment variables, the driver uses the following hierarchy to determine which values to use:

* If a proxy is defined in the `Connection`, it takes precedence. The driver ignores the `HTTP_PROXY` and `HTTPS_PROXY` environment variables.
* If the Connection does not set the proxy values, the driver uses the values in the `HTTP_PROXY` and `HTTPS_PROXY` environment variables if they are defined.
* If the `useEnvProxy` connection setting is set to `false`, the driver ignores `HTTP_PROXY` and `HTTPS_PROXY` environment variables if they are defined.

If you want to disable support for proxy environment variables, you must disable it in the global configuration, as follows:

```javascript
const snowflake=require('snowflake-sdk');
snowflake.configure({ useEnvProxy: false });
```

> **Note:**
>
> The environmental variables are case-sensitive on Linux and MacOS. On Windows, they are not.
>
> * If both the lower-case (`https_proxy`) and upper-case (`HTTPS_PROXY`) variants are defined for the same environment variable, the driver uses the value from the lower-case (`https_proxy`) variable.
> * If only the upper-case (`HTTPS_PROXY`) variant is present, the driver use the upper-case variable’s value.

## Connecting through an authenticated proxy

You can connect to Snowflake through an authenticated proxy by supplying authentication credentials as connection
options when creating a `Connection` object.

> **Note:**
>
> Connecting through an authenticated proxy server is supported starting with version 1.6.4 of the Snowflake Node.js Driver.

The following example shows how to connect to an authenticated proxy using HTTP:

```javascript
var connection = snowflake.createConnection({
      account: "account",
      username: "user",
      password: "password",
      proxyHost: "localhost",
      proxyPort: 3128,
      proxyUser: "myname",
      proxyPassword: "mypass"
});
```

To connect to an authenticated proxy using HTTPS you must also provide the `proxyProtocol` connection property as shown below:

```javascript
var connection = snowflake.createConnection({
      account: "account",
      username: "user",
      password: "password",
      proxyHost: "localhost",
      proxyPort: 3128,
      proxyUser: "myname",
      proxyPassword: "mypass",
      proxyProtocol: "https"
});
```

## Verifying the network connection to Snowflake with SnowCD

After configuring your driver, you can evaluate and troubleshoot your network connectivity to Snowflake using [SnowCD](../../user-guide/snowcd.md).

You can use SnowCD during the initial configuration process and on-demand at any time to evaluate and troubleshoot your network connection to Snowflake.

## OCSP (online certificate status protocol)

When the driver connects, Snowflake sends a certificate to confirm that the connection is to Snowflake rather than to
a host that is impersonating Snowflake. The driver sends that certificate to an OCSP (Online Certificate Status
Protocol) server to verify that the certificate has not been revoked.

If the driver cannot reach the OCSP server to verify the certificate, the driver can
[“fail open” or “fail closed”](../../user-guide/ocsp.md).

## Terminating a connection

A connection can be terminated by calling the `connection.destroy()` method. This immediately ends the session associated with the connection without waiting for running statements to complete:

> ```javascript
> connection.destroy(function(err, conn) {
>   if (err) {
>     console.error('Unable to disconnect: ' + err.message);
>   } else {
>     console.log('Disconnected connection with id: ' + connection.getId());
>   }
> });
> ```
