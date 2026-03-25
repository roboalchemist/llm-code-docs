# Source: https://kreya.app/docs/named-pipes.md

# Windows Named Pipes Endpoints

Kreya supports Windows named pipes as endpoints, enabling communication with services that expose named pipe interfaces. This feature is particularly useful for interacting with local Windows services.

## How to Use Named Pipes in Kreya[​](#how-to-use-named-pipes-in-kreya "Direct link to How to Use Named Pipes in Kreya")

1. **Endpoint Format**:<br /><!-- -->Use the following format to specify a named pipe endpoint in Kreya:

   ```
   np://<pipe-name>
   ```

   Replace `<pipe-name>` with the actual name of the named pipe.

2. **Example: Interacting with a Named Pipe**:<br /><!-- -->To interact with a service exposing a named pipe, configure the endpoint as follows:

   ```
   np://./pipe/mypipe
   ```

   This assumes that the named pipe is called `./pipe/mypipe`.

3. **Accessing Named Pipes**:<br /><!-- -->Ensure that the named pipe is accessible by the user running Kreya. Some services may require elevated permissions to access their named pipes.

## Example Request[​](#example-request "Direct link to Example Request")

Here’s an example of how to configure a request to a service using a named pipe in Kreya:

1. Set the endpoint to:

   ```
   np://./pipe/mypipe
   ```

2. Configure the request details, such as the method and payload, according to the service's API.

3. Send the request, and Kreya will communicate with the service over the named pipe.

## Notes[​](#notes "Direct link to Notes")

* Named pipes are a Windows-specific feature and are not supported on other operating systems.
* Ensure that the service exposing the named pipe is running and accessible.
* If you encounter permission issues, consider running Kreya with elevated privileges.
* SSL / TLS is not supported for named pipes.

For more information on Windows named pipes and their usage, refer to the official documentation of the service you are interacting with.
