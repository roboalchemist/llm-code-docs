# Source: https://novita.ai/docs/guides/llm-playgrounds.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Interactive Playground

To help users better understand and test the behavior of large language models, **Novita** provides a flexible interactive playground. Users can fine-tune a series of parameters to precisely control the model's generation logic, content style, and response structure, enabling more targeted output.

## Response Format

Users can choose between two modes:

* **Custom JSON Output Structure**: Define a JSON Schema to guide the model in generating output that follows a predefined format, ideal for structured tasks or API integration scenarios.
* **Free-form Generation**: Allow the model to freely organize answers based on context, suitable for open-ended Q\&A and creative writing applications.

## System Prompt

By setting a system prompt, users can define the model's "persona" and behavioral context. For example, if you set the prompt as “You are a professional travel planner,” the model will respond from that perspective, enhancing consistency and contextual coherence.

## Parameter Configuration

The playground supports the adjustment of the following core parameters:

* **max\_tokens**: Sets the maximum number of tokens the model can generate. Lower values improve response speed, while higher values are suitable for complex, lengthy outputs.
* **temperature**: Controls the creativity and randomness of the output. Higher values lead to more diverse and imaginative responses, while lower values yield more conservative and deterministic outputs, ideal for precise tasks.
* **top\_p (nucleus sampling)**: Dynamically adjusts the token sampling range per step to improve diversity and fluency. Recommended to use alongside temperature.
* **top\_k**: Limits the model to select from the top K highest probability tokens at each step, which enhances efficiency and reduces noise.
* **min\_p**: An alternative to top\_p and top\_k, used to filter out tokens with probabilities below a certain threshold, suitable for accuracy-critical tasks.
* **presence\_penalty**: Encourages the model to introduce new topics in its output. Positive values increase the likelihood of expanding to new content.
* **frequency\_penalty**: Suppresses the generation of repeated tokens. Positive values reduce repetition and help maintain originality.
* **repetition\_penalty**: Further reduces the risk of loops or repetitive prompts, enhancing output robustness.

## Usage Recommendations

* **For Creative Writing**: Increase temperature, top\_p, and presence\_penalty to encourage diverse and imaginative outputs.
* **For Structured Tasks and Tool Invocation**: Use a fixed JSON schema with lower temperature and top\_k to ensure consistent and reliable outputs.
* **For Testing Interactions**: Compare different parameter combinations to observe changes in generation style, information density, and contextual understanding, aiding in faster prompt iteration.

***

To replicate the behavior from the playground in API calls, refer to the corresponding parameter documentation in the platform guide.


Built with [Mintlify](https://mintlify.com).