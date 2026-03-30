# Source: https://documentation.onesignal.com/docs/en/find-set-test-subscriptions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test subscriptions

> How to find and set up Test Subscriptions in OneSignal.

**Audience > Subscriptions** shows a list of every subscription in your OneSignal App, and [Data Collected by the OneSignal SDK](./data-collected-by-the-onesignal-sdk). More details in our [Users](./users) guide.

There are 3 types of subscriptions. Check the *Channel* and *Device* columns for each:

<Columns cols={3}>
  <Card
    title="Push Subscription"
    icon={<svg
  xmlns="http://www.w3.org/2000/svg"
  width={18}
  height={18}
  fill="currentColor"
  viewBox="0 0 16 16"
  {...props}
>
  <path
    fillRule="evenodd"
    d="M16 3a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm-7-.333A2.791 2.791 0 0 0 9 3a4 4 0 0 0 4 3.98c.111.007.222.007.333 0V14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4.667a2 2 0 0 1 2-2h7ZM2.86 7.5a.86.86 0 0 0 0 1.72h6.83a.86.86 0 1 0 0-1.72H2.86Zm0 3.98a.86.86 0 1 0 0 1.72h4.58a.86.86 0 0 0 0-1.72H2.86Z"
    clipRule="evenodd"
  />
</svg>
}
  >
    Can be sent push notifications.
  </Card>

  <Card
    title="Email Subscription"
    icon={<svg
  xmlns="http://www.w3.org/2000/svg"
  width={18}
  height={18}
  fill="currentColor"
  {...props}
>
  <path d="M7.448 7.026A.968.968 0 0 0 8 7.198a.968.968 0 0 0 .552-.172l6.638-4.98a.403.403 0 0 0 .11-.13.402.402 0 0 0 .044-.166.403.403 0 0 0-.123-.31A2.4 2.4 0 0 0 13.6.8H2.4a2.4 2.4 0 0 0-1.62.64.398.398 0 0 0-.101.143.398.398 0 0 0-.03.171.398.398 0 0 0 .047.168.398.398 0 0 0 .114.132l6.638 4.972Z" />
  <path d="M9.51 8.304a2.56 2.56 0 0 1-3.02 0L.64 3.918a.4.4 0 0 0-.204-.078.4.4 0 0 0-.215.04.4.4 0 0 0-.221.358V12.8a2.4 2.4 0 0 0 2.4 2.4h11.2a2.4 2.4 0 0 0 2.4-2.4V4.238a.4.4 0 0 0-.06-.21.4.4 0 0 0-.161-.147.4.4 0 0 0-.419.037L9.51 8.304Z" />
</svg>}
  >
    Can be sent email messages.
  </Card>

  <Card
    title="SMS Subscription"
    icon={<svg
  xmlns="http://www.w3.org/2000/svg"
  width={18}
  height={18}
  fill="currentColor"
  {...props}
>
  <path
    fillRule="evenodd"
    d="M1.15 12.24a.409.409 0 0 1-.046.186l-1.066 2.81a.551.551 0 0 0 .088.55.588.588 0 0 0 .445.214h.106l3.858-.693a.391.391 0 0 1 .249 0A8.103 8.103 0 0 0 8 15.982a7.997 7.997 0 0 0 7.857-6.614c.092-.456.14-.92.142-1.386A8.001 8.001 0 0 0 5.892.283a7.998 7.998 0 0 0-4.788 11.77c.03.058.045.122.045.187zm4.183-2.907a1.333 1.333 0 1 0 0-2.666 1.333 1.333 0 0 0 0 2.666zm5.334 0a1.333 1.333 0 1 0 0-2.666 1.333 1.333 0 0 0 0 2.666z"
    clipRule="evenodd"
  />
</svg>}
  >
    Can be sent SMS and MMS messages.
  </Card>
</Columns>

<Note>
  Android, iOS, Huawei and Amazon mobile app push subscriptions can also get In-App Messages.
</Note>

You can search for a user and all associated subscription records by the External ID or OneSignal ID (details in [Aliases & External ID](./users)). If you don't know the ID of the user, you can search by email address or phone number to find it.

Set any subscriptions for a given user to be test subscriptions to make it easier to find them.

You can show/hide the data attributes with the **columns** button (1), search by Subscription ID, OneSignal ID, External ID, Email or Phone Number (2) and filter by [Segments](./segmentation) (3).

<Frame caption="Steps from the 'Subscriptions' tab">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f13a5d8-subscription-records-add-test-subscriber.jpg?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=13d71269896011e7c6f86cec978bd6da" width="1839" height="957" data-path="images/docs/f13a5d8-subscription-records-add-test-subscriber.jpg" />
</Frame>

## Test Subscriptions

Test Subscriptions are a group of records that you manage directly in order to test delivery of messages.

To add your device as a Test Subscription:

1. First [find your subscription](#finding-subscriptions). There are several options listed below.
2. Once you have your External ID, OneSignal ID or Subscription ID, you can search for it (1), then next to the device record select **Options** > **Add to Test Subscriptions** (2).

<Frame>
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6a79d57-subscription-records-config.jpg?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=e2235b3c0e5568c07a1ef79604df4f91" width="2065" height="961" data-path="images/docs/6a79d57-subscription-records-config.jpg" />
</Frame>

Next you can [Segment](./segmentation) devices by Test Subscriptions Filter and/or send messages using the **Send To Test Device Button**.

<Frame>
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/878ade1-Screenshot_2023-08-11_at_1.13.24_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=4b2a5aa7fb8c24de7c40e46ecdcdb4b2" width="1976" height="1072" data-path="images/docs/878ade1-Screenshot_2023-08-11_at_1.13.24_PM.png" />
</Frame>

## Finding Subscriptions

There are a couple options for finding your device depending on the data you currently have.

<Accordion title="Find your Subscription ID for Web Push">
  <Tabs>
    <Tab title="Desktop Web Push">
      1. Using the same browser profile you are subscribed to your site, open the site URL with the OneSignal code active.
      2. Open the Debugger console (F12 or Right Click the site > Inspect).
      3. Click the "Console" section
      4. Add this code: `OneSignal.User.PushSubscription.id`
      5. You will see your OneSignal Subscription Id logged to the console if you have a device record.

      <Check>
        Copy the Subscription ID without quotes and see above to add it as a Test Subscription.
      </Check>
    </Tab>

    <Tab title="Mobile Web Push">
      1. Plug your Android device subscribed to the site into your computer and visit your site on the Android device.
      2. On your desktop, open chrome to this url: `chrome://inspect/#devices` Your mobile device should prompt you to enable USB Debugging
      3. Select the **inspect** button

      <Frame>
        <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/87b3a68-d107be1-Screen_Shot_2020-04-03_at_10.28.47_AM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=293b3471cc272b2178e43d8d8fd041be" width="900" height="362" data-path="images/docs/87b3a68-d107be1-Screen_Shot_2020-04-03_at_10.28.47_AM.png" />
      </Frame>

      4. A new window on desktop should open to your site seen on the mobile device.
      5. Make sure the site URL is correct with the OneSignal code active.
      6. Click the "Console" section
      7. Add this code: `OneSignal.User.PushSubscription.id`
      8. You will see your OneSignal Subscription ID logged to the console if you have a device record.

      <Check>
        Copy the Subscription ID without quotes and see above to add it as a Test Subscription.
      </Check>
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Find your device for Mobile App">
  Using the OneSignal SDK [User Data Methods](./mobile-sdk-reference), plugin your device to Xcode or Android Studio and log the Subscription ID of your device in the console.

  <Check>
    Copy the Subscription ID without quotes and see above to add it as a Test Subscription.
  </Check>
</Accordion>

<Accordion title="Find Subscription in Dashboard">
  Open your app or site with your subscribed device. Make sure you are visiting a page of your site/app with OneSignal initialized (code actively running). Then in your OneSignal dashboard **Audience > Subscriptions** sort by "Last Active" so the arrow points up to see the latest active devices.

  You may need to confirm it is your device by making some data visible. Click the **Displayed Columns List** filter at the top-right. Some helpful data to check is:

  | Column                | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **External ID**       | This should be the same ID found in your database for your user. You may need to ask your developer for more info.                                                                                                                                                                                                                                                                                                                                                         |
  | **Last Active**       | The most recent time the user visited the site/app. You may want to refresh the page to get updated values.                                                                                                                                                                                                                                                                                                                                                                |
  | **First Session**     | The first time you subscribed to the website or opened the app with OneSignal code. Check if this is the first time you subscribed to the site/app.                                                                                                                                                                                                                                                                                                                        |
  | **IP Address**        | If enabled, visit [https://whatismyipaddress.com/](https://whatismyipaddress.com/) to see if the IPs match. More details in [Data Collected by the OneSignal SDK](./data-collected-by-the-onesignal-sdk)                                                                                                                                                                                                                                                                   |
  | **Tags**, **Country** | This is additional information that can be used to check if you know this data.                                                                                                                                                                                                                                                                                                                                                                                            |
  | **Device**            | - Mobile Website subscribers will show "Linux Arm..." with the Browser icon and Browser version. - Desktop Website subscribers will show Mac or Win with Browser icon and Browser version. - Android Mobile Apps - will have the device model and corresponding icons. - iOS Mobile Apps - the model is based on the [Hardware String](https://www.theiphonewiki.com/wiki/Models). For example "iPhone9,3 (12.3.1)" means "iPhone 7 with operating system version 12.3.1". |

#### Segmenting by Tag

  If you added a specific tag to the user like a `user_name`, `email` tag, or other identifier, you can create a [Segment with the User Tag filter](./segmentation#section-creating-advanced-segments) to find your specific device.

  <Frame>
    <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d0e0918-segment-user-tag-filter.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=b0168905a85a4e6424dc0c38e746e25d" width="1678" height="214" data-path="images/docs/d0e0918-segment-user-tag-filter.png" />
  </Frame>

  <Check>
    Copy the Subscription ID without quotes and see above to add it as a Test Subscription.
  </Check>
</Accordion>

***

Built with [Mintlify](https://mintlify.com).
