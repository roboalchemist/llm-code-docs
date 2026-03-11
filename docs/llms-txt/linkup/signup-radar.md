# Source: https://docs.linkup.so/pages/documentation/tutorials/signup-radar.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Signup Radar 

> Building a signup radar to get to know your new users

This tutorial will show you how to build a simple "signup radar" that takes an email address and returns information about the person who signed up, using the Linkup API's structured output feature.

## What We're Building

Our signup radar will:

* Take an email address as input
* Use Linkup API to search for information about the person
* Return structured data about the person (name, position, company, LinkedIn URL, etc.)

## Prerequisites

* A Linkup API key
* Python or Node.js installed

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>

<Steps>
  <Step title="Install the SDK">
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

  <Step title="Define the Structured Output Schema">
    The key to our signup radar is using Linkup's structured output feature. We need to define a schema that specifies what information we want to extract.

    <CodeGroup>
      ```python python theme={null}
      import json

      schema = {
        "type": "object",
        "properties": {
          "fullName": {
            "type": "string",
            "description": "The full name of the person"
          },
          "company": {
            "type": "string",
            "description": "The company the person works for"
          },
          "position": {
            "type": "string",
            "description": "The job title or position of the person"
          },
          "linkedInUrl": {
            "type": "string",
            "description": "The LinkedIn profile URL of the person"
          },
          "companyWebsite": {
            "type": "string",
            "description": "The website of the company"
          },
          "additionalInfo": {
            "type": "string",
            "description": "Any additional relevant information about the person"
          }
        },
        "required": ["fullName", "company"]
      }

      schema_str = json.dumps(schema)
      ```

      ```javascript js theme={null}
      const schema = {
        type: "object",
        properties: {
          fullName: {
            type: "string",
            description: "The full name of the person"
          },
          company: {
            type: "string",
            description: "The company the person works for"
          },
          position: {
            type: "string",
            description: "The job title or position of the person"
          },
          linkedInUrl: {
            type: "string",
            description: "The LinkedIn profile URL of the person"
          },
          companyWebsite: {
            type: "string",
            description: "The website of the company"
          },
          additionalInfo: {
            type: "string",
            description: "Any additional relevant information about the person"
          }
        },
        required: ["fullName", "company"]
      };
      ```
    </CodeGroup>
  </Step>

  <Step title="Create the Signup Radar Function">
    <CodeGroup>
      ```python python theme={null}
      def signup_radar(email):
          # Extract name and domain
          name_part = email.split('@')[0]
          domain = email.split('@')[1]
          
          # Format name for searching (convert saksena to Saksena)
          formatted_name = name_part.capitalize()
          
          # Determine company from domain (if not common email provider)
          company_hint = ""
          common_domains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"]
          if domain not in common_domains:
              company_hint = domain.split('.')[0]
          
          # Create search query
          if company_hint:
              query = f"Find the LinkedIn profile URL for {formatted_name} who works at {company_hint}. Return their full name, current position, and company information."
          else:
              query = f"Find the LinkedIn profile URL for someone with the email username {formatted_name}. Return their full name, current position, and company information."
          
          # Call Linkup API
          response = client.search(
              query=query,
              depth="deep",  # Use deep for more thorough results
              output_type="structured",
              structured_output_schema=schema_str
          )
          
          return response

      # Example usage
      from pprint import pprint

      result = signup_radar("philippe@linkup.so")
      pprint(result)
      ```

      ```javascript js theme={null}
      async function signupRadar(email) {
          // Extract name and domain
          const [namePart, domain] = email.split('@');
          
          // Format name for searching
          const formattedName = namePart.charAt(0).toUpperCase() + namePart.slice(1);
          
          // Determine company from domain (if not common email provider)
          let companyHint = "";
          const commonDomains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"];
          if (!commonDomains.includes(domain)) {
              companyHint = domain.split('.')[0];
          }
          
          // Create search query
          let query;
          if (companyHint) {
              query = `Find the LinkedIn profile URL for ${formattedName} who works at ${companyHint}. Return their full name, current position, and company information.`;
          } else {
              query = `Find the LinkedIn profile URL for someone with the email username ${formattedName}. Return their full name, current position, company, and LinkedIn URL.`;
          }
          
          // Call Linkup API
          const response = await client.search({
              query: query,
              depth: "deep",  // Use deep for more thorough results
              outputType: "structured",
              structuredOutputSchema: schema
          });
          
          return response;
      }

      // Example usage
      signupRadar("philippe@linkup.so").then(console.log);
      ```
    </CodeGroup>
  </Step>

  <Step title="Enhance Query Generation">
    Let's improve our query to get better results:

    <CodeGroup>
      ```python python theme={null}
      def generate_query(email):
          name_part = email.split('@')[0]
          domain = email.split('@')[1]
          
          # Handle different name formats (snake_case, dot.case, etc.)
          if "_" in name_part:
              name_parts = name_part.split("_")
              formatted_name = " ".join(part.capitalize() for part in name_parts)
          elif "." in name_part:
              name_parts = name_part.split(".")
              formatted_name = " ".join(part.capitalize() for part in name_parts)
          else:
              formatted_name = name_part.capitalize()
          
          # Determine company from domain
          common_domains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"]
          if domain not in common_domains:
              company = domain.split('.')[0].capitalize()
              return f"Find the LinkedIn profile URL for this person: {formatted_name} at {company}. If the domain of the email address ({domain}) is not a common email provider, it is probably the name of the company this person works for and {domain} is probably the company website, so search specifically for someone with that name at this company. Return their full name, position, company details, LinkedIn URL, as well as any relevant information you can find about them."
          else:
              return f"Find the LinkedIn profile URL for this person with email username {formatted_name}. Return their full name, current position, company, and LinkedIn URL."
      ```

      ```javascript js theme={null}
      function generateQuery(email) {
          const [namePart, domain] = email.split('@');
          
          // Handle different name formats (snake_case, dot.case, etc.)
          let formattedName;
          if (namePart.includes("_")) {
              formattedName = namePart.split("_")
                  .map(part => part.charAt(0).toUpperCase() + part.slice(1))
                  .join(" ");
          } else if (namePart.includes(".")) {
              formattedName = namePart.split(".")
                  .map(part => part.charAt(0).toUpperCase() + part.slice(1))
                  .join(" ");
          } else {
              formattedName = namePart.charAt(0).toUpperCase() + namePart.slice(1);
          }
          
          // Determine company from domain
          const commonDomains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"];
          if (!commonDomains.includes(domain)) {
              const company = domain.split('.')[0].charAt(0).toUpperCase() + domain.split('.')[0].slice(1);
              return `Find the LinkedIn profile URL for this person: ${formattedName} at ${company}. If the domain of the email address (${domain}) is not a common email provider, it is probably the name of the company this person works for and ${domain} is probably the company website, so search specifically for someone with that name at this company. Return their full name, position, company details, and LinkedIn URL, as well as any relevant information you can find about them.`;
          } else {
              return `Find the LinkedIn profile URL for this person with email username ${formattedName}. Return their full name, current position, company, and LinkedIn URL.`;
          }
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Put It All Together">
    Here's the complete implementation:

    <CodeGroup>
      ```python python [expandable] theme={null}
      from linkup import LinkupClient
      import json
      from pprint import pprint

      class SignupRadar:
          def __init__(self, api_key):
              self.client = LinkupClient(api_key=api_key)
              self.schema = {
                  "type": "object",
                  "properties": {
                      "fullName": {
                          "type": "string",
                          "description": "The full name of the person"
                      },
                      "company": {
                          "type": "string",
                          "description": "The company the person works for"
                      },
                      "position": {
                          "type": "string",
                          "description": "The job title or position of the person"
                      },
                      "linkedInUrl": {
                          "type": "string",
                          "description": "The LinkedIn profile URL of the person"
                      },
                      "companyWebsite": {
                          "type": "string",
                          "description": "The website of the company"
                      },
                      "additionalInfo": {
                          "type": "string",
                          "description": "Any additional relevant information about the person"
                      }
                  },
                  "required": ["fullName", "company"]
              }
              self.schema_str = json.dumps(self.schema)
          
          def generate_query(self, email):
              name_part = email.split('@')[0]
              domain = email.split('@')[1]
              
              # Handle different name formats (snake_case, dot.case, etc.)
              if "_" in name_part:
                  name_parts = name_part.split("_")
                  formatted_name = " ".join(part.capitalize() for part in name_parts)
              elif "." in name_part:
                  name_parts = name_part.split(".")
                  formatted_name = " ".join(part.capitalize() for part in name_parts)
              else:
                  formatted_name = name_part.capitalize()
              
              # Determine company from domain
              common_domains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"]
              if domain not in common_domains:
                  company = domain.split('.')[0].capitalize()
                  return f"Find the LinkedIn profile URL for this person: {formatted_name} at {company}. If the domain of the email address ({domain}) is not a common email provider, it is probably the name of the company this person works for and {domain} is probably the company website, so search specifically for someone with that name at this company. Return their full name, position, company details, LinkedIn URL, as well as any relevant information you can find about them."
              else:
                  return f"Find the LinkedIn profile URL for this person with email username {formatted_name}. Return their full name, current position, company, and LinkedIn URL."
          
          def lookup(self, email):
              query = self.generate_query(email)
              
              response = self.client.search(
                  query=query,
                  depth="deep",  # Use deep for more thorough results
                  output_type="structured",
                  structured_output_schema=self.schema_str
              )
              
              return response

      # Example usage
      if __name__ == "__main__":
          radar = SignupRadar(api_key="<YOUR_LINKUP_API_KEY>")
          
          # Example emails
          emails = [
              "philippe@linkup.so",
              "boris@linkup.so"
          ]
          
          for email in emails:
              print(f"\nLooking up: {email}")
              result = radar.lookup(email)
              pprint(result)
      ```

      ```javascript js [expandable] theme={null}
      import { LinkupClient } from 'linkup-sdk';

      class SignupRadar {
          constructor(apiKey) {
              this.client = new LinkupClient({
                  apiKey: apiKey,
              });
              
              this.schema = {
                  type: "object",
                  properties: {
                      fullName: {
                          type: "string",
                          description: "The full name of the person"
                      },
                      company: {
                          type: "string",
                          description: "The company the person works for"
                      },
                      position: {
                          type: "string",
                          description: "The job title or position of the person"
                      },
                      linkedInUrl: {
                          type: "string",
                          description: "The LinkedIn profile URL of the person"
                      },
                      companyWebsite: {
                          type: "string",
                          description: "The website of the company"
                      },
                      additionalInfo: {
                          type: "string",
                          description: "Any additional relevant information about the person"
                      }
                  },
                  required: ["fullName", "company"]
              };
          }
          
          generateQuery(email) {
              const [namePart, domain] = email.split('@');
              
              // Handle different name formats (snake_case, dot.case, etc.)
              let formattedName;
              if (namePart.includes("_")) {
                  formattedName = namePart.split("_")
                      .map(part => part.charAt(0).toUpperCase() + part.slice(1))
                      .join(" ");
              } else if (namePart.includes(".")) {
                  formattedName = namePart.split(".")
                      .map(part => part.charAt(0).toUpperCase() + part.slice(1))
                      .join(" ");
              } else {
                  formattedName = namePart.charAt(0).toUpperCase() + namePart.slice(1);
              }
              
              // Determine company from domain
              const commonDomains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com"];
              if (!commonDomains.includes(domain)) {
                  const company = domain.split('.')[0].charAt(0).toUpperCase() + domain.split('.')[0].slice(1);
                  return `Find the LinkedIn profile URL for this person: ${formattedName} at ${company}. If the domain of the email address (${domain}) is not a common email provider, it is probably the name of the company this person works for and ${domain} is probably the company website, so search specifically for someone with that name at this company. Return their full name, position, company details, and LinkedIn URL, as well as any relevant information you can find about them.`;
              } else {
                  return `Find the LinkedIn profile URL for this person with email username ${formattedName}. Return their full name, current position, company, and LinkedIn URL.`;
              }
          }
          
          async lookup(email) {
              const query = this.generateQuery(email);
              
              const response = await this.client.search({
                  query: query,
                  depth: "deep",  // Use deep for more thorough results
                  outputType: "structured",
                  structuredOutputSchema: this.schema
              });
              
              return response;
          }
      }

      // Example usage
      async function main() {
          const radar = new SignupRadar('<YOUR_LINKUP_API_KEY>');
          
          // Example emails
          const emails = [
              "philippe@linkup.so",
              "boris@linkup.so"
          ];
          
          for (const email of emails) {
              console.log(`\nLooking up: ${email}`);
              const result = await radar.lookup(email);
              console.log(JSON.stringify(result, null, 2));
          }
      }

      main().catch(console.error);
      ```
    </CodeGroup>
  </Step>
</Steps>

## How It Works

1. **Email Analysis**: The tool parses the email to extract the username and domain.
2. **Query Generation**: It creates a smart search query based on the email components:
   * Formats the username to handle common patterns (first.last, first\_last)
   * Uses the domain as a company hint if it's not a common email provider
3. **Structured Output**: Uses Linkup's structured output feature with a custom schema to ensure consistent, well-formatted results.
4. **Deep Search**: Uses the "deep" search depth for more comprehensive results.

## Test Examples

Try the signup radar with these email examples:

* [philippe@linkup.so](mailto:philippe@linkup.so)
* [boris@linkup.so](mailto:boris@linkup.so)
* [sacha@linkup.so](mailto:sacha@linkup.so)
* [philippe.mizrahi@gmail.com](mailto:philippe.mizrahi@gmail.com)

## Advanced Enhancements

For a production version, consider adding:

* Other relevant information on your users you receive in the sign up form. These should be added to the prompt
* Better manage ambiguity when multiple people could own the same email. Change the prompt and the structured output format to allow for multiple potential people
* Error handling for invalid emails or API failures
* Rate limiting to manage API usage
* Async batch processing for multiple emails

## Conclusion

You've now built a simple but powerful "signup radar" using the Linkup API that can extract structured information about users from just their email address. The structured output feature ensures you get consistent, well-formatted data that can be easily integrated into your systems.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).