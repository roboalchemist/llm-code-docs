# Essay:
{insert essay text here}

Step 1: In this step, provide three short summaries of the given essay. Each summary should be clear, concise, and capture the key points of the speech. Aim for around 2-3 sentences for each summary.
Step 2: Evaluate the three summaries from Step 1 and rate which one you believe is the best. Explain your choice by pointing out specific reasons such as clarity, completeness, and relevance to the speech content.
```
</details>


### Employ another LLM for evaluation
In production systems, it is common to employ another LLM for evaluation so that the evaluation step can be separate from the generation summaries.

- **Step 1**: use the first LLM to generate three summaries

<table class="prompt-example">
    <tr>
        <td>Assistant</td>
        <td>

```
Summary 1: The author writes about their experiences with programming and writing before college. They started programming using Fortran on an IBM 1401 and wrote short stories. They later got into AI, but became disillusioned with it while in graduate school. The author then turned their focus to Lisp, eventually writing a book about it called "On Lisp". They also tried pursuing art, but found it difficult to make a living from it.

Summary 2: The author describes their experiences with programming in college and later in the workforce. They learned Lisp while in college, which expanded their concept of what a program could do. After graduation, the author worked at Interleaf, a company that made document creation software. They also did some consulting and writing on the side, eventually writing a book called "On Lisp". The author enjoyed working at Interleaf, but found that the Lisp they used was just a thin layer on top of a larger C cake.

Summary 3: The author tells the story of their early experiences with programming and writing. They started writing short stories before college, but they were not very good. The first programs they wrote were on an IBM 1401 using Fortran. In college, they got into AI, but found it disappointing. The author then turned their focus to Lisp, which they found to be more interesting. They also tried pursuing art, but found it difficult to make a living from it. The author eventually wrote a book called "On Lisp" and worked at Interleaf, a company that made document creation software. They enjoyed their time at Interleaf, but found that the Lisp they used was just a thin layer on top of a larger C cake.
```

</td>
    </tr>
</table>

<details>
<summary><b>Prompt</b></summary>

```
Provide three short summaries of the given essay. Each summary should be clear, concise, and capture the key points of the essay.
Aim for around 2-3 sentences for each summary.