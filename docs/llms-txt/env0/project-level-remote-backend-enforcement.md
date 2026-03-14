# Source: https://docs.envzero.com/changelogs/2023/05/project-level-remote-backend-enforcement.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🎛️ Project-Level Remote Backend Enforcement

> Have you taken the env0 Remote Backend Terraform for a spin? You would probably want all of your project's Terraform environments to be created with the env0 remote backend. Now you can! Introducing our brand new project-level `Force env0 Remote Backend` policy that lets you enforce the use of the env0 remote backend throughout your project.

Have you taken the env0 Remote Backend Terraform for a spin? You would probably want all of your project's Terraform environments to be created with the env0 remote backend. Now you can! Introducing our brand new project-level `Force env0 Remote Backend` policy that lets you enforce the use of the env0 remote backend throughout your project.

## ✨ Setting The Policy ✨

Simply go over to your project's settings -> policies:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/05/fccc06a-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=3672e31f9cc82894883efe38fee1408d" alt="Feature demonstration screenshot showing new functionality" width="974" height="464" data-path="images/changelogs/2023/05/fccc06a-image.png" />
</Frame>

Tick the `Force env0 Remote Backend` checkbox & save:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/05/c3ab018-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=0c179618c2719c1acfe2aae187915d69" alt="Feature demonstration screenshot showing new functionality" width="789" height="274" data-path="images/changelogs/2023/05/c3ab018-image.png" />
</Frame>

Now, every *new* Terraform environment, in this project, will be forced to have a remote state. See the ticked & blocked `Use env0 Remote Backend` checkbox in the environment creation view below:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/05/f3e1faa-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=aaa81472db9894e70435e713c2a80e30" alt="Feature demonstration screenshot showing new functionality" width="744" height="248" data-path="images/changelogs/2023/05/f3e1faa-image.png" />
</Frame>

For more information see [this](/guides/policies-governance/force-remote-backend)

Built with [Mintlify](https://mintlify.com).
