# Source: https://docs.base44.com/Community-and-support/Troubleshooting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Issues

> Get help with common issues in Base44 so you can keep working without interruptions. Find quick solutions for publishing, domain problems, and more.

Sometimes things do not go as planned, but you can quickly fix most problems and get back on track. Use this guide to troubleshoot common issues with publishing, login, chat, and other key features.

<Tip>
  **Quick troubleshooting tips:**

  * If something in your app is not working as expected and you do not see a clear error, type 'Something is wrong' in the AI chat. Base44 analyzes what is happening in your app, surfaces possible issues, and suggests fixes directly in context so you can resolve problems faster before trying manual troubleshooting steps.
  * Check the [Base44 status page](https://status.base44.com/) to see if there are system-wide problems.
</Tip>

***

## Editor and Dashboard

<AccordionGroup>
  <Accordion title="Unable to access the landing page of my app">
    You cannot access your app's landing page because of how Base44 manages privacy settings for apps with both public and private areas.

    By default, Base44 requires every app to set one privacy level for all its pages. If your app's privacy is set to "Private (Login Required)," all pages, including the landing page, will require a login. At this time, Base44 does not support making one page public (like a landing page) while the rest of the app stays private.

    To fix it, you need to make your app public so everyone can access your landing page.

    1. Go to your app's dashboard.
    2. Click **Overview**.
    3. Under **App Visibility**, select **Public**.

    **If your app needs both public and private areas, follow this workaround:**

    1. Create a separate app for your public landing page.
    2. Publish both apps.
    3. Link this landing app to your main, private app.
    4. Assign your primary domain to the landing page app, and a subdomain to your private app.

    <Tip>
      Tip: Try viewing in an incognito window to check access without being logged in.
    </Tip>

    **Alternative workaround:**\
    If you want a single app with both a public landing page and private content, you can set up row-level security (RLS) to block all pages except your landing page.

    * Ask the AI to create a public landing page, set it as default for all users.
    * Lock all other pages behind RLS (so only logged-in users can see them).
    * Configure redirects: Anyone logged out is sent to landing, logged-in users are sent to dashboard.
    * Prompt suggestion:\
      “Please implement a landing page for our app that allows users to login/signup at /Login utilizing our existing theme. Make sure all pages except the landing page are secured behind RLS and that logged-in users can't access the landing page but are redirected to the dashboard.”

    For more on privacy settings, see the [Authentication](/Setting-up-your-app/Managing-login-and-registration) guide.
  </Accordion>

  <Accordion title="The screen is white when I click on something in my app">
    If you see a white screen in the editor, this usually points to a technical problem that needs further review.

    **Here are some steps you can try:**

    1. Click the **Revert** icon on a chat message to restore your app to a previous working version.
    2. Open the Version History (the clock icon in AI chat) and roll back to an older version where clicking on something did not cause a white screen.
    3. Try describing your problem to AI chat with more specific details, such as exactly where, when, and how the issue appears.

    If these steps do not resolve the problem, this might be a bug in your app's code or configuration. In this case, submit a support ticket with detailed information about what triggers the white screen, which device/browser you are using, and any screenshots or error messages you see. This will help the Base44 team investigate and resolve the issue.
  </Accordion>

  <Accordion title="Error message: &#x22;Failed to load app: Error serializing to JSON: UnicodeEncodeError&#x22;">
    This error can happen if your app name contains an emoji or a special character that is not supported. When this error occurs, you will not be able to open the app editor or rename your app.

    If you encounter this issue, contact Base44 support so the team can help escalate your case.
  </Accordion>

  <Accordion title="App editor won't load or is slow">
    When you try to open the Base44 app editor, you might see a blank screen, get stuck on the loading icon, or notice that everything is running slowly or unresponsive. This can happen for several reasons related to your browser, internet connection, or temporary platform issues.

    **Try these steps:**

    1. Check that you're using an up-to-date, supported browser.
    2. Clear your browser cache and Base44 cookies.
    3. Turn off browser extensions, especially ad blockers or privacy tools.
    4. Open the editor in an incognito window or try a different browser.
    5. Check the Discord [community](https://discord.com/invite/ThpYPZpVts) for any reported outages.
    6. If the editor still isn't working, take a screenshot of any errors (especially from your browser's console), and [contact Base44 support](/Community-and-support/Contacting-support) with your browser and operating system details.
  </Accordion>

  <Accordion title="Can't see my published changes live">
    Sometimes after publishing your app, updates such as new content, design changes, or bug fixes don't appear on your live site. This can be caused by caching, deployment issues, or missed steps in the publishing process.

    **Try these steps:**

    1. Clear your browser and device cache, then reload your app.
    2. Double-check your app from a different browser or device.
    3. Make sure you clicked **Publish** and saw a “success” message.
    4. If you updated a backend function, redeploy it from the dashboard.
    5. Look for any error logs in your Base44 dashboard.
    6. If nothing works, include your app link and details about what's missing when you [contact Base44 support](/Community-and-support/Contacting-support).
  </Accordion>

  <Accordion title="Blank screens and JSON schema errors after publishing">
    If you see a blank screen after publishing your app, or get an error such as “**Uncaught Error: Error in json schema: properties is required for object type**,” there is usually a mismatch between your field definitions and the data being saved.

    For example, if you use a flexible object or a custom input (like `meal_preferences`), make sure the input type and value type match your schema. Any mismatch can cause your app to load incorrectly or display a blank screen.

    Check your JSON schema and make sure your field types and the data being stored are aligned. If you need  to insert a flexible object, only use JsonSchemaForm if the properties are clearly defined in advance.

    > **Tip:** If your app code and settings look correct in the editor but your live app still shows blank screens or missing updates, double-check your field schemas and saved data. Hidden schema mismatches are a common cause.
  </Accordion>
</AccordionGroup>

***

## AI Chat

<AccordionGroup>
  <Accordion title="Using too many credits when chatting with the AI">
    If you notice your credits are being used up faster than expected, it may be because you are chatting with the AI in regular mode instead of **Discuss** mode. When you work with the AI in regular mode, each interaction spends more credits. Discuss mode helps save credits by letting you plan and review steps without triggering costly AI actions.

    **To save credits while chatting with the AI:**

    1. Click **Discuss** in the AI chat window before you start chatting. The **Discuss** button should be highlighted.
    2. Plan, ask questions, and talk through your ideas with the AI.
    3. When you are finished discussing and ready for the AI to take action or build something, click **Discuss** again to turn it off. The **Discuss** button will no longer be highlighted, and then you can ask the AI to implement your changes.

    <img src="https://mintcdn.com/base44/wBpevXyc0D3u_kIU/images/2025-09-14_14-27-32.png?fit=max&auto=format&n=wBpevXyc0D3u_kIU&q=85&s=90d1386eba858486d62af775cb80b2c6" alt="2025 09 14 14 27 32 Pn" title="2025 09 14 14 27 32 Pn" className="mx-auto" style={{ width:"63%" }} width="960" height="1218" data-path="images/2025-09-14_14-27-32.png" />

    <Tip>
      **Tip:** Always use **Discuss** mode for planning and brainstorming. Turn it off only when you want the AI to perform actions, generate outputs, or make changes. The **Discuss** mode only uses 0.3 credits per request.
    </Tip>

    For more information about how credits work and the best ways to manage them, [learn more about your credits](/Account-and-billing/Credits).
  </Accordion>

  <Accordion title="The AI is not fixing my issue">
    This can happen when you describe a problem in general terms, and the AI starts guessing where the issue is.

    Try this workflow when you want to explain a specific bug, for example, a button that does nothing, a form that will not submit, or a feature that behaves unexpectedly.

    **Point the AI to the exact element (Visual Edit + Discuss):**

    1. Click **Visual Edit** and **Discuss** in the AI chat.
    2. Click the element in your app preview that you want to work on, for example, a button, form, input, or table row.
    3. Click **Discuss** on the element to open a focused chat linked to that component.
    4. In the AI chat, explain what is happening and what should happen.

    <img src="https://mintcdn.com/base44/-LM4zq7EW2h5nXcQ/images/visualdiscusselement.png?fit=max&auto=format&n=-LM4zq7EW2h5nXcQ&q=85&s=bf48f224e196f246cd7451997fa688b0" alt="AI chat with Visual Edit and Discuss enabled and an element selected." title="AI chat with Visual Edit and Discuss enabled and an element selected." className="mx-auto" width="1027" height="160" data-path="images/visualdiscusselement.png" />

    <Tip>
      Include the expected outcome. This helps the AI understand the current logic and what you want it to do.

      **Examples:**

      * This button does not react when clicked, check its `onClick` handler.
      * After clicking this button, a PDF should download, but currently nothing happens.
      * This button should take me to the Orders page, but I stay on the same screen.
    </Tip>
  </Accordion>

  <Accordion title="The AI chat isn't responding">
    Sometimes the AI chat panel may fail to load, get stuck processing, or not respond at all. This can happen if your prompt is too long or complex, due to browser or network issues, or temporarily from system updates.

    **Try these steps:**

    1. Click the **Revert** icon on a chat message, or go back to the last version of your app that was working correctly. This can reset the AI's state and often resolves the issue.
    2. Click the **Stop** button on the chat if it is stuck in a state such as 'thinking', 'applying changes', or 'undoing'.
    3. If your AI request is very long or complex, split it into smaller, more manageable parts. This helps the AI process your instructions accurately.
    4. Refresh your browser and check your internet connection
    5. Clear your browser cache and turn off browser extensions that could block scripts
    6. Open your app in a private or incognito window
    7. If it's still not working, check [Discord](https://discord.com/invite/ThpYPZpVts) for reported issues.

       <Note>
         If the chat processing state lasts longer than 10 minutes or does not provide updates, click the **Stop** button and let the support team know, including the following details:

         * Where the AI got stuck (location or function in the app)
         * The prompt or action you were performing
         * How long the processing state lasted
       </Note>
  </Accordion>

  <Accordion title="Error: 'dict' object has no attribute 'lower'">
    You may see the error **'dict' object has no attribute 'lower'** when using the chat prompt or trying to send a message. This usually happens when the chat expects text but receives an unexpected object, often due to a temporary glitch.

    **To resolve this error:**

    1. Revert your last message, as suggested by the error.
    2. Refresh the page fully:
       * On Windows or Linux, press **Ctrl + Shift + R** or **Ctrl + F5**.
       * On Mac, press **Cmd + Shift + R**.
    3. Try clearing the chat section and start a new prompt.
    4. If the error continues, contact support and include details about your prompt and the error.
  </Accordion>

  <Accordion title="AI chat is stuck on &#x22;Thinking...&#x22; after my first prompt to create the app">
    If AI chat stays on "Thinking..." after your first prompt and the app does not progress, try these steps.

    **Often, the app has been partially created. Try cloning the app:**

    1. Go to your app **Dashboard**.
    2. Go to **Settings** and then **App settings**.
    3. Click **Clone app**.
    4. Open the cloned app.

    **If cloning does not help, create a new app:**

    1. Copy your original prompt text.
    2. Create a new app.
    3. Paste the same prompt into the AI chat and run it again.

    <Tip>
      **Tips to prevent this:**

      * For complex prompts, break your request into smaller, sequential prompts.
      * Very long first prompts with many details can cause the chat to get stuck.
      * Complex first prompts can sometimes take 10 to 15 minutes to complete. If nothing changes after that time, try one of the steps above.
    </Tip>
  </Accordion>
</AccordionGroup>

***

## Data and Security

<AccordionGroup>
  <Accordion title="Row-level security (RLS) is not restricting data access correctly">
    Row-level security (RLS) rules control which users can access specific data in your app. If unauthorized users can see or edit data, or RLS rules are not working as expected, use the built-in security check to find and fix issues.

    **To troubleshoot RLS problems:**

    1. Go to your app's dashboard and click **Security**.
    2. Click **Start security check** to scan for missing or misconfigured RLS rules.
    3. Review the issues found and click **Apply Fixes** to use the recommended safe defaults, or adjust rules for each data entity manually.
    4. Sign in with different user roles to confirm only authorized people can access each type of data.

    For more details on setting up and managing security rules, see the [**guide to managing security settings**](https://docs.base44.com/Setting-up-your-app/Managing-security-settings).
  </Accordion>
</AccordionGroup>

***

## Performance and Speed

<AccordionGroup>
  <Accordion title="Error 500 appears when loading, saving, or using your app">
    You may see a “500 Internal Server Error” message while loading your app, saving data, accessing pages, or using platform features like forms or dashboards. This can lead to blank screens, missing data, lost progress, or features not working.

    This issue is usually caused by a problem on the Base44 backend or with the platform configuration, such as an invalid App ID, server outages, deployment issues, API problems, or overloaded resources. It can affect both published and development versions of your app.

    A 500 error means something went wrong on the server side, and you usually cannot fix it yourself.

    **What you should do:**

    1. Refresh the page or try again later, as some 500 errors are temporary.
    2. Check the status page or [Discord channels](https://discord.com/channels/1303811506080841758) to see if there is a known platform incident.

    If the problem continues, contact Base44 support. Include the following details:

    * Your app name
    * Where and when the error happens
    * Any error messages from the console (screenshots if possible)
    * What steps led to the problem
  </Accordion>

  <Accordion title="App does not load or shows a blank/white screen">
    Sometimes, an app fails to load and only displays a blank screen, loading spinner, or basic header. You might see this after making edits, trying to preview your app, or after publishing. The issue can occur on both web and mobile devices and can include issues such as:

    * The app loads briefly, then disappears.
    * Clicking the app link shows nothing but a white page or loading wheel.
    * Some pages, tabs, or features remain frozen and unresponsive.
    * The app crashes when clicking buttons or making selections.
    * Nothing appears when trying to access the dashboard, preview, or key pages.

    Most loading issues are caused by a problem in your app's code or a temporary platform issue.

    **Try the following steps:**

    1. Refresh the page or open the app in a new browser window.
    2. Clear your browser cache and cookies, then try loading again.
    3. Make sure your internet connection is stable.
    4. Switch browsers or devices to see if the issue persists elsewhere.
    5. If you made recent edits before the issue started, try reverting your most recent changes if possible.
    6. Wait a few minutes. Sometimes the platform is updating or experiencing temporary downtime.

    **If your app still won't load, contact Base44 support and provide:**

    * A description of what you see (e.g. blank page/spinner)
    * When the issue began and any recent edits you made
    * The app name or link
    * Any error messages shown in your browser console (if possible)

    The support team will investigate and work with you to restore your app.

    <Tip>
      If you're stuck in an infinite loading state after using all your credits or after a large edit, mention this in your message.
    </Tip>
  </Accordion>

  <Accordion title="My prompt or stop button is stuck and I can't revert">
    If your prompt keeps running and the stop button does nothing, try these steps:

    1. Use Version History to quickly revert your app to before the stuck prompt. This is the fastest way to get back to a previous state.
    2. Change the LLM in your app settings, switch to Discuss mode, and send any prompt (for example, "hi") to break the stuck state.
    3. Use Visual Edit mode to make a small change—such as adding an extra space or updating text—to force a state change.
    4. If possible, open your app on a mobile device, enable Discuss mode, and send a prompt.
  </Accordion>

  <Accordion title="Everything is broken and reverting in chat does nothing">
    If your app is broken but asking the AI to revert in chat does not work:

    1. Every prompt in your chat history has a **Revert** button. Click this to roll your app back to just before that change.
    2. Rolling back your app by “asking” the AI in chat never actually undoes prompt changes—only the **Revert** button or Version History will fix it.
    3. If the **Revert** button does not work, use **Version History** (usually found near the dashboard or preview). This lets you restore to an earlier app version.
    4. If both **Revert** and Version History do not work, contact Base44 support for further help.
  </Accordion>

  <Accordion title="Tailwind CDN script is injected by the platform and cannot be removed">
    If you see any warnings in your browser or development tools about the Tailwind CDN script (such as “cdn.tailwindcss.com should not be used in production”), there's no need to worry. The Tailwind CDN script is added automatically by the Base44 platform and is required for your app's styling. This script cannot be removed or disabled at this time.

    The warning does not affect your app's functionality or security. The script ensures consistent styling and a stable experience across all Base44 apps.

    Base44 is working on a solution for this in the near future. For now, please keep the script as part of your app setup.
  </Accordion>
</AccordionGroup>

***

## Apps and Integrations

<AccordionGroup>
  <Accordion title="Backend functions are returning 404 errors at public URLs">
    Backend functions are designed to handle POST requests and are not accessible in a browser. If you visit a backend function URL in your browser, you will always see an error. However, if all your backend functions return 404 Not Found errors, especially when using the dashboard test tool or in your external integrations, this is a critical issue. It usually points to a problem with your app’s routing or deployment, not your code or configuration.

    Follow the steps below to test your backend function using the dashboard, and then proceed to the troubleshooting steps.

    <AccordionGroup>
      <Accordion title="Step 1 | Test your backend function">
        1. Click **Dashboard** in your app editor.
        2. Click **Code**.
        3. Click **Functions**.
        4. Select the relevant function.
        5. Click **Test Function** at the bottom right.
        6. (Optional) Copy the function URL from the top right sidebar for use in integrations.

        * **If the test passes:** Your backend function is working. Errors from visiting the URL in a browser are normal.
        * **If the test returns a 404 error** **or none of your integrations are working**: Continue with the troubleshooting steps below.
      </Accordion>

      <Accordion title="Step 2 | Troubleshooting persistent 404 errors">
        1. **Confirm your plan supports backend functions:** Make sure you are on the Builder plan or higher.
        2. **Verify file locations and naming:**
           * Make sure your function files (e.g. ebayAuth) are in the correct directory.
           * Check file and function names for typos.
           * Each file should export the function using `Deno.serve()`.
        3. **Redeploy your app:** Redeploy from the dashboard to trigger a fresh deployment and update app routing.
        4. **Review recent build and deployment:** If your app was recently updated, check that all build and deployment steps completed successfully.
      </Accordion>
    </AccordionGroup>

    If the problem continues after these checks, this is likely a platform-level routing or deployment issue rather than something wrong with your app setup. Contact Base44 support and include:

    * The link to your app
    * A list of affected backend function names (for example, ebayAuth)
    * Screenshots showing the 404 errors at each endpoint
    * When the issue started, such as after a deploy, migration, or platform update

    <Tip>
      Tip: Mentioning when the issue began helps the support team troubleshoot the problem faster.
    </Tip>
  </Accordion>

  <Accordion title="Base44 unable to fetch API key">
    For security reasons, external services like Stripe, OpenAI, or Notion don’t let third parties (even Base44) access your credentials automatically. API keys are like passwords for services. Keeping them private and user-controlled keeps your data safe and ensures only *you* authorize access.

    **Instead, you need to:**

    1. Log in to the service.
    2. Go to the API or developer section.
    3. Generate your key.
    4. Paste it into Base44 as a *Secret.*

    Once added, your app can use that key behind the scenes safely, and without code.
  </Accordion>

  <Accordion title="Error when opening backend function URL in browser">
    Backend functions in Base44 now support both GET and POST requests. You can use either method to call your backend functions, depending on your use case.

    * **GET requests** let you pass data in the query string of the URL.
    * **POST requests** allow you to send data securely in the request body.

    If you see an error when opening a backend function URL in your browser, check that your request is formatted correctly for either GET or POST. Make sure to pass any required data using the appropriate method so your backend function receives it as expected.
  </Accordion>

  <Accordion title="500 error when making a POST request to webhook function">
    A 500 error usually means the URL for your webhook POST request is incorrect. Make sure you are using your app’s default Base44 app link as the base URL in your function endpoint.

    For example: `https://app--your-app-name.base44.app/api/apps/your-app-id/functions/yourFunctionName`

    If you have a custom domain connected, it is still recommended to use the default app link for POST requests to ensure proper routing and fewer errors. Double-check the structure of your URL and update your integration as needed.
  </Accordion>

  <Accordion title="Error ISOLATE_INTERNAL_FAILURE in backend functions">
    You might see the `ISOLATE_INTERNAL_FAILURE` error when you try to save or deploy a backend function. This usually means that one of the files in your `/functions` folder does not follow the platform requirements and cannot start in Base44’s Deno environment.

    **Common causes:**

    1. **Missing Deno.serve entrypoint:** Each function file in the `/functions` folder must use `Deno.serve()` as the entrypoint. For example: `Deno.serve((request) => { ... })`
    2. **Utility files or empty files in** `/functions:` Utility modules or completely empty files inside the `/functions` folder can trigger this error, even if they are not meant to be real endpoints. Helper files should be moved out of `/functions` or excluded from deployment.
    3. **Invalid imports:** Backend functions must be self contained. Keep only imports from supported npm packages. Do not import:

    * Frontend components
    * Shared project utilities from other folders
    * Other backend functions directly

    4. **Unsupported APIs:** The Deno runtime does not support some Node.js built ins or browser only APIs. Remove or replace things like:

    * Node.js modules such as `fs`, `path`, `process`, `crypto`
    * DOM or window based browser APIs

    **How to fix ISOLATE\_INTERNAL\_FAILURE errors:**

    1. **Check the entrypoint:** Make sure every file in `/functions` that is deployed as a backend function defines a `Deno.serve()` block as its entrypoint.
    2. **Clean up the** `/functions`**folder**
       * Remove or move out any empty files or pure utility modules that should not be deployed as functions.
       * Make sure only actual function files live in `/functions`.
    3. **Fix imports and APIs**
       * Remove local imports of frontend components, shared utilities, or other backend functions.
       * Replace unsupported Node.js or browser specific APIs with supported alternatives.
       * Keep only imports from supported npm packages.
    4. **Save and publish:** Save your changes and publish your app so the backend functions can be rebuilt and deployed.
    5. **Ask the Base44 AI to refactor the function:** If you still see the error, copy the function code into the Base44 AI chat and say something like: “This backend function returns ISOLATE\_INTERNAL\_FAILURE. Make it self contained and compatible with Deno.serve without changing what it does.” 

       The AI can help rewrite the function so it follows the correct Deno patterns while keeping your logic the same.
  </Accordion>

  <Accordion title="App link does not open in other browsers">
    If your app opens for you but not when you paste the link into a different browser or device, it is usually related to publishing, domain setup, or app visibility.

    **To check that your app is published:**

    1. Go to your app dashboard.
    2. Click **Publish** in the top right.
    3. Select **Publish app** if the app is not already published. 

    **To check your app visibility:**

    1. In your app dashboard, click **Overview**. 
    2. Under **App visibility**, select **Public (No login required)** or **Public (Login required)**, depending on who should access your app.
    3. If the app is set to **Private (Base44 login required)**, only email addresses you explicitly invite can open the link.

    **To check your domain configuration:**

    1. If you use a custom domain instead of the default Base44 app URL, make sure the domain is connected and verified in your Base44 settings.
    2. Try opening the default Base44 app URL directly to confirm that the app itself loads as expected.

    <Note>
      If your app link still does not open after these checks, contact support with the exact app URL, whether the app is published, and whether you are using a custom domain. This helps the team investigate more quickly.
    </Note>
  </Accordion>
</AccordionGroup>

***

## Domains

<AccordionGroup>
  <Accordion title="Domain is stuck in 'Pending'">
    When your domain is stuck on "pending" after updating DNS to add it to Base44, this usually means there's an issue with your DNS configuration or propagation.

    First, check that your nameservers are set up correctly. Read our [guide on domains](https://docs.base44.com/Setting-up-your-app/Setting-up-your-custom-domain) to check this. If you are still having issues, follow the steps below.

    **Troubleshooting steps:**

    1. Remove any AAAA (IPv6) records for your domain, as these can interfere with proper setup.
    2. Wait 48-72 hours for changes to fully propagate across the internet.
    3. Use a tool like [whatsmydns.net](http://whatsmydns.net) to confirm your updated records are visible globally.
    4. Double-check that you entered the exact record values.
    5. If the status is still pending after about 30 minutes, try unlinking the domain in Base44, then re-adding it.

    **If your domain still does not connect, contact support with:**

    * A screenshot of your DNS records
    * Your domain name
    * Your Base44 app link
  </Accordion>

  <Accordion title="Domain from Base44 is not connecting">
    If you purchased your domain in Base44, you need to verify it first. If you skip this step, your domain will not connect.

    You need to confirm your domain ownership by verifying your email address with IONOS.\
    Check your inbox for an email from [support@ionos.com](mailto:support@ionos.com) with the subject "Please Confirm the Contact Details for Your Domain." Open this email and click the "Confirm Email Address" button within 14 days. This step is required by ICANN to keep your domain active and ensure your contact details are valid.

    If you do not confirm your email address within 14 days, your domain may be deactivated according to ICANN's requirements. If you cannot find the email, check your spam or junk folders. If the email or link has expired, contact IONOS support to request a new confirmation email.

    **Here's what you need to do:**

    1. Open the IONOS email and click the link to confirm your email address.
    2. In Base44, go to your app's Dashboard and click **Domains**, select the domain, and click **Unlink domain**.
    3. Connect the domain again.
    4. Wait a few minutes for the connection to complete.
  </Accordion>

  <Accordion title="Domain is stuck in 'Connecting'">
    If your domain is stuck in 'Connecting' status for longer than 30 minutes, go to your app's dashboard and click **Domains**, then unlink and link the domain again.
  </Accordion>

  <Accordion title="Domain is connected but it is not working and the site is not loading">
    Run through this checklist to set that it is set up correctly:

    * Make sure DNS records match exactly what's shown in this guide for your setup type.
    * Remove any **AAAA (IPv6)** records, as they can block connections.
    * Double-check for typos. Be sure to copy and paste values exactly from this guide.
    * Ensure both www and the root domain are set up correctly.
    * Confirm your domain is renewed and active.
    * Wait up to 72 hours for changes to take effect.

    **Advanced troubleshooting:**

    * Double check CNAME and ANAME/ALIAS record requirements:
      * www → [base44.onrender.com](http://base44.onrender.com) (CNAME)
      * root / @ → [base44.onrender.com](http://base44.onrender.com) (ANAME/ALIAS or A record if ANAME/ALIAS is not supported)
      * If using A record, set @ → 216.24.57.1
    * Remove any AAAA records. Base44 only supports IPv4 and AAAA records can break domain resolution.
    * For IONOS domains, try unlinking and relinking the domain to resolve most issues.
    * If you tried these steps and are still seeing problems after full DNS propagation, contact support.

    <Tip>
      **Tip:** If your domain uses a DNS manager like Cloudflare, update the records there instead of at your registrar. During setup or troubleshooting, set Base44 related records to **DNS only** (grey cloud) so Cloudflare only answers DNS and does not proxy traffic. This does not turn off SSL in Base44. It just removes an extra proxy layer while you fix the connection.
    </Tip>
  </Accordion>

  <Accordion title="SSL setup issues or ERR_SSL_PROTOCOL_ERROR after connecting a custom domain">
    If you encounter SSL errors or an ERR\_SSL\_PROTOCOL\_ERROR after connecting your custom domain to Base44, follow these steps to resolve the issue:

    * Check that your domain's DNS records match exactly what is shown in your Base44 dashboard.
    * Remove any AAAA (IPv6) records from your DNS settings, as these can block secure connections.
    * Carefully check for typos or missing values in your DNS entries.
    * Make sure both your www and root domain point to the correct Base44 IP addresses or CNAME.
    * Verify that your domain registration is active and has been confirmed.
    * Allow up to 72 hours for DNS and SSL changes to fully propagate worldwide.
    * If you use a DNS service like Cloudflare, update your records directly within that service and set Base44 related records to **DNS only** (grey cloud) while you set up or troubleshoot.

    **If you still see SSL errors after completing these steps, submit a support ticket and include:**

    * A screenshot of your current DNS records
    * Your domain name
    * A link to your Base44 app
  </Accordion>

  <Accordion title="Unable to connect a domain to a new app after deleting the previous app">
    If you’ve deleted an app and are trying to connect the domain to a new app, you might see an error saying the domain already exists. This can happen if the domain is still registered in our system, even after the old app is removed.

    You won't be able to fix this on your own right now. Please contact our support team for help on this.
  </Accordion>

  <Accordion title="Did not receive the domain verification email after purchasing a domain from Base44">
    After purchasing a domain from us, you need to verify your contact information to activate it. If you have not received a verification email from IONOS (the domain registrar), your domain may not connect or work as expected. This can prevent your website from going live.

    **To resolve this issue:**

    1. Check your inbox, spam, and junk folders for an email from IONOS.
    2. If you cannot find the email, contact IONOS (the domain registrar) and request a new verification email.
    3. When you contact IONOS, provide your domain name and explain that you have not received the verification email after purchasing your domain.
    4. Follow the steps from IONOS to complete your domain verification.
  </Accordion>

  <Accordion title="429 error when reconnecting domain">
    A 429 error usually appears due to a temporary limit on the Base44 side. This issue resolves itself automatically. \
    \
    Wait a few minutes before trying to reconnect your domain. If the problem continues after waiting, try again later.
  </Accordion>

  <Accordion title="Public DNS tools show an extra A record that I cannot see in my registrar's DNS">
    When you look up your domain in public DNS tools (such as Google Dig or Whatsmydns), you might see an extra A record pointing to an IP address you do not recognize. However, when you check your registrar's DNS zone, that A record is not listed. This usually happens because domain forwarding, URL redirect, or parking is enabled at the registrar, which silently creates an A record in the background and can interfere with connecting your domain or generating SSL.

    **To fix this issue:**

    1. Open a public DNS lookup tool and look up your domain's A records.
    2. Compare the IPs you see there with the A records in your registrar's DNS zone and confirm that one IP appears only in the public tool.
    3. Sign in to your domain registrar account and open the management page for your domain.
    4. Look for sections named Domain forwarding, URL redirect, Web forwarding, or Parking.
    5. If any forwarding, redirect, or parking option is turned on for your domain, turn it off or delete it, then save your changes.
    6. If you are not sure where the extra IP comes from, copy the IP address from the DNS tool and run a WHOIS lookup on it.
    7. If the IP belongs to your registrar (such as GoDaddy or Namecheap), it is almost certainly a default parking or forwarding page. Make sure all forwarding and parking features are fully disabled for this domain.
    8. Wait for DNS changes to propagate and then check your domain connection or SSL status again.
  </Accordion>
</AccordionGroup>

<Info>
  If you are still having problems with your domain, contact [**Base44 support**](https://app.base44.com/support/conversations) and include:

  * A screenshot of your DNS records
  * Your domain name
  * A link to your Base44 app
</Info>

***

## Content and Media

<AccordionGroup>
  <Accordion title="Unable to upload videos to the AI chat">
    Uploading videos to the AI chat is not supported. Instead, you can link to videos hosted elsewhere (such as YouTube, Vimeo, Loom). If you would like this feature let us know on our [Feedback board](https://feedback.base44.com/).
  </Accordion>

  <Accordion title="Error message: Invalid MIME type. Only image types are supported">
    This error appears when you try to upload a file format that is not supported by Base44 AI chat modes. You can only upload specific image types or document formats, and uploading an unsupported file triggers this message.

    **To fix the issue:**

    1. Check that your file is one of the supported formats.
    2. Make sure your file does not exceed the size limits set by Base44.
    3. If you accidentally uploaded a wrong file, click **Revert** on the message to undo the last prompt.
    4. Try uploading your file again using a supported format.

    For more details on supported files, see the [Media guide](https://docs.base44.com/Building-your-app/Using-media).
  </Accordion>

  <Accordion title="Error message: Image does not match the provided media type">
    This error appears if you upload an image where the file's actual format does not match its file extension or what Base44 expected. This often happens if you rename a file from another format (for example, from .webp to .png) without converting it properly, or if the image was saved in a different format than its extension indicates.

    **To resolve this error:**

    1. Revert your last message, especially if the image upload was in your previous step.
    2. Open the file in an image editor and re-save or export it in a supported format (PNG, JPG, or JPEG) instead of just renaming the file extension.
    3. Check that your file meets the [limits for AI chat](https://docs.base44.com/Building-your-app/Using-media#uploading-media-to-the-ai-chat):
    4. Try uploading the newly exported image again using a supported format.

    <Tip>
      Always use images exported or saved as PNG, JPG, or JPEG from an image editor. Renaming a file's extension does not convert it to a proper format and may cause upload errors.
    </Tip>
  </Accordion>
</AccordionGroup>

***

## Error Codes

<AccordionGroup>
  <Accordion title="200 - Things are working as expected">
    The action you tried completed successfully. You usually will not see this code in the Base44 interface, but you might spot it in API responses, logs, or integration tools.

    **What should you do?** No action is needed. This means everything is working correctly.
  </Accordion>

  <Accordion title="400 - Bad request">
    A 400 error means the Base44 server could not process your request, often because some information is missing or in the wrong format.

    **Examples:**

    * Submitting a form with missing required fields.
    * Calling an API with the wrong data format.

    **What should you do?** Check the information you entered and try again. If using an API, make sure your request matches the expected format.
  </Accordion>

  <Accordion title="401 - Unauthorized">
    You are not logged in, or your login session has expired. The requested action requires authentication.

    **Examples:**

    * Trying to view a dashboard page without signing in.
    * Calling an API or integration feature with invalid credentials or an expired token.

    **What should you do?** Sign in to Base44 and try again. If using integrations, update your API keys or login credentials.
  </Accordion>

  <Accordion title="403 - Forbidden">
    You are signed in but do not have permission to perform this action or access the resource. This can happen if your role or permissions are limited, or if Row-Level Security (RLS) settings for certain data entities are not properly set.

    **Examples:**

    * Trying to change settings in an app you do not have access to.
    * Attempting to access data or pages restricted by your role or RLS rules in your app.

    **What should you do?** Check with your workspace admin to see if your permissions need to be updated. If you are an admin or developer, review the RLS rules for any relevant data entities and make sure the correct access is set up for the actions you want to take.

    Note that backend functions are only available on Builder tier plans and higher.

    **If you see 403 errors when connecting webhooks from external services (like Telegram or WhatsApp):**

    Some external services, such as Telegram or WhatsApp, send webhook requests from their servers but do not support including authentication credentials (like an `api_key` or custom headers). If your webhook or backend function requires authentication, these services return a 403 error.

    * Make sure your webhook endpoint does not require any authentication for services that can't send credentials. The endpoint must be public to work with these types of integrations.
    * If you want to keep authentication for other integrations, set up a separate public-only function or endpoint for these services, and only use it for actions that are not sensitive.

    After making your endpoint public, the external service should connect without a 403 error.
  </Accordion>

  <Accordion title="404 - Not found">
    The page, link, or resource you tried to access does not exist.

    **Examples:**

    * Entering an incorrect URL for your app or dashboard.
    * Accessing a deleted or moved file.

    **What should you do?** Check for typos and confirm you have the correct link. If the resource should exist, check with your workspace admin or teammates to make sure it has not been moved or deleted. If you still can't access it, contact Base44 support.
  </Accordion>

  <Accordion title="429 – Too many requests">
    You tried to perform an action too many times in a short time period. This triggers a temporary rate limit that protects performance and stability.

    **Examples:**

    * Rapidly clicking to reconnect a domain or repeat the same action in your dashboard.
    * Sending many repeated requests in a short time via the API, backend functions, or automations.

    **What should you do?** Wait a short time before trying again. When you retry, avoid repeating the same action quickly so you do not hit the limit again.

    **Additional info:**

    * Rate limits apply per person, so capacity scales with the number of people using your app.
    * Spread requests out over time instead of sending them all at once.
    * Use batch requests where your integration supports them.
    * Add caching so you do not call the same endpoint for the same data again and again.
    * Add retry logic that waits a short time before sending a new request after a 429 response.
    * If 429 errors appear during normal activity, contact Base44 support with the time of the error and what you were trying to do.
  </Accordion>

  <Accordion title="500 – Internal server error">
    There was a problem with the Base44 server when processing your request.

    **Examples:**

    * Seeing a “500 Internal Server Error” page.
    * Features failing when saving or loading data.

    **What should you do?** Refresh and try again. If the issue keeps happening, check the [Base44 Discord](https://discord.com/channels/1303811506080841758/1303811506848272516) for known issues or contact support with details about the error.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).