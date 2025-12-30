# Source: https://ml-explore.github.io/mlx/build/html/python/distributed.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/python/distributed.rst "Download source file")
- [ ] [.pdf]

[ ]

# Distributed Communication

[]

# Distributed Communication[\#](#distributed-communication "Link to this heading")

MLX provides a distributed communication package using MPI. The MPI library is loaded at runtime; if MPI is available then distributed communication is also made available.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`Group`]](_autosummary/mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group")                                                  An [[`mlx.core.distributed.Group`]](_autosummary/mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group") represents a group of independent mlx processes that can communicate.
  [[`is_available`]](_autosummary/mlx.core.distributed.is_available.html#mlx.core.distributed.is_available "mlx.core.distributed.is_available")(\[backend\])         Check if a communication backend is available.
  [[`init`]](_autosummary/mlx.core.distributed.init.html#mlx.core.distributed.init "mlx.core.distributed.init")(\[strict, backend\])                                 Initialize the communication backend and create the global communication group.
  [[`all_sum`]](_autosummary/mlx.core.distributed.all_sum.html#mlx.core.distributed.all_sum "mlx.core.distributed.all_sum")(x, \*\[, group, stream\])                All reduce sum.
  [[`all_gather`]](_autosummary/mlx.core.distributed.all_gather.html#mlx.core.distributed.all_gather "mlx.core.distributed.all_gather")(x, \*\[, group, stream\])    Gather arrays from all processes.
  [[`send`]](_autosummary/mlx.core.distributed.send.html#mlx.core.distributed.send "mlx.core.distributed.send")(x, dst, \*\[, group, stream\])                       Send an array from the current process to the process that has rank [`dst`] in the group.
  [[`recv`]](_autosummary/mlx.core.distributed.recv.html#mlx.core.distributed.recv "mlx.core.distributed.recv")(shape, dtype, src, \*\[, group, stream\])            Recv an array with shape [`shape`] and dtype [`dtype`] from process with rank [`src`].
  [[`recv_like`]](_autosummary/mlx.core.distributed.recv_like.html#mlx.core.distributed.recv_like "mlx.core.distributed.recv_like")(x, src, \*\[, group, stream\])   Recv an array with shape and type like [`x`] from process with rank [`src`].
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[](_autosummary/mlx.optimizers.clip_grad_norm.html "previous page")

previous

mlx.optimizers.clip_grad_norm

[](_autosummary/mlx.core.distributed.Group.html "next page")

next

mlx.core.distributed.Group

By MLX Contributors

© Copyright 2023, Apple.\