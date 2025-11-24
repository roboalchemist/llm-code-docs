# Source: https://www.daytona.io/docs/en.md

The Daytona SDK provides official Python and TypeScript interfaces for interacting with Daytona,
enabling you to programmatically manage development environments and execute code.

### Quick Start

Run your first line of code in a Daytona Sandbox. Use our [LLMs context files](https://www.daytona.io/docs/en/getting-started.md#additional-examples) for faster development with AI assistants.

#### 1. Get Your API Key

- Go to the Daytona [Dashboard](https://app.daytona.io/dashboard).
- Create a new [API key](https://app.daytona.io/dashboard/keys). Make sure to save it securely,
  as it won't be shown again.

#### 2. Install the SDK

    ```bash
    pip install daytona
    ```

    ```bash
    npm install @daytonaio/sdk
    ```

#### 3. Write Your Code

    Create a file named: `main.py`

    ```python
    from daytona import Daytona, DaytonaConfig

    # Define the configuration

    config = DaytonaConfig(api_key="your-api-key")

    # Initialize the Daytona client

    daytona = Daytona(config)

    # Create the Sandbox instance

    sandbox = daytona.create()

    # Run the code securely inside the Sandbox

    response = sandbox.process.code_run('print("Hello World from code!")')
    if response.exit_code != 0:
      print(f"Error: {response.exit_code} {response.result}")
    else:
        print(response.result)

    # Clean up

    sandbox.delete()

    ```

    Create a file named: `index.mts`

    ```typescript
    import { Daytona } from '@daytonaio/sdk';

    // Initialize the Daytona client
    const daytona = new Daytona({ apiKey: 'your-api-key' });

    // Create the Sandbox instance
    const sandbox = await daytona.create({
      language: 'typescript',
    });

    // Run the code securely inside the Sandbox
    const response = await sandbox.process.codeRun('console.log("Hello World from code!")')
    console.log(response.result);

    // Clean up
    await sandbox.delete()
    ```

:::note
Replace `your-api-key` with the value from your Daytona dashboard.
:::

#### 4. Run It

    ```bash
    python main.py
    ```

    ```bash
    npx tsx index.mts
    ```

#### ✅ What You Just Did

- Installed the Daytona SDK.
- Created a secure sandbox environment.
- Executed code remotely inside that sandbox.
- Retrieved and displayed the output locally.

You're now ready to use Daytona for secure, isolated code execution.

<ExploreMore />