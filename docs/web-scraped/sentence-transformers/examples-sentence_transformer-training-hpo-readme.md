# Source: https://www.sbert.net/examples/sentence_transformer/training/hpo/README.html

# Hyperparameter Optimization[ïƒ?](#hyperparameter-optimization "Link to this heading")

The [[`SentenceTransformerTrainer`]](../../../../docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer") supports hyperparameter optimization using [`transformers`], which in turn supports four hyperparameter search backends: [optuna](https://optuna.org/), [sigopt](https://sigopt.org/), [raytune](https://docs.ray.io/en/latest/tune/index.html), and [wandb](https://wandb.ai/site/sweeps). You should install your backend of choice before using it:

    pip install optuna/sigopt/wandb/ray[tune]

On this page, weâ€™ll show you how to use the hyperparameter optimization feature with the optuna backend. The other backends are similar to use, but you should refer to their respective documentation or the [transformers HPO documentation](https://huggingface.co/docs/transformers/en/hpo_train) for more information.

## HPO Components[ïƒ?](#hpo-components "Link to this heading")

The hyperparameter optimization process consists of the following components:

[](#hyperparameter-search-space)

Hyperparameter Search Space

Specify ranges for hyperparameter values. [](#model-initialization)

Model Initialization

Initialize a SentenceTransformer model for a trial. [](#loss-initialization)

Loss Initialization

Initialize a loss function given a model. [](#compute-objective)

Compute Objective

Determines the value to be minimized or maximized.

\

### Hyperparameter Search Space[ïƒ?](#hyperparameter-search-space "Link to this heading")

The hyperparameter search space is defined by a function that returns a dictionary of hyperparameters and their respective search spaces. Hereâ€™s an example using [`optuna`] of a search space function that defines the hyperparameters for a SentenceTransformer model:

    def hpo_search_space(trial):
        return 

### Model Initialization[ïƒ?](#model-initialization "Link to this heading")

The model initialization function is a function that takes the hyperparameters of the current â€œtrialâ€? as input and returns a SentenceTransformer model. Generally, this function is quite simple. Hereâ€™s an example of a model initialization function:

    def hpo_model_init(trial):
        return SentenceTransformer("distilbert-base-uncased")

### Loss Initialization[ïƒ?](#loss-initialization "Link to this heading")

The loss initialization function is a function that takes the model initialized for the current trial and returns a loss function. Hereâ€™s an example of a loss initialization function:

    def hpo_loss_init(model):
        return losses.CosineSimilarityLoss(model)

### Compute Objective[ïƒ?](#compute-objective "Link to this heading")

The compute objective function is a function that takes the evaluation [`metrics`] and returns the float value to be minimized or maximized. Hereâ€™s an example of a compute objective function:

    def hpo_compute_objective(metrics):
        return metrics["eval_sts-dev_spearman_cosine"]

## Putting It All Together[ïƒ?](#putting-it-all-together "Link to this heading")

You can perform HPO on any regular training loop, the only difference being that you donâ€™t call [[`SentenceTransformerTrainer.train`]](../../../../docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer.train "sentence_transformers.trainer.SentenceTransformerTrainer.train"), but [[`SentenceTransformerTrainer.hyperparameter_search`]](../../../../docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer.hyperparameter_search "sentence_transformers.trainer.SentenceTransformerTrainer.hyperparameter_search") instead. Hereâ€™s an example of how to put it all together:

Documentation

1.  [sentence-transformers/all-nli](https://huggingface.co/datasets/sentence-transformers/all-nli)

2.  [[`EmbeddingSimilarityEvaluator`]](../../../../docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator "sentence_transformers.evaluation.EmbeddingSimilarityEvaluator")

3.  [Hyperparameter Search Space](#hyperparameter-search-space)

4.  [Model Initialization](#model-initialization)

5.  [Loss Initialization](#loss-initialization)

6.  [Compute Objective](#compute-objective)

7.  [[`SentenceTransformerTrainingArguments`]](../../../../docs/package_reference/sentence_transformer/training_args.html#sentence_transformers.training_args.SentenceTransformerTrainingArguments "sentence_transformers.training_args.SentenceTransformerTrainingArguments")

8.  [[`SentenceTransformerTrainer`]](../../../../docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer "sentence_transformers.trainer.SentenceTransformerTrainer")

9.  [[`hyperparameter_search()`]](../../../../docs/package_reference/sentence_transformer/trainer.html#sentence_transformers.trainer.SentenceTransformerTrainer.hyperparameter_search "sentence_transformers.trainer.SentenceTransformerTrainer.hyperparameter_search")

    from sentence_transformers import losses
    from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer, SentenceTransformerTrainingArguments
    from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator, SimilarityFunction
    from sentence_transformers.training_args import BatchSamplers
    from datasets import load_dataset

    # 1. Load the AllNLI dataset: https://huggingface.co/datasets/sentence-transformers/all-nli, only 10k train and 1k dev
    train_dataset = load_dataset("sentence-transformers/all-nli", "triplet", split="train[:10000]")
    eval_dataset = load_dataset("sentence-transformers/all-nli", "triplet", split="dev[:1000]")

    # 2. Create an evaluator to perform useful HPO
    stsb_eval_dataset = load_dataset("sentence-transformers/stsb", split="validation")
    dev_evaluator = EmbeddingSimilarityEvaluator(
        sentences1=stsb_eval_dataset["sentence1"],
        sentences2=stsb_eval_dataset["sentence2"],
        scores=stsb_eval_dataset["score"],
        main_similarity=SimilarityFunction.COSINE,
        name="sts-dev",
    )

    # 3. Define the Hyperparameter Search Space
    def hpo_search_space(trial):
        return 

    # 4. Define the Model Initialization
    def hpo_model_init(trial):
        return SentenceTransformer("distilbert-base-uncased")

    # 5. Define the Loss Initialization
    def hpo_loss_init(model):
        return losses.MultipleNegativesRankingLoss(model)

    # 6. Define the Objective Function
    def hpo_compute_objective(metrics):
        """
        Valid keys are: 'eval_loss', 'eval_sts-dev_pearson_cosine', 'eval_sts-dev_spearman_cosine',
        'eval_sts-dev_pearson_manhattan', 'eval_sts-dev_spearman_manhattan', 'eval_sts-dev_pearson_euclidean',
        'eval_sts-dev_spearman_euclidean', 'eval_sts-dev_pearson_dot', 'eval_sts-dev_spearman_dot',
        'eval_sts-dev_pearson_max', 'eval_sts-dev_spearman_max', 'eval_runtime', 'eval_samples_per_second',
        'eval_steps_per_second', 'epoch'

        due to the evaluator that we're using.
        """
        return metrics["eval_sts-dev_spearman_cosine"]

    # 7. Define the training arguments
    args = SentenceTransformerTrainingArguments(
        # Required parameter:
        output_dir="checkpoints",
        # Optional training parameters:
        # max_steps=10000, # We might want to limit the number of steps for HPO
        fp16=True,  # Set to False if you get an error that your GPU can't run on FP16
        bf16=False,  # Set to True if you have a GPU that supports BF16
        batch_sampler=BatchSamplers.NO_DUPLICATES,  # MultipleNegativesRankingLoss benefits from no duplicate samples in a batch
        # Optional tracking/debugging parameters:
        eval_strategy="no", # We don't need to evaluate/save during HPO
        save_strategy="no",
        logging_steps=10,
        run_name="hpo",  # Will be used in W&B if `wandb` is installed
    )

    # 8. Create the trainer with model_init rather than model
    trainer = SentenceTransformerTrainer(
        model=None,
        args=args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        evaluator=dev_evaluator,
        model_init=hpo_model_init,
        loss=hpo_loss_init,
    )

    # 9. Perform the HPO
    best_trial = trainer.hyperparameter_search(
        hp_space=hpo_search_space,
        compute_objective=hpo_compute_objective,
        n_trials=20,
        direction="maximize",
        backend="optuna",
    )
    print(best_trial)

    [I 2024-05-17 15:10:47,844] Trial 0 finished with value: 0.7889856589698055 and parameters: . Best is trial 0 with value: 0.7889856589698055.
    [I 2024-05-17 15:12:13,283] Trial 1 finished with value: 0.7927780672090986 and parameters: . Best is trial 1 with value: 0.7927780672090986.
    [I 2024-05-17 15:12:43,896] Trial 2 finished with value: 0.7684829743509601 and parameters: . Best is trial 1 with value: 0.7927780672090986.
    [I 2024-05-17 15:14:49,730] Trial 3 finished with value: 0.7873032743147989 and parameters: . Best is trial 1 with value: 0.7927780672090986.
    [I 2024-05-17 15:15:39,597] Trial 4 finished with value: 0.7759251781929949 and parameters: . Best is trial 1 with value: 0.7927780672090986.
    [I 2024-05-17 15:17:02,191] Trial 5 finished with value: 0.7964580509886684 and parameters: . Best is trial 5 with value: 0.7964580509886684.
    [I 2024-05-17 15:18:55,559] Trial 6 finished with value: 0.7901878917859169 and parameters: . Best is trial 5 with value: 0.7964580509886684.
    [I 2024-05-17 15:20:27,027] Trial 7 finished with value: 0.7935671067660925 and parameters: . Best is trial 5 with value: 0.7964580509886684.
    [I 2024-05-17 15:22:23,147] Trial 8 finished with value: 0.7848123114933252 and parameters: . Best is trial 5 with value: 0.7964580509886684.
    [I 2024-05-17 15:22:52,826] Trial 9 finished with value: 0.7909708416168918 and parameters: . Best is trial 5 with value: 0.7964580509886684.
    [I 2024-05-17 15:23:30,395] Trial 10 finished with value: 0.7928991732385567 and parameters: . Best is trial 5 with value: 0.7964580509886684.
    [I 2024-05-17 15:24:18,024] Trial 11 finished with value: 0.7991870087507459 and parameters: . Best is trial 11 with value: 0.7991870087507459.
    [I 2024-05-17 15:25:44,198] Trial 12 finished with value: 0.7923304174306207 and parameters: . Best is trial 11 with value: 0.7991870087507459.
    [I 2024-05-17 15:26:20,739] Trial 13 finished with value: 0.8020260244040395 and parameters: . Best is trial 13 with value: 0.8020260244040395.
    [I 2024-05-17 15:26:57,783] Trial 14 finished with value: 0.7571110256860063 and parameters: . Best is trial 13 with value: 0.8020260244040395.
    [I 2024-05-17 15:27:32,581] Trial 15 finished with value: 0.8009013936824717 and parameters: . Best is trial 13 with value: 0.8020260244040395.
    [I 2024-05-17 15:28:05,850] Trial 16 finished with value: 0.8017668050806169 and parameters: . Best is trial 13 with value: 0.8020260244040395.
    [I 2024-05-17 15:28:37,393] Trial 17 finished with value: 0.7769412380909586 and parameters: . Best is trial 13 with value: 0.8020260244040395.
    [I 2024-05-17 15:29:19,340] Trial 18 finished with value: 0.8011921300048339 and parameters: . Best is trial 13 with value: 0.8020260244040395.
    [I 2024-05-17 15:29:59,508] Trial 19 finished with value: 0.8027501854704168 and parameters: . Best is trial 19 with value: 0.8027501854704168.

    BestRun(run_id='19', objective=0.8027501854704168, hyperparameters=, run_summary=None)

As you can see, the strongest hyperparameters reached **0.802** Spearman correlation on the STS (dev) benchmark. For context, training with the default training arguments ([`per_device_train_batch_size=8`], [`learning_rate=5e-5`]) results in **0.736**, and hyperparameters chosen based on experience ([`per_device_train_batch_size=64`], [`learning_rate=2e-5`]) results in **0.783** Spearman correlation. Consequently, HPO proved quite effective here in improving the model performance.

## Example Scripts[ïƒ?](#example-scripts "Link to this heading")

- [hpo_nli.py](https://github.com/huggingface/sentence-transformers/blob/master/examples/sentence_transformer/training/hpo/hpo_nli.py) - An example script that performs hyperparameter optimization on the AllNLI dataset.