# Source: https://www.daytona.io/docs/en.md

Daytona is an open-source, secure and elastic infrastructure for running AI-generated code.

Daytona provides isolated sandbox environments that you can manage programmatically using the Daytona SDK to run and control code execution.

Daytona SDK is available for [Python](https://www.daytona.io/docs/en/python-sdk.md), [TypeScript](https://www.daytona.io/docs/en/typescript-sdk.md) and [Ruby](https://www.daytona.io/docs/en/ruby-sdk.md) interfaces.

## Create an account

Open the [Daytona Dashboard ↗](https://app.daytona.io/) and create your account. Daytona supports account creation using an email and password, or by connecting your Google or GitHub account.

## Obtain an API key

Generate an [API key](https://www.daytona.io/docs/en/api-keys.md) from the [Daytona Dashboard ↗](https://app.daytona.io/dashboard/keys) to authenticate SDK requests and access Daytona services. Save the API key securely, as it won't be shown again.

:::tip
Daytona supports multiple options to configure your environment: [in code](https://www.daytona.io/docs/en/configuration.md#configuration-in-code), [environment variables](https://www.daytona.io/docs/en/configuration.md#environment-variables), [.env file](https://www.daytona.io/docs/en/configuration.md#env-file), and [default values](https://www.daytona.io/docs/en/configuration.md#default-values).
:::

## Install the SDK

Install the Daytona SDK to interact with sandboxes from your code using [Python](https://www.daytona.io/docs/python-sdk.md), [TypeScript](https://www.daytona.io/docs/typescript-sdk.md) or [Ruby](https://www.daytona.io/docs/ruby-sdk.md).


    ```bash
    pip install daytona
    ```



    ```bash
    npm install @daytonaio/sdk
    ```


    ```bash
    gem install daytona
    ```

## Create a Sandbox

Create a Daytona Sandbox to run your code securely in an isolated environment.

  
    ```python
    # Import the Daytona SDK
    from daytona import Daytona, DaytonaConfig

    # Define the configuration
    config = DaytonaConfig(api_key="YOUR_API_KEY") # Replace with your API key

    # Initialize the Daytona client
    daytona = Daytona(config)

    # Create the Sandbox instance
    sandbox = daytona.create()
    ```

  
    ```typescript
    // Import the Daytona SDK
    import { Daytona } from '@daytonaio/sdk';

    // Initialize the Daytona client
    const daytona = new Daytona({ apiKey: 'YOUR_API_KEY' }); // Replace with your API key

    // Create the Sandbox instance
    const sandbox = await daytona.create({
      language: 'typescript',
    });
    ```


    Create a file named: `main.rb`

    ```ruby
    require 'daytona'

    # Initialize the Daytona client
    config = Daytona::Config.new(api_key: 'your-api-key')
    daytona = Daytona::Daytona.new(config)

    # Create the Sandbox instance
    sandbox = daytona.create

    # Run the code securely inside the Sandbox
    response = sandbox.process.code_run(code: 'print("Hello World from code!")')
    if response.exit_code != 0
      puts "Error: #{response.exit_code} #{response.result}"
    else
      puts response.result
    end

    # Clean up
    daytona.delete(sandbox)
    ```

## Write code

Create a program that runs code inside a Daytona Sandbox. The following snippet is an example "Hello World" program that runs securely inside a Daytona Sandbox.


`main.py`

```python
# Import the Daytona SDK
from daytona import Daytona, DaytonaConfig

# Define the configuration
config = DaytonaConfig(api_key="YOUR_API_KEY") # Replace with your API key

# Initialize the Daytona client
daytona = Daytona(config)

# Create the Sandbox instance
sandbox = daytona.create()

# Run the code securely inside the Sandbox
response = sandbox.process.code_run('print("Hello World")')

# Check the response
if response.exit_code != 0:
  print(f"Error: {response.exit_code} {response.result}")
else:
  print(response.result)

# Clean up
sandbox.delete()
```



`index.mts`

```typescript
// Import the Daytona SDK
import { Daytona } from '@daytonaio/sdk'

// Initialize the Daytona client
const daytona = new Daytona({ apiKey: 'YOUR_API_KEY' }) // Replace with your API key

// Create the Sandbox instance
const sandbox = await daytona.create({
  language: 'typescript',
})

// Run the code securely inside the Sandbox
const response = await sandbox.process.codeRun('console.log("Hello World")')

// Check the response
if (response.exitCode !== 0) {
  console.error(`Error: ${response.exitCode} ${response.result}`)
} else {
  console.log(response.result)
}

// Clean up
await sandbox.delete()
```



`main.rb`

```ruby
require 'daytona'

# Initialize the Daytona client
config = Daytona::Config.new(api_key: 'your-api-key')
daytona = Daytona::Daytona.new(config)

# Create the Sandbox instance
sandbox = daytona.create

# Run the code securely inside the Sandbox
response = sandbox.process.code_run(code: 'print("Hello World")')
```


## Run code

Run the program to execute your code in a secure and isolated Daytona Sandbox environment.


```bash
python main.py
```



```bash
npx tsx index.mts
```


```text
Hello World
```


## Summary

By following the steps above, you successfully create a Daytona account, obtain an API key, install the SDK, create a sandbox, write code, and run it securely in a Daytona Sandbox.

:::tip
For faster development with AI agents and assistants, use our LLMs context files. Copy the [llms-full.txt](https://www.daytona.io/docs/llms-full.txt.md) and [llms.txt](https://www.daytona.io/docs/llms.txt.md) files and include them in your projects or chat contexts.
:::

<ExploreMore />