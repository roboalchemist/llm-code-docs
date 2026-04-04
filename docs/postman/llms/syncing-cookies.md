# Sync cookies using Postman Interceptor and the Postman proxy

Postman enables you to capture and sync cookies from a web browser or another client application to the [Postman cookie jar](/docs/sending-requests/response-data/cookies/). You can sync cookies using either the Postman proxy or Postman Interceptor at any time, without having to start a [proxy or Interceptor session](/docs/sending-requests/capturing-request-data/capture-overview/).

Once configured, Postman continuously captures cookies from the browser or client applications. For the domains you specify, captured cookies are automatically synced to the Postman cookie jar. You can then [use the cookies](/docs/sending-requests/response-data/cookies/) when sending requests from Postman.

You can also capture requests and cookies during a proxy or Interceptor session. Learn more about capturing requests and cookies with the [Postman proxy](/docs/sending-requests/capturing-request-data/capturing-http-requests/) or [Postman Interceptor](/docs/sending-requests/capturing-request-data/interceptor/).

## Sync cookies with Postman Interceptor

Postman Interceptor is a browser extension that captures network requests from a web browser and saves them to Postman. You can use Interceptor to continuously sync the cookies in your browser to the Postman cookie jar. This option works with either the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/) or the [Postman web app](/docs/getting-started/installation/installation-and-updates/#use-the-postman-web-app).

The Postman cookie jar always has the latest value for a given cookie. If you need to observe how cookie values change during a request flow, start an [Interceptor session](/docs/sending-requests/capturing-request-data/interceptor/).

To sync cookies using Postman Interceptor, do the following:

1. Install the Postman Interceptor extension by following the steps in [Install Interceptor](/docs/sending-requests/capturing-request-data/interceptor/#install-interceptor).
2. Click ![Image 1: Cookie icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-cookie-stroke-small.svg#icon) **Cookies** in the Postman footer.
3. In the **Cookies** window, click **Sync Cookies**. If you're using the Postman desktop app, click **Interceptor**.

    If you get the message "No connection to Interceptor", make sure your browser is open and the [Interceptor extension is installed](/docs/sending-requests/capturing-request-data/interceptor/#install-interceptor). If you're using the Postman desktop app, try closing any browser tabs where the Postman web app is open.

4. Enter one or more **Domains**. Postman will sync cookies for the specified domains to the Postman cookie jar.

    > Adding a domain automatically syncs cookies for its subdomains as well. For example, adding the domain `postman-echo.com` will also sync cookies from `docs.postman-echo.com`. To sync cookies for the domain only, you can add `https://` in front of the domain, such as `https://postman-echo.com`.

5. Click **Start Syncing**. Cookies for the domains you specified are automatically synced from your browser to Postman.

    * To stop syncing cookies for a domain, click ![Image 2: Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon) next to the domain name.
    * To stop capturing and syncing all cookies, click **Stop Syncing**.

    ![Image 3: Sync cookies with Interceptor](https://assets.postman.com/postman-docs/v11/cookies-interceptor-capture-v11.png)

## Sync cookies from the Interceptor extension

You can use the Postman Interceptor extension to sync cookies from your browser to the Postman cookie jar, without starting an Interceptor session. This option works with either the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/) or the [Postman web app](/docs/getting-started/installation/installation-and-updates/#use-the-postman-web-app).

To sync cookies from the Interceptor extension:

1. Install the Postman Interceptor extension by following the steps in [Install Interceptor](/docs/sending-requests/capturing-request-data/interceptor/#install-interceptor).
2. Open the Interceptor extension by clicking the Interceptor icon in your browser's toolbar.
3. Click ![Image 4: Cookie icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-cookie-stroke.svg#icon) **Sync Cookies**.

    Make sure the message **Ready to sync** appears at the bottom of the Interceptor window. If the message **Interceptor disconnected** appears, make sure either the Postman desktop app is running or the Postman web app is open in your browser.

4. Enter one or more **Domains**. Postman will sync cookies for the specified domains to the Postman cookie jar.

    > Adding a domain automatically syncs cookies for its subdomains as well. For example, adding the domain `postman-echo.com` will also sync cookies from `docs.postman-echo.com`. To sync cookies for the domain only, you can add `https://` in front of the domain, such as `https://postman-echo.com`.

5. Click **Sync Cookies**. Cookies for the domains you specified are automatically synced from your browser to Postman.

    * To stop syncing cookies for a domain, click ![Image 5: Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon) next to the domain name.
    * To stop capturing and syncing all cookies, click **Stop Syncing**.

    ![Image 6: Sync cookies with the Interceptor extension](https://assets.postman.com/postman-docs/v11/interceptor-sync-cookies-v11.png)

## Sync cookies with the Postman proxy

A proxy acts as an intermediary between a client application (like a mobile app) and a server (like an API). You can use Postman's built-in proxy to capture any cookies passing between a client and a server. The captured cookies are synced to the Postman cookie jar for later use. This option doesn't work with the [Postman web app](/docs/getting-started/installation/installation-and-updates/#use-the-postman-web-app), so make sure to use the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/).

The Postman cookie jar always has the latest value for a given cookie. If you need to observe how cookie values change during a request flow, start a [proxy session](/docs/sending-requests/capturing-request-data/capturing-http-requests/).

To sync cookies using the Postman proxy, do the following:

1. Open the Postman desktop app and click ![Image 7: Cookie icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-cookie-stroke-small.svg#icon) **Cookies** in the Postman footer.
2. In the **Cookies** window, click **Sync Cookies** and click **Proxy**.
3. Enter a **Port** number. The default value is `5559`. You will use this port number when configuring clients.

    > You can't change the port number while the proxy is enabled.

4. Turn on **Enable Postman as a proxy**.
5. Enter one or more **Domains**. Postman will sync cookies for the specified domains to the Postman cookie jar.

    > Adding a domain automatically syncs cookies for its subdomains as well. For example, adding the domain `postman-echo.com` will also sync cookies from `docs.postman-echo.com`. To sync cookies for the domain only, you can add `https://` in front of the domain, such as `https://postman-echo.com`.

6. Click **Start Syncing**.

    * To start syncing cookies, configure one or more clients to use the Postman proxy. Learn more about [configuring the proxy on a client device](/docs/sending-requests/capturing-request-data/capturing-http-requests/#step-3-configure-the-proxy-on-a-client-device).
    * To stop syncing cookies for a domain, click ![Image 8: Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon) next to the domain name.
    * To stop capturing and syncing all cookies, click **Stop Syncing**.

    ![Image 9: Capture cookies with the proxy](https://assets.postman.com/postman-docs/v11/cookies-proxy-capture-v11.png)