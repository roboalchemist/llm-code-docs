# Unibeautify Documentation
# Source: https://unibeautify.com/docs/about

**Unibeautify is a universal code beautifier.**

The one beautifier to rule them all!

Unibeautify joins multiple beautifiers into one unified experience.

![diagram](https://docs.google.com/drawings/d/1elu3OU4o37_lDiDNgovolXdY7D1VQ-_9nsDs5y1HlQY/pub?w=1314&h=732)

> "Beautifier" will refer to either a code formatter (e.g.
> [Prettier](https://prettier.io/)) or linter with fix mode enabled (e.g.
> `eslint --fix`).

Let's say you want to use multiple beautifiers to format the code in your
project, which use multiple languages. For example, for your
[JavaScript](/docs/language-javascript) you may format using
[Prettier](https://prettier.io/) and [ESLint](https://eslint.org/). You may
also have [Python](/docs/language-python) code you format with
[autopep8](https://github.com/hhatto/autopep8) or C++ code you format with
[ClangFormat](https://clang.llvm.org/docs/ClangFormat.html).

Each of these beautifiers support different options, languages, and editor
integrations. With Unibeautify, this experience is made consistent.

Let's consider [Atom](https://atom.io/) editor integration.

Atom Package| Prettier| ESLint| Autopep8| ClangFormat  
---|---|---|---|---  
[`atom-beautify`](https://atom.io/packages/atom-beautify) (Unibeautify for
Atom)| ✅| ✅| ✅| ✅  
[`prettier-atom`](https://atom.io/packages/prettier-atom)| ✅| ✅| ❌| ❌  
[`linter-eslint`](https://atom.io/packages/linter-eslint)| ❌| ✅| ❌| ❌  
[`python-autopep8`](https://atom.io/packages/python-autopep8)| ❌| ❌| ✅| ❌  
[`clang-format`](https://atom.io/packages/clang-format)| ❌| ❌| ❌| ✅  
  
**Unibeautify does not handle any of the code formatting itself.** Instead
Unibeautify focuses on managing the underlying beautifiers and providing an
exceptional user experience regardless of languages or beautifiers involved.

