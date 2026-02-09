# Source: https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/rmsprop.md

# RMSprop

RMSprop is an adaptive learning rate optimizer that is very similar to `Adagrad`. RMSprop stores a *weighted average* of the squared past gradients for each parameter and uses it to scale their learning rate. This allows the learning rate to be automatically lower or higher depending on the magnitude of the gradient, and it prevents the learning rate from diminishing.

## RMSprop[[api-class]][[bitsandbytes.optim.RMSprop]]

#### bitsandbytes.optim.RMSprop[[bitsandbytes.optim.RMSprop]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/rmsprop.py#L8)

## RMSprop8bit[[bitsandbytes.optim.RMSprop8bit]]

#### bitsandbytes.optim.RMSprop8bit[[bitsandbytes.optim.RMSprop8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/rmsprop.py#L72)

## RMSprop32bit[[bitsandbytes.optim.RMSprop32bit]]

#### bitsandbytes.optim.RMSprop32bit[[bitsandbytes.optim.RMSprop32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/rmsprop.py#L135)

