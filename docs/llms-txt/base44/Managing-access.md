# Source: https://docs.base44.com/Setting-up-your-app/Managing-access.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Choosing who can access your app

> Set who can use your Base44 app with visibility settings, roles, and collaborators.

Use visibility settings to decide who can open your app and whether they need to sign in. Then use roles to control what each person can see and do inside the app, such as viewing data or managing orders. Finally, add collaborators to work with you in the app editor to design, configure, and maintain the app.

Only collaborators and the app owner can access the app editor and your app’s dashboard. Roles such as Admin and User control what people can do in the live app, but they do not give access to the app editor or dashboard.

<Frame caption="Managing your app users and their roles">
    <img src="https://mintcdn.com/base44/UO-XTofw-GWx8lKi/images/users-1.png?fit=max&auto=format&n=UO-XTofw-GWx8lKi&q=85&s=5ff3c3dfae27371d04654ea0bccc0e62" alt="Users 1" width="2302" height="1132" data-path="images/users-1.png" />
</Frame>

***

## Setting your app visibility

App visibility controls who can open your app and whether they need to sign in. You choose the visibility level that matches your app’s purpose.

Base44 uses smart app visibility to suggest a starting point for you. Apps that act like public sites, such as landing pages or portfolios, are automatically set to **Public** without requiring login. You can change this setting at any time.

<Frame caption="Choosing your app visibility from your app's dashboard">
    <img src="https://mintcdn.com/base44/tebV-vnNE9oTZ2M6/images/appvis-1.png?fit=max&auto=format&n=tebV-vnNE9oTZ2M6&q=85&s=bffcaeb5b8e3d01e90acd45c8714c551" alt="Appvis 1" width="2316" height="1122" data-path="images/appvis-1.png" />
</Frame>

**To set your app visibility:**

1. Go to your app’s **Dashboard**.
2. Click **Overview**.
3. Click the **App Visibility** drop-down and select one of the following:
   * **Private:** Only invited people can open and use the app. Sign in is required.
   * **Workspace:** Everyone in your Base44 workspace can open and use the app. Sign in is required. This option appears only if your app belongs to a workspace.
   * **Public:** Anyone with the link can open the app. To require sign in, select **Require login to access**. For extra protection, click **Run security scan**.

<Warning>
  **Important:**

  * Private apps are available on paid plans only.
  * If you set your app to **Private**, you need to invite people so they can log in and use your app. Click **Send Invites** to send invitations or share your app link. If someone tries to access a private app without being invited, they see an error message.
</Warning>

<Note>
  Features that rely on user identity, such as profiles, are not available if login is not required.
</Note>

***

## Inviting users to your app

Invite people to use your app by sending them an email invitation from your dashboard or from inside your app.

Inviting someone as a user or admin controls what they can do in the live app. It does not give them access to the app editor or your app’s dashboard.

<Note>
  **Notes:**

  * If your app is set to **Workspace** visibility, all workspace members automatically have access and do not need individual invites.
  * Invite permissions depend on your app’s visibility:
    * **Private application:** Only admins can invite people and can choose whether the role is user or admin.
    * **Public application:** Admins can invite people and choose roles. People with the user role can invite other users.
</Note>

### From your dashboard

Send invitations from your app's dashboard and choose the role for each person.

**To invite people from your dashboard:**

1. Click **Dashboard** in your app editor.
2. Click **Overview**.
3. In the **Invite Users** section, click **Send Invites**.
4. Enter the email address for each person you want to invite.
5. Click the **Access level** drop-down and choose a role.
6. Click **Send Invitation**.

<Frame caption="Inviting people to your app from your dashboard">
    <img src="https://mintcdn.com/base44/UO-XTofw-GWx8lKi/images/sendinvites-1.png?fit=max&auto=format&n=UO-XTofw-GWx8lKi&q=85&s=65a8c452584e22bbc26ebbd400d28bf5" alt="Sendinvites 1" width="2318" height="992" data-path="images/sendinvites-1.png" />
</Frame>

### From your app

You can also invite people directly from inside your app by asking the AI chat to set up in-app invites. Use the invite option it adds to enter each person's email address and, if prompted, choose the role you want to give them.

**Example prompt:**

`Add the option to invite users to the app from inside the app`

<Frame caption="Asking the AI chat to add the ability to invite users from inside your app">
    <img src="https://mintcdn.com/base44/k8g2-6NMpU1DHqeL/images/inviteinapp.png?fit=max&auto=format&n=k8g2-6NMpU1DHqeL&q=85&s=69e087f514c995587fbcb3b2aab5a58e" alt="Asking the AI chat to add the ability to invite users from inside your app" width="3444" height="1906" data-path="images/inviteinapp.png" />
</Frame>

***

## Choosing your users' roles

Roles control what each person can do on your live app. By default, every app includes 2 roles:

* **Admin:** Can manage areas that are restricted to admins on the live app.
* **User:** Can view and use the app with no special permissions.

Being an Admin or User does not give anyone access to the app editor or your app’s dashboard.

<Note>
  **Note:** To work in the app editor or change dashboard settings, someone must be a collaborator or the app owner.
</Note>

For example, in a store app you might give your shop manager the **Admin** role so they can update stock levels and process orders in the live app, while giving your sales staff the **User** role so they can view products, check order status, and use the app without changing settings.

<Tip>
  **Tip:** You can create extra roles and fields if you need more control. For example, you can ask the AI chat to:

  * `Create a role called Staff Manager that can update staff shifts and schedules on the live app.`
  * `Add a field called app_role to the Users entity with values Admin, Staff, and Viewer.`
</Tip>

**To update a user's role:**

1. Click **Dashboard** in your app editor.
2. Click **Users**.
3. Select the user whose role you want to change.
4. Click the **Role** drop-down and choose **Admin** or **User**.
5. Click **Submit**.

***

## Sharing your app link

Share a link to your app so people can access it directly.

**To share your app link:**

1. Click **Dashboard** in your app editor.
2. Click **Overview**.
3. In the **Invite Users** section, click **Copy Link**.
4. Share the link wherever you want people to access your app.

<Frame caption="Sharing a link to your app">
    <img src="https://mintcdn.com/base44/Wf5Bup18InzyuLCe/images/copylink-1.png?fit=max&auto=format&n=Wf5Bup18InzyuLCe&q=85&s=dbea62c60080439ff178a595c5646be9" alt="Copylink 1" width="2318" height="992" data-path="images/copylink-1.png" />
</Frame>

If you share a link with someone but they do not have permissions to access your app, they see a pop-up asking them to request access.

***

## Testing your app as a user

View and interact with your app as any user or role to check permissions, troubleshoot issues, or test user flows.

<Note>
  Changes you make while testing as a user are saved to that person's data. To avoid affecting real data, test with sample or dummy users whenever possible.
</Note>

<Card icon="image-portrait" title="Why would you want to test your app as a user?">
  * **Realistic testing:** Test the app exactly as a specific user or role sees it
  * **Faster troubleshooting:** Reproduce and debug user reported issues in their real context
  * **Permission visibility:** Quickly verify what each role or user can and cannot access
  * **Access tuning:** Decide if permissions or roles need to be updated based on real behavior
  * **Flow validation:** Run end to end checks (onboarding, key tasks, critical paths) before releases
  * **Safe experimentation:** Use fake or test users to safely test risky or destructive actions
  * **Stronger support:** Guide people more effectively by seeing their exact experience
  * **UX insight:** Build empathy and improve UX by viewing the app as different user types
</Card>

**To test your app as a user:**

1. Go to your app editor.
2. Click **Preview** at the top.
3. Click the **More Actions** icon at the top right.
4. Select **Act as a user**.

<Frame caption="Selecting &#x22;Act as a user&#x22; in the Base44 app editor">
    <img src="https://mintcdn.com/base44/lvidpF5IxzSIWGr4/images/actasuser-1.png?fit=max&auto=format&n=lvidpF5IxzSIWGr4&q=85&s=8263ba4618e5bcf8b6623aafad23da3f" alt="Actasuser 1" width="2320" height="490" data-path="images/actasuser-1.png" />
</Frame>

5. Click the drop-down next to **You're acting as** and select the relevant user.\
   **Tip:** The user's role appears in parenthesis next to their email address.
6. Preview and interact with the app as that user.
7. Click **Exit mode** when you're done testing as another user.

<Frame caption="Testing your app as a user in Base44">
    <img src="https://mintcdn.com/base44/vWatP1qHLcz4SnUQ/images/actasuser.png?fit=max&auto=format&n=vWatP1qHLcz4SnUQ&q=85&s=4287b74b8400bbd3aca2bcd73e774f7a" alt="Using the &#x22;Act as a user&#x22; feature in Base44" width="1636" height="1104" data-path="images/actasuser.png" />
</Frame>

***

## Inviting collaborators to your app

Collaborators are people who help you build your app in your app editor. Add collaborators when you want someone to design, configure, or maintain the app with you.

<Check>
  **What is the difference between collaborators and admins?**

  * **Collaborators**
    * Can open the app editor and your app’s dashboard.
    * Help you design pages, change logic, connect data, and configure settings.
    * Are invited from the **Invite collaborators** icon in the app editor.
  * **Admins**
    * Sign in to the live app.
    * Access admin-only areas on the live app, such as protected reports or management tools.
    * Cannot open the app editor or your app’s dashboard unless they are also collaborators.
</Check>

Collaborators are separate from user roles. When you add someone as a collaborator, they are added to your app as an Admin in **Users** by default so they can manage content, data, and settings in the live app while they build. You can later change their app role on the **Users** page without affecting their access to the app editor.

<Note>
  If you add a collaborator, they must have a paid Base44 plan or a seat in the workspace that owns the app.
</Note>

**To invite collaborators to build your app:**

1. Go to your app editor.
2. Click the **Invite collaborators** icon <Icon icon="user-plus" /> at the top right.
3. Enter the email addresses of the people you want to invite, separated by commas.
4. Click the **Send invite** icon <Icon icon="paper-plane" />.

<Frame caption="Inviting collaborators to your app in Base44">
    <img src="https://mintcdn.com/base44/54vC6tx-z8L934Nk/images/addcollab.png?fit=max&auto=format&n=54vC6tx-z8L934Nk&q=85&s=d917dea73ba25cc607faf4623dc9f276" alt="Addcollab" width="673" height="338" data-path="images/addcollab.png" />
</Frame>

**To manage collaborators:**

1. Go to your app editor.
2. Click the **Invite collaborators** icon <Icon icon="user-plus" /> at the top right.
3. Find the relevant collaborator and click the **More Actions** icon <Icon icon="ellipsis" />.
4. Click **Remove Collaborator**.
5. In the confirmation window, select an option:
   * **Remove collaborator access only:** Immediately revoke their access to the app editor and prevent them from making changes, but keep them in the **Users** list with their existing role so they can still use the live app.
   * **Remove from app entirely:** Revoke their collaborator access and remove them from the **Users** list so they can no longer sign in or use the app.

***

## FAQs

Click below to learn more about managing access to your app.

<AccordionGroup>
  <Accordion title="Can people sign up to use my app on their own?">
    If your app’s visibility is set to **Public (Require login)**, anyone with the link can create an account and sign in.
  </Accordion>

  <Accordion title="How do I review access requests for my private app?">
    When someone requests access to a private app, owners and collaborators get a notification.

    **To review an access request:** 

    1. Click the notifications icon <Icon icon="bell" /> at the top right of Base44.
    2. Click **Review** to open the request and decide whether to grant access.

    <Frame>
            <img src="https://mintcdn.com/base44/AXSC4iCKfLmgNj__/images/reviewaccess.png?fit=max&auto=format&n=AXSC4iCKfLmgNj__&q=85&s=317d1f4229e894f4312a87f9d0b7ef4b" alt="Reviewaccess" width="1320" height="860" data-path="images/reviewaccess.png" />
    </Frame>
  </Accordion>

  <Accordion title="What is the difference between an app user and a collaborator?">
    An app user is someone who signs in and uses your app. Their access is controlled by visibility settings and roles such as Admin or User. They can only see and use the live app (including any admin-only sections), not the app editor or dashboard.

    A collaborator is someone who helps you build the app in the app editor. Only collaborators and the app owner can open the app editor and your app’s dashboard. When you add someone as a collaborator, they are automatically assigned the **Admin** role in **Users** in the app by default so they can manage live data and settings while they build. You can change their app role later without changing their collaborator status.

    <Note>
      **Update:** On February 16, 2026, we released the ability to add app collaborators. Before this date, if you wanted someone to help edit your app, you made them an admin from the **Users** page in the dashboard. This also gave them access to the app editor, even if you only wanted them to manage things inside the app.

      With app collaborators, you can now invite people directly from the app editor to help build and maintain your app, without changing their role as an app user. This means you can safely use the built in Admin role for people who manage your live app, while keeping app editor access limited to collaborators.

      Following this change, existing admins in existing apps are not blocked from editing. They keep their current access and are added as collaborators so they can continue working on the app as before. For new people, you can choose whether you want them to be a collaborator, admin, or both, based on whether they need access to the app editor, in app admin access, or both.
    </Note>
  </Accordion>

  <Accordion title="Do I need to make someone an admin in Users so they can edit my app?">
    No. If you want someone to help build or edit your app, invite them as a collaborator from the app editor. This gives them access to the app editor and, by default, the Admin role in your app. Make someone an admin in **Users** without adding them as a collaborator only when they need admin access in the live app but do not need to work in the app editor.
  </Accordion>

  <Accordion title="Do collaborators need a seat or paid plan?">
    Yes. Collaborators must either have a paid Base44 plan or a seat in the workspace that owns the app. If they do not, they cannot be invited as collaborators and you see an ineligible users message in the invite panel.
  </Accordion>

  <Accordion title="Which roles can access the Users entity?">
    Only collaborators and the app owner can access the **Users** dataset in the app dashboard.
  </Accordion>

  <Accordion title="How can I manage app security settings?">
    You can control who can access, read, write, or delete records in your app’s data entities by setting **Row Level Security (RLS)** rules and permissions. Configure access for each entity to ensure data is only available to authorized people. Learn more about [managing security settings](https://docs.base44.com/Setting-up-your-app/Managing-security-settings).
  </Accordion>

  <Accordion title="Can I remove a user from my app?">
    Yes. Go to your app’s **Dashboard** → **Users** and click the **Delete** icon <Icon icon="trash" color="#EE1106" size={16} /> next to the person you want to remove. Removing them immediately revokes their access.
  </Accordion>

  <Accordion title="I made a feature for my members, but it’s only working for admins. Why is that?">
    By default, features connected to the 'User' entity are only available to admins. If you build a member facing feature such as a member profile page using the 'User' entity, it works for admins but is not visible or accessible to regular members.

    To make your feature available to all members, or just to specific members, set up a custom entity for member data such as 'MemberProfile'. Connect your features to this new entity instead of the default 'User' entity. This lets you decide exactly which members have access, so both admins and the members you choose can use your feature as expected.

    <Tip>
      You can explain what you want to happen in the AI chat, and it will set it up for you.
    </Tip>
  </Accordion>

  <Accordion title="How can I create fake users to safely test user flows?">
    To safely test user flows without affecting real data, add a test person directly to your app. Once the test profile exists, you can use the **Act as a user** feature to impersonate them and preview their experience.

    **To create a fake (test) user:**

    1. Go to your app’s **Dashboard**.
    2. Click **Users**.
    3. Click **Invite User** to send an invitation, or register a new account using your app’s public signup page.
    4. Assign the desired role or permissions to the test profile.

    <Tip>
      You can also ask the AI chat to create a test user.
    </Tip>

    After you create your test user, open your app, click the **More Actions** icon at the top, and select **Act as a user**. Then, choose your test user from the list to interact with your app as that person. Any actions taken affect only the test user's data, not your live accounts.

    Use this method to check permissions, visibility rules, and user flows before rolling out changes to everyone.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).