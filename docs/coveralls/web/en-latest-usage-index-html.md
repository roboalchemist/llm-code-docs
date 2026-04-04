# Source: https://coveralls-python.readthedocs.io/en/latest/usage/index.html

Title: Usage — coveralls-python 4.1.0 documentation

URL Source: https://coveralls-python.readthedocs.io/en/latest/usage/index.html

Markdown Content:
Usage — coveralls-python 4.1.0 documentation
===============

Usage[¶](https://coveralls-python.readthedocs.io/en/latest/usage/index.html#usage "Link to this heading")
=========================================================================================================

This package works with any CI environment. Special handling has been included for some CI service providers, but coveralls-python can run anywhere.

To get started with coveralls-python, make sure to [add your repo](https://coveralls.io/repos/new) on the coveralls.io website. If you will be using coveralls-python on TravisCI, you’re done here – otherwise, take note of the “repo token” in the coveralls.io dashboard.

After that, its as simple as installing coveralls-python, collecting coverage results, and sending them to coveralls.io.

For example:

pip install coveralls
coverage run --source=my_package setup.py test
COVERALLS_REPO_TOKEN=tGSdG5Qcd2dcQa2oQN9GlJkL50wFZPv1j coveralls

coveralls-python can be configured with several environment variables, as seen above. See [Configuration](https://coveralls-python.readthedocs.io/en/latest/usage/configuration.html#configuration) for more details.

[coveralls-python](https://coveralls-python.readthedocs.io/en/latest/index.html)
================================================================================

### Navigation

*   [Usage](https://coveralls-python.readthedocs.io/en/latest/usage/index.html#)
*   [Configuration](https://coveralls-python.readthedocs.io/en/latest/usage/configuration.html)
*   [VCS Configuration](https://coveralls-python.readthedocs.io/en/latest/usage/vcsconfig.html)
*   [Usage Within Tox](https://coveralls-python.readthedocs.io/en/latest/usage/tox.html)
*   [Multiple Language Support](https://coveralls-python.readthedocs.io/en/latest/usage/multilang.html)
*   [Tips for .coveragerc](https://coveralls-python.readthedocs.io/en/latest/tips/coveragerc.html)
*   [Nosetests](https://coveralls-python.readthedocs.io/en/latest/tips/nosetests.html)
*   [Troubleshooting](https://coveralls-python.readthedocs.io/en/latest/troubleshooting.html)

*   [Authors](https://coveralls-python.readthedocs.io/en/latest/authors.html)

*   [Release](https://coveralls-python.readthedocs.io/en/latest/release.html)

### Related Topics

*   [Documentation overview](https://coveralls-python.readthedocs.io/en/latest/index.html)
    *   Previous: [coveralls-python](https://coveralls-python.readthedocs.io/en/latest/index.html "previous chapter")
    *   Next: [Configuration](https://coveralls-python.readthedocs.io/en/latest/usage/configuration.html "next chapter")

[![Image 1: Sponsored: Augment](https://media.ethicalads.io/media/images/2026/01/cropped_EBRxlX2.png)](https://server.ethicalads.io/proxy/click/10069/019cdec4-6810-7931-9b6d-fc175481bbad/)

[**Augment Code Review**Benchmarked #1 Against Cursor, Copilot, Claude**Install Now**](https://server.ethicalads.io/proxy/click/10069/019cdec4-6810-7931-9b6d-fc175481bbad/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)_ · [ℹ️](https://www.ethicalads.io/advertisers/?ref=rtd-sidebar-buy-ads)

![Image 2](https://server.ethicalads.io/proxy/view/10069/019cdec4-6810-7931-9b6d-fc175481bbad/)

 ©2013, TheKevJames. | Powered by [Sphinx 9.1.0](https://www.sphinx-doc.org/)&[Alabaster 1.0.0](https://alabaster.readthedocs.io/) | [Page source](https://coveralls-python.readthedocs.io/en/latest/_sources/usage/index.rst.txt)
