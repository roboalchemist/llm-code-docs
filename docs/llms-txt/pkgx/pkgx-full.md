# Pkgx Documentation

Source: https://docs.pkgx.sh/llms-full.txt

---

# Highlights

## `pkgx`

`pkgx` is a 4 MiB, standalone binary that can *run anything*.

### Quick Start

```sh
brew install pkgx || curl https://pkgx.sh | sh
```

```pwsh
irm https://pkgx.sh | iex  # Windows
```

{% hint style="info" %}
[Installation Guide](https://docs.pkgx.sh/pkgx/installing-pkgx)
{% endhint %}

### Using `pkgx`

* [Run Anything](https://docs.pkgx.sh/pkgx/pkgx)
* [Scripting](https://docs.pkgx.sh/pkgx/scripting)

## The `pkgx` Ecosystem

`pkgx` is more than a package runner, it’s a composable primitive that can be\
used to build a whole ecosystem of tools. Here’s what we’ve built so far:

### `dev`

`dev` uses shellcode and `pkgx` to create “virtual environments” for any project\
and any toolset.

{% hint style="info" %}
<https://github.com/pkgxdev/dev>
{% endhint %}

### `pkgm`

`pkgm` installs `pkgx` packages to `/usr/local`.

{% hint style="info" %}
<https://github.com/pkgxdev/pkgm>
{% endhint %}

### `mash`

`mash` is a package manager for scripts that use `pkgx` to make the whole open\
source ecosystem available to them.

{% hint style="info" %}
<https://github.com/pkgxdev/mash>
{% endhint %}

### `pkgo` (Package…GO!)

Some Open Source resists packaging and instead includes long installation\
instructions that can be… tedious. `pkgo` makes using amazing tools like[“Stable Diffusion WebUI”](https://github.com/AUTOMATIC1111/stable-diffusion-webui) as easy as typing `pkgo` (thanks to `pkgx`).

{% hint style="info" %}
<https://github.com/pkgxdev/pkgo>
{% endhint %}

## Support

[Discord](https://discord.gg/rNwNUY83XS)


# Installing pkgx

There are quite a few ways to install `pkgx` but this is our recommendation:

```sh
brew install pkgx || curl https://pkgx.sh | sh
```

## Complete Installation Method Listing

### Homebrew

```sh
brew install pkgx
```

### cURL Installer

Our installer both installs and upgrades `pkgx`:

```sh
curl -fsS https://pkgx.sh | sh
```

### Windows

```pwsh
irm https://pkgx.sh | iex
# ^^ limited packages so far, list available programs with `pkgx -Q`
```

{% hint style="info" %}
Wanna read that script before you run it?[github.com/pkgxdev/setup/installer.sh](https://github.com/pkgxdev/setup/blob/main/installer.sh)
{% endhint %}

### Download Manually

`pkgx` is a standalone binary, so you can just download it directly:

```sh
# download it to `./pkgx`
curl -o ./pkgx \
   --compressed --fail --proto '=https' \
   https://pkgx.sh/$(uname)/$(uname -m)

# install it to `/usr/local/bin/pkgx`
sudo install -m 755 pkgx /usr/local/bin
```

For your convenience we provide a `.tgz` so you can one-liner that:

```sh
curl -Ssf https://pkgx.sh/$(uname)/$(uname -m).tgz | sudo tar xz -C /usr/local/bin
```

You can also download straight from [GitHub Releases](https://github.com/pkgxdev/pkgx/releases) (you’ll likely need to\
unquarantine the downloaded binary).

### Cargo

```sh
cargo install pkgx
```

### Docker

```sh
docker run -it pkgxdev/pkgx

# or, eg.
docker run pkgxdev/pkgx +python@3.10 node@22 start
```

Or in your `Dockerfile`:

```dockerfile
FROM pkgxdev/pkgx
RUN pkgx +node@16 npm start
```

{% hint style="info" %}
[hub.docker.com/r/pkgxdev/pkgx](https://hub.docker.com/r/pkgxdev/pkgx)
{% endhint %}

### GitHub Actions

```yaml
- uses: pkgxdev/setup@v4
```

{% hint style="info" %}
[github.com/pkgxdev/setup](https://github.com/pkgxdev/setup)
{% endhint %}

{% hint style="success" %}
`pkgx` makes it easy to consistently use the GNU or\
BSD versions of core utilities across different platforms—handy for\
cross-platform CI/CD scripts. eg. `pkgx +gnu.org/coreutils ls`
{% endhint %}

### Arch Linux

If you're on Arch Linux (or any of it's derivatives) you can also use the[`pkgx` AUR](https://aur.archlinux.org/packages/pkgx) (latest released version) or [`pkgx-git` AUR](https://aur.archlinux.org/packages/pkgx-git) (latest development\
version, might not be stable).

{% hint style="warning" %}
The AURs are community-maintained and might be\
out-of-date. Use them with caution.
{% endhint %}


# Getting Started

With `pkgx` it couldn’t be simpler to run anything from the Open Source\
ecosystem:

```sh
$ pkgx openai --version
openai 1.59.6
```

## Search

Generally you don’t need to search since you already know what you want to\
run, so just type it! Sometimes though you want to browse.

We have a web based package listing at[pkgx.dev/pkgs/](https://pkgx.dev/pkgs/). This is the most thorough resource\
at this time.

And from the CLI you can use query mode:

```sh
$ pkgx -Q git
# ^^ can we run git?

$ pkgx -Q | grep git-
# ^^ search for all git extensions

$ $ pkgx -Q
# ^^ list every program pkgx can run
```

## Run Any Version

```sh
$ pkgx postgres@12 --version
postgres (PostgreSQL) 12.14
```

{% hint style="info" %}

#### SemVer

Generally you probably want `@` syntax, but if you need more specificity we\
fully support [SemVer](https://devhints.io/semver):

```sh
$ pkgx postgres^12 --version
postgres (PostgreSQL) 12.14

$ pkgx "postgres>=12<14" --version
postgres (PostgreSQL) 13.11

$ pkgx deno=1.35.3 --version
deno 1.35.3
```

{% endhint %}

### Running the Latest Version

`pkgx foo` runs the latest “foo” that **is installed**.

If you want to ensure the latest version of “foo” is installed, use`pkgx mash upgrade foo`.

## Adding Additional Packages to the Execution Environment

It can be useful to run a program with additional packages in the environment.

```sh
pkgx +openssl cargo build
```

Here `+pkg` syntax added OpenSSL to Cargo’s environment. Thus the build will see\
the OpenSSL headers and libraries.

## Disambiguation

In some cases `pkgx foo` may be ambiguous because multiple packages provide`foo`.

In such cases `pkgx` will error and ask you be more specific by using\
fully-qualified-names:

```sh
$ pkgx yarn --version
error: multiple projects provide `yarn`. please be more specific:

    pkgx +classic.yarnpkg.com yarn --version
    pkgx +yarnpkg.com yarn --version
```

In general it's a good idea to specify fully qualified names in scripts, etc.\
since you want these to work forever.

## Running System Commands

It can be useful to run system commands with a package environment injected. To\
do this either specify the full path of the system executable:

```sh
pkgx +llvm.org /usr/bin/make
```

Or separate your commands with `--`:

```sh
pkgx +llvm.org -- make  # finds `make` in PATH, failing if none found
```

{% hint style="warning" %}
If you only specified `make` rather than `/usr/bin/make` or separating with`-- make` then `pkgx` would install GNU make for you and use that.
{% endhint %}

## Dumping the Environment

If you don’t specify anything to run, `pkgx` will install any `+pkg`s and then\
dump the environment:

```sh
$ pkgx +gum
PATH="$HOME/.pkgx/charm.sh/gum/v0.14.5/bin${PATH:+:$PATH}"
```

This can be useful in scripts or for adding tools to your shell:

```sh
$ eval "$(pkgx +gum)"
$ gum --version
gum version 0.14.5
```

For this mode we can also output JSON: `pkgx +gum --json`.

## Quietening Output

````sh
$ pkgx --quiet gum format 'download progress is still shown'
# ^^ supresses resolving/syncing etc. messages but not download progress info
# `pkgx -q` is the same

```sh
pkgx --silent gum format 'no output at all'
# ^^ silences everything, even errors
# ^^ `pkgx -qq` is the same
````

Note that this only effects `pkgx` *not the tools you run with `pkgx`*.

## Ensuring Packages

In some cases you don’t want to use a `pkgx` package if the user has that\
package already installed to their system. For these cases we provide an`ensure` script:

```sh
$ pkgx mash ensure git --version
# ^^ runs system `git` if installed, otherwise installs the `pkgx` pkg

$ eval "$(pkgx mash ensure +git)"
# ^^ adds pkgx git to the environment *unless* it is installed to the system
```

## “Virtual Environments”

You can set `PKGX_DIR` to have `pkgx` install packages there. This can be useful\
for creating “virtual environments” for various usages.

```sh
$ export PKGX_DIR="$PWD/foo"  # must be an absolute path or is ignored

$ pkgx +gum
$ find foo
foo/charm.sh/gum/v0.14.5/bin/gum

$ eval "$(pkgx +gum)"
$ echo $PATH
$PWD/foo/charm.sh/gum/v0.14.5/bin/gum:…
```

## Other Common Needs

`pkgx` is not a package manager. Thus the command itself doesn’t typically offer\
such operations you may expect, however the way `pkgx` works is simple and\
standardized so we offer some `mash` scripts to help.

Longer term we will make a tool `pkgq` to help with these operations.

### Listing Outdated Packages

```sh
pkgx mash outdated
```

### Upgrading Packages

`pkgx foo` executes the latest version of `foo` that is *downloaded*. To ensure\
you have (any) newer versions installed use this command:

```sh
$ pkgx mash upgrade
updating: /Users/mxcl/.pkgx/python.org/v3.11.11
# snip…
```

You can specify args to upgrade only specific packages.

### Pruning Older Versions of Packages

The `pkgx` download cache can get large over time. To prune older versions:

```sh
$ pkgx mash prune
pruning: ~/.pkgx/deno.land/v1.39.4
pruning: ~/.pkgx/deno.land/v1.46.3
# snip…
```

This may delete versions that you use—if so—this is fine. `pkgx` will just\
reinstall them next time you need them.

### Listing Available Versions for a Package

ie. what versions *could be* run by `pkgx`:

```sh
$ pkgx mash inventory git
2.38.1
2.39.0
# snip…
```

### Listing What is Downloaded

```sh
$ pkgx mash ls

  Parent Directory                │Version
  ────────────────────────────────┼──────────
  perl.org                        │5.40.0
  x.org/xcb                       │1.17.0
  # snip…
```


# Scripting

You can use `pkgx` as the [shebang](https://en.wikipedia.org/wiki/Shebang_\(Unix\)) for your scripts:

```python
#!/usr/bin/env -S pkgx python@3.9

import sys

print(sys.version)
```

```sh
$ chmod +x ./my-script.py
$ ./my-script.py
3.9.17
```

{% hint style="info" %}
Using `env` to invoke `pkgx` is typical for tools that\
have no POSIX location.

The `-S` parameter is required to pass multiple arguments.
{% endhint %}

## Including Additional pkgs

Scripts are the glue that allows open source to be composed into powerful new\
tools. With our `+pkg` syntax you make anything in open source available to your\
script.

```sh
#!/usr/bin/env -S pkgx +openssl deno run

Deno.dlopen("libssl.dylib")
```

{% hint style="info" %}
Robustness requires precisely specifying your\
environment:

```sh
#!/usr/bin/env -S pkgx bash>=4

source <(pkgx dev --shellcode)
# ^^ bash >=4 is required for this syntax, and eg macOS only comes with bash 3
```

{% endhint %}

## Scripting for Various Languages & Their Dependencies

### Python

Use `uv` to import PyPi dependencies:

```python
#!/usr/bin/env -S pkgx +python@3.11 uv run --with requests<=3 --with rich

import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
```

### Ruby

Use [Bundler](https://bundler.io):

```ruby
#!/usr/bin/env -S pkgx ruby@3

require 'bundler/inline'

gemfile do
  source 'https://rubygems.org'
  gem 'ruby-macho', '~> 3'
end
```

### JavaScript & TypeScript

Use [Deno](https://deno.land):

```javascript
#!/usr/bin/env -S pkgx deno@2 run

import fs from "npm:fs";
```

### Rust

````rust
#!/usr/bin/env -S pkgx rust-script

//! ```cargo
//! [dependencies]
//! time = "0.1.25"
//! ```
````

> \[!TIP]\
> Probably you should specify a more precise Rust version as a plus-pkg arg.

### Go, C, C++, etc

Use [Scriptisto](https://github.com/igor-petruk/scriptisto):

```c
#!/usr/bin/env pkgx +clang +pkg-config scriptisto

#include <stdio.h>
#include <glib.h>

// scriptisto-begin
// script_src: main.c
// build_cmd: clang -O2 main.c `pkg-config --libs --cflags glib-2.0` -o ./script
// scriptisto-end

int main(int argc, char *argv[]) {
  gchar* user = g_getenv("USER");
  printf("Hello, C! Current user: %s\n", user);
  return 0;
}
```

## Mash

We think `pkgx` scripting is so powerful that we made a whole package manager to\
show it off.

> <https://github.com/pkgxdev/mash>

## Other Examples

We make use of `pkgx` scripting all over our repositories. Check them out!

## Ultra Portable Scripts

Requiring a `pkgx` shebang is somewhat limiting. Instead you can use our `cURL`\
one-liner coupled with `+pkg` syntax to temporarily install pkgs and utilize\
them in your scripts:

```sh
#!/bin/bash

eval "$(sh <(curl https://pkgx.sh) +git)"

which git  # prints soemthing like /tmp/pkgx/git-scm.org/v2.46.3/bin/git
```


# FAQ

## How do I run the latest version of `pkgx`?

Typically you want to upgrade `pkgx` so either:

1. `brew upgrade pkgx`; or
2. `curl -LSsf pkgx.sh | sh`

{% hint style="info" %}
Yes. Our installer upgrades `pkgx` too.
{% endhint %}

## How do I run the latest version of a specific pkg?

Unless otherwise instructed, `pkgx` executes the latest version of packages that*are downloaded*. The first time you run a package the latest version will be\
downloaded, but after that updates will only be fetched if requested or required\
by other packages.

For us neophiliacs we have written a \[`mash`] script to upgrade your `pkgx`\
packages:

```sh
pkgx mash upgrade
```

## How do I “install” pkgs?

Use [`pkgm`](https://github.com/pkgxdev/pkgm).

## What is a package?

A package is:

* A plain tarball containing a single project for a single platform and\
  architecture compiled from that project’s sources
* A bundle of metadata (`package.yml`) from the \[pantry]

Relative to some other packaging systems:

* No scripts are executed post “install”
* Packages must work from any location (we say our pkgs are “relocatable“)

## A package version I need is unavailable

Sorry about that. Open a [ticket](https://github.com/pkgxdev/pantry/issues/new) asking for it and we’ll build it.

## I need a pkg greater than v20.1.3 but less than v21

The commonly used `@` syntax would evaluate to v20.1.x (`@20.1.3`).

To provide more control we support the[full semantic version range syntax](https://devhints.io/semver). So for the\
given example we would use the caret (`^`):

```sh
$ pkgx node^20.1.3 --version
v20.1.5
```

Which will match node v20.1.3 up to but not including v21.

## What does `+pkg` syntax do?

`+pkg` syntax is a way to include additional pkgs in your environment. Typing`pkgx +deno` dumps the environment to the terminal, if you add additional\
commands then those commands are invoked in that environment.

## How do I list what packages are downloaded?

We have created a \[`mash`] script to list everything `pkgx` has downloaded:

```sh
pkgx mash ls
```

All packages are encapsulated in individual, versioned folders in `~/.pkgx` just\
like `brew` so you can just browse them with a file browser.

## A pkg I was expecting is not available

Open source is ever moving and somebody needs to keep up with it. You may need\
to contribute to the [pantry](https://github.com/pkgxdev/pkgx/blob/main/docs/pantry.md).

## Where do you put pkgs?

Everything goes in `~/.pkgx`. eg. Deno v1.2.3 is an independent POSIX prefix at`~/.pkgx/deno.land/v1.2.3`, thus the `deno` executable is at`~/.pkgx/deno.land/v1.2.3/bin/deno`.

We also create symlinks for majors, minors and latest:

```sh
$ cd ~/.pkgx/deno.land
$ ls -la
v*   -> v1.2.3
v1   -> v1.2.3
v1.2 -> v1.2.3
```

Open source is vast and unregulated, thus we use fully-qualified naming scheme\
to ensure pkgs can be disambiguated.

## Can I bundle `~/.pkgx` into my distributable app?

Yes! Our pkgs are relocatable.

## Will you support other platforms?

We would love to support all platforms. All that is holding is back from new\
platforms is expertise. Will you help? [Let’s talk](https://github.com/pkgxdev/pkgx/issues/607).

## How do I add my package to pkgx?

You need to add to the [pantry](https://github.com/pkgxdev/pkgx/blob/main/docs/pantry.md).

{% hint style="info" %}
Eventually we will support describing how to build or\
obtain distributables for your package via your repo so you can just add a`pkgx.yaml` and users can use pkgx to use your package automatically.
{% endhint %}

## How should I recommend people use my pkg with pkgx?

```sh
pkgx your-package --args
```

You can also recommend our shell one-liner if you like:

```sh
sh <(curl https://pkgx.sh) your-package --args
```

This is neat because `pkgx` is *not installed* and it runs your package from a\
temporary location making this a very low friction way to try out your package.

Finally, you can have them try your package out via our Docker image:

```sh
docker run pkgxdev/pkgx your-package --args
```

## How do I uninstall `pkgx`?

```sh
sudo rm /usr/local/bin/pkg[xm]
rm -rf ~/.pkgx
```

Then there are a couple platform specific cache/data directories:

### macOS

```sh
rm -rf ~/Library/Caches/pkgx
rm -rf ~/Library/Application\ Support/pkgx
```

### Non macOS

```sh
rm -rf "${XDG_CACHE_HOME:-$HOME/.cache}/pkgx"
rm -rf "${XDG_DATA_HOME:-$HOME/.local/share}"/pkgx
```

{% hint style="warning" %}

#### Caveats

Though not a problem unique to `pkgx` you should note that tools run with `pkgx`\
may have polluted your system during use. Check directories like:

* `~/.local`
* `~/.gem`
* `~/.npm`
* `~/.node`
* etc.
  {% endhint %}

## What are the rules for `@` syntax?

The rules for `@` are complex, but more human. We convert them to the following[semver](https://devhints.io/semver) syntax:

* `@3` → `^3`
* `@3.1` → `~3.1`
* `@3.1.2` → `>=3.1.2<3.1.3`
* `@3.1.2.3` → `>=3.1.2.3<3.1.3.4`
* etc.

## Where does `pkgx` store files

Packages are downloaded to `$PKGX_DIR` if set. If not set:

* macOS
  * `~/Library/Packages` if the directory exists
  * `~/.pkgx` otherwise
* \*nix
  * `~/.pkgx` if the directory exists
  * `${XDG_DATA_HOME:-$HOME/.local/share}/pkgx` otherwise

Some cache data is stored:

* `~/Library/Caches/pkgx` on Mac
* `${XDG_CACHE_HOME:-$HOME/.cache}/pkgx` on \*nix
* `%LOCALAPPDATA%/pkgx` on Windows

## What happens if two packages provide the same named program?

We error with a method to disambiguation, eg:

```sh
$ yarn
× multiple projects provide: yarn
│ pls be more specific:
│
│     pkgx +classic.yarnpkg.com --internal.use +yarn
│     pkgx +yarnpkg.com --internal.use +yarn
│
╰─➤ https://docs.pkgx.sh/help/ambiguous-pkgspec
```

## How do I see a man page for a pkgx pkg?

`man foo` won’t work since pkgx pkgs are not “installed”. Thus you have to first\
create an environment that contains that package before invoking `man`:

```sh
pkgx +foo man foo
```

This uses pkgx’s `man` tool. To use the system `man`:

```sh
pkgx +foo -- man foo
```

## Where is the `pkgx` GPG Public Key?

<https://dist.pkgx.dev/gpg-public.asc>.

## I have another question

[Support](https://github.com/pkgxdev/pkgx/blob/main/docs/support.md)

[`mash`](https://mash/pkgx.sh)


# Deeper Dives


# How pkgx Works: A Conceptual Overview

Everything `pkgx` does involves initially creating package environment. It then either runs commands inside those environments or injects those environments into your running shell.

A command like:

```sh
pkgx node start
```

Is in fact implicitly:

```sh
pkgx +node -- node start
```

Which more precisely† is in fact:

```sh
pkgx +nodejs.org -- node start
```

> † see [disambiguation](https://github.com/pkgxdev/pkgx/blob/main/docs/deeper-dives/pkgx-cmd.md#disambiguation)

The `+pkg` syntax creates the package environment that `node start` is then run within.

In fact you can see that env if you invoke `pkgx` raw:

```sh
$ pkgx +node
SSL_CERT_FILE=~/.pkgx/curl.se/ca-certs/v2023.5.30/ssl/cert.pem
PATH=~/.pkgx/unicode.org/v71.1.0/bin:~/.pkgx/unicode.org/v71.1.0/sbin:~/.pkgx/openssl.org/v1.1.1u/bin:~/.pkgx/nodejs.org/v20.5.0/bin
MANPATH=~/.pkgx/unicode.org/v71.1.0/share/man:~/.pkgx/zlib.net/v1.2.13/share/man:~/.pkgx/nodejs.org/v20.5.0/share/man:/usr/share/man
PKG_CONFIG_PATH=~/.pkgx/unicode.org/v71.1.0/lib/pkgconfig:~/.pkgx/openssl.org/v1.1.1u/lib/pkgconfig:~/.pkgx/zlib.net/v1.2.13/lib/pkgconfig
LIBRARY_PATH=~/.pkgx/unicode.org/v71.1.0/lib:~/.pkgx/openssl.org/v1.1.1u/lib:~/.pkgx/zlib.net/v1.2.13/lib
LD_LIBRARY_PATH=~/.pkgx/unicode.org/v71.1.0/lib:~/.pkgx/openssl.org/v1.1.1u/lib:~/.pkgx/zlib.net/v1.2.13/lib
CPATH=~/.pkgx/unicode.org/v71.1.0/include:~/.pkgx/openssl.org/v1.1.1u/include:~/.pkgx/zlib.net/v1.2.13/include:~/.pkgx/nodejs.org/v20.5.0/include
XDG_DATA_DIRS=~/.pkgx/unicode.org/v71.1.0/share:~/.pkgx/zlib.net/v1.2.13/share:~/.pkgx/nodejs.org/v20.5.0/share
DYLD_FALLBACK_LIBRARY_PATH=~/.pkgx/unicode.org/v71.1.0/lib:~/.pkgx/openssl.org/v1.1.1u/lib:~/.pkgx/zlib.net/v1.2.13/lib
```

This is a composable primitive, you could imagine `pkgx npm start` to be:

```sh
env "$(pkgx +npmjs.org)" npm start
```


# Using pkgx with a C/C++ Pipeline

We have most of the most popular c & c++ libraries pkg’d so just add them to your developer environment.

```yaml
# pkgx.yaml

dependencies:
  openssl.org: ^3
  github.com/gabime/spdlog: ^1
  llvm.org: ^14
  gnu.org/autoconf: ^2
  cmake.org: ^3
```

Usually this is enough to have tools like Autoconf or CMake find the libraries sometimes though you may need to provide a helping hand. Examine the devenv with `pkgx` for path information.

Then `dev` to activate the environment.


# Packaging


# Contributing Packages

There’s millions of open source projects and `pkgx` needs your help to package\
them up!

{% hint style="success" %}
Visit [github.com/pkgxdev/pantry](https://github.com/pkgxdev/pantry) for the full documentation.
{% endhint %}

{% hint style="info" %}
Curious about a specific pkg? `pkgx bk edit deno` will open deno’s`package.yml` in your editor.
{% endhint %}

## Packagers Who Care

You trust us to just work and make your workflows happen. We take this job\
seriously and we go the extra mile on a per-package basis, for example:

* Our `git` ignores `.DS_Store` files by default
* Our RubyGems defaults to user-installs and ensures gems are in `PATH`
* Our `python` comes unversioned so the huge numbers of scripts that invoke`/usr/bin/env python` actually work
* Our `pyenv` automatically installs the python versions it needs

Additionally, we insist our pkgs are relocatable, which is why we can install in\
your home directory (but this also means you could pick up the whole `~/.pkgx`\
directory and bundle it with your app.) We also begin packaging new releases\
almost immediately as soon as they go live using various automations.

We care about your developer experience, *not ours*.


# API

Visit [dist.pkgx.dev](https://dist.pkgx.dev) for an HTTP index.

* sources (mirror)
  * `dist.pkgx.dev/<PKG>/versions.txt`
  * `dist.pkgx.dev/<PKG>/v<VERSION>.tar.gz`
  * `dist.pkgx.dev/<PKG>/v<VERSION>.sha256sum`
* bottles
  * `dist.pkgx.dev/<PKG>/<PLATFORM>/<ARCH>/versions.txt`
  * `dist.pkgx.dev/<PKG>/<PLATFORM>/<ARCH>/v<VERSION>.tar.gz`
  * `dist.pkgx.dev/<PKG>/<PLATFORM>/<ARCH>/v<VERSION>.tar.xz`
  * `dist.pkgx.dev/<PKG>/<PLATFORM>/<ARCH>/v<VERSION>.asc`
  * `dist.pkgx.dev/<PKG>/<PLATFORM>/<ARCH>/v<VERSION>.sha256sum`

`versions.txt` files are newline separated, sorted lists of available versions\
for each type of distributable.

{% hint style="warning" %}
`dist.pkgx.dev/<PKG>/versions.txt` and the bottle`versions.txt` may not be the same. Always check the more specific`versions.txt`.
{% endhint %}

## The Pantry

The [pantry](https://github.com/pkgxdev/pantry) is our API for pkg metadata.

## libpkgx

Install and run `pkgx` packages from your apps.

* [Rust](https://github.com/pkgxdev/pkgx)
* [TypeScript](https://github.com/pkgxdev/libpkgx)


