# Source: https://docs.prefect.io/contribute/contribute-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Contribute to integrations

Prefect welcomes contributions to existing integrations.

<Tip>
  Thinking about making your own integration? Feel free to [create a new discussion](https://github.com/PrefectHQ/prefect/discussions/new?category=ideas) to flesh out your idea with other contributors.
</Tip>

## Contributing to existing integrations

All integrations are hosted in the [Prefect GitHub repository](https://github.com/PrefectHQ/prefect) under `src/integrations`.

To contribute to an existing integration, please follow these steps:

<Steps>
  <Step title="Fork the repository 🍴">
    Fork the [Prefect GitHub repository](https://github.com/PrefectHQ/prefect)
  </Step>

  <Step title="Clone your fork 👯">
    ```bash  theme={null}
    git clone https://github.com/your-username/prefect.git
    ```
  </Step>

  <Step title="Create a new branch 🌲">
    ```bash  theme={null}
    git checkout -b my-new-branch
    ```
  </Step>

  <Step title="Set up your environment 📂">
    Move to the integration directory and install the dependencies:

    ```bash  theme={null}
    cd src/integrations/my-integration
    uv venv --python 3.12
    source .venv/bin/activate
    uv sync
    ```
  </Step>

  <Step title="Make your changes 👩‍🍳">
    Make the necessary changes to the integration code.
  </Step>

  <Step title="Add tests 🧪">
    If you're adding new functionality, please add tests.

    You can run the tests with:

    ```bash  theme={null}
    pytest tests
    ```
  </Step>

  <Step title="Submit your changes 📨">
    ```bash  theme={null}
    git add .
    git commit -m "My new integration"
    git push origin my-new-branch
    ```
  </Step>

  <Step title="Create a pull request ⏰">
    Submit your pull request upstream through the GitHub interface.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).