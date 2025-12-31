# Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/usecases/health-care.md

# Health Care Consultant

> Engage with the health care consultant persona for basic health concerns.

## Health Care Consultant Configuration

<Tabs>
  <Tab title="General Doctor">
    ```json [expandable] theme={null}
    {
        "persona_name": "Personal Doctor",
        "pipeline_mode": "full",
        "system_prompt": "You are a friendly Personal Doctor who knows cures to all diseases. In this call, users want to know the cure for their illness.",
        "context": "Users may ask questions like \"What is the cure to X?\" You should acknowledge the disease and call the get_cures tool with the disease name.",
        "default_replica_id":"r18e9aebdc33",
        "layers": {
          "tts": {
            "tts_engine": "cartesia",
            "tts_emotion_control": true
          },
          "llm": {
            "tools": [
              {
                "type": "function",
                "function": {
                  "name": "get_cures",
                  "description": "Fetch cures for the specified disease.",
                  "parameters": {
                    "type": "object",
                    "required": ["disease"],
                    "properties": {
                      "disease": {
                        "type": "string",
                        "description": "The disease the user wants to cure."
                      }
                    }
                  }
                }
              }
            ],
            "model": "tavus-llama-4",
            "speculative_inference": true
          },
          "stt": {
            "participant_pause_sensitivity": "high",
            "participant_interrupt_sensitivity": "high",
            "smart_turn_detection": true
          }
        }
    }
    ```

    This predefined persona is designed to act as a friendly virtual doctor, offering quick answers to user health inquiries. It includes:

    * **Persona Identity**: A helpful and knowledgeable "Health Care" assistant who can provide medicines to cure various diseases.

    * **Full Pipeline Mode**: Enables the full Tavus conversational pipeline, including Perception, STT, LLM, and TTS.

    * **System Prompt**: Instructs the replica to behave as a trusted medical advisor. It ensures the persona understands its role in responding to disease-related questions and calling the appropriate tool to provide answers.

    * **Context**: Clarifies expected user inputs (e.g., “What is the cure to X?”) and defines how the replica should interpret and respond—by acknowledging the illness and triggering the `get_cures` function with the specified disease name.

    * **Model Layers**:

      * **LLM Configuration**: Uses the `tavus-llama-4` model with speculative inference. Includes the `get_cures` tool, which accepts a single string parameter (`disease`) and limits AI behavior to relevant function calls only when disease-related queries are detected.

      * **TTS Layer**: Employs the `cartesia` voice engine with emotion control.

      - **STT Layer**: Uses `tavus-advanced` engine with smart turn detection for seamless real-time conversations.
  </Tab>

  <Tab title="Dermatologist">
    ```json [expandable] theme={null}
    {
      "persona_name": "Personal Skin Doctor",
      "pipeline_mode": "full",
      "system_prompt": "You are a friendly Personal Skin Doctor who know cures to all the disease in the world. In this call, users want to know what are the cures to the user's disease",
      "context": "User want to know what is the cure to his/her skin problem. When a user says \"What is the cure to X\" or \"What is the solution to X\", you should acknowledge their disease and use the get_skin_cures tool to return the cures of the disease's cures based on user request",
      "default_replica_id":"r18e9aebdc33",
      "layers": {
        "tts": {
          "tts_engine": "cartesia",
          "tts_emotion_control": true,
        },
        "llm": {
          "tools": [
            {
              "type": "function",
              "function": {
                "name": "get_skin_cures",
                "parameters": {
                  "type": "object",
                  "required": ["disease"],
                  "properties": {
                    "disease": {
                      "type": "string",
                      "description": "The disease which the user wanted to know how to cure"
                    }
                  }
                },
                "description": "Record the user's disease"
              }
            }
          ],
          "model": "tavus-llama-4",
          "speculative_inference": true
        },
        "perception": {
          "perception_model": "raven-0",
          "ambient_awareness_queries": [
            "Is the user have an acne in his or her face?",
            "Does the user appear distressed or uncomfortable?"
          ],
          "perception_tool_prompt": "You have a tool to notify the system when an acne is detected on user face, named `acne_detected`. You MUST use this tool when an acne is detected on user face.",
          "perception_tools": [
            {
              "type": "function",
              "function": {
                "name": "acne_detected",
                "description": "Use this function when acne is detected in the image with high confidence",
                "parameters": {
                  "type": "object",
                  "properties": {
                    "have_acne": {
                      "type": "boolean",
                      "description": "is acne detected on user's face?"
                    }
                  },
                  "required": [
                    "have_acne"
                  ]
                }
              }
            }
          ]
        },
        "stt": {
          "participant_pause_sensitivity": "high",
          "participant_interrupt_sensitivity": "high",
          "smart_turn_detection": true,
        }
      }
    }
    ```

    This predefined persona acts as a virtual skin care specialist. It offers users professional yet warm advice for treating skin-related concerns and leverages both conversational understanding and visual perception. It includes:

    * **Persona Identity**: A friendly and knowledgeable "Personal Skin Doctor" who helps users find cures for skin conditions.

    * **Full Pipeline Mode**: Enables the full Tavus conversational pipeline, including Perception, STT, LLM, and TTS.

    * **System Prompt**: Directs the persona to behave like a helpful skin doctor, answering cure-related questions clearly and empathetically.

    * **Context**: Guides the persona to respond when users ask questions like “What is the cure to X” or “What is the solution to X.” The AI is instructed to extract the disease name and call the `get_skin_cures` tool to fetch a relevant response.

    * **Model Layers**

      * **LLM Configuration**: Uses the `tavus-llama-4` model with speculative inference. Includes the `get_skin_cures` function, which takes a `disease` input to provide specific treatment guidance.

      * **Perception Configuration**:

        Integrates the `raven-0` model to visually assess the user’s face. It runs ambient queries like:

        * “Does the user have acne on their face?”
        * “Does the user appear distressed or uncomfortable?”

        If acne is detected, the persona is instructed to use the `acne_detected` tool, which reports visual findings using a boolean `have_acne` parameter.

      * **TTS Layer**: Employs the `cartesia` voice engine with emotion control.

      - **STT Layer**: Uses `tavus-advanced` engine with smart turn detection for seamless real-time conversations.
  </Tab>
</Tabs>

## Create a Conversation with the Health Care Consultant

<Steps>
  <Step title="Step 1: Create a Persona">
    Create the Health Care persona using the following request:

    <CodeGroup>
      ```shell General Doctor [expandable] theme={null}
      curl --request POST \
        --url https://tavusapi.com/v2/personas \
        --header 'Content-Type: application/json' \
        --header 'x-api-key: <api-key>' \
        --data '{
          "persona_name": "Personal Doctor",
          "pipeline_mode": "full",
          "system_prompt": "You are a friendly Personal Doctor who knows cures to all diseases. In this call, users want to know the cure for their illness.",
          "context": "Users may ask questions like \"What is the cure to X?\" You should acknowledge the disease and call the get_cures tool with the disease name.",
          "layers": {
            "tts": {
              "tts_engine": "cartesia",
              "tts_emotion_control": true
            },
            "llm": {
              "tools": [
                {
                  "type": "function",
                  "function": {
                    "name": "get_cures",
                    "description": "Fetch cures for the specified disease.",
                    "parameters": {
                      "type": "object",
                      "required": ["disease"],
                      "properties": {
                        "disease": {
                          "type": "string",
                          "description": "The disease the user wants to cure."
                        }
                      }
                    }
                  }
                }
              ],
              "model": "tavus-llama-4",
              "speculative_inference": true
            },
            "stt": {
              "participant_pause_sensitivity": "high",
              "participant_interrupt_sensitivity": "high",
              "smart_turn_detection": true
            }
          }
        }'

      ```

      ```shell Dermatologist [expandable] theme={null}
      curl --request POST \
        --url https://tavusapi.com/v2/personas \
        --header 'Content-Type: application/json' \
        --header 'x-api-key: <api-key>' \
        --data '{
          "persona_name": "Personal Skin Doctor",
          "pipeline_mode": "full",
          "system_prompt": "You are a friendly Personal Skin Doctor who know cures to all the disease in the world. In this call, users want to know what are the cures to the user's disease",
          "context": "User want to know what is the cure to his/her skin problem. When a user says \"What is the cure to X\" or \"What is the solution to X\", you should acknowledge their disease and use the get_skin_cures tool to return the cures of the disease's cures based on user request",
          "layers": {
            "tts": {
              "tts_engine": "cartesia",
              "tts_emotion_control": true,
            },
            "llm": {
              "tools": [
                {
                  "type": "function",
                  "function": {
                    "name": "get_skin_cures",
                    "parameters": {
                      "type": "object",
                      "required": ["disease"],
                      "properties": {
                        "disease": {
                          "type": "string",
                          "description": "The disease which the user wanted to know how to cure"
                        }
                      }
                    },
                    "description": "Record the user's disease"
                  }
                }
              ],
              "model": "tavus-llama-4",
              "speculative_inference": true
            },
            "perception": {
              "perception_model": "raven-0",
              "ambient_awareness_queries": [
                "Is the user have an acne in his or her face?",
                "Does the user appear distressed or uncomfortable?"
              ],
              "perception_tool_prompt": "You have a tool to notify the system when an acne is detected on user face, named `acne_detected`. You MUST use this tool when an acne is detected on user face.",
              "perception_tools": [
                {
                  "type": "function",
                  "function": {
                    "name": "acne_detected",
                    "description": "Use this function when acne is detected in the image with high confidence",
                    "parameters": {
                      "type": "object",
                      "properties": {
                        "have_acne": {
                          "type": "boolean",
                          "description": "is acne detected on user's face?"
                        }
                      },
                      "required": [
                        "have_acne"
                      ]
                    }
                  }
                }
              ]
            },
            "stt": {
              "participant_pause_sensitivity": "high",
              "participant_interrupt_sensitivity": "high",
              "smart_turn_detection": true,
            }
          }
        }'

      ```
    </CodeGroup>

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Create a Conversation">
    Create a conversation using the following request:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "<health_care_persona_id>"
    }'
    ```

    <Note>
      * Replace `<api_key>` with your actual API key.
      * Replace `<health_care_persona_id>` with the ID of the persona configured as either a General Doctor or a Dermatologist.
    </Note>
  </Step>

  <Step title="Step 3: Join the Conversation">
    Click the link in the ***`conversation_url`*** field to join the conversation:

    ```json  theme={null}
    {
      "conversation_id": "c7f3fc6d799f",
      "conversation_name": "New Conversation 1747719531479",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "",
      "created_at": "2025-05-20T05:38:51.501467Z"
    }
    ```
  </Step>
</Steps>
