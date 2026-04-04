# Source: https://exa.ai/docs/integrations/agentops.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exa

Use Exa's semantic search and contents endpoints to give your agents access to up-to-date, relevant information on the web.

***

<Steps>
  <Step title="Install the AgentOps SDK">
    ```bash  theme={null}
    pip install agentops
    ```
  </Step>

  <Step title="Install the Exa SDK">
    ```bash  theme={null}
    pip install exa_py
    ```
  </Step>

  <Step title="Set Up Environment Variables">
    Create a `.env` file to store your API keys:

    ```env  theme={null}
    AGENTOPS_API_KEY=your_agentops_api_key_here
    EXA_API_KEY=your_exa_api_key_here
    ```
  </Step>

  <Step title="Initialize the Clients">
    Set up both AgentOps and Exa in your code:

    ```python  theme={null}
    import agentops
    from exa_py import Exa
    from dotenv import load_dotenv
    import os

    # Load environment variables
    load_dotenv()

    # Initialize AgentOps
    agentops.init(os.getenv('AGENTOPS_API_KEY'))

    # Initialize Exa client
    exa = Exa(api_key=os.getenv('EXA_API_KEY'))
    ```
  </Step>

  <Step title="Create Your Search Tool">
    Create a tool that uses Exa's search capabilities:

    ```python  theme={null}
    from crewai_tools import tool
    from exa_py import Exa
    from dotenv import load_dotenv
    import os

    # Load environment variables
    load_dotenv()

    @tool("Exa search and get contents")
    def search_and_contents(question: str) -> str:
        """
        Args: The search query or question to find information about
        Returns: Formatted string containing titles, URLs, and highlights from the search results
        """
        exa = Exa(api_key=os.getenv('EXA_API_KEY'))

        response = exa.search_and_contents(
            query,
            type="auto",
            num_results=10,
            highlights=True
        )

        parsedResult = ''.join([
            f'<Title id={idx}>{eachResult.title}</Title>'
            f'<URL id={idx}>{eachResult.url}</URL>'
            f'<Highlight id={idx}>{"".join(eachResult.highlights)}</Highlight>' 
            for (idx, eachResult) in enumerate(response.results)
        ])

        return parsedResult
    ```
  </Step>
</Steps>

## Full Example

```python  theme={null}
import agentops
from crewai_tools import tool
from exa_py import Exa
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

agentops.init(os.getenv('AGENTOPS_API_KEY'))

@tool("Exa search and get contents")
def search_and_contents(question: str) -> str:
    """
    Tool using Exa's Python SDK to run semantic search and return result highlights.
    """
    exa = Exa(api_key=os.getenv('EXA_API_KEY'))

    response = exa.search_and_contents(
        query,
        type="auto",
        num_results=3,
        highlights=True
    )

    parsedResult = ''.join([
        f'<Title id={idx}>{eachResult.title}</Title>'
        f'<URL id={idx}>{eachResult.url}</URL>'
        f'<Highlight id={idx}>{"".join(eachResult.highlights)}</Highlight>' 
        for (idx, eachResult) in enumerate(response.results)
    ])

    return parsedResult

# Example usage
results = search_and_contents("Latest advancements in AI")
print(results)

agentops.end_session('Success')
```
