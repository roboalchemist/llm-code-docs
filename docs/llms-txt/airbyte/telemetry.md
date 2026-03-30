# Source: https://docs.airbyte.com/platform/operator-guides/telemetry.md

# Source: https://docs.airbyte.com/platform/2.0/operator-guides/telemetry.md

# Source: https://docs.airbyte.com/platform/1.8/operator-guides/telemetry.md

# Source: https://docs.airbyte.com/platform/1.7/operator-guides/telemetry.md

# Source: https://docs.airbyte.com/platform/1.6/operator-guides/telemetry.md

# Telemetry

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Airbyte collects telemetry data in the UI and the servers to help us understand users and their use-cases better to improve the product.

Also check our [privacy policy](https://airbyte.com/privacy-policy) for more details.

* Self Managed
* Cloud
* PyAirbyte

To disable telemetry for your instance, modify the `values.yaml` file and define the following environment variable:

```
TRACKING_STRATEGY=logging
```

When visiting the webapp or our homepage the first time, you'll be asked for your consent to telemetry collection depending on the legal requirements of your location.

To change this later go to **Settings** > **User Settings** > **Cookie Preferences** or **Cookie Preferences** in the footer of our [homepage](https://airbyte.com).

Server side telemetry collection can't be changed using Airbyte Cloud.

When running [PyAirbyte](https://docs.airbyte.com/pyairbyte) for the first time on a new machine, you'll be informed that anonymous usage data is collected, along with a link to this page for more information.

Anonymous usage tracking ("telemetry") helps us understand how PyAirbyte is being used, including which connectors are working well and which connectors are frequently failing. This helps us to prioritize product improvements which benefit users of PyAirbyte as well as Airbyte Cloud, OSS, and Enterprise.

We will *never* collect any information which could be considered PII (personally identifiable information) or sensitive data. We *do not* collect IP addresses, hostnames, or any other information that could be used to identify you or your organization.

You can opt-out of anonymous usage reporting by setting the environment variable `DO_NOT_TRACK` to any value.
