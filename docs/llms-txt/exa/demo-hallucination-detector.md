# Source: https://exa.ai/docs/examples/demo-hallucination-detector.md

> **Documentation Index**
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hallucination Detector

> A live demo that detects hallucinations in content using Exa's search.

<div>
  <a href="https://demo.exa.ai/hallucination-detector" target="_blank" rel="noopener noreferrer">
    <button class="api-button">
      \> try the app
    </button>
  </a>
</div>

***

We built a live hallucination detector that uses Exa to verify LLM-generated content. When you input text, the app breaks it into individual claims, searches for evidence to verify each one, and returns relevant sources with a verification confidence score.

A claim is a single, verifiable statement that can be proven true or false - like "The Eiffel Tower is in Paris" or "It was built in 1822."

<Card title="Click here to try it out." href="https://demo.exa.ai/hallucination-detector" img="https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/Screenshot%202024-11-19%20at%203.19.48%E2%80%AFPM.png?fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=75ac7324f228fb3d0d19f18603998228" data-og-width="1832" width="1832" data-og-height="1170" height="1170" data-path="images/Screenshot 2024-11-19 at 3.19.48 PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/Screenshot%202024-11-19%20at%203.19.48%E2%80%AFPM.png?w=280&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=efd378652d3d4b95bc8ce2eeb30d2c7d 280w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/Screenshot%202024-11-19%20at%203.19.48%E2%80%AFPM.png?w=560&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=c3413cedc97f7d2d99428cbb248782da 560w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/Screenshot%202024-11-19%20at%203.19.48%E2%80%AFPM.png?w=840&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=2f854f02938ef3992bbf8a28097d50fa 840w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/Screenshot%202024-11-19%20at%203.19.48%E2%80%AFPM.png?w=1100&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=f27814fd501730881b12e9b5f98e7342 1100w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/Screenshot%202024-11-19%20at%203.19.48%E2%80%AFPM.png?w=1650&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=a6fbfa924159fbddfd541a18a8bbd6f5 1650w, https://mintcdn.com/exa-52/tmzyKnsgpKLGddKC/images/Screenshot%202024-11-19%20at%203.19.48%E2%80%AFPM.png?w=2500&fit=max&auto=format&n=tmzyKnsgpKLGddKC&q=85&s=f57f2087ea2cbb27c371c21117b25703 2500w" />

This document explains the functions behind the three steps of the fact-checker:

1. The LLM extracts verifiable claims from your text
2. Exa searches for relevant sources for each claim
3. The LLM evaluates each claim against its sources, returning whether or not its true, along with a confidence score.

<Info>See the full [step-by-step guide](/examples/identifying-hallucinations-with-exa) and [github repo](https://github.com/exa-labs/exa-hallucination-detector) if you'd like to recreate. </Info>

***

## Function breakdown

<Steps>
  <Step title="Extracting claims">
    The `extract_claims` function uses an LLM (Anthropic's, in this case) to identify distinct, verifiable statements from your inputted text, returning these claims as a JSON array of strings.

    <Warning>For simpilicity, we did not include a try/catch block in the code below. However, if you are building your own hallucination detector, you should include one that catches any errors in the LLM parsing and uses a regex method that treats each sentence (text between capital letter and end punctuation) as a claim.</Warning>

    ```python Python theme={null}
    def extract_claims(text: str) -> List[str]:
        """Extract factual claims from the text using an LLM."""
        system_message = SystemMessage(content="""
            You are an expert at extracting claims from text.
            Your task is to identify and list all claims present, true or false,
            in the given text. Each claim should be a single, verifiable statement.
            Present the claims as a JSON array of strings.
        """)
        
        human_message = HumanMessage(content=f"Extract factual claims from this text: {text}")
        response = llm.invoke([system_message, human_message])
        
        claims = json.loads(response.content)
        return claims
    ```
  </Step>

  <Step title="Searching for evidence">
    The `exa_search` function uses Exa search to find evidence for each extracted claim. For every claim, it retrieves the 5 most relevant sources, formats them with their URLs and content (`text`), passing them to the next function for verification.

    ```python Python theme={null}
    def exa_search(query: str) -> List[str]:
        """Retrieve relevant documents using Exa's semantic search."""
        search = ExaSearchRetriever(k=5, text=True)
        
        document_prompt = PromptTemplate.from_template("""
            <source>
                <url>{url}</url>
                <text>{text}</text>
            </source>
        """)
        
        parse_info = RunnableLambda(
            lambda document: {
                "url": document.metadata["url"],
                "text": document.page_content or "No text available",
            }
        )
        
        document_chain = (parse_info | document_prompt)
        search_chain = search | document_chain.map()
        documents = search_chain.invoke(query)
        
        return [str(doc) for doc in documents]
    ```
  </Step>

  <Step title="Verifying claims">
    The `verify_claim` function checks each claim against the sources from `exa_search`. It uses an LLM to determine if the sources support or refute the claim and returns a decision with a confidence score. If no sources are found, it returns "insufficient information".

    ```python Python theme={null}
    def verify_claim(claim: str, sources: List[str]) -> Dict[str, Any]:
        """Verify a single claim using combined Exa search sources."""
        if not sources:
            return {
                "claim": claim,
                "assessment": "Insufficient information",
                "confidence_score": 0.5,
                "supporting_sources": [],
                "refuting_sources": []
            }
        
        combined_sources = "\n\n".join(sources)
        
        system_message = SystemMessage(content="""
            You are an expert fact-checker.
            Given a claim and sources, determine whether the claim is supported,
            refuted, or lacks sufficient evidence.
            Provide your answer as a JSON object with assessment and confidence score.
        """)
        
        human_message = HumanMessage(content=f'Claim: "{claim}"\nSources:\n{combined_sources}')
        response = llm.invoke([system_message, human_message])
        
        return json.loads(response.content)
    ```
  </Step>
</Steps>

Using LLMs to extract claims and verify them against Exa search sources is a simple way to detect hallucinations in content. If you'd like to recreate it, the full documentation for the script is [here](/examples/identifying-hallucinations-with-exa) and the github repo is [here](https://github.com/exa-labs/exa-hallucination-detector).
