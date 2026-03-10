# Essay:
{insert essay text here}
```

</details>

#### Strategies we used:
- **JSON output**: For facilitating downstream tasks, JSON format output is frequently preferred. We can enable the JSON mode by setting the response_format to `{"type": "json_object"}` and specify in the prompt that "You will only respond with a JSON object with the key Summary and Confidence." Specifying these keys within the JSON object is beneficial for clarity and consistency.
- **Higher Temperature**: In this example, we increase the temperature score to encourage the model to be more creative and output three generated summaries that are different from each other.

### Introduce an evaluation step
We can also add a second step in the prompt for evaluation. We ask the LLM to generate three summaries and evaluate these three summaries. 

<table class="prompt-example">
    <tr>
        <td>Assistant</td>
        <td>

```
Summary 1: The essay discusses the author's experiences with writing and programming before college, his initial struggles with learning Fortran on an IBM 1401, and the shift towards microcomputers that led to his interest in AI. He also touches on his decision to pursue a degree in AI and the disillusionment he felt when he realized that AI as practiced at the time was a hoax.

Summary 2: The author tells the story of his journey into programming, starting with writing short stories before discovering the world of computers. He describes his early experiences with an IBM 1401 and how it was like a mini Bond villain's lair. He also talks about his fascination with microcomputers and how it led him to learn Lisp and become interested in AI. However, he eventually became disillusioned with AI and decided to focus on Lisp instead.

Summary 3: The essay recounts the author's experiences with writing and programming before college, including his early attempts at writing short stories and his struggles with learning to program on an IBM 1401. He discusses how the arrival of microcomputers changed everything and sparked his interest in AI. However, he eventually realized that AI, as practiced at the time, was a hoax, and he turned his attention to Lisp. He also touches on his decision to pursue a degree in AI despite his disillusionment with the field.

Evaluation: I believe that Summary 1 is the best summary because it provides a clear and concise overview of the author's experiences with writing and programming before college, the shift towards microcomputers, and his eventual disillusionment with AI. It covers the key points of the essay without getting bogged down in unnecessary details. Summary 2 is also good, but it focuses more on the author's early experiences with computers and less on his later experiences with AI. Summary 3 is the weakest summary because it does not capture the full scope of the author's experiences and does not mention his decision to pursue a degree in AI despite his disillusionment with the field.
```

</td>
    </tr>
</table>

<details>
<summary><b>Prompt</b></summary>

```
You are given an essay text and need to provide summaries and evaluate them.