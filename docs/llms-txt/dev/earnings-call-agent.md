# Source: https://dev.writer.com/no-code/earnings-call-agent.md

# Create an earnings call agent

This agent takes information from an earnings call transcript and puts it together in a summary report. The report covers results for the period, future plans, and management opinions. It uses [Palmyra Financial](/home/models#palmyra-fin), a Writer model specifically trained for financial analysis with a large context window to handle the length of earnings call transcripts.

<img src="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/earnings-agent.png?fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=7aeb92264f6596690ab927f114d096cb" alt="Earnings call agent" data-og-width="3814" width="3814" data-og-height="1748" height="1748" data-path="images/no-code/earnings-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/earnings-agent.png?w=280&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=4fae7b7e59d2a3ddaeb0ab25bd6ceef7 280w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/earnings-agent.png?w=560&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=4c6441615e6a65cbcd32e935eb77c263 560w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/earnings-agent.png?w=840&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=77cb6da1490f14fdcba5ea9b5b678bf3 840w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/earnings-agent.png?w=1100&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=cf77485f68175be032c6470dbc198d4d 1100w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/earnings-agent.png?w=1650&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=ae733f54060f64409b4df8e4ac704490 1650w, https://mintcdn.com/writer/EtzIGhya5-RmdX2Q/images/no-code/earnings-agent.png?w=2500&fit=max&auto=format&n=EtzIGhya5-RmdX2Q&q=85&s=3d17694b40d2d54e221f8286529d01e2 2500w" />

Below are the steps to create this earnings call agent. To follow along, first log in to [AI Studio](https://app.writer.com/aistudio).

<Steps>
  <Step title="Create a new agent with text generation capabilities">
    From the [AI Studio home page](https://app.writer.com/aistudio), click **Build an agent** in the top right corner. Then, select **Text generation** as the type of agent you want to create.
  </Step>

  <Step title="Define your inputs">
    This agent requires the earnings call transcript as input.

    Define one input of type **File upload** with the name: **Earnings Call Transcript**. You can specify whether to allow the user to add a URL, upload a file, or paste text. You can also specify the file type to be uploaded.

    *Optional: You could also add text inputs for company name and reporting period if you want those to be dynamic.*
  </Step>

  <Step title="Add the quarterly results prompt">
    This agent uses multiple prompts to break down the task: one for summarizing results, one for forward-looking guidance, and one for management commentary.

    Add a prompt of type with the name **Quarterly Results** and select **Palmyra Financial** as the model.

    Add the following prompt:

    ```
    You are a financial analyst who excels at producing summaries of financial reports.

    Here is your report to analyze:

    <report>@File input</report>

    Instructions:

    - Analyze the dates given in the report to determine what timeframe the report is for
    - Financial reports are often produced on a quarterly basis.
    - Extract key business result here for the quarter the earnings call is for
    - These highlights should be all about the numbers
    - You must pull out as many of these as you can find in the earnings call.
    - You must pull out a minimum of 5 results, but you should write more if there are more key results to share.
    - Copy the most relevant portion of the earnings call for each result you find here. Each result should have a supporting extract copied from the document. Do not modify the extract, just copy it exactly as it appears in the earnings call.
    - Output as HTML instead of Markdown

    Output:
    ```
  </Step>

  <Step title="Add the future guidance prompt">
    Add a prompt of type with the name **Future Guidance** and select **Palmyra Financial** as the model.

    Add the following prompt:

    ```
    You are a financial analyst who excels at producing summaries of financial reports.

    Here is your report to analyze:

    <report>@File input</report>

    Instructions:

    - If this report contains information about future quarters:
    - Extract as many statistics from the future quarter guidance as you can
    - There should be at least 5 of these statistics
    - Remember to focus on the numbers
    - Output as HTML, not Markdown

    Output:
    ```
  </Step>

  <Step title="Add the management commentary prompt">
    Add a prompt of type with the name **Management Commentary** and select **Palmyra Financial** as the model.

    Add the following prompt:

    ```
    You are a financial analyst who excels at producing summaries of financial reports. The management of the company the earnings call is for will cover a variety of themes during the earnings call. 

    Here is your report to analyze:

    <report>@File input</report>

    Instructions:

    - Pull out a list of at least 5 themes
    - Each theme should have a longer quote from the report that covers what the management of the company has to say about it. These can be quite lengthy and should give detail about the selected theme. Include a quote to go with each theme.
    - Output as HTML, not Markdown

    Output:
    ```
  </Step>

  <Step title="Add the participants prompt">
    Add a prompt of type with the name **Participants** and select **Palmyra Financial** as the model.

    Add the following prompt:

    ```
    You are a financial analyst who excels at producing summaries of financial reports. Your specific goal is to extract any and all participants from financial call transcripts or reports. Include any names and titles of participants.

    Here is your report to analyze:

    <report>@File input</report>

    Instructions:

    - Pull out all participants from the report
    - Include all participants as a bulleted list
    - If included, share the title/job name of each participant
    - Output as HTML, not Markdown

    Output:
    ```
  </Step>

  <Step title="Format your output">
    Add the following to the **Output formatting** section:

    ```
    <h3>Participants:</h3>
    @Participants
    <h3>Quarterly Report:</h3>
    @Quarterly Results
    <h3>Future Guidance:</h3>
    @Future Guidance
    <h3>Management Commentary:</h3>
    @Management
    ```
  </Step>

  <Step title="Test and refine your output">
    Review the generated summary. If it's not capturing the right information or the tone is off, tweak your prompts. Consider adding more specific instructions or examples to guide the model.
  </Step>

  <Step title="Deploy your agent">
    Once you're happy with the summary quality, [deploy your agent](/no-code/deploying-an-agent) so others can use it. Developers can also [invoke this agent with the API](/home/applications) and [use it with tool calling](/home/applications-tool-calling) to integrate into other agentic workflows.
  </Step>
</Steps>
