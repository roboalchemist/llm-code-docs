








<!doctype html>
<html 
      lang="en"
      dir="ltr">
  <head>
    <meta name="google-signin-client-id" content="721724668570-nbkv1cfusk7kk4eni4pjvepaus73b13t.apps.googleusercontent.com"><meta name="google-signin-scope"
          content="profile email https://www.googleapis.com/auth/developerprofiles https://www.googleapis.com/auth/developerprofiles.award https://www.googleapis.com/auth/devprofiles.full_control.firstparty"><meta property="og:site_name" content="Google Cloud Documentation">
    <meta property="og:type" content="website"><meta name="theme-color" content="#1a73e8"><meta charset="utf-8">
    <meta content="IE=Edge" http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    

    <link rel="manifest" href="/_pwa/clouddocs/manifest.json"
          crossorigin="use-credentials">
    <link rel="preconnect" href="//www.gstatic.com" crossorigin>
    <link rel="preconnect" href="//fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="//fonts.googleapis.com" crossorigin>
    <link rel="preconnect" href="//apis.google.com" crossorigin>
    <link rel="preconnect" href="//www.google-analytics.com" crossorigin><link rel="stylesheet" href="//fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700&display=swap">
      <link rel="stylesheet"
            href="//fonts.googleapis.com/css2?family=Material+Icons&family=Material+Symbols+Outlined&display=block"><link rel="stylesheet" href="https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/css/app.css">
      <link rel="shortcut icon" href="https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/images/favicons/onecloud/favicon.ico">
    <link rel="apple-touch-icon" href="https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/images/favicons/onecloud/super_cloud.png"><link rel="canonical" href="https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest"><link rel="search" type="application/opensearchdescription+xml"
            title="Google Cloud Documentation" href="https://docs.cloud.google.com/s/opensearch.xml">
      <link rel="alternate" hreflang="en"
          href="https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest" /><link rel="alternate" hreflang="x-default" href="https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest" /><link rel="alternate" hreflang="en"
          href="https://berlin.devsitetest.how/python/docs/reference/cloudbuild/latest" /><link rel="alternate" hreflang="x-default" href="https://berlin.devsitetest.how/python/docs/reference/cloudbuild/latest" /><title>Python client libraries &nbsp;|&nbsp; Google Cloud Documentation</title>

<meta property="og:title" content="Python client libraries &nbsp;|&nbsp; Google Cloud Documentation"><meta property="og:url" content="https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest"><meta property="og:image" content="https://docs.cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630"><meta property="og:locale" content="en"><meta name="twitter:card" content="summary_large_image"><script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    
    "headline": ""
  }
</script><script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [{
      "@type": "ListItem",
      "position": 1,
      "name": "Python",
      "item": "https://docs.cloud.google.com/python/docs"
    },{
      "@type": "ListItem",
      "position": 2,
      "name": "Client libraries",
      "item": "https://docs.cloud.google.com/python/docs/reference"
    }]
  }
  </script>
  
    
    
    

    
    
    <meta name="gtm_var" data-key="docType" data-value="reference">
    
    
    
  

    
      <link rel="stylesheet" href="/extras.css"></head>
  <body class="color-scheme--light"
        template="page"
        theme="clouddocs-theme"
        type="article"
        
        
        
        layout="docs"
        
        
        free-trial
        
        
        display-toc
        pending>
  
    <devsite-progress type="indeterminate" id="app-progress"></devsite-progress>
  
  
    <a href="#main-content" class="skip-link button">
      
      Skip to main content
    </a>
    <section class="devsite-wrapper">
      <devsite-cookie-notification-bar></devsite-cookie-notification-bar><cloudx-track userCountry="US"></cloudx-track>

<devsite-header role="banner" keep-tabs-visible>
  
    





















<div class="devsite-header--inner" data-nosnippet>
  <div class="devsite-top-logo-row-wrapper-wrapper">
    <div class="devsite-top-logo-row-wrapper">
      <div class="devsite-top-logo-row">
        <button type="button" id="devsite-hamburger-menu"
          class="devsite-header-icon-button button-flat material-icons gc-analytics-event"
          data-category="Site-Wide Custom Events"
          data-label="Navigation menu button"
          visually-hidden
          aria-label="Open menu">
        </button>
        
<div class="devsite-product-name-wrapper">

  <a href="/" class="devsite-site-logo-link gc-analytics-event"
   data-category="Site-Wide Custom Events" data-label="Site logo" track-type="globalNav"
   track-name="googleCloudDocumentation" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <img src="https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/images/lockup.svg" class="devsite-site-logo" alt="Google Cloud Documentation">
  </picture>
  
</a>



</div>
        <div class="devsite-top-logo-row-middle">
          <div class="devsite-header-upper-tabs">
            
              
              
  <devsite-tabs class="upper-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Upper tabs">
      
        
          <tab class="devsite-dropdown
    
    devsite-active
    devsite-clickable
    ">
  
    <a href="https://docs.cloud.google.com/docs"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/docs"
    
       track-type="nav"
       track-metadata-position="nav - docs-home"
       track-metadata-module="primary nav"
       aria-label="Technology areas, selected" 
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Technology areas"
         
           track-name="docs-home"
         
           track-link-column-type="single-column"
         
       >
    Technology areas
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Technology areas"
         track-type="nav"
         track-metadata-eventdetail="https://docs.cloud.google.com/docs"
         track-metadata-position="nav - docs-home"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Technology areas"
          
            track-name="docs-home"
          
            track-link-column-type="single-column"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
        <button class="devsite-tabs-close-button material-icons button-flat gc-analytics-event"
                data-category="Site-Wide Custom Events"
                data-label="Close dropdown menu"
                aria-label="Close dropdown menu"
                track-type="nav"
                track-name="close"
                track-metadata-eventdetail="#"
                track-metadata-position="nav - docs-home"
                track-metadata-module="tertiary nav">close</button>
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/ai-ml"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/ai-ml"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      AI and ML
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/application-development"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/application-development"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Application development
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/application-hosting"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/application-hosting"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Application hosting
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/compute-area"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/compute-area"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Compute
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/data"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/data"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Data analytics and pipelines
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/databases"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/databases"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Databases
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/dhm-cloud"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/dhm-cloud"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Distributed, hybrid, and multicloud
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/industry"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/industry"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Industry solutions
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/migration"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/migration"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Migration
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/networking"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/networking"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Networking
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/observability"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/observability"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Observability and monitoring
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/security"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/security"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Security
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/storage"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/storage"
                     track-metadata-position="nav - docs-home"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Storage
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
        
          <tab class="devsite-dropdown
    
    
    devsite-clickable
    ">
  
    <a href="https://docs.cloud.google.com/docs/cross-product-overviews"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/docs/cross-product-overviews"
    
       track-type="nav"
       track-metadata-position="nav - crossproduct"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Cross-product tools"
         
           track-name="crossproduct"
         
           track-link-column-type="single-column"
         
       >
    Cross-product tools
  
    </a>
    
      <button
         aria-haspopup="menu"
         aria-expanded="false"
         aria-label="Dropdown menu for Cross-product tools"
         track-type="nav"
         track-metadata-eventdetail="https://docs.cloud.google.com/docs/cross-product-overviews"
         track-metadata-position="nav - crossproduct"
         track-metadata-module="primary nav"
         
          
            data-category="Site-Wide Custom Events"
          
            data-label="Tab: Cross-product tools"
          
            track-name="crossproduct"
          
            track-link-column-type="single-column"
          
        
         class="devsite-tabs-dropdown-toggle devsite-icon devsite-icon-arrow-drop-down"></button>
    
  
  <div class="devsite-tabs-dropdown" role="menu" aria-label="submenu" hidden>
    <div class="devsite-tabs-dropdown-content">
      
        <button class="devsite-tabs-close-button material-icons button-flat gc-analytics-event"
                data-category="Site-Wide Custom Events"
                data-label="Close dropdown menu"
                aria-label="Close dropdown menu"
                track-type="nav"
                track-name="close"
                track-metadata-eventdetail="#"
                track-metadata-position="nav - crossproduct"
                track-metadata-module="tertiary nav">close</button>
      
      
        <div class="devsite-tabs-dropdown-column
                    ">
          
            <ul class="devsite-tabs-dropdown-section
                       ">
              
              
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/access-resources"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/access-resources"
                     track-metadata-position="nav - crossproduct"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Access and resources management
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/costs-usage"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/costs-usage"
                     track-metadata-position="nav - crossproduct"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Costs and usage management
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/iac"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/iac"
                     track-metadata-position="nav - crossproduct"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      Infrastructure as code
                    </div>
                    
                  </a>
                </li>
              
                <li class="devsite-nav-item">
                  <a href="https://docs.cloud.google.com/docs/devtools"
                    
                     track-type="nav"
                     track-metadata-eventdetail="https://docs.cloud.google.com/docs/devtools"
                     track-metadata-position="nav - crossproduct"
                     track-metadata-module="tertiary nav"
                     
                     tooltip
                  >
                    
                    <div class="devsite-nav-item-title">
                      SDK, languages, frameworks, and tools
                    </div>
                    
                  </a>
                </li>
              
            </ul>
          
        </div>
      
    </div>
  </div>
</tab>
        
      
    </nav>

  </devsite-tabs>

            
           </div>
          
<devsite-search
    enable-signin
    enable-search
    enable-suggestions
      
    
    enable-search-summaries
    project-name="Python client libraries"
    tenant-name="Google Cloud Documentation"
    project-scope="/python/docs/reference"
    url-scoped="https://docs.cloud.google.com/s/results/python/docs/reference"
    
    
    
    >
  <form class="devsite-search-form" action="https://docs.cloud.google.com/s/results" method="GET">
    <div class="devsite-search-container">
      <button type="button"
              search-open
              class="devsite-search-button devsite-header-icon-button button-flat material-icons"
              
              aria-label="Open search"></button>
      <div class="devsite-searchbox">
        <input
          aria-activedescendant=""
          aria-autocomplete="list"
          
          aria-label="Search"
          aria-expanded="false"
          aria-haspopup="listbox"
          autocomplete="off"
          class="devsite-search-field devsite-search-query"
          name="q"
          
          placeholder="Search"
          role="combobox"
          type="text"
          value=""
          >
          <div class="devsite-search-image material-icons" aria-hidden="true">
            
              <svg class="devsite-search-ai-image" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <g clip-path="url(#clip0_6641_386)">
                    <path d="M19.6 21L13.3 14.7C12.8 15.1 12.225 15.4167 11.575 15.65C10.925 15.8833 10.2333 16 9.5 16C7.68333 16 6.14167 15.375 4.875 14.125C3.625 12.8583 3 11.3167 3 9.5C3 7.68333 3.625 6.15 4.875 4.9C6.14167 3.63333 7.68333 3 9.5 3C10.0167 3 10.5167 3.05833 11 3.175C11.4833 3.275 11.9417 3.43333 12.375 3.65L10.825 5.2C10.6083 5.13333 10.3917 5.08333 10.175 5.05C9.95833 5.01667 9.73333 5 9.5 5C8.25 5 7.18333 5.44167 6.3 6.325C5.43333 7.19167 5 8.25 5 9.5C5 10.75 5.43333 11.8167 6.3 12.7C7.18333 13.5667 8.25 14 9.5 14C10.6667 14 11.6667 13.625 12.5 12.875C13.35 12.1083 13.8417 11.15 13.975 10H15.975C15.925 10.6333 15.7833 11.2333 15.55 11.8C15.3333 12.3667 15.05 12.8667 14.7 13.3L21 19.6L19.6 21ZM17.5 12C17.5 10.4667 16.9667 9.16667 15.9 8.1C14.8333 7.03333 13.5333 6.5 12 6.5C13.5333 6.5 14.8333 5.96667 15.9 4.9C16.9667 3.83333 17.5 2.53333 17.5 0.999999C17.5 2.53333 18.0333 3.83333 19.1 4.9C20.1667 5.96667 21.4667 6.5 23 6.5C21.4667 6.5 20.1667 7.03333 19.1 8.1C18.0333 9.16667 17.5 10.4667 17.5 12Z" fill="#5F6368"/>
                  </g>
                <defs>
                <clipPath id="clip0_6641_386">
                <rect width="24" height="24" fill="white"/>
                </clipPath>
                </defs>
              </svg>
            
          </div>
          <div class="devsite-search-shortcut-icon-container" aria-hidden="true">
            <kbd class="devsite-search-shortcut-icon">/</kbd>
          </div>
      </div>
    </div>
  </form>
  <button type="button"
          search-close
          class="devsite-search-button devsite-header-icon-button button-flat material-icons"
          
          aria-label="Close search"></button>
</devsite-search>

        </div>

        

  

  
    <a class="devsite-header-link devsite-top-button button gc-analytics-event button-with-icon"
    href="//console.cloud.google.com/"
    data-category="Site-Wide Custom Events"
    data-label="Site header link: Console"
    
      
        referrerpolicy="no-referrer-when-downgrade"
      
        track-type="globalNav"
      
        track-metadata-position="nav"
      
        track-name="console"
      
        track-metadata-eventDetail="nav"
      
    >
  Console
</a>
  

  

  

  
<devsite-language-selector>
  <ul role="presentation">
    
    
    <li role="presentation">
      <a role="menuitem" lang="en"
        >English</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="de"
        >Deutsch</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="es_419"
        >Español – América Latina</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fr"
        >Français</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_cn"
        >中文 – 简体</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ja"
        >日本語</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ko"
        >한국어</a>
    </li>
    
  </ul>
</devsite-language-selector>




        
          <devsite-user 
                        
                        
                          enable-profiles
                        
                        
                          fp-auth
                        
                        id="devsite-user">
            
              
              <span class="button devsite-top-button" aria-hidden="true" visually-hidden>Sign in</span>
            
          </devsite-user>
        
        
        
      </div>
    </div>
  </div>



  <div class="devsite-collapsible-section
    ">
    <div class="devsite-header-background">
      
        
          <div class="devsite-product-id-row"
           >
            <div class="devsite-product-description-row">
              
                
                <div class="devsite-product-id">
                  
                    
  
  <a href="https://docs.cloud.google.com/python/docs/reference">
    
  <div class="devsite-product-logo-container"
       
       
       
    size="medium"
  >
  
    <picture>
      
      <img class="devsite-product-logo"
           alt=""
           src="https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/developer-tools-color.svg"
           srcset=" /_static/clouddocs/images/icons/categories/developer-tools-color.svg"
           sizes="64px"
           loading="lazy"
           >
    </picture>
  
  </div>
  
  </a>
  

                  
                  
                  
                    <ul class="devsite-breadcrumb-list"
  
    aria-label="Lower header breadcrumb">
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
        
  <a href="https://docs.cloud.google.com/python/docs"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Lower Header"
      
        data-value="1"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="1"
      
        track-metadata-eventdetail="Python"
      
    >
    
          Python
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://docs.cloud.google.com/python/docs/reference"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Lower Header"
      
        data-value="2"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="2"
      
        track-metadata-eventdetail="Python client libraries"
      
    >
    
          Client libraries
        
  </a>
  
      
    
  </li>
  
</ul>
                </div>
                
              
              
            </div>
            
              <div class="devsite-product-button-row">
  

  
  <a href="//console.cloud.google.com/freetrial"
  
    class="cloud-free-trial-button button button-primary
      "
    
    
      
        track-name="gcpCta"
      
        track-metadata-position="nav"
      
        track-metadata-eventDetail="nav"
      
        track-type="freeTrial"
      
        referrerpolicy="no-referrer-when-downgrade"
      
    
    >Start free</a>

</div>
            
          </div>
          
        
      
      
        <div class="devsite-doc-set-nav-row">
          
          
            
            
  <devsite-tabs class="lower-tabs">

    <nav class="devsite-tabs-wrapper" aria-label="Lower tabs">
      
        
          <tab  >
            
    <a href="https://docs.cloud.google.com/python/docs"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/python/docs"
    
       track-type="nav"
       track-metadata-position="nav - overview"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Overview"
         
           track-name="overview"
         
       >
    Overview
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://docs.cloud.google.com/python/docs/setup"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/python/docs/setup"
    
       track-type="nav"
       track-metadata-position="nav - guides"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Guides"
         
           track-name="guides"
         
       >
    Guides
  
    </a>
    
  
          </tab>
        
      
        
          <tab  class="devsite-active">
            
    <a href="https://docs.cloud.google.com/python/docs/reference"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/python/docs/reference"
    
       track-type="nav"
       track-metadata-position="nav - reference"
       track-metadata-module="primary nav"
       aria-label="Reference, selected" 
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Reference"
         
           track-name="reference"
         
       >
    Reference
  
    </a>
    
  
          </tab>
        
      
        
          <tab  >
            
    <a href="https://docs.cloud.google.com/docs/samples/?language=python"
    class="devsite-tabs-content gc-analytics-event "
      track-metadata-eventdetail="https://docs.cloud.google.com/docs/samples/?language=python"
    
       track-type="nav"
       track-metadata-position="nav - samples"
       track-metadata-module="primary nav"
       
       
         
           data-category="Site-Wide Custom Events"
         
           data-label="Tab: Samples"
         
           track-name="samples"
         
       >
    Samples
  
    </a>
    
  
          </tab>
        
      
    </nav>

  </devsite-tabs>

          
          
        </div>
      
    </div>
  </div>

</div>



  

  
</devsite-header>
      <devsite-book-nav scrollbars >
        
          





















<div class="devsite-book-nav-filter"
     >
  <span class="filter-list-icon material-icons" aria-hidden="true"></span>
  <input type="text"
         placeholder="Filter"
         
         aria-label="Type to filter"
         role="searchbox">
  
  <span class="filter-clear-button hidden"
        data-title="Clear filter"
        aria-label="Clear filter"
        role="button"
        tabindex="0"></span>
</div>

<nav class="devsite-book-nav devsite-nav nocontent"
     aria-label="Side menu">
  <div class="devsite-mobile-header">
    <button type="button"
            id="devsite-close-nav"
            class="devsite-header-icon-button button-flat material-icons gc-analytics-event"
            data-category="Site-Wide Custom Events"
            data-label="Close navigation"
            aria-label="Close navigation">
    </button>
    <div class="devsite-product-name-wrapper">

  <a href="/" class="devsite-site-logo-link gc-analytics-event"
   data-category="Site-Wide Custom Events" data-label="Site logo" track-type="globalNav"
   track-name="googleCloudDocumentation" track-metadata-position="nav"
   track-metadata-eventDetail="nav">
  
  <picture>
    
    <img src="https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/images/lockup.svg" class="devsite-site-logo" alt="Google Cloud Documentation">
  </picture>
  
</a>


</div>
  </div>

  <div class="devsite-book-nav-wrapper">
    <div class="devsite-mobile-nav-top">
      
        <ul class="devsite-nav-list">
          
            <li class="devsite-nav-item">
              
  
  <a href="/docs"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Technology areas"
      
        track-name="docs-home"
      
        track-link-column-type="single-column"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Technology areas"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Technology areas
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Technology areas"
      
        track-name="docs-home"
      
        track-link-column-type="single-column"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Technology areas">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Technology areas">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
                <ul class="devsite-nav-responsive-tabs">
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/python/docs"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Overview"
      
        track-name="overview"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Overview"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Overview
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/python/docs/setup"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Guides"
      
        track-name="guides"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Guides"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Guides
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/python/docs/reference"
    
       class="devsite-nav-title gc-analytics-event
              
              devsite-nav-active"
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Reference"
      
        track-name="reference"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Reference"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip menu="_book">
      Reference
   </span>
    
  
  </a>
  

  
                    </li>
                  
                    
                    
                    
                    <li class="devsite-nav-item">
                      
  
  <a href="/docs/samples/?language=python"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Samples"
      
        track-name="samples"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Samples"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Samples
   </span>
    
  
  </a>
  

  
                    </li>
                  
                </ul>
              
            </li>
          
            <li class="devsite-nav-item">
              
  
  <a href="/docs/cross-product-overviews"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Cross-product tools"
      
        track-name="crossproduct"
      
        track-link-column-type="single-column"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Cross-product tools"
     track-type="globalNav"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Cross-product tools
   </span>
    
  
  </a>
  

  
    <ul class="devsite-nav-responsive-tabs devsite-nav-has-menu
               ">
      
<li class="devsite-nav-item">

  
  <span
    
       class="devsite-nav-title"
       tooltip
    
    
      
        data-category="Site-Wide Custom Events"
      
        data-label="Tab: Cross-product tools"
      
        track-name="crossproduct"
      
        track-link-column-type="single-column"
      
    >
  
    <span class="devsite-nav-text" tooltip menu="Cross-product tools">
      More
   </span>
    
    <span class="devsite-nav-icon material-icons" data-icon="forward"
          menu="Cross-product tools">
    </span>
    
  
  </span>
  

</li>

    </ul>
  
              
            </li>
          
          
    
    
<li class="devsite-nav-item">

  
  <a href="//console.cloud.google.com/"
    
       class="devsite-nav-title gc-analytics-event button-with-icon"
    

    
      
        referrerpolicy="no-referrer-when-downgrade"
      
        track-type="globalNav"
      
        track-metadata-position="nav"
      
        track-name="console"
      
        track-metadata-eventDetail="nav"
      
    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Console"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Console
   </span>
    
  
  </a>
  

</li>

  
          
        </ul>
      
    </div>
    
      <div class="devsite-mobile-nav-bottom">
        
          
          <ul class="devsite-nav-list" menu="_book">
            <li class="devsite-nav-item"><a href="/python/docs/reference"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-heading"><div class="devsite-nav-title devsite-nav-title-no-path">
        <span class="devsite-nav-text" tooltip>Library reference docs</span>
      </div></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/bigframes/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/bigframes/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/bigframes/latest"
      ><span class="devsite-nav-text" tooltip>BigQuery DataFrames</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/accessapproval/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/accessapproval/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/accessapproval/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-access-approval</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/advisorynotifications/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/advisorynotifications/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/advisorynotifications/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-advisorynotifications</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/aiplatform/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/aiplatform/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/aiplatform/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-aiplatform</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/alloydb/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/alloydb/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/alloydb/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-alloydb</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/connectors/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/connectors/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/connectors/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-alloydb-connectors</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/apigateway/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/apigateway/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/apigateway/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-api-gateway</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/apikeys/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/apikeys/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/apikeys/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-api-keys</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/apigeeconnect/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/apigeeconnect/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/apigeeconnect/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-apigee-connect</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/apigeeregistry/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/apigeeregistry/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/apigeeregistry/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-apigee-registry</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-apihub/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-apihub/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-apihub/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-apihub</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/appengine/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/appengine/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/appengine/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-appengine-admin</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/appenginelogging/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/appenginelogging/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/appenginelogging/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-appengine-logging</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-apphub/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-apphub/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-apphub/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-apphub</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/artifactregistry/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/artifactregistry/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/artifactregistry/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-artifact-registry</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudasset/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudasset/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudasset/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-asset</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/assuredworkloads/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/assuredworkloads/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/assuredworkloads/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-assured-workloads</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/auditlog/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/auditlog/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/auditlog/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-audit-log</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/automl/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/automl/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/automl/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-automl</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/backupdr/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/backupdr/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/backupdr/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-backupdr</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/baremetalsolution/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/baremetalsolution/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/baremetalsolution/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bare-metal-solution</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/batch/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/batch/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/batch/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-batch</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/beyondcorpappconnections/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/beyondcorpappconnections/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/beyondcorpappconnections/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-beyondcorp-appconnections</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/beyondcorpappconnectors/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/beyondcorpappconnectors/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/beyondcorpappconnectors/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-beyondcorp-appconnectors</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/beyondcorpappgateways/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/beyondcorpappgateways/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/beyondcorpappgateways/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-beyondcorp-appgateways</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/beyondcorpclientconnectorservices/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/beyondcorpclientconnectorservices/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/beyondcorpclientconnectorservices/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-beyondcorp-clientconnectorservices</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/beyondcorpclientgateways/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/beyondcorpclientgateways/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/beyondcorpclientgateways/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-beyondcorp-clientgateways</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-biglake/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-biglake/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-biglake/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-biglake</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/bigquery/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/bigquery/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/bigquery/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigquery</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/biglake/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/biglake/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/biglake/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigquery-biglake</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/bigqueryconnection/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/bigqueryconnection/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/bigqueryconnection/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigquery-connection</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/analyticshub/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/analyticshub/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/analyticshub/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigquery-data-exchange</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/bigquerydatapolicy/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/bigquerydatapolicy/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/bigquerydatapolicy/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigquery-datapolicies</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/bigquerydatatransfer/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/bigquerydatatransfer/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/bigquerydatatransfer/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigquery-datatransfer</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/bigquerylogging/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/bigquerylogging/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/bigquerylogging/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigquery-logging</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/bigquerymigration/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/bigquerymigration/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/bigquerymigration/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigquery-migration</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/bigqueryreservation/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/bigqueryreservation/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/bigqueryreservation/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigquery-reservation</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/bigquerystorage/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/bigquerystorage/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/bigquerystorage/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigquery-storage</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/bigtable/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/bigtable/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/bigtable/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-bigtable</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudbilling/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbilling/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbilling/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-billing</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/billingbudgets/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/billingbudgets/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/billingbudgets/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-billing-budgets</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/binaryauthorization/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/binaryauthorization/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/binaryauthorization/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-binary-authorization</span></a></li>

  <li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>google-cloud-build</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>cloudbuild APIs</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/summary_overview"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/summary_overview"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/summary_overview"
      ><span class="devsite-nav-text" tooltip>API overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/summary_class"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/summary_class"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/summary_class"
      ><span class="devsite-nav-text" tooltip>Classes</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/summary_method"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/summary_method"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/summary_method"
      ><span class="devsite-nav-text" tooltip>Methods</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/summary_property"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/summary_property"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/summary_property"
      ><span class="devsite-nav-text" tooltip>Properties and Attributes</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/changelog"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/changelog"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/changelog"
      ><span class="devsite-nav-text" tooltip>Changelog</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/multiprocessing"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/multiprocessing"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/multiprocessing"
      ><span class="devsite-nav-text" tooltip>Multiprocessing</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Devtools</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>cloud_build</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>pagers</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildTriggersAsyncPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildTriggersAsyncPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildTriggersAsyncPager"
      ><span class="devsite-nav-text" tooltip>ListBuildTriggersAsyncPager</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildTriggersPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildTriggersPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildTriggersPager"
      ><span class="devsite-nav-text" tooltip>ListBuildTriggersPager</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildsAsyncPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildsAsyncPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildsAsyncPager"
      ><span class="devsite-nav-text" tooltip>ListBuildsAsyncPager</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildsPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildsPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildsPager"
      ><span class="devsite-nav-text" tooltip>ListBuildsPager</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListWorkerPoolsAsyncPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListWorkerPoolsAsyncPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListWorkerPoolsAsyncPager"
      ><span class="devsite-nav-text" tooltip>ListWorkerPoolsAsyncPager</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListWorkerPoolsPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListWorkerPoolsPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListWorkerPoolsPager"
      ><span class="devsite-nav-text" tooltip>ListWorkerPoolsPager</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.CloudBuildAsyncClient"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.CloudBuildAsyncClient"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.CloudBuildAsyncClient"
      ><span class="devsite-nav-text" tooltip>CloudBuildAsyncClient</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.CloudBuildClient"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.CloudBuildClient"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.CloudBuildClient"
      ><span class="devsite-nav-text" tooltip>CloudBuildClient</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>cloudbuild_v1.types</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApprovalConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApprovalConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApprovalConfig"
      ><span class="devsite-nav-text" tooltip>ApprovalConfig</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>ApprovalResult</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApprovalResult"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApprovalResult"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApprovalResult"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApprovalResult.Decision"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApprovalResult.Decision"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApprovalResult.Decision"
      ><span class="devsite-nav-text" tooltip>Decision</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApproveBuildRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApproveBuildRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ApproveBuildRequest"
      ><span class="devsite-nav-text" tooltip>ApproveBuildRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ArtifactResult"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ArtifactResult"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ArtifactResult"
      ><span class="devsite-nav-text" tooltip>ArtifactResult</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Artifacts</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.ArtifactObjects"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.ArtifactObjects"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.ArtifactObjects"
      ><span class="devsite-nav-text" tooltip>ArtifactObjects</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.GoModule"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.GoModule"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.GoModule"
      ><span class="devsite-nav-text" tooltip>GoModule</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.MavenArtifact"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.MavenArtifact"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.MavenArtifact"
      ><span class="devsite-nav-text" tooltip>MavenArtifact</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.NpmPackage"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.NpmPackage"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.NpmPackage"
      ><span class="devsite-nav-text" tooltip>NpmPackage</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.PythonPackage"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.PythonPackage"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Artifacts.PythonPackage"
      ><span class="devsite-nav-text" tooltip>PythonPackage</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Build</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>FailureInfo</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.FailureInfo"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.FailureInfo"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.FailureInfo"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.FailureInfo.FailureType"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.FailureInfo.FailureType"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.FailureInfo.FailureType"
      ><span class="devsite-nav-text" tooltip>FailureType</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.Status"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.Status"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.Status"
      ><span class="devsite-nav-text" tooltip>Status</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.SubstitutionsEntry"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.SubstitutionsEntry"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.SubstitutionsEntry"
      ><span class="devsite-nav-text" tooltip>SubstitutionsEntry</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.TimingEntry"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.TimingEntry"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.TimingEntry"
      ><span class="devsite-nav-text" tooltip>TimingEntry</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Warning</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.Warning"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.Warning"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.Warning"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.Warning.Priority"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.Warning.Priority"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.Warning.Priority"
      ><span class="devsite-nav-text" tooltip>Priority</span></a></li></ul></div></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>BuildApproval</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildApproval"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildApproval"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildApproval"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildApproval.State"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildApproval.State"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildApproval.State"
      ><span class="devsite-nav-text" tooltip>State</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOperationMetadata"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOperationMetadata"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOperationMetadata"
      ><span class="devsite-nav-text" tooltip>BuildOperationMetadata</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>BuildOptions</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.DefaultLogsBucketBehavior"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.DefaultLogsBucketBehavior"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.DefaultLogsBucketBehavior"
      ><span class="devsite-nav-text" tooltip>DefaultLogsBucketBehavior</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.LogStreamingOption"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.LogStreamingOption"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.LogStreamingOption"
      ><span class="devsite-nav-text" tooltip>LogStreamingOption</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.LoggingMode"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.LoggingMode"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.LoggingMode"
      ><span class="devsite-nav-text" tooltip>LoggingMode</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.MachineType"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.MachineType"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.MachineType"
      ><span class="devsite-nav-text" tooltip>MachineType</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.PoolOption"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.PoolOption"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.PoolOption"
      ><span class="devsite-nav-text" tooltip>PoolOption</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.SubstitutionOption"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.SubstitutionOption"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.SubstitutionOption"
      ><span class="devsite-nav-text" tooltip>SubstitutionOption</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.VerifyOption"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.VerifyOption"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildOptions.VerifyOption"
      ><span class="devsite-nav-text" tooltip>VerifyOption</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildStep"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildStep"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildStep"
      ><span class="devsite-nav-text" tooltip>BuildStep</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>BuildTrigger</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildTrigger"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildTrigger"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildTrigger"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildTrigger.SubstitutionsEntry"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildTrigger.SubstitutionsEntry"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuildTrigger.SubstitutionsEntry"
      ><span class="devsite-nav-text" tooltip>SubstitutionsEntry</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuiltImage"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuiltImage"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuiltImage"
      ><span class="devsite-nav-text" tooltip>BuiltImage</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CancelBuildRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CancelBuildRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CancelBuildRequest"
      ><span class="devsite-nav-text" tooltip>CancelBuildRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ConnectedRepository"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ConnectedRepository"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ConnectedRepository"
      ><span class="devsite-nav-text" tooltip>ConnectedRepository</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateBuildRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateBuildRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateBuildRequest"
      ><span class="devsite-nav-text" tooltip>CreateBuildRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateBuildTriggerRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateBuildTriggerRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateBuildTriggerRequest"
      ><span class="devsite-nav-text" tooltip>CreateBuildTriggerRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateWorkerPoolOperationMetadata"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateWorkerPoolOperationMetadata"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateWorkerPoolOperationMetadata"
      ><span class="devsite-nav-text" tooltip>CreateWorkerPoolOperationMetadata</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateWorkerPoolRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateWorkerPoolRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.CreateWorkerPoolRequest"
      ><span class="devsite-nav-text" tooltip>CreateWorkerPoolRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DefaultServiceAccount"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DefaultServiceAccount"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DefaultServiceAccount"
      ><span class="devsite-nav-text" tooltip>DefaultServiceAccount</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DeleteBuildTriggerRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DeleteBuildTriggerRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DeleteBuildTriggerRequest"
      ><span class="devsite-nav-text" tooltip>DeleteBuildTriggerRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DeleteWorkerPoolOperationMetadata"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DeleteWorkerPoolOperationMetadata"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DeleteWorkerPoolOperationMetadata"
      ><span class="devsite-nav-text" tooltip>DeleteWorkerPoolOperationMetadata</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DeleteWorkerPoolRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DeleteWorkerPoolRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DeleteWorkerPoolRequest"
      ><span class="devsite-nav-text" tooltip>DeleteWorkerPoolRequest</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Dependency</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Dependency"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Dependency"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Dependency"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Dependency.GitSourceDependency"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Dependency.GitSourceDependency"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Dependency.GitSourceDependency"
      ><span class="devsite-nav-text" tooltip>GitSourceDependency</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Dependency.GitSourceRepository"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Dependency.GitSourceRepository"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Dependency.GitSourceRepository"
      ><span class="devsite-nav-text" tooltip>GitSourceRepository</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.FileHashes"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.FileHashes"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.FileHashes"
      ><span class="devsite-nav-text" tooltip>FileHashes</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetBuildRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetBuildRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetBuildRequest"
      ><span class="devsite-nav-text" tooltip>GetBuildRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetBuildTriggerRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetBuildTriggerRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetBuildTriggerRequest"
      ><span class="devsite-nav-text" tooltip>GetBuildTriggerRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetDefaultServiceAccountRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetDefaultServiceAccountRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetDefaultServiceAccountRequest"
      ><span class="devsite-nav-text" tooltip>GetDefaultServiceAccountRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetWorkerPoolRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetWorkerPoolRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GetWorkerPoolRequest"
      ><span class="devsite-nav-text" tooltip>GetWorkerPoolRequest</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>GitConfig</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitConfig"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitConfig.HttpConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitConfig.HttpConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitConfig.HttpConfig"
      ><span class="devsite-nav-text" tooltip>HttpConfig</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>GitFileSource</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitFileSource"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitFileSource"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitFileSource"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitFileSource.RepoType"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitFileSource.RepoType"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitFileSource.RepoType"
      ><span class="devsite-nav-text" tooltip>RepoType</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitHubEnterpriseConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitHubEnterpriseConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitHubEnterpriseConfig"
      ><span class="devsite-nav-text" tooltip>GitHubEnterpriseConfig</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitHubEnterpriseSecrets"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitHubEnterpriseSecrets"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitHubEnterpriseSecrets"
      ><span class="devsite-nav-text" tooltip>GitHubEnterpriseSecrets</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitHubEventsConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitHubEventsConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitHubEventsConfig"
      ><span class="devsite-nav-text" tooltip>GitHubEventsConfig</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitRepoSource"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitRepoSource"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitRepoSource"
      ><span class="devsite-nav-text" tooltip>GitRepoSource</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitSource"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitSource"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.GitSource"
      ><span class="devsite-nav-text" tooltip>GitSource</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Hash</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Hash"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Hash"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Hash"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Hash.HashType"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Hash.HashType"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Hash.HashType"
      ><span class="devsite-nav-text" tooltip>HashType</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>InlineSecret</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.InlineSecret"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.InlineSecret"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.InlineSecret"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.InlineSecret.EnvMapEntry"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.InlineSecret.EnvMapEntry"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.InlineSecret.EnvMapEntry"
      ><span class="devsite-nav-text" tooltip>EnvMapEntry</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildTriggersRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildTriggersRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildTriggersRequest"
      ><span class="devsite-nav-text" tooltip>ListBuildTriggersRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildTriggersResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildTriggersResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildTriggersResponse"
      ><span class="devsite-nav-text" tooltip>ListBuildTriggersResponse</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildsRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildsRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildsRequest"
      ><span class="devsite-nav-text" tooltip>ListBuildsRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildsResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildsResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListBuildsResponse"
      ><span class="devsite-nav-text" tooltip>ListBuildsResponse</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListWorkerPoolsRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListWorkerPoolsRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListWorkerPoolsRequest"
      ><span class="devsite-nav-text" tooltip>ListWorkerPoolsRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListWorkerPoolsResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListWorkerPoolsResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ListWorkerPoolsResponse"
      ><span class="devsite-nav-text" tooltip>ListWorkerPoolsResponse</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>PrivatePoolV1Config</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>NetworkConfig</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.NetworkConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.NetworkConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.NetworkConfig"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.NetworkConfig.EgressOption"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.NetworkConfig.EgressOption"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.NetworkConfig.EgressOption"
      ><span class="devsite-nav-text" tooltip>EgressOption</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.PrivateServiceConnect"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.PrivateServiceConnect"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.PrivateServiceConnect"
      ><span class="devsite-nav-text" tooltip>PrivateServiceConnect</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.WorkerConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.WorkerConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PrivatePoolV1Config.WorkerConfig"
      ><span class="devsite-nav-text" tooltip>WorkerConfig</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>PubsubConfig</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PubsubConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PubsubConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PubsubConfig"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PubsubConfig.State"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PubsubConfig.State"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PubsubConfig.State"
      ><span class="devsite-nav-text" tooltip>State</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>PullRequestFilter</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PullRequestFilter"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PullRequestFilter"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PullRequestFilter"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PullRequestFilter.CommentControl"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PullRequestFilter.CommentControl"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PullRequestFilter.CommentControl"
      ><span class="devsite-nav-text" tooltip>CommentControl</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PushFilter"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PushFilter"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.PushFilter"
      ><span class="devsite-nav-text" tooltip>PushFilter</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ReceiveTriggerWebhookRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ReceiveTriggerWebhookRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ReceiveTriggerWebhookRequest"
      ><span class="devsite-nav-text" tooltip>ReceiveTriggerWebhookRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ReceiveTriggerWebhookResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ReceiveTriggerWebhookResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.ReceiveTriggerWebhookResponse"
      ><span class="devsite-nav-text" tooltip>ReceiveTriggerWebhookResponse</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>RepoSource</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepoSource"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepoSource"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepoSource"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepoSource.SubstitutionsEntry"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepoSource.SubstitutionsEntry"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepoSource.SubstitutionsEntry"
      ><span class="devsite-nav-text" tooltip>SubstitutionsEntry</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>RepositoryEventConfig</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepositoryEventConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepositoryEventConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepositoryEventConfig"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepositoryEventConfig.RepositoryType"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepositoryEventConfig.RepositoryType"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RepositoryEventConfig.RepositoryType"
      ><span class="devsite-nav-text" tooltip>RepositoryType</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Results"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Results"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Results"
      ><span class="devsite-nav-text" tooltip>Results</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RetryBuildRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RetryBuildRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RetryBuildRequest"
      ><span class="devsite-nav-text" tooltip>RetryBuildRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RunBuildTriggerRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RunBuildTriggerRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.RunBuildTriggerRequest"
      ><span class="devsite-nav-text" tooltip>RunBuildTriggerRequest</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Secret</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Secret"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Secret"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Secret"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Secret.SecretEnvEntry"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Secret.SecretEnvEntry"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Secret.SecretEnvEntry"
      ><span class="devsite-nav-text" tooltip>SecretEnvEntry</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.SecretManagerSecret"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.SecretManagerSecret"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.SecretManagerSecret"
      ><span class="devsite-nav-text" tooltip>SecretManagerSecret</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Secrets"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Secrets"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Secrets"
      ><span class="devsite-nav-text" tooltip>Secrets</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Source"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Source"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Source"
      ><span class="devsite-nav-text" tooltip>Source</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>SourceProvenance</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.SourceProvenance"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.SourceProvenance"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.SourceProvenance"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.SourceProvenance.FileHashesEntry"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.SourceProvenance.FileHashesEntry"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.SourceProvenance.FileHashesEntry"
      ><span class="devsite-nav-text" tooltip>FileHashesEntry</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>StorageSource</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.StorageSource"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.StorageSource"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.StorageSource"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.StorageSource.SourceFetcher"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.StorageSource.SourceFetcher"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.StorageSource.SourceFetcher"
      ><span class="devsite-nav-text" tooltip>SourceFetcher</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.StorageSourceManifest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.StorageSourceManifest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.StorageSourceManifest"
      ><span class="devsite-nav-text" tooltip>StorageSourceManifest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.TimeSpan"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.TimeSpan"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.TimeSpan"
      ><span class="devsite-nav-text" tooltip>TimeSpan</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UpdateBuildTriggerRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UpdateBuildTriggerRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UpdateBuildTriggerRequest"
      ><span class="devsite-nav-text" tooltip>UpdateBuildTriggerRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UpdateWorkerPoolOperationMetadata"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UpdateWorkerPoolOperationMetadata"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UpdateWorkerPoolOperationMetadata"
      ><span class="devsite-nav-text" tooltip>UpdateWorkerPoolOperationMetadata</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UpdateWorkerPoolRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UpdateWorkerPoolRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UpdateWorkerPoolRequest"
      ><span class="devsite-nav-text" tooltip>UpdateWorkerPoolRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedGoModule"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedGoModule"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedGoModule"
      ><span class="devsite-nav-text" tooltip>UploadedGoModule</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedMavenArtifact"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedMavenArtifact"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedMavenArtifact"
      ><span class="devsite-nav-text" tooltip>UploadedMavenArtifact</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedNpmPackage"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedNpmPackage"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedNpmPackage"
      ><span class="devsite-nav-text" tooltip>UploadedNpmPackage</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedPythonPackage"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedPythonPackage"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedPythonPackage"
      ><span class="devsite-nav-text" tooltip>UploadedPythonPackage</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Volume"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Volume"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Volume"
      ><span class="devsite-nav-text" tooltip>Volume</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>WebhookConfig</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WebhookConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WebhookConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WebhookConfig"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WebhookConfig.State"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WebhookConfig.State"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WebhookConfig.State"
      ><span class="devsite-nav-text" tooltip>State</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>WorkerPool</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WorkerPool"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WorkerPool"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WorkerPool"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WorkerPool.AnnotationsEntry"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WorkerPool.AnnotationsEntry"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WorkerPool.AnnotationsEntry"
      ><span class="devsite-nav-text" tooltip>AnnotationsEntry</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WorkerPool.State"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WorkerPool.State"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.WorkerPool.State"
      ><span class="devsite-nav-text" tooltip>State</span></a></li></ul></div></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>repository_manager</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>pagers</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.FetchLinkableRepositoriesAsyncPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.FetchLinkableRepositoriesAsyncPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.FetchLinkableRepositoriesAsyncPager"
      ><span class="devsite-nav-text" tooltip>FetchLinkableRepositoriesAsyncPager</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.FetchLinkableRepositoriesPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.FetchLinkableRepositoriesPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.FetchLinkableRepositoriesPager"
      ><span class="devsite-nav-text" tooltip>FetchLinkableRepositoriesPager</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListConnectionsAsyncPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListConnectionsAsyncPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListConnectionsAsyncPager"
      ><span class="devsite-nav-text" tooltip>ListConnectionsAsyncPager</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListConnectionsPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListConnectionsPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListConnectionsPager"
      ><span class="devsite-nav-text" tooltip>ListConnectionsPager</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListRepositoriesAsyncPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListRepositoriesAsyncPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListRepositoriesAsyncPager"
      ><span class="devsite-nav-text" tooltip>ListRepositoriesAsyncPager</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListRepositoriesPager"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListRepositoriesPager"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.ListRepositoriesPager"
      ><span class="devsite-nav-text" tooltip>ListRepositoriesPager</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.RepositoryManagerAsyncClient"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.RepositoryManagerAsyncClient"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.RepositoryManagerAsyncClient"
      ><span class="devsite-nav-text" tooltip>RepositoryManagerAsyncClient</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.RepositoryManagerClient"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.RepositoryManagerClient"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.RepositoryManagerClient"
      ><span class="devsite-nav-text" tooltip>RepositoryManagerClient</span></a></li></ul></div></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>cloudbuild_v2.types</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BatchCreateRepositoriesRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BatchCreateRepositoriesRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BatchCreateRepositoriesRequest"
      ><span class="devsite-nav-text" tooltip>BatchCreateRepositoriesRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BatchCreateRepositoriesResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BatchCreateRepositoriesResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BatchCreateRepositoriesResponse"
      ><span class="devsite-nav-text" tooltip>BatchCreateRepositoriesResponse</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BitbucketCloudConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BitbucketCloudConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BitbucketCloudConfig"
      ><span class="devsite-nav-text" tooltip>BitbucketCloudConfig</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BitbucketDataCenterConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BitbucketDataCenterConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.BitbucketDataCenterConfig"
      ><span class="devsite-nav-text" tooltip>BitbucketDataCenterConfig</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Connection</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Connection"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Connection"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Connection"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Connection.AnnotationsEntry"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Connection.AnnotationsEntry"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Connection.AnnotationsEntry"
      ><span class="devsite-nav-text" tooltip>AnnotationsEntry</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.CreateConnectionRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.CreateConnectionRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.CreateConnectionRequest"
      ><span class="devsite-nav-text" tooltip>CreateConnectionRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.CreateRepositoryRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.CreateRepositoryRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.CreateRepositoryRequest"
      ><span class="devsite-nav-text" tooltip>CreateRepositoryRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.DeleteConnectionRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.DeleteConnectionRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.DeleteConnectionRequest"
      ><span class="devsite-nav-text" tooltip>DeleteConnectionRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.DeleteRepositoryRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.DeleteRepositoryRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.DeleteRepositoryRequest"
      ><span class="devsite-nav-text" tooltip>DeleteRepositoryRequest</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>FetchGitRefsRequest</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchGitRefsRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchGitRefsRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchGitRefsRequest"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchGitRefsRequest.RefType"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchGitRefsRequest.RefType"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchGitRefsRequest.RefType"
      ><span class="devsite-nav-text" tooltip>RefType</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchGitRefsResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchGitRefsResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchGitRefsResponse"
      ><span class="devsite-nav-text" tooltip>FetchGitRefsResponse</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesRequest"
      ><span class="devsite-nav-text" tooltip>FetchLinkableRepositoriesRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesResponse"
      ><span class="devsite-nav-text" tooltip>FetchLinkableRepositoriesResponse</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadTokenRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadTokenRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadTokenRequest"
      ><span class="devsite-nav-text" tooltip>FetchReadTokenRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadTokenResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadTokenResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadTokenResponse"
      ><span class="devsite-nav-text" tooltip>FetchReadTokenResponse</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadWriteTokenRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadWriteTokenRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadWriteTokenRequest"
      ><span class="devsite-nav-text" tooltip>FetchReadWriteTokenRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadWriteTokenResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadWriteTokenResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchReadWriteTokenResponse"
      ><span class="devsite-nav-text" tooltip>FetchReadWriteTokenResponse</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GetConnectionRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GetConnectionRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GetConnectionRequest"
      ><span class="devsite-nav-text" tooltip>GetConnectionRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GetRepositoryRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GetRepositoryRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GetRepositoryRequest"
      ><span class="devsite-nav-text" tooltip>GetRepositoryRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitHubConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitHubConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitHubConfig"
      ><span class="devsite-nav-text" tooltip>GitHubConfig</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitHubEnterpriseConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitHubEnterpriseConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitHubEnterpriseConfig"
      ><span class="devsite-nav-text" tooltip>GitHubEnterpriseConfig</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitLabConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitLabConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.GitLabConfig"
      ><span class="devsite-nav-text" tooltip>GitLabConfig</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>InstallationState</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.InstallationState"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.InstallationState"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.InstallationState"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.InstallationState.Stage"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.InstallationState.Stage"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.InstallationState.Stage"
      ><span class="devsite-nav-text" tooltip>Stage</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListConnectionsRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListConnectionsRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListConnectionsRequest"
      ><span class="devsite-nav-text" tooltip>ListConnectionsRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListConnectionsResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListConnectionsResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListConnectionsResponse"
      ><span class="devsite-nav-text" tooltip>ListConnectionsResponse</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListRepositoriesRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListRepositoriesRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListRepositoriesRequest"
      ><span class="devsite-nav-text" tooltip>ListRepositoriesRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListRepositoriesResponse"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListRepositoriesResponse"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ListRepositoriesResponse"
      ><span class="devsite-nav-text" tooltip>ListRepositoriesResponse</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.OAuthCredential"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.OAuthCredential"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.OAuthCredential"
      ><span class="devsite-nav-text" tooltip>OAuthCredential</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.OperationMetadata"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.OperationMetadata"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.OperationMetadata"
      ><span class="devsite-nav-text" tooltip>OperationMetadata</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ProcessWebhookRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ProcessWebhookRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ProcessWebhookRequest"
      ><span class="devsite-nav-text" tooltip>ProcessWebhookRequest</span></a></li><li class="devsite-nav-item
           devsite-nav-expandable"><div class="devsite-expandable-nav">
      <a class="devsite-nav-toggle" aria-hidden="true"></a><div class="devsite-nav-title devsite-nav-title-no-path" tabindex="0" role="button">
        <span class="devsite-nav-text" tooltip>Repository</span>
      </div><ul class="devsite-nav-section"><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Repository"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Repository"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Repository"
      ><span class="devsite-nav-text" tooltip>Overview</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Repository.AnnotationsEntry"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Repository.AnnotationsEntry"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.Repository.AnnotationsEntry"
      ><span class="devsite-nav-text" tooltip>AnnotationsEntry</span></a></li></ul></div></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.RunWorkflowCustomOperationMetadata"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.RunWorkflowCustomOperationMetadata"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.RunWorkflowCustomOperationMetadata"
      ><span class="devsite-nav-text" tooltip>RunWorkflowCustomOperationMetadata</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ServiceDirectoryConfig"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ServiceDirectoryConfig"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.ServiceDirectoryConfig"
      ><span class="devsite-nav-text" tooltip>ServiceDirectoryConfig</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.UpdateConnectionRequest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.UpdateConnectionRequest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.UpdateConnectionRequest"
      ><span class="devsite-nav-text" tooltip>UpdateConnectionRequest</span></a></li><li class="devsite-nav-item"><a href="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.UserCredential"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.UserCredential"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.UserCredential"
      ><span class="devsite-nav-text" tooltip>UserCredential</span></a></li></ul></div></li></ul></div></li></ul></div></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-capacityplanner/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-capacityplanner/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-capacityplanner/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-capacityplanner</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/certificatemanager/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/certificatemanager/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/certificatemanager/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-certificate-manager</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudchannel/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudchannel/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudchannel/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-channel</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-chronicle/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-chronicle/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-chronicle/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-chronicle</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-cloudcontrolspartner/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-cloudcontrolspartner/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-cloudcontrolspartner/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-cloudcontrolspartner</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-cloudsecuritycompliance/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-cloudsecuritycompliance/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-cloudsecuritycompliance/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-cloudsecuritycompliance</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/procurement/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/procurement/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/procurement/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-commerce-consumer-procurement</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/common/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/common/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/common/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-common</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/compute/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/compute/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/compute/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-compute</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-compute-v1beta/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-compute-v1beta/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-compute-v1beta/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-compute-v1beta</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/confidentialcomputing/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/confidentialcomputing/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/confidentialcomputing/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-confidentialcomputing</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/config/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/config/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/config/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-config</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-configdelivery/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-configdelivery/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-configdelivery/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-configdelivery</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/contactcenterinsights/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/contactcenterinsights/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/contactcenterinsights/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-contact-center-insights</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/container/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/container/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/container/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-container</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/containeranalysis/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/containeranalysis/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/containeranalysis/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-containeranalysis</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/contentwarehouse/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/contentwarehouse/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/contentwarehouse/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-contentwarehouse</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-core/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-core/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-core/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-core</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/datafusion/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/datafusion/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/datafusion/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-data-fusion</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/dataqna/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/dataqna/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/dataqna/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-data-qna</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-databasecenter/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-databasecenter/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-databasecenter/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-databasecenter</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/datacatalog/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/datacatalog/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/datacatalog/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-datacatalog</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/lineage/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/lineage/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/lineage/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-datacatalog-lineage</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/dataflow/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/dataflow/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/dataflow/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-dataflow-client</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/dataform/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/dataform/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/dataform/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-dataform</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/datalabeling/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/datalabeling/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/datalabeling/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-datalabeling</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/dataplex/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/dataplex/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/dataplex/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-dataplex</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/dataproc/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/dataproc/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/dataproc/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-dataproc</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/metastore/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/metastore/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/metastore/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-dataproc-metastore</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/datastore/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/datastore/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/datastore/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-datastore</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/datastream/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/datastream/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/datastream/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-datastream</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/clouddebugger/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/clouddebugger/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/clouddebugger/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-debugger-client</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/clouddeploy/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/clouddeploy/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/clouddeploy/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-deploy</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-developerconnect/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-developerconnect/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-developerconnect/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-developerconnect</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-devicestreaming/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-devicestreaming/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-devicestreaming/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-devicestreaming</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/dialogflow/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/dialogflow/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/dialogflow/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-dialogflow</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/dialogflow-cx/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/dialogflow-cx/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/dialogflow-cx/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-dialogflow-cx</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/discoveryengine/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/discoveryengine/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/discoveryengine/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-discoveryengine</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/dlp/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/dlp/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/dlp/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-dlp</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/datamigration/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/datamigration/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/datamigration/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-dms</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/dns/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/dns/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/dns/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-dns</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/documentai/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/documentai/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/documentai/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-documentai</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/documentai-toolbox/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/documentai-toolbox/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/documentai-toolbox/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-documentai-toolbox</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/domains/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/domains/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/domains/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-domains</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/edgecontainer/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/edgecontainer/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/edgecontainer/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-edgecontainer</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-edgenetwork/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-edgenetwork/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-edgenetwork/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-edgenetwork</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/enterpriseknowledgegraph/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/enterpriseknowledgegraph/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/enterpriseknowledgegraph/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-enterpriseknowledgegraph</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/clouderrorreporting/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/clouderrorreporting/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/clouderrorreporting/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-error-reporting</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/essentialcontacts/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/essentialcontacts/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/essentialcontacts/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-essential-contacts</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/eventarc/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/eventarc/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/eventarc/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-eventarc</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/eventarcpublishing/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/eventarcpublishing/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/eventarcpublishing/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-eventarc-publishing</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/file/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/file/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/file/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-filestore</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-financialservices/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-financialservices/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-financialservices/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-financialservices</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/firestore/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/firestore/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/firestore/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-firestore</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudfunctions/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudfunctions/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudfunctions/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-functions</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/gameservices/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/gameservices/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/gameservices/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-game-servers</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-gdchardwaremanagement/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-gdchardwaremanagement/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-gdchardwaremanagement/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-gdchardwaremanagement</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-geminidataanalytics/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-geminidataanalytics/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-geminidataanalytics/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-geminidataanalytics</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/gkebackup/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/gkebackup/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/gkebackup/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-gke-backup</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/connectgateway/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/connectgateway/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/connectgateway/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-gke-connect-gateway</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/gkehub/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/gkehub/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/gkehub/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-gke-hub</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/gkemulticloud/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/gkemulticloud/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/gkemulticloud/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-gke-multicloud</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-gkerecommender/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-gkerecommender/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-gkerecommender/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-gkerecommender</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/gsuiteaddons/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/gsuiteaddons/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/gsuiteaddons/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-gsuiteaddons</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-hypercomputecluster/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-hypercomputecluster/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-hypercomputecluster/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-hypercomputecluster</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/iam/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/iam/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/iam/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-iam</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/iamlogging/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/iamlogging/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/iamlogging/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-iam-logging</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/iap/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/iap/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/iap/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-iap</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/ids/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/ids/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/ids/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-ids</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudiot/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudiot/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudiot/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-iot</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudkms/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudkms/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudkms/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-kms</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/inventory/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/inventory/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/inventory/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-kms-inventory</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/language/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/language/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/language/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-language</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-licensemanager/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-licensemanager/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-licensemanager/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-licensemanager</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/lifesciences/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/lifesciences/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/lifesciences/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-life-sciences</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-locationfinder/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-locationfinder/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-locationfinder/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-locationfinder</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/logging/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/logging/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/logging/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-logging</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-lustre/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-lustre/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-lustre/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-lustre</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-maintenance-api/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-maintenance-api/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-maintenance-api/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-maintenance-api</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/managedidentities/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/managedidentities/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/managedidentities/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-managed-identities</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-managedkafka/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-managedkafka/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-managedkafka/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-managedkafka</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-managedkafka-schemaregistry/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-managedkafka-schemaregistry/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-managedkafka-schemaregistry</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/mediatranslation/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/mediatranslation/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/mediatranslation/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-media-translation</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/memcache/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/memcache/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/memcache/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-memcache</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-memorystore/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-memorystore/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-memorystore/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-memorystore</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/migrationcenter/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/migrationcenter/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/migrationcenter/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-migrationcenter</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-modelarmor/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-modelarmor/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-modelarmor/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-modelarmor</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/monitoring/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/monitoring/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/monitoring/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-monitoring</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/monitoring-dashboards/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/monitoring-dashboards/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/monitoring-dashboards/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-monitoring-dashboards</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-monitoring-metrics-scopes/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-monitoring-metrics-scopes/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-monitoring-metrics-scopes/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-monitoring-metrics-scopes</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/netapp/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/netapp/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/netapp/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-netapp</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/networkconnectivity/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/networkconnectivity/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/networkconnectivity/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-network-connectivity</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/networkmanagement/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/networkmanagement/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/networkmanagement/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-network-management</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/networksecurity/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/networksecurity/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/networksecurity/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-network-security</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/networkservices/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/networkservices/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/networkservices/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-network-services</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/notebooks/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/notebooks/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/notebooks/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-notebooks</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/optimization/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/optimization/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/optimization/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-optimization</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-oracledatabase/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-oracledatabase/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-oracledatabase/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-oracledatabase</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/composer/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/composer/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/composer/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-orchestration-airflow</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/orgpolicy/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/orgpolicy/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/orgpolicy/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-org-policy</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/osconfig/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/osconfig/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/osconfig/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-os-config</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/oslogin/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/oslogin/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/oslogin/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-os-login</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-parallelstore/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-parallelstore/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-parallelstore/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-parallelstore</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-parametermanager/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-parametermanager/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-parametermanager/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-parametermanager</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/phishingprotection/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/phishingprotection/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/phishingprotection/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-phishing-protection</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/policytroubleshooter/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/policytroubleshooter/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/policytroubleshooter/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-policy-troubleshooter</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/policysimulator/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/policysimulator/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/policysimulator/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-policysimulator</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/policytroubleshooter-iam/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/policytroubleshooter-iam/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/policytroubleshooter-iam/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-policytroubleshooter-iam</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/privateca/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/privateca/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/privateca/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-private-ca</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudprivatecatalog/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudprivatecatalog/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudprivatecatalog/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-private-catalog</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-privilegedaccessmanager/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-privilegedaccessmanager/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-privilegedaccessmanager/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-privilegedaccessmanager</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/pubsub/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/pubsub/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/pubsub/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-pubsub</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/pubsublite/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/pubsublite/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/pubsublite/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-pubsublite</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-cloudquotas/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-cloudquotas/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-cloudquotas/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-quotas</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/rapidmigrationassessment/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/rapidmigrationassessment/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/rapidmigrationassessment/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-rapidmigrationassessment</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/recaptchaenterprise/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/recaptchaenterprise/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/recaptchaenterprise/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-recaptcha-enterprise</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/recommendationengine/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/recommendationengine/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/recommendationengine/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-recommendations-ai</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/recommender/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/recommender/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/recommender/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-recommender</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/redis/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/redis/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/redis/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-redis</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-redis-cluster/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-redis-cluster/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-redis-cluster/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-redis-cluster</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudresourcemanager/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudresourcemanager/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudresourcemanager/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-resource-manager</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/retail/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/retail/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/retail/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-retail</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/run/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/run/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/run/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-run</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/runtimeconfig/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/runtimeconfig/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/runtimeconfig/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-runtimeconfig</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-saasplatform-saasservicemgmt</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudscheduler/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudscheduler/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudscheduler/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-scheduler</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/secretmanager/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/secretmanager/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/secretmanager/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-secret-manager</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/securesourcemanager/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/securesourcemanager/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/securesourcemanager/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-securesourcemanager</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/publicca/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/publicca/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/publicca/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-security-publicca</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/securitycenter/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/securitycenter/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/securitycenter/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-securitycenter</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-securitycentermanagement/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-securitycentermanagement/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-securitycentermanagement/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-securitycentermanagement</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/servicecontrol/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/servicecontrol/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/servicecontrol/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-service-control</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/servicedirectory/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/servicedirectory/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/servicedirectory/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-service-directory</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/servicemanagement/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/servicemanagement/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/servicemanagement/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-service-management</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/serviceusage/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/serviceusage/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/serviceusage/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-service-usage</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-servicehealth/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-servicehealth/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-servicehealth/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-servicehealth</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudshell/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudshell/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudshell/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-shell</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/source/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/source/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/source/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-source-context</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/spanner/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/spanner/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/spanner/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-spanner</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/speech/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/speech/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/speech/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-speech</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/storage/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/storage/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/storage/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-storage</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-storage-control/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-storage-control/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-storage-control/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-storage-control</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/storagetransfer/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/storagetransfer/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/storagetransfer/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-storage-transfer</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-storagebatchoperations/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-storagebatchoperations/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-storagebatchoperations/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-storagebatchoperations</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/storageinsights/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/storageinsights/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/storageinsights/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-storageinsights</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/support/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/support/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/support/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-support</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/talent/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/talent/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/talent/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-talent</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudtasks/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudtasks/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudtasks/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-tasks</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-telcoautomation/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-telcoautomation/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-telcoautomation/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-telcoautomation</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/texttospeech/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/texttospeech/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/texttospeech/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-texttospeech</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/tpu/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/tpu/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/tpu/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-tpu</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/cloudtrace/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/cloudtrace/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/cloudtrace/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-trace</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/translate/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/translate/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/translate/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-translate</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-vectorsearch/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-vectorsearch/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-vectorsearch/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-vectorsearch</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/vertexai/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/vertexai/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/vertexai/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-vertexai</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/livestream/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/livestream/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/livestream/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-video-live-stream</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/videostitcher/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/videostitcher/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/videostitcher/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-video-stitcher</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/transcoder/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/transcoder/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/transcoder/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-video-transcoder</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/videointelligence/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/videointelligence/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/videointelligence/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-videointelligence</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/vision/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/vision/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/vision/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-vision</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-cloud-visionai/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-cloud-visionai/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-cloud-visionai/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-visionai</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/vmmigration/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/vmmigration/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/vmmigration/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-vm-migration</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/vmwareengine/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/vmwareengine/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/vmwareengine/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-vmwareengine</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/vpcaccess/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/vpcaccess/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/vpcaccess/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-vpc-access</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/webrisk/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/webrisk/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/webrisk/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-webrisk</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/websecurityscanner/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/websecurityscanner/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/websecurityscanner/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-websecurityscanner</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/workflows/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/workflows/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/workflows/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-workflows</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/workstations/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/workstations/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/workstations/latest"
      ><span class="devsite-nav-text" tooltip>google-cloud-workstations</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/google-resumable-media/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/google-resumable-media/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/google-resumable-media/latest"
      ><span class="devsite-nav-text" tooltip>google-resumable-media</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/googleapis-common-protos/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/googleapis-common-protos/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/googleapis-common-protos/latest"
      ><span class="devsite-nav-text" tooltip>googleapis-common-protos</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/grpc-iam/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/grpc-iam/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/grpc-iam/latest"
      ><span class="devsite-nav-text" tooltip>grpc-google-iam-v1</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/langchain-google-alloydb-pg/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/langchain-google-alloydb-pg/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/langchain-google-alloydb-pg/latest"
      ><span class="devsite-nav-text" tooltip>langchain-google-alloydb-pg</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/langchain-google-bigtable/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/langchain-google-bigtable/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/langchain-google-bigtable/latest"
      ><span class="devsite-nav-text" tooltip>langchain-google-bigtable</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/langchain-google-cloud-sql-mssql/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/langchain-google-cloud-sql-mssql/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/langchain-google-cloud-sql-mssql/latest"
      ><span class="devsite-nav-text" tooltip>langchain-google-cloud-sql-mssql</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/langchain-google-cloud-sql-mysql/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/langchain-google-cloud-sql-mysql/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/langchain-google-cloud-sql-mysql/latest"
      ><span class="devsite-nav-text" tooltip>langchain-google-cloud-sql-mysql</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/langchain-google-cloud-sql-pg/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/langchain-google-cloud-sql-pg/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/langchain-google-cloud-sql-pg/latest"
      ><span class="devsite-nav-text" tooltip>langchain-google-cloud-sql-pg</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/langchain-google-datastore/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/langchain-google-datastore/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/langchain-google-datastore/latest"
      ><span class="devsite-nav-text" tooltip>langchain-google-datastore</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/langchain-google-el-carro/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/langchain-google-el-carro/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/langchain-google-el-carro/latest"
      ><span class="devsite-nav-text" tooltip>langchain-google-el-carro</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/langchain-google-firestore/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/langchain-google-firestore/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/langchain-google-firestore/latest"
      ><span class="devsite-nav-text" tooltip>langchain-google-firestore</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/langchain-google-memorystore-redis/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/langchain-google-memorystore-redis/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/langchain-google-memorystore-redis/latest"
      ><span class="devsite-nav-text" tooltip>langchain-google-memorystore-redis</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/langchain-google-spanner/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/langchain-google-spanner/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/langchain-google-spanner/latest"
      ><span class="devsite-nav-text" tooltip>langchain-google-spanner</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/llama-index-alloydb-pg/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/llama-index-alloydb-pg/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/llama-index-alloydb-pg/latest"
      ><span class="devsite-nav-text" tooltip>llama-index-alloydb-pg</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/llama-index-cloud-sql-pg/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/llama-index-cloud-sql-pg/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/llama-index-cloud-sql-pg/latest"
      ><span class="devsite-nav-text" tooltip>llama-index-cloud-sql-pg</span></a></li>

  <li class="devsite-nav-item"><a href="/python/docs/reference/llama-index-spanner/latest"
        class="devsite-nav-title gc-analytics-event"
        data-category="Site-Wide Custom Events"
        data-label="Book nav link, pathname: /python/docs/reference/llama-index-spanner/latest"
        track-type="bookNav"
        track-name="click"
        track-metadata-eventdetail="/python/docs/reference/llama-index-spanner/latest"
      ><span class="devsite-nav-text" tooltip>llama-index-spanner</span></a></li>
          </ul>
        
        
          
    
      
      <ul class="devsite-nav-list" menu="Technology areas"
          aria-label="Side menu" hidden>
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/ai-ml"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: AI and ML"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      AI and ML
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/application-development"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Application development"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Application development
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/application-hosting"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Application hosting"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Application hosting
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/compute-area"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Compute"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Compute
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/data"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Data analytics and pipelines"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Data analytics and pipelines
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/databases"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Databases"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Databases
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/dhm-cloud"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Distributed, hybrid, and multicloud"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Distributed, hybrid, and multicloud
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/industry"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Industry solutions"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Industry solutions
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/migration"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Migration"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Migration
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/networking"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Networking"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Networking
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/observability"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Observability and monitoring"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Observability and monitoring
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/security"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Security"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Security
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/storage"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Storage"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Storage
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
    
      
      <ul class="devsite-nav-list" menu="Cross-product tools"
          aria-label="Side menu" hidden>
        
          
            
            
              
<li class="devsite-nav-item">

  
  <a href="/docs/access-resources"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Access and resources management"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Access and resources management
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/costs-usage"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Costs and usage management"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Costs and usage management
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/iac"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: Infrastructure as code"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      Infrastructure as code
   </span>
    
  
  </a>
  

</li>

            
              
<li class="devsite-nav-item">

  
  <a href="/docs/devtools"
    
       class="devsite-nav-title gc-analytics-event
              
              "
    

    
     data-category="Site-Wide Custom Events"
     data-label="Responsive Tab: SDK, languages, frameworks, and tools"
     track-type="navMenu"
     track-metadata-eventDetail="globalMenu"
     track-metadata-position="nav">
  
    <span class="devsite-nav-text" tooltip >
      SDK, languages, frameworks, and tools
   </span>
    
  
  </a>
  

</li>

            
          
        
      </ul>
    
  
        
        
          
    
  
    
  
    
  
    
  
        
      </div>
    
  </div>
</nav>
        
      </devsite-book-nav>
      <section id="gc-wrapper">
        <main role="main" id="main-content" class="devsite-main-content"
            
              has-book-nav
              has-sidebar
            >
          <div class="devsite-sidebar">
            <div class="devsite-sidebar-content">
                
                <devsite-toc class="devsite-nav"
                            role="navigation"
                            aria-label="On this page"
                            depth="2"
                            scrollbars
                  ></devsite-toc>
                <devsite-recommendations-sidebar class="nocontent devsite-nav">
                </devsite-recommendations-sidebar>
            </div>
          </div>
          <devsite-content>
            
              












<article class="devsite-article">
  
  
  
  
  

  <div class="devsite-article-meta nocontent" role="navigation">
    
    
    <ul class="devsite-breadcrumb-list"
  
    aria-label="Breadcrumb">
  
  <li class="devsite-breadcrumb-item
             ">
    
    
    
      
        
  <a href="https://docs.cloud.google.com/"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="1"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="1"
      
        track-metadata-eventdetail="Google Cloud Documentation"
      
    >
    
          Home
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://docs.cloud.google.com/docs"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="2"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="2"
      
        track-metadata-eventdetail="Documentation"
      
    >
    
          Documentation
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://docs.cloud.google.com/docs/costs-usage"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="3"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="3"
      
        track-metadata-eventdetail="{{gcp_name_short}} SDK, languages, frameworks, and tools
"
      
    >
    
          Developer tools
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://docs.cloud.google.com/python/docs"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="4"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="4"
      
        track-metadata-eventdetail="Python"
      
    >
    
          Python
        
  </a>
  
      
    
  </li>
  
  <li class="devsite-breadcrumb-item
             ">
    
      
      <div class="devsite-breadcrumb-guillemet material-icons" aria-hidden="true"></div>
    
    
    
      
        
  <a href="https://docs.cloud.google.com/python/docs/reference"
      
        class="devsite-breadcrumb-link gc-analytics-event"
      
        data-category="Site-Wide Custom Events"
      
        data-label="Breadcrumbs"
      
        data-value="5"
      
        track-type="globalNav"
      
        track-name="breadcrumb"
      
        track-metadata-position="5"
      
        track-metadata-eventdetail="Python client libraries"
      
    >
    
          Client libraries
        
  </a>
  
      
    
  </li>
  
</ul>
    
      
    <devsite-thumb-rating position="header">
    </devsite-thumb-rating>
  
    
  </div>
  
    <devsite-feedback
  position="header"
  project-name="Python client libraries"
  product-id="1632431"
  bucket="python"
  context=""
  version="t-devsite-webserver-20260310-r00-rc00.476021692791623284"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="header"
  class="nocontent"
  
  
  
    project-icon="https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/images/favicons/onecloud/super_cloud.png"
  
  
  
  >

  <button>
  
    
    Send feedback
  
  </button>
</devsite-feedback>
  <devsite-actions hidden data-nosnippet><devsite-feature-tooltip
      ack-key="AckCollectionsBookmarkTooltipDismiss"
      analytics-category="Site-Wide Custom Events"
      analytics-action-show="Callout Profile displayed"
      analytics-action-close="Callout Profile dismissed"
      analytics-label="Create Collection Callout"
      class="devsite-page-bookmark-tooltip nocontent"
      dismiss-button="true"
      id="devsite-collections-dropdown"
      
      dismiss-button-text="Dismiss"

      
      close-button-text="Got it">

    
    
      <devsite-bookmark></devsite-bookmark>
    

    <span slot="popout-heading">
      
      Stay organized with collections
    </span>
    <span slot="popout-contents">
      
      Save and categorize content based on your preferences.
    </span>
  </devsite-feature-tooltip></devsite-actions>
  
    
  

  <devsite-toc class="devsite-nav"
    depth="2"
    devsite-toc-embedded
    >
  </devsite-toc>
  
    
  <div class="devsite-article-body clearfix
  devsite-no-page-title">

  
    
    
    
    











<cloudx-select-dropdown>
  <button class="button button-with-icon cloud-select-dropdown__button " aria-haspopup="true" >Version latest<span class="material-icons icon-after cloud-select-dropdown__icon" aria-hidden="true" translate="no">keyboard_arrow_down</i></button>
  <ul class="cloud-select-dropdown__items" role="menu" tabindex="0">
    

  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.35.0 (latest)" track-metadata-eventdetail="/python/docs/reference/cloudbuild/latest" href="/python/docs/reference/cloudbuild/latest" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.35.0 (latest)
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.34.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.34.0" href="/python/docs/reference/cloudbuild/3.34.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.34.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.33.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.33.0" href="/python/docs/reference/cloudbuild/3.33.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.33.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.32.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.32.0" href="/python/docs/reference/cloudbuild/3.32.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.32.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.31.3" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.31.3" href="/python/docs/reference/cloudbuild/3.31.3" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.31.3
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.30.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.30.0" href="/python/docs/reference/cloudbuild/3.30.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.30.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.29.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.29.0" href="/python/docs/reference/cloudbuild/3.29.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.29.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.28.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.28.0" href="/python/docs/reference/cloudbuild/3.28.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.28.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.27.1" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.27.1" href="/python/docs/reference/cloudbuild/3.27.1" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.27.1
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.26.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.26.0" href="/python/docs/reference/cloudbuild/3.26.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.26.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.25.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.25.0" href="/python/docs/reference/cloudbuild/3.25.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.25.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.24.2" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.24.2" href="/python/docs/reference/cloudbuild/3.24.2" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.24.2
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.23.3" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.23.3" href="/python/docs/reference/cloudbuild/3.23.3" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.23.3
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.22.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.22.0" href="/python/docs/reference/cloudbuild/3.22.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.22.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.21.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.21.0" href="/python/docs/reference/cloudbuild/3.21.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.21.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.20.1" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.20.1" href="/python/docs/reference/cloudbuild/3.20.1" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.20.1
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.19.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.19.0" href="/python/docs/reference/cloudbuild/3.19.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.19.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.18.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.18.0" href="/python/docs/reference/cloudbuild/3.18.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.18.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.17.1" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.17.1" href="/python/docs/reference/cloudbuild/3.17.1" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.17.1
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.16.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.16.0" href="/python/docs/reference/cloudbuild/3.16.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.16.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.15.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.15.0" href="/python/docs/reference/cloudbuild/3.15.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.15.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.14.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.14.0" href="/python/docs/reference/cloudbuild/3.14.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.14.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.13.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.13.0" href="/python/docs/reference/cloudbuild/3.13.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.13.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.12.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.12.0" href="/python/docs/reference/cloudbuild/3.12.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.12.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.11.1" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.11.1" href="/python/docs/reference/cloudbuild/3.11.1" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.11.1
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.10.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.10.0" href="/python/docs/reference/cloudbuild/3.10.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.10.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.9.3" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.9.3" href="/python/docs/reference/cloudbuild/3.9.3" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.9.3
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.8.3" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.8.3" href="/python/docs/reference/cloudbuild/3.8.3" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.8.3
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.7.1" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.7.1" href="/python/docs/reference/cloudbuild/3.7.1" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.7.1
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.6.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.6.0" href="/python/docs/reference/cloudbuild/3.6.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.6.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.5.2" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.5.2" href="/python/docs/reference/cloudbuild/3.5.2" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.5.2
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.4.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.4.0" href="/python/docs/reference/cloudbuild/3.4.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.4.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.3.2" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.3.2" href="/python/docs/reference/cloudbuild/3.3.2" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.3.2
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.2.1" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.2.1" href="/python/docs/reference/cloudbuild/3.2.1" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.2.1
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.1.1" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.1.1" href="/python/docs/reference/cloudbuild/3.1.1" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.1.1
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="3.0.2" track-metadata-eventdetail="/python/docs/reference/cloudbuild/3.0.2" href="/python/docs/reference/cloudbuild/3.0.2" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  3.0.2
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="2.0.2" track-metadata-eventdetail="/python/docs/reference/cloudbuild/2.0.2" href="/python/docs/reference/cloudbuild/2.0.2" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  2.0.2
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="1.1.2" track-metadata-eventdetail="/python/docs/reference/cloudbuild/1.1.2" href="/python/docs/reference/cloudbuild/1.1.2" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  1.1.2
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="1.0.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/1.0.0" href="/python/docs/reference/cloudbuild/1.0.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  1.0.0
</a>
</li>


  
  



<li class="cloud-select-dropdown__item">
  <a track-type="cloud select dropdown" track-name="0.1.0" track-metadata-eventdetail="/python/docs/reference/cloudbuild/0.1.0" href="/python/docs/reference/cloudbuild/0.1.0" role="menuitem" class="cloud-select-dropdown__item-link" tabindex="-1">
  0.1.0
</a>
</li>



  </ul>
</cloudx-select-dropdown>


    
    
    
    <div>
      <article>
<h1 id="python-client-for-cloud-build" data-text="Python Client for Cloud Build" tabindex="-1">Python Client for Cloud Build</h1>


<p><a href="https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels"><img src="https://img.shields.io/badge/support-stable-gold.svg" alt="image"></a> <a href="https://pypi.org/project/google-cloud-build/"><img src="https://img.shields.io/pypi/v/google-cloud-build.svg" alt="image"></a> <a href="https://pypi.org/project/google-cloud-build/"><img src="https://img.shields.io/pypi/pyversions/google-cloud-build.svg" alt="image"></a></p>
<p><a href="https://cloud.google.com/cloud-build/docs/">Cloud Build</a>: lets you build software quickly across all languages. Get complete control over defining custom workflows for building, testing, and deploying across multiple environments such as VMs, serverless, Kubernetes, or Firebase.</p>
<ul>
<li><p><a href="https://cloud.google.com/python/docs/reference/cloudbuild/latest/summary_overview">Client Library Documentation</a></p>
</li>
<li><p><a href="https://cloud.google.com/cloud-build/docs/">Product Documentation</a></p>
</li>
</ul>
<h2 id="quick-start" data-text="Quick Start" tabindex="-1">Quick Start</h2>
<p>In order to use this library, you first need to go through the following steps:</p>
<ol>
<li><p><a href="https://console.cloud.google.com/project">Select or create a Cloud Platform project.</a></p>
</li>
<li><p><a href="https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project">Enable billing for your project.</a></p>
</li>
<li><p><a href="https://cloud.google.com/cloud-build/docs/">Enable the Cloud Build.</a></p>
</li>
<li><p><a href="https://googleapis.dev/python/google-api-core/latest/auth.html">Set up Authentication.</a></p>
</li>
</ol>
<h3 id="installation" data-text="Installation" tabindex="-1">Installation</h3>
<p>Install this library in a virtual environment using <a href="https://docs.python.org/3/library/venv.html">venv</a>. <a href="https://docs.python.org/3/library/venv.html">venv</a> is a tool that
creates isolated Python environments. These isolated environments can have separate
versions of Python packages, which allows you to isolate one project’s dependencies
from the dependencies of other projects.</p>
<p>With <a href="https://docs.python.org/3/library/venv.html">venv</a>, it’s possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.</p>
<h3 id="code-samples-and-snippets" data-text="Code samples and snippets" tabindex="-1">Code samples and snippets</h3>
<p>Code samples and snippets live in the <a href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-build/samples">samples/</a> folder.</p>
<h4 id="supported-python-versions" data-text="Supported Python Versions" tabindex="-1">Supported Python Versions</h4>
<p>Our client libraries are compatible with all current <a href="https://devguide.python.org/devcycle/#in-development-main-branch">active</a> and <a href="https://devguide.python.org/devcycle/#maintenance-branches">maintenance</a> versions of
Python.</p>
<p>Python &gt;= 3.7, including 3.14</p>
<h4 id="unsupported-python-versions" data-text="Unsupported Python Versions" tabindex="-1">Unsupported Python Versions</h4>
<p>Python &lt;= 3.6</p>
<p>If you are using an <a href="https://devguide.python.org/devcycle/#end-of-life-branches">end-of-life</a>
version of Python, we recommend that you update as soon as possible to an actively supported version.</p>
<h4 id="maclinux" data-text="Mac/Linux" tabindex="-1">Mac/Linux</h4>
<div></div><devsite-code><pre translate="no" dir="ltr" is-upgraded><code class="prettyprint lang-console" translate="no" dir="ltr">python3 -m venv &lt;your-env&gt;
source &lt;your-env&gt;/bin/activate
pip install google-cloud-build
</code></pre></devsite-code><h4 id="windows" data-text="Windows" tabindex="-1">Windows</h4>
<div></div><devsite-code><pre translate="no" dir="ltr" is-upgraded><code class="prettyprint lang-console" translate="no" dir="ltr">py -m venv &lt;your-env&gt;
.\&lt;your-env&gt;\Scripts\activate
pip install google-cloud-build
</code></pre></devsite-code><h3 id="next-steps" data-text="Next Steps" tabindex="-1">Next Steps</h3>
<ul>
<li><p>Read the <a href="https://cloud.google.com/python/docs/reference/cloudbuild/latest/summary_overview">Client Library Documentation</a> for Cloud Build
to see other available methods on the client.</p>
</li>
<li><p>Read the <a href="https://cloud.google.com/cloud-build/docs/">Cloud Build Product documentation</a> to learn
more about the product and see How-to Guides.</p>
</li>
<li><p>View this <a href="https://github.com/googleapis/google-cloud-python/blob/main/README.rst">README</a> to see the full list of Cloud
APIs that we cover.</p>
</li>
</ul>
<h2 id="logging" data-text="Logging" tabindex="-1">Logging</h2>
<p>This library uses the standard Python <code translate="no" dir="ltr">logging</code> functionality to log some RPC events that could be of interest for debugging and monitoring purposes.
Note the following:</p>
<ol>
<li><p>Logs may contain sensitive information. Take care to <strong>restrict access to the logs</strong> if they are saved, whether it be on local storage or on Google Cloud Logging.</p>
</li>
<li><p>Google may refine the occurrence, level, and content of various log messages in this library without flagging such changes as breaking. <strong>Do not depend on immutability of the logging events</strong>.</p>
</li>
<li><p>By default, the logging events from this library are not handled. You must <strong>explicitly configure log handling</strong> using one of the mechanisms below.</p>
</li>
</ol>
<h3 id="simple-environment-based-configuration" data-text="Simple, environment-based configuration" tabindex="-1">Simple, environment-based configuration</h3>
<p>To enable logging for this library without any changes in your code, set the <code translate="no" dir="ltr">GOOGLE_SDK_PYTHON_LOGGING_SCOPE</code> environment variable to a valid Google
logging scope. This configures handling of logging events (at level <code translate="no" dir="ltr">logging.DEBUG</code> or higher) from this library in a default manner, emitting the logged
messages in a structured format. It does not currently allow customizing the logging levels captured nor the handlers, formatters, etc. used for any logging
event.</p>
<p>A logging scope is a period-separated namespace that begins with <code translate="no" dir="ltr">google</code>, identifying the Python module or package to log.</p>
<ul>
<li><p>Valid logging scopes: <code translate="no" dir="ltr">google</code>, <code translate="no" dir="ltr">google.cloud.asset.v1</code>, <code translate="no" dir="ltr">google.api</code>, <code translate="no" dir="ltr">google.auth</code>, etc.</p>
</li>
<li><p>Invalid logging scopes: <code translate="no" dir="ltr">foo</code>, <code translate="no" dir="ltr">123</code>, etc.</p>
</li>
</ul>
<p><strong>NOTE</strong>: If the logging scope is invalid, the library does not set up any logging handlers.</p>
<h4 id="environment-based-examples" data-text="Environment-Based Examples" tabindex="-1">Environment-Based Examples</h4>
<ul>
<li>Enabling the default handler for all Google-based loggers</li>
</ul>
<div></div><devsite-code><pre translate="no" dir="ltr" is-upgraded><code class="prettyprint lang-console" translate="no" dir="ltr">export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google
</code></pre></devsite-code><ul>
<li>Enabling the default handler for a specific Google module (for a client library called <code translate="no" dir="ltr">library_v1</code>):</li>
</ul>
<div></div><devsite-code><pre translate="no" dir="ltr" is-upgraded><code class="prettyprint lang-console" translate="no" dir="ltr">export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google.cloud.library_v1
</code></pre></devsite-code><h3 id="advanced-code-based-configuration" data-text="Advanced, code-based configuration" tabindex="-1">Advanced, code-based configuration</h3>
<p>You can also configure a valid logging scope using Python’s standard logging mechanism.</p>
<h4 id="code-based-examples" data-text="Code-Based Examples" tabindex="-1">Code-Based Examples</h4>
<ul>
<li>Configuring a handler for all Google-based loggers</li>
</ul>
<div></div><devsite-code><pre translate="no" dir="ltr" is-upgraded><code class="prettyprint lang-python" translate="no" dir="ltr">import logging

from google.cloud import library_v1

base_logger = logging.getLogger(&#34;google&#34;)
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
</code></pre></devsite-code><ul>
<li>Configuring a handler for a specific Google module (for a client library called <code translate="no" dir="ltr">library_v1</code>):</li>
</ul>
<div></div><devsite-code><pre translate="no" dir="ltr" is-upgraded><code class="prettyprint lang-python" translate="no" dir="ltr">import logging

from google.cloud import library_v1

base_logger = logging.getLogger(&#34;google.cloud.library_v1&#34;)
base_logger.addHandler(logging.StreamHandler())
base_logger.setLevel(logging.DEBUG)
</code></pre></devsite-code><h3 id="logging-details" data-text="Logging details" tabindex="-1">Logging details</h3>
<ol>
<li><p>Regardless of which of the mechanisms above you use to configure logging for this library, by default logging events are not propagated up to the root
logger from the google-level logger. If you need the events to be propagated to the root logger, you must explicitly set
<code translate="no" dir="ltr">logging.getLogger(&#34;google&#34;).propagate = True</code> in your code.</p>
</li>
<li><p>You can mix the different logging configurations above for different Google modules. For example, you may want use a code-based logging configuration for
one library, but decide you need to also set up environment-based logging configuration for another library.</p>
<ol>
<li>If you attempt to use both code-based and environment-based configuration for the same module, the environment-based configuration will be ineffectual
if the code -based configuration gets applied first.</li>
</ol>
</li>
<li><p>The Google-specific logging configurations (default handlers for environment-based configuration; not propagating logging events to the root logger) get
executed the first time <em>any</em> client library is instantiated in your application, and only if the affected loggers have not been previously configured.
(This is the reason for 2.i. above.)</p>
</li>
</ol>

</article>
    </div>
    


  
  

  
    <devsite-hats-survey class="nocontent"
      hats-id="mwETRvWii0eU5NUYprb0Y9z5GVbc"
      listnr-id="83405"></devsite-hats-survey>
  

  
</div>

  
    
    
      
    <devsite-thumb-rating position="footer">
    </devsite-thumb-rating>
  
       
         <devsite-feedback
  position="footer"
  project-name="Python client libraries"
  product-id="1632431"
  bucket="python"
  context=""
  version="t-devsite-webserver-20260310-r00-rc00.476021692791623284"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="footer"
  class="nocontent"
  
  
  
    project-icon="https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/images/favicons/onecloud/super_cloud.png"
  
  
  
  >

  <button>
  
    
    Send feedback
  
  </button>
</devsite-feedback>
       
    
    
  

  <div class="devsite-floating-action-buttons"></div></article>


<devsite-content-footer class="nocontent">
  <p>Except as otherwise noted, the content of this page is licensed under the <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 License</a>, and code samples are licensed under the <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 License</a>. For details, see the <a href="https://developers.google.com/site-policies">Google Developers Site Policies</a>. Java is a registered trademark of Oracle and/or its affiliates.</p>
  <p>Last updated 2026-03-09 UTC.</p>
</devsite-content-footer>


<devsite-notification
>
</devsite-notification>


  
<div class="devsite-content-data">
  
    
    
    <template class="devsite-thumb-rating-feedback">
      <devsite-feedback
  position="thumb-rating"
  project-name="Python client libraries"
  product-id="1632431"
  bucket="python"
  context=""
  version="t-devsite-webserver-20260310-r00-rc00.476021692791623284"
  data-label="Send Feedback Button"
  track-type="feedback"
  track-name="sendFeedbackLink"
  track-metadata-position="thumb-rating"
  class="nocontent"
  
  
  
    project-icon="https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/images/favicons/onecloud/super_cloud.png"
  
  
  
  >

  <button>
  
    Need to tell us more?
  
  </button>
</devsite-feedback>
    </template>
  
  
    <template class="devsite-content-data-template">
      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]]
    </template>
  
</div>
            
          </devsite-content>
        </main>
        <devsite-footer-promos class="devsite-footer">
          
            
          
        </devsite-footer-promos>
        <devsite-footer-linkboxes class="devsite-footer">
          
            
<nav class="devsite-footer-linkboxes nocontent" aria-label="Footer links">
  
  <ul class="devsite-footer-linkboxes-list">
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Products and pricing</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/products/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-type="footer link"track-metadata-module="footer"track-metadata-eventDetail="cloud.google.com/products/"track-metadata-child_headline="products and pricing"track-name="see all products"track-metadata-position="footer">
            
          
            See all products
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/pricing/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-child_headline="products and pricing"track-metadata-eventDetail="cloud.google.com/pricing/"track-metadata-position="footer"track-name="google cloud pricing"track-metadata-module="footer"track-type="footer link">
            
          
            Google Cloud pricing
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/marketplace/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-module="footer"track-type="footer link"track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/marketplace/"track-metadata-position="footer"track-name="google cloud marketplace">
            
          
            Google Cloud Marketplace
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/contact/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-position="footer"track-name="contact sales"track-metadata-child_headline="engage"track-metadata-eventDetail="cloud.google.com/contact/"track-metadata-module="footer"track-type="footer link">
            
              
              
            
          
            Contact sales
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Support</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//discuss.google.dev/c/google-cloud/14/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-type="footer link"target="_blank"track-metadata-module="footer"rel="noopener"track-metadata-eventDetail="www.googlecloudcommunity.com"track-metadata-child_headline="engage"track-name="google cloud community"track-metadata-position="footer">
            
          
            Community forums
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/support-hub/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/support-hub/"track-metadata-position="footer"track-name="support"track-metadata-module="footer"track-type="footer link">
            
          
            Support
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//docs.cloud.google.com/release-notes"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-name="release notes"track-metadata-position="footer"track-metadata-eventDetail="cloud.google.com/release-notes/"track-metadata-child_headline="resources"track-type="footer link"track-metadata-module="footer">
            
          
            Release Notes
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//status.cloud.google.com"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-module="footer"track-type="footer link"target="_blank"track-metadata-child_headline="resources"track-metadata-eventDetail="status.cloud.google.com"track-metadata-position="footer"track-name="system status">
            
              
              
            
          
            System status
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Resources</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//github.com/googlecloudPlatform/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-type="footer link"track-metadata-module="footer"track-metadata-eventDetail="github.com/googlecloudPlatform/"track-metadata-child_headline="resources"track-name="github"track-metadata-position="footer">
            
          
            GitHub
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/get-started/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-position="footer"track-name="google cloud quickstarts"track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/docs/get-started/"track-metadata-module="footer"track-type="footer link">
            
          
            Getting Started with Google Cloud
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/docs/samples"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/docs/samples"track-metadata-position="footer"track-name="code samples"track-metadata-module="footer"track-type="footer link">
            
          
            Code samples
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="/architecture/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            track-metadata-module="footer"track-type="footer link"track-metadata-position="footer"track-name="cloud architecture center"track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/architecture/">
            
          
            Cloud Architecture Center
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/learn/training/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            track-metadata-position="footer"track-name="training"track-metadata-child_headline="resources"track-metadata-eventDetail="cloud.google.com/learn/training/"track-metadata-module="footer"track-type="footer link">
            
              
              
            
          
            Training and Certification
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
    <li class="devsite-footer-linkbox ">
    <h3 class="devsite-footer-linkbox-heading no-link">Engage</h3>
      <ul class="devsite-footer-linkbox-list">
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/blog/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 1)"
            track-metadata-child_headline="engage"track-metadata-eventDetail="cloud.google.com/blog/"track-metadata-position="footer"track-name="blog"track-metadata-module="footer"track-type="footer link">
            
          
            Blog
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//cloud.google.com/events/"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 2)"
            track-metadata-module="footer"track-type="footer link"track-metadata-position="footer"track-name="events"track-metadata-child_headline="engage"track-metadata-eventDetail="cloud.google.com/events/">
            
          
            Events
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//x.com/googlecloud"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 3)"
            track-metadata-position="footer"track-name="follow on x"track-metadata-child_headline="engage"track-metadata-eventDetail="x.com/googlecloud"rel="noopener"track-metadata-module="footer"target="_blank"track-type="footer link">
            
          
            X (Twitter)
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/googlecloud"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 4)"
            target="_blank"track-type="footer link"track-metadata-module="footer"rel="noopener"track-metadata-eventDetail="www.youtube.com/googlecloud"track-metadata-child_headline="engage"track-name="google cloud on youtube"track-metadata-position="footer">
            
          
            Google Cloud on YouTube
          
          </a>
          
          
        </li>
        
        <li class="devsite-footer-linkbox-item">
          
          <a href="//www.youtube.com/googlecloudplatform"
             class="devsite-footer-linkbox-link gc-analytics-event"
             data-category="Site-Wide Custom Events"
            
             data-label="Footer Link (index 5)"
            rel="noopener"target="_blank"track-type="footer link"track-metadata-module="footer"track-name="google cloud tech on youtube"track-metadata-position="footer"track-metadata-eventDetail="www.youtube.com/googlecloudplatform"track-metadata-child_headline="engage">
            
              
              
            
          
            Google Cloud Tech on YouTube
          
          </a>
          
          
        </li>
        
      </ul>
    </li>
    
  </ul>
  
</nav>
          
        </devsite-footer-linkboxes>
        <devsite-footer-utility class="devsite-footer">
          
            

<div class="devsite-footer-utility nocontent">
  

  
  <nav class="devsite-footer-utility-links" aria-label="Utility links">
    
    <ul class="devsite-footer-utility-list">
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//about.google/"
           data-category="Site-Wide Custom Events"
           data-label="Footer About Google link"
         
           track-metadata-eventDetail="//about.google/"
         
           track-name="about google"
         
           track-metadata-position="footer"
         
           track-type="footer link"
         
           target="_blank"
         
           track-metadata-module="utility footer"
         >
          About Google
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 devsite-footer-privacy-link">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/privacy"
           data-category="Site-Wide Custom Events"
           data-label="Footer Privacy link"
         
           track-name="privacy"
         
           track-metadata-position="footer"
         
           track-metadata-eventDetail="//policies.google.com/privacy"
         
           track-type="footer link"
         
           target="_blank"
         
           track-metadata-module="utility footer"
         >
          Privacy
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//policies.google.com/terms?hl=en"
           data-category="Site-Wide Custom Events"
           data-label="Footer Site terms link"
         
           target="_blank"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="//www.google.com/intl/en/policies/terms/regional.html"
         
           track-name="site terms"
         
           track-metadata-position="footer"
         >
          Site terms
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 ">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//cloud.google.com/product-terms"
           data-category="Site-Wide Custom Events"
           data-label="Footer Google Cloud terms link"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="//cloud.google.com/product-terms"
         
           track-name="google cloud terms"
         
           track-metadata-position="footer"
         >
          Google Cloud terms
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 glue-cookie-notification-bar-control">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="#"
           data-category="Site-Wide Custom Events"
           data-label="Footer Manage cookies link"
         
           track-name="Manage cookies"
         
           track-metadata-position="footer"
         
           track-metadata-eventDetail="#"
         
           aria-hidden="true"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         >
          Manage cookies
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 devsite-footer-carbon-button">
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//cloud.google.com/sustainability"
           data-category="Site-Wide Custom Events"
           data-label="Footer Our third decade of climate action: join us link"
         
           track-metadata-eventDetail="/sustainability/"
         
           track-name="Our third decade of climate action: join us"
         
           track-metadata-position="footer"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         >
          Our third decade of climate action: join us
        </a>
        
      </li>
      
      <li class="devsite-footer-utility-item
                 devsite-footer-utility-button">
        
        <span class="devsite-footer-utility-description">Sign up for the Google Cloud newsletter</span>
        
        
        <a class="devsite-footer-utility-link gc-analytics-event"
           href="//cloud.google.com/newsletter/"
           data-category="Site-Wide Custom Events"
           data-label="Footer Subscribe link"
         
           track-type="footer link"
         
           track-metadata-module="utility footer"
         
           track-metadata-eventDetail="/newsletter/"
         
           track-name="subscribe"
         
           track-metadata-position="footer"
         >
          Subscribe
        </a>
        
      </li>
      
    </ul>
    
    
<devsite-language-selector>
  <ul role="presentation">
    
    
    <li role="presentation">
      <a role="menuitem" lang="en"
        >English</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="de"
        >Deutsch</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="es_419"
        >Español – América Latina</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="fr"
        >Français</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="pt_br"
        >Português – Brasil</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="zh_cn"
        >中文 – 简体</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ja"
        >日本語</a>
    </li>
    
    <li role="presentation">
      <a role="menuitem" lang="ko"
        >한국어</a>
    </li>
    
  </ul>
</devsite-language-selector>

  </nav>
</div>
          
        </devsite-footer-utility>
        <devsite-panel>
          
        </devsite-panel>
        
      </section></section>
    <devsite-sitemask></devsite-sitemask>
    <devsite-snackbar></devsite-snackbar>
    <devsite-tooltip ></devsite-tooltip>
    <devsite-heading-link></devsite-heading-link>
    <devsite-analytics>
      
        <script type="application/json" analytics>[]</script>
<script type="application/json" tag-management>{&#34;at&#34;: &#34;True&#34;, &#34;ga4&#34;: [], &#34;ga4p&#34;: [], &#34;gtm&#34;: [{&#34;id&#34;: &#34;GTM-5CVQBG&#34;, &#34;purpose&#34;: 1}], &#34;parameters&#34;: {&#34;internalUser&#34;: &#34;False&#34;, &#34;language&#34;: {&#34;machineTranslated&#34;: &#34;False&#34;, &#34;requested&#34;: &#34;en&#34;, &#34;served&#34;: &#34;en&#34;}, &#34;pageType&#34;: &#34;article&#34;, &#34;projectName&#34;: &#34;Python client libraries&#34;, &#34;signedIn&#34;: &#34;False&#34;, &#34;tenant&#34;: &#34;clouddocs&#34;, &#34;recommendations&#34;: {&#34;sourcePage&#34;: &#34;&#34;, &#34;sourceType&#34;: 0, &#34;sourceRank&#34;: 0, &#34;sourceIdenticalDescriptions&#34;: 0, &#34;sourceTitleWords&#34;: 0, &#34;sourceDescriptionWords&#34;: 0, &#34;experiment&#34;: &#34;&#34;}, &#34;experiment&#34;: {&#34;ids&#34;: &#34;&#34;}}}</script>
      
    </devsite-analytics>
    
      <devsite-badger></devsite-badger>
    
    
    <cloudx-user></cloudx-user>



  <cloudx-free-trial-eligible-store freeTrialEligible="true"></cloudx-free-trial-eligible-store>

    
<script nonce="eRakXuJknpnQRUhbtP5zg9QeoFpFbp">
  
  (function(d,e,v,s,i,t,E){d['GoogleDevelopersObject']=i;
    t=e.createElement(v);t.async=1;t.src=s;E=e.getElementsByTagName(v)[0];
    E.parentNode.insertBefore(t,E);})(window, document, 'script',
    'https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/js/app_loader.js', '[39,"en",null,"/js/devsite_app_module.js","https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b","https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs","https://clouddocs-dot-devsite-v2-prod.appspot.com",1,null,["/_pwa/clouddocs/manifest.json","https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/images/video-placeholder.svg","https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/images/favicons/onecloud/favicon.ico","https://www.gstatic.com/devrel-devsite/prod/va845a6a69ec71f6762e80b2da8e8faa65e74307aa7e53d6c2485adee73edb48b/clouddocs/images/lockup.svg","https://fonts.googleapis.com/css?family=Google+Sans:400,500|Roboto:400,400italic,500,500italic,700,700italic|Roboto+Mono:400,500,700&display=swap"],1,null,[1,6,8,12,14,17,21,25,50,52,63,70,75,76,80,87,91,92,93,97,98,100,101,102,103,104,105,107,108,109,110,112,113,117,118,120,122,124,125,126,127,129,130,131,132,133,134,135,136,138,140,141,147,148,149,151,152,156,157,158,159,161,163,164,168,169,170,179,180,182,183,186,191,193,196],"AIzaSyAP-jjEJBzmIyKR4F-3XITp8yM9T1gEEI8","AIzaSyB6xiKGDR5O3Ak2okS4rLkauxGUG7XP0hg","docs.cloud.google.com","AIzaSyAQk0fBONSGUqCNznf6Krs82Ap1-NV6J4o","AIzaSyCCxcqdrZ_7QMeLCRY20bh_SXdAYqy70KY",null,null,null,["Profiles__enable_purchase_prompts","CloudShell__cloud_code_overflow_menu","DevPro__enable_g1_integration","Profiles__enable_callout_notifications","MiscFeatureFlags__emergency_css","Concierge__enable_actions_menu","MiscFeatureFlags__gdp_dashboard_reskin_enabled","MiscFeatureFlags__enable_firebase_utm","Cloud__enable_cloud_dlp_service","Cloud__cache_serialized_dynamic_content","Profiles__enable_playlist_community_acl","Cloud__enable_free_trial_server_call","DevPro__enable_google_payments_buyflow","DevPro__enable_firebase_workspaces_card","Search__enable_ai_eligibility_checks","TpcFeatures__proxy_prod_host","Profiles__enable_targeted_hero","Profiles__enable_auto_apply_credits","Profiles__enable_recognition_badges","EngEduTelemetry__enable_engedu_telemetry","Experiments__reqs_query_experiments","MiscFeatureFlags__remove_cross_domain_tracking_params","Search__enable_dynamic_content_confidential_banner","Cloud__enable_llm_concierge_chat","SignIn__enable_l1_signup_flow","Profiles__enable_developer_profile_pages_as_content","Search__enable_page_map","MiscFeatureFlags__developers_footer_dark_image","DevPro__enable_enterprise","Profiles__enable_completequiz_endpoint","Analytics__enable_devpro_interaction_logging","Cloud__fast_free_trial","Profiles__enable_awarding_url","MiscFeatureFlags__enable_framebox_badge_methods","Profiles__enable_completecodelab_endpoint","MiscFeatureFlags__enable_view_transitions","BookNav__enable_tenant_cache_key","Profiles__enable_stripe_subscription_management","Cloud__enable_legacy_calculator_redirect","DevPro__enable_nvidia_credits_card","DevPro__enable_google_one_card","Profiles__enable_dashboard_curated_recommendations","Concierge__enable_concierge_restricted","DevPro__enable_cloud_innovators_plus","DevPro__enable_developer_subscriptions","DevPro__enable_free_benefits","CloudShell__cloud_shell_button","MiscFeatureFlags__enable_explicit_template_dependencies","Profiles__enable_developer_profiles_callout","MiscFeatureFlags__enable_appearance_cookies","Profiles__enable_complete_playlist_endpoint","Cloud__enable_cloud_shell_fte_user_flow","Concierge__enable_remove_info_panel_tags","MiscFeatureFlags__enable_explain_this_code","Profiles__enable_page_saving","OnSwitch__enable","MiscFeatureFlags__enable_variable_operator_index_yaml","Profiles__require_profile_eligibility_for_signin","MiscFeatureFlags__enable_project_variables","MiscFeatureFlags__developers_footer_image","DevPro__enable_vertex_credit_card","Search__enable_suggestions_from_borg","MiscFeatureFlags__fix_lower_breadcrumbs","TpcFeatures__enable_unmirrored_page_left_nav","Analytics__enable_clearcut_logging","Profiles__enable_public_developer_profiles","Profiles__enable_developer_profile_benefits_ui_redesign","Profiles__enable_user_type","Concierge__enable_pushui","Search__enable_ai_search_summaries_for_all","Cloud__enable_cloud_shell","DevPro__enable_embed_profile_creation","Cloud__enable_cloudx_experiment_ids","Concierge__enable_tutorial_this_code","Profiles__enable_join_program_group_endpoint","MiscFeatureFlags__enable_variable_operator","DevPro__remove_eu_tax_intake_form","DevPro__enable_code_assist","Profiles__enable_profile_collections","DevPro__enable_devpro_offers"],null,null,"AIzaSyBLEMok-5suZ67qRPzx0qUtbnLmyT_kCVE","https://developerscontentserving-pa.clients6.google.com","AIzaSyCM4QpTRSqP5qI4Dvjt4OAScIN8sOUlO-k","https://developerscontentsearch-pa.clients6.google.com",1,4,1,"https://developerprofiles-pa.clients6.google.com",[39,"clouddocs","Google Cloud Documentation","docs.cloud.google.com",null,"clouddocs-dot-devsite-v2-prod.appspot.com",null,null,[1,1,null,null,null,null,null,null,null,null,null,[1],null,null,null,null,null,1,[1],[null,null,null,[1,20],"/terms/recommendations"],[1],null,[1],[1,null,1],null,[1]],null,[54,null,null,null,null,null,"/images/lockup.svg","/images/favicons/onecloud/apple-icon.png",null,null,null,1,1,1,1,null,[],null,null,[[],[],[],[],[],[],[],[]],null,1,null,null,null,"/images/lockup-dark-theme.svg",[]],[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[6,1,14,15,22,23,29,37],null,[[null,null,null,null,null,null,[1,[["docType","Choose a content type",[["ApiReference",null,null,null,null,null,null,null,null,"API reference"],["Sample",null,null,null,null,null,null,null,null,"Code sample"],["ReferenceArchitecture",null,null,null,null,null,null,null,null,"Reference architecture"],["Tutorial",null,null,null,null,null,null,null,null,"Tutorial"]]],["category","Choose a topic",[["AiAndMachineLearning",null,null,null,null,null,null,null,null,"Artificial intelligence and machine learning (AI/ML)"],["ApplicationDevelopment",null,null,null,null,null,null,null,null,"Application development"],["BigDataAndAnalytics",null,null,null,null,null,null,null,null,"Big data and analytics"],["Compute",null,null,null,null,null,null,null,null,"Compute"],["Containers",null,null,null,null,null,null,null,null,"Containers"],["Databases",null,null,null,null,null,null,null,null,"Databases"],["HybridCloud",null,null,null,null,null,null,null,null,"Hybrid and multicloud"],["LoggingAndMonitoring",null,null,null,null,null,null,null,null,"Logging and monitoring"],["Migrations",null,null,null,null,null,null,null,null,"Migrations"],["Networking",null,null,null,null,null,null,null,null,"Networking"],["SecurityAndCompliance",null,null,null,null,null,null,null,null,"Security and compliance"],["Serverless",null,null,null,null,null,null,null,null,"Serverless"],["Storage",null,null,null,null,null,null,null,null,"Storage"]]]]]],[1],null,1],[[null,null,null,null,null,["GTM-5CVQBG"],null,null,null,null,null,[["GTM-5CVQBG",2]],1],null,null,null,null,null,1],"mwETRvWii0eU5NUYprb0Y9z5GVbc",4],null,"pk_live_5170syrHvgGVmSx9sBrnWtA5luvk9BwnVcvIi7HizpwauFG96WedXsuXh790rtij9AmGllqPtMLfhe2RSwD6Pn38V00uBCydV4m",1,null,"https://developerscontentinsights-pa.clients6.google.com","AIzaSyCg-ZUslalsEbXMfIo9ZP8qufZgo3LSBDU","AIzaSyDxT0vkxnY_KeINtA4LSePJO-4MAZPMRsE","https://developers.clients6.google.com",null,null,"AIzaSyBQom12tzI-rybN7Sf-KfeL4nwm-Rf7PmI\n",null,null,"https://developers.googleapis.com"]')
  
</script>

    <devsite-a11y-announce></devsite-a11y-announce>
  </body>
</html>