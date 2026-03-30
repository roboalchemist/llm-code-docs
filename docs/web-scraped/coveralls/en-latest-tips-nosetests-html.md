# Source: https://coveralls-python.readthedocs.io/en/latest/tips/nosetests.html

Title: Nosetests — coveralls-python 4.1.0 documentation

URL Source: https://coveralls-python.readthedocs.io/en/latest/tips/nosetests.html

Markdown Content:
Nosetests — coveralls-python 4.1.0 documentation
===============

Nosetests[¶](https://coveralls-python.readthedocs.io/en/latest/tips/nosetests.html#nosetests "Link to this heading")
====================================================================================================================

[Nosetests](http://nose.readthedocs.org/en/latest/plugins/cover.html) provide a plugin for coverage measurement of your code:

$ nosetests  --with-coverage --cover-package=<your_package_name>

However, nosetests gathers coverage for all executed code, ignoring the `source` config option in `.coveragerc`.

This well make `coveralls` report unnecessary files, which can be inconvenient. To workaround this issue, you can use the `omit` option in your `.coveragerc` to specify a list of filename patterns to leave out of reporting.

For example:

[report]
omit =
    */venv/*
    */my_project/ignorable_file.py
    */test_script.py

Note, that native `coverage.py` and `py.test` are not affected by this problem and do not require this workaround.

[coveralls-python](https://coveralls-python.readthedocs.io/en/latest/index.html)
================================================================================

### Navigation

*   [Usage](https://coveralls-python.readthedocs.io/en/latest/usage/index.html)
*   [Configuration](https://coveralls-python.readthedocs.io/en/latest/usage/configuration.html)
*   [VCS Configuration](https://coveralls-python.readthedocs.io/en/latest/usage/vcsconfig.html)
*   [Usage Within Tox](https://coveralls-python.readthedocs.io/en/latest/usage/tox.html)
*   [Multiple Language Support](https://coveralls-python.readthedocs.io/en/latest/usage/multilang.html)
*   [Tips for .coveragerc](https://coveralls-python.readthedocs.io/en/latest/tips/coveragerc.html)
*   [Nosetests](https://coveralls-python.readthedocs.io/en/latest/tips/nosetests.html#)
*   [Troubleshooting](https://coveralls-python.readthedocs.io/en/latest/troubleshooting.html)

*   [Authors](https://coveralls-python.readthedocs.io/en/latest/authors.html)

*   [Release](https://coveralls-python.readthedocs.io/en/latest/release.html)

### Related Topics

*   [Documentation overview](https://coveralls-python.readthedocs.io/en/latest/index.html)
    *   Previous: [Tips for .coveragerc](https://coveralls-python.readthedocs.io/en/latest/tips/coveragerc.html "previous chapter")
    *   Next: [Troubleshooting](https://coveralls-python.readthedocs.io/en/latest/troubleshooting.html "next chapter")

[![Image 1: Sponsored: MongoDB](https://media.ethicalads.io/media/images/2026/02/Build_Without_Limits-_240x180.jpg)](https://server.ethicalads.io/proxy/click/10206/019cdec5-515e-70e0-80e2-3f7a3296698f/)

[Stop mapping data to rigid tables. Use a document model that evolves with your AI models.](https://server.ethicalads.io/proxy/click/10206/019cdec5-515e-70e0-80e2-3f7a3296698f/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)_ · [ℹ️](https://www.ethicalads.io/advertisers/?ref=rtd-sidebar-buy-ads)

![Image 2](https://server.ethicalads.io/proxy/view/10206/019cdec5-515e-70e0-80e2-3f7a3296698f/)

 ©2013, TheKevJames. | Powered by [Sphinx 9.1.0](https://www.sphinx-doc.org/)&[Alabaster 1.0.0](https://alabaster.readthedocs.io/) | [Page source](https://coveralls-python.readthedocs.io/en/latest/_sources/tips/nosetests.rst.txt)
