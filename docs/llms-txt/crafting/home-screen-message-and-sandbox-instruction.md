# Source: https://docs.sandboxes.cloud/docs/home-screen-message-and-sandbox-instruction.md

# Home screen message and sandbox instruction

As each engineering team has their own workflows and practices, they typically have some documentation on how each developer follows the workflows and practices. As a development platform, Crafting often has its own user guide somewhere in teams wiki or notion pages. Even though it's good to have out-of-band comprehensive documentation, it's better to have some key custom messages inline for every developer to keep in mind.

Crafting provides this type messaging support on two levels: *Home screen message* and *Sandbox instructions*. Both of them use *Markdown* syntax and it's easy for the dev environment admin to edit. In this page, we talk about how to use them.

### Home screen message

The home screen message is shown on the home page of Crafting web console (dashboard) for an organization to broadcast to every member of the team visiting the platform. Given it's on the first page a developer sees before doing anything on the platform, the following information is often put there:

* How to set up and onboard a developer to Crafting, e.g. git access, personal customization, dev credentials, etc., and links to detailed instructions.
* Best practices for the developers.
* Brief information on which template is for what purpose.

You can edit the message right on the Home page by clicking the `Customize` button on the top right corner. Only *Admins* can edit the message.

<details>
  <summary>Image</summary>

  <img src="https://files.readme.io/fd0e17f-image.png" align="center" style={{ border: "true" }} />
</details>

**Overview** is a markdown snippet associated with either an org or a template, each serving a different purpose. Additionally, you can inject runtime variables with double curly brackets. An overview of an organization and an app support different variables, and an unknown variable will be parsed as an empty string if referenced.

### Sandbox instructions

The `Sandbox instruction` is used to provide information on how sandboxes from a particular template should be used and offer short-cuts for developers to use the sandbox. It's defined in the template, and the instruction will be rendered on the sandbox page for all sandboxes created from that template.

<details>
  <summary>Image</summary>

  <img src="https://files.readme.io/3fc271d-image.png" align="center" style={{ border: "true" }} />
</details>

Because you can inject runtime variables with double curly brackets into the sandbox instructions, it can be very useful to directly guide developers to the places according to the runtime information, e.g. URL, hostname, etc. For example, the above message came from the following mark down:

```markdown
This is a sandbox for demo purposes. Visit [this URL]({{endpoints.app.url}}) to see it.
```

*Sandbox instructions* can be customized by open a Template and click the **SANDBOX INSTRUCTIONS** button:

<details>
  <summary>Image</summary>

  <img src="https://files.readme.io/6bb92b9-TemplateDetails.png" align="center" />
</details>

#### Variables and Syntax

For the full details about the variables and syntax, please read [Overview in Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition#overview).

The following is a list of commonly used variables and whether they are supported in org overview or sandbox overview:

| Variable Name                 | Description                                                                                                           | Org       | Sandbox   |
| :---------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :-------- | :-------- |
| org.name                      | The name of current org.                                                                                              | Supported | Supported |
| user.email                    | Email of current user.                                                                                                | Supported | Supported |
| sandbox.name                  | Name of the current sandbox, if applicable.                                                                           |           | Supported |
| sandbox.createdAt             | Sandbox creation time, if applicable.                                                                                 |           | Supported |
| sandbox.updatedAt             | The last updated time of the current sandbox, if applicable.                                                          |           | Supported |
| sandbox.template              | The associated template's name of the current sandbox, if applicable.                                                 |           | Supported |
| sandbox.owner                 | The owner of current sandbox, if applicable.                                                                          |           | Supported |
| endpoints.\[endpoint-name].url | The full URL of an endpoint. If there is no endpoint named as *endpoint-name*, the variable is deemed as unknown one. |           | Supported |
| endpoints.\[endpoint-name].dns | The DNS part of an endpoint. If there is no endpoint named as *endpoint-name*, the variable is deemed as unknown one. |           | Supported |

## Example

```markdown
Sandbox Notes

Sandbox name {{sandbox.name}}
Last updated {{sandbox.updatedAt}}
Owner {{sandbox.owner}}
Template {{sandbox.template}}

For unknown variable, we display {{unknown}}
```

An example rendered result will be as below:

```
Sandbox Notes

Sandbox name sandbox-name
Last updated 2022-01-01
Owner sandbox-user
Template example-template

For unknown variable, we display 
```