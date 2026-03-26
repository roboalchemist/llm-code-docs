# Source: https://docs.infrahub.app/development/docs.md

# Documentation guide

Welcome to the Infrahub documentation guide. This document aims to answer any questions that may come up when creating or updating documentation.

## Base prerequisites[​](#base-prerequisites "Direct link to Base prerequisites")

| Prerequisite Tool(s)                | Post Installation Steps |
| ----------------------------------- | ----------------------- |
| [Python](https://www.python.org/)   |                         |
| [Invoke](https://www.pyinvoke.org/) |                         |
| [uv](https://docs.astral.sh/uv/)    | `uv sync --all-groups`  |

## Frontend prerequisites[​](#frontend-prerequisites "Direct link to Frontend prerequisites")

| Prerequisite Tool(s)                                            | Post Installation Steps |
| --------------------------------------------------------------- | ----------------------- |
| [Node.js (and npm)](https://nodejs.org/en)                      | `docs.install`          |
| [Vale](https://vale.sh/)                                        |                         |
| [Markdownlint-cli2](https://github.com/DavidAnson/markdownlint) |                         |

Supported Node versions: `22`.

## Working with the docs site locally[​](#working-with-the-docs-site-locally "Direct link to Working with the docs site locally")

The recommended way to run and build the docs locally is with Infrahub's suite of `invoke`-driven tasks.

Use the Invoke tasks to build the documentation and generate source code derived documentation.

```
invoke docs.build docs.generate
```

Once the documentation has been built, make sure to validate the documentation.

```
invoke docs.validate
```

After the documentation has been validated, it can be served locally on port **3000**.

```
invoke docs.serve
```

[Explore the local documentationhttp://localhost:3000/](http://localhost:3000/)

To see more documentation Invoke tasks use the help functionality.

```
invoke -l docs
```

```
Available 'docs' tasks:

  .build                   Build documentation website.
  .format                  This will run all formatter.
  .format-markdownlint     Run markdownlint-cli2 to format all .md/mdx files.
  .generate                Generate all documentation output from code.
  .generate-bus-events     Generate documentation for the Bus events.
  .generate-infrahub-cli   Generate documentation for the infrahub cli.
  .generate-infrahubctl    Generate documentation for the infrahubctl cli.
  .generate-python-sdk     Generate documentation for the Python SDK.
  .generate-repository     Generate documentation for the repository configuration file.
  .generate-schema         Generate documentation for the schema.
  .install                 Install documentation dependencies.
  .lint                    This will run all linter.
  .markdownlint
  .serve                   Run documentation server in development mode.
  .vale                    Run vale to validate the documentation.
  .validate                Validate that the generated documentation is committed to Git.
```

## Writing documentation with AI[​](#writing-documentation-with-ai "Direct link to Writing documentation with AI")

We are increasingly using AI to assist developers in writing technical documentation. To ensure consistency, we maintain a set of instructions that guide the AI when generating documentation for Infrahub.

You can find these instructions in the `.github/instructions/documentation.instructions.md` file.

warning

This process is experimental. We are evaluating available options and will refine the process as we learn more.

### Example use cases and prompts[​](#example-use-cases-and-prompts "Direct link to Example use cases and prompts")

Below are some examples of how to use AI to write documentation. These are not exhaustive, but should give you a good starting point.

* **Writing new documentation**: `Write a new documentation guide about [feature]. You can find the existing topic in [topic file]. The feature works like this: [description]. Make sure to include examples for [graphql, cli, etc.].`
* **Updating existing documentation**: `We recently changed [this feature] to include [change]. Identify the documentation that needs to be updated and update it accordingly.`
* **Assessing documentation quality**: `Review the documentation in [folder], evaluate it against our guidelines, and draft a report prioritizing which pages need updates.`

### General guidelines[​](#general-guidelines "Direct link to General guidelines")

* Always use the `.github/instructions/documentation.instructions.md` file as your reference when writing documentation.
* We have not yet committed to a specific LLM, so you may use the one you prefer.
* Treat AI-generated documentation as a starting point. Always review and refine the content to ensure it meets our standards and accurately reflects the intended message.
* Provide clear, specific prompts to the AI. The more context and detail you give, the better the output will be.

### Using an IDE[​](#using-an-ide "Direct link to Using an IDE")

success

Using an agent like GitHub Copilot, Cursor, or windsurf in your IDE improves the documentation writing experience. These tools can access files directly and provide better context.

Example steps using GitHub Copilot in VSCode:

* Open a chat with GitHub Copilot.
* Add the `.github/instructions/documentation.instructions.md` file to the chat context.
* Prompt the AI to perform tasks on documentation files.
* Depending on the task, switch between `Ask`, `Edit`, and `Agent` modes.

### Using a web interface[​](#using-a-web-interface "Direct link to Using a web interface")

If you prefer a web interface, more manual work is required.

Example steps using OpenAI's ChatGPT:

* Create a new project dedicated to writing documentation for Infrahub.
* Copy the instructions from `.github/instructions/documentation.instructions.md` into the project.
* Copy the content of reference files (`docs/docs/development/docs.mdx`, `.vale/styles/`, `.markdownlint.yaml`) into the project.
* Prompt the AI to perform documentation tasks.
* Copy the generated content into the appropriate `.mdx` file in the `docs/docs` folder.

warning

Update the instructions and reference files in your project whenever they change in the repository.

## Linting and automation[​](#linting-and-automation "Direct link to Linting and automation")

Infrahub uses [Vale](https://vale.sh) to check grammar, style, and word usage. You can find Vale's configuration in `.vale.ini`, and the Infrahub styles located in `.vale/styles/Infrahub`.

[Markdownlint](https://github.com/DavidAnson/markdownlint) is used to encourage consistent markdown files, and Infrahub's configuration is located at `.markdownlint.yaml`.

Most Vale warnings match up with the [style guide](/development/style-guide.md) explanations. Other warnings often fall into the `Infrahub.spelling` rule. These are caused by misspellings, product names, names of people, or otherwise unknown technical terms. See the [procedures for updating rules](#spelling-errors) below for details on adding terms to the approved list.

### Install VS Code linting extensions[​](#install-vs-code-linting-extensions "Direct link to Install VS Code linting extensions")

It is preferred to install extensions into VSCode so that you can see the visual errors and fix them as you write documentation.

* [Vale](https://marketplace.visualstudio.com/items?itemName=chrischinchilla.vale-vscode)
* [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

### Disabling Vale and markdownlint[​](#disabling-vale-and-markdownlint "Direct link to Disabling Vale and markdownlint")

You can disable Vale and markdownlint in-line with the following markdown comments:

```
<!-- vale off -->
Ignored Specialized Phrase ignored by vale
<!-- vale on -->

<!-- markdownlint-disable -->
## Ignored markdown line
<!-- markdownlint-restore -->
```

This is useful in situations where specific style choices or markdown quirks force the use of an otherwise conflicting rule. In general, it is better to update existing configurations or create new rules rather than disable scanning of individual files.

### Creating new Vale rules[​](#creating-new-vale-rules "Direct link to Creating new Vale rules")

For questions regarding how to add to or update an existing rule, see the [Vale styles documentation](https://vale.sh/docs/topics/styles/). A wealth of examples are also available in [GitLab's vale configuration](https://gitlab.com/gitlab-org/gitlab/-/tree/master/doc/.vale/gitlab).

#### Spelling errors[​](#spelling-errors "Direct link to Spelling errors")

If Vale warns of a spelling mistake and the word is valid, you can fix it by updating the `spelling-exceptions.txt` file in the `.vale/styles/` directory. When adding a new term, update and alphabetize the list to make future scanning easier.

#### Common replacement words[​](#common-replacement-words "Direct link to Common replacement words")

Add common shorthand words and phrases that have better alternatives to the `swap.yml` rule. For example, `repo` becomes `repository`.

Add special case capitalization words to the `branded-terms-case-swap.yml` rule. For example, `hooli` becomes `Hooli`.

## Writing markdown[​](#writing-markdown "Direct link to Writing markdown")

Pages are written in MDX, which is a enhanced version of markdown or generated by the app source.

In addition, Docusaurus has its own [markdown-inspired components](https://docusaurus.io/docs/markdown-features). You'll often find reference links, panels, and snippets used throughout the Infrahub docs.

### Markdown tips[​](#markdown-tips "Direct link to Markdown tips")

#### Ensure proper newlines[​](#ensure-proper-newlines "Direct link to Ensure proper newlines")

Use two full returns between paragraphs (one empty line). This ensures a new paragraph is created.

#### Notification blocks[​](#notification-blocks "Direct link to Notification blocks")

When writing documentation, it's essential to guide the reader's attention to specific types of information. Notification blocks are a powerful tool to achieve this, allowing you to highlight information based on its nature and importance. Here are the types of notification blocks and how to use them:

* **Info:** Use info blocks for additional, helpful information that isn't required to complete the task but offers more context or useful tips.

  ```
  :::info
  ```

  **Example**

  This feature is available in version 2.1 and later.

* **Success:** Use success blocks to highlight expected outcomes and "status checks" to ensure the reader is on track with the guide. These blocks can reinforce the reader's progress and provide positive feedback.

  ```
  :::success
  ```

  **Example**

  If you've followed the steps correctly, your installation should now be complete.

* **Warning:** Warning blocks should be used to highlight common errors or mistakes that may occur during the process. They serve as preventive measures to help the reader avoid potential pitfalls.

  ```
  :::warning
  ```

  **Example**

  Ensure you've backed up your files before proceeding with this step to prevent data loss.

* **Danger:** Use danger blocks to highlight irreversible or breaking actions. These notifications are critical for steps that could significantly affect the system or data if mishandled.

  ```
  :::danger
  ```

  **Example**

  This action will permanently delete your data and cannot be undone.

Incorporating these blocks into your documentation makes it more interactive and user-friendly, guiding the reader through different stages of their learning or implementation process with visual cues that emphasize the significance of each piece of information.

## Documentation sync to `infrahub-docs`[​](#documentation-sync-to-infrahub-docs "Direct link to documentation-sync-to-infrahub-docs")

Infrahub documentation is synced and ultimately published via the [`infrahub-docs`](https://github.com/opsmill/infrahub-docs) repository. This is done via the GitHub action `.github/workflows/sync-docs.yml`.

Please note the following important points:

* Today, spelling (the `.vale` directory) is authoritative in the `infrahub` repository, not the `infrahub-docs` repository. If you need to add a spelling exception in another repository (i.e. `infrahub-demo-dc`), you have to add the exception to the `infrahub` repository.

* All documentation URLs need to be relative:

  <!-- -->

  * Do this: `[some page](../path/to/file.mdx)`
  * Not this: `[some page](/absolute_path/to/file)`

## Organizing new pages[​](#organizing-new-pages "Direct link to Organizing new pages")

We organize all documentation into **four** categories: tutorials, guides, topics, and reference. This is heavily influenced by the [Diátaxis framework](https://diataxis.fr/). The goal is to maintain a more organized, understandable set of docs.

Here are questions to ask when deciding where to place a new document:

* Are you walking the user through a scenario? Select **Tutorials**.
* Are you providing steps to complete a specific task? Select **Guides**.
* Are you providing background information, explanation, or abstract concepts? Select **Topics**.
* Are you providing APIs, command references, or concise reference information? Select **Reference**.

If you're unsure where something goes, diátaxis offers a [map](https://diataxis.fr/map/) and [compass](https://diataxis.fr/compass/) to help.

When creating a new page in the documentation, in addition to creating the `.mdx` file containing the documentation itself, you must also add the page to the relevant section of the `sidebars.ts` file.

### Tutorials[​](#tutorials "Direct link to Tutorials")

Tutorials are an opportunity to guide users through a repeatable process. The purpose is to **provide basic competence** in Infrahub or a feature-set.

They should:

* Introduce the user to the end goal.
* Be repeatable by any user.
* Describe practical steps, rather than abstract concepts.
* Provide immediate results.

The "Getting started" tutorial is a good example, as it walks the user through a scripted scenario in a demo environment.

For a deeper dive into tutorials, refer to the [diátaxis tutorials page](https://diataxis.fr/tutorials/).

> Tutorials are complex learning endeavors. Before deciding if a tutorial is necessary, consider how you might update an existing tutorial or if a guide would be a better option.

### Guides[​](#guides "Direct link to Guides")

Guides may seem like tutorials, but they are a shorter set of universal instructions that can apply to any user's task. The purpose is to **teach how to perform a specific task**.

**Naming guideline:** Describe the task that the guide describes, preferably in 2-5 words.

For example:

* Installing Infrahub
* Creating new devices
* How to invite collaborators

For a deeper dive into guides, refer to the [diátaxis guides page](https://diataxis.fr/how-to-guides/).

### Topics[​](#topics "Direct link to Topics")

Sometimes called *explanations*, topics offer additional context and rationale into the workings of Infrahub. They should answer the question: "how does X work?"

**Naming guideline:** Write the topic name, but not a sentence.

For example:

* Artifact
* User management and authentication

Begin by giving a one to two sentence description of the topic, then dive in deeper as needed.

For a deeper dive into topics, refer to the [diátaxis explanations page](https://diataxis.fr/explanation/).

### Reference[​](#reference "Direct link to Reference")

Reference docs serve a single purpose. To provide quick, clear information when a user needs it. The intention is not that users *read* the reference, but instead they *consult* it as needed when working with Infrahub.

**Naming guidelines:** Mirror the code-level naming guidelines where possible. This makes it easier to connect docs to code quickly.

For a deeper dive into reference docs, refer to the [diátaxis reference page](https://diataxis.fr/reference/).

## Application screenshots[​](#application-screenshots "Direct link to Application screenshots")

To ensure that Infrahub's screenshots remain up to date and to check that our guides work properly, we use [end-to-end (e2e) tests](/development/frontend/testing-guidelines.md#e2e-tests). You'll find the e2e tests specifically designed for tutorials located in `frontend/app/tests/e2e/tutorial`.

### Updating all screenshots manually[​](#updating-all-screenshots-manually "Direct link to Updating all screenshots manually")

#### 1. Start with a fresh data environment[​](#1-start-with-a-fresh-data-environment "Direct link to 1. Start with a fresh data environment")

Start with fresh demo data each time you want to take new screenshots, as the tests are not idempotent. This ensures consistency across screenshots.

```
invoke dev.destroy dev.start dev.load-infra-schema dev.load-infra-data dev.infra-git-import dev.infra-git-create
```

#### 2. run the e2e tests[​](#2-run-the-e2e-tests "Direct link to 2. run the e2e tests")

E2E test commands are accessible through inside the `frontend/app` directory. To run the tests with screenshots, execute:

```
cd frontend/app
npm run test:e2e:screenshots
```

info

By default, tests are run in headless mode. To run them in a visible browser, use `npm run test:e2e:screenshots:headed` instead.

#### 3. Check the results[​](#3-check-the-results "Direct link to 3. Check the results")

The screenshots will be saved in `docs/docs/media`. You can then use them in our documentation:

```
![optional caption](../../media/my-screenshot-name.png)
```

### Add a screenshot[​](#add-a-screenshot "Direct link to Add a screenshot")

#### 1. Locate on which test the screenshot should be added[​](#1-locate-on-which-test-the-screenshot-should-be-added "Direct link to 1. Locate on which test the screenshot should be added")

If the test does not exist yet, create must create it first. Refer to the [write e2e tests](/development/frontend/testing-guidelines.md#writing-e2e-tests) for more information.

#### 2. Add the screenshot[​](#2-add-the-screenshot "Direct link to 2. Add the screenshot")

To add a new screenshot in the documentation, use this command within the tutorial e2e test:

```
await saveScreenshotForDocs(page, "my-screenshot-name");
```

You can also organize your screenshots using folders, by specifying the folder name like this:

```
await saveScreenshotForDocs(page, "my-folder/my-screenshot-name" );
```

## Documentation release checklist[​](#documentation-release-checklist "Direct link to Documentation release checklist")

Before publishing new changes to documentation, complete the following tasks:

* <!-- -->

  Generate output files for automated pages with `invoke docs.generate`.

  <!-- -->

  * <!-- -->
    Confirm build of `infrahubctl` pages.
  * <!-- -->
    Confirm build of `infrahub-cli` pages.
  * <!-- -->
    Confirm build of schema pages.

* [ ] [Update application screenshots](#updating-all-screenshots-manually).

* <!-- -->
  If there is a new app version, create a new release notes document in `docs/release-notes`.

* <!-- -->
  Run [linters](#linting-and-automation) and fix valid errors on all source files.

* <!-- -->
  Perform test build of docs, `invoke docs.build`.
