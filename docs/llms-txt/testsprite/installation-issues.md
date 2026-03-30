# Source: https://docs.testsprite.com/mcp/troubleshooting/installation-issues.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.testsprite.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation Issues

> Solutions to common installation problems with TestSprite MCP Server.

## Command Not Found

If you experience issues about **`npx @testsprite/testsprite-mcp@latest` command not found**. Please follow the solution below:

<Steps>
  <Step title="Check if Node.js and npm are installed">
    ```bash  theme={null}
    node --version
    npm --version
    ```

    If Node.js is not installed, install it first:

    <Tabs>
      <Tab title="Homebrew (macOS)">
        ```bash  theme={null}
        brew install node
        ```
      </Tab>

      <Tab title="Direct Download">
        Download from [Node.js Official Site <Icon icon="arrow-up-right-from-square" size={12} />](https://nodejs.org/)
      </Tab>
    </Tabs>
  </Step>

  <Step title="Check if npx is available">
    ```bash  theme={null}
    npx --version
    ```

    If npx is not found (should come with npm 5.2+), update npm:

    ```bash  theme={null}
    npm install -g npm@latest
    ```
  </Step>

  <Step title="Try alternative installation methods">
    <Tabs>
      <Tab title="Direct package installation">
        ```bash  theme={null}
        npm install -g @testsprite/mcp-server
        testsprite-mcp --version
        ```
      </Tab>

      <Tab title="Use npm exec (npm 7+)">
        ```bash  theme={null}
        npm exec @testsprite/testsprite-mcp@latest
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Clear npm cache if packages aren't found">
    ```bash  theme={null}
    npm cache clean --force
    ```

    After cache cleaned, verify npx can find the package

    ```bash  theme={null}
    npx --version
    npx @testsprite/testsprite-mcp@latest --help
    ```
  </Step>

  <Step title="Check npm registry connectivity">
    ```bash  theme={null}
    npm ping
    npm config get registry
    ```
  </Step>
</Steps>

## Permission Errors

If you experience issues about **Permission denied when installing `@testsprite/testsprite-mcp` globally**. Please follow the solution below:

<Steps>
  <Step title="Choose your preferred solution method">
    <Tabs>
      <Tab title="Fix npm permissions (Recommended)">
        1. **Setup npm permissions**

        ```bash  theme={null}
        mkdir ~/.npm-global
        npm config set prefix '~/.npm-global'
        echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zshrc  # or ~/.bashrc for bash
        source ~/.zshrc  # or source ~/.bashrc
        ```

        2. **Install Latest Version**

        ```bash  theme={null}
        npm install -g @testsprite/testsprite-mcp@latest
        ```

        3. **Verify Installation**

        ```bash  theme={null}
        testsprite-mcp --version
        ```
      </Tab>

      <Tab title="Use npx (Alternative)">
        This automatically uses the latest version without permission issues:

        ```bash  theme={null}
        npx @testsprite/testsprite-mcp@latest --version
        ```
      </Tab>

      <Tab title="Install using sudo">
        <Warning>Not recommended due to security risks</Warning>

        ```bash  theme={null}
        sudo npm install -g @testsprite/testsprite-mcp@latest
        ```
      </Tab>

      <Tab title="Use Node Version Manager (nvm)">
        Install nvm for clean permissions:

        ```bash  theme={null}
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
        nvm install node  # Installs latest Node.js with proper permissions
        npm install -g @testsprite/testsprite-mcp@latest
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Troubleshooting permission issues on macOS">
    If you still get permission errors, check npm ownership:

    ```bash  theme={null}
    sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
    ```
  </Step>

  <Step title="For fresh npm setup on macOS">
    ```bash  theme={null}
    sudo chown -R $(whoami) /usr/local/lib/node_modules
    sudo chown -R $(whoami) /usr/local/bin
    ```
  </Step>
</Steps>

## Node.js Version Compatibility

If you experience issues about **TestSprite MCP Server requires Node.js 22+**. Please follow the solution below:

<Note>Node.js 22 is required for optimal compatibility with TestSprite MCP Server features and dependencies.</Note>

<Steps>
  <Step title="Check current version">
    ```bash  theme={null}
    node --version
    ```

    If version is below 22, **upgrade Node.js**

    <Tabs>
      <Tab title="nvm (Recommended)">
        ```bash  theme={null}
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
        source ~/.zshrc  # or source ~/.bashrc
        nvm install 22
        nvm use 22
        nvm alias default 22  
        node --version
        ```

        After upgrading, verify installation:

        ```bash  theme={null}
        testsprite-mcp --version
        ```
      </Tab>

      <Tab title="Homebrew (macOS)">
        ```bash  theme={null}
        brew uninstall node  # Remove old version if needed
        brew install node@22
        brew link node@22 --force
        ```
      </Tab>

      <Tab title="Direct Download">
        Visit [Node.js Official Site <Icon icon="arrow-up-right-from-square" size={12} />](https://nodejs.org/) and download Node.js 22 LTS

        Follow the installer instructions for your operating system.
      </Tab>
    </Tabs>
  </Step>

  <Step title="Verify npm and npx are working">
    ```bash  theme={null}
    npm --version
    npx --version
    ```
  </Step>

  <Step title="Test TestSprite MCP installation">
    ```bash  theme={null}
    npx @testsprite/testsprite-mcp@latest --version
    ```
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).