# Source: https://docs.fireflies.ai/schema/input/create-live-soundbite-input.md

# CreateLiveSoundbiteInput

> Schema for CreateLiveSoundbiteInput

<ParamField path="meeting_id" type="ID!" required>
  The ID of the live meeting to create the soundbite for
</ParamField>

<ParamField path="prompt" type="String!" required>
  Natural language description of the soundbite to create. Fred will interpret this prompt and create the appropriate soundbite.

  Min / max of 5 / 255 characters.
</ParamField>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireflies.ai/llms.txt