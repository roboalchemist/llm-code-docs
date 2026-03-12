# Source: https://help.cloudsmith.io/docs/python-repository.md

# Python Repository

Cloudsmith provides public & private repositories for Python packages

![](https://files.readme.io/c7d3d7f-cloudsmith-python-banner-hd.jpg "cloudsmith-python-banner-hd.jpg")

Python is an awesome general-purpose programming language (we use it!). Cloudsmith is proud to support fully-featured registries for managing your own public and private python packages.

For more information on Python, please see:

* [Python](https://python.org): The official website for Python
* [PyPi](https://pypi.org): The Python Package Index

<HTMLBlock>
  {`
  <div class="row cs-box-row">
      <div class="cs-box cs-box-66 cs-box-green">
        <div class="cs-box-title cs-box-title-green">Contextual Documentation</div>
        <p>The examples in this document are generic. Cloudsmith provides contextual setup instructions within each repository, complete with copy n' paste snippets (with your namespace/repo pre-configured).</p>
      </div>
      <div class="cs-box cs-box-33 cs-center-all cs-box-grey">
        <a href="https://youtu.be/UdeNORGn_oA" target="_blank">
          <img src="https://files.readme.io/b6d41b3-cloudsmith-youtube-play-python-small.png" /></a>
      </div>
    </div>
  </div>
  `}
</HTMLBlock>

In the following examples:

| Identifier       | Description                                                                               |
| :--------------- | :---------------------------------------------------------------------------------------- |
| OWNER            | Your Cloudsmith account name or organization name (namespace)                             |
| REPOSITORY       | Your Cloudsmith Repository name (also called "slug")                                      |
| TOKEN            | Your Cloudsmith Entitlement Token (see [Entitlements](https://help.cloudsmith.io/docs/entitlements) for more details) |
| USERNAME         | Your Cloudsmith username                                                                  |
| PASSWORD         | Your Cloudsmith password                                                                  |
| API-KEY          | Your Cloudsmith API Key                                                                   |
| PACKAGE\_NAME    | The name of your package                                                                  |
| PACKAGE\_VERSION | The version number of your package                                                        |

## Upload a Package

To upload, you need to generate your package first. You can do this with:

```shell
python setup.py bdist_wheel --universal
```

This generates a wheel package file (`.whl`) like `your-package-1.2.3.whl` that you can upload.

<Callout icon="📘" theme="info">
  This assumes that you've created a `setup.py` file for your project. Please see the [official PyPA](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py) packaging guide on how to create a `setup.py` for more information. There are also different types of distributions that you might be interested in, such as a source distribution, tarball distribution, etc.
</Callout>

### Upload via native Python tooling

The endpoint for the native Python API is:

```
https://python.cloudsmith.io/OWNER/REPOSITORY/
```

In order to authenticate for native publishing, you'll need to create a `.pypirc` file (in your `$HOME` or project directory), with the following:

```ini
[distutils]
index-servers =
  pypi
  cloudsmith
[cloudsmith]
  repository: https://python.cloudsmith.io/OWNER/REPOSITORY/
  username: USERNAME
  password: API-KEY
```

You can then publish from your project directory using [twine](https://pypi.org/project/twine/):

```shell
twine upload -r cloudsmith dist/PACKAGE_NAME-PACKAGE_VERSION.whl
```

### Upload via the Cloudsmith CLI

For full details of how to install and setup the Cloudsmith CLI, see [Command Line Interface](https://help.cloudsmith.io/docs/upload-via-cloudsmith-cli-api).

The command to upload a Python package via the Cloudsmith CLI is:

```shell
cloudsmith push python OWNER/REPOSITORY PACKAGE_NAME-PACKAGE_VERSION.whl
```

Example:

```shell
cloudsmith push python org/repo boto3-1.4.4.py2.p3-none-any.whl
```

### Upload via Cloudsmith Website

Please see [Upload a Package](https://help.cloudsmith.io/docs/upload-package#upload-via-website-ui) for details of how to upload via the Website UI.

***

## Download / Install a package

### Setup

You have a choice of 2 methods to set up your Cloudsmith repository:

* Python set up via command line
* Python set up via Pip

#### Public Repositories

#### Set up via command line

Tell pip the location of your Cloudsmith repository using the the `--index-url` option.

```shell
pip install PACKAGE_NAME==PACKAGE_VERSION --index-url https://dl.cloudsmith.io/public/OWNER/REPOSITORY/python/simple/
```

#### Set up via Pip

Similar to set up via command-line, pip needs to be passed the `--index-url` configuration option. To do this add `--index-url` to the top of your `requirements.txt` (or similar) file:

```
--index-url https://dl.cloudsmith.io/public/OWNER/REPOSITORY/python/simple/
PACKAGE_NAME==PACKAGE_VERSION
```

#### Private Repositories

<Callout icon="📘" theme="info">
  Private Cloudsmith repositories require authentication.  You can choose between two types of authentication:

  * Entitlement Token Authentication
  * HTTP Basic Authentication.

  The setup method will differ depending on what authentication type you choose to use.
</Callout>

<Callout icon="🚧" theme="warn">
  Entitlement Tokens, User Credentials and API-Keys should be treated as secrets, and you should ensure that you do not commit them in configurations files along with source code or expose them in any logs.
</Callout>

#### Set up via command line

```shell Entitlement Token Auth
pip install PACKAGE_NAME==PACKAGE_VERSION --index-url https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/python/simple/
```

```shell HTTP Basic Auth (User & Pass)
pip install PACKAGE_NAME==PACKAGE_VERSION --index-url https://USERNAME:PASSWORD@dl.cloudsmith.io/basic/OWNER/REPOSITORY/python/simple/
```

```shell HTTP Basic Auth (API-Key)
pip install PACKAGE_NAME==PACKAGE_VERSION --index-url https://USERNAME:API-KEY@dl.cloudsmith.io/basic/OWNER/REPOSITORY/python/simple/
```

```shell HTTP Basic Auth (Token)
pip install PACKAGE_NAME==PACKAGE_VERSION --index-url https://token:TOKEN@dl.cloudsmith.io/basic/OWNER/REPOSITORY/python/simple/
```

#### Set up via Pip

Similar to set up via command-line, pip needs to be passed the `--index-url` configuration option. To do this add `--index-url` to the top of your `requirements.txt` (or similar) file:

```text Entitlement Token Auth
--index-url https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/python/simple/
PACKAGE_NAME==PACKAGE_VERSION
```

```text HTTP Basic Auth (User & Pass)
--index-url https://USERNAME:PASSWORD@dl.cloudsmith.io/basic/OWNER/REPOSITORY/python/simple/
PACKAGE_NAME==PACKAGE_VERSION
```

```text HTTP Basic Auth (API-Key)
--index-url https://USERNAME:API-KEY@dl.cloudsmith.io/basic/OWNER/REPOSITORY/python/simple/
PACKAGE_NAME==PACKAGE_VERSION
```

```text HTTP Basic Auth (Token)
--index-url https://token:TOKEN@dl.cloudsmith.io/basic/OWNER/REPOSITORY/python/simple/
PACKAGE_NAME==PACKAGE_VERSION
```

#### Private Repository Credential Security

As private repositories require authentication in order to access the repository content, when specifying a private repository in a `requirements.txt` file please bear in mind that the URL will contain the credentials (especially important if the `requirements.txt` file is shared.)

You could choose to encrypt your `requirements.txt` file via something like [git-crypt](https://github.com/AGWA/git-crypt) (if you're using git or GitHub, for example).

***

### Removing Setup

If you no longer want to install packages from the repository, remove the `--index-url` line from your `$HOME/.pip/pip.conf file`.

***

### Extra index url

When using pip to access your packages, there are two parameter options to ensure pip searches your repository - they are [`--index-url`](https://pip.pypa.io/en/stable/cli/pip_wheel/?highlight=--index-url#cmdoption-i) and [`--extra-index-url`](https://pip.pypa.io/en/stable/cli/pip_wheel/?highlight=--index-url#cmdoption-extra-index-url).

There is an important distinction to be made between these parameters, especially from a security perspective.

Specifying `--index-url` will override pip's default repository and *only* search the specified repository. This is the recommended approach from Cloudsmith. This improves your security posture as it reduces the risk of malicious public packages being installed in place of your own.

> 📘 Dependency confusion
>
> An attack known as [dependency confusion](https://cloudsmith.com/blog/dependency-confusion-attacks/): where an attacker can claim the package on the public repository in a way that will ensure it gets chosen over the private package.

If you still wish to access third-party repositories, like `pypi.org`, paid-for Cloudsmith plans include upstream proxying. This allows your repository to call out to other python repositories whenever a package cannot be found in your repository. See the Upstream Proxying section below.

If your Cloudsmith plan does not include upstream proxying and some of your dependencies live outside your Cloudsmith repository, then you can also also specify extra index urls to pip. This is done by specifying `--extra-index-url`.  When pip is supplied with extra index urls, it has a *list* of repositories it searches for packages (the extra urls plus the index url). Note, *this list is not ordered*. All repositories are considered equal and pip will simply search for the *best* package match according to [PEP 440](https://peps.python.org/pep-0440/). Using the `--extra-index-url` increases your exposure to dependency confusion attacks.

See [pip install](https://pip.pypa.io/en/stable/cli/pip_install/#pip-install) for more information.

> 📘 TLDR
>
> To search your Cloudsmith repository for packages use the `--index-url` Pip configuration argument.
>
> Using the `--index-url` configuration option will force pip to search only the Cloudsmith repository and will result in pip not being able to install public (PyPi) packages that your private package may depend on. This reduces your exposure to dependency confusion attacks.

***

## Security Scanning

<br />

<span class="cs-tag cs-tag-dark-green">Supported</span>
Please see our

[Security Scanning](https://help.cloudsmith.io/docs/vulnerability-scanning) documentation for further information.

## Upstream Proxying / Caching

<span class="cs-tag cs-tag-dark-green">Configurable Proxying</span> <span class="cs-tag cs-tag-orange">Caching</span>.

Please see [Upstream Proxying](https://help.cloudsmith.io/docs/upstream-proxying-caching) for more details.

Upstreams provide a way to *blend* multiple Python repositories into a single repository. This allows your single Cloudsmith repository to serve packages from multiple 'upstream' repositories (like PyPi.org, Artifactory, DevPi etc). Please note, blended upstreams can be a source of dependency confusion attacks.

## Key Signing Support

<span class="cs-tag cs-tag-blue">GPG</span>

## Troubleshooting

Please see the [Troubleshooting](https://help.cloudsmith.io/docs/troubleshooting) page for further help and information.