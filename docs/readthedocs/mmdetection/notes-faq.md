# Frequently Asked Questions

We list some common troubles faced by many users and their corresponding solutions here. Feel free to enrich the list if you find any frequent issues and have ways to help others to solve them. If the contents here do not cover your issue, please create an issue using the provided templates [https://github.com/open-mmlab/mmdetection/blob/main/.github/ISSUE_TEMPLATE/error-report.md/] and make sure you fill in all required information in the template.

## PyTorch 2.0 Support

The vast majority of algorithms in MMDetection now support PyTorch 2.0 and its `torch.compile` function. Users only need to install MMDetection 3.0.0rc7 or later versions to enjoy this feature. If any unsupported algorithms are found during use, please feel free to give us feedback. We also welcome contributions from the community to benchmark the speed improvement brought by using the `torch.compile` function.

To enable the `torch.compile` function, simply add `--cfg-options compile=True` after `train.py` or `test.py`. For example, to enable `torch.compile` for RTMDet, you can use the following command:

```
# Single GPU
python tools/train.py configs/rtmdet/rtmdet_s_8xb32-300e_coco.py  --cfg-options compile=True

# Single node multiple GPUs
./tools/dist_train.sh configs/rtmdet/rtmdet_s_8xb32-300e_coco.py 8 --cfg-options compile=True

# Single node multiple GPUs + AMP
./tools/dist_train.sh configs/rtmdet/rtmdet_s_8xb32-300e_coco.py 8 --cfg-options compile=True --amp

```