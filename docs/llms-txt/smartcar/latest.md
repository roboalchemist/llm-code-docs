# Source: https://smartcar.com/docs/changelog/latest.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Latest Releases

> Learn about Smartcar's latest product updates and improvements

[Subscribe to changelog updates](https://sta26.share.hsforms.com/2CCbdweFdSOeE5B58UvjVlw) and receive email notifications for new releases and updates.

<Update label="January 28th, 2026">
  ## Charging signal CONNECTOR replaced with CHARGING\_TYPE is now live

  The charging signal change [announced on January 12th](#upcoming-change-charging-signal-connector-to-charging_type) is now live. The `CONNECTOR` type has been replaced with `CHARGING_TYPE` in the following signals:

  * Charge.ChargeLimits
  * Charge.ChargeRecords
  * Charge.ChargeTimers

  These signals now return the charging current type (`AC` or `DC`) instead of a connector hardware type. If your integration parses any of these signals and still references the `CONNECTOR` type, update your code to use `CHARGING_TYPE` and parse the `chargingType` field.

  For full details on the change, see the [original announcement](#upcoming-change-charging-signal-connector-to-charging_type) below.
</Update>

<Update label="January 20th, 2026">
  ## Send Destination now available for Volkswagen

  You can now use the Smartcar API to send destinations to Volkswagen vehicles in the United States.

  With the Send Destination command, your application can route a destination directly to a driver's built-in navigation screen. This unlocks new workflows:

  * Fleet management: Route drivers to their next pickup, delivery, or service location
  * Car sharing and rentals: Send return location addresses when a rental period is ending
  * Repair and maintenance: Direct customers to your nearest service center when maintenance is needed
  * Charging networks: Guide EV drivers to available chargers when battery is low

  **Get started**: Request the `control_navigation` permission during the Smartcar Connect flow and call [Send Destination](/api-reference/send-destination-to-vehicle).
</Update>

<Update label="January 16th, 2026">
  ## Ruby SDK and Java SDK Updated to Support Version 3 of the Vehicles API

  The [Ruby SDK](https://github.com/smartcar/ruby-sdk) and [Java SDK](https://github.com/smartcar/java-sdk) have been updated to support [Version 3 of the Vehicles API](/api-reference/vehicles-api-intro).

  Both SDKs now include three new methods:

  * `get_vehicle` - Retrieve vehicle information
  * `get_signal` - Get a specific signal for a vehicle
  * `get_signals` - Get all available signals for a vehicle

  These new methods provide easier access to vehicle data through the latest API version, enabling developers to work with Smartcar's expanded signal catalog and improved data delivery capabilities.

  **Get started**: Update to the latest SDK version and explore the new methods in the [Ruby SDK](https://github.com/smartcar/ruby-sdk) and [Java SDK](https://github.com/smartcar/java-sdk) documentation.
</Update>

<Update label="January 14th, 2026">
  ## Volvo Cars Partner Integration now available!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/BeQEjJv4IeTUpsgG/images/changelog/volvo-partnership.png?fit=max&auto=format&n=BeQEjJv4IeTUpsgG&q=85&s=ea8cf4e82c39f8eb3772b51c7c8ca21d" alt="" data-og-width="2000" width="2000" data-og-height="1200" height="1200" data-path="images/changelog/volvo-partnership.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/BeQEjJv4IeTUpsgG/images/changelog/volvo-partnership.png?w=280&fit=max&auto=format&n=BeQEjJv4IeTUpsgG&q=85&s=3fcf8c4187d4e7a5fd3d79053c14c2d2 280w, https://mintcdn.com/smartcar-docs/BeQEjJv4IeTUpsgG/images/changelog/volvo-partnership.png?w=560&fit=max&auto=format&n=BeQEjJv4IeTUpsgG&q=85&s=7eee730bf5f97a57f03515b6dc914d66 560w, https://mintcdn.com/smartcar-docs/BeQEjJv4IeTUpsgG/images/changelog/volvo-partnership.png?w=840&fit=max&auto=format&n=BeQEjJv4IeTUpsgG&q=85&s=b972ceec2fd22858acfff13ee05e339d 840w, https://mintcdn.com/smartcar-docs/BeQEjJv4IeTUpsgG/images/changelog/volvo-partnership.png?w=1100&fit=max&auto=format&n=BeQEjJv4IeTUpsgG&q=85&s=44547ea92ff52bc017aab6b243675669 1100w, https://mintcdn.com/smartcar-docs/BeQEjJv4IeTUpsgG/images/changelog/volvo-partnership.png?w=1650&fit=max&auto=format&n=BeQEjJv4IeTUpsgG&q=85&s=fc444b2d6b215deec4db64df17faee40 1650w, https://mintcdn.com/smartcar-docs/BeQEjJv4IeTUpsgG/images/changelog/volvo-partnership.png?w=2500&fit=max&auto=format&n=BeQEjJv4IeTUpsgG&q=85&s=e0dc184772c8a5fb11798312c1eb1d66 2500w" />
  </Frame>

  Smartcar is excited to announce a partnership with Volvo Cars, providing access to vehicles across the United States and Europe.

  **What's new:**

  * Access charging, battery, location, and odometer data through Smartcar signals
  * Use the updated consent flow through Volvo's official portal

  Learn more in the [Volvo integration updates](/help/oem-integrations/volvo/whats-new).
</Update>

<Update label="January 12th, 2026">
  ## Upcoming change: Charging signal `CONNECTOR` to `CHARGING_TYPE`

  On January 28th, 2026, we're updating three charging-related signals. This is a breaking change that may require updates to your integration.

  **Affected signals:**

  * `Charge.ChargeLimits`
  * `Charge.ChargeRecords`
  * `Charge.ChargeTimers`

  **What's changing:**
  In all three signals, the `CONNECTOR` type is being replaced with `CHARGING_TYPE`. Instead of returning a connector hardware type (e.g., `J1772`), these signals will now return the charging current type (`AC` or `DC`).

  **Before (current format):**

  ```json  theme={null}
  {
    "type": "CONNECTOR",
    "condition": {
      "connectorType": "J1772"
    }
  }
  ```

  **After (new format):**

  ```json  theme={null}
  {
    "type": "CHARGING_TYPE",
    "condition": {
      "chargingType": "AC"
    }
  }
  ```

  Other types such as `GLOBAL` and `LOCATION` remain unchanged.

  **Why we're making this change:**
  OEMs report connector hardware types inconsistently--some return proprietary strings, others return nothing at all. In contrast, AC vs. DC charging type is more widely provided across manufacturers.

  This change gives you more consistent, actionable data. Rather than maintaining a mapping of connector type strings, you can rely on a simple AC or DC value to determine whether the vehicle is on Level 1/2 charging or DC fast charging.

  **What you need to do:**
  If your integration parses any of these signals and handles the `CONNECTOR` type, update your code to:

  * Expect `CHARGING_TYPE` instead of `CONNECTOR`
  * Parse `chargingType` (values: `AC` or `DC`) instead of `connectorType`

  **Timeline:**

  * Now -> January 27th, 2026: Current format remains in place
  * January 28th, 2026: New format goes live

  **Questions?**
  Reach out to your Smartcar account manager or [contact support](https://smartcar.com/contact).
</Update>

<Update label="December 15th, 2025">
  ## Mercedes-Benz Partner Integration Now Available in Europe!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=2f0a2839bdea0e7a22abb7bdf499d080" alt="" data-og-width="2000" width="2000" data-og-height="1200" height="1200" data-path="images/changelog/mercedes-benz-partnership.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=280&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=19863b313464c4fc620d30df12c4a9c9 280w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=560&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=8adc584c8118cc3862e4a70e0fdc7d91 560w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=840&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=18ca7624f3954d817a3cd7b51d51a15c 840w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=1100&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=9c4cace159b682759250eafbe4dda527 1100w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=1650&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=e87c7810fbb22b610592ce86c4a8709e 1650w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=2500&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=408823c8d10c25f95d4b0deedd48f7c3 2500w" />
  </Frame>

  We're excited to announce that Mercedes-Benz is now available on Smartcar! Connect Mercedes-Benz electric vehicles (BEV and PHEV) to access vehicle data and enable smart charging capabilities.

  **What's new:**

  * Mercedes-Benz BEV and PHEV vehicles can now connect through Smartcar
  * Enhanced connect flow with VIN verification for Mercedes vehicles
  * Support for key vehicle data signals including battery level, charge status, and location

  **Important notes:**

  * Currently, only Battery Electric Vehicles (BEV) and Plug-in Hybrid Electric Vehicles (PHEV) are supported with this integration.
  * Need support for other Mercedes vehicle types? [Contact us](https://smartcar.com/contact) to discuss your requirements.

  Check out the [Mercedes-Benz integration guide](/help/oem-integrations/mercedes/whats-new) for more details.
</Update>

<Update label="December 5th, 2025">
  ## Vehicle data in Dashboard Coming Soon!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/vehicle-data-dashboard.png?fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=3acd45cd6de7b63ecfbdc4fae8592e50" alt="" data-og-width="2892" width="2892" data-og-height="1912" height="1912" data-path="images/changelog/vehicle-data-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/vehicle-data-dashboard.png?w=280&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=4721f9823579d7fcfe0794f1db5cb992 280w, https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/vehicle-data-dashboard.png?w=560&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=e45a0e4a91772c8b459952c4f06c88b9 560w, https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/vehicle-data-dashboard.png?w=840&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=0cbc3270924d126450adbfea672963e1 840w, https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/vehicle-data-dashboard.png?w=1100&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=1a549de5674c535bf26a7fea9f7d6ff3 1100w, https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/vehicle-data-dashboard.png?w=1650&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=02d4ae539e1f569bc07d38ce66d6e6a2 1650w, https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/vehicle-data-dashboard.png?w=2500&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=1cbf8ecc3ebac04727d45a7438ab02a5 2500w" />
  </Frame>

  Vehicle data will be available in your Smartcar Dashboard. This feature is now rolling out to some customers and will be available to all customers over the next few weeks.

  If you are interested in this feature or have any questions, please reach out to your Smartcar account manager or contact our support team.
</Update>

<Update label="December 5th, 2025">
  ## Dashboard updates: API logs, timezone controls, and more!

  We've added more visibility into production usage in the Dashboard so you can monitor API requests and webhook delivery health in one place.

  **What's new:**

  * **API V3 call tracking**: See which API V3 endpoints are being called directly in the Dashboard to monitor migration progress
  * **Active vehicle counter**: Track how many vehicles are actively delivering webhooks successfully to spot delivery gaps faster
  * **Timezone customization**: Set your preferred timezone in the Dashboard so charts and tables align with your operations

  **Get started**: Check out these updates in the [Smartcar Dashboard](https://dashboard.smartcar.com/).
</Update>

<Update label="December 5th, 2025">
  ## BMW Charging API now live across Europe

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/smartcarxbmw.png?fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=e8ca42461ce3d3d54bb2449dbd45435b" alt="" data-og-width="2104" width="2104" data-og-height="1166" height="1166" data-path="images/changelog/smartcarxbmw.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/smartcarxbmw.png?w=280&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=c44c6ed488ca620b305f21106c49f2e9 280w, https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/smartcarxbmw.png?w=560&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=abffe64e385e5460f3c41104fd0135c6 560w, https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/smartcarxbmw.png?w=840&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=8ef36d9c517b6749f0c0f91f8fd2c3af 840w, https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/smartcarxbmw.png?w=1100&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=09683c1cc6b0f3db8c58f204590c5a38 1100w, https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/smartcarxbmw.png?w=1650&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=6d2d60d425fa423915ca2ad3e243e8b5 1650w, https://mintcdn.com/smartcar-docs/rT1IH8yV6VQUOKv9/images/changelog/smartcarxbmw.png?w=2500&fit=max&auto=format&n=rT1IH8yV6VQUOKv9&q=85&s=1ea7543fe353d8f175ddd84e1643877b 2500w" />
  </Frame>

  We've partnered with BMW to bring their new Charging API to Europe, giving energy providers privacy-first access to BMW EVs for smart charging, grid optimization, and home energy management.

  This integration is now available in select European markets. Reach out to your Smartcar team to enable BMW Charging for your app or learn more in the [partnership announcement](https://smartcar.com/blog/smartcar-and-bmw-partnership).
</Update>

<Update label="November 19th, 2025">
  ## Improved Webhook Logs in Dashboard

  We've significantly improved the webhook logging experience in the Smartcar Dashboard, making it easier to monitor and debug webhook deliveries.

  **What's New:**

  * **Delivery-focused logging**: Each log row now represents a single webhook delivery, providing a clearer view of your webhook activity
  * **Detailed inspection**: Click "View logs" on any delivery to inspect the signal or endpoint items included in that delivery and their individual statuses
  * **Faster performance**: Reduced latency in both Webhook Logs and the webhook deliveries over time chart for a more responsive experience

  **Where to Find It:**
  You can view your webhook logs in two locations:

  * **Logs > Webhooks** in the main navigation
  * **Vehicles > \[Selected vehicle] > Webhooks** for vehicle-specific logs

  **Get started**: Head to the [Smartcar Dashboard](https://dashboard.smartcar.com/logs?tab=webhooks) to explore the improved webhook logs.
</Update>

<Update label="November 18th, 2025">
  ## Python SDK and Node SDK Updated to Support Version 3 of the Vehicles API

  The [Python SDK](https://github.com/smartcar/python-sdk) and [Node SDK](https://github.com/smartcar/node-sdk) have been updated to support [Version 3 of the Vehicles API](/api-reference/vehicles-api-intro).

  Both SDKs now include three new methods:

  * `get_vehicle` - Retrieve vehicle information
  * `get_signal` - Get a specific signal for a vehicle
  * `get_signals` - Get all available signals for a vehicle

  These new methods provide easier access to vehicle data through the latest API version, enabling developers to work with Smartcar's expanded signal catalog and improved data delivery capabilities.

  **Get started**: Update to the latest SDK version and explore the new methods in the [Python SDK](https://github.com/smartcar/python-sdk) and [Node SDK](https://github.com/smartcar/node-sdk) documentation.
</Update>

<Update label="November 12th, 2025">
  ## Polestar and BYD are now available on Smartcar!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=e5ef2ea3f67b7dc0a692aa7fbf5c2be3" alt="" data-og-width="4000" width="4000" data-og-height="2400" height="2400" data-path="images/changelog/byd-polestar-hero.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=280&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=d5525d01ad95038c2704d81263df8570 280w, https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=560&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=dbe61497a58c32af80e52d4242a4c281 560w, https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=840&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=e8f5aa463531ed1decef7f3acc947a1f 840w, https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=1100&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=008cf97c1eb1a226a57f11774d800fde 1100w, https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=1650&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=3b333c105d53f52ec5640bb2b0896bf2 1650w, https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=2500&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=dc62215046c3ede7ecda74c217cbcdbf 2500w" />
  </Frame>

  We're excited to bring compatibility for Polestar and BYD, expanding the number of brands on the platform to 45!

  To enroll vehicles from these brands, make sure you have them enabled for your application in the [Dashboard](https://dashboard.smartcar.com/configuration?tab=oem-brands).

  Once enabled, you can direct vehicle owners to connect their Polestar and BYD vehicles through the Smartcar Connect flow.

  For a list of data points supported for these brands, see the [compatibility matrix](https://smartcar.com/product/compatible-vehicles).

  See important note about [BYD's login requirement](/help/brand-quirks#byd).
</Update>

<Update label="November 12th, 2025">
  ## Upcoming Change to Webhook Payload Structure

  Webhook `VEHICLE_STATE` payloads are being updated to include a `status` value for all signals. Previously, a `status` value was only passed for signals with errors.

  Example Payload:

  ```json  theme={null}
  {
    "code": "location-preciselocation",
    "name": "PreciseLocation",
    "group": "Location",
    "body": {
      "latitude": 37.386051,
      "longitude": -122.083855
    },
    "status": {
      "value": "SUCCESS"
    }
  },
  ```

  This change will go live on November 17, 2025, at 11:00AM Pacific Time. Please ensure your webhook receiver is prepared to handle deliveries in this format.
</Update>

<Update label="November 12th, 2025">
  ## Extended Expiration Times for Vehicle Refresh Tokens

  Starting November 12, 2025, Vehicle Refresh Tokens will expire 10 minutes after they are used to generate a new token set. This is an extension from the previous expiration time of 1 minute.

  For more information about access tokens, see [Refreshing Access Tokens](/api-reference/authorization/refreshing-access-token)
</Update>

<Update label="November 10th, 2025">
  ## Verifying webhooks just got a lot easier!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=9106c3a746b703281d6fc2ada9bd6249" alt="" data-og-width="1344" width="1344" data-og-height="1095" height="1095" data-path="images/changelog/webhook-challenge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=280&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=2af7016d356c723b2c5f2abf8f55e130 280w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=560&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c402b715adfe634727c3db3777518002 560w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=840&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=663b8794492a757bc94bb456642ba025 840w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=1100&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c94a590072ee00fe31f2381424ab4866 1100w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=1650&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c36a0f87b244b4a1915d30d9440724c0 1650w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=2500&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=f4870c0fed07dab78526f68c81bd989a 2500w" />
  </Frame>

  When you verify a webhook, you’ll see a guided modal with a sample challenge string, copy-ready SDK snippets (Python, Node, Java, Ruby), and inline instructions for hashing the `application_management_token` plus challenge.

  When your server responds with your webhook verification, you'll see the response that Smartcar received compared to the expected hash output.

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=12cd5091ce9d0c9f0355569227931374" alt="" data-og-width="1344" width="1344" data-og-height="1095" height="1095" data-path="images/changelog/webhook-challenge-calculator.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=280&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=01c41a08770277ac722cf56d2207755d 280w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=560&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=eb0f7b5c79d5f1d5001cf2b4e0c1fc94 560w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=840&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=e6a0dedfdd279d20479326bcd0f855e2 840w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=1100&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=a8fe313d141c595525270f50f960da76 1100w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=1650&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=b671a190797c06c85e5fea49b0dab359 1650w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=2500&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=bc0b603ce9b29e082e1c5372681297e3 2500w" />
  </Frame>

  If the verification fails, the new response tab surfaces the HTTP status, challenge string, expected hash output, and the payload Smartcar received so you can immediately compare and retry. This feedback loop removes trial-and-error, shortens onboarding for new teams, and ensures your webhook endpoint is producing the correct `SC-Signature` before you start ingesting production signals.

  **Get started**

  * Head to the [Smartcar Dashboard](https://dashboard.smartcar.com/integrations) and select your webhook integration to launch the verifier.
  * Follow the updated [Payload verification guide](/integrations/webhooks/payload-verification) to reproduce the same HMAC calculation server-side.
  * After verification succeeds, wire up your [webhook receiver tutorial](/getting-started/tutorials/webhook-receiver-recipe) or call the [webhook overview](/integrations/webhooks/overview) docs for deployment best practices.
</Update>

<Update label="November 5th, 2025">
  ## TypeScript Webhook Recipe Now Available

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=f79b6068e67c4abf926be8364ba2c927" alt="" data-og-width="1084" width="1084" data-og-height="478" height="478" data-path="images/changelog/webhook-recipe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=280&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=e7a2254c470e0b0c0ad02bb633e7a46a 280w, https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=560&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=f69339b3afb0046da2cfc90373c0c4dc 560w, https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=840&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=36992d7750724602a81a7ef810e01749 840w, https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=1100&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=e3bf0d348cd7ef1365f650918a3bb25a 1100w, https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=1650&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=68708cc3b32099325654da2d395d978a 1650w, https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=2500&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=2c572f846670d048baaf62d2b94d0eb2 2500w" />
  </Frame>

  Deploy production-ready webhook receivers in minutes with our new [TypeScript Webhook Recipe](https://github.com/smartcar/typescript-webhook-recipe)! This AWS serverless template provides everything you need to handle Smartcar webhooks at scale:

  * **Complete Infrastructure**: Lambda + API Gateway + SQS with AWS CDK
  * **Built-in Validation**: Automatic webhook verification and payload validation
  * **Error Handling**: Dead letter queues and retry logic for reliability
  * **Production Ready**: CloudWatch monitoring, IAM security, and auto-scaling
  * **Developer Friendly**: TypeScript types and comprehensive documentation

  The recipe eliminates the complexity of building webhook infrastructure from scratch, letting you focus on your business logic. Perfect for new webhook implementations or teams wanting to deploy quickly without infrastructure overhead.

  **Get started**: [Webhook Receiver Recipe Documentation](/getting-started/tutorials/webhook-receiver-recipe) | [GitHub Repository](https://github.com/smartcar/typescript-webhook-recipe)
</Update>

<Update label="September 18th, 2025">
  ## Battery Capacity Selection in the Smartcar Connect Flow

  <Frame style={{ width: '250px', align:'center' }}>
        <img src="https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=ae0a84b03f024606bfce72e9c1f4a66b" alt="" data-og-width="388" width="388" data-og-height="842" height="842" data-path="images/connect/battery-capacity-selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=280&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=0efc0d1d7b90e454505fe7243a4695a9 280w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=560&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=d8622e19ba50d06c2f9a03b44c426475 560w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=840&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=1628e58db5cbcb928930c083347fcbc5 840w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=1100&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=474b6ff769fd376096adcca85a67f05f 1100w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=1650&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=0940140efeb5fc2101b3119fd83bcb01 1650w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=2500&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=d246877f0146b9d4241e0280fb33be5d 2500w" />
  </Frame>

  When you request the `read_battery` permission and Smartcar detects multiple possible battery capacity matches for a vehicle, users will now be automatically prompted to select their battery capacity during the Connect flow.

  This streamlined experience eliminates the need for developers to prompt users or source the battery capacity selection from other sources. This step ensures that battery capacity data is available immediately after vehicle connection if Smartcar is not able to identify it.

  Read more about the [User Selected Battery Capacity](/connect/user-selected-batcap).
</Update>

<Update label="September 15th, 2025">
  ## Smartcar Partners with Mercedes-Benz Connectivity Services GmbH!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=2f0a2839bdea0e7a22abb7bdf499d080" alt="" data-og-width="2000" width="2000" data-og-height="1200" height="1200" data-path="images/changelog/mercedes-benz-partnership.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=280&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=19863b313464c4fc620d30df12c4a9c9 280w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=560&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=8adc584c8118cc3862e4a70e0fdc7d91 560w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=840&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=18ca7624f3954d817a3cd7b51d51a15c 840w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=1100&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=9c4cace159b682759250eafbe4dda527 1100w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=1650&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=e87c7810fbb22b610592ce86c4a8709e 1650w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=2500&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=408823c8d10c25f95d4b0deedd48f7c3 2500w" />
  </Frame>

  We are excited to announce our partnership with Mercedes-Benz Connectivity Services GmbH, expanding seamless access to connected vehicle data for developers and businesses across Europe.

  This integration enables developers to build innovative applications using data from Mercedes-Benz vehicles, including popular models such as the A-Class, C-Class, E-Class, S-Class, GLA, GLC, and more.

  With this partnership, Smartcar customers can leverage secure, reliable, and real-time access to vehicle data for a wide range of use cases, from fleet management to mobility services.

  Read more about this partnership and its impact in our [blog post](https://smartcar.com/blog/smartcar-partners-with-mercedes-benz-connectivity-services-gmbh).
</Update>

<Update label="August 26th, 2025">
  ## Introducing the new Smartcar Platform!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=22175cab894749206bdc7f3bbd118c56" alt="" data-og-width="2402" width="2402" data-og-height="1184" height="1184" data-path="images/changelog/data-delivery-announcement.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d6cc8471788593a5626764cc2881cbf4 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a39af0f2a272dafddd4207bce668ca2f 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=145259f351c51046c8409214ddca69bc 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=84cf82cc8964d47d7809359cf7a7c434 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=90a50fe89f0b8f119233a93dd88ce2e4 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=495ecd701a81e7bd883a2edf05fea531 2500w" />
  </Frame>

  We are excited to announce the launch of the new Smartcar Platform, designed to provide a more reliable and efficient way to access vehicle data. With our new [webhook integration](/integrations/webhooks/overview) and [API](/api-reference/intro), developers can now receive vehicle data at higher frequencies and with improved reliability.

  For all use cases, Smartcar can deliver data as it detects changes based on our new standardized Signal Schema while avoiding unnecessary polling. With over 80 signals available, developers can access a wide range of vehicle data to build innovative applications.

  Getting started with Smartcar is now even easier. [Configure](/getting-started/configure-application) your app, [Connect](/getting-started/connect-vehicles) vehicles, and start receiving data via [webhooks](/integrations/webhooks/overview) in just a few minutes.

  To get started with the new webhooks, check out our [Getting Started guide](/getting-started/introduction) and [Webhook integration overview](/integrations/webhooks/overview).

  These new features are now available to all new customers. Existing customers can reach out to their account manager or contact our support team at [support@smartcar.com](mailto:support@smartcar.com)
</Update>

<Update label="August 6th, 2025">
  ## Smartcar Partners with Ford in Europe!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0d8bdcb5a9506b6871a972831f8f2ea9" alt="" data-og-width="4000" width="4000" data-og-height="2400" height="2400" data-path="images/changelog/ford-partnership-hero.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c95f5ac2fc4be0ae6e976f9ff19b99d9 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=81b7a259276aaa1018ed43c3068ec7d6 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6fe1ba02a4edb13d5e6d45bfbe8376d6 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a34b4271c1cbcb43a00857abdd70e9f3 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=93cbb87a39be0a94283a776a836e0e7b 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b1c4cb8b89e99434d0b80b3474f414e9 2500w" />
  </Frame>

  Smartcar is thrilled to announce our partnership with Ford in Europe, enabling developers to access vehicle data from millions of Ford vehicles across the continent.

  This upcoming integration will give developers seamless access to vehicle data from models including the Mustang Mach‑E®, E‑Transit™, Puma, Fiesta, and Kuga.

  Read more about this exciting partnership in our [blog post](https://smartcar.com/blog/smartcar-partners-with-ford-to-expand-access-to-connected-vehicle-apis?utm_source=docs\&utm_medium=changelog).
</Update>

<Update label="July 9, 2025">
  ## Rivian Commands Now Available!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c07a5542bef44eada0f996aa37b5cd71" alt="" data-og-width="2000" width="2000" data-og-height="1200" height="1200" data-path="images/changelog/rivian-commands.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b7e1528a5bdecde87feec868ef567ffa 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e874ee657fe65071470b4f5682e9029c 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=332b861fac4a870fd621e4810189b2f6 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c931d52c272e3d09db38da14b72fd5d7 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=05381fedbebf1706cfe27e567cf2adef 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3145f275f64ee54ee870e0fff89b6013 2500w" />
  </Frame>

  You can now use the Smartcar API to send commands—such as lock, unlock, and start/stop charge—to Rivian vehicles!

  When requesting command permissions (like `control_security` or `control_charge`), Rivian owners will be prompted to pair their phone with their vehicle. After successful pairing, your application will be able to issue commands to the connected Rivian.

  For step-by-step instructions, see our [Rivian Bluetooth Pairing guide](/connect/other-actions/rivian-bluetooth-pairing).

  > **Note:** Read data permissions (such as `read_location` or `read_charge`) do not require Bluetooth pairing.
  >
  > Smartcar mobile SDKs for iOS and Android are required for Bluetooth pairing.
</Update>

<Update label="June 23, 2025">
  ## Hyundai Lock and Unlock now available!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=365b003efcb521065fb5e8c2bffcc405" alt="" data-og-width="2000" width="2000" data-og-height="1200" height="1200" data-path="images/changelog/hyundai-lock-unlock.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=ae688d6acdb297e0f9c8a62e621bbb19 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9811e1c70e06bbcb8cae0494702aa6cc 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=643ad4fdbf60a0baacc687701202343d 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b894dc8e9c8b243baf9edabafe3a2f41 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=28721498b08fdfc567d952f9b22931d5 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d908456253a214a14d8ba6ecc19db8ff 2500w" />
  </Frame>

  You can now lock and unlock Hyundai vehicles using the same standard Smartcar API. This new feature enables remote control of vehicle doors for supported Hyundai models, making it easier to build secure and convenient experiences for your users.

  For more details on how to use this capability, see our [API reference](/api-reference/control-lock-unlock).

  ## Webhook Logs Now Available in Dashboard

  You can now view logs for your webhooks directly in the Smartcar Dashboard, alongside your API request logs. This update gives you greater visibility into webhook deliveries, making it easier to monitor, debug, and ensure successful integrations.

  To see your webhook logs in action, head over to the [Smartcar Dashboard](https://dashboard.smartcar.com/logs?tab=webhooks).
</Update>

<Update label="June 10, 2025">
  ## New Dashboard Overview Page

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=fb8a6c0720322cad92144050d38a9e57" alt="" data-og-width="2000" width="2000" data-og-height="1200" height="1200" data-path="images/changelog/overview-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=cae166f5c4c019ddf09ff1d4b07f2f1f 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5f9be6c5690e6848193188ba11aaf116 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6e3057b0d701384a7c8f1a9f9a0acc34 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5758913ff218c5e75f5e4ddc8b6be3ce 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1573f58184b866977b041b4732319e60 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b73c2dbf3e821e13c28600522548b131 2500w" />
  </Frame>

  Our new Dashboard overview page offers a comprehensive snapshot of your application's performance at a glance. Now, you can quickly visualize:

  * Total vehicle connections
  * New connections in the last 7 days
  * Request trends over time
  * Conversion rates
  * Top five vehicle brands connected to your application

  This update is designed to help you monitor key metrics effortlessly.
</Update>

<Update label="May 20, 2025">
  ## Virtual Keys installation Is Now Supported in Connect

  Smartcar now provides detailed steps for adding and managing Virtual Keys during the connection flow. Virtual Keys are required for third-party applications to issue commands to Tesla vehicles and are the preferred method for accessing data.

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e504d181b6936f3e0ba17926a2923be2" alt="" data-og-width="2283" width="2283" data-og-height="931" height="931" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=02c5b864bdd1e8c5541ed1a1bfc80549 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a1ca3a12ee41154e396ae4ce1b56af65 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=89747ff417caaf5f36b30737aa24bd0a 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6f5036a32588937a17a0ea6fb0adc4bb 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=3e4e9358fb3e91fc7e6b1ad8bc7bac0d 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b8b9c2e23830523d41d1c9c753d3b309 2500w" />
  </Frame>

  For more details, visit the [Virtual Key documentation](/help/oem-integrations/tesla/virtual-key-tesla).
</Update>

<Update label="May 9, 2025">
  ## atHome signal is now available!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6fd0f9ec342e5836f7f424b0d84c1551" alt="" data-og-width="1193" width="1193" data-og-height="605" height="605" data-path="images/changelog/athome.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a011b2164337d474b5d280ae97ee291b 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c23ed8efcf27123587ab12e1ce5ac08d 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=142571bd4b338cac17e14765929a0cad 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e48de1bbc49d223ed4923582f72371f9 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9d615b05e54d84695fb7f52965ed2788 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=2b157e38c55ef34959bd080a5f7198df 2500w" />
  </Frame>

  Smartcar now supports a new vehicle signal `atHome` that returns true or false if a vehicle is at the configured home location. This signal is currently available for Tesla vehicles capable of streaming via [this endpoint](/api-reference/tesla/get-ext-vehicle-info).
</Update>

<Update label="April 21, 2025">
  ## Our New Support Features Are Live!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b47b4cecbce18a2f9c9b54f1ed1703e4" alt="" data-og-width="3348" width="3348" data-og-height="1746" height="1746" data-path="images/changelog/support_center.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=09434d78152cf5a4fb5fc8f0544f518a 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1030ad4e23f917c159899d6dcff3d8a4 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7b4cc7e8c048371f57c71d267ee22680 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=41df3dd4696763920e8780d3557801f7 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=80d4221ec447492ac02d377f6ee8bcd9 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0bc42dc428026b00fc53bdf7819ead91 2500w" />
  </Frame>

  We’re excited to share that our new support experience is now available. These updates are designed to make it easier and faster to get the help you need through self-service tools, AI-powered assistance, and improved visibility into your support history.

  **Customer Support Portal** *(Available to paid customers via the Smartcar Dashboard)*

  Your new central hub for all support-related needs:

  * Browse the **Knowledge Base** for helpful articles, guides, and troubleshooting tips
  * Submit new support requests through a user-friendly form
  * View and update **open tickets**, track past communications, and receive timely updates
  * Get help fast with our **AI-powered chat agent**, available 24/7

  **Enhanced Slack Support** *(For eligible plans)*

  Our upgraded Slack support includes:

  * AI-powered answers to common questions directly in your Slack channel
  * Ability to create and track support tickets without leaving Slack
  * One-click access to the Customer Support Portal
  * Real-time updates and faster response workflows

  For more information about what’s included in your current plan, please reach out to your account manager or contact us at [**support@smartcar.com**](mailto:support@smartcar.com).

  For step-by-step instructions on how to use the new features, check out our documentation [here](https://smartcar.com/docs/help/accessing-support-center).
</Update>

<Update label="March 26, 2025">
  ## Support for Single Sign-on (SSO)

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=048c472c915140a7f30819b3867f2dc0" alt="" data-og-width="1400" width="1400" data-og-height="1060" height="1060" data-path="images/changelog/sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=22c8c3065dfae30246b8b7ce849685a9 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b4526a7300ae12b574a813b20ebd1d26 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=2b91d146ccb5bbe18bb7cfc31bd43e92 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=639e3dfd1732e648b1345fd0dbb186be 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c042b2ae5b902f1af67c3f7cff74d767 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=af0ff4a69b4c60aae59f1d010c7375df 2500w" />
  </Frame>

  Single Sign-On (SSO) is now available for teams on an Enterprise plan. To get
  started, reach out to your account manager to have it enabled. For
  implementation details and setup instructions, check out our [SSO
  documentation](/getting-started/dashboard/single-sign-on).
</Update>

<Update label="February 26, 2025">
  ## User Selected Battery Capacity

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c961d991a12ec7159956c2c019c2c3d3" alt="" data-og-width="1557" width="1557" data-og-height="844" height="844" data-path="images/changelog/battery-capacity-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e5adb5112b52ea9e44dfec0560a553c0 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=39d36e8ce845e2160e7b4c53f2fc3a8d 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=98e1670947a946171f6317d42ef64395 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e18cbf7b80707eaaadfc77ae045e96ee 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=abd113f48a42da549583afb78a8cb640 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=548482aa480e985154dbcaef33171082 2500w" />
  </Frame>

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8c3bb7b334461e7cb0c51541b5f65f14" alt="" data-og-width="1568" width="1568" data-og-height="1209" height="1209" data-path="images/changelog/battery-capacity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7c334ae84b82eab6a73957919d7f7d54 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8b97a7c6bed8fd28ba4ef169345bac29 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5499cebd357e498dc3ffa1275cddf8d9 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b95903505b20ef79d8b58326e7e992af 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8081dbd7c77135f86f12bb622b0c2da1 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=20983c624dcb77f3a2d5d00e8ba06402 2500w" />
  </Frame>

  Developers can now redirect vehicle owners to a Smartcar Connect url where they can select the [battery capacity](/api-reference/get-nominal-capacity) of their vehicle for cases where the battery capacity cannot be accurately determined. This can occur when vehicle owners purchase extension packs, or software upgrades specific to their vehicle. When a user selects an option, Smartcar will return this value with `USER_SELECTED` as the source.
</Update>

<Update label="February 14, 2025">
  ## Diagnostics Webhooks, DTSs, and System Status

  Smartcar now provides Diagnostic Webhooks, DTCs, and System Status vehicle data for an [initial set of brands](https://smartcar.com/product/compatible-vehicles) with more brands added in the future.
</Update>

<Update label="February 6, 2025">
  ## Support for Simplified Chinese

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c8d7225d911a5d6582055f33660021b6" alt="" data-og-width="1050" width="1050" data-og-height="1620" height="1620" data-path="images/changelog/simplified-chinese.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a8db316e1b5b4548710116205c6c2daf 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=4cc6ed25b42c4120b3ec8177e4472961 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=2c16cd2f676e87737aa84219847e30d1 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=91621b392e156878162b725ffe2db228 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a86833cdbd8f53bd6ff079031fe57c1b 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5da4895e6c83a1b561563ecd9b68ae9c 2500w" />
  </Frame>

  Vehicle owners can now select Simplified Chinese as they go through the Smartcar Connect flow to connect their cars.
</Update>

<Update label="January 30, 2025">
  ## Tesla Telemetry API

  Smartcar natively supports Tesla's Telemetry API as the default mechanism for retrieving data from Tesla vehicles out of the box and without any configuration from developers. Tesla's Telemetry API is the most efficient and effective way of gathering data from Tesla vehicles. It allows vehicles to stream data directly to Smartcar, eliminating the need to poll Tesla servers. This prevents unnecessary vehicle wakes and battery drain.
</Update>

<Update label="January 10, 2025">
  ## Smartcar MFA

  When a vehicle owner attempts to login to their OEM Connected Services Account and they do not have MFA enabled, Smartcar customers can enable this feature to enforce MFA verification for extra security. If you don't see this option in the Smartcar dashboard, contact [support@smartcar.com](mailto:support@smartcar.com) to get access to this feature.
</Update>

<Update label="January 6, 2025">
  ## New Billing page in Dashboard

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a397ed2408731b110969d82626753f8e" alt="" data-og-width="2844" width="2844" data-og-height="2734" height="2734" data-path="images/changelog/billing-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a28d49467d764e61a30ee3b55d829ca8 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=4aa6539c0d3a00e7e24e854122c6f97d 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=fcae21a3d6f8f2b15152ea98081ed751 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=017dcc3fc88a12b09724d1ca36d4ace5 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=53a863969b8390b2072e5df30d4e922b 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=df3f822c49f8021f089f19bd48a78ade 2500w" />
  </Frame>

  This new page provides more visibility and the ability to update your billing information, view past invoices, and view your plan features and available upgrade options.
</Update>
