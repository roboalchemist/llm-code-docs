# Source: https://docs.wandb.ai/models/integrations/xgboost.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Integrate W&B with XGBoost to log gradient boosting metrics, feature importance, and model performance automatically.

# XGBoost

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

<ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/boosting/Credit_Scorecards_with_XGBoost_and_W%26B.ipynb" />

The `wandb` library has a `WandbCallback` callback for logging metrics, configs and saved boosters from training with XGBoost. Here you can see a [live W\&B Dashboard](https://wandb.ai/morg/credit_scorecard) with outputs from the XGBoost `WandbCallback`.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/w-lBKSCruauC3-2f/images/integrations/xgb_dashboard.png?fit=max&auto=format&n=w-lBKSCruauC3-2f&q=85&s=5a8652cd442eeb41733d541a934f733b" alt="W&B Dashboard using XGBoost" width="2756" height="1430" data-path="images/integrations/xgb_dashboard.png" />
</Frame>

## Get started

Logging XGBoost metrics, configs and booster models to W\&B is as easy as passing the `WandbCallback` to XGBoost:

```python  theme={null}
from wandb.integration.xgboost import WandbCallback
import xgboost as XGBClassifier

...
# Start a wandb run
with wandb.init() as run:
  # Pass WandbCallback to the model
  bst = XGBClassifier()
  bst.fit(X_train, y_train, callbacks=[WandbCallback(log_model=True)])
```

You can open [this notebook](https://wandb.me/xgboost) for a comprehensive look at logging with XGBoost and W\&B

## `WandbCallback` reference

### Functionality

Passing `WandbCallback` to a XGBoost model will:

* log the booster model configuration to W\&B
* log evaluation metrics collected by XGBoost, such as rmse, accuracy etc to W\&B
* log training metrics collected by XGBoost (if you provide data to eval\_set)
* log the best score and the best iteration
* save and upload your trained model to W\&B Artifacts (when `log_model = True`)
* log feature importance plot when `log_feature_importance=True` (default).
* Capture the best eval metric in `wandb.Run.summary` when `define_metric=True` (default).

### Arguments

* `log_model`: (boolean) if True save and upload the model to W\&B Artifacts

* `log_feature_importance`: (boolean) if True log a feature importance bar plot

* `importance_type`: (str) one of `{weight, gain, cover, total_gain, total_cover}` for tree model. weight for linear model.

* `define_metric`: (boolean) if True (default) capture model performance at the best step, instead of the last step, of training in your `run.summary`.

You can review the [source code for WandbCallback](https://github.com/wandb/wandb/blob/main/wandb/integration/xgboost/xgboost.py).

For additional examples, check out the [repository of examples on GitHub](https://github.com/wandb/examples/tree/master/examples/boosting-algorithms).

## Tune your hyperparameters with Sweeps

Attaining the maximum performance out of models requires tuning hyperparameters, like tree depth and learning rate. W\&B [Sweeps](/models/sweeps/) is a powerful toolkit for configuring, orchestrating, and analyzing large hyperparameter testing experiments.

<ColabLink url="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/boosting/Using_W%26B_Sweeps_with_XGBoost.ipynb" />

You can also try this [XGBoost & Sweeps Python script](https://github.com/wandb/examples/blob/master/examples/wandb-sweeps/sweeps-xgboost/xgboost_tune.py).

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/w-lBKSCruauC3-2f/images/integrations/xgboost_sweeps_example.png?fit=max&auto=format&n=w-lBKSCruauC3-2f&q=85&s=70f40737f6467eaab407e3b3a42c48d9" alt="XGBoost performance comparison" width="1190" height="868" data-path="images/integrations/xgboost_sweeps_example.png" />
</Frame>
