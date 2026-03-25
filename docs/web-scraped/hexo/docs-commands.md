# Source: https://hexo.io/docs/commands

Title: Commands

URL Source: https://hexo.io/docs/commands

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
[](https://github.com/hexojs/site/edit/master/source/docs/commands.md "Improve this doc")

[](https://hexo.io/docs/commands#init "init")init
-------------------------------------------------

$ hexo init [folder]

Initializes a website. If no `folder` is provided, Hexo will set up a website in the current directory.

This command is a shortcut that runs the following steps:

1. Git clone [hexo-starter](https://github.com/hexojs/hexo-starter) including [hexo-theme-landscape](https://github.com/hexojs/hexo-theme-landscape) into the current directory or a target folder if specified.
2. Install dependencies using a package manager: [Yarn 1](https://classic.yarnpkg.com/lang/en/), [pnpm](https://pnpm.io/) or [npm](https://docs.npmjs.com/cli/install), whichever is installed; if there are more than one installed, the priority is as listed. npm is bundled with [Node.js](https://hexo.io/docs/#Install-Node-js) by default.

[](https://hexo.io/docs/commands#new "new")new
----------------------------------------------

$ hexo new [layout] <title>

Creates a new article. If no `layout` is provided, Hexo will use the `default_layout` from [_config.yml](https://hexo.io/docs/configuration). Use the layout `draft` to create a draft. If the `title` contains spaces, surround it with quotation marks.

| Option | Description |
| --- | --- |
| `-p`, `--path` | Post path. Customize the path of the post. |
| `-r`, `--replace` | Replace the current post if existed. |
| `-s`, `--slug` | Post slug. Customize the URL of the post. |

By default, Hexo will use the title to define the path of the file. For pages, it will create a directory of that name and an `index.md` file in it. Use the `--path` option to override that behaviour and define the file path:

hexo new page --path about/me "About me"

will create `source/about/me.md` file with the title “About me” set in the front matter.

Please note that the title is mandatory. For example, this will not result in the behaviour you might expect:

hexo new page --path about/me

will create the post `source/_posts/about/me.md` with the title “page” in the front matter. This is because there is only one argument (`page`) and the default layout is `post`.

[](https://hexo.io/docs/commands#generate "generate")generate
-------------------------------------------------------------

$ hexo generate

Generates static files.

| Option | Description |
| --- | --- |
| `-d`, `--deploy` | Deploy after generation finishes |
| `-w`, `--watch` | Watch file changes |
| `-b`, `--bail` | Raise an error if any unhandled exception is thrown during generation |
| `-f`, `--force` | Force regenerate |
| `-c`, `--concurrency` | Maximum number of files to be generated in parallel. Default is infinity |

[](https://hexo.io/docs/commands#publish "publish")publish
----------------------------------------------------------

$ hexo publish [layout] <filename>

Publishes a draft.

[](https://hexo.io/docs/commands#server "server")server
-------------------------------------------------------

$ hexo server

Starts a local server. By default, this is at `http://localhost:4000/`.

| Option | Description |
| --- | --- |
| `-p`, `--port` | Override default port |
| `-s`, `--static` | Only serve static files |
| `-l`, `--log` | Enable logger. Override logger format. |

[](https://hexo.io/docs/commands#deploy "deploy")deploy
-------------------------------------------------------

$ hexo deploy

Deploys your website.

| Option | Description |
| --- | --- |
| `-g`, `--generate` | Generate before deployment |

[](https://hexo.io/docs/commands#render "render")render
-------------------------------------------------------

$ hexo render <file1> [file2] ...

Renders files.

| Option | Description |
| --- | --- |
| `-o`, `--output` | Output destination |

[](https://hexo.io/docs/commands#migrate "migrate")migrate
----------------------------------------------------------

$ hexo migrate <type>

[Migrates](https://hexo.io/docs/migration) content from other blog systems.

[](https://hexo.io/docs/commands#clean "clean")clean
----------------------------------------------------

$ hexo clean

Cleans the cache file (`db.json`) and generated files (`public`).

[](https://hexo.io/docs/commands#list "list")list
-------------------------------------------------

$ hexo list <type>

Lists all routes.

[](https://hexo.io/docs/commands#version "version")version
----------------------------------------------------------

$ hexo version

Displays version information.

[](https://hexo.io/docs/commands#config "config")config
-------------------------------------------------------

$ hexo config [key] [value]

Lists the configuration (`_config.yml`). If `key` is specified, only the value of the corresponding `key` in the configuration is shown; if both `key` and `value` are specified, the value of the corresponding `key` in the configuration is changed to `value`.

[](https://hexo.io/docs/commands#Options "Options")Options
----------------------------------------------------------

### [](https://hexo.io/docs/commands#Safe-mode "Safe mode")Safe mode

$ hexo --safe

Disables loading plugins and scripts. Try this if you encounter problems after installing a new plugin.

### [](https://hexo.io/docs/commands#Debug-mode "Debug mode")Debug mode

$ hexo --debug

Logs verbose messages to the terminal and to `debug.log`. Try this if you encounter any problems with Hexo. If you see errors, please [raise a GitHub issue](https://github.com/hexojs/hexo/issues/new?assignees=&labels=&projects=&template=bug_report.yml).

### [](https://hexo.io/docs/commands#Silent-mode "Silent mode")Silent mode

$ hexo --silent

Silences output to the terminal.

### [](https://hexo.io/docs/commands#Customize-config-file-path "Customize config file path")Customize config file path

$ hexo --config custom.yml

Uses a custom config file (instead of `_config.yml`). Also accepts a comma-separated list (no spaces) of JSON or YAML config files that will combine the files into a single `_multiconfig.yml`.

$ hexo --config custom.yml,custom2.json

### [](https://hexo.io/docs/commands#Display-drafts "Display drafts")Display drafts

$ hexo --draft

Displays draft posts (stored in the `source/_drafts` folder).

### [](https://hexo.io/docs/commands#Customize-CWD "Customize CWD")Customize CWD

$ hexo --cwd /path/to/cwd

Customizes the path of current working directory.
