# Source: https://docs.openpipe.ai/features/evaluations/criterion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Criterion Evaluations

>  Evaluate your LLM outputs using criteria. 

<Note>
  Criterion evaluations are useful for evaluating your LLM outputs against a set of criteria. If you
  haven't defined any criteria yet, check out the criteria [Quick
  Start](/features/criteria/quick-start) guide.
</Note>

Criterion evaluations are a reliable way to judge the quality of your LLM outputs according to the criteria you've defined. For each model being evaluated, the output of that model is compared against the criteria you've defined for every entry in the evaluation dataset.

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-settings.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=47b136c45f57a3e0cf03fbb407be629f" alt="" data-og-width="2548" width="2548" data-og-height="1578" height="1578" data-path="images/features/evaluations/criterion-eval-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-settings.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=723584b6cee1afc18aebdc5dfb58426f 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-settings.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=b038a9c76076b1610b334bdc78b2e923 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-settings.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=4516b0f660b9f0a6e0aa4ec2b5951e32 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-settings.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=1a9c6edc6fb16869f7e92a1b242fce55 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-settings.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=765fcef0165c8383584a6ee343726b2a 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-settings.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=147c2c7e62785617fc050714dcc7f752 2500w" /></Frame>

<Info>
  A criterion evaluation is only as reliable as the criterion you've defined. To improve your
  criterion, check out the [alignment docs](/features/criteria/alignment-set).
</Info>

Each output in the evaluation dataset is compared against the criterion you've defined. The output is then scored as either `PASS` or `FAIL` based on the criterion.

<br />

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-results-table.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=9f4e723c5c8ed589c64c2432ce601d3a" alt="" data-og-width="2544" width="2544" data-og-height="974" height="974" data-path="images/features/evaluations/criterion-eval-results-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-results-table.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=45092241d06962bb47bf48a48894c047 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-results-table.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=f5a11538968e17a2703a5ad284be2d83 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-results-table.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=2eaa9842ed0120b7104fbb9ff2ed54fb 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-results-table.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=1f5a8bf04686368b786eb4bdd40f11a6 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-results-table.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=f77a33750c08227b1a8d8204f80cdcaa 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-results-table.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=3440cfb8a766ef1bc6c997b87e19b310 2500w" /></Frame>

<br />

To see why one model might be outperforming another, you can navigate back to the [evaluation table](https://app.openpipe.ai/p/BRZFEx50Pf/datasets/3e7e82c1-b066-476c-9f17-17fd85a2169b/evaluate) and click on a result pill to see the evaluation judge's reasoning.

<br />

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-explanation.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=691da15800edc8179dce1cb990e1988b" alt="" data-og-width="3022" width="3022" data-og-height="1716" height="1716" data-path="images/features/evaluations/criterion-eval-explanation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-explanation.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=14a359eb8e46dc462e1f24f42049502e 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-explanation.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=5a0d79b51563bb57a52b5b539ab88dd3 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-explanation.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=e91eb153cbb54b855856174b830b222f 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-explanation.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=3c88c684269a6158e44217b3abfadea1 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-explanation.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=ddb3bd2e67d05b0dfeda918d3b552909 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/evaluations/criterion-eval-explanation.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=88fd24dc3ec4c047c53bab05c26aadf2 2500w" /></Frame>

<br />

While criterion evaluations are powerful and flexible, they're much more expensive to run than pure code. If your models' outputs can be easily evaluated by code alone, consider using [code evaluations](/features/evaluations/code) instead.
