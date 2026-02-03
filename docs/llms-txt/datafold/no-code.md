# Source: https://docs.datafold.com/deployment-testing/getting-started/universal/no-code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# No-Code

> Set up Datafold's No-Code CI integration to create and manage Data Diffs without writing code.

Monitors are easy to create and manage in the Datafold app. But for teams (or individual users) who prefer a more code-based approach, our monitors as code feature allows managing monitors via version-controlled YAML.

## Getting Started

Get up and running with our No-Code CI integration in just a few steps.

### 1. Create a repository integration

Connect your code repository using the appropriate [integration](/integrations/code-repositories).

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=45fd70946a2add757d79098af039b429" data-og-width="2084" width="2084" data-og-height="742" height="742" data-path="images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a69e88590a390b61e72569c53a496d24 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fd0d01e133d73d97290b898e2f53623b 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3cc0312866dc746c1654834ce3d07382 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=2ada31061cc7d4abc5d4939d4e8d80c3 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=cf99b0fd987b5dbc15bc46d84fc7d927 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_repo_integration-d436bfd0149ef5b49b3cd2baff167737.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b4ab64b5e13ef955ff4aab55f4d16879 2500w" />
</Frame>

### 2. Create a No-Code integration

From the integrations page, create a new No-Code CI integration.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7be3befc9aa261a2f155ee155143944f" data-og-width="2072" width="2072" data-og-height="1094" height="1094" data-path="images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=5d13b05cc2d3dd048ad48377bb57949f 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0e86d492621fd5f2659d3cb40a837dbd 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=50a25d67b9a037262eb9b655aff8fa47 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0e1e685b014a75fc3fb1c2089c72618a 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=128ba338ad334a2fe0d45e75905ded8a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_ci_integration-63a004100ab880d71821d7f41a5aeebb.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4a47c0ba9c62d731a7da05666aac7cd5 2500w" />
</Frame>

### 3. Set up the No-Code integration

Complete the configuration by specifying the following fields:

#### Basic settings

| Field Name         | Description                                           |
| ------------------ | ----------------------------------------------------- |
| Configuration name | Choose a name for your Datafold integration.          |
| Repository         | Select the repository you configured in step 1.       |
| Data Connection    | Select the data connection your repository writes to. |

#### Advanced settings

| Field Name         | Description                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Pull request label | When this is selected, the Datafold CI process will only run when the `datafold` label has been applied to your pull request. |
| Custom base branch | If provided, the Datafold CI process will only run on pull requests against the specified base branch.                        |

### 4. Create a pull request and add diffs

Datafold will automatically post a comment on your pull request with a link to generate a CI run that corresponds to the latest set of changes.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e8dc9f691dd36c5b59f8a832f7c5ef90" data-og-width="1033" width="1033" data-og-height="622" height="622" data-path="images/1-7a001321004a1afa68a3bd74a4bb822d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=59cb82e2ee41b716816ede9085085353 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=239b202662245ccb9c78fd41786d5f91 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f387cd9dc8c008824f6eeca5ec21e71c 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a8b9eee6e6aef7d0c0f8d280858cfb15 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5c44de689cfb9f78de714064eb6d3609 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/1-7a001321004a1afa68a3bd74a4bb822d.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=dc5ca756ef235c762cde0f0f9e941212 2500w" />
</Frame>

### 5. Add diffs to your CI run

Once in Datafold, add as many pull requests as you'd like to the CI run. If you need a refresher on how to configure data diffs, check out [our docs](/data-diff/in-database-diffing/creating-a-new-data-diff).

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b8de0e72e6d42738e3538834bd51ad19" data-og-width="1292" width="1292" data-og-height="696" height="696" data-path="images/4-800a438c5251d6888b83a1f9e3c811bb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a322fb992c2f19bc19aeee0370e1e0bb 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=8d24e8bbd9faf0e9e0968391dc7a4da9 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a556956ee858b83f15df1183405742eb 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=46d75ba6cb4e9f6d2987c9f97fd58186 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2654e257f99837a8e9311575632577d0 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/4-800a438c5251d6888b83a1f9e3c811bb.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1f77b255c440ee8f54e24e4f91efbd22 2500w" />
</Frame>

### 6. Add a summary to your pull request

Click on **Save and Add Preview to PR** to post a summary to your pull request.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=386e1a389aae5b12600fc22912f5f48b" data-og-width="1321" width="1321" data-og-height="522" height="522" data-path="images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=eca70eecd76a85c1bc0240f7049ef059 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e4bb9cfe5324703779943c9db4324bc0 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d962ce1398ce803578a3af02bcaa851f 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0e88cf6e1992e2bbe6b9f4282698f6e8 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e4de295c456d6de6f98e79c40e20eedb 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/2-cb3997ac8f47fe7d5ad651478f1fe7d8.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=488eae433e397515264c7ec6c7f75055 2500w" />
</Frame>

### 7. View the summary in your pull request

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b43855e4da91adf49b0dfbab2da269f1" data-og-width="934" width="934" data-og-height="789" height="789" data-path="images/3-33123cf19f9ff7f5fa1aef9952d8208d.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=847b01768e805d2de27656f71b4d6a14 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e870cd6078f7a841649326c90ae40faa 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1123c9dbd70ed78a60a10431feab998a 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=76db4ba13ca6dbd931f2cca19715120a 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=d788e7d68bac7eb90e8e204e8dd467a9 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/3-33123cf19f9ff7f5fa1aef9952d8208d.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0decfea251860812a4fdca7bfcade7b4 2500w" />
</Frame>

## Cloning diffs from the last CI run

If you make additional changes to your pull request, clicking the **Add data diff** button generates a new CI run in Datafold. From there, you can:

* Create a new Data Diff from scratch
* Clone diffs from the last CI run

You can also diff downstream tables by clicking on the **Add Data Diff** button in the Downstream Impact table. This creates additional Data Diffs:

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=cfddbf0cccec7c25713c3ef567b27096" data-og-width="1143" width="1143" data-og-height="743" height="743" data-path="images/5-c411b13fcdaebb9587fabcfcef92c740.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=a8f12789bbbc07e1c70f14fbc19b7581 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=24b431abf786e2daa6e4711c8f55e007 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3a1d9f4d32c7393e774a5fd1fc05f0b4 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=dd996cbef054a8180126ac567c6b2fb0 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=282130b7029845acf13096e609cdfa0b 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/5-c411b13fcdaebb9587fabcfcef92c740.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=adbf58519948c822bc29e4dce9c64fdb 2500w" />
</Frame>

You can then post another summary to your pull request by clicking **Save and Add Preview to PR**.
