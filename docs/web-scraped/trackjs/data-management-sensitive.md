# Source: https://docs.trackjs.com/data-management/sensitive/

Title: Sensitive Data

URL Source: https://docs.trackjs.com/data-management/sensitive/

Markdown Content:
Many applications handle sensitive data such as health records, payment cards, or personal data. You can use TrackJS on these data-sensitive applications by applying the appropriate security controls to you account and installation.

TrackJS does not have the security controls necessary to store sensitive data. We’re an error-reporting tool, not a payment processor after all. Our focus is giving you the controls to keep your data private and secure within your own application, and out of your logs.

[Sanitizing Telemetry](https://docs.trackjs.com/data-management/sensitive/#sanitizing-telemetry "Permalink Here")
-----------------------------------------------------------------------------------------------------------------

By default, the TrackJS agent records metadata about user and network actions, rather than the details of the actions themselves, to prevent sensitive data from ending up in your logs. When a user interacts with an input control, we record how many characters where entered, but not the characters themselves.

**User inputs are never recorded by the TrackJS agent.**

Likewise for network actions, the agent records the HTTP method, URL, and response code of the request, but not the headers or payload of either the request or the response body.

**Network request payloads are never recorded by the TrackJS agent.**

The TrackJS agent also records messages sent to the console. Sensitive data should not be logged to the console, regardless of TrackJS as a general security best-practice. However, if you are concerned that sensitive data might be leaked through the console, [you can disable console recording](https://docs.trackjs.com/browser-agent/tips-and-tricks/hide-console/). With console recording disabled, you can still send TrackJS Telemetry explicitly by calling [`TrackJS.console.log`](https://docs.trackjs.com/browser-agent/sdk-reference/agent-methods/#consolelog)

If you have more advanced needs, or want to examine what is being sent to TrackJS directly, you can provide an [onError](https://docs.trackjs.com/browser-agent/sdk-reference/agent-config/#onerror) callback to us, which allows you to modify error payloads before being reported.

For example, consider an application that deals with United States Social Security Numbers, which follow the format `000-00-0000`. If you are concerned that one such number might be included in your console, but you do not want to disable the console entirely because it is a valuable debugging resource, you could sanitize them using a custom onError function like the following.

[Excluding IP Addresses](https://docs.trackjs.com/data-management/sensitive/#excluding-ip-addresses "Permalink Here")
---------------------------------------------------------------------------------------------------------------------

When recording an error, TrackJS will store the `IP Address` of the remote client as part of the error report. This helps correlate errors from noisy clients and provide the ability to do rough geolocation. If your organization considers the IP Address of the client to be sensitive data, you can configure your TrackJS to truncate the last octet or exclude it entirely in your [Account Settings Page](https://my.trackjs.com/Account/Organization).

**TIP** You must be an [Owner](https://docs.trackjs.com/user-accounts/permissions/) of the account to change this setting.

[Purging Your Data](https://docs.trackjs.com/data-management/sensitive/#purging-your-data "Permalink Here")
-----------------------------------------------------------------------------------------------------------

If sensitive data has inadvertently entered your account, you can purge your account error data from the [Account Settings Page](https://my.trackjs.com/Account/Organization). This will irrecoverably delete all of the error data across all applications in your account.

**TIP** You must be an [Owner](https://docs.trackjs.com/user-accounts/permissions/) of the account to purge error data.

TrackJS complies with the EU GDPR as a Data Processor. There is a specific clause in our [Terms of Service](https://trackjs.com/terms) calling out the added requirements and a reference to our [Data Processing Agreement](https://trackjs.com/dpa).

If you have any questions or concerns about how we process data, please [contact us](https://docs.trackjs.com/support/).
