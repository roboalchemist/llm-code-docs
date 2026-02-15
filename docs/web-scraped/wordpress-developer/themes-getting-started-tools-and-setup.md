# Tools and Setup

**Source:** [https://developer.wordpress.org/themes/getting-started/tools-and-setup/](https://developer.wordpress.org/themes/getting-started/tools-and-setup/)



# Tools and Setup




## In this article


Table of Contents- Development environmentWhy set up a development environment?Setting up a local development environment
- Installing WordPress
- Code editor
- Other development toolsTest dataPlugins
- WordPress.org Theme Review Guidelines



↑Back to top



In this document, you will learn about the tools that you will need to get off to a solid start when building WordPress themes. You will also find resources on setting up a development environment for testing your projects.


While it is definitely possible to create and build block themes without any of these tools, they are foundational pieces of a good workflow.


## Development environment


When building WordPress themes, it is a good idea to do it within an environment that is separate from a live (i.e., production) site. Before creating your first WordPress theme, you should set up a development environment.


Don’t let this process scare you if it’s your first time. In the long run, you will be happy you learned how to set this up.


### Why set up a development environment?


Development environments allow you to test code before it goes live on a production site. You don’t want to change something, push it live, and later realize you created a fatal error that took down the whole website.


By using a development environment, you can test things to ensure they work before they are live.


Your development environment can either be local (on your computer) or on a remote server. But configuring a local environment to work on your theme is beneficial for several reasons:


- You do not need an internet connection to build your theme.
- You can build your theme without relying on a remote server. This speeds up the building process, and you can see changes instantly in your browser.
- You can test your theme from many perspectives. This is important if you plan on releasing it to a larger audience and want maximum compatibility.


### Setting up a local development environment


For developing WordPress themes, you need to set up a development environment that is suited to WordPress. This list is not exhaustive, but here are several options to choose from:


- @wordpress/env(local WordPress environment package)
- Docker
- WordPress Studio
- Local
- MAMP
- XAMPP
- Varying Vagrant Vagrants(VVV)


For more information, read theSetting Up a Development Environmentdocumentation in the Core Handbook.


## Installing WordPress


Before you begin building themes in your development environment, you must also install WordPress.


Some of the development environments include methods for automatically installing an instance of WordPress. You can skip this step if this is the case for you.


To install WordPress on your own, follow theHow to install WordPressdocumentation from the Advanced Administration handbook. Then, of course, come back here and learn more about creating WordPress themes!


## Code editor


> A good code editor is worth its weight in gold.Someone Wise


On a more serious note, a good code editor gives you proper syntax highlighting, error reporting, integration with version control systems (VCS), and much more. It’s there to make your life easier.


Technically, you could edit code in a plain text editor, but you’d be missing out on all the best features that true code editors and IDEs (Integrated Development Environments) bring to life.


Editing a theme’s `single.html` template in Visual Studio Code
There are many free and open-source editors to choose from. Here are some of the more popular ones:


- Visual Studio Code(VS Code)
- VIM
- Brackets
- Notepad++
- GNU Emacs
- TextMate


There are also many proprietary editors that are free or cost a fee to use. Whatever you decide to use, pick something you feel comfortable with.


## Other development tools


A code editor and development environment are the foundational pieces of creating a WordPress theme. However, there are other tools and resources that you will likely find useful for your project.


### Test data


WordPress allows you toimport XML filescontaining real or dummy data for testing your themes. This lets you see how your theme performs with different types of content and layouts. Here are two options for importing:


- WordPress.org Theme Test Data
- WordPress.com Theme Test Data(includes WordPress.com-specific data)


If nothing else, you need some type of demo/test content to see what your theme looks like in action. You could even create test posts and pages of your own!


### Plugins


In addition to test data, there are several WordPress plugins that can help make sure your theme is following standard practices and not producing debugging notices. These are optional but can be useful:


- Theme Check: Tests your theme for compliance with the latest WordPress standards and practices.
- Debug Bar: Adds an admin bar to your WordPress admin and provides a central location for debugging.
- Query Monitor: Allows debugging of database queries, API requests, and AJAX used to generate theme pages and functionality.
- Log Deprecated Notices: Logs incorrect function usage, deprecated file usage, and deprecated function usage in your theme.
- Monster Widget: Consolidates the core WordPress widgets into a single widget, making it easier to test them all at once (classic themes only).


## WordPress.org Theme Review Guidelines


It is a good idea to stay up to date with thetheme guidelinesprovided by the WordPress.org Themes Team. These guidelines are required if you plan to submit your theme to the officialTheme Directory, but they are also good principles for anyone creating a theme.


You should also follow theWordPress Coding Standardswhen writing any code for your theme. This will help make sure what you are creating meets some minimum quality standards.





First published


November 21, 2023


Last updated


July 11, 2025



[PreviousReading This HandbookPrevious: Reading This Handbook](https://developer.wordpress.org/themes/getting-started/reading-this-handbook/)
[NextQuick-Start GuideNext: Quick-Start Guide](https://developer.wordpress.org/themes/getting-started/quick-start-guide/)


