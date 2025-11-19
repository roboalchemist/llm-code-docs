# Source: https://docs.tavus.io/sections/conversational-video-interface/conversation/usecases/customer-service.md

# Customer Service Agent

> Engage in real-time customer support conversations that adapt to user emotions and behavior.

## Customer Service Agent Configuration

```json [expandable] theme={null}
{
  "persona_name": "Customer Service Agent",
  "pipeline_mode": "full",
  "system_prompt": "You are a calm, helpful customer service agent. You assist users with product or service issues, and adapt based on their emotional state. Remain professional and empathetic at all times.",
  "context": "User needs support with a product or service. Listen carefully, identify the issue, and offer a helpful resolution. Monitor body language and voice tone to adapt your responses when the user appears frustrated or confused.",
  "default_replica_id":"r95fd27b5a37",
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
            "name": "resolve_customer_issue",
            "parameters": {
              "type": "object",
              "required": ["product", "issue_description", "urgency"],
              "properties": {
                "product": {
                  "type": "string",
                  "description": "The product or service the user is having trouble with"
                },
                "issue_description": {
                  "type": "string",
                  "description": "The specific problem or complaint reported by the user"
                },
                "urgency": {
                  "type": "string",
                  "enum": ["low", "medium", "high"],
                  "description": "How urgent or critical the issue is for the user"
                }
              }
            },
            "description": "Attempt to resolve the user's issue by logging the product, issue, and urgency for appropriate follow-up or resolution."
          }
        }
      ],
      "model": "tavus-llama-4",
      "speculative_inference": true
    },
    "perception": {
      "perception_model": "raven-0",
      "ambient_awareness_queries": [
        "Does the user appear frustrated or confused?",
        "Is the user sighing, fidgeting, or visibly anxious?",
        "Is the user's posture disengaged or tense?",
        "Is the user calm and cooperative?"
      ],
      "perception_tool_prompt": "Use the `user_emotional_state` tool when body language or facial expressions indicate a strong emotional state such as frustration, confusion, or calmness.",
      "perception_tools": [
        {
          "type": "function",
          "function": {
            "name": "user_emotional_state",
            "description": "Use this function to report the user's emotional state as inferred from body language and voice tone.",
            "parameters": {
              "type": "object",
              "required": ["emotional_state", "indicator"],
              "properties": {
                "emotional_state": {
                  "type": "string",
                  "description": "Inferred emotion from the user's body language (e.g., frustrated, calm, confused)"
                },
                "indicator": {
                  "type": "string",
                  "description": "The visual behavior that triggered the inference (e.g., furrowed brow, fidgeting, sighing)"
                }
              }
            }
          }
        }
      ]
    },
    "stt": {
      "participant_pause_sensitivity": "medium",
      "participant_interrupt_sensitivity": "high",
      "smart_turn_detection": true
    }
  }
}
```

This predefined persona is configured to provide personalized history lessons. It includes:

* **Persona Identity**: A professional customer service agent that helps users with real product or service issues. The agent speaks clearly and responds with empathy, adjusting based on how the user sounds or looks.

- **Full Pipeline Mode**: Enables the full Tavus conversational pipeline, including Perception, STT, LLM, and TTS.

* **System Prompt**: Tells the agent to act professionally and respond helpfully, while being aware of the user’s emotional state.
* **Context**: Describes a real customer support situation. The agent listens to the user’s issue, helps resolve it, and changes its tone or pace if the user seems frustrated or confused.
* **Persona Layer**:
  * **LLM Layer**: Uses the `resolve_customer_issue` tool to gather:
    * `product`: what the issue is about
    * `issue_description`: a short explanation of the problem
    * `urgency`: how serious the issue is (`low`, `medium`, or `high`)
  * **Perception Layer**: Uses the `raven-0` model to watch for signs like fidgeting, slouching, or facial expressions. If the user appears upset, it calls the `user_emotional_state` tool with:
    * `emotional_state`: what the user seems to feel (e.g., frustrated, calm)
    * `indicator`: what was observed (e.g., sighing, avoiding eye contact)
  * **TTS Layer**: Employs the `cartesia` voice engine with emotion control.
  * **STT Layer**: Uses `tavus-advanced` engine with smart turn detection for seamless real-time conversations.

## Create a Conversation with the Customer Service Agent Persona

<Steps>
  <Step title="Step 1: Create a Persona">
    Create AI Interviewer persona using the following request:

    ```sh cURL [expandable] theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/personas \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api-key>' \
      --data '{
        "persona_name": "Customer Service Agent",
        "pipeline_mode": "full",
        "system_prompt": "You are a calm, helpful customer service agent. You assist users with product or service issues, and adapt based on their emotional state. Remain professional and empathetic at all times.",
        "context": "User needs support with a product or service. Listen carefully, identify the issue, and offer a helpful resolution. Monitor body language and voice tone to adapt your responses when the user appears frustrated or confused.",
        "default_replica_id": "r95fd27b5a37",
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
                  "name": "resolve_customer_issue",
                  "description": "Attempt to resolve the user'\''s issue by logging the product, issue, and urgency for appropriate follow-up or resolution.",
                  "parameters": {
                    "type": "object",
                    "required": ["product", "issue_description", "urgency"],
                    "properties": {
                      "product": {
                        "type": "string",
                        "description": "The product or service the user is having trouble with"
                      },
                      "issue_description": {
                        "type": "string",
                        "description": "The specific problem or complaint reported by the user"
                      },
                      "urgency": {
                        "type": "string",
                        "enum": ["low", "medium", "high"],
                        "description": "How urgent or critical the issue is for the user"
                      }
                    }
                  }
                }
              }
            ],
            "model": "tavus-llama-4",
            "speculative_inference": true
          },
          "perception": {
            "perception_model": "raven-0",
            "ambient_awareness_queries": [
              "Does the user appear frustrated or confused?",
              "Is the user sighing, fidgeting, or visibly anxious?",
              "Is the user's posture disengaged or tense?",
              "Is the user calm and cooperative?"
            ],
            "perception_tool_prompt": "Use the `user_emotional_state` tool when body language or facial expressions indicate a strong emotional state such as frustration, confusion, or calmness.",
            "perception_tools": [
              {
                "type": "function",
                "function": {
                  "name": "user_emotional_state",
                  "description": "Use this function to report the user's emotional state as inferred from body language and voice tone.",
                  "parameters": {
                    "type": "object",
                    "required": ["emotional_state", "indicator"],
                    "properties": {
                      "emotional_state": {
                        "type": "string",
                        "description": "Inferred emotion from the user's body language (e.g., frustrated, calm, confused)"
                      },
                      "indicator": {
                        "type": "string",
                        "description": "The visual behavior that triggered the inference (e.g., furrowed brow, fidgeting, sighing)"
                      }
                    }
                  }
                }
              }
            ]
          },
          "stt": {
            "participant_pause_sensitivity": "medium",
            "participant_interrupt_sensitivity": "high",
            "smart_turn_detection": true
          }
        }
      }'
    ```

    <Note>
      Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
    </Note>
  </Step>

  <Step title="Step 2: Create a Conversation">
    Use the following request body example:

    ```shell cURL theme={null}
    curl --request POST \
      --url https://tavusapi.com/v2/conversations \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: <api_key>' \
      --data '{
      "persona_id": "<customer_service_persona_id>"
    }'
    ```

    <Note>
      * Replace `<api_key>` with your actual API key.
      * Replace `<customer_service_persona_id>` with the ID of the persona you created using the Customer Service Agent configuration.
    </Note>
  </Step>

  <Step title="Step 3: Join the Conversation">
    Click the link in the ***`conversation_url`*** field to join the conversation:

    ```json  theme={null}
    {
      "conversation_id": "c7f3fc6d766f",
      "conversation_name": "New Conversation 1747719531479",
      "conversation_url": "<conversation_link>",
      "status": "active",
      "callback_url": "",
      "created_at": "2025-05-20T05:38:51.501467Z"
    }
    ```
  </Step>
</Steps>
