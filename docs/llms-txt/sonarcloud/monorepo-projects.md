# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/monorepo-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/monorepo-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/monorepo-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/monorepo-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/monorepo-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/monorepo-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/monorepo-projects.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/monorepo-projects.md

# Monorepo projects

You can add the SonarQube Cloud analysis to your Azure build pipeline for a monorepo.

Proceed as follows:

1. If not already done, import your monorepo to create the corresponding projects in SonarQube Cloud: see the [monorepo-support](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/monorepo-support "mention") page.
2. For each project, configure your [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention").
3. For each project, set up the integration features. See the [azure-devops](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/devops-platform-integration/azure-devops "mention") page for more details.
4. Add the SonarQube Cloud analysis to your YAML pipeline. To do so, see the section corresponding to your project type and use the YAML file example below add analysis to a:
   * [gradle-or-maven-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/gradle-or-maven-project "mention")
   * [dotnet-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/dotnet-project "mention")
   * [c-family-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/c-family-project "mention")
   * [js-ts-go-python-php](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/js-ts-go-python-php "mention")

### Typical YAML file example for a monorepo analysis <a href="#yaml-file-example" id="yaml-file-example"></a>

```yaml
# Template pipeline that build 2 distinct .NET projects, living in 2 separate folders in the repo. We are analyzing them on SonarQube Cloud, each targets a specific SonarQube Cloud project.
 
trigger:
- main # or another name representing your main branch
 
pool:
 vmImage: windows-latest
 
steps:
- task: VisualStudioTestPlatformInstaller@1
 inputs:
   packageFeedSelector: 'nugetOrg'
   versionSelector: 'latestPreRelease'
 
- task: UseDotNet@2
 inputs:
   packageType: 'sdk'
   version: '6.x'
   includePreviewVersions: true
 
- task: NuGetToolInstaller@1
 inputs:
   versionSpec: '5.9.0'
   checkLatest: true
 
- task: DotNetCoreCLI@2
 inputs:
   command: 'restore'
   projects: '**/*.sln'
   feedsToUse: 'select'
 
- task: SonarCloudPrepare@4
 inputs:
   SonarCloud: '<YourSonarqubeServiceEndpoint>'
   scannerMode: 'dotnet'
   projectKey: 'myRepo_myProject1'
 
- task: DotNetCoreCLI@2
 inputs:
   command: 'build'
   projects: 'myproject1/solution.sln'
   arguments: '/nr:false' // this flag is important to avoid DLL lock for the 2nd build/analysis
 
- task: SonarCloudAnalyze@4
 
- task: SonarCloudPrepare@4
 inputs:
   SonarCloud: '<YourSonarqubeServiceEndpoint>'
   scannerMode: 'dotnet'
   projectKey: 'myRepo_myProject2'
 
- task: DotNetCoreCLI@2
 inputs:
   command: 'build'
   projects: 'myProject2/solution.sln'
   arguments: '/nr:false'
 
- task: SonarCloudAnalyze@4
```
