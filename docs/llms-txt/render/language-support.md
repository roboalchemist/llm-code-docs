# Source: https://render.com/docs/language-support.md

# Supported Languages

Render natively supports *Node.js* / *Bun*, *Python*, *Ruby*, *Go*, *Rust*, and *Elixir*. While [creating a service](https://dashboard.render.com/create?type=web), just link your GitHub/GitLab/Bitbucket repo, choose the runtime for your language, and specify a branch to deploy.

Plus, you can use virtually _any_ programming language if you [deploy your code as a Docker image](#docker-support).

## Set your language version

By default, Render uses a recent, actively supported version of each natively supported language (listed in the table below).

*However, we still recommend setting a language version for your service.* Doing so helps you ensure consistent behavior between Render and your other environments (such as development).

See the table to learn how to set your language version:

------

###### Language

[*Node.js*](node-version)

###### Default Version*

`22.22.0`

###### How to Set a Version

Set the `NODE_VERSION` [environment variable](configure-environment-variables#setting-environment-variables), or add a `.node-version` file to your project root containing only the version number: ```
21.1.0
``` For additional options, see [Setting Your Node.js Version](node-version).

---

###### Language

[*Bun*](bun-version)

###### Default Version*

`1.3.4`

###### How to Set a Version

Set the `BUN_VERSION` [environment variable](configure-environment-variables#setting-environment-variables): ```
1.3.4
```

---

###### Language

[*Python*](python-version)

###### Default Version*

`3.14.3`

###### How to Set a Version

Set the `PYTHON_VERSION` [environment variable](configure-environment-variables#setting-environment-variables), or add a `.python-version` file to your project root containing only the version number: ```
3.12.11
``` For details, see [Setting Your Python Version](python-version). You can also set versions for the following package management tools:

- [uv](uv-version)
- [Poetry](poetry-version)

---

###### Language

[*Ruby*](ruby-version)

###### Default Version*

`3.4.4`

###### How to Set a Version

Set [the `ruby` directive](https://bundler.io/guides/gemfile_ruby.html) in your `Gemfile`, or add a `.ruby-version` file to your project root containing only the version number: ```
3.1.4
``` For details, see [Setting Your Ruby Version](ruby-version).

---

###### Language

**Go**

###### Default Version*

`1.26.0`

###### How to Set a Version

Render's native Go environment _always_ uses the latest stable Go `1.x` version. You can't set a different version unless you deploy a [Docker image](#docker-support).

---

###### Language

[*Rust*](rust-toolchain)

###### Default Version*

`stable`

###### How to Set a Version

Set the `RUSTUP_TOOLCHAIN` [environment variable](configure-environment-variables#setting-environment-variables), or add a `rust-toolchain` file to your project root containing only the toolchain version: ```
beta
``` For details, see [Specifying a Rust Toolchain](rust-toolchain).

---

###### Language

[*Elixir*](elixir-erlang-versions)

###### Default Version*

`1.18.4`

###### How to Set a Version

Set the `ELIXIR_VERSION` and/or `ERLANG_VERSION` [environment variables](configure-environment-variables#setting-environment-variables). If you don't set `ERLANG_VERSION`, Render automatically uses an Erlang version that's compatible with your `ELIXIR_VERSION`. For details, see [Setting Your Elixir and Erlang Versions](elixir-erlang-versions).

---

###### Language

*Other languages*

###### Default Version*

N/A

###### How to Set a Version

To use any language besides those listed above, deploy your code as a [Docker image](docker).

------

> **\*Render updates the default version for each language over time.*
>
> With the exception of Go and Rust, a particular service's default language version depends on when that service was first created. For details, see the version documentation for your language (linked from the table above).

### Minimum supported language versions

Render services cannot use versions of certain languages earlier than those listed below:

| Language | Minimum Supported Version |
| -------- | ------------------------- |
| Python   | `3.7.3`                   |
| Ruby     | `3.1.0`                   |
| Elixir   | `1.12.0`                  |
| Erlang   | `24.3.4`                  |

> *Render periodically updates the underlying version of Debian used by all services.**
>
> The language versions above correspond to the minimum supported versions for Debian 12.x [bookworm](https://www.debian.org/releases/bookworm/).

## Docker support

When you deploy a Docker image on Render, it can use virtually _any_ programming language and framework. This is true regardless of whether you:

- [Build your image on Render](docker#building-from-a-dockerfile), or
- [Pull a prebuilt image](/deploying-an-image) from your container registry.

Learn more about [Docker versus native runtimes](docker#docker-or-native-runtime).