# Source: https://smartcar.com/docs/errors/connect-errors/vehicle-incompatible.md

# Vehicle Incompatible

> This error occurs when a user tries to authorize an incompatible vehicle in Smartcar Connect.

| Parameter           | Required | Description                           |
| ------------------- | -------- | ------------------------------------- |
| `error`             | `true`   | `vehicle_incompatible`                |
| `error_description` | `true`   | The user’s vehicle is not compatible. |
| `make`              | `false`  | The manufacturer of the vehicle.      |
| `vin`               | `false`  | The VIN of the vehicle.               |

In order to be compatible, a vehicle must:

* Have the hardware required for internet connectivity
* Belong to the makes and models Smartcar is compatible with
* Be capable of the required permissions that your application is requesting access to
* If the user’s vehicle is incompatible, Smartcar will let the user know and offer them to share their vehicle’s VIN, make, model, and year with your application.

This error is triggered when a user selects an unspported make, or selects "I don't see my brand..." and then hits "Back to application"

<Frame caption="Vehicle Incompatible">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0490adb032508a9965758ab02c26cd29" data-og-width="2643" width="2643" data-og-height="1472" height="1472" data-path="images/errors/connect-errors/vehicle-incompatible.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4d6f086ca74d32d88ccd37991392679c 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0ce9294c9716e4f64008d1c22305b363 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e082e76f4139fbbe58199d68373f3a4d 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8bdde4128b6703822e6614c214ccd8e1 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=97adb5491804bc5589800448937d8491 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c90da19a6ad6ceebe5bdad7963ff051c 2500w" />
</Frame>

We recommend that your application provides a flow for incompatible vehicles like in the example below.

<Frame caption="Vehicle Incompatible">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=004f2159102e0d0c756b2eeeff08fcec" data-og-width="1275" width="1275" data-og-height="774" height="774" data-path="images/api-reference/vehicle_incompatible.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1d42a9b16af715d5479263ebef9d3806 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c43ba0468743922e945d8a0dc5579b1b 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=362847a86983a35cb81c0228987893eb 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=61f4dc4a21af5f1a7d73ec095e95c28f 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3ba9a62f4c6e9c36c9d2fcde981d6225 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1aa0e0fa04a5f90a5c3af5fafb7badd2 2500w" />
</Frame>

<br />

<Info>
  Note: This error will never occur if your application uses the Compatibility API. The Compatibility API verifies the compatibility of a vehicle before the user enters Smartcar Connect.
</Info>

To test this error, launch Smartcar Connect in test mode and log in with the email [smartcar@vehicle-incompatible.com](mailto:smartcar@vehicle-incompatible.com) and any password.

If you use Single Select, please see the table below for a simulated VIN.

| Email                                                                         | VIN               |
| ----------------------------------------------------------------------------- | ----------------- |
| [smartcar@vehicle-incompatible.com](mailto:smartcar@vehicle-incompatible.com) | 0SCAUDI012FE3B132 |
