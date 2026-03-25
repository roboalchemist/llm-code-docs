# Source: https://docs.luciq.ai/organization-settings/user-management/sso-using-saml.md

# SSO Using SAML

{% hint style="warning" %}
This document shows in detail how to configure your SAML SSO using [Okta](https://okta.com/), but most similar platforms that support SAML should have similar steps.
{% endhint %}

### Configuration Steps:

To configure Luciq with Okta, you will need to follow these steps:

1. Create an Okta account <https://www.okta.com/free-trial/>
2. Sign up in Luciq's dashboard using the same email address as Okta
3. At Luciq's dashboard, open the account settings> SSO > SAML and configure it.
4. At Okta's dashboard, click on the "Admin" button to open the admin panel
   1. Set up verification with the Okta Verify app (if needed)

      <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1401581126/b42d0b66b400d8b7f9ac6e5be51a/image.png?expires=1764258300&#x26;signature=897cb180ff68652d61619b04618d028a39d287797d13359e7f415850d2ca01bd&#x26;req=dSQnF8x2nIBdX%2FMW1HO4zZbyRreMfEvT702JzJ6p1GDrpHKma9PmbqtDiJu0%0AdbO8%0A" alt=""><figcaption></figcaption></figure>
5. Create a new application of "SAML" type
   1. From the sidebar, go to applications
   2. Select "Create App Integration"

      <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1401582755/fb6726bb45742092e2073ed30bf6/image.png?expires=1764258300&#x26;signature=942d67b1274c55dbaa7194dc6db1e57b059dd4de19794a1a85eddba71efced3d&#x26;req=dSQnF8x2n4ZaXPMW1HO4zdCIiPo2cyz%2Byk5w5y4E3W3vOu93V9utiAtwlk1b%0AOQFG%0A" alt=""><figcaption></figcaption></figure>
   3. Select SAML 2.0 type and click “Next“

      <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1401584548/1fc0f00ad5999ff3b59768ff9ff9/image.png?expires=1764258300&#x26;signature=1744bc7bf0464b498c6b0cf97883bf24f673ac72d42697e0987e64817568a7ac&#x26;req=dSQnF8x2mYRbUfMW1HO4zY2olfJRmstxgTg5ofyxNyoBzCMMErf6dpCFnipa%0AvZhW%0A" alt=""><figcaption></figcaption></figure>
   4. General settings: enter the app name and click “Next“\
      ​

      <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1401585455/7a5269c678624db48f2a182fd3bd/image.png?expires=1764258300&#x26;signature=261ed2e9a37290a44def5ed0e9ef141284b234a51917fd4e686068a79da0ac36&#x26;req=dSQnF8x2mIVaXPMW1HO4zRXh5U%2F3gxmnND0z%2FrgI9wGyMlPzpMoMzZaiOIiW%0ADsDw%0A" alt=""><figcaption></figcaption></figure>
   5. At configurations: enter the mapped values as follows from the dashboard Configure SAML SSO modal and then click “Next“
      1. Single sign-on URL → Service Provider SSO Callback URL (found on Configure SAML SSO modal on dashboard)
      2. Audience URI (SP Entity ID) → Service Provider Entity ID modal (found on Configure SAML SSO modal on the dashboard)
      3. leave Default RelayState empty
      4. Name ID format: select EmailAddress
      5. Application username: select email
   6. Feedback: select I'm a software vendor. I'd like to integrate my app with Okta and click “Finish”
6. Assign Users to App: Go to applications, click on assign users to app then select app and user, click “Next“ and confirm assignment.

   [![](https://downloads.intercomcdn.com/i/o/ih9pma6x/1401590860/68a65004f4d71654c6eccf12892a/image.png?expires=1764258300\&signature=2da87be964d34ce24a1d7ece734c68f0003232457d78e3d120139eac6eeea9ef\&req=dSQnF8x3nYlZWfMW1HO4zUKAE9DyFTrwDzyGkHAE9QZto9Tn8MtjqFbF5YNB%0AQ7yX%0A)](https://downloads.intercomcdn.com/i/o/ih9pma6x/1401590860/68a65004f4d71654c6eccf12892a/image.png?expires=1764258300\&signature=2da87be964d34ce24a1d7ece734c68f0003232457d78e3d120139eac6eeea9ef\&req=dSQnF8x3nYlZWfMW1HO4zUKAE9DyFTrwDzyGkHAE9QZto9Tn8MtjqFbF5YNB%0AQ7yX%0A)[![](https://downloads.intercomcdn.com/i/o/ih9pma6x/1401591562/00c281d11596de1a9fa13c517c26/image.png?expires=1764258300\&signature=c078047b97e64b03e85a9127fb5a97a2728deb3b03e0f9dc82ce232aac5f4e92\&req=dSQnF8x3nIRZW%2FMW1HO4zVbmR3HQZ%2BrW%2Bvy16Z4vLrnQBVU4aXFmhGgVIy6t%0At15b%0A)](https://downloads.intercomcdn.com/i/o/ih9pma6x/1401591562/00c281d11596de1a9fa13c517c26/image.png?expires=1764258300\&signature=c078047b97e64b03e85a9127fb5a97a2728deb3b03e0f9dc82ce232aac5f4e92\&req=dSQnF8x3nIRZW%2FMW1HO4zVbmR3HQZ%2BrW%2Bvy16Z4vLrnQBVU4aXFmhGgVIy6t%0At15b%0A)
7. From applications, open the created app, then select the “Sign On” tab
8. Scroll to “View Setup Instructions” and open it

   <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1401592923/3648379873e4fb1e9662cd15aa73/image.png?expires=1764258300&#x26;signature=0c22cb910707b2cb2156120ba0f6ed2abf42eb25919475c6f3774c9bd8805585&#x26;req=dSQnF8x3n4hdWvMW1HO4zZiNJlvHEydn%2Ffu1E89lmWmu91QKLDHuRPZ0SnLH%0AFhsd%0A" alt=""><figcaption></figcaption></figure>
9. Download Okta certificate
10. You can set up a fingerprint or upload the certificate directly
    1. Uploading certificate
       1. At the Luciq dashboard, Configure SAML SSO modal and select Certificate
          1. Upload downloaded certificate from step 9

             <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1732780238/86a37716bb566ab741d7484f1501/85800EDA-CE0D-48DF-9E7E-909574002640.jpeg?expires=1764258300&#x26;signature=4f7b46fb4ef3df473a9892e4dc8651d1139d6da2f44624616c4525156c4e82ff&#x26;req=dSckFM52nYNcUfMW1HO4zU%2B2R3kp%2Fw1azBuAkGgoNu%2B3xqv3U4xKgBFr6pYp%0AL6o5%0A" alt=""><figcaption></figcaption></figure>
          2. In SAML/idP metadata URL → add the Identity Provider Single Sign-On URL value on “View Setup Instructions” in Okta dashboard
    2. Setting fingerprint manually
       1. At your terminal change directory to where you downloaded the certificate in step 9
       2. Execute `openssl x509 -noout -fingerprint -sha1 -inform pem -in okta.cert`
       3. Copy the fingerprint value, which should look something like this: `F4:95:55:6E:97:D7:B6:26:56:3C:D0:4D:A0:D3:E4:05:B3:11:FF:B7`
       4. At the dashboard Configure SAML SSO modal select Fingerprint and enter the mapped values
          1. Identity Provider Certificate Fingerprint → paste the value you get from the terminal
          2. Identity Provider Certificate Fingerprint Algorithm → choose SHA1
          3. SAML/idP metadata URL → Identity Provider Single Sign-On URL value on View Setup Instructions in Okta dashboard
11. Logout from your normal account
12. Select login with SSO
13. Enter the Okta email that you assigned app to then your credentials on Okta form
14. After redirecting change dash-dev to deploy
15. Tada! 🎉

    <figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1732782238/d0f3e03c019891295cb6f7086e62/image.png?expires=1764258300&#x26;signature=e8c5b43589b27770055b515325b6750230e490f1e2c90cb5599538eac8348f9e&#x26;req=dSckFM52n4NcUfMW1HO4zUsIPw3%2BurUxFeFK8UOQU4BjeKqHWf53TdjzEeh0%0AMZP3%0A" alt=""><figcaption></figcaption></figure>

***

{% hint style="info" %}
To enable SAML/OAuth to your company for all members, you need to login using SSO at least once after configuring it.

After this, no member can login with their email/password, only logging in using SSO is allowed.
{% endhint %}

{% hint style="warning" %}
If you disabled SSO and then re-enable it, it will be enabled immediately for the whole company (without needing to login using SSO first)
{% endhint %}
