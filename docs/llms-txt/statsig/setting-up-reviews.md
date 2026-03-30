# Source: https://docs.statsig.com/guides/setting-up-reviews.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting up Reviews for Team Workflows

You can enable reviews for all Statsig resources such as feature gates, dynamic configs, segments, and experiments that you'll likely deploy to a production environment.

### Turning on Change Reviews for a Project

As a Project Admin, you can configure your project to require reviews for any changes. To enable reviews for your project, navigate to the **Project Settings** page, switch to the Reviews tab and toggle this on.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/setting-up-reviews/45a439b5-7cf7-4f32-82d0-596c089f2359.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=096e95e9ef2ac2ddce80471e1cc69959" alt="Project settings reviews configuration interface" width="1854" height="669" data-path="images/guides/setting-up-reviews/45a439b5-7cf7-4f32-82d0-596c089f2359.png" />
</Frame>

* You can optionally allow different roles to bypass the review requirement and self-approve review requests by customizing the permissions available to user roles:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/setting-up-reviews/4b7db056-a6be-4a76-99c9-08f8dc053ed8.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=92f12fecdef595d9350ee923bbcf09aa" alt="User role permissions configuration screen" width="1913" height="1400" data-path="images/guides/setting-up-reviews/4b7db056-a6be-4a76-99c9-08f8dc053ed8.png" />
</Frame>

* Now when you make any configuration changes, say to a feature gate or experiment, you'll be asked to **Submit for Review**; you can add reviewers when you submit the change for review

<img width="1168" alt="Submit for Review modal prompting for reviewer selection" src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/setting-up-reviews/166678241-272adade-ca60-4942-bd04-a1413d54864c.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=4bc9e0a8826d1161239c80496603922b" data-path="images/guides/setting-up-reviews/166678241-272adade-ca60-4942-bd04-a1413d54864c.png" />

* Reviewers will now see a notification on the Statsig console as shown below. When they click on **View Proposed Changes**, they will see a diff of the *current version* in production and *new version*. Reviewers can now **Approve** or **Reject** the submitted changes.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/proposed_changes.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=94a8823f06acfe0fa5b207aeb141150a" alt="proposed changes" width="2212" height="364" data-path="images/proposed_changes.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/F_V_VJJ-2qC3MQMI/images/example_review_page.png?fit=max&auto=format&n=F_V_VJJ-2qC3MQMI&q=85&s=16e0a5c7eda15971183a253d40a9865a" alt="example review" width="3094" height="1550" data-path="images/example_review_page.png" />
</Frame>

### Teams

To create a predefined group of reviewers, you can create Teams

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/setting-up-reviews/1b1c72a9-ac98-4590-8690-c39d2e68489a.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=28397b15ae74a311b100086c5ce52be9" alt="Teams creation interface" width="1719" height="707" data-path="images/guides/setting-up-reviews/1b1c72a9-ac98-4590-8690-c39d2e68489a.png" />
</Frame>

You can now use these predefined **Teams** when you submit any changes for review.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/setting-up-reviews/166684577-29598c7f-fcba-4c7e-848d-9a45b031bd79.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=d6ca092c85629af067ec8aa1a36d5b6f" alt="Team selection for review submission" width="2206" height="984" data-path="images/guides/setting-up-reviews/166684577-29598c7f-fcba-4c7e-848d-9a45b031bd79.png" />
</Frame>

### Enforcing Team Reviews

You can restrict who can make changes to your Project by (a) turning on **Reviews Required** for your Project and (b) adding designated **Teams** or **Reviewers** when you create the Feature Gate or Experiment.

For (a), see section **Turning on Change Reviews for a Project** to turn on project-wide reviews. For (b), as an owner of a Feature Gate or Experiment, you can add designated **Teams** or **Reviewers** at any time as shown below. This ensures that only these designated groups or members can review and approve any subsequent changes. When another member now tries to edit these designated review groups/reviewers, this will require approval from currently designated reviewers.

<img width="655" alt="Team review configuration settings" src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/setting-up-reviews/166682283-c9e2de57-0b9a-473e-adf2-100a240ab6b0.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=4f4c2a10148dd53ea39675e9addf2a6b" data-path="images/guides/setting-up-reviews/166682283-c9e2de57-0b9a-473e-adf2-100a240ab6b0.png" />

<img width="458" alt="Teams and reviewers selector for enforcing approvals" src="https://mintcdn.com/statsig-4b2ff144/JoVpINC5Q0MyHWkm/images/guides/setting-up-reviews/166682177-d44411e6-c4ab-49fe-9250-c77b063621af.png?fit=max&auto=format&n=JoVpINC5Q0MyHWkm&q=85&s=d79b6cbc0d8c78aa0123757af2d99807" data-path="images/guides/setting-up-reviews/166682177-d44411e6-c4ab-49fe-9250-c77b063621af.png" />

### Configuring Review Settings for Different Environments

Many teams build, test, and launch new features and experiments across multiple development environments. Statsig makes creating and using environments in feature launches easy via our [Environments support](/guides/using-environments#configuring-environments).

You can also configure which environments require reviews via your **Project Settings**. To do so, go to **Project Settings** → [**Keys & Environments**](https://console.statsig.com/BPJcDV1K1g87fTib5ZEMk/api_keys) → tap **Edit** on **Environments**.

By default if you have turned on "Reviews Required" for your Project, reviews will be required for Production, but not non-Production (lower) environments.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/td7uQ1R6kn1ySihe/images/environments.png?fit=max&auto=format&n=td7uQ1R6kn1ySihe&q=85&s=ffbccedf78a345513570849135094cb1" alt="Environments settings showing environments and order" width="2322" height="388" data-path="images/environments.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/td7uQ1R6kn1ySihe/images/edit-environment-dialog.png?fit=max&auto=format&n=td7uQ1R6kn1ySihe&q=85&s=6774e14d9b65fcea32d14d98cac8cb06" alt="Manage environments dialog with environment list and review settings" width="2824" height="1334" data-path="images/edit-environment-dialog.png" />
</Frame>

#### Team-based Required Reviews per Environment

You can assign specific teams as reviewers for each environment. This ensures that only designated team members can approve changes for that environment.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/td7uQ1R6kn1ySihe/images/environment-reviews.png?fit=max&auto=format&n=td7uQ1R6kn1ySihe&q=85&s=094a45340eb3389c1b4b1bb0dd11ad0d" alt="Assigning teams as reviewers for specific environments" width="1630" height="1048" data-path="images/environment-reviews.png" />
</Frame>

#### Code Freeze Use Case

During code freeze periods, you can prevent feature flags or configs from being deployed to production by assigning a dedicated code freeze team as the production reviewer. This ensures that only members of that team (such as your SRE team or designated code freeze owners) can approve production changes. Once the code freeze period ends, you can remove the team assignment to restore normal review workflows.


Built with [Mintlify](https://mintlify.com).