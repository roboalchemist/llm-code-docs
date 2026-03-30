# Source: https://firebase.google.com/docs/studio/troubleshooting.md.txt

# Firebase Studio troubleshooting &amp; FAQ

{ # disableFinding(CONTRACT) #}

<br />

> [!TIP]
> **Tip:** If you don't find an answer to your question, contact [Firebase Support](https://firebase.google.com/support/troubleshooter/studio) or [ask in our community forums](https://community.firebasestudio.dev/).

## Firebase Studio general

### How do I download my files from
Firebase Studio?

To download your files as a zip file:

- Right-click on any directory in the Explorer pane and select **Zip and Download**.

To download everything in your project directory:

1. Select **File \> Open Folder**.

2. Accept the default `/home/user` directory.

3. After the files load, right-click your working directory and select
   **Zip and Download** . If using
   the App Prototyping agent, your working directory will be `studio`. If
   using a template or uploaded project, this will be your project name.

4. When prompted to rebuild the environment, click **Cancel**.

5. After your download completes, re-open your working directory from the
   **File** menu to move back into your workspace.

> [!TIP]
> **Tip:** You can also [export to GitHub](https://firebase.google.com/docs/studio/github).

### Third-party cookies aren't enabled.

Before you get started, you might need to enable third-party cookies for your
browser. Firebase Studio requires third-party cookies in most browsers
to authenticate workspaces.

### Chrome

On desktop:

1. Open **Settings**.
2. Open the **Privacy and Security** tab.
3. Make sure **Allow all cookies** is enabled.
4. Open [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).
5. Click the visibility icon in the address bar visibility_off to open the **Tracking
   Protection** panel. Turn on the **Third-party cookies** setting to temporarily allow third-party cookies. This enables cookies on Firebase Studio for 90 days.

On Android phones and tablets:

1. Tap ( more_vert ) **More** \> **Settings**.
2. Open **Site settings** \> **Third-party cookies**.
3. Make sure **Allow all cookies** is enabled.
4. Open [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).
5. Click the visibility icon in the address bar visibility_off to open the **Tracking
   Protection** panel. Turn on the **Third-party cookies** setting to temporarily allow third-party cookies. This enables cookies on Firebase Studio for 90 days.

On iPhones and iPads:

1. Open the **Settings** app \> **Apps** \> **Chrome**.
2. Turn on **Allow Cross-Website Tracking**.
3. Open [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).

### Safari

On desktop:

1. Open **Safari \> Settings...**.
2. Turn off the following settings:
   - **Advanced \> Block all cookies**
   - **Privacy \> Prevent cross-site tracking**
3. Open [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).

On iPhones and iPads:

1. Open the **Settings** app \> **Apps** \> **Safari**.
2. Turn off the following settings:
   - **Prevent Cross-Site Tracking**
   - **Advanced** \> **Block All Cookies**
3. Open [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).

### Firefox

You don't need to enable third-party cookies for Firefox.
Open [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).

### Opera

1. Open Opera.
2. Open the menu and click **Settings**.
3. Go to the **Privacy \& Security** section and expand the **Third-party cookies** option.
4. Select **Block third-party cookies in Incognito mode** or **Allow third-party cookies**.
5. Open [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).

### Arc

1. Go to <arc://settings>.
2. Go to the **Privacy and security** section and expand the **Third-party cookies** option.
3. Select **Block third-party cookies in Incognito mode** or **Allow third-party cookies**.
4. Open [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).

### Brave

You don't need to enable third-party cookies for Brave. Open
[Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/).

<br />

<br />

### Why does Firebase Studio need
third-party (3P) cookies enabled?

Firebase Studio needs 3P cookies enabled since we render an iframe from
one domain (a subdomain of `cloudworkstations.dev`) on another domain
(`studio.firebase.google.com`), and 3P cookies enable secure cross-origin
communication.

<br />

<br />

<br />

<br />

### How do I update to the latest
version of React or Next.js?

A critical Remote Code Execution (RCE) vulnerability affects applications built
with Next.js and React Server Components. To protect your application and data,
you must update to the latest stable version.

1. Open your Firebase Studio project, and switch to ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg) Code view.
2. Open the terminal (`Shift+Ctrl+C`), and run the command `npx fix-react2shell-next`.
3. Follow the prompts in the terminal to proceed and apply any fixes. ![fixes applied](https://firebase.google.com/static/docs/studio/images/terminal-command-applied.png)
4. When the process completes, [publish your updated app](https://firebase.google.com/docs/studio/deploy-app).

<br />

<br />

<br />

<br />

### While opening a workspace,
the message *Unable to forward your request to backend. Couldn't
connect to a server on port 80* appears.

Wait approximately five seconds and refresh the page.

<br />

<br />

<br />

<br />

### My preview doesn't load, but I
can't find any issues in code. How can I restart Firebase Studio?

If Firebase Studio isn't refreshing properly (typically as a result of major
refactors, or changes to your environment `dev.nix` file), open the command
palette
(`Cmd+Shift+P` on Mac or `Ctrl+Shift+P` on ChromeOS, Windows, or
Linux) and run the **Hard Restart** command. If that doesn't work,
try running the **Rebuild Environment** command.

<br />

<br />

<br />

<br />

### My workspace is not
responsive, all I see is a blank screen when it loads

If your workspace is not responding, you can try restarting the VM. To do this:

1. From [Firebase Studio](https://firebase.google.com/docs/studio/https://studio.firebase.google.com/), click the
   **More** ( more_horiz ) menu,
   then select **Restart**.

2. When prompted, click **Restart** again.

3. Re-open your workspace.

<br />

<br />

<br />

<br />

### While creating a workspace, I see a
message, *Whoops...We need to start a new VM*, and the UI hangs after
that.

Firebase Studio maintains a warm pool of VMs used to provision
workspaces on demand. When the pool runs low, the workspaces are
provisioned after a new virtual machine is started. The process can take
time (sometimes up to five minutes) but eventually succeeds.

<br />

<br />

<br />

<br />

### \[Errno 28\] No space left on
device

You might encounter this message if the disk is full. The Firebase Studio
workspace provides:

- 100 GiB total disk space for [Nix
  packages](https://firebase.google.com/docs/studio/get-started-workspace#configure-nix-file) and `/tmp`
- 10 GiB for your `/home` directory

<br />

<br />

<br />

<br />

### When
creating a workspace, I receive *an internal error occurred*.

In most cases of internal errors during workspace provisioning, refreshing the
page after a minute or so should get you past the error and into the workspace.

<br />

<br />

<br />

<br />

### How many workspaces can I
create?

The Firebase Studio no-cost plan is limited to three workspaces per user.
You can increase the number of workspaces you can create up to 10 by joining
the [Google Developer
Program](https://developers.google.com/profile/u/_/dashboard).
To upgrade to 30 workspaces, subscribe to the [Google Developer Premium
Program](https://developers.google.com/profile/u/_/plans-and-pricing).

<br />

<br />

<br />

<br />

### How do I submit a feature
request or feedback on an issue I encountered?

If you encounter an issue while using Firebase Studio or have a feature
request, [contact Firebase
Support](https://firebase.google.com/support/troubleshooter/studio).

<br />

<br />

<br />

<br />

### I was using a particular feature in
Firebase Studio but I can't find it anymore. Why was it removed?

Some of the features in Firebase Studio are experimental. We value your
feedback and actively use it to inform our current and planned feature set,
periodically removing features that aren't living up to your expectations
or our own. If there are features you'd like to see in your ideal version
of Firebase Studio, [send us
feedback](https://firebase.google.com/docs/studio/connect). We want to hear from you!

<br />

<br />

## Firebase Studio Code workspaces

<br />

<br />

### My workspace loads, but the
emulator is blank.

We're actively improving the reliability of our cloud-based emulators. If a page
refresh does not fix the problem, [report the issue to Firebase
Support](https://firebase.google.com/support/troubleshooter/studio).

<br />

<br />

<br />

<br />

### Firebase Studio workspaces
have a Flutter version that is incompatible with my project.

You can upgrade or downgrade the version of almost all pre-installed
software inside a workspace just as you would on your local machine (using
apt-get or brew). You can upgrade or downgrade software in your workspace,
but installed software is not persistent across sessions. We recommend
including all required packages in your
[dev.nix](https://firebase.google.com/docs/studio/customize-workspace) file.

We're actively working to improve Flutter version management in
Firebase Studio.

<br />

<br />

<br />

<br />

### I shared my workstation URL with
someone, but they cannot see it.

You can only share a workspace URL with users that have access to the workspace.
Users without permission see an error when trying to visit the URL. Be sure to
explicitly [share the workspace with them](https://firebase.google.com/docs/studio/share-your-workspace).

<br />

<br />

<br />

<br />

### When I share my workstation, what
can my collaborator see?

Users added to your workspace have complete access to the VM's entire file
system, which may contain sensitive files like private keys and access
tokens that are stored on disk. **Only share your workspace with
people you trust.** While this approach helps other users view the exact
state of your workspace, it means that they see everything on your
workspace.

<br />

<br />

<br />

<br />

### I shared my workspace;
why can't my collaborator publish or monitor my app?

Users added to your workspace may not have permission to its underlying Firebase
project which powers the "App overview" publishing and monitoring features. To
grant them permission to your Firebase project, see [Permissions and access to
Firebase
projects](https://firebase.google.com/support/faq#projects-permissions-and-access)

<br />

<br />

<br />

<br />

### Can I use frameworks that
Firebase Studio does not have a template for to build my application?

Yes! You can [customize your environment](https://firebase.google.com/docs/studio/customize-workspace) to
work with just about any framework or language in Firebase Studio.

<br />

<br />

<br />

<br />

### What target directory should I
select when publishing a Flutter app to Firebase Hosting?

Choose the `build/web` directory. This directory should contain an `index.html`
and all the static assets needed to render your web app after the app is built
successfully (via `flutter build web`).

<br />

<br />

<br />

<br />

### How can I set up my app's backend
on my workspace so that my frontend can communicate with it?

You can temporarily publicly open the TCP port your backend server is running on
to make it easier to develop your frontend and backend separately, across
different workspaces:

1. Start your backend or API server either manually in a terminal, or as part
   of your [`dev.nix` file](https://firebase.google.com/docs/studio/customize-workspace)'s preview
   configuration or `onStart` lifecycle hook.

2. Click the **Firebase Studio** icon in the activity bar (on the left by
   default) to open the **Firebase Studio** panel.

3. ![Backend ports](https://firebase.google.com/static/docs/studio/images/backend-ports.png)

   Expand the **Backend ports** section to see a list of running servers,
   including their port number and process ID (PID).
4. Click the ![image of a lock
   icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-lock.svg) **Make
   public** icon (a lock) to the left of the port number.

   > [!WARNING]
   > **Warning:** This enables anyone on the internet to access your port while the workspace is active and until you explicitly turn off public access.

5. Click the ![image of copy
   icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-copy.svg)
   **Copy URL** icon to the right of the port number to copy its
   fully-qualified URL.

6. You can now reference this URL directly (for example, with a `fetch` call)
   from your frontend.

   > [!NOTE]
   > **Note:** If your frontend is a web browser, you may need to enable [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) support in your backend or API server (for example, using the `cors` NPM package for Node.js apps or `flask-cors` for Python Flask apps).

<br />

<br />

<br />

<br />

### I closed my preview tab. How do
I bring it back?

Open the command palette using `Ctrl+Shift+P` (or `Cmd-Shift-P` on MacOS), then
select **Firebase Studio: Show Android preview** or
**Firebase Studio: Show web preview**.

<br />

<br />

<br />

<br />

### What is Code OSS?

Code-Open Source Software (Code-OSS) is an open-source project that's the core
layer of VS Code. Code-OSS is available on GitHub under the standard MIT
License, and is where Microsoft develops the VS Code product.

<br />

<br />

<br />

<br />

### How can I prevent my code
completions and Gemini chat prompts from being used as training
data?

Your use of Firebase Studio is governed by the [Google Terms of
Service](https://policies.google.com/terms).

However, note that your use of generative AI features within
Firebase Studio is governed by the [Generative AI Prohibited Use
Policy](https://policies.google.com/terms/generative-ai/use-policy) and the
[Gemini API Additional Terms of
Service](https://ai.google.dev/gemini-api/terms) (specifically governed by
[Gemini API Additional Terms of Service: Unpaid
Services](https://ai.google.dev/gemini-api/terms#unpaid-services)).

To block the use of your *prompts and responses* for model training, do not
use the App Prototyping agent, and do not use Gemini in Firebase within
Firebase Studio. To block the use of your *code* for model training,
[turn off code
completion](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-complete)
and [code
indexing](https://firebase.google.com/docs/studio/set-up-gemini#adjust-code-indexing)
in your Firebase Studio settings.

<br />

<br />

## Gemini

<br />

<br />

### How do I view the request per
minute quota for my auto-generated Gemini API key?

You can view the quotas associated with your auto-generated API key on
the **Generative Language API Quotas and System Limits** page in the
[Google Cloud console](https://firebase.google.com/docs/studio/https://console.cloud.google.com//apis/api/generativelanguage.googleapis.com/quotas).

<br />

<br />

<br />

<br />

### I received an error about exceeding the
maximum number of tokens allowed

The amount of data (represented as "tokens") in your project is larger than the
maximum limit the model can accept. To resolve this error, adjust which files in
your codebase should be hidden from Gemini:

1. In your workspace, switch to
   ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)
   Code view.

2. [Create an `.aiexclude` file](https://firebase.google.com/docs/studio/set-up-gemini#exclude-files).

3. Include files or directories Gemini should ignore to reduce the
   amount of data in your project. For example, you might want to add `.next/`
   and all subdirectories. The path should be relative to the directory that
   contains the `.aiexclude` file:

        .next/

4. Try again to use Gemini. If you still receive an error about
   exceeding the
   maximum number of tokens, try adding other large files or directories to the
   `.aiexclude` file.

<br />

<br />

## The App Prototyping agent

<br />

<br />

### I was unable to create a project

When provisioning resources like a Gemini API key or deploying to
Firebase App Hosting, a project is automatically provisioned for you, based
on the name of your Firebase Studio workspace.

If you receive a "Failed to create a project" error:

- If your Google Account is part of an organization, it's possible that you
  don't have permission to create Google Cloud projects or that you've met
  your project quota limit. Contact your administrator for assistance or see
  [Creating and managing
  projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

- If your Google Account is not part of an organization, you may have met your
  Google Cloud project quota limit. [Request a quota
  increase](https://support.google.com/code/contact/project_quota_increase).

  See [Managing project
  quotas](https://cloud.google.com/resource-manager/docs/creating-managing-projects#managing_project_quotas)
  to learn more about project quotas.

Learn more about Firebase and Google Cloud projects at
[Understand Firebase projects](https://firebase.google.com/docs/projects/learn-more).

<br />

<br />

<br />

<br />

### Cloud Billing account
creation failed

When provisioning resources like deploying to
Firebase App Hosting, you can choose or create a Cloud Billing account.

If you receive a "Failed to create a Cloud Billing account" error:

- Make sure that you have permission to create Cloud Billing accounts. Check your permissions or contact your administrator for assistance.

If you receive a "Too many projects with this billing account" error:

- You may have met the project limit for your Cloud Billing account. You can [request a quota
  increase](https://support.google.com/code/contact/billing_quota_increase). [Learn more about Cloud Billing account
  quotas](https://cloud.google.com/billing/quotas).

Learn more about creating a Cloud Billing account at [Create a new
self-serve billing
account](https://cloud.google.com/billing/docs/how-to/create-billing-account).

If none of these options resolve your issue, contact [Cloud Billing
support](https://cloud.google.com/support/docs/get-billing-support).

<br />

<br />

<br />

<br />

### How do I get
the App Prototyping agent to automatically add Cloud Firestore and
Firebase Authentication to my app?

Prompt the App Prototyping agent to add a database or authentication

while working on an existing app.
When you ask to add a database or authentication,
the App Prototyping agent asks for confirmation. If you agree,
the App Prototyping agent sets up a Firebase project with the requested
backend services for you.

<br />

<br />

<br />

<br />

### Why doesn't
the App Prototyping agent offer to fix my issue?

The App Prototyping agent detects Next.js errors and offers to
fix them. If you receive an error and it doesn't offer to fix it, copy the
issue text and paste it into the chat.

For best results, provide more information about the nature of the issue,
if you have it.

For example, if you see a Firebase error like `Property access is undefined
on object. for 'list' @ L6`, which is indicative of an issue with
Cloud Firestore rules, preface the error with, "Can you help me fix this
Cloud Firestore rules issue?"

<br />

<br />

<br />

<br />

### I received a "Failed to publish app" error after publishing

Publishing failures will typically log actionable errors to
Cloud Build logs. To debug and resolve publish failures:

1. In the **App Details** page (if minimized, click **Publish** to reveal
   it), click **View Details** . This opens App Hosting in the
   Firebase console.

2. From the [Firebase console
   App Hosting](https://firebase.google.com/docs/studio/https://console.firebase.google.com/project/_/apphosting) page, click **View Cloud Build logs**.

   This opens the Firebase console where you can see build logs and locate
   the error.
3. Copy the error and paste it into the App Prototyping agent or
   Gemini in Firebase chat in your workspace and ask
   Gemini to fix it.

4. To verify the fix, switch to **Code** view, open Terminal, and run `npm
   run build`. If you see another error, try again. If you see a
   `FirebaseError`, see [Why doesn't the App Prototyping agent offer to fix
   my issue?](https://firebase.google.com/docs/studio/troubleshooting#prototyping-agent-fix).

5. When the build is successful, click `npm run start` and open the localhost
   link that's provided and test your app functionality. You can check the
   terminal for any runtime errors.

6. If all is successful, `Ctrl-C` in Terminal to stop the
   production-packaged build running in your workspace, then try the
   App Hosting publishing flow again.

<br />

<br />

<br />

<br />

### I'm unable to make changes using
the App Prototyping agent

If the App Prototyping agent doesn't complete requested code changes,
reverts back to the App Blueprint step, or repeatedly returns an error saying
it hit a snag:

1. [Restart the VM](https://firebase.google.com/docs/studio/troubleshooting#unresponsive-workspace).

2. If the problem persists when you reopen your workspace, enter `/clear` in
   the the App Prototyping agent chat.

   > [!NOTE]
   > **Note:** This command erases your chat history, including the button to **Restore** to a previous point.

3. If the problem continues, you can try creating a branch from a previous
   version of your app:

   1. Switch to ![Code switch icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)
      Code view.

   2. Open the **Source Control** tab.

   3. In the Source Control Graph, right-click an earlier version \> **Create
      Branch**. Enter a name for your branch.

   4. Return to Prototyper mode. If the agent still doesn't respond or returns an error, try branching from an even earlier version of your app.

   5. To switch between branches you create (or return to the main branch),
      click the branch name located in the bottom-left corner of
      Code view and choose the branch you want to use.

<br />

<br />

<br />

<br />

### I'm having trouble prompting
the App Prototyping agent to integrate Firebase services.

We're working on improving the process of integrating Firebase services
using the App Prototyping agent. In the meantime, here are some common
challenges and tips.

- **Configuration file didn't update** : In your prompt, include the specific value that you want to update. The values can be found in the [Project settings](https://console.firebase.google.com/project/_/settings/general) page of the Firebase console. For example, you could prompt: "Update the measurementId in my config with G-1234567890."
- **Authentication doesn't work when previewing my app** : You may need to include the preview URL as an authorized domain:
  1. In Prototyper mode, click open_in_new **Open in New Window**.
  2. In the new preview window that opens, copy the URL. Note that the URL should start with `6000`. If it starts with `9000`, update it before proceeding to the next step.
  3. In the [Authentication settings](https://console.firebase.google.com/project/_/authentication/settings) page of the Firebase console, add the URL you copied in the previous step to the **Authorized domains** . Note: This method only enables the default preview shown in Prototyper mode. The preview within Code view and the preview pop-out might not allow you to authenticate.
- **Firebase Security Rules weren't created** : Gemini can help you write security rules, but can't yet automatically add them to your Firebase project. You need to copy your Firebase rules into the [Firebase console](https://console.firebase.google.com/) to publish them.
- **Unexpected interaction with the Firebase MCP server** : If you set up the [Firebase MCP server](https://firebase.google.com/docs/studio/mcp-servers), you might encounter unexpected behavior when using Prototyper for Firebase integrations. If this occurs, switch to Code view and prompt Gemini in Firebase to integrate Firebase services.

<br />

<br />

### How do I change my app's favicon?

> [!TIP]
> **Tip:** If you're creating a Firebase Studio template, you can set the workspace icon inside your template for all subsequent uses. Learn more at [Set your workspace icon](https://firebase.google.com/docs/studio/customize-workspace#custom-icon).

You can change the icon from inside Firebase Studio:

1. Switch to ![Code switch
   icon](https://firebase.google.com/static/docs/studio/images/icons/codicon-code.svg)
   **Code** view.

2. If not already active, click **Explorer** (`Ctrl+Shift+E` or
   `Cmd+Shift+E` on Mac) to view all of your files.

3. Expand `src`, right-click on the `app` directory, and choose
   **Upload...**

4. When prompted, navigate to and select your `favicon.ico` file from your
   local file system.

5. When prompted to replace the existing favicon file, click **Replace**.

6. Re-deploy your app or clear your browser cache to view the change.

<br />

<br />