# Imgly React Native Documentation

Source: https://img.ly/docs/pesdk/react-native/llms-full.txt

---

<!DOCTYPE html><!-- Last Published: Mon Dec 29 2025 10:04:46 GMT+0000 (Coordinated Universal Time) --><html data-wf-domain="www2.img.ly" data-wf-page="5ff596e2ff1e2c660a273609" data-wf-site="5ff596e2ff1e2cb058273601" lang="en"><head><meta charset="utf-8"/><title>IMG.LY: Page Not Found - 404</title><meta content="IMG.LY: Page Not Found - 404" property="og:title"/><meta content="https://cdn.prod.website-files.com/5ff596e2ff1e2cb058273601/603cd542e1c145588bd9d7f9_opengraph.png" property="og:image"/><meta content="IMG.LY: Page Not Found - 404" property="twitter:title"/><meta content="https://cdn.prod.website-files.com/5ff596e2ff1e2cb058273601/603cd542e1c145588bd9d7f9_opengraph.png" property="twitter:image"/><meta content="width=device-width, initial-scale=1" name="viewport"/><link href="https://cdn.prod.website-files.com/5ff596e2ff1e2cb058273601/css/pesdk-xyz.webflow.shared.d26723015.min.css" rel="stylesheet" type="text/css"/><link href="https://fonts.googleapis.com" rel="preconnect"/><link href="https://fonts.gstatic.com" rel="preconnect" crossorigin="anonymous"/><script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script><script type="text/javascript">WebFont.load({  google: {    families: ["Lato:100,100italic,300,300italic,400,400italic,700,700italic,900,900italic"]  }});</script><script type="text/javascript">!function(o,c){var n=c.documentElement,t=" w-mod-";n.className+=t+"js",("ontouchstart"in o||o.DocumentTouch&&c instanceof DocumentTouch)&&(n.className+=t+"touch")}(window,document);</script><link href="https://cdn.prod.website-files.com/5ff596e2ff1e2cb058273601/60266208f66b13176543c178_favicon.png" rel="shortcut icon" type="image/x-icon"/><link href="https://cdn.prod.website-files.com/5ff596e2ff1e2cb058273601/6026620bdcd77b00c33e7d05_webclip.png" rel="apple-touch-icon"/><link href="https://img.ly/404" rel="canonical"/><script defer data-domain="img.ly" src="https://plausible.io/js/script.js"></script>
<script>window.plausible = window.plausible || function() { (window.plausible.q = window.plausible.q || []).push(arguments) }</script>

<link rel="sitemap" type="application/xml" href="https://img.ly/sitemap.xml" />

<style type="text/css">
  html, body {
    overflow-x: hidden; 
  }
  
  @supports (overflow:clip) {
    html, body {
     overflow-x: clip;
    }
  }
  
  .cta-parallax-container {
  	pointer-events:none;
  }
  
  .tooltip {
    pointer-events: none;
  }
  a:focus {
    outline: none;
  }
  .footer-links {
    word-wrap: break-word;
  }

  .hljs {
    background: transparent !important;
  }

  /**
   * Theming for:
   * - Accent Theme
   * - Dark Theme
   */
  .navbarv2 {
    color: #161617 !important;
  }

  /* NavbarV2 Logo (Default State) */
  body.accent-theme .navbarv2 .navbarv2_logo,
  body.dark-theme .navbarv2 .navbarv2_logo {
    color: #fff !important;
  }

  
  /* NavbarV2 Hamburger Menu (Default State) */
  body.accent-theme .navbarv2 .is--hamburger,
  body.dark-theme .navbarv2 .is--hamburger {
    color: #fff !important;
  }

  /* NavbarV2 Join Us Button (Default State) */
  body.accent-theme .navbarv2 .navbarv2_metalink,
  body.dark-theme .navbarv2 .navbarv2_metalink {
    color: rgba(0, 255, 183, 1) !important;
  }

  /* Navbar (old) */
  body.white-theme .navbar .menu-button .menu-icon {
    color: #161617 !important;
  }

  @media only screen and (min-width: 991px) {
    /* NavbarV2 Regular Buttons (Default State) */
    body.accent-theme .navbarv2 .is--navbar,
    body.dark-theme .navbarv2 .is--navbar {
      color: #fff !important;
    }
    /* NavbarV2 Regular Buttons (Hover State) */
    body.accent-theme .navbarv2 .is--navbar:hover,
    body.dark-theme .navbarv2 .is--navbar:hover {
      color: #fff !important;
      background-color: rgba(255, 255, 255, 0.25) !important;
    }

    /* NavbarV2 CTA Primary Button (Default State) */
    body.accent-theme .navbarv2 .is--navbar.is--theme-accent,
    body.dark-theme .navbarv2 .is--navbar.is--theme-accent {
      color: #161617 !important;
      border-color: #00ffb7 !important;
      background-color: #00ffb7 !important;
    }
    /* NavbarV2 CTA Primary Buttons (Hover State) */
    body.accent-theme .navbarv2 .is--navbar.is--theme-accent:hover,
    body.dark-theme .navbarv2 .is--navbar.is--theme-accent:hover {
      color: #161617 !important;
      border-color: #00ffb7 !important;
      background-color: rgba(128, 255, 219, 0.65) !important;
    }

    /* NavbarV2 CTA Secondary Button (Default State) */
    body.accent-theme .navbarv2 .is--navbar.is--theme-accent2,
    body.dark-theme .navbarv2 .is--navbar.is--theme-accent2 {
      color: #fff !important;
      border-color: rgba(255, 255, 255, 0.3) !important;
    }
    /* NavbarV2 CTA Secondary Button (Hover State) */
    body.accent-theme .navbarv2 .is--navbar.is--theme-accent2:hover,
    body.dark-theme .navbarv2 .is--navbar.is--theme-accent2:hover {
      color: #fff !important;
      border-color: rgba(255, 255, 255, 0.3) !important;
      background-color: rgba(255, 255, 255, 0.25) !important;
    }

    /* Navbar (old) */
    body.dark-theme .navbar .accent,
    body.white-theme .navbar .accent {
      background-color: #471aff !important;
      box-shadow: 0 4px 10px 1px rgb(47 18 165 / 25%) !important;
      color: #fff;
      border: none;
    }

    body.dark-theme .navbar .accent:hover,
    body.white-theme .navbar .accent:hover {
      background-color: rgba(71, 26, 255, 0.65) !important;
      border: none;
    }

    body.white-theme .navbar .nav-item,
    body.white-theme .navbar .menu-button {
      color: #161617 !important;
    }

    body.white-theme .navbar .nav-item:hover {
      background-color: rgba(0, 0, 0, 0.12) !important;
      color: #161617 !important;
    }

    body.white-theme .navbar .nav-item:focus {
      border-color: rgba(0, 0, 0, 0.24) !important;
    }

    .navbarv2 .w-dropdown-list,
    .nav-dropdown-list {
      visibility: hidden;
    }
    .navbarv2 .w-dropdown-list.w--open,
    .nav-dropdown-list.w--open {
      visibility: visible;
    }
    .use-case-button.active .cc-circle {
      background-color: #2b55ff;
    }
  }


</style>

<style type="text/css">

body.accent-theme .IMGLY__header_logo,
body.dark-theme .IMGLY__header_logo {
  color: #fff !important;
}

body.accent-theme .IMGLY__header_hamburger,
body.dark-theme .IMGLY__header_hamburger {
  color: #fff !important;
}

body.accent-theme .IMGLY__Header_Item,
body.dark-theme .IMGLY__Header_Item {
  color: #fff !important;
}

body.accent-theme .IMGLY__Header_Item:hover,
body.dark-theme .IMGLY__Header_Item:hover {
  color: #fff !important;
  background-color: rgba(255, 255, 255, 0.25) !important;
}

body.accent-theme .IMGLY__Header_Careers,
body.dark-theme .IMGLY__Header_Careers {
  color: rgba(0, 255, 183, 1) !important;
}
  
/* added temporary styling until cross-platform banner is removed */
@media (max-width: 479px) {
  .navbarv2 {
    margin-top: 1rem !important;
  }
  
  .IMGLY__Header_Careers {
    display: none !important;
  }
}  
</style>

<script type="module" src="https://img.ly/static/imgly-website-components/script.js"></script>

<link
  rel="preload"
  href="https://img.ly/static/imgly-website-components/imgly-website-components.css"
  as="style"
  onload="this.onload=null;this.rel='stylesheet'"
/>
<noscript>
  <link
    rel="stylesheet"
    href="https://img.ly/static/imgly-website-components/imgly-website-components.css"
  />
</noscript>

<script>
  'function' != typeof Object.assign &&
    (Object.assign = function (n) {
      'use strict'
      if (null == n)
        throw new TypeError('Cannot convert undefined or null to object')
      n = Object(n)
      for (var t = 1; t < arguments.length; t++) {
        var r = arguments[t]
        if (null != r)
          for (var e in r)
            Object.prototype.hasOwnProperty.call(r, e) && (n[e] = r[e])
      }
      return n
    })
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "IMG.LY",
  "url": "https://img.ly/",
  "logo": "https://cdn.prod.website-files.com/5ff596e2ff1e2cb058273601/62988e6e8c1a8b2f49b11e07_IMG.LY%20LOGO%20Dark%20Accent.svg",

  "sameAs": [
    "https://twitter.com/imgly",
    "https://www.instagram.com/img.ly/",
    "https://www.youtube.com/@imgly",
    "https://www.linkedin.com/company/img.ly",
    "https://github.com/imgly"
  ]
}
</script>
<script src="https://app.optibase.io/script.js" type="text/javascript" crossorigin="anonymous" data-public-api-key="b2fbb714-c2ca-4486-b4f3-122ba8f3af3b"></script><script src="https://cdn.prod.website-files.com/5ff596e2ff1e2cb058273601%2F652d31f3dc22d7b4ee708e44%2F6904b3b136ea6108bd775f19%2Fclarity_script-7.4.1.js" type="text/javascript"></script><script src="https://app.optibase.io/script.js" type="text/javascript" integrity="sha384-mUZZ11h5hB3RAZ9fOKTEfF4GV/qSPvHtTSy6ZuebXDj7T7s4s3noqQHtabhjLKfP" crossorigin="anonymous" data-public-api-key="b2fbb714-c2ca-4486-b4f3-122ba8f3af3b"></script></head><body class="white-theme small-page"><div id="navbar-top" data-animation="default" data-collapse="medium" data-duration="400" data-easing="ease" data-easing2="ease" role="banner" class="navbar-root w-nav"><div class="navbarv2"><header id="imgly-website-components-header" data-hiring="false" class="navbarv2_container"></header></div></div><div class="section-old small"><h1>404 Not Found</h1><p>Sorry, but the page you were looking for could not be found. You can return to our <a href="/">home page</a>, or <a href="/company/contact-us">contact us</a> if you can&#x27;t find what you&#x27;re looking for.</p></div><footer id="imgly-website-components-footer"></footer><script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=5ff596e2ff1e2cb058273601" type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script><script src="https://cdn.prod.website-files.com/5ff596e2ff1e2cb058273601/js/webflow.schunk.59c6248219f37ae8.js" type="text/javascript"></script><script src="https://cdn.prod.website-files.com/5ff596e2ff1e2cb058273601/js/webflow.schunk.022b75323d9f20dc.js" type="text/javascript"></script><script src="https://cdn.prod.website-files.com/5ff596e2ff1e2cb058273601/js/webflow.6d92e262.5c6f84d4e5a043d9.js" type="text/javascript"></script><div id="imgly-website-components-cookies"></div>

<script type="text/javascript"
      src="https://onsite.optimonk.com/script.js?account=261668"
      async></script>

<script>
	window.onload = function () {
    document.addEventListener('DOMContentLoaded', function () { plausible('404', { props: { path: document.location.pathname } }); });
    }
</script></body></html>