# Source: https://www.jenkins.io/doc/pipeline/steps/

Title: Pipeline Steps Reference

URL Source: https://www.jenkins.io/doc/pipeline/steps/

Markdown Content:
Pipeline Steps Reference
===============

[> User Documentation Home](https://www.jenkins.io/doc/)

##### User Handbook

*   [User Handbook Overview](https://www.jenkins.io/doc/book/getting-started/)
*   [Installing Jenkins](https://www.jenkins.io/doc/book/installing/)
*   [Platform Information](https://www.jenkins.io/doc/book/platform-information/)
*   [Using Jenkins](https://www.jenkins.io/doc/book/using/)
*   [Pipeline](https://www.jenkins.io/doc/book/pipeline/)
*   [Blue Ocean](https://www.jenkins.io/doc/book/blueocean/)
*   [Managing Jenkins](https://www.jenkins.io/doc/book/managing/)
*   [Securing Jenkins](https://www.jenkins.io/doc/book/security/)
*   [System Administration](https://www.jenkins.io/doc/book/system-administration/)
*   [Scaling Jenkins](https://www.jenkins.io/doc/book/scaling/)
*   [Troubleshooting Jenkins](https://www.jenkins.io/doc/book/troubleshooting/)
*   [Glossary](https://www.jenkins.io/doc/book/glossary/)

##### Tutorials

*   [Guided Tour](https://www.jenkins.io/doc/pipeline/tour/getting-started/)
*   [Jenkins Pipeline](https://www.jenkins.io/doc/tutorials#pipeline)
*   [Using Build Tools](https://www.jenkins.io/doc/tutorials#tools)

##### Resources

*   [Pipeline Syntax reference](https://www.jenkins.io/doc/book/pipeline/syntax/)
*   [Pipeline Steps reference](https://www.jenkins.io/doc/pipeline/steps/)
*   [LTS Upgrade guides](https://www.jenkins.io/doc/upgrade-guide/)

Pipeline Steps Reference
========================

The following plugins offer Pipeline-compatible steps. Each plugin link offers more information about the parameters for each step.

Read more about how to integrate steps into your Pipeline in the [Steps](https://www.jenkins.io/doc/book/pipeline/syntax/#declarative-steps) section of the [Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax) page.

*   [.NET SDK Support](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/)
    *   [`dotnetBuild`: .NET: Build project (build)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnetbuild-net-build-project-build)
    *   [`dotnetClean`: .NET: Clean project output (clean)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnetclean-net-clean-project-output-clean)
    *   [`dotnetNuGetDelete`: .NET: Delete/Unlist NuGet package (nuget delete)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnetnugetdelete-net-deleteunlist-nuget-package-nuget-delete)
    *   [`dotnetListPackage`: .NET: Show dependencies (list package)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnetlistpackage-net-show-dependencies-list-package)
    *   [`dotnetNuGetLocals`: .NET: Clear/List NuGet cache locations (nuget locals)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnetnugetlocals-net-clearlist-nuget-cache-locations-nuget-locals)
    *   [`dotnetPack`: .NET: Create NuGet package (pack)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnetpack-net-create-nuget-package-pack)
    *   [`dotnetPublish`: .NET: Publish project (publish)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnetpublish-net-publish-project-publish)
    *   [`dotnetNuGetPush`: .NET: Publish NuGet package (nuget push)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnetnugetpush-net-publish-nuget-package-nuget-push)
    *   [`dotnetTest`: .NET: Run unit tests (test)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnettest-net-run-unit-tests-test)
    *   [`dotnetRestore`: .NET: Restore project dependencies (restore)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnetrestore-net-restore-project-dependencies-restore)
    *   [`dotnetToolRestore`: .NET: Restore local tools (tool restore)](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#dotnettoolrestore-net-restore-local-tools-tool-restore)
    *   [`withDotNet`: With .NET](https://www.jenkins.io/doc/pipeline/steps/dotnet-sdk/#withdotnet-with-net)

*   [1Password Secrets](https://www.jenkins.io/doc/pipeline/steps/onepassword-secrets/)
    *   [`withSecrets`: 1Password Secrets](https://www.jenkins.io/doc/pipeline/steps/onepassword-secrets/#withsecrets-1password-secrets)
    *   [`wrap([$class: 'OnePasswordBuildWrapper'])`: 1Password Secrets](https://www.jenkins.io/doc/pipeline/steps/onepassword-secrets/#wrapclass-onepasswordbuildwrapper-1password-secrets)

*   [42Crunch REST API Static Security Testing](https://www.jenkins.io/doc/pipeline/steps/42crunch-security-audit/)
    *   [`audit`: 42Crunch API Security Audit](https://www.jenkins.io/doc/pipeline/steps/42crunch-security-audit/#audit-42crunch-api-security-audit)

*   [Abap Continuous Integration Plugin](https://www.jenkins.io/doc/pipeline/steps/abap-ci/)
    *   [`abapCi`: ABAP Continuous Integration Plugin](https://www.jenkins.io/doc/pipeline/steps/abap-ci/#abapci-abap-continuous-integration-plugin)

*   [AbsInt Astrée Plugin for Jenkins](https://www.jenkins.io/doc/pipeline/steps/absint-astree/)
    *   [`step([$class: 'AstreeBuilder'])`: Astrée Analysis Run](https://www.jenkins.io/doc/pipeline/steps/absint-astree/#stepclass-astreebuilder-astr%C3%A9e-analysis-run)

*   [AbsInt a³ Jenkins Plugin (deprecated)](https://www.jenkins.io/doc/pipeline/steps/absint-a3/)
    *   [`step([$class: 'A3Builder'])`: a³ Analysis Run](https://www.jenkins.io/doc/pipeline/steps/absint-a3/#stepclass-a3builder-a-analysis-run)

*   [ACCELQ CI-Connect Plugin](https://www.jenkins.io/doc/pipeline/steps/accelq-ci-connect/)
    *   [`step([$class: 'AQPluginBuilderAction'])`: ACCELQ Connect](https://www.jenkins.io/doc/pipeline/steps/accelq-ci-connect/#stepclass-aqpluginbuilderaction-accelq-connect)

*   [Acunetix](https://www.jenkins.io/doc/pipeline/steps/acunetix/)
    *   [`step([$class: 'BuildScanner'])`: Acunetix](https://www.jenkins.io/doc/pipeline/steps/acunetix/#stepclass-buildscanner-acunetix)

*   [Acunetix 360 Scan Plugin](https://www.jenkins.io/doc/pipeline/steps/acunetix-360-scan/)
    *   [`ACXScanBuilder`: Acunetix 360 Scan](https://www.jenkins.io/doc/pipeline/steps/acunetix-360-scan/#acxscanbuilder-acunetix-360-scan)

*   [Add Changes to Build Changelog](https://www.jenkins.io/doc/pipeline/steps/add-changes-to-build-changelog/)
    *   [`addchangestobuildchangelog`: Add Changes to Build Changelog](https://www.jenkins.io/doc/pipeline/steps/add-changes-to-build-changelog/#addchangestobuildchangelog-add-changes-to-build-changelog)

*   [Adobe Cloud Manager Plugin](https://www.jenkins.io/doc/pipeline/steps/adobe-cloud-manager/)
    *   [`acmAdvancePipeline`: Adobe Cloud Manager Advance Pipeline](https://www.jenkins.io/doc/pipeline/steps/adobe-cloud-manager/#acmadvancepipeline-adobe-cloud-manager-advance-pipeline)
    *   [`acmPipelineEnd`: Adobe Cloud Manager Pipeline End](https://www.jenkins.io/doc/pipeline/steps/adobe-cloud-manager/#acmpipelineend-adobe-cloud-manager-pipeline-end)
    *   [`acmPipelineStepState`: Adobe Cloud Manager Pipeline Step State](https://www.jenkins.io/doc/pipeline/steps/adobe-cloud-manager/#acmpipelinestepstate-adobe-cloud-manager-pipeline-step-state)
    *   [`acmPollPipeline`: Poll Adobe Cloud Manager Pipeline](https://www.jenkins.io/doc/pipeline/steps/adobe-cloud-manager/#acmpollpipeline-poll-adobe-cloud-manager-pipeline)
    *   [`acmRepoSync`: Adobe Cloud Manager Repository Sync](https://www.jenkins.io/doc/pipeline/steps/adobe-cloud-manager/#acmreposync-adobe-cloud-manager-repository-sync)
    *   [`acmStartPipeline`: Start Adobe Cloud Manager pipeline](https://www.jenkins.io/doc/pipeline/steps/adobe-cloud-manager/#acmstartpipeline-start-adobe-cloud-manager-pipeline)

*   [Advanced Installer Msi Builder Plugin](https://www.jenkins.io/doc/pipeline/steps/advanced-installer-msi-builder/)
    *   [`advinstBuilder`: Invoke Advanced Installer](https://www.jenkins.io/doc/pipeline/steps/advanced-installer-msi-builder/#advinstbuilder-invoke-advanced-installer)

*   [Agiletestware Pangolin Connector for TestRail](https://www.jenkins.io/doc/pipeline/steps/pangolin-testrail-connector/)
    *   [`pangolinTestRail`: Pangolin: Upload test results into TestRail](https://www.jenkins.io/doc/pipeline/steps/pangolin-testrail-connector/#pangolintestrail-pangolin-upload-test-results-into-testrail)
    *   [`pangolinRunReport`: Pangolin: Run TestRail report](https://www.jenkins.io/doc/pipeline/steps/pangolin-testrail-connector/#pangolinrunreport-pangolin-run-testrail-report)

*   [AIO Tests](https://www.jenkins.io/doc/pipeline/steps/aio-tests/)
    *   [`aioImport`: Publish results to AIO Tests - Jira](https://www.jenkins.io/doc/pipeline/steps/aio-tests/#aioimport-publish-results-to-aio-tests-jira)

*   [Akeyless Plugin](https://www.jenkins.io/doc/pipeline/steps/akeyless/)
    *   [`withAkeyless`: Akeyless Plugin](https://www.jenkins.io/doc/pipeline/steps/akeyless/#withakeyless-akeyless-plugin)
    *   [`wrap([$class: 'AkeylessBuildWrapper'])`: Akeyless Plugin](https://www.jenkins.io/doc/pipeline/steps/akeyless/#wrapclass-akeylessbuildwrapper-akeyless-plugin)

*   [Alauda DevOps Pipeline Plugin](https://www.jenkins.io/doc/pipeline/steps/alauda-devops-pipeline/)
    *   [`base64Decode`: Decode Base64 string](https://www.jenkins.io/doc/pipeline/steps/alauda-devops-pipeline/#base64decode-decode-base64-string)
    *   [`_AcpAction`: Internal utility function for DevOps DSL](https://www.jenkins.io/doc/pipeline/steps/alauda-devops-pipeline/#acpaction-internal-utility-function-for-devops-dsl)
    *   [`_AcpContextInit`: Internal utility function for Devops DSL](https://www.jenkins.io/doc/pipeline/steps/alauda-devops-pipeline/#acpcontextinit-internal-utility-function-for-devops-dsl)
    *   [`_OcWatch`: Internal utility function for Devops DSL](https://www.jenkins.io/doc/pipeline/steps/alauda-devops-pipeline/#ocwatch-internal-utility-function-for-devops-dsl)

*   [Alauda Pipeline Plugin](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/)
    *   [`AlaudaDeleteBuild`: AlaudaDeleteBuild](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudadeletebuild-alaudadeletebuild)
    *   [`alaudaDeployComponent`: Alauda deploy component](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudadeploycomponent-alauda-deploy-component)
    *   [`alaudaDeployService`: Alauda deploy service](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudadeployservice-alauda-deploy-service)
    *   [`alaudaNotify`: AlaudaNotifier](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudanotify-alaudanotifier)
    *   [`alaudaSendNotification`: SendNotification](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudasendnotification-sendnotification)
    *   [`alaudaStartBuild`: alaudaStartBuild](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudastartbuild-alaudastartbuild)
    *   [`AlaudaDeleteBuild`: AlaudaDeleteBuild](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudadeletebuild-alaudadeletebuild)
    *   [`alaudaStartBuild`: alaudaStartBuild](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudastartbuild-alaudastartbuild)
    *   [`alaudaNotify`: AlaudaNotifier](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudanotify-alaudanotifier)
    *   [`alaudaSendNotification`: SendNotification](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudasendnotification-sendnotification)
    *   [`alaudaDeployComponent`: Alauda deploy component](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudadeploycomponent-alauda-deploy-component)
    *   [`alaudaRetrieveComponent`: Retrieve the Component](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudaretrievecomponent-retrieve-the-component)
    *   [`alaudaRetrieveIntegration`: Retrieve the integration](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudaretrieveintegration-retrieve-the-integration)
    *   [`alaudaDeployService`: Alauda deploy service](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudadeployservice-alauda-deploy-service)
    *   [`alaudaRetrieveService`: Retrieve the service](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudaretrieveservice-retrieve-the-service)
    *   [`alaudaRetrieveComponent`: Retrieve the Component](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudaretrievecomponent-retrieve-the-component)
    *   [`alaudaRetrieveIntegration`: Retrieve the integration](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudaretrieveintegration-retrieve-the-integration)
    *   [`alaudaRetrieveService`: Retrieve the service](https://www.jenkins.io/doc/pipeline/steps/alauda-pipeline/#alaudaretrieveservice-retrieve-the-service)

*   [Alibaba Cloud ECS Plugin](https://www.jenkins.io/doc/pipeline/steps/alibabacloud-ecs/)
    *   [`EcsTemplate`: EcsTemplateStep](https://www.jenkins.io/doc/pipeline/steps/alibabacloud-ecs/#ecstemplate-ecstemplatestep)
    *   [`alibabaEcs`: Cloud template provisioning](https://www.jenkins.io/doc/pipeline/steps/alibabacloud-ecs/#alibabaecs-cloud-template-provisioning)

*   [Alibabacloud Package Deployment](https://www.jenkins.io/doc/pipeline/steps/alibabacloud-pkg-deployment/)
    *   [`oosExecuteNotify`: notify oos Execute](https://www.jenkins.io/doc/pipeline/steps/alibabacloud-pkg-deployment/#oosexecutenotify-notify-oos-execute)
    *   [`oosStatusQuery`: query oos execute status](https://www.jenkins.io/doc/pipeline/steps/alibabacloud-pkg-deployment/#oosstatusquery-query-oos-execute-status)
    *   [`ossUploadAndOosExec`: OSS upload built project and OOS execute](https://www.jenkins.io/doc/pipeline/steps/alibabacloud-pkg-deployment/#ossuploadandoosexec-oss-upload-built-project-and-oos-execute)
    *   [`Alibabacloud Automatic Package Deployment`: Alibabacloud Automatic Package Deployment](https://www.jenkins.io/doc/pipeline/steps/alibabacloud-pkg-deployment/#alibabacloud-automatic-package-deployment-alibabacloud-automatic-package-deployment)

*   [Aliyun OSS Uploader](https://www.jenkins.io/doc/pipeline/steps/aliyun-oss-uploader/)
    *   [`aliyunOSSUpload`: Aliyun OSS Upload](https://www.jenkins.io/doc/pipeline/steps/aliyun-oss-uploader/#aliyunossupload-aliyun-oss-upload)

*   [Allure Jenkins Plugin](https://www.jenkins.io/doc/pipeline/steps/allure-jenkins-plugin/)
    *   [`allure`: Allure Report](https://www.jenkins.io/doc/pipeline/steps/allure-jenkins-plugin/#allure-allure-report)

*   [Amazon EC2 plugin](https://www.jenkins.io/doc/pipeline/steps/ec2/)
    *   [`ec2`: Cloud template provisioning](https://www.jenkins.io/doc/pipeline/steps/ec2/#ec2-cloud-template-provisioning)

*   [Amazon Elastic Container Service (ECS) / Fargate plugin](https://www.jenkins.io/doc/pipeline/steps/amazon-ecs/)
    *   [`ecsTaskTemplate`: Define a task template to use in the AWS ECS plugin](https://www.jenkins.io/doc/pipeline/steps/amazon-ecs/#ecstasktemplate-define-a-task-template-to-use-in-the-aws-ecs-plugin)

*   [Amazon Inspector Scanner](https://www.jenkins.io/doc/pipeline/steps/amazon-inspector-image-scanner/)
    *   [`amazonInspector`: Amazon Inspector Scan](https://www.jenkins.io/doc/pipeline/steps/amazon-inspector-image-scanner/#amazoninspector-amazon-inspector-scan)

*   [Anchore Container Image Scanner Plugin](https://www.jenkins.io/doc/pipeline/steps/anchore-container-scanner/)
    *   [`anchore`: Anchore Container Image Scanner](https://www.jenkins.io/doc/pipeline/steps/anchore-container-scanner/#anchore-anchore-container-image-scanner)

*   [Android Emulator Plugin](https://www.jenkins.io/doc/pipeline/steps/android-emulator/)
    *   [`adb`: ADB Executable](https://www.jenkins.io/doc/pipeline/steps/android-emulator/#adb-adb-executable)
    *   [`avdmanager`: AVDManager Script](https://www.jenkins.io/doc/pipeline/steps/android-emulator/#avdmanager-avdmanager-script)
    *   [`emulator`: QEMU Executable](https://www.jenkins.io/doc/pipeline/steps/android-emulator/#emulator-qemu-executable)
    *   [`sdkmanager`: AVDManager Script](https://www.jenkins.io/doc/pipeline/steps/android-emulator/#sdkmanager-avdmanager-script)
    *   [`androidEmulator`: Run an Android emulator during build](https://www.jenkins.io/doc/pipeline/steps/android-emulator/#androidemulator-run-an-android-emulator-during-build)

*   [Android Signing Plugin](https://www.jenkins.io/doc/pipeline/steps/android-signing/)
    *   [`signAndroidApks`: Sign Android APKs](https://www.jenkins.io/doc/pipeline/steps/android-signing/#signandroidapks-sign-android-apks)
    *   [`signAndroidApks`: Sign Android APKs](https://www.jenkins.io/doc/pipeline/steps/android-signing/#signandroidapks-sign-android-apks)

*   [Anka Plugin](https://www.jenkins.io/doc/pipeline/steps/anka-build/)
    *   [`ankaGetSaveImageResult`: Wait for previous save image requests results](https://www.jenkins.io/doc/pipeline/steps/anka-build/#ankagetsaveimageresult-wait-for-previous-save-image-requests-results)
    *   [`createDynamicAnkaNode`: create dynamic anka node](https://www.jenkins.io/doc/pipeline/steps/anka-build/#createdynamicankanode-create-dynamic-anka-node)

*   [Ansible plugin](https://www.jenkins.io/doc/pipeline/steps/ansible/)
    *   [`ansibleAdhoc`: Invoke an ansible adhoc command](https://www.jenkins.io/doc/pipeline/steps/ansible/#ansibleadhoc-invoke-an-ansible-adhoc-command)
    *   [`ansiblePlaybook`: Invoke an ansible playbook](https://www.jenkins.io/doc/pipeline/steps/ansible/#ansibleplaybook-invoke-an-ansible-playbook)
    *   [`ansibleVault`: Invoke ansible vault](https://www.jenkins.io/doc/pipeline/steps/ansible/#ansiblevault-invoke-ansible-vault)
    *   [`step([$class: 'AnsibleAdHocCommandBuilder'])`: Invoke Ansible Ad-Hoc Command](https://www.jenkins.io/doc/pipeline/steps/ansible/#stepclass-ansibleadhoccommandbuilder-invoke-ansible-ad-hoc-command)
    *   [`step([$class: 'AnsiblePlaybookBuilder'])`: Invoke Ansible Playbook](https://www.jenkins.io/doc/pipeline/steps/ansible/#stepclass-ansibleplaybookbuilder-invoke-ansible-playbook)
    *   [`step([$class: 'AnsibleVaultBuilder'])`: Invoke Ansible Vault](https://www.jenkins.io/doc/pipeline/steps/ansible/#stepclass-ansiblevaultbuilder-invoke-ansible-vault)

*   [Ansible Tower Plugin](https://www.jenkins.io/doc/pipeline/steps/ansible-tower/)
    *   [`ansibleTower`: Have Ansible Tower run a job template](https://www.jenkins.io/doc/pipeline/steps/ansible-tower/#ansibletower-have-ansible-tower-run-a-job-template)
    *   [`ansibleTowerProjectRevision`: Have Ansible Tower update a Tower project’s revision](https://www.jenkins.io/doc/pipeline/steps/ansible-tower/#ansibletowerprojectrevision-have-ansible-tower-update-a-tower-projects-revision)
    *   [`ansibleTowerProjectSync`: Have Ansible Tower update a Tower project](https://www.jenkins.io/doc/pipeline/steps/ansible-tower/#ansibletowerprojectsync-have-ansible-tower-update-a-tower-project)

*   [AnsiColor](https://www.jenkins.io/doc/pipeline/steps/ansicolor/)
    *   [`ansiColor`: Color ANSI Console Output](https://www.jenkins.io/doc/pipeline/steps/ansicolor/#ansicolor-color-ansi-console-output)
    *   [`wrap([$class: 'AnsiColorBuildWrapper'])`: Color ANSI Console Output](https://www.jenkins.io/doc/pipeline/steps/ansicolor/#wrapclass-ansicolorbuildwrapper-color-ansi-console-output)

*   [Ant Plugin](https://www.jenkins.io/doc/pipeline/steps/ant/)
    *   [`withAnt`: With Ant](https://www.jenkins.io/doc/pipeline/steps/ant/#withant-with-ant)

*   [Apimap.io](https://www.jenkins.io/doc/pipeline/steps/apimap/)
    *   [`publishAPI`: File content publishing](https://www.jenkins.io/doc/pipeline/steps/apimap/#publishapi-file-content-publishing)
    *   [`validateAPI`: File content validation](https://www.jenkins.io/doc/pipeline/steps/apimap/#validateapi-file-content-validation)

*   [App Center](https://www.jenkins.io/doc/pipeline/steps/appcenter/)
    *   [`appCenter`: Upload app to AppCenter](https://www.jenkins.io/doc/pipeline/steps/appcenter/#appcenter-upload-app-to-appcenter)

*   [App-Ray Security check plugin](https://www.jenkins.io/doc/pipeline/steps/appray/)
    *   [`appray`: App-Ray security check](https://www.jenkins.io/doc/pipeline/steps/appray/#appray-app-ray-security-check)

*   [Appcircle Enterprise App Store](https://www.jenkins.io/doc/pipeline/steps/appcircle-enterprise-store/)
    *   [`appcircleEnterpriseAppStore`: Appcircle Enterprise App Store](https://www.jenkins.io/doc/pipeline/steps/appcircle-enterprise-store/#appcircleenterpriseappstore-appcircle-enterprise-app-store)

*   [Appcircle Testing Distribution](https://www.jenkins.io/doc/pipeline/steps/appcircle-testing-distribution/)
    *   [`appcircleTestingDistribution`: Appcircle Testing Distribution](https://www.jenkins.io/doc/pipeline/steps/appcircle-testing-distribution/#appcircletestingdistribution-appcircle-testing-distribution)

*   [Appdome Build-2secure](https://www.jenkins.io/doc/pipeline/steps/appdome-build-2secure/)
    *   [`AppdomeBuilder`: Appdome Build-2secure](https://www.jenkins.io/doc/pipeline/steps/appdome-build-2secure/#appdomebuilder-appdome-build-2secure)

*   [Appdome Validate-2secure](https://www.jenkins.io/doc/pipeline/steps/appdome-validate-2secure/)
    *   [`AppdomeValidator`: Appdome Validate-2secure](https://www.jenkins.io/doc/pipeline/steps/appdome-validate-2secure/#appdomevalidator-appdome-validate-2secure)

*   [Appknox Security Scanner](https://www.jenkins.io/doc/pipeline/steps/appknox-scanner/)
    *   [`appKnoxScanner`: Appknox Security Scanner](https://www.jenkins.io/doc/pipeline/steps/appknox-scanner/#appknoxscanner-appknox-security-scanner)

*   [Applatix](https://www.jenkins.io/doc/pipeline/steps/applatix/)
    *   [`applatix`: Applatix System Integration](https://www.jenkins.io/doc/pipeline/steps/applatix/#applatix-applatix-system-integration)

*   [Applitools Eyes Plugin](https://www.jenkins.io/doc/pipeline/steps/applitools-eyes/)
    *   [`Applitools`: Applitools Support](https://www.jenkins.io/doc/pipeline/steps/applitools-eyes/#applitools-applitools-support)

*   [Apprenda Plugin](https://www.jenkins.io/doc/pipeline/steps/apprenda/)
    *   [`step([$class: 'ApprendaBuilder'])`: Deploy to Apprenda](https://www.jenkins.io/doc/pipeline/steps/apprenda/#stepclass-apprendabuilder-deploy-to-apprenda)

*   [Aqua MicroScanner](https://www.jenkins.io/doc/pipeline/steps/aqua-microscanner/)
    *   [`aquaMicroscanner`: Aqua MicroScanner](https://www.jenkins.io/doc/pipeline/steps/aqua-microscanner/#aquamicroscanner-aqua-microscanner)

*   [Aqua Security Scanner](https://www.jenkins.io/doc/pipeline/steps/aqua-security-scanner/)
    *   [`aqua`: Aqua Security](https://www.jenkins.io/doc/pipeline/steps/aqua-security-scanner/#aqua-aqua-security)

*   [Aqua Security Serverless Scanner](https://www.jenkins.io/doc/pipeline/steps/aqua-serverless/)
    *   [`aquaServerlessScanner`: Aqua Serverless Security](https://www.jenkins.io/doc/pipeline/steps/aqua-serverless/#aquaserverlessscanner-aqua-serverless-security)

*   [Arachni Scanner Plugin](https://www.jenkins.io/doc/pipeline/steps/arachni-scanner/)
    *   [`arachniScanner`: Arachni Scanner](https://www.jenkins.io/doc/pipeline/steps/arachni-scanner/#arachniscanner-arachni-scanner)

*   [aRESTocats Plugin](https://www.jenkins.io/doc/pipeline/steps/arestocats/)
    *   [`arestocats`: aRESTocats](https://www.jenkins.io/doc/pipeline/steps/arestocats/#arestocats-arestocats)

*   [Aristiun Aribot](https://www.jenkins.io/doc/pipeline/steps/aribot/)
    *   [`aribot`: Aristiun Aribot](https://www.jenkins.io/doc/pipeline/steps/aribot/#aribot-aristiun-aribot)

*   [ArmorCode Release Gate](https://www.jenkins.io/doc/pipeline/steps/armorcode-release-gate/)
    *   [`armorcodeReleaseGate`: ArmorCode Release Gate](https://www.jenkins.io/doc/pipeline/steps/armorcode-release-gate/#armorcodereleasegate-armorcode-release-gate)

*   [artifact-promotion](https://www.jenkins.io/doc/pipeline/steps/artifact-promotion/)
    *   [`artifactPromotion`: ArtifactPromotionStep](https://www.jenkins.io/doc/pipeline/steps/artifact-promotion/#artifactpromotion-artifactpromotionstep)
    *   [`step([$class: 'ArtifactPromotionBuilder'])`: Single Artifact Promotion](https://www.jenkins.io/doc/pipeline/steps/artifact-promotion/#stepclass-artifactpromotionbuilder-single-artifact-promotion)

*   [Artifactory Plugin](https://www.jenkins.io/doc/pipeline/steps/artifactory/)
    *   [`ArtifactoryGradleBuild`: run Artifactory gradle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorygradlebuild-run-artifactory-gradle)
    *   [`MavenDescriptorStep`: Get Artifactory Maven descriptor](https://www.jenkins.io/doc/pipeline/steps/artifactory/#mavendescriptorstep-get-artifactory-maven-descriptor)
    *   [`addInteractivePromotion`: Add interactive promotion](https://www.jenkins.io/doc/pipeline/steps/artifactory/#addinteractivepromotion-add-interactive-promotion)
    *   [`artifactoryBuildTrigger`: Trigger Artifactory build](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorybuildtrigger-trigger-artifactory-build)
    *   [`artifactoryDistributeBuild`: Distribute build](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorydistributebuild-distribute-build)
    *   [`artifactoryDownload`: Download artifacts](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorydownload-download-artifacts)
    *   [`artifactoryEditProps`: Edit properties](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactoryeditprops-edit-properties)
    *   [`artifactoryGoPublish`: Run Artifactory Go Publish command](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorygopublish-run-artifactory-go-publish-command)
    *   [`artifactoryGoRun`: Run Artifactory Go command](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorygorun-run-artifactory-go-command)
    *   [`artifactoryMavenBuild`: run Artifactory maven](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorymavenbuild-run-artifactory-maven)
    *   [`artifactoryNpmCi`: Run Artifactory npm ci](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorynpmci-run-artifactory-npm-ci)
    *   [`artifactoryNpmInstall`: Run Artifactory npm install](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorynpminstall-run-artifactory-npm-install)
    *   [`artifactoryNpmPublish`: Run Artifactory npm publish](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorynpmpublish-run-artifactory-npm-publish)
    *   [`artifactoryNugetRun`: Run Artifactory NuGet](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorynugetrun-run-artifactory-nuget)
    *   [`artifactoryPipRun`: Run Artifactory pip install](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorypiprun-run-artifactory-pip-install)
    *   [`artifactoryPromoteBuild`: Promote build](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactorypromotebuild-promote-build)
    *   [`artifactoryUpload`: Upload artifacts](https://www.jenkins.io/doc/pipeline/steps/artifactory/#artifactoryupload-upload-artifacts)
    *   [`buildAppend`: Build append](https://www.jenkins.io/doc/pipeline/steps/artifactory/#buildappend-build-append)
    *   [`collectEnv`: Collect environment variables and system properties](https://www.jenkins.io/doc/pipeline/steps/artifactory/#collectenv-collect-environment-variables-and-system-properties)
    *   [`collectIssues`: Collect issues from git and add them to a build](https://www.jenkins.io/doc/pipeline/steps/artifactory/#collectissues-collect-issues-from-git-and-add-them-to-a-build)
    *   [`conanAddRemote`: Add new repo to Conan config](https://www.jenkins.io/doc/pipeline/steps/artifactory/#conanaddremote-add-new-repo-to-conan-config)
    *   [`conanAddUser`: Add new user to Conan config](https://www.jenkins.io/doc/pipeline/steps/artifactory/#conanadduser-add-new-user-to-conan-config)
    *   [`createDockerBuildStep`: Artifactory create Docker build](https://www.jenkins.io/doc/pipeline/steps/artifactory/#createdockerbuildstep-artifactory-create-docker-build)
    *   [`createReleaseBundle`: Create a release bundle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#createreleasebundle-create-a-release-bundle)
    *   [`deleteReleaseBundle`: Delete a release bundle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#deletereleasebundle-delete-a-release-bundle)
    *   [`deployArtifacts`: Deploy artifacts](https://www.jenkins.io/doc/pipeline/steps/artifactory/#deployartifacts-deploy-artifacts)
    *   [`distributeReleaseBundle`: Distribute a release bundle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#distributereleasebundle-distribute-a-release-bundle)
    *   [`dockerPullStep`: Artifactory docker pull](https://www.jenkins.io/doc/pipeline/steps/artifactory/#dockerpullstep-artifactory-docker-pull)
    *   [`dockerPushStep`: Artifactory docker push](https://www.jenkins.io/doc/pipeline/steps/artifactory/#dockerpushstep-artifactory-docker-push)
    *   [`dsCreateReleaseBundle`: Create release bundle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#dscreatereleasebundle-create-release-bundle)
    *   [`dsDeleteReleaseBundle`: Delete a release bundle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#dsdeletereleasebundle-delete-a-release-bundle)
    *   [`dsDistributeReleaseBundle`: Distribute a release bundle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#dsdistributereleasebundle-distribute-a-release-bundle)
    *   [`dsSignReleaseBundle`: Sign a release bundle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#dssignreleasebundle-sign-a-release-bundle)
    *   [`dsUpdateReleaseBundle`: Update a release bundle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#dsupdatereleasebundle-update-a-release-bundle)
    *   [`getArtifactoryServer`: Get Artifactory server from Jenkins config](https://www.jenkins.io/doc/pipeline/steps/artifactory/#getartifactoryserver-get-artifactory-server-from-jenkins-config)
    *   [`getJFrogPlatformInstance`: Get JFrog Platform instance from Jenkins config](https://www.jenkins.io/doc/pipeline/steps/artifactory/#getjfrogplatforminstance-get-jfrog-platform-instance-from-jenkins-config)
    *   [`initConanClient`: Create Conan Client](https://www.jenkins.io/doc/pipeline/steps/artifactory/#initconanclient-create-conan-client)
    *   [`jfPipelines`: Set output resources and report results for JFrog Pipelines](https://www.jenkins.io/doc/pipeline/steps/artifactory/#jfpipelines-set-output-resources-and-report-results-for-jfrog-pipelines)
    *   [`jfrogInstance`: Creates new JFrog instance](https://www.jenkins.io/doc/pipeline/steps/artifactory/#jfroginstance-creates-new-jfrog-instance)
    *   [`newArtifactoryServer`: Returns new Artifactory server](https://www.jenkins.io/doc/pipeline/steps/artifactory/#newartifactoryserver-returns-new-artifactory-server)
    *   [`newBuildInfo`: New buildInfo](https://www.jenkins.io/doc/pipeline/steps/artifactory/#newbuildinfo-new-buildinfo)
    *   [`newGoBuild`: New Artifactory Go](https://www.jenkins.io/doc/pipeline/steps/artifactory/#newgobuild-new-artifactory-go)
    *   [`newGradleBuild`: New Artifactory gradle executor](https://www.jenkins.io/doc/pipeline/steps/artifactory/#newgradlebuild-new-artifactory-gradle-executor)
    *   [`newJFrogPlatformInstance`: Returns new JFrog platform instance](https://www.jenkins.io/doc/pipeline/steps/artifactory/#newjfrogplatforminstance-returns-new-jfrog-platform-instance)
    *   [`newMavenBuild`: New Artifactory maven](https://www.jenkins.io/doc/pipeline/steps/artifactory/#newmavenbuild-new-artifactory-maven)
    *   [`newNpmBuild`: New Artifactory npm executor](https://www.jenkins.io/doc/pipeline/steps/artifactory/#newnpmbuild-new-artifactory-npm-executor)
    *   [`newNugetBuild`: New Artifactory NuGet executor](https://www.jenkins.io/doc/pipeline/steps/artifactory/#newnugetbuild-new-artifactory-nuget-executor)
    *   [`newPipBuild`: New Artifactory pip executor](https://www.jenkins.io/doc/pipeline/steps/artifactory/#newpipbuild-new-artifactory-pip-executor)
    *   [`publishBuildInfo`: Publish build Info to Artifactory](https://www.jenkins.io/doc/pipeline/steps/artifactory/#publishbuildinfo-publish-build-info-to-artifactory)
    *   [`rtAddInteractivePromotion`: Add interactive promotion](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtaddinteractivepromotion-add-interactive-promotion)
    *   [`rtBuildAppend`: Build append](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtbuildappend-build-append)
    *   [`rtBuildInfo`: Create build info](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtbuildinfo-create-build-info)
    *   [`rtBuildTrigger`: Trigger Artifactory build](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtbuildtrigger-trigger-artifactory-build)
    *   [`rtCollectIssues`: Collect issues](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtcollectissues-collect-issues)
    *   [`rtConanClient`: Creates new Conan client](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtconanclient-creates-new-conan-client)
    *   [`rtConanRemote`: Add new repo to Conan config](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtconanremote-add-new-repo-to-conan-config)
    *   [`rtConanRun`: Run a Conan command](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtconanrun-run-a-conan-command)
    *   [`rtCreateDockerBuild`: run Artifactory create Docker build](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtcreatedockerbuild-run-artifactory-create-docker-build)
    *   [`rtDeleteProps`: Delete properties](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtdeleteprops-delete-properties)
    *   [`rtDockerPull`: run Artifactory docker pull](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtdockerpull-run-artifactory-docker-pull)
    *   [`rtDockerPush`: run Artifactory docker push](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtdockerpush-run-artifactory-docker-push)
    *   [`rtDotnetResolver`: set .NET resolver](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtdotnetresolver-set-net-resolver)
    *   [`rtDotnetRun`: run Artifactory .NET](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtdotnetrun-run-artifactory-net)
    *   [`rtDownload`: Download artifacts](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtdownload-download-artifacts)
    *   [`rtGoDeployer`: set go deployer](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtgodeployer-set-go-deployer)
    *   [`rtGoPublish`: run Artifactory Go publish](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtgopublish-run-artifactory-go-publish)
    *   [`rtGoResolver`: set Go resolver](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtgoresolver-set-go-resolver)
    *   [`rtGoRun`: run Artifactory Go publish](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtgorun-run-artifactory-go-publish)
    *   [`rtGradleDeployer`: set gradle deployer](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtgradledeployer-set-gradle-deployer)
    *   [`rtGradleResolver`: set gradle resolver](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtgradleresolver-set-gradle-resolver)
    *   [`rtGradleRun`: run Artifactory gradle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtgradlerun-run-artifactory-gradle)
    *   [`rtMavenDeployer`: set maven deployer](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtmavendeployer-set-maven-deployer)
    *   [`rtMavenResolver`: set maven resolver](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtmavenresolver-set-maven-resolver)
    *   [`rtMavenRun`: run Artifactory maven](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtmavenrun-run-artifactory-maven)
    *   [`rtNpmCi`: run Artifactory npm ci](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtnpmci-run-artifactory-npm-ci)
    *   [`rtNpmDeployer`: set npm deployer](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtnpmdeployer-set-npm-deployer)
    *   [`rtNpmInstall`: run Artifactory npm install](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtnpminstall-run-artifactory-npm-install)
    *   [`rtNpmPublish`: run Artifactory npm publish](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtnpmpublish-run-artifactory-npm-publish)
    *   [`rtNpmResolver`: set npm resolver](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtnpmresolver-set-npm-resolver)
    *   [`rtNugetResolver`: set NuGet resolver](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtnugetresolver-set-nuget-resolver)
    *   [`rtNugetRun`: run Artifactory NuGet](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtnugetrun-run-artifactory-nuget)
    *   [`rtPipInstall`: run Artifactory pip install](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtpipinstall-run-artifactory-pip-install)
    *   [`rtPipResolver`: set pip resolver](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtpipresolver-set-pip-resolver)
    *   [`rtPromote`: Promote build](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtpromote-promote-build)
    *   [`rtPublishBuildInfo`: Publish build info](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtpublishbuildinfo-publish-build-info)
    *   [`rtServer`: Creates new Artifactory server](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtserver-creates-new-artifactory-server)
    *   [`rtSetProps`: Set properties](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtsetprops-set-properties)
    *   [`rtUpload`: Upload artifacts](https://www.jenkins.io/doc/pipeline/steps/artifactory/#rtupload-upload-artifacts)
    *   [`runConanCommand`: Run a Conan command](https://www.jenkins.io/doc/pipeline/steps/artifactory/#runconancommand-run-a-conan-command)
    *   [`signReleaseBundle`: Sign a release bundle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#signreleasebundle-sign-a-release-bundle)
    *   [`updateReleaseBundle`: Update a release bundle](https://www.jenkins.io/doc/pipeline/steps/artifactory/#updatereleasebundle-update-a-release-bundle)
    *   [`xrayScan`: run Xray scan](https://www.jenkins.io/doc/pipeline/steps/artifactory/#xrayscan-run-xray-scan)
    *   [`xrayScanBuild`: Xray build scanning](https://www.jenkins.io/doc/pipeline/steps/artifactory/#xrayscanbuild-xray-build-scanning)

*   [Artifactz.io Plugin](https://www.jenkins.io/doc/pipeline/steps/artifactz/)
    *   [`publishArtifact`: Publish Artifact Version](https://www.jenkins.io/doc/pipeline/steps/artifactz/#publishartifact-publish-artifact-version)
    *   [`pushArtifact`: Push Artifact Version](https://www.jenkins.io/doc/pipeline/steps/artifactz/#pushartifact-push-artifact-version)
    *   [`retrieveArtifacts`: Retrieve Artifact Versions](https://www.jenkins.io/doc/pipeline/steps/artifactz/#retrieveartifacts-retrieve-artifact-versions)
    *   [`artifactVersion`: Send Artifact Version To Artifactor Web Service Deprecated](https://www.jenkins.io/doc/pipeline/steps/artifactz/#artifactversion-send-artifact-version-to-artifactor-web-service-deprecated)
    *   [`artifactVersion`: Push Artifact Version to the next stage in the flow Deprecated](https://www.jenkins.io/doc/pipeline/steps/artifactz/#artifactversion-push-artifact-version-to-the-next-stage-in-the-flow-deprecated)
    *   [`artifactVersion`: Send Artifact Version To Artifactor Web Service](https://www.jenkins.io/doc/pipeline/steps/artifactz/#artifactversion-send-artifact-version-to-artifactor-web-service)
    *   [`artifactVersion`: Push Artifact Version to the next stage in the flow](https://www.jenkins.io/doc/pipeline/steps/artifactz/#artifactversion-push-artifact-version-to-the-next-stage-in-the-flow)
    *   [`step([$class: 'RetrieveArtifactsBuildStep'])`: Retrieve Artifact version for stage](https://www.jenkins.io/doc/pipeline/steps/artifactz/#stepclass-retrieveartifactsbuildstep-retrieve-artifact-version-for-stage)

*   [AssertThat BDD Jira Plugin](https://www.jenkins.io/doc/pipeline/steps/assertthat-bdd-jira/)
    *   [`assertthatBddFeatures`: Download AssertThat features](https://www.jenkins.io/doc/pipeline/steps/assertthat-bdd-jira/#assertthatbddfeatures-download-assertthat-features)
    *   [`assertthatBddReport`: Upload AssertThat report](https://www.jenkins.io/doc/pipeline/steps/assertthat-bdd-jira/#assertthatbddreport-upload-assertthat-report)

*   [Atlassian Jira Software Cloud](https://www.jenkins.io/doc/pipeline/steps/atlassian-jira-software-cloud/)
    *   [`checkGatingStatus`: Atlassian Jira Service Desk Software Cloud Jenkins Integration (Deployment Gating)](https://www.jenkins.io/doc/pipeline/steps/atlassian-jira-software-cloud/#checkgatingstatus-atlassian-jira-service-desk-software-cloud-jenkins-integration-deployment-gating)
    *   [`jiraSendBuildInfo`: Atlassian Jira Software Cloud Jenkins Integration (Build)](https://www.jenkins.io/doc/pipeline/steps/atlassian-jira-software-cloud/#jirasendbuildinfo-atlassian-jira-software-cloud-jenkins-integration-build)
    *   [`jiraSendDeploymentInfo`: Atlassian Jira Software Cloud Jenkins Integration (Deployment)](https://www.jenkins.io/doc/pipeline/steps/atlassian-jira-software-cloud/#jirasenddeploymentinfo-atlassian-jira-software-cloud-jenkins-integration-deployment)
    *   [`step([$class: 'FreeStylePostBuildStep'])`: Send build information to Jira](https://www.jenkins.io/doc/pipeline/steps/atlassian-jira-software-cloud/#stepclass-freestylepostbuildstep-send-build-information-to-jira)

*   [Autify Plugin](https://www.jenkins.io/doc/pipeline/steps/autify/)
    *   [`autifyMobile`: Run test on Autify for Mobile](https://www.jenkins.io/doc/pipeline/steps/autify/#autifymobile-run-test-on-autify-for-mobile)
    *   [`autifyMobileUpload`: Upload build to Autify for Mobile](https://www.jenkins.io/doc/pipeline/steps/autify/#autifymobileupload-upload-build-to-autify-for-mobile)
    *   [`autifyWeb`: Run test on Autify for Web](https://www.jenkins.io/doc/pipeline/steps/autify/#autifyweb-run-test-on-autify-for-web)

*   [AutoAction Plugin](https://www.jenkins.io/doc/pipeline/steps/autoaction-step/)
    *   [`chlAtuoAction`: Run AutoAction](https://www.jenkins.io/doc/pipeline/steps/autoaction-step/#chlatuoaction-run-autoaction)

*   [Autocancel Plugin](https://www.jenkins.io/doc/pipeline/steps/autocancel/)
    *   [`autocancelBranchBuildsOnPullRequestBuilds`: Autocancel branch builds on pull request builds](https://www.jenkins.io/doc/pipeline/steps/autocancel/#autocancelbranchbuildsonpullrequestbuilds-autocancel-branch-builds-on-pull-request-builds)
    *   [`autocancelConsecutiveBuilds`: Autocancel consecutive builds](https://www.jenkins.io/doc/pipeline/steps/autocancel/#autocancelconsecutivebuilds-autocancel-consecutive-builds)

*   [Autograding Plugin](https://www.jenkins.io/doc/pipeline/steps/autograding/)
    *   [`autoGrade`: Autograde project](https://www.jenkins.io/doc/pipeline/steps/autograding/#autograde-autograde-project)

*   [AWS Beanstalk Releaser](https://www.jenkins.io/doc/pipeline/steps/aws-beanstalk-releaser/)
    *   [`awsebReleaser`: AWS Elastic Beanstalk Releaser](https://www.jenkins.io/doc/pipeline/steps/aws-beanstalk-releaser/#awsebreleaser-aws-elastic-beanstalk-releaser)

*   [AWS CodeBuild Plugin](https://www.jenkins.io/doc/pipeline/steps/aws-codebuild/)
    *   [`awsCodeBuild`: Invoke an AWS CodeBuild build](https://www.jenkins.io/doc/pipeline/steps/aws-codebuild/#awscodebuild-invoke-an-aws-codebuild-build)
    *   [`step([$class: 'CodeBuilder'])`: AWS CodeBuild](https://www.jenkins.io/doc/pipeline/steps/aws-codebuild/#stepclass-codebuilder-aws-codebuild)

*   [AWS CodeDeploy Plugin for Jenkins](https://www.jenkins.io/doc/pipeline/steps/codedeploy/)
    *   [`step([$class: 'AWSCodeDeployPublisher'])`: Deploy an application to AWS CodeDeploy](https://www.jenkins.io/doc/pipeline/steps/codedeploy/#stepclass-awscodedeploypublisher-deploy-an-application-to-aws-codedeploy)

*   [AWS Lambda Plugin](https://www.jenkins.io/doc/pipeline/steps/aws-lambda/)
    *   [`eventSourceLambda`: AWS Lambda eventsource mapping](https://www.jenkins.io/doc/pipeline/steps/aws-lambda/#eventsourcelambda-aws-lambda-eventsource-mapping)
    *   [`invokeLambda`: AWS Lambda invocation](https://www.jenkins.io/doc/pipeline/steps/aws-lambda/#invokelambda-aws-lambda-invocation)
    *   [`publishLambda`: AWS Lambda publish new version and update alias](https://www.jenkins.io/doc/pipeline/steps/aws-lambda/#publishlambda-aws-lambda-publish-new-version-and-update-alias)
    *   [`deployLambda`: AWS Lambda deployment](https://www.jenkins.io/doc/pipeline/steps/aws-lambda/#deploylambda-aws-lambda-deployment)

*   [AWS Parameter Store Build Wrapper](https://www.jenkins.io/doc/pipeline/steps/aws-parameter-store/)
    *   [`withAWSParameterStore`: With AWS Parameter Store](https://www.jenkins.io/doc/pipeline/steps/aws-parameter-store/#withawsparameterstore-with-aws-parameter-store)

*   [AWS SAM](https://www.jenkins.io/doc/pipeline/steps/aws-sam/)
    *   [`samDeploy`: AWS SAM deploy application](https://www.jenkins.io/doc/pipeline/steps/aws-sam/#samdeploy-aws-sam-deploy-application)

*   [aws-device-farm](https://www.jenkins.io/doc/pipeline/steps/aws-device-farm/)
    *   [`devicefarm`: Run Tests on AWS Device Farm](https://www.jenkins.io/doc/pipeline/steps/aws-device-farm/#devicefarm-run-tests-on-aws-device-farm)

*   [AWSEB Deployment Plugin](https://www.jenkins.io/doc/pipeline/steps/awseb-deployment-plugin/)
    *   [`step([$class: 'AWSEBDeploymentBuilder'])`: AWS Elastic Beanstalk](https://www.jenkins.io/doc/pipeline/steps/awseb-deployment-plugin/#stepclass-awsebdeploymentbuilder-aws-elastic-beanstalk)

*   [Azure App Service Plugin](https://www.jenkins.io/doc/pipeline/steps/azure-app-service/)
    *   [`azureWebAppPublish`: Publish an Azure Web App](https://www.jenkins.io/doc/pipeline/steps/azure-app-service/#azurewebapppublish-publish-an-azure-web-app)
    *   [`azureWebAppSwapSlots`: Swap slots for an Azure Web App](https://www.jenkins.io/doc/pipeline/steps/azure-app-service/#azurewebappswapslots-swap-slots-for-an-azure-web-app)

*   [Azure Container Registry Tasks Plugin](https://www.jenkins.io/doc/pipeline/steps/azure-container-registry-tasks/)
    *   [`acrQuickTask`: Queue an ACR Quick Task](https://www.jenkins.io/doc/pipeline/steps/azure-container-registry-tasks/#acrquicktask-queue-an-acr-quick-task)

*   [Azure Container Service Plugin](https://www.jenkins.io/doc/pipeline/steps/azure-acs/)
    *   [`acsDeploy`: Deploy to Azure Container Service (AKS)](https://www.jenkins.io/doc/pipeline/steps/azure-acs/#acsdeploy-deploy-to-azure-container-service-aks)
    *   [`step([$class: 'ACSDeploymentBuilder'])`: Deploy to Azure Container Service (AKS)](https://www.jenkins.io/doc/pipeline/steps/azure-acs/#stepclass-acsdeploymentbuilder-deploy-to-azure-container-service-aks)

*   [Azure Cosmos DB Plugin](https://www.jenkins.io/doc/pipeline/steps/azure-cosmosdb/)
    *   [`azureCosmosDBCreateDocument`: Create document in Azure Cosmos DB](https://www.jenkins.io/doc/pipeline/steps/azure-cosmosdb/#azurecosmosdbcreatedocument-create-document-in-azure-cosmos-db)

*   [Azure Function Plugin](https://www.jenkins.io/doc/pipeline/steps/azure-function/)
    *   [`azureFunctionAppPublish`: Publish an Azure Function App](https://www.jenkins.io/doc/pipeline/steps/azure-function/#azurefunctionapppublish-publish-an-azure-function-app)

*   [Azure Key Vault Plugin](https://www.jenkins.io/doc/pipeline/steps/azure-keyvault/)
    *   [`azureKeyVault`: Bind credentials in Azure Key Vault to environment variables](https://www.jenkins.io/doc/pipeline/steps/azure-keyvault/#azurekeyvault-bind-credentials-in-azure-key-vault-to-environment-variables)
    *   [`withAzureKeyvault`: Bind credentials in Azure Key Vault to environment variables](https://www.jenkins.io/doc/pipeline/steps/azure-keyvault/#withazurekeyvault-bind-credentials-in-azure-key-vault-to-environment-variables)

*   [Azure Service Fabric Plugin](https://www.jenkins.io/doc/pipeline/steps/service-fabric/)
    *   [`azureServiceFabricPublish`: Deploy Service Fabric Project](https://www.jenkins.io/doc/pipeline/steps/service-fabric/#azureservicefabricpublish-deploy-service-fabric-project)
    *   [`step([$class: 'ServiceFabricPublisher'])`: Deploy Service Fabric Project](https://www.jenkins.io/doc/pipeline/steps/service-fabric/#stepclass-servicefabricpublisher-deploy-service-fabric-project)

*   [Azure Storage plugin](https://www.jenkins.io/doc/pipeline/steps/windows-azure-storage/)
    *   [`azureDownload`: Download from Azure storage](https://www.jenkins.io/doc/pipeline/steps/windows-azure-storage/#azuredownload-download-from-azure-storage)
    *   [`azureUpload`: Upload artifacts to Azure Storage](https://www.jenkins.io/doc/pipeline/steps/windows-azure-storage/#azureupload-upload-artifacts-to-azure-storage)

*   [Azure Virtual Machine Scale Set Plugin](https://www.jenkins.io/doc/pipeline/steps/azure-vmss/)
    *   [`azureVMSSUpdateInstances`: Update Azure Virtual Machine Scale Set Instances](https://www.jenkins.io/doc/pipeline/steps/azure-vmss/#azurevmssupdateinstances-update-azure-virtual-machine-scale-set-instances)
    *   [`azureVMSSUpdate`: Update Azure Virtual Machine Scale Set](https://www.jenkins.io/doc/pipeline/steps/azure-vmss/#azurevmssupdate-update-azure-virtual-machine-scale-set)

*   [Backlog plugin](https://www.jenkins.io/doc/pipeline/steps/backlog/)
    *   [`backlogPullRequest`: Notify Pull Request on Backlog](https://www.jenkins.io/doc/pipeline/steps/backlog/#backlogpullrequest-notify-pull-request-on-backlog)

*   [Badge](https://www.jenkins.io/doc/pipeline/steps/badge/)
    *   [`addBadge`: Add Badge](https://www.jenkins.io/doc/pipeline/steps/badge/#addbadge-add-badge)
    *   [`addErrorBadge`: Add Error Badge](https://www.jenkins.io/doc/pipeline/steps/badge/#adderrorbadge-add-error-badge)
    *   [`addInfoBadge`: Add Info Badge](https://www.jenkins.io/doc/pipeline/steps/badge/#addinfobadge-add-info-badge)
    *   [`addSummary`: Add Summary](https://www.jenkins.io/doc/pipeline/steps/badge/#addsummary-add-summary)
    *   [`addWarningBadge`: Add Warning Badge](https://www.jenkins.io/doc/pipeline/steps/badge/#addwarningbadge-add-warning-badge)
    *   [`removeBadges`: Remove Badges](https://www.jenkins.io/doc/pipeline/steps/badge/#removebadges-remove-badges)
    *   [`removeSummaries`: Remove Summaries](https://www.jenkins.io/doc/pipeline/steps/badge/#removesummaries-remove-summaries)
    *   [`addHtmlBadge`: Add a HTML Badge](https://www.jenkins.io/doc/pipeline/steps/badge/#addhtmlbadge-add-a-html-badge)
    *   [`addShortText`: Add Short Text](https://www.jenkins.io/doc/pipeline/steps/badge/#addshorttext-add-short-text)
    *   [`createSummary`: Create Summary](https://www.jenkins.io/doc/pipeline/steps/badge/#createsummary-create-summary)
    *   [`removeHtmlBadges`: Remove HTML Badges](https://www.jenkins.io/doc/pipeline/steps/badge/#removehtmlbadges-remove-html-badges)

*   [Beagle Security](https://www.jenkins.io/doc/pipeline/steps/beagle-security/)
    *   [`step([$class: 'BeaglePlugin'])`: Trigger Beagle Penetration Testing](https://www.jenkins.io/doc/pipeline/steps/beagle-security/#stepclass-beagleplugin-trigger-beagle-penetration-testing)

*   [Benchmark Evaluator Plugin](https://www.jenkins.io/doc/pipeline/steps/benchmark-evaluator/)
    *   [`benchmark`: Benchmark](https://www.jenkins.io/doc/pipeline/steps/benchmark-evaluator/#benchmark-benchmark)

*   [Benchmark Plugin](https://www.jenkins.io/doc/pipeline/steps/benchmark/)
    *   [`benchmark`: Benchmark results](https://www.jenkins.io/doc/pipeline/steps/benchmark/#benchmark-benchmark-results)

*   [BeVigil CI Plugin](https://www.jenkins.io/doc/pipeline/steps/bevigil-ci/)
    *   [`greet`: Scan your app with BeVigil CI](https://www.jenkins.io/doc/pipeline/steps/bevigil-ci/#greet-scan-your-app-with-bevigil-ci)

*   [Bitbar Run-in-Cloud Plugin](https://www.jenkins.io/doc/pipeline/steps/testdroid-run-in-cloud/)
    *   [`runInCloud`: Start a run in Bitbar Cloud](https://www.jenkins.io/doc/pipeline/steps/testdroid-run-in-cloud/#runincloud-start-a-run-in-bitbar-cloud)

*   [Bitbucket Build Status Notifier Plugin](https://www.jenkins.io/doc/pipeline/steps/bitbucket-build-status-notifier/)
    *   [`bitbucketStatusNotify`: Notify a build status to BitBucket.](https://www.jenkins.io/doc/pipeline/steps/bitbucket-build-status-notifier/#bitbucketstatusnotify-notify-a-build-status-to-bitbucket)

*   [Bitbucket Server Integration](https://www.jenkins.io/doc/pipeline/steps/atlassian-bitbucket-server-integration/)
    *   [`bbs_checkout`: BitbucketSCMStep](https://www.jenkins.io/doc/pipeline/steps/atlassian-bitbucket-server-integration/#bbs-checkout-bitbucketscmstep)
    *   [`bbs_deploy`: Wrapper step to notify Bitbucket Server of the deployment status.](https://www.jenkins.io/doc/pipeline/steps/atlassian-bitbucket-server-integration/#bbs-deploy-wrapper-step-to-notify-bitbucket-server-of-the-deployment-status)
    *   [`step([$class: 'DeploymentNotifier'])`: Notify Bitbucket Server of deployment](https://www.jenkins.io/doc/pipeline/steps/atlassian-bitbucket-server-integration/#stepclass-deploymentnotifier-notify-bitbucket-server-of-deployment)

*   [Bitbucket Server Notifier](https://www.jenkins.io/doc/pipeline/steps/stashNotifier/)
    *   [`notifyBitbucket`: Notify Bitbucket Instance](https://www.jenkins.io/doc/pipeline/steps/stashNotifier/#notifybitbucket-notify-bitbucket-instance)

*   [Black Duck Coverity on Polaris](https://www.jenkins.io/doc/pipeline/steps/blackduck-coverity-on-polaris/)
    *   [`polaris`: Execute Coverity on Polaris CLI](https://www.jenkins.io/doc/pipeline/steps/blackduck-coverity-on-polaris/#polaris-execute-coverity-on-polaris-cli)
    *   [`polarisIssueCheck`: Check for issues in the Coverity on Polaris found by a previous execution of the CLI](https://www.jenkins.io/doc/pipeline/steps/blackduck-coverity-on-polaris/#polarisissuecheck-check-for-issues-in-the-coverity-on-polaris-found-by-a-previous-execution-of-the-cli)

*   [Black Duck Detect](https://www.jenkins.io/doc/pipeline/steps/blackduck-detect/)
    *   [`blackduck_detect`: Black Duck Detect](https://www.jenkins.io/doc/pipeline/steps/blackduck-detect/#blackduck-detect-black-duck-detect)

*   [Black Duck Rapid Scan Static Plugin](https://www.jenkins.io/doc/pipeline/steps/black-duck-sigma/)
    *   [`sigma`: Execute Black Duck Rapid Scan Static](https://www.jenkins.io/doc/pipeline/steps/black-duck-sigma/#sigma-execute-black-duck-rapid-scan-static)

*   [Black Duck Security Scan](https://www.jenkins.io/doc/pipeline/steps/blackduck-security-scan/)
    *   [`security_scan`: Black Duck Security Scan](https://www.jenkins.io/doc/pipeline/steps/blackduck-security-scan/#security-scan-black-duck-security-scan)
    *   [`step([$class: 'SecurityScanFreestyle'])`: Black Duck Security Scan](https://www.jenkins.io/doc/pipeline/steps/blackduck-security-scan/#stepclass-securityscanfreestyle-black-duck-security-scan)

*   [BlazeMeter plugin](https://www.jenkins.io/doc/pipeline/steps/BlazeMeterJenkinsPlugin/)
    *   [`blazeMeterTest`: BlazeMeter](https://www.jenkins.io/doc/pipeline/steps/BlazeMeterJenkinsPlugin/#blazemetertest-blazemeter)

*   [BMC AMI DevOps for Application Checkpoint Analysis](https://www.jenkins.io/doc/pipeline/steps/bmc-cfa/)
    *   [`BMC DevOps for CFA Plugin`: BMC AMI DevOps for Application Checkpoint Analysis](https://www.jenkins.io/doc/pipeline/steps/bmc-cfa/#bmc-devops-for-cfa-plugin-bmc-ami-devops-for-application-checkpoint-analysis)

*   [BMC AMI DevOps for Change Manager for IMS TM](https://www.jenkins.io/doc/pipeline/steps/bmc-change-manager-imstm/)
    *   [`BMC DevOps for BMC AMI Change Manager for IMS TM Plugin`: BMC AMI DevOps for Change Manager for IMS TM](https://www.jenkins.io/doc/pipeline/steps/bmc-change-manager-imstm/#bmc-devops-for-bmc-ami-change-manager-for-ims-tm-plugin-bmc-ami-devops-for-change-manager-for-ims-tm)

*   [BMC AMI DevX Code Debug Code Coverage](https://www.jenkins.io/doc/pipeline/steps/compuware-xpediter-code-coverage/)
    *   [`step([$class: 'CodeCoverageBuilder'])`: Retrieve BMC AMI DevX Code Debug Code Coverage Statistics](https://www.jenkins.io/doc/pipeline/steps/compuware-xpediter-code-coverage/#stepclass-codecoveragebuilder-retrieve-bmc-ami-devx-code-debug-code-coverage-statistics)

*   [BMC AMI DevX Code Pipeline Operations Plugin](https://www.jenkins.io/doc/pipeline/steps/compuware-ispw-operations/)
    *   [`gitToIspwIntegration`: Git to ISPW Integration](https://www.jenkins.io/doc/pipeline/steps/compuware-ispw-operations/#gittoispwintegration-git-to-ispw-integration)
    *   [`ispwOperation`: Perform a Compuware ISPW Rest API Request and return a JSON object](https://www.jenkins.io/doc/pipeline/steps/compuware-ispw-operations/#ispwoperation-perform-a-compuware-ispw-rest-api-request-and-return-a-json-object)
    *   [`ispwRegisterWebhook`: Creates and returns a ISPW webhook that can be used by an external system to notify a pipeline](https://www.jenkins.io/doc/pipeline/steps/compuware-ispw-operations/#ispwregisterwebhook-creates-and-returns-a-ispw-webhook-that-can-be-used-by-an-external-system-to-notify-a-pipeline)
    *   [`ispwWaitForWebhook`: Wait for ISPW webhook to be posted to by external system](https://www.jenkins.io/doc/pipeline/steps/compuware-ispw-operations/#ispwwaitforwebhook-wait-for-ispw-webhook-to-be-posted-to-by-external-system)

*   [BMC AMI DevX Data Studio](https://www.jenkins.io/doc/pipeline/steps/compuware-topaz-for-enterprise-data/)
    *   [`ted`: BMC AMI DevX Data Studio - Execute Specifications.](https://www.jenkins.io/doc/pipeline/steps/compuware-topaz-for-enterprise-data/#ted-bmc-ami-devx-data-studio-execute-specifications)

*   [BMC AMI DevX Total Test](https://www.jenkins.io/doc/pipeline/steps/compuware-topaz-for-total-test/)
    *   [`totaltestUT`: Total Test - Execute unit tests (deprecated)](https://www.jenkins.io/doc/pipeline/steps/compuware-topaz-for-total-test/#totaltestut-total-test-execute-unit-tests-deprecated)
    *   [`totaltest`: Total Test - Execute Total Test scenarios](https://www.jenkins.io/doc/pipeline/steps/compuware-topaz-for-total-test/#totaltest-total-test-execute-total-test-scenarios)

*   [BMC AMI Strobe Measurement Task](https://www.jenkins.io/doc/pipeline/steps/compuware-strobe-measurement/)
    *   [`strobeMeasurement`: BMC AMI Strobe Measurement Task](https://www.jenkins.io/doc/pipeline/steps/compuware-strobe-measurement/#strobemeasurement-bmc-ami-strobe-measurement-task)

*   [bootstraped-multi-test-results-report](https://www.jenkins.io/doc/pipeline/steps/bootstraped-multi-test-results-report/)
    *   [`step([$class: 'CucumberTestReportPublisher'])`: Publish Cucumber reports generated with handlebars](https://www.jenkins.io/doc/pipeline/steps/bootstraped-multi-test-results-report/#stepclass-cucumbertestreportpublisher-publish-cucumber-reports-generated-with-handlebars)
    *   [`step([$class: 'JUnitTestReportPublisher'])`: Publish JUnit reports generated with handlebars](https://www.jenkins.io/doc/pipeline/steps/bootstraped-multi-test-results-report/#stepclass-junittestreportpublisher-publish-junit-reports-generated-with-handlebars)
    *   [`step([$class: 'RSpecTestReportPublisher'])`: Publish RSpec reports generated with handlebars](https://www.jenkins.io/doc/pipeline/steps/bootstraped-multi-test-results-report/#stepclass-rspectestreportpublisher-publish-rspec-reports-generated-with-handlebars)
    *   [`step([$class: 'TestNGTestReportPublisher'])`: Publish TestNG reports generated with handlebars](https://www.jenkins.io/doc/pipeline/steps/bootstraped-multi-test-results-report/#stepclass-testngtestreportpublisher-publish-testng-reports-generated-with-handlebars)

*   [Breachlock DAST Plugin](https://www.jenkins.io/doc/pipeline/steps/breachlock-dast/)
    *   [`DASTScan`: Breachlock DAST scan](https://www.jenkins.io/doc/pipeline/steps/breachlock-dast/#dastscan-breachlock-dast-scan)

*   [BrowserStack](https://www.jenkins.io/doc/pipeline/steps/browserstack-integration/)
    *   [`browserStackReportAut`: BrowserStack Test Report](https://www.jenkins.io/doc/pipeline/steps/browserstack-integration/#browserstackreportaut-browserstack-test-report)
    *   [`browserstack`: BrowserStack](https://www.jenkins.io/doc/pipeline/steps/browserstack-integration/#browserstack-browserstack)
    *   [`browserstackAppUploader`: BrowserStack App Uploader](https://www.jenkins.io/doc/pipeline/steps/browserstack-integration/#browserstackappuploader-browserstack-app-uploader)
    *   [`step([$class: 'BrowserStackCypressReportPublisher'])`: BrowserStack Cypress Test Report](https://www.jenkins.io/doc/pipeline/steps/browserstack-integration/#stepclass-browserstackcypressreportpublisher-browserstack-cypress-test-report)
    *   [`step([$class: 'BrowserStackReportPublisher'])`: BrowserStack Test Report](https://www.jenkins.io/doc/pipeline/steps/browserstack-integration/#stepclass-browserstackreportpublisher-browserstack-test-report)
    *   [`browserStackReportPublisher`: BrowserStack Test Report and Insights](https://www.jenkins.io/doc/pipeline/steps/browserstack-integration/#browserstackreportpublisher-browserstack-test-report-and-insights)

*   [Buckminster](https://www.jenkins.io/doc/pipeline/steps/buckminster/)
    *   [`step([$class: 'TargetPlatformPublisher'])`: Archive and publish an Eclipse Target Platform](https://www.jenkins.io/doc/pipeline/steps/buckminster/#stepclass-targetplatformpublisher-archive-and-publish-an-eclipse-target-platform)

*   [build log file size checker plugin](https://www.jenkins.io/doc/pipeline/steps/logfilesizechecker/)
    *   [`wrap([$class: 'LogfilesizecheckerWrapper'])`: Abort the build if its log file size is too big](https://www.jenkins.io/doc/pipeline/steps/logfilesizechecker/#wrapclass-logfilesizecheckerwrapper-abort-the-build-if-its-log-file-size-is-too-big)

*   [Build Name and Description Setter](https://www.jenkins.io/doc/pipeline/steps/build-name-setter/)
    *   [`buildDescription`: Changes build description](https://www.jenkins.io/doc/pipeline/steps/build-name-setter/#builddescription-changes-build-description)
    *   [`buildName`: Changes build name](https://www.jenkins.io/doc/pipeline/steps/build-name-setter/#buildname-changes-build-name)

*   [Build Steps from Json Plugin](https://www.jenkins.io/doc/pipeline/steps/build-steps-from-json/)
    *   [`step([$class: 'BuildStepsFromJsonBuilder'])`: Build Steps from Json](https://www.jenkins.io/doc/pipeline/steps/build-steps-from-json/#stepclass-buildstepsfromjsonbuilder-build-steps-from-json)

*   [Build Token Trigger Plugin](https://www.jenkins.io/doc/pipeline/steps/build-token-trigger/)
    *   [`buildTokenTrigger`: Build Token Trigger](https://www.jenkins.io/doc/pipeline/steps/build-token-trigger/#buildtokentrigger-build-token-trigger)

*   [build user vars plugin](https://www.jenkins.io/doc/pipeline/steps/build-user-vars-plugin/)
    *   [`withBuildUser`: Set jenkins user build variables](https://www.jenkins.io/doc/pipeline/steps/build-user-vars-plugin/#withbuilduser-set-jenkins-user-build-variables)
    *   [`wrap([$class: 'BuildUser'])`: Set jenkins user build variables](https://www.jenkins.io/doc/pipeline/steps/build-user-vars-plugin/#wrapclass-builduser-set-jenkins-user-build-variables)

*   [Buildkite Plugin](https://www.jenkins.io/doc/pipeline/steps/buildkite/)
    *   [`buildkite`: Trigger a Buildkite Build](https://www.jenkins.io/doc/pipeline/steps/buildkite/#buildkite-trigger-a-buildkite-build)

*   [Buildstash](https://www.jenkins.io/doc/pipeline/steps/buildstash/)
    *   [`step([$class: 'BuildstashBuilder'])`: Upload to Buildstash](https://www.jenkins.io/doc/pipeline/steps/buildstash/#stepclass-buildstashbuilder-upload-to-buildstash)
    *   [`buildstash`: Upload to Buildstash](https://www.jenkins.io/doc/pipeline/steps/buildstash/#buildstash-upload-to-buildstash)

*   [Bumblebee HP ALM Plugin](https://www.jenkins.io/doc/pipeline/steps/bumblebee/)
    *   [`step([$class: 'AddTestToSetStep'])`: Bumblebee: Add Test to Test Set](https://www.jenkins.io/doc/pipeline/steps/bumblebee/#stepclass-addtesttosetstep-bumblebee-add-test-to-test-set)
    *   [`step([$class: 'BumblebeePublisher'])`: Bumblebee HP ALM Uploader](https://www.jenkins.io/doc/pipeline/steps/bumblebee/#stepclass-bumblebeepublisher-bumblebee-hp-alm-uploader)
    *   [`step([$class: 'GetTestResults'])`: Bumblebee: Import HP ALM Test Results](https://www.jenkins.io/doc/pipeline/steps/bumblebee/#stepclass-gettestresults-bumblebee-import-hp-alm-test-results)
    *   [`step([$class: 'RunPcTestBuildStep'])`: Bumblebee HP PC Test Runner](https://www.jenkins.io/doc/pipeline/steps/bumblebee/#stepclass-runpctestbuildstep-bumblebee-hp-pc-test-runner)
    *   [`step([$class: 'RunTestSetBuildStep'])`: Bumblebee HP ALM Test Set Runner](https://www.jenkins.io/doc/pipeline/steps/bumblebee/#stepclass-runtestsetbuildstep-bumblebee-hp-alm-test-set-runner)
    *   [`step([$class: 'RunUftTestBuildStep'])`: Bumblebee Local UFT Test Runner](https://www.jenkins.io/doc/pipeline/steps/bumblebee/#stepclass-runufttestbuildstep-bumblebee-local-uft-test-runner)

*   [ByteGuard Build Actions Plugin](https://www.jenkins.io/doc/pipeline/steps/byteguard-build-actions/)
    *   [`byteguardGreet`: ByteGuard Build Actions](https://www.jenkins.io/doc/pipeline/steps/byteguard-build-actions/#byteguardgreet-byteguard-build-actions)

*   [CA Service Virtualization Plugin](https://www.jenkins.io/doc/pipeline/steps/ca-service-virtualization/)
    *   [`svCreateAndDeployVirtualService`: CA Service Virtualization - Create And Deploy Virtual Service](https://www.jenkins.io/doc/pipeline/steps/ca-service-virtualization/#svcreateanddeployvirtualservice-ca-service-virtualization-create-and-deploy-virtual-service)
    *   [`svDeployTest`: CA Service Virtualization - Deploy Test](https://www.jenkins.io/doc/pipeline/steps/ca-service-virtualization/#svdeploytest-ca-service-virtualization-deploy-test)
    *   [`svDeployVirtualService`: CA Service Virtualization - Deploy Virtual Service](https://www.jenkins.io/doc/pipeline/steps/ca-service-virtualization/#svdeployvirtualservice-ca-service-virtualization-deploy-virtual-service)
    *   [`svStartVirtualService`: CA Service Virtualization - Start Virtual Service](https://www.jenkins.io/doc/pipeline/steps/ca-service-virtualization/#svstartvirtualservice-ca-service-virtualization-start-virtual-service)
    *   [`svStopVirtualService`: CA Service Virtualization - Stop Virtual Service](https://www.jenkins.io/doc/pipeline/steps/ca-service-virtualization/#svstopvirtualservice-ca-service-virtualization-stop-virtual-service)
    *   [`svPublishTestReport`: CA Service Virtualization Report Publisher](https://www.jenkins.io/doc/pipeline/steps/ca-service-virtualization/#svpublishtestreport-ca-service-virtualization-report-publisher)
    *   [`svUndeployVirtualService`: CA Service Virtualization - Undeploy Virtual Service](https://www.jenkins.io/doc/pipeline/steps/ca-service-virtualization/#svundeployvirtualservice-ca-service-virtualization-undeploy-virtual-service)

*   [CA-APM Plugin](https://www.jenkins.io/doc/pipeline/steps/ca-apm/)
    *   [`caapmplugin`: Jenkins Plugin for CA APM](https://www.jenkins.io/doc/pipeline/steps/ca-apm/#caapmplugin-jenkins-plugin-for-ca-apm)

*   [Cachet Gating Plugin](https://www.jenkins.io/doc/pipeline/steps/cachet-gating/)
    *   [`cachetgatingmetrics`: Cachet Gating Metrics](https://www.jenkins.io/doc/pipeline/steps/cachet-gating/#cachetgatingmetrics-cachet-gating-metrics)

*   [Cadence vManager Plugin for Jenkins](https://www.jenkins.io/doc/pipeline/steps/vmanager-plugin/)
    *   [`step([$class: 'DSLPublisher'])`: vManager Post Build Actions](https://www.jenkins.io/doc/pipeline/steps/vmanager-plugin/#stepclass-dslpublisher-vmanager-post-build-actions)
    *   [`vmanagerLaunch`: Cadence vManager Session Launcher](https://www.jenkins.io/doc/pipeline/steps/vmanager-plugin/#vmanagerlaunch-cadence-vmanager-session-launcher)
    *   [`vmanagerPostBuildActions`: vManager Post Build Actions](https://www.jenkins.io/doc/pipeline/steps/vmanager-plugin/#vmanagerpostbuildactions-vmanager-post-build-actions)

*   [Carbonetes Serverless Container Scanning and Policy Compliance](https://www.jenkins.io/doc/pipeline/steps/carbonetes-serverless-container-scanning-and-policy-compliance/)
    *   [`carbonetes`: Carbonetes Serverless Container Scanning and Policy Compliance](https://www.jenkins.io/doc/pipeline/steps/carbonetes-serverless-container-scanning-and-policy-compliance/#carbonetes-carbonetes-serverless-container-scanning-and-policy-compliance)

*   [Carl plugin](https://www.jenkins.io/doc/pipeline/steps/carl/)
    *   [`carl`: Carl](https://www.jenkins.io/doc/pipeline/steps/carl/#carl-carl)

*   [Cerberus Testing Plugin](https://www.jenkins.io/doc/pipeline/steps/cerberus-testing/)
    *   [`executeCerberusCampaign`: Execute Cerberus Campaign](https://www.jenkins.io/doc/pipeline/steps/cerberus-testing/#executecerberuscampaign-execute-cerberus-campaign)

*   [change-assembly-version-plugin](https://www.jenkins.io/doc/pipeline/steps/change-assembly-version-plugin/)
    *   [`changeAsmVer`: Change Assembly Version](https://www.jenkins.io/doc/pipeline/steps/change-assembly-version-plugin/#changeasmver-change-assembly-version)

*   [Chatter Notifier Plugin](https://www.jenkins.io/doc/pipeline/steps/chatter-notifier/)
    *   [`chatterPost`: Post to Chatter](https://www.jenkins.io/doc/pipeline/steps/chatter-notifier/#chatterpost-post-to-chatter)

*   [Checkmarx AST Scanner Plugin](https://www.jenkins.io/doc/pipeline/steps/checkmarx-ast-scanner/)
    *   [`checkmarxASTScanner`: Execute Checkmarx AST Scan](https://www.jenkins.io/doc/pipeline/steps/checkmarx-ast-scanner/#checkmarxastscanner-execute-checkmarx-ast-scan)

*   [Checkmarx Plugin](https://www.jenkins.io/doc/pipeline/steps/checkmarx/)
    *   [`step([$class: 'CxScanBuilder'])`: Execute Checkmarx Scan](https://www.jenkins.io/doc/pipeline/steps/checkmarx/#stepclass-cxscanbuilder-execute-checkmarx-scan)

*   [CheckPoint CloudGuard Shiftleft](https://www.jenkins.io/doc/pipeline/steps/cloudguard-shiftleft/)
    *   [`step([$class: 'BladeBuilder'])`: CheckPoint Shiftleft](https://www.jenkins.io/doc/pipeline/steps/cloudguard-shiftleft/#stepclass-bladebuilder-checkpoint-shiftleft)

*   [Checks API plugin](https://www.jenkins.io/doc/pipeline/steps/checks-api/)
    *   [`publishChecks`: Publish customized checks to SCM platforms](https://www.jenkins.io/doc/pipeline/steps/checks-api/#publishchecks-publish-customized-checks-to-scm-platforms)
    *   [`withChecks`: Inject checks properties into its closure](https://www.jenkins.io/doc/pipeline/steps/checks-api/#withchecks-inject-checks-properties-into-its-closure)

*   [Chef Cookbook Pipeline Plugin](https://www.jenkins.io/doc/pipeline/steps/chef-cookbook-pipeline/)
    *   [`chef_cookbook_cookstyle`: Chef Cookbook Lint (Cookstyle)](https://www.jenkins.io/doc/pipeline/steps/chef-cookbook-pipeline/#chef-cookbook-cookstyle-chef-cookbook-lint-cookstyle)
    *   [`chef_cookbook_foodcritic`: Chef Cookbook Lint (Foodcritic)](https://www.jenkins.io/doc/pipeline/steps/chef-cookbook-pipeline/#chef-cookbook-foodcritic-chef-cookbook-lint-foodcritic)
    *   [`chef_cookbook_functional`: Chef Cookbook Functional](https://www.jenkins.io/doc/pipeline/steps/chef-cookbook-pipeline/#chef-cookbook-functional-chef-cookbook-functional)
    *   [`chef_cookbook_unit`: Chef Cookbook Unit](https://www.jenkins.io/doc/pipeline/steps/chef-cookbook-pipeline/#chef-cookbook-unit-chef-cookbook-unit)

*   [Chef Identity Plugin](https://www.jenkins.io/doc/pipeline/steps/chef-identity/)
    *   [`wrap([$class: 'ChefIdentityBuildWrapper'])`: Chef Identity Plugin](https://www.jenkins.io/doc/pipeline/steps/chef-identity/#wrapclass-chefidentitybuildwrapper-chef-identity-plugin)

*   [ChuckNorris Plugin](https://www.jenkins.io/doc/pipeline/steps/chucknorris/)
    *   [`chuckNorris`: Submit to Chuck Norris' will](https://www.jenkins.io/doc/pipeline/steps/chucknorris/#chucknorris-submit-to-chuck-norris-will)
    *   [`step([$class: 'CordellWalkerRecorder'])`: Activate Chuck Norris](https://www.jenkins.io/doc/pipeline/steps/chucknorris/#stepclass-cordellwalkerrecorder-activate-chuck-norris)

*   [Cisco Spark Notifier](https://www.jenkins.io/doc/pipeline/steps/cisco-spark-notifier/)
    *   [`sparkSend`: Send spark message](https://www.jenkins.io/doc/pipeline/steps/cisco-spark-notifier/#sparksend-send-spark-message)

*   [Cisco Spark Plugin](https://www.jenkins.io/doc/pipeline/steps/cisco-spark/)
    *   [`step([$class: 'SparkNotifier'])`: Cisco Spark Notification](https://www.jenkins.io/doc/pipeline/steps/cisco-spark/#stepclass-sparknotifier-cisco-spark-notification)

*   [Claim Plugin](https://www.jenkins.io/doc/pipeline/steps/claim/)
    *   [`step([$class: 'ClaimPublisher'])`: Allow broken build claiming](https://www.jenkins.io/doc/pipeline/steps/claim/#stepclass-claimpublisher-allow-broken-build-claiming)

*   [Cloud Foundry Plugin](https://www.jenkins.io/doc/pipeline/steps/cloudfoundry/)
    *   [`pushToCloudFoundry`: Push to Cloud Foundry](https://www.jenkins.io/doc/pipeline/steps/cloudfoundry/#pushtocloudfoundry-push-to-cloud-foundry)

*   [CloudAEye Plugin](https://www.jenkins.io/doc/pipeline/steps/cloudaeye/)
    *   [`sendNotificationsToCloudAEye`: Send build notifications to CloudAEye](https://www.jenkins.io/doc/pipeline/steps/cloudaeye/#sendnotificationstocloudaeye-send-build-notifications-to-cloudaeye)

*   [CloudBees CD](https://www.jenkins.io/doc/pipeline/steps/electricflow/)
    *   [`cloudBeesFlowCallRestApi`: CloudBees CD - Call REST API](https://www.jenkins.io/doc/pipeline/steps/electricflow/#cloudbeesflowcallrestapi-cloudbees-cd-call-rest-api)
    *   [`cloudBeesFlowAssociateBuildToRelease`: CloudBees CD - Associate Build To Release](https://www.jenkins.io/doc/pipeline/steps/electricflow/#cloudbeesflowassociatebuildtorelease-cloudbees-cd-associate-build-to-release)
    *   [`cloudBeesFlowDeployApplication`: CloudBees CD - Deploy Application](https://www.jenkins.io/doc/pipeline/steps/electricflow/#cloudbeesflowdeployapplication-cloudbees-cd-deploy-application)
    *   [`step([$class: 'ElectricFlowGenericRestApi'])`: CloudBees CD - Call REST API](https://www.jenkins.io/doc/pipeline/steps/electricflow/#stepclass-electricflowgenericrestapi-cloudbees-cd-call-rest-api)
    *   [`cloudBeesFlowRunPipeline`: CloudBees CD - Run Pipeline](https://www.jenkins.io/doc/pipeline/steps/electricflow/#cloudbeesflowrunpipeline-cloudbees-cd-run-pipeline)
    *   [`cloudBeesFlowCreateAndDeployAppFromJenkinsPackage`: CloudBees CD - Create/Deploy Application from Deployment Package](https://www.jenkins.io/doc/pipeline/steps/electricflow/#cloudbeesflowcreateanddeployappfromjenkinspackage-cloudbees-cd-createdeploy-application-from-deployment-package)
    *   [`cloudBeesFlowRunProcedure`: CloudBees CD - Run Procedure](https://www.jenkins.io/doc/pipeline/steps/electricflow/#cloudbeesflowrunprocedure-cloudbees-cd-run-procedure)
    *   [`cloudBeesFlowTriggerRelease`: CloudBees CD - Trigger Release](https://www.jenkins.io/doc/pipeline/steps/electricflow/#cloudbeesflowtriggerrelease-cloudbees-cd-trigger-release)
    *   [`cloudBeesFlowPublishArtifact`: CloudBees CD - Publish Artifact](https://www.jenkins.io/doc/pipeline/steps/electricflow/#cloudbeesflowpublishartifact-cloudbees-cd-publish-artifact)

*   [CloudBees Feature Management](https://www.jenkins.io/doc/pipeline/steps/cloudbees-feature-management/)
    *   [`featureManagementConfig`: CloudBees Feature Management configuration](https://www.jenkins.io/doc/pipeline/steps/cloudbees-feature-management/#featuremanagementconfig-cloudbees-feature-management-configuration)

*   [CloudCoreo DeployTime Plugin](https://www.jenkins.io/doc/pipeline/steps/cloudcoreo-deploytime/)
    *   [`step([$class: 'CloudCoreoPublisher'])`: Analyze CloudCoreo Results](https://www.jenkins.io/doc/pipeline/steps/cloudcoreo-deploytime/#stepclass-cloudcoreopublisher-analyze-cloudcoreo-results)
    *   [`wrap([$class: 'CloudCoreoBuildWrapper'])`: CloudCoreo Enabled for Workload Analysis](https://www.jenkins.io/doc/pipeline/steps/cloudcoreo-deploytime/#wrapclass-cloudcoreobuildwrapper-cloudcoreo-enabled-for-workload-analysis)

*   [CloudHub Deployer](https://www.jenkins.io/doc/pipeline/steps/cloudhub-deployer/)
    *   [`cloudhubDeployer`: CloudHub Deployment](https://www.jenkins.io/doc/pipeline/steps/cloudhub-deployer/#cloudhubdeployer-cloudhub-deployment)

*   [Cloudify](https://www.jenkins.io/doc/pipeline/steps/cloudify/)
    *   [`cfyAzureArm`: Create Azure ARM Deployment](https://www.jenkins.io/doc/pipeline/steps/cloudify/#cfyazurearm-create-azure-arm-deployment)
    *   [`cfyAnsible`: Run Ansible Playbook](https://www.jenkins.io/doc/pipeline/steps/cloudify/#cfyansible-run-ansible-playbook)
    *   [`cfyCloudFormation`: Create CloudFormation Stack](https://www.jenkins.io/doc/pipeline/steps/cloudify/#cfycloudformation-create-cloudformation-stack)
    *   [`createCloudifyEnv`: Create Cloudify Environment](https://www.jenkins.io/doc/pipeline/steps/cloudify/#createcloudifyenv-create-cloudify-environment)
    *   [`deleteCloudifyBlueprint`: Delete Cloudify Blueprint](https://www.jenkins.io/doc/pipeline/steps/cloudify/#deletecloudifyblueprint-delete-cloudify-blueprint)
    *   [`deleteCloudifyEnv`: Delete Cloudify Environment](https://www.jenkins.io/doc/pipeline/steps/cloudify/#deletecloudifyenv-delete-cloudify-environment)
    *   [`executeCloudifyWorkflow`: Execute Cloudify Workflow](https://www.jenkins.io/doc/pipeline/steps/cloudify/#executecloudifyworkflow-execute-cloudify-workflow)
    *   [`cfyKubernetes`: Create Kubernetes Resources](https://www.jenkins.io/doc/pipeline/steps/cloudify/#cfykubernetes-create-kubernetes-resources)
    *   [`cfyOutputsToInputs`: Convert Cloudify Environment Outputs/Capabilities to Inputs](https://www.jenkins.io/doc/pipeline/steps/cloudify/#cfyoutputstoinputs-convert-cloudify-environment-outputscapabilities-to-inputs)
    *   [`cfyTerraform`: Apply Terraform Module](https://www.jenkins.io/doc/pipeline/steps/cloudify/#cfyterraform-apply-terraform-module)
    *   [`uploadCloudifyBlueprint`: Upload Cloudify Blueprint](https://www.jenkins.io/doc/pipeline/steps/cloudify/#uploadcloudifyblueprint-upload-cloudify-blueprint)
    *   [`uploadCloudifyBlueprint`: Upload Cloudify Plugin](https://www.jenkins.io/doc/pipeline/steps/cloudify/#uploadcloudifyblueprint-upload-cloudify-plugin)
    *   [`wrap([$class: 'CloudifyBuildWrapper'])`: Cloudify Environment](https://www.jenkins.io/doc/pipeline/steps/cloudify/#wrapclass-cloudifybuildwrapper-cloudify-environment)

*   [CloudShare Docker-Machine Plugin](https://www.jenkins.io/doc/pipeline/steps/cloudshare-docker/)
    *   [`cloudshareDockerMachine`: CloudShare Docker-Machine](https://www.jenkins.io/doc/pipeline/steps/cloudshare-docker/#cloudsharedockermachine-cloudshare-docker-machine)
    *   [`wrap([$class: 'DockerMachineWrapper'])`: Run Docker commands on CloudShare VM](https://www.jenkins.io/doc/pipeline/steps/cloudshare-docker/#wrapclass-dockermachinewrapper-run-docker-commands-on-cloudshare-vm)

*   [CloudShell Sandbox Plugin](https://www.jenkins.io/doc/pipeline/steps/cloudshell-sandbox/)
    *   [`startSandbox`: starts a CloudShell Sandbox](https://www.jenkins.io/doc/pipeline/steps/cloudshell-sandbox/#startsandbox-starts-a-cloudshell-sandbox)
    *   [`stopSandbox`: Stops a CloudShell Sandbox](https://www.jenkins.io/doc/pipeline/steps/cloudshell-sandbox/#stopsandbox-stops-a-cloudshell-sandbox)
    *   [`withSandbox`: Use sandbox in a specific scope](https://www.jenkins.io/doc/pipeline/steps/cloudshell-sandbox/#withsandbox-use-sandbox-in-a-specific-scope)

*   [Clover plugin](https://www.jenkins.io/doc/pipeline/steps/clover/)
    *   [`clover`: Publish OpenClover coverage report](https://www.jenkins.io/doc/pipeline/steps/clover/#clover-publish-openclover-coverage-report)

*   [CMake plugin](https://www.jenkins.io/doc/pipeline/steps/cmakebuilder/)
    *   [`cmake`: Run cmake with arbitrary arguments](https://www.jenkins.io/doc/pipeline/steps/cmakebuilder/#cmake-run-cmake-with-arbitrary-arguments)
    *   [`cmakeBuild`: Generate build-scripts with cmake and execute them](https://www.jenkins.io/doc/pipeline/steps/cmakebuilder/#cmakebuild-generate-build-scripts-with-cmake-and-execute-them)
    *   [`cpack`: Run cpack](https://www.jenkins.io/doc/pipeline/steps/cmakebuilder/#cpack-run-cpack)
    *   [`ctest`: Run ctest](https://www.jenkins.io/doc/pipeline/steps/cmakebuilder/#ctest-run-ctest)

*   [Cobertura Plugin](https://www.jenkins.io/doc/pipeline/steps/cobertura/)
    *   [`cobertura`: Publish Cobertura Coverage Report](https://www.jenkins.io/doc/pipeline/steps/cobertura/#cobertura-publish-cobertura-coverage-report)

*   [Code Coverage Plugin](https://www.jenkins.io/doc/pipeline/steps/code-coverage-api/)
    *   [`publishCoverage`: Publish Coverage Report [deprecated]](https://www.jenkins.io/doc/pipeline/steps/code-coverage-api/#publishcoverage-publish-coverage-report-deprecated)

*   [Code Dx Plugin](https://www.jenkins.io/doc/pipeline/steps/codedx/)
    *   [`step([$class: 'CodeDxPublisher'])`: Publish to Code Dx](https://www.jenkins.io/doc/pipeline/steps/codedx/#stepclass-codedxpublisher-publish-to-code-dx)

*   [Code Signing with SignPath](https://www.jenkins.io/doc/pipeline/steps/signpath/)
    *   [`getSignedArtifact`: Download SignPath Signed Artifact](https://www.jenkins.io/doc/pipeline/steps/signpath/#getsignedartifact-download-signpath-signed-artifact)
    *   [`submitSigningRequest`: Submit SignPath Signing Request](https://www.jenkins.io/doc/pipeline/steps/signpath/#submitsigningrequest-submit-signpath-signing-request)

*   [Code signing with Software Trust Manager](https://www.jenkins.io/doc/pipeline/steps/digicert-software-trust-code-sign/)
    *   [`SoftwareTrustManagerSetup`: SoftwareTrustManagerSetup](https://www.jenkins.io/doc/pipeline/steps/digicert-software-trust-code-sign/#softwaretrustmanagersetup-softwaretrustmanagersetup)

*   [Codebeamer xUnit Importer Plugin](https://www.jenkins.io/doc/pipeline/steps/codebeamer-xunit-importer/)
    *   [`xUnitImporter`: Codebeamer xUnit Importer](https://www.jenkins.io/doc/pipeline/steps/codebeamer-xunit-importer/#xunitimporter-codebeamer-xunit-importer)

*   [CodeBeamer XUnit Uploader](https://www.jenkins.io/doc/pipeline/steps/codebeamer-xunit-uploader/)
    *   [`xUnitUploader`: CodeBeamer XUnit Uploader](https://www.jenkins.io/doc/pipeline/steps/codebeamer-xunit-uploader/#xunituploader-codebeamer-xunit-uploader)

*   [CodeBuilder: AWS CodeBuild Cloud Agents](https://www.jenkins.io/doc/pipeline/steps/codebuilder-cloud/)
    *   [`wrap([$class: 'CodeBuilderLogger'])`: Add Build ID Link to CodeBuilder Jobs](https://www.jenkins.io/doc/pipeline/steps/codebuilder-cloud/#wrapclass-codebuilderlogger-add-build-id-link-to-codebuilder-jobs)

*   [Codefresh Integration Plugin](https://www.jenkins.io/doc/pipeline/steps/codefresh/)
    *   [`codefreshLaunch`: Launch a Codefresh Composition](https://www.jenkins.io/doc/pipeline/steps/codefresh/#codefreshlaunch-launch-a-codefresh-composition)
    *   [`codefreshRun`: Trigger a Codefresh Pipeline](https://www.jenkins.io/doc/pipeline/steps/codefresh/#codefreshrun-trigger-a-codefresh-pipeline)

*   [CodeQL Plugin](https://www.jenkins.io/doc/pipeline/steps/codeql/)
    *   [`withCodeQL`: Provide codeql environment](https://www.jenkins.io/doc/pipeline/steps/codeql/#withcodeql-provide-codeql-environment)

*   [CodeScene Plugin](https://www.jenkins.io/doc/pipeline/steps/codescene/)
    *   [`codescene`: Run CodeScene Delta Analysis](https://www.jenkins.io/doc/pipeline/steps/codescene/#codescene-run-codescene-delta-analysis)

*   [CodeSonar Plugin](https://www.jenkins.io/doc/pipeline/steps/codesonar/)
    *   [`codesonar`: CodeSonar](https://www.jenkins.io/doc/pipeline/steps/codesonar/#codesonar-codesonar)

*   [CodeThreat](https://www.jenkins.io/doc/pipeline/steps/codethreat-scanner/)
    *   [`CodeThreatScan`: CodeThreat](https://www.jenkins.io/doc/pipeline/steps/codethreat-scanner/#codethreatscan-codethreat)

*   [CollabNet Plugins](https://www.jenkins.io/doc/pipeline/steps/collabnet/)
    *   [`publishTeamForge`: Notify TeamForge](https://www.jenkins.io/doc/pipeline/steps/collabnet/#publishteamforge-notify-teamforge)

*   [Comments Remover plugin](https://www.jenkins.io/doc/pipeline/steps/comments-remover/)
    *   [`step([$class: 'CommentsRemoverBuilder'])`: Invoke Comments Remover](https://www.jenkins.io/doc/pipeline/steps/comments-remover/#stepclass-commentsremoverbuilder-invoke-comments-remover)

*   [Compuware Topaz Utilities](https://www.jenkins.io/doc/pipeline/steps/compuware-topaz-utilities/)
    *   [`topazSubmitFreeFormJcl`: Topaz submit free-form JCL](https://www.jenkins.io/doc/pipeline/steps/compuware-topaz-utilities/#topazsubmitfreeformjcl-topaz-submit-free-form-jcl)
    *   [`topazSubmitJclMembers`: Topaz submit JCL members](https://www.jenkins.io/doc/pipeline/steps/compuware-topaz-utilities/#topazsubmitjclmembers-topaz-submit-jcl-members)

*   [Compuware zAdviser API](https://www.jenkins.io/doc/pipeline/steps/compuware-zadviser-api/)
    *   [`zAdviserDownload`: zAdviser download data and optionally upload to Compuware](https://www.jenkins.io/doc/pipeline/steps/compuware-zadviser-api/#zadviserdownload-zadviser-download-data-and-optionally-upload-to-compuware)
    *   [`zAdviserUpload`: zAdviser upload data to Compuware](https://www.jenkins.io/doc/pipeline/steps/compuware-zadviser-api/#zadviserupload-zadviser-upload-data-to-compuware)

*   [Concurrent Step](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/)
    *   [`acquireSemaphore`: Wait until the latch has counted down to zero.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#acquiresemaphore-wait-until-the-latch-has-counted-down-to-zero)
    *   [`awaitBarrier`: Waits until all parties have invoked await on this barrier.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#awaitbarrier-waits-until-all-parties-have-invoked-await-on-this-barrier)
    *   [`awaitCondition`: Causes the current thread to wait until it is signalled or interrupted.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#awaitcondition-causes-the-current-thread-to-wait-until-it-is-signalled-or-interrupted)
    *   [`awaitLatch`: Wait until the latch has counted down to zero.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#awaitlatch-wait-until-the-latch-has-counted-down-to-zero)
    *   [`countDownLatch`: Decrements the count of the latch.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#countdownlatch-decrements-the-count-of-the-latch)
    *   [`createBarrier`: Create a Cyclic Barrier.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#createbarrier-create-a-cyclic-barrier)
    *   [`createCondition`: Create a lock.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#createcondition-create-a-lock)
    *   [`createLatch`: Create a count down latch.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#createlatch-create-a-count-down-latch)
    *   [`createSemaphore`: Create a semaphore.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#createsemaphore-create-a-semaphore)
    *   [`releaseSemaphore`: Release the semaphore.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#releasesemaphore-release-the-semaphore)
    *   [`signalAll`: Notify all wa.](https://www.jenkins.io/doc/pipeline/steps/concurrent-step/#signalall-notify-all-wa)

*   [Config File Provider Plugin](https://www.jenkins.io/doc/pipeline/steps/config-file-provider/)
    *   [`configFileProvider`: Provide Configuration files](https://www.jenkins.io/doc/pipeline/steps/config-file-provider/#configfileprovider-provide-configuration-files)

*   [Consul KV Builder](https://www.jenkins.io/doc/pipeline/steps/consul-kv-builder/)
    *   [`step([$class: 'ConsulKVBuilder'])`: Consul K/V Builder](https://www.jenkins.io/doc/pipeline/steps/consul-kv-builder/#stepclass-consulkvbuilder-consul-kv-builder)
    *   [`wrap([$class: 'ConsulKVReadWrapper'])`: Add Consul K/V Read Config(s)](https://www.jenkins.io/doc/pipeline/steps/consul-kv-builder/#wrapclass-consulkvreadwrapper-add-consul-kv-read-configs)

*   [Consul Plugin](https://www.jenkins.io/doc/pipeline/steps/consul/)
    *   [`Consul`: ConsulStep](https://www.jenkins.io/doc/pipeline/steps/consul/#consul-consulstep)

*   [Content Replace](https://www.jenkins.io/doc/pipeline/steps/content-replace/)
    *   [`contentReplace`: Content Replace](https://www.jenkins.io/doc/pipeline/steps/content-replace/#contentreplace-content-replace)

*   [Continuum Plugin](https://www.jenkins.io/doc/pipeline/steps/continuum/)
    *   [`ctmInitiatePipeline`: Initiate a Continuum Pipeline Definition with matching 'key' information.](https://www.jenkins.io/doc/pipeline/steps/continuum/#ctminitiatepipeline-initiate-a-continuum-pipeline-definition-with-matching-key-information)
    *   [`ctmPostPiData`: Post data to the workspace on a running Continuum pipeline instance.](https://www.jenkins.io/doc/pipeline/steps/continuum/#ctmpostpidata-post-data-to-the-workspace-on-a-running-continuum-pipeline-instance)
    *   [`ctmSetPiData`: Set workspace data on a running Continuum pipeline instance.](https://www.jenkins.io/doc/pipeline/steps/continuum/#ctmsetpidata-set-workspace-data-on-a-running-continuum-pipeline-instance)

*   [Contrast Continuous Application Security](https://www.jenkins.io/doc/pipeline/steps/contrast-continuous-application-security/)
    *   [`contrastAgent`: Download latest Contrast agent](https://www.jenkins.io/doc/pipeline/steps/contrast-continuous-application-security/#contrastagent-download-latest-contrast-agent)
    *   [`contrastVerification`: Verify vulnerabilities in a build](https://www.jenkins.io/doc/pipeline/steps/contrast-continuous-application-security/#contrastverification-verify-vulnerabilities-in-a-build)

*   [Conventional Commits Plugin](https://www.jenkins.io/doc/pipeline/steps/conventional-commits/)
    *   [`currentVersion`: determine the current version from the conventional commit history](https://www.jenkins.io/doc/pipeline/steps/conventional-commits/#currentversion-determine-the-current-version-from-the-conventional-commit-history)
    *   [`nextVersion`: Next Version: determine the next version from the conventional commit history](https://www.jenkins.io/doc/pipeline/steps/conventional-commits/#nextversion-next-version-determine-the-next-version-from-the-conventional-commit-history)

*   [Copy Artifact Plugin](https://www.jenkins.io/doc/pipeline/steps/copyartifact/)
    *   [`copyArtifacts`: Copy artifacts from another project](https://www.jenkins.io/doc/pipeline/steps/copyartifact/#copyartifacts-copy-artifacts-from-another-project)

*   [Cortex Metrics Plugin](https://www.jenkins.io/doc/pipeline/steps/cortex-metrics/)
    *   [`publishCortexMetrics`: Publish metrics to Cortex](https://www.jenkins.io/doc/pipeline/steps/cortex-metrics/#publishcortexmetrics-publish-metrics-to-cortex)

*   [Coverage Plugin](https://www.jenkins.io/doc/pipeline/steps/coverage/)
    *   [`recordCoverage`: Record code coverage results](https://www.jenkins.io/doc/pipeline/steps/coverage/#recordcoverage-record-code-coverage-results)

*   [Coverity plugin](https://www.jenkins.io/doc/pipeline/steps/coverity/)
    *   [`coverityResults`: Publish Coverity View Results](https://www.jenkins.io/doc/pipeline/steps/coverity/#coverityresults-publish-coverity-view-results)
    *   [`withCoverityEnv`: Binds Coverity Tool path and Coverity Connect Instance information to Environment Variables](https://www.jenkins.io/doc/pipeline/steps/coverity/#withcoverityenv-binds-coverity-tool-path-and-coverity-connect-instance-information-to-environment-variables)

*   [Cppcheck Plug-in](https://www.jenkins.io/doc/pipeline/steps/cppcheck/)
    *   [`publishCppcheck`: Publish Cppcheck results](https://www.jenkins.io/doc/pipeline/steps/cppcheck/#publishcppcheck-publish-cppcheck-results)

*   [Credentials Binding Plugin](https://www.jenkins.io/doc/pipeline/steps/credentials-binding/)
    *   [`withCredentials`: Bind credentials to variables](https://www.jenkins.io/doc/pipeline/steps/credentials-binding/#withcredentials-bind-credentials-to-variables)

*   [CrowdStrike Security](https://www.jenkins.io/doc/pipeline/steps/crowdstrike-security/)
    *   [`crowdStrikeSecurity`: CrowdStrike Security Plugin](https://www.jenkins.io/doc/pipeline/steps/crowdstrike-security/#crowdstrikesecurity-crowdstrike-security-plugin)

*   [CRX Content Package Deployer Plugin](https://www.jenkins.io/doc/pipeline/steps/crx-content-package-deployer/)
    *   [`crxBuild`: Build a Content Package on CRX](https://www.jenkins.io/doc/pipeline/steps/crx-content-package-deployer/#crxbuild-build-a-content-package-on-crx)
    *   [`crxDeploy`: Deploy Content Packages to CRX](https://www.jenkins.io/doc/pipeline/steps/crx-content-package-deployer/#crxdeploy-deploy-content-packages-to-crx)
    *   [`crxDownload`: Download Content Packages from CRX](https://www.jenkins.io/doc/pipeline/steps/crx-content-package-deployer/#crxdownload-download-content-packages-from-crx)
    *   [`crxReplicate`: Replicate Content Packages from CRX](https://www.jenkins.io/doc/pipeline/steps/crx-content-package-deployer/#crxreplicate-replicate-content-packages-from-crx)
    *   [`crxValidate`: Validate CRX Content Packages](https://www.jenkins.io/doc/pipeline/steps/crx-content-package-deployer/#crxvalidate-validate-crx-content-packages)

*   [CTRF](https://www.jenkins.io/doc/pipeline/steps/ctrf-json/)
    *   [`publishCtrfResults`: Publish CTRF test result report](https://www.jenkins.io/doc/pipeline/steps/ctrf-json/#publishctrfresults-publish-ctrf-test-result-report)

*   [Cucumber json test reporting.](https://www.jenkins.io/doc/pipeline/steps/cucumber-testresult-plugin/)
    *   [`cucumber`: Publish Cucumber test result report](https://www.jenkins.io/doc/pipeline/steps/cucumber-testresult-plugin/#cucumber-publish-cucumber-test-result-report)

*   [Cucumber Living Documentation Plugin](https://www.jenkins.io/doc/pipeline/steps/cucumber-living-documentation/)
    *   [`livingDocs`: Living documentation](https://www.jenkins.io/doc/pipeline/steps/cucumber-living-documentation/#livingdocs-living-documentation)

*   [Cucumber reports](https://www.jenkins.io/doc/pipeline/steps/cucumber-reports/)
    *   [`cucumber`: Cucumber reports](https://www.jenkins.io/doc/pipeline/steps/cucumber-reports/#cucumber-cucumber-reports)

*   [cucumber-slack-notifier](https://www.jenkins.io/doc/pipeline/steps/cucumber-slack-notifier/)
    *   [`cucumberSlackSend`: Send cucumber notifications to slack](https://www.jenkins.io/doc/pipeline/steps/cucumber-slack-notifier/#cucumberslacksend-send-cucumber-notifications-to-slack)

*   [Custom Build Properties Plugin](https://www.jenkins.io/doc/pipeline/steps/custom-build-properties/)
    *   [`getCustomBuildProperty`: Get custom build property](https://www.jenkins.io/doc/pipeline/steps/custom-build-properties/#getcustombuildproperty-get-custom-build-property)
    *   [`setCustomBuildProperty`: Set custom build property](https://www.jenkins.io/doc/pipeline/steps/custom-build-properties/#setcustombuildproperty-set-custom-build-property)
    *   [`setJUnitCounts`: Set junit test result counts as custom build properties](https://www.jenkins.io/doc/pipeline/steps/custom-build-properties/#setjunitcounts-set-junit-test-result-counts-as-custom-build-properties)
    *   [`waitForCustomBuildProperties`: Wait until specified custom build properties are set](https://www.jenkins.io/doc/pipeline/steps/custom-build-properties/#waitforcustombuildproperties-wait-until-specified-custom-build-properties-are-set)

*   [Cyber Chief Security Scanner](https://www.jenkins.io/doc/pipeline/steps/cyberchief-security-scanner/)
    *   [`greet`: Cyber Chief Security Scanner](https://www.jenkins.io/doc/pipeline/steps/cyberchief-security-scanner/#greet-cyber-chief-security-scanner)

*   [Data Theorem Mobile Security: CI/CD Plugin](https://www.jenkins.io/doc/pipeline/steps/datatheorem-mobile-app-security/)
    *   [`sendBuildToDataTheorem`: Upload build to Data Theorem](https://www.jenkins.io/doc/pipeline/steps/datatheorem-mobile-app-security/#sendbuildtodatatheorem-upload-build-to-data-theorem)

*   [Database](https://www.jenkins.io/doc/pipeline/steps/database/)
    *   [`getDatabaseConnection`: Get Database Connection](https://www.jenkins.io/doc/pipeline/steps/database/#getdatabaseconnection-get-database-connection)
    *   [`sql`: Run SQL](https://www.jenkins.io/doc/pipeline/steps/database/#sql-run-sql)

*   [Datadog Plugin](https://www.jenkins.io/doc/pipeline/steps/datadog/)
    *   [`datadog`: DatadogOptions](https://www.jenkins.io/doc/pipeline/steps/datadog/#datadog-datadogoptions)

*   [Debian Pbuilder](https://www.jenkins.io/doc/pipeline/steps/debian-pbuilder/)
    *   [`debianPbuilder`: Build Debian packages in a pbuilder environment](https://www.jenkins.io/doc/pipeline/steps/debian-pbuilder/#debianpbuilder-build-debian-packages-in-a-pbuilder-environment)

*   [Deep Security Smart Check Plugin](https://www.jenkins.io/doc/pipeline/steps/deepsecurity-smartcheck/)
    *   [`smartcheckScan`: Deep Security Smart Check Scan](https://www.jenkins.io/doc/pipeline/steps/deepsecurity-smartcheck/#smartcheckscan-deep-security-smart-check-scan)

*   [Deepcrawl Automation Hub](https://www.jenkins.io/doc/pipeline/steps/deepcrawl-test/)
    *   [`runAutomationHubBuild`: Run Deepcrawl Automation Hub Build](https://www.jenkins.io/doc/pipeline/steps/deepcrawl-test/#runautomationhubbuild-run-deepcrawl-automation-hub-build)

*   [DefectDojo Plugin](https://www.jenkins.io/doc/pipeline/steps/defectdojo/)
    *   [`defectDojoPublisher`: DefectDojoPublisher](https://www.jenkins.io/doc/pipeline/steps/defectdojo/#defectdojopublisher-defectdojopublisher)

*   [Defensics](https://www.jenkins.io/doc/pipeline/steps/defensics/)
    *   [`defensics`: Defensics fuzz test](https://www.jenkins.io/doc/pipeline/steps/defensics/#defensics-defensics-fuzz-test)
    *   [`step([$class: 'FuzzBuildStep'])`: Defensics fuzz test](https://www.jenkins.io/doc/pipeline/steps/defensics/#stepclass-fuzzbuildstep-defensics-fuzz-test)
    *   [`step([$class: 'FuzzPostBuildStep'])`: Defensics fuzz test](https://www.jenkins.io/doc/pipeline/steps/defensics/#stepclass-fuzzpostbuildstep-defensics-fuzz-test)

*   [Delinea Secret Server_Platform Plugin](https://www.jenkins.io/doc/pipeline/steps/thycotic-secret-server/)
    *   [`withSecretServer`: Use Delinea Secret Server or Platform Secrets](https://www.jenkins.io/doc/pipeline/steps/thycotic-secret-server/#withsecretserver-use-delinea-secret-server-or-platform-secrets)

*   [Delivery Pipeline Plugin](https://www.jenkins.io/doc/pipeline/steps/delivery-pipeline-plugin/)
    *   [`task`: Task](https://www.jenkins.io/doc/pipeline/steps/delivery-pipeline-plugin/#task-task)

*   [Delphix Plugin](https://www.jenkins.io/doc/pipeline/steps/delphix/)
    *   [`deleteVDB`: Delphix: Delete VDB](https://www.jenkins.io/doc/pipeline/steps/delphix/#deletevdb-delphix-delete-vdb)
    *   [`provisionVDBFromBookmark`: Delphix: Provision VDB From Bookmark](https://www.jenkins.io/doc/pipeline/steps/delphix/#provisionvdbfrombookmark-delphix-provision-vdb-from-bookmark)
    *   [`provisionVDBFromSnapshot`: Delphix: Provision VDB From Snapshot](https://www.jenkins.io/doc/pipeline/steps/delphix/#provisionvdbfromsnapshot-delphix-provision-vdb-from-snapshot)

*   [Deploy Dashboard Plugin by Namecheap](https://www.jenkins.io/doc/pipeline/steps/deploy-dashboard/)
    *   [`buildAddUrl`: Build Add Url](https://www.jenkins.io/doc/pipeline/steps/deploy-dashboard/#buildaddurl-build-add-url)
    *   [`addDeployToDashboard`: Deployment](https://www.jenkins.io/doc/pipeline/steps/deploy-dashboard/#adddeploytodashboard-deployment)

*   [Deploy to container Plugin](https://www.jenkins.io/doc/pipeline/steps/deploy/)
    *   [`deploy`: Deploy war/ear to a container](https://www.jenkins.io/doc/pipeline/steps/deploy/#deploy-deploy-warear-to-a-container)

*   [Deploy to webMethods Integration Server Plugin](https://www.jenkins.io/doc/pipeline/steps/deploy-integrationserver/)
    *   [`deployintegrationserver`: Deploy to webMethods Integration Server](https://www.jenkins.io/doc/pipeline/steps/deploy-integrationserver/#deployintegrationserver-deploy-to-webmethods-integration-server)

*   [deployment-notification](https://www.jenkins.io/doc/pipeline/steps/deployment-notification/)
    *   [`awaitDeployment`: Awaiting for deployment](https://www.jenkins.io/doc/pipeline/steps/deployment-notification/#awaitdeployment-awaiting-for-deployment)

*   [DEPRECATED: Synopsys Security Scan](https://www.jenkins.io/doc/pipeline/steps/synopsys-security-scan/)
    *   [`step([$class: 'SecurityScanFreestyle'])`: DEPRECATED: Synopsys Security Scan](https://www.jenkins.io/doc/pipeline/steps/synopsys-security-scan/#stepclass-securityscanfreestyle-deprecated-synopsys-security-scan)
    *   [`synopsys_scan`: DEPRECATED: Synopsys Security Scan](https://www.jenkins.io/doc/pipeline/steps/synopsys-security-scan/#synopsys-scan-deprecated-synopsys-security-scan)

*   [Describe With Params Plugin](https://www.jenkins.io/doc/pipeline/steps/describe-with-params/)
    *   [`step([$class: 'DescribeWithParamsBuilder'])`: Describe with params](https://www.jenkins.io/doc/pipeline/steps/describe-with-params/#stepclass-describewithparamsbuilder-describe-with-params)

*   [DevOps Portal](https://www.jenkins.io/doc/pipeline/steps/devops-portal/)
    *   [`reportArtifactRelease`: Record an artifact release](https://www.jenkins.io/doc/pipeline/steps/devops-portal/#reportartifactrelease-record-an-artifact-release)
    *   [`reportBuild`: Record a build report](https://www.jenkins.io/doc/pipeline/steps/devops-portal/#reportbuild-record-a-build-report)
    *   [`reportDeployOperation`: Record a Deployment operation](https://www.jenkins.io/doc/pipeline/steps/devops-portal/#reportdeployoperation-record-a-deployment-operation)
    *   [`reportJMeterPerformanceTest`: Record a performance test with JMeter](https://www.jenkins.io/doc/pipeline/steps/devops-portal/#reportjmeterperformancetest-record-a-performance-test-with-jmeter)
    *   [`reportMavenDependenciesAnalysis`: Record a dependencies analysis](https://www.jenkins.io/doc/pipeline/steps/devops-portal/#reportmavendependenciesanalysis-record-a-dependencies-analysis)
    *   [`reportPerformanceTest`: Record a performance test](https://www.jenkins.io/doc/pipeline/steps/devops-portal/#reportperformancetest-record-a-performance-test)
    *   [`reportQualityAudit`: Record a quality audit manually](https://www.jenkins.io/doc/pipeline/steps/devops-portal/#reportqualityaudit-record-a-quality-audit-manually)
    *   [`reportSonarQubeAudit`: Record a SonarQube quality audit](https://www.jenkins.io/doc/pipeline/steps/devops-portal/#reportsonarqubeaudit-record-a-sonarqube-quality-audit)
    *   [`reportSurefireTest`: Record a Surefire UT report](https://www.jenkins.io/doc/pipeline/steps/devops-portal/#reportsurefiretest-record-a-surefire-ut-report)
    *   [`reportUnitTest`: Record a UT report manually](https://www.jenkins.io/doc/pipeline/steps/devops-portal/#reportunittest-record-a-ut-report-manually)

*   [Diawi Upload Plugin](https://www.jenkins.io/doc/pipeline/steps/diawi-upload/)
    *   [`step([$class: 'DiawiUploader'])`: Diawi Upload Step](https://www.jenkins.io/doc/pipeline/steps/diawi-upload/#stepclass-diawiuploader-diawi-upload-step)

*   [Digital.ai App Management Publisher](https://www.jenkins.io/doc/pipeline/steps/ease-plugin/)
    *   [`step([$class: 'ApperianRecorder'])`: Digital.ai App Management Publisher](https://www.jenkins.io/doc/pipeline/steps/ease-plugin/#stepclass-apperianrecorder-digital-ai-app-management-publisher)

*   [Dimensions Plugin](https://www.jenkins.io/doc/pipeline/steps/dimensionsscm/)
    *   [`dimensionsscm`: Dimensions](https://www.jenkins.io/doc/pipeline/steps/dimensionsscm/#dimensionsscm-dimensions)

*   [Dingding JSON Pusher Plugin](https://www.jenkins.io/doc/pipeline/steps/dingding-json-pusher/)
    *   [`dingding`: Dingding Json Pusher](https://www.jenkins.io/doc/pipeline/steps/dingding-json-pusher/#dingding-dingding-json-pusher)

*   [DingTalk](https://www.jenkins.io/doc/pipeline/steps/dingding-notifications/)
    *   [`dingtalk`: Send DingTalk message](https://www.jenkins.io/doc/pipeline/steps/dingding-notifications/#dingtalk-send-dingtalk-message)

*   [Discord Notifier](https://www.jenkins.io/doc/pipeline/steps/discord-notifier/)
    *   [`discordSend`: Send an embed message to Webhook URL](https://www.jenkins.io/doc/pipeline/steps/discord-notifier/#discordsend-send-an-embed-message-to-webhook-url)

*   [Docker Compose Build Step Plugin](https://www.jenkins.io/doc/pipeline/steps/docker-compose-build-step/)
    *   [`step([$class: 'DockerComposeBuilder'])`: Docker Compose Build Step](https://www.jenkins.io/doc/pipeline/steps/docker-compose-build-step/#stepclass-dockercomposebuilder-docker-compose-build-step)

*   [Docker Pipeline](https://www.jenkins.io/doc/pipeline/steps/docker-workflow/)
    *   [`dockerFingerprintFrom`: Record trace of a Docker image used in FROM](https://www.jenkins.io/doc/pipeline/steps/docker-workflow/#dockerfingerprintfrom-record-trace-of-a-docker-image-used-in-from)
    *   [`dockerFingerprintRun`: Record trace of a Docker image run in a container](https://www.jenkins.io/doc/pipeline/steps/docker-workflow/#dockerfingerprintrun-record-trace-of-a-docker-image-run-in-a-container)
    *   [`withDockerContainer`: Run build steps inside a Docker container](https://www.jenkins.io/doc/pipeline/steps/docker-workflow/#withdockercontainer-run-build-steps-inside-a-docker-container)
    *   [`withDockerRegistry`: Sets up Docker registry endpoint](https://www.jenkins.io/doc/pipeline/steps/docker-workflow/#withdockerregistry-sets-up-docker-registry-endpoint)
    *   [`withDockerServer`: Sets up Docker server endpoint](https://www.jenkins.io/doc/pipeline/steps/docker-workflow/#withdockerserver-sets-up-docker-server-endpoint)

*   [Docker plugin](https://www.jenkins.io/doc/pipeline/steps/docker-plugin/)
    *   [`dockerNode`: Docker Node (⚠️ Experimental)](https://www.jenkins.io/doc/pipeline/steps/docker-plugin/#dockernode-docker-node-%EF%B8%8F-experimental)
    *   [`step([$class: 'DockerBuilderControl'])`: Start/Stop Docker Containers](https://www.jenkins.io/doc/pipeline/steps/docker-plugin/#stepclass-dockerbuildercontrol-startstop-docker-containers)
    *   [`step([$class: 'DockerBuilderPublisher'])`: Build / Publish Docker Image](https://www.jenkins.io/doc/pipeline/steps/docker-plugin/#stepclass-dockerbuilderpublisher-build-publish-docker-image)

*   [Dogu Integration](https://www.jenkins.io/doc/pipeline/steps/dogu-integration/)
    *   [`doguRunRoutine`: Dogu pipeline step](https://www.jenkins.io/doc/pipeline/steps/dogu-integration/#dogurunroutine-dogu-pipeline-step)
    *   [`doguUploadApplication`: Dogu application step](https://www.jenkins.io/doc/pipeline/steps/dogu-integration/#doguuploadapplication-dogu-application-step)

*   [Doktor](https://www.jenkins.io/doc/pipeline/steps/doktor/)
    *   [`doktor`: Publish documentation to Confluence](https://www.jenkins.io/doc/pipeline/steps/doktor/#doktor-publish-documentation-to-confluence)

*   [Dotcom-Monitor LoadView](https://www.jenkins.io/doc/pipeline/steps/dotcommonitor-loadview/)
    *   [`dotcomMonitor`: LoadView-Run load test scenario](https://www.jenkins.io/doc/pipeline/steps/dotcommonitor-loadview/#dotcommonitor-loadview-run-load-test-scenario)

*   [DotCover](https://www.jenkins.io/doc/pipeline/steps/dotcoverrunner/)
    *   [`dotcover`: Generate code coverage data and report(s)](https://www.jenkins.io/doc/pipeline/steps/dotcoverrunner/#dotcover-generate-code-coverage-data-and-reports)

*   [Downstream Build Cache Plugin](https://www.jenkins.io/doc/pipeline/steps/downstream-build-cache/)
    *   [`downstreamBuilds`: Provide list of downstream builds](https://www.jenkins.io/doc/pipeline/steps/downstream-build-cache/#downstreambuilds-provide-list-of-downstream-builds)

*   [Dynatrace Application Monitoring Plugin (deprecated)](https://www.jenkins.io/doc/pipeline/steps/dynatrace-dashboard/)
    *   [`appMonPublishTestResults`: Dynatrace AppMon - Finish Registered Tests Runs and Publish Results](https://www.jenkins.io/doc/pipeline/steps/dynatrace-dashboard/#appmonpublishtestresults-dynatrace-appmon-finish-registered-tests-runs-and-publish-results)
    *   [`appMonRegisterTestRun`: Dynatrace AppMon - Register Test Run](https://www.jenkins.io/doc/pipeline/steps/dynatrace-dashboard/#appmonregistertestrun-dynatrace-appmon-register-test-run)
    *   [`step([$class: 'TAReportingRecorder'])`: Dynatrace AppMon - Finish Registered Tests Runs and Publish Results](https://www.jenkins.io/doc/pipeline/steps/dynatrace-dashboard/#stepclass-tareportingrecorder-dynatrace-appmon-finish-registered-tests-runs-and-publish-results)
    *   [`step([$class: 'TATestRunRegistrationBuildStep'])`: Dynatrace AppMon - Register Test Run](https://www.jenkins.io/doc/pipeline/steps/dynatrace-dashboard/#stepclass-tatestrunregistrationbuildstep-dynatrace-appmon-register-test-run)
    *   [`appMonBuildEnvironment`: Use Dynatrace AppMon to monitor tests](https://www.jenkins.io/doc/pipeline/steps/dynatrace-dashboard/#appmonbuildenvironment-use-dynatrace-appmon-to-monitor-tests)

*   [ecu.test execution plugin](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/)
    *   [`ttCheckPackage`: [TT] Check an ecu.test package](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttcheckpackage-tt-check-an-ecu-test-package)
    *   [`ttGenerateReports`: [TT] Generate ecu.test reports](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttgeneratereports-tt-generate-ecu-test-reports)
    *   [`ttLoadConfig`: [TT] Load ecu.test configurations](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttloadconfig-tt-load-ecu-test-configurations)
    *   [`ttProvideGeneratedReports`: [TT] Provide generated ecu.test reports as job artifacts.](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttprovidegeneratedreports-tt-provide-generated-ecu-test-reports-as-job-artifacts)
    *   [`ttProvideLogs`: [TT] Provide ecu.test logs as job artifacts.](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttprovidelogs-tt-provide-ecu-test-logs-as-job-artifacts)
    *   [`ttProvideReports`: [TT] Provide ecu.test reports as job artifacts.](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttprovidereports-tt-provide-ecu-test-reports-as-job-artifacts)
    *   [`ttProvideUnitReports`: [TT] Provide generated unit reports as job test results.](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttprovideunitreports-tt-provide-generated-unit-reports-as-job-test-results)
    *   [`ttRunPackage`: [TT] Run an ecu.test package](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttrunpackage-tt-run-an-ecu-test-package)
    *   [`ttRunProject`: [TT] Run an ecu.test project](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttrunproject-tt-run-an-ecu-test-project)
    *   [`ttRunTestFolder`: [TT] Run an ecu.test test folder](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttruntestfolder-tt-run-an-ecu-test-test-folder)
    *   [`ttStartTool`: [TT] Start an ecu.test or trace.check instance](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttstarttool-tt-start-an-ecu-test-or-trace-check-instance)
    *   [`ttStopTool`: [TT] Stop an ecu.test or trace.check instance](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttstoptool-tt-stop-an-ecu-test-or-trace-check-instance)
    *   [`ttUploadReports`: [TT] Upload ecu.test reports to test.guide](https://www.jenkins.io/doc/pipeline/steps/ecu-test-execution/#ttuploadreports-tt-upload-ecu-test-reports-to-test-guide)

*   [ECX Copy Data Management Plugin](https://www.jenkins.io/doc/pipeline/steps/catalogic-ecx/)
    *   [`step([$class: 'ECXCDMBuilder'])`: Catalogic ECX CDM Integration](https://www.jenkins.io/doc/pipeline/steps/catalogic-ecx/#stepclass-ecxcdmbuilder-catalogic-ecx-cdm-integration)

*   [EDAS Plugin](https://www.jenkins.io/doc/pipeline/steps/alibabacloud-edas/)
    *   [`edasClient`: Deploy to EDAS](https://www.jenkins.io/doc/pipeline/steps/alibabacloud-edas/#edasclient-deploy-to-edas)

*   [Eggplant Runner Plugin](https://www.jenkins.io/doc/pipeline/steps/eggplant-runner/)
    *   [`eggplantRunner`: Eggplant Runner](https://www.jenkins.io/doc/pipeline/steps/eggplant-runner/#eggplantrunner-eggplant-runner)

*   [Eiffel Broadcaster Plugin](https://www.jenkins.io/doc/pipeline/steps/eiffel-broadcaster/)
    *   [`buildWithEiffel`: Build a job with custom Eiffel activity name](https://www.jenkins.io/doc/pipeline/steps/eiffel-broadcaster/#buildwitheiffel-build-a-job-with-custom-eiffel-activity-name)
    *   [`createPackageURL`: Construct a package URL and return it as a string](https://www.jenkins.io/doc/pipeline/steps/eiffel-broadcaster/#createpackageurl-construct-a-package-url-and-return-it-as-a-string)
    *   [`publishEiffelArtifacts`: Publishes previously announced Eiffel artifacts](https://www.jenkins.io/doc/pipeline/steps/eiffel-broadcaster/#publisheiffelartifacts-publishes-previously-announced-eiffel-artifacts)
    *   [`sendEiffelEvent`: Send an Eiffel event](https://www.jenkins.io/doc/pipeline/steps/eiffel-broadcaster/#sendeiffelevent-send-an-eiffel-event)

*   [ElasTest Plugin (deprecated)](https://www.jenkins.io/doc/pipeline/steps/elastest/)
    *   [`elastest`: Integrate Jenkins with ElasTest](https://www.jenkins.io/doc/pipeline/steps/elastest/#elastest-integrate-jenkins-with-elastest)
    *   [`wrap([$class: 'ElasTestBuildWrapper'])`: Integrate Jenkins with ElasTest](https://www.jenkins.io/doc/pipeline/steps/elastest/#wrapclass-elastestbuildwrapper-integrate-jenkins-with-elastest)

*   [Elasticsearch Query](https://www.jenkins.io/doc/pipeline/steps/elasticsearch-query/)
    *   [`step([$class: 'ElasticsearchQueryBuilder'])`: Elasticsearch Query](https://www.jenkins.io/doc/pipeline/steps/elasticsearch-query/#stepclass-elasticsearchquerybuilder-elasticsearch-query)

*   [Email Extension Plugin](https://www.jenkins.io/doc/pipeline/steps/email-ext/)
    *   [`emailext`: Extended Email](https://www.jenkins.io/doc/pipeline/steps/email-ext/#emailext-extended-email)
    *   [`emailextrecipients`: Extended Email Recipients](https://www.jenkins.io/doc/pipeline/steps/email-ext/#emailextrecipients-extended-email-recipients)

*   [Embeddable Build Status Plugin](https://www.jenkins.io/doc/pipeline/steps/embeddable-build-status/)
    *   [`addEmbeddableBadgeConfiguration`: Add an Embeddable Badge Configuration](https://www.jenkins.io/doc/pipeline/steps/embeddable-build-status/#addembeddablebadgeconfiguration-add-an-embeddable-badge-configuration)

*   [Environment Dashboard Plugin](https://www.jenkins.io/doc/pipeline/steps/environment-dashboard/)
    *   [`environmentDashboard`: Details for Environment dashboard](https://www.jenkins.io/doc/pipeline/steps/environment-dashboard/#environmentdashboard-details-for-environment-dashboard)

*   [Exclusion Plug-in](https://www.jenkins.io/doc/pipeline/steps/Exclusion/)
    *   [`step([$class: 'CriticalBlockEnd'])`: Critical block end](https://www.jenkins.io/doc/pipeline/steps/Exclusion/#stepclass-criticalblockend-critical-block-end)
    *   [`step([$class: 'CriticalBlockStart'])`: Critical block start](https://www.jenkins.io/doc/pipeline/steps/Exclusion/#stepclass-criticalblockstart-critical-block-start)

*   [Explain Error Plugin](https://www.jenkins.io/doc/pipeline/steps/explain-error/)
    *   [`explainError`: Explain Error with AI](https://www.jenkins.io/doc/pipeline/steps/explain-error/#explainerror-explain-error-with-ai)

*   [Extensive Testing Plugin](https://www.jenkins.io/doc/pipeline/steps/extensivetesting/)
    *   [`step([$class: 'ExtensiveTestingBuilder'])`: Launch eXtensive Testing job](https://www.jenkins.io/doc/pipeline/steps/extensivetesting/#stepclass-extensivetestingbuilder-launch-extensive-testing-job)

*   [External Workspace Manager Plugin](https://www.jenkins.io/doc/pipeline/steps/external-workspace-manager/)
    *   [`exws`: Use external workspace](https://www.jenkins.io/doc/pipeline/steps/external-workspace-manager/#exws-use-external-workspace)
    *   [`exwsAllocate`: Allocate external workspace](https://www.jenkins.io/doc/pipeline/steps/external-workspace-manager/#exwsallocate-allocate-external-workspace)

*   [Fedora Module Build System Plugin](https://www.jenkins.io/doc/pipeline/steps/fedora-module-build-system/)
    *   [`queryModuleBuildRequest`: Query Module Build Request](https://www.jenkins.io/doc/pipeline/steps/fedora-module-build-system/#querymodulebuildrequest-query-module-build-request)
    *   [`submitModuleBuildRequest`: Submit Module Build Request](https://www.jenkins.io/doc/pipeline/steps/fedora-module-build-system/#submitmodulebuildrequest-submit-module-build-request)

*   [Figlet Buildstep](https://www.jenkins.io/doc/pipeline/steps/figlet-buildstep/)
    *   [`figlet`: Figlet](https://www.jenkins.io/doc/pipeline/steps/figlet-buildstep/#figlet-figlet)

*   [File Operations Plugin](https://www.jenkins.io/doc/pipeline/steps/file-operations/)
    *   [`fileOperations`: File Operations](https://www.jenkins.io/doc/pipeline/steps/file-operations/#fileoperations-file-operations)

*   [File Parameter Plugin](https://www.jenkins.io/doc/pipeline/steps/file-parameters/)
    *   [`withFileParameter`: Bind file parameter](https://www.jenkins.io/doc/pipeline/steps/file-parameters/#withfileparameter-bind-file-parameter)

*   [Finite State Analysis](https://www.jenkins.io/doc/pipeline/steps/finite-state-analysis/)
    *   [`finiteStateAnalyzeBinary`: Finite State Analyze Binary](https://www.jenkins.io/doc/pipeline/steps/finite-state-analysis/#finitestateanalyzebinary-finite-state-analyze-binary)
    *   [`finiteStateImportSbom`: Finite State Import SBOM](https://www.jenkins.io/doc/pipeline/steps/finite-state-analysis/#finitestateimportsbom-finite-state-import-sbom)
    *   [`finiteStateImportThirdParty`: Finite State Import 3rd Party Scan](https://www.jenkins.io/doc/pipeline/steps/finite-state-analysis/#finitestateimportthirdparty-finite-state-import-3rd-party-scan)

*   [FitNesse plugin](https://www.jenkins.io/doc/pipeline/steps/fitnesse/)
    *   [`step([$class: 'FitnesseBuilder'])`: Execute FitNesse tests](https://www.jenkins.io/doc/pipeline/steps/fitnesse/#stepclass-fitnessebuilder-execute-fitnesse-tests)
    *   [`step([$class: 'FitnesseResultsRecorder'])`: Publish Fitnesse results report](https://www.jenkins.io/doc/pipeline/steps/fitnesse/#stepclass-fitnesseresultsrecorder-publish-fitnesse-results-report)

*   [Fluentd Plugin](https://www.jenkins.io/doc/pipeline/steps/fluentd/)
    *   [`step([$class: 'Fluentd'])`: Send to Fluentd](https://www.jenkins.io/doc/pipeline/steps/fluentd/#stepclass-fluentd-send-to-fluentd)

*   [Flyway Runner](https://www.jenkins.io/doc/pipeline/steps/flyway-runner/)
    *   [`flywayrunner`: Invoke Flyway](https://www.jenkins.io/doc/pipeline/steps/flyway-runner/#flywayrunner-invoke-flyway)

*   [Folder Properties Plugin](https://www.jenkins.io/doc/pipeline/steps/folder-properties/)
    *   [`withFolderProperties`: A step to retrieve folder properties](https://www.jenkins.io/doc/pipeline/steps/folder-properties/#withfolderproperties-a-step-to-retrieve-folder-properties)
    *   [`withFolderProperties`: Folder Properties](https://www.jenkins.io/doc/pipeline/steps/folder-properties/#withfolderproperties-folder-properties)

*   [Forensics API Plugin](https://www.jenkins.io/doc/pipeline/steps/forensics-api/)
    *   [`mineRepository`: Mine SCM repository](https://www.jenkins.io/doc/pipeline/steps/forensics-api/#minerepository-mine-scm-repository)
    *   [`discoverReferenceBuild`: Discover reference build](https://www.jenkins.io/doc/pipeline/steps/forensics-api/#discoverreferencebuild-discover-reference-build)

*   [FortiCNP CICD Plugin](https://www.jenkins.io/doc/pipeline/steps/forticwp-cicd/)
    *   [`fortiCWPScanner`: Scan container images](https://www.jenkins.io/doc/pipeline/steps/forticwp-cicd/#forticwpscanner-scan-container-images)

*   [Fortify](https://www.jenkins.io/doc/pipeline/steps/fortify/)
    *   [`fortifyClean`: Run Fortify SCA clean](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyclean-run-fortify-sca-clean)
    *   [`fortifyRemoteAnalysis`: Upload a project for remote Fortify SCA analysis](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyremoteanalysis-upload-a-project-for-remote-fortify-sca-analysis)
    *   [`fortifyRemoteArguments`: Set options for remote Fortify SCA analysis](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyremotearguments-set-options-for-remote-fortify-sca-analysis)
    *   [`fortifyRemoteScan`: Upload a translated project for remote scan](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyremotescan-upload-a-translated-project-for-remote-scan)
    *   [`fortifyScan`: Run Fortify SCA scan](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyscan-run-fortify-sca-scan)
    *   [`fortifyTranslate`: Run Fortify SCA translation](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifytranslate-run-fortify-sca-translation)
    *   [`fortifyUpdate`: Update Fortify Security Content](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyupdate-update-fortify-security-content)
    *   [`fortifyUpload`: Upload Fortify scan results to SSC](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyupload-upload-fortify-scan-results-to-ssc)
    *   [`fortifyRemoteArguments`: Set options for remote Fortify SCA analysis](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyremotearguments-set-options-for-remote-fortify-sca-analysis)
    *   [`fortifyRemoteScan`: Upload a translated project for remote scan](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyremotescan-upload-a-translated-project-for-remote-scan)
    *   [`fortifyRemoteAnalysis`: Upload a project for remote Fortify SCA analysis](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyremoteanalysis-upload-a-project-for-remote-fortify-sca-analysis)
    *   [`fortifyClean`: Run Fortify SCA clean](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyclean-run-fortify-sca-clean)
    *   [`fortifyScan`: Run Fortify SCA scan](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyscan-run-fortify-sca-scan)
    *   [`fortifyTranslate`: Run Fortify SCA translation](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifytranslate-run-fortify-sca-translation)
    *   [`fortifyUpdate`: Update Fortify Security Content](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyupdate-update-fortify-security-content)
    *   [`fortifyUpload`: Upload Fortify scan results to SSC](https://www.jenkins.io/doc/pipeline/steps/fortify/#fortifyupload-upload-fortify-scan-results-to-ssc)

*   [Fortify on Demand](https://www.jenkins.io/doc/pipeline/steps/fortify-on-demand-uploader/)
    *   [`fodPollResults`: Poll Fortify on Demand for Results](https://www.jenkins.io/doc/pipeline/steps/fortify-on-demand-uploader/#fodpollresults-poll-fortify-on-demand-for-results)
    *   [`fodStaticAssessment`: Run Fortify on Demand Upload](https://www.jenkins.io/doc/pipeline/steps/fortify-on-demand-uploader/#fodstaticassessment-run-fortify-on-demand-upload)
    *   [`step([$class: 'FortifyDastFreeStyleBuildStep'])`: Fortify on Demand Dynamic Assessment](https://www.jenkins.io/doc/pipeline/steps/fortify-on-demand-uploader/#stepclass-fortifydastfreestylebuildstep-fortify-on-demand-dynamic-assessment)
    *   [`fodPollResults`: Poll Fortify on Demand for Results](https://www.jenkins.io/doc/pipeline/steps/fortify-on-demand-uploader/#fodpollresults-poll-fortify-on-demand-for-results)
    *   [`fodStaticAssessment`: Run Fortify on Demand Upload](https://www.jenkins.io/doc/pipeline/steps/fortify-on-demand-uploader/#fodstaticassessment-run-fortify-on-demand-upload)
    *   [`step([$class: 'PollingBuildStep'])`: Poll Fortify on Demand for Results](https://www.jenkins.io/doc/pipeline/steps/fortify-on-demand-uploader/#stepclass-pollingbuildstep-poll-fortify-on-demand-for-results)
    *   [`step([$class: 'StaticAssessmentBuildStep'])`: Fortify on Demand Static Assessment](https://www.jenkins.io/doc/pipeline/steps/fortify-on-demand-uploader/#stepclass-staticassessmentbuildstep-fortify-on-demand-static-assessment)

*   [Frugal Testing](https://www.jenkins.io/doc/pipeline/steps/frugal-testing/)
    *   [`frugalTesting`: Frugal Testing](https://www.jenkins.io/doc/pipeline/steps/frugal-testing/#frugaltesting-frugal-testing)

*   [FTP Rename Plugin](https://www.jenkins.io/doc/pipeline/steps/ftp-rename/)
    *   [`step([$class: 'FtpRenameBuilder'])`: FTP Rename](https://www.jenkins.io/doc/pipeline/steps/ftp-rename/#stepclass-ftprenamebuilder-ftp-rename)
    *   [`step([$class: 'FtpRenamePublisher'])`: FTP Rename](https://www.jenkins.io/doc/pipeline/steps/ftp-rename/#stepclass-ftprenamepublisher-ftp-rename)

*   [Gamekins Plugin](https://www.jenkins.io/doc/pipeline/steps/gamekins/)
    *   [`gamekins`: Gamekins Publisher](https://www.jenkins.io/doc/pipeline/steps/gamekins/#gamekins-gamekins-publisher)

*   [Gating Core](https://www.jenkins.io/doc/pipeline/steps/gating-core/)
    *   [`requireResources`: GatingStep](https://www.jenkins.io/doc/pipeline/steps/gating-core/#requireresources-gatingstep)

*   [Gatling Check Plugin](https://www.jenkins.io/doc/pipeline/steps/gatling-check/)
    *   [`gatlingCheck`: GatlingCheckStep](https://www.jenkins.io/doc/pipeline/steps/gatling-check/#gatlingcheck-gatlingcheckstep)
    *   [`step([$class: 'GatlingChecker'])`: Gatling Checker](https://www.jenkins.io/doc/pipeline/steps/gatling-check/#stepclass-gatlingchecker-gatling-checker)

*   [Gatling Jenkins Plugin](https://www.jenkins.io/doc/pipeline/steps/gatling/)
    *   [`gatlingArchive`: Archive Gatling reports](https://www.jenkins.io/doc/pipeline/steps/gatling/#gatlingarchive-archive-gatling-reports)
    *   [`step([$class: 'GatlingPublisher'])`: Track a Gatling load simulation](https://www.jenkins.io/doc/pipeline/steps/gatling/#stepclass-gatlingpublisher-track-a-gatling-load-simulation)

*   [GCloud SDK Plugin](https://www.jenkins.io/doc/pipeline/steps/gcloud-sdk/)
    *   [`wrap([$class: 'GCloudBuildWrapper'])`: GCloud SDK authentication](https://www.jenkins.io/doc/pipeline/steps/gcloud-sdk/#wrapclass-gcloudbuildwrapper-gcloud-sdk-authentication)

*   [GCR Vulnerability Scanner Plugin](https://www.jenkins.io/doc/pipeline/steps/gcr-scanner/)
    *   [`gcrImageVulnerabilityScanner`: GCR Image Vulnerability Scanner](https://www.jenkins.io/doc/pipeline/steps/gcr-scanner/#gcrimagevulnerabilityscanner-gcr-image-vulnerability-scanner)

*   [GeneXus Plugin](https://www.jenkins.io/doc/pipeline/steps/genexus/)
    *   [`gxserver`: Checks out (or updates) a GeneXus Knowledge Base from a GeneXus Server](https://www.jenkins.io/doc/pipeline/steps/genexus/#gxserver-checks-out-or-updates-a-genexus-knowledge-base-from-a-genexus-server)

*   [Gerrit Code Review plugin](https://www.jenkins.io/doc/pipeline/steps/gerrit-code-review/)
    *   [`gerritCheck`: Gerrit Review Check](https://www.jenkins.io/doc/pipeline/steps/gerrit-code-review/#gerritcheck-gerrit-review-check)
    *   [`gerritComment`: Gerrit Review Comment](https://www.jenkins.io/doc/pipeline/steps/gerrit-code-review/#gerritcomment-gerrit-review-comment)
    *   [`gerritReview`: Gerrit Review Label](https://www.jenkins.io/doc/pipeline/steps/gerrit-code-review/#gerritreview-gerrit-review-label)

*   [Gerrit Trigger](https://www.jenkins.io/doc/pipeline/steps/gerrit-trigger/)
    *   [`setGerritReview`: Set Gerrit review](https://www.jenkins.io/doc/pipeline/steps/gerrit-trigger/#setgerritreview-set-gerrit-review)

*   [Ghost Inspector Plugin](https://www.jenkins.io/doc/pipeline/steps/ghost-inspector/)
    *   [`ghostInspector`: Run Ghost Inspector Test Suite](https://www.jenkins.io/doc/pipeline/steps/ghost-inspector/#ghostinspector-run-ghost-inspector-test-suite)

*   [Giphy API Plugin](https://www.jenkins.io/doc/pipeline/steps/pipeline-giphy-api/)
    *   [`giphyRandom`: GiphyRandomStepImpl](https://www.jenkins.io/doc/pipeline/steps/pipeline-giphy-api/#giphyrandom-giphyrandomstepimpl)
    *   [`giphySearch`: GiphySearchStepImpl](https://www.jenkins.io/doc/pipeline/steps/pipeline-giphy-api/#giphysearch-giphysearchstepimpl)
    *   [`giphySearchRandomByKeyword`: GiphySearchRandomByKeywordStep](https://www.jenkins.io/doc/pipeline/steps/pipeline-giphy-api/#giphysearchrandombykeyword-giphysearchrandombykeywordstep)
    *   [`giphyTranslate`: GiphyTranslateStepImpl](https://www.jenkins.io/doc/pipeline/steps/pipeline-giphy-api/#giphytranslate-giphytranslatestepimpl)

*   [Git Automerger Plugin](https://www.jenkins.io/doc/pipeline/steps/git-automerger/)
    *   [`gitAutomerger`: Git automerge](https://www.jenkins.io/doc/pipeline/steps/git-automerger/#gitautomerger-git-automerge)

*   [Git Bisect Plugin](https://www.jenkins.io/doc/pipeline/steps/git-bisect/)
    *   [`gitbisect`: Git Bisect](https://www.jenkins.io/doc/pipeline/steps/git-bisect/#gitbisect-git-bisect)
    *   [`step([$class: 'GitBisectOnFailure'])`: Git Bisect On Failure](https://www.jenkins.io/doc/pipeline/steps/git-bisect/#stepclass-gitbisectonfailure-git-bisect-on-failure)

*   [Git Changelog](https://www.jenkins.io/doc/pipeline/steps/git-changelog/)
    *   [`getHighestSemanticVersion`: Get the highest version, determined by tags in repo. Also tag available as '.findTag().orElse("")'.](https://www.jenkins.io/doc/pipeline/steps/git-changelog/#gethighestsemanticversion-get-the-highest-version-determined-by-tags-in-repo-also-tag-available-as-findtag-orelse)
    *   [`getNextSemanticVersion`: Next semantic version based on tags and conventional commits in Git repository](https://www.jenkins.io/doc/pipeline/steps/git-changelog/#getnextsemanticversion-next-semantic-version-based-on-tags-and-conventional-commits-in-git-repository)
    *   [`gitChangelog`: Changelog from Git repository](https://www.jenkins.io/doc/pipeline/steps/git-changelog/#gitchangelog-changelog-from-git-repository)
    *   [`step([$class: 'GitChangelogRecorder'])`: Git Changelog](https://www.jenkins.io/doc/pipeline/steps/git-changelog/#stepclass-gitchangelogrecorder-git-changelog)

*   [Git Collect Plugin](https://www.jenkins.io/doc/pipeline/steps/git-collect/)
    *   [`collectGit`: Git Collect: Register Local Data](https://www.jenkins.io/doc/pipeline/steps/git-collect/#collectgit-git-collect-register-local-data)

*   [Git Forensics Plugin](https://www.jenkins.io/doc/pipeline/steps/git-forensics/)
    *   [`gitDiffStat`: Git Diff Statistics](https://www.jenkins.io/doc/pipeline/steps/git-forensics/#gitdiffstat-git-diff-statistics)
    *   [`discoverGitReferenceBuild`: Discover Git reference build](https://www.jenkins.io/doc/pipeline/steps/git-forensics/#discovergitreferencebuild-discover-git-reference-build)

*   [Git plugin](https://www.jenkins.io/doc/pipeline/steps/git/)
    *   [`git`: Git](https://www.jenkins.io/doc/pipeline/steps/git/#git-git)

*   [Git Push Plugin](https://www.jenkins.io/doc/pipeline/steps/git-push/)
    *   [`gitPush`: Git Push](https://www.jenkins.io/doc/pipeline/steps/git-push/#gitpush-git-push)

*   [Gitea Plugin](https://www.jenkins.io/doc/pipeline/steps/gitea/)
    *   [`publishGiteaAssets`: Publishes an asset to the gitea release, if the build was triggered by an release](https://www.jenkins.io/doc/pipeline/steps/gitea/#publishgiteaassets-publishes-an-asset-to-the-gitea-release-if-the-build-was-triggered-by-an-release)

*   [Gitee Plugin](https://www.jenkins.io/doc/pipeline/steps/gitee/)
    *   [`acceptGiteeMR`: Accept Gitee Pull Request](https://www.jenkins.io/doc/pipeline/steps/gitee/#acceptgiteemr-accept-gitee-pull-request)
    *   [`addGiteeMRComment`: Add comment on Gitee Pull Request](https://www.jenkins.io/doc/pipeline/steps/gitee/#addgiteemrcomment-add-comment-on-gitee-pull-request)

*   [GitHub Coverage Reporter](https://www.jenkins.io/doc/pipeline/steps/github-coverage-reporter/)
    *   [`publishCoverageGithub`: Publish Coverage reports to Github](https://www.jenkins.io/doc/pipeline/steps/github-coverage-reporter/#publishcoveragegithub-publish-coverage-reports-to-github)

*   [GitHub Integration Plugin](https://www.jenkins.io/doc/pipeline/steps/github-pullrequest/)
    *   [`setGitHubPullRequestStatus`: Set GitHub PullRequest Commit Status](https://www.jenkins.io/doc/pipeline/steps/github-pullrequest/#setgithubpullrequeststatus-set-github-pullrequest-commit-status)
    *   [`githubPRStatusPublisher`: GitHub PR: set PR status](https://www.jenkins.io/doc/pipeline/steps/github-pullrequest/#githubprstatuspublisher-github-pr-set-pr-status)
    *   [`githubPRClosePublisher`: GitHub PR: close PR](https://www.jenkins.io/doc/pipeline/steps/github-pullrequest/#githubprclosepublisher-github-pr-close-pr)
    *   [`githubPRComment`: GitHub PR: post comment](https://www.jenkins.io/doc/pipeline/steps/github-pullrequest/#githubprcomment-github-pr-post-comment)
    *   [`githubPRAddLabels`: GitHub PR: add labels](https://www.jenkins.io/doc/pipeline/steps/github-pullrequest/#githubpraddlabels-github-pr-add-labels)
    *   [`githubPRRemoveLabels`: GitHub PR: remove labels](https://www.jenkins.io/doc/pipeline/steps/github-pullrequest/#githubprremovelabels-github-pr-remove-labels)
    *   [`gitHubPRStatus`: GitHub PR: set 'pending' status](https://www.jenkins.io/doc/pipeline/steps/github-pullrequest/#githubprstatus-github-pr-set-pending-status)

*   [GitHub Issues Plugin](https://www.jenkins.io/doc/pipeline/steps/github-issues/)
    *   [`step([$class: 'GitHubIssueNotifier'])`: Create GitHub issue on failure](https://www.jenkins.io/doc/pipeline/steps/github-issues/#stepclass-githubissuenotifier-create-github-issue-on-failure)

*   [GitHub plugin](https://www.jenkins.io/doc/pipeline/steps/github/)
    *   [`step([$class: 'GitHubCommitNotifier'])`: Set build status on GitHub commit [deprecated]](https://www.jenkins.io/doc/pipeline/steps/github/#stepclass-githubcommitnotifier-set-build-status-on-github-commit-deprecated)
    *   [`step([$class: 'GitHubCommitStatusSetter'])`: Set GitHub commit status (universal)](https://www.jenkins.io/doc/pipeline/steps/github/#stepclass-githubcommitstatussetter-set-github-commit-status-universal)
    *   [`step([$class: 'GitHubSetCommitStatusBuilder'])`: Set build status to "pending" on GitHub commit](https://www.jenkins.io/doc/pipeline/steps/github/#stepclass-githubsetcommitstatusbuilder-set-build-status-to-pending-on-github-commit)

*   [GitHub Pull Request Builder](https://www.jenkins.io/doc/pipeline/steps/ghprb/)
    *   [`step([$class: 'GhprbPullRequestMerge'])`: Github Pull Request Merger](https://www.jenkins.io/doc/pipeline/steps/ghprb/#stepclass-ghprbpullrequestmerge-github-pull-request-merger)

*   [GitHub Pull Request Coverage Status](https://www.jenkins.io/doc/pipeline/steps/github-pr-coverage-status/)
    *   [`step([$class: 'CompareCoverageAction'])`: Publish coverage to GitHub](https://www.jenkins.io/doc/pipeline/steps/github-pr-coverage-status/#stepclass-comparecoverageaction-publish-coverage-to-github)
    *   [`step([$class: 'MasterCoverageAction'])`: Record Master Coverage](https://www.jenkins.io/doc/pipeline/steps/github-pr-coverage-status/#stepclass-mastercoverageaction-record-master-coverage)

*   [Github Release Plugin](https://www.jenkins.io/doc/pipeline/steps/github-release/)
    *   [`createGitHubRelease`: createGitHubRelease](https://www.jenkins.io/doc/pipeline/steps/github-release/#creategithubrelease-creategithubrelease)
    *   [`listGitHubReleases`: listGitHubReleases](https://www.jenkins.io/doc/pipeline/steps/github-release/#listgithubreleases-listgithubreleases)
    *   [`uploadGithubReleaseAsset`: uploadGithubReleaseAsset](https://www.jenkins.io/doc/pipeline/steps/github-release/#uploadgithubreleaseasset-uploadgithubreleaseasset)

*   [GitHub Status Wrapper Plugin](https://www.jenkins.io/doc/pipeline/steps/pipeline-gitstatuswrapper/)
    *   [`gitStatusWrapper`: gitStatusWrapper](https://www.jenkins.io/doc/pipeline/steps/pipeline-gitstatuswrapper/#gitstatuswrapper-gitstatuswrapper)

*   [GitLab Plugin](https://www.jenkins.io/doc/pipeline/steps/gitlab-plugin/)
    *   [`GitLabMergeRequestLabelExists`: Check if a GitLab merge request has a specific label](https://www.jenkins.io/doc/pipeline/steps/gitlab-plugin/#gitlabmergerequestlabelexists-check-if-a-gitlab-merge-request-has-a-specific-label)
    *   [`acceptGitLabMR`: Accept GitLab Merge Request](https://www.jenkins.io/doc/pipeline/steps/gitlab-plugin/#acceptgitlabmr-accept-gitlab-merge-request)
    *   [`addGitLabMRComment`: Add comment on GitLab Merge Request](https://www.jenkins.io/doc/pipeline/steps/gitlab-plugin/#addgitlabmrcomment-add-comment-on-gitlab-merge-request)
    *   [`gitlabBuilds`: Notify gitlab about pending builds](https://www.jenkins.io/doc/pipeline/steps/gitlab-plugin/#gitlabbuilds-notify-gitlab-about-pending-builds)
    *   [`gitlabCommitStatus`: Update the commit status in GitLab depending on the build status](https://www.jenkins.io/doc/pipeline/steps/gitlab-plugin/#gitlabcommitstatus-update-the-commit-status-in-gitlab-depending-on-the-build-status)
    *   [`updateGitlabCommitStatus`: Update the commit status in GitLab](https://www.jenkins.io/doc/pipeline/steps/gitlab-plugin/#updategitlabcommitstatus-update-the-commit-status-in-gitlab)

*   [Global YAML Properties](https://www.jenkins.io/doc/pipeline/steps/global-yaml-properties/)
    *   [`getGlobalYAMLCategories`: Get all categories defined in Global YAML Properties](https://www.jenkins.io/doc/pipeline/steps/global-yaml-properties/#getglobalyamlcategories-get-all-categories-defined-in-global-yaml-properties)
    *   [`getGlobalYAMLConfigNames`: Get list of all defined config names](https://www.jenkins.io/doc/pipeline/steps/global-yaml-properties/#getglobalyamlconfignames-get-list-of-all-defined-config-names)
    *   [`getGlobalYAMLConfigNamesByCategory`: Get list of configs by category](https://www.jenkins.io/doc/pipeline/steps/global-yaml-properties/#getglobalyamlconfignamesbycategory-get-list-of-configs-by-category)
    *   [`getGlobalYAMLProperties`: Get Global YAML Properties in HashMap format](https://www.jenkins.io/doc/pipeline/steps/global-yaml-properties/#getglobalyamlproperties-get-global-yaml-properties-in-hashmap-format)
    *   [`getLocalYAMLProperties`: Get Local YAML Properties in HashMap format](https://www.jenkins.io/doc/pipeline/steps/global-yaml-properties/#getlocalyamlproperties-get-local-yaml-properties-in-hashmap-format)

*   [Google Analyze Code Security](https://www.jenkins.io/doc/pipeline/steps/google-analyze-code-security/)
    *   [`step([$class: 'CodeScanBuildStep'])`: Perform Code Scan During Build](https://www.jenkins.io/doc/pipeline/steps/google-analyze-code-security/#stepclass-codescanbuildstep-perform-code-scan-during-build)

*   [Google Chat Notification](https://www.jenkins.io/doc/pipeline/steps/google-chat-notification/)
    *   [`googlechatnotification`: Google Chat Notification](https://www.jenkins.io/doc/pipeline/steps/google-chat-notification/#googlechatnotification-google-chat-notification)

*   [Google Cloud Build Plugin](https://www.jenkins.io/doc/pipeline/steps/google-cloudbuild/)
    *   [`googleCloudBuild`: Execute Google Cloud Build](https://www.jenkins.io/doc/pipeline/steps/google-cloudbuild/#googlecloudbuild-execute-google-cloud-build)

*   [Google Cloud Storage plugin](https://www.jenkins.io/doc/pipeline/steps/google-storage-plugin/)
    *   [`googleStorageUpload`: Google Storage Classic Upload](https://www.jenkins.io/doc/pipeline/steps/google-storage-plugin/#googlestorageupload-google-storage-classic-upload)
    *   [`googleStorageDownload`: Google Storage Download](https://www.jenkins.io/doc/pipeline/steps/google-storage-plugin/#googlestoragedownload-google-storage-download)
    *   [`googleStorageBucketLifecycle`: Google Storage Bucket Lifecycle](https://www.jenkins.io/doc/pipeline/steps/google-storage-plugin/#googlestoragebucketlifecycle-google-storage-bucket-lifecycle)
    *   [`googleStorageBuildLogUpload`: Google Storage Build Log Upload](https://www.jenkins.io/doc/pipeline/steps/google-storage-plugin/#googlestoragebuildlogupload-google-storage-build-log-upload)

*   [Google Kubernetes Engine Plugin](https://www.jenkins.io/doc/pipeline/steps/google-kubernetes-engine/)
    *   [`kubernetesEngineDeploy`: Deploy to Google Kubernetes Engine](https://www.jenkins.io/doc/pipeline/steps/google-kubernetes-engine/#kubernetesenginedeploy-deploy-to-google-kubernetes-engine)

*   [Google Play Android Publisher Plugin](https://www.jenkins.io/doc/pipeline/steps/google-play-android-publisher/)
    *   [`androidApkUpload`: Upload Android AAB/APKs to Google Play](https://www.jenkins.io/doc/pipeline/steps/google-play-android-publisher/#androidapkupload-upload-android-aabapks-to-google-play)
    *   [`androidApkMove`: Move Android apps to a different release track](https://www.jenkins.io/doc/pipeline/steps/google-play-android-publisher/#androidapkmove-move-android-apps-to-a-different-release-track)

*   [GParams](https://www.jenkins.io/doc/pipeline/steps/global-pipeline-parameters/)
    *   [`gpRead`: Read global parameter](https://www.jenkins.io/doc/pipeline/steps/global-pipeline-parameters/#gpread-read-global-parameter)
    *   [`gpWrite`: Write global parameter](https://www.jenkins.io/doc/pipeline/steps/global-pipeline-parameters/#gpwrite-write-global-parameter)

*   [GPRbuild Plugin](https://www.jenkins.io/doc/pipeline/steps/gprbuild/)
    *   [`gprbuild`: Execute GPRbuild build tool](https://www.jenkins.io/doc/pipeline/steps/gprbuild/#gprbuild-execute-gprbuild-build-tool)

*   [Gradle Plugin](https://www.jenkins.io/doc/pipeline/steps/gradle/)
    *   [`findBuildScans`: Find published build scans](https://www.jenkins.io/doc/pipeline/steps/gradle/#findbuildscans-find-published-build-scans)
    *   [`withGradle`: WithGradle](https://www.jenkins.io/doc/pipeline/steps/gradle/#withgradle-withgradle)
    *   [`wrap([$class: 'BuildScanBuildWrapper'])`: Inspect build log for published build scans](https://www.jenkins.io/doc/pipeline/steps/gradle/#wrapclass-buildscanbuildwrapper-inspect-build-log-for-published-build-scans)

*   [Groovy](https://www.jenkins.io/doc/pipeline/steps/groovy/)
    *   [`withGroovy`: Execute Groovy script](https://www.jenkins.io/doc/pipeline/steps/groovy/#withgroovy-execute-groovy-script)

*   [GrypeScanner Plugin](https://www.jenkins.io/doc/pipeline/steps/grypescanner/)
    *   [`grypeScan`: Vulnerability scan with grype](https://www.jenkins.io/doc/pipeline/steps/grypescanner/#grypescan-vulnerability-scan-with-grype)

*   [Habitat Executor](https://www.jenkins.io/doc/pipeline/steps/habitat/)
    *   [`habitat`: Habitat Executor](https://www.jenkins.io/doc/pipeline/steps/habitat/#habitat-habitat-executor)

*   [Harbor Plugin](https://www.jenkins.io/doc/pipeline/steps/harbor/)
    *   [`waitForHarborWebHook`: WaitForHarborWebhookStep](https://www.jenkins.io/doc/pipeline/steps/harbor/#waitforharborwebhook-waitforharborwebhookstep)

*   [Hashicorp Vault Pipeline Plugin](https://www.jenkins.io/doc/pipeline/steps/hashicorp-vault-pipeline/)
    *   [`vault`: VaultReadStep](https://www.jenkins.io/doc/pipeline/steps/hashicorp-vault-pipeline/#vault-vaultreadstep)

*   [HashiCorp Vault Plugin](https://www.jenkins.io/doc/pipeline/steps/hashicorp-vault-plugin/)
    *   [`withVault`: Vault Plugin](https://www.jenkins.io/doc/pipeline/steps/hashicorp-vault-plugin/#withvault-vault-plugin)
    *   [`wrap([$class: 'VaultBuildWrapper'])`: Vault Plugin](https://www.jenkins.io/doc/pipeline/steps/hashicorp-vault-plugin/#wrapclass-vaultbuildwrapper-vault-plugin)

*   [HCL AppScan](https://www.jenkins.io/doc/pipeline/steps/appscan/)
    *   [`appscan`: Run AppScan on Cloud/AppScan 360° Security Test](https://www.jenkins.io/doc/pipeline/steps/appscan/#appscan-run-appscan-on-cloudappscan-360-security-test)
    *   [`appscanenterprise`: Run AppScan Enterprise Security Test](https://www.jenkins.io/doc/pipeline/steps/appscan/#appscanenterprise-run-appscan-enterprise-security-test)

*   [Helix ALM Test Management](https://www.jenkins.io/doc/pipeline/steps/helix-alm-test-management/)
    *   [`halm_report`: Helix ALM Test Results Reporter](https://www.jenkins.io/doc/pipeline/steps/helix-alm-test-management/#halm-report-helix-alm-test-results-reporter)
    *   [`step([$class: 'HALMTestReporter'])`: Helix ALM Test Results Reporting](https://www.jenkins.io/doc/pipeline/steps/helix-alm-test-management/#stepclass-halmtestreporter-helix-alm-test-results-reporting)

*   [HiddenLayer Model Scanner Plugin](https://www.jenkins.io/doc/pipeline/steps/hiddenlayer-model-scanner/)
    *   [`hlScanModel`: Scan ML Model with HiddenLayer](https://www.jenkins.io/doc/pipeline/steps/hiddenlayer-model-scanner/#hlscanmodel-scan-ml-model-with-hiddenlayer)

*   [HipChat Plugin](https://www.jenkins.io/doc/pipeline/steps/hipchat/)
    *   [`hipchatSend`: Send HipChat Message](https://www.jenkins.io/doc/pipeline/steps/hipchat/#hipchatsend-send-hipchat-message)

*   [Horreum Plugin](https://www.jenkins.io/doc/pipeline/steps/horreum/)
    *   [`horreumExpect`: Notify Horreum that a run will be uploaded.](https://www.jenkins.io/doc/pipeline/steps/horreum/#horreumexpect-notify-horreum-that-a-run-will-be-uploaded)
    *   [`horreumUpload`: Upload a JSON object to a Horreum instance](https://www.jenkins.io/doc/pipeline/steps/horreum/#horreumupload-upload-a-json-object-to-a-horreum-instance)

*   [HP ALM Quality Center Plugin](https://www.jenkins.io/doc/pipeline/steps/hp-quality-center/)
    *   [`qc`: HP Quality Center Integration](https://www.jenkins.io/doc/pipeline/steps/hp-quality-center/#qc-hp-quality-center-integration)

*   [HTML Publisher plugin](https://www.jenkins.io/doc/pipeline/steps/htmlpublisher/)
    *   [`publishHTML`: Publish HTML reports](https://www.jenkins.io/doc/pipeline/steps/htmlpublisher/#publishhtml-publish-html-reports)

*   [HTTP Request Plugin](https://www.jenkins.io/doc/pipeline/steps/http_request/)
    *   [`httpRequest`: Perform an HTTP Request and return a response object](https://www.jenkins.io/doc/pipeline/steps/http_request/#httprequest-perform-an-http-request-and-return-a-response-object)

*   [Hubot Pipeline Steps](https://www.jenkins.io/doc/pipeline/steps/hubot-steps/)
    *   [`hubotApprove`: Hubot: Send approval message](https://www.jenkins.io/doc/pipeline/steps/hubot-steps/#hubotapprove-hubot-send-approval-message)
    *   [`hubotSend`: Hubot: Send message](https://www.jenkins.io/doc/pipeline/steps/hubot-steps/#hubotsend-hubot-send-message)

*   [Hugo Plugin](https://www.jenkins.io/doc/pipeline/steps/hugo/)
    *   [`hugo`: Hugo Builder](https://www.jenkins.io/doc/pipeline/steps/hugo/#hugo-hugo-builder)
    *   [`hugoGitPublish`: Hugo Git Publisher](https://www.jenkins.io/doc/pipeline/steps/hugo/#hugogitpublish-hugo-git-publisher)
    *   [`hugoGitSubmodulePublsh`: Hugo Git Submodule Publisher](https://www.jenkins.io/doc/pipeline/steps/hugo/#hugogitsubmodulepublsh-hugo-git-submodule-publisher)

*   [Hyper.sh Build Step Plugin](https://www.jenkins.io/doc/pipeline/steps/hyper-build-step/)
    *   [`step([$class: 'HyperBuilder'])`: Execute shell in Hyper.sh](https://www.jenkins.io/doc/pipeline/steps/hyper-build-step/#stepclass-hyperbuilder-execute-shell-in-hyper-sh)

*   [IBM Cloud DevOps](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/)
    *   [`evaluateGate`: IBM Cloud DevOps Gate](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#evaluategate-ibm-cloud-devops-gate)
    *   [`notifyOTC`: Send notification to OTC](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#notifyotc-send-notification-to-otc)
    *   [`publishBuildRecord`: Publish build record to IBM Cloud DevOps](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#publishbuildrecord-publish-build-record-to-ibm-cloud-devops)
    *   [`publishDeployRecord`: Publish deploy record to IBM Cloud DevOps](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#publishdeployrecord-publish-deploy-record-to-ibm-cloud-devops)
    *   [`publishSQResults`: Publish SonarQube test results to IBM Cloud DevOps](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#publishsqresults-publish-sonarqube-test-results-to-ibm-cloud-devops)
    *   [`publishTestResult`: Publish test result to IBM Cloud DevOps](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#publishtestresult-publish-test-result-to-ibm-cloud-devops)
    *   [`sendDeployableMessage`: Send deployable mapping message to OTC](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#senddeployablemessage-send-deployable-mapping-message-to-otc)
    *   [`step([$class: 'EvaluateGate'])`: IBM Cloud DevOps Gate](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#stepclass-evaluategate-ibm-cloud-devops-gate)
    *   [`step([$class: 'PublishBuild'])`: Publish build information to IBM Cloud DevOps](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#stepclass-publishbuild-publish-build-information-to-ibm-cloud-devops)
    *   [`step([$class: 'PublishDeploy'])`: Publish deployment information to IBM Cloud DevOps](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#stepclass-publishdeploy-publish-deployment-information-to-ibm-cloud-devops)
    *   [`step([$class: 'PublishSQ'])`: Publish SonarQube test result to IBM Cloud DevOps](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#stepclass-publishsq-publish-sonarqube-test-result-to-ibm-cloud-devops)
    *   [`step([$class: 'PublishTest'])`: Publish test result to IBM Cloud DevOps](https://www.jenkins.io/doc/pipeline/steps/ibm-cloud-devops/#stepclass-publishtest-publish-test-result-to-ibm-cloud-devops)

*   [IBM Continuous Release](https://www.jenkins.io/doc/pipeline/steps/ibm-continuous-release/)
    *   [`step([$class: 'ContinuousReleaseProperties'])`: Pass Properties to Continuous Release Version](https://www.jenkins.io/doc/pipeline/steps/ibm-continuous-release/#stepclass-continuousreleaseproperties-pass-properties-to-continuous-release-version)

*   [IBM i Pipeline Steps](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/)
    *   [`ibmiCommand`: Run an IBM i command](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/#ibmicommand-run-an-ibm-i-command)
    *   [`ibmiGetIFS`: Download a remote IFS file or folder into local workspace folder](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/#ibmigetifs-download-a-remote-ifs-file-or-folder-into-local-workspace-folder)
    *   [`ibmiGetSAVF`: Download a Save File into the workspace](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/#ibmigetsavf-download-a-save-file-into-the-workspace)
    *   [`ibmiGetSPLF`: Download spooled files of a given job to a local workspace folder](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/#ibmigetsplf-download-spooled-files-of-a-given-job-to-a-local-workspace-folder)
    *   [`ibmiPutIFS`: Upload a local workspace file or folder into a remote IFS folder](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/#ibmiputifs-upload-a-local-workspace-file-or-folder-into-a-remote-ifs-folder)
    *   [`ibmiPutSAVF`: Upload a stream file restore its Save File object](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/#ibmiputsavf-upload-a-stream-file-restore-its-save-file-object)
    *   [`ibmiRunSQL`: Run an SQL query on Db2 for i](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/#ibmirunsql-run-an-sql-query-on-db2-for-i)
    *   [`ibmiShellExec`: Run a shell command](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/#ibmishellexec-run-a-shell-command)
    *   [`ibmiWaitJob`: Wait for an IBM i to end](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/#ibmiwaitjob-wait-for-an-ibm-i-to-end)
    *   [`onIBMi`: Provides an IBM i execution environment to run IBM i steps](https://www.jenkins.io/doc/pipeline/steps/ibmi-steps/#onibmi-provides-an-ibm-i-execution-environment-to-run-ibm-i-steps)

*   [IBM Security AppScan Source Scanner](https://www.jenkins.io/doc/pipeline/steps/ibm-security-appscansource-scanner/)
    *   [`step([$class: 'AppScanSourceBuilder'])`: Run AppScan Source](https://www.jenkins.io/doc/pipeline/steps/ibm-security-appscansource-scanner/#stepclass-appscansourcebuilder-run-appscan-source)

*   [IBM Security AppScan Standard Scanner](https://www.jenkins.io/doc/pipeline/steps/ibm-security-appscanstandard-scanner/)
    *   [`step([$class: 'AppScanStandardBuilder'])`: Run AppScan Standard](https://www.jenkins.io/doc/pipeline/steps/ibm-security-appscanstandard-scanner/#stepclass-appscanstandardbuilder-run-appscan-standard)

*   [IBM z/OS Connector](https://www.jenkins.io/doc/pipeline/steps/zos-connector/)
    *   [`step([$class: 'ZOSJobSubmitter'])`: Submit z/OS job](https://www.jenkins.io/doc/pipeline/steps/zos-connector/#stepclass-zosjobsubmitter-submit-zos-job)

*   [ICQ and MyTeam Notification Plugin](https://www.jenkins.io/doc/pipeline/steps/icq-notification/)
    *   [`step([$class: 'SendMessageBuildStep'])`: Send message to ICQ or MyTeam](https://www.jenkins.io/doc/pipeline/steps/icq-notification/#stepclass-sendmessagebuildstep-send-message-to-icq-or-myteam)
    *   [`icqMessage`: Send message to ICQ or MyTeam](https://www.jenkins.io/doc/pipeline/steps/icq-notification/#icqmessage-send-message-to-icq-or-myteam)

*   [ImmuniWeb Neuron](https://www.jenkins.io/doc/pipeline/steps/immuniweb/)
    *   [`step([$class: 'ScannerBuilder'])`: Run ImmuniWeb Neuron scan](https://www.jenkins.io/doc/pipeline/steps/immuniweb/#stepclass-scannerbuilder-run-immuniweb-neuron-scan)

*   [in-toto provenance agent](https://www.jenkins.io/doc/pipeline/steps/in-toto/)
    *   [`in_toto_wrap`: in-toto record wrapper](https://www.jenkins.io/doc/pipeline/steps/in-toto/#in-toto-wrap-in-toto-record-wrapper)

*   [Indusface-WAS-Plugin](https://www.jenkins.io/doc/pipeline/steps/indusface-was/)
    *   [`indusfaceWasScan`: Indusface Was Scan](https://www.jenkins.io/doc/pipeline/steps/indusface-was/#indusfacewasscan-indusface-was-scan)

*   [Inedo BuildMaster Plugin.](https://www.jenkins.io/doc/pipeline/steps/inedo-buildmaster/)
    *   [`buildMasterCreateBuild`: Create BuildMaster Build](https://www.jenkins.io/doc/pipeline/steps/inedo-buildmaster/#buildmastercreatebuild-create-buildmaster-build)
    *   [`step([$class: 'CreateBuildBuilder'])`: Create BuildMaster Build](https://www.jenkins.io/doc/pipeline/steps/inedo-buildmaster/#stepclass-createbuildbuilder-create-buildmaster-build)
    *   [`buildMasterDeployBuildToStage`: Deploy BuildMaster Build To Stage](https://www.jenkins.io/doc/pipeline/steps/inedo-buildmaster/#buildmasterdeploybuildtostage-deploy-buildmaster-build-to-stage)
    *   [`buildMasterWithApplicationRelease`: Inject BuildMaster release details as environment variables](https://www.jenkins.io/doc/pipeline/steps/inedo-buildmaster/#buildmasterwithapplicationrelease-inject-buildmaster-release-details-as-environment-variables)

*   [Inedo ProGet Plugin.](https://www.jenkins.io/doc/pipeline/steps/inedo-proget/)
    *   [`downloadProgetPackage`: ProGet Package Download](https://www.jenkins.io/doc/pipeline/steps/inedo-proget/#downloadprogetpackage-proget-package-download)
    *   [`uploadProgetPackage`: ProGet Package Upload](https://www.jenkins.io/doc/pipeline/steps/inedo-proget/#uploadprogetpackage-proget-package-upload)

*   [Infisical Plugin](https://www.jenkins.io/doc/pipeline/steps/infisical/)
    *   [`withInfisical`: Infisical Plugin](https://www.jenkins.io/doc/pipeline/steps/infisical/#withinfisical-infisical-plugin)

*   [InfluxDB Plugin](https://www.jenkins.io/doc/pipeline/steps/influxdb/)
    *   [`influxDbPublisher`: Publish build data to InfluxDB](https://www.jenkins.io/doc/pipeline/steps/influxdb/#influxdbpublisher-publish-build-data-to-influxdb)
    *   [`step([$class: 'InfluxDbPublisher'])`: Publish build data to InfluxDB](https://www.jenkins.io/doc/pipeline/steps/influxdb/#stepclass-influxdbpublisher-publish-build-data-to-influxdb)

*   [InfluxDB Query Plugin](https://www.jenkins.io/doc/pipeline/steps/influxdb-query/)
    *   [`influxDbQuery`: Query InfluxDB](https://www.jenkins.io/doc/pipeline/steps/influxdb-query/#influxdbquery-query-influxdb)

*   [InsightVM Container Image Scanner](https://www.jenkins.io/doc/pipeline/steps/rapid7-insightvm-container-assessment/)
    *   [`assessContainerImage`: Assess Container Image with Rapid7 InsightVM](https://www.jenkins.io/doc/pipeline/steps/rapid7-insightvm-container-assessment/#assesscontainerimage-assess-container-image-with-rapid7-insightvm)

*   [Instana integration](https://www.jenkins.io/doc/pipeline/steps/instana/)
    *   [`releaseMarker`: Perform an HTTP Request and return a response object](https://www.jenkins.io/doc/pipeline/steps/instana/#releasemarker-perform-an-http-request-and-return-a-response-object)

*   [IRC Plugin](https://www.jenkins.io/doc/pipeline/steps/ircbot/)
    *   [`ircNotify`: IRC Notification](https://www.jenkins.io/doc/pipeline/steps/ircbot/#ircnotify-irc-notification)

*   [IronMQ-notifier](https://www.jenkins.io/doc/pipeline/steps/ironmq-notifier/)
    *   [`step([$class: 'IronMQNotifier'])`: Send Message to IronMQ Service](https://www.jenkins.io/doc/pipeline/steps/ironmq-notifier/#stepclass-ironmqnotifier-send-message-to-ironmq-service)

*   [Jabber (XMPP) notifier and control plugin](https://www.jenkins.io/doc/pipeline/steps/jabber/)
    *   [`jabberNotify`: Jabber Notification](https://www.jenkins.io/doc/pipeline/steps/jabber/#jabbernotify-jabber-notification)

*   [Jacked](https://www.jenkins.io/doc/pipeline/steps/jacked/)
    *   [`jacked`: Jacked Vulnerability Analyzer](https://www.jenkins.io/doc/pipeline/steps/jacked/#jacked-jacked-vulnerability-analyzer)

*   [JaCoCo plugin](https://www.jenkins.io/doc/pipeline/steps/jacoco/)
    *   [`jacoco`: Record JaCoCo coverage report](https://www.jenkins.io/doc/pipeline/steps/jacoco/#jacoco-record-jacoco-coverage-report)

*   [Javadoc Plugin](https://www.jenkins.io/doc/pipeline/steps/javadoc/)
    *   [`javadoc`: Publish Javadoc](https://www.jenkins.io/doc/pipeline/steps/javadoc/#javadoc-publish-javadoc)

*   [JClouds plugin](https://www.jenkins.io/doc/pipeline/steps/jclouds-jenkins/)
    *   [`jcloudsTakeOffline`: Take current JClouds agent offline conditionally](https://www.jenkins.io/doc/pipeline/steps/jclouds-jenkins/#jcloudstakeoffline-take-current-jclouds-agent-offline-conditionally)
    *   [`withJclouds`: Create supplemental nodes](https://www.jenkins.io/doc/pipeline/steps/jclouds-jenkins/#withjclouds-create-supplemental-nodes)
    *   [`jcloudsOneOffAgent`: JClouds Single-use agent](https://www.jenkins.io/doc/pipeline/steps/jclouds-jenkins/#jcloudsoneoffagent-jclouds-single-use-agent)

*   [JDCloud CodeDeploy Plugin](https://www.jenkins.io/doc/pipeline/steps/jdcloud-codedeploy/)
    *   [`step([$class: 'JDCodeDeployPublisher'])`: Deploy to JDCloud CodeDeploy](https://www.jenkins.io/doc/pipeline/steps/jdcloud-codedeploy/#stepclass-jdcodedeploypublisher-deploy-to-jdcloud-codedeploy)

*   [Jenkins Core](https://www.jenkins.io/doc/pipeline/steps/core/)
    *   [`archiveArtifacts`: Archive the artifacts](https://www.jenkins.io/doc/pipeline/steps/core/#archiveartifacts-archive-the-artifacts)
    *   [`fingerprint`: Record fingerprints of files to track usage](https://www.jenkins.io/doc/pipeline/steps/core/#fingerprint-record-fingerprints-of-files-to-track-usage)

*   [JetBrains SpaceCode Plugin](https://www.jenkins.io/doc/pipeline/steps/jetbrains-space/)
    *   [`callSpaceApi`: Make a call to JetBrains SpaceCode HTTP API](https://www.jenkins.io/doc/pipeline/steps/jetbrains-space/#callspaceapi-make-a-call-to-jetbrains-spacecode-http-api)
    *   [`postBuildStatusToSpace`: Post build status to JetBrains SpaceCode](https://www.jenkins.io/doc/pipeline/steps/jetbrains-space/#postbuildstatustospace-post-build-status-to-jetbrains-spacecode)
    *   [`postReviewTimelineMessageToSpace`: Post message to the review timeline in JetBrains SpaceCode](https://www.jenkins.io/doc/pipeline/steps/jetbrains-space/#postreviewtimelinemessagetospace-post-message-to-the-review-timeline-in-jetbrains-spacecode)

*   [JFrog Plugin](https://www.jenkins.io/doc/pipeline/steps/jfrog/)
    *   [`jf`: jf command](https://www.jenkins.io/doc/pipeline/steps/jfrog/#jf-jf-command)

*   [JGiven Jenkins Plugin](https://www.jenkins.io/doc/pipeline/steps/jgiven/)
    *   [`step([$class: 'JgivenReportGenerator'])`: Generate JGiven Reports](https://www.jenkins.io/doc/pipeline/steps/jgiven/#stepclass-jgivenreportgenerator-generate-jgiven-reports)

*   [Jira Integration](https://www.jenkins.io/doc/pipeline/steps/jira-integration/)
    *   [`step([$class: 'DeploymentBuildMarker'])`: Deployment Build Marker](https://www.jenkins.io/doc/pipeline/steps/jira-integration/#stepclass-deploymentbuildmarker-deployment-build-marker)

*   [JIRA Pipeline Steps](https://www.jenkins.io/doc/pipeline/steps/jira-steps/)
    *   [`jiraAddComment`: JIRA Steps: Add Comment](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiraaddcomment-jira-steps-add-comment)
    *   [`jiraAddWatcher`: JIRA Steps: Add Watcher](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiraaddwatcher-jira-steps-add-watcher)
    *   [`jiraAssignIssue`: JIRA Steps: Assign Issue](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiraassignissue-jira-steps-assign-issue)
    *   [`jiraAssignableUserSearch`: JIRA Steps: Searches assignable JIRA Users by username, name or email address for the given project/issueKey](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiraassignableusersearch-jira-steps-searches-assignable-jira-users-by-username-name-or-email-address-for-the-given-projectissuekey)
    *   [`jiraDeleteAttachment`: JIRA Steps: Delete Attachment](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiradeleteattachment-jira-steps-delete-attachment)
    *   [`jiraDeleteIssueLink`: JIRA Steps: Delete IssueLink](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiradeleteissuelink-jira-steps-delete-issuelink)
    *   [`jiraDeleteIssueRemoteLink`: JIRA Steps: Delete Issue’s Remote Link by linkId.](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiradeleteissueremotelink-jira-steps-delete-issues-remote-link-by-linkid)
    *   [`jiraDeleteIssueRemoteLinks`: JIRA Steps: Delete Issue’s Remote Links by globalId.](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiradeleteissueremotelinks-jira-steps-delete-issues-remote-links-by-globalid)
    *   [`jiraDownloadAttachment`: JIRA Steps: Download a file to workspace (directory is optional)](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiradownloadattachment-jira-steps-download-a-file-to-workspace-directory-is-optional)
    *   [`jiraEditComment`: JIRA Steps: Edit Issue Comment](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiraeditcomment-jira-steps-edit-issue-comment)
    *   [`jiraEditComponent`: JIRA Steps: Edit Component](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiraeditcomponent-jira-steps-edit-component)
    *   [`jiraEditIssue`: JIRA Steps: Edit Issue](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiraeditissue-jira-steps-edit-issue)
    *   [`jiraEditVersion`: JIRA Steps: Edit Version](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiraeditversion-jira-steps-edit-version)
    *   [`jiraGetAttachmentInfo`: JIRA Steps: Get Attachment Info](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetattachmentinfo-jira-steps-get-attachment-info)
    *   [`jiraGetComment`: JIRA Steps: Get Issue Comment](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetcomment-jira-steps-get-issue-comment)
    *   [`jiraGetComments`: JIRA Steps: Get Issue Comments](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetcomments-jira-steps-get-issue-comments)
    *   [`jiraGetComponent`: JIRA Steps: Get Component](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetcomponent-jira-steps-get-component)
    *   [`jiraGetComponentIssueCount`: JIRA Steps: Get Component Issue Count](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetcomponentissuecount-jira-steps-get-component-issue-count)
    *   [`jiraGetFields`: JIRA Steps: Get Fields](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetfields-jira-steps-get-fields)
    *   [`jiraGetIssue`: JIRA Steps: Get Issue](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetissue-jira-steps-get-issue)
    *   [`jiraGetIssueLink`: JIRA Steps: Get IssueLink](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetissuelink-jira-steps-get-issuelink)
    *   [`jiraGetIssueLinkTypes`: JIRA Steps: Get Issue Link Types](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetissuelinktypes-jira-steps-get-issue-link-types)
    *   [`jiraGetIssueRemoteLink`: JIRA Steps: Get Issue’s Remote Link by linkId.](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetissueremotelink-jira-steps-get-issues-remote-link-by-linkid)
    *   [`jiraGetIssueRemoteLinks`: JIRA Steps: Get Issue’s Remote Links by globalId.](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetissueremotelinks-jira-steps-get-issues-remote-links-by-globalid)
    *   [`jiraGetIssueTransitions`: JIRA Steps: Get Issue Transitions](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetissuetransitions-jira-steps-get-issue-transitions)
    *   [`jiraGetIssueWatches`: JIRA Steps: Get Issue Watches](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetissuewatches-jira-steps-get-issue-watches)
    *   [`jiraGetProject`: JIRA Steps: Get Project](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetproject-jira-steps-get-project)
    *   [`jiraGetProjectComponents`: JIRA Steps: Get Project Components](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetprojectcomponents-jira-steps-get-project-components)
    *   [`jiraGetProjectStatuses`: JIRA Steps: Get Project Statuses](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetprojectstatuses-jira-steps-get-project-statuses)
    *   [`jiraGetProjectVersions`: JIRA Steps: Get Project Versions](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetprojectversions-jira-steps-get-project-versions)
    *   [`jiraGetProjects`: JIRA Steps: Get Projects](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetprojects-jira-steps-get-projects)
    *   [`jiraGetServerInfo`: JIRA Steps: Get Server Info](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetserverinfo-jira-steps-get-server-info)
    *   [`jiraGetVersion`: JIRA Steps: Get Version](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiragetversion-jira-steps-get-version)
    *   [`jiraJqlSearch`: JIRA Steps: JQL Search](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jirajqlsearch-jira-steps-jql-search)
    *   [`jiraLinkIssues`: JIRA Steps: Link Issues](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiralinkissues-jira-steps-link-issues)
    *   [`jiraNewComponent`: JIRA Steps: Create New Component](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiranewcomponent-jira-steps-create-new-component)
    *   [`jiraNewIssue`: JIRA Steps: Create New Issue](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiranewissue-jira-steps-create-new-issue)
    *   [`jiraNewIssueRemoteLink`: JIRA Steps: Create new remote link for given issue.](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiranewissueremotelink-jira-steps-create-new-remote-link-for-given-issue)
    *   [`jiraNewIssues`: JIRA Steps: Create New Issues](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiranewissues-jira-steps-create-new-issues)
    *   [`jiraNewVersion`: JIRA Steps: Create New Version](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiranewversion-jira-steps-create-new-version)
    *   [`jiraNotifyIssue`: JIRA Steps: Notify Issue](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiranotifyissue-jira-steps-notify-issue)
    *   [`jiraTransitionIssue`: JIRA Steps: Transition Issue](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jiratransitionissue-jira-steps-transition-issue)
    *   [`jiraUploadAttachment`: JIRA Steps: Attach a file from workspace to an issue](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jirauploadattachment-jira-steps-attach-a-file-from-workspace-to-an-issue)
    *   [`jiraUserSearch`: JIRA Steps: Search Active JIRA Users by username, name or email address.](https://www.jenkins.io/doc/pipeline/steps/jira-steps/#jirausersearch-jira-steps-search-active-jira-users-by-username-name-or-email-address)

*   [Jira plugin](https://www.jenkins.io/doc/pipeline/steps/jira/)
    *   [`jiraComment`: Jira: Add a comment to issue(s)](https://www.jenkins.io/doc/pipeline/steps/jira/#jiracomment-jira-add-a-comment-to-issues)
    *   [`jiraIssueSelector`: Jira: Issue selector](https://www.jenkins.io/doc/pipeline/steps/jira/#jiraissueselector-jira-issue-selector)
    *   [`jiraSearch`: Jira: Search issues](https://www.jenkins.io/doc/pipeline/steps/jira/#jirasearch-jira-search-issues)
    *   [`jiraUpdateIssueField`: Jira: Issue custom field updater](https://www.jenkins.io/doc/pipeline/steps/jira/#jiraupdateissuefield-jira-issue-custom-field-updater)
    *   [`jiraExecuteWorkflow`: Jira: Progress issues by workflow action](https://www.jenkins.io/doc/pipeline/steps/jira/#jiraexecuteworkflow-jira-progress-issues-by-workflow-action)
    *   [`jiraCommentIssues`: Jira: Update relevant issues](https://www.jenkins.io/doc/pipeline/steps/jira/#jiracommentissues-jira-update-relevant-issues)
    *   [`jiraMarkVersionReleased`: Jira: Mark a version as Released](https://www.jenkins.io/doc/pipeline/steps/jira/#jiramarkversionreleased-jira-mark-a-version-as-released)
    *   [`jiraCreateVersion`: Jira: Create new version](https://www.jenkins.io/doc/pipeline/steps/jira/#jiracreateversion-jira-create-new-version)
    *   [`jiraCreateReleaseNotes`: Generate Release Notes](https://www.jenkins.io/doc/pipeline/steps/jira/#jiracreatereleasenotes-generate-release-notes)

*   [Jira Service Management Integration Plugin](https://www.jenkins.io/doc/pipeline/steps/jsm-alert/)
    *   [`JSM`: Jira Service Management step](https://www.jenkins.io/doc/pipeline/steps/jsm-alert/#jsm-jira-service-management-step)

*   [JMH Report](https://www.jenkins.io/doc/pipeline/steps/jmh-report/)
    *   [`jmhReport`: JMH Report](https://www.jenkins.io/doc/pipeline/steps/jmh-report/#jmhreport-jmh-report)

*   [JMS Messaging Plugin](https://www.jenkins.io/doc/pipeline/steps/jms-messaging/)
    *   [`sendCIMessage`: CI Notifier](https://www.jenkins.io/doc/pipeline/steps/jms-messaging/#sendcimessage-ci-notifier)
    *   [`waitForCIMessage`: CI Subscriber](https://www.jenkins.io/doc/pipeline/steps/jms-messaging/#waitforcimessage-ci-subscriber)

*   [Job Cacher plugin](https://www.jenkins.io/doc/pipeline/steps/jobcacher/)
    *   [`cache`: Caches files from previous build to current build](https://www.jenkins.io/doc/pipeline/steps/jobcacher/#cache-caches-files-from-previous-build-to-current-build)
    *   [`jobcacher`: Job Cacher](https://www.jenkins.io/doc/pipeline/steps/jobcacher/#jobcacher-job-cacher)

*   [Job DSL](https://www.jenkins.io/doc/pipeline/steps/job-dsl/)
    *   [`jobDsl`: Process Job DSLs](https://www.jenkins.io/doc/pipeline/steps/job-dsl/#jobdsl-process-job-dsls)

*   [Job Environment Variables Status Sync](https://www.jenkins.io/doc/pipeline/steps/environment-variables-status-sync/)
    *   [`notify`: Task environment variables and message notifications](https://www.jenkins.io/doc/pipeline/steps/environment-variables-status-sync/#notify-task-environment-variables-and-message-notifications)

*   [JUnit Plugin](https://www.jenkins.io/doc/pipeline/steps/junit/)
    *   [`junit`: Archive JUnit-formatted test results](https://www.jenkins.io/doc/pipeline/steps/junit/#junit-archive-junit-formatted-test-results)
    *   [`step([$class: 'JUnitResultArchiver'])`: Publish JUnit test result report](https://www.jenkins.io/doc/pipeline/steps/junit/#stepclass-junitresultarchiver-publish-junit-test-result-report)

*   [JUnit Realtime Test Reporter Plugin](https://www.jenkins.io/doc/pipeline/steps/junit-realtime-test-reporter/)
    *   [`realtimeJUnit`: Display JUnit test results as they appear](https://www.jenkins.io/doc/pipeline/steps/junit-realtime-test-reporter/#realtimejunit-display-junit-test-results-as-they-appear)

*   [Kafka Logs Plugin](https://www.jenkins.io/doc/pipeline/steps/kafkalogs/)
    *   [`withKafkaLog`: Kafka Log Build Wrapper](https://www.jenkins.io/doc/pipeline/steps/kafkalogs/#withkafkalog-kafka-log-build-wrapper)
    *   [`withKafkaLog`: Kafka Log Build Wrapper](https://www.jenkins.io/doc/pipeline/steps/kafkalogs/#withkafkalog-kafka-log-build-wrapper)

*   [Karaf Build Step Plugin](https://www.jenkins.io/doc/pipeline/steps/karaf-build-step/)
    *   [`step([$class: 'KarafBuildStepBuilder'])`: Execute Karaf command](https://www.jenkins.io/doc/pipeline/steps/karaf-build-step/#stepclass-karafbuildstepbuilder-execute-karaf-command)

*   [Katalon Plugin](https://www.jenkins.io/doc/pipeline/steps/katalon/)
    *   [`executeKatalon`: Execute Katalon Studio Tests](https://www.jenkins.io/doc/pipeline/steps/katalon/#executekatalon-execute-katalon-studio-tests)
    *   [`executeKatalonTestOps`: Execute Katalon TestOps Plan](https://www.jenkins.io/doc/pipeline/steps/katalon/#executekatalontestops-execute-katalon-testops-plan)

*   [Keeper Secrets Manager](https://www.jenkins.io/doc/pipeline/steps/keeper-secrets-manager/)
    *   [`withKsm`: Inject secrets with Keeper Secrets Manager](https://www.jenkins.io/doc/pipeline/steps/keeper-secrets-manager/#withksm-inject-secrets-with-keeper-secrets-manager)

*   [Kiuwan plugin](https://www.jenkins.io/doc/pipeline/steps/kiuwanJenkinsPlugin/)
    *   [`kiuwan`: Analyze your source code with Kiuwan!](https://www.jenkins.io/doc/pipeline/steps/kiuwanJenkinsPlugin/#kiuwan-analyze-your-source-code-with-kiuwan)

*   [Klocwork Analysis Plug-in](https://www.jenkins.io/doc/pipeline/steps/klocwork/)
    *   [`klocworkBuildSpecGeneration`: Klocwork - Step 1 (CI/Full) - Capture Build Information](https://www.jenkins.io/doc/pipeline/steps/klocwork/#klocworkbuildspecgeneration-klocwork-step-1-cifull-capture-build-information)
    *   [`klocworkFailureCondition`: Klocwork - Post Analysis (Full/CI) - Build Failure Conditions (Optional)](https://www.jenkins.io/doc/pipeline/steps/klocwork/#klocworkfailurecondition-klocwork-post-analysis-fullci-build-failure-conditions-optional)
    *   [`klocworkIncremental`: Klocwork - Step 2 (CI) - Run Differential Analysis](https://www.jenkins.io/doc/pipeline/steps/klocwork/#klocworkincremental-klocwork-step-2-ci-run-differential-analysis)
    *   [`klocworkIntegrationStep1`: Klocwork - Step 2 (Full) - Run Analysis](https://www.jenkins.io/doc/pipeline/steps/klocwork/#klocworkintegrationstep1-klocwork-step-2-full-run-analysis)
    *   [`klocworkIntegrationStep2`: Klocwork - Step 3 (Full) - Load Analysis Results](https://www.jenkins.io/doc/pipeline/steps/klocwork/#klocworkintegrationstep2-klocwork-step-3-full-load-analysis-results)
    *   [`klocworkIssueSync`: Klocwork - Post Analysis (Full) - Cross-Project Issue Sync (Optional)](https://www.jenkins.io/doc/pipeline/steps/klocwork/#klocworkissuesync-klocwork-post-analysis-full-cross-project-issue-sync-optional)
    *   [`step([$class: 'KlocworkBuildSpecBuilder'])`: Klocwork - Step 1 (CI/Full) - Capture Build Information](https://www.jenkins.io/doc/pipeline/steps/klocwork/#stepclass-klocworkbuildspecbuilder-klocwork-step-1-cifull-capture-build-information)
    *   [`step([$class: 'KlocworkCiBuilder'])`: Klocwork - Step 2 (CI) - Run Differential Analysis](https://www.jenkins.io/doc/pipeline/steps/klocwork/#stepclass-klocworkcibuilder-klocwork-step-2-ci-run-differential-analysis)
    *   [`step([$class: 'KlocworkFailureConditionPublisher'])`: Klocwork - Post Analysis (Full/CI) - Build Failure Conditions (Optional)](https://www.jenkins.io/doc/pipeline/steps/klocwork/#stepclass-klocworkfailureconditionpublisher-klocwork-post-analysis-fullci-build-failure-conditions-optional)
    *   [`step([$class: 'KlocworkServerAnalysisBuilder'])`: Klocwork - Step 2 (Full) - Run Analysis](https://www.jenkins.io/doc/pipeline/steps/klocwork/#stepclass-klocworkserveranalysisbuilder-klocwork-step-2-full-run-analysis)
    *   [`step([$class: 'KlocworkServerLoadBuilder'])`: Klocwork - Step 3 (Full) - Load Analysis Results](https://www.jenkins.io/doc/pipeline/steps/klocwork/#stepclass-klocworkserverloadbuilder-klocwork-step-3-full-load-analysis-results)
    *   [`step([$class: 'KlocworkXSyncBuilder'])`: Klocwork - Post Analysis (Full) - Cross-Project Issue Sync (Optional)](https://www.jenkins.io/doc/pipeline/steps/klocwork/#stepclass-klocworkxsyncbuilder-klocwork-post-analysis-full-cross-project-issue-sync-optional)
    *   [`klocworkWrapper`: Klocwork - Build Environment Settings](https://www.jenkins.io/doc/pipeline/steps/klocwork/#klocworkwrapper-klocwork-build-environment-settings)

*   [Kobiton](https://www.jenkins.io/doc/pipeline/steps/kobiton-integration/)
    *   [`appUploaderBuilder`: Upload application to Kobiton Apps Repository](https://www.jenkins.io/doc/pipeline/steps/kobiton-integration/#appuploaderbuilder-upload-application-to-kobiton-apps-repository)
    *   [`credentialsBuildWrapper`: Kobiton](https://www.jenkins.io/doc/pipeline/steps/kobiton-integration/#credentialsbuildwrapper-kobiton)

*   [Kryptowire Plugin](https://www.jenkins.io/doc/pipeline/steps/kryptowire/)
    *   [`kwSubmit`: Submit to Kryptowire](https://www.jenkins.io/doc/pipeline/steps/kryptowire/#kwsubmit-submit-to-kryptowire)

*   [Kubernetes :: Pipeline :: DevOps Steps](https://www.jenkins.io/doc/pipeline/steps/kubernetes-pipeline-devops-steps/)
    *   [`approveReceivedEvent`: Updates an Approve event in Elasticsearch](https://www.jenkins.io/doc/pipeline/steps/kubernetes-pipeline-devops-steps/#approvereceivedevent-updates-an-approve-event-in-elasticsearch)
    *   [`approveRequestedEvent`: Creates an Approve requested event in Elasticsearch](https://www.jenkins.io/doc/pipeline/steps/kubernetes-pipeline-devops-steps/#approverequestedevent-creates-an-approve-requested-event-in-elasticsearch)
    *   [`createEvent`: Creates a JSON payload event in Elasticsearch](https://www.jenkins.io/doc/pipeline/steps/kubernetes-pipeline-devops-steps/#createevent-creates-a-json-payload-event-in-elasticsearch)
    *   [`kubernetesApply`: Apply resources to Kubernetes, lazily creating environments and routes](https://www.jenkins.io/doc/pipeline/steps/kubernetes-pipeline-devops-steps/#kubernetesapply-apply-resources-to-kubernetes-lazily-creating-environments-and-routes)

*   [Kubernetes CLI Plugin](https://www.jenkins.io/doc/pipeline/steps/kubernetes-cli/)
    *   [`withKubeConfig`: Configure Kubernetes CLI (kubectl)](https://www.jenkins.io/doc/pipeline/steps/kubernetes-cli/#withkubeconfig-configure-kubernetes-cli-kubectl)
    *   [`withKubeCredentials`: Configure Kubernetes CLI (kubectl) with multiple credentials](https://www.jenkins.io/doc/pipeline/steps/kubernetes-cli/#withkubecredentials-configure-kubernetes-cli-kubectl-with-multiple-credentials)
    *   [`wrap([$class: 'MultiKubectlBuildWrapper'])`: Configure Kubernetes CLI (kubectl) with multiple credentials](https://www.jenkins.io/doc/pipeline/steps/kubernetes-cli/#wrapclass-multikubectlbuildwrapper-configure-kubernetes-cli-kubectl-with-multiple-credentials)
    *   [`wrap([$class: 'KubectlBuildWrapper'])`: Configure Kubernetes CLI (kubectl) (deprecated, use the multi credentials one instead)](https://www.jenkins.io/doc/pipeline/steps/kubernetes-cli/#wrapclass-kubectlbuildwrapper-configure-kubernetes-cli-kubectl-deprecated-use-the-multi-credentials-one-instead)

*   [Kubernetes Ephemeral Container Plugin](https://www.jenkins.io/doc/pipeline/steps/kubernetes-ephemeral-container/)
    *   [`withEphemeralContainer`: Define an Ephemeral Container to add to the current Pod](https://www.jenkins.io/doc/pipeline/steps/kubernetes-ephemeral-container/#withephemeralcontainer-define-an-ephemeral-container-to-add-to-the-current-pod)
    *   [`ephemeralContainer`: Define an Ephemeral Container to add to the current Pod](https://www.jenkins.io/doc/pipeline/steps/kubernetes-ephemeral-container/#ephemeralcontainer-define-an-ephemeral-container-to-add-to-the-current-pod)

*   [Kubernetes plugin](https://www.jenkins.io/doc/pipeline/steps/kubernetes/)
    *   [`container`: Run build steps in a container](https://www.jenkins.io/doc/pipeline/steps/kubernetes/#container-run-build-steps-in-a-container)
    *   [`podTemplate`: Define a podTemplate to use in the kubernetes plugin](https://www.jenkins.io/doc/pipeline/steps/kubernetes/#podtemplate-define-a-podtemplate-to-use-in-the-kubernetes-plugin)
    *   [`kubeconfig`: Setup Kubernetes CLI (kubectl)](https://www.jenkins.io/doc/pipeline/steps/kubernetes/#kubeconfig-setup-kubernetes-cli-kubectl)
    *   [`containerLog`: Get container log from Kubernetes](https://www.jenkins.io/doc/pipeline/steps/kubernetes/#containerlog-get-container-log-from-kubernetes)

*   [Labeled Test Groups Publisher](https://www.jenkins.io/doc/pipeline/steps/labeled-test-groups-publisher/)
    *   [`step([$class: 'LabeledTestResultGroupPublisher'])`: Publish Test Results in Labeled Groups](https://www.jenkins.io/doc/pipeline/steps/labeled-test-groups-publisher/#stepclass-labeledtestresultgrouppublisher-publish-test-results-in-labeled-groups)

*   [Labelled Pipeline Steps Plugin](https://www.jenkins.io/doc/pipeline/steps/labelled-steps/)
    *   [`labelledShell`: Shell Script](https://www.jenkins.io/doc/pipeline/steps/labelled-steps/#labelledshell-shell-script)

*   [Lacework Security Scanner](https://www.jenkins.io/doc/pipeline/steps/lacework-security-scanner/)
    *   [`lacework`: Lacework Security](https://www.jenkins.io/doc/pipeline/steps/lacework-security-scanner/#lacework-lacework-security)

*   [LambdaTest Automation Plugin](https://www.jenkins.io/doc/pipeline/steps/lambdatest-automation/)
    *   [`lambdaTestReportPublisher`: LambdaTest Pipeline Report](https://www.jenkins.io/doc/pipeline/steps/lambdatest-automation/#lambdatestreportpublisher-lambdatest-pipeline-report)
    *   [`step([$class: 'LambdaTestAppAutomationReportPublisher'])`: LambdaTest App Automation Report](https://www.jenkins.io/doc/pipeline/steps/lambdatest-automation/#stepclass-lambdatestappautomationreportpublisher-lambdatest-app-automation-report)
    *   [`step([$class: 'LambdaTestReportPublisher'])`: LambdaTest Report](https://www.jenkins.io/doc/pipeline/steps/lambdatest-automation/#stepclass-lambdatestreportpublisher-lambdatest-report)

*   [Last Changes Plugin](https://www.jenkins.io/doc/pipeline/steps/last-changes/)
    *   [`getLastChangesPublisher`: Get Last Changes Publisher](https://www.jenkins.io/doc/pipeline/steps/last-changes/#getlastchangespublisher-get-last-changes-publisher)
    *   [`publishLastChanges`: publish the changes](https://www.jenkins.io/doc/pipeline/steps/last-changes/#publishlastchanges-publish-the-changes)
    *   [`lastChanges`: Publish Last Changes](https://www.jenkins.io/doc/pipeline/steps/last-changes/#lastchanges-publish-last-changes)

*   [LeanIX Value Stream Management](https://www.jenkins.io/doc/pipeline/steps/leanix-microservice-intelligence/)
    *   [`leanIXMicroserviceIntelligence`: LeanIX Value Stream Management](https://www.jenkins.io/doc/pipeline/steps/leanix-microservice-intelligence/#leanixmicroserviceintelligence-leanix-value-stream-management)

*   [Leapwork](https://www.jenkins.io/doc/pipeline/steps/leapwork/)
    *   [`step([$class: 'LeapworkJenkinsBridgeBuilder'])`: Leapwork](https://www.jenkins.io/doc/pipeline/steps/leapwork/#stepclass-leapworkjenkinsbridgebuilder-leapwork)

*   [Levo Plugin](https://www.jenkins.io/doc/pipeline/steps/levo/)
    *   [`levo-test-plan`: Levo Test Plan](https://www.jenkins.io/doc/pipeline/steps/levo/#levo-test-plan-levo-test-plan)

*   [LIFX notifier - smart lightbulbs build indicator](https://www.jenkins.io/doc/pipeline/steps/lifx-notifier/)
    *   [`step([$class: 'LifxNotifier'])`: Lifx notifier](https://www.jenkins.io/doc/pipeline/steps/lifx-notifier/#stepclass-lifxnotifier-lifx-notifier)

*   [Lighthouse Report Plugin](https://www.jenkins.io/doc/pipeline/steps/lighthouse-report/)
    *   [`lighthouseReport`: Lighthouse Report](https://www.jenkins.io/doc/pipeline/steps/lighthouse-report/#lighthousereport-lighthouse-report)

*   [Liquibase Runner](https://www.jenkins.io/doc/pipeline/steps/liquibase-runner/)
    *   [`step([$class: 'DropAllBuilder'])`: Liquibase: Drop everything in database](https://www.jenkins.io/doc/pipeline/steps/liquibase-runner/#stepclass-dropallbuilder-liquibase-drop-everything-in-database)
    *   [`step([$class: 'RawCliBuilder'])`: Liquibase: CLI Command](https://www.jenkins.io/doc/pipeline/steps/liquibase-runner/#stepclass-rawclibuilder-liquibase-cli-command)
    *   [`step([$class: 'RollbackBuilder'])`: Liquibase: Roll Back Changes](https://www.jenkins.io/doc/pipeline/steps/liquibase-runner/#stepclass-rollbackbuilder-liquibase-roll-back-changes)
    *   [`step([$class: 'TagBuilder'])`: Liquibase: Tag Database](https://www.jenkins.io/doc/pipeline/steps/liquibase-runner/#stepclass-tagbuilder-liquibase-tag-database)
    *   [`step([$class: 'UpdateBuilder'])`: Liquibase: Update Database](https://www.jenkins.io/doc/pipeline/steps/liquibase-runner/#stepclass-updatebuilder-liquibase-update-database)

*   [LoadComplete support plugin](https://www.jenkins.io/doc/pipeline/steps/loadcomplete/)
    *   [`loadcompletetest`: LoadComplete Test](https://www.jenkins.io/doc/pipeline/steps/loadcomplete/#loadcompletetest-loadcomplete-test)

*   [Loadmance Plugin](https://www.jenkins.io/doc/pipeline/steps/loadmance/)
    *   [`loadmance`: Loadmance Test Builder](https://www.jenkins.io/doc/pipeline/steps/loadmance/#loadmance-loadmance-test-builder)

*   [LoadNinja Plugin](https://www.jenkins.io/doc/pipeline/steps/loadninja/)
    *   [`step([$class: 'LoadNinjaBuilder'])`: LoadNinja](https://www.jenkins.io/doc/pipeline/steps/loadninja/#stepclass-loadninjabuilder-loadninja)

*   [LoadRunner Cloud](https://www.jenkins.io/doc/pipeline/steps/loadrunner-cloud/)
    *   [`lrcRunTest`: Run test in LoadRunner Cloud](https://www.jenkins.io/doc/pipeline/steps/loadrunner-cloud/#lrcruntest-run-test-in-loadrunner-cloud)
    *   [`lrcGenTrendingReport`: Generate LoadRunner Cloud trending report](https://www.jenkins.io/doc/pipeline/steps/loadrunner-cloud/#lrcgentrendingreport-generate-loadrunner-cloud-trending-report)

*   [Lockable Resources plugin](https://www.jenkins.io/doc/pipeline/steps/lockable-resources/)
    *   [`lock`: Lock shared resource](https://www.jenkins.io/doc/pipeline/steps/lockable-resources/#lock-lock-shared-resource)

*   [Log File Filter Plugin](https://www.jenkins.io/doc/pipeline/steps/log-file-filter/)
    *   [`logFileFilter`: LogFileFilterStep](https://www.jenkins.io/doc/pipeline/steps/log-file-filter/#logfilefilter-logfilefilterstep)

*   [Log Flow Visualizer](https://www.jenkins.io/doc/pipeline/steps/log-flow-visualizer/)
    *   [`logFlowVisualizer`: Log Flow Visualizer](https://www.jenkins.io/doc/pipeline/steps/log-flow-visualizer/#logflowvisualizer-log-flow-visualizer)

*   [Log Parser Plugin](https://www.jenkins.io/doc/pipeline/steps/log-parser/)
    *   [`logParser`: Console output (build log) parsing](https://www.jenkins.io/doc/pipeline/steps/log-parser/#logparser-console-output-build-log-parsing)

*   [Logstash](https://www.jenkins.io/doc/pipeline/steps/logstash/)
    *   [`logstash`: Send individual log lines to Logstash](https://www.jenkins.io/doc/pipeline/steps/logstash/#logstash-send-individual-log-lines-to-logstash)
    *   [`logstashSend`: Send console log to Logstash](https://www.jenkins.io/doc/pipeline/steps/logstash/#logstashsend-send-console-log-to-logstash)
    *   [`step([$class: 'LogstashNotifier'])`: Send console log to Logstash](https://www.jenkins.io/doc/pipeline/steps/logstash/#stepclass-logstashnotifier-send-console-log-to-logstash)

*   [mabl](https://www.jenkins.io/doc/pipeline/steps/mabl-integration/)
    *   [`mabl`: Run mabl tests](https://www.jenkins.io/doc/pipeline/steps/mabl-integration/#mabl-run-mabl-tests)

*   [Machine Learning Plugin](https://www.jenkins.io/doc/pipeline/steps/machine-learning/)
    *   [`ipythonBuilder`: IPython Builder](https://www.jenkins.io/doc/pipeline/steps/machine-learning/#ipythonbuilder-ipython-builder)

*   [Mailer Plugin](https://www.jenkins.io/doc/pipeline/steps/mailer/)
    *   [`step([$class: 'Mailer'])`: E-mail Notification](https://www.jenkins.io/doc/pipeline/steps/mailer/#stepclass-mailer-e-mail-notification)

*   [Marathon Deployment](https://www.jenkins.io/doc/pipeline/steps/marathon/)
    *   [`marathon`: Marathon Deployment](https://www.jenkins.io/doc/pipeline/steps/marathon/#marathon-marathon-deployment)

*   [MarkdownParams](https://www.jenkins.io/doc/pipeline/steps/markdown-params/)
    *   [`markdownParams`: MarkdownParams](https://www.jenkins.io/doc/pipeline/steps/markdown-params/#markdownparams-markdownparams)

*   [Mask Passwords Plugin](https://www.jenkins.io/doc/pipeline/steps/mask-passwords/)
    *   [`maskPasswords`: Mask passwords and regexes (and enable global passwords)](https://www.jenkins.io/doc/pipeline/steps/mask-passwords/#maskpasswords-mask-passwords-and-regexes-and-enable-global-passwords)

*   [MAT Performance Benchmarking by Broadcom](https://www.jenkins.io/doc/pipeline/steps/ca-mat-performance-benchmarking-by-broadcom/)
    *   [`step([$class: 'Autogen'])`: Autogen](https://www.jenkins.io/doc/pipeline/steps/ca-mat-performance-benchmarking-by-broadcom/#stepclass-autogen-autogen)
    *   [`step([$class: 'EmailPostBuildAction'])`: Performance Benchmarking Report](https://www.jenkins.io/doc/pipeline/steps/ca-mat-performance-benchmarking-by-broadcom/#stepclass-emailpostbuildaction-performance-benchmarking-report)
    *   [`step([$class: 'PerformanceAnalysisBuilder'])`: Performance Benchmarking](https://www.jenkins.io/doc/pipeline/steps/ca-mat-performance-benchmarking-by-broadcom/#stepclass-performanceanalysisbuilder-performance-benchmarking)

*   [MathWorks Polyspace Plugin](https://www.jenkins.io/doc/pipeline/steps/mathworks-polyspace/)
    *   [`step([$class: 'PolyspacePostBuildActions'])`: Polyspace Notification](https://www.jenkins.io/doc/pipeline/steps/mathworks-polyspace/#stepclass-polyspacepostbuildactions-polyspace-notification)
    *   [`wrap([$class: 'PolyspaceBuildWrapper'])`: Select Polyspace installation settings](https://www.jenkins.io/doc/pipeline/steps/mathworks-polyspace/#wrapclass-polyspacebuildwrapper-select-polyspace-installation-settings)

*   [MATLAB Plugin](https://www.jenkins.io/doc/pipeline/steps/matlab/)
    *   [`runMATLABBuild`: Run a MATLAB build using the MATLAB build tool](https://www.jenkins.io/doc/pipeline/steps/matlab/#runmatlabbuild-run-a-matlab-build-using-the-matlab-build-tool)
    *   [`runMATLABCommand`: Run MATLAB commands, scripts, or functions](https://www.jenkins.io/doc/pipeline/steps/matlab/#runmatlabcommand-run-matlab-commands-scripts-or-functions)
    *   [`runMATLABTests`: Run MATLAB tests and generate artifacts](https://www.jenkins.io/doc/pipeline/steps/matlab/#runmatlabtests-run-matlab-tests-and-generate-artifacts)
    *   [`step([$class: 'RunMatlabBuildBuilder'])`: Run MATLAB Build](https://www.jenkins.io/doc/pipeline/steps/matlab/#stepclass-runmatlabbuildbuilder-run-matlab-build)
    *   [`step([$class: 'RunMatlabCommandBuilder'])`: Run MATLAB Command](https://www.jenkins.io/doc/pipeline/steps/matlab/#stepclass-runmatlabcommandbuilder-run-matlab-command)
    *   [`step([$class: 'RunMatlabTestsBuilder'])`: Run MATLAB Tests](https://www.jenkins.io/doc/pipeline/steps/matlab/#stepclass-runmatlabtestsbuilder-run-matlab-tests)
    *   [`wrap([$class: 'UseMatlabVersionBuildWrapper'])`: Use MATLAB version](https://www.jenkins.io/doc/pipeline/steps/matlab/#wrapclass-usematlabversionbuildwrapper-use-matlab-version)

*   [Matrix Communication Plugin](https://www.jenkins.io/doc/pipeline/steps/matrix-communication/)
    *   [`matrixSendMessage`: Send message to a Matrix room](https://www.jenkins.io/doc/pipeline/steps/matrix-communication/#matrixsendmessage-send-message-to-a-matrix-room)

*   [Mattermost Notification Plugin](https://www.jenkins.io/doc/pipeline/steps/mattermost/)
    *   [`mattermostSend`: Send Mattermost message](https://www.jenkins.io/doc/pipeline/steps/mattermost/#mattermostsend-send-mattermost-message)

*   [Maven Invoker plugin](https://www.jenkins.io/doc/pipeline/steps/maven-invoker-plugin/)
    *   [`maven_invoker`: Archive Maven Invoker test results](https://www.jenkins.io/doc/pipeline/steps/maven-invoker-plugin/#maven-invoker-archive-maven-invoker-test-results)
    *   [`step([$class: 'MavenInvokerRecorder'])`: Maven Invoker Plugin Results](https://www.jenkins.io/doc/pipeline/steps/maven-invoker-plugin/#stepclass-maveninvokerrecorder-maven-invoker-plugin-results)

*   [Maven Repository Server Plugin](https://www.jenkins.io/doc/pipeline/steps/repository/)
    *   [`step([$class: 'UpdaterPublisher'])`: Publish Maven Artifacts](https://www.jenkins.io/doc/pipeline/steps/repository/#stepclass-updaterpublisher-publish-maven-artifacts)
    *   [`wrap([$class: 'RepositoryDefinitionProperty'])`: Define Upstream Maven Repository](https://www.jenkins.io/doc/pipeline/steps/repository/#wrapclass-repositorydefinitionproperty-define-upstream-maven-repository)

*   [Maven SNAPSHOT Check Plugin](https://www.jenkins.io/doc/pipeline/steps/maven-snapshot-check/)
    *   [`mavenSnapshotCheck`: Maven SNAPSHOT Check](https://www.jenkins.io/doc/pipeline/steps/maven-snapshot-check/#mavensnapshotcheck-maven-snapshot-check)

*   [meliora-testlab](https://www.jenkins.io/doc/pipeline/steps/meliora-testlab/)
    *   [`melioraTestlab`: Publish test results to Testlab](https://www.jenkins.io/doc/pipeline/steps/meliora-testlab/#melioratestlab-publish-test-results-to-testlab)

*   [Memory Map Plugin](https://www.jenkins.io/doc/pipeline/steps/memory-map/)
    *   [`memoryMap`: Memory Map Publisher](https://www.jenkins.io/doc/pipeline/steps/memory-map/#memorymap-memory-map-publisher)

*   [Mend Cloud Native Plugin](https://www.jenkins.io/doc/pipeline/steps/mend-cloud-native-security-scanner/)
    *   [`step([$class: 'MendCnScannerBuilder'])`: Mend Cloud Native Security Scanner](https://www.jenkins.io/doc/pipeline/steps/mend-cloud-native-security-scanner/#stepclass-mendcnscannerbuilder-mend-cloud-native-security-scanner)

*   [MergeBase SCA Plugin](https://www.jenkins.io/doc/pipeline/steps/mergebase-sca/)
    *   [`mergebaseScan`: Run MergeBase SCA Scan](https://www.jenkins.io/doc/pipeline/steps/mergebase-sca/#mergebasescan-run-mergebase-sca-scan)
    *   [`step([$class: 'MergebaseStepBuilder'])`: MergeBase Build Step](https://www.jenkins.io/doc/pipeline/steps/mergebase-sca/#stepclass-mergebasestepbuilder-mergebase-build-step)

*   [MetaDefender Plugin](https://www.jenkins.io/doc/pipeline/steps/metadefender/)
    *   [`step([$class: 'ScanBuilder'])`: Scan with MetaDefender](https://www.jenkins.io/doc/pipeline/steps/metadefender/#stepclass-scanbuilder-scan-with-metadefender)

*   [Metrics Aggregation](https://www.jenkins.io/doc/pipeline/steps/metrics-aggregation/)
    *   [`metrics`: Record Metrics](https://www.jenkins.io/doc/pipeline/steps/metrics-aggregation/#metrics-record-metrics)
    *   [`step([$class: 'MetricsRecorder'])`: Record Metrics](https://www.jenkins.io/doc/pipeline/steps/metrics-aggregation/#stepclass-metricsrecorder-record-metrics)

*   [MicroNova EXAM Plugin](https://www.jenkins.io/doc/pipeline/steps/exam/)
    *   [`examCleanTarget`: EXAM Clear target](https://www.jenkins.io/doc/pipeline/steps/exam/#examcleantarget-exam-clear-target)
    *   [`examTest_ExecutionFile`: EXAM Start test run (execution file)](https://www.jenkins.io/doc/pipeline/steps/exam/#examtest-executionfile-exam-start-test-run-execution-file)
    *   [`examTest_Model`: EXAM Start test run (model)](https://www.jenkins.io/doc/pipeline/steps/exam/#examtest-model-exam-start-test-run-model)
    *   [`examTCG`: EXAM Test Case Generator](https://www.jenkins.io/doc/pipeline/steps/exam/#examtcg-exam-test-case-generator)
    *   [`examRun_Groovy`: EXAM Start Groovy script](https://www.jenkins.io/doc/pipeline/steps/exam/#examrun-groovy-exam-start-groovy-script)

*   [Minio Plugin](https://www.jenkins.io/doc/pipeline/steps/minio/)
    *   [`minio`: Upload build artifacts to Minio](https://www.jenkins.io/doc/pipeline/steps/minio/#minio-upload-build-artifacts-to-minio)
    *   [`minioDelete`: Delete build artifacts from Minio](https://www.jenkins.io/doc/pipeline/steps/minio/#miniodelete-delete-build-artifacts-from-minio)
    *   [`minioDownload`: Download files from Minio](https://www.jenkins.io/doc/pipeline/steps/minio/#miniodownload-download-files-from-minio)

*   [Minio Storage](https://www.jenkins.io/doc/pipeline/steps/minio-storage/)
    *   [`step([$class: 'MinioUploader'])`: Upload build artifacts to Minio server](https://www.jenkins.io/doc/pipeline/steps/minio-storage/#stepclass-miniouploader-upload-build-artifacts-to-minio-server)

*   [misc-info-tools](https://www.jenkins.io/doc/pipeline/steps/misc-info-tools/)
    *   [`findJobs`: Job Finder list generator](https://www.jenkins.io/doc/pipeline/steps/misc-info-tools/#findjobs-job-finder-list-generator)
    *   [`getAllLabelsForAllNodes`: Get All Jenkins Nodes and Labels](https://www.jenkins.io/doc/pipeline/steps/misc-info-tools/#getalllabelsforallnodes-get-all-jenkins-nodes-and-labels)
    *   [`getCurrentBuildHost`: Get the Build Hostname in context](https://www.jenkins.io/doc/pipeline/steps/misc-info-tools/#getcurrentbuildhost-get-the-build-hostname-in-context)
    *   [`getLastSuccessfulBuildNumber`: Job build number getter](https://www.jenkins.io/doc/pipeline/steps/misc-info-tools/#getlastsuccessfulbuildnumber-job-build-number-getter)
    *   [`relatedJobChecks`: Related Job Checks](https://www.jenkins.io/doc/pipeline/steps/misc-info-tools/#relatedjobchecks-related-job-checks)

*   [MISRA Compliance Report Plugin](https://www.jenkins.io/doc/pipeline/steps/misra-compliance-report-generator/)
    *   [`misraReport`: Build MISRA Guideline Compliance Summary (GCS)](https://www.jenkins.io/doc/pipeline/steps/misra-compliance-report-generator/#misrareport-build-misra-guideline-compliance-summary-gcs)

*   [Mock Load Builder Plugin](https://www.jenkins.io/doc/pipeline/steps/mock-load-builder/)
    *   [`step([$class: 'MockLoadBuilder'])`: Mock Load](https://www.jenkins.io/doc/pipeline/steps/mock-load-builder/#stepclass-mockloadbuilder-mock-load)
    *   [`withMockLoad`: Mock load with separate sh command](https://www.jenkins.io/doc/pipeline/steps/mock-load-builder/#withmockload-mock-load-with-separate-sh-command)

*   [MQ Notifier](https://www.jenkins.io/doc/pipeline/steps/mq-notifier/)
    *   [`publishMQMessage`: Publish MQ Message](https://www.jenkins.io/doc/pipeline/steps/mq-notifier/#publishmqmessage-publish-mq-message)

*   [MQTT Notification Plugin](https://www.jenkins.io/doc/pipeline/steps/mqtt-notification-plugin/)
    *   [`mqttNotification`: MQTT Notification](https://www.jenkins.io/doc/pipeline/steps/mqtt-notification-plugin/#mqttnotification-mqtt-notification)

*   [MSTest plugin](https://www.jenkins.io/doc/pipeline/steps/mstest/)
    *   [`mstest`: Publish MSTest test result report](https://www.jenkins.io/doc/pipeline/steps/mstest/#mstest-publish-mstest-test-result-report)

*   [NeoLoad Plugin](https://www.jenkins.io/doc/pipeline/steps/neoload-jenkins-plugin/)
    *   [`neoloadRefreshTrends`: Refresh NeoLoad Trends](https://www.jenkins.io/doc/pipeline/steps/neoload-jenkins-plugin/#neoloadrefreshtrends-refresh-neoload-trends)
    *   [`neoloadRun`: Run a NeoLoad scenario](https://www.jenkins.io/doc/pipeline/steps/neoload-jenkins-plugin/#neoloadrun-run-a-neoload-scenario)
    *   [`step([$class: 'NeoBuildAction'])`: Execute a NeoLoad Scenario](https://www.jenkins.io/doc/pipeline/steps/neoload-jenkins-plugin/#stepclass-neobuildaction-execute-a-neoload-scenario)

*   [Nested Data Reporting](https://www.jenkins.io/doc/pipeline/steps/nested-data-reporting/)
    *   [`publishReport`: Publish report files like json, yaml, csv or xml](https://www.jenkins.io/doc/pipeline/steps/nested-data-reporting/#publishreport-publish-report-files-like-json-yaml-csv-or-xml)

*   [Netsparker Enterprise Scan Plugin](https://www.jenkins.io/doc/pipeline/steps/netsparker-cloud-scan/)
    *   [`NCScanBuilder`: Netsparker Enterprise Scan](https://www.jenkins.io/doc/pipeline/steps/netsparker-cloud-scan/#ncscanbuilder-netsparker-enterprise-scan)

*   [NeuVector Vulnerability Scanner Plugin](https://www.jenkins.io/doc/pipeline/steps/neuvector-vulnerability-scanner/)
    *   [`neuvector`: NeuVector Vulnerability Scanner](https://www.jenkins.io/doc/pipeline/steps/neuvector-vulnerability-scanner/#neuvector-neuvector-vulnerability-scanner)

*   [New Relic Deployment Notifier Plugin](https://www.jenkins.io/doc/pipeline/steps/newrelic-deployment-notifier/)
    *   [`step([$class: 'NewRelicDeploymentNotifier'])`: New Relic Deployment Notifications](https://www.jenkins.io/doc/pipeline/steps/newrelic-deployment-notifier/#stepclass-newrelicdeploymentnotifier-new-relic-deployment-notifications)

*   [Nexus Artifact Uploader](https://www.jenkins.io/doc/pipeline/steps/nexus-artifact-uploader/)
    *   [`nexusArtifactUploader`: Nexus Artifact Uploader](https://www.jenkins.io/doc/pipeline/steps/nexus-artifact-uploader/#nexusartifactuploader-nexus-artifact-uploader)
    *   [`step([$class: 'NexusArtifactUploader'])`: Nexus artifact uploader](https://www.jenkins.io/doc/pipeline/steps/nexus-artifact-uploader/#stepclass-nexusartifactuploader-nexus-artifact-uploader)

*   [Nirmata Plugin](https://www.jenkins.io/doc/pipeline/steps/nirmata/)
    *   [`nirmata`: Invoke Nirmata Service](https://www.jenkins.io/doc/pipeline/steps/nirmata/#nirmata-invoke-nirmata-service)

*   [NodeJS Plugin](https://www.jenkins.io/doc/pipeline/steps/nodejs/)
    *   [`nodejs`: Provide Node & npm bin/ folder to PATH](https://www.jenkins.io/doc/pipeline/steps/nodejs/#nodejs-provide-node-npm-bin-folder-to-path)

*   [NodePool Agents Plugin](https://www.jenkins.io/doc/pipeline/steps/nodepool-agents/)
    *   [`nodePoolHold`: Set NodePool hold from within a job](https://www.jenkins.io/doc/pipeline/steps/nodepool-agents/#nodepoolhold-set-nodepool-hold-from-within-a-job)

*   [Non Dynamic Hello World: TESTING PLUGIN](https://www.jenkins.io/doc/pipeline/steps/non-dynamic-hello-world/)
    *   [`greet`: Say hello world](https://www.jenkins.io/doc/pipeline/steps/non-dynamic-hello-world/#greet-say-hello-world)

*   [Notifer Plugin](https://www.jenkins.io/doc/pipeline/steps/notifer/)
    *   [`notifer`: Send Notifer Notification](https://www.jenkins.io/doc/pipeline/steps/notifer/#notifer-send-notifer-notification)
    *   [`step([$class: 'NotiferNotifier'])`: Send Notifer Notification](https://www.jenkins.io/doc/pipeline/steps/notifer/#stepclass-notifernotifier-send-notifer-notification)

*   [Notification plugin](https://www.jenkins.io/doc/pipeline/steps/notification/)
    *   [`notifyEndpoints`: Notify configured endpoints](https://www.jenkins.io/doc/pipeline/steps/notification/#notifyendpoints-notify-configured-endpoints)

*   [Notify.Events](https://www.jenkins.io/doc/pipeline/steps/notify-events/)
    *   [`notifyEvents`: Send notification](https://www.jenkins.io/doc/pipeline/steps/notify-events/#notifyevents-send-notification)
    *   [`step([$class: 'NotifyEventsBuilder'])`: Notify.Events](https://www.jenkins.io/doc/pipeline/steps/notify-events/#stepclass-notifyeventsbuilder-notify-events)
    *   [`step([$class: 'NotifyEventsPublisher'])`: Notify.Events](https://www.jenkins.io/doc/pipeline/steps/notify-events/#stepclass-notifyeventspublisher-notify-events)

*   [NowSecure Auto Plugin](https://www.jenkins.io/doc/pipeline/steps/nowsecure-auto-security-test/)
    *   [`apiKey`: NowSecure Auto Security Test](https://www.jenkins.io/doc/pipeline/steps/nowsecure-auto-security-test/#apikey-nowsecure-auto-security-test)

*   [NowSecure CI Assessments](https://www.jenkins.io/doc/pipeline/steps/nowsecure-ci-assessments/)
    *   [`nowsecureAssessment`: NowSecure Assessment Configuration](https://www.jenkins.io/doc/pipeline/steps/nowsecure-ci-assessments/#nowsecureassessment-nowsecure-assessment-configuration)

*   [NPM and Yarn Wrapper and Steps](https://www.jenkins.io/doc/pipeline/steps/npm-yarn-wrapper-steps/)
    *   [`npm`: Run an npm command](https://www.jenkins.io/doc/pipeline/steps/npm-yarn-wrapper-steps/#npm-run-an-npm-command)
    *   [`yarn`: Run a yarn command](https://www.jenkins.io/doc/pipeline/steps/npm-yarn-wrapper-steps/#yarn-run-a-yarn-command)
    *   [`withNPMWrapper`: Set NPM Environment](https://www.jenkins.io/doc/pipeline/steps/npm-yarn-wrapper-steps/#withnpmwrapper-set-npm-environment)

*   [NS-ND Integration Performance Publisher Plugin](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/)
    *   [`step([$class: 'CreateVM'])`: Create Virtual Server](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-createvm-create-virtual-server)
    *   [`step([$class: 'CreateVirtualService'])`: Cavisson Service Virtualization : Create](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-createvirtualservice-cavisson-service-virtualization-create)
    *   [`step([$class: 'DeleteVirtualService'])`: Cavisson Service Virtualization : Delete](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-deletevirtualservice-cavisson-service-virtualization-delete)
    *   [`step([$class: 'DestroyVM'])`: Destroy VM](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-destroyvm-destroy-vm)
    *   [`step([$class: 'DisableVirtualService'])`: Cavisson Service Virtualization : Disable](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-disablevirtualservice-cavisson-service-virtualization-disable)
    *   [`step([$class: 'EditVirtualService'])`: Cavisson Service Virtualization : Edit](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-editvirtualservice-cavisson-service-virtualization-edit)
    *   [`step([$class: 'EnableVirtualService'])`: Cavisson Service Virtualization : Enable](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-enablevirtualservice-cavisson-service-virtualization-enable)
    *   [`step([$class: 'FetchTestAssets'])`: Fetch Test Assets](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-fetchtestassets-fetch-test-assets)
    *   [`step([$class: 'NSNDIntegrationResultsPublisher'])`: NS/NC-ND Integration Performance Publisher](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-nsndintegrationresultspublisher-nsnc-nd-integration-performance-publisher)
    *   [`step([$class: 'NetDiagnosticsResultsPublisher'])`: NetDiagnostics Performance Publisher](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-netdiagnosticsresultspublisher-netdiagnostics-performance-publisher)
    *   [`step([$class: 'NetStormBuilder'])`: Execute NetStorm/NetCloud Test](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-netstormbuilder-execute-netstormnetcloud-test)
    *   [`step([$class: 'NetStormResultsPublisher'])`: NetStorm/NetCloud Performance Publisher](https://www.jenkins.io/doc/pipeline/steps/cavisson-ns-nd-integration/#stepclass-netstormresultspublisher-netstormnetcloud-performance-publisher)

*   [Nuclei Plugin](https://www.jenkins.io/doc/pipeline/steps/nuclei/)
    *   [`step([$class: 'NucleiBuilder'])`: Nuclei Vulnerability Scanner](https://www.jenkins.io/doc/pipeline/steps/nuclei/#stepclass-nucleibuilder-nuclei-vulnerability-scanner)

*   [NUnit plugin](https://www.jenkins.io/doc/pipeline/steps/nunit/)
    *   [`nunit`: Publish NUnit test result report](https://www.jenkins.io/doc/pipeline/steps/nunit/#nunit-publish-nunit-test-result-report)

*   [Nutanix Calm Plugin](https://www.jenkins.io/doc/pipeline/steps/nutanix-calm/)
    *   [`step([$class: 'BlueprintLaunch'])`: Nutanix Calm Blueprint Launch](https://www.jenkins.io/doc/pipeline/steps/nutanix-calm/#stepclass-blueprintlaunch-nutanix-calm-blueprint-launch)
    *   [`step([$class: 'RunApplicationAction'])`: Nutanix Calm Application Action Run](https://www.jenkins.io/doc/pipeline/steps/nutanix-calm/#stepclass-runapplicationaction-nutanix-calm-application-action-run)

*   [nvm-wrapper](https://www.jenkins.io/doc/pipeline/steps/nvm-wrapper/)
    *   [`nvm`: Setup the environment for an NVM installation.](https://www.jenkins.io/doc/pipeline/steps/nvm-wrapper/#nvm-setup-the-environment-for-an-nvm-installation)

*   [oak9](https://www.jenkins.io/doc/pipeline/steps/oak9/)
    *   [`step([$class: 'Oak9Builder'])`: oak9 Runner](https://www.jenkins.io/doc/pipeline/steps/oak9/#stepclass-oak9builder-oak9-runner)

*   [OctoPerf Load Testing Plugin.](https://www.jenkins.io/doc/pipeline/steps/octoperf/)
    *   [`octoPerfTest`: Runs test in OctoPerf Cloud](https://www.jenkins.io/doc/pipeline/steps/octoperf/#octoperftest-runs-test-in-octoperf-cloud)
    *   [`step([$class: 'OctoperfBuilder'])`: OctoPerf](https://www.jenkins.io/doc/pipeline/steps/octoperf/#stepclass-octoperfbuilder-octoperf)

*   [Octopus Deploy](https://www.jenkins.io/doc/pipeline/steps/octopusdeploy/)
    *   [`octopusDeployRelease`: Octopus Deploy: Deploy Release](https://www.jenkins.io/doc/pipeline/steps/octopusdeploy/#octopusdeployrelease-octopus-deploy-deploy-release)
    *   [`octopusPack`: Octopus Deploy: Package application](https://www.jenkins.io/doc/pipeline/steps/octopusdeploy/#octopuspack-octopus-deploy-package-application)
    *   [`octopusPushBuildInformation`: Octopus Deploy: Push build information](https://www.jenkins.io/doc/pipeline/steps/octopusdeploy/#octopuspushbuildinformation-octopus-deploy-push-build-information)
    *   [`octopusPushPackage`: Octopus Deploy: Push packages](https://www.jenkins.io/doc/pipeline/steps/octopusdeploy/#octopuspushpackage-octopus-deploy-push-packages)
    *   [`octopusCreateRelease`: Octopus Deploy: Create Release](https://www.jenkins.io/doc/pipeline/steps/octopusdeploy/#octopuscreaterelease-octopus-deploy-create-release)

*   [Office 365 Connector / Power Automate workflows](https://www.jenkins.io/doc/pipeline/steps/Office-365-Connector/)
    *   [`office365ConnectorSend`: Send job status notifications to Office 365 (e.g. Microsoft Teams or Outlook)](https://www.jenkins.io/doc/pipeline/steps/Office-365-Connector/#office365connectorsend-send-job-status-notifications-to-office-365-e-g-microsoft-teams-or-outlook)

*   [OneSky Jenkins plugin](https://www.jenkins.io/doc/pipeline/steps/onesky/)
    *   [`OneSky`: Download translation resources from One Sky](https://www.jenkins.io/doc/pipeline/steps/onesky/#onesky-download-translation-resources-from-one-sky)

*   [ontrack Jenkins plug-in](https://www.jenkins.io/doc/pipeline/steps/ontrack/)
    *   [`ontrackBranchName`: Transforms a branch name, as provided by the pipeline for example, into a name suitable for a branch in Ontrack.](https://www.jenkins.io/doc/pipeline/steps/ontrack/#ontrackbranchname-transforms-a-branch-name-as-provided-by-the-pipeline-for-example-into-a-name-suitable-for-a-branch-in-ontrack)
    *   [`ontrackBranchSetup`: Setup an Ontrack branch, and creates it if it does not exist.](https://www.jenkins.io/doc/pipeline/steps/ontrack/#ontrackbranchsetup-setup-an-ontrack-branch-and-creates-it-if-it-does-not-exist)
    *   [`ontrackBuild`: Creates an Ontrack build](https://www.jenkins.io/doc/pipeline/steps/ontrack/#ontrackbuild-creates-an-ontrack-build)
    *   [`ontrackGraphQL`: Runs some Ontrack GraphQL script](https://www.jenkins.io/doc/pipeline/steps/ontrack/#ontrackgraphql-runs-some-ontrack-graphql-script)
    *   [`ontrackProjectSetup`: Setup an Ontrack project, and creates it if it does not exist.](https://www.jenkins.io/doc/pipeline/steps/ontrack/#ontrackprojectsetup-setup-an-ontrack-project-and-creates-it-if-it-does-not-exist)
    *   [`ontrackPromote`: Promotes an Ontrack build](https://www.jenkins.io/doc/pipeline/steps/ontrack/#ontrackpromote-promotes-an-ontrack-build)
    *   [`ontrackScript`: Runs some Ontrack DSL script](https://www.jenkins.io/doc/pipeline/steps/ontrack/#ontrackscript-runs-some-ontrack-dsl-script)
    *   [`ontrackValidate`: Validates an Ontrack build](https://www.jenkins.io/doc/pipeline/steps/ontrack/#ontrackvalidate-validates-an-ontrack-build)

*   [OpenEdge (Progress ABL)](https://www.jenkins.io/doc/pipeline/steps/openedge/)
    *   [`wrap([$class: 'OpenEdgeBuildWrapper'])`: OpenEdge](https://www.jenkins.io/doc/pipeline/steps/openedge/#wrapclass-openedgebuildwrapper-openedge)

*   [OpenShift Client Jenkins Plugin](https://www.jenkins.io/doc/pipeline/steps/openshift-client/)
    *   [`_OcAction`: Internal utility function for OpenShift DSL](https://www.jenkins.io/doc/pipeline/steps/openshift-client/#ocaction-internal-utility-function-for-openshift-dsl)
    *   [`_OcContextInit`: Internal utility function for OpenShift DSL](https://www.jenkins.io/doc/pipeline/steps/openshift-client/#occontextinit-internal-utility-function-for-openshift-dsl)

*   [OpenShift Pipeline Jenkins Plugin](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/)
    *   [`openshiftBuild`: Trigger OpenShift Build](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftbuild-trigger-openshift-build)
    *   [`openshiftCreateResource`: Create OpenShift Resource(s)](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftcreateresource-create-openshift-resources)
    *   [`openshiftDeleteResourceByJsonYaml`: Delete OpenShift Resource(s) from JSON or YAML](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftdeleteresourcebyjsonyaml-delete-openshift-resources-from-json-or-yaml)
    *   [`openshiftDeleteResourceByKey`: Delete OpenShift Resource(s) by Key](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftdeleteresourcebykey-delete-openshift-resources-by-key)
    *   [`openshiftDeleteResourceByLabels`: Delete OpenShift Resource(s) using Labels](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftdeleteresourcebylabels-delete-openshift-resources-using-labels)
    *   [`openshiftDeploy`: Trigger OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftdeploy-trigger-openshift-deployment)
    *   [`openshiftExec`: OpenShift Exec](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftexec-openshift-exec)
    *   [`openshiftImageStream`: OpenShift ImageStreams](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftimagestream-openshift-imagestreams)
    *   [`openshiftScale`: Scale OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftscale-scale-openshift-deployment)
    *   [`openshiftTag`: Tag OpenShift Image](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshifttag-tag-openshift-image)
    *   [`openshiftVerifyBuild`: Verify OpenShift Build](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftverifybuild-verify-openshift-build)
    *   [`openshiftVerifyDeployment`: Verify OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftverifydeployment-verify-openshift-deployment)
    *   [`openshiftVerifyService`: Verify OpenShift Service](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftverifyservice-verify-openshift-service)
    *   [`step([$class: 'OpenShiftBuildCanceller'])`: Cancel OpenShift Builds](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftbuildcanceller-cancel-openshift-builds)
    *   [`step([$class: 'OpenShiftDeployCanceller'])`: Cancel OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftdeploycanceller-cancel-openshift-deployment)
    *   [`step([$class: 'OpenShiftScalerPostAction'])`: Scale OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftscalerpostaction-scale-openshift-deployment)
    *   [`step([$class: 'OpenShiftBuildVerifier'])`: Verify OpenShift Build](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftbuildverifier-verify-openshift-build)
    *   [`step([$class: 'OpenShiftBuilder'])`: Trigger OpenShift Build](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftbuilder-trigger-openshift-build)
    *   [`step([$class: 'OpenShiftCreator'])`: Create OpenShift Resource(s)](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftcreator-create-openshift-resources)
    *   [`step([$class: 'OpenShiftDeleterJsonYaml'])`: Delete OpenShift Resource(s) from JSON or YAML](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftdeleterjsonyaml-delete-openshift-resources-from-json-or-yaml)
    *   [`step([$class: 'OpenShiftDeleterLabels'])`: Delete OpenShift Resource(s) using Labels](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftdeleterlabels-delete-openshift-resources-using-labels)
    *   [`step([$class: 'OpenShiftDeleterList'])`: Delete OpenShift Resource(s) by Key](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftdeleterlist-delete-openshift-resources-by-key)
    *   [`step([$class: 'OpenShiftDeployer'])`: Trigger OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftdeployer-trigger-openshift-deployment)
    *   [`step([$class: 'OpenShiftDeploymentVerifier'])`: Verify OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftdeploymentverifier-verify-openshift-deployment)
    *   [`step([$class: 'OpenShiftExec'])`: OpenShift Exec](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftexec-openshift-exec)
    *   [`step([$class: 'OpenShiftImageTagger'])`: Tag OpenShift Image](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftimagetagger-tag-openshift-image)
    *   [`step([$class: 'OpenShiftScaler'])`: Scale OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftscaler-scale-openshift-deployment)
    *   [`step([$class: 'OpenShiftServiceVerifier'])`: Verify OpenShift Service](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#stepclass-openshiftserviceverifier-verify-openshift-service)
    *   [`openshiftVerifyBuild`: Verify OpenShift Build](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftverifybuild-verify-openshift-build)
    *   [`openshiftBuild`: Trigger OpenShift Build](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftbuild-trigger-openshift-build)
    *   [`openshiftCreateResource`: Create OpenShift Resource(s)](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftcreateresource-create-openshift-resources)
    *   [`openshiftDeleteResourceByJsonYaml`: Delete OpenShift Resource(s) from JSON or YAML](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftdeleteresourcebyjsonyaml-delete-openshift-resources-from-json-or-yaml)
    *   [`openshiftDeleteResourceByLabels`: Delete OpenShift Resource(s) using Labels](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftdeleteresourcebylabels-delete-openshift-resources-using-labels)
    *   [`openshiftDeleteResourceByKey`: Delete OpenShift Resource(s) by Key](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftdeleteresourcebykey-delete-openshift-resources-by-key)
    *   [`openshiftDeploy`: Trigger OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftdeploy-trigger-openshift-deployment)
    *   [`openshiftVerifyDeployment`: Verify OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftverifydeployment-verify-openshift-deployment)
    *   [`openshiftExec`: OpenShift Exec](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftexec-openshift-exec)
    *   [`openshiftTag`: Tag OpenShift Image](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshifttag-tag-openshift-image)
    *   [`openshiftScale`: Scale OpenShift Deployment](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftscale-scale-openshift-deployment)
    *   [`openshiftVerifyService`: Verify OpenShift Service](https://www.jenkins.io/doc/pipeline/steps/openshift-pipeline/#openshiftverifyservice-verify-openshift-service)

*   [Openstack Cloud plugin](https://www.jenkins.io/doc/pipeline/steps/openstack-cloud/)
    *   [`openstackMachine`: Cloud instances provisioning](https://www.jenkins.io/doc/pipeline/steps/openstack-cloud/#openstackmachine-cloud-instances-provisioning)

*   [OpenTelemetry Plugin](https://www.jenkins.io/doc/pipeline/steps/opentelemetry/)
    *   [`setSpanAttributes`: Set Span Attributes](https://www.jenkins.io/doc/pipeline/steps/opentelemetry/#setspanattributes-set-span-attributes)
    *   [`withNewSpan`: Step with a new user-defined Span](https://www.jenkins.io/doc/pipeline/steps/opentelemetry/#withnewspan-step-with-a-new-user-defined-span)
    *   [`withSpanAttribute`: Set Span Attribute](https://www.jenkins.io/doc/pipeline/steps/opentelemetry/#withspanattribute-set-span-attribute)
    *   [`withSpanAttributes`: Set Span Attributes on child spans](https://www.jenkins.io/doc/pipeline/steps/opentelemetry/#withspanattributes-set-span-attributes-on-child-spans)

*   [OpenText Application Automation Tools](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/)
    *   [`loadRunnerTest`: Run LoadRunner performance scenario tests](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#loadrunnertest-run-loadrunner-performance-scenario-tests)
    *   [`runLoadRunnerScript`: Run LoadRunner script](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#runloadrunnerscript-run-loadrunner-script)
    *   [`sseBuildAndPublish`: Execute OpenText functional tests using ALM Lab Management and Publish test results](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#ssebuildandpublish-execute-opentext-functional-tests-using-alm-lab-management-and-publish-test-results)
    *   [`collectBranchesToAlmOctane`: Software Delivery Management branch collector](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#collectbranchestoalmoctane-software-delivery-management-branch-collector)
    *   [`commonResultUploadBuilder`: Upload test result to ALM using field mapping](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#commonresultuploadbuilder-upload-test-result-to-alm-using-field-mapping)
    *   [`publishGherkinResults`: Software Delivery Management Cucumber test reporter](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#publishgherkinresults-software-delivery-management-cucumber-test-reporter)
    *   [`executeTestsFromAlmOctane`: Execute OpenText functional tests from Software Delivery Management (Tech Preview)](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#executetestsfromalmoctane-execute-opentext-functional-tests-from-software-delivery-management-tech-preview)
    *   [`healthAnalyzer`: OpenText Health Analyzer](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#healthanalyzer-opentext-health-analyzer)
    *   [`step([$class: 'JobConfigRebrander'])`: Fix old OpenText Jenkins builds](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#stepclass-jobconfigrebrander-fix-old-opentext-jenkins-builds)
    *   [`step([$class: 'MigrateAlmCredentialsBuilder'])`: Migrate ALM Credentials](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#stepclass-migratealmcredentialsbuilder-migrate-alm-credentials)
    *   [`pcBuild`: Execute OpenText Enterprise Performance Engineering test](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#pcbuild-execute-opentext-enterprise-performance-engineering-test)
    *   [`collectPullRequestsToAlmOctane`: Software Delivery Management pull-request collector](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#collectpullrequeststoalmoctane-software-delivery-management-pull-request-collector)
    *   [`runFromAlmBuilder`: Execute OpenText functional tests from OpenText ALM](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#runfromalmbuilder-execute-opentext-functional-tests-from-opentext-alm)
    *   [`runFromCodelessBuilder`: Execute OpenText codeless tests](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#runfromcodelessbuilder-execute-opentext-codeless-tests)
    *   [`runFromFSBuilder`: Execute OpenText functional tests from file system](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#runfromfsbuilder-execute-opentext-functional-tests-from-file-system)
    *   [`step([$class: 'RunLoadRunnerScript'])`: Run LoadRunner script](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#stepclass-runloadrunnerscript-run-loadrunner-script)
    *   [`publishMicroFocusTestResults`: Publish OpenText test results](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#publishmicrofocustestresults-publish-opentext-test-results)
    *   [`addALMOctaneSonarQubeListener`: OpenText Software Delivery Management SonarQube listener](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#addalmoctanesonarqubelistener-opentext-software-delivery-management-sonarqube-listener)
    *   [`sseBuild`: Execute OpenText functional tests using OpenText ALM Lab Management](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#ssebuild-execute-opentext-functional-tests-using-opentext-alm-lab-management)
    *   [`step([$class: 'SvChangeModeBuilder'])`: SV: Change Mode of Virtual Service](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#stepclass-svchangemodebuilder-sv-change-mode-of-virtual-service)
    *   [`step([$class: 'SvDeployBuilder'])`: SV: Deploy Virtual Service](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#stepclass-svdeploybuilder-sv-deploy-virtual-service)
    *   [`step([$class: 'SvExportBuilder'])`: SV: Export Virtual Service](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#stepclass-svexportbuilder-sv-export-virtual-service)
    *   [`step([$class: 'SvUndeployBuilder'])`: SV: Undeploy Virtual Service](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#stepclass-svundeploybuilder-sv-undeploy-virtual-service)
    *   [`uploadResultToALM`: Upload test result to ALM](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#uploadresulttoalm-upload-test-result-to-alm)
    *   [`convertTestsToRun`: OpenText Software Delivery Management testing framework converter](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#convertteststorun-opentext-software-delivery-management-testing-framework-converter)
    *   [`publishCodeCoverage`: Software Delivery Management code coverage publisher](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#publishcodecoverage-software-delivery-management-code-coverage-publisher)
    *   [`svChangeModeStep`: SV: Change Mode of Virtual Service](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#svchangemodestep-sv-change-mode-of-virtual-service)
    *   [`svDeployStep`: SV: Deploy Virtual Service](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#svdeploystep-sv-deploy-virtual-service)
    *   [`svExportStep`: SV: Export Virtual Service](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#svexportstep-sv-export-virtual-service)
    *   [`svUndeployStep`: SV: Undeploy Virtual Service](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#svundeploystep-sv-undeploy-virtual-service)
    *   [`uftScenarioLoad`: Run UFT scenario](https://www.jenkins.io/doc/pipeline/steps/hp-application-automation-tools-plugin/#uftscenarioload-run-uft-scenario)

*   [OpenText Enterprise Performance Engineering integration With Git](https://www.jenkins.io/doc/pipeline/steps/micro-focus-performance-center-integration/)
    *   [`pcGitBuild`: Synchronize OpenText Enterprise Performance Engineering With Git](https://www.jenkins.io/doc/pipeline/steps/micro-focus-performance-center-integration/#pcgitbuild-synchronize-opentext-enterprise-performance-engineering-with-git)
    *   [`pcRunBuild`: Run OpenText Enterprise Performance Engineering Test](https://www.jenkins.io/doc/pipeline/steps/micro-focus-performance-center-integration/#pcrunbuild-run-opentext-enterprise-performance-engineering-test)

*   [OpsGenie Plugin](https://www.jenkins.io/doc/pipeline/steps/opsgenie/)
    *   [`opsgenie`: OpsGenie step](https://www.jenkins.io/doc/pipeline/steps/opsgenie/#opsgenie-opsgenie-step)

*   [OpsLevel Plugin](https://www.jenkins.io/doc/pipeline/steps/opslevel/)
    *   [`opsLevelNotify`: opsLevelNotify](https://www.jenkins.io/doc/pipeline/steps/opslevel/#opslevelnotify-opslevelnotify)

*   [Oracle Cloud Infrastructure DevOps Plugin](https://www.jenkins.io/doc/pipeline/steps/oracle-cloud-infrastructure-devops/)
    *   [`OCIUploadArtifact`: OCI Artifact Upload](https://www.jenkins.io/doc/pipeline/steps/oracle-cloud-infrastructure-devops/#ociuploadartifact-oci-artifact-upload)
    *   [`OCIDeployment`: OCI Deployment](https://www.jenkins.io/doc/pipeline/steps/oracle-cloud-infrastructure-devops/#ocideployment-oci-deployment)

*   [OSF Builder Suite :: Standalone Sonar Linter](https://www.jenkins.io/doc/pipeline/steps/osf-builder-suite-standalone-sonar-linter/)
    *   [`osfBuilderSuiteStandaloneSonarLinter`: OSF Builder Suite :: Standalone Sonar Linter](https://www.jenkins.io/doc/pipeline/steps/osf-builder-suite-standalone-sonar-linter/#osfbuildersuitestandalonesonarlinter-osf-builder-suite-standalone-sonar-linter)

*   [OSF Builder Suite For Salesforce Commerce Cloud :: Data Import](https://www.jenkins.io/doc/pipeline/steps/osf-builder-suite-for-sfcc-data-import/)
    *   [`osfBuilderSuiteForSFCCDataImport`: OSF Builder Suite For Salesforce Commerce Cloud :: Data Import](https://www.jenkins.io/doc/pipeline/steps/osf-builder-suite-for-sfcc-data-import/#osfbuildersuiteforsfccdataimport-osf-builder-suite-for-salesforce-commerce-cloud-data-import)

*   [OSF Builder Suite For Salesforce Commerce Cloud :: Deploy](https://www.jenkins.io/doc/pipeline/steps/osf-builder-suite-for-sfcc-deploy/)
    *   [`osfBuilderSuiteForSFCCDeploy`: OSF Builder Suite For Salesforce Commerce Cloud :: Deploy](https://www.jenkins.io/doc/pipeline/steps/osf-builder-suite-for-sfcc-deploy/#osfbuildersuiteforsfccdeploy-osf-builder-suite-for-salesforce-commerce-cloud-deploy)

*   [OSF Builder Suite For Salesforce Commerce Cloud :: Run Job](https://www.jenkins.io/doc/pipeline/steps/osf-builder-suite-for-sfcc-run-job/)
    *   [`osfBuilderSuiteForSFCCRunJob`: OSF Builder Suite For Salesforce Commerce Cloud :: Run Job](https://www.jenkins.io/doc/pipeline/steps/osf-builder-suite-for-sfcc-run-job/#osfbuildersuiteforsfccrunjob-osf-builder-suite-for-salesforce-commerce-cloud-run-job)

*   [Ostorlab Security And Privacy Scanner](https://www.jenkins.io/doc/pipeline/steps/ostorlab/)
    *   [`ostorlabScan`: Run Ostorlab Security Scanner](https://www.jenkins.io/doc/pipeline/steps/ostorlab/#ostorlabscan-run-ostorlab-security-scanner)

*   [Otel agent host metrics monitoring](https://www.jenkins.io/doc/pipeline/steps/opentelemetry-agent-metrics/)
    *   [`onMonit`: Start node_exporter + otel-contrib before the build, and shut them down after.](https://www.jenkins.io/doc/pipeline/steps/opentelemetry-agent-metrics/#onmonit-start-node-exporter-otel-contrib-before-the-build-and-shut-them-down-after)

*   [OverOps Query Plugin](https://www.jenkins.io/doc/pipeline/steps/overops-query/)
    *   [`OverOpsQuery`: OverOps Quality Report](https://www.jenkins.io/doc/pipeline/steps/overops-query/#overopsquery-overops-quality-report)

*   [Oversecured](https://www.jenkins.io/doc/pipeline/steps/oversecured/)
    *   [`oversecuredUpload`: Oversecured](https://www.jenkins.io/doc/pipeline/steps/oversecured/#oversecuredupload-oversecured)

*   [OWASP Dependency-Check Plugin](https://www.jenkins.io/doc/pipeline/steps/dependency-check-jenkins-plugin/)
    *   [`dependencyCheckPublisher`: Publish Dependency-Check results](https://www.jenkins.io/doc/pipeline/steps/dependency-check-jenkins-plugin/#dependencycheckpublisher-publish-dependency-check-results)
    *   [`step([$class: 'DependencyCheckPublisher'])`: Publish Dependency-Check results](https://www.jenkins.io/doc/pipeline/steps/dependency-check-jenkins-plugin/#stepclass-dependencycheckpublisher-publish-dependency-check-results)
    *   [`dependencyCheck`: Invoke Dependency-Check](https://www.jenkins.io/doc/pipeline/steps/dependency-check-jenkins-plugin/#dependencycheck-invoke-dependency-check)

*   [OWASP Dependency-Track Plugin](https://www.jenkins.io/doc/pipeline/steps/dependency-track/)
    *   [`dependencyTrackPublisher`: Publish BOM to Dependency-Track](https://www.jenkins.io/doc/pipeline/steps/dependency-track/#dependencytrackpublisher-publish-bom-to-dependency-track)

*   [P4 Plugin](https://www.jenkins.io/doc/pipeline/steps/p4/)
    *   [`p4`: P4 Groovy](https://www.jenkins.io/doc/pipeline/steps/p4/#p4-p4-groovy)
    *   [`p4SwarmUpdate`: P4 Swarm Update](https://www.jenkins.io/doc/pipeline/steps/p4/#p4swarmupdate-p4-swarm-update)
    *   [`p4approve`: P4 ApproveImpl Review](https://www.jenkins.io/doc/pipeline/steps/p4/#p4approve-p4-approveimpl-review)
    *   [`p4publish`: P4 Publish](https://www.jenkins.io/doc/pipeline/steps/p4/#p4publish-p4-publish)
    *   [`p4sync`: P4 Sync](https://www.jenkins.io/doc/pipeline/steps/p4/#p4sync-p4-sync)
    *   [`p4tag`: P4 Tag](https://www.jenkins.io/doc/pipeline/steps/p4/#p4tag-p4-tag)
    *   [`p4unshelve`: P4 Unshelve](https://www.jenkins.io/doc/pipeline/steps/p4/#p4unshelve-p4-unshelve)
    *   [`cleanup`: Perforce: Cleanup](https://www.jenkins.io/doc/pipeline/steps/p4/#cleanup-perforce-cleanup)

*   [Package Drone Deployer](https://www.jenkins.io/doc/pipeline/steps/package-drone/)
    *   [`pdrone`: Package Drone Deployer](https://www.jenkins.io/doc/pipeline/steps/package-drone/#pdrone-package-drone-deployer)

*   [PagerDuty Plugin](https://www.jenkins.io/doc/pipeline/steps/pagerduty/)
    *   [`pagerduty`: PagerDuty trigger/resolve step](https://www.jenkins.io/doc/pipeline/steps/pagerduty/#pagerduty-pagerduty-triggerresolve-step)
    *   [`pagerdutyChangeEvent`: PagerDuty Change Event step](https://www.jenkins.io/doc/pipeline/steps/pagerduty/#pagerdutychangeevent-pagerduty-change-event-step)
    *   [`step([$class: 'ChangeEvents'])`: PagerDuty Change Events](https://www.jenkins.io/doc/pipeline/steps/pagerduty/#stepclass-changeevents-pagerduty-change-events)

*   [Panoptica Vulnerability Scanner Plugin](https://www.jenkins.io/doc/pipeline/steps/portshift-scanner/)
    *   [`secureCNVulnerabilityScanner`: SecureCN Vulnerability Scanner](https://www.jenkins.io/doc/pipeline/steps/portshift-scanner/#securecnvulnerabilityscanner-securecn-vulnerability-scanner)

*   [Parallel Test Executor Plugin](https://www.jenkins.io/doc/pipeline/steps/parallel-test-executor/)
    *   [`splitTests`: Split Test Runs](https://www.jenkins.io/doc/pipeline/steps/parallel-test-executor/#splittests-split-test-runs)

*   [Parameterized Remote Trigger Plugin](https://www.jenkins.io/doc/pipeline/steps/Parameterized-Remote-Trigger/)
    *   [`step([$class: 'RemoteBuildConfiguration'])`: Trigger a remote parameterized job](https://www.jenkins.io/doc/pipeline/steps/Parameterized-Remote-Trigger/#stepclass-remotebuildconfiguration-trigger-a-remote-parameterized-job)
    *   [`triggerRemoteJob`: Trigger Remote Job](https://www.jenkins.io/doc/pipeline/steps/Parameterized-Remote-Trigger/#triggerremotejob-trigger-remote-job)

*   [Parasoft Findings](https://www.jenkins.io/doc/pipeline/steps/parasoft-findings/)
    *   [`recordParasoftCoverage`: Record Parasoft code coverage results](https://www.jenkins.io/doc/pipeline/steps/parasoft-findings/#recordparasoftcoverage-record-parasoft-code-coverage-results)

*   [Peass-CI](https://www.jenkins.io/doc/pipeline/steps/peass-ci/)
    *   [`cleanPerformanceMeasurement`: Clean Peass-CI Cache](https://www.jenkins.io/doc/pipeline/steps/peass-ci/#cleanperformancemeasurement-clean-peass-ci-cache)
    *   [`measure`: Measure Version Performance](https://www.jenkins.io/doc/pipeline/steps/peass-ci/#measure-measure-version-performance)
    *   [`peassOverview`: Peass Overview](https://www.jenkins.io/doc/pipeline/steps/peass-ci/#peassoverview-peass-overview)

*   [Perforce Static Analysis Plugin](https://www.jenkins.io/doc/pipeline/steps/p4sa/)
    *   [`p4StaticAnalysis`: Run Perforce Static Analysis](https://www.jenkins.io/doc/pipeline/steps/p4sa/#p4staticanalysis-run-perforce-static-analysis)

*   [Performance Plugin](https://www.jenkins.io/doc/pipeline/steps/performance/)
    *   [`perfReport`: Publish Performance test result report](https://www.jenkins.io/doc/pipeline/steps/performance/#perfreport-publish-performance-test-result-report)
    *   [`bzt`: Run Performance Test](https://www.jenkins.io/doc/pipeline/steps/performance/#bzt-run-performance-test)

*   [Performance Publisher plugin](https://www.jenkins.io/doc/pipeline/steps/perfpublisher/)
    *   [`perfpublisher`: Activate PerfPublisher for this project](https://www.jenkins.io/doc/pipeline/steps/perfpublisher/#perfpublisher-activate-perfpublisher-for-this-project)

*   [Performance Signature: Dynatrace](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatracesaas/)
    *   [`createDynatraceDeploymentEvent`: create Dynatrace Deployment event](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatracesaas/#createdynatracedeploymentevent-create-dynatrace-deployment-event)
    *   [`perfSigDynatraceReports`: Performance Signature Dynatrace reports](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatracesaas/#perfsigdynatracereports-performance-signature-dynatrace-reports)
    *   [`recordDynatraceSession`: record Dynatrace Saas/Managed session](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatracesaas/#recorddynatracesession-record-dynatrace-saasmanaged-session)
    *   [`recordDynatraceCustomSession`: record Dynatrace Saas/Managed custom session](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatracesaas/#recorddynatracecustomsession-record-dynatrace-saasmanaged-custom-session)

*   [Performance Signature: Dynatrace AppMon (deprecated)](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatrace/)
    *   [`createDeploymentEvent`: create Dynatrace Deployment event](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatrace/#createdeploymentevent-create-dynatrace-deployment-event)
    *   [`activateDTConfiguration`: activate Dynatrace profile configuration](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatrace/#activatedtconfiguration-activate-dynatrace-profile-configuration)
    *   [`createMemoryDump`: create memory dump](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatrace/#creatememorydump-create-memory-dump)
    *   [`perfSigReports`: Publish Performance Signature reports](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatrace/#perfsigreports-publish-performance-signature-reports)
    *   [`startSession`: Start Dynatrace session recording](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatrace/#startsession-start-dynatrace-session-recording)
    *   [`stopSession`: Stop Dynatrace session recording](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatrace/#stopsession-stop-dynatrace-session-recording)
    *   [`createThreadDump`: create thread dump](https://www.jenkins.io/doc/pipeline/steps/performance-signature-dynatrace/#createthreaddump-create-thread-dump)

*   [Performance Signature: Viewer](https://www.jenkins.io/doc/pipeline/steps/performance-signature-viewer/)
    *   [`pullPerfSigReports`: Pull Performance Signature reports](https://www.jenkins.io/doc/pipeline/steps/performance-signature-viewer/#pullperfsigreports-pull-performance-signature-reports)
    *   [`triggerInputStep`: trigger input step remotely](https://www.jenkins.io/doc/pipeline/steps/performance-signature-viewer/#triggerinputstep-trigger-input-step-remotely)

*   [Phabricator Differential Plugin](https://www.jenkins.io/doc/pipeline/steps/phabricator-plugin/)
    *   [`step([$class: 'PhabricatorNotifier'])`: Post to Phabricator](https://www.jenkins.io/doc/pipeline/steps/phabricator-plugin/#stepclass-phabricatornotifier-post-to-phabricator)

*   [piketec-tpt](https://www.jenkins.io/doc/pipeline/steps/piketec-tpt/)
    *   [`tptReport`: TPT Report](https://www.jenkins.io/doc/pipeline/steps/piketec-tpt/#tptreport-tpt-report)
    *   [`tptExecute`: Execute TPT test cases](https://www.jenkins.io/doc/pipeline/steps/piketec-tpt/#tptexecute-execute-tpt-test-cases)
    *   [`tptAgent`: Execute TPT tests as a worker for a TPT distributing job](https://www.jenkins.io/doc/pipeline/steps/piketec-tpt/#tptagent-execute-tpt-tests-as-a-worker-for-a-tpt-distributing-job)

*   [PingCode Plugin](https://www.jenkins.io/doc/pipeline/steps/worktile/)
    *   [`pingcodeBuildRecord`: Send build result to pingcode](https://www.jenkins.io/doc/pipeline/steps/worktile/#pingcodebuildrecord-send-build-result-to-pingcode)
    *   [`pingcodeDeployRecord`: Send deploy result to pingcode](https://www.jenkins.io/doc/pipeline/steps/worktile/#pingcodedeployrecord-send-deploy-result-to-pingcode)
    *   [`step([$class: 'PCBuildNotifier'])`: PingCode: create build record](https://www.jenkins.io/doc/pipeline/steps/worktile/#stepclass-pcbuildnotifier-pingcode-create-build-record)
    *   [`step([$class: 'PCDeployNotifier'])`: PingCode: create deploy record](https://www.jenkins.io/doc/pipeline/steps/worktile/#stepclass-pcdeploynotifier-pingcode-create-deploy-record)
    *   [`step([$class: 'WTBuildNotifier'])`: Worktile: create build record](https://www.jenkins.io/doc/pipeline/steps/worktile/#stepclass-wtbuildnotifier-worktile-create-build-record)
    *   [`step([$class: 'WTDeployNotifier'])`: Worktile: create deploy record](https://www.jenkins.io/doc/pipeline/steps/worktile/#stepclass-wtdeploynotifier-worktile-create-deploy-record)
    *   [`worktileBuildRecord`: Send build result to worktile](https://www.jenkins.io/doc/pipeline/steps/worktile/#worktilebuildrecord-send-build-result-to-worktile)
    *   [`worktileDeployRecord`: Send deploy result to worktile](https://www.jenkins.io/doc/pipeline/steps/worktile/#worktiledeployrecord-send-deploy-result-to-worktile)

*   [Pipeline Dependency Walker Plugin](https://www.jenkins.io/doc/pipeline/steps/pipeline-dependency-walker/)
    *   [`walk`: Execute a pipeline task for the job and all its downstream jobs.](https://www.jenkins.io/doc/pipeline/steps/pipeline-dependency-walker/#walk-execute-a-pipeline-task-for-the-job-and-all-its-downstream-jobs)

*   [Pipeline GitHub Notify Step Plugin](https://www.jenkins.io/doc/pipeline/steps/pipeline-githubnotify-step/)
    *   [`githubNotify`: Notifies GitHub of the status of a Pull Request](https://www.jenkins.io/doc/pipeline/steps/pipeline-githubnotify-step/#githubnotify-notifies-github-of-the-status-of-a-pull-request)

*   [Pipeline Graph View Plugin](https://www.jenkins.io/doc/pipeline/steps/pipeline-graph-view/)
    *   [`hideFromView`: Hide from View](https://www.jenkins.io/doc/pipeline/steps/pipeline-graph-view/#hidefromview-hide-from-view)

*   [Pipeline Keep Running Step](https://www.jenkins.io/doc/pipeline/steps/pipeline-keep-running-step/)
    *   [`keepRunning`: Keep the process running even if the build has finished.](https://www.jenkins.io/doc/pipeline/steps/pipeline-keep-running-step/#keeprunning-keep-the-process-running-even-if-the-build-has-finished)

*   [Pipeline Maven Integration Plugin](https://www.jenkins.io/doc/pipeline/steps/pipeline-maven/)
    *   [`withMaven`: Provide Maven environment](https://www.jenkins.io/doc/pipeline/steps/pipeline-maven/#withmaven-provide-maven-environment)

*   [Pipeline NPM Integration Plugin](https://www.jenkins.io/doc/pipeline/steps/pipeline-npm/)
    *   [`withNPM`: Provide NPM environment](https://www.jenkins.io/doc/pipeline/steps/pipeline-npm/#withnpm-provide-npm-environment)

*   [Pipeline Project-Env Plugin](https://www.jenkins.io/doc/pipeline/steps/pipeline-project-env/)
    *   [`withProjectEnv`: WithProjectEnvStep](https://www.jenkins.io/doc/pipeline/steps/pipeline-project-env/#withprojectenv-withprojectenvstep)

*   [Pipeline Utility Steps](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/)
    *   [`compareVersions`: Compare two version number strings](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#compareversions-compare-two-version-number-strings)
    *   [`findFiles`: Find files in the workspace](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#findfiles-find-files-in-the-workspace)
    *   [`md5`: Compute the MD5 of a given file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#md5-compute-the-md5-of-a-given-file)
    *   [`nodesByLabel`: List of nodes by Label, by default excludes offline nodes.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#nodesbylabel-list-of-nodes-by-label-by-default-excludes-offline-nodes)
    *   [`prependToFile`: Create a file (if not already exist) in the workspace, and prepend given content to that file.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#prependtofile-create-a-file-if-not-already-exist-in-the-workspace-and-prepend-given-content-to-that-file)
    *   [`readCSV`: Read content from a CSV file in the workspace or text.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#readcsv-read-content-from-a-csv-file-in-the-workspace-or-text)
    *   [`readJSON`: Read JSON from a file in the workspace or text.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#readjson-read-json-from-a-file-in-the-workspace-or-text)
    *   [`readManifest`: Read a Jar Manifest](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#readmanifest-read-a-jar-manifest)
    *   [`readMavenPom`: Read a maven project file.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#readmavenpom-read-a-maven-project-file)
    *   [`readProperties`: Read properties from a file in the workspace or text.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#readproperties-read-properties-from-a-file-in-the-workspace-or-text)
    *   [`readTOML`: Read toml from a file in the workspace or text.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#readtoml-read-toml-from-a-file-in-the-workspace-or-text)
    *   [`readYaml`: Read yaml from a file in the workspace or text.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#readyaml-read-yaml-from-a-file-in-the-workspace-or-text)
    *   [`sha1`: Compute the SHA1 of a given file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#sha1-compute-the-sha1-of-a-given-file)
    *   [`sha256`: Compute the SHA256 of a given file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#sha256-compute-the-sha256-of-a-given-file)
    *   [`tar`: Create Tar file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#tar-create-tar-file)
    *   [`tee`: Tee output to file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#tee-tee-output-to-file)
    *   [`touch`: Create a file (if not already exist) in the workspace, and set the timestamp](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#touch-create-a-file-if-not-already-exist-in-the-workspace-and-set-the-timestamp)
    *   [`untar`: Extract Tar file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#untar-extract-tar-file)
    *   [`unzip`: Extract Zip file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#unzip-extract-zip-file)
    *   [`verifyMd5`: Verify the MD5 of a given file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#verifymd5-verify-the-md5-of-a-given-file)
    *   [`verifySha1`: Verify the SHA1 of a given file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#verifysha1-verify-the-sha1-of-a-given-file)
    *   [`verifySha256`: Verify the SHA256 of a given file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#verifysha256-verify-the-sha256-of-a-given-file)
    *   [`writeCSV`: Write content to a CSV file in the workspace.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#writecsv-write-content-to-a-csv-file-in-the-workspace)
    *   [`writeJSON`: Write JSON to a file in the workspace.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#writejson-write-json-to-a-file-in-the-workspace)
    *   [`writeMavenPom`: Write a maven project file.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#writemavenpom-write-a-maven-project-file)
    *   [`writeTOML`: Write toml to a file in the workspace.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#writetoml-write-toml-to-a-file-in-the-workspace)
    *   [`writeYaml`: Write a yaml from an object or objects.](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#writeyaml-write-a-yaml-from-an-object-or-objects)
    *   [`zip`: Create Zip file](https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#zip-create-zip-file)

*   [Pipeline: AWS Steps](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/)
    *   [`awaitDeploymentCompletion`: Wait for AWS CodeDeploy deployment completion](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#awaitdeploymentcompletion-wait-for-aws-codedeploy-deployment-completion)
    *   [`awsIdentity`: Print and return the AWS identity](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#awsidentity-print-and-return-the-aws-identity)
    *   [`cfInvalidate`: Invalidate given paths in CloudFront distribution](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#cfinvalidate-invalidate-given-paths-in-cloudfront-distribution)
    *   [`cfnCreateChangeSet`: Create CloudFormation change set](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#cfncreatechangeset-create-cloudformation-change-set)
    *   [`cfnDelete`: Delete CloudFormation stack](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#cfndelete-delete-cloudformation-stack)
    *   [`cfnDeleteStackSet`: Delete CloudFormation Stack Set](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#cfndeletestackset-delete-cloudformation-stack-set)
    *   [`cfnDescribe`: Describe outputs of CloudFormation stack](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#cfndescribe-describe-outputs-of-cloudformation-stack)
    *   [`cfnExecuteChangeSet`: Execute CloudFormation change set](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#cfnexecutechangeset-execute-cloudformation-change-set)
    *   [`cfnExports`: Describe CloudFormation global exports](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#cfnexports-describe-cloudformation-global-exports)
    *   [`cfnUpdate`: Create or Update CloudFormation stack](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#cfnupdate-create-or-update-cloudformation-stack)
    *   [`cfnUpdateStackSet`: Create or Update CloudFormation Stack Set](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#cfnupdatestackset-create-or-update-cloudformation-stack-set)
    *   [`cfnValidate`: Validate CloudFormation template](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#cfnvalidate-validate-cloudformation-template)
    *   [`createDeployment`: Deploys an application revision through the specified deployment group (AWS CodeDeploy).](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#createdeployment-deploys-an-application-revision-through-the-specified-deployment-group-aws-codedeploy)
    *   [`deployAPI`: Deploy the given API Gateway API](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#deployapi-deploy-the-given-api-gateway-api)
    *   [`ebCreateApplication`: Creates a new Elastic Beanstalk application](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ebcreateapplication-creates-a-new-elastic-beanstalk-application)
    *   [`ebCreateApplicationVersion`: Creates a new version for an elastic beanstalk application](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ebcreateapplicationversion-creates-a-new-version-for-an-elastic-beanstalk-application)
    *   [`ebCreateConfigurationTemplate`: Creates a new configuration template for an elastic beanstalk application](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ebcreateconfigurationtemplate-creates-a-new-configuration-template-for-an-elastic-beanstalk-application)
    *   [`ebCreateEnvironment`: Creates a new Elastic Beanstalk environment](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ebcreateenvironment-creates-a-new-elastic-beanstalk-environment)
    *   [`ebSwapEnvironmentCNAMEs`: Swaps the CNAMEs of two elastic beanstalk environments.](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ebswapenvironmentcnames-swaps-the-cnames-of-two-elastic-beanstalk-environments)
    *   [`ebWaitOnEnvironmentHealth`: Waits until the specified environment application becomes available](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ebwaitonenvironmenthealth-waits-until-the-specified-environment-application-becomes-available)
    *   [`ebWaitOnEnvironmentStatus`: Waits until the specified environment becomes available](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ebwaitonenvironmentstatus-waits-until-the-specified-environment-becomes-available)
    *   [`ec2ShareAmi`: Share an AMI with other accounts](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ec2shareami-share-an-ami-with-other-accounts)
    *   [`ecrDeleteImage`: Delete ecr images](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ecrdeleteimage-delete-ecr-images)
    *   [`ecrListImages`: List ECR Images](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ecrlistimages-list-ecr-images)
    *   [`ecrLogin`: Create and return the ECR login string](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ecrlogin-create-and-return-the-ecr-login-string)
    *   [`ecrSetRepositoryPolicy`: Set ECR Repository Policy](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#ecrsetrepositorypolicy-set-ecr-repository-policy)
    *   [`elbDeregisterInstance`: Deregisters the specified instances from the specified load balancer.](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#elbderegisterinstance-deregisters-the-specified-instances-from-the-specified-load-balancer)
    *   [`elbIsInstanceDeregistered`: Registers the specified instances from the specified load balancer.](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#elbisinstancederegistered-registers-the-specified-instances-from-the-specified-load-balancer)
    *   [`elbIsInstanceRegistered`: Registers the specified instances from the specified load balancer.](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#elbisinstanceregistered-registers-the-specified-instances-from-the-specified-load-balancer)
    *   [`elbRegisterInstance`: Registers the specified instances from the specified load balancer.](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#elbregisterinstance-registers-the-specified-instances-from-the-specified-load-balancer)
    *   [`invokeLambda`: Invoke a given Lambda function](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#invokelambda-invoke-a-given-lambda-function)
    *   [`lambdaVersionCleanup`: Cleanup old lambda versions](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#lambdaversioncleanup-cleanup-old-lambda-versions)
    *   [`listAWSAccounts`: List all AWS accounts of the organization](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#listawsaccounts-list-all-aws-accounts-of-the-organization)
    *   [`s3Copy`: Copy file between S3 buckets](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#s3copy-copy-file-between-s3-buckets)
    *   [`s3Delete`: Delete file from S3](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#s3delete-delete-file-from-s3)
    *   [`s3DoesObjectExist`: Check if object exists in S3](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#s3doesobjectexist-check-if-object-exists-in-s3)
    *   [`s3Download`: Copy file from S3](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#s3download-copy-file-from-s3)
    *   [`s3FindFiles`: Find files in S3](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#s3findfiles-find-files-in-s3)
    *   [`s3PresignURL`: Presign file in S3](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#s3presignurl-presign-file-in-s3)
    *   [`s3Upload`: Copy file to S3](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#s3upload-copy-file-to-s3)
    *   [`setAccountAlias`: Set the AWS account alias](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#setaccountalias-set-the-aws-account-alias)
    *   [`snsPublish`: Publish notification to SNS](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#snspublish-publish-notification-to-sns)
    *   [`updateIdP`: Update thirdparty Identity Provider](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#updateidp-update-thirdparty-identity-provider)
    *   [`updateTrustPolicy`: Update trust policy of IAM roles](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#updatetrustpolicy-update-trust-policy-of-iam-roles)
    *   [`withAWS`: set AWS settings for nested block](https://www.jenkins.io/doc/pipeline/steps/pipeline-aws/#withaws-set-aws-settings-for-nested-block)

*   [Pipeline: Bamboo Step](https://www.jenkins.io/doc/pipeline/steps/pipeline-bamboo/)
    *   [`buildBamboo`: Build Bamboo](https://www.jenkins.io/doc/pipeline/steps/pipeline-bamboo/#buildbamboo-build-bamboo)

*   [Pipeline: Basic Steps](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/)
    *   [`catchError`: Catch error and set build result to failure](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#catcherror-catch-error-and-set-build-result-to-failure)
    *   [`deleteDir`: Recursively delete the current directory from the workspace](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#deletedir-recursively-delete-the-current-directory-from-the-workspace)
    *   [`echo`: Print Message](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#echo-print-message)
    *   [`error`: Error signal](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#error-error-signal)
    *   [`fileExists`: Verify if file exists in workspace](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#fileexists-verify-if-file-exists-in-workspace)
    *   [`isUnix`: Checks if running on a Unix-like node](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#isunix-checks-if-running-on-a-unix-like-node)
    *   [`mail`: Mail](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#mail-mail)
    *   [`pwd`: Determine current directory](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#pwd-determine-current-directory)
    *   [`readFile`: Read file from workspace](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#readfile-read-file-from-workspace)
    *   [`retry`: Retry the body up to N times](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#retry-retry-the-body-up-to-n-times)
    *   [`sleep`: Sleep](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#sleep-sleep)
    *   [`stash`: Stash some files to be used later in the build](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#stash-stash-some-files-to-be-used-later-in-the-build)
    *   [`step`: General Build Step](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#step-general-build-step)
    *   [`timeout`: Enforce time limit](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#timeout-enforce-time-limit)
    *   [`tool`: Use a tool from a predefined Tool Installation](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#tool-use-a-tool-from-a-predefined-tool-installation)
    *   [`unstable`: Set stage result to unstable](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#unstable-set-stage-result-to-unstable)
    *   [`unstash`: Restore files previously stashed](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#unstash-restore-files-previously-stashed)
    *   [`waitUntil`: Wait for condition](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#waituntil-wait-for-condition)
    *   [`warnError`: Catch error and set build and stage result to unstable](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#warnerror-catch-error-and-set-build-and-stage-result-to-unstable)
    *   [`withEnv`: Set environment variables](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#withenv-set-environment-variables)
    *   [`wrap`: General Build Wrapper](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#wrap-general-build-wrapper)
    *   [`writeFile`: Write file to workspace](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#writefile-write-file-to-workspace)
    *   [`archive`: Archive artifacts](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#archive-archive-artifacts)
    *   [`getContext`: Get contextual object from internal APIs](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#getcontext-get-contextual-object-from-internal-apis)
    *   [`unarchive`: Copy archived artifacts into the workspace](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#unarchive-copy-archived-artifacts-into-the-workspace)
    *   [`withContext`: Use contextual object from internal APIs within a block](https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#withcontext-use-contextual-object-from-internal-apis-within-a-block)

*   [Pipeline: Build Step](https://www.jenkins.io/doc/pipeline/steps/pipeline-build-step/)
    *   [`build`: Build a job](https://www.jenkins.io/doc/pipeline/steps/pipeline-build-step/#build-build-a-job)
    *   [`waitForBuild`: Wait for build to complete](https://www.jenkins.io/doc/pipeline/steps/pipeline-build-step/#waitforbuild-wait-for-build-to-complete)

*   [Pipeline: Declarative](https://www.jenkins.io/doc/pipeline/steps/pipeline-model-definition/)
    *   [`script`: Run arbitrary Pipeline script](https://www.jenkins.io/doc/pipeline/steps/pipeline-model-definition/#script-run-arbitrary-pipeline-script)
    *   [`validateDeclarativePipeline`: Validate a file containing a Declarative Pipeline](https://www.jenkins.io/doc/pipeline/steps/pipeline-model-definition/#validatedeclarativepipeline-validate-a-file-containing-a-declarative-pipeline)
    *   [`envVarsForTool`: Fetches the environment variables for a given tool in a list of 'FOO=bar' strings suitable for the withEnv step.](https://www.jenkins.io/doc/pipeline/steps/pipeline-model-definition/#envvarsfortool-fetches-the-environment-variables-for-a-given-tool-in-a-list-of-foobar-strings-suitable-for-the-withenv-step)

*   [Pipeline: Deploymon.io Steps](https://www.jenkins.io/doc/pipeline/steps/pipeline-deploymon/)
    *   [`notifyDeploymon`: Notify deploymon.io about a new deployment](https://www.jenkins.io/doc/pipeline/steps/pipeline-deploymon/#notifydeploymon-notify-deploymon-io-about-a-new-deployment)

*   [Pipeline: GCP Steps](https://www.jenkins.io/doc/pipeline/steps/pipeline-gcp/)
    *   [`computeFirewallRulesCreate`: Create a firewall rule](https://www.jenkins.io/doc/pipeline/steps/pipeline-gcp/#computefirewallrulescreate-create-a-firewall-rule)
    *   [`computeFirewallRulesDelete`: Delete a firewall rule](https://www.jenkins.io/doc/pipeline/steps/pipeline-gcp/#computefirewallrulesdelete-delete-a-firewall-rule)
    *   [`computeFirewallRulesList`: List firewall rules](https://www.jenkins.io/doc/pipeline/steps/pipeline-gcp/#computefirewallruleslist-list-firewall-rules)
    *   [`withGCP`: Set GCP credentials for nested block](https://www.jenkins.io/doc/pipeline/steps/pipeline-gcp/#withgcp-set-gcp-credentials-for-nested-block)

*   [Pipeline: Groovy](https://www.jenkins.io/doc/pipeline/steps/workflow-cps/)
    *   [`load`: Evaluate a Groovy source file into the Pipeline script](https://www.jenkins.io/doc/pipeline/steps/workflow-cps/#load-evaluate-a-groovy-source-file-into-the-pipeline-script)
    *   [`parallel`: Execute in parallel](https://www.jenkins.io/doc/pipeline/steps/workflow-cps/#parallel-execute-in-parallel)

*   [Pipeline: Groovy Libraries](https://www.jenkins.io/doc/pipeline/steps/pipeline-groovy-lib/)
    *   [`library`: Load a library on the fly](https://www.jenkins.io/doc/pipeline/steps/pipeline-groovy-lib/#library-load-a-library-on-the-fly)
    *   [`libraryResource`: Load a resource file from a library](https://www.jenkins.io/doc/pipeline/steps/pipeline-groovy-lib/#libraryresource-load-a-resource-file-from-a-library)

*   [Pipeline: HuaweiCloud Steps](https://www.jenkins.io/doc/pipeline/steps/pipeline-huaweicloud-plugin/)
    *   [`invokeFunction`: Invoke a given function](https://www.jenkins.io/doc/pipeline/steps/pipeline-huaweicloud-plugin/#invokefunction-invoke-a-given-function)
    *   [`obsUpload`: Copy file to obs](https://www.jenkins.io/doc/pipeline/steps/pipeline-huaweicloud-plugin/#obsupload-copy-file-to-obs)
    *   [`withOBS`: set OBS settings for nested block](https://www.jenkins.io/doc/pipeline/steps/pipeline-huaweicloud-plugin/#withobs-set-obs-settings-for-nested-block)

*   [Pipeline: Input Step](https://www.jenkins.io/doc/pipeline/steps/pipeline-input-step/)
    *   [`input`: Wait for interactive input](https://www.jenkins.io/doc/pipeline/steps/pipeline-input-step/#input-wait-for-interactive-input)

*   [Pipeline: Keep Environment Step Plugin](https://www.jenkins.io/doc/pipeline/steps/pipeline-keepenv-step/)
    *   [`keepEnv`: Keep only specified environment variables](https://www.jenkins.io/doc/pipeline/steps/pipeline-keepenv-step/#keepenv-keep-only-specified-environment-variables)

*   [Pipeline: Milestone Step](https://www.jenkins.io/doc/pipeline/steps/pipeline-milestone-step/)
    *   [`milestone`: The milestone step forces all builds to go through in order](https://www.jenkins.io/doc/pipeline/steps/pipeline-milestone-step/#milestone-the-milestone-step-forces-all-builds-to-go-through-in-order)

*   [Pipeline: Multibranch](https://www.jenkins.io/doc/pipeline/steps/workflow-multibranch/)
    *   [`properties`: Set job properties](https://www.jenkins.io/doc/pipeline/steps/workflow-multibranch/#properties-set-job-properties)
    *   [`readTrusted`: Read trusted file from SCM](https://www.jenkins.io/doc/pipeline/steps/workflow-multibranch/#readtrusted-read-trusted-file-from-scm)
    *   [`resolveScm`: Resolves an SCM from an SCM Source and a list of candidate target branch names](https://www.jenkins.io/doc/pipeline/steps/workflow-multibranch/#resolvescm-resolves-an-scm-from-an-scm-source-and-a-list-of-candidate-target-branch-names)

*   [Pipeline: Nodes and Processes](https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/)
    *   [`bat`: Windows Batch Script](https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#bat-windows-batch-script)
    *   [`dir`: Change current directory](https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#dir-change-current-directory)
    *   [`node`: Allocate node](https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#node-allocate-node)
    *   [`powershell`: Windows PowerShell Script](https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#powershell-windows-powershell-script)
    *   [`pwsh`: PowerShell Core Script](https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#pwsh-powershell-core-script)
    *   [`sh`: Shell Script](https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#sh-shell-script)
    *   [`ws`: Allocate workspace](https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#ws-allocate-workspace)

*   [Pipeline: SCM Step](https://www.jenkins.io/doc/pipeline/steps/workflow-scm-step/)
    *   [`checkout`: Check out from version control](https://www.jenkins.io/doc/pipeline/steps/workflow-scm-step/#checkout-check-out-from-version-control)
    *   [`readScmFile`: Read file from SCM](https://www.jenkins.io/doc/pipeline/steps/workflow-scm-step/#readscmfile-read-file-from-scm)

*   [Pipeline: Stage Step](https://www.jenkins.io/doc/pipeline/steps/pipeline-stage-step/)
    *   [`stage`: Stage](https://www.jenkins.io/doc/pipeline/steps/pipeline-stage-step/#stage-stage)

*   [PIT Mutation Plugin](https://www.jenkins.io/doc/pipeline/steps/pitmutation/)
    *   [`pitmutation`: Record Pit mutation testing report](https://www.jenkins.io/doc/pipeline/steps/pitmutation/#pitmutation-record-pit-mutation-testing-report)

*   [PlasticSCM Plugin](https://www.jenkins.io/doc/pipeline/steps/plasticscm-plugin/)
    *   [`cm`: Plastic SCM](https://www.jenkins.io/doc/pipeline/steps/plasticscm-plugin/#cm-plastic-scm)
    *   [`mergebotCheckout`: Plastic SCM Mergebot Checkout](https://www.jenkins.io/doc/pipeline/steps/plasticscm-plugin/#mergebotcheckout-plastic-scm-mergebot-checkout)

*   [Plot plugin](https://www.jenkins.io/doc/pipeline/steps/plot/)
    *   [`plot`: Plot build data](https://www.jenkins.io/doc/pipeline/steps/plot/#plot-plot-build-data)

*   [Port scanner Plugin](https://www.jenkins.io/doc/pipeline/steps/portscanner/)
    *   [`step([$class: 'PortScannerStep'])`: Port scanner](https://www.jenkins.io/doc/pipeline/steps/portscanner/#stepclass-portscannerstep-port-scanner)

*   [Pragprog Plugin](https://www.jenkins.io/doc/pipeline/steps/pragprog/)
    *   [`pragprog`: Activate tips from The Pragmatic Programmer](https://www.jenkins.io/doc/pipeline/steps/pragprog/#pragprog-activate-tips-from-the-pragmatic-programmer)
    *   [`step([$class: 'PragprogBuildStep'])`: Activate tips from The Pragmatic Programmer](https://www.jenkins.io/doc/pipeline/steps/pragprog/#stepclass-pragprogbuildstep-activate-tips-from-the-pragmatic-programmer)

*   [PreFlight](https://www.jenkins.io/doc/pipeline/steps/preflight-integration/)
    *   [`step([$class: 'PreflightBuilder'])`: Run PreFlight Test](https://www.jenkins.io/doc/pipeline/steps/preflight-integration/#stepclass-preflightbuilder-run-preflight-test)

*   [Pretested Integration Plugin](https://www.jenkins.io/doc/pipeline/steps/pretested-integration/)
    *   [`pretestedIntegrationPublisher`: Pretested Integration publisher to push to integration branch](https://www.jenkins.io/doc/pipeline/steps/pretested-integration/#pretestedintegrationpublisher-pretested-integration-publisher-to-push-to-integration-branch)

*   [Prisma Cloud IaC Scan Plugin](https://www.jenkins.io/doc/pipeline/steps/prisma-cloud-iac-scan/)
    *   [`prismaIaC`: Prisma Cloud IaC Scan](https://www.jenkins.io/doc/pipeline/steps/prisma-cloud-iac-scan/#prismaiac-prisma-cloud-iac-scan)

*   [Probely Security Scanner Plugin](https://www.jenkins.io/doc/pipeline/steps/probely-security/)
    *   [`probelyScan`: Probely Security Scanner](https://www.jenkins.io/doc/pipeline/steps/probely-security/#probelyscan-probely-security-scanner)

*   [Progress MobileStudio Plugin](https://www.jenkins.io/doc/pipeline/steps/teststudiomobiletesting/)
    *   [`step([$class: 'MobileStudioTestBuilder'])`: Mobile Studio runner configuration](https://www.jenkins.io/doc/pipeline/steps/teststudiomobiletesting/#stepclass-mobilestudiotestbuilder-mobile-studio-runner-configuration)

*   [Progress TestStudio for API Plugin](https://www.jenkins.io/doc/pipeline/steps/teststudioapitesting/)
    *   [`step([$class: 'TestStudioAPITestBuilder'])`: Test Studio for API runner configuration](https://www.jenkins.io/doc/pipeline/steps/teststudioapitesting/#stepclass-teststudioapitestbuilder-test-studio-for-api-runner-configuration)

*   [Progress TestStudio Plugin](https://www.jenkins.io/doc/pipeline/steps/teststudio/)
    *   [`step([$class: 'TestStudioTestBuilder'])`: Test Studio runner configuration](https://www.jenkins.io/doc/pipeline/steps/teststudio/#stepclass-teststudiotestbuilder-test-studio-runner-configuration)

*   [Propelo’s Job Reporter](https://www.jenkins.io/doc/pipeline/steps/propelo-job-reporter/)
    *   [`step([$class: 'LevelOpsPostBuildPublisher'])`: Propelo Job Reporter Plugin](https://www.jenkins.io/doc/pipeline/steps/propelo-job-reporter/#stepclass-levelopspostbuildpublisher-propelo-job-reporter-plugin)

*   [Provar Automation CLI](https://www.jenkins.io/doc/pipeline/steps/provar-automation/)
    *   [`withProvarAutomation`: With Provar Automation](https://www.jenkins.io/doc/pipeline/steps/provar-automation/#withprovarautomation-with-provar-automation)

*   [PTC RV&S CM - Jenkins Plugin](https://www.jenkins.io/doc/pipeline/steps/integrity-plugin/)
    *   [`siaddprojectlabel`: PTC RV&S SCM Label](https://www.jenkins.io/doc/pipeline/steps/integrity-plugin/#siaddprojectlabel-ptc-rvs-scm-label)
    *   [`sicheckpoint`: PTC RV&S SCM Checkpoint](https://www.jenkins.io/doc/pipeline/steps/integrity-plugin/#sicheckpoint-ptc-rvs-scm-checkpoint)
    *   [`sici`: PTC RV&S SCM Checkin](https://www.jenkins.io/doc/pipeline/steps/integrity-plugin/#sici-ptc-rvs-scm-checkin)

*   [Publish Over CIFS](https://www.jenkins.io/doc/pipeline/steps/publish-over-cifs/)
    *   [`step([$class: 'CifsPromotionPublisherPlugin'])`: Send build artifacts to a windows share](https://www.jenkins.io/doc/pipeline/steps/publish-over-cifs/#stepclass-cifspromotionpublisherplugin-send-build-artifacts-to-a-windows-share)
    *   [`cifsPublisher`: Send build artifacts to a windows share](https://www.jenkins.io/doc/pipeline/steps/publish-over-cifs/#cifspublisher-send-build-artifacts-to-a-windows-share)

*   [Publish Over Dropbox](https://www.jenkins.io/doc/pipeline/steps/publish-over-dropbox/)
    *   [`dropbox`: Publish to Dropbox folder](https://www.jenkins.io/doc/pipeline/steps/publish-over-dropbox/#dropbox-publish-to-dropbox-folder)
    *   [`step([$class: 'DropboxPublisherPlugin'])`: Send build artifacts over Dropbox](https://www.jenkins.io/doc/pipeline/steps/publish-over-dropbox/#stepclass-dropboxpublisherplugin-send-build-artifacts-over-dropbox)

*   [Publish Over FTP](https://www.jenkins.io/doc/pipeline/steps/publish-over-ftp/)
    *   [`step([$class: 'BapFtpPromotionPublisherPlugin'])`: Send build artifacts over FTP](https://www.jenkins.io/doc/pipeline/steps/publish-over-ftp/#stepclass-bapftppromotionpublisherplugin-send-build-artifacts-over-ftp)
    *   [`ftpPublisher`: Send build artifacts over FTP](https://www.jenkins.io/doc/pipeline/steps/publish-over-ftp/#ftppublisher-send-build-artifacts-over-ftp)

*   [Publish Over SSH](https://www.jenkins.io/doc/pipeline/steps/publish-over-ssh/)
    *   [`step([$class: 'BapSshPromotionPublisherPlugin'])`: Send build artifacts over SSH](https://www.jenkins.io/doc/pipeline/steps/publish-over-ssh/#stepclass-bapsshpromotionpublisherplugin-send-build-artifacts-over-ssh)
    *   [`sshPublisher`: Send build artifacts over SSH](https://www.jenkins.io/doc/pipeline/steps/publish-over-ssh/#sshpublisher-send-build-artifacts-over-ssh)

*   [Publish to Bitbucket Plugin](https://www.jenkins.io/doc/pipeline/steps/publish-to-bitbucket/)
    *   [`step([$class: 'BitbucketPublisher'])`: Publish to Bitbucket Server](https://www.jenkins.io/doc/pipeline/steps/publish-to-bitbucket/#stepclass-bitbucketpublisher-publish-to-bitbucket-server)

*   [Pull Request Monitoring](https://www.jenkins.io/doc/pipeline/steps/pull-request-monitoring/)
    *   [`monitoring`: Configure Monitoring Dashboard](https://www.jenkins.io/doc/pipeline/steps/pull-request-monitoring/#monitoring-configure-monitoring-dashboard)

*   [PureLoad Plugin](https://www.jenkins.io/doc/pipeline/steps/pureload/)
    *   [`publishPureLoad`: Publish PureLoad Results](https://www.jenkins.io/doc/pipeline/steps/pureload/#publishpureload-publish-pureload-results)

*   [Pyenv Pipeline Plugin](https://www.jenkins.io/doc/pipeline/steps/pyenv-pipeline/)
    *   [`pybat`: PyEnvVar Batch Script](https://www.jenkins.io/doc/pipeline/steps/pyenv-pipeline/#pybat-pyenvvar-batch-script)
    *   [`pysh`: PyEnvVar Shell Script](https://www.jenkins.io/doc/pipeline/steps/pyenv-pipeline/#pysh-pyenvvar-shell-script)
    *   [`withPythonEnv`: Code Block](https://www.jenkins.io/doc/pipeline/steps/pyenv-pipeline/#withpythonenv-code-block)

*   [QF-Test Plugin](https://www.jenkins.io/doc/pipeline/steps/qftest/)
    *   [`QFTest`: Run the configured QF-Test suites.](https://www.jenkins.io/doc/pipeline/steps/qftest/#qftest-run-the-configured-qf-test-suites)

*   [Qiniu](https://www.jenkins.io/doc/pipeline/steps/qiniu/)
    *   [`archiveArtifactsToQiniu`: Archive the artifacts to Qiniu](https://www.jenkins.io/doc/pipeline/steps/qiniu/#archiveartifactstoqiniu-archive-the-artifacts-to-qiniu)

*   [QMetry for JIRA - Test Management Plugin](https://www.jenkins.io/doc/pipeline/steps/qmetry-for-jira-test-management/)
    *   [`step([$class: 'QTM4JResultPublisher'])`: Publish test result to QMetry for JIRA Old](https://www.jenkins.io/doc/pipeline/steps/qmetry-for-jira-test-management/#stepclass-qtm4jresultpublisher-publish-test-result-to-qmetry-for-jira-old)
    *   [`step([$class: 'TestReportDeployPublisher'])`: Publish results to QMetry for Jira version 3.X below](https://www.jenkins.io/doc/pipeline/steps/qmetry-for-jira-test-management/#stepclass-testreportdeploypublisher-publish-results-to-qmetry-for-jira-version-3-x-below)
    *   [`step([$class: 'TestReportDeployPublisherCloudV4'])`: Publish results to QMetry for Jira version 4.X above](https://www.jenkins.io/doc/pipeline/steps/qmetry-for-jira-test-management/#stepclass-testreportdeploypublishercloudv4-publish-results-to-qmetry-for-jira-version-4-x-above)

*   [QMetry Test Management Plugin](https://www.jenkins.io/doc/pipeline/steps/qmetry-test-management/)
    *   [`step([$class: 'QTMReportPublisher'])`: Publish Build Result(s) to QMetry Test Management](https://www.jenkins.io/doc/pipeline/steps/qmetry-test-management/#stepclass-qtmreportpublisher-publish-build-results-to-qmetry-test-management)

*   [QRebel Plugin](https://www.jenkins.io/doc/pipeline/steps/qrebel/)
    *   [`qrebel`: Monitor performance regressions with QRebel](https://www.jenkins.io/doc/pipeline/steps/qrebel/#qrebel-monitor-performance-regressions-with-qrebel)

*   [qTest Plugin](https://www.jenkins.io/doc/pipeline/steps/qtest/)
    *   [`submitJUnitTestResultsToqTest`: Submit jUnit test result to qTest](https://www.jenkins.io/doc/pipeline/steps/qtest/#submitjunittestresultstoqtest-submit-junit-test-result-to-qtest)

*   [Quali Torque plugin](https://www.jenkins.io/doc/pipeline/steps/quali-torque/)
    *   [`endTorqueSandboxEnvironment`: "End Environment"](https://www.jenkins.io/doc/pipeline/steps/quali-torque/#endtorquesandboxenvironment-end-environment)
    *   [`startTorqueSandboxEnvironment`: "Start Environment"](https://www.jenkins.io/doc/pipeline/steps/quali-torque/#starttorquesandboxenvironment-start-environment)
    *   [`waitForTorqueSandboxEnvironment`: "Wait for environment"](https://www.jenkins.io/doc/pipeline/steps/quali-torque/#waitfortorquesandboxenvironment-wait-for-environment)

*   [Quality Clouds Scan Plugin](https://www.jenkins.io/doc/pipeline/steps/qualityclouds/)
    *   [`qualityCloudsScan`: Quality Clouds Instance Scan](https://www.jenkins.io/doc/pipeline/steps/qualityclouds/#qualitycloudsscan-quality-clouds-instance-scan)

*   [Qualys Container Scanning Connector](https://www.jenkins.io/doc/pipeline/steps/qualys-cs/)
    *   [`getImageVulnsFromQualys`: Scan container images with Qualys CS](https://www.jenkins.io/doc/pipeline/steps/qualys-cs/#getimagevulnsfromqualys-scan-container-images-with-qualys-cs)

*   [Qualys Host Scanning Connector](https://www.jenkins.io/doc/pipeline/steps/qualys-vm/)
    *   [`qualysVulnerabilityAnalyzer`: Scan host/instances with Qualys VM](https://www.jenkins.io/doc/pipeline/steps/qualys-vm/#qualysvulnerabilityanalyzer-scan-hostinstances-with-qualys-vm)

*   [Qualys IaC Security](https://www.jenkins.io/doc/pipeline/steps/qualys-iac-security/)
    *   [`qualysIaCScan`: Qualys IaC Scan](https://www.jenkins.io/doc/pipeline/steps/qualys-iac-security/#qualysiacscan-qualys-iac-scan)
    *   [`step([$class: 'TemplateScanBuilder'])`: Qualys IaC Scan](https://www.jenkins.io/doc/pipeline/steps/qualys-iac-security/#stepclass-templatescanbuilder-qualys-iac-scan)

*   [Qualys Policy Compliance Scanning Connector](https://www.jenkins.io/doc/pipeline/steps/qualys-pc/)
    *   [`qualysPolicyComplianceScanner`: Scan host/instances with Qualys PC](https://www.jenkins.io/doc/pipeline/steps/qualys-pc/#qualyspolicycompliancescanner-scan-hostinstances-with-qualys-pc)

*   [Qualys Web App Scanning Connector](https://www.jenkins.io/doc/pipeline/steps/qualys-was/)
    *   [`qualysWASScan`: Scan web applications with Qualys WAS](https://www.jenkins.io/doc/pipeline/steps/qualys-was/#qualyswasscan-scan-web-applications-with-qualys-was)
    *   [`step([$class: 'WASScanNotifier'])`: Scan web applications with Qualys WAS](https://www.jenkins.io/doc/pipeline/steps/qualys-was/#stepclass-wasscannotifier-scan-web-applications-with-qualys-was)

*   [Quay Tag Parameter Plugin](https://www.jenkins.io/doc/pipeline/steps/quay-tag-parameter/)
    *   [`quayImage`: Get Quay.io Image Reference](https://www.jenkins.io/doc/pipeline/steps/quay-tag-parameter/#quayimage-get-quay-io-image-reference)

*   [Questa VRM](https://www.jenkins.io/doc/pipeline/steps/mentor-questa-vrm/)
    *   [`questavrm`: Publish Questa VRM Regression Results](https://www.jenkins.io/doc/pipeline/steps/mentor-questa-vrm/#questavrm-publish-questa-vrm-regression-results)

*   [Qy Wechat Notification Plugin](https://www.jenkins.io/doc/pipeline/steps/qy-wechat-notification/)
    *   [`qyWechatNotification`: 企业微信通知](https://www.jenkins.io/doc/pipeline/steps/qy-wechat-notification/#qywechatnotification-%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E9%80%9A%E7%9F%A5)

*   [R Plugin](https://www.jenkins.io/doc/pipeline/steps/r/)
    *   [`r`: Execute R script](https://www.jenkins.io/doc/pipeline/steps/r/#r-execute-r-script)

*   [Rabbit-MQ Publisher Plugin](https://www.jenkins.io/doc/pipeline/steps/rabbitmq-publisher/)
    *   [`rabbitMQPublisher`: Publish to Rabbit-MQ](https://www.jenkins.io/doc/pipeline/steps/rabbitmq-publisher/#rabbitmqpublisher-publish-to-rabbit-mq)

*   [RadarGun Reporting Plugin](https://www.jenkins.io/doc/pipeline/steps/radargun-reporting/)
    *   [`radargunreporting`: Report RadarGun Performance Test](https://www.jenkins.io/doc/pipeline/steps/radargun-reporting/#radargunreporting-report-radargun-performance-test)
    *   [`step([$class: 'RadarGunPublisher'])`: Report Performance Test Results (RadarGun)](https://www.jenkins.io/doc/pipeline/steps/radargun-reporting/#stepclass-radargunpublisher-report-performance-test-results-radargun)

*   [Railflow for TestRail](https://www.jenkins.io/doc/pipeline/steps/railflow-testrail/)
    *   [`railflow`: Railflow Plugin: TestRail Test Results Processor](https://www.jenkins.io/doc/pipeline/steps/railflow-testrail/#railflow-railflow-plugin-testrail-test-results-processor)

*   [Rancher Plugin](https://www.jenkins.io/doc/pipeline/steps/rancher/)
    *   [`rancher`: Deploy/Upgrade Rancher Service](https://www.jenkins.io/doc/pipeline/steps/rancher/#rancher-deployupgrade-rancher-service)

*   [Ranorex Test Execution Plugin](https://www.jenkins.io/doc/pipeline/steps/ranorex-integration/)
    *   [`ranorex`: Run a Ranorex test suite](https://www.jenkins.io/doc/pipeline/steps/ranorex-integration/#ranorex-run-a-ranorex-test-suite)

*   [Rapid7 Application Security (InsightAppSec)](https://www.jenkins.io/doc/pipeline/steps/insightappsec/)
    *   [`insightAppSec`: Scan using Application Security](https://www.jenkins.io/doc/pipeline/steps/insightappsec/#insightappsec-scan-using-application-security)

*   [Raspberry Pi Build Status Plugin](https://www.jenkins.io/doc/pipeline/steps/rpi-build-status/)
    *   [`step([$class: 'LedBorgPublisher'])`: LED Borg controller](https://www.jenkins.io/doc/pipeline/steps/rpi-build-status/#stepclass-ledborgpublisher-led-borg-controller)

*   [ReadyAPI Functional Testing Plugin](https://www.jenkins.io/doc/pipeline/steps/soapui-pro-functional-testing/)
    *   [`SoapUIPro`: ReadyAPI Test: Run Functional Test](https://www.jenkins.io/doc/pipeline/steps/soapui-pro-functional-testing/#soapuipro-readyapi-test-run-functional-test)

*   [Red Hat Dependency Analytics Plugin](https://www.jenkins.io/doc/pipeline/steps/redhat-dependency-analytics/)
    *   [`rhdaAnalysis`: Invoke Red Hat Dependency Analytics (RHDA)](https://www.jenkins.io/doc/pipeline/steps/redhat-dependency-analytics/#rhdaanalysis-invoke-red-hat-dependency-analytics-rhda)
    *   [`step([$class: 'CRDABuilder'])`: Invoke Red Hat Dependency Analysis (RHDA)](https://www.jenkins.io/doc/pipeline/steps/redhat-dependency-analytics/#stepclass-crdabuilder-invoke-red-hat-dependency-analysis-rhda)

*   [Redeploy Rancher2.x Workload Plugin](https://www.jenkins.io/doc/pipeline/steps/redeploy-rancher2-workload/)
    *   [`rancherRedeploy`: Redeploy Rancher2.x Workload](https://www.jenkins.io/doc/pipeline/steps/redeploy-rancher2-workload/#rancherredeploy-redeploy-rancher2-x-workload)

*   [Redmine Metrics Report](https://www.jenkins.io/doc/pipeline/steps/redmine-metrics-report/)
    *   [`redmineMetricsReport`: Generate Redmine Metrics Report](https://www.jenkins.io/doc/pipeline/steps/redmine-metrics-report/#redminemetricsreport-generate-redmine-metrics-report)

*   [Release Plugin](https://www.jenkins.io/doc/pipeline/steps/release/)
    *   [`release`: Trigger release for the job](https://www.jenkins.io/doc/pipeline/steps/release/#release-trigger-release-for-the-job)

*   [Reliza Integration](https://www.jenkins.io/doc/pipeline/steps/reliza-integration/)
    *   [`addRelizaRelease`: RelizaBuilder](https://www.jenkins.io/doc/pipeline/steps/reliza-integration/#addrelizarelease-relizabuilder)
    *   [`submitPrData`: RelizaPR](https://www.jenkins.io/doc/pipeline/steps/reliza-integration/#submitprdata-relizapr)
    *   [`withReliza`: RelizaBuildWrapper](https://www.jenkins.io/doc/pipeline/steps/reliza-integration/#withreliza-relizabuildwrapper)

*   [Remote Result Trigger Plugin](https://www.jenkins.io/doc/pipeline/steps/remote-result-trigger/)
    *   [`readRemoteJobs`: ReadRemoteJobsStep](https://www.jenkins.io/doc/pipeline/steps/remote-result-trigger/#readremotejobs-readremotejobsstep)
    *   [`readRemoteResult`: ReadRemoteResultStep](https://www.jenkins.io/doc/pipeline/steps/remote-result-trigger/#readremoteresult-readremoteresultstep)
    *   [`pubResult`: Publish Build Result](https://www.jenkins.io/doc/pipeline/steps/remote-result-trigger/#pubresult-publish-build-result)

*   [Repository Connector](https://www.jenkins.io/doc/pipeline/steps/repository-connector/)
    *   [`artifactDeployer`: Maven Artifact Deployer](https://www.jenkins.io/doc/pipeline/steps/repository-connector/#artifactdeployer-maven-artifact-deployer)
    *   [`artifactResolver`: Maven Artifact Resolver](https://www.jenkins.io/doc/pipeline/steps/repository-connector/#artifactresolver-maven-artifact-resolver)

*   [Reqtify Plugin](https://www.jenkins.io/doc/pipeline/steps/reqtify/)
    *   [`reqtifyFunction`: Reqtify: Call Function](https://www.jenkins.io/doc/pipeline/steps/reqtify/#reqtifyfunction-reqtify-call-function)
    *   [`reqtifyReport`: Reqtify: Generate Report](https://www.jenkins.io/doc/pipeline/steps/reqtify/#reqtifyreport-reqtify-generate-report)
    *   [`step([$class: 'CallFunction'])`: Reqtify: Call Function](https://www.jenkins.io/doc/pipeline/steps/reqtify/#stepclass-callfunction-reqtify-call-function)
    *   [`step([$class: 'ReqtifyGenerateReport'])`: Reqtify: Generate Report](https://www.jenkins.io/doc/pipeline/steps/reqtify/#stepclass-reqtifygeneratereport-reqtify-generate-report)

*   [Review Board Plugin](https://www.jenkins.io/doc/pipeline/steps/rb/)
    *   [`notifyReviewBoard`: Publish build status to Review Board](https://www.jenkins.io/doc/pipeline/steps/rb/#notifyreviewboard-publish-build-status-to-review-board)
    *   [`publishReview`: Apply patch from Review Board](https://www.jenkins.io/doc/pipeline/steps/rb/#publishreview-apply-patch-from-review-board)

*   [Rich Text Publisher Plugin](https://www.jenkins.io/doc/pipeline/steps/rich-text-publisher-plugin/)
    *   [`rtp`: Publish rich text message](https://www.jenkins.io/doc/pipeline/steps/rich-text-publisher-plugin/#rtp-publish-rich-text-message)
    *   [`step([$class: 'RichTextPublisher'])`: Publish rich text message](https://www.jenkins.io/doc/pipeline/steps/rich-text-publisher-plugin/#stepclass-richtextpublisher-publish-rich-text-message)

*   [Robot Framework plugin](https://www.jenkins.io/doc/pipeline/steps/robot/)
    *   [`robot`: Configure robot framework report collection](https://www.jenkins.io/doc/pipeline/steps/robot/#robot-configure-robot-framework-report-collection)
    *   [`step([$class: 'RobotPublisher'])`: Publish Robot Framework test results](https://www.jenkins.io/doc/pipeline/steps/robot/#stepclass-robotpublisher-publish-robot-framework-test-results)

*   [RocketChat Notifier](https://www.jenkins.io/doc/pipeline/steps/rocketchatnotifier/)
    *   [`rocketSend`: Send RocketChat Message](https://www.jenkins.io/doc/pipeline/steps/rocketchatnotifier/#rocketsend-send-rocketchat-message)

*   [Role-based Authorization Strategy](https://www.jenkins.io/doc/pipeline/steps/role-strategy/)
    *   [`currentUserGlobalRoles`: Current Users Global Roles](https://www.jenkins.io/doc/pipeline/steps/role-strategy/#currentuserglobalroles-current-users-global-roles)
    *   [`currentUserItemRoles`: Current Users Item Roles](https://www.jenkins.io/doc/pipeline/steps/role-strategy/#currentuseritemroles-current-users-item-roles)

*   [RubyMetrics plugin for Jenkins](https://www.jenkins.io/doc/pipeline/steps/rubyMetrics/)
    *   [`step([$class: 'RcovPublisher'])`: Publish Rcov report](https://www.jenkins.io/doc/pipeline/steps/rubyMetrics/#stepclass-rcovpublisher-publish-rcov-report)

*   [Run Selector Plugin](https://www.jenkins.io/doc/pipeline/steps/run-selector/)
    *   [`selectRun`: Select Run](https://www.jenkins.io/doc/pipeline/steps/run-selector/#selectrun-select-run)

*   [Rundeck plugin](https://www.jenkins.io/doc/pipeline/steps/rundeck/)
    *   [`step([$class: 'RundeckNotifier'])`: Rundeck](https://www.jenkins.io/doc/pipeline/steps/rundeck/#stepclass-rundecknotifier-rundeck)

*   [S3 publisher plugin](https://www.jenkins.io/doc/pipeline/steps/s3/)
    *   [`s3Upload`: Publish artifacts to S3 Bucket](https://www.jenkins.io/doc/pipeline/steps/s3/#s3upload-publish-artifacts-to-s3-bucket)
    *   [`s3CopyArtifact`: S3 Copy Artifact](https://www.jenkins.io/doc/pipeline/steps/s3/#s3copyartifact-s3-copy-artifact)

*   [SaltStack plugin](https://www.jenkins.io/doc/pipeline/steps/saltstack/)
    *   [`salt`: Send a message to Salt API](https://www.jenkins.io/doc/pipeline/steps/saltstack/#salt-send-a-message-to-salt-api)
    *   [`step([$class: 'SaltAPIBuilder'])`: Send a message to Salt API](https://www.jenkins.io/doc/pipeline/steps/saltstack/#stepclass-saltapibuilder-send-a-message-to-salt-api)

*   [Sauce OnDemand plugin](https://www.jenkins.io/doc/pipeline/steps/sauce-ondemand/)
    *   [`sauce`: Sauce](https://www.jenkins.io/doc/pipeline/steps/sauce-ondemand/#sauce-sauce)
    *   [`sauceconnect`: Sauce Connect](https://www.jenkins.io/doc/pipeline/steps/sauce-ondemand/#sauceconnect-sauce-connect)
    *   [`saucePublisher`: Run Sauce Labs Test Publisher](https://www.jenkins.io/doc/pipeline/steps/sauce-ondemand/#saucepublisher-run-sauce-labs-test-publisher)

*   [SCM HttpClient (deprecated)](https://www.jenkins.io/doc/pipeline/steps/scm-httpclient/)
    *   [`scmHttpClient`: SCM HttpClient](https://www.jenkins.io/doc/pipeline/steps/scm-httpclient/#scmhttpclient-scm-httpclient)

*   [SCM Skip Plugin](https://www.jenkins.io/doc/pipeline/steps/scmskip/)
    *   [`scmSkip`: SCM Skip Step](https://www.jenkins.io/doc/pipeline/steps/scmskip/#scmskip-scm-skip-step)

*   [Scoverage Plugin](https://www.jenkins.io/doc/pipeline/steps/scoverage/)
    *   [`step([$class: 'ScoveragePublisher'])`: Publish Scoverage Report](https://www.jenkins.io/doc/pipeline/steps/scoverage/#stepclass-scoveragepublisher-publish-scoverage-report)

*   [SD Elements Plugin](https://www.jenkins.io/doc/pipeline/steps/sdelements/)
    *   [`sdelements`: SD Elements](https://www.jenkins.io/doc/pipeline/steps/sdelements/#sdelements-sd-elements)

*   [Seapine Surround SCM Plug-in](https://www.jenkins.io/doc/pipeline/steps/Surround-SCM-plugin/)
    *   [`sscm`: Surround SCM](https://www.jenkins.io/doc/pipeline/steps/Surround-SCM-plugin/#sscm-surround-scm)

*   [Sec1 Security Scanner](https://www.jenkins.io/doc/pipeline/steps/secone-sca-sast-security-scanner/)
    *   [`sec1ScaSastSecurity`: Execute Sec1 Sca Sast Security Scan](https://www.jenkins.io/doc/pipeline/steps/secone-sca-sast-security-scanner/#sec1scasastsecurity-execute-sec1-sca-sast-security-scan)

*   [Sedstart Runner Plugin](https://www.jenkins.io/doc/pipeline/steps/sedstart-runner/)
    *   [`sedStart`: SedStart Runner](https://www.jenkins.io/doc/pipeline/steps/sedstart-runner/#sedstart-sedstart-runner)

*   [Selenium HTML report](https://www.jenkins.io/doc/pipeline/steps/seleniumhtmlreport/)
    *   [`step([$class: 'SeleniumHtmlReportPublisher'])`: Publish Selenium Html Report](https://www.jenkins.io/doc/pipeline/steps/seleniumhtmlreport/#stepclass-seleniumhtmlreportpublisher-publish-selenium-html-report)

*   [Sensedia Api Platform tools](https://www.jenkins.io/doc/pipeline/steps/sensedia-api-platform/)
    *   [`sensediaApiDeploy`: Sensedia API Platformdeploy](https://www.jenkins.io/doc/pipeline/steps/sensedia-api-platform/#sensediaapideploy-sensedia-api-platformdeploy)
    *   [`sensediaApiJson`: Sensedia API Platform get json](https://www.jenkins.io/doc/pipeline/steps/sensedia-api-platform/#sensediaapijson-sensedia-api-platform-get-json)
    *   [`sensediaApiQA`: Sensedia API Platform QA](https://www.jenkins.io/doc/pipeline/steps/sensedia-api-platform/#sensediaapiqa-sensedia-api-platform-qa)

*   [Service Now Plugin](https://www.jenkins.io/doc/pipeline/steps/service-now/)
    *   [`serviceNow_attachFile`: AttachFileStep](https://www.jenkins.io/doc/pipeline/steps/service-now/#servicenow-attachfile-attachfilestep)
    *   [`serviceNow_attachZip`: AttachZipStep](https://www.jenkins.io/doc/pipeline/steps/service-now/#servicenow-attachzip-attachzipstep)
    *   [`serviceNow_createChange`: CreateChangeStep](https://www.jenkins.io/doc/pipeline/steps/service-now/#servicenow-createchange-createchangestep)
    *   [`serviceNow_getCTask`: GetCTaskStep](https://www.jenkins.io/doc/pipeline/steps/service-now/#servicenow-getctask-getctaskstep)
    *   [`serviceNow_getChangeState`: GetChangeStateStep](https://www.jenkins.io/doc/pipeline/steps/service-now/#servicenow-getchangestate-getchangestatestep)
    *   [`serviceNow_updateChangeItem`: UpdateChangeItemStep](https://www.jenkins.io/doc/pipeline/steps/service-now/#servicenow-updatechangeitem-updatechangeitemstep)
    *   [`serviceNow_updateTask`: UpdateChangeTaskStep](https://www.jenkins.io/doc/pipeline/steps/service-now/#servicenow-updatetask-updatechangetaskstep)

*   [ServiceNow CI/CD Plugin](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/)
    *   [`snActivatePlugin`: SN: Activate plugin](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/#snactivateplugin-sn-activate-plugin)
    *   [`snApplyChanges`: SN: Apply changes](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/#snapplychanges-sn-apply-changes)
    *   [`snBatchInstall`: SN: Batch install](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/#snbatchinstall-sn-batch-install)
    *   [`snBatchRollback`: SN: Batch rollback](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/#snbatchrollback-sn-batch-rollback)
    *   [`snInstallApp`: SN: Install application](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/#sninstallapp-sn-install-application)
    *   [`snInstanceScan`: SN: Instance scan](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/#sninstancescan-sn-instance-scan)
    *   [`snPublishApp`: SN: Publish application](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/#snpublishapp-sn-publish-application)
    *   [`snRollbackApp`: SN: Roll back application](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/#snrollbackapp-sn-roll-back-application)
    *   [`snRollbackPlugin`: SN: Roll back plugin](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/#snrollbackplugin-sn-roll-back-plugin)
    *   [`snRunTestSuite`: SN: Run test suite with results](https://www.jenkins.io/doc/pipeline/steps/servicenow-cicd/#snruntestsuite-sn-run-test-suite-with-results)

*   [ServiceNow DevOps Plugin](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/)
    *   [`snDevOpsArtifact`: ServiceNow DevOps - Register Artifact step](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsartifact-servicenow-devops-register-artifact-step)
    *   [`snDevOpsChange`: ServiceNow DevOps - Change Control step](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopschange-servicenow-devops-change-control-step)
    *   [`snDevOpsConfig`: ServiceNow DevOps - DevOps Configuration Pipeline](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsconfig-servicenow-devops-devops-configuration-pipeline)
    *   [`snDevOpsConfigExport`: ServiceNow DevOps - DevOps Configuration Export](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsconfigexport-servicenow-devops-devops-configuration-export)
    *   [`snDevOpsConfigGetSnapshots`: ServiceNow DevOps - Get latest and validated snapshots](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsconfiggetsnapshots-servicenow-devops-get-latest-and-validated-snapshots)
    *   [`snDevOpsConfigPublish`: ServiceNow DevOps - DevOps Configuration Publish](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsconfigpublish-servicenow-devops-devops-configuration-publish)
    *   [`snDevOpsConfigRegisterPipeline`: ServiceNow DevOps - DevOps Configuration Register Pipeline](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsconfigregisterpipeline-servicenow-devops-devops-configuration-register-pipeline)
    *   [`snDevOpsConfigUpload`: ServiceNow DevOps - DevOps Configuration Upload](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsconfigupload-servicenow-devops-devops-configuration-upload)
    *   [`snDevOpsConfigValidate`: ServiceNow DevOps - DevOps Configuration Validate](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsconfigvalidate-servicenow-devops-devops-configuration-validate)
    *   [`snDevOpsGetChangeNumber`: ServiceNow DevOps - get Change Number step](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsgetchangenumber-servicenow-devops-get-change-number-step)
    *   [`snDevOpsPackage`: ServiceNow DevOps - Register Package step](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopspackage-servicenow-devops-register-package-step)
    *   [`snDevOpsSecurityResult`: ServiceNow DevOps - Register Security Step](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopssecurityresult-servicenow-devops-register-security-step)
    *   [`snDevOpsStep`: ServiceNow DevOps - Mapping step](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsstep-servicenow-devops-mapping-step)
    *   [`snDevOpsUpdateChangeInfo`: ServiceNow DevOps - Update Change Request Info](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#sndevopsupdatechangeinfo-servicenow-devops-update-change-request-info)
    *   [`step([$class: 'DevOpsCreateArtifactPackageBuildStep'])`: ServiceNow DevOps - Register Package step](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#stepclass-devopscreateartifactpackagebuildstep-servicenow-devops-register-package-step)
    *   [`step([$class: 'DevOpsFreestyleRegisterSecurityStep'])`: ServiceNow DevOps - Register Security Step](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#stepclass-devopsfreestyleregistersecuritystep-servicenow-devops-register-security-step)
    *   [`step([$class: 'DevOpsRegisterArtifactBuildStep'])`: ServiceNow DevOps - Register Artifact step](https://www.jenkins.io/doc/pipeline/steps/servicenow-devops/#stepclass-devopsregisterartifactbuildstep-servicenow-devops-register-artifact-step)

*   [SideeX](https://www.jenkins.io/doc/pipeline/steps/sideex/)
    *   [`step([$class: 'SideeX'])`: Execute SideeX Web Testing](https://www.jenkins.io/doc/pipeline/steps/sideex/#stepclass-sideex-execute-sideex-web-testing)

*   [SimplifyQA Automation Hub](https://www.jenkins.io/doc/pipeline/steps/simplifyqa-pipeline-executor/)
    *   [`SQAPipelineExecutor`: SimplifyQA (Old UI Executor)](https://www.jenkins.io/doc/pipeline/steps/simplifyqa-pipeline-executor/#sqapipelineexecutor-simplifyqa-old-ui-executor)
    *   [`simplifyQA`: SimplifyQA Pipeline Executor](https://www.jenkins.io/doc/pipeline/steps/simplifyqa-pipeline-executor/#simplifyqa-simplifyqa-pipeline-executor)

*   [Sken.ai CLI](https://www.jenkins.io/doc/pipeline/steps/skenai/)
    *   [`skenai`: Sken.ai](https://www.jenkins.io/doc/pipeline/steps/skenai/#skenai-sken-ai)

*   [Slack Notification Plugin](https://www.jenkins.io/doc/pipeline/steps/slack/)
    *   [`slackSend`: Send Slack Message](https://www.jenkins.io/doc/pipeline/steps/slack/#slacksend-send-slack-message)
    *   [`slackUploadFile`: Upload file to slack](https://www.jenkins.io/doc/pipeline/steps/slack/#slackuploadfile-upload-file-to-slack)
    *   [`slackUserIdFromEmail`: Resolve Slack UserId from Email Address](https://www.jenkins.io/doc/pipeline/steps/slack/#slackuseridfromemail-resolve-slack-userid-from-email-address)
    *   [`slackUserIdsFromCommitters`: Resolve Slack UserIds from Changeset Authors](https://www.jenkins.io/doc/pipeline/steps/slack/#slackuseridsfromcommitters-resolve-slack-userids-from-changeset-authors)

*   [SLOCCount Plug-in](https://www.jenkins.io/doc/pipeline/steps/sloccount/)
    *   [`sloccountPublish`: Publish Sloccount reports](https://www.jenkins.io/doc/pipeline/steps/sloccount/#sloccountpublish-publish-sloccount-reports)
    *   [`step([$class: 'SloccountPublisher'])`: Publish SLOCCount analysis results](https://www.jenkins.io/doc/pipeline/steps/sloccount/#stepclass-sloccountpublisher-publish-sloccount-analysis-results)

*   [SLSA Provenance Attestation Plugin](https://www.jenkins.io/doc/pipeline/steps/slsa/)
    *   [`provenanceRecorder`: Generate SLSA provenance attestations](https://www.jenkins.io/doc/pipeline/steps/slsa/#provenancerecorder-generate-slsa-provenance-attestations)

*   [SmileHub Notifier](https://www.jenkins.io/doc/pipeline/steps/smilehubnotifier/)
    *   [`smilehubSend`: Send SmileHub Message](https://www.jenkins.io/doc/pipeline/steps/smilehubnotifier/#smilehubsend-send-smilehub-message)

*   [Snow Commander Plugin](https://www.jenkins.io/doc/pipeline/steps/embotics-vcommander/)
    *   [`vCommander`: Commander Services](https://www.jenkins.io/doc/pipeline/steps/embotics-vcommander/#vcommander-commander-services)

*   [SnowGlobe Plugin](https://www.jenkins.io/doc/pipeline/steps/snowglobe/)
    *   [`snowglobe_apply`: ApplyStep](https://www.jenkins.io/doc/pipeline/steps/snowglobe/#snowglobe-apply-applystep)
    *   [`snowglobe_clone`: CloneStep](https://www.jenkins.io/doc/pipeline/steps/snowglobe/#snowglobe-clone-clonestep)
    *   [`snowglobe_destroy`: DestroyStep](https://www.jenkins.io/doc/pipeline/steps/snowglobe/#snowglobe-destroy-destroystep)
    *   [`snowglobe_get_variables`: GetVariablesStep](https://www.jenkins.io/doc/pipeline/steps/snowglobe/#snowglobe-get-variables-getvariablesstep)
    *   [`snowglobe_set_variables`: SetVariablesStep](https://www.jenkins.io/doc/pipeline/steps/snowglobe/#snowglobe-set-variables-setvariablesstep)
    *   [`snowglobe_state`: StateStep](https://www.jenkins.io/doc/pipeline/steps/snowglobe/#snowglobe-state-statestep)

*   [Snyk Security Plugin](https://www.jenkins.io/doc/pipeline/steps/snyk-security-scanner/)
    *   [`snykSecurity`: Invoke Snyk Security task](https://www.jenkins.io/doc/pipeline/steps/snyk-security-scanner/#snyksecurity-invoke-snyk-security-task)
    *   [`step([$class: 'SnykStepBuilder'])`: Invoke Snyk Security task](https://www.jenkins.io/doc/pipeline/steps/snyk-security-scanner/#stepclass-snykstepbuilder-invoke-snyk-security-task)

*   [Sonar Gerrit Plugin](https://www.jenkins.io/doc/pipeline/steps/sonar-gerrit/)
    *   [`sonarToGerrit`: Post SonarQube issues as Gerrit comments](https://www.jenkins.io/doc/pipeline/steps/sonar-gerrit/#sonartogerrit-post-sonarqube-issues-as-gerrit-comments)

*   [Sonargraph Integration Jenkins Plugin](https://www.jenkins.io/doc/pipeline/steps/sonargraph-integration/)
    *   [`SonargraphReport`: Sonargraph Integration Report Generation & Analysis](https://www.jenkins.io/doc/pipeline/steps/sonargraph-integration/#sonargraphreport-sonargraph-integration-report-generation-analysis)

*   [SonarQube Scanner for Jenkins](https://www.jenkins.io/doc/pipeline/steps/sonar/)
    *   [`waitForQualityGate`: Wait for SonarQube analysis to be completed and return quality gate status](https://www.jenkins.io/doc/pipeline/steps/sonar/#waitforqualitygate-wait-for-sonarqube-analysis-to-be-completed-and-return-quality-gate-status)
    *   [`withSonarQubeEnv`: Prepare SonarQube Scanner environment](https://www.jenkins.io/doc/pipeline/steps/sonar/#withsonarqubeenv-prepare-sonarqube-scanner-environment)

*   [Sonic CI Helper](https://www.jenkins.io/doc/pipeline/steps/sonic-ci-helper/)
    *   [`upload-sonic`: Upload package to Sonic Testing Platform.](https://www.jenkins.io/doc/pipeline/steps/sonic-ci-helper/#upload-sonic-upload-package-to-sonic-testing-platform)

*   [SOOS SCA](https://www.jenkins.io/doc/pipeline/steps/soos-sca/)
    *   [`step([$class: 'SoosSCA'])`: SOOS SCA](https://www.jenkins.io/doc/pipeline/steps/soos-sca/#stepclass-soossca-soos-sca)

*   [Split Admin plugin](https://www.jenkins.io/doc/pipeline/steps/split-admin/)
    *   [`split`: Split Admin Task](https://www.jenkins.io/doc/pipeline/steps/split-admin/#split-split-admin-task)

*   [Splunk Plugin](https://www.jenkins.io/doc/pipeline/steps/splunk-devops/)
    *   [`step([$class: 'SplunkArtifactNotifier'])`: Send files to Splunk](https://www.jenkins.io/doc/pipeline/steps/splunk-devops/#stepclass-splunkartifactnotifier-send-files-to-splunk)

*   [Splunk Plugin Extension](https://www.jenkins.io/doc/pipeline/steps/splunk-devops-extend/)
    *   [`sendSplunkConsoleLog`: Send console log Splunk](https://www.jenkins.io/doc/pipeline/steps/splunk-devops-extend/#sendsplunkconsolelog-send-console-log-splunk)
    *   [`sendSplunkFile`: Send files to Splunk](https://www.jenkins.io/doc/pipeline/steps/splunk-devops-extend/#sendsplunkfile-send-files-to-splunk)

*   [Spring Config Plugin](https://www.jenkins.io/doc/pipeline/steps/spring-config/)
    *   [`springConfig`: A step to read spring style profile configs](https://www.jenkins.io/doc/pipeline/steps/spring-config/#springconfig-a-step-to-read-spring-style-profile-configs)
    *   [`springProfiles`: A step to retrieve spring profiles defined in Job](https://www.jenkins.io/doc/pipeline/steps/spring-config/#springprofiles-a-step-to-retrieve-spring-profiles-defined-in-job)

*   [Spring Initalzr plugin](https://www.jenkins.io/doc/pipeline/steps/spring-initalzr/)
    *   [`springBoot`: Generate spring boot application](https://www.jenkins.io/doc/pipeline/steps/spring-initalzr/#springboot-generate-spring-boot-application)

*   [SQLPlus Script Runner](https://www.jenkins.io/doc/pipeline/steps/sqlplus-script-runner/)
    *   [`step([$class: 'SQLPlusRunnerBuilder'])`: SQLPlus Script Runner](https://www.jenkins.io/doc/pipeline/steps/sqlplus-script-runner/#stepclass-sqlplusrunnerbuilder-sqlplus-script-runner)

*   [SSH Agent Plugin](https://www.jenkins.io/doc/pipeline/steps/ssh-agent/)
    *   [`sshagent`: SSH Agent](https://www.jenkins.io/doc/pipeline/steps/ssh-agent/#sshagent-ssh-agent)

*   [SSH Pipeline Steps](https://www.jenkins.io/doc/pipeline/steps/ssh-steps/)
    *   [`sshCommand`: SSH Steps: sshCommand - Execute command on remote node.](https://www.jenkins.io/doc/pipeline/steps/ssh-steps/#sshcommand-ssh-steps-sshcommand-execute-command-on-remote-node)
    *   [`sshGet`: SSH Steps: sshGet - Get a file or directory from remote node.](https://www.jenkins.io/doc/pipeline/steps/ssh-steps/#sshget-ssh-steps-sshget-get-a-file-or-directory-from-remote-node)
    *   [`sshPut`: SSH Steps: sshPut - Put a file or directory on remote node.](https://www.jenkins.io/doc/pipeline/steps/ssh-steps/#sshput-ssh-steps-sshput-put-a-file-or-directory-on-remote-node)
    *   [`sshRemove`: SSH Steps: sshRemove - Remove a file or directory from remote node.](https://www.jenkins.io/doc/pipeline/steps/ssh-steps/#sshremove-ssh-steps-sshremove-remove-a-file-or-directory-from-remote-node)
    *   [`sshScript`: SSH Steps: sshScript - Execute script(file) on remote node.](https://www.jenkins.io/doc/pipeline/steps/ssh-steps/#sshscript-ssh-steps-sshscript-execute-scriptfile-on-remote-node)

*   [StackRox Container Image Scanner](https://www.jenkins.io/doc/pipeline/steps/stackrox-container-image-scanner/)
    *   [`stackrox`: StackRox Container Image Scanner](https://www.jenkins.io/doc/pipeline/steps/stackrox-container-image-scanner/#stackrox-stackrox-container-image-scanner)

*   [Start Windocks Containers](https://www.jenkins.io/doc/pipeline/steps/windocks-start-container/)
    *   [`step([$class: 'WinDocksBuilder'])`: Setup Docker Container](https://www.jenkins.io/doc/pipeline/steps/windocks-start-container/#stepclass-windocksbuilder-setup-docker-container)

*   [StepCounter Plugin](https://www.jenkins.io/doc/pipeline/steps/stepcounter/)
    *   [`stepcounter`: Count steps](https://www.jenkins.io/doc/pipeline/steps/stepcounter/#stepcounter-count-steps)

*   [Stoplight Report Plugin](https://www.jenkins.io/doc/pipeline/steps/stoplightio-report/)
    *   [`publishStoplight`: Publish Stoplight Report](https://www.jenkins.io/doc/pipeline/steps/stoplightio-report/#publishstoplight-publish-stoplight-report)
    *   [`step([$class: 'StoplightReportPublisher'])`: Publish Stoplight Report](https://www.jenkins.io/doc/pipeline/steps/stoplightio-report/#stepclass-stoplightreportpublisher-publish-stoplight-report)

*   [Subversion Partial Release Manager plugin](https://www.jenkins.io/doc/pipeline/steps/svn-partial-release-mgr/)
    *   [`step([$class: 'PartialReleaseMgrSuccessfulBuilder'])`: Svn-Partial Release Manager (After build)](https://www.jenkins.io/doc/pipeline/steps/svn-partial-release-mgr/#stepclass-partialreleasemgrsuccessfulbuilder-svn-partial-release-manager-after-build)

*   [Subversion Plug-in](https://www.jenkins.io/doc/pipeline/steps/subversion/)
    *   [`svn`: Subversion](https://www.jenkins.io/doc/pipeline/steps/subversion/#svn-subversion)

*   [Summary Display Plugin](https://www.jenkins.io/doc/pipeline/steps/summary_report/)
    *   [`step([$class: 'ACIPluginPublisher'])`: Publish XML Summary Reports](https://www.jenkins.io/doc/pipeline/steps/summary_report/#stepclass-acipluginpublisher-publish-xml-summary-reports)

*   [Sumologic Publisher](https://www.jenkins.io/doc/pipeline/steps/sumologic-publisher/)
    *   [`SumoPipelineLogCollection`: SumoPipelineLogCollection](https://www.jenkins.io/doc/pipeline/steps/sumologic-publisher/#sumopipelinelogcollection-sumopipelinelogcollection)
    *   [`SumoSDOEvent`: Upload Events specific to Software Delivery Optimization Solution to Sumo Logic.](https://www.jenkins.io/doc/pipeline/steps/sumologic-publisher/#sumosdoevent-upload-events-specific-to-software-delivery-optimization-solution-to-sumo-logic)
    *   [`SumoUpload`: Upload files or Text to Sumo Logic HTTP source as provided in Sumo Logic Publisher Configuration.](https://www.jenkins.io/doc/pipeline/steps/sumologic-publisher/#sumoupload-upload-files-or-text-to-sumo-logic-http-source-as-provided-in-sumo-logic-publisher-configuration)
    *   [`step([$class: 'SumoBuildNotifier'])`: Sumo Logic build logger](https://www.jenkins.io/doc/pipeline/steps/sumologic-publisher/#stepclass-sumobuildnotifier-sumo-logic-build-logger)

*   [Swarm Agents Cloud Plugin](https://www.jenkins.io/doc/pipeline/steps/swarm-agents-cloud/)
    *   [`swarmAgent`: Provision Docker Swarm Agent](https://www.jenkins.io/doc/pipeline/steps/swarm-agents-cloud/#swarmagent-provision-docker-swarm-agent)

*   [SWEAGLE Plugin](https://www.jenkins.io/doc/pipeline/steps/sweagle/)
    *   [`SWEAGLEExport`: SWEAGLE Get Config](https://www.jenkins.io/doc/pipeline/steps/sweagle/#sweagleexport-sweagle-get-config)
    *   [`SWEAGLESnapshot`: SWEAGLE Snapshot](https://www.jenkins.io/doc/pipeline/steps/sweagle/#sweaglesnapshot-sweagle-snapshot)
    *   [`SWEAGLEUpload`: SWEAGLE Upload](https://www.jenkins.io/doc/pipeline/steps/sweagle/#sweagleupload-sweagle-upload)
    *   [`SWEAGLEValidate`: SWEAGLE Validate](https://www.jenkins.io/doc/pipeline/steps/sweagle/#sweaglevalidate-sweagle-validate)

*   [Synopsys Coverity plugin](https://www.jenkins.io/doc/pipeline/steps/synopsys-coverity/)
    *   [`coverityIssueCheck`: Check for Issues in Coverity View](https://www.jenkins.io/doc/pipeline/steps/synopsys-coverity/#coverityissuecheck-check-for-issues-in-coverity-view)
    *   [`withCoverityEnvironment`: Inject Coverity environment into the build process](https://www.jenkins.io/doc/pipeline/steps/synopsys-coverity/#withcoverityenvironment-inject-coverity-environment-into-the-build-process)

*   [Sysdig Secure Container Image Scanner Plugin](https://www.jenkins.io/doc/pipeline/steps/sysdig-secure/)
    *   [`step([$class: 'IaCScanningBuilder'])`: Sysdig Secure Code Scan](https://www.jenkins.io/doc/pipeline/steps/sysdig-secure/#stepclass-iacscanningbuilder-sysdig-secure-code-scan)
    *   [`step([$class: 'ImageScanningBuilder'])`: Sysdig Image Scanning](https://www.jenkins.io/doc/pipeline/steps/sysdig-secure/#stepclass-imagescanningbuilder-sysdig-image-scanning)
    *   [`sysdigImageScan`: Sysdig Image Scanning pipeline step](https://www.jenkins.io/doc/pipeline/steps/sysdig-secure/#sysdigimagescan-sysdig-image-scanning-pipeline-step)

*   [Tacotruck Plugin](https://www.jenkins.io/doc/pipeline/steps/tacotruck/)
    *   [`tacotruck`: Execute Tacotruck](https://www.jenkins.io/doc/pipeline/steps/tacotruck/#tacotruck-execute-tacotruck)

*   [Talend](https://www.jenkins.io/doc/pipeline/steps/talend/)
    *   [`createTask`: Talend Create Task](https://www.jenkins.io/doc/pipeline/steps/talend/#createtask-talend-create-task)
    *   [`runPromotion`: Talend Promotion](https://www.jenkins.io/doc/pipeline/steps/talend/#runpromotion-talend-promotion)
    *   [`runTask`: Talend Run Task](https://www.jenkins.io/doc/pipeline/steps/talend/#runtask-talend-run-task)

*   [Tanaguru Plugin](https://www.jenkins.io/doc/pipeline/steps/tanaguru/)
    *   [`tanaguru`: Jenkins Tanaguru Plugin](https://www.jenkins.io/doc/pipeline/steps/tanaguru/#tanaguru-jenkins-tanaguru-plugin)

*   [TAP Plugin](https://www.jenkins.io/doc/pipeline/steps/tap/)
    *   [`step([$class: 'TapPublisher'])`: Publish TAP Results](https://www.jenkins.io/doc/pipeline/steps/tap/#stepclass-tappublisher-publish-tap-results)

*   [Team Concert Git Plugin](https://www.jenkins.io/doc/pipeline/steps/teamconcert-git/)
    *   [`step([$class: 'RTCGitBuilder'])`: Rational Team Concert(RTC) integration for Git](https://www.jenkins.io/doc/pipeline/steps/teamconcert-git/#stepclass-rtcgitbuilder-rational-team-concertrtc-integration-for-git)

*   [Team Concert Plugin](https://www.jenkins.io/doc/pipeline/steps/teamconcert/)
    *   [`rtcBuild`: Step for interacting with EWM (RTC) Build](https://www.jenkins.io/doc/pipeline/steps/teamconcert/#rtcbuild-step-for-interacting-with-ewm-rtc-build)
    *   [`step([$class: 'RTCPostBuildDeliverPublisher'])`: RTC Post Build Deliver](https://www.jenkins.io/doc/pipeline/steps/teamconcert/#stepclass-rtcpostbuilddeliverpublisher-rtc-post-build-deliver)
    *   [`teamconcert`: Team Concert](https://www.jenkins.io/doc/pipeline/steps/teamconcert/#teamconcert-team-concert)

*   [teamscale-upload](https://www.jenkins.io/doc/pipeline/steps/teamscale-upload/)
    *   [`teamscale`: Teamscale Upload](https://www.jenkins.io/doc/pipeline/steps/teamscale-upload/#teamscale-teamscale-upload)

*   [Tekton Client Plugin](https://www.jenkins.io/doc/pipeline/steps/tekton-client/)
    *   [`step([$class: 'CreateCustomTaskrun'])`: Tekton : Create TaskRun](https://www.jenkins.io/doc/pipeline/steps/tekton-client/#stepclass-createcustomtaskrun-tekton-create-taskrun)
    *   [`step([$class: 'DeleteRaw'])`: Tekton : Delete Resource (Raw)](https://www.jenkins.io/doc/pipeline/steps/tekton-client/#stepclass-deleteraw-tekton-delete-resource-raw)

*   [Telegram Bot Plugin](https://www.jenkins.io/doc/pipeline/steps/telegram-notifications/)
    *   [`step([$class: 'TelegramBotBuilder'])`: TelegramBot](https://www.jenkins.io/doc/pipeline/steps/telegram-notifications/#stepclass-telegrambotbuilder-telegrambot)
    *   [`telegramSend`: TelegramBot](https://www.jenkins.io/doc/pipeline/steps/telegram-notifications/#telegramsend-telegrambot)
    *   [`step([$class: 'TelegramBotPublisher'])`: TelegramBot](https://www.jenkins.io/doc/pipeline/steps/telegram-notifications/#stepclass-telegrambotpublisher-telegrambot)

*   [Test Results Aggregator Plugin](https://www.jenkins.io/doc/pipeline/steps/test-results-aggregator/)
    *   [`testResultsAggregator`: Aggregate Test Results](https://www.jenkins.io/doc/pipeline/steps/test-results-aggregator/#testresultsaggregator-aggregate-test-results)

*   [TestComplete support plug-in](https://www.jenkins.io/doc/pipeline/steps/TestComplete/)
    *   [`testcompletetest`: TestComplete Test](https://www.jenkins.io/doc/pipeline/steps/TestComplete/#testcompletetest-testcomplete-test)

*   [Testein](https://www.jenkins.io/doc/pipeline/steps/testein/)
    *   [`step([$class: 'TesteinRunBuilder'])`: Run Testein test/suite/application](https://www.jenkins.io/doc/pipeline/steps/testein/#stepclass-testeinrunbuilder-run-testein-testsuiteapplication)
    *   [`step([$class: 'TesteinUploadStepBuilder'])`: Upload Testein custom test steps](https://www.jenkins.io/doc/pipeline/steps/testein/#stepclass-testeinuploadstepbuilder-upload-testein-custom-test-steps)

*   [TestFLO - Test Management for Jira](https://www.jenkins.io/doc/pipeline/steps/testflo-for-jira-test-management-automation/)
    *   [`step([$class: 'TestResultSenderBuildStep'])`: TestFLO Automation test results publisher](https://www.jenkins.io/doc/pipeline/steps/testflo-for-jira-test-management-automation/#stepclass-testresultsenderbuildstep-testflo-automation-test-results-publisher)

*   [TestingBot plugin](https://www.jenkins.io/doc/pipeline/steps/testingbot/)
    *   [`testingbotPublisher`: Run TestingBot Test Publisher](https://www.jenkins.io/doc/pipeline/steps/testingbot/#testingbotpublisher-run-testingbot-test-publisher)
    *   [`testingbot`: TestingBot](https://www.jenkins.io/doc/pipeline/steps/testingbot/#testingbot-testingbot)
    *   [`testingbotTunnel`: TestingBotTunnel](https://www.jenkins.io/doc/pipeline/steps/testingbot/#testingbottunnel-testingbottunnel)

*   [Testinium Plugin](https://www.jenkins.io/doc/pipeline/steps/testinium/)
    *   [`testiniumExecution`: Start Testinium Execution](https://www.jenkins.io/doc/pipeline/steps/testinium/#testiniumexecution-start-testinium-execution)

*   [Testkube CLI](https://www.jenkins.io/doc/pipeline/steps/testkube-cli/)
    *   [`setupTestkube`: Testkube Setup Step](https://www.jenkins.io/doc/pipeline/steps/testkube-cli/#setuptestkube-testkube-setup-step)

*   [TestNG Results Plugin](https://www.jenkins.io/doc/pipeline/steps/testng-plugin/)
    *   [`testNG`: Publish TestNG Results](https://www.jenkins.io/doc/pipeline/steps/testng-plugin/#testng-publish-testng-results)

*   [TestWeaver Plugin](https://www.jenkins.io/doc/pipeline/steps/testweaver/)
    *   [`testweaver`: TestWeaver](https://www.jenkins.io/doc/pipeline/steps/testweaver/#testweaver-testweaver)

*   [TestWheel Automation Plugin](https://www.jenkins.io/doc/pipeline/steps/testwheel-trigger/)
    *   [`testwheelTrigger`: TestwheelTrigger](https://www.jenkins.io/doc/pipeline/steps/testwheel-trigger/#testwheeltrigger-testwheeltrigger)

*   [Text Finder](https://www.jenkins.io/doc/pipeline/steps/text-finder/)
    *   [`findText`: Search files or the console log for regular expression(s)](https://www.jenkins.io/doc/pipeline/steps/text-finder/#findtext-search-files-or-the-console-log-for-regular-expressions)

*   [Themis Plugin](https://www.jenkins.io/doc/pipeline/steps/themis/)
    *   [`themisRefresh`: Refresh Themis Project](https://www.jenkins.io/doc/pipeline/steps/themis/#themisrefresh-refresh-themis-project)
    *   [`themisReport`: Send report files to Themis](https://www.jenkins.io/doc/pipeline/steps/themis/#themisreport-send-report-files-to-themis)

*   [ThreadFix Plugin](https://www.jenkins.io/doc/pipeline/steps/threadfix/)
    *   [`step([$class: 'ThreadFixPublisher'])`: Publish ThreadFix Scan](https://www.jenkins.io/doc/pipeline/steps/threadfix/#stepclass-threadfixpublisher-publish-threadfix-scan)

*   [Throttle Concurrent Builds Plug-in](https://www.jenkins.io/doc/pipeline/steps/throttle-concurrents/)
    *   [`throttle`: Throttle execution of node blocks within this body](https://www.jenkins.io/doc/pipeline/steps/throttle-concurrents/#throttle-throttle-execution-of-node-blocks-within-this-body)

*   [Thycotic DevOps Secrets Vault Plugin](https://www.jenkins.io/doc/pipeline/steps/thycotic-devops-secrets-vault/)
    *   [`dsvSecret`: VaultSecretStep](https://www.jenkins.io/doc/pipeline/steps/thycotic-devops-secrets-vault/#dsvsecret-vaultsecretstep)
    *   [`wrap([$class: 'VaultBuildWrapper'])`: Use Thycotic DevOps Secrets Vault Secrets](https://www.jenkins.io/doc/pipeline/steps/thycotic-devops-secrets-vault/#wrapclass-vaultbuildwrapper-use-thycotic-devops-secrets-vault-secrets)

*   [Thycotic DevOps Secrets Vault Plugin](https://www.jenkins.io/doc/pipeline/steps/thycotic-vault/)
    *   [`wrap([$class: 'ThycoticVaultBuildWrapper'])`: Thycotic DevOps Secrets Vault Plugin](https://www.jenkins.io/doc/pipeline/steps/thycotic-vault/#wrapclass-thycoticvaultbuildwrapper-thycotic-devops-secrets-vault-plugin)

*   [TICS Plugin](https://www.jenkins.io/doc/pipeline/steps/tics/)
    *   [`step([$class: 'TicsAnalyzer'])`: Run TICS](https://www.jenkins.io/doc/pipeline/steps/tics/#stepclass-ticsanalyzer-run-tics)
    *   [`publishTicsResults`:](https://www.jenkins.io/doc/pipeline/steps/tics/#publishticsresults)
    *   [`runTics`:](https://www.jenkins.io/doc/pipeline/steps/tics/#runtics)
    *   [`step([$class: 'TicsPublisher'])`: Publish TICS results](https://www.jenkins.io/doc/pipeline/steps/tics/#stepclass-ticspublisher-publish-tics-results)

*   [Timestamper](https://www.jenkins.io/doc/pipeline/steps/timestamper/)
    *   [`timestamps`: Timestamps](https://www.jenkins.io/doc/pipeline/steps/timestamper/#timestamps-timestamps)
    *   [`wrap([$class: 'TimestamperBuildWrapper'])`: Add timestamps to the Console Output](https://www.jenkins.io/doc/pipeline/steps/timestamper/#wrapclass-timestamperbuildwrapper-add-timestamps-to-the-console-output)

*   [Token Macro Plugin](https://www.jenkins.io/doc/pipeline/steps/token-macro/)
    *   [`tm`: Expand a string containing macros](https://www.jenkins.io/doc/pipeline/steps/token-macro/#tm-expand-a-string-containing-macros)

*   [tracetronic ecu.test Plugin](https://www.jenkins.io/doc/pipeline/steps/ecutest/)
    *   [`publishATX`: [TT] Publish ATX Reports](https://www.jenkins.io/doc/pipeline/steps/ecutest/#publishatx-tt-publish-atx-reports)
    *   [`generateCache`: [TT] Generate Caches](https://www.jenkins.io/doc/pipeline/steps/ecutest/#generatecache-tt-generate-caches)
    *   [`downstreamPublisher`: [TT] Downstream Report Generation](https://www.jenkins.io/doc/pipeline/steps/ecutest/#downstreampublisher-tt-downstream-report-generation)
    *   [`publishETLogs`: [TT] Publish ecu.test Logs](https://www.jenkins.io/doc/pipeline/steps/ecutest/#publishetlogs-tt-publish-ecu-test-logs)
    *   [`exportPackages`: [TT] Export Packages](https://www.jenkins.io/doc/pipeline/steps/ecutest/#exportpackages-tt-export-packages)
    *   [`exportProjects`: [TT] Export Projects](https://www.jenkins.io/doc/pipeline/steps/ecutest/#exportprojects-tt-export-projects)
    *   [`importPackages`: [TT] Import Packages](https://www.jenkins.io/doc/pipeline/steps/ecutest/#importpackages-tt-import-packages)
    *   [`importProjects`: [TT] Import Projects](https://www.jenkins.io/doc/pipeline/steps/ecutest/#importprojects-tt-import-projects)
    *   [`publishUNIT`: [TT] Publish UNIT Reports](https://www.jenkins.io/doc/pipeline/steps/ecutest/#publishunit-tt-publish-unit-reports)
    *   [`checkETLicense`: [TT] Check ecu.test License](https://www.jenkins.io/doc/pipeline/steps/ecutest/#checketlicense-tt-check-ecu-test-license)
    *   [`publishGenerators`: [TT] Publish Generator Reports](https://www.jenkins.io/doc/pipeline/steps/ecutest/#publishgenerators-tt-publish-generator-reports)
    *   [`startET`: [TT] Start ecu.test](https://www.jenkins.io/doc/pipeline/steps/ecutest/#startet-tt-start-ecu-test)
    *   [`startTS`: [TT] Start Tool-Server](https://www.jenkins.io/doc/pipeline/steps/ecutest/#startts-tt-start-tool-server)
    *   [`stopET`: [TT] Stop ecu.test](https://www.jenkins.io/doc/pipeline/steps/ecutest/#stopet-tt-stop-ecu-test)
    *   [`stopTS`: [TT] Stop Tool-Server](https://www.jenkins.io/doc/pipeline/steps/ecutest/#stopts-tt-stop-tool-server)
    *   [`publishTMS`: [TT] Publish to Test Management System](https://www.jenkins.io/doc/pipeline/steps/ecutest/#publishtms-tt-publish-to-test-management-system)
    *   [`publishTRF`: [TT] Publish TRF Reports](https://www.jenkins.io/doc/pipeline/steps/ecutest/#publishtrf-tt-publish-trf-reports)
    *   [`testFolder`: [TT] Run Test Folder](https://www.jenkins.io/doc/pipeline/steps/ecutest/#testfolder-tt-run-test-folder)
    *   [`testPackage`: [TT] Run Package](https://www.jenkins.io/doc/pipeline/steps/ecutest/#testpackage-tt-run-package)
    *   [`testProject`: [TT] Run Project](https://www.jenkins.io/doc/pipeline/steps/ecutest/#testproject-tt-run-project)
    *   [`publishTraceAnalysis`: [TT] Publish Trace Analysis](https://www.jenkins.io/doc/pipeline/steps/ecutest/#publishtraceanalysis-tt-publish-trace-analysis)
    *   [`getATXServer`: Get test.guide server by name](https://www.jenkins.io/doc/pipeline/steps/ecutest/#getatxserver-get-test-guide-server-by-name)
    *   [`getETInstallation`: Get ecu.test installation by name](https://www.jenkins.io/doc/pipeline/steps/ecutest/#getetinstallation-get-ecu-test-installation-by-name)
    *   [`isConfigStarted`: Check ecu.test configuration status](https://www.jenkins.io/doc/pipeline/steps/ecutest/#isconfigstarted-check-ecu-test-configuration-status)
    *   [`newATXServer`: Return new test.guide server](https://www.jenkins.io/doc/pipeline/steps/ecutest/#newatxserver-return-new-test-guide-server)
    *   [`newETInstallation`: Return new ecu.test installation](https://www.jenkins.io/doc/pipeline/steps/ecutest/#newetinstallation-return-new-ecu-test-installation)

*   [Tricentis Continuous Integration](https://www.jenkins.io/doc/pipeline/steps/tricentis-ci/)
    *   [`tricentisCI`: Tricentis Continuous Integration](https://www.jenkins.io/doc/pipeline/steps/tricentis-ci/#tricentisci-tricentis-continuous-integration)

*   [Tuleap API Plugin](https://www.jenkins.io/doc/pipeline/steps/tuleap-api/)
    *   [`tuleapNotifyCommitStatus`: Update the build status of the commit in Tuleap](https://www.jenkins.io/doc/pipeline/steps/tuleap-api/#tuleapnotifycommitstatus-update-the-build-status-of-the-commit-in-tuleap)
    *   [`tuleapSendTTMResults`: Send Tuleap Test Management Results](https://www.jenkins.io/doc/pipeline/steps/tuleap-api/#tuleapsendttmresults-send-tuleap-test-management-results)

*   [Typetalk Plugin](https://www.jenkins.io/doc/pipeline/steps/typetalk/)
    *   [`typetalkSend`: Notify Typetalk when the build fails](https://www.jenkins.io/doc/pipeline/steps/typetalk/#typetalksend-notify-typetalk-when-the-build-fails)
    *   [`withTypetalk`: Notify Typetalk when the build starts/ends](https://www.jenkins.io/doc/pipeline/steps/typetalk/#withtypetalk-notify-typetalk-when-the-build-startsends)

*   [UiPath Plugin](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/)
    *   [`UiPathAssets`: UiPath Manage Assets](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathassets-uipath-manage-assets)
    *   [`UiPathDeploy`: UiPath Deploy](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathdeploy-uipath-deploy)
    *   [`UiPathInstallPlatform`: UiPath InstallPlatform](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathinstallplatform-uipath-installplatform)
    *   [`UiPathPack`: UiPath Pack](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathpack-uipath-pack)
    *   [`UiPathRunJob`: UiPath Run Job](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathrunjob-uipath-run-job)
    *   [`UiPathSolutionActivateDeployment`: UiPath Solution: Activate Deployment](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathsolutionactivatedeployment-uipath-solution-activate-deployment)
    *   [`UiPathSolutionDeletePackage`: UiPath Solution: Delete Package](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathsolutiondeletepackage-uipath-solution-delete-package)
    *   [`UiPathSolutionDeploy`: UiPath Solution: Deploy](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathsolutiondeploy-uipath-solution-deploy)
    *   [`UiPathSolutionDownloadConfig`: UiPath Solution: Download Config](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathsolutiondownloadconfig-uipath-solution-download-config)
    *   [`UiPathSolutionDownloadPackage`: UiPath Solution: Download Package](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathsolutiondownloadpackage-uipath-solution-download-package)
    *   [`UiPathSolutionPack`: UiPath Solution: Pack](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathsolutionpack-uipath-solution-pack)
    *   [`UiPathSolutionUninstallDeployment`: UiPath Solution: Uninstall Deployment](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathsolutionuninstalldeployment-uipath-solution-uninstall-deployment)
    *   [`UiPathSolutionUploadPackage`: UiPath Solution: Upload Package](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathsolutionuploadpackage-uipath-solution-upload-package)
    *   [`UiPathTest`: UiPath Run tests](https://www.jenkins.io/doc/pipeline/steps/uipath-automation-package/#uipathtest-uipath-run-tests)

*   [Uleska Plugin](https://www.jenkins.io/doc/pipeline/steps/uleska/)
    *   [`uleskaScanner`: UleskaScanner](https://www.jenkins.io/doc/pipeline/steps/uleska/#uleskascanner-uleskascanner)

*   [Unblocked Notify Plugin](https://www.jenkins.io/doc/pipeline/steps/unblocked/)
    *   [`unblockedNotify`: Send notification to Unblocked](https://www.jenkins.io/doc/pipeline/steps/unblocked/#unblockednotify-send-notification-to-unblocked)

*   [Updatebot Plugin](https://www.jenkins.io/doc/pipeline/steps/updatebot/)
    *   [`updateBotPush`: UpdateBot Push](https://www.jenkins.io/doc/pipeline/steps/updatebot/#updatebotpush-updatebot-push)

*   [Updraft Android/iOS Publisher](https://www.jenkins.io/doc/pipeline/steps/updraft-publisher/)
    *   [`updraftPublish`: Updraft Android/iOS Publisher](https://www.jenkins.io/doc/pipeline/steps/updraft-publisher/#updraftpublish-updraft-androidios-publisher)

*   [Upload to zScan](https://www.jenkins.io/doc/pipeline/steps/zscan-upload/)
    *   [`zScanUpload`: Upload build artifacts to zScan](https://www.jenkins.io/doc/pipeline/steps/zscan-upload/#zscanupload-upload-build-artifacts-to-zscan)

*   [UrbanCode Velocity Plugin](https://www.jenkins.io/doc/pipeline/steps/urbancode-velocity/)
    *   [`step([$class: 'CheckGate'])`: UCV - Check Gate in UrbanCode Velocity](https://www.jenkins.io/doc/pipeline/steps/urbancode-velocity/#stepclass-checkgate-ucv-check-gate-in-urbancode-velocity)
    *   [`step([$class: 'UploadBuild'])`: UCV - Upload Build to UrbanCode Velocity](https://www.jenkins.io/doc/pipeline/steps/urbancode-velocity/#stepclass-uploadbuild-ucv-upload-build-to-urbancode-velocity)
    *   [`step([$class: 'UploadDeployment'])`: UCV - Upload Deployment to UrbanCode Velocity](https://www.jenkins.io/doc/pipeline/steps/urbancode-velocity/#stepclass-uploaddeployment-ucv-upload-deployment-to-urbancode-velocity)
    *   [`step([$class: 'UploadJUnitTestResult'])`: UCV - Upload JUnit Results to UrbanCode Velocity](https://www.jenkins.io/doc/pipeline/steps/urbancode-velocity/#stepclass-uploadjunittestresult-ucv-upload-junit-results-to-urbancode-velocity)
    *   [`step([$class: 'UploadMetricsFile'])`: UCV - Upload Metrics File to UrbanCode Velocity](https://www.jenkins.io/doc/pipeline/steps/urbancode-velocity/#stepclass-uploadmetricsfile-ucv-upload-metrics-file-to-urbancode-velocity)

*   [User1st uTester Plugin](https://www.jenkins.io/doc/pipeline/steps/user1st-utester/)
    *   [`uTesterPageCountTask`: Execute uTester Page Count Task](https://www.jenkins.io/doc/pipeline/steps/user1st-utester/#utesterpagecounttask-execute-utester-page-count-task)
    *   [`uTesterUrlListTask`: Execute uTester URL List Task](https://www.jenkins.io/doc/pipeline/steps/user1st-utester/#utesterurllisttask-execute-utester-url-list-task)

*   [Valgrind Plug-in](https://www.jenkins.io/doc/pipeline/steps/valgrind/)
    *   [`publishValgrind`: Publish valgrind reports](https://www.jenkins.io/doc/pipeline/steps/valgrind/#publishvalgrind-publish-valgrind-reports)
    *   [`runValgrind`: Run valgrind](https://www.jenkins.io/doc/pipeline/steps/valgrind/#runvalgrind-run-valgrind)
    *   [`step([$class: 'ValgrindBuilder'])`: Run Valgrind](https://www.jenkins.io/doc/pipeline/steps/valgrind/#stepclass-valgrindbuilder-run-valgrind)
    *   [`step([$class: 'ValgrindPublisher'])`: Publish Valgrind results](https://www.jenkins.io/doc/pipeline/steps/valgrind/#stepclass-valgrindpublisher-publish-valgrind-results)

*   [Variables Replace](https://www.jenkins.io/doc/pipeline/steps/variables-replace-plugin/)
    *   [`contentReplace`: Variables Replace](https://www.jenkins.io/doc/pipeline/steps/variables-replace-plugin/#contentreplace-variables-replace)

*   [Vdoo Vision Scanner](https://www.jenkins.io/doc/pipeline/steps/vdoo-vision/)
    *   [`vdooScan`: Vdoo Vision Scanner](https://www.jenkins.io/doc/pipeline/steps/vdoo-vision/#vdooscan-vdoo-vision-scanner)

*   [VectorCAST Coverage](https://www.jenkins.io/doc/pipeline/steps/vectorcast-coverage/)
    *   [`step([$class: 'VectorCASTPublisher'])`: Record VectorCAST Coverage Information](https://www.jenkins.io/doc/pipeline/steps/vectorcast-coverage/#stepclass-vectorcastpublisher-record-vectorcast-coverage-information)

*   [VectorCAST Execution](https://www.jenkins.io/doc/pipeline/steps/vectorcast-execution/)
    *   [`step([$class: 'VectorCASTCommand'])`: VectorCAST Command](https://www.jenkins.io/doc/pipeline/steps/vectorcast-execution/#stepclass-vectorcastcommand-vectorcast-command)
    *   [`step([$class: 'VectorCASTSetup'])`: VectorCAST Setup](https://www.jenkins.io/doc/pipeline/steps/vectorcast-execution/#stepclass-vectorcastsetup-vectorcast-setup)

*   [Venafi CodeSign Protect](https://www.jenkins.io/doc/pipeline/steps/venafi-codesigning/)
    *   [`venafiCodeSignWithJarSigner`: Venafi CodeSign Protect: sign with jarsigner](https://www.jenkins.io/doc/pipeline/steps/venafi-codesigning/#venaficodesignwithjarsigner-venafi-codesign-protect-sign-with-jarsigner)
    *   [`venafiVerifyWithJarSigner`: Venafi CodeSign Protect: verify with jarsigner](https://www.jenkins.io/doc/pipeline/steps/venafi-codesigning/#venafiverifywithjarsigner-venafi-codesign-protect-verify-with-jarsigner)
    *   [`venafiCodeSignWithSignTool`: Venafi CodeSign Protect: sign with signtool](https://www.jenkins.io/doc/pipeline/steps/venafi-codesigning/#venaficodesignwithsigntool-venafi-codesign-protect-sign-with-signtool)
    *   [`venafiVerifyWithSignTool`: Venafi CodeSign Protect: verify with signtool](https://www.jenkins.io/doc/pipeline/steps/venafi-codesigning/#venafiverifywithsigntool-venafi-codesign-protect-verify-with-signtool)

*   [Venafi Machine Identity Management](https://www.jenkins.io/doc/pipeline/steps/venafi-vcert/)
    *   [`venafiVcertRequestCertificate`: Venafi Machine Identity Management: request certificate](https://www.jenkins.io/doc/pipeline/steps/venafi-vcert/#venafivcertrequestcertificate-venafi-machine-identity-management-request-certificate)

*   [Veracode Scan](https://www.jenkins.io/doc/pipeline/steps/veracode-scan/)
    *   [`veracodeDynamicAnalysisReview`: Review Veracode Dynamic Analysis Results](https://www.jenkins.io/doc/pipeline/steps/veracode-scan/#veracodedynamicanalysisreview-review-veracode-dynamic-analysis-results)
    *   [`veracodeDynamicAnalysisResubmit`: Resubmit Veracode Dynamic Analysis](https://www.jenkins.io/doc/pipeline/steps/veracode-scan/#veracodedynamicanalysisresubmit-resubmit-veracode-dynamic-analysis)
    *   [`veracodeDynamicRescan`: Dynamic Rescan with Veracode Pipeline](https://www.jenkins.io/doc/pipeline/steps/veracode-scan/#veracodedynamicrescan-dynamic-rescan-with-veracode-pipeline)
    *   [`veracode`: Upload and Scan with Veracode Pipeline](https://www.jenkins.io/doc/pipeline/steps/veracode-scan/#veracode-upload-and-scan-with-veracode-pipeline)

*   [Version Number Plugin](https://www.jenkins.io/doc/pipeline/steps/versionnumber/)
    *   [`VersionNumber`: Determine the correct version number](https://www.jenkins.io/doc/pipeline/steps/versionnumber/#versionnumber-determine-the-correct-version-number)

*   [view-cloner](https://www.jenkins.io/doc/pipeline/steps/view-cloner/)
    *   [`step([$class: 'ViewCloner'])`: View clone](https://www.jenkins.io/doc/pipeline/steps/view-cloner/#stepclass-viewcloner-view-clone)

*   [Vigilnz Security](https://www.jenkins.io/doc/pipeline/steps/vigilnz-security/)
    *   [`vigilnzScan`: Run Vigilnz Security Scan](https://www.jenkins.io/doc/pipeline/steps/vigilnz-security/#vigilnzscan-run-vigilnz-security-scan)

*   [Violation Comments to Bitbucket Server Plugin](https://www.jenkins.io/doc/pipeline/steps/violation-comments-to-stash/)
    *   [`ViolationsToBitbucketServer`: Report Violations to Bitbucket Server](https://www.jenkins.io/doc/pipeline/steps/violation-comments-to-stash/#violationstobitbucketserver-report-violations-to-bitbucket-server)

*   [Violation Comments to GitHub Plugin](https://www.jenkins.io/doc/pipeline/steps/violation-comments-to-github/)
    *   [`ViolationsToGitHub`: Report Violations to GitHub](https://www.jenkins.io/doc/pipeline/steps/violation-comments-to-github/#violationstogithub-report-violations-to-github)

*   [Violation Comments to GitLab Plugin](https://www.jenkins.io/doc/pipeline/steps/violation-comments-to-gitlab/)
    *   [`ViolationsToGitLab`: Report Violations to GitLab](https://www.jenkins.io/doc/pipeline/steps/violation-comments-to-gitlab/#violationstogitlab-report-violations-to-gitlab)

*   [Visual Basic 6 Plugin](https://www.jenkins.io/doc/pipeline/steps/visual-basic-6/)
    *   [`vb6`: VB6](https://www.jenkins.io/doc/pipeline/steps/visual-basic-6/#vb6-vb6)

*   [visualexpert](https://www.jenkins.io/doc/pipeline/steps/visualexpert/)
    *   [`visualexpert`: Visual Expert](https://www.jenkins.io/doc/pipeline/steps/visualexpert/#visualexpert-visual-expert)

*   [VK Notifier](https://www.jenkins.io/doc/pipeline/steps/vk-notifier/)
    *   [`vkSend`: VkNotifierCustomSendStep](https://www.jenkins.io/doc/pipeline/steps/vk-notifier/#vksend-vknotifiercustomsendstep)
    *   [`vkSendEnd`: VkNotifierEndSendStep](https://www.jenkins.io/doc/pipeline/steps/vk-notifier/#vksendend-vknotifierendsendstep)
    *   [`vkSendStart`: VkNotifierStartSendStep](https://www.jenkins.io/doc/pipeline/steps/vk-notifier/#vksendstart-vknotifierstartsendstep)

*   [VncViewer Plugin](https://www.jenkins.io/doc/pipeline/steps/vncviewer/)
    *   [`wrap([$class: 'VncViewerBuildWrapper'])`: Enable VNC viewer](https://www.jenkins.io/doc/pipeline/steps/vncviewer/#wrapclass-vncviewerbuildwrapper-enable-vnc-viewer)

*   [vRealize Automation 8.x Plugin](https://www.jenkins.io/doc/pipeline/steps/vrealize-automation-8/)
    *   [`vraDeleteDeployment`: vRA - Delete Deployment](https://www.jenkins.io/doc/pipeline/steps/vrealize-automation-8/#vradeletedeployment-vra-delete-deployment)
    *   [`vraDeployFromCatalog`: vRA - Deploy from catalog](https://www.jenkins.io/doc/pipeline/steps/vrealize-automation-8/#vradeployfromcatalog-vra-deploy-from-catalog)
    *   [`vraGetDeployment`: vRA - Get Deployment](https://www.jenkins.io/doc/pipeline/steps/vrealize-automation-8/#vragetdeployment-vra-get-deployment)
    *   [`vraGetResourceActionDetails`: vRA - Get Resource Action Details](https://www.jenkins.io/doc/pipeline/steps/vrealize-automation-8/#vragetresourceactiondetails-vra-get-resource-action-details)
    *   [`vraGetResourceActions`: vRA - Get Resource Actions](https://www.jenkins.io/doc/pipeline/steps/vrealize-automation-8/#vragetresourceactions-vra-get-resource-actions)
    *   [`vraRunAction`: vRA - Run Action](https://www.jenkins.io/doc/pipeline/steps/vrealize-automation-8/#vrarunaction-vra-run-action)
    *   [`vraWaitForAddress`: vRA - Wait for Address](https://www.jenkins.io/doc/pipeline/steps/vrealize-automation-8/#vrawaitforaddress-vra-wait-for-address)

*   [vSphere Plugin](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/)
    *   [`step([$class: 'DeleteSnapshot'])`: Delete a Snapshot](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-deletesnapshot-delete-a-snapshot)
    *   [`step([$class: 'Deploy'])`: Deploy VM from template](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-deploy-deploy-vm-from-template)
    *   [`step([$class: 'ExposeGuestInfo'])`: Expose Guest Info](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-exposeguestinfo-expose-guest-info)
    *   [`step([$class: 'PowerOff'])`: Power-Off VM](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-poweroff-power-off-vm)
    *   [`step([$class: 'Reconfigure'])`: Reconfigure VM](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-reconfigure-reconfigure-vm)
    *   [`step([$class: 'Rename'])`: Rename VM](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-rename-rename-vm)
    *   [`step([$class: 'RenameSnapshot'])`: Rename Snapshot](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-renamesnapshot-rename-snapshot)
    *   [`step([$class: 'RevertToSnapshot'])`: Revert to Snapshot](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-reverttosnapshot-revert-to-snapshot)
    *   [`step([$class: 'SuspendVm'])`: Suspend VM](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-suspendvm-suspend-vm)
    *   [`step([$class: 'TakeSnapshot'])`: Take Snapshot](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-takesnapshot-take-snapshot)
    *   [`step([$class: 'VSphereBuildStepContainer'])`: vSphere Build Step](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#stepclass-vspherebuildstepcontainer-vsphere-build-step)
    *   [`vSphere`: Invoke an vSphere action, exposing the VM IP under some actions](https://www.jenkins.io/doc/pipeline/steps/vsphere-cloud/#vsphere-invoke-an-vsphere-action-exposing-the-vm-ip-under-some-actions)

*   [VSTest Runner plugin](https://www.jenkins.io/doc/pipeline/steps/vstestrunner/)
    *   [`vsTest`: Run unit tests with VSTest.console](https://www.jenkins.io/doc/pipeline/steps/vstestrunner/#vstest-run-unit-tests-with-vstest-console)

*   [Vulnerability Vines AI Plugin](https://www.jenkins.io/doc/pipeline/steps/vulnerability-vines-ai/)
    *   [`vinesScan`: Vines AI DAST Scan](https://www.jenkins.io/doc/pipeline/steps/vulnerability-vines-ai/#vinesscan-vines-ai-dast-scan)

*   [Wallarm Fast](https://www.jenkins.io/doc/pipeline/steps/wallarm-fast/)
    *   [`step([$class: 'WallarmFastBuilder'])`: WallarmFastBuilder](https://www.jenkins.io/doc/pipeline/steps/wallarm-fast/#stepclass-wallarmfastbuilder-wallarmfastbuilder)

*   [WAPT Pro plugin](https://www.jenkins.io/doc/pipeline/steps/waptpro/)
    *   [`step([$class: 'WaptPro'])`: Publish WAPT Pro reports](https://www.jenkins.io/doc/pipeline/steps/waptpro/#stepclass-waptpro-publish-wapt-pro-reports)
    *   [`waptProReport`: Publish WAPT Pro reports](https://www.jenkins.io/doc/pipeline/steps/waptpro/#waptproreport-publish-wapt-pro-reports)

*   [Warnings Plugin](https://www.jenkins.io/doc/pipeline/steps/warnings-ng/)
    *   [`publishIssues`: Publish issues created by a static analysis scan](https://www.jenkins.io/doc/pipeline/steps/warnings-ng/#publishissues-publish-issues-created-by-a-static-analysis-scan)
    *   [`recordIssues`: Record compiler warnings and static analysis results](https://www.jenkins.io/doc/pipeline/steps/warnings-ng/#recordissues-record-compiler-warnings-and-static-analysis-results)
    *   [`scanForIssues`: Scan files or the console log for warnings or issues](https://www.jenkins.io/doc/pipeline/steps/warnings-ng/#scanforissues-scan-files-or-the-console-log-for-warnings-or-issues)

*   [Warrior Framework Plugin](https://www.jenkins.io/doc/pipeline/steps/warrior/)
    *   [`step([$class: 'WarriorPluginBuilder'])`: Warrior Framework Plugin](https://www.jenkins.io/doc/pipeline/steps/warrior/#stepclass-warriorpluginbuilder-warrior-framework-plugin)

*   [Wattspeed](https://www.jenkins.io/doc/pipeline/steps/wattspeed/)
    *   [`wattspeed`: Wattspeed](https://www.jenkins.io/doc/pipeline/steps/wattspeed/#wattspeed-wattspeed)

*   [Wavefront Plugin](https://www.jenkins.io/doc/pipeline/steps/wavefront/)
    *   [`wavefrontTimedCall`: Sets up wavefront closure](https://www.jenkins.io/doc/pipeline/steps/wavefront/#wavefronttimedcall-sets-up-wavefront-closure)

*   [Web Security Application Project (WSAP)](https://www.jenkins.io/doc/pipeline/steps/wsap/)
    *   [`step([$class: 'WsapBuilder'])`: Web Security Application Project (WSAP)](https://www.jenkins.io/doc/pipeline/steps/wsap/#stepclass-wsapbuilder-web-security-application-project-wsap)

*   [Webhook Step Plugin](https://www.jenkins.io/doc/pipeline/steps/webhook-step/)
    *   [`registerWebhook`: Creates and returns a webhook that can be used by an external system to notify a pipeline](https://www.jenkins.io/doc/pipeline/steps/webhook-step/#registerwebhook-creates-and-returns-a-webhook-that-can-be-used-by-an-external-system-to-notify-a-pipeline)
    *   [`waitForWebhook`: Wait for webhook to be POSTed to by external system](https://www.jenkins.io/doc/pipeline/steps/webhook-step/#waitforwebhook-wait-for-webhook-to-be-posted-to-by-external-system)

*   [Websocket.in Notification Plugin](https://www.jenkins.io/doc/pipeline/steps/websocketin-notification/)
    *   [`websocketin`: Websocket.in Notifier](https://www.jenkins.io/doc/pipeline/steps/websocketin-notification/#websocketin-websocket-in-notifier)

*   [WeTest Automated Testing Plugin](https://www.jenkins.io/doc/pipeline/steps/wetest-automation/)
    *   [`wetest`: WeTest Automated Testing](https://www.jenkins.io/doc/pipeline/steps/wetest-automation/#wetest-wetest-automated-testing)

*   [Windows Exe Runner Plugin](https://www.jenkins.io/doc/pipeline/steps/windows-exe-runner/)
    *   [`runexe`: Windows Exe](https://www.jenkins.io/doc/pipeline/steps/windows-exe-runner/#runexe-windows-exe)

*   [WinRM Client Plugin](https://www.jenkins.io/doc/pipeline/steps/winrm-client/)
    *   [`winRMClient`: WinRM Client](https://www.jenkins.io/doc/pipeline/steps/winrm-client/#winrmclient-winrm-client)

*   [Wiz Scanner](https://www.jenkins.io/doc/pipeline/steps/wiz-scanner/)
    *   [`wizcli`: Wiz Scanner](https://www.jenkins.io/doc/pipeline/steps/wiz-scanner/#wizcli-wiz-scanner)

*   [Worksoft Continuous Test Manager Plugin](https://www.jenkins.io/doc/pipeline/steps/ws-ctm/)
    *   [`execMan`: Run Continuous Testing Manager Suite](https://www.jenkins.io/doc/pipeline/steps/ws-ctm/#execman-run-continuous-testing-manager-suite)

*   [Worksoft Execution Manager Plugin](https://www.jenkins.io/doc/pipeline/steps/ws-execution-manager/)
    *   [`execMan`: Run Execution Manager Request](https://www.jenkins.io/doc/pipeline/steps/ws-execution-manager/#execman-run-execution-manager-request)

*   [Workspace Cleanup Plugin](https://www.jenkins.io/doc/pipeline/steps/ws-cleanup/)
    *   [`cleanWs`: Delete workspace when build is done](https://www.jenkins.io/doc/pipeline/steps/ws-cleanup/#cleanws-delete-workspace-when-build-is-done)

*   [WXWork Notification Plugin](https://www.jenkins.io/doc/pipeline/steps/wxwork-notification/)
    *   [`wxwork`: 企业微信机器人通知](https://www.jenkins.io/doc/pipeline/steps/wxwork-notification/#wxwork-%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%9C%BA%E5%99%A8%E4%BA%BA%E9%80%9A%E7%9F%A5)

*   [Xcode integration](https://www.jenkins.io/doc/pipeline/steps/xcode-plugin/)
    *   [`importDeveloperProfile`: Import developer profile](https://www.jenkins.io/doc/pipeline/steps/xcode-plugin/#importdeveloperprofile-import-developer-profile)
    *   [`exportIpa`: Export IPA](https://www.jenkins.io/doc/pipeline/steps/xcode-plugin/#exportipa-export-ipa)
    *   [`unlockMacOSKeychain`: Unlock macOS X Keychain](https://www.jenkins.io/doc/pipeline/steps/xcode-plugin/#unlockmacoskeychain-unlock-macos-x-keychain)
    *   [`xcodeBuild`: Xcode](https://www.jenkins.io/doc/pipeline/steps/xcode-plugin/#xcodebuild-xcode)

*   [XebiaLabs XL Deploy Plugin](https://www.jenkins.io/doc/pipeline/steps/deployit-plugin/)
    *   [`xldCreatePackage`: Create a deployment package](https://www.jenkins.io/doc/pipeline/steps/deployit-plugin/#xldcreatepackage-create-a-deployment-package)
    *   [`xldDeploy`: Deploy a package to a environment](https://www.jenkins.io/doc/pipeline/steps/deployit-plugin/#xlddeploy-deploy-a-package-to-a-environment)
    *   [`xldPublishPackage`: Publish a deployment package to XLDeploy](https://www.jenkins.io/doc/pipeline/steps/deployit-plugin/#xldpublishpackage-publish-a-deployment-package-to-xldeploy)

*   [XebiaLabs XL Release Plugin](https://www.jenkins.io/doc/pipeline/steps/xlrelease-plugin/)
    *   [`xlrCreateRelease`: Create and invoke a XLR release](https://www.jenkins.io/doc/pipeline/steps/xlrelease-plugin/#xlrcreaterelease-create-and-invoke-a-xlr-release)

*   [XLRelease Variables Setter](https://www.jenkins.io/doc/pipeline/steps/xlrelease-var-setter/)
    *   [`step([$class: 'XLRVarSetterBuilder'])`: XL-Release Var Setter](https://www.jenkins.io/doc/pipeline/steps/xlrelease-var-setter/#stepclass-xlrvarsetterbuilder-xl-release-var-setter)

*   [Xooa](https://www.jenkins.io/doc/pipeline/steps/xooa/)
    *   [`xooa`: Upgrade Xooa app](https://www.jenkins.io/doc/pipeline/steps/xooa/#xooa-upgrade-xooa-app)

*   [Xray - Test Management for Jira Plugin](https://www.jenkins.io/doc/pipeline/steps/xray-connector/)
    *   [`step([$class: 'XrayExportBuilder'])`: Xray: Cucumber Features Export Task](https://www.jenkins.io/doc/pipeline/steps/xray-connector/#stepclass-xrayexportbuilder-xray-cucumber-features-export-task)
    *   [`step([$class: 'XrayImportBuilder'])`: Xray: Results Import Task](https://www.jenkins.io/doc/pipeline/steps/xray-connector/#stepclass-xrayimportbuilder-xray-results-import-task)
    *   [`step([$class: 'XrayImportFeatureBuilder'])`: Xray: Cucumber Features Import Task](https://www.jenkins.io/doc/pipeline/steps/xray-connector/#stepclass-xrayimportfeaturebuilder-xray-cucumber-features-import-task)

*   [xUnit plugin](https://www.jenkins.io/doc/pipeline/steps/xunit/)
    *   [`step([$class: 'XUnitPublisher'])`: Publish xUnit test result report](https://www.jenkins.io/doc/pipeline/steps/xunit/#stepclass-xunitpublisher-publish-xunit-test-result-report)
    *   [`xunit`: Publish xUnit test result report](https://www.jenkins.io/doc/pipeline/steps/xunit/#xunit-publish-xunit-test-result-report)

*   [Xvfb plugin](https://www.jenkins.io/doc/pipeline/steps/xvfb/)
    *   [`wrap([$class: 'Xvfb'])`: Start Xvfb before the build, and shut it down after.](https://www.jenkins.io/doc/pipeline/steps/xvfb/#wrapclass-xvfb-start-xvfb-before-the-build-and-shut-it-down-after)

*   [Xvnc plugin](https://www.jenkins.io/doc/pipeline/steps/xvnc/)
    *   [`xvnc`: Run Xvnc during build](https://www.jenkins.io/doc/pipeline/steps/xvnc/#xvnc-run-xvnc-during-build)

*   [Xygeni Sensor](https://www.jenkins.io/doc/pipeline/steps/xygeni-sensor/)
    *   [`xygeniSaltAtAdd`: Xygeni Salt Attestation 'Add' command](https://www.jenkins.io/doc/pipeline/steps/xygeni-sensor/#xygenisaltatadd-xygeni-salt-attestation-add-command)
    *   [`xygeniSaltAtCommit`: Xygeni Salt Attestation 'Commit' command](https://www.jenkins.io/doc/pipeline/steps/xygeni-sensor/#xygenisaltatcommit-xygeni-salt-attestation-commit-command)
    *   [`xygeniSaltAtInit`: Xygeni Salt Attestation 'Init' command](https://www.jenkins.io/doc/pipeline/steps/xygeni-sensor/#xygenisaltatinit-xygeni-salt-attestation-init-command)
    *   [`xygeniSaltAtRun`: Xygeni Salt Attestation 'Run' command](https://www.jenkins.io/doc/pipeline/steps/xygeni-sensor/#xygenisaltatrun-xygeni-salt-attestation-run-command)
    *   [`xygeniSaltAtSlsa`: Xygeni Salt Attestation 'Slsa Provenance' command](https://www.jenkins.io/doc/pipeline/steps/xygeni-sensor/#xygenisaltatslsa-xygeni-salt-attestation-slsa-provenance-command)
    *   [`xygeniSaltVerify`: Xygeni Salt 'Verify' command](https://www.jenkins.io/doc/pipeline/steps/xygeni-sensor/#xygenisaltverify-xygeni-salt-verify-command)

*   [Zanata Plugin](https://www.jenkins.io/doc/pipeline/steps/zanata/)
    *   [`step([$class: 'ZanataCliBuilder'])`: Zanata Sync via CLI](https://www.jenkins.io/doc/pipeline/steps/zanata/#stepclass-zanataclibuilder-zanata-sync-via-cli)
    *   [`step([$class: 'ZanataSyncStep'])`: Zanata Sync](https://www.jenkins.io/doc/pipeline/steps/zanata/#stepclass-zanatasyncstep-zanata-sync)

*   [ZAP Pipeline Plugin](https://www.jenkins.io/doc/pipeline/steps/zap-pipeline/)
    *   [`archiveZap`: Create & Archive ZAP report](https://www.jenkins.io/doc/pipeline/steps/zap-pipeline/#archivezap-create-archive-zap-report)
    *   [`configurePassiveRules`: Configures the list of passive rules to apply / avoid (](https://www.jenkins.io/doc/pipeline/steps/zap-pipeline/#configurepassiverules-configures-the-list-of-passive-rules-to-apply-avoid-httpswww-zaproxy-orgdocsalerts)[https://www.zaproxy.org/docs/alerts/](https://www.zaproxy.org/docs/alerts/)) 
    *   [`importZapScanPolicy`: Import a ZAP scan policy from the specified path](https://www.jenkins.io/doc/pipeline/steps/zap-pipeline/#importzapscanpolicy-import-a-zap-scan-policy-from-the-specified-path)
    *   [`importZapUrls`: Load a list of URLs for ZAP to use from the specified path](https://www.jenkins.io/doc/pipeline/steps/zap-pipeline/#importzapurls-load-a-list-of-urls-for-zap-to-use-from-the-specified-path)
    *   [`runZapAttack`: Run ZAP attack by changing to attack mode and starting the attack](https://www.jenkins.io/doc/pipeline/steps/zap-pipeline/#runzapattack-run-zap-attack-by-changing-to-attack-mode-and-starting-the-attack)
    *   [`runZapCrawler`: Run ZAP crawler on a specified host](https://www.jenkins.io/doc/pipeline/steps/zap-pipeline/#runzapcrawler-run-zap-crawler-on-a-specified-host)
    *   [`startZap`: Start ZAP process](https://www.jenkins.io/doc/pipeline/steps/zap-pipeline/#startzap-start-zap-process)
    *   [`stopZap`: Stop the ZAP instance.](https://www.jenkins.io/doc/pipeline/steps/zap-pipeline/#stopzap-stop-the-zap-instance)

*   [Zephyr](https://www.jenkins.io/doc/pipeline/steps/tm4j-automation/)
    *   [`downloadFeatureFiles`: Zephyr: Download Feature Files](https://www.jenkins.io/doc/pipeline/steps/tm4j-automation/#downloadfeaturefiles-zephyr-download-feature-files)
    *   [`publishTestResults`: Zephyr: Publish Test Results](https://www.jenkins.io/doc/pipeline/steps/tm4j-automation/#publishtestresults-zephyr-publish-test-results)

*   [Zephyr Enterprise Test Management plugin](https://www.jenkins.io/doc/pipeline/steps/zephyr-enterprise-test-management/)
    *   [`zeeReporter`: Publish test result to Zephyr Enterprise](https://www.jenkins.io/doc/pipeline/steps/zephyr-enterprise-test-management/#zeereporter-publish-test-result-to-zephyr-enterprise)

*   [zerobug Plugin](https://www.jenkins.io/doc/pipeline/steps/zerobug/)
    *   [`ZeroBugPublisher`: zerobug](https://www.jenkins.io/doc/pipeline/steps/zerobug/#zerobugpublisher-zerobug)

*   [Zoho QEngine](https://www.jenkins.io/doc/pipeline/steps/zohoqengine/)
    *   [`zohoQEngineTestPlanExecution`: Zoho QEngine Test Plan Execution](https://www.jenkins.io/doc/pipeline/steps/zohoqengine/#zohoqenginetestplanexecution-zoho-qengine-test-plan-execution)

*   [Zoho Sprints](https://www.jenkins.io/doc/pipeline/steps/zohosprints/)
    *   [`addSprintComment`: [Zoho Sprints] Add a sprint comment](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#addsprintcomment-zoho-sprints-add-a-sprint-comment)
    *   [`addSprintsReleaseComment`: [Zoho Sprints] Add a release comment](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#addsprintsreleasecomment-zoho-sprints-add-a-release-comment)
    *   [`completeSprint`: [Zoho Sprints] Complete a sprint](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#completesprint-zoho-sprints-complete-a-sprint)
    *   [`createSprints`: [Zoho Sprints] Create a sprint](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#createsprints-zoho-sprints-create-a-sprint)
    *   [`sprintsAddFeedStatus`: [Zoho Sprints] Add a feed status](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#sprintsaddfeedstatus-zoho-sprints-add-a-feed-status)
    *   [`sprintsAddWorkItem`: [Zoho Sprints] Create a work item](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#sprintsaddworkitem-zoho-sprints-create-a-work-item)
    *   [`sprintsAddWorkItemComment`: [Zoho Sprints] Add an item comment](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#sprintsaddworkitemcomment-zoho-sprints-add-an-item-comment)
    *   [`sprintsCreateRelease`: [Zoho Sprints] Create a release](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#sprintscreaterelease-zoho-sprints-create-a-release)
    *   [`sprintsUpdateRelease`: [Zoho Sprints] Update a release](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#sprintsupdaterelease-zoho-sprints-update-a-release)
    *   [`sprintsUpdateWorkItem`: [Zoho Sprints] Update a work item](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#sprintsupdateworkitem-zoho-sprints-update-a-work-item)
    *   [`startSprint`: [Zoho Sprints] Start a sprint](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#startsprint-zoho-sprints-start-a-sprint)
    *   [`updateSprints`: [Zoho Sprints] Update a sprint](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#updatesprints-zoho-sprints-update-a-sprint)
    *   [`wrap([$class: 'AddWorkItemOnFailure'])`: [Zoho Sprints] Create a work item on failure](https://www.jenkins.io/doc/pipeline/steps/zohosprints/#wrapclass-addworkitemonfailure-zoho-sprints-create-a-work-item-on-failure)

*   [Zoom Plugin](https://www.jenkins.io/doc/pipeline/steps/zoom/)
    *   [`zoomSend`: zoomSend](https://www.jenkins.io/doc/pipeline/steps/zoom/#zoomsend-zoomsend)

*   [Zowe zDevOps](https://www.jenkins.io/doc/pipeline/steps/zdevops/)
    *   [`allocateDS`: Allocate Dataset Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#allocateds-allocate-dataset-declarative)
    *   [`step([$class: 'AllocateDatasetStep'])`: [z/OS] - Allocate dataset](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-allocatedatasetstep-zos-allocate-dataset)
    *   [`deleteDataset`: Delete Dataset or Dataset member Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#deletedataset-delete-dataset-or-dataset-member-declarative)
    *   [`step([$class: 'DeleteDatasetStep'])`: [z/OS] - Delete dataset/member](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-deletedatasetstep-zos-delete-datasetmember)
    *   [`deleteDatasetsByMask`: Delete Datasets (bulk) by mask Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#deletedatasetsbymask-delete-datasets-bulk-by-mask-declarative)
    *   [`step([$class: 'DeleteDatasetsByMaskStep'])`: [z/OS] - Delete datasets by mask](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-deletedatasetsbymaskstep-zos-delete-datasets-by-mask)
    *   [`step([$class: 'DownloadDatasetStep'])`: [z/OS] - Download dataset/member](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-downloaddatasetstep-zos-download-datasetmember)
    *   [`downloadDS`: Download File Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#downloadds-download-file-declarative)
    *   [`performTsoCommand`: Perform TSO command Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#performtsocommand-perform-tso-command-declarative)
    *   [`step([$class: 'PerformTsoCommandStep'])`: [z/OS] - Perform TSO command](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-performtsocommandstep-zos-perform-tso-command)
    *   [`step([$class: 'SubmitJobStep'])`: [z/OS] - Submit job](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-submitjobstep-zos-submit-job)
    *   [`submitJob`: Submit Job Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#submitjob-submit-job-declarative)
    *   [`submitJobSync`: Submit Job Synchronously Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#submitjobsync-submit-job-synchronously-declarative)
    *   [`writeFileToMember`: Write file to Dataset Member Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#writefiletomember-write-file-to-dataset-member-declarative)
    *   [`writeFileToDS`: Write file to Dataset Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#writefiletods-write-file-to-dataset-declarative)
    *   [`step([$class: 'WriteFileToDatasetStep'])`: [z/OS] - Write file to dataset](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-writefiletodatasetstep-zos-write-file-to-dataset)
    *   [`writeFileToFile`: Write file to Unix file Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#writefiletofile-write-file-to-unix-file-declarative)
    *   [`step([$class: 'WriteFileToFileStep'])`: [z/OS] - Write file to USS file](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-writefiletofilestep-zos-write-file-to-uss-file)
    *   [`step([$class: 'WriteFileToMemberStep'])`: [z/OS] - Write file to member](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-writefiletomemberstep-zos-write-file-to-member)
    *   [`writeToDS`: Write to Dataset Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#writetods-write-to-dataset-declarative)
    *   [`step([$class: 'WriteToDatasetStep'])`: [z/OS] - Write text to dataset](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-writetodatasetstep-zos-write-text-to-dataset)
    *   [`writeToFile`: Write to Unix file Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#writetofile-write-to-unix-file-declarative)
    *   [`step([$class: 'WriteToFileStep'])`: [z/OS] - Write text to USS file](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-writetofilestep-zos-write-text-to-uss-file)
    *   [`writeToMember`: Write to Dataset Member Declarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#writetomember-write-to-dataset-member-declarative)
    *   [`step([$class: 'WriteToMemberStep'])`: [z/OS] - Write text to member](https://www.jenkins.io/doc/pipeline/steps/zdevops/#stepclass-writetomemberstep-zos-write-text-to-member)
    *   [`zosmf`: ZosmfStepDeclarative](https://www.jenkins.io/doc/pipeline/steps/zdevops/#zosmf-zosmfstepdeclarative)

*   [Zscaler IaC Scanner](https://www.jenkins.io/doc/pipeline/steps/zscaler-iac-scan/)
    *   [`wrap([$class: 'ZscalerScan'])`: Zscaler IaC scan](https://www.jenkins.io/doc/pipeline/steps/zscaler-iac-scan/#wrapclass-zscalerscan-zscaler-iac-scan)

*   [Zulip Plugin](https://www.jenkins.io/doc/pipeline/steps/zulip/)
    *   [`zulipNotification`: Zulip Notification](https://www.jenkins.io/doc/pipeline/steps/zulip/#zulipnotification-zulip-notification)
    *   [`zulipSend`: Zulip Send](https://www.jenkins.io/doc/pipeline/steps/zulip/#zulipsend-zulip-send)

* * *

[Was this page helpful?](https://www.jenkins.io/doc/pipeline/steps/#feedback)

Please submit your feedback about this page through this [quick form](https://www.jenkins.io/doc/feedback-form/).

Alternatively, if you don't wish to complete the quick form, you can simply indicate if you found this page helpful?

Yes No

Submit

See existing feedback [here](https://docs.google.com/spreadsheets/d/1IIdpVs39JDYKg0sLQIv-MNO928qcGApAIfdW5ohfD78).
