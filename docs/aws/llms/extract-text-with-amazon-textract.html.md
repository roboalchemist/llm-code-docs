# Source: https://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html

<!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en-US"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title>Extract information from unstructured documents with Amazon Bedrock and Amazon Textract - Extract information from unstructured documents with Amazon Bedrock and Amazon Textract</title><meta name="viewport" content="width=device-width,initial-scale=1" /><meta name="assets_root" content="/assets" /><meta name="target_state" content="extract-text-with-amazon-textract" /><meta name="default_state" content="extract-text-with-amazon-textract" /><link rel="icon" type="image/ico" href="/assets/images/favicon.ico" /><link rel="shortcut icon" type="image/ico" href="/assets/images/favicon.ico" /><link rel="canonical" href="https://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" /><meta name="description" content="In this tutorial, you will learn how to utilize Amazon Bedrock and Amazon Textract to extract and process information from unstructured documents." /><meta name="deployment_region" content="IAD" /><meta name="product" content="Extract information from unstructured documents with Amazon Bedrock and Amazon Textract" /><meta name="guide" content="Hands-on tutorials" /><meta name="abstract" content="In this tutorial, you will learn how to utilize Amazon Bedrock and Amazon Textract to extract and process information from unstructured documents." /><meta name="guide-locale" content="en_us" /><meta name="tocs" content="toc-contents.json" /><link rel="canonical" href="https://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" /><link rel="alternative" href="https://docs.aws.amazon.com/id_id/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="id-id" /><link rel="alternative" href="https://docs.aws.amazon.com/id_id/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="id" /><link rel="alternative" href="https://docs.aws.amazon.com/de_de/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="de-de" /><link rel="alternative" href="https://docs.aws.amazon.com/de_de/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="de" /><link rel="alternative" href="https://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="en-us" /><link rel="alternative" href="https://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="en" /><link rel="alternative" href="https://docs.aws.amazon.com/es_es/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="es-es" /><link rel="alternative" href="https://docs.aws.amazon.com/es_es/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="es" /><link rel="alternative" href="https://docs.aws.amazon.com/fr_fr/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="fr-fr" /><link rel="alternative" href="https://docs.aws.amazon.com/fr_fr/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="fr" /><link rel="alternative" href="https://docs.aws.amazon.com/it_it/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="it-it" /><link rel="alternative" href="https://docs.aws.amazon.com/it_it/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="it" /><link rel="alternative" href="https://docs.aws.amazon.com/ja_jp/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="ja-jp" /><link rel="alternative" href="https://docs.aws.amazon.com/ja_jp/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="ja" /><link rel="alternative" href="https://docs.aws.amazon.com/ko_kr/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="ko-kr" /><link rel="alternative" href="https://docs.aws.amazon.com/ko_kr/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="ko" /><link rel="alternative" href="https://docs.aws.amazon.com/pt_br/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="pt-br" /><link rel="alternative" href="https://docs.aws.amazon.com/pt_br/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="pt" /><link rel="alternative" href="https://docs.aws.amazon.com/zh_cn/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="zh-cn" /><link rel="alternative" href="https://docs.aws.amazon.com/zh_tw/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="zh-tw" /><link rel="alternative" href="https://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" hreflang="x-default" /><meta name="feedback-folder" content="f8f24ea3-648d-452a-b7b1-9ea97afb6055" /><meta name="this_doc_product" content="Extract information from unstructured documents with Amazon Bedrock and Amazon Textract" /><meta name="this_doc_guide" content="Hands-on tutorials" /><head xmlns="http://www.w3.org/1999/xhtml"> <script defer="" src="/assets/r/awsdocs-doc-page.2.0.0.js"></script><link href="/assets/r/awsdocs-doc-page.2.0.0.css" rel="stylesheet"/></head>
<script defer="" id="awsc-panorama-bundle" type="text/javascript" src="https://prod.pa.cdn.uis.awsstatic.com/panorama-nav-init.js" data-config="{'appEntity':'aws-documentation','region':'us-east-1','service':'hands-on'}"></script><meta id="panorama-serviceSubSection" value="Hands-on tutorials" /><meta id="panorama-serviceConsolePage" value="Extract information from unstructured documents with Amazon Bedrock and Amazon Textract" /><meta name="uiVersion" content="2024.10" /></head><body class="awsdocs awsui"><div class="awsdocs-container"><awsdocs-header></awsdocs-header><awsui-app-layout id="app-layout" class="awsui-util-no-gutters" ng-controller="ContentController as $ctrl" header-selector="awsdocs-header" navigation-hide="false" navigation-width="$ctrl.navWidth" navigation-open="$ctrl.navOpen" navigation-change="$ctrl.onNavChange($event)" tools-hide="$ctrl.hideTools" tools-width="$ctrl.toolsWidth" tools-open="$ctrl.toolsOpen" tools-change="$ctrl.onToolsChange($event)"><div id="guide-toc" dom-region="navigation"><awsdocs-toc></awsdocs-toc></div><div id="main-column" dom-region="content" tabindex="-1"><awsdocs-view class="awsdocs-view"><div id="awsdocs-content"><head><title>Extract information from unstructured documents with Amazon Bedrock and Amazon Textract - Extract information from unstructured documents with Amazon Bedrock and Amazon Textract</title><meta name="pdf" content="/pdfs/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.pdf#extract-text-with-amazon-textract" /><meta name="forums" content="https://repost.aws/search/content?globalSearch=AWS Hands-on Tutorials" /><meta name="feedback" content="https://docs.aws.amazon.com/forms/aws-doc-feedback?feedback_destination_id=f8f24ea3-648d-452a-b7b1-9ea97afb6055&amp;topic_url=https://docs.aws.amazon.com/en_us/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" /><meta name="feedback-yes" content="feedbackyes.html?topic_url=https://docs.aws.amazon.com/en_us/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" /><meta name="feedback-no" content="feedbackno.html?topic_url=https://docs.aws.amazon.com/en_us/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html" /><meta name="keywords" content="Extract information from unstructured documents with Amazon Bedrock and Amazon Textract,hands-on,hands-on tutorials" /><script type="application/ld+json">
{
    "@context" : "https://schema.org",
    "@type" : "BreadcrumbList",
    "itemListElement" : [
      {
        "@type" : "ListItem",
        "position" : 1,
        "name" : "AWS",
        "item" : "https://aws.amazon.com"
      },
      {
        "@type" : "ListItem",
        "position" : 2,
        "name" : "AWS Hands-on Tutorials",
        "item" : "https://aws.amazon.com/getting-started/hands-on/"
      },
      {
        "@type" : "ListItem",
        "position" : 3,
        "name" : "Hands-on tutorials",
        "item" : "https://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract"
      },
      {
        "@type" : "ListItem",
        "position" : 4,
        "name" : "Extract information from unstructured documents with Amazon Bedrock and Amazon Textract",
        "item" : "https://docs.aws.amazon.com/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html"
      }
    ]
}
</script></head><body><div id="main"><div style="display: none"><a href="/pdfs/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.pdf#extract-text-with-amazon-textract" target="_blank" rel="noopener noreferrer" title="Open PDF"></a></div><div id="breadcrumbs" class="breadcrumb"><a href="/index.html">Documentation</a><a href="https://aws.amazon.com/getting-started/hands-on/">AWS Hands-on Tutorials</a><a href="extract-text-with-amazon-textract.html">Hands-on tutorials</a></div><div id="page-toc-src"><a href="#overview">Overview</a><a href="#what-you-will-accomplish">What you will accomplish</a><a href="#prerequisites">Prerequisites</a><a href="#implementation">Implementation</a><a href="#congratulations">Congratulations</a></div><awsdocs-doc-page-banner></awsdocs-doc-page-banner><div id="main-content" class="awsui-util-container"><div id="main-col-body"><awsdocs-language-banner data-service="$ctrl.pageService"></awsdocs-language-banner><h1 class="topictitle" id="extract-text-with-amazon-textract">Extract information from unstructured documents with Amazon Bedrock and Amazon Textract</h1><div class="awsdocs-page-header-container"><awsdocs-page-header></awsdocs-page-header><awsdocs-filter-selector id="awsdocs-filter-selector"></awsdocs-filter-selector></div><div class="table-container"><div class="table-contents disable-scroll"><table id="w55aab5b3">
        <tr>
          <td tabindex="-1">
            <p><b>AWS experience</b></p>
          </td>
          <td tabindex="-1">
            <p>Beginner </p>
          </td>
        </tr>
        <tr>
          <td tabindex="-1">
            <p><b>Time to complete</b></p>
          </td>
          <td tabindex="-1">
            <p>20 minutes </p>
          </td>
        </tr>
        <tr>
          <td tabindex="-1">
            <p><b>Cost to complete</b></p>
          </td>
          <td tabindex="-1">
            <p>Less than $0.15 if completed within two hours and the notebook is deleted at the
              end of the tutorial. </p>
          </td>
        </tr>
        <tr>
          <td tabindex="-1">
            <p><b>Get help</b></p>
          </td>
          <td tabindex="-1">
            <p><a href="https://docs.aws.amazon.com/bedrock/latest/userguide/fine-tuning-troubleshooting.html">Troubleshooting
                Amazon Bedrock models</a>
            </p>
            <p><a href="https://docs.aws.amazon.com/textract/latest/dg/textract-debugging-failures-adapters.html">Debugging traning
                issues</a>
            </p>
          </td>
        </tr>
        <tr>
          <td tabindex="-1">
            <p><b>Last update</b></p>
          </td>
          <td tabindex="-1">
            <p>November 14, 2024 </p>
          </td>
        </tr>
      </table></div></div>
  <h2 id="overview">Overview</h2>
    <p>In this tutorial, you will learn how to utilize Amazon Bedrock and
      Amazon Textract to extract and process information from
      unstructured documents.
    </p>
    <p>Amazon Bedrock is a fully managed service that offers a choice of
      high-performing foundation models (FMs) from leading AI companies
      like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI,
      and Amazon through a single API, along with a broad set of
      capabilities you need to build generative AI applications with
      security, privacy, and responsible AI.
    </p>
    <p>Amazon Textract is a machine learning (ML) service that
      automatically extracts text, handwriting, layout elements, and
      data from scanned documents.
    </p>
   
  <h2 id="what-you-will-accomplish">What you will accomplish</h2>
    <p>In this tutorial, you will:
    </p>
    <div class="itemizedlist">
       
       
       
       
    <ul class="itemizedlist"><li class="listitem">
        <p>Enable access to a foundation model on your AWS account
        </p>
      </li><li class="listitem">
        <p>Create a new Jupyter notebook to write test code and run tests
        </p>
      </li><li class="listitem">
        <p>Generate code
        </p>
      </li><li class="listitem">
        <p>Clean up your resources
        </p>
      </li></ul></div>
   
  <h2 id="prerequisites">Prerequisites</h2>
    <p>Before starting this tutorial, you will need:
    </p>
    <div class="itemizedlist">
       
    <ul class="itemizedlist"><li class="listitem">
        <p>An AWS account: if you don't already have one follow
          theÂ <a href="https://docs.aws.amazon.com/hands-on/latest/setup-environment/">Setup
          Your Environment</a> tutorial.
        </p>
      </li></ul></div>
   
  <h2 id="implementation">Implementation</h2>

    
  




<div class="collapsible" data-expand-section="_collapse_all_"><awsui-expandable-section variant="container" header="Step 1: Enable Anthropic FM" id="enable-anthropic-fm" expanded="false"><p>In this step, you will enable the use of Anthropic models on your
    AWS account.
  </p><div class="awsdocs-note"><div class="awsdocs-note-title"><awsui-icon name="status-info" variant="link"></awsui-icon><h6>Note</h6></div><div class="awsdocs-note-text"><p><b>Already requested and obtained access to Anthropic models on
              Amazon Bedrock?</b> Skip to <a href="#create-a-jupyter-notebook">Step 2: Create a Jupyter Notebook</a>.</p></div></div><div class="procedure"><ol><li>
      <p>Open Amazon Bedrock</p>
<p><b>Sign in</b> to the AWS Management
      console, and <b>open</b> the Amazon
      Bedrock console at
      <a href="https://console.aws.amazon.com/bedrock/home" rel="noopener noreferrer" target="_blank"><span>https://console.aws.amazon.com/bedrock/home</span><awsui-icon class="awsdocs-link-icon" name="external"></awsui-icon></a>.
    </p>
    <p>In the left navigation pane, under <b>Bedrock
      configurations</b>, choose <b>Model
      Access</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/navigation-interface.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="The navigation interface." />
       
       
    </div>
  
    </li><li>
      <p>Enable a model</p>
<p>On the <b>What is Model access?</b>
      page, choose <b>Enable specific
      models</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/bedrock-model-access-page-options-enable.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="Amazon Bedrock model access page with options to enable all models or enable specific models, and links to IAM permissions and quotas." />
       
       
    </div>
  
    </li><li>
      <p>Choose the Anthropic models</p>
<p>On the <b>Edit model access</b> page,
      select the <b>Anthropic models</b>,
      and choose <b>Next</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/user-interface-editing-model-access-list.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="A user interface for editing model access, showing a list of AI models grouped by provider, with all models under &#34;Anthropic&#34; selected and the &#34;Next&#34; button highlighted." />
       
       
    </div>
  
    </li><li>
      <p>Review and submit the change</p>
<p>On the <b>Review and submit</b> page,
      review your selections, and choose
      <b>Submit</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/interface-editing-model-access-listing.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="Interface for editing model access in AWS, listing eight Claude models with 'Request access' options, and a 'Submit' button highlighted at the bottom." />
       
       
    </div>
  
    </li></ol></div></awsui-expandable-section><awsui-expandable-section variant="container" header="Step 2: Create a Jupyter Notebook" id="create-a-jupyter-notebook" expanded="false"><p>In this step, you will create a Jupyter notebook to write your
    Proof-of-Concept code and test it out with real documents.
  </p><div class="procedure"><ol><li>
      <p>Open Amazon SageMaker AI</p>
<p><b>Open</b> the Amazon Sagemaker
      console at
      <a href="https://console.aws.amazon.com/sagemaker/home" rel="noopener noreferrer" target="_blank"><span>https://console.aws.amazon.com/sagemaker/home</span><awsui-icon class="awsdocs-link-icon" name="external"></awsui-icon></a>.
    </p>
    <p>In the left navigation pane, under
      <b>Applications and IDEs</b>, choose
      <b>Notebooks</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/navigation-interface-1.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="The navigation interface." />
       
       
    </div>
  
    </li><li>
      <p>Create a notebook instance</p>
<p>On the <b>Notebooks and Git repos</b>
      page, choose <b>Create notebook
      instance</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/interface-notebook-instances-tab-resources.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="Amazon SageMaker AI interface showing the &#34;Notebook instances&#34; tab with no resources listed and an orange &#34;Create notebook instance&#34; button highlighted." />
       
       
    </div>
  
    </li><li>
      <p>Configure notebook instance settings</p>
<p>On the <b>Create notebook instance</b>
      page:
    </p>
    <p>In the <b>Notebook instance
      settings</b> section:
    </p>
    <div class="itemizedlist">
       
       
       
    <ul class="itemizedlist"><li class="listitem">
        <p>For <b>Notebook instance name</b>,
          enter a <b>name</b> for your
          Jupyter instance.
        </p>
      </li><li class="listitem">
        <p>For <b>Notebook instance type</b>,
          verify <b>ml.t3.medium</b> is
          selected.
        </p>
      </li><li class="listitem">
        <p>Keep all other default settings.
        </p>
      </li></ul></div>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/interface-creating-notebook-instance.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="Amazon SageMaker AI interface for creating a notebook instance, showing settings for instance name, type, IAM role creation success, and the 'Create notebook instance' button highlighted." />
       
       
    </div>
  
    </li><li>
      <p>Configure permissions and encryption</p>
<p>In the <b>Permissions and
      encryption</b> section:
    </p>
    <div class="itemizedlist">
       
       
    <ul class="itemizedlist"><li class="listitem">
        <p>For <b>IAM role</b>, choose
          <b>Create a new role</b>.
        </p>
      </li><li class="listitem">
        <p>On the <b>Create an IAM role</b>
          pop up window, for <b>S3 buckets you
          specify</b> â <b>optional</b>, choose
          <b>None</b>, and then choose
          <b>Create role</b>.
        </p>
      </li></ul></div>
    <p>Then, choose <b>Create notebook
      instance</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/iam-role-creation-screen-bucket-access.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="AWS IAM role creation screen with S3 bucket access options, 'None' selected, and 'Create role' button highlighted." />
       
       
    </div>
  
    </li></ol></div></awsui-expandable-section><awsui-expandable-section variant="container" header="Step 3: Generate code to process your documents" id="generate-code-to-process-your-documents" expanded="false"><p>In this step, you will use Bedrock playground to generate code for
    your Jupyter notebook.
  </p><div class="procedure"><ol><li>
      <p>Open JupyterLab</p>
<p>On the <b>Notebook instance</b> page,
      choose <b>Open JupyterLab</b> for the
      instance you created in the previous step. Â 
    </p>
    <div class="awsdocs-note"><div class="awsdocs-note-title"><awsui-icon name="status-info" variant="link"></awsui-icon><h6>Note</h6></div><div class="awsdocs-note-text"><p>The notebook will open in
      a separate browser tab.</p></div></div>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/navigation-interface-2.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="The navigation interface." />
       
       
    </div>
  
    </li><li>
      <p>Create a new notebook</p>
<p>On the <b>JupyterLab</b> tab,
      right-click the file area, and then select
      <b>New Notebook</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/jupyterlab-interface-context-menu-new.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="A JupyterLab interface showing a context menu with the &#34;New Notebook&#34; option highlighted in red." />
       
       
    </div>
  
    </li><li>
      <p>Select kernel</p>
<p>On the <b>Select Kernel</b> pop up
      window, choose <b>conda_python3</b>,
      and choose <b>Select</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/dialog-box-titled-select-kernel-dropdown.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="Dialog box titled &#34;Select Kernel&#34; with a dropdown showing &#34;conda_python3&#34; selected and two buttons: &#34;No Kernel&#34; and &#34;Select.&#34;." />
       
       
    </div>
  
    </li><li>
      <p>Open the chat playground</p>
<p>In a new tab, <b>open</b> the Amazon
      Bedrock console at
      <a href="https://console.aws.amazon.com/bedrock/home" rel="noopener noreferrer" target="_blank"><span>https://console.aws.amazon.com/bedrock/home</span><awsui-icon class="awsdocs-link-icon" name="external"></awsui-icon></a>.
    </p>
    <p>In the left navigation pane, under
      <b>Playgrounds</b>, choose
      <b>Chat/text</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/bedrock-interface-navigation-options-left.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="Amazon Bedrock interface showing navigation options on the left, including &#34;Playgrounds&#34; with &#34;Chat/text&#34; highlighted, and foundation model options on the right." />
       
       
    </div>
  
    </li><li>
      <p>Select the model</p>
<p>On the <b>Mode</b> page, choose
      <b>Select model</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/bedrock-interface-select-model-button.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="Amazon Bedrock interface showing a &#34;Select model&#34; button highlighted in orange, with options for input, output, and latency." />
       
       
    </div>
  
    </li><li>
      <p>Specify the model details</p>
<p>In the <b>Select model</b> dialog box:
    </p>
    <div class="itemizedlist">
       
       
       
    <ul class="itemizedlist"><li class="listitem">
        <p>For <b>Categories</b>, choose
          <b>Anthropic</b>.
        </p>
      </li><li class="listitem">
        <p>For <b>Models with access</b>,
          choose the <b>Claude 3.5
          Sonnet</b> model.
        </p>
      </li><li class="listitem">
        <p>Then, choose <b>Apply</b>.
        </p>
      </li></ul></div>
    <div class="awsdocs-note"><div class="awsdocs-note-title"><awsui-icon name="status-info" variant="link"></awsui-icon><h6>Note</h6></div><div class="awsdocs-note-text"><p>The Claude 3.5 Sonnet is
      the most intelligent model from Anthropic. You can see a more
      detailed model comparison
      <a href="https://docs.anthropic.com/en/docs/about-claude/models" rel="noopener noreferrer" target="_blank"><span>here</span><awsui-icon class="awsdocs-link-icon" name="external"></awsui-icon></a>.</p></div></div>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/model-selection-interface-anthropic-chosen.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="A model selection interface showing &#34;Anthropic&#34; as the chosen provider, &#34;Claude 3.5 Sonnet&#34; as the selected model, and an &#34;Apply&#34; button highlighted in orange." />
       
       
    </div>
  
    </li><li>
      <p>Generate code</p>
<p>In the <b>Chat playground</b>, you can
      now ask the LLM to write sample code. The following is an example
      prompt that you can use to extract information from an
      unstructured document.
    </p>
    <pre class="programlisting"><div class="code-btn-container"><div class="btn-copy-code" title="Copy"><awsui-icon name="copy"></awsui-icon></div></div><!--DEBUG: cli ()--><code class="">
I am writing a Jupyter notebook with a proof of concept python code snippets to perform a few tasks. 
To start, write a snippet to iterate the current folder and read all the jpg/png files and for each file call textract DetectDocumentText API to extract all the text on the image.
Re-save the result with the same file name and txt extension.
Also make sure to: 
- Not reprocess any files that already have the txt file existing in the directory 
- Print a progress bar output using tdqm 
- Keep everything readable and properly componentized in methods 
- No need for __main__ implementations as it's a snippet to run on Jupyter notebook.
</code></pre>
    <p>Once you enter your prompt, and choose
      <b>Run</b>, the prompt response will
      include code and also explanation of everything that the model
      generated. The code will typically be enclosed in quotation marks.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/bedrock-chat-text-playground-interface.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="Amazon Bedrock's Chat/text playground interface with a prompt about writing a Python script for text extraction using the DetectDocumentText API in a Jupyter notebook." />
       
       
    </div>
  
    </li><li>
      <p>Check the output</p>
<p>The generated code with the example prompt should look similar to
      the following example. You can also use the
      <b>copy</b> function to
      <b>paste</b> the code directly into
      the Jupyter notebook.
    </p>
    <pre class="programlisting"><div class="code-btn-container"><div class="btn-copy-code" title="Copy"><awsui-icon name="copy"></awsui-icon></div></div><!--DEBUG: cli (none)--><code class="nohighlight">import os
import boto3
from tqdm import tqdm
from PIL import Image

def get_image_files(directory):
    """Get all jpg and png files in the given directory."""
    return [f for f in os.listdir(directory) if f.lower().endswith(('.jpg', '.png'))]

def should_process_file(file_path):
    """Check if the file should be processed (i.e., no corresponding txt file exists)."""
    txt_path = os.path.splitext(file_path)[0] + '.txt'
    return not os.path.exists(txt_path)

def extract_text_from_image(image_path):
    """Extract text from the image using Amazon Textract."""
    client = boto3.client('textract')

    with open(image_path, 'rb') as image:
        response = client.detect_document_text(Document=<span>{</span>'Bytes': image.read()})

    extracted_text = []
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            extracted_text.append(item['Text'])

    return '\n'.join(extracted_text)

def save_text_to_file(text, file_path):
    """Save the extracted text to a file."""
    txt_path = os.path.splitext(file_path)[0] + '.txt'
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

def process_images_in_directory(directory):
    """Process all images in the given directory."""
    image_files = get_image_files(directory)

    for image_file in tqdm(image_files, desc="Processing images"):
        image_path = os.path.join(directory, image_file)

        if should_process_file(image_path):
            extracted_text = extract_text_from_image(image_path)
            save_text_to_file(extracted_text, image_path)

# Usage in Jupyter notebook
directory = '.'  # Current directory
process_images_in_directory(directory)</code></pre>
    <div class="awsdocs-note"><div class="awsdocs-note-title"><awsui-icon name="status-info" variant="link"></awsui-icon><h6>Note</h6></div><div class="awsdocs-note-text"><p>The previous example code
      is built to process all files on the current directory and needs
      an image in order to fully process the code.</p></div></div>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/coding-interface-processing-image-files.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="A coding interface showing a Python script for processing image files and extracting text using Amazon Textract, with a highlighted copy icon in the top-right corner." />
       
       
    </div>
  
    </li><li>
      <p>Prepare your image file</p>
<p>You can use your own image or download and save this
      <a href="images/health_insurance_card_redacted.png" rel="noopener noreferrer" target="_blank">image</a>.
      Then, <b>find</b> the image you want
      to use on your local machine, and
      <b>drag</b> the file to the Jupyter
      Notebook file explorer in order to copy and paste it.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/jupyter-notebook-code-processing-image.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="A Jupyter Notebook showing Python code for processing image files and extracting text using AWS Amazon Textract, alongside a file browser displaying a health insurance card image file." />
       
       
    </div>
  
    </li><li>
      <p>Configure permissions</p>
<p>Before you can run the code in your JupyterLab, the IAM role that
      was previously created for your Jupyter notebook, needs the
      appropriate permissions to run the AWS services that your code is
      going to use. If you chose to use the previous example, Amazon Textract is the AWS service that would need the appropriate
      permissions.
    </p>
    <p><b>Open</b> the AWS IAM console at
      <a href="https://console.aws.amazon.com/iam/home" rel="noopener noreferrer" target="_blank"><span>https://console.aws.amazon.com/iam/home</span><awsui-icon class="awsdocs-link-icon" name="external"></awsui-icon></a>.
    </p>
    <p>In the left navigation pane, choose
      <b>Roles</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/identity-access-management-iam-menu-roles.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="Identity and Access Management (IAM) menu with 'Roles' highlighted in red under Access management." />
       
       
    </div>
  
    </li><li>
      <p>Search for the IAM role</p>
<p>In the <b>search box</b>, find the
      previously created
      <b><b>AmazonSageMaker AI-ExecutionRole-&lt;timestamp&gt;</b></b>
      role, and <b>open</b> the role.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/iam-roles-page-search-executionrole-one.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="The AWS IAM Roles page showing a search for &#34;AmazonSageMaker AI-ExecutionRole&#34; with one matching result listed." />
       
       
    </div>
  
    </li><li>
      <p>Add permissions</p>
<p>On the
      <b>AmazonSageMaker AI-ExecutionRole-&lt;timestamp&gt;</b>
      page, choose the <b>Add
      permissions</b> drop down, and select
      <b>Attach policies</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/execution-role-management-interface.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="AWS SageMaker AI execution role management interface showing summary details, permissions policies, and options to add or attach policies." />
       
       
    </div>
  
    </li><li>
      <p>Attach the policy</p>
<p>On the <b>Attach policy to
      AmazonSageMaker AI-ExecutionRole-&lt;timestamp&gt;</b> page,
      in the <b>Other permissions
      policies</b> section search bar, enter
      <b>AmazonAmazon TextractFullAccess</b>. Then,
      select the <b>policy</b>, and choose
      <b>Add permissions</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/console-attachment-textractlong-fullaccess.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="AWS console showing the attachment of the &#34;AmazonAmazon TextractFullAccess&#34; policy to an Amazon SageMaker AI execution role, with the policy selected and the &#34;Add permissions&#34; button highlighted." />
       
       
    </div>
  
    </li><li>
      <p>Run the notebook</p>
<p>Navigate back to your
      <b>JupyterLab</b> tab, and select
      <b>Run</b>.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/jupyter-notebook-interface-code-processing.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="A Jupyter Notebook interface showing Python code for processing image files, including functions to list image files, check if a file should be processed, and extract text using Amazon Textract." />
       
       
    </div>
  
    </li><li>
      <p>View the text file</p>
<p>After your code runs you should now be able to see a
      <b><b>.txt file</b></b>
      with the extracted text in the left navigation pane of your
      JupyterLab.
    </p>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/file-explorer-text-editor-health-insurance.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="A file explorer and text editor showing a health insurance card's redacted details, including member name, ID, plan type, and coverage information." />
       
       
    </div>
  
    </li></ol></div></awsui-expandable-section><awsui-expandable-section variant="container" header="Clean up resources" id="clean-up-resources" expanded="false"><p>In this step, you will go through the steps to delete all the
    resources you created throughout this tutorial. It is recommended
    that you stop the Jupyter notebook you created to prevent unexpected
    costs.
  </p><div class="procedure"><ul><li>
      <p>Delete the notebook</p>
<p>In the SageMaker AI console, in the left navigation pane, choose
      <b>Notebooks</b>, and select the
      <b>Notebook</b>. Then, choose
      <b>Actions</b>, and select
      <b>Stop</b>.
    </p>
    <div class="awsdocs-note"><div class="awsdocs-note-title"><awsui-icon name="status-info" variant="link"></awsui-icon><h6>Note</h6></div><div class="awsdocs-note-text"><p>The stop operation might
      take around 5 minutes. Once the notebook is stopped you can also
      delete it by choosing <b>Actions</b>
      and selecting <b>Delete</b>.</p></div></div>
  <div class="mediaobject">
       
        <img src="/images/hands-on/latest/extract-text-with-amazon-textract/images/navigation-menu-interface.png" class="aws-docs-img-whiteBg aws-docs-img-padding" alt="The navigation menu interface." />
       
       
    </div>
    </li></ul></div></awsui-expandable-section></div>
  <h2 id="congratulations">Congratulations</h2>
    
  <p>You have created a sample Proof-of-Concept to extract information
    from documents.
  </p>
  <awsdocs-copyright class="copyright-print"></awsdocs-copyright><awsdocs-thumb-feedback right-edge="{{$ctrl.thumbFeedbackRightEdge}}"></awsdocs-thumb-feedback></div><noscript><div><div><div><div id="js_error_message"><p><img src="https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png" alt="Warning" /> <strong>Javascript is disabled or is unavailable in your browser.</strong></p><p>To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.</p></div></div></div></div></noscript><div id="main-col-footer" class="awsui-util-font-size-0"><div id="doc-conventions"><a target="_top" href="/general/latest/gr/docconventions.html">Document Conventions</a></div><div class="prev-next"></div></div><awsdocs-page-utilities></awsdocs-page-utilities></div><div id="quick-feedback-yes" style="display: none;"><div class="title">Did this page help you? - Yes</div><div class="content"><p>Thanks for letting us know we're doing a good job!</p><p>If you've got a moment, please tell us what we did right so we can do more of it.</p><p><awsui-button id="fblink" rel="noopener noreferrer" target="_blank" text="Feedback" click="linkClick($event)" href="https://docs.aws.amazon.com/forms/aws-doc-feedback?feedback_destination_id=f8f24ea3-648d-452a-b7b1-9ea97afb6055&amp;topic_url=https://docs.aws.amazon.com/en_us/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html"></awsui-button></p></div></div><div id="quick-feedback-no" style="display: none;"><div class="title">Did this page help you? - No</div><div class="content"><p>Thanks for letting us know this page needs work. We're sorry we let you down.</p><p>If you've got a moment, please tell us how we can make the documentation better.</p><p><awsui-button id="fblink" rel="noopener noreferrer" target="_blank" text="Feedback" click="linkClick($event)" href="https://docs.aws.amazon.com/forms/aws-doc-feedback?feedback_destination_id=f8f24ea3-648d-452a-b7b1-9ea97afb6055&amp;topic_url=https://docs.aws.amazon.com/en_us/hands-on/latest/extract-text-with-amazon-textract/extract-text-with-amazon-textract.html"></awsui-button></p></div></div></div></body></div></awsdocs-view><div class="page-loading-indicator" id="page-loading-indicator"><awsui-spinner size="large"></awsui-spinner></div></div><div id="tools-panel" dom-region="tools"><awsdocs-tools-panel id="awsdocs-tools-panel"></awsdocs-tools-panel></div></awsui-app-layout><awsdocs-cookie-banner class="doc-cookie-banner"></awsdocs-cookie-banner></div></body></html>