# Get started with wp-env

**Source:** [https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-wp-env/](https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-wp-env/)

## In this article

Table of Contents- Quick start

- Set up Docker Desktop
- Install and run wp-envWhere to run wp-envUninstall or reset wp-env
- TroubleshootingCommon errorsUbuntu Docker setup
- Additional resources

↑Back to top

The@wordpress/envpackage (wp-env) lets you set up a local WordPress environment (site) for building and testing plugins and themes, without any additional configuration.

Before following this guide, installNode.js development toolsif you have not already done so.

## Quick start

1. Download, install, and startDocker Desktopfollowing the instructions for your operating system.
1. Runnpm -g install @wordpress/envin the terminal to installwp-envglobally.
1. In the terminal, navigate to an existing plugin directory, theme directory, or a new working directory.
1. Runwp-env startin the terminal to start the local WordPress environment.
1. After the script runs, navigate tohttp://localhost:8888/wp-adminand log into the WordPress dashboard using usernameadminand passwordpassword.

## Set up Docker Desktop

Thewp-envtool usesDockerto create a virtual machine that runs the local WordPress site. The Docker Desktop application is free for small businesses, personal use, education, and non-commercial open-source projects. See theirFAQfor more information.

Use the links below to download and install Docker Desktop for your operating system.

- Docker Desktop for Mac
- Docker Desktop for Windows
- Docker Desktop for Linux

If you are using a version of Ubuntu prior to 20.04.1, see the additionaltroubleshooting notesbelow.

After successful installation, start the Docker Desktop application and follow the prompts to get set up. You should generally use the recommended (default) settings, and creating a Docker account is optional.

## Install and run wp-env

Thewp-envtool is used to create a local WordPress environment with Docker. So, after you have set up Docker Desktop, open the terminal and install thewp-envby running the command:

```bash
npm -g install @wordpress/env

```python

This will install thewp-envglobally, allowing the tool to be run from any directory. To confirm it’s installed and available, runwp-env --version, and the version number should appear.

Next, navigate to an existing plugin directory, theme directory, or a new working directory in the terminal and run:

```text

wp-env start

```text

Once the script completes, you can access the local environment at:http://localhost:8888. Log into the WordPress dashboard using usernameadminand passwordpassword.

```text

Some projects, like Gutenberg, include their own specific `wp-env` configurations, and the documentation might prompt you to run `npm run wp-env start` instead.

```python

For more information on controlling the Docker environment, see the@wordpress/env packagereadme.

### Where to run wp-env

Thewp-envtool can run from practically anywhere. When using the script while developing a single plugin,wp-env startcan mount and activate the plugin automatically when run from the directory containing the plugin. This also works for themes when run from the directory in which you are developing the theme.

A generic WordPress environment will be created if you runwp-env startfrom a directory that is not a plugin or theme. The script will display the following warning, but ignore if this is your intention.

```text

!! Warning: could not find a .wp-env.json configuration file and could not determine if 'DIR' is a WordPress installation, a plugin, or a theme.

```python

You can also use the.wp-env.jsonconfiguration file to create an environment that works with multiple plugins and/or themes. See the@wordpress/env packagereadme for more configuration details.

### Uninstall or reset wp-env

Here are a few instructions if you need to start over or want to remove what was installed.

- If you just want to reset and clean the WordPress database, runwp-env clean all
- To remove the local environment completely for a specific project, runwp-env destroy
- To globally uninstall thewp-envtool, runnpm -g uninstall @wordpress/env

## Troubleshooting

### Common errors

When usingwp-env, it’s common to get the error:Error while running docker-compose command

- Check that Docker Desktop is started and running.
- Check Docker Desktop dashboard for logs, restart, or remove existing virtual machines.
- Then try rerunningwp-env start.

If you see the error:Host is already in use by another container

- The container you are attempting to start is already running, or another container is. You can stop an existing container by runningwp-env stopfrom the directory that you started it in.
- If you do not remember the directory where you startedwp-env, you can stop all containers by runningdocker stop $(docker ps -q). This will stop all Docker containers, so use with caution.
- Then try rerunningwp-env start.

### Ubuntu Docker setup

If you are using a version of Ubuntu prior to 20.04.1, you may encounter errors when setting up a local WordPress environment withwp-env.

To resolve this, start by following theinstallation guidefrom Docker.docker-composeis also required, which you may need to install separately. Refer to theDocker compose documentation.

Once Docker andwp-envare installed, and assumingwp-envis configured globally, try runningwp-env startin a directory. If you run into this error:

```text

ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?

If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.

```text

First, make sure Docker is running. You can check by runningps -ef | grep docker, which should return something like:

```text

/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

```text

If Docker is not running, try starting the service by runningsudo systemctl start docker.service.

If Docker is running, then it is not listening to how the WordPress environment is trying to communicate. Try adding the following service override file to include listening ontcp. Seethis Docker documentationon how to configure remote access for Docker daemon.

```text

[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2376

```python

Restart the service from the command-line:

```text

sudo systemctl daemon-reload
sudo systemctl restart docker.service

```text

After restarting the services, set the environment variableDOCKER_HOSTand try startingwp-envwith:

```javascript

export DOCKER_HOST=tcp://127.0.0.1:2376
wp-env start

```text

Your environment should now be set up athttp://localhost:8888.

## Additional resources

- @wordpress/env(Official documentation)
- Docker Desktop(Official documentation)
- Quick and easy local WordPress development with wp-env(WordPress Developer Blog)
- wp-env: Simple Local Environments for WordPress(Make WordPress Core Blog)
- wp-envBasics diagram(Excalidraw)

First published

September 18, 2023

Last updated

December 16, 2024

Edit article

Improve it on GitHub: Get started with wp-env

[PreviousNode.js development environmentPrevious: Node.js development environment](https://developer.wordpress.org/block-editor/getting-started/devenv/nodejs-development-environment/)
[NextGet started with create-blockNext: Get started with create-block](https://developer.wordpress.org/block-editor/getting-started/devenv/get-started-with-create-block/)
