# Customize Losses

MMDetection provides users with different loss functions. But the default configuration may be not applicable for different datasets or models, so users may want to modify a specific loss to adapt the new situation.

This tutorial first elaborate the computation pipeline of losses, then give some instructions about how to modify each step. The modification can be categorized as tweaking and weighting.

## Computation pipeline of a loss

Given the input prediction and target, as well as the weights, a loss function maps the input tensor to the final loss scalar. The mapping can be divided into five steps:

- 

Set the sampling method to sample positive and negative samples.

- 

Get **element-wise** or **sample-wise** loss by the loss kernel function.

- 

Weighting the loss with a weight tensor **element-wisely**.

- 

Reduce the loss tensor to a **scalar**.

- 

Weighting the loss with a **scalar**.