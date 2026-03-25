# Source: https://docs.envzero.com/guides/admin-guide/variables/variable-sets.md

# Source: https://docs.envzero.com/changelogs/2024/05/variable-sets.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 📦 Variable Sets

> We are excited to announce the release of Variable Sets! Variable Sets are designed to enhance configuration management within env zero. With Variable Sets, users can organize and manage frequently used or closely related variables with ease, streamlining workflows and promoting consistency across projects. For example, you might have multiple environments across different projects that spin up an RDS instance, you can create a Variable Set with all of the necessary shared configuration (such as the "instance type", "engine" and so on) and use that Set in every environment that requires those variables. Create once and reuse wherever needed.

We are excited to announce the release of Variable Sets! Variable Sets are designed to enhance configuration management within env zero. With Variable Sets, users can organize and manage frequently used or closely related variables with ease, streamlining workflows and promoting consistency across projects.

For example, you might have multiple environments across different projects that spin up an RDS instance, you can create a Variable Set with all of the necessarily shared configurations (such as the "instance type", "engine" and so on) and use that Set in every environment that requires those variables. Create once and reuse wherever needed.

Variable Sets can be defined at the Organization level, making them accessible to all entities within env zero, or at the Project level, allowing for more granular control within specific projects and their sub-entities

Creating a new Variable Set is intuitive and straightforward. Simply navigate to the Organization/Project Variables page, switch to the `SETS` tab and click on the `CREATE NEW SET` button, fill in the Set's name and variables, and you're ready to go.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/05/213e63a-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=d4f451bd1defb56458e884bb95a6175e" alt="Variable Sets creation interface showing the SETS tab with CREATE NEW SET button" width="1430" height="591" data-path="images/changelogs/2024/05/213e63a-image.png" />
</Frame>

Variable Sets can be assigned to Organizations, Projects, Templates, Workflows, or Environments, providing seamless integration into your existing workflows. Use the selector within the variables table to mark the sets you wish to use.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/05/57a5d67-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=5e2ceb716a521773e3a7c6d937adc6bb" alt="Variable Sets assignment interface showing selector checkboxes for Organizations, Projects, Templates, Workflows, and Environments" width="1416" height="353" data-path="images/changelogs/2024/05/57a5d67-image.png" />
</Frame>

Like any other variable in env zero, you can easily override variables within a Variable Set. Simply navigate to the Variable Set's group in the variables table and edit the variable's value as needed.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/05/5bd71dd-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=6262bf6db59a7355ec6f26e3b77f6348" alt="Variable Set override interface showing how to edit variable values within a Variable Set group" width="1425" height="404" data-path="images/changelogs/2024/05/5bd71dd-image.png" />
</Frame>

For more info, read about [Variable Sets](/guides/admin-guide/variables/variable-sets).

Built with [Mintlify](https://mintlify.com).
