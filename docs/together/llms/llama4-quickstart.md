# Source: https://docs.together.ai/docs/llama4-quickstart.md

# Llama 4 Quickstart

> How to get the most out of the new Llama 4 models.

Together AI offers day 1 support for the new Llama 4 multilingual vision models that can analyze multiple images and respond to queries about them.

Register for a [Together AI account](https://api.together.xyz/) to get an API key. New accounts come with free credits to start. Install the Together AI library for your preferred language.

## How to use Llama 4 Models

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()  # API key via api_key param or TOGETHER_API_KEY env var

  # Query image with Llama 4 Maverick model
  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What can you see in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();  // API key via apiKey param or TOGETHER_API_KEY env var

  async function main() {
   const response = await together.chat.completions.create({
     model: "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
     messages: [{
       role: "user",
       content: [
         { type: "text", text: "What can you see in this image?" },
         { type: "image_url", image_url: { url: "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png" }}
       ]
     }]
   });

   console.log(response.choices[0].message.content);
  }

  main();
  ```
</CodeGroup>

### Output

```
The image depicts a serene landscape of Yosemite National Park, featuring a river flowing through a valley surrounded by towering cliffs and lush greenery.

*   **River:**
    *   The river is calm and peaceful, with clear water that reflects the surrounding scenery.
    *   It flows gently from the bottom-left corner to the center-right of the image.
    *   The riverbank is lined with rocks and grasses, adding to the natural beauty of the scene.
*   **Cliffs:**
    *   The cliffs are massive and imposing, rising steeply from the valley floor.
    *   They are composed of light-colored rock, possibly granite, and feature vertical striations.
    *   The cliffs are covered in trees and shrubs, which adds to their rugged charm.
*   **Trees and Vegetation:**
    *   The valley is densely forested, with tall trees growing along the riverbanks and on the cliffsides.
    *   The trees are a mix of evergreen and deciduous species, with some displaying vibrant green foliage.
    *   Grasses and shrubs grow in the foreground, adding texture and color to the scene.
*   **Sky:**
    *   The sky is a brilliant blue, with only a few white clouds scattered across it.
    *   The sun appears to be shining from the right side of the image, casting a warm glow over the scene.

In summary, the image presents a breathtaking view of Yosemite National Park, showcasing the natural beauty of the valley and its surroundings. The calm river, towering cliffs, and lush vegetation all contribute to a sense of serenity and wonder.
```

<Info>
  ### Llama4 Notebook

  If you'd like to see common use-cases in code see our [notebook here](https://github.com/togethercomputer/together-cookbook/blob/main/Getting_started_with_Llama4.ipynb) .
</Info>

## Llama 4 Model Details

### Llama 4 Maverick

* **Model String**: *meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8*

* **Specs**:

  * 17B active parameters (400B total)
  * 128-expert MoE architecture
  * 524,288 context length (will be increased to 1M)
  * Support for 12 languages: Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese
  * Multimodal capabilities (text + images)
  * Support Function Calling

* **Best for**: Enterprise applications, multilingual support, advanced document intelligence

* **Knowledge Cutoff**: August 2024

### Llama 4 Scout

* **Model String**: *meta-llama/Llama-4-Scout-17B-16E-Instruct*

* **Specs**:

  * 17B active parameters (109B total)
  * 16-expert MoE architecture
  * 327,680 context length (will be increased to 10M)
  * Support for 12 languages: Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese
  * Multimodal capabilities (text + images)
  * Support Function Calling

* **Best for**: Multi-document analysis, codebase reasoning, and personalized tasks

* **Knowledge Cutoff**: August 2024

## Function Calling

<CodeGroup>
  ```python Python theme={null}
  import os
  import json
  import openai

  client = openai.OpenAI(
      base_url="https://api.together.xyz/v1",
      api_key=os.environ["TOGETHER_API_KEY"],
  )

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_current_weather",
              "description": "Get the current weather in a given location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA",
                      },
                      "unit": {
                          "type": "string",
                          "enum": ["celsius", "fahrenheit"],
                      },
                  },
              },
          },
      }
  ]

  messages = [
      {
          "role": "system",
          "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
      },
      {
          "role": "user",
          "content": "What is the current temperature of New York, San Francisco and Chicago?",
      },
  ]

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=messages,
      tools=tools,
      tool_choice="auto",
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
  ```
</CodeGroup>

### Output

<CodeGroup>
  ```json JSON theme={null}
  [
    {
      "id": "call_1p75qwks0etzfy1g6noxvsgs",
      "function": {
        "arguments": "{\"location\":\"New York, NY\",\"unit\":\"fahrenheit\"}",
        "name": "get_current_weather"
      },
      "type": "function"
    },
    {
      "id": "call_aqjfgn65d0c280fjd3pbzpc6",
      "function": {
        "arguments": "{\"location\":\"San Francisco, CA\",\"unit\":\"fahrenheit\"}",
        "name": "get_current_weather"
      },
      "type": "function"
    },
    {
      "id": "call_rsg8muko8hymb4brkycu3dm5",
      "function": {
        "arguments": "{\"location\":\"Chicago, IL\",\"unit\":\"fahrenheit\"}",
        "name": "get_current_weather"
      },
      "type": "function"
    }
  ]
  ```
</CodeGroup>

## Query models with multiple images

Currently this model supports **5 images** as input.

<CodeGroup>
  ```python Python theme={null}
  # Multi-modal message with multiple images
  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Compare these two images."},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                      },
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/slack.png"
                      },
                  },
              ],
          }
      ],
  )
  print(response.choices[0].message.content)
  ```
</CodeGroup>

### Output

```
The first image is a collage of multiple identical landscape photos showing a natural scene with rocks, trees, and a stream under a blue sky. The second image is a screenshot of a mobile app interface, specifically the navigation menu of the Canva app, which includes icons for Home, DMs (Direct Messages), Activity, Later, Canvases, and More.

### Comparison:
1. **Content**:
   - The first image focuses on a natural landscape.
   - The second image shows a digital interface from an app.

2. **Purpose**:
   - The first image could be used for showcasing nature, design elements in graphic work, or as a background.
   - The second image represents the functionality and layout of the Canva app's navigation system.

3. **Visual Style**:
   - The first image has vibrant colors and realistic textures typical of outdoor photography.
   - The second image uses flat design icons with a simple color palette suited for user interface design.

4. **Context**:
   - The first image is likely intended for artistic or environmental contexts.
   - The second image is relevant to digital design and app usability discussions.
```

## Llama 4 Use-cases

### Llama 4 Maverick:

* **Instruction following and Long context ICL**: Very consistent in following precise instructions with in-context learning across very long contexts
* **Multilingual customer support**: Process support tickets with screenshots in 12 languages to quickly diagnose technical issues
* **Multimodal capabilities**: Particularly strong at OCR and chart/graph interpretation
* **Agent/tool calling work**: Designed for agentic workflows with consistent tool calling capabilities

### Llama 4 Scout:

* **Summarization**: Excels at condensing information effectively
* **Function calling**: Performs well in executing predefined functions
* **Long context ICL recall**: Shows strong ability to recall information from long contexts using in-context learning
* **Long Context RAG**: Serves as a workhorse model for coding flows and RAG (Retrieval-Augmented Generation) applications
* **Cost-efficient**: Provides good performance as an affordable long-context model


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt