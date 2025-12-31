# Source: https://smartcar.com/docs/api-reference/compatibility-api-intro.md

# Compatibility API Overview

> The Compatibility API helps you determine if a specific vehicle is supported by Smartcar before launching the Connect flow. This allows you to provide a seamless user experience by verifying eligibility up front.

## What You Can Do

* Check if a vehicle is compatible by VIN
* Query supported makes and regions

## Authentication

The Compatibility API uses a bearer token, which you can obtain from your Smartcar Dashboard or via the OAuth2 flow.

## Base URL

```
https://api.smartcar.com/compatibility/v2.0
```

## Key Resources

* [Check Compatibility by VIN](/api-reference/compatibility/by-vin)
* [Check Compatibility by Region and Make](/api-reference/compatibility/by-region-and-make)

## Example Use Cases

* Pre-qualifying users before showing Smartcar Connect
* Displaying supported makes and models in your app
* Reducing user friction by avoiding unsupported vehicles

<Info>
  For more details on using the Compatibility API, see [Compatibility API Reference](/api-reference/compatibility/by-vin).
</Info>
