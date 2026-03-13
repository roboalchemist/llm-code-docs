# Source: https://ngrok.com/docs/using-ngrok-with/nginx.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with NGINX

> Learn how to use ngrok with NGINX by setting the host header flag to properly route requests to your virtual hosts.

It's a good idea to get a background on how [NGINX processes a request](https://nginx.org/en/docs/http/request_processing.html). What that usually means is you need to ensure the `--host-header` flag is set when creating an endpoint for your service.


Built with [Mintlify](https://mintlify.com).