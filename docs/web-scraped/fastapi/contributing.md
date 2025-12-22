# Source: https://fastapi.tiangolo.com/contributing/

# Development - Contributing[&para;](#development-contributing)

First, you might want to see the basic ways to [help FastAPI and get help](../help-fastapi/).

## Developing[&para;](#developing)

If you already cloned the [fastapi repository](https://github.com/fastapi/fastapi) and you want to deep dive in the code, here are some guidelines to set up your environment.

### Virtual environment[&para;](#virtual-environment)

Follow the instructions to create and activate a [virtual environment](../virtual-environments/) for the internal code of `fastapi`.

### Install requirements[&para;](#install-requirements)

After activating the environment, install the required packages:

`pip``uv`

It will install all the dependencies and your local FastAPI in your local environment.

### Using your local FastAPI[&para;](#using-your-local-fastapi)

If you create a Python file that imports and uses FastAPI, and run it with the Python from your local environment, it will use your cloned local FastAPI source code.

And if you update that local FastAPI source code when you run that Python file again, it will use the fresh version of FastAPI you just edited.

That way, you don't have to "install" your local version to be able to test every change.

Technical Details

This only happens when you install using this included `requirements.txt` instead of running `pip install fastapi` directly.

That is because inside the `requirements.txt` file, the local version of FastAPI is marked to be installed in "editable" mode, with the `-e` option.

### Format the code[&para;](#format-the-code)

There is a script that you can run that will format and clean all your code:

`$ bash scripts/format.sh
`

It will also auto-sort all your imports.

## Tests[&para;](#tests)

There is a script that you can run locally to test all the code and generate coverage reports in HTML:

`$ bash scripts/test-cov-html.sh
`

This command generates a directory `./htmlcov/`, if you open the file `./htmlcov/index.html` in your browser, you can explore interactively the regions of code that are covered by the tests, and notice if there is any region missing.

## Docs[&para;](#docs)

First, make sure you set up your environment as described above, that will install all the requirements.

### Docs live[&para;](#docs-live)

During local development, there is a script that builds the site and checks for any changes, live-reloading:

`$ python ./scripts/docs.py live

<span style="color: green;">[INFO]</span> Serving on http://127.0.0.1:8008
<span style="color: green;">[INFO]</span> Start watching changes
<span style="color: green;">[INFO]</span> Start detecting changes
`

It will serve the documentation on `http://127.0.0.1:8008`.

That way, you can edit the documentation/source files and see the changes live.

Tip

Alternatively, you can perform the same steps that scripts does manually.

Go into the language directory, for the main docs in English it's at `docs/en/`:

`$ cd docs/en/
`

Then run `mkdocs` in that directory:

`$ mkdocs serve --dev-addr 127.0.0.1:8008
`

#### Typer CLI (optional)[&para;](#typer-cli-optional)

The instructions here show you how to use the script at `./scripts/docs.py` with the `python` program directly.

But you can also use [Typer CLI](https://typer.tiangolo.com/typer-cli/), and you will get autocompletion in your terminal for the commands after installing completion.

If you install Typer CLI, you can install completion with:

`$ typer --install-completion

zsh completion installed in /home/user/.bashrc.
Completion will take effect once you restart the terminal.
`

### Docs Structure[&para;](#docs-structure)

The documentation uses [MkDocs](https://www.mkdocs.org/).

And there are extra tools/scripts in place to handle translations in `./scripts/docs.py`.

Tip

You don't need to see the code in `./scripts/docs.py`, you just use it in the command line.

All the documentation is in Markdown format in the directory `./docs/en/`.

Many of the tutorials have blocks of code.

In most of the cases, these blocks of code are actual complete applications that can be run as is.

In fact, those blocks of code are not written inside the Markdown, they are Python files in the `./docs_src/` directory.

And those Python files are included/injected in the documentation when generating the site.

### Docs for tests[&para;](#docs-for-tests)

Most of the tests actually run against the example source files in the documentation.

This helps to make sure that:

- The documentation is up-to-date.

- The documentation examples can be run as is.

- Most of the features are covered by the documentation, ensured by test coverage.

#### Apps and docs at the same time[&para;](#apps-and-docs-at-the-same-time)

If you run the examples with, e.g.:

`$ fastapi dev tutorial001.py

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
`

as Uvicorn by default will use the port `8000`, the documentation on port `8008` won't clash.

### Translations[&para;](#translations)

Attention

**Update on Translations**

We're updating the way we handle documentation translations.

Until now, we invited community members to translate pages via pull requests, which were then reviewed by at least two native speakers. While this has helped bring FastAPI to many more users, we’ve also run into several challenges - some languages have only a few translated pages, others are outdated and hard to maintain over time.
To improve this, we’re working on automation tools 🤖 to manage translations more efficiently. Once ready, documentation will be machine-translated and still reviewed by at least two native speakers ✅ before publishing. This will allow us to keep translations up-to-date while reducing the review burden on maintainers.

What’s changing now:

- 

🚫 We’re no longer accepting new community-submitted translation PRs.

- 

⏳ Existing open PRs will be reviewed and can still be merged if completed within the next 3 weeks (since July 11 2025).

- 

🌐 In the future, we will only support languages where at least three active native speakers are available to review and maintain translations.

This transition will help us keep translations more consistent and timely while better supporting our contributors 🙌. Thank you to everyone who has contributed so far — your help has been invaluable! 💖

Help with translations is VERY MUCH appreciated! And it can't be done without the help from the community. 🌎 🚀

Here are the steps to help with translations.

#### Tips and guidelines[&para;](#tips-and-guidelines)

- 

Check the currently [existing pull requests](https://github.com/fastapi/fastapi/pulls) for your language. You can filter the pull requests by the ones with the label for your language. For example, for Spanish, the label is [`lang-es`](https://github.com/fastapi/fastapi/pulls?q=is%3Aopen+sort%3Aupdated-desc+label%3Alang-es+label%3Aawaiting-review).

- 

Review those pull requests, requesting changes or approving them. For the languages I don't speak, I'll wait for several others to review the translation before merging.

Tip

You can [add comments with change suggestions](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request) to existing pull requests.

Check the docs about [adding a pull request review](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-reviews) to approve it or request changes.

- 

Check if there's a [GitHub Discussion](https://github.com/fastapi/fastapi/discussions/categories/translations) to coordinate translations for your language. You can subscribe to it, and when there's a new pull request to review, an automatic comment will be added to the discussion.

- 

If you translate pages, add a single pull request per page translated. That will make it much easier for others to review it.

- 

To check the 2-letter code for the language you want to translate, you can use the table [List of ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

#### Existing language[&para;](#existing-language)

Let's say you want to translate a page for a language that already has translations for some pages, like Spanish.

In the case of Spanish, the 2-letter code is `es`. So, the directory for Spanish translations is located at `docs/es/`.

Tip

The main ("official") language is English, located at `docs/en/`.

Now run the live server for the docs in Spanish:

`// Use the command "live" and pass the language code as a CLI argument
$ python ./scripts/docs.py live es

<span style="color: green;">[INFO]</span> Serving on http://127.0.0.1:8008
<span style="color: green;">[INFO]</span> Start watching changes
<span style="color: green;">[INFO]</span> Start detecting changes
`

Tip

Alternatively, you can perform the same steps that scripts does manually.

Go into the language directory, for the Spanish translations it's at `docs/es/`:

`$ cd docs/es/
`

Then run `mkdocs` in that directory:

`$ mkdocs serve --dev-addr 127.0.0.1:8008
`

Now you can go to [http://127.0.0.1:8008](http://127.0.0.1:8008) and see your changes live.

You will see that every language has all the pages. But some pages are not translated and have an info box at the top, about the missing translation.

Now let's say that you want to add a translation for the section [Features](../features/).

- Copy the file at:

`docs/en/docs/features.md
`

- Paste it in exactly the same location but for the language you want to translate, e.g.:

`docs/es/docs/features.md
`

Tip

Notice that the only change in the path and file name is the language code, from `en` to `es`.

If you go to your browser you will see that now the docs show your new section (the info box at the top is gone). 🎉

Now you can translate it all and see how it looks as you save the file.

#### Don't Translate these Pages[&para;](#dont-translate-these-pages)

🚨 Don't translate:

- Files under `reference/`

- `release-notes.md`

- `fastapi-people.md`

- `external-links.md`

- `newsletter.md`

- `management-tasks.md`

- `management.md`

- `contributing.md`

Some of these files are updated very frequently and a translation would always be behind, or they include the main content from English source files, etc.

#### Request a New Language[&para;](#request-a-new-language)

Let's say that you want to request translations for a language that is not yet translated, not even some pages. For example, Latin.

If there is no discussion for that language, you can start by requesting the new language. For that, you can follow these steps:

- Create a new discussion following the template.

- Get a few native speakers to comment on the discussion and commit to help review translations for that language.

Once there are several people in the discussion, the FastAPI team can evaluate it and can make it an official translation.

Then the docs will be automatically translated using AI, and the team of native speakers can review the translation, and help tweak the AI prompts.

Once there's a new translation, for example if docs are updated or there's a new section, there will be a comment in the same discussion with the link to the new translation to review.

#### New Language[&para;](#new-language)

Note

These steps will be performed by the FastAPI team.

Checking the link from above (List of ISO 639-1 codes), you can see that the 2-letter code for Latin is `la`.

Now you can create a new directory for the new language, running the following script:

`// Use the command new-lang, pass the language code as a CLI argument
$ python ./scripts/docs.py new-lang la

Successfully initialized: docs/la
`

Now you can check in your code editor the newly created directory `docs/la/`.

That command created a file `docs/la/mkdocs.yml` with a simple config that inherits everything from the `en` version:

`INHERIT: ../en/mkdocs.yml
`

Tip

You could also simply create that file with those contents manually.

That command also created a dummy file `docs/la/index.md` for the main page, you can start by translating that one.

You can continue with the previous instructions for an "Existing Language" for that process.

You can make the first pull request with those two files, `docs/la/mkdocs.yml` and `docs/la/index.md`. 🎉

#### Preview the result[&para;](#preview-the-result)

As already mentioned above, you can use the `./scripts/docs.py` with the `live` command to preview the results (or `mkdocs serve`).

Once you are done, you can also test it all as it would look online, including all the other languages.

To do that, first build all the docs:

`// Use the command "build-all", this will take a bit
$ python ./scripts/docs.py build-all

Building docs for: en
Building docs for: es
Successfully built docs for: es
`

This builds all those independent MkDocs sites for each language, combines them, and generates the final output at `./site/`.

Then you can serve that with the command `serve`:

`// Use the command "serve" after running "build-all"
$ python ./scripts/docs.py serve

Warning: this is a very simple server. For development, use mkdocs serve instead.
This is here only to preview a site with translations already built.
Make sure you run the build-all command first.
Serving at: http://127.0.0.1:8008
`

#### Translation specific tips and guidelines[&para;](#translation-specific-tips-and-guidelines)

- 
Translate only the Markdown documents (`.md`). Do not translate the code examples at `./docs_src`.

- 

In code blocks within the Markdown document, translate comments (`# a comment`), but leave the rest unchanged.

- 

Do not change anything enclosed in "``" (inline code).

- 

In lines starting with `///` translate only the text part after `|`. Leave the rest unchanged.

- 

You can translate info boxes like `/// warning` with for example `/// warning | Achtung`. But do not change the word immediately after the `///`, it determines the color of the info box.

- 

Do not change the paths in links to images, code files, Markdown documents.

- 

However, when a Markdown document is translated, the `#hash-parts` in links to its headings may change. Update these links if possible.

Search for such links in the translated document using the regex `#[^# ]`.

- Search in all documents already translated into your language for `your-translated-document.md`. For example VS Code has an option "Edit" -> "Find in Files".

- When translating a document, do not "pre-translate" `#hash-parts` that link to headings in untranslated documents.