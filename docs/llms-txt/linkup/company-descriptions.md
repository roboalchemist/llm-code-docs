# Source: https://docs.linkup.so/pages/documentation/tutorials/company-descriptions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Company Descriptions Generator

> Building a tool to generate rich company descriptions using Linkup API

This tutorial will show you how to build a company description generator that takes a company name and country as input and returns comprehensive information about the company using the Linkup API's structured output feature.

## What We're Building

Our company description generator will:

* Take a company name and country as input
* Use Linkup API to search for information about the company
* Return structured data about the company (description, industry, size, location, etc.)

## Building the Generator

<Steps>
  <Step title="Define the Schema">
    Before we start coding, let's define the schema that specifies what information we want to extract about companies. This schema will be used throughout our implementation:

    <CodeGroup>
      ```python python [expandable] theme={null}
      COMPANY_SCHEMA = {
          "type": "object",
          "properties": {
              "name": {
                  "type": "string",
                  "description": "The official name of the company"
              },
              "description": {
                  "type": "string",
                  "description": "A comprehensive description of what the company does"
              },
              "location": {
                  "type": "string",
                  "description": "Location of company headquarters"
              },
              "companySize": {
                  "type": "string",
                  "description": "Approximate number of employees"
              },
              "linkedInUrl": {
                  "type": "string",
                  "description": "Company's LinkedIn profile URL"
              }
          },
          "required": ["name", "description"]
      }
      ```

      ```javascript js [expandable] theme={null}
      const COMPANY_SCHEMA = {
          "type": "object",
          "properties": {
              "name": {
                  "type": "string",
                  "description": "The official name of the company"
              },
              "description": {
                  "type": "string",
                  "description": "A comprehensive description of what the company does"
              },
              "location": {
                  "type": "string",
                  "description": "Location of company headquarters"
              },
              "companySize": {
                  "type": "string",
                  "description": "Approximate number of employees"
              },
              "linkedInUrl": {
                  "type": "string",
                  "description": "Company's LinkedIn profile URL"
              }
          },
          "required": ["name", "description"]
      };
      ```
    </CodeGroup>

    This schema defines all the fields we want to extract about a company. The required fields are `name`, `description`, and `industry`, while the rest are optional but provide valuable additional information.
  </Step>

  <Step title="Install the SDK">
    Next, let's install the Linkup SDK in your preferred language:

    <CodeGroup>
      ```python python theme={null}
      pip install linkup-sdk
      ```

      ```javascript js theme={null}
      npm i linkup-sdk
      ```
    </CodeGroup>
  </Step>

  <Step title="Set Up the Client">
    Initialize the Linkup client with your API key:

    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>

    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")
      ```

      ```javascript js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: '<YOUR_LINKUP_API_KEY>',
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Create the Query Generator">
    Create a function to generate the search query:

    <CodeGroup>
      ```python python theme={null}
      def generate_query(company_name: str, country: str) -> str:
          query = (
                  f"Find detailed information about {company_name} in {country}. "
                  "Include their main products/services, industry focus, company size, "
                  "and any notable achievements or recent news. Also find their "
                  "LinkedIn company page if available."
              )
          return query
      ```

      ```typescript js theme={null}
      function generateQuery(companyName: string, country: string) {
          let query;

          query = (
                  `Find detailed information about ${companyName} in ${country}. ` +
                  "Include their main products/services, industry focus, company size, " +
                  "and any notable achievements or recent news. Also find their " +
                  "LinkedIn company page if available."
              );

          return query;
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Complete Implementation">
    Here's the complete implementation that puts everything together:

    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient
      import json
      from typing import Dict, Any
      from pprint import pprint

      # Schema definition (from Step 1)
      COMPANY_SCHEMA = {
          "type": "object",
          "properties": {
              "name": {
                  "type": "string",
                  "description": "The official name of the company"
              },
              "description": {
                  "type": "string",
                  "description": "A comprehensive description of what the company does"
              },
              "location": {
                  "type": "string",
                  "description": "Location of company headquarters"
              },
              "companySize": {
                  "type": "string",
                  "description": "Approximate number of employees"
              },
              "linkedInUrl": {
                  "type": "string",
                  "description": "Company's LinkedIn profile URL"
              }
          },
          "required": ["name", "description"]
      }

      # Initialize the client
      client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")

      # Query generator (from Step 4)
      def generate_query(company_name: str, country: str) -> str:
          query = (
                  f"Find detailed information about {company_name} in {country}. "
                  "Include their main products/services, industry focus, company size, "
                  "and any notable achievements or recent news. Also find their "
                  "LinkedIn company page if available."
              )
          return query

      def generate_company_description(company_name: str, country: str) -> Dict[str, Any]:
          """
          Generate a structured description of a company using its name, country.

          Args:
              company_name: Name of the company
              country: Country where the company operates

          Returns:
              Dictionary containing structured company information
          """
          try:
              # Clean input
              company_name = company_name.strip()
              country = country.strip()

              # Generate search query using the function from Step 4
              query = generate_query(company_name, country)

              # Call Linkup API
              response = client.search(
                  query=query,
                  depth="deep",  # Use deep for more thorough results
                  output_type="structured",
                  structured_output_schema=json.dumps(COMPANY_SCHEMA)
              )

              return response

          except Exception as e:
              return {
                  "error": str(e),
                  "company_name": company_name,
                  "country": country
              }

      # Example usage
      if __name__ == "__main__":
          # Example companies
          companies = [
              ("Anthropic", "United States"),
              ("Stripe", "United States"),
              ("OpenAI", "United States")
          ]

          for company_name, country in companies:
              print(f"\nLooking up: {company_name} in {country}")
              result = generate_company_description(company_name, country)
              pprint(result)
      ```

      ```typescript js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      // Schema definition (from Step 1)
      const COMPANY_SCHEMA = {
          "type": "object",
          "properties": {
              "name": {
                  "type": "string",
                  "description": "The official name of the company"
              },
              "description": {
                  "type": "string",
                  "description": "A comprehensive description of what the company does"
              },
              "location": {
                  "type": "string",
                  "description": "Location of company headquarters"
              },
              "companySize": {
                  "type": "string",
                  "description": "Approximate number of employees"
              },
              "linkedInUrl": {
                  "type": "string",
                  "description": "Company's LinkedIn profile URL"
              }
          },
          "required": ["name", "description"]
      };

      // Initialize the client
      const client = new LinkupClient({
          apiKey: '<YOUR_LINKUP_API_KEY>',
      });

      // Query generator (from Step 4)
      function generateQuery(companyName: string, country: string) {
          let query;
          query = (
                  `Find detailed information about ${companyName} in ${country}. ` +
                  "Include their main products/services, industry focus, company size, " +
                  "and any notable achievements or recent news. Also find their " +
                  "LinkedIn company page if available."
              );
          return query;
      }

      async function generateCompanyDescription(companyName: string, country: string) {
          try {
              // Clean input
              companyName = companyName.trim();
              country = country.trim();

              // Generate search query using the function from Step 4
              const query = generateQuery(companyName, country);

              // Call Linkup API
              const response = await client.search({
                  query: query,
                  depth: "deep",  // Use deep for more thorough results
                  outputType: "structured",
                  structuredOutputSchema: COMPANY_SCHEMA
              });

              return response;

          } catch (error: any) {
              return {
                  error: error.message,
                  companyName: companyName,
                  country: country
              };
          }
      }

      // Example usage
      async function main() {
          // Example companies
          const companies = [
              ["Anthropic", "United States"],
              ["Stripe", "United States"],
              ["OpenAI", "United States"]
          ];

          for await (const [companyName, country] of companies) {
              console.log(`\nLooking up: ${companyName} in ${country}`);
              const result = await generateCompanyDescription(companyName, country);
              console.log(JSON.stringify(result, null, 2));
          }
      }

      main().catch(console.error);
      ```
    </CodeGroup>
  </Step>
</Steps>

## How It Works

The company description generator works in three main steps:

1. **Input Processing**: The tool takes a company name and country as input and cleans them.
2. **Query Generation**: It creates a search query that includes both the company name and country to improve search accuracy.
3. **Structured Output**: Uses Linkup's structured output feature with a comprehensive schema to ensure consistent, well-formatted results.

## Possible Enhancements

For a production version, consider adding:

* Add as much information you have about companies in the queries, to limit ambiguity about which company you are searching for.
* Implement rate limiting and error handling for API usage.
* Batch processing to search for multiple companies in parallel if you are enriching a dataset for example.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).