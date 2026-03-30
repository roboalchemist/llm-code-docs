# Source: https://kreya.app/docs/unix-sockets.md

# Unix Sockets Endpoints

Kreya supports Unix sockets as endpoints, allowing you to communicate with services that expose Unix socket interfaces. This feature is particularly useful for interacting with local services like Docker.

## How to Use Unix Sockets in Kreya[​](#how-to-use-unix-sockets-in-kreya "Direct link to How to Use Unix Sockets in Kreya")

* **Endpoint Format**:<br /><!-- -->Use the following format to specify a Unix socket endpoint in Kreya:

  ```
  unix://<absolute-or-project-relative-path>
  ```

  Replace `<absolute-or-project-relative-path>` with the actual path to the Unix socket file.

* **Relative Paths**:<br /><!-- -->Kreya also supports relative paths from the Kreya project root. For example:

  ```
  unix://../../relative/path/to/socket
  ```

## Example Request[​](#example-request "Direct link to Example Request")

Here’s an example of how to configure a request to the Docker API using Kreya:

1. Set the endpoint to:

   ```
   unix:///var/run/docker.sock
   ```

2. Configure the HTTP method and path. For example, to list Docker containers:

   * **Method**: `GET`
   * **Path**: `/containers/json`

3. Send the request, and Kreya will communicate with the Docker API over the Unix socket.

## Notes[​](#notes "Direct link to Notes")

* Ensure that the Unix socket file is accessible by the user running Kreya.
* Some services may require elevated permissions to access their Unix sockets. In such cases, you may need to run Kreya with appropriate privileges.
* SSL / TLS is not supported for Unix sockets.

For more information on Unix sockets and their usage, refer to the official documentation of the service you are interacting with.
