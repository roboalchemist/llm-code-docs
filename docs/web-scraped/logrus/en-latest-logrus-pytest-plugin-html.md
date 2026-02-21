# Source: https://python-logrus.readthedocs.io/en/latest/logrus.pytest_plugin.html

Title: logrus.pytest_plugin module — logrus documentation

URL Source: https://python-logrus.readthedocs.io/en/latest/logrus.pytest_plugin.html

Markdown Content:
*   [](https://python-logrus.readthedocs.io/en/latest/index.html) »
*   [logrus](https://python-logrus.readthedocs.io/en/latest/modules.html) »
*   [logrus package](https://python-logrus.readthedocs.io/en/latest/logrus.html) »
*   logrus.pytest_plugin module
*   [Edit on GitHub](https://github.com/bbugyi200/logrus/blob/master/docs/source/logrus.pytest_plugin.rst)

* * *

A pytest plugin for testing the logrus package.

This plugin can be enabled via the pytest_plugins conftest.py variable. This allows us to use this plugin in external packages’ tests instead of just for this package’s tests.

Examples

The following line should be found in the “tests/conftest.py” file:

>>> pytest_plugins = ["logrus.pytest_plugin"]

mock_dynamic_log_fields(_mocker_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/pytest_plugin.html#mock_dynamic_log_fields)[](https://python-logrus.readthedocs.io/en/latest/logrus.pytest_plugin.html#logrus.pytest_plugin.mock_dynamic_log_fields "Permalink to this definition")
Mock dynamic fields that may be contained in log records.

Parameters
**mocker** (`MockerFixture`) –

Return type
`None`
