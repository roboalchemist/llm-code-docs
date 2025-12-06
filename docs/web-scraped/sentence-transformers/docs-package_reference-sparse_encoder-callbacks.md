# Source: https://www.sbert.net/docs/package_reference/sparse_encoder/callbacks.html

# Callbacks[ïƒ?](#callbacks "Link to this heading")

## SpladeRegularizerWeightSchedulerCallback[ïƒ?](#spladeregularizerweightschedulercallback "Link to this heading")

*[class][ ]*[[sentence_transformers.sparse_encoder.callbacks.splade_callbacks.]][[SpladeRegularizerWeightSchedulerCallback]][(]*[[loss]][[:]][ ][[[SpladeLoss]](losses.html#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss.SpladeLoss")]*, *[[scheduler_type]][[:]][ ][[str][ ][[\|]][ ][SchedulerType]][ ][[=]][ ][[SchedulerType.QUADRATIC]]*, *[[warmup_ratio]][[:]][ ][[float]][ ][[=]][ ][[0.3333333333333333]]*[)][[[\[source\]]]](https://github.com/huggingface/sentence-transformers/blob/master/sentence_transformers\sparse_encoder\callbacks\splade_callbacks.py#L21-L148)[ïƒ?](#sentence_transformers.sparse_encoder.callbacks.splade_callbacks.SpladeRegularizerWeightSchedulerCallback "Link to this definition")

:   Callback that updates the query_regularizer_weight and document_regularizer_weight parameters of SpladeLoss based on a schedule.

    The scheduler gradually increases the weight values from 0 to their max value within the specified warmup ratio of the total training steps.

    Parameters[:]

    :   - **loss** ([*SpladeLoss*](losses.html#sentence_transformers.sparse_encoder.losses.SpladeLoss "sentence_transformers.sparse_encoder.losses.SpladeLoss")) â€" SpladeLoss instance to be updated

        - **scheduler_type** (*str*) â€" Type of scheduler (â€˜linearâ€™ or â€˜quadraticâ€™)

        - **warmup_ratio** (*float*) â€" Ratio of total steps to reach max weight values (default: 1/3)