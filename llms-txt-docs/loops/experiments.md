# Source: https://loops.so/docs/loop-builder/experiments.md

# Experiments

> Learn how to use experiments to test different versions of your emails.

Experiments are a way to run split tests within loops. This lets you test different versions of your emails, allowing you to see which version performs best.

You can test things like subject lines, preheaders, and content, and specify the percentage of contacts who should be sent down each variant branch.

## Creating an experiment

To add an experiment, add a new node by clicking the `+` button in the loop builder and select **Experiment**. You can add an experiment to any loop.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-experiment.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=9878f0e7c5450dad2cbe54c4ddd6e69d" alt="Adding an experiment" data-og-width="2280" width="2280" data-og-height="1859" height="1859" data-path="images/add-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-experiment.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b3b8794926d97a190f591f40ad267173 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-experiment.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=083c18f2157bf18ae74f8e953dfba48b 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-experiment.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=29ec6be0e5ecb9643ca75bfab2cb9133 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-experiment.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ba7e00719e4b156e1007f2c51ac6aac6 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-experiment.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=9768548ee9a9f43b1bd3f81a053ba00b 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-experiment.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=042d30aac4bf18111a5053315ac1c7e7 2500w" />

You can add multiple experiments to a loop—even within other experiments if you want. Each experiment can contain any number of variants.

Each variant can contain emails, timers and audience filters.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-experiment.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=74039905794c1ca9794fcab5db39f54b" alt="Experiment with emails and filters" data-og-width="2280" width="2280" data-og-height="1859" height="1859" data-path="images/loop-experiment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-experiment.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b23d69ed39437fa2dee26b962c924cd8 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-experiment.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f15cac23950d74fea3892858224ca41d 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-experiment.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b51a3f4fdcda02a0bd857ec30a0a33bd 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-experiment.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=3e3ebe150b8c6ae0408df4325308c6ac 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-experiment.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=8e7a1e61a9ade0df84db50aca7ced121 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-experiment.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=21ec1346348006dd33a590ccbbfe9261 2500w" />

## Variants and controls

Experiments are made up of variant and control branches.

* **Variant** branches contain the email(s) you are testing, which will be sent to a specific percentage of contacts that you define.
* The **Control** branch contains the email(s) that will be sent to all contacts not included in the experiment, and should be used as the baseline for the experiment. A control is optional; you can create an experiment without a control branch.

<Tip>
  An experiment node must be followed by at least one variant or control branch, otherwise you cannot start the loop.\
  Likewise, you must add at least one email within each control or variant branch before starting the loop.
</Tip>

## Sample size

You can specify the percentage of contacts who will be sent to control and variant branches by dragging the slider in Experiment nodes.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-slider.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=3f825e8276129a9e581890fbe442bf35" alt="Changing sample size" data-og-width="2280" width="2280" data-og-height="1757" height="1757" data-path="images/experiment-slider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-slider.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=b2bd7887a6787d9999f632ea9fbe7a8e 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-slider.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=c3009af24ee0ed54a220b353e16b0791 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-slider.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=bcd13028df09e60aa95a9d0d7ee20184 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-slider.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=af1c7ea9d8178b2a0457478253c18295 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-slider.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=a3a4fd238e16d02adb5c1f225fcf041e 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-slider.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=b1ce2f87b5c1151ee0dbca14c78c03c6 2500w" />

Every variant you add will receive an equal percentage of contacts within the experiment sample. For example, if you set the sample size to 60% and add three variants and a control, 20% of contacts will be sent to each variant branch (60% / 3) and 40% of contacts will be sent to the control branch.

You can change a variant to be the control by clicking on the variant node and toggling the **Use as control** option.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/change-control.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=95aa662d27adf1f0a7030b3b060b829a" alt="Changing the control node" data-og-width="2280" width="2280" data-og-height="1683" height="1683" data-path="images/change-control.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/change-control.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6828044fa7ffd14f5dd58f56bcbd4bb8 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/change-control.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f7d04f87a4f6c9486059b826325f77ae 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/change-control.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b9a5d279e97eb6eb5b1e5f746a6c208a 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/change-control.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=14f6094c2aa353c06f03d964f4e95c17 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/change-control.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=7bb5c97821e28d8b7d2fd0509d1b1044 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/change-control.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6b84d7170bd0d87e80eedf94bea2e2a0 2500w" />

If you do not add a control branch, only your selected sample size will be sent through the experiment node. For example, if you have three variants and no control and select 60% for your sample size, 40% of contacts entering the loop will exit at the experiment node and not receive any emails.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-no-control.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=15344c1344deb2d6a4b3a4f1339174ce" alt="Experiment without a control" data-og-width="2280" width="2280" data-og-height="1716" height="1716" data-path="images/experiment-no-control.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-no-control.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=2f11ebc969c0b646a07e139215444bfc 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-no-control.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=2c27786f7e7b36312f3480f62430fde8 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-no-control.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=86c2a6f0c9fc5011330b190f957e4dcc 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-no-control.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=93518dc43262c94c822c04beb419e764 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-no-control.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=d42ad5c6c183a4b8487a49526bdc6a9a 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/experiment-no-control.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=86deae06cdac502f5d9e6e164687fcb1 2500w" />

## Editing experiments

Once you have started your loop you can edit the number of contacts passing through each variant and control by first [pausing the loop](/loop-builder/pausing-loops) from the top right of the loop builder.

Once you have paused the loop, you can change the sample size, edit your variants and controls, and update any content.

Click **Resume** to start the loop again.

<Info>
  When paused, email sending is stopped and contacts are queued behind their respective nodes as expected.\
  All contacts that were scheduled to receive an email during the pause will receive it once you resume the Loop.
</Info>

### Closing an experiment

After some time testing, you may want to close experiment branches, to send all future contacts down the your best-performing branch.

To do this while retaining the metrics for all branches, first change your best-performing branch to a control branch (click its **Use as control** toggle; see image above).

Then set the Experiment node sample size to 0%. This will change the Control size to 100%, sending all contacts down the new control branch.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/close-experiment-branch.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=4a8ff7a5a5bfdd5a28686575cf0d4699" alt="Close an experiment branch" data-og-width="2280" width="2280" data-og-height="1254" height="1254" data-path="images/close-experiment-branch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/close-experiment-branch.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d201248b3a084ea11b96baffde93e50b 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/close-experiment-branch.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=3a0e18aa4832a5ded85215f59161553a 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/close-experiment-branch.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=8470ae4f33f31543ffce724cdcfa8530 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/close-experiment-branch.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=988dfae4b2dd8da96bf90d948796abe0 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/close-experiment-branch.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=86a7ac0ee17ea06b6e94b872c76f4d10 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/close-experiment-branch.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=240d0732a8183a13e4cddeb653aff38b 2500w" />

## Results

Once your experiment is running and contacts have flowed through the loop, you can see the results by visiting the **Metrics** tab.

Here you can compare your variants and view metrics for sends, opens and clicks.
