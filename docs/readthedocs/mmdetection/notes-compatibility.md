# Compatibility of MMDetection 2.x

## MMDetection 2.25.0

In order to support Mask2Former for instance segmentation, the original config files of Mask2Former for panpotic segmentation need to be renamed PR #7571 [https://github.com/open-mmlab/mmdetection/pull/7571].

    
        
            before v2.25.0
            after v2.25.0
        
    
    
    

```
'mask2former_xxx_coco.py' represents config files for **panoptic segmentation**.

```