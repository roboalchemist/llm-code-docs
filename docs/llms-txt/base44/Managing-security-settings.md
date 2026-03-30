# Source: https://docs.base44.com/Setting-up-your-app/Managing-security-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing your app's security

> Protect your data by setting who can view, edit, or delete records using visibility controls and security rules. Learn how to secure each entity for public, private, or business apps with practical examples.

***

## Setting up your app's security settings

Protecting your app’s data helps keep information private and makes sure only the right people can access it. Base44 gives you flexible security settings so you can decide who can view, edit, or delete anything in your app. With the right setup, you avoid data leaks, mistakes, and people seeing things they shouldn’t.

<Tip>
  Check each step below to help keep your app and data secure, even if you are just testing. You might not need to complete every step, but reviewing them all helps prevent unwanted access and data leaks. You can always update your settings as your needs change. Setting up security early is much easier than fixing issues later.
</Tip>

***

## Step 1 | Set your app’s visibility

Start by choosing who can access your app as a whole. This is called app visibility. Decide if your app is only for you, for your team, or open to the public.

<Frame caption="Choosing who can access your app in Base44">
    <img src="https://mintcdn.com/base44/52M9psv6htLBF9Z-/images/appvis.png?fit=max&auto=format&n=52M9psv6htLBF9Z-&q=85&s=0542b282c49f8a089262b42fdbe00b48" alt="Choosing who can access your app in Base44" width="1418" height="480" data-path="images/appvis.png" />
</Frame>

**To set your app’s visibility:**

1. Click **Dashboard** in your app editor.
2. In **Overview**, select an option from the **App Visibility** drop-down:
   * **Private**: Only invited people can access the app.

     <Warning>
       **Important:**

       * Private apps are available on the **Starter** plan and higher.
       * If you set your app to **Private**, you need to invite people so they can log in and use your app. Click **Send Invites** to send invitations or share your app’s link. If someone tries to access a private app without being invited, they get an error message.
     </Warning>
   * **Workspace**: Anyone in your workspace can access your app.
   * **Public**: Anyone with the link can access your app.
3. (Optional) Select the **Require login to access** checkbox to force people to sign in before using your app.

<Tip>
  Even if you want your app to be public, select the **Require login to access** checkbox if it includes personal information for each person, such as messages or saved data. This helps keep everyone’s private information safe.
</Tip>

***

## Step 2 | Review your data access

After setting your app’s visibility, check each data entity to see who can access its information. This helps you spot anything that should not be public, such as sensitive tables or collections.

When you first create a data entity, it may be set to public by default. Always review each entity’s access settings and update them if you need to keep private data protected or control who can see and change information.

<Info>
  **Before you begin:** Create your data entities before setting up security rules in the next steps. You can only apply security settings after your entities are in place.
</Info>

**To review your data entities:**

2. Click **Dashboard** in your app editor.
3. Click **Security**.
4. Under **Data Entities** review the access to the entities in your app:
   * **Public:** All users can access every record in the entity.
   * **Restricted:** Only users matching the access rules can access records.

<Frame caption="Security settings on your data entities in your app">
    <img src="https://mintcdn.com/base44/Nss06ppgKLn6MEUa/images/datasecurity.png?fit=max&auto=format&n=Nss06ppgKLn6MEUa&q=85&s=07e45326a2b54da431db05185a1de487" alt="A screenshot showing the secruity on data entities on your Base44 app." width="1413" height="644" data-path="images/datasecurity.png" />
</Frame>

<Tip>
  If any entity shows a warning icon (red), it is public and may need rules to keep your data safe.
</Tip>

***

## Step 3 | Create access rules for your data

If you want to control who can view, add, edit, or delete records in your data entities, you can set up access rules.

Access rules let you decide exactly who can access or change specific data in your app. By setting security for each entity, you help protect sensitive information and make sure only the right people have the right access.

<Card title="Example">
  If you have an online store app, you can set up access rules so each customer can see only their own past orders, while store staff can see and manage all orders. You might also let only managers add or update product information. Start by selecting the action you want to control (Create, Read, Update, or Delete) and then set the rule you need:

  * **Store contact info (Read):** You want everyone to see your store’s address, phone number, and email. Select the **Read** tab and use the **No restrictions** setting so anyone can view your contact info, even if they are not logged in.
  * **Store orders (Read):** You want customers to see only their own orders. Select the **Read** tab and use the **Entity-user field comparison** setting to match the order’s customer ID with the logged-in user’s ID.
  * **Products (Create/Update):** You want only managers to add or update products. Select the **Create** or **Update** tab and select the **User property check** setting to allow create and update access for users with a manager role.
</Card>

<Frame caption="Setting up access rules for your data entities">
    <img src="https://mintcdn.com/base44/Nss06ppgKLn6MEUa/images/dataentitiesa.png?fit=max&auto=format&n=Nss06ppgKLn6MEUa&q=85&s=1642fa4e7fe0959dde80210069960f85" alt="Setting up access rules for your data entities in your Base44 app" width="1032" height="473" data-path="images/dataentitiesa.png" />
</Frame>

**To set up access rules:**

1. Click **Dashboard** in your app editor.
2. Click **Security**.
3. Click the entity you want to secure (for example, **Store orders**, **Products**, or **Store contact info**).
4. Click **Create Access Rules**.
5. Select the action tab for the type of access you want to control:
   * **Create**: Control who can add new records
   * **Read**: Control who can view records
   * **Update**: Control who can edit records
   * **Delete**: Control who can delete records
6. Choose a rule type and fill in the required details:
   * **No restrictions:** Anyone can access records for this action.
   * **Creator only:** Only users who created a record can access it.
   * **Entity-user field comparison:** Match a value in the record with a property of the logged-in user.
   * **User property check:** Allow access for users with a specific property, such as a staff or manager role.
7. Click **Save Security Rules**.

<Note>
  **Notes:**

  * You can create multiple rules by clicking **Add Rule** on a tab. You can set up as many rules as you need for Create, Read, Update, or Delete. If a user matches any of your rules, access is allowed (it uses "OR" logic).
  * Test your rules by logging in as different roles (such as customer and manager) to make sure each role sees or edits only what they should. You can also ask the AI chat to help you test it.
  * After setting up your rules, you’ll see a **Generated Create Access Rules (JSON)** box. This shows your rules in read-only JSON format for transparency. You do not need to edit this field.
  * To remove all rules and make the entity public again, click **Remove All Rules** at the top of the entity’s access rules.
</Note>

***

## Using the security check

The security check tool helps you spot hidden security risks in your app before they become a problem. If you’re not sure which entities need security rules or want to double-check your setup, you can run the built-in security check at any time.

The security check automatically reviews your app for missing access rules, unsafe backend function exposure, and secrets left in frontend code. Running the security check helps prevent accidentally exposing private data, catches misconfigurations (such as broken webhooks), and lets you ship your app with confidence.

The recommendations are not applied automatically. The checker highlights issues and suggests fixes, but you choose when to apply them. For every issue, you’ll get clear instructions and can apply safe default settings with a single click if you want.

<Frame caption="Accessing the Base44 security check">
    <img src="https://mintcdn.com/base44/92gOscacEpK7eIuI/images/securitycheck.png?fit=max&auto=format&n=92gOscacEpK7eIuI&q=85&s=dcb97a0d9387d8d099d4cfc42a6f61ad" alt="Accessing the Base44 security check" width="1419" height="418" data-path="images/securitycheck.png" />
</Frame>

### Running the security check

1. Click **Dashboard** in your app editor.
2. Click **Security**.
3. Click **Start Security Check**
4. Click **Apply Fixes** to instantly apply recommended rules, or review and adjust them manually.

### Fixing security issues

If the security check finds issues, you will see them with recommendations.

<Frame caption="Security issues found in the security checker">
    <img src="https://mintcdn.com/base44/OFX7BPSGpFCsv-HI/images/securityissues.png?fit=max&auto=format&n=OFX7BPSGpFCsv-HI&q=85&s=59334c4908428971a7feb64f19336c2b" alt="Recommendations from the security check in Base44" width="1418" height="615" data-path="images/securityissues.png" />
</Frame>

Click a security issue below to learn more.

<AccordionGroup>
  <Accordion title="Public data access (RLS issues)" icon="shield">
    Some data should only be seen by the right people. When you run the scan, it checks each of your **data entities** (like Tasks or Comments) to make sure users don’t have more access than they should.

    ***If your app allows everyone to view or edit certain data, the scan will show:***

    ❗ All users have full access\
    ⚠️ RLS Recommendation – Apply Fixes

    <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Scan1.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=2634594e6f33d25e6465ae4ee0f52523" alt="Scan1 Pn" className="mx-auto" style={{ width:"70%" }} width="431" height="593" data-path="images/Scan1.png" />

    RLS fixes might include making sure that:

    * Only the record **creator** can view or edit it
    * Access is limited to specific users based on their email, role, or department
    * Only **admins** can make changes
  </Accordion>

  <Accordion title="Exposed secrets" icon="shield">
    **Our security check also looks for things like:**

    * API keys
    * Tokens
    * Sensitive credentials

    If it finds any of these in your frontend code, it will let you know so you can remove or move them to a secure place.

    <Info>
      <u>What is a secret?</u> Secrets are private codes/ digital keys that help your app connect to other services. If someone gets access to a secret, they might be able to misuse your app or access data they shouldn’t.
    </Info>

    **How do I fix an exposed secret?**

        <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Scan3.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=08d04770e95c937d1780370315d8f0de" alt="Scan3 Pn" width="2348" height="734" data-path="images/Scan3.png" />

    Fixing an exposed secret like an API key would require touching the code, because:

    * You need to **remove** the key from your frontend code (which is written manually),
    * And **move the logic** to a secure place, usually a **backend function** that you’ll either create or update.

    You can paste the error and the code into **Discuss mode** to get step-by-step instructions from the AI. The AI can help write the code for the backend function and modify your frontend to call it.
  </Accordion>

  <Accordion title="Backend function issues" icon="shield">
    Backend functions are parts of your app that run behind the scenes such as handling payments or saving data. These should only be triggered in safe, controlled ways.

    When you run the scan, it checks if any of your backend functions are:

    * Open to anyone (when they shouldn’t be), or
    * Set up in a way that doesn’t actually work

    **About unauthenticated backend functions**\
    Security check flags backend functions that accept sensitive data (like emails, API keys, or IDs) without checking who the user is.

        <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Scan4.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=a4216dca20f9adfa00231bdabf809ea4" alt="Scan4 Pn" width="2368" height="1076" data-path="images/Scan4.png" />

    For example, a function that returns subscription details based only on an email in the request could accidentally expose another user's info if someone changes the email in the request.

    If a function is flagged, it usually means it’s **trusting request data without verifying** that the user is logged in or has permission to access it.

    To fix this, you’ll want to add a quick check in the function to confirm:

    * The user is signed in
    * The request is for their own data

    You can paste the error message and your function code into **Discuss** mode to get step-by-step instructions from the AI. The AI can walk you through how to add a quick check to verify the user is signed in, and make sure the request is for their own data.
  </Accordion>
</AccordionGroup>

***

## App examples and their settings

Check out these common scenarios to help you design the right app security and row-level security rules in Base44.

If you’re unsure about your access settings, set the entity to “Creator only” or restrict access to your specific role. Then open your app in a private or incognito window to confirm what’s visible.

<Tip>
  For any app that handles personal, sensitive, or user-specific data, always enable **Require login to access** and carefully review your row-level security rules. This helps prevent sensitive data from being visible to the wrong people.
</Tip>

<AccordionGroup>
  <Accordion title="Personal or family app (e.g. shared calendar, home tasks)">
    * **App examples:** Home management, shared tasks, family shopping lists.
    * **App users:** Only trusted people should have access.
    * **Security settings:**
      * **App visibility:** Private (invite-only). You must invite your users.
      * **Require login:** Yes. All users must log in with their invited account.
      * **Data entity access:** Optional. For shared data, no rule needed. If you want every family member to have access to only their data (per-user data), set “Creator Only” rule on each data entity.
  </Accordion>

  <Accordion title="Public site with contact form (e.g. business or event landing page)">
    * **App examples:** Company homepage, event promo site, product marketing page.
    * **App users:** Anyone with the link (public).
    * **Security settings:**
      * **App visibility:** Public. No invite required.
      * **Require login:** No, unless you want to add protected pages.
      * **Data entity access:** For contact form submissions, set Read to “Admin/Staff only” or restrict by role so only team members can view or manage incoming messages.
  </Accordion>

  <Accordion title="Internal company dashboard (e.g. HR or team project tracker)">
    * **App examples:** HR dashboard, sales tracking, project management, employee portal.
    * **App users:** Only people in your workspace or specific teams.
    * **Security settings:**
      * **App visibility:** Workspace. Only those in your workspace can access.
      * **Require login:** Yes. Everyone must log in with their workspace account.
      * **Data entity access:** Use role-based rules. For sensitive resources, set Read/Update/Delete to managers or specific roles, and broader access for general info like announcements.
  </Accordion>

  <Accordion title="User portal (e.g. to-do list, accounts)">
    * **App examples:** Personal to-do lists, expense trackers, workout logs, user dashboards, activity journals. Everyone sees only their own records.
    * **App users:** Registered users or anyone managing their own info.
    * **Security settings:**
      * **App visibility:** Public or Workspace, depending on if you want to allow general registration or only workspace members.
      * **Require login:** Yes. Users must log in to view or edit their dashboard.
      * **Data entity access:** Always set “Creator Only” for user-specific records. Each person can access, edit, and manage only their own data; no one else can view their private entries.
  </Accordion>

  <Accordion title="Admin-only pages (e.g. staff info, finance)">
    * **App examples:** Admin portal, back office management, sensitive setup pages.
    * **App users:** Admins or staff only.
    * **Security settings:**
      * **App visibility:** Private (invite-only) or Workspace (for staff).
      * **Require login:** Yes.
      * **Data entity access:** Set Read, Write, and Delete to Admin or Manager role only. No access for regular users.
  </Accordion>

  <Accordion title="Blog or public site with private editing">
    * **App examples:** Blog, resource library, documentation site, FAQ hub. Anyone can view, only admins or editors manage content.
    * **App users:** The public can view content. Only admins or editors can add, update, or delete it.
    * **Security settings:**
      * **App visibility:** Public. Anyone with the link can see public pages.
      * **Require login:** Required for management features only. Set up a protected admin or editor section where only logged-in users with the right role (admin/editor) can access and make changes. This keeps editing controls hidden from the public.
      * **Data entity access:**
        * **Read:** Set to Public or all users so everyone can view content.
        * **Create/Update/Delete:** Set to Admin or Editor only, so only trusted users can add, edit, or remove content.

    <Tip>
      **Tip:** To require login on just some features, ask the AI chat to set up a separate admin area or dashboard in your app. Only users with the appropriate role can view and use management pages or controls. All other pages stay public and do not require sign-in.
    </Tip>
  </Accordion>

  <Accordion title="App for multiple groups (e.g. schools, companies)">
    * **App examples:** SaaS platforms supporting different companies, schools, or customer groups; internal tools with department-based permissions.
    * **App users:** Users grouped by company, school, or department.
    * **Security settings:**
      * **App visibility:** Workspace or Private. Choose based on tenant model.
      * **Require login:** Yes. Each user logs in; data is segmented by group, department, or tenant.
      * **Data entity access:** Use advanced row-level security. Set rules so each tenant, company, or department only sees and edits their own data. Admins or managers in each group can access all records in their group.
  </Accordion>
</AccordionGroup>

***

## FAQs

Click a question below to learn more about security.

<AccordionGroup>
  <Accordion title="Why isn’t row-level security (RLS) restricting data access correctly?">
    Row-level security (RLS) rules control which users can access specific data in your app. If unauthorized users can see or edit data, or RLS rules are not working as expected, use the built-in security check to find and fix issues.

    **To troubleshoot RLS problems:**

    2. Run the security check to scan for missing or misconfigured RLS rules.
    3. Review the issues found and click **Apply Fixes** to use the recommended safe defaults, or adjust rules for each data entity manually.
    4. Sign in with different user roles to confirm only authorized people can access each type of data.
  </Accordion>

  <Accordion title="If I change the security settings, does it affect users already using my app?">
    Changes to security rules can affect what users can see or do. We recommend reviewing any fix suggestions before applying them.
  </Accordion>

  <Accordion title="What if I don’t understand a warning?">
    Many recommendations come with a little dropdown arrow. Simply click it to see more details about what the issue is and why the fix is suggested.

    You can also copy the message into the AI chat (**Discuss** mode) to get a deeper explanation, step-by-step.

    Still not sure? No problem! Just create a [<u>support ticket</u>](https://app.base44.com/support/conversations). Our team is always happy to help.
  </Accordion>

  <Accordion title="How can I make sure my app’s security is set up correctly?">
    Follow these steps to check that your app’s security settings work as intended:

    1. Set all your app and data security rules in Base44.
    2. Use a third-party scanning tool like SaveVibes to test what data is exposed.
    3. Test the app yourself by trying to access different areas with your account.
    4. Log in as a different user and check if you can view or change other users’ data.
    5. Ask the AI to create or run test scenarios to confirm you get errors if you try to access restricted actions or data.

    Review the results and update your settings as needed to close any gaps.
  </Accordion>

  <Accordion title="How do backend functions help enforce complex security, and how can I secure them?">
    Backend functions let you add custom logic to your app, so you can control what actions each user can perform; for example, limiting each user to one active project or checking their status before allowing changes. All backend functions run securely on the server and are never exposed to users. Backend code is fully secure and only accessible within your app. There’s no way to access or copy backend code from outside your app; this protection is built in by design.

    To secure a backend function, include access checks in the function code, such as restricting availability to certain roles or types of users. For example, you can make a function available only to admins, or require users to meet specific conditions (like a credit balance or join date). Row-level security (RLS) rules for data access are always enforced in backend functions, adding another layer of protection.

    Backend functions are powerful for handling anything that goes beyond standard security settings. This gives you total control over complex business logic and sensitive operations.
  </Accordion>

  <Accordion title="Are my data tables encrypted and can admins see my data?">
    All data tables and private apps are encrypted for security. However, data is not end-to-end encrypted, this means that admins can access your data if needed. We do not currently support full end-to-end encryption where only the user who created the data can see it and not even admins.
  </Accordion>

  <Accordion title="Can I create more roles than just user and admin?">
    Yes, you can create as many custom roles as you need. To do this, add a new field (such as business-role) to your User entity and define values like "manager," "visitor," or others that fit your app. Then, set up security rules using user condition braces on this field, so different roles have different levels of access.
  </Accordion>

  <Accordion title="How do I secure connections to third-party APIs?">
    To safely connect with third-party services (such as Stripe, Google APIs, or email providers):

    * Handle all API requests in backend functions.
    * Store all API keys and credentials using secrets management.
    * Backend functions guarantee requests come from a secure, server environment, and never from public-facing client code.
  </Accordion>

  <Accordion title="What is secrets management and why is it important?">
    Secrets are only available in backend functions. Secrets management lets you store sensitive information, like API keys or service tokens, in a secure, encrypted vault that only backend code can access. Using secrets ensures that confidential credentials are never exposed to end users or the client side, protecting your app from external threats.
  </Accordion>

  <Accordion title="Can I restrict access to specific fields in a record (Field Level Security)?">
    Field Level Security (FLS) is not currently available in Base44. At this time, you can only set security rules for entire entities (rows or records), not for individual fields within those records. For example, you cannot show a user’s name while hiding their email address in the same record.

    We are working on adding FLS in the future. Until then, use entity-level security settings and backend functions to control data access.
  </Accordion>

  <Accordion title="Can I access the source code or cryptographic hash algorithms used in Base44?">
    No, you cannot access the underlying source code or cryptographic hash algorithms used by Base44. Base44 is a proprietary, no-code platform, so you can build apps without needing access to our infrastructure code. This includes all security protocols, authentication details, and cryptographic algorithms, which are kept confidential to protect both our systems and your data.

    If you need to export the code for an app you created, this feature is available with a Builder plan or higher. Use the export feature in the top-right corner of your app editor to do this.

    All Base44 apps use industry-standard encryption protocols for data in transit and at rest. A secure authentication system protects your information.

    If you have security concerns about your app, especially authentication, make sure your Row-Level Security (RLS) rules are correctly set in your app's dashboard.
  </Accordion>

  <Accordion title="Can I make private apps?">
    From 6 February, 2026, private apps are a paid feature. You need a plan (Starter or above) to create new private apps.

    If you are on the free plan and already have private apps from before February 6th 2026, they will continue to work and you can still edit them. However, you will not be able to change a private app to public and back to private again without upgrading.
  </Accordion>
</AccordionGroup>

<Tip>
  [See our blog post](https://base44.com/blog/application-security) to learn more about protecting your app's security.
</Tip>


Built with [Mintlify](https://mintlify.com).