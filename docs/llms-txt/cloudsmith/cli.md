# Source: https://help.cloudsmith.io/docs/cli.md

# Command-Line Interface

[![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/badges/version/cloudsmith/cli/python/cloudsmith-cli/latest/xf=bdist_wheel;xn=cloudsmith-cli;xv=py2.py3/?render=true)](https://cloudsmith.io/~cloudsmith/repos/cli/packages/detail/python/cloudsmith-cli/latest/xf=bdist_wheel;xn=cloudsmith-cli;xv=py2.py3/) [![Python Versions](https://img.shields.io/pypi/pyversions/cloudsmith-cli.svg)](https://pypi.python.org/pypi/cloudsmith-cli) [![PyPI Version](https://img.shields.io/pypi/v/cloudsmith-cli.svg)](https://pypi.python.org/pypi/cloudsmith-cli) [![CircleCI](https://circleci.com/gh/cloudsmith-io/cloudsmith-cli.svg?style=svg)](https://circleci.com/gh/cloudsmith-io/cloudsmith-cli) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/7ce010a44fd249329dab8959ca09142a)](https://www.codacy.com/app/Cloudsmith/cloudsmith-cli) [![Maintainability](https://api.codeclimate.com/v1/badges/c4ce2988b461d7b31cd5/maintainability)](https://codeclimate.com/github/cloudsmith-io/cloudsmith-cli/maintainability) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

<HTMLBlock>
  {`
  <div class="cs-headline">The Cloudsmith Command Line Interface (CLI) is a Py2/Py3 text-based interface to the <a href="https://api.cloudsmith.io">API</a>. This allows users, machines and other services to access and integrate smoothly with Cloudsmith without requiring explicit plugins or tools.</div>
  `}
</HTMLBlock>

<HTMLBlock>
  {`
  <div class="row cs-box-row">
    <div class="cs-box cs-box-66 cs-box-green">
      <div class="cs-box-title cs-box-title-green">Open source</div><p>
      The Cloudsmith CLI is built as open source allowing the community to contribute.
      <p> 
      Source Code available on <a href="https://github.com/cloudsmith-io/cloudsmith-cli">GitHub</a><br>
      </p>
  </div>
    <div class="cs-box cs-box-33 cs-center-all cs-box-grey">
      <a href="https://youtu.be/R-g8ZhDwTKk" target="_blank">
        <img src="https://files.readme.io/851d406-cloudsmith-youtube-play-cli-small.png" alt="A Walkthrough of the Cloudsmith CLI" /></a>
    </div>
  </div>
  `}
</HTMLBlock>

## Installation

You can install or deploy the latest CLI application from:

* [Cloudsmith](https://cloudsmith.io/~cloudsmith/repos/cli/packages/)
* [PyPi](https://pypi.python.org/pypi/cloudsmith-cli)
* [Homebrew Tap](https://github.com/cloudsmith-io/homebrew-cloudsmith-cli)
* [DockerHub](https://hub.docker.com/r/cloudsmith/cloudsmith-cli)

### Installing with pip

The easiest way is to use `pip`, such as:

```shell
pip install --upgrade cloudsmith-cli
```

Or you can get the latest pre-release version from Cloudsmith:

```shell
pip install --upgrade cloudsmith-cli --extra-index-url=https://dl.cloudsmith.io/public/cloudsmith/cli/python/index/
```

### Installing with zipapp

Distributing Python applications can be challenging because, as an interpreted language, Python requires an interpreter to run code, unlike compiled languages that produce standalone executables. However, for smaller, pure-Python programs, a Python Zip application offers a straightforward solution for bundling and sharing your work. This method packages all the necessary code into a single ZIP file.

<Note variant="note" headline="Requirements">
  `python3` required to use this installation method.
</Note>

```bash
# download latest release and make it executable
curl -s https://api.github.com/repos/cloudsmith-io/cloudsmith-cli/releases/latest | sed -n 's/"browser_download_url": //p' | xargs wget -qO cloudsmith.pyz
chmod +x ./cloudsmith.pyz
# move it into your $PATH
sudo mv ./cloudsmith.pyz /usr/local/bin/cloudsmith
```

You are ready to use it:

```bash
cloudsmith -h
```

### Installing with Homebrew Tap

Homebrew is a package manager that can be \[installed]\([https://brew.sh/](https://brew.sh/)) and used in different operative systems (MacOS, Linux, and also Windows). To install the Cloudsmith CLI with Brew, add the tap first:

```shell
brew tap cloudsmith-io/cloudsmith-cli
```

Then, install it with:

```shell
brew install cloudsmith-cli
```

And you should be able to start using it! If you need to upgrade:

```shell
brew upgrade cloudsmith-cli
```

For issues with the tap, please open a [GitHub issue](https://github.com/cloudsmith-io/homebrew-cloudsmith-cli/issues/new) or contact [support@cloudsmith.io](mailto:support@cloudsmith.io).

### Installing on Windows

The instructions below detail how to install the Cloudsmith CLI using [chocolatey](https://chocolatey.org/):

1. Click Start on your Windows machine and type “powershell“
2. Right-click Windows Powershell and select to “Run as Administrator“
3. To install chocolatey, type the following command into the Powershell terminal:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; `
  iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

4. Close and reopen Powershell in Administrator mode.
5. Install the cloudsmith cli using chocolately:

```powershell
choco install python -y
refreshenv
choco install cloudsmith-cli --source python
```

### Deploying the CLI containerized

Cloudsmith maintains a [Docker image for the Cloudsmith CLI](https://hub.docker.com/r/cloudsmith/cloudsmith-cli)⁠ built for use in CI/CD pipelines and automation environments.

To deploy it, replace the `API_TOKEN` with the API Token associated to the service account you want to use, specifiying the Cloudsmith CLI command you want to use. For example, you can run `cloudsmith whoami`:

```bash
docker run --rm \
-e CLOUDSMITH_API_KEY=API_TOKEN \
cloudsmith/cloudsmith-cli:1.8.3 \
whoami
```

Successful execution of the command above will return the member or service account associated to the API Token used:

```text
Retrieving your authentication status from the API ... OK
You are authenticated as:
M. Bolton (slug: mbolton, email: mbolton@initech.com)
```

For example, you can use the Cloudsmith CLI container to push a python package to your workspace/repository `WORKSPACE/REPOSITORY`. In this example, the python package `PACKAGE.whl` is located in `/path_to_package/`, and the package is being mounted in the container filesystem in `/tmp/` as `my_package.whl`:

```bash
docker run --rm \
-e CLOUDSMITH_API_KEY=API_TOKEN \
-v "/path_to_package/PACKAGE.whl:/tmp/my_package.whl" \
cloudsmith/cloudsmith-cli:1.8.3 \
push python WORKSPACE/REPOSITORY /tmp/my_package.whl 
```

Successful execution of the command will return:

```text
Checking python package upload parameters ... OK
Checking PACKAGE.whl file upload parameters ... OK
Requesting file upload for PACKAGE.whl ... OK
Uploading PACKAGE.whl:
Creating a new python package ... OK
Created: WORKSPACE/REPOSITORY/PACKAGEwhl (package_slug)

Synchronising PACKAGEwhl:

Package synchronised successfully in 6.001236 second(s)!
```

### Getting your API Key

You'll need to authenticate Cloudsmith for any CLI actions that result in accessing private data or changing resources (such as pushing a new package to a repository). There are two ways to retrieve your API Key:

**1. Via the Cloudsmith Website UI**

Go to the [API Key](https://cloudsmith.io/user/settings/api/) page in your user settings to view the API Key.

**2. via the Cloudsmith CLI**

You can retrieve your API key using the `cloudsmith login` command:

```
cloudsmith login
Login: you@example.com
Password: PASSWORD
Repeat for confirmation: PASSWORD
```

**NOTE**: Please ensure you use your email for the 'Login' prompt and not your user slug/identifier.

The resulting output is:

```
Retrieving API token for 'you@example.com' ... OK
Your API token is: 1234567890abcdef1234567890abcdef
```

Once you have your API key, you can put it in your `credentials.ini` file, use it as an environment variable `export CLOUDSMITH_API_KEY=<YOUR_API_KEY>`,  or pass it to the CLI using the `-k <YOUR_API_KEY>` flag.

For convenience, the CLI will ask you if you want to install the default configuration files, complete with your API key, if they don't already exist. Enter `y` or `yes` to create the configuration files.

If the configuration files already exist, you'll have to put the API key into the configuration files manually, but the CLI will print out their locations.

> 📘 SAML / Single Sign On Users
>
> SSO Users do not have a Cloudsmith password and cannot use the `cloudsmith login`command to retrieve their API-Key.
>
> SSO Users should instead use the `cloudsmith auth`command and pass their workspace identifier like:\
> `cloudsmith auth -o my-workspace`
>
> You will then be prompted to complete the SSO login process via your web browser (if not already signed in), and 2FA if applicable. Once authentication is complete, the CLI is issued an access token for your account.
>
> To authenticate in environments without a web browser, such as a remote terminal session, set the CLOUDSMITH\_API\_KEY environment variable. You can set it for your current session like this:
>
> ```shell
> export CLOUDSMITH_API_KEY="your-api-key-here"
> ```

***

## Configuration / Setup

There are two configuration files used by the CLI:

* `config.ini`: For non-credentials configuration.
* `credentials.ini`: For credentials (authentication) configuration.

By default, the CLI will look for these in the following locations:

* The current working directory.
* A directory called cloudsmith in the OS-defined application directory. For example:

**Linux**

* `$HOME/.config/cloudsmith`
* `$HOME/.cloudsmith`

**Mac OS**

* `$HOME/Library/Application Support/cloudsmith`
* `$HOME/.cloudsmith`

**Windows**

* `C:\Users\<user>\AppData\Local\cloudsmith (Win7+, not roaming)`
* `C:\Users\<user>\AppData\Roaming\cloudsmith (Win7+, roaming)`
* `C:\Documents and Settings\<user>\Application Data\cloudsmith (WinXP, not roaming)`
* `C:\Documents and Settings\<user>\Local Settings\Application Data\cloudsmith (WinXP, roaming)`

### config.ini

You can specify the following configuration options:

`api_host:` The API host to connect to.\
`api_proxy:` The API proxy to connect through.\
`api_ssl_verify:` Whether or not to use SSL verification for requests.\
`api_user_agent:` The user agent to use for requests.

The default config is:

```shell config.ini
# Default configuration
[default]
# The API host to connect to (default: api.cloudsmith.io).
api_host=

# The API proxy to connect through (default: None).
api_proxy=

# Whether to verify SSL connection to the API (default: True)
api_ssl_verify=true

# The user agent to use for requests (default: calculated).
api_user_agent=


# Profile-based configuration
# You can set as many additional profiles as you need to provide
# for different configuration environments (e.g. prod vs staging).
# Add your overrides in the sections and then specify one of:
#  * -P your-profile-name (as an argument)
#  * --profile your-profile-name (an an argument)
#  * CLOUDSMITH_PROFILE=your-profile-name (as an env variable)
[profile:your-profile-name]
```

### credentials.ini

You can specify the following configuration options:

`api_key:` The API key for authenticating with the API.

```shell credentials.ini
# Default configuration
[default]
# The API key for authenticating with the API.
api_key=<YOUR_API_KEY>


# Profile-based configuration
# You can set as many additional profiles as you need to provide
# for different configuration environments (e.g. prod vs staging).
# Add your overrides in the sections and then specify one of:
#  * -P your-profile-name (as an argument)
#  * --profile your-profile-name (an an argument)
#  * CLOUDSMITH_PROFILE=your-profile-name (as an env variable)
[profile:your-profile-name]
```

## CLI Scripting

There are certain operations, such as moving multiple packages at a time, that currently require additional scripting to achieve using the CLI. View the [CLI Scripting guide](https://help.cloudsmith.io/docs/cli-scripting) for details and examples of CLI Scripting.

# Troubleshooting

When upgrading the Cloudsmith CLI, you may also need to update the Cloudsmith API using:

```shell
pip install --upgrade cloudsmith-api
```

If using a proxy with self-signed / internal TLS Certificates, you may need to point to your custom certs with:

```
export REQUESTS_CA_BUNDLE=/path/to/converted/certificate.pem
```