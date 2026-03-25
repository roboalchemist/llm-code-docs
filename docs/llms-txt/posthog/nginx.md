# Source: https://posthog.com/docs/advanced/proxy/nginx.md

# nginx reverse proxy - Docs

**Before you start**

-   If you use a self-hosted proxy, PostHog can't help troubleshoot. Use [our managed reverse proxy](/docs/advanced/proxy/managed-reverse-proxy.md) if you want support.
-   Use domains matching your PostHog region: `us.i.posthog.com` for US, `eu.i.posthog.com` for EU.
-   Don't use obvious path names like `/analytics`, `/tracking`, `/telemetry`, or `/posthog`. Blockers will catch them. Use something unique to your app instead.

This guide shows you how to use [nginx](https://nginx.org/en/docs/) as a reverse proxy for PostHog.

## How it works

nginx acts as an intermediary between your users and PostHog. When a user triggers an event, the request goes to your nginx server first, which forwards it to PostHog's servers and returns the response.

Here's the request flow:

1.  User triggers an event in your app
2.  Request goes to your nginx server (e.g., `e.yourdomain.com`)
3.  nginx forwards the request to PostHog with the correct headers
4.  PostHog processes the request and returns a response
5.  nginx returns PostHog's response to the user

This works because ad blockers see requests going to your domain, not PostHog's. The proxy is transparent to the browser.

**Why two location blocks?** PostHog uses separate domains for API requests and static assets. Your nginx config needs two location blocks:

-   **`/static/`:** Routes to `us-assets.i.posthog.com` or `eu-assets.i.posthog.com` for the JavaScript SDK and other static files
-   **`/`:** Routes everything else to `us.i.posthog.com` or `eu.i.posthog.com` for event capture, feature flags, and API calls

## Prerequisites

-   A server with root or sudo access
-   A domain with DNS pointing to your server
-   Ports 80 and 443 open for HTTP/HTTPS traffic

## Choose your setup option

Both options accomplish the same goal. Choose based on your infrastructure:

-   [**Direct installation:**](#option-1-direct-installation) Install nginx on your server and configure it manually. Use this for dedicated servers or VMs.
-   [**Docker:**](#option-2-docker) Run nginx in a container with environment variables for region configuration. Use this for containerized infrastructure or local testing.

## Option 1: Direct installation

1.  1

    ## Install nginx

    Follow [nginx's installation guide](https://nginx.org/en/docs/install.html) for your operating system.

    On Ubuntu/Debian:

    Terminal

    PostHog AI

    ```bash
    sudo apt update && sudo apt install nginx
    ```

2.  2

    ## Configure nginx

    Create a new configuration file at `/etc/nginx/sites-available/posthog-proxy`:

    nginx

    PostHog AI

    ```nginx
    server {
        listen 80;
        listen [::]:80;
        server_name e.yourdomain.com;
        location /static/ {
            proxy_pass https://us-assets.i.posthog.com/static/;
            proxy_set_header Host us-assets.i.posthog.com;
            proxy_ssl_server_name on;
            proxy_ssl_name us-assets.i.posthog.com;
        }
        location / {
            proxy_pass https://us.i.posthog.com/;
            proxy_set_header Host us.i.posthog.com;
            proxy_ssl_server_name on;
            proxy_ssl_name us.i.posthog.com;
        }
    }
    ```

    Replace `e.yourdomain.com` with your subdomain. Replace `us` with `eu` for EU region.

    Here's what each directive does:

    -   `proxy_pass`: The upstream URL nginx forwards requests to. The trailing slash is important—it tells nginx to replace the matched location path.
    -   `proxy_set_header Host`: Sets the Host header sent to PostHog. Without this, PostHog receives your domain and can't route the request, causing 401 errors.
    -   `proxy_ssl_server_name on`: Enables Server Name Indication (SNI) for the upstream SSL connection. Required because PostHog uses virtual hosting.
    -   `proxy_ssl_name`: The hostname to use for SNI. Must match the upstream domain.

    Enable the site by creating a symlink:

    Terminal

    PostHog AI

    ```bash
    sudo ln -s /etc/nginx/sites-available/posthog-proxy /etc/nginx/sites-enabled/
    ```

    See [nginx proxy documentation](https://nginx.org/en/docs/http/ngx_http_proxy_module.html) for more configuration options.

3.  3

    ## Test and reload nginx

    Test your configuration for syntax errors:

    Terminal

    PostHog AI

    ```bash
    sudo nginx -t
    ```

    If the test passes, reload nginx to apply the configuration:

    Terminal

    PostHog AI

    ```bash
    sudo nginx -s reload
    ```

4.  4

    ## Add SSL/TLS

    Recommended

    Use [Certbot](https://certbot.eff.org/) to add free SSL certificates from Let's Encrypt:

    Terminal

    PostHog AI

    ```bash
    sudo apt install certbot python3-certbot-nginx
    sudo certbot --nginx -d e.yourdomain.com
    ```

    Certbot automatically updates your nginx configuration to redirect HTTP to HTTPS and manages certificate renewal.

5.  5

    ## Update your PostHog SDK

    In your application code, update your PostHog initialization to use your proxy subdomain:

    PostHog AI

    ### US

    ```javascript
    posthog.init('<ph_project_token>', {
      api_host: 'https://e.yourdomain.com',
      ui_host: 'https://us.posthog.com'
    })
    ```

    ### EU

    ```javascript
    posthog.init('<ph_project_token>', {
      api_host: 'https://e.yourdomain.com',
      ui_host: 'https://eu.posthog.com'
    })
    ```

    Replace `e.yourdomain.com` with your actual subdomain.

6.  ## Verify your setup

    Checkpoint

    Confirm events are flowing through your proxy:

    1.  Test the proxy directly with curl:

        Terminal

        PostHog AI

        ```bash
        curl -I https://e.yourdomain.com/flags?v=2
        ```

        You should see a `200 OK` response.

    2.  Open your browser's developer tools and go to the **Network** tab

    3.  Trigger an event in your app

    4.  Look for requests to your subdomain (e.g., `e.yourdomain.com`)

    5.  Verify the response status is `200 OK`

    6.  Check the [PostHog app](https://app.posthog.com) to confirm events appear

    If you see errors, check [troubleshooting](#troubleshooting) below.

## Option 2: Docker

This option runs nginx in a container with environment variables for the PostHog region.

1.  1

    ## Create a Dockerfile

    Create a `Dockerfile`:

    dockerfile

    PostHog AI

    ```dockerfile
    FROM nginx:alpine
    COPY nginx.conf /etc/nginx/nginx.conf.template
    CMD ["sh", "-c", "envsubst '\\$POSTHOG_CLOUD_REGION' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'"]
    ```

    The `envsubst` command replaces the `${POSTHOG_CLOUD_REGION}` variable in your config with the actual value at runtime. This lets you use the same image for both US and EU regions.

2.  2

    ## Create the nginx config

    Create a file named `nginx.conf`:

    nginx

    PostHog AI

    ```nginx
    worker_processes auto;
    events { worker_connections 1024; }
    http {
        sendfile on;
        server {
            listen 8080;
            server_name _;
            resolver 8.8.8.8 8.8.4.4 valid=300s;
            resolver_timeout 5s;
            location /static/ {
                proxy_pass https://${POSTHOG_CLOUD_REGION}-assets.i.posthog.com/static/;
                proxy_set_header Host "${POSTHOG_CLOUD_REGION}-assets.i.posthog.com";
                proxy_ssl_server_name on;
                proxy_hide_header 'Access-Control-Allow-Origin';
                add_header 'Access-Control-Allow-Origin' '*' always;
            }
            location / {
                proxy_pass https://${POSTHOG_CLOUD_REGION}.i.posthog.com;
                proxy_set_header Host "${POSTHOG_CLOUD_REGION}.i.posthog.com";
                proxy_ssl_server_name on;
                proxy_hide_header 'Access-Control-Allow-Origin';
                add_header 'Access-Control-Allow-Origin' '*' always;
            }
        }
    }
    ```

    The `resolver` directive configures DNS resolution for the upstream domains. This is required in containers because nginx resolves hostnames at startup, and container DNS may not be available immediately.

3.  3

    ## Build and run the container

    Build the Docker image:

    Terminal

    PostHog AI

    ```bash
    docker build -t posthog-nginx .
    ```

    Run the container:

    Terminal

    PostHog AI

    ```bash
    docker run --rm -p 8080:8080 -e POSTHOG_CLOUD_REGION=us posthog-nginx
    ```

    Replace `us` with `eu` for EU region.

4.  4

    ## Update your PostHog SDK

    In your application code, update your PostHog initialization:

    PostHog AI

    ### US

    ```javascript
    posthog.init('<ph_project_token>', {
      api_host: 'http://localhost:8080',
      ui_host: 'https://us.posthog.com'
    })
    ```

    ### EU

    ```javascript
    posthog.init('<ph_project_token>', {
      api_host: 'http://localhost:8080',
      ui_host: 'https://eu.posthog.com'
    })
    ```

    Replace `localhost:8080` with your actual host and port in production.

5.  ## Verify your setup

    Checkpoint

    Confirm events are flowing through your proxy:

    1.  Test the proxy directly:

        Terminal

        PostHog AI

        ```bash
        curl -I http://localhost:8080/flags?v=2
        ```

    2.  Open your browser's developer tools and go to the **Network** tab

    3.  Trigger an event in your app

    4.  Look for requests to your proxy host

    5.  Verify the response status is `200 OK`

    6.  Check the [PostHog app](https://app.posthog.com) to confirm events appear

    If you see errors, check [troubleshooting](#troubleshooting) below.

## Troubleshooting

### 502 Bad Gateway errors

If nginx returns `502 Bad Gateway`, it can't reach PostHog's servers:

1.  Verify your server can make HTTPS requests to PostHog domains:

    Terminal

    PostHog AI

    ```bash
    curl -I https://us.i.posthog.com/flags?v=2
    ```

2.  Check that `proxy_ssl_server_name on` is set in your config
3.  For Docker, ensure the `resolver` directive is configured

### SSL/TLS handshake errors

If you see SSL errors in nginx logs:

1.  Verify `proxy_ssl_name` matches the upstream domain exactly
2.  Check that your server's CA certificates are up to date
3.  For Docker, the alpine image may need CA certificates installed: `apk add ca-certificates`

### CORS errors

If you see `Access-Control-Allow-Origin` errors in the browser:

1.  Add CORS headers to your nginx config:

    nginx

    PostHog AI

    ```nginx
    proxy_hide_header 'Access-Control-Allow-Origin';
    add_header 'Access-Control-Allow-Origin' '*' always;
    ```

2.  The `proxy_hide_header` removes PostHog's CORS header so you can set your own

### Configuration file locations

Common nginx config locations by platform:

-   **Ubuntu/Debian:** `/etc/nginx/sites-available/` with symlinks in `/etc/nginx/sites-enabled/`
-   **CentOS/RHEL:** `/etc/nginx/conf.d/`
-   **macOS (Homebrew):** `/usr/local/etc/nginx/`

Run `nginx -t` to test your config and see which files nginx is loading.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better