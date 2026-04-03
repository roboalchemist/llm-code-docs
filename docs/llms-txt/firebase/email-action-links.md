# Source: https://firebase.google.com/docs/auth/admin/email-action-links.md.txt

<br />

Mobile apps sometimes need to interact with users and prompt them to take certain actions by sending emails.

The Firebase[Client SDKs](https://firebase.google.com/docs/libraries#client-sdks)provide the ability to send users emails containing links they can use for password resets, email address verification, and email-based sign-in. These template-based emails are sent by Google and have limited customizability.

If you want to instead use your own email templates and your own email delivery service, this page explains how to use the[Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)to programmatically generate the action links for the above flows, which you can include in emails to your users.

This comes with the following benefits:

- Customize email templates. This includes the ability to add new styles and custom branding, change wording and logos, address users by first name instead of full name, and so on.
- Apply different templates depending on context. For example, if the user is verifying their email to subscribe to a newsletter, the context may need to be provided in the email content. Another example is email link sign in: in one scenario this may be triggered by the same user, or as an invite by another user. The context would need to be included in the email.
- Localize customized email templates.
- Ability to generate the link from a secure server environment.
- Ability to customize how the link is to be opened, through a mobile app or a browser, and how to pass additional state information, etc.
- Ability to customize the mobile link domain used for mobile app flows when constructing the email action link.

## Initialize ActionCodeSettings

Before you can generate an email action link, you may need to initialize an`ActionCodeSettings`instance.

`ActionCodeSettings`allow you to pass additional state via a continue URL which is accessible after the user clicks the email link. This also provides the user the ability to go back to the app after the action is completed. In addition, you can specify whether to handle the email action link directly from a mobile application when it is installed or from a browser.

For links that are meant to be opened via a mobile app, you'll need to perform some tasks to detect these links from your mobile app. Refer to the instructions on how to[configure mobile links](https://firebase.google.com/docs/auth/web/passing-state-in-email-actions#configuring-hosting-links)for email actions.

To initialize an`ActionCodeSettings`instance, provide the following data:

|      Parameter      |                                                 Type                                                 |                                                                                                                                                                                   Description                                                                                                                                                                                   |
|---------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `url`               | string                                                                                               | Sets the link (state/continue URL) which has different meanings in different contexts: - When the link is handled in the web action widgets, this is the deep link in the`continueUrl`query parameter. - When the link is handled in the app directly, this is the`continueUrl`query parameter in the deep link of theHostinglink.                                              |
| `iOS`               | ({bundleId: string}\|undefined)                                                                      | Sets the iOS bundle ID to helpFirebase Authenticationdetermine if it should create a web-only or mobile link which is opened on an Apple device                                                                                                                                                                                                                                 |
| `android`           | ({packageName: string, installApp:boolean\|undefined, minimumVersion: string\|undefined}\|undefined) | Sets the Android package name to helpFirebase Authenticationdetermine if it should create a web-only or mobile link which is opened on an Android device                                                                                                                                                                                                                        |
| `handleCodeInApp`   | (boolean\|undefined)                                                                                 | Whether the email action link will be opened in a mobile app or a web link first. The default is false. When set to true, the action code link will be be sent as a Universal Link or Android App Link and will be opened by the app if installed. In the false case, the code will be sent to the web widget first and then on continue will redirect to the app if installed. |
| `linkDomain`        | (string\|undefined)                                                                                  | When custom Hosting link domains are defined for a project, specify which one to use when the link is to be opened by a specified mobile app. Otherwise, the default domain is automatically selected (for example,<var translate="no">PROJECT_ID</var>`.firebaseapp.com`).                                                                                                     |
| `dynamicLinkDomain` | (string\|undefined)                                                                                  | Deprecated. Don't specify this parameter.                                                                                                                                                                                                                                                                                                                                       |

The following example illustrates how to send an email verification link that will open in a mobile app first. The deep link will contain the continue URL payload`https://www.example.com/checkout?cartId=1234`. The customHostinglink domain used is`custom-domain.com`, which must be configured for use withFirebase Hosting.  

### Node.js

    const actionCodeSettings = {
      // URL you want to redirect back to. The domain (www.example.com) for
      // this URL must be whitelisted in the Firebase Console.
      url: 'https://www.example.com/checkout?cartId=1234',
      // This must be true for email link sign-in.
      handleCodeInApp: true,
      iOS: {
        bundleId: 'com.example.ios',
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12',
      },
      // The domain must be configured in Firebase Hosting and owned by the project.
      linkDomain: 'custom-domain.com',
    };

### Java

    ActionCodeSettings actionCodeSettings = ActionCodeSettings.builder()
        .setUrl("https://www.example.com/checkout?cartId=1234")
        .setHandleCodeInApp(true)
        .setIosBundleId("com.example.ios")
        .setAndroidPackageName("com.example.android")
        .setAndroidInstallApp(true)
        .setAndroidMinimumVersion("12")
        .setDynamicLinkDomain("coolapp.page.link")
        .build();

### Python

    action_code_settings = auth.ActionCodeSettings(
        url='https://www.example.com/checkout?cartId=1234',
        handle_code_in_app=True,
        ios_bundle_id='com.example.ios',
        android_package_name='com.example.android',
        android_install_app=True,
        android_minimum_version='12',
        dynamic_link_domain='coolapp.page.link',
    )

### Go

    actionCodeSettings := &auth.ActionCodeSettings{
    	URL:                   "https://www.example.com/checkout?cartId=1234",
    	HandleCodeInApp:       true,
    	IOSBundleID:           "com.example.ios",
    	AndroidPackageName:    "com.example.android",
    	AndroidInstallApp:     true,
    	AndroidMinimumVersion: "12",
    	DynamicLinkDomain:     "coolapp.page.link",
    }

### C#

    var actionCodeSettings = new ActionCodeSettings()
    {
        Url = "https://www.example.com/checkout?cartId=1234",
        HandleCodeInApp = true,
        IosBundleId = "com.example.ios",
        AndroidPackageName = "com.example.android",
        AndroidInstallApp = true,
        AndroidMinimumVersion = "12",
        LinkDomain = "coolapp.page.link",
    };

To learn more, see[Passing State in Email Actions](https://firebase.google.com/docs/auth/web/passing-state-in-email-actions).

## Generate password reset email link

To generate a password reset link, provide the existing user's email and an optional`ActionCodeSettings`object. The operation will resolve with the email action link. The email used must belong to an existing user.  

### Node.js

    // Admin SDK API to generate the password reset link.
    const userEmail = 'user@example.com';
    getAuth()
      .generatePasswordResetLink(userEmail, actionCodeSettings)
      .then((link) => {
        // Construct password reset email template, embed the link and send
        // using custom SMTP server.
        return sendCustomPasswordResetEmail(userEmail, displayName, link);
      })
      .catch((error) => {
        // Some error occurred.
      });

### Java

    String email = "user@example.com";
    try {
      String link = FirebaseAuth.getInstance().generatePasswordResetLink(
          email, actionCodeSettings);
      // Construct email verification template, embed the link and send
      // using custom SMTP server.
      sendCustomEmail(email, displayName, link);
    } catch (FirebaseAuthException e) {
      System.out.println("Error generating email link: " + e.getMessage());
    }

### Python

    email = 'user@example.com'
    link = auth.generate_password_reset_link(email, action_code_settings)
    # Construct password reset email from a template embedding the link, and send
    # using a custom SMTP server.
    send_custom_email(email, link)

### Go

    email := "user@example.com"
    link, err := client.PasswordResetLinkWithSettings(ctx, email, actionCodeSettings)
    if err != nil {
    	log.Fatalf("error generating email link: %v\n", err)
    }

    // Construct password reset template, embed the link and send
    // using custom SMTP server.
    sendCustomEmail(email, displayName, link)

### C#

    var email = "user@example.com";
    var link = await FirebaseAuth.DefaultInstance.GeneratePasswordResetLinkAsync(
        email, actionCodeSettings);
    // Construct email verification template, embed the link and send
    // using custom SMTP server.
    SendCustomEmail(email, displayName, link);

After the link is generated, it can be inserted into the custom password reset email and then emailed to the corresponding user using a custom SMTP server.

If you are not using the default password reset landing page and building your own custom handler, see[creating custom email action handlers](https://firebase.google.com/docs/auth/custom-email-handler).

## Generate email verification link

To generate an email verification link, provide the existing user's unverified email and an optional`ActionCodeSettings`object. The operation will resolve with the email action link. The email used must belong to an existing user.  

### Node.js

    // Admin SDK API to generate the email verification link.
    const useremail = 'user@example.com';
    getAuth()
      .generateEmailVerificationLink(useremail, actionCodeSettings)
      .then((link) => {
        // Construct email verification template, embed the link and send
        // using custom SMTP server.
        return sendCustomVerificationEmail(useremail, displayName, link);
      })
      .catch((error) => {
        // Some error occurred.
      });

### Java

    String email = "user@example.com";
    try {
      String link = FirebaseAuth.getInstance().generateEmailVerificationLink(
          email, actionCodeSettings);
      // Construct email verification template, embed the link and send
      // using custom SMTP server.
      sendCustomEmail(email, displayName, link);
    } catch (FirebaseAuthException e) {
      System.out.println("Error generating email link: " + e.getMessage());
    }

### Python

    email = 'user@example.com'
    link = auth.generate_email_verification_link(email, action_code_settings)
    # Construct email from a template embedding the link, and send
    # using a custom SMTP server.
    send_custom_email(email, link)

### Go

    email := "user@example.com"
    link, err := client.EmailVerificationLinkWithSettings(ctx, email, actionCodeSettings)
    if err != nil {
    	log.Fatalf("error generating email link: %v\n", err)
    }

    // Construct email verification template, embed the link and send
    // using custom SMTP server.
    sendCustomEmail(email, displayName, link)

### C#

    var email = "user@example.com";
    var link = await FirebaseAuth.DefaultInstance.GenerateEmailVerificationLinkAsync(
        email, actionCodeSettings);
    // Construct email verification template, embed the link and send
    // using custom SMTP server.
    SendCustomEmail(email, displayName, link);

After the link is generated, it can be inserted into the custom verification email and then emailed to the corresponding user using a custom SMTP server.

If you are not using the default email verification landing page and building your own custom handler, see[creating custom email action handlers](https://firebase.google.com/docs/auth/custom-email-handler).

## Generate email link for sign-in

Before you can authenticate users with email link sign-in, you will need to[enable email link sign-in](https://firebase.google.com/docs/auth/web/email-link-auth#enable_email_link_sign-in_for_your_firebase_project)for your Firebase project.

To generate a sign-in link, provide the user's email and an`ActionCodeSettings`object. The`ActionCodeSettings`object is required in this case to provide information on where to return the user after the link is clicked for sign-in completion. The operation will resolve with the email action link.

Unlike password reset and email verification, the email used does not necessarily need to belong to an existing user, as this operation can be used to sign up new users into your app via email link.  

### Node.js

    // Admin SDK API to generate the sign in with email link.
    const useremail = 'user@example.com';
    getAuth()
      .generateSignInWithEmailLink(useremail, actionCodeSettings)
      .then((link) => {
        // Construct sign-in with email link template, embed the link and
        // send using custom SMTP server.
        return sendSignInEmail(useremail, displayName, link);
      })
      .catch((error) => {
        // Some error occurred.
      });

### Java

    String email = "user@example.com";
    try {
      String link = FirebaseAuth.getInstance().generateSignInWithEmailLink(
          email, actionCodeSettings);
      // Construct email verification template, embed the link and send
      // using custom SMTP server.
      sendCustomEmail(email, displayName, link);
    } catch (FirebaseAuthException e) {
      System.out.println("Error generating email link: " + e.getMessage());
    }

### Python

    email = 'user@example.com'
    link = auth.generate_sign_in_with_email_link(email, action_code_settings)
    # Construct email from a template embedding the link, and send
    # using a custom SMTP server.
    send_custom_email(email, link)

### Go

    email := "user@example.com"
    link, err := client.EmailSignInLink(ctx, email, actionCodeSettings)
    if err != nil {
    	log.Fatalf("error generating email link: %v\n", err)
    }

    // Construct sign-in with email link template, embed the link and send
    // using custom SMTP server.
    sendCustomEmail(email, displayName, link)

### C#

    var email = "user@example.com";
    var link = await FirebaseAuth.DefaultInstance.GenerateSignInWithEmailLinkAsync(
        email, actionCodeSettings);
    // Construct email verification template, embed the link and send
    // using custom SMTP server.
    SendCustomEmail(email, displayName, link);

After the link is generated, it can be inserted into the custom sign-in email and then emailed to the corresponding user using a custom SMTP server.

Learn more about[authenticating users with Firebase using email links](https://firebase.google.com/docs/auth/web/email-link-auth). This will help provide information on how to complete sign-in after the user clicks the link and is redirected back to the app.