# Source: https://ml-explore.github.io/mlx/build/html/python/nn/losses.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/nn/losses.rst "Download source file")
- [ ] [.pdf]

[ ]

# Loss Functions

[]

# Loss Functions[\#](#loss-functions "Link to this heading")

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`binary_cross_entropy`]](_autosummary_functions/mlx.nn.losses.binary_cross_entropy.html#mlx.nn.losses.binary_cross_entropy "mlx.nn.losses.binary_cross_entropy")(inputs, targets\[, \...\])             Computes the binary cross entropy loss.
  [[`cosine_similarity_loss`]](_autosummary_functions/mlx.nn.losses.cosine_similarity_loss.html#mlx.nn.losses.cosine_similarity_loss "mlx.nn.losses.cosine_similarity_loss")(x1, x2\[, axis, eps, \...\])   Computes the cosine similarity between the two inputs.
  [[`cross_entropy`]](_autosummary_functions/mlx.nn.losses.cross_entropy.html#mlx.nn.losses.cross_entropy "mlx.nn.losses.cross_entropy")(logits, targets\[, weights, \...\])                                Computes the cross entropy loss.
  [[`gaussian_nll_loss`]](_autosummary_functions/mlx.nn.losses.gaussian_nll_loss.html#mlx.nn.losses.gaussian_nll_loss "mlx.nn.losses.gaussian_nll_loss")(inputs, targets, vars\[, \...\])                   Computes the negative log likelihood loss for a Gaussian distribution.
  [[`hinge_loss`]](_autosummary_functions/mlx.nn.losses.hinge_loss.html#mlx.nn.losses.hinge_loss "mlx.nn.losses.hinge_loss")(inputs, targets\[, reduction\])                                                Computes the hinge loss between inputs and targets.
  [[`huber_loss`]](_autosummary_functions/mlx.nn.losses.huber_loss.html#mlx.nn.losses.huber_loss "mlx.nn.losses.huber_loss")(inputs, targets\[, delta, reduction\])                                         Computes the Huber loss between inputs and targets.
  [[`kl_div_loss`]](_autosummary_functions/mlx.nn.losses.kl_div_loss.html#mlx.nn.losses.kl_div_loss "mlx.nn.losses.kl_div_loss")(inputs, targets\[, axis, reduction\])                                      Computes the Kullback-Leibler divergence loss.
  [[`l1_loss`]](_autosummary_functions/mlx.nn.losses.l1_loss.html#mlx.nn.losses.l1_loss "mlx.nn.losses.l1_loss")(predictions, targets\[, reduction\])                                                       Computes the L1 loss.
  [[`log_cosh_loss`]](_autosummary_functions/mlx.nn.losses.log_cosh_loss.html#mlx.nn.losses.log_cosh_loss "mlx.nn.losses.log_cosh_loss")(inputs, targets\[, reduction\])                                    Computes the log cosh loss between inputs and targets.
  [[`margin_ranking_loss`]](_autosummary_functions/mlx.nn.losses.margin_ranking_loss.html#mlx.nn.losses.margin_ranking_loss "mlx.nn.losses.margin_ranking_loss")(inputs1, inputs2, targets)                 Calculate the margin ranking loss that loss given inputs [\\(x_1\\)], [\\(x_2\\)] and a label [\\(y\\)] (containing 1 or -1).
  [[`mse_loss`]](_autosummary_functions/mlx.nn.losses.mse_loss.html#mlx.nn.losses.mse_loss "mlx.nn.losses.mse_loss")(predictions, targets\[, reduction\])                                                   Computes the mean squared error loss.
  [[`nll_loss`]](_autosummary_functions/mlx.nn.losses.nll_loss.html#mlx.nn.losses.nll_loss "mlx.nn.losses.nll_loss")(inputs, targets\[, axis, reduction\])                                                  Computes the negative log likelihood loss.
  [[`smooth_l1_loss`]](_autosummary_functions/mlx.nn.losses.smooth_l1_loss.html#mlx.nn.losses.smooth_l1_loss "mlx.nn.losses.smooth_l1_loss")(predictions, targets\[, beta, \...\])                          Computes the smooth L1 loss.
  [[`triplet_loss`]](_autosummary_functions/mlx.nn.losses.triplet_loss.html#mlx.nn.losses.triplet_loss "mlx.nn.losses.triplet_loss")(anchors, positives, negatives)                                         Computes the triplet loss for a set of anchor, positive, and negative samples.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[](_autosummary_functions/mlx.nn.tanh.html "previous page")

previous

mlx.nn.tanh

[](_autosummary_functions/mlx.nn.losses.binary_cross_entropy.html "next page")

next

mlx.nn.losses.binary_cross_entropy

By MLX Contributors

© Copyright 2023, Apple.\