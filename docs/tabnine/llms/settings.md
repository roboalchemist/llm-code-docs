# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings.md

# Source: https://docs.tabnine.com/main/getting-started/tabnine-cli/features/settings.md

# Source: https://docs.tabnine.com/main/getting-started/context-engine/admin-console/settings.md

# Settings

To enable and control Context Engine preprocessing, open the Context Engine Settings page. At the top, locate the Context Engine Enablement panel.

To enable advanced preprocessing, use the control in this panel and read the description to confirm what will change. Make sure your organization is ready for Context Engine to analyze the repositories you configured on the Codebase tab.

To choose the model that powers Context Engine, open the “Context Engine Model” dropdown. Select a supported model such as “Claude 4.5 Haiku” according to your performance and cost requirements.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2F4mV8I5mUO3lcHB1Tv2vS%2Funknown.png?alt=media&#x26;token=bd22b592-f227-492c-bb49-4948b6e4b93f" alt=""><figcaption></figcaption></figure>

To control which repositories Context Engine can access, set the “Context Engine User” field. Choose a user account that has exactly the repository permissions you want Context Engine to have.

To define when preprocessing can run, use the “Pre‑Processing Schedule” section. Select “Any time” to allow Context Engine to run jobs whenever needed, or choose “Controlled” if you plan to restrict heavy processing to dedicated windows.

When you need to stop Context Engine temporarily, click the “Disable Context Engine” button. To adjust model, user, or scheduling settings, click “Edit” and save your changes when done.

To manage how users access Context Engine‑powered tools, scroll to the Context Engine Tools Configuration panel. Read the description to understand how this affects tools such as Tabnine CLI and Tabnine Agent.<br>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FeUjB81APdfAYN3f2KN0g%2Funknown.png?alt=media&#x26;token=21529605-4698-4d36-9685-d885bbedcca6" alt=""><figcaption></figcaption></figure>

To expose Context Engine capabilities to end users, turn on the “Enable Context Engine tools to end users” switch. To keep Context Engine running only as an internal service, turn this switch off so client tools cannot call it.

Use this panel to stage rollouts. First, enable Context Engine and validate runs and assets, then enable end‑user tools when you are satisfied with the results.

***
