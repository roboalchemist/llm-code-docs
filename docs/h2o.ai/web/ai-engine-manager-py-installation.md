# Source: https://h2oai.github.io/ai-engine-manager/py/installation

Title: Installation | AI Engine Manager

URL Source: https://h2oai.github.io/ai-engine-manager/py/installation

Markdown Content:
The **H2O AI Engine Manager Python client** provides programmatic access to create, manage, and interact with _AI Engines_ (Driverless AI, H2O-3, and Notebook engines) in _H2O AI Cloud_.

Prerequisites[​](https://h2oai.github.io/ai-engine-manager/py/installation#prerequisites "Direct link to Prerequisites")
------------------------------------------------------------------------------------------------------------------------

Before installing the client, ensure you have:

*   **Python 3.10 or higher** installed on your system
*   You need a valid **H2O AI Cloud account** with appropriate permissions to access AI Engines. Contact your administrator if you don't have access.

Installation[​](https://h2oai.github.io/ai-engine-manager/py/installation#installation "Direct link to Installation")
---------------------------------------------------------------------------------------------------------------------

The client is published on **PyPI** and can be installed using `pip`:

`pip install h2o-engine-manager`

Quickstart[​](https://h2oai.github.io/ai-engine-manager/py/installation#quickstart "Direct link to Quickstart")
---------------------------------------------------------------------------------------------------------------

Once installed, you can import the client from `h2o_engine_manager` and verify that the package is correctly installed.

`import h2o_engine_managerprint(h2o_engine_manager.__version__)`

Next Steps[​](https://h2oai.github.io/ai-engine-manager/py/installation#next-steps "Direct link to Next Steps")
---------------------------------------------------------------------------------------------------------------

*   **[Set up authentication](https://h2oai.github.io/ai-engine-manager/py/initialization)** - Configure access to your H2O AI Cloud instance
*   **Try the examples** - Start with the following examples: [Driverless AI engine](https://h2oai.github.io/ai-engine-manager/py/dai_examples) , [H2O-3 engine](https://h2oai.github.io/ai-engine-manager/py/h2o_examples), [Notebook engine](https://h2oai.github.io/ai-engine-manager/py/notebook_examples)
*   **[Migrate from Steam](https://h2oai.github.io/ai-engine-manager/py/migration)** - If you're upgrading from Enterprise Steam

* * *

Feedback

*   [Submit and view feedback for this page](https://github.com/h2oai/docs-issues-requests/issues/new?assignees=undefined&body=%23%23%23%20Documentation%20issue%2Frequest%0A%0A%3C!--%20Please%20provide%20a%20clear%20and%20concise%20description%20of%20the%20documentation%20issue%2Frequest%20--%3E%0A%0A%23%23%23%20Additional%20context%0A%0A%3C!--%20Please%20add%20any%20other%20context%20about%20the%20issue%2Frequest%20here%20(e.g.%2C%20images)%20--%3E%0A%0A%23%23%23%20Page%20details%20%0A%0A-%20Application%20name%3A%20AI%20Engine%20Manager%0A-%20Application%20version%3A%20undefined%0A-%20Page%20title%3A%20/ai-engine-manager/py/installation%20&title=%5BHAIC-APP%5D)
*   Send feedback about AI Engine Manager to [cloud-feedback@h2o.ai](mailto:cloud-feedback@h2o.ai)
