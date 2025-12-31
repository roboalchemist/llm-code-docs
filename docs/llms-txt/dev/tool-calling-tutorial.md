# Source: https://dev.writer.com/agent-builder/tool-calling-tutorial.md

# Tool calling with external APIs

This tutorial walks through building an agent that can intelligently call external APIs to get information and make decisions based on the information. It takes the name of a city and calls several tools and APIs to determine if it's a good day to view the sunset in that location.

If you are unfamiliar with tool calling, you might want to read the [Tool calling introduction](/agent-builder/tool-calling-intro) first to get a sense of how it works.

<CardGroup>
  <Card title="Interface">
        <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d4aef7ac42aeb83f5a8501d8065cc9ee" alt="A preview of the agent interface showing a text input for city name and a submit button" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/agent-builder/tool-calling-tutorial/tool-calling-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7cc9251ddb35c40a0131b6fca0331388 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=5bf61dc17868f5f73996258637bf17d5 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=37ac613ac58c6859ebc8451489477d1f 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e4f0db2710fc8da9b495437b3f889f4e 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=257db0db9eee59ef973dd0f0056d1aed 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c6926cfe9e7ba57207dc05c8cac3f010 2500w" />
  </Card>

  <Card title="Blueprint">
        <img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7ea6f52ba3f6a26cdb0fcff07d5404bc" alt="The complete blueprint showing the workflow with API calls and logic blocks" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b10a295f72b8dd93317d5acbbb706676 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=9f76f0636739ea24946c677e10ba4749 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3a978254b56e8cdc7b2b910b0d0e6129 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=febffef411dac0c2183cd7120c0348d5 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=129b749f513561cd0c8ede4e6b26f15a 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=56501e8b880f4137459e7ff00fd03c7b 2500w" />
  </Card>
</CardGroup>

While this tutorial uses free public APIs to demonstrate tool calling fundamentals, the tool calling patterns are applicable to real-world enterprise scenarios. You can use these same techniques to connect agents with your CRM, databases, internal APIs, and other business systems.

## Agent overview

This agent connects with two free, publicly available APIs:

* [Open-meteo](https://open-meteo.com/en/docs) for weather information
* [Sunrise sunset](https://sunrise-sunset.org/api) for sunrise and sunset times

The agent uses tool calling to get the weather information and sunrise and sunset times in a particular city. It then uses the information to determine if it's a good day to view the sunset, and if so, suggests places to view it.

## Clear the demo agent

Before you start building, clear the demo agent that comes with every new Agent Builder project.

See instructions for [clearing the demo agent in the Agent Builder Quickstart](/agent-builder/quickstart#clear-the-demo-agent).

## Build the UI

The agent has a plain UI with a text input for the city, a button to submit the request, a message block to display a loading message, and a text block to display the results.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-ui.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=959565e556fdfe8f91af1f6703fc0986" alt="" data-og-width="3454" width="3454" data-og-height="1796" height="1796" data-path="images/agent-builder/tool-calling-tutorial/tool-calling-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-ui.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=2f4aec32977e896fec079c0b1bd995d9 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-ui.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=dfeb57d775697d191442218990d7548a 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-ui.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=52affffdb4feb39468f0f274aafd16d1 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-ui.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d4c9dd0f519a6812880314a20de3e9fe 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-ui.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c3759ab2c9236d8f7d4b71c7d0c8a982 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-ui.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=9ccd5686fb4efe5efb74730ab303608b 2500w" />

<Steps>
  <Step title="Add a text input">
    Drag a **Text Input** block to the canvas. In the block's configuration menu, update the following:

    * **Label**: `City`
    * **Link variable** under **Binding**: `city`

    This updates the label in the UI to `City` and binds whatever the user types in the text input to the `city` state variable.
  </Step>

  <Step title="Add a button to submit the request">
    Drag a **Button** block to the canvas. In the block's configuration menu, update the following:

    * **Label**: `Submit`
  </Step>

  <Step title="Add a message block to display a loading message">
    Drag a **Message** block to the canvas. In the block's configuration menu, update the following:

    * **Message**: `@{status}`

    This displays the `status` state variable in the UI if it's set. If there's no status, the block isn't visible.
  </Step>

  <Step title="Add a text area to display the result">
    Drag a **Text** block to the canvas. In the block's configuration menu, update the following:

    * **Text**: `@{final_result}`

    This displays the `final_result` state variable in the UI if it's set. If there's no `final_result`, the block isn't visible.
  </Step>
</Steps>

## Build the blueprint

The logic of the blueprint is as follows:

1. The UI Trigger block triggers the agent when the user clicks the button.
2. The set state block adds a loading status to the UI.
3. The tool calling block calls the available tools to get the current date and time, the weather information, and sunrise and sunset times. From the provided information, it makes a determination about whether it's a good day to view the sunset.
4. Once the tool calling block completes, the agent updates the state with the results and clears the loading message.

<Note>
  Tool calling is a powerful feature that combines the model's knowledge with real-time data and external APIs. The model can make intelligent decisions by analyzing the data it receives and drawing on its own knowledge to interpret results. For example, you don't need to manually parse timestamps or format weather data when you get a response from an API. You can provide the raw API responses and the model extracts and uses the relevant information appropriately.
</Note>

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7ea6f52ba3f6a26cdb0fcff07d5404bc" alt="" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b10a295f72b8dd93317d5acbbb706676 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=9f76f0636739ea24946c677e10ba4749 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3a978254b56e8cdc7b2b910b0d0e6129 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=febffef411dac0c2183cd7120c0348d5 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=129b749f513561cd0c8ede4e6b26f15a 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=56501e8b880f4137459e7ff00fd03c7b 2500w" />

<Steps>
  <Step title="Add a UI Trigger block">
    Drag a **UI Trigger** block to the canvas. In the block's configuration menu, update the following:

    * **Component Id**: Select the **Submit** button from the dropdown of available components.
    * **Trigger**: `wf-click`

    This triggers the blueprint when the user clicks the Submit button.
  </Step>

  <Step title="Add a set state block to add a loading status to the UI">
    Drag a **Set State** block to the canvas. In the block's configuration menu, update the following:

    * **Link variable**: `status`
    * **Value**: `%Loading...`

    This sets the `status` state variable to `Loading...` with an animated spinner when the blueprint starts.
  </Step>

  <Step title="Add a tool calling block and set the prompt">
    Drag a **Tool Calling** block to the canvas. In the block's configuration menu, update the following:

    * **Prompt**:

    ```
    You are a travel assistant helping someone in @{city} find optimal sunset viewing opportunities.

    ## Available Tools
    - `get_weather` - Get weather conditions for today
    - `get_time` - Get current time as a UTC timestamp
    - `get_sunset_time` - Get sunrise/sunset times in UTC

    ## Decision Logic
    1. **Check timing**: Use `get_time` and `get_sunset_time` to compare current time with today's sunset
       - **CRITICAL**: Both times are returned in UTC. You MUST convert both to @{city}'s local timezone before comparing
       - **Time comparison steps**:
         a. Get current UTC time using `get_time`
         b. Get sunset UTC time using `get_sunset_time`
         c. Convert BOTH times to @{city}'s local timezone
         d. Compare the local times using 24-hour format
       - **If local current time > local sunset time**: Sunset has passed
       - **If local current time < local sunset time**: Sunset is upcoming
       - **Example**: If current UTC is 23:30 and sunset UTC is 22:45, convert both to local time first. If local current time is 19:30 and local sunset is 18:45, then sunset has passed.

    2. **Assess weather conditions**: Use `get_weather` to evaluate:
       - Temperature (comfort for outdoor viewing)
       - Cloud coverage (visibility of sun)
       - Wind speed (viewing comfort)
       - Precipitation chance (weather suitability)

    3. **Make recommendation**: If conditions are favorable, suggest 3 outdoor viewing locations in @{city}

    ## Tool Usage Notes
    - Both `get_weather` and `get_sunset_time` require latitude/longitude coordinates for @{city}
    - Use your knowledge to provide accurate coordinates
    - Remember to account for @{city}'s timezone when interpreting UTC timestamps

    ## Required Output Format
    Provide a structured response including:
    - **If sunset has passed**: Begin by stating "Sunset has already passed for today in @{city}" with the prompt to ask again tomorrow closer to sunset. Otherwise, ignore this section.
    - Current date/time in @{city}'s local timezone, in a user-friendly format
    - Sunset time in @{city}'s local timezone
    - Weather factor analysis with "Good" or "Bad" rating and the values for each factor:
      - Temperature
      - Cloud coverage  
      - Wind speed
      - Precipitation chance
    - Overall viewing recommendation
    - If favorable: 3 recommended locations with brief explanations

    ## Important Reminder
    Always convert UTC timestamps to the local timezone of @{city} before making any time comparisons. Never compare UTC times directly without conversion.
    ```

    This prompt instructs the agent to use the available tools to get the weather information and sunrise and sunset times. It then makes a determination about whether it's a good day to view the sunset. In the next steps, you'll define the tools and add the logic to call them.

    <Tip>
      While AI models are highly intelligent and can reason about complex tasks, a well-structured prompt is essential for effective tool calling. The prompt serves as a blueprint that clearly defines what tools are available, guides the model through the decision-making workflow, and specifies the expected output format. Without this guidance, the model might miss important steps, use tools inefficiently, or produce results that don't match your requirements. A detailed prompt ensures consistent, reliable performance across different inputs and scenarios. See [Prompting strategies](/home/prompting) for more suggestions about writing prompts.
    </Tip>
  </Step>

  <Step title="Define a tool to get the current date and time">
    Within the **Tool calling** block, click **Add tool+** to define a new tool for the agent to use. Define the tool as follows:

    * **Tool type**: `function`
    * **Tool name**: `get_time`
    * **Function tool definition**:

    ```json  theme={null}
    {
      "description": "Gets the current time as a UTC timestamp",
      "parameters": {},
      "type": "function"
    }
    ```

    This defines a tool that the agent can use to get the current date and time in UTC. It doesn't require any parameters, so the parameters field is empty. The description field provides a brief description of what the tool does.
  </Step>

  <Step title="Add a Python block to provide the current date and time in UTC">
    This example uses a Python block to get the current date and time in UTC using Python's `datetime` library.

    Drag a **Python** block to the canvas. In the block's configuration menu, update the following:

    * **Code**:

    ```python  theme={null}
    from datetime import datetime, timezone

    utc_datetime = datetime.now(timezone.utc)
    set_output(utc_datetime)
    ```

    <Warning>
      To return a value from a Python block, you must use the `set_output` function.
    </Warning>

    This returns the current date and time in UTC.
  </Step>

  <Step title="Add a return value block to return the date and time to the tool calling block">
    If you want a tool to return a value to the Tool Calling block, you need to add a **Return Value** block at the end of the tool's logic.

    Drag a **Return Value** block to the canvas. In the block's configuration menu, update the following:

    * **Value**: `@{result}`

    This returns the result of the Python block to the Tool Calling block.
  </Step>

  <Step title="Define a tool to get the weather information">
    Within the **Tool calling** block, click **Add tool+** to define a new tool for the agent to use. Define the tool as follows:

    * **Tool type**: `function`
    * **Tool name**: `get_weather`
    * **Function tool definition**:

    ```json  theme={null}
    {
      "description": "Gets information about the weather for day. This includes cloud coverage, precipitation change, wind gusts, and temperature. The return value is a series of arrays for each of those variables, with one value for each hour. The arrays all start at GMT+0 for the first time.",
      "parameters": {
        "lat": {
          "type": "string",
          "description": "The latitude to request weather data for"
        },
        "long": {
          "type": "string",
          "description": "The longitude to request weather data for"
        }
      },
      "type": "function"
    }
    ```

    This defines a tool that the agent can use to get the weather information for a given latitude and longitude. It instructs the agent to provide the latitude and longitude in the parameters, because the API requires latitude and longitude.
  </Step>

  <Step title="Add an HTTP Request block to call the Open-meteo API">
    Now you need to add a block to call the Open-meteo API.

    Drag an **HTTP Request** block to the canvas. In the block's configuration menu, update the following:

    * **URL**: `https://api.open-meteo.com/v1/forecast?latitude=@{lat}&longitude=@{long}&hourly=temperature_2m,cloud_cover,precipitation_probability,precipitation,wind_speed_10m&forecast_days=1`

    This is the URL for the Open-meteo API. It includes the `@{lat}` and `@{long}` variables, which you defined as required parameters in the tool definition. The agent provides the latitude and longitude when it calls the tool.

    For more information about the Open-meteo API and the request this is making, see the [Open-meteo documentation](https://open-meteo.com/en/docs).
  </Step>

  <Step title="Add a return value block to return the weather information to the tool calling block">
    The HTTP Request block returns the weather information in JSON format. You need to add a **Return Value** block to return the weather information to the Tool Calling block.

    Drag a **Return Value** block to the canvas. In the block's configuration menu, update the following:

    * **Value**: `@{result}`

    This returns the result of the HTTP Request block to the Tool Calling block. The agent will be able to parse and use the JSON data that the HTTP Request block returns.
  </Step>

  <Step title="Define a tool to get the sunrise and sunset times">
    Within the **Tool calling** block, click **Add tool+** to define a new tool for the agent to use. Define the tool as follows:

    * **Tool type**: `function`
    * **Tool name**: `get_sunset_time`
    * **Function tool definition**:

    ```json  theme={null}
    {
      "description": "Gets info for about the sunset and sunrise times at a given location based on latitude and longitude",
      "parameters": {
        "lat": {
          "type": "string",
          "description": "The latitude to request weather data for"
        },
        "long": {
          "type": "string",
          "description": "The longitude to request weather data for"
        }
      },
      "type": "function"
    }
    ```

    This defines a tool that the agent can use to get the sunrise and sunset times for a given latitude and longitude. It instructs the agent to provide the latitude and longitude in the parameters, because the API requires latitude and longitude.
  </Step>

  <Step title="Add an HTTP Request block to call the Sunrise Sunset API">
    Now you need to add a block to call the Sunrise Sunset API.

    Drag an **HTTP Request** block to the canvas. In the block's configuration menu, update the following:

    * **URL**: `https://api.sunrise-sunset.org/json?lat=@{lat}&lng=@{long}&tzid=UTC&date=today`

    This is the URL for the Sunrise Sunset API. It includes the `@{lat}` and `@{long}` variables, which you defined as required parameters in the tool definition. The agent provides the latitude and longitude when it calls the tool.

    For more information about the Sunrise Sunset API and the request this is making, see the [Sunrise Sunset documentation](https://sunrise-sunset.org/api).
  </Step>

  <Step title="Add a return value block to return the sunrise and sunset times to the tool calling block">
    The HTTP Request block returns the sunrise and sunset times in JSON format. You need to add a **Return Value** block to return the sunrise and sunset times to the Tool Calling block.

    Drag a **Return Value** block to the canvas. In the block's configuration menu, update the following:

    * **Value**: `@{result}`

    This returns the result of the HTTP Request block to the Tool Calling block. The agent will be able to parse and use the JSON data that the HTTP Request block returns.
  </Step>

  <Step title="Add a set state block to display the results">
    Now that you've defined the tools for the Tool Calling block and added the logic to call them, the agent can take the prompt and provided tools and make a determination about whether it's a good day to view the sunset.

    Once the Tool Calling block completes, the agent should display the final results in the UI. You can display the final results in the UI by setting the `final_result` state variable, which will be displayed in the UI's **Text** block.

    Drag a **Set State** block to the canvas. In the block's configuration menu, update the following:

    * **Link variable**: `final_result`
    * **Value**: `%@{result}`

    This sets the `final_result` state variable to the result of the Tool Calling block.
  </Step>

  <Step title="Add a set state block to clear the loading message">
    Finally, you need to add a block to clear the loading message when the Tool Calling block completes.

    Drag a **Set State** block to the canvas. In the block's configuration menu, update the following:

    * **Link variable**: `status`
    * **Value**: Leave empty to clear the state variable

    This clears the `status` state variable when the Tool Calling block completes.
  </Step>
</Steps>

## Preview the agent

Navigate to the **Preview** tab to test the agent.

Enter a city and click the Submit button to see the agent's response. You should first see the loading message, then the final results when the Tool Calling block completes.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d4aef7ac42aeb83f5a8501d8065cc9ee" alt="" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/agent-builder/tool-calling-tutorial/tool-calling-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7cc9251ddb35c40a0131b6fca0331388 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=5bf61dc17868f5f73996258637bf17d5 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=37ac613ac58c6859ebc8451489477d1f 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e4f0db2710fc8da9b495437b3f889f4e 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=257db0db9eee59ef973dd0f0056d1aed 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-preview.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c6926cfe9e7ba57207dc05c8cac3f010 2500w" />

You can see the agent's progress and reasoning in the **Logs** tab.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-logs.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=a6f12de967657cfc738471010cf7c710" alt="" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/tool-calling-tutorial/tool-calling-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-logs.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=ca60c4a4bd2fd000b23f4c82fa85328d 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-logs.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=10febde56bfe881b8ccdbe9fd37c3bd4 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-logs.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c39dfe65a80e39fc06c2ce75821bc6f0 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-logs.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=8f00c215e34035dc060e481778ab560f 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-logs.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=dadb32ae98ac0ad47d52cc3186e63442 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-logs.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=18a300324f4a309fee3fab0a1730feb7 2500w" />

## Next steps

This tutorial demonstrates the basics of tool calling with external APIs. To continue improving on this agent, you might consider adding a **Structured Output** block after the Tool Calling block to ensure the agent returns the results in the correct format. You could also add more components to the UI to display the results in a more user-friendly way, such as a [**Metric**](/components/metric) block to display the weather conditions, a [**Google Maps**](/components/googlemaps) block to display the recommended locations, or different **Text** blocks to display the different sections of the results.

Next, you might want to learn more about tool calling:

* [Learn more about tool calling](/agent-builder/tool-calling)
* [Learn more about the Tool Calling block](/blueprints/toolcalling)
* [Learn more about the HTTP Request block](/blueprints/httprequest)

<feedback />
