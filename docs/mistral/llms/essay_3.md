# essay:
{insert essay text here}
```
</details>


- **Step 2**: use another LLM to rate the generated summaries


<table class="prompt-example">
    <tr>
        <td>Assistant</td>
        <td>

```
Summary 3 provides the most complete and accurate summary of the essay. It covers the author's experiences with writing and programming before college, their disappointment with AI in college, and their eventual focus on Lisp and work at Interleaf. Summary 1 is missing some key details, such as the author's work at Interleaf and their writing of "On Lisp". Summary 2 focuses too much on the author's time at Interleaf and neglects their early experiences with writing and programming before college. Overall, Summary 3 is the best choice as it is the most complete and accurate summary of the essay.
```

</td>
    </tr>
</table>

<details>
<summary><b>Prompt</b></summary>

```
You are given an essay and three summaries of the essay. Evaluate the three summaries and rate which one you believe is the best.
Explain your choice by pointing out specific reasons such as clarity, completeness, and relevance to the essay content.