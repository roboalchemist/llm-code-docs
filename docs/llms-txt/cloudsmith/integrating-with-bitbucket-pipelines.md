# Source: https://help.cloudsmith.io/docs/integrating-with-bitbucket-pipelines.md

# Bitbucket Pipelines

How to integrate Bitbucket Pipelines with Cloudsmith

<Image align="center" width="100%" src="https://files.readme.io/c6dd79f-Cloudsmith-Integrations-Banner-Bitbucket.png" />

Cloudsmith provides first-class support for Bitbucket Pipelines with our official **Cloudsmith Publish** pipe. Using the pipe, Bitbucket users can easily integrate publishing to Cloudsmith with their existing pipeline workflows.

<HTMLBlock>
  {`
  <div class="row">
    <div class="col-xs-12 col-sm-6 col-md-4">
      <div class="cs-box cs-box-github">
        <a class="cs-link" href="https://bitbucket.org/cloudsmith-io/publish/"><strong>cloudsmith-pipes-publish</strong></a>
        <div><small>Bitbucket Pipe for publishing artifacts</small></div>
         <i class="fa fa-bitbucket"></i>
      </div>
    </div>
  </div>
  `}
</HTMLBlock>

![](https://files.readme.io/567426e-Bitbucket-Pipe-Cloudsmith-Publish.png "Bitbucket-Pipe-Cloudsmith-Publish.png")

Content below first appeared on the [Atlassian Community Blog](https://community.atlassian.com/t5/Marketplace-Apps-Integrations/Cloudsmith-Bitbucket/ba-p/1148691).

## Using Pipelines

The Cloudsmith pipe is included in Bitbucket's collection of officially maintained pipes and is available by default for any user that wishes to include it in their pipeline.

To use the pipe you'll first need an application or library that can be packaged into one of the formats that Cloudsmith support. You can see examples of Python and Javascript libraries in [Cloudsmith's Bitbucket account](https://bitbucket.org/cloudsmith-io/?_ga=2.35066210.2132496434.1565627316-1859711499.1556636245).

For the purposes of this example we'll assume you're using the Python example from the link above.

First, ensure that you can package your code using a Bitbucket pipeline by editing bitbucket-pipelines.yml in your repository. You can do so either via Bitbucket's web UI or using your normal editor and Git workflow.

For the example library, a basic pipeline that builds a package when a new tag is created looks like so:

```text
image:
  name: atlassian/default-image:2

build: &build
  step:
    name: Build Python Package
    image: python:3.7
    script:
    - python setup.py sdist
    artifacts:
    - dist/**

pipelines:
  tags:
    release-*:
    - <<: *build
```

This pipeline will build a new package each time you push an appropriate tag you your Bitbucket repository. The built package is then discarded as we have not yet added further instructions to tell Bitbucket what to do with it.

## Configuring the Pipe

Next we'll add publish the package to Cloudsmith using our official pipe. We'll need to provide an API Key that the pipe can use to authenticate with Cloudsmith. You can find the official documentation for pipeline variables in the [Bitbucket documentation](https://confluence.atlassian.com/bitbucket/variables-in-pipelines-794502608.html?_ga=2.261427278.2132496434.1565627316-1859711499.1556636245).

The API Key should be added as a "secure" variable (so it doesn't leak into logs) with the name `CLOUDSMITH_API_KEY`.

![](https://files.readme.io/86d5c32-bitbucket_cloudsmith_api_key.png "bitbucket_cloudsmith_api_key.png")

Once authentication is configured, you can add the pipe configuration to your pipeline.

If using the web UI to configure your pipeline, you can select the Cloudsmith pipe right from your browser, from within the list of supported pipes as in the image below:

![](https://files.readme.io/b8a9b79-cloudsmith_bitbucket_pipeline.png "cloudsmith_bitbucket_pipeline.png")

If using your local editor, you can follow the instructions in the [official README on Bitbucket](https://bitbucket.org/cloudsmith-io/publish?_ga=2.189666536.2132496434.1565627316-1859711499.1556636245).

Once added, your pipeline YAML should look something like so:

```text
image:
  name: atlassian/default-image:2

build: &build
  step:
    name: Build Python Package
    image: python:3.7
    script:
    - python setup.py sdist
    artifacts:
    - dist/**

publish: &publish
  step:
    name: Publish Python Package
    script:
    - pipe: cloudsmith-io/publish:0.1.1
      variables:
        CLOUDSMITH_REPOSITORY: 'cloudsmith/examples'
        CLOUDSMITH_API_KEY: $CLOUDSMITH_API_KEY
        PACKAGE_FORMAT: 'python'
        PACKAGE_PATH: 'dist/*.tar.gz'

pipelines:
  tags:
    release-*:
    - <<: *build
    - <<: *publish
```

This configuration instructs the pipe to push artifacts to the [cloudsmith/examples](https://cloudsmith.io/~cloudsmith/repos/examples/packages/) repository, with the API key we stored earlier. We're uploading a python package which is located at dist/\*.tar.gz.

## Using the Pipe

And that's it! Your pipe is now configured and ready to run. You should be able to push a new tag to Bitbucket and see your pipe run.

Bitbucket's pipeline UI provides a great overview of the status of your jobs:

![](https://files.readme.io/3d6382e-cloudsmith_bitbucket_pipeline_ui.png "cloudsmith_bitbucket_pipeline_ui.png")

Once pushed, you should see your new package in the Cloudsmith UI, ready for download and install using your preferred tools:

<Image align="center" src="https://files.readme.io/17934157a14c18b708414fc10bdfcd44dc76f63093c8cb085da239ef0727fe45-bitbucket-cloudsmith-package.png" />

## Conclusion

Cloudsmith's Bitbucket pipe provides the easiest and simplest way for Bitbucket users to push their assets to [Cloudsmith](http://cloudsmith.com). Get started now.

> 📘 Officially Maintained
>
> Our official pipe is maintained by the Cloudsmith team and you can be sure it'll be kept up to date with all changes and features as we release them.