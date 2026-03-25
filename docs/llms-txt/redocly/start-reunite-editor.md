# Source: https://redocly.com/docs/realm/get-started/start-reunite-editor.md

# Get started with the Reunite editor

Use the Reunite editor to create, edit, and manage content in your Redocly project directly from your browser.
This guide shows you how to create your first project, add content, customize navigation, and publish changes.

## Before you begin

Make sure you have the following:

- a [Redocly account with an organization](https://auth.cloud.redocly.com/registration)
- a project that uses the **Starter** template in your Reunite organization
See: [Create a project](/docs/realm/reunite/project/manage-projects#create-a-project) for instructions on creating a project.


## Create a branch

details
summary
Learn more about branches
Reunite uses Git for version control, which means changes are made on development branches and are introduced to the main branch of the project through pull requests.

*Branches* are copies where you can make changes to the project without affecting the production project until you are ready.
If you want changes from a branch to be added to the production project, you merge a pull request.

Before you make any changes to your project, create a new branch.
This new branch is a place where you can make changes without affecting the published site until you are ready.
After you have iterated on your changes based on reviews by your team and the updates have been approved, you can merge your changes into the published site.

To create a new branch:

1. From the Reunite editor, click the name of the current branch at the top of the page.

2. Enter the name for your new branch, for example `new-dev-branch`, and select **Create branch**.
Reunite automatically replaces spaces with hyphens `-`because spaces are not allowed in branch names.


## Add content to the landing page

By default, the landing page for each directory in your project is either an `index.md` or `index.page.tsx` file.
New projects in Reunite come with a landing page file.

Replace the content in the current landing page file.
Add your own content or use the following sample Markdown:

details
summary
Example content

```markdown index.md
# Start something new

There's a real excitement to starting something new.

- A blank page
- A fresh opportunity
- Limitless potential

## Good for writers

Writers need strong tooling so they can deliver a lot of content in a short time.
Efficiency is key, so this platform supports [Markdoc](https://markdoc.dev/) format (it's a lot like Markdown, but with added niceness).

Build-in link checking and branch previews lets writers move quickly and safely when creating content or managing updates.

## Good for readers

Clean layout and a visible table of contents makes good content a pleasure to read and process.
```

The content can be a Markdown file with all the supported features of Markdoc, a React file, or an API description (such as an OpenAPI, GraphQL, or AsyncAPI description).

Learn more about [Markdown in Redocly](/docs/realm/content/markdown) for all formatting options, or see [Use the editor](/docs/realm/reunite/project/use-editor) for details about the editor toolbar and features.

Now that you have added some content to your landing page, you can preview your project.

Autosave
The Reunite editor automatically saves your changes as you make edits to your files.

## Preview your changes

Reunite includes a webview pane where you can view your changes as you make them in the editor.

Preview how your changes look in a sample build before publishing to production.

### In the live webview pane

The Webview pane shows formatting updates to ensure they render correctly before you publish.

Screenshot of Webview preview pane
Change the view to meet your needs, such as seeing how the landing page renders on mobile screens.
See [Use the Webview](/docs/realm/reunite/project/use-webview) to learn more about the options you have when using this webview pane.

### In the deployment preview

Reunite creates deployment previews for all branches that have an open pull request.
The deployment preview includes all changes you have committed to your branch.

details
summary
Learn more about pull requests
Reunite uses *Git* for *version control*, which means changes are made on *development branches* and are introduced to the *main branch* of the project through *pull requests*.

Before you can open a pull request, you must make a commit to your development branch.
A *commit* is a way of storing your changes to the branch in Git.
You can continue to make updates to your branch and make additional commits.

After you have committed, you can [open a pull request](/docs/realm/reunite/project/pull-request/open-pull-request) with your commits.
*Pull requests* show the differences between your branch and the main branch.
They run checks for broken links, create deployment preview builds, and allow team members to review changes before merging.

To see a preview build of your project:

1. Commit your updates.
Steps to commit
2. After you commit changes to the branch, open a pull request.
Steps to open a pull request
3. Click the **Preview** button in the top right corner of the page.
You might need to wait until the deployment completes before you can access the preview deployment,
otherwise you will be redirected to the deployment details page.



A deployment preview of the project with your changes opens in a separate browser window.

## Add more pages

Now that you have updated the `index.md` page and seen a deployment preview, let's return to the editor to make some more changes to your project.
To return to the editor, click **Editor** in the navigation pane on the left side of the page.
If you only see icons, you may need to click the "greater than" symbol to expand the navigation pane.

Since a single Markdown page isn't very exciting, we should add a few more.
Using the following steps, create the following two new files:

- `style-guide.md`
- `about.md`


To create a new Markdown file:

1. Click the **+** icon in the top right corner of the file tree in your editor.

2. Select **New file**.
3. Enter the file name into the text field and press `return` or `enter` on your keyboard.


Add your own content to the Markdown files or use the following example content:

details
summary
Example content

```markdown style-guide.md
# Style guide

10-second style guide:

- Please write in sentences.
- Use bullet lists, tables, and subheadings to break up the text.
- Every page needs links to other interesting pages.
- Never use future tense.
```


```markdown about.md
# About

This is an _excellent_ project.
You will learn **all** the things.
```

Tip
You can turn on word wrap in the editor by selecting the **More actions** menu in the top right corner of the editing pane and selecting **Word wrap**.

Screenshot showing word wrap option in the editor in Reunite
## Customize the sidebar navigation

When you add more files to your project, a link to those files is automatically added to the generated sidebar navigation menu.
This generated sidebar is based on the file structure of your project and requires an `index.md` file at the root of your project, in other words, not in a folder.

Where is the sidebar?
The sidebar navigation menu usually displays on the left side of the page in the Webview; however, when the Webview pane is a small width, it is hidden under a slide drawer menu icon that displays in the top right of the Webview pane.

Screenshot that shows the slide drawer icon in the top right corner of the Webview panel
To customize the sidebar navigation for your project, you need to add and configure a new file named `sidebars.yaml` to the root of your project.

### Add a `sidebars.yaml` file

The `sidebars.yaml` file gives you control over the sidebar navigation menu.
You add it as you would any new file.
It must be named `sidebars.yaml`.

To add a `sidebars.yaml` file to your project:

1. Click the **+** icon in the top right corner of the file tree in your editor.\

2. Select **New file**.
3. Enter the `sidebars.yaml` as the file name into the text field and press `return` or `enter` on your keyboard.


Now that you have added a `sidebars.yaml` file to your project, you can configure it.

### Configure the `sidebars.yaml` file

After you have added a `sidebars.yaml` file to your project, you need to add to it the pages and links you want included in your sidebar navigation using YAML syntax.

Add the following sample configuration to your `sidebars.yaml` file:


```yaml sidebars.yaml
- page: index.md
  label: Home
- page: style-guide.md
- page: about.md
- group: Museum API
  items:
    - page: ./openapi.yaml
```

The sample configuration adds the index page, with the link text "Home", your new Markdown pages, using the first heading as the link text, and the Museum API reference documentation, generated from the OpenAPI file.

After adding a `sidebars.yaml` file to a project, any pages you want listed in your sidebar navigation, must be included in the `sidebars.yaml` file.

Now that you have more pages and a sidebar to customize the navigation for those pages, let's update the look and feel of your project to better reflect your brand.

## Add a logo

One way to customize your project to better reflect your brand is by updating the logo.
To update the logo, you need to add a logo image file to your project, and add a `logo` configuration to the `redocly.yaml` file.

### Add an image file

Images should be stored in `images` folders close to the content where they are referenced.
Use multiple `images` folders throughout your project.
For this task, we need an `images` folder at the root of the project.

For the following steps, you can use your own image or download the following sample logo image:

details
summary
Download a sample logo image
To use the Redocly logo:

1. Right-click on the image.
2. Select **Save Image As...**.
3. Enter `logo.png` as the name for the image.
4. Select where you want to save the image.
5. Click **Save**.


Redocly logo
To add an image file to your project, drag the logo image file from where it is located on your computer and drop it into your `index.md` file.
Afterward, a correctly formatted image Markdown tag is added to your `index.md` file.
Also, the image is automatically saved to an automatically generated `images` folder at the root of your project.

### Add a `logo` configuration

Now that you have your logo added to the `images` folder in your project, you can configure the `logo` option in the `redocly.yaml` configuration file.

To add a `logo` configuration:

1. Select the `redocly.yaml` configuration file in the file tree.
2. Copy and paste the following configuration into the file using the editor:

```yaml redocly.yaml
logo:
  image: ./images/logo.png
  link: /
```
If you used a different image or updated the logo name - update the file path in the configuration to reflect your changes.


The logo updates immediately in the webview pane.
If you don't see your changes, try refreshing the webview pane by clicking the [Reload](/docs/realm/reunite/project/use-webview#reload) button.
You can also commit your update to view it [in the preview build](#in-the-deployment-preview).

## Update styles

Customize your project's appearance using [CSS variables](/docs/realm/branding/customize-styles).
Create a `@theme/styles.css` file to override the default styling.

### Create a `@theme` folder

1. Click the **+** icon in the top right corner of the file tree.

2. Select **New folder**.
3. Enter `@theme` and press `return`.


### Create a `styles.css` file

1. Right-click on the `@theme` folder.
2. Select **New file**.
3. Enter `styles.css`.


### Add CSS variables

Add the following to your `styles.css` file to change the heading color:


```css @theme/styles.css
:root {
   --heading-text-color: red;
}
```

Use hexadecimal codes, rgba values, or HTML color names.
The editor includes a color picker when you hover over color values.

Screenshot of the color picker tool in the Reunite editor
The headings' color updates immediately in the live webview pane.
If you don't see your changes, try restarting Webview by clicking the [Reload](/docs/realm/reunite/project/use-webview#reload) button.
You can also commit your update to view it [in the preview build](#in-the-deployment-preview).

## Resources

- **[Sidebars configuration](/docs/realm/navigation/sidebars)** - Configure `sidebars.yaml` with nested items and groups for custom navigation structure
- **[CSS variables dictionary](/docs/realm/branding/css-variables)** - Complete reference for customizing colors, fonts, spacing, and visual styling
- **[Configure Redocly](/docs/realm/config)** - All configuration options available in the `redocly.yaml` file for project customization
- **[User profile menu](/docs/realm/reunite/user-profile-menu)** - Manage notification settings, Git provider connections, and Reunite appearance preferences
- **[Markdown overview for technical writers](https://redocly.com/learn/markdoc)** - Learn Markdoc syntax for adding interactive elements to your documentation