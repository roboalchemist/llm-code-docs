# Source: https://dateparser.readthedocs.io/en/latest/contributing.html

Title: Contributing — DateParser 1.3.0 documentation

URL Source: https://dateparser.readthedocs.io/en/latest/contributing.html

Published Time: Tue, 10 Feb 2026 02:14:27 GMT

Markdown Content:
Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions[](https://dateparser.readthedocs.io/en/latest/contributing.html#types-of-contributions "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

### Report Bugs[](https://dateparser.readthedocs.io/en/latest/contributing.html#report-bugs "Link to this heading")

Report bugs at [https://github.com/scrapinghub/dateparser/issues](https://github.com/scrapinghub/dateparser/issues).

If you are reporting a bug, please include:

* Your operating system name and version.

* Any details about your local setup that might be helpful in troubleshooting.

* Detailed steps to reproduce the bug.

### Fix Bugs and Implement Features[](https://dateparser.readthedocs.io/en/latest/contributing.html#fix-bugs-and-implement-features "Link to this heading")

Look through the GitHub issues for bugs and feature requests. To avoid duplicate efforts, try to choose issues without related PRs or with staled PRs. We also encourage you to add new languages to the existing stack.

### Write Documentation[](https://dateparser.readthedocs.io/en/latest/contributing.html#write-documentation "Link to this heading")

Dateparser could always use more documentation, whether as part of the official Dateparser docs, in docstrings, or even on the web in blog posts, articles, and such.

After you make local changes to the documentation, you will be able to build the project running:

tox -e docs

Then open `.tox/docs/tmp/html/index.html` in a web browser to see your local build of the documentation.

Note

If you don’t have `tox` installed, you need to install it first using `pip install tox`.

### Submit Feedback[](https://dateparser.readthedocs.io/en/latest/contributing.html#submit-feedback "Link to this heading")

The best way to send feedback is to file an issue at [https://github.com/scrapinghub/dateparser/issues](https://github.com/scrapinghub/dateparser/issues).

If you are proposing a feature:

* Explain in detail how it would work.

* Keep the scope as narrow as possible, to make it easier to implement.

* Remember that contributions are welcome :)

Get Started![](https://dateparser.readthedocs.io/en/latest/contributing.html#get-started "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

Ready to contribute? Here’s how to set up dateparser for local development.

1. Fork the dateparser repo on GitHub.

2. Clone your fork locally:

$ git clone git@github.com:your_name_here/dateparser.git

1. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development:

$ mkvirtualenv dateparser
$ cd dateparser/
$ pip install -e .

1. Create a branch for local development:

$ git checkout -b name-of-your-bugfix-or-feature
Now you can make your changes locally.

1. When you’re done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox:

 $ tox

To get ``tox``, just ``pip install`` it into your virtualenv. In addition to tests, ``tox`` checks for code style and maximum line length (119 characters).

1. Commit your changes and push your branch to GitHub:

$ git add .
$ git commit -m "Your detailed description of your changes."
$ git push origin name-of-your-bugfix-or-feature
2.   Submit a pull request through the GitHub website.

Pull Request Guidelines[](https://dateparser.readthedocs.io/en/latest/contributing.html#pull-request-guidelines "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring, and add the feature to the list in _README.rst_.

3. Check the pipelines (Github Actions) in the PR comments (or in [https://github.com/scrapinghub/dateparser/actions](https://github.com/scrapinghub/dateparser/actions)) and make sure that the tests pass for all supported Python versions.

4. Check the new project coverage in the PR comments (or in [https://app.codecov.io/gh/scrapinghub/dateparser/pulls](https://app.codecov.io/gh/scrapinghub/dateparser/pulls)) and make sure that it remained equal or higher than previously.

5. Follow the core developers’ advice which aims to ensure code’s consistency regardless of the variety of approaches used by many contributors.

6. In case you are unable to continue working on a PR, please leave a short comment to notify us. We will be pleased to make any changes required to get it done.

Guidelines for Editing Translation Data[](https://dateparser.readthedocs.io/en/latest/contributing.html#guidelines-for-editing-translation-data "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

English is the primary language of Dateparser. Dates in all other languages are translated into English equivalents before they are parsed.

The language data that Dateparser uses to parse dates is in `dateparser/data/date_translation_data`. For each supported language, there is a Python file containing translation data.

Each translation data Python files contains different kinds of translation data for date parsing: month and week names - and their abbreviations, prepositions, conjunctions, frequently used descriptive words and phrases (like “today”), etc.

Translation data Python files are generated from the following sources:

* [Unicode CLDR](http://cldr.unicode.org/) data in JSON format, located at `dateparser_data/cldr_language_data/date_translation_data`

* Additional data from the Dateparser community in YAML format, located at `dateparser_data/supplementary_language_data/date_translation_data`

If you wish to extend the data of an existing language, or add data for a new language, you must:

1. Edit or create the corresponding file within `dateparser_data/supplementary_language_data/date_translation_data`

See existing files to learn how they are defined, and see [Language Data Template](https://dateparser.readthedocs.io/en/latest/template.html#language-data-template) for details.

1. Regenerate the corresponding file within `dateparser/data/date_translation_data` running the following script:

dateparser_scripts/write_complete_data.py
3.   Write tests that cover your changes

You should be able to find tests that cover the affected data, and use copy-and-paste to create the corresponding new test.

If in doubt, ask Dateparser maintainers for help.

Updating the List of Supported Languages and Locales[](https://dateparser.readthedocs.io/en/latest/contributing.html#updating-the-list-of-supported-languages-and-locales "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Whenever the content of `dateparser.data.languages_info.language_locale_dict` is modified, use `dateparser_scripts/update_supported_languages_and_locales.py` to update the corresponding documentation table:

dateparser_scripts/update_supported_languages_and_locales.py

Updating the Timezone Cache[](https://dateparser.readthedocs.io/en/latest/contributing.html#updating-the-timezone-cache "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

Whenever the content of `dateparser/timezones.py` is modified you need to rebuild the timezone cache.

Run this command: `BUILD_TZ_CACHE=1 python -c "import dateparser"`

which should update `dateparser/data/dateparser_tz_cache.pkl`
