# Source: https://docs.openpipe.ai/features/evaluations/head-to-head.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Head-to-Head Evaluations

>  Evaluate your LLM outputs against one another using head-to-head evaluations. 

<Note>
  Head-to-head evaluations are useful for evaluating your LLM outputs against one another to
  determine which models are generally better at a given task. However, they do not provide precise
  metrics on how often a given model makes a certain error, only how often it outperforms another
  model. For more precise metrics, please consider [criteria](/features/evaluations/criterion) or
  [code](/features/evaluations/code) evaluations.
</Note>

Head to head evaluations are a fast way to get a sense of how well your models perform against one another. For each model being evaluated, the output of that model is compared against the output of every other model for every entry in the evaluation dataset.

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-settings.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=c6723424745e09a486c4daef06cfe6da" alt="" data-og-width="2646" width="2646" data-og-height="1358" height="1358" data-path="images/features/evaluations/h2h-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-settings.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=6d25a35299f776595c67c36f032b3e72 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-settings.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=3c40a446b9fad9742339456c65bddfa6 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-settings.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=ba256f21cd1854a528aa64484f684084 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-settings.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=a03f3630e408f5051ef16631145e6d35 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-settings.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=b63d54ebbb2104db2656459794f6523a 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-settings.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=3e55e23c7b540bfff548a633d569f123 2500w" /></Frame>

<Info>
  The number of comparisons performed in a head to head eval scales linearly with the number of
  entries and quadratically with the number of models. If you're evaluating 2 models on 100 entries,
  there will be 100 \* 1 = 100 comparisons. If you're evaluating 3 models on 100 entries, there will
  be 100 \* 2 + 100 \* 1 = 300 comparisons.
</Info>

As outputs are compared against one another, each model is assigned a "win rate" score. For example, if you're evaluating 2 models on 100 entries and model A outperforms model B 55 times, model A will have a win rate of 55% and model B will have a win rate of 45%. In cases where both models produce the same output or the judge is unable to determine a winner, the score will be a tie (equivalent to 50% win rate).

<br />

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-results-table.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=501937db4075ceb497ca9b2814046c3e" alt="" data-og-width="2454" width="2454" data-og-height="446" height="446" data-path="images/features/evaluations/h2h-results-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-results-table.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=1adfc5846d96606021dfa0d827efb639 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-results-table.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=22f5a7ad4a2c80886be147a7cada77fa 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-results-table.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=a9f8ed449afc618368cfa17a21ecf930 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-results-table.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=37b2e2775d0192325bd3648c6173e4f2 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-results-table.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=2581a70e14da0e42923b52431547d0e4 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-results-table.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=4469b26cb70fdbb7bfb9bcb4a3b1f0ea 2500w" /></Frame>

<br />

In addition to the results table, you can also view results in a matrix format. This is useful for visualizing how specific models perform against one another.

<br />

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-matrix.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=6a4d6ec9858b1f4e8504c97bf284b447" alt="" data-og-width="2458" width="2458" data-og-height="1382" height="1382" data-path="images/features/evaluations/h2h-matrix.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-matrix.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=1f8eeb419eb6f02570662380cff57440 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-matrix.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=de66bf0cb944a3e3b668fae7aa44ee60 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-matrix.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=f537ac6aca9ebe7bdc9f8a24332710a3 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-matrix.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=4f7f0cbc6fdb5ed179e5de636083d61e 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-matrix.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=5a40dd47f4047c2cfb9eb10449f1aa2c 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-matrix.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=1afb59ca3ce46fdd168cc2e05c433687 2500w" /></Frame>

<br />

To see why one model might be outperforming another, you can navigate back to the [evaluation table](https://app.openpipe.ai/p/BRZFEx50Pf/datasets/3e7e82c1-b066-476c-9f17-17fd85a2169b/evaluate) and click on a result pill to see the evaluation judge's reasoning.

<br />

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-judge-explanation.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=26c36887b15184d12d0630e749c1511a" alt="" data-og-width="2994" width="2994" data-og-height="1716" height="1716" data-path="images/features/evaluations/h2h-judge-explanation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-judge-explanation.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=254a5f549a86120a4e1f76ae0b384fb1 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-judge-explanation.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=54afa8401c878667d99c20ffbfff7bea 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-judge-explanation.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=88ac2b09def6058c7c90a1479eaaf3a3 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-judge-explanation.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=eaa9e11489844bf117d5b2168ea36850 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-judge-explanation.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=38d6e6b9f06cceaac9ab5db7349b319c 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/h2h-judge-explanation.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=d4f85bf8cef61d86de7bec3db72e3c27 2500w" /></Frame>

<br />

While head-to-head evaluations are convenient, they can quickly become expensive to run, and provide limited insight into how well a model performs. For more precise metrics, consider [criterion](/features/evaluations/criterion) or [code](/features/evaluations/code) evaluations.
