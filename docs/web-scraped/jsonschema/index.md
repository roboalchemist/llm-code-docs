# Source: https://python-jsonschema.readthedocs.io/

Title: jsonschema

URL Source: https://python-jsonschema.readthedocs.io/

Markdown Content:
[![Image 1: PyPI version](https://img.shields.io/pypi/v/jsonschema.svg)](https://pypi.org/project/jsonschema/)[![Image 2: Supported Python versions](https://img.shields.io/pypi/pyversions/jsonschema.svg)](https://pypi.org/project/jsonschema/)[![Image 3: Build status](https://github.com/python-jsonschema/jsonschema/workflows/CI/badge.svg)](https://github.com/python-jsonschema/jsonschema/actions?query=workflow%3ACI)[![Image 4: ReadTheDocs status](https://readthedocs.org/projects/python-jsonschema/badge/?version=stable&style=flat)](https://python-jsonschema.readthedocs.io/en/stable/)[![Image 5: pre-commit.ci status](https://results.pre-commit.ci/badge/github/python-jsonschema/jsonschema/main.svg)](https://results.pre-commit.ci/latest/github/python-jsonschema/jsonschema/main)[![Image 6: Zenodo DOI](https://zenodo.org/badge/3072629.svg)](https://zenodo.org/badge/latestdoi/3072629)

`jsonschema` is an implementation of the [JSON Schema](https://json-schema.org/) specification for Python.

>>> from jsonschema import validate

>>> # A sample schema, like what we'd get from json.load()
>>> schema = {
...     "type" : "object",
...     "properties" : {
...         "price" : {"type" : "number"},
...         "name" : {"type" : "string"},
...     },
... }

>>> # If no exception is raised by validate(), the instance is valid.
>>> validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)

>>> validate(
...     instance={"name" : "Eggs", "price" : "Invalid"}, schema=schema,
... )
Traceback (most recent call last):
 ...
ValidationError: 'Invalid' is not of type 'number'

It can also be used from the command line by installing [check-jsonschema](https://github.com/python-jsonschema/check-jsonschema).

Features[¶](https://python-jsonschema.readthedocs.io/#features "Link to this heading")
--------------------------------------------------------------------------------------

*   Full support for [Draft 2020-12](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/validators/#jsonschema.validators.Draft202012Validator), [Draft 2019-09](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/validators/#jsonschema.validators.Draft201909Validator), [Draft 7](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/validators/#jsonschema.validators.Draft7Validator), [Draft 6](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/validators/#jsonschema.validators.Draft6Validator), [Draft 4](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/validators/#jsonschema.validators.Draft4Validator) and [Draft 3](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/validators/#jsonschema.validators.Draft3Validator)

*   [Lazy validation](https://python-jsonschema.readthedocs.io/en/latest/api/jsonschema/protocols/#jsonschema.protocols.Validator.iter_errors) that can iteratively report _all_ validation errors.

*   [Programmatic querying](https://python-jsonschema.readthedocs.io/en/latest/errors/) of which properties or items failed validation.

Installation[¶](https://python-jsonschema.readthedocs.io/#installation "Link to this heading")
----------------------------------------------------------------------------------------------

`jsonschema` is available on [PyPI](https://pypi.org/project/jsonschema/). You can install using [pip](https://pip.pypa.io/en/stable/):

$ pip install jsonschema

Running the Test Suite[¶](https://python-jsonschema.readthedocs.io/#running-the-test-suite "Link to this heading")
------------------------------------------------------------------------------------------------------------------

If you have `nox` installed (perhaps via `pipx install nox` or your package manager), running `nox` in the directory of your source checkout will run `jsonschema`’s test suite on all of the versions of Python `jsonschema` supports. If you don’t have all of the versions that `jsonschema` is tested under, you’ll likely want to run using `nox`’s `--no-error-on-missing-interpreters` option.

Of course you’re also free to just run the tests on a single version with your favorite test runner. The tests live in the `jsonschema.tests` package.

Benchmarks[¶](https://python-jsonschema.readthedocs.io/#benchmarks "Link to this heading")
------------------------------------------------------------------------------------------

`jsonschema`’s benchmarks make use of [pyperf](https://pyperf.readthedocs.io/). Running them can be done via:

$ nox -s perf

About[¶](https://python-jsonschema.readthedocs.io/#about "Link to this heading")
--------------------------------------------------------------------------------

I’m Julian Berman.

`jsonschema` is on [GitHub](https://github.com/python-jsonschema/jsonschema).

Get in touch, via GitHub or otherwise, if you’ve got something to contribute, it’d be most welcome!

If you feel overwhelmingly grateful, you can also [sponsor me](https://github.com/sponsors/Julian/).

And for companies who appreciate `jsonschema` and its continued support and growth, `jsonschema` is also now supportable via [TideLift](https://tidelift.com/subscription/pkg/pypi-jsonschema?utm_source=pypi-jsonschema&utm_medium=referral&utm_campaign=readme).

Contents[¶](https://python-jsonschema.readthedocs.io/#contents "Link to this heading")
--------------------------------------------------------------------------------------

*   [Schema Validation](https://python-jsonschema.readthedocs.io/en/stable/validate/)
    *   [The Basics](https://python-jsonschema.readthedocs.io/en/stable/validate/#the-basics)
    *   [The Validator Protocol](https://python-jsonschema.readthedocs.io/en/stable/validate/#the-validator-protocol)
    *   [Type Checking](https://python-jsonschema.readthedocs.io/en/stable/validate/#type-checking)
    *   [Versioned Validators](https://python-jsonschema.readthedocs.io/en/stable/validate/#versioned-validators)
    *   [Validating Formats](https://python-jsonschema.readthedocs.io/en/stable/validate/#validating-formats)

*   [Handling Validation Errors](https://python-jsonschema.readthedocs.io/en/stable/errors/)
    *   [`ValidationError.message`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.message)
    *   [`ValidationError.validator`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.validator)
    *   [`ValidationError.validator_value`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.validator_value)
    *   [`ValidationError.schema`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.schema)
    *   [`ValidationError.relative_schema_path`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.relative_schema_path)
    *   [`ValidationError.absolute_schema_path`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.absolute_schema_path)
    *   [`ValidationError.schema_path`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.schema_path)
    *   [`ValidationError.relative_path`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.relative_path)
    *   [`ValidationError.absolute_path`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.absolute_path)
    *   [`ValidationError.json_path`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.json_path)
    *   [`ValidationError.path`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.path)
    *   [`ValidationError.instance`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.instance)
    *   [`ValidationError.context`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.context)
    *   [`ValidationError.cause`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.cause)
    *   [`ValidationError.parent`](https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError.parent)
    *   [ErrorTrees](https://python-jsonschema.readthedocs.io/en/stable/errors/#errortrees)
    *   [best_match and relevance](https://python-jsonschema.readthedocs.io/en/stable/errors/#best-match-and-relevance)

*   [JSON (Schema) Referencing](https://python-jsonschema.readthedocs.io/en/stable/referencing/)
    *   [Introduction to the `referencing` API](https://python-jsonschema.readthedocs.io/en/stable/referencing/#introduction-to-the-referencing-api)
    *   [Common Scenarios](https://python-jsonschema.readthedocs.io/en/stable/referencing/#common-scenarios)
    *   [Migrating From `RefResolver`](https://python-jsonschema.readthedocs.io/en/stable/referencing/#migrating-from-refresolver)

*   [Creating or Extending Validator Classes](https://python-jsonschema.readthedocs.io/en/stable/creating/)
    *   [Creating Validation Errors](https://python-jsonschema.readthedocs.io/en/stable/creating/#creating-validation-errors)
    *   [The Validator Protocol](https://python-jsonschema.readthedocs.io/en/stable/creating/#the-validator-protocol)

*   [Frequently Asked Questions](https://python-jsonschema.readthedocs.io/en/stable/faq/)
    *   [My schema specifies format validation. Why do invalid instances seem valid?](https://python-jsonschema.readthedocs.io/en/stable/faq/#my-schema-specifies-format-validation-why-do-invalid-instances-seem-valid)
    *   [Can jsonschema be used to validate YAML, TOML, etc.?](https://python-jsonschema.readthedocs.io/en/stable/faq/#can-jsonschema-be-used-to-validate-yaml-toml-etc)
    *   [Why doesn’t my schema’s default property set the default on my instance?](https://python-jsonschema.readthedocs.io/en/stable/faq/#why-doesn-t-my-schema-s-default-property-set-the-default-on-my-instance)
    *   [How do jsonschema version numbers work?](https://python-jsonschema.readthedocs.io/en/stable/faq/#how-do-jsonschema-version-numbers-work)

*   [API Reference](https://python-jsonschema.readthedocs.io/en/stable/api/)
    *   [Submodules](https://python-jsonschema.readthedocs.io/en/stable/api/#submodules)
    *   [`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/api/#module-jsonschema)

### Indices and tables[¶](https://python-jsonschema.readthedocs.io/#indices-and-tables "Link to this heading")

*   [Index](https://python-jsonschema.readthedocs.io/en/stable/genindex/)
