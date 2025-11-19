# Source: https://www.daytona.io/docs/en/python-sdk.md

The Daytona Python SDK provides a robust interface for programmatically interacting with Daytona Sandboxes.

## Installation

Install the Daytona Python SDK using pip:

```bash
pip install daytona
```

Or using poetry:

```bash
poetry add daytona
```

## Getting Started

Here's a simple example to help you get started with the Daytona Python SDK:

    ```python
    from daytona import Daytona

    def main():
        # Initialize the SDK (uses environment variables by default)
        daytona = Daytona()

        # Create a new sandbox
        sandbox = daytona.create()

        # Execute a command
        response = sandbox.process.exec("echo 'Hello, World!'")
        print(response.result)

    if __name__ == "__main__":
        main()
    ```

    ```python
    import asyncio
    from daytona import AsyncDaytona

    async def main():
        # Initialize the SDK (uses environment variables by default)
        async with AsyncDaytona() as daytona:
            # Create a new sandbox
            sandbox = await daytona.create()

            # Execute a command
            response = await sandbox.process.exec("echo 'Hello, World!'")
            print(response.result)

    if __name__ == "__main__":
        asyncio.run(main())
    ```

## Configuration

The SDK can be configured using environment variables or by passing options to the constructor:

    ```python
    from daytona import Daytona, DaytonaConfig

    # Using environment variables (DAYTONA_API_KEY, DAYTONA_API_URL, DAYTONA_TARGET)
    daytona = Daytona()

    # Using explicit configuration
    config = DaytonaConfig(
        api_key="your-api-key",
        api_url="https://app.daytona.io/api",
        target="us"
    )
    daytona = Daytona(config)
    ```

    ```python
    import asyncio
    from daytona import AsyncDaytona, DaytonaConfig

    async def main():
        try:
            # Using environment variables (DAYTONA_API_KEY, DAYTONA_API_URL, DAYTONA_TARGET)
            daytona = AsyncDaytona()
            # Your async code here
            pass
        finally:
            await daytona.close()

        # Using explicit configuration
        config = DaytonaConfig(
            api_key="your-api-key",
            api_url="https://app.daytona.io/api",
            target="us"
        )
        async with AsyncDaytona(config) as daytona:
            # Your code here
            pass

    if __name__ == "__main__":
        asyncio.run(main())
    ```