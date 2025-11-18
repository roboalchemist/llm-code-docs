# Source: https://docs.asapp.com/changelog/generativeagent.md

# GenerativeAgent Updates

> New updates and improvements for the GenerativeAgent

<Update label="2025-06-17 - Evaluation for Scenario Testing">
  ## Evaluation for Scenario Testing

  **Test Scenarios** now support automated evaluation of simulated conversations through a new **Evaluations** section.

  With these updates, you can:

  * Define **applicability criteria** to control when evaluations should run
  * Specify **evaluation criteria** to automatically assess key outcomes in simulated conversations
  * View pass/fail results in the **Previewer**, side-by-side with the conversation
  * Rerun evaluations after editing the test scenario, using the **Run Eval Again** button
  * Set a **max number of turns** (default: 25) for simulations
  * Preview your test scenario directly from the test file after saving

  <Frame>
    <img width="500px" src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=0f1049b2d1f2f707bb0052d49ba8fb64" data-og-width="1892" data-og-height="1114" data-path="images/generativeagent/EvaluationsResultsPanel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=f91575a650cbf2245812c91e7463ad81 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=872257a5336ec50d1ebb209924d60a72 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=013a7ce07d9fef850f3c08cd3aca4c66 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=d0fb1113bf79b41daae155307c87acaa 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=3aa307719a0b6b106ca7383ad9c099ee 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=a76d877f2d656e20c8a9bdb5ee409e7f 2500w" />
  </Frame>

  <Card title="Using Evaluations in Test Scenarios" href="/generativeagent/configuring/tasks-and-functions/test-scenarios">
    Learn how to define and run evaluations on simulated customer conversations.
  </Card>
</Update>

<Update label="2025-05-27 - Scenario Testing">
  ## Scenario Testing

  **Test Scenarios** enable more efficient testing of GenerativeAgent configurations through automated simulations of customer interactions. They are an evolution from Test Users, offering not just mock API profiles, but also integrated goals, information customers have on them, and personalities to simulate a customer in a specific scenario.

  With Test Scenarios, you can:

  * Automatically generate mock API responses fitting a customer scenario
  * Add customer goals, information customers have, and personalities to vary how the simulated customer will interact with GenerativeAgent
  * Run simulated interactions and review how GenerativeAgent handles a customer with that scenario

  **Test Users** have been migrated to Test Scenarios

  All workflows involving Test Users will still be accessible through Test Scenarios and all Test Users have been migrated to Test Scenarios.

  <Frame>
    <img width="500px" src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScenarioTesting-changelog.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=f2e9cbc35d5d94c0abfa7e7a11cfb576" data-og-width="1948" data-og-height="1368" data-path="images/generativeagent/ScenarioTesting-changelog.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScenarioTesting-changelog.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=2216a057a31d105ac33ca136efab525c 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScenarioTesting-changelog.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=31f6241db6ae9a710c513c01df989fa8 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScenarioTesting-changelog.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c68d7d47b9c23cb2c9813fafb06dd530 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScenarioTesting-changelog.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=1067c2f99339c853bd9e2a7cf73cd131 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScenarioTesting-changelog.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=ed841b9d6f9ef02eaa27890df7efbc9f 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScenarioTesting-changelog.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=2c6b0c191f8c2d5ed212de51c20e0e7b 2500w" />
  </Frame>

  <Card title="Creating and running Test Scenarios" href="/generativeagent/configuring/tasks-and-functions/test-scenarios">
    Learn how to create Test Scenarios and use them to speed up testing of GenerativeAgent configurations.
  </Card>
</Update>

<Update label="2025-05-20 - Configuration Branches">
  ## Configuration Branches

  **Configuration Branches** enables seamless experimentation with GenerativeAgent configurations through local branching. This new feature allows you to safely test and iterate on changes without affecting your main environments.

  With Configuration Branches, you can:

  * Create isolated branches from Draft, Sandbox, or Production environments
  * Edit tasks, functions, and settings in a protected workspace
  * Preview changes before promoting them to main environments
  * Collaborate with team members on configuration improvements

  <Frame>
    <img width="500px" src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a314f6eb26503284ac8c7b00e5f9a4b0" data-og-width="2282" data-og-height="1116" data-path="images/generativeagent/LocalConfig.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=45cc97ffb114e54615947704df7ecdca 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c0cb57489c8f651b954b18c337c7c7ea 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=73329c558e53c5134e36315b6648fd18 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=6b1b06f456194255a1e9a3b34af8245a 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=b54db09ce5eb37cf5b80ad25555352b5 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/LocalConfig.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=58a3e47f6d306e80d647a67bef386545 2500w" />
  </Frame>

  <Card title="Managing Configuration Branches" href="/generativeagent/configuring/tasks-and-functions/local-configs">
    Learn how to create branches, make configuration changes, and safely promote them to your main environments.
  </Card>
</Update>

<Update label="2025-05-07 - Advanced Syncing and Auto-Deploy for Knowledge Base Content">
  ## Advanced Syncing and Auto-Deploy for Knowledge Base Content

  We've launched enhanced controls for syncing and deploying your knowledge base, giving you the flexibility to prioritize critical updates and deliver the most current information through GenerativeAgent—automatically and with less manual overhead.

  **What’s new?**

  * **Configurable Sync Modes:** Set each content source to update with manual review, auto-deploy updates directly to production, or turn off syncing.
  * **Frequent Article Refresh:** Enable high-frequency (every 15 minutes) automatic updates and instant deployment for critical, time-sensitive articles.

  <Frame>
    <img width="500px" src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d60991544408edcc59048fe3e016d82f" data-og-width="2218" data-og-height="1022" data-path="images/generativeagent/KBAutoDeploy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7507be3f1bfa199d78945a8d1cfecec0 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8cb94ed1f45d413852348bc548acf2ac 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=25b57b54afc7b31666f5cbd710b16f7a 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7955403056759a22955512bac5dc3ffe 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8b85131a343f9c67317e5844e2e4e57c 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7e4a97f2e29c37bd791da2d02b665fc7 2500w" />
  </Frame>

  <Frame>
    <img width="500px" src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a83e93fa21e826debd49bc49e88fff63" data-og-width="1316" data-og-height="540" data-path="images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=2d57d236b38ad6492f9eada2265d2682 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=bad9a018dd06e44c30c2f12912788767 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=660032038785ca09c4acf3c19e70c2d9 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0a8170d814a39560ee47ff7b7b702f78 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=36703d8d7a2cb4f6191ead166d7b11ee 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=59ea85fd895c31174dd0255e761eae04 2500w" />
  </Frame>

  <Card title="Knowledge Base Syncing & Deploy Options" href="/generativeagent/configuring/connecting-your-knowledge-base">
    Learn how to configure syncing and deploy preferences for maximum accuracy and responsiveness.
  </Card>
</Update>

<Update label="2025-04-04 - Auto-generating Test Users">
  ## Auto-generating Test Users

  We've introduced the ability to **automatically generate test** users by describing test scenarios, making it easier to simulate API interactions for testing purposes.

  This feature accelerates your testing process by automatically creating realistic test data based on your scenario descriptions, helping you validate GenerativeAgent's behavior more efficiently.

  <Frame>
    <img width="500px" src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserCreate.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0c5d7dcf642b33ac6b0f72ef8a536523" data-og-width="1263" data-og-height="1024" data-path="images/generativeagent/TestUserCreate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserCreate.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d05cfe690b5cb40d08e06eb5d8e41b12 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserCreate.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=437942b1ac38fe7d54d6e9c59b8d1f20 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserCreate.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=1d59c650f8f293186bd89af72dd5a495 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserCreate.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=e2cc157b1ad068321655805e102f30c5 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserCreate.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=31740d744aeeba27da688b3e75c389a4 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserCreate.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=597c3c8c5a63df1d6dd99cff55e8598d 2500w" />
  </Frame>

  <Card title="Test Users" href="/generativeagent/configuring/tasks-and-functions/test-users">
    Learn how to create and configure test users to simulate API responses and test your GenerativeAgent's behavior
  </Card>
</Update>

<Update label="2025-02-20 - Pinned Versions">
  ## Pinned Versions

  **Pinned Versions** allows you to pin specific versions of GenerativeAgent to a deployment, enabling safer and more predictable deployments.

  This enables you to:

  * Maintain version stability in production environments
  * Control the rollout of new features
  * Test version changes in preview before deployment
  * Ensure consistent behavior across GenerativeAgent deployments

  <Frame>
    <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=ad670c19b880f7bfdd598ef154a1a235" data-og-width="426" width="426" data-og-height="393" height="393" data-path="images/generativeagent/PinnedVersionSelector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=5be5b0cb79c65efb339acf53a15007b0 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=292617ecf55604d42896e306fe35e7ee 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a34c7afef5547a17d84600ed6fc04964 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=1836def9129e2681606fd5c26dbdf2c0 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=cb18c77085843a69b0f6cc2c23636e7c 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/PinnedVersionSelector.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=cd669a02ebcc03bffd4422ac2de8aba8 2500w" />
  </Frame>

  <Card title="Pinned Versions Documentation" href="/generativeagent/configuring/deploying-to-generativeagent#generativeagent-versions">
    Learn how to configure and manage GenerativeAgent versions
  </Card>
</Update>

<Update label="2025-01-28 - Scope and Safety">
  ## Scope and Safety

  **Scope and Safety Fine Tuning** allows customizable guardrails that let you define what's considered "in-scope" and "safe" for your specific use cases, while maintaining core safety protections.

  With this feature, you can:

  * Customize safety boundaries aligned with business policies
  * Expand permissible topics without compromising default protections
  * Control input safety and scope definitions with precision

  <Frame>
    <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputSafety.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=88d5e7ce0f800d9f44c15669accbf968" data-og-width="1408" width="1408" data-og-height="1176" height="1176" data-path="images/generativeagent/InputSafety.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputSafety.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=c79acf4d9c28c4f57d25f4a139e624ff 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputSafety.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=184fea8ba95cce8bf6d0932baa05ff7b 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputSafety.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=474d531ddf7bc784a76a145c1ce37758 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputSafety.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=c275b9cf92c24c2cff9e1f02862b36f5 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputSafety.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=adfabba0292f4ef380416b8da9c3b8d6 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputSafety.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=d070c1fca7dec2ef687bdd6862475ad8 2500w" />

    <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScopeTopic.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d91eb7c3737f3334fb92787d87cf32db" data-og-width="1408" width="1408" data-og-height="1416" height="1416" data-path="images/generativeagent/ScopeTopic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScopeTopic.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=f3d975e50a2a42bf116e46387e1c3717 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScopeTopic.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=e9ad38422e52b71be778107efb641daa 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScopeTopic.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=55155d5044c9c2b42303b4ec53fa4fa0 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScopeTopic.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=5f0e301954b582cabeb2de963706f0ce 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScopeTopic.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a01d75ee847a6e56d0cecb1e2812dd14 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/ScopeTopic.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=2eea551095c76244ad2f0f7173365f71 2500w" />
  </Frame>

  <Card title="Safety Tuning Documentation" href="/generativeagent/configuring/safety/scope-and-safety-tuning">
    Learn how to configure safety and scope settings
  </Card>
</Update>

<Update label="2025-01-13 - Mock Functions">
  ## Mock Functions

  **Mock Functions** enable rapid prototyping and testing of GenerativeAgent integrations without requiring live API endpoints.

  This feature allows you to:

  * Prototype and validate Function behaviors before building actual APIs
  * Test GenerativeAgent's parameter handling and response processing
  * Accelerate development by simulating API responses during initial setup

  Once you have a working mock function, you can convert it to a live function by pointing it to your live API via an API connection.

  <Frame>
    <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=33b627189a3e45b34a1065eb5963390f" data-og-width="3302" width="3302" data-og-height="1058" height="1058" data-path="images/generativeagent/MockAPIExample.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=308c3ef5b5602f5f5cc51d6d3f5ba902 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=3d62ce5e183d7d50b99afa3de05ad113 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=18289c4d24f26ebaa6f34c567ff9d42f 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8f86c20e578678a68428f7ed3df20a7d 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0d0ecefb562fa98ba7ee3bf411575841 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/MockAPIExample.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c103fa114bf62cbb408a1f8e7787fc74 2500w" />
  </Frame>

  <Card title="Mock API Documentation" href="/generativeagent/configuring/tasks-and-functions/mock-api">
    Learn how to create and use Mock Functions
  </Card>
</Update>

<Update label="2024-11-22 - Turn Inspector">
  ## Turn Inspector

  **Turn Inspector** is an advanced diagnostic feature in [Previewer](/generativeagent/configuring/previewer) that provides granular visibility into GenerativeAgent's interaction workflow.

  It enables you to diagnose unexpected behaviors, fine-tune instructions, and ensure more predictable and reliable interactions with GenerativeAgent.

  You can inspect:

  * Active Task configuration
  * Current reference variables
  * Instruction parsing
  * Function call context
  * Execution state per turn

  <Frame>
    <img width="300px" src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a9786a9830cb1ef62896cf38fadf9b5c" data-og-width="598" data-og-height="919" data-path="images/generativeagent/TurnInspector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=5412035082402d7db9fc291547ada4c9 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=328366cd8d46b62a62963b463e5a0cd6 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=3d9df75c9e2cc2ca3c09539c97569d5a 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7d49297d2d6cee7f9998b57642135d7f 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=3c2fd6930b78ed835e4c6efec5ec1eb5 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=5a15c51f78cab842527b72035732b48b 2500w" />
  </Frame>

  <Card title="Using the Previewer" href="/generativeagent/configuring/previewer">
    Learn how to use the Previewer to inspect and debug your GenerativeAgent workflows
  </Card>
</Update>

<Update label="2024-10-21 - KB Search">
  ## Knowledge Base Search

  **Knowledge Base Search** enables powerful free-text search across article titles, text, and URLs. The search includes metadata filtering capabilities for content source, creation details, and deployment status.

  This makes it easier to manage and navigate your Knowledge Base.

  <Frame>
    <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearch.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=fb0e3f8cb3d276bd5f8948b281255927" data-og-width="1600" width="1600" data-og-height="909" height="909" data-path="images/generativeagent/KBSearch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearch.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8f7c4d6aa4bed44df50c8b4751771f55 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearch.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c15be8d16805f11ca44de43075a1c95a 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearch.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d9abf6ab8415c7999ebc2605b74d5448 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearch.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=f81ef81b7d5b374a93f076074ec102de 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearch.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=93a7221a1a0e5630ae73867fd1b087e8 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearch.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=83a0fd66a1d3e8eb9de2548874acf487 2500w" />
  </Frame>

  <Tip>
    Users can combine multiple filters with AND operators, maintain search context while navigating, and perform bulk operations on search results.
  </Tip>

  <Card title="Managing Knowledge Base Content" href="/generativeagent/configuring/connecting-your-knowledge-base">
    Learn how to effectively manage and search your Knowledge Base content
  </Card>
</Update>

<Update label="2024-10-03 - KB Article API">
  ## Knowledge Base Article API

  The [Knowledge Base Article API](/apis/knowledge-base/create-a-submission) enables programmatic management of Knowledge Base articles, allowing you to programmatically add and modify articles within the GenerativeAgent Knowledge Base.

  Key use cases include:

  * Integration with private internal knowledge bases not publicly accessible
  * Importing content from non-scrapable sources like Content Management Systems (CMS)
  * Fine-grained programmatic control over knowledge ingestion and management

  <Card title="Article Submission API Documentation" href="/generativeagent/configuring/connecting-your-knowledge-base/add-via-api">Learn how to use the API</Card>
</Update>

<Update label="2024-10-03 - Trial Mode">
  ## Trial Mode

  **Trial Mode** allows you to safely deploy GenerativeAgent use cases by trialing functions in production. When developing AI applications, it's critical to validate how your AI system interacts with external functions and APIs before full deployment. Trial mode provides this safety layer.

  This can allow you to:

  * Ensure GenerativeAgent called the function properly given the conversation context.
  * Ensure GenerativeAgent interpreted the function response.
  * Be protected from unknown API response variations that you might not have accounted for during development and testing.

  <Frame>
    <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738fefcd-4a0f-936d-6456-12a389aac78e.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=22f7582b9d99bdc4b7865b9469cd9bd2" data-og-width="1600" width="1600" data-og-height="788" height="788" data-path="image/uuid-738fefcd-4a0f-936d-6456-12a389aac78e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738fefcd-4a0f-936d-6456-12a389aac78e.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5a2c1e820aaa0f62a37a61d775ff4fda 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738fefcd-4a0f-936d-6456-12a389aac78e.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=9e28640ff786769fb2ba5f752b3e26a1 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738fefcd-4a0f-936d-6456-12a389aac78e.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=aab39f839367c90d738ce142ff1893c7 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738fefcd-4a0f-936d-6456-12a389aac78e.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=7d93de6bd735537fbd2465be2d4e3c08 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738fefcd-4a0f-936d-6456-12a389aac78e.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=00b8ea833bd339451d77cea34c04f0c2 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-738fefcd-4a0f-936d-6456-12a389aac78e.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=a6aa4658ba12fe319187c7c28ff54e37 2500w" />
  </Frame>

  Check out the [Trial Mode guide](/generativeagent/configuring/tasks-and-functions/trial-mode) for more information.
</Update>
