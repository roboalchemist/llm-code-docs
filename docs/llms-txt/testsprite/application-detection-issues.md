# Source: https://docs.testsprite.com/mcp/troubleshooting/application-detection-issues.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.testsprite.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Application Detection Issues

> Solutions to application detection problems with TestSprite MCP Server.

## "Application not accessible" Error

If you experience issues where **TestSprite can't access your running application**, please follow the solution below:

<Steps>
  <Step title="Diagnostic checks">
    Check if application is running

    ```bash  theme={null}
    curl http://localhost:3000
    curl http://localhost:8000
    ```

    Check which ports are in use

    ```bash  theme={null}
    lsof -i :3000
    lsof -i :8000
    ```

    Check firewall settings (Linux)

    ```bash  theme={null}
    sudo ufw status
    ```

    <Info>**For macOS:** Go to System `Preferences > Security & Privacy > Firewall` to check firewall settings.</Info>
  </Step>

  <Step title="Ensure application is running">
    <Tabs>
      <Tab title="Frontend Applications">
        ```bash  theme={null}
        npm start
        npm run dev
        yarn dev
        ```
      </Tab>

      <Tab title="Backend Applications">
        ```bash  theme={null}
        npm run server
        python app.py
        node server.js
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Check port configuration">
    Find actual port

    ```bash  theme={null}
    netstat -tulpn | grep LISTEN
    ```

    Update bootstrap call

    ```bash  theme={null}
    testsprite_bootstrap_tests ({
      localPort: 3000,  // Use actual port
      type: "frontend",
      projectPath: "/path/to/project",
      testScope: "codebase"
    })
    ```
  </Step>

  <Step title="Check for port conflicts">
    Kill conflicting processes

    ```bash  theme={null}
    lsof -ti:3000 | xargs kill -9
    ```

    Use different port

    ```bash  theme={null}
    PORT=3001 npm start
    ```
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).