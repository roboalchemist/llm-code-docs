# Source: https://docs.envzero.com/guides/admin-guide/environments/drift-detection/drift-cause.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analyze Drift Cause

> Identify the root cause of infrastructure drift in env zero - unmanaged changes, provider updates, or unapplied code

<Note>
  **Feature Compatibility**

  The feature is fully compatible starting from agent version 1.0.1044
  The feature is supported only for Opentofu, Terragrunt, and Terraform.
</Note>

Drift refers to the divergence between the actual state of infrastructure and the state defined in configuration files. This can occur when changes are made outside of the Infrastructure as Code (IaC) tool, such as manual updates through a cloud provider's console or automated processes outside of the IaC pipeline.

Drift is risky because it can lead to unexpected behavior, inconsistencies in resource management, and potentially compromise system reliability or security. If not detected and addressed, drift can cause deployments to fail, resulting in costly misconfigurations and possibly leaving systems vulnerable to exploitation. Regular drift analysis is crucial for maintaining infrastructure consistency and ensuring that all changes are tracked and aligned with the defined code.

When resources are managed in env zero, identifying the root cause of environment drift is straightforward. Whether a user has modified the state directly, a provider version change has introduced differences, or new code was pushed without being applied - env zero captures these events.

## Drift Cause Analysis

Based on the IaC data, env zero will analyze the drift to determine whether it was caused by one or more of the following reasons:

1. ### Unmanaged Change

A resource was changed manually (by a user or API) in the cloud provider's console. Unmanaged changes to infrastructure are risky and not recommended. env zero will check if a change was made to the resource outside of the IaC code. If a change is detected, it will appear here:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/dc87af165638c3f824e82187b39cb5977f3a3df819f4f7b58f160fab97940654-1.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=f3210c9d5c978ed832e9ada14c35a100" alt="Interface screenshot showing configuration options" width="512" height="235" data-path="images/guides/admin-guide/environments/drift-detection/dc87af165638c3f824e82187b39cb5977f3a3df819f4f7b58f160fab97940654-1.png" />
</Frame>

If you have [Cloud Compass](/guides/cloud-compass/cloud-compass) configured, a 'More Details' link will appear. Clicking it will show all the events that occurred within the resource between the last modifying deployment and the drift check deployment. In the events modal, you can view event details related to the changed resource - Event Date, Event Resource, Event Name, and the user who took the action.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/e04965fe524d3a0fade0295edb6aad45de4c4aabb339b774f8c83f8414cc33ab-1.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=a8c9fff1f235255b523743a141260c89" alt="Interface screenshot showing configuration options" width="512" height="195" data-path="images/guides/admin-guide/environments/drift-detection/e04965fe524d3a0fade0295edb6aad45de4c4aabb339b774f8c83f8414cc33ab-1.png" />
</Frame>

Each event has a link that provides more information directly from the Cloud Provider.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/b217f3056e5b186daa5cfed6732207a83262d9ae90401226560cbfa40743f639-1.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=d00f8214a642664d0714e4258427b4c9" alt="Interface screenshot showing configuration options" width="512" height="330" data-path="images/guides/admin-guide/environments/drift-detection/b217f3056e5b186daa5cfed6732207a83262d9ae90401226560cbfa40743f639-1.png" />
</Frame>

<Warning>
  Getting Events

  Currently, retrieving resource events is supported only for AWS and Azure.\
  In order to retrieve resource events, you must first set up Cloud Compass in your organization.\
  For more information, please refer to the documentation.
</Warning>

1. ### Provider Version Change

A provider's version was changed, causing the drift. This can occur when the infrastructure code doesn't use static provider versions. env zero will display which provider's version changed, along with the old and new versions.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/c38b85a2635d1ff7ce89d49bf5cfee10f10c3b0bbcfafcab0dad79b9e13627e1-2.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=2959e54cc9794c2fe5c0d3eb2e79c3d4" alt="Interface screenshot showing configuration options" width="512" height="174" data-path="images/guides/admin-guide/environments/drift-detection/c38b85a2635d1ff7ce89d49bf5cfee10f10c3b0bbcfafcab0dad79b9e13627e1-2.png" />
</Frame>

1. ### Module Version Change

A remote module's version was changed, causing the drift. This can happen when the infrastructure code doesn't use static module versions. env zero will display which module's version changed, along with the old and new versions.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/f98b44bc5e5d742c145f2cbd2812c909174157886c657a03263ce247862a5385-3.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=600ebc07eb575fd81e210fa6191b505b" alt="Interface screenshot showing configuration options" width="512" height="174" data-path="images/guides/admin-guide/environments/drift-detection/f98b44bc5e5d742c145f2cbd2812c909174157886c657a03263ce247862a5385-3.png" />
</Frame>

1. ### Variable Change

One of the environment's inputs in env zero changed, causing the drift. env zero will display who made the change, when it occurred, and the variable's name, scope, old value, and new value. The old and new values will not be displayed for sensitive values.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/1f29a759b846950c5b7c71019835b54269c14a795579ebfaf7138c016fae10f1-4.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=9e3088df12f71af55f06094f149a1f95" alt="Interface screenshot showing configuration options" width="512" height="231" data-path="images/guides/admin-guide/environments/drift-detection/1f29a759b846950c5b7c71019835b54269c14a795579ebfaf7138c016fae10f1-4.png" />
</Frame>

1. ### Unapplied Commit

A change was made to the infrastructure code but has not yet been applied. env zero will check if a commit was made to the infrastructure code after the last modifying deployment and show the commit (with a link to it in the VCS provider), along with who made it and when.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/31c8b2920028bd88ee5345b035bb86d341dd8c49dd9193d200e8f32dd2d8312e-5.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=4dd4e1a4bbcfeecc66406eb5ba65b054" alt="Interface screenshot showing configuration options" width="512" height="189" data-path="images/guides/admin-guide/environments/drift-detection/31c8b2920028bd88ee5345b035bb86d341dd8c49dd9193d200e8f32dd2d8312e-5.png" />
</Frame>

env zero uses globs to make this check more accurate. The default globs are:

```
${TEMPLATEPATH}/**/\*.tf;${TEMPLATE_PATH}/**/.tofu;${TEMPLATEPATH}/\*\*/.hcl;env0.yml;env0.yaml
```

where `${TEMPLATE_PATH}` is the template's path.\
These default globs can be overwritten by using the `DRIFT_CAUSE_UNAPPLIED_COMMITS_GLOBS` environment variable on the environment in env zero. It is a semicolon-delimited list of globs. env zero will also ensure that the environment's revision and the revision at the time of the drift check are the same.

1. ### State Modified

The environment's state was directly modified. env zero will detect a state change and try to find a corresponding remote apply and link to it. If no remote apply is found, a message indicating that the state has changed will appear.\
When a remote apply was detected:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/6c67f293910029dc3090435d1281ce5fe893a27a2501eeb0ef03f360c4e2330b-6.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=6676b84be5b854610568786823ca6e7a" alt="Interface screenshot showing configuration options" width="512" height="210" data-path="images/guides/admin-guide/environments/drift-detection/6c67f293910029dc3090435d1281ce5fe893a27a2501eeb0ef03f360c4e2330b-6.png" />
</Frame>

When no remote apply was detected but the state has changed:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/46d229f4d0b11b20233cb52f41ae5884588451cf6abf29fcd1de319fe03dae40-6.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=ec3bf8df7955d5f9b76a28bcc0748072" alt="Interface screenshot showing configuration options" width="512" height="172" data-path="images/guides/admin-guide/environments/drift-detection/46d229f4d0b11b20233cb52f41ae5884588451cf6abf29fcd1de319fe03dae40-6.png" />
</Frame>

## Using Drift Cause

There are two ways to utilize Drift Cause:

1. ### In The Environment Page

If a drift has been detected in your environment, you will see a collapsible showing the number of issues found and a link to the drift deployment. Opening the collapsible will show a list of the different drift causes env zero checks for, as well as the check's status. These results will appear on the right.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/88471782e903d629a4ff17b06efb65c55c497083d6004cec4db4974a270cf773-7.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=9ccbc7932dfd52d5e061fca94e06de46" alt="Interface screenshot showing configuration options" width="512" height="233" data-path="images/guides/admin-guide/environments/drift-detection/88471782e903d629a4ff17b06efb65c55c497083d6004cec4db4974a270cf773-7.png" />
</Frame>

1. ### On The Deployment Page

The 'Drifts' tab on a drifted deployment page shows a list of the different drift causes env zero checks for, as well as the check's status. The drift cause check results will appear on the right.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/1abee4d5c9d8af0bbef61f25e456902c25293d59a84ed4614796e6f063b74766-8.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=8f87435d7c2fd66fb17609ccb3b568cc" alt="Interface screenshot showing configuration options" width="512" height="245" data-path="images/guides/admin-guide/environments/drift-detection/1abee4d5c9d8af0bbef61f25e456902c25293d59a84ed4614796e6f063b74766-8.png" />
</Frame>

Below it you will see the changed resources list and what changed. You will also be able to get the resource's events by pressing the 'Analyze Drift Cause' button.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/drift-detection/212b9c0b7abbe1a5e0c11b6a08817f775978682654184ac76b5fa0220b5cdea2-9.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=bd1cd54f716816ee01eb1dcebaff7e59" alt="Interface screenshot showing configuration options" width="512" height="106" data-path="images/guides/admin-guide/environments/drift-detection/212b9c0b7abbe1a5e0c11b6a08817f775978682654184ac76b5fa0220b5cdea2-9.png" />
</Frame>

<Info>
  **Reasons Drift Cause won't be able to show events for resource**

  There are several reasons why events will not be available:

* A missing resource ID, which can happen for a number of reasons:
  * An old agent is being used
  * The drift reason is a resource being manually deleted
* Unsupported provider, as detailed above
* A user is missing the View Drift Cause permission
</Info>

Built with [Mintlify](https://mintlify.com).
