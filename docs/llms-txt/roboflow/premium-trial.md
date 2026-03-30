# Source: https://docs.roboflow.com/roboflow/roboflow-ko/billing/premium-trial.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/qing-qiu/premium-trial.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/billing/premium-trial.md

# Source: https://docs.roboflow.com/billing/premium-trial.md

# Premium Trial

The Premium Trial is a limited, 14 day trial of premium features to help you assess whether or not Roboflow's computer vision platform is right for your use case.

## Trial Features

The trial gives you access to specific premium features in the application and $150 worth of [included credits](https://docs.roboflow.com/billing/credits) to use. The trial does not map 100% to a specific paid plan.

While using your trial, if there is a feature that you care most about, we've provided the below comparison table to make it easy to understand which plans will give you the equivalent level of access. When the plan name is listed with a `+`, the feature is available on the named plan and all higher plans.

{% hint style="warning" %}
For up-to-date information on our plans and their associated features, see our [pricing page](https://roboflow.com/pricing).
{% endhint %}

### Access

| Feature                                                                                                         | Included             | Plan Equivelant |
| --------------------------------------------------------------------------------------------------------------- | -------------------- | --------------- |
| Private Data                                                                                                    | :white\_check\_mark: | Basic+          |
| [Included Credits](https://docs.roboflow.com/billing/credits)                                                   | 50                   |                 |
| [Team Members](https://docs.roboflow.com/workspaces/team-members)                                               | 5                    | Basic+          |
| Projects                                                                                                        | 10                   | Basic+          |
| [Role Based Access Control (RBAC)](https://docs.roboflow.com/workspaces/team-members/role-based-access-control) | :white\_check\_mark: | Enterprise      |

### Data

| Feature                                                                                                                               | Included             | Plan Equivelant |
| ------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------------- |
| Workspace Dataset Size Limit                                                                                                          | Uncapped             | Basic+          |
| [Image Augmentations](https://docs.roboflow.com/datasets/dataset-versions/image-augmentation)                                         | 10x                  | Enterprise      |
| [Enhanced Augmentations](https://docs.roboflow.com/datasets/dataset-versions/image-augmentation#augmentation-options) & Preprocessing | :white\_check\_mark: | Basic+          |

### Label

| Feature                                                                                         | Included             | Plan Equivelant |
| ----------------------------------------------------------------------------------------------- | -------------------- | --------------- |
| Review Mode                                                                                     | :white\_check\_mark: | Enterprise      |
| [Labeling History](https://docs.roboflow.com/annotate/use-roboflow-annotate/annotation-history) | :white\_check\_mark: | Enterprise      |

### Train

| Feature                  | Included             | Plan Equivelant |
| ------------------------ | -------------------- | --------------- |
| All Model Sizes          | :white\_check\_mark: | Enterprise      |
| Model Evaluation         | :white\_check\_mark: | Enterprise      |
| Concurrent Training Jobs | :white\_check\_mark: | Enterprise      |

### Deploy

| Feature                                                                           | Included             | Plan Equivelant |
| --------------------------------------------------------------------------------- | -------------------- | --------------- |
| [Model Monitoring](https://docs.roboflow.com/deploy/model-monitoring)             | 7 Days of Data       | Enterprise      |
| [Dedicated Deployments](https://docs.roboflow.com/deploy/dedicated-deployments)   | :white\_check\_mark: | Basic+          |
| [Workflow Versions](https://docs.roboflow.com/workflows/manage-workflow-versions) | :white\_check\_mark: | Enterprise      |

### Support

| Feature       | Included             | Plan Equivelant |
| ------------- | -------------------- | --------------- |
| Email Support | :white\_check\_mark: | Enterprise      |
| Live Chat     | :white\_check\_mark: | Enterprise      |

### Unsupported Features

There are some features of our paid plans that we don't offer as a part of the Premium Trial. To be abundantly clear about their exclusion, you can find these features listed below.

| Feature                                                                                       | Included | Plan Equivelant     |
| --------------------------------------------------------------------------------------------- | -------- | ------------------- |
| Purchasing Prepaid Credits                                                                    | :x:      | Basic+              |
| [Outsourced Labeling Services](https://docs.roboflow.com/annotate/roboflow-labeling-services) | :x:      | Enterprise (Annual) |
| [Download Model Weights](https://docs.roboflow.com/deploy/download-roboflow-model-weights)    | :x:      | Basic+              |
| Premium GPU Access for Training                                                               | :x:      | Enterprise          |
| Inference Model License                                                                       | :x:      | Basic+              |
| Self-Hosted Model License                                                                     | :x:      | Enterprise          |
| Onboarding Call                                                                               | :x:      | Enterprise          |

## Trial Start

Most users that sign up to Roboflow will be automatically started on the trial, while some may have to explicitly opt into the trial. You can verify if you are on the Trial or not by going to the [Plan & Billing](https://app.roboflow.com/test-growth-trial/settings/plan) page.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-623e30db4571b2fbe4ba727442a826419e1a7113%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

## Trial End

When your trial expires, your account will automatically be put in a sandbox state. In this state, you cannot use platform until you perform at least one of the following actions:

* [Purchase a Plan](https://docs.roboflow.com/billing/plans/purchase-a-plan)
* Select the Public Plan

As a part of selecting the public plan, you will be required to:

* Manually set any previously private datasets to public
* Remove projects and team members until you are under the Public Plan limits

{% hint style="info" %}
When your trial expires, your datasets only go public with your explicit consent. We require this extra action to ensure that your private datasets are not leaked to the public!
{% endhint %}
