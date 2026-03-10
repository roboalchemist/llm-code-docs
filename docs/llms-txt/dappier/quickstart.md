# Quickstart
Source: https://docs.dappier.com/quickstart



## Introduction

<b>Developers: Build Smarter AI with Real-Time, Trusted Data from Dappier. </b>

Dappier's RAG (Retrieval-Augmented Generation) API marketplace designed to supercharge your AI applications with real-time, trusted data from the world's leading brands.

Fully LLM-agnostic and ready to integrate with any AI system. Our easy-to-integrate RAG APIs deliver up-to-date content, reducing hallucinations and enhancing the accuracy of your models without the need for retraining.

<b>
  Publishers: Monetize your content and increase engagement on your sites with
  Dappier!
</b>

Dappier provides publishers with an easy-to-use platform to syndicate their content in our marketplace for AI companies and generate revenue. You can monetize through a pay-per-query model or a revenue-sharing, ad-supported model. Get paid as your content is accessed.

Boost engagement and generate revenue with Dappier's AI-powered tools! Use our AI recommendations widget (over 40% engagement increase) or embed the Ask AI widget to provide instant answers for your users.

## Steps to get started

<Steps>
  <Step title="Get API Key">
    You first need the API key to access the Dappier API. Please visit [Dappier Platform](https://platform.dappier.com) to sign up and create an API key under Settings > Profile > API Keys.

    <img className="block" src="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_profile_api_key.png?fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=f45be031c15ce8eb4c0515e505d889f3" alt="Dappier Profile" data-og-width="1452" width="1452" data-og-height="638" height="638" data-path="images/dappier_profile_api_key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_profile_api_key.png?w=280&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=3a48456e34f3944b331ccaaa8f3f07ac 280w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_profile_api_key.png?w=560&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=be4134760695c6f32e0049798cc592a3 560w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_profile_api_key.png?w=840&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=e0cb14b386215869823fecac77090174 840w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_profile_api_key.png?w=1100&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=75211b6c260641613d2df71677555b7e 1100w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_profile_api_key.png?w=1650&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=78d3e75995de8a15045e4d69cc1ad486 1650w, https://mintcdn.com/dappier-20/GPubPuGcoHagv5PD/images/dappier_profile_api_key.png?w=2500&fit=max&auto=format&n=GPubPuGcoHagv5PD&q=85&s=dd4390b889687d26e0b4f5400871acf1 2500w" />
  </Step>

  <Step title="Pick RAG model from Marketplace">
    You can browse through different RAG models available in the [Dappier Marketplace](https://marketplace.dappier.com). You can select the RAG model that best fits your use case. Once selected get the RAG model id from the request endpoint. RAG model id starts with dm\_.
  </Step>

  <Step title="Make API call">
    The Curl request to access the RAG model is as follows:

    <CodeGroup>
      ```python Python theme={null}
      # Python code example
      import requests

      def fetch_dappier_data(query):
      api_key = "<YOUR_DAPPIER_API_KEY>" # Replace with your actual Dappier API key
      endpoint = "https://api.dappier.com/app/aimodel/am_01j06ytn18ejftedz6dyhz2b15"
      headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
      body = {"query": query}
      response = requests.post(endpoint, headers=headers, json=body)
      return response.json()

      # Example usage
      results = fetch_dappier_data("Plan me an itinerary for a 3 day trip to Puerto Rico")
      print(results)
      ```

      ```bash cURL theme={null}
          curl -L 'https://api.dappier.com/app/aimodel/am_01j06ytn18ejftedz6dyhz2b15'
          -H 'Content-Type: application/json'
          -H 'Authorization: Bearer <YOUR_DAPPIER_API_KEY>'
              -d "{
                  \"query\": \"Plan me an itinerary for a 3 day trip to Puerto Rico\"
              }"
      ```
    </CodeGroup>
  </Step>
</Steps>

## Features

<CardGroup cols={2}>
  <Card title="API" icon="code" href="api-reference/endpoint/real-time-search">
    Access powerful APIs to integrate Dappier’s real-time data into your
    applications seamlessly.
  </Card>

  <Card title="Integrations" icon="link" href="/integrations/introduction-integration">
    Connect with third-party platforms effortlessly using our built-in
    integration tools.
  </Card>

  <Card title="Real time Data" icon="globe" href="api-reference/endpoint/real-time-search">
    Get real-time access to trusted data sources for enhanced AI-driven
    insights.
  </Card>

  <Card title="AI Recommendations" icon="thumbs-up" href="api-reference/endpoint/ai-recommendations">
    Use AI-powered recommendations to personalize experiences for your
    users.
  </Card>

  <Card title="RAG Marketplace" icon="comments-dollar" href="/rag-marketplace">
    Browse and access high-quality RAG models in our RAG Marketplace, or
    deploy and monetize your own RAG models.
  </Card>

  <Card title="Embed Chatbot" icon="comment-dots" href="embed-widgets">
    Build and deploy intelligent chatbots using our data and AI models.
  </Card>

  <Card title="GPTs" icon="play" href="/real-time-data-openai-schema">
    We provide OpenAI's GPT schema, enabling anyone to easily deploy and
    manage their own GPTs.
  </Card>
</CardGroup>