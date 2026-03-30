# Source: https://docs.envzero.com/changelogs/2024/11/custom-flows-for-tasks.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 📝 Custom Flows For Tasks

> With this update, you can now configure custom hooks for your tasks, allowing you to define specific setups and teardowns for all ad-hoc tasks.

[Tasks](/guides/admin-guide/environments/ad-hoc-tasks) now support [custom flows](/guides/admin-guide/custom-flows)!

With this update, you can now configure custom hooks for your tasks, allowing you to define specific setups and teardowns for all ad-hoc tasks.

For example, if you want to set up specific credentials for all running tasks, you can create an additional step called "Setup Credentials" using custom hooks and configure the credentials as needed.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/11/8bd913eee21ce546f5e77bcd8edc61e0c7c66f475da35ea6b1ed0e94779f3db3-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=4122af96028f9844ca7113f13e54970c" alt="Feature demonstration screenshot showing new functionality" width="1427" height="673" data-path="images/changelogs/2024/11/8bd913eee21ce546f5e77bcd8edc61e0c7c66f475da35ea6b1ed0e94779f3db3-image.png" />
</Frame>

You can learn more about the available hook options [here](/guides/admin-guide/custom-flows#hook-stages).

Please note that your custom flows could be set up individually, by creating an \*\*env0.yml \*\*file with the rest of your configuration, or by using a global policy that will be set on every environment in your project.

Visit  [here](/guides/admin-guide/custom-flows/project-level-custom-flow) to learn more about setting up project-level custom flows.

Built with [Mintlify](https://mintlify.com).
