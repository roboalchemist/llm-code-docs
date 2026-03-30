# Source: https://docs.statsig.com/feature-flags/test-gate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test your Feature Gate

> Learn how to validate your feature gate using built-in tools, test apps, and live diagnostics in the Statsig console

There are three ways to test your feature gate and to validate that it's working as expected with the rules you have created:

1. Using the built-in **Test Gate** tool in the Statsig console
2. Using the prototype Javascript **Test App** available in the Statsig console
3. Using the **Diagnostics** tab in the Statsig console

## Option 1: Use the Test Gate tool

To validate your feature gate using the built-in Test Gate tool:

* Log into the Statsig console at [https://console.statsig.com](https://console.statsig.com)
* On the left-hand navigation panel, select **Feature Gates**
* Select the feature gate that you want to validate
* At the bottom of the page, the **Test Gate** window that lists all properties available in the rules you have created as shown below.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/test-gate/129104501-9e7349ae-31fe-47ea-97da-0520fd3d7e1b.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=40a57219a419bc841a40e5830071c3e1" alt="Test Gate interface showing property fields" width="743" height="203" data-path="images/feature-flags/test-gate/129104501-9e7349ae-31fe-47ea-97da-0520fd3d7e1b.png" />
</Frame>

* Click in the window and edit the value of the Email property to include the users that you want to target. For example, type [jdoe@example.com](mailto:jdoe@example.com) as shown below. When email domain matches "@example.com", the feature gate check succeeds and the window shows a PASS. Otherwise, it fails and the window shows a FAIL.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/test-gate/129104434-0f09087d-80da-4a62-84ac-c51e607e72a1.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=6b19eea0886181732a0e8f852bf7455f" alt="Test Gate showing PASS result for email validation" width="743" height="204" data-path="images/feature-flags/test-gate/129104434-0f09087d-80da-4a62-84ac-c51e607e72a1.png" />
</Frame>

## Option 2: Use the Statsig Test App

To validate your feature gate using the Test App:

* Log into the Statsig console at [https://console.statsig.com](https://console.statsig.com)
* On the left-hand navigation panel, select **Feature Gates**
* Select the feature gate that you want to validate
* At the bottom of the page, click on **Check Gate in Test App** at the top right of the Test Gate window as shown below by the red arrow; this will open a new browser window with a prototype Javascript client that initializes and calls the Statsig `checkGate` API.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/test-gate/138148684-581bb8d5-86ba-4aef-b24d-44e540fa91f1.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=765c85e595d3676685d36533b37ec6c7" alt="Check Gate in Test App button location" width="746" height="249" data-path="images/feature-flags/test-gate/138148684-581bb8d5-86ba-4aef-b24d-44e540fa91f1.png" />
</Frame>

## Option 3: Use the Diagnostics tab

To validate your feature gate using a live log stream:

* Log into the Statsig console at [https://console.statsig.com](https://console.statsig.com)
* On the left-hand navigation panel, select **Feature Gates**
* Select the feature gate that you want to validate
* Click on the **Diagnostics** tab (next to the Setup tab)
* Scroll down to the **Exposure Stream** panel, where you will see a live stream of gate check events as they happen as shown below

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/test-gate/138149819-5082d7e5-f7ee-42e8-b1ac-f57d9732e68f.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=4c678430db18e449f2e05cfc611a5c0a" alt="Exposure Stream panel showing live gate check events" width="928" height="352" data-path="images/feature-flags/test-gate/138149819-5082d7e5-f7ee-42e8-b1ac-f57d9732e68f.png" />
</Frame>

* In the **Event Count by Group panel** as shown below, you can also validate that your application is recording events as expected for users who are exposed to the new feature (or not). Specifically, if you've started to record a new event type to test the impact of a new feature, you can also validate that these events are starting to show as more users are exposed to the new feature.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/test-gate/141017409-f750c1c6-4c54-4140-bc4d-a3b83f1568fc.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=18e8eff67b709c9ae409268f82a48305" alt="Event Count by Group panel showing feature exposure metrics" width="901" height="346" data-path="images/feature-flags/test-gate/141017409-f750c1c6-4c54-4140-bc4d-a3b83f1568fc.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).