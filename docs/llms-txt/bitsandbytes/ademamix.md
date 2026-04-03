# Source: https://huggingface.co/docs/bitsandbytes/v0.49.0/reference/optim/ademamix.md

# AdEMAMix

[AdEMAMix](https://hf.co/papers/2409.03137) is a variant of the `Adam` optimizer.

bitsandbytes also supports paged optimizers which take advantage of CUDAs unified memory to transfer memory from the GPU to the CPU when GPU memory is exhausted.

## AdEMAMix[[api-class]][[bitsandbytes.optim.AdEMAMix]]

#### bitsandbytes.optim.AdEMAMix[[bitsandbytes.optim.AdEMAMix]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L107)

__init__bitsandbytes.optim.AdEMAMix.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L108[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "optim_bits", "val": ": typing.Literal[8, 32] = 32"}, {"name": "min_8bit_size", "val": ": int = 4096"}, {"name": "is_paged", "val": ": bool = False"}]

## AdEMAMix8bit[[bitsandbytes.optim.AdEMAMix8bit]]

#### bitsandbytes.optim.AdEMAMix8bit[[bitsandbytes.optim.AdEMAMix8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L274)

__init__bitsandbytes.optim.AdEMAMix8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L275[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "min_8bit_size", "val": ": int = 4096"}, {"name": "is_paged", "val": ": bool = False"}]

## AdEMAMix32bit[[bitsandbytes.optim.AdEMAMix32bit]]

#### bitsandbytes.optim.AdEMAMix32bit[[bitsandbytes.optim.AdEMAMix32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L359)

__init__bitsandbytes.optim.AdEMAMix32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L360[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "min_8bit_size", "val": ": int = 4096"}, {"name": "is_paged", "val": ": bool = False"}]

## PagedAdEMAMix[[bitsandbytes.optim.PagedAdEMAMix]]

#### bitsandbytes.optim.PagedAdEMAMix[[bitsandbytes.optim.PagedAdEMAMix]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L330)

__init__bitsandbytes.optim.PagedAdEMAMix.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L331[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "optim_bits", "val": ": typing.Literal[8, 32] = 32"}, {"name": "min_8bit_size", "val": ": int = 4096"}]

## PagedAdEMAMix8bit[[bitsandbytes.optim.PagedAdEMAMix8bit]]

#### bitsandbytes.optim.PagedAdEMAMix8bit[[bitsandbytes.optim.PagedAdEMAMix8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L303)

__init__bitsandbytes.optim.PagedAdEMAMix8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L304[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "min_8bit_size", "val": ": int = 4096"}]

## PagedAdEMAMix32bit[[bitsandbytes.optim.PagedAdEMAMix32bit]]

#### bitsandbytes.optim.PagedAdEMAMix32bit[[bitsandbytes.optim.PagedAdEMAMix32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L392)

__init__bitsandbytes.optim.PagedAdEMAMix32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/ademamix.py#L393[{"name": "params", "val": ": Iterable"}, {"name": "lr", "val": ": float = 0.001"}, {"name": "betas", "val": ": tuple = (0.9, 0.999, 0.9999)"}, {"name": "alpha", "val": ": float = 5.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}, {"name": "eps", "val": ": float = 1e-08"}, {"name": "weight_decay", "val": ": float = 0.01"}, {"name": "min_8bit_size", "val": ": int = 4096"}]

