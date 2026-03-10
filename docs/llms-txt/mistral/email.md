# Email
{insert customer email here}
```
</details>


#### Strategies we used:
- **Providing facts**: Incorporating facts into prompts can be useful for developing customer support bots. It's important to use clear and concise language when presenting these facts. This can help the LLM to provide accurate and quick responses to customer queries.

## Evaluation
There are many ways to evaluate LLM outputs. Here are three approaches for your reference: include a confidence score, introduce an evaluation step, or employ another LLM for evaluation.

### Include a confidence score
We can include a confidence score along with the generated output.

<table class="prompt-example">
    <tr>
        <td>Assistant</td>
        <td>

```
{
  "Summaries": [
    {
      "Summary": "The author discusses their early experiences with programming and writing, starting with writing short stories and programming on an IBM 1401 in 9th grade. They then moved on to working with microcomputers, building their own from a Heathkit, and eventually convincing their father to buy a TRS-80 in 1980. They wrote simple games, a program to predict rocket flight trajectories, and a word processor.",
      "Confidence": 0.9
    },
    {
      "Summary": "The author began college as a philosophy major, but found it to be unfulfilling and switched to AI. They were inspired by a novel and a PBS documentary, as well as the potential for AI to create intelligent machines like those in the novel. Despite this excitement, they eventually realized that the traditional approach to AI was flawed and shifted their focus to Lisp.",
      "Confidence": 0.85
    },
    {
      "Summary": "The author briefly worked at Interleaf, where they found that their Lisp skills were highly valued. They eventually left Interleaf to return to RISD, but continued to work as a freelance Lisp hacker. While at RISD, they started painting still lives in their bedroom at night, which led to them applying to art schools and eventually attending the Accademia di Belli Arti in Florence.",
      "Confidence": 0.9
    }
  ]
}
```

</td>
    </tr>
</table>


<details>
<summary><b>Prompt</b></summary>

```
You are a summarization system that can provide summaries with associated confidence scores.
In clear and concise language, provide three short summaries of the following essay, along with their confidence scores.
You will only respond with a JSON object with the key Summary and Confidence. Do not provide explanations.