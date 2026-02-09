# Source: https://docs.avaamo.com/user-guide/debug/debug-log.md

# Source: https://docs.avaamo.com/user-guide/skills/prompt-skill/debug-log.md

# Debug Log

In case you are unable to receive the expected response from the **Prompt** skill, you can debug using the following troubleshooting tips:

### Using Debug logs <a href="#using-debug-logs" id="using-debug-logs"></a>

Use console.log to log messages at specific steps in the script. This helps to verify if the script is executing as expected and to identify points of failure. You can then use the **Debug logs** options in **Dialog skill** to display all the logs generated using console.log.

**Note**: In the `Debug logs` pop-up window, a maximum of 50 consecutive `Console.log` statements can be printed.

### Using Conversation history <a href="#using-conversation-history" id="using-conversation-history"></a>

You can check the user query from the [Conversation history](https://docs.avaamo.com/user-guide/debug/conversation-history) to view the complete flow that caused an error or unexpected response.

<br>
