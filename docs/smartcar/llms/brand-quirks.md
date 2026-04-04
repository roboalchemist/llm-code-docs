# Source: https://smartcar.com/docs/help/brand-quirks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Brand Quirks

> Brand specific quirks to keep in mind while building out your application.

## Acura

### Ignition On

Depending on model year, certain Acura vehicles do not return data when the ignition/engine is on.

### Sleep State

Most Acuras will go into a sleep state after about a week of inactivity,

## Audi

### Primary Key User

In order to have access to all vehicle functionality the account that connects to Smartcar will need to be flagged as a Key User by Audi.

## BMW/MINI

### CONNECTED\_SERVICES\_ACCOUNT - SUBSCRIPTION errors

Smartcar API will throw a CONNECTED\_SERVICES\_ACCOUNT - SUBSCRIPTION when the data we receive from the vehicle is older than a month as this normally indicates a subscription issue.

## BYD

### Concurrent login requirement

BYD accounts can only maintain one active session at a time. Vehicle owners should sign in with a dedicated BYD login for Smartcar that is separate from the credentials used in the BYD mobile app. If the same account signs into the OEM app after connecting through Smartcar, the Smartcar session will be revoked and require re-authentication.

If customers reach out about being logged out of their BYD mobile app, we recommend instructing users to create a secondary BYD account exclusively for your app.

## GM (Buick, Chevrolet, Cadillac, GMC)

### VEHICLE\_STATE - ASLEEP errors

After 3-4 days of no activity, GM vehicles will enter a deep sleep state at which point they will no longer respond to API requests to preserve their 12v battery. In order to get data from the vehicle again, the car will need to go through an ignition cycle.

### UPSTREAM - RATE\_LIMIT errors

In order to avoid hitting UPSTREAM - RATE\_LIMIT errors use batch requests and ping no more than once every 30 minutes. Use of the OEM app also counts towards the rate limit.

## Hyundai/Kia

### Telemetry Update Behavior

#### Pre-2025 Models (Gen 2 Navigation)

Hyundai/Kia vehicles have event-based logic that sends telemetry updates based on state changes such as:

* Every 10% of SoC while charging
* 5 minutes after ignition off
* Vehicle doors are left unlocked for 5 minutes
* After a command successfully completes
* Whenever charging stops

#### 2025+ Models (Gen 3 / CCnC Navigation)

Newer Hyundai/Kia models update more frequently, as often as every five minutes, including while the vehicle is driving.

## Nissan

### “Vehicle has been found” MyNISSAN notifications

Vehicle owners may receive a notification from the MyNISSAN app stating “Success! We found the location of your vehicle. Check the map for the location of your YYYY Model.” every time the location endpoint is hit.

The app appears to have an option to edit notifications, but as of Feb 2024 they are not available in the app. Notifications may need to be turned off at the iOS/Android level by the vehicle owner.

## PSA Group (Citroen, DS, Opel, Peugeot, Vauxhall)

### Requesting control\_charge permissions

If you request control\_charge permissions for PSA EVs, upon login owners will be presented with a PIN and MFA screen in Connect upon submitting their credentials. They will need to have set this up on their OEMs application in order to grant your application this permission.

## Polestar

### Stop charge command limitations

Smartcar cannot fulfill stop charge commands if the vehicle is below 40% state of charge due to limitations with the current Polestar APIs.

## Rivian

### MFA

If MFA is enabled the vehicle owner will need to re-authorize via Connect about every 2 weeks.

## Tesla

### Remote Access

It may take a few hours or up to a full day for the REMOTE\_ACCESS\_DISABLED errors to subside after remote access is enabled.

### Charge Billing Records

In order to retrieve charge billing records, the main Tesla account must connect the vehicle, as driver profiles do not have access to this data.

### Virtual Key

Tesla now requires virtual keys for 3rd-party applications in order to issue commands for the following models:

* All Cybertrucks, Model 3 and Model Y
* 2021+ Model S and X

Please see [Virtual Keys](/help/oem-integrations/tesla/virtual-key-tesla) for more information.

### Enterprise Tenant Configuration

<Warning>
  For enterprise customers, Tesla tenant setup must occur **before** any customer-facing Tesla vehicles are onboarded. Configure this during initial implementation, coordinated with Smartcar.
</Warning>

Changing Tesla tenant configurations after vehicles are already connected will require all affected users to re-authenticate. See [OEM Migrations and Re-authentication](/connect/re-auth/oem-migrations) for guidance on handling this scenario.

## Volkswagen

### Control charge limits

Volkswagen limits charge commands to safeguard battery longevity based on environmental and system conditions. Excessive consecutive requests may result in being temporarily rate limited. To restore functionality, the vehicle must be driven again.

### CONNECTED\_SERVICES\_ACCOUNT errors on lock/unlock commands

In addition to verifying the VW account with the activation code, some cars will need to undergo the VW Ident Process before you can access remote lock/unlock functionality. This involves contacting the dealership to verify your ownership of the vehicle.

### Missing Subscription (European VWs)

Upon purchasing (or activating the free trial), VW needs to review the request. You will get an email confirmation once they've cleared everything on their side.

### Primary Driver Status

In order to fully interact with Smartcar, the credentials need to be flagged as the primary driver. You'll need to tap the "become primary driver" flow in the VW app. Depending on the model, this may require you to be in the car to interact with the infotainment system.

A vehicle owner can verify whether or not they are the primary driver by following the steps below:

1. Open the VW mobile app tap the profile icon in the bottom right
2. Go to **Vehicle Management**
3. If there’s an **Additional Users** section, tap their name to see whether it says **Primary User** or **Additional User**

## Volvo

### Lock/unlock commands

Volvo is an outlier regarding how unlock requests are processed. After initiating the request, after about 10 seconds you'll need to open the trunk (boot) to successfully complete the request. You'll know the car is ready to unlock the trunk as the hazard lights will flash. We recommend adding a notification for Volvos as part of the request loading animation to inform the user of this process.

### Phone number username

Smartcar Connect currently checks for an email format, as such phone number usernames cannot be used. The owner will need to add their email to their Volvo account via the web portal.

### Compatibility

Some models are not compatible because the device needs to be physically in the vehicle during authentication, which Connect doesn’t support at the moment:

* 2021+: XC40 Recharge
* 2022+: S90, S90 Recharge, V90, V90 Recharge, V90 Cross Country, XC60, XC60 Recharge, C40 Recharge
* 2023+: All models with the exception of the XC40

Even if the vehicle has been connected to and shows up in the Volvo app, if they go through Connect the account will present as if there are no vehicles on the account.
