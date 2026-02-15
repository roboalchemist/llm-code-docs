# Documentation Contributions

**Source:** [https://developer.wordpress.org/block-editor/contributors/documentation/](https://developer.wordpress.org/block-editor/contributors/documentation/)



# Documentation Contributions




## In this article


Table of Contents- Discussions
- Documentation types
- Block editor handbook processHandbook structureTemplatesUpdate a documentCreate a new documentDocumenting packagesUsing linksCode examplesCallout noticesEditor configVideo embeds
- Resources



↑Back to top


A guide on how to get started contributing documentation to the Gutenberg project.


## Discussions


TheMake WordPress Docs blogis the primary spot for the latest information around WordPress documentation, including announcements, product goals, meeting notes, meeting agendas, and more.


Real-time discussions for documentation take place in the#docschannel inMake WordPress Slack(registration required). Weekly meetings for the Documentation team are on Tuesdays at 14:00UTC.


The Gutenberg project uses GitHub for managing code and tracking issues. The main repository is at:https://github.com/WordPress/gutenberg. To find documentation issues to work on, browseissues with documentation label.


## Documentation types


There are two major sets of documentation for the Gutenberg project:


1. User documentationis information on how to use the Editor as an author publishing posts. For contributing to user docs, follow the docs blog or ask in the #docs Slack channel to understand the current priorities.
1. Block editor handbookis everything related to the Gutenberg project including: developing, extending, and—what you are reading right now—contributing specific to Gutenberg.


The rest of this document covers contributing to the block editor handbook.


## Block editor handbook process


The block editor handbook is a mix of markdown files in the/docs/directory of theGutenberg project repositoryand generated documentation from the packages.


An automated job publishes the docs every 15 minutes to theblock editor handbook site.


Seethe Git Workflowdocumentation for how to use git to deploy changes using pull requests. Additionally, see thevideo walk-throughand the accompanyingslides for contributing documentation to Gutenberg.


### Handbook structure


The handbook is organized into four sections based on the functional types of documents.The Documentation Systemdoes a great job explaining the needs and functions of each type, but in short, they are:


- Getting started tutorials– full lessons that take learners step by step to complete an objective, for example thecreate a block tutorial.
- How-to guides– short lessons specific to completing a small specific task, for examplehow to add a button to the block toolbar.
- Reference guides– API documentation, purely functional descriptions,
- Explanations– longer documentation focused on learning, not a specific task.


### Templates


Ahow-to guide templateis available to provide a common structure to guides. If starting a new how-to guide, copy the markdown from the template to get started.


The template is based on examples from The Good Docs Project. See theirtemplate repositoryfor additional examples to help you create quality documentation.


### Update a document


To update an existing page:


1. Check out the Gutenberg repository.
1. Create a branch to work, for exampledocs/update-contrib-guide.
1. Make the necessary changes to the existing document.
1. Commit your changes.
1. Create a pull request using the[Type] Developer Documentationlabel.


### Create a new document


To add a new document requires a working JavaScript development environment to build the documentation, see theJavaScript build setup documentation:


1. Create a Markdown file in thedocsfolder, use lower-case, no spaces, if needed a dash separator, and.mdextension.
1. Add content using markdown notation. All documents require one and onlyh1tag.
1. Add document entry to thetoc.jsonhierarchy. See existing entries for format.
1. Runnpm run docs:buildto updatemanifest.json.
1. Commitmanifest.jsonwith other files updated.


If you forget to run,npm run docs:buildyour PR will fail the static analysis check since themanifest.jsonfile is an uncommitted local change that must be committed.


### Documenting packages


Package documentation is generated automatically by the documentation tool by pulling the contents of the README.md file located in the root of the package. Sometimes, however, it is preferable to split the contents of the README into smaller, easier-to-read portions.


This can be accomplished by creating adocsdirectory in the package and addingtoc.jsonfile that contains references other markdown files also contained in thedocsdirectory. Thetoc.jsonfile should contain an array of pages to be added as sub-pages of the main README file. The formatting follows themanifest.jsonfile that is generated automatically.


In order for these pages to be nested under the main package name, be sure to set theparentproperty correctly. See the example below that adds child pages to the@wordpress/create-blocksection.


```
[
    {
        "title": "@wordpress/create-block External Template",
        "slug": "packages-create-block-external-template",
        "markdown_source": "../packages/create-block/docs/external-template.md",
        "parent": "packages-create-block"
    }
]

```


### Using links


It’s likely at some point, you’ll want to link to other internal documentation pages. It’s worth emphasizing all documents can be browsed in different contexts:


- Block editor handbook
- GitHub website
- npm website


To create links that work in all contexts, you must use absolute path links without the `https://github.com/WordPress/gutenberg` prefix. You can reference files using the following patterns:


- /docs/*.md
- /packages/*/README.md
- /packages/components/src/**/README.md


This way, they will be properly handled in all three aforementioned contexts.


Use the full directory and filename from the Gutenberg repository, not the published path; the Block Editor Handbook creates short URLs—you can see this in the tutorials section. Likewise, thereadme.mdportion is dropped in the handbook but should be included in the links.


An example, the link to this page is:/docs/contributors/documentation/README.md



**Note:** The usual link transformation is not applied to links in callouts. See below.

### Code examples


The code example in markdown should be wrapped in three tick marks ``` and should additionally include a language specifier. See thisGitHub documentation around fenced code blocks.


A unique feature to the Gutenberg documentation is thecodetabstoggle, this allows two versions of code to be shown at once. This is used for showing bothJSXandPlaincode samples.


Here is an examplecodetabssection:


```
    \{\% codetabs \%\}
    \{\% JSX \%\}
    ```js
    // JSX code here
    ```
    \{\% Plain \%\}
    ```js
    // Plain code here
    ```
    \{\% end \%\}

```


The preferred format for code examples is JSX. This should be the default view. The example placed first in source will be shown as the default.


Note:It is not required to include plain JavaScript code examples for every guide. The recommendation is to include plain code for beginner tutorials or short examples, but the majority of code in Gutenberg packages and across the larger React and JavaScript ecosystem are in JSX that requires a build process.


### Callout notices


The Block Editor handbook supports the samenotice styles as other WordPress handbooks. However, the shortcode implementation is not ideal with the different locations the block editor handbook documentation is published (npm, GitHub).


The recommended way to implement in markdown is to use the raw HTML andcallout callout-LEVELclasses. For example:


```
<div class="callout callout-info">This is an **info** callout.</div>

```


The following classes are available:info,tip,alert,warning


```
<div class="callout callout-tip">
This is a **tip** callout.
</div>

<div class="callout callout-info">
This is an **info** callout.
</div>

<div class="callout callout-alert">
This is an **alert** callout.
</div>

<div class="callout callout-warning">
This is a **warning** callout.
</div>

```


Note: In callout notices, links also need to be HTML<a href=""></a>notations.The usual link transformation is not applied to links in callouts.For instance, to reach the Getting started > Create Block page, the URL in GitHub ishttps://github.com/WordPress/gutenberg/blob/trunk/docs/getting-started/devenv/get-started-with-create-block.md/and will have to be hardcoded for the endpoint in the Block Editor Handbook as<a href="https://developer.wordpress.org/block-editor/getting-started/create-block/">https://developer.wordpress.org/block-editor/getting-started/create-block/</a>to link correctly in the handbook.


### Editor config


You should configure your editor to use Prettier to auto-format markdown documents. See theGetting Started documentationfor complete details.


An example config for using Visual Studio Code and the Prettier extensions:


```
"[[markdown]]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true
},

```



Depending on where you are viewing this document, the brackets may show as double. The proper format is just a single bracket.

### Video embeds


Videos in the Block Editor Handbook need to be hosted on theWordPress YouTube channelas unlisted videos. This process requires additional permissions. Reach out in the #marketing Slack channel for assistance.


Once the video has been uploaded to YouTube, retrieve the video embed link. It should look something like this:


```
https://www.youtube.com/embed/nrut8SfXA44?si=YxvmHmAoYx-BDCog

```


Then, place the following code where you want the video to be embedded in the documentation. Update the embed link and video title accordingly.


```
<iframe width="960" height="540" src="[Video embed link]" title="[Video title]" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="true"></iframe>

```



Videos should have an aspect ratio of `16:9` and be filmed at the highest resolution possible.

## Resources


- Copy Guidelinesfor writing instructions, documentation, or other contributions to the Gutenberg project.
- Tone and Voice Guidefrom WordPress Documentation.





First published


March 9, 2021


Last updated


January 16, 2026


Edit article


Improve it on GitHub: Documentation Contributions





[PreviousBlocks are the InterfacePrevious: Blocks are the Interface](https://developer.wordpress.org/block-editor/contributors/design/the-block/)
[NextCopy GuidelinesNext: Copy Guidelines](https://developer.wordpress.org/block-editor/contributors/documentation/copy-guide/)


