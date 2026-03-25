# Source: https://ngrok.com/docs/using-ngrok-with/gRPC.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with gRPC

> Learn how to use ngrok with gRPC services by specifying the HTTP/2 app protocol or using TCP endpoints.

Since gRPC uses HTTP/2, you may need to specify the `app-protocol` when forwarding a gRPC endpoint:

`ngrok http --app-protocol=http2 80`

This works with other ngrok features like custom domains and ports.

This [Stack Overflow user](https://stackoverflow.com/a/59555606/7282727) also reports that forwarding to gRPC services works using `proto: tcp`.


Built with [Mintlify](https://mintlify.com).