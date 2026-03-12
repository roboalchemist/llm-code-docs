# Source: https://docs.snowflake.com/en/developer-guide/native-apps/snowflake-ml-na-about.md

# Use Snowflake machine learning models in a Snowflake Native App

This topic describes how to use a [Snowflake ML](../snowflake-ml/overview.md)
model in a Snowflake Native App. It also describes how to call
[Snowflake Cortex](../../user-guide/snowflake-cortex/aisql.md) functions from an app.

## Overview of using Snowpark ML in a Snowflake Native App

Snowflake ML is an integrated set of capabilities for end-to-end machine learning
in a single platform on top of your governed data. You can this functionality within
a Snowflake Native App.

The Snowflake Native App Framework supports the following use cases:

* Providers include a training algorithm in the app, but the trained model is not included.
  Providers include the source code for the model, for example linear regression or logistical
  regression, in the app.

  After the app is installed, training occurs on data in the consumer account, for example by calling the
  model’s `fit()` method.

  For more information, see [Create, train and use a Snowflake ML model in an app](snowflake-ml-na-no-model.md).
* Providers share data with the consumer and include a training algorithm in the app. After installation,
  the app trains the model based on data in the consumer account that has been shared with the app

  For more information, see [Create, train and use a Snowflake ML model in an app](snowflake-ml-na-no-model.md).
* Providers train a model based on data in their account and include these models in the app. When the app
  is installed, consumers can use the model directly, for example by calling the model’s
  :predict() method.

  For more information, see [Include a trained model in an app](snowflake-ml-na-with-model.md).

## Limitations when using Snowflake ML in an app

The following limitations apply when using Snowflake ML in an app:

* Only models based on warehouses are currently supported.
* Providers must use the Snowflake Model Registry to share models with consumers. Snowpark
  ML functions like `fit()` store results in a temporary stage which is not supported
  for Snowflake Native Apps.
* There are limitations on machine learning algorithms that are runnable in a Snowpark sandbox
  within a warehouse. More complex machine learning frameworks like TensorFlow or PyTorch are
  not runnable in these sandboxes.
* Training performed on a provider’s dataset may not yield a model sufficiently effective for
  a consumer’s data. Training a model on consumer data may provide better results.

## Calling Snowflake Cortex functions from an app

To call a [Snowflake Cortex function](../../user-guide/snowflake-cortex/aisql.md) from
an app, *consumers* must first grant the CORTEX_USER database role to the app as shown in the following
example:

```sqlexample
GRANT DATABASE ROLE SNOWFLAKE.CORTEX_USER TO APPLICATION my_app;
```

> **Note:**
>
> Providers should mention in the listing of an app that consumers must grant the CORTEX_USER database role.

The CORTEX_USER database role in the SNOWFLAKE database includes the privileges that allow users to
call Snowflake Cortex LLM functions. See [Snowflake Cortex AI Functions (including LLM functions)](../../user-guide/snowflake-cortex/aisql.md) for more information.

After consumers this role to the app, the app can call Snowflake Cortex functions as shown in the following
example:

```sqlexample
SELECT SNOWFLAKE.CORTEX.TRANSLATE('La plateforme unique de Snowflake élimine les silos de données!','fr','en');
```
