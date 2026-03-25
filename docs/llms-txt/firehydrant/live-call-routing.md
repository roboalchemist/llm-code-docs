# Source: https://docs.firehydrant.com/docs/live-call-routing.md

# Live Call Routing

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Required Permissions
      </th>

      <th style={{ textAlign: "left" }}>
        Required Entitlements
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        <Glossary>Member</Glossary>
        <Glossary>Owner</Glossary>
      </td>

      <td style={{ textAlign: "left" }}>
        <Glossary>Signals</Glossary>
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note
>
> Users with Signals access have up to 5 live call routes included. If you'd like more, reach out to your account team.

Live Call Routing is a feature where end users, like customers or internal team members, may call a phone number and either directly connect to an on-call responder over phone or leave a voicemail.

## Setting Up a Call Route

Like most Signals features, these are configured on a per-team basis. You can find Call Route settings by visiting a specific Team's page in FireHydrant and then clicking on the **Call Routes** tab.

1. Start by clicking '+ New call route\` on the top right side. This will expand a drawer where you can fill in information about the new call route you'd like to create.
2. Fill in some key details:
   1. **Name (required)** - Provide a clear name for this call route.
   2. **Description** - Provide a longer, more detailed description for the purpose of this call route.
   3. **Greeting Message** - This will be read out loud by a text-to-speech engine to the end user making the call.
   4. **Country Code (required)** - Select the country code of the destination number that end users will call. Current countries supported are USA, Canada, and UK. Once selected, FireHydrant will automatically generate a Phone Number.
   5. **Phone Number (required)** - Automatically filled in when you select a Country Code above.
   6. **Voicemail** vs. **Direct Connect**
      1. **Voicemail** - Allows the calling end-user to leave a voicemail. This voicemail will be recorded and transcribed, and an alert will be created with links to this voicemail recording.
      2. **Direct Connect** - Allows the calling end-user to directly connect to an on-call user and speak over the phone. This phone call will be recorded and transcribed, and this will similarly also create an alert with the link to the recorded phone conversation.
   7. **Contact Steps**
      1. **Wait for...Then contact (Direct Connect only)** - Like notification preferences, this allows you to configure wait/delay times as well as targets for connecting the calling user to someone live. Available targets include users and on-call schedules.
      2. **Fallback target (required)** - For Voicemail flows, this will be the user who is assigned to the generated alert. For Direct Connect, if all previously configured targets above don't pick up, then this will be the final target.
3. When finished, click 'Create call route'. Once the call route has been created, you can test it out by calling the number and leaving a voicemail.

<Image alt="Example Alert opened from a Voicemail Call Route" align="center" width="647px" src="https://files.readme.io/005be3ab177674bbd5f9e2e622fc835b1309a0988293a40c4825e41d4fdc674a-CleanShot_2025-01-13_at_17.28.24.png">
  Example Alert opened from a Voicemail Call Route. The phone number of the original caller will be present in the title of the opened alert.
</Image>

## Troubleshooting

### For T-Mobile Users

<Image alt="Allowing FireHydrant calls in T-Mobile's Scam Shield settings" align="center" width="650px" src="https://files.readme.io/e5b37c11994f16dfe46673ced96554f4c4cef8e63ae2ae379845a8bbb50d35f5-Diff.png">
  Allowing FireHydrant calls in T-Mobile's Scam Shield settings
</Image>

When using Direct Connect call routing, the number that reaches your on-call responder will be a FireHydrant number, ***not the end user's phone number***.

T-Mobile has a feature called **Scam Shield**, and this seems to function regardless of whether you have the T-Life app installed. This feature will automatically screen and block incoming calls, and it will sometimes block calls from FireHydrant even if you have FireHydrant added as a contact in your phone.

We are working to register all of our phone numbers with the appropriate registries and authorities, but in the meantime, to overcome this:

1. **Download the T-Life app, it's free** ([Google Play](https://play.google.com/store/apps/details?id=com.tmobile.tuesdays\&hl=en_US\&pli=1), [Apple Store](https://apps.apple.com/us/app/t-life/id1111876388)).
2. **Log in to your T-Mobile account and do any setup required for the app**.
3. **When setup is complete, navigate to Scam Shield settings**.
   1. You can get there by scrolling down on the home page to **Alerts** and clicking on **Scam Shield**.
   2. Alternatively, you can go to **Manage (bottom right)**, scrolling down to **Benefits**, and clicking on **Scam Shield**.
4. **On the Scam Shield page, you should see several sections and settings. Scroll down to Recent activity and check if a call from FireHydrant was blocked.**
   1. If you added FireHydrant as a contact via the vCard (see [Notification Preferences](https://docs.firehydrant.com/docs/signals-notification-preferences)), then you will see a FireHydrant logo next to the number.
   2. If not, download the vCard from the Notification Preferences page and add FireHydrant as a contact. From then on, any calls in this list history will show the FireHydrant logo next to them.
5. **Tap on any call from FireHydrant in this recent activity list, and then tap ":star: Calls allowed"**.
   1. This ensures any calls from FireHydrant moving forward will be allowed to reach you.