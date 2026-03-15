# Source: https://docs.firehydrant.com/docs/signals-notification-preferences.md

# Notification Preferences

> 📘 Note:
>
> 📱 To download a vCard (Virtual Contact File) for FireHydrant, visit the following link: [http://fh.dev/vcf](http://fh.dev/vcf)

## Types of Notifications

<Image alt="Example of all types of notifications in different priorities" align="center" width="650px" src="https://files.readme.io/4c3573f43ac29f60b50de88730e142447e610d542e49369822504fd2005804c6-CleanShot_2025-01-08_at_17.22.42.png">
  Example of all types of notifications in different priorities
</Image>

Users can receive alerts from FireHydrant in several ways. Any alert a user receives, regardless of where they receive it, allows them to act on it: acknowledging, escalating, or opening an incident.

* **Mobile App Notifications (Push)** - Users who have installed the FireHydrant mobile app can also receive push notifications for any alerts. Clicking on the push notification allows them to respond to the alert easily by clicking on the correct action on the Alert page in the mobile app.
* **Slack Messages** - Users can also receive direct messages about alerts from the FireHydrant app in Slack. These messages will include action buttons to allow them to choose the correct action when quickly responding to the Alert.
* **Email** - Users can choose to receive an email every time an Alert is sent to them. The email will contain links to quickly choose the correct action for responding to the Alert. Any alternate emails you've configured can also be used for notifications.
* **WhatsApp Messages** - Users can add their mobile phone number to receive a WhatsApp message with information about the alert. Users can respond to text messages with codes for different alert actions. Each message will provide unique number codes for users to reply with for each action.
* **SMS or Text Messages** - Users can add their mobile phone number to receive a text message (SMS) with information about the alert. Users can respond to text messages with codes for different alert actions. Each message will provide unique number codes for users to reply with for each action.
* **Voice Calls** - Users can also use their mobile number to receive a voice call from FireHydrant. The voice call allows them to respond verbally to prompts to take the correct action on the alert.

> 👍 Emoji and Tapback Reactions
>
> When responding to an SMS Message, you can respond with emoji or tapback reactions to take action on the alert:
>
> * 👍 - a thumbs up reaction will **acknowledge** the alert
> * 👎 - a thumbs down reaction will **dismiss** the alert
> * ❓- a question mark will **escalate** the alert
> * ❗️❗️- a double exclamation reaction will automatically **open an incident**
>
> **Note:** Due to a reclassification of our messages by WhatsApp, emoji/tapback reactions are no longer supported for WhatsApp messages.

## Configuring Notifications

### Verifying Phone Numbers

<Image alt="Verifying a phone number" align="center" width="650px" src="https://files.readme.io/89927ab4e346040afec98833e28f5ed2bd459ac01a38ed3af8b0824c10ed7d8d-CleanShot_2025-01-08_at_17.19.01.png">
  Verifying a phone number
</Image>

To add a phone number to your user account

1. Navigate to your profile page (User Avatar > Profile) and find the Phone Numbers section of your profile.

2. Click “Add Phone Number” and add your phone number when prompted. Additionally, you should select a verification method, either SMS or a Call.

3. Verify your phone number using the method you selected. You will receive a six-digit code in either an SMS or a Call. Enter that code into the modal.

4. Once your phone number is verified, you should see a green check mark next to the phone number as it is listed.

5. Now, you can add your phone number as an SMS or Voice call notification preference in your Alert Notification Preferences.

Any user in your system responding to alerts can set up personal preferences about how they’d like to receive alerts from FireHydrant.

### Adding Notification Preferences

When an alert comes in and routes to a specific user, FireHydrant will first check if the user has preferences set for a particular priority. If not, then it will escalate upward. In the scenario where no notification preferences are set, or none exist for higher priorities, **FireHydrant will default to Slack + email notifications**.

<Image alt="Progressive notification fallback" align="center" width="650px" src="https://files.readme.io/b160c9f-CleanShot_2024-08-19_at_09.57.122x.png">
  Progressive notification fallback
</Image>

<Image alt="Alert notifications split by priority" align="center" width="650px" src="https://files.readme.io/65858f2-CleanShot_2024-06-28_at_11.53.21.png">
  Alert notifications split by priority
</Image>

To update or add notification preferences, click on your user avatar in the upper right-hand corner of the screen and navigate to **Profile** and then **Signals Notifications** tab on your profile page.

Users can configure their notifications according to priority of the Alert. They are split into three levels: `HIGH`, `MEDIUM`, and `LOW` priority.

Alternatively, on the mobile application, you can also click on the Settings gear icon on the FireHydrant mobile app ([iOS](https://apps.apple.com/us/app/firehydrant/id6473452572), [Android](https://play.google.com/store/apps/details?id=com.firehydrant.radio\&hl=en\&gl=US\&pli=1)) and then **Notifications**.

<Image alt="Notification settings in the mobile app" align="center" width="250px" src="https://files.readme.io/7c6d8bf-image.png">
  Notification settings in the mobile app
</Image>

* **Adding a new notification step -** Click the “Add notification step” button at the bottom of the preferences list to add a new notification preference. You can select a **Notification Type** and a **Delay**, which allows you to create gaps between the notifications.
* **Updating a notification step -** Clicking on any preference in the list of Notification Preferences will allow you to update the timing of that preference.
* **Removing a notification -** Click on any notification step and click on the trash can icon that appears as the right-most button in the notification step.

## Shift Reminders

<Image alt="A less verbose setting where user is only notified 5 minutes before a shift starts. No notification is sent when the shift ends" align="center" width="650px" src="https://files.readme.io/f91e1a3-CleanShot_2024-08-13_at_16.33.09.png">
  A less verbose setting where user is only notified 5 minutes before a shift starts. No notification is sent when the shift ends
</Image>

You can also customize your shift reminders - by default, FireHydrant will notify users about their assigned shifts through email and Slack DM at the following times:

* **24 hours before shift starts**
* **1 minute before shift starts**
* **1 minute before shift ends**

Users can customize this and change when they receive shift start notifications. FireHydrant will only notify users that their on-call shift is ending if they have configured a shift-start notification. You'll have options that range from a minute up to a week before the designated shift's start.

## Overriding Do Not Disturb (DND)

Often, users may have **Do Not Disturb** turned on, which can interfere with alert delivery to users. For each phone OS, there are different settings you can configure.

### Android Devices

On Android devices, your settings may vary depending on who your phone manufacturer is. Check the instructions below, and if they don't seem to match or align, you may need to look up information or docs for your specific phone manufacturer.

#### SMS and Voice

After importing the vCard contact above, we recommend adding the FireHydrant contact to your Starred contacts, and then allowing the Starred contacts to override messages and calls in Do Not Disturb mode.

1. First, go to FireHydrant in your contacts and ensure it is Starred :star:.
2. Next, head to **Settings> Notifications > Do Not Disturb > People**.
3. In this window, tap **Messages** and then check the Starred box to allow Starred users to message you in DND mode.
4. Go back one screen, then tap **Calls**. Do the same here and check the Starred box.

#### WhatsApp

You will need to allow WhatsApp as an application exception to your Do Not Disturb mode. Head to **Settings> Do not disturb > Apps** and then allow WhatsApp to override your DND settings.

#### Push Notifications

On Android, you'll need to go through two steps: first, allow FireHydrant access to Do Not Disturb settings, and then enable the override in the application.

<Image alt="Allow FireHydrant app access to DND settings" align="center" width="400px" src="https://files.readme.io/1bc1773-Untitled-2024-04-19-1118.png">
  Allow FireHydrant app access to DND settings
</Image>

<Image alt="Once allowed, configure the DND Override setting in FireHydrant app" align="center" width="400px" src="https://files.readme.io/b5488f8-Untitled-2024-04-19-1119.png">
  Once allowed, configure the DND Override setting in FireHydrant app
</Image>

### iOS Devices

#### SMS, WhatsApp, Voice

<Image alt="Adding the FireHydrant contact, then the contact to allowed People in DND Focus" align="center" width="400px" src="https://files.readme.io/1c80fb0-Untitled-2024-04-19-1120.png">
  Adding the FireHydrant contact, then the contact to allowed People in DND Focus
</Image>

Once you've imported the vCard file above, ensure you add the FireHydrant contact to your list of allowed people in the Do Not Disturb Focus type.

For WhatsApp, iOS automatically matches one of the phone numbers in the vCard contact to WhatsApp, so if the contact is allowed to bypass DND, you will also receive alerts on WhatsApp messages from them without needing to allow the all WhatsApp notifications.

#### Push Notifications

<Image alt="Critical Alerts setting on iOS devices" align="center" width="400px" src="https://files.readme.io/ca64971-IMG_8269.png">
  Critical Alerts setting on iOS devices
</Image>

Head to  **Settings> FireHydrant** and ensure "Critical Alerts" are checked to always deliver immediately. This will ensure you will always receive **Push notifications** from the app if configured.