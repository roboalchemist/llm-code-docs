# Source: https://coveralls-python.readthedocs.io/en/latest/usage/vcsconfig.html

Title: VCS Configuration — coveralls-python 4.1.0 documentation

URL Source: https://coveralls-python.readthedocs.io/en/latest/usage/vcsconfig.html

Markdown Content:
VCS Configuration — coveralls-python 4.1.0 documentation
===============

VCS Configuration[¶](https://coveralls-python.readthedocs.io/en/latest/usage/vcsconfig.html#vcs-configuration "Link to this heading")
=====================================================================================================================================

`coveralls-python` supports `git` by default and will run the necessary `git` commands to collect the required information without any intervention.

As describe in [the coveralls docs](https://docs.coveralls.io/mercurial-support), you may also configure these values by setting environment variables. These will be used in the fallback case, eg. if `git` is not available or your project is not a `git` repository.

As described in the linked documentation, you can also use this method to support non- `git` projects:

GIT_ID=$(hg tip --template '{node}\n')
GIT_AUTHOR_NAME=$(hg tip --template '{author|person}\n')
GIT_AUTHOR_EMAIL=$(hg tip --template '{author|email}\n')
GIT_COMMITTER_NAME=$(hg tip --template '{author|person}\n')
GIT_COMMITTER_EMAIL=$(hg tip --template '{author|email}\n')
GIT_MESSAGE=$(hg tip --template '{desc}\n')
GIT_BRANCH=$(hg branch)

[coveralls-python](https://coveralls-python.readthedocs.io/en/latest/index.html)
================================================================================

### Navigation

*   [Usage](https://coveralls-python.readthedocs.io/en/latest/usage/index.html)
*   [Configuration](https://coveralls-python.readthedocs.io/en/latest/usage/configuration.html)
*   [VCS Configuration](https://coveralls-python.readthedocs.io/en/latest/usage/vcsconfig.html#)
*   [Usage Within Tox](https://coveralls-python.readthedocs.io/en/latest/usage/tox.html)
*   [Multiple Language Support](https://coveralls-python.readthedocs.io/en/latest/usage/multilang.html)
*   [Tips for .coveragerc](https://coveralls-python.readthedocs.io/en/latest/tips/coveragerc.html)
*   [Nosetests](https://coveralls-python.readthedocs.io/en/latest/tips/nosetests.html)
*   [Troubleshooting](https://coveralls-python.readthedocs.io/en/latest/troubleshooting.html)

*   [Authors](https://coveralls-python.readthedocs.io/en/latest/authors.html)

*   [Release](https://coveralls-python.readthedocs.io/en/latest/release.html)

### Related Topics

*   [Documentation overview](https://coveralls-python.readthedocs.io/en/latest/index.html)
    *   Previous: [Configuration](https://coveralls-python.readthedocs.io/en/latest/usage/configuration.html "previous chapter")
    *   Next: [Usage Within Tox](https://coveralls-python.readthedocs.io/en/latest/usage/tox.html "next chapter")

[![Image 1: Sponsored: CheckMK / Tribe29](https://media.ethicalads.io/media/images/2023/05/rtd_creatives_q2_23_dashboard_blue.png)](https://server.ethicalads.io/proxy/click/9865/019cdec4-a9e9-70c0-9c84-ab7612ff67f8/)

[**No more downtime.**Monitor your entire IT infrastructure with Checkmk all-in-one tool.**Start for free**](https://server.ethicalads.io/proxy/click/9865/019cdec4-a9e9-70c0-9c84-ab7612ff67f8/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)_ · [ℹ️](https://www.ethicalads.io/advertisers/topics/devops/?ref=rtd-sidebar-buy-ads)

![Image 2](https://server.ethicalads.io/proxy/view/9865/019cdec4-a9e9-70c0-9c84-ab7612ff67f8/)

 ©2013, TheKevJames. | Powered by [Sphinx 9.1.0](https://www.sphinx-doc.org/)&[Alabaster 1.0.0](https://alabaster.readthedocs.io/) | [Page source](https://coveralls-python.readthedocs.io/en/latest/_sources/usage/vcsconfig.rst.txt)
