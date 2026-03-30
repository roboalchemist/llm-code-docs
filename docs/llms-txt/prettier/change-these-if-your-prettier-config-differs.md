# (change these if your Prettier config differs)
end_of_line = lf
indent_style = space
indent_size = 2
max_line_length = 80
```

Here’s a copy+paste-ready `.editorconfig` file if you use the default options:

```ini
[*]
charset = utf-8
insert_final_newline = true
end_of_line = lf
indent_style = space
indent_size = 2
max_line_length = 80
```


---


### Editor Integration

---
id: editors
title: Editor Integration
---

To get the most out of Prettier, it’s recommended to run it from your editor.

If your editor does not support Prettier, you can instead [run Prettier with a file watcher](watching-files.md).

**Note!** It’s important to [install](install.md) Prettier locally in every project, so each project gets the correct Prettier version.

## Visual Studio Code

`prettier-vscode` can be installed using the extension sidebar – it’s called “Prettier - Code formatter.” [Check its repository for configuration and shortcuts](https://github.com/prettier/prettier-vscode).

If you’d like to toggle the formatter on and off, install [`vscode-status-bar-format-toggle`](https://marketplace.visualstudio.com/items?itemName=tombonnike.vscode-status-bar-format-toggle).

## Emacs

Check out the [prettier-emacs](https://github.com/prettier/prettier-emacs) repo, or [prettier.el](https://github.com/jscheid/prettier.el). The package [Apheleia](https://github.com/raxod502/apheleia) supports multiple code formatters, including Prettier.

## Vim

[vim-prettier](https://github.com/prettier/vim-prettier) is a Prettier-specific Vim plugin. [Neoformat](https://github.com/sbdchd/neoformat), [ALE](https://github.com/w0rp/ale), and [coc-prettier](https://github.com/neoclide/coc-prettier) are multi-language Vim linter/formatter plugins that support Prettier.

For more details see [the Vim setup guide](vim.md).

## Helix

A formatter can be specified in your [Helix language configuration](https://docs.helix-editor.com/languages.html#language-configuration), which will take precedence over any language servers.

For more details see the [Helix external binary formatter configuration for Prettier](https://github.com/helix-editor/helix/wiki/External-formatter-configuration#prettier).

## Sublime Text

Sublime Text support is available through Package Control and the [JsPrettier](https://packagecontrol.io/packages/JsPrettier) plug-in.

## JetBrains WebStorm, PHPStorm, PyCharm...

See the [WebStorm setup guide](webstorm.md).

## Visual Studio

Install the [JavaScript Prettier extension](https://github.com/madskristensen/JavaScriptPrettier).

## Espresso

Espresso users can install the [espresso-prettier](https://github.com/eablokker/espresso-prettier) plugin.


---


### For Enterprise

---
id: for-enterprise
title: For Enterprise
---

## Available as part of the Tidelift Subscription

Tidelift is working with the maintainers of Prettier and thousands of other open source projects to deliver commercial support and maintenance for the open source dependencies you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact dependencies you use.

<a class="button button--primary" href="https://tidelift.com/subscription/pkg/npm-prettier?utm_source=npm-prettier&utm_medium=referral&utm_campaign=enterprise">Learn more</a>
<a class="button button--primary" href="https://tidelift.com/subscription/request-a-demo?utm_source=npm-prettier&utm_medium=referral&utm_campaign=enterprise">Request a demo</a>

<br />

### Enterprise-ready open source software—managed for you

The Tidelift Subscription is a managed open source subscription for application dependencies covering millions of open source projects across JavaScript, Python, Java, PHP, Ruby, .NET, and more.

Your subscription includes:

**Security updates**

Tidelift’s security response team coordinates patches for new breaking security vulnerabilities and alerts immediately through a private channel, so your software supply chain is always secure.

**Licensing verification and indemnification**

Tidelift verifies license information to enable easy policy enforcement and adds intellectual property indemnification to cover creators and users in case something goes wrong. You always have a 100% up-to-date bill of materials for your dependencies to share with your legal team, customers, or partners.

**Maintenance and code improvement**

Tidelift ensures the software you rely on keeps working as long as you need it to work. Your managed dependencies are actively maintained and we recruit additional maintainers where required.

**Package selection and version guidance**

We help you choose the best open source packages from the start—and then guide you through updates to stay on the best releases as new issues arise.

**Roadmap input**

Take a seat at the table with the creators behind the software you use. Tidelift’s participating maintainers earn more income as their software is used by more subscribers, so they’re interested in knowing what you need.

**Tooling and cloud integration**

Tidelift works with GitHub, GitLab, BitBucket, and more. We support every cloud platform (and other deployment targets, too).

The end result? All of the capabilities you expect from commercial-grade software, for the full breadth of open source you use. That means less time grappling with esoteric open source trivia, and more time building your own applications—and your business.

<a class="button button--primary" href="https://tidelift.com/subscription/pkg/npm-prettier?utm_source=npm-prettier&utm_medium=referral&utm_campaign=enterprise">Learn more</a>
<a class="button button--primary" href="https://tidelift.com/subscription/request-a-demo?utm_source=npm-prettier&utm_medium=referral&utm_campaign=enterprise">Request a demo</a>


---


### Ignoring Code

---
id: ignore
title: Ignoring Code
---

Use `.prettierignore` to ignore (i.e. not reformat) certain files and folders completely.

Use “prettier-ignore” comments to ignore parts of files.

## Ignoring Files: .prettierignore

To exclude files from formatting, create a `.prettierignore` file in the root of your project. `.prettierignore` uses [gitignore syntax](https://git-scm.com/docs/gitignore#_pattern_format).

Example:

```text