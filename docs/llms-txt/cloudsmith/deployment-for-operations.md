# Source: https://help.cloudsmith.io/docs/deployment-for-operations.md

# Deployment (for Operations)

<HTMLBlock>
  {`
  <div class="cs-headline">Cloudsmith provides a stable platform from which to deploy software assets and integrates with leading infrastructure-as-code tools.</div>
  `}
</HTMLBlock>

<HTMLBlock>
  {`
  <div class="row cs-box-row">
  <div class="cs-box-50"> 
     <br>  <p>
    Cloudsmith provides a safe haven for all your software assets; whether they be npm packages or Docker images. With multiple authentication methods; Cloudsmith is ideally suited to provide the artifacts and packages required to build your infrastructure; whether it be an EC2 box or a full Kubernetes cluster.
      <br><br>
    <p>
    Promote and track assets through your pipelines; building a provenance trail of all deployed software.
  </div>
    <div class="cs-box-50">
      <img src="https://files.readme.io/ceb30eb-CS_Development_Pipeline.svg" />
  </div>
  </div>
  `}
</HTMLBlock>

<HTMLBlock>
  {`
  <div class="row cs-box-row">
      <div class="cs-box cs-box-grey cs-box-50">
        <div class="cs-box-title">Automation</div>
        <div class="cs-box-text">Configure for automated deployments 
        </div>
         <ul>
           <li><a href="https://help.cloudsmith.io/docs/bot-service-accounts">Bot Service Accounts</a></li>
           <li><a href="https://help.cloudsmith.io/docs/webhooks">Webhooks</a></li>
            <li><a href="https://help.cloudsmith.io/docs/package-tags">Package Tags</a></li>
        </ul>
    </div>
      <div class="cs-box cs-box-grey cs-box-50"><div class="cs-box-title">Platform</div>
        <div class="cs-box-text">
      Stability to drive deployments
        </div>
        <ul><li><a href="https://help.cloudsmith.io/docs/operational-performance">Operational Performance</a></li>
          <li><a href="https://help.cloudsmith.io/docs/security">Security</a></li><li><a href="https://status.cloudsmith.io">Status</a></li>
        </ul>
      </div>
  </div>
  `}
</HTMLBlock>

## Integrate with any Continuous Deployment tooling

Cloudsmith can integrate with any CI/CD or CCA tool through a number of methods (first-class integration, API, CLI, or native format tooling).

* [Ansible](https://help.cloudsmith.io/docs/integrating-ansible)
* [AWS CodeBuild](https://help.cloudsmith.io/docs/integrating-with-aws-codebuild)
* [Bitbucket Pipelines](https://help.cloudsmith.io/docs/integrating-with-bitbucket-pipelines)
* [Buildkite](https://help.cloudsmith.io/docs/integrating-with-buildkite)
* [Chef](https://help.cloudsmith.io/docs/integrating-chef)
* [CircleCI](https://help.cloudsmith.io/docs/integrations-circleci)
* [Drone CI](https://help.cloudsmith.io/docs/integrating-with-drone-ci)
* [GitLab CI/CD](https://help.cloudsmith.io/docs/gitlab-cicd)
* [GitHub Actions](https://help.cloudsmith.io/docs/integrating-with-github-actions)
* [Harness CD](https://help.cloudsmith.io/docs/integrating-harness)
* [Jenkins](https://help.cloudsmith.io/docs/integrating-with-jenkins)
* [Octopus Deploy](https://help.cloudsmith.io/docs/integrating-octopus-deploy)
* [Puppet](https://help.cloudsmith.io/docs/integrating-puppet)
* [Terraform](https://help.cloudsmith.io/docs/integrating-terraform)
* [Travis-CI](https://help.cloudsmith.io/docs/integrating-with-travis-ci)

## Provenance: Promote Assets for Deployment

Use webhooks to automate deployment pipelines and promote assets. On Cloudsmith, you can mirror your production pipeline and manage assets in logical groupings such as development, test, staging, and production.

Once you upload an asset, you can move it from development -> test -> staging -> production keeping the integrity of the asset and a provenance trail, without the bandwidth cost of downloading from staging and then re-uploading to production.