# optuna.pruners.SuccessiveHalvingPruner

class optuna.pruners.SuccessiveHalvingPruner(*min_resource='auto'*, *reduction_factor=4*, *min_early_stopping_rate=0*, *bootstrap_count=0*)

Pruner using Asynchronous Successive Halving Algorithm.

Successive Halving [https://proceedings.mlr.press/v51/jamieson16.html] is a bandit-based
algorithm to identify the best one among multiple configurations. This class implements an
asynchronous version of Successive Halving. Please refer to the paper of
Asynchronous Successive Halving [https://proceedings.mlsys.org/paper_files/paper/2020/file/a06f20b349c6cf09a6b171c71b88bbfc-Paper.pdf] for detailed descriptions.

Note that, this class does not take care of the parameter for the maximum
resource, referred to as \(R\) in the paper. The maximum resource allocated to a trial is
typically limited inside the objective function (e.g., `step` number in simple_pruning.py [https://github.com/optuna/optuna-examples/blob/main/basic/pruning.py],
`EPOCH` number in chainer_integration.py [https://github.com/optuna/optuna-examples/tree/main/chainer/chainer_integration.py#L73]).

See also

Please refer to `report()`.