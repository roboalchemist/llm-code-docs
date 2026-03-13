# Source: https://hexo.io/docs/troubleshooting

Title: Troubleshooting

URL Source: https://hexo.io/docs/troubleshooting

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
Troubleshooting | Hexo
===============

[Hexo](https://hexo.io/)
========================

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)[](https://github.com/hexojs/hexo)

English

[](https://hexo.io/docs/troubleshooting)

Troubleshooting
===============

[](https://github.com/hexojs/site/edit/master/source/docs/troubleshooting.md "Improve this doc")

In case you’re experiencing problems with using Hexo, here is a list of solutions to some frequently encountered issues. If this page doesn’t help you solve your problem, try doing a search on [GitHub](https://github.com/hexojs/hexo/issues) or our [Google Group](https://groups.google.com/group/hexo).

[](https://hexo.io/docs/troubleshooting#YAML-Parsing-Error "YAML Parsing Error")YAML Parsing Error[](https://hexo.io/docs/troubleshooting#YAML-Parsing-Error)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

JS-YAML: incomplete explicit mapping pair; a key node is missed at line 18, column 29:

 last_updated: Last updated: %s

Wrap the string with quotations if it contains colons.

JS-YAML: bad indentation of a mapping entry at line 18, column 31:

 last_updated:"Last updated: %s"

Make sure you are using soft tabs and add a space after colons.

You can see [YAML Spec](http://www.yaml.org/spec/1.2/spec.html) for more info.

[](https://hexo.io/docs/troubleshooting#EMFILE-Error "EMFILE Error")EMFILE Error[](https://hexo.io/docs/troubleshooting#EMFILE-Error)
-------------------------------------------------------------------------------------------------------------------------------------

Error: EMFILE, too many open files

Though Node.js has non-blocking I/O, the maximum number of synchronous I/O is still limited by the system. You may come across an EMFILE error when trying to generate a large number of files. You can try to run the following command to increase the number of allowed synchronous I/O operations.

$ ulimit -n 10000

**Error: cannot modify limit**

If you encounter the following error:

$ ulimit -n 10000

ulimit: open files: cannot modify limit: Operation not permitted

It means some system-wide configurations are preventing `ulimit` to being increased to a certain limit.

To override the limit:

1. Add the following line to “/etc/security/limits.conf”:

* * nofile 10000

# '*' applies to all users and '-' set both soft and hard limits

* The above setting may not apply in some cases, ensure “/etc/pam.d/login” and “/etc/pam.d/lightdm” have the following line. (Ignore this step if those files do not exist)

session required pam_limits.so

1. If you are on a [systemd-based](https://en.wikipedia.org/wiki/Systemd#Adoption) distribution, systemd may override “limits.conf”. To set the limit in systemd, add the following line in “/etc/systemd/system.conf” and “/etc/systemd/user.conf”:

DefaultLimitNOFILE=10000

1. Reboot

[](https://hexo.io/docs/troubleshooting#Process-Out-of-Memory "Process Out of Memory")Process Out of Memory[](https://hexo.io/docs/troubleshooting#Process-Out-of-Memory)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you encounter this error during generation:

FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - process out of memory

Increase Node.js heap memory size by changing the first line of `hexo-cli` (`which hexo` to look for the file).

# !/usr/bin/env node --max_old_space_size=8192

[Out of memory while generating a huge blog · Issue #1735 · hexojs/hexo](https://github.com/hexojs/hexo/issues/1735)

[](https://hexo.io/docs/troubleshooting#Git-Deployment-Problems "Git Deployment Problems")Git Deployment Problems[](https://hexo.io/docs/troubleshooting#Git-Deployment-Problems)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://hexo.io/docs/troubleshooting#RPC-failed "RPC failed")RPC failed[](https://hexo.io/docs/troubleshooting#RPC-failed)

error: RPC failed; result=22, HTTP code = 403

fatal: 'username.github.io' does not appear to be a git repository

Make sure you have [set up git](https://help.github.com/articles/set-up-git) on your computer properly or try to use HTTPS repository URL instead.

### [](https://hexo.io/docs/troubleshooting#Error-ENOENT-no-such-file-or-directory "Error: ENOENT: no such file or directory")Error: ENOENT: no such file or directory[](https://hexo.io/docs/troubleshooting#Error-ENOENT-no-such-file-or-directory)

If you get an error like `Error: ENOENT: no such file or directory` it’s probably due to mixing uppercase and lowercase letters in your tags, categories, or filenames. Git cannot automatically merge this change, so it breaks the automatic branching.

To fix this, try

1. Check every tag’s and category’s case and make sure they are the same.
2. Commit
3. Clean and build: `./node_modules/.bin/hexo clean && ./node_modules/.bin/hexo generate`
4. Manually copy the public folder to your desktop
5. Switch branch from your master branch to your deployment branch locally
6. Copy the contents of the public folder from your desktop into the deployment branch
7. Commit. You should see any merge conflicts appear that you can manually resolve.
8. Switch back to your master branch and deploy normally: `./node_modules/.bin/hexo deploy`

[](https://hexo.io/docs/troubleshooting#Server-Problems "Server Problems")Server Problems[](https://hexo.io/docs/troubleshooting#Server-Problems)
-------------------------------------------------------------------------------------------------------------------------------------------------

Error: listen EADDRINUSE

You may have started two Hexo servers at the same time or there might be another application using the same port. Try to modify the `port` setting or start the Hexo server with the `-p` flag.

$ hexo server -p 5000

[](https://hexo.io/docs/troubleshooting#Plugin-Installation-Problems "Plugin Installation Problems")Plugin Installation Problems[](https://hexo.io/docs/troubleshooting#Plugin-Installation-Problems)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

npm ERR! node-waf configure build

This error may occur when trying to install a plugin written in C, C++ or other non-JavaScript languages. Make sure you have installed the right compiler on your computer.

[](https://hexo.io/docs/troubleshooting#Error-with-DTrace-Mac-OS-X "Error with DTrace (Mac OS X)")Error with DTrace (Mac OS X)[](https://hexo.io/docs/troubleshooting#Error-with-DTrace-Mac-OS-X)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

{ [Error: Cannot find module './build/Release/DTraceProviderBindings'] code: 'MODULE_NOT_FOUND' }

{ [Error: Cannot find module './build/default/DTraceProviderBindings'] code: 'MODULE_NOT_FOUND' }

{ [Error: Cannot find module './build/Debug/DTraceProviderBindings'] code: 'MODULE_NOT_FOUND' }

DTrace install may have issue, use this:

$ npm install hexo --no-optional

See [#1326](https://github.com/hexojs/hexo/issues/1326#issuecomment-113871796)

[](https://hexo.io/docs/troubleshooting#Iterate-Data-Model-on-Jade-or-Swig "Iterate Data Model on Jade or Swig")Iterate Data Model on Jade or Swig[](https://hexo.io/docs/troubleshooting#Iterate-Data-Model-on-Jade-or-Swig)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Hexo uses [Warehouse](https://github.com/hexojs/warehouse) for its data model. It’s not an array so you may have to transform objects into iterables.

{% for post in site.posts.toArray() %}

{% endfor %}

[](https://hexo.io/docs/troubleshooting#Data-Not-Updated "Data Not Updated")Data Not Updated[](https://hexo.io/docs/troubleshooting#Data-Not-Updated)
-----------------------------------------------------------------------------------------------------------------------------------------------------

Some data cannot be updated, or the newly generated files are identical to those of the last version. Clean the cache and try again.

$ hexo clean

[](https://hexo.io/docs/troubleshooting#No-command-is-executed "No command is executed")No command is executed[](https://hexo.io/docs/troubleshooting#No-command-is-executed)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you can’t get any command except `help`, `init` and `version` to work and you keep getting content of `hexo help`, it could be caused by a missing `hexo` in `package.json`:

{

 "hexo": {

 "version": "3.2.2"

 }

}

[](https://hexo.io/docs/troubleshooting#Escape-Contents "Escape Contents")Escape Contents[](https://hexo.io/docs/troubleshooting#Escape-Contents)
-------------------------------------------------------------------------------------------------------------------------------------------------

Hexo uses [Nunjucks](https://mozilla.github.io/nunjucks/) to render posts ([Swig](https://node-swig.github.io/swig-templates/) was used in the older version, which shares a similar syntax). Content wrapped with `{{ }}` or `{% %}` will get parsed and may cause problems. You can skip the parsing by wrapping it with the [`raw`](https://hexo.io/docs/tag-plugins#Raw) tag plugin, a single backtick ``{{ }}`` or a triple backtick.

Alternatively, Nunjucks tags can be disabled through the renderer’s option (if supported), [API](https://hexo.io/api/renderer#Disable-Nunjucks-tags) or [front-matter](https://hexo.io/docs/front-matter).

{% raw %}

Hello {{ world }}

{% endraw %}

```

Hello {{ world }}

```

[](https://hexo.io/docs/troubleshooting#ENOSPC-Error-Linux "ENOSPC Error (Linux)")ENOSPC Error (Linux)[](https://hexo.io/docs/troubleshooting#ENOSPC-Error-Linux)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes when running the command `$ hexo server` it returns an error:

Error: watch ENOSPC ...

It can be fixed by running `$ npm dedupe` or, if that doesn’t help, try the following in the Linux console:

$ echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

This will increase the limit for the number of files you can watch.

[](https://hexo.io/docs/troubleshooting#EMPERM-Error-Windows-Subsystem-for-Linux "EMPERM Error (Windows Subsystem for Linux)")EMPERM Error (Windows Subsystem for Linux)[](https://hexo.io/docs/troubleshooting#EMPERM-Error-Windows-Subsystem-for-Linux)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When running `$ hexo server` in a BashOnWindows environment, it returns the following error:

Error: watch /path/to/hexo/theme/ EMPERM

Unfortunately, WSL does not currently support filesystem watchers. Therefore, the live updating feature of hexo’s server is currently unavailable. You can still run the server from a WSL environment by first generating the files and then running it as a static server:

$ hexo generate

$ hexo server -s

This is [a known BashOnWindows issue](https://github.com/Microsoft/BashOnWindows/issues/216), and on 15 Aug 2016, the Windows team said they would work on it. You can get progress updates and encourage them to prioritize it on [the issue’s UserVoice suggestion page](https://wpdev.uservoice.com/forums/266908-command-prompt-console-bash-on-ubuntu-on-windo/suggestions/13469097-support-for-filesystem-watchers-like-inotify).

[](https://hexo.io/docs/troubleshooting#Template-render-error "Template render error")Template render error[](https://hexo.io/docs/troubleshooting#Template-render-error)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes when running the command `$ hexo generate` it returns an error:

FATAL Something's wrong. Maybe you can find the solution here: http://hexo.io/docs/troubleshooting.html

Template render error: (unknown path)

Possible cause:

* There are some unrecognizable words in your file, e.g. invisible zero width characters.

* Incorrect use or limitation of [tag plugin](https://hexo.io/docs/tag-plugins).

  * Block-style tag plugin with content is not enclosed with `{% endplugin_name %}`

# Incorrect

{% codeblock %}

fn()

{% codeblock %}

# Incorrect

{% codeblock %}

fn()

# Correct

{% codeblock %}

fn()

{% endcodeblock %}

    *   Having Nunjucks-like syntax in a tag plugin, e.g. [`{#`](https://mozilla.github.io/nunjucks/templating.html#comments). A workaround for this example is to use [triple backtick](https://hexo.io/docs/tag-plugins#Backtick-Code-Block) instead. [Escape Contents](https://hexo.io/docs/troubleshooting#Escape-Contents) section has more details.

{% codeblock lang:bash %}

Size of array is ${#ARRAY}

{% endcodeblock %}

[](https://hexo.io/docs/troubleshooting#YAMLException-Issue-4917 "YAMLException (Issue #4917)")YAMLException (Issue [#4917](https://github.com/hexojs/hexo/issues/4917))[](https://hexo.io/docs/troubleshooting#YAMLException-Issue-4917)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Upgrading to `hexo^6.1.0` from an older version may cause the following error when running `$ hexo generate`:

YAMLException: Specified list of YAML types (or a single Type object) contains a non-Type object.

 at ...

This may be caused by an incorrect dependency(i.e. `js-yaml`) setting that can’t be solved automatically by the package manager, and you may have to update it manually running:

$ npm install js-yaml@latest

or

$ yarn add js-yaml@latest

if you use `yarn`.

Last updated: 2026-03-12[Prev](https://hexo.io/docs/plugins "Plugins")[Next](https://hexo.io/docs/contributing "Contributing")

**Contents**

1. [YAML Parsing Error](https://hexo.io/docs/troubleshooting#YAML-Parsing-Error)
2. [EMFILE Error](https://hexo.io/docs/troubleshooting#EMFILE-Error)
3. [Process Out of Memory](https://hexo.io/docs/troubleshooting#Process-Out-of-Memory)
4. [Git Deployment Problems](https://hexo.io/docs/troubleshooting#Git-Deployment-Problems)
    1.   [RPC failed](https://hexo.io/docs/troubleshooting#RPC-failed)
    2.   [Error: ENOENT: no such file or directory](https://hexo.io/docs/troubleshooting#Error-ENOENT-no-such-file-or-directory)

5. [Server Problems](https://hexo.io/docs/troubleshooting#Server-Problems)
6. [Plugin Installation Problems](https://hexo.io/docs/troubleshooting#Plugin-Installation-Problems)
7. [Error with DTrace (Mac OS X)](https://hexo.io/docs/troubleshooting#Error-with-DTrace-Mac-OS-X)
8. [Iterate Data Model on Jade or Swig](https://hexo.io/docs/troubleshooting#Iterate-Data-Model-on-Jade-or-Swig)
9. [Data Not Updated](https://hexo.io/docs/troubleshooting#Data-Not-Updated)
10. [No command is executed](https://hexo.io/docs/troubleshooting#No-command-is-executed)
11. [Escape Contents](https://hexo.io/docs/troubleshooting#Escape-Contents)
12. [ENOSPC Error (Linux)](https://hexo.io/docs/troubleshooting#ENOSPC-Error-Linux)
13. [EMPERM Error (Windows Subsystem for Linux)](https://hexo.io/docs/troubleshooting#EMPERM-Error-Windows-Subsystem-for-Linux)
14. [Template render error](https://hexo.io/docs/troubleshooting#Template-render-error)
15. [YAMLException (Issue #4917)](https://hexo.io/docs/troubleshooting#YAMLException-Issue-4917)

[Back to Top](https://hexo.io/docs/troubleshooting#)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

 © 2026 [Hexo](https://github.com/hexojs/hexo/graphs/contributors)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

[![Image 1](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)[](https://twitter.com/hexojs)[](https://github.com/hexojs/hexo)

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)*   [GitHub](https://github.com/hexojs/hexo)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

English
