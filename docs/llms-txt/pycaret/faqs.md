# Source: https://pycaret.gitbook.io/docs/learn-pycaret/faqs.md

# FAQs

<details>

<summary>Why PyCaret?</summary>

The short answer is it's an open-source, low-code machine learning library built on top of your favorite libraries and frameworks like *scikit-learn, xgboost, lightgbm, etc.* Machine Learning experments take a lot of iterations and the primary goal of PyCaret is to give you the ability to iterate with lightning speed. In comparison with the other awesome open-source machine learning libraries, PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with a few lines only. Give it a try!

</details>

<details>

<summary>Does PyCaret work with all OS and Python versions?</summary>

PyCaret is tested and supported on 64-bit systems:

* Python 3.7, 3.8, 3.9, and 3.10
* Ubuntu 16.04 or later
* Windows 7 or later

PyCaret also works on Mac OS but we do not guarantee the performance as the releases are not tested for Mac. To learn more about our testing workflows, [click here](https://github.com/pycaret/pycaret/blob/master/.github/workflows/test.yml).

</details>

<details>

<summary>Can  I use PyCaret on Google Colab or Kaggle Notebooks?</summary>

Absolutely. Just do `pip install pycaret`

</details>

<details>

<summary>Does PyCaret support model training on GPU?</summary>

Yes. We have integrated PyCaret with the amazing [Rapids.AI](https://rapids.ai/) project. To use GPU instead of CPU, just pass `use_gpu=True` in the `setup` function.&#x20;

**This will use CPU for model training:**

{% code lineNumbers="true" %}

```python
from pycaret.classification import *
s = setup(data, target = 'target_name')
```

{% endcode %}

**This will use GPU for model training:**

{% code lineNumbers="true" %}

```python
from pycaret.classification import *
s = setup(data, target = 'target_name', use_gpu = True)
```

{% endcode %}

There is no change in the use of the API, however, in some cases, additional libraries have to be installed as they are not installed with the default version or the full version of PyCaret. You can learn more about this [here](https://pycaret.gitbook.io/docs/get-started/installation#training-on-gpu).

</details>

<details>

<summary>Can I use PyCaret with parallel processing frameworks like Spark?</summary>

Absolutely Yes. PyCaret 3.0 has integration with [`Fugue`](https://github.com/fugue-project/fugue). You can now distribute `compare_models` function using the `parallel` parameter on your choice of framework. The current supported frameworks are `Ray`, `Dask`, and `Spark`. To learn more about this, check out [this link](https://pycaret.gitbook.io/docs/get-started/functions/train#distributed-training-on-a-cluster).

</details>

<details>

<summary>How can I contribute to PyCaret?</summary>

Thank you for choosing to contribute to PyCaret. There are a ton of great open-source projects out there, so we appreciate your interest in contributing to PyCaret. Please check out our [Contribution Guidelines](https://github.com/pycaret/pycaret/blob/master/CONTRIBUTING.md).

</details>

<details>

<summary>Does PyCaret support Deep Learning or Reinforcement Learning?</summary>

Not yet. In the future, maybe.

</details>

<details>

<summary>Can I integrate PyCaret with BI tools like Power BI, Tableau, Qlik, etc.?</summary>

Yes, any tool that supports the Python environment. You can use PyCaret within Power BI, Tableau, SQL, Alteryx, KNIME.&#x20;

</details>

<details>

<summary>How can I change verbosity in PyCaret?</summary>

Most functions in PyCaret has `verbose` parameter. Simply set `verbose=False` in the function.&#x20;

**Example:**

{% code lineNumbers="true" %}

```python
lr = create_model('lr', verbose = False)
```

{% endcode %}

</details>

<details>

<summary>How can can I silent the logger?</summary>

We have noticed in some situations that the logger of PyCaret can conflict with other libraries in the environment causing an abnormal behavior resulting in logs being printed on the screen (Notebook or CLI) as the code is running. While in the next major release (3.0), we are planning to make the logger more configurable, allowing you to totally disable it if you want. In the meantime, there is a way around using environment variables. Run the following code on the top of your Notebook:

{% code lineNumbers="true" %}

```python
import os
os.environ["PYCARET_CUSTOM_LOGGING_LEVEL"] = "CRITICAL"
```

{% endcode %}

**NOTE:** This command will set an environment variable that is used by PyCaret's logger. Setting it to `CRITICAL` means that only critical messages will be logged and there aren't many critical messages in PyCaret.&#x20;

</details>

<details>

<summary>I am having issues in installing PyCaret, what can I do?</summary>

Search on our [GitHub](https://github.com/pycaret/pycaret/issues) if others may have faced the same issue. If you are still stuck feel free to open a [new issue](https://github.com/pycaret/pycaret/issues).

</details>

<details>

<summary>Can I add my own custom models in PyCaret?</summary>

Absolutely. PyCaret's vision is to give you full control of your ML pipeline. To add custom models, there is only one rule. They must be compatible with standard `sklearn` API. To learn how to do it, you can read the following tutorials by Fahad Akbar:

* [Custom Estimator with PyCaret - Part I](https://towardsdatascience.com/custome-estimator-with-pycaret-part-1-by-fahad-akbar-839513315965)
* [Custom Estimator with PyCaret - Part II](https://towardsdatascience.com/custom-estimator-with-pycaret-part-2-by-fahad-akbar-aee4dbdacbf)

</details>

<details>

<summary>Can I add custom metrics for cross-validation in PyCaret?</summary>

Absolutely. PyCaret aim's to balance the abstraction with flexibility and so far we are doing a pretty good job. You can use PyCaret's `add_metric` and `remove_metric` functions to add or remove metrics used for cross-validation.  [Learn More](https://pycaret.gitbook.io/docs/get-started/functions/others#add_metric).

</details>

<details>

<summary>Can I just use PyCaret for data preprocessing?</summary>

Yes if you would like. You can run the `setup` function which handles all the data preprocessing and after that you can access the transformed train set and test set using the `get_config` function.&#x20;

**Example:**

{% code overflow="wrap" lineNumbers="true" %}

```python
from pycaret.classification import *
s = setup(data, target = 'target_name')

X_train, y_train = get_config('X_train_transformed'), get_config('y_train_transformed')
X_test, y_test = get_config('X_test_transformed'), get_config('y_test_transformed')
```

{% endcode %}

</details>

<details>

<summary>Can I export models from PyCaret and work on them outside of PyCaret?</summary>

Absolutely. You can use the `save_model` function of PyCaret to export the entire Pipeline as a `pkl` file. [Learn more](https://pycaret.gitbook.io/docs/get-started/functions/deploy#save_model) about this function.

</details>

<details>

<summary>Can I deploy ML pipelines on cloud using PyCaret?</summary>

Absolutely. PyCaret is an end-to-end library with a lot of deployment functionalities. There are many official tutorials on deployment on different cloud platforms such as Azure, AWS, and GCP. You can check out these [tutorials here](https://pycaret.gitbook.io/docs/official-blog#pycaret-add-ml-deployment).

</details>

<details>

<summary>Can I install and run PyCaret on an Apple M1 MacBook?</summary>

It's not straightforward due to some issues in the underlying dependencies of PyCaret. However, if you have tried everything and still can't find a solution, this [article](https://pareekshithkatti.medium.com/setting-up-python-for-data-science-on-m1-mac-ced8a0d05911) by Pareekshith Katti may help you.

</details>

<details>

<summary>Do I need a powerful computer to use PyCaret?</summary>

No, as long as your data can fit in the memory, you can use PyCaret. No super computer is needed.

</details>

<details>

<summary>Why is my pull request not getting any attention?</summary>

The review process may take some time. You should not be discouraged by delays in review on your pull request. We have many features that are requested by the community and only limited time from our maintainers to review and approve these pull requests. Since every feature comes at a cost of lifetime maintenance, we care a lot about getting things right the first time.&#x20;

</details>

<details>

<summary>Is PyCaret comparable to scikit-learn and ML libraries and framework?</summary>

Well, PyCaret is built on top of common ML libraries and frameworks such as scikit-learn, LightGBM, XGBoost, etc. The benefit of using PyCaret is that you don't have to write a lot of code. The underlying models and evaluation framework are the same as what you are used to.&#x20;

</details>
