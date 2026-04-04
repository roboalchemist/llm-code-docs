# Source: https://docs.base44.com/Setting-up-your-app/Managing-login-and-registration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing login and registration

> Choose how people sign up and access your app with authentication.

Authentication controls how your app’s users sign in, register, and access its features. With Base44, you can choose among popular login providers, decide how data is collected at registration, and shape the experience for your users.

<img src="https://mintcdn.com/base44/5X5sbBT0yOIFN9Cs/images/2025-10-26_19-01-00.png?fit=max&auto=format&n=5X5sbBT0yOIFN9Cs&q=85&s=f632bfd67ebeb721554a7cb30b1d3846" alt="Login options in Base44 apps" width="1890" height="1206" data-path="images/2025-10-26_19-01-00.png" />

***

## Choosing login options for your app

Choose the authentication methods that work best for your app and your audience. You can offer multiple ways for people to sign up, such as email, Google, or other providers, so that login stays simple, secure, and familiar.

You can enable more than one login option.

**To choose your app’s login options:**

1. Click **Dashboard** in your app editor.
2. Click **Settings**.
3. Click **Authentication**.
4. Enable the toggle next to the relevant authentication options:
   * **Email and password**: Allow people to create an account with their email address and a secure password.
   * **Google**: Allow people to log in using their Google account credentials.
   * **Microsoft**: Allow people to log in using their Microsoft credentials.
   * **Facebook**: Allow people to log in using their Facebook credentials.
   * **Apple**: Allow people to log in using their Apple account.
   * **Single sign-on (SSO)**: Connect an external identity provider that supports OIDC, such as Okta or your company’s identity provider, so people can log in using credentials from that provider.

     <Warning>
       **Important:** SSO is only available for the Elite plan. Learn more about [setting up SSO](https://docs.base44.com/Setting-up-your-app/Setting-up-SSO).
     </Warning>

<Frame caption="Adding authentication methods to your app in Base44">
    <img src="https://mintcdn.com/base44/WQGg9I6yHW8iaAjb/apple.png?fit=max&auto=format&n=WQGg9I6yHW8iaAjb&q=85&s=9f413dfb56f7bd084c81009c7d3d01f0" alt="Adding authentication methods to your app in Base44" width="1293" height="749" data-path="apple.png" />
</Frame>

<Note>
  **Note:** For Facebook login to work, the person logging in needs a verified Facebook account. If their Facebook email or identity is not verified, Facebook can block the login and show an error message. They must complete Facebook's identity confirmation process in their Meta account before they can sign in to your app with Facebook.
</Note>

***

## Customizing the Google login

Base44 gives you 2 ways to set up Google login, so you can manage how your users experience sign-in and how your brand is displayed:

* **Default Google login:** Fast setup using Base44’s credentials. The login window shows “Sign in with Google” and is branded with [base44.com](http://base44.com). To use this method, enable the **Google authentication** toggle and select **Use the default Base44 OAuth**.

<img src="https://mintcdn.com/base44/5X5sbBT0yOIFN9Cs/images/2025-10-26_15-27-56.png?fit=max&auto=format&n=5X5sbBT0yOIFN9Cs&q=85&s=7f94cb9199797bf91588cc686ecbe79d" alt="2025 10 26 15 27 56 Pn" style={{ width:"98%" }} width="2164" height="926" data-path="images/2025-10-26_15-27-56.png" />

* **Custom Google OAuth:** Connect your own Google Cloud client ID and secret in the Authentication panel. Your users will see your app’s domain, not "base44.com" when they sign in with Google. Custom Google OAuth is a great choice if you want full control over your login branding or need your app’s domain and messaging to appear in the Google login window. This is ideal for businesses that require a fully branded experience or need to meet enterprise requirements.

<img src="https://mintcdn.com/base44/orZls59geuFavS1L/images/2025-10-29_12-51-25.png?fit=max&auto=format&n=orZls59geuFavS1L&q=85&s=f0064170474883a227040ac547867442" alt="Custom Google OAuth login screen" className="mx-auto" style={{ width:"100%" }} width="2548" height="1028" data-path="images/2025-10-29_12-51-25.png" />

<Note>
  **Before you begin:**

  * You must be on a Builder plan or higher to use custom Google OAuth.
  * To set up custom Google OAuth, you must have a [payment method connected to your project](https://cloud.google.com/billing/docs/how-to/payment-methods) in your Google Cloud Console.
</Note>

**To set up custom Google OAuth:**

1. [Connect a custom domain](https://docs.base44.com/Setting-up-your-app/Setting-up-your-custom-domain) to your app.
2. Go to [Google Cloud Console ](https://console.cloud.google.com/)and create a new project for your app.
3. Verify your domain [here](https://search.google.com/search-console/welcome?sjid=16943951970559052415-EU).
4. Set up your OAuth app by completing the following information:

   <img src="https://mintcdn.com/base44/9sHhqsCTbHswHd-n/images/googlecloud.png?fit=max&auto=format&n=9sHhqsCTbHswHd-n&q=85&s=7df96ef4c50f258c9692f241341caae6" alt="Setting up your OAuth app" width="1992" height="1102" data-path="images/googlecloud.png" />

   1. **Overview:** Enter your app information.
   2. **Branding:** Set up your app's branding ([learn more about branding](https://support.google.com/cloud/answer/13804963)):
      1. Add your logo. This must be similar to your app's logo.
      2. Create a home page in your app following [these guidelines](https://support.google.com/cloud/answer/13807376).
      3. Create a privacy policy linked from your home page following [these guidelines](https://support.google.com/cloud/answer/13806988).
      4. Add a support page to your app.
      5. Add your domain as an authorized domain.
   3. **Audience:** Choose if your app is for internal or external use.
   4. **Clients:** Get your Client ID and Secret:
      1. Click **Create client.**
      2. Enter the relevant details including the following:
      * **Authorized JavaScript origins:** Enter your app domain.
      * **Authorized redirect URIs:** Enter `https://app.base44.com/api/apps/auth/callback`

        <img src="https://mintcdn.com/base44/LjZOSZWi-0Bg7jzi/images/clientid.png?fit=max&auto=format&n=LjZOSZWi-0Bg7jzi&q=85&s=f7f223d2801d4de2cb29f985ef47fd31" alt="Entering Client details in Google Console" title="Entering Client details in Google Console" style={{ width:"100%" }} width="1966" height="1296" data-path="images/clientid.png" />
      3. Click **Create.**
   5. **Data Access:** Select the following scopes:

      * `openid`
      * `https://www.googleapis.com/auth/userinfo.email`

      <Warning>
        You must add a landing page to your app that includes your privacy policy and terms of service. These pages must be public and not behind a login. This is required for Google OAuth approval and lets your users see your legal information before signing in.
      </Warning>
5. Go back to Base44 and finish setting up your custom login:

   1. Click **Dashboard** in your app editor.
   2. Click **Settings**.
   3. Click **Authentication**.
   4. Enable the **Google authentication** toggle.
   5. Select **Use a custom OAuth from Google Console.**
   6. Enter the relevant information from your Google OAuth app and click **Update**.

   <img src="https://mintcdn.com/base44/dAdRCAX7btyUXjVa/images/2025-10-28_23-59-20.png?fit=max&auto=format&n=dAdRCAX7btyUXjVa&q=85&s=447a0efe62b0bb4fdcb61f7c3cfc9273" alt="Setting up custom Google OAuth in Base44" width="744" height="401" data-path="images/2025-10-28_23-59-20.png" />

   <Note>
     Once you have completed the steps above, you need to wait for Google to verify and approve which can take up to 5 days.
   </Note>

***

## Collecting data at sign-up

Personalize your app experience by collecting key details from your users when they sign up. You can prompt the chat to generate a custom sign-up form that gathers information beyond just an email and password (e.g. full name, company, or role) so you can onboard people smoothly and tailor their app experience from the start.

**Choose where to store the data:**

* **Users dataset:** Store data securely, viewable only by app admins. This is ideal for sensitive or admin-only details.
* **Connected dataset:** Store user responses in a separate public-facing dataset. This is recommended for data displayed or shared in-app (like company names).

***

## FAQs

Click a question below to learn more about authentication.

<AccordionGroup>
  <Accordion title="Why didn't my user receive a verification or password reset email?">
    If people do not receive verification or password reset emails, start with these checks:

    * Ask them to check their spam or junk folders in case the email was filtered.
    * Let them know it can take a few minutes for some email providers to deliver the message.
    * Ask them to add [app@base44.com](mailto:app@base44.com) to their safe senders or allowlist so future emails are not blocked.
    * During sign up, encourage them to enter their email address in lowercase and to check for typos.

    If they still do not receive the email, ask them to click the resend link from your app.

    If that does not work, remove their record from the Users list in your dashboard and ask them to sign up again with the same email address.

    If several people report the same issue at the same time, or if resend and re-signup do not solve it, contact Base44 support with your app URL and the affected email addresses so we can check for any deliverability or platform issues.
  </Accordion>

  <Accordion title="Why do people see an error when they try to log in with Facebook?">
    This usually happens when the person's Facebook account is not fully verified. Facebook can block the login until they confirm their identity and verify the email on their account.

    Ask them to:

    1. Open Facebook and go to **Settings and privacy**.
    2. Go to **Accounts Center**.
    3. Go to **Verification** and then **Identity confirmation**.
    4. Complete the identity confirmation steps.

    After they finish Facebook's verification flow, they can try logging in to your app again with Facebook. Facebook controls this requirement, not Base44, so you cannot bypass it from your app settings.
  </Accordion>

  <Accordion title="How do I show a public landing page but require login for other pages?">
    It's not possible to make some pages in your app public and keep others private. We know this is a common request, and we’re actively working on adding it. You can follow progress (and add your voice) here: [**<u>Hybrid Apps – Authentication Support</u>**](https://feedback.base44.com/p/hybrid-apps-authentication-support) .

    As a workaround, to set up your Base44 app so that everyone can visit your landing page while requiring users to log in for other pages, follow these steps:

    1. **Set your app to Public (no login required):**\
       In your **Dashboard**, go to **Settings** → **App Settings**. Set **App Visibility** to Public (no login required). This allows anyone to see your landing page.
    2. **Create your landing page with login and sign-up buttons:**\
       Prompt the AI to “create a landing page with login and sign-up buttons.” Make sure this is your app’s main page by selecting it under “Main Page” in your settings.
    3. **Require login for other pages:**\
       Ask the AI to require login on all other pages and redirect visitors who aren’t logged in back to your landing page.

    With this setup, all visitors see your landing page first. Only users who have logged in or signed up can view the rest of your app’s pages.
  </Accordion>

  <Accordion title="How are passwords managed and what happens if someone forgets theirs?">
    Base44 automatically handles all passwords securely behind the scenes. If someone forgets their password, they can reset it directly from the login screen by clicking **Forgot password?**.

        <img src="https://mintcdn.com/base44/70bAE-4HKlQWJyVs/images/PasswordManagement.png?fit=max&auto=format&n=70bAE-4HKlQWJyVs&q=85&s=43f88606cb8c1badf7404e3f25a12e55" alt="Use login sceen with Forgot password option to reset it." width="1713" height="813" data-path="images/PasswordManagement.png" />
  </Accordion>

  <Accordion title="Can I add a logout option for my users?">
    Yes. Adding a logout option keeps things secure and gives users peace of mind. You can prompt the chat to include a **Logout button** and place it in the sidebar or app header, wherever it best fits your design.

        <img src="https://mintcdn.com/base44/CJeh3u8yWYgfl23o/images/LogoutButton.png?fit=max&auto=format&n=CJeh3u8yWYgfl23o&q=85&s=66c92f89bacf212a1c209e4354097460" alt="Prompting the chat for a logout button." width="1749" height="870" data-path="images/LogoutButton.png" />
  </Accordion>

  <Accordion title="Can I create a custom authentication flow from scratch in Base44? ">
    No, Base44 does not currently support creating a fully custom authentication flow from scratch. This means you cannot build your own authentication pages, change the design or language of the built-in auth screens, or fully white label the authentication process. Authentication is managed by the platform to keep your app secure and consistent.

    Features like white labeling are planned for the future, but are not available yet. Check out the [**feature request**](https://feedback.base44.com/p/better-white-label-experience-for-applications) for more information.
  </Accordion>

  <Accordion title="Does Base44 support external authentication providers like Kakao? ">
    Yes. Base44 supports external authentication providers that use OpenID Connect (OIDC), including providers such as Kakao.

    If you are on the Elite plan, you can connect external providers such as Google, Microsoft, GitHub, Okta, or Kakao using Single sign-on (SSO) and the Advanced / Manual configuration option. You need your own account with the identity provider, and you are responsible for creating and managing the app, client ID, client secret, redirect URI, and any other credentials in that provider.

    For step-by-step instructions, see the guide on [setting up SSO](https://docs.base44.com/Setting-up-your-app/Setting-up-SSO) in Base44.

        <img src="https://mintcdn.com/base44/MdbM17mdo5Ofrrmp/Advancedconfiguration.png?fit=max&auto=format&n=MdbM17mdo5Ofrrmp&q=85&s=f6885e7eec42fba949d662b1eee9e8e2" alt="Advancedconfiguration Pn" width="779" height="554" data-path="Advancedconfiguration.png" />
  </Accordion>

  <Accordion title="Can I customize the login screen?">
    Currently, you cannot customize the design and styling  of your login page.
  </Accordion>

  <Accordion title="Why am I getting an error when I use User.login() in the Base44 SDK? What should I use instead?">
    The Base44 SDK does not support `User.login()`, so if you try to use it in your code, you will see an error.

    To log users in, always use `base44.auth.redirectToLogin(nextUrl)`. This method sends the user to the login page and brings them back to your site after they sign in.

    If you are having issues with authentication, check that you are using this correct method in your app.

    **Incorrect (will cause an error):**

    ```js  theme={null}
    User.login(nextUrl);
    ```

    **Correct:**

    ```js  theme={null}
    base44.auth.redirectToLogin(nextUrl);
    ```

    **Tip:** If you see an error like "TypeError: User.login is not a function", check your imports and ensure you are using `base44.auth.redirectToLogin` instead.
  </Accordion>

  <Accordion title="Can I preview the signup form on my app?">
    No. You cannot use or test your app’s signup, login, or logout flows inside the app preview window. Authentication features are only fully available on the live app.

    **To test your signup and login flows:**

    1. Publish your app.
    2. Open your app’s live URL in a browser.
    3. Go to the signup or login page.
    4. Complete the flow with a relevant, valid email address.

    This way you see the same experience that people will have when they sign up or log in to your app on the live site.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).