# Source: https://smartcar.com/docs/connect/advanced-config/country-flag.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Country Selection

> By default Connect will launch based on the devices location impacting the brands that are available to the user e.g. Renault is only available in Europe.

You can override this behavior by passing a country feature flag in your Connect URL in the form `country:{country_code}`.

Your feature flag should contain the [two-character ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
of the country that your user is located in.

<Tip>
  Our SDKs provide ways for you to add this as part of the various `authUrlBuilder` or `getAuthUrl` methods.
</Tip>

```plaintext Connect URL w/ country feature flag theme={null}
https://connect.smartcar.com/oauth/authorize?
response_type=code
&client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07
&scope=read_odometer read_vehicle_info
&redirect_uri=https://example.com/home
&flags=country:GB
```

Alternatively, your users can manually change their country and language on Connect's preamble screen:

<Frame caption="Country selector dropdown on the Preamble screen in Connect" type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6ec90575ab9a84181c4be3ef06a66bfc" data-og-width="786" width="786" data-og-height="1132" height="1132" data-path="images/connect/countrySelector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f225235b0f894d8b89f5546bbfea87b3 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=04a23419bd9c409983c2c5d68095c954 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dad237a120e8b3206c84447fd709280b 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ef748d2898f29a73762bf2183b351306 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=76f51cd9c73acae174b740211ddfd99e 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a6846d3072186cd52a0b2a22c104a678 2500w" />
</Frame>
