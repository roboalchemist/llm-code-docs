# Source: https://docs.buildnatively.com/natively-platform/features/service-worker.md

# Service Worker

Service Worker Support allows your app to cache specific resources and data locally on the user's device. Enabling this feature significantly improves your app's loading speed and enables offline capabilities.

### Prerequisites

Before enabling this in Natively, you must configure a Service Worker on your web application.

* Natively provides the *environment* for the Service Worker to run inside the mobile app, but the caching logic and the `service-worker.js` file must be implemented and active on your website first.
* We recommend the official [MDN Web Docs: Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) or [Google's Workbox Guide](https://developer.chrome.com/docs/workbox/) for best practices.

### How to setup in Natively

* Open your App Dashboard: Navigate to the Features page on the Natively dashboard.
* Enable the Feature: Locate the Service Worker feature, open its settings and toggle the switch to Enable.
* Add Trusted Hosts: You need to specify which domains (hosts) the Service Worker is allowed to cache.
  * Enter the domain names where your app loads resources from (e.g., `example.com`, `cdn.example.com`).
  * Limit: You can add a maximum of 10 hosts.
* Save & Rebuild: Click Save, then create a new build.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FFw15PGXfGaXggvtTmzJb%2Fservice_worker_docs.png?alt=media&#x26;token=d2bde5f5-1888-45f7-8496-91f81f15170b" alt=""><figcaption></figcaption></figure>

### Important: Network Checks & Offline Mode

Enabling Service Worker changes how your app handles internet connectivity. Please review the settings below to ensure your users have a smooth experience.

1\. **Default Network Check is Disabled** When you enable Service Worker, is automatically disabled.

* You must implement a Fallback UI on your website to handle cases where there is no network connection and no cached data available.

2\. **Offline Mode Configuration** If you plan to use the Service Worker to let users access the app while Offline:

* You must disable the [Continuous Network Check](https://docs.buildnatively.com/natively-platform/appearance/network-screen) feature in your Error screen settings.
* If Continuous Network Check is left enabled, Natively will display the Error screen as soon as the device goes offline, which will block your users from seeing the cached content you prepared.
