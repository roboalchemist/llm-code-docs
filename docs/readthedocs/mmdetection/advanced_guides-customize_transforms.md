# Customize Data Pipelines

- 

Write a new transform in a file, e.g., in `my_pipeline.py`. It takes a dict as input and returns a dict.

```
import random
from mmcv.transforms import BaseTransform
from mmdet.registry import TRANSFORMS

@TRANSFORMS.register_module()
class MyTransform(BaseTransform):
    """Add your transform

    Args:
        p (float): Probability of shifts. Default 0.5.
    """

    def __init__(self, prob=0.5):
        self.prob = prob

    def transform(self, results):
        if random.random() > self.prob:
            results['dummy'] = True
        return results

```