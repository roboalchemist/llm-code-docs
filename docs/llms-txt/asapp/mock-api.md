# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/mock-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mock API Connections

You can mock API connections using Mock APIs.

GenerativeAgent supports mocking API connections to test your raw API responses. Mock API Functions let you define request parameters (in JSON) without needing a live API.

The main benefits of mocking API connections are:

* Rapid prototyping of new Functions without a fully built API.
* Testing how GenerativeAgent processes or populates request parameters before real integration.
* Simplifying configuration for teams that want to get interacting with GenerativeAgent quickly before building or exposing internal APIs.

## Create a Mock API Function

Navigate to the Functions page in the main GenerativeAgent menu.

1. Click "Create Function"

2. Choose "Integrate Later"
   * You will be prompted to select an existing API or "Integrate later."
   * Select "Integrate later" to mark this Function as a Mock API and define the request parameters directly.
   <Frame>
     <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/IntegrateLater.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=b778dc3043fd7c028f1ae9bd55b339d8" data-og-width="1570" width="1570" data-og-height="430" height="430" data-path="images/generativeagent/IntegrateLater.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/IntegrateLater.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=144ecd4ab4f0d15aaa9a138dfea7a89d 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/IntegrateLater.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=936c1de2296b2615a110411dcb2e0d80 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/IntegrateLater.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=ff4a55271feae205cec783d4495b8dda 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/IntegrateLater.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=96acf18cd8117d8f95eb9b04493c0afd 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/IntegrateLater.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=01510b19fb9a55a07a4c177e1df0c58a 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/IntegrateLater.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=fb14baff9f49a670f15823cfe119e024 2500w" />
   </Frame>

3. Name and describe the new Function
   * **Function Name**: Give it a concise, unique name
   * **Function Purpose**: Briefly describe what the Mock Function is for
   <Tip>
     Example:

     * Name: “get\_flight\_details”
     * Purpose: “Retrieves flight information given a PNR”
   </Tip>

4. Define Request Parameters (JSON)
   * Under "Request parameters," enter a valid JSON schema describing the parameters you want.
   * You can pick a template from the "Examples" dropdown or start with an empty JSON schema.
   <Frame>
     <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=33b627189a3e45b34a1065eb5963390f" data-og-width="3302" width="3302" data-og-height="1058" height="1058" data-path="images/generativeagent/MockAPIExample.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=308c3ef5b5602f5f5cc51d6d3f5ba902 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=3d62ce5e183d7d50b99afa3de05ad113 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=18289c4d24f26ebaa6f34c567ff9d42f 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8f86c20e578678a68428f7ed3df20a7d 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0d0ecefb562fa98ba7ee3bf411575841 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c103fa114bf62cbb408a1f8e7787fc74 2500w" />
   </Frame>
   * **Example Request**
   ```json  theme={null}
       {  
       "name": "name_of_function",  
       "description": "Brief description of what the Function is for",  
       "strict": true,  
       "parameters": {  
           "type": "object",  
           "required": ["account_number"],  
           "properties": {  
           "account_number": {  
               "type": "string",  
               "description": "The user’s account number."  
           },  
           "include_details": {  
               "type": "boolean",  
               "description": "Whether to include itemized details."  
           }  
           }  
       }  
       }  
   ```
   <Note>
     Make sure the JSON is valid.
     The system prevents invalid schemas from being saved.
   </Note>

5. Save your Function

   * Click "Create Function" (or "Save"). If any part of your schema is invalid, an error will appear.
   * After saving, you remain on the function detail page, which shows the Function's configuration and preview.

   <Note>
     You can configure additional fields and variables if you need prompts or placeholders in the conversation flow.

     For example: “Message before sending”, “Confirmation Message”, “Reference Variables”
   </Note>

### Best Practices

Here are some recommendations to help you make the best use of the Mock API feature:

<AccordionGroup>
  <Accordion title="Keep it Simple">
    Start with the core parameters. Add more detail as your needs become clearer.
  </Accordion>

  <Accordion title="Use Meaningful Descriptions">
    Parameter descriptions help GenerativeAgent understand what the parameters are and how to determine their values.
    They also help future users to remember each parameter purpose.
  </Accordion>

  <Accordion title="Prototype First, Integrate Later">
    Begin testing your Function with a Mock schema, then transition smoothly to a real API when ready.
  </Accordion>
</AccordionGroup>

## Connect to a real API

When you are ready to connect the Function to an existing API in the Console:

1. Click "Replace" on the Function detail page.
2. Select an existing API connection or create a new one.
3. Once replaced, the Function will call the real API during interactions instead of the Mock schema.

### Use Test Users

You can use [Test Scenarios](/generativeagent/configuring/tasks-and-functions/test-scenarios) to mock API return scenarios in the Previewer.
