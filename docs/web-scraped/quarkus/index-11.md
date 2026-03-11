# Source: https://pages.github.com/

Title: GitHub Pages

URL Source: https://pages.github.com/

Published Time: Wed, 13 Aug 2025 12:02:54 GMT

Markdown Content:
GitHub Pages | Websites for you and your projects, hosted directly from your GitHub repository. Just edit, push, and your changes are live.
===============
[![Image 1: GitHub Pages](https://pages.github.com/images/logo.svg)](https://pages.github.com/)
Websites for you and your projects.
===================================

Hosted directly from your [GitHub repository](https://github.com/). Just edit, push, and your changes are live.
---------------------------------------------------------------------------------------------------------------

[Pages Help](https://help.github.com/pages/)

![Image 2: Bootstrap](https://pages.github.com/images/slideshow/bootstrap.png)

Ready to get started? Build your own site from scratch or generate one for your project.
========================================================================================

You get one site per GitHub account and organization, 

and unlimited project sites. Let‘s get started.
-------------------------------------------------------------------------------------------------------

*   [User or organization site](https://pages.github.com/#user-site)
*   [Project site](https://pages.github.com/#project-site)

*   #### Create a repository

Head over to [GitHub](https://github.com/) and [create a new public repository](https://github.com/new) named _username_.github.io, where _username_ is your username (or organization name) on GitHub.

If the first part of the repository doesn’t exactly match your username, it won’t work, so make sure to get it right.

*   #### What git client are you using?

    *   [A terminal](https://pages.github.com/#terminal-step-1)
    *   [GitHub Desktop](https://pages.github.com/#setup-in-desktop)
    *   [I don't know](https://pages.github.com/#new-user-step-1)

*   #### Download GitHub Desktop

GitHub Desktop is a great way to use Git and GitHub on macOS and Windows.

[Download GitHub Desktop](https://desktop.github.com/)![Image 3: GitHub Desktop screenshot](https://pages.github.com/images/dashboard@2x.png)
*   #### Clone the repository

Go to the folder where you want to store your project, and clone the new repository:

 ~$git clone https://github.com/_username_/_username_.github.io  
*   #### Clone the repository

Click the "Set up in Desktop" button. When the GitHub desktop app opens, save the project.

If the app doesn't open, launch it and clone the repository from the app.

*   #### Clone the repository

After finishing the installation, head back to GitHub.com and refresh the page. Click the "Set up in Desktop" button. When the GitHub desktop app opens, save the project.

If the app doesn't open, launch it and clone the repository from the app.

*   #### Hello World

Enter the project folder and add an index.html file:

 ~$cd _username_.github.io

~$echo "Hello World" > index.html  
*   #### Create an index file

Grab your favorite text editor and add an index.html file to your project:

index.html 
```
<!DOCTYPE html>
<html>
<body>
<h1>Hello World</h1>
<p>I'm hosted with GitHub Pages.</p>
</body>
</html>
``` 
*   #### Push it

Add, commit, and push your changes:

 ~$git add --all

~$git commit -m "Initial commit"

~$git push -u origin main  
*   #### Commit & publish

Enter the repository, commit your changes, and press the publish button.

![Image 4: Demonstration of steps required to create the initial commit and publish the repository in GitHub Desktop](https://pages.github.com/images/desktop-demo@2x.gif)
*   #### …and you're done!

Fire up a browser and go to **https://_username_.github.io**.

 

*   #### Use a theme, or start from scratch?

You have the option to start with one of the pre-built themes, 

or to create a site from scratch.

    *   [Choose a theme](https://pages.github.com/#generate-step-1)
    *   [Start from scratch](https://pages.github.com/#vanilla-step-1)

*   #### Repository Settings

Head over to [GitHub.com](https://github.com/) and create a new repository, or go to an existing one. 

**Click on the Settings tab**.

![Image 5: Settings for a repository](https://pages.github.com/images/repo-settings@2x.png)
*   #### Theme chooser

Scroll down to the **GitHub Pages** section. Press **Choose a theme**.

![Image 6: Automatic Generator button on GitHub.com, Settings](https://pages.github.com/images/launch-theme-chooser@2x.png)
*   #### Pick a theme

Choose one of the themes from the carousel at the top. 

When you're done, click **Select theme** on the right.

![Image 7: Choose layout](https://pages.github.com/images/theme-chooser@2x.png)
*   #### Edit content

Use the editor to add content to your site.

![Image 8: Add content to your GitHub Pages site](https://pages.github.com/images/code-editor@2x.png)
*   #### Commit

Enter a commit comment and click on **Commit changes** below the editor.

![Image 9: Commit Markdown content to your repository](https://pages.github.com/images/commit-edits@2x.png)
*   #### Create an index file

Head over to [GitHub.com](https://github.com/) and [create a new repository](https://github.com/new), or go to an existing one. 

Click on the **Create new file** button.

![Image 10: Create a file in your repository](https://pages.github.com/images/new-create-file@2x.png)
*   #### Hello World

Name the file `index.html` and type some HTML content into the editor.

![Image 11: Hello World on GitHub.com](https://pages.github.com/images/new-index-html@2x.png)
*   #### Commit the file

Scroll to the bottom of the page, write a commit message, and commit the new file.

![Image 12: Commit the file](https://pages.github.com/images/new-commit-file@2x.png)
*   #### Repository Settings

**Click on the Settings tab** and scroll down to the GitHub Pages section. 

Then select the **main branch** source and click on the **Save** button.

![Image 13: GitHub Pages Source Setting](https://pages.github.com/images/source-setting@2x.png)
*   #### …and you're done!

Fire up a browser and go to **http://_username_.github.io/_repository_**.

 

Now that you’re up and running, here are a few things you should know.
======================================================================

*   [](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)
#### [Blogging with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)

Using [Jekyll](https://jekyllrb.com/), you can blog using beautiful Markdown syntax, and without having to deal with any databases. [Learn how to set up Jekyll](https://jekyllrb.com/docs/).

*   [](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
#### [Custom URLs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

Want to use your own custom domain for a GitHub Pages site? Just create a file named CNAME and include your URL. [Read more](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).

*   [](https://docs.github.com/pages)
#### [Guides](https://docs.github.com/pages)

Learn how to create custom 404 pages, use submodules, and [learn more about GitHub Pages](https://docs.github.com/pages).

*   [Status](https://www.githubstatus.com/)
*   [API](https://docs.github.com/rest)
*   [Training](https://training.github.com/)
*   [Shop](https://shop.github.com/)
*   [Blog](https://github.blog/)
*   [About](https://github.com/about)

[](https://pages.github.com/)
*   © 2025 GitHub, Inc.
*   [Terms](https://docs.github.com/en/github/site-policy/github-terms-of-service)
*   [Privacy](https://docs.github.com/en/github/site-policy/github-privacy-statement)
*   [Security](https://github.com/security)
*   [Contact](https://support.github.com/)
