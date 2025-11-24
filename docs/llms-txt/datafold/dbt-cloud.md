# Source: https://docs.datafold.com/integrations/orchestrators/dbt-cloud.md

# dbt Cloud

> Integrate Datafold with dbt Cloud to automate Data Diffs in your CI pipeline, leveraging dbt jobs to detect changes and ensure data quality before merging.

<Note>
  **NOTE**

  You will need a dbt **Team** account or higher to access the dbt Cloud API that Datafold uses to connect the accounts.
</Note>

## Prerequisites

### Set up dbt Cloud CI

In dbt Cloud, [set up dbt Cloud CI](https://docs.getdbt.com/docs/deploy/cloud-ci-job) so that your Pull Request job runs when you open or update a Pull Request. This job will provide Datafold information about the changes included in the PR.

### Create an Artifacts Job in dbt Cloud

The Artifacts job generates production `manifest.json` on merge to main/master, giving Datafold information about the state of production. The simplest method is to set up a dbt Cloud job that executes the `dbt ls` command on merge to main/master.

> Note: `dbt ls` is preferred over `dbt compile` as it runs faster and data diffing does not require fully compiled models to work.

Example dbt Cloud artifact job settings and successful run:

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cf58a3156778571d811e995c186a60ab" data-og-width="1592" width="1592" data-og-height="916" height="916" data-path="images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=b49999afef6210c65540b26b35405d8d 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=b826caa7c2d0ef0d9935e28b31aed4d7 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4a71e7da80a014c6fdc5ba72fa92d55f 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=13a4e60fc51d4ab8845071b01cf7c301 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a7beb8c2ce700409b4205346b77640b0 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_select_merge_job-590292c72209454e660444ea1a78fb5f.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e267803f50ef3e2ac00562ea12a8063d 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6e21263f5fa0b9317a58d335f59d02ec" data-og-width="2010" width="2010" data-og-height="1854" height="1854" data-path="images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0775d8bbe2360ce68a896d09ffa670a7 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d6a5b6271d4073fc60eb86f6b346d01b 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a526b0ac3e33ceab5fce9a35ef557a86 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d73678e8ddd48d24eaacea3a642f9989 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e8dbdee5ce84f68d4334b716f22fe5d4 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_artifacts_job_settings-939f1ce3f456698459c9045115706775.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fac813f0fe74aeee26672f67271ffd5e 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5889e462f19a3cbba05fd60f7f1a26bf" data-og-width="1841" width="1841" data-og-height="1210" height="1210" data-path="images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e9c9f109f7a7273b442e7276d5d2a950 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9ad27fd2667a61813bcde95460f2c93f 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=79f2d1de22adc241d3dabb4574f2dd71 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=37e8dc56d3f3e10723743d7f4eb7a4fe 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=8777748ffa6404d73bfd7632b3ec3632 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_ls_artifacts_job_example-2839e9104f9a64ca2833966db3900131.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f1c41706ec622fbc37c82810a29841a7 2500w" />
</Frame>

<Accordion title="Continuous Deployment">
  If you are interested in continuous deployment, you can use a [Merge Trigger Production Job](https://docs.datafold.com/cd#merge-trigger-production-job) instead of the Artifacts Job listed above.
</Accordion>

### dbt Cloud Access URL

You will need your [access url](https://docs.getdbt.com/docs/cloud/about-cloud/regions-ip-addresses) to connect Datafold to your dbt Cloud account.

### Add dbt Cloud Service Account Token

To connect Datafold to your dbt Cloud account, you will need to use a [Service Token](https://docs.getdbt.com/docs/dbt-cloud-apis/service-tokens).

info

Please note that the use of User API Keys for this purpose is no longer recommended due to a [recent security update](https://docs.getdbt.com/docs/dbt-cloud-apis/service-tokens) in dbt Cloud. [Learn more below](/integrations/orchestrators/dbt-cloud#deprecating-user-tokens)

1. Navigate to **Account Settings → Service Tokens → + New Token**.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a1853f25fa9a05cd5346385fe9de836b" data-og-width="2023" width="2023" data-og-height="832" height="832" data-path="images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=75f7c9808844db6e8f375e03264adbdf 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=884faa5d94bc096d9478521a925c7aca 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1858d0ef767eadb26037b57e0e7b1578 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=0ddea931e0c9a5ba475e437fe40f6931 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=98b4c7baa4cb7b9d4eb7af0a8a74ce4a 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token-2367d19382e6d25416b452ec5378bbfb.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=8603849aa46bdfdbfc2f0e89972bd238 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=84146d65087fe8a89d0037d5b158018d" data-og-width="1322" width="1322" data-og-height="864" height="864" data-path="images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=834fbaca8bab6e64f77c140a5774e715 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e7672e8ec2a88e2e66aadf52071706cc 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cd502aad0a0716ed1ea25be21605c63a 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4f0757783da2259ad5b4b6f95e8d8fd8 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a0e8887e9d3b56dcfb8cec48c8853083 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_add_service_token_permission-9fbdbb501c79f8a0bdee4abbf7483270.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3c0c5054d2879c4bb61cc9baca41996e 2500w" />
</Frame>

1. Add a Permission Set and select `Member` or `Developer`.
2. Select `All Projects`, or check only the projects you intend to use with Datafold.
3. Save your changes.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=87fc12ff14d1a74898d821e87b935c77" data-og-width="1308" width="1308" data-og-height="886" height="886" data-path="images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=10e3c018d832c6a955d7243ccc3a58a3 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=70bfb9cdf1d7db62075057264b25fff5 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6cefe9e7c967c8d56cd852b7b36f4e84 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=edfc4503837b70c884003ed5abe8c0dc 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=03436a64c167e679b6911c1fb94d39d7 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_service_token-5a4c080cb6b778f030eaf02988c36978.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9a9d578f71fd670b3ee9231344f0143f 2500w" />
</Frame>

1. Navigate to **Your Profile → API Access** and copy the token.

#### Deprecating User Tokens

dbt Cloud is transitioning away from the use of User API Keys for authentication. The User API Key will be replaced by account-scoped Personal Access Tokens (PATs).

This update will affect the functionality of certain API endpoints. Specifically, `/v2/accounts`, `/v3/accounts`, and `/whoami` (undocumented API) will no longer return information about all the accounts tied to a user. Instead, the response will be filtered to include only the context of the specific account in the request.

dbt Cloud users have until April 30, 2024, to implement this change. After this date, all user API keys will be scoped to an account. New customers are required to use the new account-scoped PATs.

For more information, please refer to the [dbt Cloud API Documentation](https://docs.getdbt.com/docs/dbt-cloud-apis/service-tokens).

If you have any questions or require further assistance, please don't hesitate to contact our support team.

## Create a dbt Cloud Integration in the Datafold app

* Navigate to Settings > Integrations > CI and create a new dbt Cloud integration.

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f7e0c8fb8d7fd554c4fdc36adf746cb7" data-og-width="2306" width="2306" data-og-height="496" height="496" data-path="images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f45ee4ad2bd8d407c1108c591cfcdf28 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=41827079f10c7fa05944138c2a7c1bd8 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cff0a79a8878070ff17a997fbdc20a51 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fc241868e30d85d6306c9e18051a1391 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=a4cc47cc9738ace1cf6d827fb98d7a2d 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_setup-b9dab8af8ca813283d0aaa3b99556eb0.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f71b1ca704af7318afca6fd774f42c2c 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=52c6d10f5b06085543f09dcff9106f97" data-og-width="1436" width="1436" data-og-height="640" height="640" data-path="images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f6c08b4a490fdda4c93ff0347d388dce 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e179f0a9cb37cc6b8c0a34f26f03497a 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=36acbde6d839dd22b1025263f3bbc254 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cd8ebc2c3207c0d5a004d202fb6351d7 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1551ad0d625bb0ed3bcb907e09df3e48 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_api_key-f3e2f3669695bdedf80f47fa1ccc91b3.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=bae50b6b6085801874fe965a421dd38f 2500w" />
</Frame>

## Configuration

### Basic Settings

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=cffb2b8c4bc7893601e6268b88fcbdc3" data-og-width="2294" width="2294" data-og-height="1354" height="1354" data-path="images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=98da01d5853b7937aa6b7383fbbd66d0 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=d744c777a4f34448b8bad2403f0b10b1 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4900264b8e46454f00a7684d8e1754c2 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=15dfbfe23d1d65df71070d08bc96ddda 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=496dd997a76f6706071de42485d914b7 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_basic_settings-022522ea2690dcc55c4bc7d3b1e4a411.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=06c5de14ae2640627cda4eef6ded9d2a 2500w" />
</Frame>

* **Repository**: Select a repository that you set up in [the Code Repositories setup step](/integrations/code-repositories).
* **Data Connection**: Select a connection that you set up in [the Data Connections setup step](/integrations/databases).
* **Name**: This can be anything!
* **Primary key tag**: This is a text string that you may use to tag primary keys in your dbt project yaml. Note that to avoid the need for tagging, [primary keys can be inferred from dbt uniqueness tests](/deployment-testing/configuration/primary-key).
* **Account name**: This will be autofilled using your dbt API key.
* **Job that creates dbt artifacts**: This will be [the Artifacts Job that you created](#create-an-artifacts-job-in-dbt-cloud). Or, if you have a dbt production job that runs on each merge to main, select that job.
* **Job that builds pull requests**: This is the dbt CI job that is triggered when you open a Pull Request or Merge Request.

### Advanced Settings

<Frame>
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ac03933bcc83efe52d9fae35874ee500" data-og-width="2306" width="2306" data-og-height="1432" height="1432" data-path="images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=36be894c12c54d680c65c00ec31e7377 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=9e424e6606c2bc34bb2ed7b2bf025d18 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4cd6464cb569f6d61c3f28bfb257bdc3 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4617f1e0877d5d5dd2d3b855a1c83868 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3b221781ca235a27113b3943825ba23e 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt_cloud_advanced_settings-c862158fc664963c51377f0daaadaca3.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=655f696a55d9a7d6c0a8c0f3f260e218 2500w" />
</Frame>

* **Enable Datafold in CI/CD**: High-level switch to turn Datafold off or on in CI (but we hope you'll leave it on!).
* **Import dbt tags and descriptions**: Populate our Lineage tool with dbt metadata. ⚠️ This feature is in development. ⚠️
* **Slim Diff**: Only diff modified models in CI, instead of all models. [Please read more about Slim Diff](/deployment-testing/best-practices/slim-diff), which is highly configurable using dbt yaml, and each organization will need to set a strategy based on their data environment.
  * Downstream Hightouch models will be diffed even when Slim Diff is turned on.
* **Diff Hightouch Models**: Hightouch customers can see diffs of downstream Hightouch assets in Pull Requests.
* **CI fails on primary key issues**: The existence of null or duplicate primary keys causes the Datafold CI check to fail.
* **Pull Request Label**: For when you want Datafold to *only* run in CI when a label is manually applied in GitHub/GitLab.
* **CI Diff Threshold**: For when you want Datafold to *only* run automatically if the number of diffs doesn't exceed this threshold for a given CI run.
* **Files to ignore**: If at least one modified file doesn’t match the ignore pattern, Datafold CI diffs all changed models in the PR. If all modified files should be ignored, Datafold CI does not run in the PR. ([Additional details.](/deployment-testing/configuration/datafold-ci/on-demand))
* **Custom base branch**: For when you want Datafold to **only** run in CI when a PR is opened against a specific base branch. You might need this if you have multiple environments built from different branches. See [Custom branch](https://docs.getdbt.com/faqs/Environments/custom-branch-settings) in dbt Cloud docs.

Click save, and that's it! <Icon icon="party-horn" />

Now that you've set up a dbt Cloud integration, Datafold will diff your impacted tables whenever you push commits to a PR. A summary of the diff will appear in GitHub, and detailed results will appear in the Datafold app.
