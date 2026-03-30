**We provide lots of useful tools under the `tools/` directory.**

# MOT Test-time Parameter Search

`tools/analysis_tools/mot/mot_param_search.py` can search the parameters of the `tracker` in MOT models.
It is used as the same manner with `tools/test.py` but **different** in the configs.

Here is an example that shows how to modify the configs:

- 

Define the desirable evaluation metrics to record.

For example, you can define the `evaluator` as

```
test_evaluator=dict(type='MOTChallengeMetrics', metric=['HOTA', 'CLEAR', 'Identity'])

```