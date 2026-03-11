# Source: https://symfony.com/doc/8.0/deployment.html

Title: How to Deploy a Symfony Application (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/deployment.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/deployment.rst)

Deploying a Symfony application can be a complex and varied task depending on the setup and the requirements of your application. This article is not a step-by-step guide, but rather a general list of the most common requirements and ideas for deployment.

[Symfony Deployment Basics](https://symfony.com/doc/8.0/deployment.html#symfony-deployment-basics "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------

The typical steps taken while deploying a Symfony application include:

1. Upload your code to the production server;
2. Install your vendor dependencies (typically done via Composer and may be done before uploading);
3. Running database migrations or similar tasks to update any changed data structures;
4. Clearing (and optionally, warming up) your cache.

A deployment may also include other tasks, such as:

* Tagging a particular version of your code as a release in your source control repository;
* Creating a temporary staging area to build your updated setup "offline";
* Running any tests available and [linting Twig templates](https://symfony.com/doc/current/templates.html#linting-twig-templates) to ensure code and/or server stability;
* Removal of any unnecessary files from the `public/` directory to keep your production environment clean;
* Clearing of external cache systems (like [Memcached](https://memcached.org/) or [Redis](https://redis.io/)).

[How to Deploy a Symfony Application](https://symfony.com/doc/8.0/deployment.html#how-to-deploy-a-symfony-application-1 "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------

There are several ways you can deploy a Symfony application. Start with a few basic deployment strategies and build up from there.

### [Basic File Transfer](https://symfony.com/doc/8.0/deployment.html#basic-file-transfer "Permalink to this headline")

The most basic way of deploying an application is copying the files manually via FTP/SCP (or similar method). This has its disadvantages as you lack control over the system as the upgrade progresses. This method also requires you to take some manual steps after transferring the files (see [Common Deployment Tasks](https://symfony.com/doc/current/deployment.html#common-deployment-tasks)).

### [Using Source Control](https://symfony.com/doc/8.0/deployment.html#using-source-control "Permalink to this headline")

If you're using source control (e.g. Git or SVN), you can simplify by having your live installation also be a copy of your repository. When you're ready to upgrade, fetch the latest updates from your source control system. When using Git, a common approach is to create a tag for each release and check out the appropriate tag on deployment (see [Git Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)).

This makes updating your files _easier_, but you still need to worry about manually taking other steps (see [Common Deployment Tasks](https://symfony.com/doc/current/deployment.html#common-deployment-tasks)).

### [Using Platforms as a Service](https://symfony.com/doc/8.0/deployment.html#using-platforms-as-a-service "Permalink to this headline")

Using a Platform as a Service (PaaS) can be a great way to deploy your Symfony app quickly. There are many PaaS, but we recommend [Upsun](https://symfony.com/cloud) as it provides a dedicated Symfony integration and helps fund the Symfony development.

### [Using Build Scripts and other Tools](https://symfony.com/doc/8.0/deployment.html#using-build-scripts-and-other-tools "Permalink to this headline")

There are also tools to help ease the pain of deployment. Some of them have been specifically tailored to the requirements of Symfony.

[Deployer](https://deployer.org/) This is another native PHP rewrite of Capistrano, with some ready recipes for Symfony. [Ansistrano](https://ansistrano.com/) An Ansible role that allows you to configure a powerful deploy via YAML files. [Magallanes](https://github.com/andres-montanez/Magallanes) This Capistrano-like deployment tool is built in PHP, and may be easier for PHP developers to extend for their needs. [Fabric](https://www.fabfile.org/) This Python-based library provides a basic suite of operations for executing local or remote shell commands and uploading/downloading files. [Capistrano](https://capistranorb.com/) with [Symfony plugin](https://github.com/capistrano/symfony/)[Capistrano](https://capistranorb.com/) is a remote server automation and deployment tool written in Ruby. [Symfony plugin](https://github.com/capistrano/symfony/) is a plugin to ease Symfony related tasks, inspired by [Capifony](https://github.com/everzet/capifony) (which works only with Capistrano 2).

[Common Deployment Tasks](https://symfony.com/doc/8.0/deployment.html#common-deployment-tasks "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------

Before and after deploying your actual source code, there are a number of common things you'll need to do:

### [A) Check Requirements](https://symfony.com/doc/8.0/deployment.html#a-check-requirements "Permalink to this headline")

There are some [technical requirements for running Symfony applications](https://symfony.com/doc/current/setup.html#symfony-tech-requirements). In your development machine, the recommended way to check these requirements is to use [Symfony CLI](https://symfony.com/download). However, in your production server you might prefer to not install the Symfony CLI tool. In those cases, install this other package in your application:

Then, make sure that the checker is included in your Composer scripts:

### [B) Configure your Environment Variables](https://symfony.com/doc/8.0/deployment.html#b-configure-your-environment-variables "Permalink to this headline")

Most Symfony applications read their configuration from environment variables. While developing locally, you'll usually store these in [.env files](https://symfony.com/doc/current/configuration.html#configuration-env-var-in-dev). On production, you have two options:

1. Create "real" environment variables. How you set environment variables, depends on your setup: they can be set at the command line, in your Nginx configuration, or via other methods provided by your hosting service;
2. Or, create a `.env.prod.local` file that contains values specific to your production environment.

There is no significant advantage to either option: use whichever is most natural for your hosting environment.

Tip

You might not want your application to process the `.env.*` files on every request. You can generate an optimized `.env.local.php` which overrides all other configuration files:

The generated file will contain all the configuration stored in `.env`. If you want to rely only on environment variables, generate one without any values using:

If you don't have Composer installed on the production server, use instead [the dotenv:dump Symfony command](https://symfony.com/doc/current/configuration.html#configuration-env-var-in-prod).

### [C) Install/Update your Vendors](https://symfony.com/doc/8.0/deployment.html#c-install-update-your-vendors "Permalink to this headline")

Your vendors can be updated before transferring your source code (i.e. update the `vendor/` directory, then transfer that with your source code) or afterwards on the server. Either way, update your vendors as you normally do:

Tip

The `--optimize-autoloader` flag improves Composer's autoloader performance significantly by building a "class map". The `--no-dev` flag ensures that development packages are not installed in the production environment.

Warning

If you get a "class not found" error during this step, you may need to run `export APP_ENV=prod` (or `export SYMFONY_ENV=prod` if you're not using [Symfony Flex](https://symfony.com/doc/current/setup.html#symfony-flex)) before running this command so that the `post-install-cmd` scripts run in the `prod` environment.

### [D) Clear your Symfony Cache](https://symfony.com/doc/8.0/deployment.html#d-clear-your-symfony-cache "Permalink to this headline")

Make sure you clear and warm-up your Symfony cache:

[Application Lifecycle: Continuous Integration, QA, etc.](https://symfony.com/doc/8.0/deployment.html#application-lifecycle-continuous-integration-qa-etc "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While this article covers the technical details of deploying, the full lifecycle of taking code from development up to production may have more steps: deploying to staging, QA (Quality Assurance), running tests, etc.

The use of staging, testing, QA, continuous integration, database migrations and the capability to roll back in case of failure are all strongly advised. There are simple and more complex tools and one can make the deployment as easy (or sophisticated) as your environment requires.

Don't forget that deploying your application also involves updating any dependency (typically via Composer), migrating your database, clearing your cache and other potential things like pushing assets to a CDN (see [Common Deployment Tasks](https://symfony.com/doc/current/deployment.html#common-deployment-tasks)).

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
