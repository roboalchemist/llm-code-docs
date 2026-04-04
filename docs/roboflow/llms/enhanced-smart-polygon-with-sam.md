# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/ai-labeling/enhanced-smart-polygon-with-sam.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/ai-labeling/enhanced-smart-polygon-with-sam.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/ai-labeling/enhanced-smart-polygon-with-sam.md

# Source: https://docs.roboflow.com/annotate/ai-labeling/enhanced-smart-polygon-with-sam.md

# Smart Polygon

{% hint style="info" %}
Smart Polygon is one of many [AI Labeling](https://docs.roboflow.com/annotate/ai-labeling) features. Using this feature will consume [credits](https://docs.roboflow.com/billing/credits) at the rates listed on our [credits page](https://roboflow.com/credits).
{% endhint %}

Roboflow offers a Smart Polygon experience powered by [Segment Anything (SAM)](https://blog.roboflow.com/segment-anything-breakdown/), a state-of-the-art image segmentation model. To use SAM, enable Smart Polygon in Roboflow Annotate from the annotation tool sidebar:

<figure><img src="https://lh3.googleusercontent.com/CddPzMPkYVHhe2IWrGIs6VlVmbTtwcAU1-1duKdTj03cKQTxwwSIGEp4xOffbJrxH_hzkJiZz_b4l6G1qE_lH-wl6LTe5JVn8jne7ZVRzd2YeJ2ymVeeNA8nd7tozKjCt6qDpOPO4_ljM_PwgT5Xw48" alt="" height="217" width="234"><figcaption></figcaption></figure>

Select "Enhanced" from the pop up that asks what Smart Polygon mode you want to enable:

<figure><img src="https://blog.roboflow.com/content/images/2023/04/Screenshot-2023-04-13-at-9.18.59-AM-1.png" alt="" width="375"><figcaption></figcaption></figure>

Smart Polygon is now running SAM in the browser. You’ll notice you can hover over objects and see a preview of the mask that will be generated with your initial click. These previews help save time because you can see masks before you apply them and navigate the image to find the best initial mask to create.

{% embed url="<https://blog.roboflow.com/content/media/2023/04/Untitled--9-.mp4>" %}

When you create an initial mask, you'll be able to select the complexity of your polygon (toggle between them to see the difference!) and then accept the initial mask by pressing Enter.

You can interactively edit the initial mask by clicking outside of the mask to expand the mask, or click inside the mask where it may have included more than your desired object.

{% embed url="<https://blog.roboflow.com/content/media/2023/04/Untitled--15-.mp4>" %}

For larger objects or objects where masks aren’t created properly in one click, you can click and drag to draw a box around the full object. The method you use depends on your data so experiment with what works best for you.
