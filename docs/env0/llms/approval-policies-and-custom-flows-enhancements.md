# Source: https://docs.envzero.com/changelogs/2024/04/approval-policies-and-custom-flows-enhancements.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 👮‍♂️Approval Policies and Custom Flows Enhancements

Running your Infrastructure as code might be a complicated task that may include running custom scripts and have specific policies to make sure your guardrails are in place. With env0 Custom flows, you can run extra logic (bash, python, gcloud, Ansible, etc.), whenever you want in the deployment process (before or after Terraform init/plan/apply, and even destroy/error). With approval policies, you can run your custom policies to make sure everything is meeting your standards, and according to the output we will cancel, wait for approval from a team member, or continue the deployment.

Now we have enhanced the way our approval policies and custom flows work. Here are some of the new features available:

* A single project can use multiple approval policies, allowing different policies to be organized in separate files. Each can be maintained by a different team or stored at a different location while still applying all of these to the same project.
* Approval policies can now be assigned to a template, this allows enforcing certain policies on the created environments regardless of their location (the project it belongs to).
* It is now possible to execute both project and environment-level custom flows, this allows project admin to use custom flows to run validations and security checks while allowing environments to customize their hooks. Also, project-level custom flows apply on environments that sit under sub-projects, this allows utilizing the project / sub-projects hierarchy to configure custom flows.
* A single project can also use multiple custom flows now allowing different checks/ validations to be organized in separate custom flow files each can be maintained by a different team or stored at a different location while still applying all of these to the same project. You can also easily reorder the custom flows in the table to decide their execution order.

If you are using a self hosted agent with a version earlier than `v3.0.731` you won't have access to the new approval policies enhancements until you upgrade it.

To configure multiple approval policies/custom flows for a project you can go to the project's policies settings page and click the `+Add Custom Flow / Approval Policy` button:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/04/3e647ac-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=65b309c701664fc5c64465265b6699c5" alt="Feature demonstration screenshot showing new functionality" width="2644" height="612" data-path="images/changelogs/2024/04/3e647ac-image.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/04/bfce0f9-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=f74ed6b4f05814a04fd9e73bdf46ffff" alt="Feature demonstration screenshot showing new functionality" width="2636" height="572" data-path="images/changelogs/2024/04/bfce0f9-image.png" />
</Frame>

To configure approval policies for a template you can go to the template's settings page and under the advanced section click the `+Add Approval Policy`button:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/04/041f35c-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=823f259ad48b4acbc1388bfc1fca9c02" alt="Feature demonstration screenshot showing new functionality" width="2636" height="976" data-path="images/changelogs/2024/04/041f35c-image.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
