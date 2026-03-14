# Source: https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Structured Output Guide

> How to take advantage of Structured Outputs

Linkup's structured output feature allows you to receive responses in a custom format that you define. This is particularly useful when you need to integrate Linkup's responses directly into your application's data structure or when you want to ensure consistency in the response format.

## How It Works

To use structured outputs:

1. Set `outputType` to `structured` in your API request
2. Provide a JSON schema string in the `structuredOutputSchema` parameter
3. The API will return a response that strictly follows your schema

<Warning>
  Write your query so that its answer contains the information requested in the
  `structuredOutputSchema`- the system will use the query response to fill the
  output
</Warning>

## Basic Examples

Let's look at some simple examples that demonstrate how to use structured outputs for different use cases:

<AccordionGroup>
  <Accordion title="Company Revenue Example" icon="building">
    <p>This example extracts company classification information:</p>

    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="YOUR_API_KEY")

      schema = """{
          "type": "object",
          "properties": {
              "companyName": {
                  "type": "string",
                  "description": "The name of the company"
              },
              "revenueAmount": {
                  "type": "number",
                  "description": "The revenue amount"
              },
              "fiscalYear": {
                  "type": "string",
                  "description": "The fiscal year for this revenue"
              }
          }
      }"""

      response = client.search(
          query="What is Microsoft's 2024 revenue?",
          depth="deep",
          output_type="structured",
          structured_output_schema=schema
      )

      print(response)
      ```

      ```js js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: 'YOUR_API_KEY',
      });

      const schema = {
        "type": "object",
        "properties": {
          "companyName": {
            "type": "string",
            "description": "The name of the company"
          },
          "revenueAmount": {
            "type": "number",
            "description": "The revenue amount"
          },
          "fiscalYear": {
            "type": "string",
            "description": "The fiscal year for this revenue"
          }
        }
      };

      const getCompanyRevenue = async () => {
        return await client.search({
          query: "What is Microsoft's 2024 revenue?",
          depth: 'deep',
          outputType: 'structured',
          structuredOutputSchema: schema
        });
      };

      getCompanyRevenue().then(console.log);
      ```

      ```bash curl theme={null}
      curl --request POST \
        --url https://api.linkup.so/v1/search \
        --header 'Authorization: Bearer YOUR_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "q": "What is Microsoft'\''s 2024 revenue?",
        "depth": "deep",
        "outputType": "structured",
        "structuredOutputSchema": "{\"type\":\"object\",\"properties\":{\"companyName\":{\"type\":\"string\",\"description\":\"The name of the company\"},\"revenueAmount\":{\"type\":\"number\",\"description\":\"The revenue amount\"},\"fiscalYear\":{\"type\":\"string\",\"description\":\"The fiscal year for this revenue\"}}}"
      }'
      ```
    </CodeGroup>

    Example response:

    ```json  theme={null}
    {
        "companyName": "Microsoft",
        "revenueAmount": 245100000000,
        "fiscalYear": "2024"
    }
    ```
  </Accordion>

  <Accordion title="Movie Information Example" icon="film">
    <p>This example shows how to retrieve basic information about a movie:</p>

    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="YOUR_API_KEY")

      schema = """{
          "type": "object",
          "properties": {
              "movieTitle": {
                  "type": "string",
                  "description": "The title of the movie"
              },
              "director": {
                  "type": "string",
                  "description": "The director of the movie"
              },
              "releaseYear": {
                  "type": "integer",
                  "description": "The year the movie was released"
              },
              "boxOfficeRevenue": {
                  "type": "number",
                  "description": "The worldwide box office revenue in USD"
              }
          },
          "required": ["movieTitle", "director", "releaseYear", "boxOfficeRevenue"]
      }"""

      response = client.search(
          query="What was the director, release year, and box office revenue for The Matrix?",
          depth="deep",
          output_type="structured",
          structured_output_schema=schema
      )

      print(response)
      ```

      ```js js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: 'YOUR_API_KEY',
      });

      const schema = {
          "type": "object",
          "properties": {
              "movieTitle": {
                  "type": "string",
                  "description": "The title of the movie"
              },
              "director": {
                  "type": "string",
                  "description": "The director of the movie"
              },
              "releaseYear": {
                  "type": "integer",
                  "description": "The year the movie was released"
              },
              "boxOfficeRevenue": {
                  "type": "number",
                  "description": "The worldwide box office revenue in USD"
              }
          },
          "required": ["movieTitle", "director", "releaseYear", "boxOfficeRevenue"]
      };

      const getMovieInfo = async () => {
        return await client.search({
          query: "What was the director, release year, and box office revenue for The Matrix?",
          depth: 'deep',
          outputType: 'structured',
          structuredOutputSchema: schema
        });
      };

      getMovieInfo().then(console.log);
      ```

      ```bash curl theme={null}
      curl --request POST \
        --url https://api.linkup.so/v1/search \
        --header 'Authorization: Bearer YOUR_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "q": "What was the director, release year, and box office revenue for The Matrix?",
        "depth": "deep",
        "outputType": "structured",
        "structuredOutputSchema": "{\"type\":\"object\",\"properties\":{\"movieTitle\":{\"type\":\"string\",\"description\":\"The title of the movie\"},\"director\":{\"type\":\"string\",\"description\":\"The director of the movie\"},\"releaseYear\":{\"type\":\"integer\",\"description\":\"The year the movie was released\"},\"boxOfficeRevenue\":{\"type\":\"number\",\"description\":\"The worldwide box office revenue in USD\"}}}"
      }'
      ```
    </CodeGroup>

    Example response:

    ```json  theme={null}
    {
        "movieTitle": "The Matrix",
        "director": "Lana and Lilly Wachowski",
        "releaseYear": 1999,
        "boxOfficeRevenue": 465300000
    }
    ```
  </Accordion>

  <Accordion title="Weather Information Example" icon="cloud-sun">
    <p>This example retrieves weather information for travel planning:</p>

    <CodeGroup>
      ```python python theme={null}
      from linkup import LinkupClient

      client = LinkupClient(api_key="YOUR_API_KEY")

      schema = """{
          "type": "object",
          "properties": {
              "city": {
                  "type": "string",
                  "description": "The name of the city"
              },
              "averageTemperature": {
                  "type": "object",
                  "properties": {
                      "summer": {
                          "type": "number",
                          "description": "Average temperature in summer (°C)"
                      },
                      "winter": {
                          "type": "number",
                          "description": "Average temperature in winter (°C)"
                      }
                  }
              },
              "annualRainfall": {
                  "type": "number",
                  "description": "Annual rainfall in millimeters"
              },
              "bestTimeToVisit": {
                  "type": "array",
                  "items": {
                      "type": "string"
                  },
                  "description": "The recommended months to visit"
              }
          }
      }"""

      response = client.search(
          query="What is the average temperature, rainfall, and best time to visit Tokyo?",
          depth="deep",
          output_type="structured",
          structured_output_schema=schema
      )

      print(response)
      ```

      ```js js theme={null}
      import { LinkupClient } from 'linkup-sdk';

      const client = new LinkupClient({
        apiKey: 'YOUR_API_KEY',
      });

      const schema = {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The name of the city"
          },
          "averageTemperature": {
            "type": "object",
            "properties": {
              "summer": {
                "type": "number",
                "description": "Average temperature in summer (°C)"
              },
              "winter": {
                "type": "number",
                "description": "Average temperature in winter (°C)"
              }
            }
          },
          "annualRainfall": {
            "type": "number",
            "description": "Annual rainfall in millimeters"
          },
          "bestTimeToVisit": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The recommended months to visit"
          }
        }
      };

      const getWeatherInfo = async () => {
        return await client.search({
          query: "What is the average temperature, rainfall, and best time to visit Tokyo?",
          depth: 'deep',
          outputType: 'structured',
          structuredOutputSchema: schema
        });
      };

      getWeatherInfo().then(console.log);
      ```

      ```bash curl theme={null}
      curl --request POST \
        --url https://api.linkup.so/v1/search \
        --header 'Authorization: Bearer YOUR_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "q": "What is the average temperature, rainfall, and best time to visit Tokyo?",
        "depth": "deep",
        "outputType": "structured",
        "structuredOutputSchema": "{\"type\":\"object\",\"properties\":{\"city\":{\"type\":\"string\",\"description\":\"The name of the city\"},\"averageTemperature\":{\"type\":\"object\",\"properties\":{\"summer\":{\"type\":\"number\",\"description\":\"Average temperature in summer (°C)\"},\"winter\":{\"type\":\"number\",\"description\":\"Average temperature in winter (°C)\"}}},\"annualRainfall\":{\"type\":\"number\",\"description\":\"Annual rainfall in millimeters\"},\"bestTimeToVisit\":{\"type\":\"array\",\"items\":{\"type\":\"string\"},\"description\":\"The recommended months to visit\"}}}"
      }'
      ```
    </CodeGroup>

    Example response:

    ```json  theme={null}
    {
        "city": "Tokyo",
        "averageTemperature": {
            "summer": 26.4,
            "winter": 6.1
        },
        "annualRainfall": 1530.8,
        "bestTimeToVisit": ["March", "April", "October", "November"]
    }
    ```
  </Accordion>
</AccordionGroup>

## Advanced Example: Competitive Analysis

This example shows how to extract structured competitive analysis information:

<CodeGroup>
  ```python python [expandable] theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="YOUR_API_KEY")

  schema = """{
    "type": "object",
    "properties": {
      "companies": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "marketPosition": {
              "type": "object",
              "properties": {
                "globalMarketShare": {
                  "type": "number"
                },
                "rankingByRevenue": {
                  "type": "integer"
                }
              }
            },
            "strengths": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "challenges": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        }
      },
      "marketOverview": {
        "type": "string"
      }
    }
  }"""

  response = client.search(
    query="Compare Apple and Samsung in the smartphone market, focusing on their market share, global revenue, key strengths, and primary challenges.",
    depth="deep",
    output_type="structured",
    structured_output_schema=schema
  )

  print(response)

  ```

  ```js js [expandable] theme={null}
  import { LinkupClient } from "linkup-sdk";

  const client = new LinkupClient({
  	apiKey: "YOUR_API_KEY",
  });

  const schema = {
  	type: "object",
  	properties: {
  		companies: {
  			type: "array",
  			items: {
  				type: "object",
  				properties: {
  					name: {
  						type: "string",
  					},
  					marketPosition: {
  						type: "object",
  						properties: {
  							globalMarketShare: {
  								type: "number",
  							},
  							rankingByRevenue: {
  								type: "integer",
  							},
  						},
  					},
  					strengths: {
  						type: "array",
  						items: {
  							type: "string",
  						},
  					},
  					challenges: {
  						type: "array",
  						items: {
  							type: "string",
  						},
  					},
  				},
  			},
  		},
  		marketOverview: {
  			type: "string",
  		},
  	},
  };

  const getCompetitiveAnalysis = async () => {
  	return await client.search({
  		query:
  			"Compare Apple and Samsung in the smartphone market, focusing on their market share, global revenue, key strengths, and primary challenges.",
  		depth: "deep",
  		outputType: "structured",
  		structuredOutputSchema: schema,
  	});
  };

  getCompetitiveAnalysis().then(console.log);
  ```

  ```bash curl [expandable] theme={null}
  curl --request POST \
    --url https://api.linkup.so/v1/search \
    --header 'Authorization: Bearer YOUR_API_KEY' \
    --header 'Content-Type: application/json' \
    --data '{
    "q": "Compare Apple and Samsung in the smartphone market, focusing on their market share, global revenue, key strengths, and primary challenges.",
    "outputType": "structured",
    "depth": "deep",
    "structuredOutputSchema": "{\"type\":\"object\",\"properties\":{\"companies\":{\"type\":\"array\",\"items\":{\"type\":\"object\",\"properties\":{\"name\":{\"type\":\"string\"},\"marketPosition\":{\"type\":\"object\",\"properties\":{\"globalMarketShare\":{\"type\":\"number\"},\"rankingByRevenue\":{\"type\":\"integer\"}}},\"strengths\":{\"type\":\"array\",\"items\":{\"type\":\"string\"}},\"challenges\":{\"type\":\"array\",\"items\":{\"type\":\"string\"}}}}},\"marketOverview\":{\"type\":\"string\"}}}"
  }'
  ```
</CodeGroup>

Example response:

```json [expandable] theme={null}
{
	"companies": [
		{
			"name": "Apple",
			"marketPosition": {
				"globalMarketShare": 17.2,
				"rankingByRevenue": 1
			},
			"strengths": [
				"Strong brand loyalty",
				"Premium pricing power",
				"Integrated ecosystem"
			],
			"challenges": [
				"Market saturation",
				"Strong competition in emerging markets",
				"Supply chain dependencies"
			]
		},
		{
			"name": "Samsung",
			"marketPosition": {
				"globalMarketShare": 20.1,
				"rankingByRevenue": 2
			},
			"strengths": [
				"Diverse product portfolio",
				"Vertical integration",
				"Strong presence in emerging markets"
			],
			"challenges": [
				"Intense competition at all price points",
				"Margin pressure in mid-range segment",
				"Brand perception vs Apple in premium segment"
			]
		}
	],
	"marketOverview": "The smartphone market continues to be highly competitive with a focus on 5G capabilities and AI integration. Premium segment shows steady growth while mid-range experiences intense competition."
}
```

## Making Fields Required

To make sure that the key fields you defined are filled, you can mark them as `required` in your json schema.

```json Required Fields Highlight {17} theme={null}
{
	"type": "object",
	"properties": {
		"movieTitle": {
			"type": "string",
			"description": "The title of the movie"
		},
		"director": {
			"type": "string",
			"description": "The director of the movie"
		},
		"releaseYear": {
			"type": "integer",
			"description": "The year the movie was released"
		}
	},
	"required": ["movieTitle", "director"]
}
```

## Best Practices

1. **Schema Design**:

   * Keep your schema as simple as possible while meeting your needs
   * Add descriptions to the fields to limit ambiguity
   * Use appropriate data types (string, number, boolean, etc.)
   * When in doubt, refer to the [JSON documentation](https://json-schema.org/learn/getting-started-step-by-step)

2. **Query Formulation**:
   * Write your query so that its answer contains the information requested in the `structuredOutputSchema`- the system will use the query response to fill the output
   * Provide clear context in your query and use explicit instructions

## Common Use Cases

* Company classification and categorization
* Competitive analysis
* Market research
* Product comparisons
* Company performance assessments

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).