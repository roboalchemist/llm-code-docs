# Source: https://firebase.google.com/docs/test-lab/ios/available-testing-devices.md.txt

# Available devices in Test Lab

> [!NOTE]
> **Note:** iOS 18+ devices don't support videos in the results.

Test Lab lets you test your app on a wide variety of different devices and
iOS versions. There are a few ways to see which devices are available:

- **Firebase console:** If you're running tests from the Firebase console,
  you can see a list of available devices during the **Select dimensions** step
  of the **Run a test** workflow.

- **gcloud CLI:** To see a list of available devices from the Google Cloud
  CLI, use the following command:

  ```
  gcloud firebase test ios models list
  ```
- **Google APIs Explorer:** You can even look up the devices directly, without a
  Firebase project or the gcloud CLI, using the
  [Google APIs Explorer](https://developers.google.com/apis-explorer/#p/testing/v1/testing.testEnvironmentCatalog.get?environmentType=IOS).

## Device stability indicator

Test Lab indicates devices that are experiencing degraded stability in the
Firebase console and Google Cloud CLI with a **Reduced Stability** indicator.
Devices that have been labeled with the **Reduced Stability** indicator have
returned higher rates of inconclusive results for a prolonged period of 30 days
or more. This feature helps you better choose devices for your use case by
letting you know if the stability of a test device is degraded.

### View device stability in the Firebase console

You can view device stability in the Firebase console when you're setting up
a new test for a specific device.

To view device stability, follow these instructions:

1. Open the Test Lab page in the Firebase console.

   > [!NOTE]
   > **Note:** If this is your first time running a test, follow the onboarding instructions on the main Test Lab page in the Firebase console.

2. Select **Run a test** and then select a test type.

3. Upload your app binary.

4. On the Select dimensions step, click **Customize**.

5. Choose one or more devices to run your test on. Depending on device
   stability, you might see a **Reduced Stability** label next to the selected
   devices.

6. Run your test.

### View device stability in the Google Cloud CLI

You can view device stability in the gcloud CLI for a specific device when
you're setting up a new test.

To view device stability, follow these instructions:

1. Download the latest [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk#installing_the_latest_version) and follow the
   instructions.

2. Run one of these commands:
   `gcloud firebase test ios models list` or
   `gcloud firebase test ios models describe MODEL_ID`

If a test device is experiencing degraded stability, you can see the
`reduced_stability` tag in the TAGS column listing the versions that are affected.

## Device capacity

Test Lab provides aggregated mobile device capacity information
through the Firebase console and Firebase CLI. *Device capacity* is the
aggregated number of online devices in Google's mobile device lab. This feature
helps you ensure that there are enough devices in our device lab to run your
tests more efficiently. Device capacity is measured as High, Medium, and Low.

> [!NOTE]
> **Note:** Device capacity does not reflect real-time factors like the length of the pending test queue at a moment in time, real-time traffic on the devices, or the state of the devices. For physical devices, the number is the average of online devices in the last 30 days.

Tests running on any device capacity level may take longer due to the
following factors:

- Traffic, which affects when the test starts. To check if there are reported outages or failures, see the [Firebase status dashboard](https://status.firebase.google.com/summary).
- Device or infrastructure failures, which can happen at any time and affect how long the test takes to run.

The following table describes the types of device capacity and
provides recommendations about when to use each capacity type:

|---|---|---|
| **Capacity** | **Description** | **Recommended use** |
| High capacity | The Test Lab device catalog contains many devices. | Use when you are running a large number of tests. |
| Medium capacity | The Test Lab device catalog contains a moderate number of devices. | This capacity level is suitable for running most of your tests. |
| Low capacity | The Test Lab device catalog contains few devices. While deprecated devices belong to the low-capacity group, not all low-capacity devices are deprecated. | Use when you need to run a test on a specific device model and version. These tests are not suitable for test sharding. Due to low capacity, tests might take a long time to finish, especially if you invoke a large number of tests at the same time. |

### View device capacity in the Firebase console

You can view device capacity in the Firebase console for a specific device
when you're setting up a new test.

To view device capacity, follow these instructions:

1. Open the Test Lab page in the Firebase console.

   > [!NOTE]
   > **Note:** If this is your first time running a test, follow the onboarding instructions on the main Test Lab page in the Firebase console.

2. Select **Run a test** and then select a test type.

3. Upload your app binary.

4. On the Select dimensions step, click **Customize**.

5. (Optional) To filter devices by capacity level, follow these steps:

   1. Click the **Filter** icon.

   2. Select **Capacity**.

   3. Click the capacity level you want to filter by: **Medium** or **High**.
      To filter out any low-capacity devices, filter by both Medium and High.

   4. Click **Apply**.

6. Choose one or more devices to run your test on. Depending on device
   capacity, you might see a **Medium** or **High** label next
   to the selected devices.

7. Run your test.

### View device capacity in the Google Cloud CLI

You can view device capacity in the gcloud CLI for a specific device
when you're setting up a new test.

To view device capacity, follow these instructions:

1. Download the latest [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk#installing_the_latest_version) and follow the instructions. The version must be 417.0.0 or greater.
2. Run one of these commands:  
   `gcloud firebase test ios list-device-capacities`  
   or  
   `gcloud firebase test ios models describe MODEL_ID`

The output includes device capacity, model ID, model name, and OS version ID.


## Deprecated devices and versions

Deprecated devices are available for at least one month before being removed
from the Test Lab device catalog. Once a device is removed, Test Lab
no longer runs test requests targeted at the device; those requests are
marked as `Skipped`.

#### Deprecated devices

| Model | Type | Device/Version | Removing on |
|---|---|---|---|
| iPad 5 | Physical | iPad5/15.4 | 2024-04-07 |
| iPhone 13 Pro | Physical | Iphone13pro/15.2 | 2024-04-07 |
| iPad Mini 4 | Physical | ipadmini4/15.4 | 2024-04-07 |
| iPhone 8 | Physical | iphone8/14.7 | 2025-04-03 |
| iPhone 11 Pro | Physical | iphone11pro/14.7 | 2025-04-03 |
| iPhone 12 Pro | Physical | iphone12pro/14.8 | 2025-04-03 |

## Request a device

If you want to use a device that is not available in Test Lab, you can
[submit a request](https://firebase.google.com/support/troubleshooter/test_lab/requestdevice) for a device
to be added to the catalog.