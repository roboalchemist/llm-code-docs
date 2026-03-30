# Source: https://docs.trackjs.com/browser-agent/integrations/axios/

Title: Integrating with Axios

URL Source: https://docs.trackjs.com/browser-agent/integrations/axios/

Markdown Content:
Axios is a popular HTTP client library that works in both browser and Node.js environments. By default, Axios only exposes generic “Network Error” messages when requests fail, hiding valuable debugging information within its error objects. This integration extracts that detailed information and sends it to TrackJS for better error tracking.

**Why this integration?** Without this integration, all Axios network failures appear as generic “Network Error” messages in TrackJS, making debugging difficult. This integration captures the HTTP method, URL, and optionally request details for faster troubleshooting.

[Install TrackJS](https://docs.trackjs.com/browser-agent/integrations/axios/#install-trackjs "Permalink Here")
--------------------------------------------------------------------------------------------------------------

First, ensure TrackJS is installed and configured in your application. If you haven’t already, follow the [standard installation guide](https://docs.trackjs.com/browser-agent/integrations/installation) for your framework.

window.TrackJS && TrackJS.install({ token: "YOUR_TOKEN", /* Other settings, like application identifier: application: "YOUR_APP_ID" */});
[Configure Axios Interceptor](https://docs.trackjs.com/browser-agent/integrations/axios/#configure-axios-interceptor "Permalink Here")
--------------------------------------------------------------------------------------------------------------------------------------

Add a response interceptor to Axios that captures network errors and sends detailed information to TrackJS. This interceptor extracts the HTTP method and URL from failed requests, creating more descriptive error messages.

### [Basic Integration](https://docs.trackjs.com/browser-agent/integrations/axios/#basic-integration "Permalink Here")

// Add response interceptor to capture network errors axios.interceptors.response.use( // Pass through successful responses unchanged (response) => response, // Handle errors and send details to TrackJS (error) => { // Capture a formatted error with method and URL if (error.config && error.config.method && error.config.url) { TrackJS.track(`Network Error ${error.config.method.toUpperCase()}: ${error.config.url}`); } else { // Fallback for errors without config TrackJS.track(error); } // Re-throw the error so other error handlers can process it return Promise.reject(error); });

[Basic Axios interceptor](https://docs.trackjs.com/browser-agent/integrations/axios/#code-basic-axios-interceptor)

[Advanced Configuration (Optional)](https://docs.trackjs.com/browser-agent/integrations/axios/#advanced-configuration-optional "Permalink Here")
------------------------------------------------------------------------------------------------------------------------------------------------

For more detailed debugging, you can optionally capture request headers and body data. Use this approach carefully as it may log sensitive information.

**Security Warning:** Request headers and body data may contain sensitive information like authentication tokens or personal data. Only enable this in development or ensure you’re filtering out sensitive fields.

### [Integration with Request Details](https://docs.trackjs.com/browser-agent/integrations/axios/#integration-with-request-details "Permalink Here")

axios.interceptors.response.use( (response) => response, (error) => { // Optional: Log request headers (be careful with sensitive data!) if (error.config && error.config.headers) { TrackJS.console.info({ "request": { headers: error.config.headers, body: error.config.data } }); } // Optional: Log response details if available (be careful with sensitive data!) if (error.response) { TrackJS.console.info({ "response": { headers: error.response.headers, body: error.response.data } }); } // Capture formatted error with method and URL if (error.config && error.config.method && error.config.url) { TrackJS.track(`Network Error ${error.config.method.toUpperCase()}: ${error.config.url}`); } else { TrackJS.track(error); } return Promise.reject(error); });

[Advanced Axios interceptor with request details](https://docs.trackjs.com/browser-agent/integrations/axios/#code-advanced-axios-interceptor-with-request-details)

[Example Error Output](https://docs.trackjs.com/browser-agent/integrations/axios/#example-error-output "Permalink Here")
------------------------------------------------------------------------------------------------------------------------

With this integration, your TrackJS dashboard will show detailed network errors instead of generic messages:

**Before Integration:**

*   `Network Error`
*   `Network Error`
*   `Network Error`

**After Integration:**

*   `Network Error GET: https://api.example.com/users/123`
*   `Network Error POST: https://api.example.com/login`
*   `Network Error DELETE: https://api.example.com/posts/456`

This makes it much easier to identify and debug failing API calls in your application.
