# Source: https://docs.datafold.com/deployment-testing/best-practices/slim-diff.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Slim Diff

> Choose which downstream tables to diff to optimize time, cost, and performance.

By default, Datafold diffs all modified models and downstream models. However, it won't make sense for all organizations to diff every downstream table every time you make a code update. Tradeoffs of time, cost, and risk must be considered.

That's why we created Slim Diff.

With Slim Diff enabled, Datafold will only diff models with dbt code changes in your Pull Request (PR).

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=7f8df7c3088ee7de6303eba741627e5b" data-og-width="1600" width="1600" data-og-height="1073" height="1073" data-path="images/deployment_testing/slim-diff-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=7c1e3d7326d4b2c4bcdf5c8a9408d6ed 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e0477c72f52c568e2a17b3ae87cc8caf 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4da34a62237b4a9c780b179a87fc8d25 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e6101b2ee0015bcb5bcee4522883ac77 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f2894cb5950383fd85990d9d66374c94 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff-diagram.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4bf3a98d8595c537b00533e39f4a02a1 2500w" />
</Frame>

## Setting up Slim Diff

In Datafold, Slim Diff can be enabled by adjusting your diff settings by navigating to Settings → Integrations → CI → Select your CI tool → Advanced Settings and check the Slim Diff box:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=47702904f2d17c9cdeb39b99e6454b95" data-og-width="883" width="883" data-og-height="688" height="688" data-path="images/deployment_testing/slim-diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=8adae9bb4e6df64a9a4ecb4ae16733d1 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6d01d60c69efa14b65dcc562f485929f 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=709b877b189afb6f3d648639e5bb285e 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5fceec0f457ccd32402349936bf79a73 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=beecbe434fb9d97388d72a0406727454 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/deployment_testing/slim-diff.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=532581c6f5c4c052e6d18219b3e59d31 2500w" />
</Frame>

## Diffing only modified models

With this setting turned on, only the modified models will be diffed by default.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e0707c61bf5e85634a3924ef30650492" data-og-width="1886" width="1886" data-og-height="802" height="802" data-path="images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1eb8c1594ac03c0c2d5bcfaf30d2b13f 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f57bd3e88ed16e9db6267a690319b6cb 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1d6db32c3365da0ac92a5f634432a2cf 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0f490ba01fbe6c53f44b30d09737dbca 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=345a3a197c39924a24e6b38229344bcb 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832523-c3552417-8975-4460-91ed-fd7b0df7d7b7.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=04e1b5fca810ee9c2b42b2730dc84e0f 2500w" />
</Frame>

## Diff individual downstream models

Once Datafold has diffed only the modified models, you still have the option of diffing individual downstream models right within your PR.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=dc39127b63705424aa89cc2f504d7b4a" data-og-width="1734" width="1734" data-og-height="700" height="700" data-path="images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b3884df7d44e0ef5430cf095a546d55c 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=9a1cff3b0991afcddbe46dc7bcbdea8e 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=74cd9f3e2d5c3a7bcd18a637da99615c 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=fe210acaef87f3e69fcb946d113743eb 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2f1585b55169073505a424cd434bb3c3 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208832659-e3cdb9d9-c468-459f-85ff-990b2a68b57c.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=bde7b6c2b15c7f153bbf869996812100 2500w" />
</Frame>

## Diff all downstream models

You can also add the `datafold:diff-all-downstream` label within your PR, which will automatically diff *all* downstream models.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ee1105716276b26d932c303a0db51733" data-og-width="1884" width="1884" data-og-height="870" height="870" data-path="images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f36e4fedc137345a6d7314542a118289 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2152ddb5c3d92e55f124621d8960b625 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1637c775d06e35b5f03679002e8364e4 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=18d225eb875b9a1fd6c0fc07a5fa50c6 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=b7ad5d7ade28ed877cb2c5325e71489c 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833093-f853bde7-d12a-4b9f-b5ac-a4d8d9666076.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=97ba0d9d4a62d99b078673e9093b6d2b 2500w" />
</Frame>

## Explicitly define which models to always diff

Finally, with Slim Diff turned on, there might be certain models or subdirectories that you want to *always* diff when downstream. You can think of this as an exclusion to the Slim Diff behavior.

Apply the `slim_diff: diff_when_downstream` meta tag to individual models or entire folders in your `dbt_project.yml` file:

```Bash  theme={null}
models:
  <project_name>:
    <directory_name>:
      +materialized: view
      <model_name>:
        +meta:
          datafold:
            datadiff:
              slim_diff: diff_when_downstream

    <directory_name>:
      +meta:
        datafold:
          datadiff:
            slim_diff: diff_when_downstream
```

These meta tags can also be added in individual yaml files or in config blocks. More details about using meta tags are available in [the dbt docs](https://docs.getdbt.com/reference/resource-configs/meta).

With this configuration in place, Slim Diff will prevent downstream models from being run *unless* they have been designated as exceptions with the `slim_diff: diff_when_downstream` dbt meta tag.

<Frame>
  <img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=1f117e6880687fabc1575f4964a91722" data-og-width="1924" width="1924" data-og-height="874" height="874" data-path="images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=faa6bc4aeefa6ab362cc19ee1f7fb28d 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f41b1cb4db53e415bf3030f44e80200d 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=04313891c34afe163d0741ebf059b5bf 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c1fbf4c72b4ba74fb70203548c0b6cc9 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0f6efbef8db741e874fefa7ae030a211 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/208833985-031a04fe-864a-4487-8a64-ec80e4c232e1.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c848d3307d3760207c2d6a7f683765ff 2500w" />
</Frame>

As usual, once the PR has been opened, you'll still have the option of diffing individual downstream models that weren't diffed, or diffing all downstream models using the `datafold:diff-all-downstream` label.
