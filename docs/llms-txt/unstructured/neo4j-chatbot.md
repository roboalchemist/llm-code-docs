# Source: https://docs.unstructured.io/examplecode/tools/neo4j-chatbot.md

<!doctype html>
<!--[if IE 9]>
<html class="no-js ie9" lang="en"> <![endif]-->
<html class="no-js" lang="en">

<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="msvalidate.01" content="B5163518CBE4A854B63801277FE5E35C" />
  <meta name="google-site-verification" content="ucqagxjVuq0lJZeLKs0F5AppzK111lNt3IoxU6mzlJE" />
  <meta name="facebook-domain-verification" content="hli4d7mfso56r97lmed0ee7v88bzw8" />

  <script>window.dataLayer = window.dataLayer || [];</script>
<script>
    (function(){
        function loadGTM() {
            // GTM Snippet
            (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-WK23PSS');
        }
        // Load later to avoid affecting TBT
        if ('requestIdleCallback' in window) {
            requestIdleCallback(loadGTM);
        } else {
            setTimeout(loadGTM, 200);
        }
    })();
</script>
  <!-- Start VWO Async SmartCode -->
<link rel="preconnect" href="https://dev.visualwebsiteoptimizer.com" />
<script type='text/javascript' id='vwoCode'>
	window._vwo_code ||
	(function () {
		var w=window,
			d=document;
		var account_id=571133,
			version=2.2,
			settings_tolerance=2000,
			hide_element='body',
			hide_element_style = 'opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important';
		/* DO NOT EDIT BELOW THIS LINE */
		if(f=!1,v=d.querySelector('#vwoCode'),cc={},-1<d.URL.indexOf('__vwo_disable__')||w._vwo_code)return;try{var e=JSON.parse(localStorage.getItem('_vwo_'+account_id+'_config'));cc=e&&'object'==typeof e?e:{}}catch(e){}function r(t){try{return decodeURIComponent(t)}catch(e){return t}}var s=function(){var e={combination:[],combinationChoose:[],split:[],exclude:[],uuid:null,consent:null,optOut:null},t=d.cookie||'';if(!t)return e;for(var n,i,o=/(?:^|;\s*)(?:(_vis_opt_exp_(\d+)_combi=([^;]*))|(_vis_opt_exp_(\d+)_combi_choose=([^;]*))|(_vis_opt_exp_(\d+)_split=([^:;]*))|(_vis_opt_exp_(\d+)_exclude=[^;]*)|(_vis_opt_out=([^;]*))|(_vwo_global_opt_out=[^;]*)|(_vwo_uuid=([^;]*))|(_vwo_consent=([^;]*)))/g;null!==(n=o.exec(t));)try{n[1]?e.combination.push({id:n[2],value:r(n[3])}):n[4]?e.combinationChoose.push({id:n[5],value:r(n[6])}):n[7]?e.split.push({id:n[8],value:r(n[9])}):n[10]?e.exclude.push({id:n[11]}):n[12]?e.optOut=r(n[13]):n[14]?e.optOut=!0:n[15]?e.uuid=r(n[16]):n[17]&&(i=r(n[18]),e.consent=i&&3<=i.length?i.substring(0,3):null)}catch(e){}return e}();function i(){var e=function(){if(w.VWO&&Array.isArray(w.VWO))for(var e=0;e<w.VWO.length;e++){var t=w.VWO[e];if(Array.isArray(t)&&('setVisitorId'===t[0]||'setSessionId'===t[0]))return!0}return!1}(),t='a='+account_id+'&u='+encodeURIComponent(w._vis_opt_url||d.URL)+'&vn='+version+'&ph=1'+('undefined'!=typeof platform?'&p='+platform:'')+'&st='+w.performance.now();e||((n=function(){var e,t=[],n={},i=w.VWO&&w.VWO.appliedCampaigns||{};for(e in i){var o=i[e]&&i[e].v;o&&(t.push(e+'-'+o+'-1'),n[e]=!0)}if(s&&s.combination)for(var r=0;r<s.combination.length;r++){var a=s.combination[r];n[a.id]||t.push(a.id+'-'+a.value)}return t.join('|')}())&&(t+='&c='+n),(n=function(){var e=[],t={};if(s&&s.combinationChoose)for(var n=0;n<s.combinationChoose.length;n++){var i=s.combinationChoose[n];e.push(i.id+'-'+i.value),t[i.id]=!0}if(s&&s.split)for(var o=0;o<s.split.length;o++)t[(i=s.split[o]).id]||e.push(i.id+'-'+i.value);return e.join('|')}())&&(t+='&cc='+n),(n=function(){var e={},t=[];if(w.VWO&&Array.isArray(w.VWO))for(var n=0;n<w.VWO.length;n++){var i=w.VWO[n];if(Array.isArray(i)&&'setVariation'===i[0]&&i[1]&&Array.isArray(i[1]))for(var o=0;o<i[1].length;o++){var r,a=i[1][o];a&&'object'==typeof a&&(r=a.e,a=a.v,r&&a&&(e[r]=a))}}for(r in e)t.push(r+'-'+e[r]);return t.join('|')}())&&(t+='&sv='+n)),s&&s.optOut&&(t+='&o='+s.optOut);var n=function(){var e=[],t={};if(s&&s.exclude)for(var n=0;n<s.exclude.length;n++){var i=s.exclude[n];t[i.id]||(e.push(i.id),t[i.id]=!0)}return e.join('|')}();return n&&(t+='&e='+n),s&&s.uuid&&(t+='&id='+s.uuid),s&&s.consent&&(t+='&consent='+s.consent),w.name&&-1<w.name.indexOf('_vis_preview')&&(t+='&pM=true'),w.VWO&&w.VWO.ed&&(t+='&ed='+w.VWO.ed),t}code={nonce:v&&v.nonce,library_tolerance:function(){return'undefined'!=typeof library_tolerance?library_tolerance:void 0},settings_tolerance:function(){return cc.sT||settings_tolerance},hide_element_style:function(){return'{'+(cc.hES||hide_element_style)+'}'},hide_element:function(){return performance.getEntriesByName('first-contentful-paint')[0]?'':'string'==typeof cc.hE?cc.hE:hide_element},getVersion:function(){return version},finish:function(e){var t;f||(f=!0,(t=d.getElementById('_vis_opt_path_hides'))&&t.parentNode.removeChild(t),e&&((new Image).src='https://dev.visualwebsiteoptimizer.com/ee.gif?a='+account_id+e))},finished:function(){return f},addScript:function(e){var t=d.createElement('script');t.type='text/javascript',e.src?t.src=e.src:t.text=e.text,v&&t.setAttribute('nonce',v.nonce),d.getElementsByTagName('head')[0].appendChild(t)},load:function(e,t){t=t||{};var n=new XMLHttpRequest;n.open('GET',e,!0),n.withCredentials=!t.dSC,n.responseType=t.responseType||'text',n.onload=function(){if(t.onloadCb)return t.onloadCb(n,e);200===n.status?_vwo_code.addScript({text:n.responseText}):_vwo_code.finish('&e=loading_failure:'+e)},n.onerror=function(){if(t.onerrorCb)return t.onerrorCb(e);_vwo_code.finish('&e=loading_failure:'+e)},n.send()},init:function(){var e,t=this.settings_tolerance();w._vwo_settings_timer=setTimeout(function(){_vwo_code.finish()},t),'body'!==this.hide_element()?(n=d.createElement('style'),e=(t=this.hide_element())?t+this.hide_element_style():'',t=d.getElementsByTagName('head')[0],n.setAttribute('id','_vis_opt_path_hides'),v&&n.setAttribute('nonce',v.nonce),n.setAttribute('type','text/css'),n.styleSheet?n.styleSheet.cssText=e:n.appendChild(d.createTextNode(e)),t.appendChild(n)):(n=d.getElementsByTagName('head')[0],(e=d.createElement('div')).style.cssText='z-index: 2147483647 !important;position: fixed !important;left: 0 !important;top: 0 !important;width: 100% !important;height: 100% !important;background: white !important;',e.setAttribute('id','_vis_opt_path_hides'),e.classList.add('_vis_hide_layer'),n.parentNode.insertBefore(e,n.nextSibling));var n='https://dev.visualwebsiteoptimizer.com/j.php?'+i();-1!==w.location.search.indexOf('_vwo_xhr')?this.addScript({src:n}):this.load(n+'&x=true',{l:1})}};w._vwo_code=code;code.init();})();
</script>
<!-- End VWO Async SmartCode -->
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=bOXynyJWa61">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png?v=bOXynyJWa61">
  <link rel="icon" type="image/png" sizes="194x194" href="/favicon-194x194.png?v=bOXynyJWa61">
  <link rel="icon" type="image/png" sizes="192x192" href="/android-chrome-192x192.png?v=bOXynyJWa61">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png?v=bOXynyJWa61">
  <link rel="manifest" href="/site.webmanifest?v=bOXynyJWa61">
  <link rel="mask-icon" href="/safari-pinned-tab.svg?v=bOXynyJWa6a" color="#018bff">
  <link rel="shortcut icon" href="/favicon.ico?v=bOXynyJWa61">
  <meta name="msapplication-TileColor" content="#018bff">
  <meta name="theme-color" content="#0069c1">
    <title>Build a GenAI Chatbot From Technical Docs Using Neo4j &amp; Unstructured.io</title>
  
  <!-- preload custom font files -->
  <link rel="preload" href="/wp-content/themes/neo4jweb/assets/fonts/syne-neo/SyneNeo-Medium.woff2" as="font" type="font/woff2" crossorigin>

  <!-- connect to domain of font files -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin>
  <!-- async CSS -->
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;600;700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Fira+Code&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">

  <!-- no-JS fallback -->
  <noscript>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;600;700&display=swap">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fira+Code&display=swap">
  </noscript>

  <meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

	<!-- This site is optimized with the Yoast SEO Premium plugin v26.8 (Yoast SEO v26.8) - https://yoast.com/product/yoast-seo-premium-wordpress/ -->
	<meta name="description" content="Build a GraphRAG chatbot using energy docs, Unstructured.io for chunking, and Neo4j to create a context-rich knowledge graph." />
	<link rel="canonical" href="https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="How to Build a GenAI Chatbot From Technical Documents Using Neo4j and Unstructured.io - Graph Database &amp; Analytics" />
	<meta property="og:description" content="Build a GraphRAG chatbot using energy docs, Unstructured.io for chunking, and Neo4j to create a context-rich knowledge graph." />
	<meta property="og:url" content="https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/" />
	<meta property="og:site_name" content="Graph Database &amp; Analytics" />
	<meta property="article:publisher" content="https://www.facebook.com/neo4j.graph.database" />
	<meta property="article:published_time" content="2025-07-30T15:45:05+00:00" />
	<meta property="article:modified_time" content="2025-08-07T18:50:27+00:00" />
	<meta property="og:image" content="https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io.png" />
	<meta property="og:image:width" content="1200" />
	<meta property="og:image:height" content="627" />
	<meta property="og:image:type" content="image/png" />
	<meta name="author" content="Enzo" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:creator" content="@neo4j" />
	<meta name="twitter:site" content="@neo4j" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"Article","@id":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/#article","isPartOf":{"@id":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/"},"author":{"name":"Enzo","@id":"https://neo4j.com/#/schema/person/d14f62a25cb4f78275e6d8fd28d54566"},"headline":"How to Build a GenAI Chatbot From Technical Documents Using Neo4j and Unstructured.io","datePublished":"2025-07-30T15:45:05+00:00","dateModified":"2025-08-07T18:50:27+00:00","mainEntityOfPage":{"@id":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/"},"wordCount":2222,"publisher":{"@id":"https://neo4j.com/#organization"},"image":{"@id":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/#primaryimage"},"thumbnailUrl":"https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io.png","articleSection":["GenAI"],"inLanguage":"en-US"},{"@type":"WebPage","@id":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/","url":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/","name":"Build a GenAI Chatbot From Technical Docs Using Neo4j & Unstructured.io","isPartOf":{"@id":"https://neo4j.com/#website"},"primaryImageOfPage":{"@id":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/#primaryimage"},"image":{"@id":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/#primaryimage"},"thumbnailUrl":"https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io.png","datePublished":"2025-07-30T15:45:05+00:00","dateModified":"2025-08-07T18:50:27+00:00","description":"Build a GraphRAG chatbot using energy docs, Unstructured.io for chunking, and Neo4j to create a context-rich knowledge graph.","breadcrumb":{"@id":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/"]}]},{"@type":"ImageObject","inLanguage":"en-US","@id":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/#primaryimage","url":"https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io.png","contentUrl":"https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io.png","width":1200,"height":627},{"@type":"BreadcrumbList","@id":"https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"The Neo4j Blog","item":"https://neo4j.com/blog/"},{"@type":"ListItem","position":2,"name":"How to Build a GenAI Chatbot From Technical Documents Using Neo4j and Unstructured.io"}]},{"@type":"WebSite","@id":"https://neo4j.com/#website","url":"https://neo4j.com/","name":"Graph Database &amp; Analytics","description":"The Leader in Graph Databases","publisher":{"@id":"https://neo4j.com/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://neo4j.com/?s={search_term_string}"},"query-input":{"@type":"PropertyValueSpecification","valueRequired":true,"valueName":"search_term_string"}}],"inLanguage":"en-US"},{"@type":"Organization","@id":"https://neo4j.com/#organization","name":"Neo4j","url":"https://neo4j.com/","logo":{"@type":"ImageObject","inLanguage":"en-US","@id":"https://neo4j.com/#/schema/logo/image/","url":"https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg","contentUrl":"https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg","width":677,"height":242,"caption":"Neo4j"},"image":{"@id":"https://neo4j.com/#/schema/logo/image/"},"sameAs":["https://www.facebook.com/neo4j.graph.database","https://x.com/neo4j","https://instagram.com/neo4j","https://www.linkedin.com/company/neo4j","https://www.pinterest.com/neo4j/","https://www.youtube.com/neo4j"]},{"@type":"Person","@id":"https://neo4j.com/#/schema/person/d14f62a25cb4f78275e6d8fd28d54566","name":"Enzo","image":{"@type":"ImageObject","inLanguage":"en-US","@id":"https://neo4j.com/#/schema/person/image/","url":"https://secure.gravatar.com/avatar/914196cddc1a1db55aaac98f7ace2cb93b07197ce5f03a86577be1816351f559?s=96&r=g","contentUrl":"https://secure.gravatar.com/avatar/914196cddc1a1db55aaac98f7ace2cb93b07197ce5f03a86577be1816351f559?s=96&r=g","caption":"Enzo"}}]}</script>
	<!-- / Yoast SEO Premium plugin. -->


<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://neo4j.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fneo4j.com%2Fblog%2Fgenai%2Fgraphrag-chatbot-unstructured-io%2F" />
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://neo4j.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fneo4j.com%2Fblog%2Fgenai%2Fgraphrag-chatbot-unstructured-io%2F&#038;format=xml" />
<style id='wp-img-auto-sizes-contain-inline-css' type='text/css'>
img:is([sizes=auto i],[sizes^="auto," i]){contain-intrinsic-size:3000px 1500px}
/*# sourceURL=wp-img-auto-sizes-contain-inline-css */
</style>
<style id='wp-emoji-styles-inline-css' type='text/css'>

	img.wp-smiley, img.emoji {
		display: inline !important;
		border: none !important;
		box-shadow: none !important;
		height: 1em !important;
		width: 1em !important;
		margin: 0 0.07em !important;
		vertical-align: -0.1em !important;
		background: none !important;
		padding: 0 !important;
	}
/*# sourceURL=wp-emoji-styles-inline-css */
</style>
<link rel='stylesheet' id='foundation-css' href='https://neo4j.com/wp-content/themes/neo4jweb/assets/css/app.css?ver=1770082050' type='text/css' media='all' />
<link rel='stylesheet' id='search-preact-css' href='https://neo4j.com/wp-content/themes/neo4jweb/assets/neo4j-react-modules-assets/search-preact/bundle.d3a831c0.css?ver=6.9' type='text/css' media='print' onload="this.media='all'" />
<link rel='stylesheet' id='site-animations-css' href='https://neo4j.com/wp-content/themes/neo4jweb/assets/css/site-animations.css?ver=1770082044' type='text/css' media='print' onload="this.media='all'" />
	<link rel='preload' as='style' onload="this.onload=null;this.rel='stylesheet'" id='neo4j-block-styles' href='https://neo4j.com/wp-content/themes/neo4jweb/assets/css/blocks/block-styles.css?ver=1770082038' type='text/css' media='all' /><style id='block-visibility-screen-size-styles-inline-css' type='text/css'>
/* Large screens (desktops, 992px and up) */
@media ( min-width: 992px ) {
	.block-visibility-hide-large-screen {
		display: none !important;
	}
}

/* Medium screens (tablets, between 768px and 992px) */
@media ( min-width: 768px ) and ( max-width: 991.98px ) {
	.block-visibility-hide-medium-screen {
		display: none !important;
	}
}

/* Small screens (mobile devices, less than 768px) */
@media ( max-width: 767.98px ) {
	.block-visibility-hide-small-screen {
		display: none !important;
	}
}
/*# sourceURL=block-visibility-screen-size-styles-inline-css */
</style>
<script type="text/javascript" src="https://neo4j.com/wp-content/themes/neo4jweb/assets/js/vendor/jquery-3.6.1.min.js?ver=3.6.1" id="jquery-js"></script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://neo4j.com/xmlrpc.php?rsd" />
<link rel='shortlink' href='https://neo4j.com/?p=385564' />
<!-- Stream WordPress user activity plugin v4.1.1 -->
<meta name="tec-api-version" content="v1"><meta name="tec-api-origin" content="https://neo4j.com"><link rel="alternate" href="https://neo4j.com/wp-json/tribe/events/v1/" /><style class='wp-fonts-local' type='text/css'>
@font-face{font-family:syne-neo;font-style:normal;font-weight:400;font-display:fallback;src:url('https://neo4j.com/wp-content/themes/neo4jweb/assets/fonts/syne-neo/SyneNeo-Medium.woff2') format('woff2'), url('https://neo4j.com/wp-content/themes/neo4jweb/assets/fonts/syne-neo/SyneNeo-Medium.woff') format('woff');font-stretch:normal;}
</style>
  
<style id='wp-block-heading-inline-css' type='text/css'>
h1:where(.wp-block-heading).has-background,h2:where(.wp-block-heading).has-background,h3:where(.wp-block-heading).has-background,h4:where(.wp-block-heading).has-background,h5:where(.wp-block-heading).has-background,h6:where(.wp-block-heading).has-background{padding:1.25em 2.375em}h1.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h1.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h2.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h2.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h3.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h3.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h4.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h4.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h5.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h5.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]),h6.has-text-align-left[style*=writing-mode]:where([style*=vertical-lr]),h6.has-text-align-right[style*=writing-mode]:where([style*=vertical-rl]){rotate:180deg}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/heading/style.min.css */
</style>
<style id='wp-block-image-inline-css' type='text/css'>
.wp-block-image>a,.wp-block-image>figure>a{display:inline-block}.wp-block-image img{box-sizing:border-box;height:auto;max-width:100%;vertical-align:bottom}@media not (prefers-reduced-motion){.wp-block-image img.hide{visibility:hidden}.wp-block-image img.show{animation:show-content-image .4s}}.wp-block-image[style*=border-radius] img,.wp-block-image[style*=border-radius]>a{border-radius:inherit}.wp-block-image.has-custom-border img{box-sizing:border-box}.wp-block-image.aligncenter{text-align:center}.wp-block-image.alignfull>a,.wp-block-image.alignwide>a{width:100%}.wp-block-image.alignfull img,.wp-block-image.alignwide img{height:auto;width:100%}.wp-block-image .aligncenter,.wp-block-image .alignleft,.wp-block-image .alignright,.wp-block-image.aligncenter,.wp-block-image.alignleft,.wp-block-image.alignright{display:table}.wp-block-image .aligncenter>figcaption,.wp-block-image .alignleft>figcaption,.wp-block-image .alignright>figcaption,.wp-block-image.aligncenter>figcaption,.wp-block-image.alignleft>figcaption,.wp-block-image.alignright>figcaption{caption-side:bottom;display:table-caption}.wp-block-image .alignleft{float:left;margin:.5em 1em .5em 0}.wp-block-image .alignright{float:right;margin:.5em 0 .5em 1em}.wp-block-image .aligncenter{margin-left:auto;margin-right:auto}.wp-block-image :where(figcaption){margin-bottom:1em;margin-top:.5em}.wp-block-image.is-style-circle-mask img{border-radius:9999px}@supports ((-webkit-mask-image:none) or (mask-image:none)) or (-webkit-mask-image:none){.wp-block-image.is-style-circle-mask img{border-radius:0;-webkit-mask-image:url('data:image/svg+xml;utf8,<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="50"/></svg>');mask-image:url('data:image/svg+xml;utf8,<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="50"/></svg>');mask-mode:alpha;-webkit-mask-position:center;mask-position:center;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;-webkit-mask-size:contain;mask-size:contain}}:root :where(.wp-block-image.is-style-rounded img,.wp-block-image .is-style-rounded img){border-radius:9999px}.wp-block-image figure{margin:0}.wp-lightbox-container{display:flex;flex-direction:column;position:relative}.wp-lightbox-container img{cursor:zoom-in}.wp-lightbox-container img:hover+button{opacity:1}.wp-lightbox-container button{align-items:center;backdrop-filter:blur(16px) saturate(180%);background-color:#5a5a5a40;border:none;border-radius:4px;cursor:zoom-in;display:flex;height:20px;justify-content:center;opacity:0;padding:0;position:absolute;right:16px;text-align:center;top:16px;width:20px;z-index:100}@media not (prefers-reduced-motion){.wp-lightbox-container button{transition:opacity .2s ease}}.wp-lightbox-container button:focus-visible{outline:3px auto #5a5a5a40;outline:3px auto -webkit-focus-ring-color;outline-offset:3px}.wp-lightbox-container button:hover{cursor:pointer;opacity:1}.wp-lightbox-container button:focus{opacity:1}.wp-lightbox-container button:focus,.wp-lightbox-container button:hover,.wp-lightbox-container button:not(:hover):not(:active):not(.has-background){background-color:#5a5a5a40;border:none}.wp-lightbox-overlay{box-sizing:border-box;cursor:zoom-out;height:100vh;left:0;overflow:hidden;position:fixed;top:0;visibility:hidden;width:100%;z-index:100000}.wp-lightbox-overlay .close-button{align-items:center;cursor:pointer;display:flex;justify-content:center;min-height:40px;min-width:40px;padding:0;position:absolute;right:calc(env(safe-area-inset-right) + 16px);top:calc(env(safe-area-inset-top) + 16px);z-index:5000000}.wp-lightbox-overlay .close-button:focus,.wp-lightbox-overlay .close-button:hover,.wp-lightbox-overlay .close-button:not(:hover):not(:active):not(.has-background){background:none;border:none}.wp-lightbox-overlay .lightbox-image-container{height:var(--wp--lightbox-container-height);left:50%;overflow:hidden;position:absolute;top:50%;transform:translate(-50%,-50%);transform-origin:top left;width:var(--wp--lightbox-container-width);z-index:9999999999}.wp-lightbox-overlay .wp-block-image{align-items:center;box-sizing:border-box;display:flex;height:100%;justify-content:center;margin:0;position:relative;transform-origin:0 0;width:100%;z-index:3000000}.wp-lightbox-overlay .wp-block-image img{height:var(--wp--lightbox-image-height);min-height:var(--wp--lightbox-image-height);min-width:var(--wp--lightbox-image-width);width:var(--wp--lightbox-image-width)}.wp-lightbox-overlay .wp-block-image figcaption{display:none}.wp-lightbox-overlay button{background:none;border:none}.wp-lightbox-overlay .scrim{background-color:#fff;height:100%;opacity:.9;position:absolute;width:100%;z-index:2000000}.wp-lightbox-overlay.active{visibility:visible}@media not (prefers-reduced-motion){.wp-lightbox-overlay.active{animation:turn-on-visibility .25s both}.wp-lightbox-overlay.active img{animation:turn-on-visibility .35s both}.wp-lightbox-overlay.show-closing-animation:not(.active){animation:turn-off-visibility .35s both}.wp-lightbox-overlay.show-closing-animation:not(.active) img{animation:turn-off-visibility .25s both}.wp-lightbox-overlay.zoom.active{animation:none;opacity:1;visibility:visible}.wp-lightbox-overlay.zoom.active .lightbox-image-container{animation:lightbox-zoom-in .4s}.wp-lightbox-overlay.zoom.active .lightbox-image-container img{animation:none}.wp-lightbox-overlay.zoom.active .scrim{animation:turn-on-visibility .4s forwards}.wp-lightbox-overlay.zoom.show-closing-animation:not(.active){animation:none}.wp-lightbox-overlay.zoom.show-closing-animation:not(.active) .lightbox-image-container{animation:lightbox-zoom-out .4s}.wp-lightbox-overlay.zoom.show-closing-animation:not(.active) .lightbox-image-container img{animation:none}.wp-lightbox-overlay.zoom.show-closing-animation:not(.active) .scrim{animation:turn-off-visibility .4s forwards}}@keyframes show-content-image{0%{visibility:hidden}99%{visibility:hidden}to{visibility:visible}}@keyframes turn-on-visibility{0%{opacity:0}to{opacity:1}}@keyframes turn-off-visibility{0%{opacity:1;visibility:visible}99%{opacity:0;visibility:visible}to{opacity:0;visibility:hidden}}@keyframes lightbox-zoom-in{0%{transform:translate(calc((-100vw + var(--wp--lightbox-scrollbar-width))/2 + var(--wp--lightbox-initial-left-position)),calc(-50vh + var(--wp--lightbox-initial-top-position))) scale(var(--wp--lightbox-scale))}to{transform:translate(-50%,-50%) scale(1)}}@keyframes lightbox-zoom-out{0%{transform:translate(-50%,-50%) scale(1);visibility:visible}99%{visibility:visible}to{transform:translate(calc((-100vw + var(--wp--lightbox-scrollbar-width))/2 + var(--wp--lightbox-initial-left-position)),calc(-50vh + var(--wp--lightbox-initial-top-position))) scale(var(--wp--lightbox-scale));visibility:hidden}}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/image/style.min.css */
</style>
<style id='wp-block-image-theme-inline-css' type='text/css'>
:root :where(.wp-block-image figcaption){color:#555;font-size:13px;text-align:center}.is-dark-theme :root :where(.wp-block-image figcaption){color:#ffffffa6}.wp-block-image{margin:0 0 1em}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/image/theme.min.css */
</style>
<style id='wp-block-list-inline-css' type='text/css'>
ol,ul{box-sizing:border-box}:root :where(.wp-block-list.has-background){padding:1.25em 2.375em}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/list/style.min.css */
</style>
	<link rel='preload' as='style' onload="this.onload=null;this.rel='stylesheet'" id='wp-block-navigation' href='https://neo4j.com/wp-includes/blocks/navigation/style.min.css?ver=6.9' type='text/css' media='all' /><style id='wp-block-navigation-link-inline-css' type='text/css'>
.wp-block-navigation .wp-block-navigation-item__label{overflow-wrap:break-word}.wp-block-navigation .wp-block-navigation-item__description{display:none}.link-ui-tools{outline:1px solid #f0f0f0;padding:8px}.link-ui-block-inserter{padding-top:8px}.link-ui-block-inserter__back{margin-left:8px;text-transform:uppercase}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/navigation-link/style.min.css */
</style>
<style id='wp-block-post-content-inline-css' type='text/css'>
.wp-block-post-content{display:flow-root}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/post-content/style.min.css */
</style>
<style id='wp-block-post-date-inline-css' type='text/css'>
.wp-block-post-date{box-sizing:border-box}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/post-date/style.min.css */
</style>
<style id='wp-block-post-featured-image-inline-css' type='text/css'>
.wp-block-post-featured-image{margin-left:0;margin-right:0}.wp-block-post-featured-image a{display:block;height:100%}.wp-block-post-featured-image :where(img){box-sizing:border-box;height:auto;max-width:100%;vertical-align:bottom;width:100%}.wp-block-post-featured-image.alignfull img,.wp-block-post-featured-image.alignwide img{width:100%}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim{background-color:#000;inset:0;position:absolute}.wp-block-post-featured-image{position:relative}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-gradient{background-color:initial}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-0{opacity:0}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-10{opacity:.1}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-20{opacity:.2}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-30{opacity:.3}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-40{opacity:.4}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-50{opacity:.5}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-60{opacity:.6}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-70{opacity:.7}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-80{opacity:.8}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-90{opacity:.9}.wp-block-post-featured-image .wp-block-post-featured-image__overlay.has-background-dim-100{opacity:1}.wp-block-post-featured-image:where(.alignleft,.alignright){width:100%}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/post-featured-image/style.min.css */
</style>
<style id='wp-block-post-title-inline-css' type='text/css'>
.wp-block-post-title{box-sizing:border-box;word-break:break-word}.wp-block-post-title :where(a){display:inline-block;font-family:inherit;font-size:inherit;font-style:inherit;font-weight:inherit;letter-spacing:inherit;line-height:inherit;text-decoration:inherit}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/post-title/style.min.css */
</style>
<style id='wp-block-columns-inline-css' type='text/css'>
.wp-block-columns{box-sizing:border-box;display:flex;flex-wrap:wrap!important}@media (min-width:782px){.wp-block-columns{flex-wrap:nowrap!important}}.wp-block-columns{align-items:normal!important}.wp-block-columns.are-vertically-aligned-top{align-items:flex-start}.wp-block-columns.are-vertically-aligned-center{align-items:center}.wp-block-columns.are-vertically-aligned-bottom{align-items:flex-end}@media (max-width:781px){.wp-block-columns:not(.is-not-stacked-on-mobile)>.wp-block-column{flex-basis:100%!important}}@media (min-width:782px){.wp-block-columns:not(.is-not-stacked-on-mobile)>.wp-block-column{flex-basis:0;flex-grow:1}.wp-block-columns:not(.is-not-stacked-on-mobile)>.wp-block-column[style*=flex-basis]{flex-grow:0}}.wp-block-columns.is-not-stacked-on-mobile{flex-wrap:nowrap!important}.wp-block-columns.is-not-stacked-on-mobile>.wp-block-column{flex-basis:0;flex-grow:1}.wp-block-columns.is-not-stacked-on-mobile>.wp-block-column[style*=flex-basis]{flex-grow:0}:where(.wp-block-columns){margin-bottom:1.75em}:where(.wp-block-columns.has-background){padding:1.25em 2.375em}.wp-block-column{flex-grow:1;min-width:0;overflow-wrap:break-word;word-break:break-word}.wp-block-column.is-vertically-aligned-top{align-self:flex-start}.wp-block-column.is-vertically-aligned-center{align-self:center}.wp-block-column.is-vertically-aligned-bottom{align-self:flex-end}.wp-block-column.is-vertically-aligned-stretch{align-self:stretch}.wp-block-column.is-vertically-aligned-bottom,.wp-block-column.is-vertically-aligned-center,.wp-block-column.is-vertically-aligned-top{width:100%}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/columns/style.min.css */
</style>
<style id='wp-block-group-inline-css' type='text/css'>
.wp-block-group{box-sizing:border-box}:where(.wp-block-group.wp-block-group-is-layout-constrained){position:relative}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/group/style.min.css */
</style>
<style id='wp-block-group-theme-inline-css' type='text/css'>
:where(.wp-block-group.has-background){padding:1.25em 2.375em}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/group/theme.min.css */
</style>
<style id='wp-block-paragraph-inline-css' type='text/css'>
.is-small-text{font-size:.875em}.is-regular-text{font-size:1em}.is-large-text{font-size:2.25em}.is-larger-text{font-size:3em}.has-drop-cap:not(:focus):first-letter{float:left;font-size:8.4em;font-style:normal;font-weight:100;line-height:.68;margin:.05em .1em 0 0;text-transform:uppercase}body.rtl .has-drop-cap:not(:focus):first-letter{float:none;margin-left:.1em}p.has-drop-cap.has-background{overflow:hidden}:root :where(p.has-background){padding:1.25em 2.375em}:where(p.has-text-color:not(.has-link-color)) a{color:inherit}p.has-text-align-left[style*="writing-mode:vertical-lr"],p.has-text-align-right[style*="writing-mode:vertical-rl"]{rotate:180deg}
/*# sourceURL=https://neo4j.com/wp-includes/blocks/paragraph/style.min.css */
</style>
	<link rel='preload' as='style' onload="this.onload=null;this.rel='stylesheet'" id='neo4j-blog-card-style' href='https://neo4j.com/wp-content/plugins/neo4j-blocks//build/blogCard.css?ver=613b7f0366e90e610d5f' type='text/css' media='all' /><style id='neo4j-display-terms-style-inline-css' type='text/css'>
.wp-block-neo4j-display-terms ul{display:flex;flex-wrap:wrap;gap:var(--wp--style--block-gap);list-style:none;margin:0;padding:0}a.wp-block-neo4j-display-terms__link{background-color:var(--wp--preset--color--baltic-10);border-radius:100px;color:inherit;font-family:var(--wp--preset--font-family--public-sans),sans-serif;font-size:14px;font-weight:700;line-height:20px;padding:4px 8px;text-decoration:none}

/*# sourceURL=https://neo4j.com/wp-content/plugins/neo4j-blocks/build/blocks/display-terms/style-index.css */
</style>
<style id='neo4j-limited-terms-style-inline-css' type='text/css'>
.wp-block-neo4j-limited-terms{display:flex;gap:1rem}.wp-block-neo4j-limited-terms ul{display:flex;flex-wrap:wrap;gap:var(--wp--style--block-gap);list-style:none;margin:0;padding:0}a.wp-block-neo4j-limited-terms__link,span.wp-block-neo4j-limited-terms__link{background-color:var(--wp--preset--color--baltic-10);border-radius:100px;color:inherit;font-family:var(--wp--preset--font-family--public-sans),sans-serif;font-size:14px;font-weight:700;line-height:20px;padding:4px 8px;text-decoration:none}.wp-block-neo4j-limited-terms.is-style-gray a.wp-block-neo4j-limited-terms__link,.wp-block-neo4j-limited-terms.is-style-gray span.wp-block-neo4j-limited-terms__link{background-color:var(--wp--preset--color--neutral-15)}

/*# sourceURL=https://neo4j.com/wp-content/plugins/neo4j-blocks/build/blocks/limited-terms/style-index.css */
</style>
<style id='neo4j-neo-codemirror-style-inline-css' type='text/css'>
.wp-block-neo4j-neo-codemirror{background-color:var(--title-background);border-radius:5px;font-family:monospace;position:relative}.wp-block-neo4j-neo-codemirror__title{color:var(--title-color);font-size:var(--wp--preset--font-size--sm);margin:0;padding:12px}.wp-block-neo4j-neo-codemirror pre{font-size:var(--wp--preset--font-size--sm);max-height:var(--max-height);overflow:auto;padding:32px 24px 24px}.wp-block-neo4j-neo-codemirror.expandable.expanded{--max-height:none!important}.wp-block-neo4j-neo-codemirror.expandable .expand-button{cursor:pointer;height:14px;width:14px}.wp-block-neo4j-neo-codemirror .button-wrapper{display:flex;gap:10px;position:absolute;right:20px;top:12px}.wp-block-neo4j-neo-codemirror .copy-button{cursor:pointer;display:flex;position:relative}.wp-block-neo4j-neo-codemirror .copy-button__display{display:flex}.wp-block-neo4j-neo-codemirror .copy-button__success{background:var(--wp--preset--color--forest-30);border-radius:4px;color:var(--wp--preset--color--white);font-size:var(--wp--preset--font-size--small);left:50%;opacity:0;padding:4px;position:absolute;top:0;transform:translate(-50%,100%);transition:opacity .3s ease-in-out;width:60px}.wp-block-neo4j-neo-codemirror .copy-button__success-wrapper{overflow:visible}.wp-block-neo4j-neo-codemirror .copy-button.copied .copy-button__success{opacity:1}

/*# sourceURL=https://neo4j.com/wp-content/plugins/neo4j-blocks/build/blocks/neo-codemirror/style-index.css */
</style>
<style id='neo4j-reading-time-style-inline-css' type='text/css'>


/*# sourceURL=https://neo4j.com/wp-content/plugins/neo4j-blocks/build/blocks/reading-time/style-index.css */
</style>
<style id='neo4j-share-links-style-inline-css' type='text/css'>
.wp-block-neo4j-share-links__text{font-family:var(--wp--preset--font-family--syne-neo),sans-serif;font-size:14px;font-weight:600;letter-spacing:1px;margin:0;text-transform:uppercase}.wp-block-neo4j-share-links p{margin-top:0}.wp-block-neo4j-share-links .social-media-icons{align-items:center;display:flex;gap:10px;list-style-type:none;margin:10px 0 0;padding:0}.wp-block-neo4j-share-links .social-media-icons li{margin-bottom:0;vertical-align:center}.wp-block-neo4j-share-links .social-media-icons li a{align-items:center;background-color:var(--wp--preset--color--baltic-50);border-radius:100%;display:flex;height:32px;justify-content:center;width:32px}

/*# sourceURL=https://neo4j.com/wp-content/plugins/neo4j-blocks/build/blocks/share-links/style-index.css */
</style>
<style id='neo4j-blog-contributors-style-inline-css' type='text/css'>
.wp-block-neo4j-blog-contributors{align-items:center;display:flex;flex-wrap:wrap;gap:var(--wp--style--block-gap)}.wp-block-neo4j-blog-contributors__photos{display:flex}.wp-block-neo4j-blog-contributors__photos .wp-block-neo4j-blog-contributors__photo:nth-child(n+2){margin-left:-5px}.wp-block-neo4j-blog-contributors__photo{border-radius:50%;display:block;height:64px;overflow:hidden;position:relative;width:64px}.wp-block-neo4j-blog-contributors__photo img{aspect-ratio:1/1;inset:0;-o-object-fit:cover;object-fit:cover;position:absolute}.wp-block-neo4j-blog-contributors__content p{margin:0}.wp-block-neo4j-blog-contributors.multiple-contributors .wp-block-neo4j-blog-contributors__content{display:flex;flex:2 1;flex-wrap:wrap;gap:5px}

/*# sourceURL=https://neo4j.com/wp-content/plugins/neo4j-blocks/build/blocks/blog/blog-contributors/style-index.css */
</style>
<style id='neo4j-blog-related-posts-style-inline-css' type='text/css'>
.wp-block-neo4j-blog-related-posts__swiper.swiper{margin:-1rem;padding:1rem}.wp-block-neo4j-blog-related-posts__swiper.swiper .swiper-slide{display:flex;height:auto}.wp-block-neo4j-blog-related-posts .wp-block-neo4j-blog-card:hover{box-shadow:0 8px 15px 0 rgba(0,0,0,.2),0 4px 8px 0 rgba(0,0,0,.12);transform:translateY(-4px)}.related-swiper-navigation{cursor:pointer;display:flex;gap:var(--wp--style--block-gap)}.related-swiper-navigation .related-swiper-next,.related-swiper-navigation .related-swiper-prev{background-repeat:no-repeat;height:48px;width:48px}.related-swiper-navigation .related-swiper-next.swiper-button-disabled,.related-swiper-navigation .related-swiper-prev.swiper-button-disabled{cursor:not-allowed;opacity:.5}.related-swiper-navigation .related-swiper-prev{background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2748%27 height=%2748%27 fill=%27none%27%3E%3Crect width=%2746.909%27 height=%2746.909%27 x=%2747.455%27 y=%2747.455%27 fill=%27%23F5F6F6%27 rx=%2723.454%27 transform=%27rotate%28-180 47.455 47.455%29%27/%3E%3Crect width=%2746.909%27 height=%2746.909%27 x=%2747.455%27 y=%2747.455%27 stroke=%27%23BBBEC3%27 stroke-width=%271.091%27 rx=%2723.454%27 transform=%27rotate%28-180 47.455 47.455%29%27/%3E%3Cpath stroke=%27%234D5157%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%272%27 d=%27M22.375 32.125 14.25 24m0 0 8.125-8.125M14.25 24h19.5%27/%3E%3C/svg%3E")}.related-swiper-navigation .related-swiper-next{background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2748%27 height=%2748%27 fill=%27none%27%3E%3Crect width=%2746.909%27 height=%2746.909%27 x=%27.545%27 y=%27.545%27 fill=%27%23F5F6F6%27 rx=%2723.454%27/%3E%3Crect width=%2746.909%27 height=%2746.909%27 x=%27.545%27 y=%27.545%27 stroke=%27%23BBBEC3%27 stroke-width=%271.091%27 rx=%2723.454%27/%3E%3Cpath stroke=%27%234D5157%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%272%27 d=%27M25.625 15.875 33.75 24m0 0-8.125 8.125M33.75 24h-19.5%27/%3E%3C/svg%3E")}

/*# sourceURL=https://neo4j.com/wp-content/plugins/neo4j-blocks/build/blocks/blog/blog-related-posts/style-index.css */
</style>
<style id='neo4j-blog-related-posts-style-2-inline-css' type='text/css'>
@font-face{font-family:swiper-icons;font-style:normal;font-weight:400;src:url("data:application/font-woff;charset=utf-8;base64, d09GRgABAAAAAAZgABAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABGRlRNAAAGRAAAABoAAAAci6qHkUdERUYAAAWgAAAAIwAAACQAYABXR1BPUwAABhQAAAAuAAAANuAY7+xHU1VCAAAFxAAAAFAAAABm2fPczU9TLzIAAAHcAAAASgAAAGBP9V5RY21hcAAAAkQAAACIAAABYt6F0cBjdnQgAAACzAAAAAQAAAAEABEBRGdhc3AAAAWYAAAACAAAAAj//wADZ2x5ZgAAAywAAADMAAAD2MHtryVoZWFkAAABbAAAADAAAAA2E2+eoWhoZWEAAAGcAAAAHwAAACQC9gDzaG10eAAAAigAAAAZAAAArgJkABFsb2NhAAAC0AAAAFoAAABaFQAUGG1heHAAAAG8AAAAHwAAACAAcABAbmFtZQAAA/gAAAE5AAACXvFdBwlwb3N0AAAFNAAAAGIAAACE5s74hXjaY2BkYGAAYpf5Hu/j+W2+MnAzMYDAzaX6QjD6/4//Bxj5GA8AuRwMYGkAPywL13jaY2BkYGA88P8Agx4j+/8fQDYfA1AEBWgDAIB2BOoAeNpjYGRgYNBh4GdgYgABEMnIABJzYNADCQAACWgAsQB42mNgYfzCOIGBlYGB0YcxjYGBwR1Kf2WQZGhhYGBiYGVmgAFGBiQQkOaawtDAoMBQxXjg/wEGPcYDDA4wNUA2CCgwsAAAO4EL6gAAeNpj2M0gyAACqxgGNWBkZ2D4/wMA+xkDdgAAAHjaY2BgYGaAYBkGRgYQiAHyGMF8FgYHIM3DwMHABGQrMOgyWDLEM1T9/w8UBfEMgLzE////P/5//f/V/xv+r4eaAAeMbAxwIUYmIMHEgKYAYjUcsDAwsLKxc3BycfPw8jEQA/gZBASFhEVExcQlJKWkZWTl5BUUlZRVVNXUNTQZBgMAAMR+E+gAEQFEAAAAKgAqACoANAA+AEgAUgBcAGYAcAB6AIQAjgCYAKIArAC2AMAAygDUAN4A6ADyAPwBBgEQARoBJAEuATgBQgFMAVYBYAFqAXQBfgGIAZIBnAGmAbIBzgHsAAB42u2NMQ6CUAyGW568x9AneYYgm4MJbhKFaExIOAVX8ApewSt4Bic4AfeAid3VOBixDxfPYEza5O+Xfi04YADggiUIULCuEJK8VhO4bSvpdnktHI5QCYtdi2sl8ZnXaHlqUrNKzdKcT8cjlq+rwZSvIVczNiezsfnP/uznmfPFBNODM2K7MTQ45YEAZqGP81AmGGcF3iPqOop0r1SPTaTbVkfUe4HXj97wYE+yNwWYxwWu4v1ugWHgo3S1XdZEVqWM7ET0cfnLGxWfkgR42o2PvWrDMBSFj/IHLaF0zKjRgdiVMwScNRAoWUoH78Y2icB/yIY09An6AH2Bdu/UB+yxopYshQiEvnvu0dURgDt8QeC8PDw7Fpji3fEA4z/PEJ6YOB5hKh4dj3EvXhxPqH/SKUY3rJ7srZ4FZnh1PMAtPhwP6fl2PMJMPDgeQ4rY8YT6Gzao0eAEA409DuggmTnFnOcSCiEiLMgxCiTI6Cq5DZUd3Qmp10vO0LaLTd2cjN4fOumlc7lUYbSQcZFkutRG7g6JKZKy0RmdLY680CDnEJ+UMkpFFe1RN7nxdVpXrC4aTtnaurOnYercZg2YVmLN/d/gczfEimrE/fs/bOuq29Zmn8tloORaXgZgGa78yO9/cnXm2BpaGvq25Dv9S4E9+5SIc9PqupJKhYFSSl47+Qcr1mYNAAAAeNptw0cKwkAAAMDZJA8Q7OUJvkLsPfZ6zFVERPy8qHh2YER+3i/BP83vIBLLySsoKimrqKqpa2hp6+jq6RsYGhmbmJqZSy0sraxtbO3sHRydnEMU4uR6yx7JJXveP7WrDycAAAAAAAH//wACeNpjYGRgYOABYhkgZgJCZgZNBkYGLQZtIJsFLMYAAAw3ALgAeNolizEKgDAQBCchRbC2sFER0YD6qVQiBCv/H9ezGI6Z5XBAw8CBK/m5iQQVauVbXLnOrMZv2oLdKFa8Pjuru2hJzGabmOSLzNMzvutpB3N42mNgZGBg4GKQYzBhYMxJLMlj4GBgAYow/P/PAJJhLM6sSoWKfWCAAwDAjgbRAAB42mNgYGBkAIIbCZo5IPrmUn0hGA0AO8EFTQAA")}:root{--swiper-theme-color:#007aff}:host{display:block;margin-left:auto;margin-right:auto;position:relative;z-index:1}.swiper{display:block;list-style:none;margin-left:auto;margin-right:auto;overflow:hidden;padding:0;position:relative;z-index:1}.swiper-vertical>.swiper-wrapper{flex-direction:column}.swiper-wrapper{box-sizing:content-box;display:flex;height:100%;position:relative;transition-property:transform;transition-timing-function:var(--swiper-wrapper-transition-timing-function,initial);width:100%;z-index:1}.swiper-android .swiper-slide,.swiper-ios .swiper-slide,.swiper-wrapper{transform:translateZ(0)}.swiper-horizontal{touch-action:pan-y}.swiper-vertical{touch-action:pan-x}.swiper-slide{display:block;flex-shrink:0;height:100%;position:relative;transition-property:transform;width:100%}.swiper-slide-invisible-blank{visibility:hidden}.swiper-autoheight,.swiper-autoheight .swiper-slide{height:auto}.swiper-autoheight .swiper-wrapper{align-items:flex-start;transition-property:transform,height}.swiper-backface-hidden .swiper-slide{backface-visibility:hidden;transform:translateZ(0)}.swiper-3d.swiper-css-mode .swiper-wrapper{perspective:1200px}.swiper-3d .swiper-wrapper{transform-style:preserve-3d}.swiper-3d{perspective:1200px}.swiper-3d .swiper-cube-shadow,.swiper-3d .swiper-slide{transform-style:preserve-3d}.swiper-css-mode>.swiper-wrapper{overflow:auto;scrollbar-width:none;-ms-overflow-style:none}.swiper-css-mode>.swiper-wrapper::-webkit-scrollbar{display:none}.swiper-css-mode>.swiper-wrapper>.swiper-slide{scroll-snap-align:start start}.swiper-css-mode.swiper-horizontal>.swiper-wrapper{scroll-snap-type:x mandatory}.swiper-css-mode.swiper-vertical>.swiper-wrapper{scroll-snap-type:y mandatory}.swiper-css-mode.swiper-free-mode>.swiper-wrapper{scroll-snap-type:none}.swiper-css-mode.swiper-free-mode>.swiper-wrapper>.swiper-slide{scroll-snap-align:none}.swiper-css-mode.swiper-centered>.swiper-wrapper:before{content:"";flex-shrink:0;order:9999}.swiper-css-mode.swiper-centered>.swiper-wrapper>.swiper-slide{scroll-snap-align:center center;scroll-snap-stop:always}.swiper-css-mode.swiper-centered.swiper-horizontal>.swiper-wrapper>.swiper-slide:first-child{margin-inline-start:var(--swiper-centered-offset-before)}.swiper-css-mode.swiper-centered.swiper-horizontal>.swiper-wrapper:before{height:100%;min-height:1px;width:var(--swiper-centered-offset-after)}.swiper-css-mode.swiper-centered.swiper-vertical>.swiper-wrapper>.swiper-slide:first-child{margin-block-start:var(--swiper-centered-offset-before)}.swiper-css-mode.swiper-centered.swiper-vertical>.swiper-wrapper:before{height:var(--swiper-centered-offset-after);min-width:1px;width:100%}.swiper-3d .swiper-slide-shadow,.swiper-3d .swiper-slide-shadow-bottom,.swiper-3d .swiper-slide-shadow-left,.swiper-3d .swiper-slide-shadow-right,.swiper-3d .swiper-slide-shadow-top{height:100%;left:0;pointer-events:none;position:absolute;top:0;width:100%;z-index:10}.swiper-3d .swiper-slide-shadow{background:rgba(0,0,0,.15)}.swiper-3d .swiper-slide-shadow-left{background-image:linear-gradient(270deg,rgba(0,0,0,.5),transparent)}.swiper-3d .swiper-slide-shadow-right{background-image:linear-gradient(90deg,rgba(0,0,0,.5),transparent)}.swiper-3d .swiper-slide-shadow-top{background-image:linear-gradient(0deg,rgba(0,0,0,.5),transparent)}.swiper-3d .swiper-slide-shadow-bottom{background-image:linear-gradient(180deg,rgba(0,0,0,.5),transparent)}.swiper-lazy-preloader{border:4px solid var(--swiper-preloader-color,var(--swiper-theme-color));border-radius:50%;border-top:4px solid transparent;box-sizing:border-box;height:42px;left:50%;margin-left:-21px;margin-top:-21px;position:absolute;top:50%;transform-origin:50%;width:42px;z-index:10}.swiper-watch-progress .swiper-slide-visible .swiper-lazy-preloader,.swiper:not(.swiper-watch-progress) .swiper-lazy-preloader{animation:swiper-preloader-spin 1s linear infinite}.swiper-lazy-preloader-white{--swiper-preloader-color:#fff}.swiper-lazy-preloader-black{--swiper-preloader-color:#000}@keyframes swiper-preloader-spin{0%{transform:rotate(0deg)}to{transform:rotate(1turn)}}
:root{--swiper-navigation-size:44px}.swiper-button-next,.swiper-button-prev{align-items:center;color:var(--swiper-navigation-color,var(--swiper-theme-color));cursor:pointer;display:flex;height:var(--swiper-navigation-size);justify-content:center;margin-top:calc(0px - var(--swiper-navigation-size)/2);position:absolute;top:var(--swiper-navigation-top-offset,50%);width:calc(var(--swiper-navigation-size)/44*27);z-index:10}.swiper-button-next.swiper-button-disabled,.swiper-button-prev.swiper-button-disabled{cursor:auto;opacity:.35;pointer-events:none}.swiper-button-next.swiper-button-hidden,.swiper-button-prev.swiper-button-hidden{cursor:auto;opacity:0;pointer-events:none}.swiper-navigation-disabled .swiper-button-next,.swiper-navigation-disabled .swiper-button-prev{display:none!important}.swiper-button-next svg,.swiper-button-prev svg{height:100%;-o-object-fit:contain;object-fit:contain;transform-origin:center;width:100%}.swiper-rtl .swiper-button-next svg,.swiper-rtl .swiper-button-prev svg{transform:rotate(180deg)}.swiper-button-prev,.swiper-rtl .swiper-button-next{left:var(--swiper-navigation-sides-offset,10px);right:auto}.swiper-button-lock{display:none}.swiper-button-next:after,.swiper-button-prev:after{font-family:swiper-icons;font-size:var(--swiper-navigation-size);font-variant:normal;letter-spacing:0;line-height:1;text-transform:none!important}.swiper-button-prev:after,.swiper-rtl .swiper-button-next:after{content:"prev"}.swiper-button-next,.swiper-rtl .swiper-button-prev{left:auto;right:var(--swiper-navigation-sides-offset,10px)}.swiper-button-next:after,.swiper-rtl .swiper-button-prev:after{content:"next"}

/*# sourceURL=https://neo4j.com/wp-content/plugins/neo4j-blocks/build/blocks/blog/blog-related-posts/view.css */
</style>
<style id='neo4j-blog-sidebar-posts-style-inline-css' type='text/css'>
.wp-block-neo4j-blog-sidebar-posts{display:grid;gap:var(--wp--style--block-gap)}

/*# sourceURL=https://neo4j.com/wp-content/plugins/neo4j-blocks/build/blocks/blog/blog-sidebar-posts/style-index.css */
</style>
<style id='global-styles-inline-css' type='text/css'>
:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #181414;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--color--baltic-80: #01121C;--wp--preset--color--baltic-70: #081E2B;--wp--preset--color--baltic-60: #014063;--wp--preset--color--baltic-55: #02507B;--wp--preset--color--baltic-50: #0A6190;--wp--preset--color--baltic-45: #30839D;--wp--preset--color--baltic-40: #4C99A4;--wp--preset--color--baltic-35: #51A6B1;--wp--preset--color--baltic-30: #5DB3BF;--wp--preset--color--baltic-25: #5CC3C9;--wp--preset--color--baltic-20: #8FE3E8;--wp--preset--color--baltic-15: #C3F8FB;--wp--preset--color--baltic-10: #E7FAFB;--wp--preset--color--marigold-70: #543800;--wp--preset--color--marigold-60: #795000;--wp--preset--color--marigold-45: #DA9105;--wp--preset--color--marigold-35: #FFA901;--wp--preset--color--marigold-25: #FFC450;--wp--preset--color--marigold-20: #FFCF72;--wp--preset--color--marigold-15: #FFDE9D;--wp--preset--color--marigold-10: #FFF0D2;--wp--preset--color--forest-55: #145439;--wp--preset--color--forest-30: #6FA646;--wp--preset--color--forest-20: #90CB62;--wp--preset--color--earth-55: #763F18;--wp--preset--color--earth-45: #AF7C4D;--wp--preset--color--earth-40: #D19660;--wp--preset--color--hibiscus-40: #D43300;--wp--preset--color--hibiscus-30: #F96746;--wp--preset--color--hibiscus-25: #FF8E6A;--wp--preset--color--beige-70: #3F3824;--wp--preset--color--beige-60: #666050;--wp--preset--color--beige-50: #999384;--wp--preset--color--beige-40: #C1B9A0;--wp--preset--color--beige-30: #F2EAD4;--wp--preset--color--beige-20: #FFF7E3;--wp--preset--color--beige-10: #FFFCF4;--wp--preset--color--neutral-80: #09090A;--wp--preset--color--neutral-75: #1A1B1D;--wp--preset--color--neutral-70: #212325;--wp--preset--color--neutral-65: #3C3F44;--wp--preset--color--neutral-60: #4D5157;--wp--preset--color--neutral-55: #5E636A;--wp--preset--color--neutral-50: #6F757E;--wp--preset--color--neutral-45: #818790;--wp--preset--color--neutral-40: #959AA1;--wp--preset--color--neutral-35: #A8ACB2;--wp--preset--color--neutral-30: #BBBEC3;--wp--preset--color--neutral-25: #CFD1D4;--wp--preset--color--neutral-20: #E2E3E5;--wp--preset--color--neutral-15: #F5F6F6;--wp--preset--color--neutral-10: #FFFFFF;--wp--preset--color--highlight-periwinkle: #6A82FF;--wp--preset--color--highlight-yellow: #FAFF00;--wp--preset--color--dark-gray: #4F4E4D;--wp--preset--color--cream: #F2EAD4;--wp--preset--color--light-gray: #FCF9F6;--wp--preset--color--full-white: #ffffff;--wp--preset--color--full-black: #000000;--wp--preset--color--transparent: transparent;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: clamp(14px, 0.875rem + ((1vw - 3.2px) * 0.721), 20px);--wp--preset--font-size--large: clamp(22.041px, 1.378rem + ((1vw - 3.2px) * 1.678), 36px);--wp--preset--font-size--x-large: clamp(25.014px, 1.563rem + ((1vw - 3.2px) * 2.042), 42px);--wp--preset--font-size--xs: 0.75rem;--wp--preset--font-size--sm: 0.875rem;--wp--preset--font-size--base: clamp(0.875rem, 0.875rem + ((1vw - 0.2rem) * 0.24), 1rem);--wp--preset--font-size--lg: clamp(0.875rem, 0.875rem + ((1vw - 0.2rem) * 0.481), 1.125rem);--wp--preset--font-size--xl: clamp(0.875rem, 0.875rem + ((1vw - 0.2rem) * 0.721), 1.25rem);--wp--preset--font-size--2-xl: clamp(0.984rem, 0.984rem + ((1vw - 0.2rem) * 0.992), 1.5rem);--wp--preset--font-size--3-xl: clamp(1.185rem, 1.185rem + ((1vw - 0.2rem) * 1.327), 1.875rem);--wp--preset--font-size--4-xl: clamp(1.378rem, 1.378rem + ((1vw - 0.2rem) * 1.677), 2.25rem);--wp--preset--font-size--5-xl: clamp(1.743rem, 1.743rem + ((1vw - 0.2rem) * 2.417), 3rem);--wp--preset--font-size--h-1: clamp(2.25rem, 3vw + 1rem, 3rem);--wp--preset--font-size--h-2: clamp(2rem, 4vw, 2.5rem);--wp--preset--font-size--h-3: clamp(1.75rem, 1vw + 1.25rem, 1.938rem);;--wp--preset--font-size--h-4: clamp(1.5rem, 1vw + 1rem, 1.563rem);;--wp--preset--font-size--h-5: clamp(0.875rem, 0.875rem + ((1vw - 0.2rem) * 0.721), 1.25rem);--wp--preset--font-size--h-6: clamp(0.875rem, 0.875rem + ((1vw - 0.2rem) * 0.24), 1rem);--wp--preset--font-family--syne-neo: syne-neo, "Helvetica Neue", helvetica, roboto, arial, sans-serif;--wp--preset--font-family--public-sans: "Public Sans", "Helvetica Neue", helvetica, roboto, arial, sans-serif;--wp--preset--spacing--20: 0.5rem;--wp--preset--spacing--30: 0.75rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.25rem;--wp--preset--spacing--60: 1.5rem;--wp--preset--spacing--70: 1.75rem;--wp--preset--spacing--80: 2rem;--wp--preset--spacing--px: 1px;--wp--preset--spacing--10: 0.25rem;--wp--preset--spacing--90: clamp(2rem, calc(2rem + ((1vw - 0.4rem) * 1.0417)), 2.25rem);--wp--preset--spacing--100: clamp(2rem, calc(2rem + ((1vw - 0.4rem) * 2.0833)), 2.5rem);--wp--preset--spacing--120: clamp(2rem, calc(2rem + ((1vw - 0.4rem) * 4.1667)), 3rem);--wp--preset--spacing--160: clamp(2rem, calc(2rem + ((1vw - 0.4rem) * 8.3333)), 4rem);--wp--preset--spacing--200: clamp(2rem, calc(2rem + ((1vw - 0.4rem) * 8.3333)), 5rem);--wp--preset--spacing--240: clamp(4rem, calc(4rem + ((1vw - 0.4rem) * 8.3333)), 6rem);--wp--preset--spacing--320: clamp(4rem, calc(4rem + ((1vw - 0.4rem) * 16.6667)), 8rem);--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);--wp--preset--shadow--card: 0px 4px 4px 0px #00000026;--wp--preset--shadow--large: 0px 10px 15px 0px #0000001A;--wp--custom--spacing--small: max(15px, 2vw);--wp--custom--spacing--medium: clamp(2rem, 8vw, calc(4 * var(--wp--style--block-gap)));--wp--custom--spacing--large: clamp(4rem, 10vw, 8rem);--wp--custom--spacing--outer: var(--wp--custom--spacing--small, 1.25rem);--wp--custom--shadow--text: 1px 1px 16px rgba(0,0,0,1);}:root { --wp--style--global--content-size: 760px;--wp--style--global--wide-size: 1152px; }:where(body) { margin: 0; }.wp-site-blocks { padding-top: var(--wp--style--root--padding-top); padding-bottom: var(--wp--style--root--padding-bottom); }.has-global-padding { padding-right: var(--wp--style--root--padding-right); padding-left: var(--wp--style--root--padding-left); }.has-global-padding > .alignfull { margin-right: calc(var(--wp--style--root--padding-right) * -1); margin-left: calc(var(--wp--style--root--padding-left) * -1); }.has-global-padding :where(:not(.alignfull.is-layout-flow) > .has-global-padding:not(.wp-block-block, .alignfull)) { padding-right: 0; padding-left: 0; }.has-global-padding :where(:not(.alignfull.is-layout-flow) > .has-global-padding:not(.wp-block-block, .alignfull)) > .alignfull { margin-left: 0; margin-right: 0; }.wp-site-blocks > .alignleft { float: left; margin-right: 2em; }.wp-site-blocks > .alignright { float: right; margin-left: 2em; }.wp-site-blocks > .aligncenter { justify-content: center; margin-left: auto; margin-right: auto; }:where(.wp-site-blocks) > * { margin-block-start: 1rem; margin-block-end: 0; }:where(.wp-site-blocks) > :first-child { margin-block-start: 0; }:where(.wp-site-blocks) > :last-child { margin-block-end: 0; }:root { --wp--style--block-gap: 1rem; }:root :where(.is-layout-flow) > :first-child{margin-block-start: 0;}:root :where(.is-layout-flow) > :last-child{margin-block-end: 0;}:root :where(.is-layout-flow) > *{margin-block-start: 1rem;margin-block-end: 0;}:root :where(.is-layout-constrained) > :first-child{margin-block-start: 0;}:root :where(.is-layout-constrained) > :last-child{margin-block-end: 0;}:root :where(.is-layout-constrained) > *{margin-block-start: 1rem;margin-block-end: 0;}:root :where(.is-layout-flex){gap: 1rem;}:root :where(.is-layout-grid){gap: 1rem;}.is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}body{color: var(--wp--preset--color--neutral-75);font-family: var(--wp--preset--font-family--public-sans);font-size: var(--wp--preset--font-size--base);line-height: 1.5;--wp--style--root--padding-top: 0px;--wp--style--root--padding-right: 1.5rem;--wp--style--root--padding-bottom: 0px;--wp--style--root--padding-left: 1.5rem;}a:where(:not(.wp-element-button)){text-decoration: none;}:root :where(a:where(:not(.wp-element-button)):hover){text-decoration: underline;}:root :where(.wp-element-button, .wp-block-button__link){background-color: #32373c;border-width: 0;color: #fff;font-family: inherit;font-size: inherit;font-style: inherit;font-weight: inherit;letter-spacing: inherit;line-height: inherit;padding-top: calc(0.667em + 2px);padding-right: calc(1.333em + 2px);padding-bottom: calc(0.667em + 2px);padding-left: calc(1.333em + 2px);text-decoration: none;text-transform: inherit;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-baltic-80-color{color: var(--wp--preset--color--baltic-80) !important;}.has-baltic-70-color{color: var(--wp--preset--color--baltic-70) !important;}.has-baltic-60-color{color: var(--wp--preset--color--baltic-60) !important;}.has-baltic-55-color{color: var(--wp--preset--color--baltic-55) !important;}.has-baltic-50-color{color: var(--wp--preset--color--baltic-50) !important;}.has-baltic-45-color{color: var(--wp--preset--color--baltic-45) !important;}.has-baltic-40-color{color: var(--wp--preset--color--baltic-40) !important;}.has-baltic-35-color{color: var(--wp--preset--color--baltic-35) !important;}.has-baltic-30-color{color: var(--wp--preset--color--baltic-30) !important;}.has-baltic-25-color{color: var(--wp--preset--color--baltic-25) !important;}.has-baltic-20-color{color: var(--wp--preset--color--baltic-20) !important;}.has-baltic-15-color{color: var(--wp--preset--color--baltic-15) !important;}.has-baltic-10-color{color: var(--wp--preset--color--baltic-10) !important;}.has-marigold-70-color{color: var(--wp--preset--color--marigold-70) !important;}.has-marigold-60-color{color: var(--wp--preset--color--marigold-60) !important;}.has-marigold-45-color{color: var(--wp--preset--color--marigold-45) !important;}.has-marigold-35-color{color: var(--wp--preset--color--marigold-35) !important;}.has-marigold-25-color{color: var(--wp--preset--color--marigold-25) !important;}.has-marigold-20-color{color: var(--wp--preset--color--marigold-20) !important;}.has-marigold-15-color{color: var(--wp--preset--color--marigold-15) !important;}.has-marigold-10-color{color: var(--wp--preset--color--marigold-10) !important;}.has-forest-55-color{color: var(--wp--preset--color--forest-55) !important;}.has-forest-30-color{color: var(--wp--preset--color--forest-30) !important;}.has-forest-20-color{color: var(--wp--preset--color--forest-20) !important;}.has-earth-55-color{color: var(--wp--preset--color--earth-55) !important;}.has-earth-45-color{color: var(--wp--preset--color--earth-45) !important;}.has-earth-40-color{color: var(--wp--preset--color--earth-40) !important;}.has-hibiscus-40-color{color: var(--wp--preset--color--hibiscus-40) !important;}.has-hibiscus-30-color{color: var(--wp--preset--color--hibiscus-30) !important;}.has-hibiscus-25-color{color: var(--wp--preset--color--hibiscus-25) !important;}.has-beige-70-color{color: var(--wp--preset--color--beige-70) !important;}.has-beige-60-color{color: var(--wp--preset--color--beige-60) !important;}.has-beige-50-color{color: var(--wp--preset--color--beige-50) !important;}.has-beige-40-color{color: var(--wp--preset--color--beige-40) !important;}.has-beige-30-color{color: var(--wp--preset--color--beige-30) !important;}.has-beige-20-color{color: var(--wp--preset--color--beige-20) !important;}.has-beige-10-color{color: var(--wp--preset--color--beige-10) !important;}.has-neutral-80-color{color: var(--wp--preset--color--neutral-80) !important;}.has-neutral-75-color{color: var(--wp--preset--color--neutral-75) !important;}.has-neutral-70-color{color: var(--wp--preset--color--neutral-70) !important;}.has-neutral-65-color{color: var(--wp--preset--color--neutral-65) !important;}.has-neutral-60-color{color: var(--wp--preset--color--neutral-60) !important;}.has-neutral-55-color{color: var(--wp--preset--color--neutral-55) !important;}.has-neutral-50-color{color: var(--wp--preset--color--neutral-50) !important;}.has-neutral-45-color{color: var(--wp--preset--color--neutral-45) !important;}.has-neutral-40-color{color: var(--wp--preset--color--neutral-40) !important;}.has-neutral-35-color{color: var(--wp--preset--color--neutral-35) !important;}.has-neutral-30-color{color: var(--wp--preset--color--neutral-30) !important;}.has-neutral-25-color{color: var(--wp--preset--color--neutral-25) !important;}.has-neutral-20-color{color: var(--wp--preset--color--neutral-20) !important;}.has-neutral-15-color{color: var(--wp--preset--color--neutral-15) !important;}.has-neutral-10-color{color: var(--wp--preset--color--neutral-10) !important;}.has-highlight-periwinkle-color{color: var(--wp--preset--color--highlight-periwinkle) !important;}.has-highlight-yellow-color{color: var(--wp--preset--color--highlight-yellow) !important;}.has-dark-gray-color{color: var(--wp--preset--color--dark-gray) !important;}.has-cream-color{color: var(--wp--preset--color--cream) !important;}.has-light-gray-color{color: var(--wp--preset--color--light-gray) !important;}.has-full-white-color{color: var(--wp--preset--color--full-white) !important;}.has-full-black-color{color: var(--wp--preset--color--full-black) !important;}.has-transparent-color{color: var(--wp--preset--color--transparent) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-baltic-80-background-color{background-color: var(--wp--preset--color--baltic-80) !important;}.has-baltic-70-background-color{background-color: var(--wp--preset--color--baltic-70) !important;}.has-baltic-60-background-color{background-color: var(--wp--preset--color--baltic-60) !important;}.has-baltic-55-background-color{background-color: var(--wp--preset--color--baltic-55) !important;}.has-baltic-50-background-color{background-color: var(--wp--preset--color--baltic-50) !important;}.has-baltic-45-background-color{background-color: var(--wp--preset--color--baltic-45) !important;}.has-baltic-40-background-color{background-color: var(--wp--preset--color--baltic-40) !important;}.has-baltic-35-background-color{background-color: var(--wp--preset--color--baltic-35) !important;}.has-baltic-30-background-color{background-color: var(--wp--preset--color--baltic-30) !important;}.has-baltic-25-background-color{background-color: var(--wp--preset--color--baltic-25) !important;}.has-baltic-20-background-color{background-color: var(--wp--preset--color--baltic-20) !important;}.has-baltic-15-background-color{background-color: var(--wp--preset--color--baltic-15) !important;}.has-baltic-10-background-color{background-color: var(--wp--preset--color--baltic-10) !important;}.has-marigold-70-background-color{background-color: var(--wp--preset--color--marigold-70) !important;}.has-marigold-60-background-color{background-color: var(--wp--preset--color--marigold-60) !important;}.has-marigold-45-background-color{background-color: var(--wp--preset--color--marigold-45) !important;}.has-marigold-35-background-color{background-color: var(--wp--preset--color--marigold-35) !important;}.has-marigold-25-background-color{background-color: var(--wp--preset--color--marigold-25) !important;}.has-marigold-20-background-color{background-color: var(--wp--preset--color--marigold-20) !important;}.has-marigold-15-background-color{background-color: var(--wp--preset--color--marigold-15) !important;}.has-marigold-10-background-color{background-color: var(--wp--preset--color--marigold-10) !important;}.has-forest-55-background-color{background-color: var(--wp--preset--color--forest-55) !important;}.has-forest-30-background-color{background-color: var(--wp--preset--color--forest-30) !important;}.has-forest-20-background-color{background-color: var(--wp--preset--color--forest-20) !important;}.has-earth-55-background-color{background-color: var(--wp--preset--color--earth-55) !important;}.has-earth-45-background-color{background-color: var(--wp--preset--color--earth-45) !important;}.has-earth-40-background-color{background-color: var(--wp--preset--color--earth-40) !important;}.has-hibiscus-40-background-color{background-color: var(--wp--preset--color--hibiscus-40) !important;}.has-hibiscus-30-background-color{background-color: var(--wp--preset--color--hibiscus-30) !important;}.has-hibiscus-25-background-color{background-color: var(--wp--preset--color--hibiscus-25) !important;}.has-beige-70-background-color{background-color: var(--wp--preset--color--beige-70) !important;}.has-beige-60-background-color{background-color: var(--wp--preset--color--beige-60) !important;}.has-beige-50-background-color{background-color: var(--wp--preset--color--beige-50) !important;}.has-beige-40-background-color{background-color: var(--wp--preset--color--beige-40) !important;}.has-beige-30-background-color{background-color: var(--wp--preset--color--beige-30) !important;}.has-beige-20-background-color{background-color: var(--wp--preset--color--beige-20) !important;}.has-beige-10-background-color{background-color: var(--wp--preset--color--beige-10) !important;}.has-neutral-80-background-color{background-color: var(--wp--preset--color--neutral-80) !important;}.has-neutral-75-background-color{background-color: var(--wp--preset--color--neutral-75) !important;}.has-neutral-70-background-color{background-color: var(--wp--preset--color--neutral-70) !important;}.has-neutral-65-background-color{background-color: var(--wp--preset--color--neutral-65) !important;}.has-neutral-60-background-color{background-color: var(--wp--preset--color--neutral-60) !important;}.has-neutral-55-background-color{background-color: var(--wp--preset--color--neutral-55) !important;}.has-neutral-50-background-color{background-color: var(--wp--preset--color--neutral-50) !important;}.has-neutral-45-background-color{background-color: var(--wp--preset--color--neutral-45) !important;}.has-neutral-40-background-color{background-color: var(--wp--preset--color--neutral-40) !important;}.has-neutral-35-background-color{background-color: var(--wp--preset--color--neutral-35) !important;}.has-neutral-30-background-color{background-color: var(--wp--preset--color--neutral-30) !important;}.has-neutral-25-background-color{background-color: var(--wp--preset--color--neutral-25) !important;}.has-neutral-20-background-color{background-color: var(--wp--preset--color--neutral-20) !important;}.has-neutral-15-background-color{background-color: var(--wp--preset--color--neutral-15) !important;}.has-neutral-10-background-color{background-color: var(--wp--preset--color--neutral-10) !important;}.has-highlight-periwinkle-background-color{background-color: var(--wp--preset--color--highlight-periwinkle) !important;}.has-highlight-yellow-background-color{background-color: var(--wp--preset--color--highlight-yellow) !important;}.has-dark-gray-background-color{background-color: var(--wp--preset--color--dark-gray) !important;}.has-cream-background-color{background-color: var(--wp--preset--color--cream) !important;}.has-light-gray-background-color{background-color: var(--wp--preset--color--light-gray) !important;}.has-full-white-background-color{background-color: var(--wp--preset--color--full-white) !important;}.has-full-black-background-color{background-color: var(--wp--preset--color--full-black) !important;}.has-transparent-background-color{background-color: var(--wp--preset--color--transparent) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-baltic-80-border-color{border-color: var(--wp--preset--color--baltic-80) !important;}.has-baltic-70-border-color{border-color: var(--wp--preset--color--baltic-70) !important;}.has-baltic-60-border-color{border-color: var(--wp--preset--color--baltic-60) !important;}.has-baltic-55-border-color{border-color: var(--wp--preset--color--baltic-55) !important;}.has-baltic-50-border-color{border-color: var(--wp--preset--color--baltic-50) !important;}.has-baltic-45-border-color{border-color: var(--wp--preset--color--baltic-45) !important;}.has-baltic-40-border-color{border-color: var(--wp--preset--color--baltic-40) !important;}.has-baltic-35-border-color{border-color: var(--wp--preset--color--baltic-35) !important;}.has-baltic-30-border-color{border-color: var(--wp--preset--color--baltic-30) !important;}.has-baltic-25-border-color{border-color: var(--wp--preset--color--baltic-25) !important;}.has-baltic-20-border-color{border-color: var(--wp--preset--color--baltic-20) !important;}.has-baltic-15-border-color{border-color: var(--wp--preset--color--baltic-15) !important;}.has-baltic-10-border-color{border-color: var(--wp--preset--color--baltic-10) !important;}.has-marigold-70-border-color{border-color: var(--wp--preset--color--marigold-70) !important;}.has-marigold-60-border-color{border-color: var(--wp--preset--color--marigold-60) !important;}.has-marigold-45-border-color{border-color: var(--wp--preset--color--marigold-45) !important;}.has-marigold-35-border-color{border-color: var(--wp--preset--color--marigold-35) !important;}.has-marigold-25-border-color{border-color: var(--wp--preset--color--marigold-25) !important;}.has-marigold-20-border-color{border-color: var(--wp--preset--color--marigold-20) !important;}.has-marigold-15-border-color{border-color: var(--wp--preset--color--marigold-15) !important;}.has-marigold-10-border-color{border-color: var(--wp--preset--color--marigold-10) !important;}.has-forest-55-border-color{border-color: var(--wp--preset--color--forest-55) !important;}.has-forest-30-border-color{border-color: var(--wp--preset--color--forest-30) !important;}.has-forest-20-border-color{border-color: var(--wp--preset--color--forest-20) !important;}.has-earth-55-border-color{border-color: var(--wp--preset--color--earth-55) !important;}.has-earth-45-border-color{border-color: var(--wp--preset--color--earth-45) !important;}.has-earth-40-border-color{border-color: var(--wp--preset--color--earth-40) !important;}.has-hibiscus-40-border-color{border-color: var(--wp--preset--color--hibiscus-40) !important;}.has-hibiscus-30-border-color{border-color: var(--wp--preset--color--hibiscus-30) !important;}.has-hibiscus-25-border-color{border-color: var(--wp--preset--color--hibiscus-25) !important;}.has-beige-70-border-color{border-color: var(--wp--preset--color--beige-70) !important;}.has-beige-60-border-color{border-color: var(--wp--preset--color--beige-60) !important;}.has-beige-50-border-color{border-color: var(--wp--preset--color--beige-50) !important;}.has-beige-40-border-color{border-color: var(--wp--preset--color--beige-40) !important;}.has-beige-30-border-color{border-color: var(--wp--preset--color--beige-30) !important;}.has-beige-20-border-color{border-color: var(--wp--preset--color--beige-20) !important;}.has-beige-10-border-color{border-color: var(--wp--preset--color--beige-10) !important;}.has-neutral-80-border-color{border-color: var(--wp--preset--color--neutral-80) !important;}.has-neutral-75-border-color{border-color: var(--wp--preset--color--neutral-75) !important;}.has-neutral-70-border-color{border-color: var(--wp--preset--color--neutral-70) !important;}.has-neutral-65-border-color{border-color: var(--wp--preset--color--neutral-65) !important;}.has-neutral-60-border-color{border-color: var(--wp--preset--color--neutral-60) !important;}.has-neutral-55-border-color{border-color: var(--wp--preset--color--neutral-55) !important;}.has-neutral-50-border-color{border-color: var(--wp--preset--color--neutral-50) !important;}.has-neutral-45-border-color{border-color: var(--wp--preset--color--neutral-45) !important;}.has-neutral-40-border-color{border-color: var(--wp--preset--color--neutral-40) !important;}.has-neutral-35-border-color{border-color: var(--wp--preset--color--neutral-35) !important;}.has-neutral-30-border-color{border-color: var(--wp--preset--color--neutral-30) !important;}.has-neutral-25-border-color{border-color: var(--wp--preset--color--neutral-25) !important;}.has-neutral-20-border-color{border-color: var(--wp--preset--color--neutral-20) !important;}.has-neutral-15-border-color{border-color: var(--wp--preset--color--neutral-15) !important;}.has-neutral-10-border-color{border-color: var(--wp--preset--color--neutral-10) !important;}.has-highlight-periwinkle-border-color{border-color: var(--wp--preset--color--highlight-periwinkle) !important;}.has-highlight-yellow-border-color{border-color: var(--wp--preset--color--highlight-yellow) !important;}.has-dark-gray-border-color{border-color: var(--wp--preset--color--dark-gray) !important;}.has-cream-border-color{border-color: var(--wp--preset--color--cream) !important;}.has-light-gray-border-color{border-color: var(--wp--preset--color--light-gray) !important;}.has-full-white-border-color{border-color: var(--wp--preset--color--full-white) !important;}.has-full-black-border-color{border-color: var(--wp--preset--color--full-black) !important;}.has-transparent-border-color{border-color: var(--wp--preset--color--transparent) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}.has-xs-font-size{font-size: var(--wp--preset--font-size--xs) !important;}.has-sm-font-size{font-size: var(--wp--preset--font-size--sm) !important;}.has-base-font-size{font-size: var(--wp--preset--font-size--base) !important;}.has-lg-font-size{font-size: var(--wp--preset--font-size--lg) !important;}.has-xl-font-size{font-size: var(--wp--preset--font-size--xl) !important;}.has-2-xl-font-size{font-size: var(--wp--preset--font-size--2-xl) !important;}.has-3-xl-font-size{font-size: var(--wp--preset--font-size--3-xl) !important;}.has-4-xl-font-size{font-size: var(--wp--preset--font-size--4-xl) !important;}.has-5-xl-font-size{font-size: var(--wp--preset--font-size--5-xl) !important;}.has-h-1-font-size{font-size: var(--wp--preset--font-size--h-1) !important;}.has-h-2-font-size{font-size: var(--wp--preset--font-size--h-2) !important;}.has-h-3-font-size{font-size: var(--wp--preset--font-size--h-3) !important;}.has-h-4-font-size{font-size: var(--wp--preset--font-size--h-4) !important;}.has-h-5-font-size{font-size: var(--wp--preset--font-size--h-5) !important;}.has-h-6-font-size{font-size: var(--wp--preset--font-size--h-6) !important;}.has-syne-neo-font-family{font-family: var(--wp--preset--font-family--syne-neo) !important;}.has-public-sans-font-family{font-family: var(--wp--preset--font-family--public-sans) !important;}
:root :where(.wp-block-image .wp-element-caption,.wp-block-image  .wp-block-audio figcaption,.wp-block-image  .wp-block-embed figcaption,.wp-block-image  .wp-block-gallery figcaption,.wp-block-image  .wp-block-image figcaption,.wp-block-image  .wp-block-table figcaption,.wp-block-image  .wp-block-video figcaption){color: var(--wp--preset--color--baltic-50);font-size: var(--wp--preset--font-size--sm);margin-top: var(--wp--style--block-gap);}
:root :where(.wp-block-group a:where(:not(.wp-element-button))){color: var(--wp--preset--color--baltic-50);text-decoration: underline;}
:root :where(.wp-block-group a:where(:not(.wp-element-button)):hover){color: var(--wp--preset--color--baltic-60);}
:root :where(.wp-block-group a:where(:not(.wp-element-button)):focus){color: var(--wp--preset--color--baltic-60);}
:root :where(.wp-block-neo4j-card){background-color: var(--wp--preset--color--full-white);border-radius: 8px;border-color: var(--wp--preset--color--neutral-20);border-width: 1px;border-style: solid;padding-top: 2rem;padding-right: 1.5rem;padding-bottom: 2rem;padding-left: 1.5rem;}
:root :where(.wp-block-neo4j-banner){border-radius: 12px;border-color: var(--wp--preset--color--neutral-20);border-width: 1px;border-style: solid;padding-top: 1.5rem;padding-right: 1.5rem;padding-bottom: 1.5rem;padding-left: 1.5rem;}
:root :where(.wp-block-neo4j-badge){background-color: #e3fcd1;border-radius: 999px;border-color: #85c457;border-width: 1px;border-style: solid;color: #376d21;padding-top: 0.25em;padding-right: 0.5em;padding-bottom: 0.25em;padding-left: 0.5em;}
:root :where(.wp-block-neo4j-pull-quote){background-color: var(--wp--preset--color--neutral-15);border-radius: 8px;border-color: transparent;border-width: 0px;border-style: solid;color: var(--wp--preset--color--neutral-75);font-size: var(--wp--preset--font-size--xl);font-weight: 600;line-height: 1.5;padding-top: 1.5rem;padding-right: 1.5rem;padding-bottom: 1.5rem;padding-left: 1.5rem;}
:root :where(.wp-block-neo4j-pull-quote cite){color: var(--wp--preset--color--neutral-60);font-size: var(--wp--preset--font-size--base);font-weight: 400;}:root :where(.wp-block-neo4j-pull-quote cite .wp-block-neo4j-pull-quote__cite-title){font-size: var(--wp--preset--font-size--sm);}
/*# sourceURL=global-styles-inline-css */
</style>
<style id='core-block-supports-inline-css' type='text/css'>
.wp-elements-07f4705aebb498b0c8c2c3d3a0c40035 a:where(:not(.wp-element-button)){color:var(--wp--preset--color--neutral-80);}.wp-container-core-navigation-is-layout-a89b3969{justify-content:center;}.wp-container-2{top:calc(0px + var(--wp-admin--admin-bar--position-offset, 0px));position:sticky;z-index:10;}.wp-elements-f66778e2b39d390902c89d839b642d8d a:where(:not(.wp-element-button)){color:var(--wp--preset--color--neutral-55);}.wp-container-core-group-is-layout-6c531013{flex-wrap:nowrap;}.wp-container-core-columns-is-layout-a42798d2{flex-wrap:nowrap;}.wp-container-core-columns-is-layout-79d6dacc{flex-wrap:nowrap;gap:2em var(--wp--preset--spacing--120);}.wp-container-core-group-is-layout-9366075c{justify-content:space-between;}
/*# sourceURL=core-block-supports-inline-css */
</style>
<style id='neo4j-core-navigation-styles-inline-css' type='text/css'>
.is-style-subnav .wp-block-navigation-item .wp-block-navigation-item__content{text-decoration:none!important;color:#0070d9;line-height:inherit;cursor:pointer}.is-style-subnav .wp-block-navigation-item .wp-block-navigation-item__content:hover{color:#0056b3;text-decoration:underline!important}.is-style-subnav .wp-block-navigation-item.current-menu-item .wp-block-navigation-item__content{color:#151e29}.wp-block-navigation__responsive-container__responsive-container-content .wp-block-navigation-item__content:not(.wp-block-navigation-submenu__toggle){padding-right:0}.wp-block-navigation.has-expandable-modal-submenus .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation__responsive-container-content .wp-block-navigation-item__content:not(.wp-block-navigation-submenu__toggle){padding-right:0}.wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation__responsive-container-content .has-child .wp-block-navigation__submenu-container{gap:1rem}@media (max-width:599px){.wp-block-navigation__submenu-icon.wp-block-navigation-submenu__toggle:before{content:"";display:block;position:absolute;inset:0;width:100vw;left:-55vw;height:1.1rem}}.wp-block-navigation.has-expandable-modal-submenus .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation__responsive-container-content .has-child .wp-block-navigation__submenu-container{height:0;opacity:0;overflow:hidden;visibility:hidden;width:0}.wp-block-navigation.has-expandable-modal-submenus .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation__responsive-container-content .has-child .wp-block-navigation-submenu__toggle[aria-expanded=true]~.wp-block-navigation__submenu-container{height:auto;opacity:1;overflow:initial;visibility:visible;width:auto}.wp-block-navigation.has-expandable-modal-submenus .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation__responsive-container-content .wp-block-navigation-item{display:block;text-align:var(--navigation-layout-justification-setting,initial)}.wp-block-navigation.has-expandable-modal-submenus .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation__responsive-container-content .items-justified-right .wp-block-navigation-item{display:block;text-align:right}.wp-block-navigation.has-expandable-modal-submenus .wp-block-navigation .has-child .wp-block-navigation__submenu-container>.wp-block-navigation-item>.wp-block-navigation-item__content{display:inline}.wp-block-navigation.has-expandable-modal-submenus .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation__responsive-container-content .wp-block-navigation-item__content{padding-right:.85em}.wp-block-navigation.has-expandable-modal-submenus .wp-block-navigation .wp-block-navigation-item__content{display:inline}.wp-block-navigation.has-expandable-modal-submenus .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation__responsive-container-content .wp-block-navigation__submenu-icon{display:inline}html.has-modal-open #main-navigation-wrapper{opacity:0;z-index:0}
/*# sourceURL=https://neo4j.com/wp-content/themes/neo4jweb/assets/css/blocks/core/navigation.css */
</style>
<style id='neo4j-core-group-styles-inline-css' type='text/css'>
.wp-block-group>:first-child{margin-top:0}:where(.wp-block-group.has-background){padding:initial}.is-style-shadow-card{box-shadow:var(--wp--preset--shadow--card)}.is-style-shadow-large{box-shadow:var(--wp--preset--shadow--large)}.wp-block-group.full-height{height:100%}@media (max-width:781px){.wp-block-group.has-mobile-background-hide{background-image:none!important}}@media (max-width:999px){.wp-block-group.has-tablet-background-hide{background-image:none!important}}@media (max-width:1239px){.wp-block-group.has-desktop-background-hide{background-image:none!important}}.wp-block-group.has-top-left-background-position{background-position:top left!important}.wp-block-group.has-top-center-background-position{background-position:top center!important}.wp-block-group.has-top-right-background-position{background-position:top right!important}.wp-block-group.has-center-left-background-position{background-position:center left!important}.wp-block-group.has-center-center-background-position{background-position:center center!important}.wp-block-group.has-center-right-background-position{background-position:center right!important}.wp-block-group.has-bottom-left-background-position{background-position:bottom left!important}.wp-block-group.has-bottom-center-background-position{background-position:bottom center!important}.wp-block-group.has-bottom-right-background-position{background-position:bottom right!important}.wp-block-group.has-cover-background-size{background-size:cover!important}.wp-block-group.has-contain-background-size{background-size:contain!important}.wp-block-group.has-none-background-size{background-size:auto!important}.wp-block-group.has-no-repeat-background-repeat{background-repeat:no-repeat!important}.wp-block-group.has-repeat-background-repeat{background-repeat:repeat!important}.wp-block-group.has-repeat-x-background-repeat{background-repeat:repeat-x!important}.wp-block-group.has-repeat-y-background-repeat{background-repeat:repeat-y!important}.wp-block-group.is-position-sticky{z-index:15;top:calc(var(--wp-sticky-navigation-height,0px) + var(--wp-admin--admin-bar--height,0px))}.wp-block-group.is-position-sticky.blog-sidebar{top:calc(var(--wp-sticky-navigation-height,0px) + var(--wp-admin--admin-bar--height,0px) + var(--wp-blog-nav-height,0px) + 10px)}.wp-block-group[id]{scroll-margin-top:calc(var(--wp-scroll-padding-top,0) * 1px)}.wp-block-group.is-position-sticky.neo4j-blog-navigation{z-index:20}@media (max-width:599px){.neo4j-blog-navigation .wp-block-navigation{justify-content:flex-start}}.neo4j-blog-navigation .wp-block-navigation__container{gap:16px}@media (min-width:786px){.neo4j-blog-navigation .wp-block-navigation__container{gap:64px}}.neo4j-blog-navigation .wp-block-navigation-item.has-child .wp-block-navigation-item__content:focus,.neo4j-blog-navigation .wp-block-navigation-item.has-child .wp-block-navigation-item__content:hover{border-bottom-color:transparent}.neo4j-blog-navigation .wp-block-navigation-item__content{padding:16px 0;border-bottom:2px solid transparent;text-decoration:none}.neo4j-blog-navigation .wp-block-navigation-item__content:focus,.neo4j-blog-navigation .wp-block-navigation-item__content:hover{color:var(--wp--preset--color--baltic-50);border-bottom-color:var(--wp--preset--color--baltic-50)}.neo4j-blog-navigation .wp-block-navigation-item.has-child .wp-block-navigation__submenu-icon{height:12px;width:16px}.neo4j-blog-navigation .wp-block-navigation-item.has-child .wp-block-navigation__submenu-icon svg{fill:none;height:12px;width:16px;margin-top:0}.neo4j-blog-navigation .wp-block-navigation__submenu-container{padding:0}.neo4j-blog-navigation .wp-block-navigation__submenu-container .wp-block-navigation-item:focus,.neo4j-blog-navigation .wp-block-navigation__submenu-container .wp-block-navigation-item:hover{background-color:#eff0f1}.neo4j-blog-navigation .wp-block-navigation__submenu-container .wp-block-navigation-item__content{padding:12px;border-bottom-color:transparent}.neo4j-blog-navigation .wp-block-navigation__responsive-container-open{padding:16px 0;align-items:center;gap:8px}.neo4j-blog-navigation .wp-block-navigation__responsive-container-open svg{fill:none;height:8px;width:12px}
/*# sourceURL=https://neo4j.com/wp-content/themes/neo4jweb/assets/css/blocks/core/group.css */
</style>
<style id='enable-linked-groups-block-styles-inline-css' type='text/css'>
.wp-block-group.is-linked{position:relative;transition:all .2s ease-in-out}.wp-block-group.is-linked:not(.block-editor-block-list__block)>:nth-child(2){margin-block-start:0}.wp-block-group.is-linked a.wp-block-group__link{bottom:0;height:100%;left:0;position:absolute;text-decoration:none!important;width:100%;z-index:3}.wp-block-group.is-linked .wp-block-button,.wp-block-group.is-linked a{position:relative;z-index:4}.wp-block-group.is-linked:hover{box-shadow:var(--wp--preset--shadow--card),var(--wp--preset--shadow--card)}

/*# sourceURL=https://neo4j.com/wp-content/plugins/neo4j-blocks/build/enable-linked-groups.css */
</style>
<style id='neo4j-core-post-featured-image-styles-inline-css' type='text/css'>
@media screen and (min-width:782px){.wp-block-blog .wp-block-post-featured-image img{object-position:top right}}@media screen and (max-width:781px){.wp-block-blog .wp-block-post-featured-image{height:auto!important}}
/*# sourceURL=https://neo4j.com/wp-content/themes/neo4jweb/assets/css/blocks/core/post-featured-image.css */
</style>
<style id='neo4j-core-columns-styles-inline-css' type='text/css'>
.is-style-justify-center{justify-content:center}.is-style-justify-start{justify-content:flex-start}.is-style-justify-end{justify-content:flex-end}.is-style-justify-between{justify-content:space-between}.is-style-justify-around{justify-content:space-around}.is-style-justify-evenly{justify-content:space-evenly}.is-style-justify-normal{justify-content:normal}.is-style-justify-stretch{justify-content:stretch}@media (max-width:782px){.wp-block-columns.is-reversed-on-mobile{flex-direction:column-reverse}}.wp-block-columns:not(.is-not-stacked-on-mobile)>.wp-block-column{flex-basis:0;flex-grow:1}.wp-block-columns:not(.is-not-stacked-on-mobile)>.wp-block-column[style*=flex-basis]{flex-grow:0}@media (max-width:781px){.wp-block-columns:not(.is-not-stacked-on-mobile)>.wp-block-column{flex-basis:100%!important}}
/*# sourceURL=https://neo4j.com/wp-content/themes/neo4jweb/assets/css/blocks/core/columns.css */
</style>
<style id='neo4j-core-paragraph-styles-inline-css' type='text/css'>
.is-style-text-shadow{text-shadow:var(--wp--custom--shadow--text)}p code{border:none;background-color:var(--wp--preset--color--neutral-15);font-family:consolas,"Liberation Mono",courier,monospace;font-weight:400;color:var(--wp--preset--color--neutral-75);display:inline;max-width:100%;word-wrap:break-word;padding:.125rem .3125rem .0625rem}.is-style-text-overline,.text-overline{letter-spacing:1px;text-transform:uppercase;font-weight:400;line-height:1.71;font-size:var(--wp--preset--font-size--sm);font-family:var(--wp--preset--font-family--syne-neo);margin-bottom:.5rem}.is-style-subtitle,.section-subtitle{font-size:1.25rem;line-height:1.4;letter-spacing:.25px;font-family:"Public Sans";font-weight:400}.hero-subtitle,.is-style-subtitle-lg{font-size:clamp(1.5rem,3vw,1.563rem);line-height:1.3;letter-spacing:.25px;font-family:"Public Sans";font-weight:500}
/*# sourceURL=https://neo4j.com/wp-content/themes/neo4jweb/assets/css/blocks/core/paragraph.css */
</style>
<style id='neo4j-core-list-styles-inline-css' type='text/css'>
.is-layout-constrained ul.is-style-checkmark{margin-left:1.25rem!important;padding-left:0}.is-layout-constrained ul.is-style-checkmark li{list-style-type:none;position:relative;margin-bottom:1rem}.is-layout-constrained ul.is-style-checkmark li:before{content:"";width:14px;height:14px;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' fill='none'%3E%3Cpath fill='%2330839D' fill-rule='evenodd' d='M6 11.6A5.6 5.6 0 1 0 6 .4a5.6 5.6 0 0 0 0 11.2Zm2.595-6.505a.7.7 0 1 0-.99-.99L5.3 6.41l-.905-.905a.7.7 0 1 0-.99.99l1.4 1.4a.7.7 0 0 0 .99 0l2.8-2.8Z' clip-rule='evenodd'/%3E%3C/svg%3E");background-repeat:no-repeat;background-size:contain;display:inline-block;position:absolute;left:-1.2rem;top:6px}
/*# sourceURL=https://neo4j.com/wp-content/themes/neo4jweb/assets/css/blocks/core/list.css */
</style>
<style id='neo4j-core-heading-styles-inline-css' type='text/css'>
.is-style-text-shadow{text-shadow:var(--wp--custom--shadow--text)}.is-style-text-overline,.text-overline{letter-spacing:1px;text-transform:uppercase;font-weight:400;line-height:1.71;font-size:var(--wp--preset--font-size--sm);font-family:var(--wp--preset--font-family--syne-neo);margin-bottom:.5rem}.is-style-subtitle,.section-subtitle{font-size:1.25rem;line-height:1.4;letter-spacing:.25px;font-family:"Public Sans";font-weight:400}.hero-subtitle,.is-style-subtitle-lg{font-size:clamp(1.5rem,3vw,1.563rem);line-height:1.3;letter-spacing:.25px;font-family:"Public Sans";font-weight:500}.is-style-h1{letter-spacing:-.25px;line-height:1.25;font-size:var(--wp--preset--font-size--h-1);font-family:syne-neo;font-weight:500}.is-style-h2{letter-spacing:0;line-height:1.2;font-family:syne-neo;font-size:var(--wp--preset--font-size--h-2);font-weight:500}.is-style-h3{line-height:1.3;letter-spacing:.25px;font-family:syne-neo;font-size:var(--wp--preset--font-size--h-3);font-weight:500}.is-style-h4{line-height:1.3;letter-spacing:.25px;font-family:var(--wp--preset--font-family--public-sans);font-size:var(--wp--preset--font-size--h-4);font-weight:500}.is-style-h5{line-height:1.4;letter-spacing:.25px;font-family:var(--wp--preset--font-family--public-sans);font-size:var(--wp--preset--font-size--h-5);font-weight:700}.is-style-h6{line-height:1.5;letter-spacing:.25px;font-family:var(--wp--preset--font-family--public-sans);font-size:var(--wp--preset--font-size--h-6);font-weight:700}h2[id],h3[id],h4[id],h5[id]{scroll-margin-top:calc(var(--wp-scroll-padding-top,0px) * 1px)}
/*# sourceURL=https://neo4j.com/wp-content/themes/neo4jweb/assets/css/blocks/core/heading.css */
</style>
<style id='neo4j-core-image-styles-inline-css' type='text/css'>
.wp-block-image.is-style-color-on-hover{filter:grayscale(1);opacity:.8;transition:all .5s ease-in-out}.wp-block-image.is-style-color-on-hover:hover{filter:grayscale(0);opacity:1}.wp-block-image.has-custom-border img{border-style:solid}
/*# sourceURL=https://neo4j.com/wp-content/themes/neo4jweb/assets/css/blocks/core/image.css */
</style>
<style id='neo4j-core-separator-styles-inline-css' type='text/css'>
.wp-block-separator{width:100%;height:2px;max-width:100%;border:none;background-color:var(--wp--preset--color--neutral-20)}
/*# sourceURL=https://neo4j.com/wp-content/themes/neo4jweb/assets/css/blocks/core/separator.css */
</style>
</head>

<body class="wp-singular post-template-default single single-post postid-385564 single-format-standard wp-embed-responsive wp-theme-neo4jweb is_v1_build tribe-no-js has-gutenberg-blocks">
  <a class="show-on-focus skip-link" href="#skip-to-content" title="Skip to content">Skip to content</a>
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WK23PSS" height="0" width="0"
      style="display:none;visibility:hidden"></iframe></noscript>
  
    <div data-c="header mini banner">
    <div data-l="mini banner neo4j5" style="text-decoration: none;">
      <div id="callout-banner" style="background: #181414; color: #fff; padding: .3em;">
        <div class="row text-center">
          <div class="columns">
            <p style="font-size: 16px;font-weight: 600;margin-bottom:0;padding:0.5rem; color: #fff;">
              NODES AI: Online Conference for Graph + AI - April 15, 2026 | <a style="color: #fff; text-decoration: underline;"href="https://neo4j.com/nodes-ai">Save the Date</a></p>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <style>
  .n-contact-us-menu a {
    font-weight: 700;
    color: #0A6190;
    line-height: 1;
    padding: 0.85em 2em;
  }

  .n-contact-us-menu a:hover {
    color: #014063; 
  }

  li .dropdown.absolute.top-full {
    top: 100%;
    width: 100%;
    left: 0 !important;
    position: fixed;
    border-radius: 0;
    background: white;
  }

</style>

<div data-c="mobile main navigation" class="sticky hide-for-large z-40" style="height: 70px; top: 0" id="main-navigation-wrapper">
  <div class="title-bar justify-between px-4 py-2 hide-for-large sticky w-full top-0 z-10 shadow-sm"
    style="height: 70px; top: 0">
    <a href="/" aria-label="Neo4j Home Page">
      <img height="34px" width="104px" src="https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg" alt="The Neo4j Graph Platform – The #1 Platform for Connected Data" role="img" aria-hidden="true" />
    </a>
    <button type="button" aria-controls="toggle-neo4j-mobile-menu-container" aria-expanded="false" data-toggle="toggle-neo4j-mobile-menu-container"
      class="m-0 mobile-menu-toggle-button inline-block">
      <span class="sr-only">Menu</span>
      <span class="n-icon n-icon-navigation-menu n-icon-lg"></span>
    </button>
  </div>
</div>


<!-- Height is set to 70px to work well with secondary menu that stay fixed after scroll on pages like /product -->


<div class="off-canvas position-left" data-off-canvas id="toggle-neo4j-mobile-menu-container">
  <div class="title-bar">
    <img height="34px" width="104px"
      src="https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg" alt="Neo4j logo" />
    <button class="search-button cursor-pointer p-4 rounded-none flex items-center text-sm" style="line-height:0;margin-left: auto;margin-right: 0.5rem;" aria-controls="neo4j-algolia-search-v2" aria-expanded="false">
      <span class="show-for-sr">Search</span>
      <span class="n-icon n-icon-search mr-2"></span>
    </button>
    <button type="button" class="m-0 mobile-menu-toggle-button inline-block"
      data-toggle="toggle-neo4j-mobile-menu-container">
      <span class="sr-only">Close Menu</span>
      <span class="n-icon n-icon-close n-icon-size-lg"></span>
    </button>
  </div>
  <div class="hide-for-large grid-container" id="mobile-menu">
    
<ul class="vertical menu drilldown" data-drilldown data-auto-height="true" data-animate-height="true">
  <li>
    <a class="drilldown-submenu-heading" href="#">Products</a>
    <ul class="menu vertical nested" style="padding-bottom: 1px;">
      <li><span class="submenu-list-heading h6">GRAPH DATABASE</span></li>
      



<li class="menu-item-wrapper ">
  <a href="/product/auradb/"
    data-l="Neo4j AuraDB"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j AuraDB    </span>
    <span class="menu-item-description">Fully managed graph database as a service</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/product/neo4j-graph-database/"
    data-l="Neo4j Graph Database"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Graph Database    </span>
    <span class="menu-item-description">Self managed, deploy anywhere graph database</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>


      <li><span class="submenu-list-heading h6">GRAPH ANALYTICS</span></li>

      



<li class="menu-item-wrapper ">
  <a href="/product/aura-graph-analytics/"
    data-l="Neo4j Aura Graph Analytics "  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Aura Graph Analytics     </span>
    <span class="menu-item-description">Fully managed graph analytics as a service</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/product/graph-data-science/"
    data-l="Neo4j Graph Data Science"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Graph Data Science    </span>
    <span class="menu-item-description">Self managed graph algorithms and ML modeling</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>


      <li><span class="submenu-list-heading h6">GRAPH TOOLS</span></li>

      



<li class="menu-item-wrapper ">
  <a href="/product/fleet-manager/"
    data-l="Neo4j Fleet Manager"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Fleet Manager    </span>
    <span class="menu-item-description">A single control plane to manage all your DB instances</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/product/bloom/"
    data-l="Neo4j Bloom"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Bloom    </span>
    <span class="menu-item-description">Easy graph visualization and exploration</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/product/cypher-graph-query-language/"
    data-l="Cypher Query Language"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Cypher Query Language    </span>
    <span class="menu-item-description">Declarative graph query language, created by Neo4j</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/product/graphql-library/"
    data-l="Neo4j GraphQL"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j GraphQL    </span>
    <span class="menu-item-description">Low-code, open-source API library</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>


      <li><span class="submenu-list-heading h6">PARTNER SOLUTIONS</span></li>
      



<li class="menu-item-wrapper ">
  <a href="/neo4j-graph-analytics-snowflake/"
    data-l="Neo4j Graph Analytics for Snowflake"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Graph Analytics for Snowflake    </span>
    <span class="menu-item-description">Fully managed graph analytics within Snowflake AI Data Cloud</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/neo4j-graph-intelligence-microsoft-fabric/"
    data-l="Neo4j Graph Intelligence for Microsoft Fabric"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Graph Intelligence for Microsoft Fabric    </span>
    <span class="menu-item-description">Fully managed graph database and analytics integrated in Fabric</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      
    </ul>
  </li>
  <li>
    <a class="drilldown-submenu-heading" href="#">Use Cases</a>
    <ul class="menu vertical nested" style="padding-bottom: 1px;">
      



<li class="menu-item-wrapper ">
  <a href="/use-cases/ai-systems/"
    data-l="AI Systems"  class="menu-dropdown-item">
    <span class="menu-item-title">
      AI Systems    </span>
    <span class="menu-item-description">Back your LLMs with a knowledge graph for better business AI</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/use-cases/"
    data-l="Industries and Use Cases"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Industries and Use Cases    </span>
    <span class="menu-item-description">Fraud detection, knowledge graphs, financial services, and more</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/customer-stories/"
    data-l="Customer Success Stories"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Customer Success Stories    </span>
    <span class="menu-item-description">Case studies, customer videos, proof points, and more</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

    </ul>
  </li>
  <li>
    <a class="drilldown-submenu-heading" href="#">Developers</a>
    <ul class="menu vertical nested" style="padding-bottom: 1px;">
      



<li class="menu-item-wrapper ">
  <a href="/developer/"
    data-l="Developer Center"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Developer Center    </span>
    <span class="menu-item-description">Best practices, guides, tutorials, and downloads</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="https://graphacademy.neo4j.com/"
    data-l="GraphAcademy" target="_blank" rel="noopener"rel="noopener" class="menu-dropdown-item">
    <span class="menu-item-title">
      GraphAcademy<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Free online courses and certifications. Join the 100K+ Neo4j experts.</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      <li><span class="submenu-list-heading h6">DEVELOPERS</span></li>
      



<li class="menu-item-wrapper ">
  <a href="/deployment-center/"
    data-l="Deployment Center"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Deployment Center    </span>
    <span class="menu-item-description">Deploy Neo4j on any cloud or architecture</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/docs/"
    data-l="Documentation"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Documentation<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Manuals for Neo4j products, Cypher, and drivers</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/blog/developer/"
    data-l="Developer Blog"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Developer Blog    </span>
    <span class="menu-item-description">Deep dives into more technical Neo4j topics</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="https://community.neo4j.com/"
    data-l="Community" target="_blank" rel="noopener"rel="noopener" class="menu-dropdown-item">
    <span class="menu-item-title">
      Community    </span>
    <span class="menu-item-description">A global forum for online discussion</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>


      <li><span class="submenu-list-heading h6">DATA SCIENTISTS</span></li>
      
      



<li class="menu-item-wrapper ">
  <a href="/docs/graph-data-science/current/"
    data-l="Data Science Documentation"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Data Science Documentation<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Manuals for the Graph Data Science library</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/product/graph-data-science/"
    data-l="Graph Data Science Home"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Graph Data Science Home    </span>
    <span class="menu-item-description">Learn what Neo4j offers for data science</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/graph-data-science-software/"
    data-l="Get Started With Graph Data Science"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Get Started With Graph Data Science    </span>
    <span class="menu-item-description">Download or get started in Sandbox today</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/"
    data-l="Data Science Community" target="_blank" rel="noopener"rel="noopener" class="menu-dropdown-item">
    <span class="menu-item-title">
      Data Science Community    </span>
    <span class="menu-item-description">A global forum for data-driven professionals</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

    </ul>
  </li>
  <li><a class="drilldown-submenu-heading" href="/use-cases/ai-systems/">AI Systems</a></li>
  <li>
    <a class="drilldown-submenu-heading" href="#">Learn</a>
    <ul class="menu vertical nested" style="padding-bottom: 1px;">
      <li><span class="submenu-list-heading h6">LEARN</span></li>
      



<li class="menu-item-wrapper ">
  <a href="/docs/"
    data-l="Documentation"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Documentation<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Manuals for Neo4j products, Cypher, and drivers</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="https://graphacademy.neo4j.com/"
    data-l="GraphAcademy"  class="menu-dropdown-item">
    <span class="menu-item-title">
      GraphAcademy<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Free online courses and certifications</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/resources/"
    data-l="Resource Library"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Resource Library    </span>
    <span class="menu-item-description">White papers, datasheets, and more</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/customer-stories/"
    data-l="Customer Success Stories"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Customer Success Stories    </span>
    <span class="menu-item-description">Case studies, customer videos, proof points, and more</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>


      <li><span class="submenu-list-heading h6">CONNECT</span></li>

      



<li class="menu-item-wrapper ">
  <a href="/events/"
    data-l="Neo4j Events Hub"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Events Hub<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240402072514/Icon-Events.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Live and on-demand events, training, webinars, and demos</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/blog/"
    data-l="Neo4j Blog"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Blog    </span>
    <span class="menu-item-description">Announcements, guides, and best practices</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

			



<li class="menu-item-wrapper ">
  <a href="/videos/"
    data-l="Neo4j Video Hub"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Video Hub    </span>
    <span class="menu-item-description">Covering graph databases, data science, analytics & AI</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>


      <li><span class="submenu-list-heading h6">FEATURED EVENTS</span></li>

      



<li class="menu-item-wrapper ">
  <a href="/events/get-to-know-graph/"
    data-l="Get to Know Graph Webinars"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Get to Know Graph Webinars    </span>
    <span class="menu-item-description">Start your graph journey with these 30-minute introductory webinars</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/nodes-2025/"
    data-l="NODES 2025"  class="menu-dropdown-item">
    <span class="menu-item-title">
      NODES 2025    </span>
    <span class="menu-item-description">The biggest graph community gathering dedicated to graph-powered apps, knowledge, and AI!</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

    </ul>
  </li>
  <li><a class="drilldown-submenu-heading" href="/pricing/">Pricing</a></li>

  <!-- Quick Links -->
  <li class="mt-6 ml-4"><span class="submenu-list-heading h6" style="padding-left:0;">QUICK LINKS</span></li>
  
  <!-- partners -->
  <li class="mobile-quicklinks">
    <a class="drilldown-submenu-heading" href="#">Partners</a>
    <ul class="menu vertical nested" style="padding-bottom: 1px;">
      



<li class="menu-item-wrapper ">
  <a href="/partners/directory/"
    data-l="Find a Partner"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Find a Partner    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/partners/neo4j-partner-program/"
    data-l="Become a Partner"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Become a Partner    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/partners/solution-partners/"
    data-l="Solution Partners"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Solution Partners    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/partners/oem-partners/"
    data-l="OEM Partners"  class="menu-dropdown-item">
    <span class="menu-item-title">
      OEM Partners    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/partners/technology-partners/"
    data-l="Technology Partners"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Technology Partners    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="https://neo4j.my.site.com/Neo4jPartnerCommunity"
    data-l="Partner Portal Login"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Partner Portal Login    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

    </ul>
  </li>

  <!-- company -->
  <li class="mobile-quicklinks">
    <a class="drilldown-submenu-heading" href="#">Company</a>
    <ul class="menu vertical nested" style="padding-bottom: 1px;">
      



<li class="menu-item-wrapper ">
  <a href="/company/"
    data-l="About Us"  class="menu-dropdown-item">
    <span class="menu-item-title">
      About Us    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/newsroom/"
    data-l="Newsroom"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Newsroom    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/awards/"
    data-l="Awards and Honors"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Awards and Honors    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/graphs4good/"
    data-l="Graphs4Good"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Graphs4Good    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/careers/"
    data-l="Careers"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Careers    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/culture/"
    data-l="Culture"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Culture    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

      



<li class="menu-item-wrapper ">
  <a href="/leadership/"
    data-l="Leadership"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Leadership    </span>
      </a>
  <!-- Maybe flyout submenu -->
  
</li>

    </ul>
  </li>

  <!-- support -->
  <li class="mobile-quicklinks"><a class="drilldown-submenu-heading" href="https://support.neo4j.com/s/">Support</a></li>
  
  <!-- aura Login -->
  <li class="mobile-quicklinks"><a class="drilldown-submenu-heading" href="https://console.neo4j.io/">Aura Login</a></li>
</ul>
<div class="cell mt-12">
  <div style="display: flex;flex-direction: column;" class="cta-buttons">
    <a href="/product/auradb/?ref=nav-get-started-cta">Get Started</a>
    <a href="/contact-us/">Contact Us</a>
  </div>
</div>
  </div>
</div>
<div id="menu-container-main" class="show-for-large bg-white shadow-sm sticky z-50" data-c="main navigation">
  <div id="eyebrow-menu-container">
    <div id="eyebrow-menu" class="grid-container vertical-flex justify-center">
      <div class="top-bar desktop-top-menu">
        <div class="top-bar-right">
          
<ul class="items-center z-20 flex m-0 mt-2" id="eyebrow-menu-items" role="menu">
      <li id="AuraLogin" class="m-0 mr-6 group relative" role="menuitem">
    <a href='https://console.neo4j.io/' class='text-xs font-normal text-neutral-60 hover:text-black p-0 cursor-pointer'>Aura Login</a>      </li>
      <li id="Partners" class="m-0 mr-6 group relative" role="menuitem">
    <a href='/partners/' class='text-xs font-normal text-neutral-60 hover:text-black p-0 cursor-pointer'>Partners</a><button class='dropdown-toggle' aria-expanded='false' type='button'><span class='show-for-sr'>Partners: submenu</span><i class='n-icon n-icon-chevron-down n-icon-sm ml-1' aria-hidden='true'></i></button>        <div class="dropdown absolute pt-2 z-50" style="left: -24px">
      <ul class="py-2 border-none border-radius shadow-md dropdown-submenu rounded-md" role="menubar">
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/partners/directory/"
            data-l="Find a Partner"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Find a Partner</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/partners/neo4j-partner-program/"
            data-l="Become a Partner"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Become a Partner</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/partners/solution-partners/"
            data-l="Solution Partners"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Solution Partners</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/partners/oem-partners/"
            data-l="OEM Partners"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">OEM Partners</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/partners/technology-partners/"
            data-l="Technology Partners"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Technology Partners</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="https://neo4j.my.site.com/Neo4jPartnerCommunity"
            data-l="Partner Portal Login" target="_blank"rel="noopener" class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Partner Portal Login</span>
          </a>
        </li>
              </ul>
    </div>
      </li>
      <li id="Company" class="m-0 mr-6 group relative" role="menuitem">
    <span class='text-xs font-normal text-neutral-60 hover:text-black p-0 cursor-default'>Company</span><button class='dropdown-toggle' aria-expanded='false' type='button'><span class='show-for-sr'>Company: submenu</span><i class='n-icon n-icon-chevron-down n-icon-sm ml-1' aria-hidden='true'></i></button>        <div class="dropdown absolute pt-2 z-50" style="left: -24px">
      <ul class="py-2 border-none border-radius shadow-md dropdown-submenu rounded-md" role="menubar">
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/company/"
            data-l="About Us"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">About Us</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/newsroom/"
            data-l="Newsroom"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Newsroom</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/awards/"
            data-l="Awards and Honors"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Awards and Honors</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/graphs4good/"
            data-l="Graphs4Good"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Graphs4Good</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/careers/"
            data-l="Careers"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Careers</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/culture/"
            data-l="Culture"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Culture</span>
          </a>
        </li>
                <li class="hover:bg-neutral-20 m-0 relative" role="menuitem">
          <a href="/leadership/"
            data-l="Leadership"  class="menu-dropdown-item  px-4 py-2 block">
            <span class="block whitespace-nowrap text-neutral-60 text-xs">Leadership</span>
          </a>
        </li>
              </ul>
    </div>
      </li>
      <li id="Support" class="m-0 mr-6 group relative" role="menuitem">
    <a href='https://support.neo4j.com/s/' class='text-xs font-normal text-neutral-60 hover:text-black p-0 cursor-pointer'>Support</a>      </li>
  
  <li id="SearchButton" class="horizontal-flex text-neutral-60 search-button cursor-pointer hover:bg-neutral-20 rounded p-2 m-0" tabindex="0" role="menuitem" aria-expanded="false" type="button" style="line-height:0">
    <span class='show-for-sr'>Search</span>
    <span class="n-icon n-icon-search"></span>
  </li>
</ul>
        </div>
      </div>
    </div>
  </div>

  <div id="neo4j-main-menu-container" class="bg-white z-10 w-full top-0">
    <div id="neo4j-main-menu" class="grid-container vertical-flex justify-center py-3">
      <div class=" desktop-menu flex items-center">
        <div id="neo4j-main-menu-logo">
          <a class="mr-8" href="/" aria-label="Neo4j Home Page">
            <img height="34px" width="104px"
              src="https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg" alt="Neo4j logo" role="img" aria-hidden="true" />
          </a>
        </div>
        <div class="flex items-center w-full ml-4">
          <div class="w-full h-full">
            
<ul id="neo4j-main-menu-items" class="items-center z-50 flex m-0 h-full" role="menu">  
  <li id='n-products-menu' class='group relative m-0 flex items-center self-stretch n-products-menu' role='menuitem'><span class='text-neutral-60 hover:text-black px-4 text-sm font-normal cursor-default'>Products</span><button class='dropdown-toggle -ml-4 mr-4' aria-expanded='false' type='button'><span class='show-for-sr'>Products: submenu</span><i class='n-icon n-icon-chevron-down n-icon-sm mx-1' aria-hidden='true'></i></button>


<style>
    #neo4j-main-menu-items .product-item-li {
      background: linear-gradient(to left, #f5f6f6, #f5f6f6 43.4%, #fff 1rem, #fff 100%) !important;
    }

    #neo4j-main-menu-items .product-right-col {
      margin-top: -2rem;
      padding-top: 2rem;
      background: #f5f6f6;
      margin-bottom: -2rem;
      margin-left: -1rem;
      padding-left: 1rem;
    }

</style>

<div class="dropdown absolute top-full product-item-li" style="top: 100%;">
  <div class="border-none border-radius menu-dropdown-shadow bg-white text-left m-0 dropdown-submenu rounded-md product-menu-bg">
    <div class="flex flex-row gap-x-4">
      <div class="flex flex-col w-full grid-container">        
          <div class="flex flex-row grid-x">
            <!-- col left -->
            <div class="medium-7 pr-6">
              <div class="grid-x" style="padding-left: 0.5rem;">                  
                  <!-- Graph Tools - Col Left -->
                  <div class="cell small-6"> 
                    <span class="main-menu-submenu-header px-4 block" style="color: #5E636A;">GRAPH DATABASE</span>                   
                    <ul style="margin-left: 0;">
                      

  <style>
  #neo4j-main-menu-items .menu-item-wrapper.products-menu .menu-dropdown-item {
    white-space: normal;
    gap: 8px;
    min-width: auto;
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu {
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu .menu-item-title {
    color: #0A6190;
  }

  #menu-container-main .menu-item-icon {
    min-width: 50px !important;
    align-self: center;
  }
  #menu-container-main .partner-solutions-panel .menu-item-icon img {
    max-width: 45px !important;
  }

  </style>

  <li class="menu-item-wrapper products-menu ">
    

      <a href="/product/auradb/"
        data-l="Neo4j AuraDB"  class="menu-dropdown-item">
        <div class="menu-item-icon">
          <img src="https://dist.neo4j.com/wp-content/uploads/20250505083953/neo4j-icon-adb.svg" alt="menu item icon" loading="lazy">
        </div>
        <div>
          <span class="menu-item-title">
            Neo4j AuraDB          </span>
          <span class="menu-item-description">Fully managed graph database as a service</span>          </div>
      </a>
    
    <!-- Maybe flyout submenu -->
    
  </li>
                      

  <style>
  #neo4j-main-menu-items .menu-item-wrapper.products-menu .menu-dropdown-item {
    white-space: normal;
    gap: 8px;
    min-width: auto;
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu {
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu .menu-item-title {
    color: #0A6190;
  }

  #menu-container-main .menu-item-icon {
    min-width: 50px !important;
    align-self: center;
  }
  #menu-container-main .partner-solutions-panel .menu-item-icon img {
    max-width: 45px !important;
  }

  </style>

  <li class="menu-item-wrapper products-menu ">
    

      <a href="/product/neo4j-graph-database/"
        data-l="Neo4j Graph Database"  class="menu-dropdown-item">
        <div class="menu-item-icon">
          <img src="https://dist.neo4j.com/wp-content/uploads/20250505083955/neo4j-icon-gdb.svg" alt="menu item icon" loading="lazy">
        </div>
        <div>
          <span class="menu-item-title">
            Neo4j Graph Database          </span>
          <span class="menu-item-description">Self managed, deploy anywhere graph database</span>          </div>
      </a>
    
    <!-- Maybe flyout submenu -->
    
  </li>
                    </ul>
                  </div>
                  <!-- Graph Tools - Col Right -->
                  <div class="cell small-6">
                    <span class="main-menu-submenu-header px-4 block">GRAPH ANALYTICS</span>
                    <ul style="margin-left: 0;">
                      

  <style>
  #neo4j-main-menu-items .menu-item-wrapper.products-menu .menu-dropdown-item {
    white-space: normal;
    gap: 8px;
    min-width: auto;
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu {
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu .menu-item-title {
    color: #0A6190;
  }

  #menu-container-main .menu-item-icon {
    min-width: 50px !important;
    align-self: center;
  }
  #menu-container-main .partner-solutions-panel .menu-item-icon img {
    max-width: 45px !important;
  }

  </style>

  <li class="menu-item-wrapper products-menu ">
    

      <a href="/product/aura-graph-analytics/"
        data-l="Neo4j Aura Graph Analytics "  class="menu-dropdown-item">
        <div class="menu-item-icon">
          <img src="https://dist.neo4j.com/wp-content/uploads/20250505083954/neo4j-icon-ga.svg" alt="menu item icon" loading="lazy">
        </div>
        <div>
          <span class="menu-item-title">
            Neo4j Aura Graph Analytics           </span>
          <span class="menu-item-description">Fully managed graph analytics as a service</span>          </div>
      </a>
    
    <!-- Maybe flyout submenu -->
    
  </li>
  
                      

  <style>
  #neo4j-main-menu-items .menu-item-wrapper.products-menu .menu-dropdown-item {
    white-space: normal;
    gap: 8px;
    min-width: auto;
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu {
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu .menu-item-title {
    color: #0A6190;
  }

  #menu-container-main .menu-item-icon {
    min-width: 50px !important;
    align-self: center;
  }
  #menu-container-main .partner-solutions-panel .menu-item-icon img {
    max-width: 45px !important;
  }

  </style>

  <li class="menu-item-wrapper products-menu ">
    

      <a href="/product/graph-data-science/"
        data-l="Neo4j Graph Data Science"  class="menu-dropdown-item">
        <div class="menu-item-icon">
          <img src="https://dist.neo4j.com/wp-content/uploads/20250505083957/neo4j-icon-gds.svg" alt="menu item icon" loading="lazy">
        </div>
        <div>
          <span class="menu-item-title">
            Neo4j Graph Data Science          </span>
          <span class="menu-item-description">Self managed graph algorithms and ML modeling</span>          </div>
      </a>
    
    <!-- Maybe flyout submenu -->
    
  </li>
                    </ul>
                  </div>
                </div>
                <div class="grid-x pt-2 partner-solutions-panel" style="padding-left: 0.5rem;">
                  <!-- Partner Solutions - Col Left -->
                  <div class="cell">
                    <span class="main-menu-submenu-header px-4 flex items-center" style="color: #5E636A;">
                        PARTNER SOLUTIONS
                        <span class="main-menu-submenu-header-divider w-full flex-1 ml-3 border-t" style="border-color:#BBBEC3"></span>
                    </span>
                  </div>           
                  <div class="cell small-6"> 
                    <ul style="margin-left: 0;">
                      

  <style>
  #neo4j-main-menu-items .menu-item-wrapper.products-menu .menu-dropdown-item {
    white-space: normal;
    gap: 8px;
    min-width: auto;
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu {
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu .menu-item-title {
    color: #0A6190;
  }

  #menu-container-main .menu-item-icon {
    min-width: 50px !important;
    align-self: center;
  }
  #menu-container-main .partner-solutions-panel .menu-item-icon img {
    max-width: 45px !important;
  }

  </style>

  <li class="menu-item-wrapper products-menu ">
    

      <a href="/neo4j-graph-intelligence-microsoft-fabric/"
        data-l="Neo4j Graph Intelligence for Microsoft Fabric"  class="menu-dropdown-item">
        <div class="menu-item-icon">
          <img src="https://dist.neo4j.com/wp-content/uploads/20251211172122/neo4j-icon-gi-microsoft-fabric.svg" alt="menu item icon" loading="lazy">
        </div>
        <div>
          <span class="menu-item-title">
            Neo4j Graph Intelligence for Microsoft Fabric          </span>
          <span class="menu-item-description">Fully managed graph database and analytics integrated in Fabric</span>          </div>
      </a>
    
    <!-- Maybe flyout submenu -->
    
  </li>
                    </ul>
                  </div>
                  <!-- Partner Solutions - Col Right -->
                  <div class="cell small-6">
                    <ul style="margin-left: 0;">
                      

  <style>
  #neo4j-main-menu-items .menu-item-wrapper.products-menu .menu-dropdown-item {
    white-space: normal;
    gap: 8px;
    min-width: auto;
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu {
    display: flex;
  }

  #menu-container-main #neo4j-main-menu li.products-menu .menu-item-title {
    color: #0A6190;
  }

  #menu-container-main .menu-item-icon {
    min-width: 50px !important;
    align-self: center;
  }
  #menu-container-main .partner-solutions-panel .menu-item-icon img {
    max-width: 45px !important;
  }

  </style>

  <li class="menu-item-wrapper products-menu ">
    

      <a href="/neo4j-graph-analytics-snowflake/"
        data-l="Neo4j Graph Analytics for Snowflake"  class="menu-dropdown-item">
        <div class="menu-item-icon">
          <img src="https://dist.neo4j.com/wp-content/uploads/20251212134250/neo4j-icon-ga-snowflake-1.svg" alt="menu item icon" loading="lazy">
        </div>
        <div>
          <span class="menu-item-title">
            Neo4j Graph Analytics for Snowflake          </span>
          <span class="menu-item-description">Fully managed graph analytics within Snowflake AI Data Cloud</span>          </div>
      </a>
    
    <!-- Maybe flyout submenu -->
    
  </li>
  
                    </ul>
                  </div>
                </div>
            </div>

            <!-- col right -->
            <div class="medium-5 product-right-col">
                <span class="main-menu-submenu-header px-6 block" style="color: #5E636A;">Graph Tools</span>
                <div class="grid-x" style="padding-left: 0.5rem;">                  
                  <!-- Graph Tools - Col Left -->
                  <div class="cell small-6">                    
                    <ul style="margin-left: 0;">
                      



<li class="menu-item-wrapper ">
  <a href="/product/fleet-manager/"
    data-l="Neo4j Fleet Manager"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Fleet Manager    </span>
    <span class="menu-item-description">A single control plane to manage all your DB instances</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="/product/bloom/"
    data-l="Neo4j Bloom"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Bloom    </span>
    <span class="menu-item-description">Easy graph visualization and exploration</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                    </ul>
                  </div>
                  <!-- Graph Tools - Col Right -->
                  <div class="cell small-6">
                    <ul style="margin-left: 0;">
                      



<li class="menu-item-wrapper ">
  <a href="/product/cypher-graph-query-language/"
    data-l="Cypher Query Language"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Cypher Query Language    </span>
    <span class="menu-item-description">Declarative graph query language, created by Neo4j</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

  
                      



<li class="menu-item-wrapper ">
  <a href="/product/graphql-library/"
    data-l="Neo4j GraphQL"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j GraphQL    </span>
    <span class="menu-item-description">Low-code, open-source API library</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                    </ul>
                  </div>
                </div>
            </div>
          </div>
      </div>
    </div>
  </div>
</div>
</li><li id='n-use-cases-menu' class='group relative m-0 flex items-center self-stretch n-use-cases-menu' role='menuitem'><span class='text-neutral-60 hover:text-black px-4 text-sm font-normal cursor-default'>Use Cases</span><button class='dropdown-toggle -ml-4 mr-4' aria-expanded='false' type='button'><span class='show-for-sr'>Use Cases: submenu</span><i class='n-icon n-icon-chevron-down n-icon-sm mx-1' aria-hidden='true'></i></button>
<div class="dropdown absolute top-full use-cases-item-li" style="top: 100%;">
  <div class="border-none border-radius menu-dropdown-shadow bg-white text-left m-0 dropdown-submenu rounded-md use-cases-menu-bg">
    <div class="flex flex-row gap-x-4">
      <div class="flex flex-col w-full grid-container">        
          <div class="flex flex-row grid-x">
            <div class="cell small-12">
              <div class=""> 
                <ul class="grid-x" style="margin-left: 0;">
                  <li class="cell small-4">
                    <a href="/use-cases/ai-systems/">
                      <div class="product-card-container industries-card-container grid-container py-2 mr-6">
                        <img class="art-industries"
                             src="https://dist.neo4j.com/wp-content/uploads/20240329130329/genai.svg" alt="" loading="lazy" />
                        <p style="font-size:14px;font-weight:600;margin-bottom:5px;">AI Systems</p>
                        <p class="" style="font-size:14px;z-index: 1;position: relative;">Back your LLMs with a Knowledge
                          Graph for better business AI</p>
                        <p class='industries-card-container__cta'>Learn More <span class="right-chevron-white"></span></p>
                      </div>
                    </a>
                  </li>
                  <li class="cell small-4">
                    <a href="/use-cases/">
                      <div
                        class="industries-card-container industries-card-container-right grid-container py-2 mr-6 card-art--industries">
                        <p style="font-size:14px;font-weight:600;margin-bottom:5px;">Industries and Use Cases</p>
                        <p class="" style="font-size:14px;z-index: 1;position: relative;">Fraud detection, knowledge
                          graphs, financial services, and more</p>
                        <p class='industries-card-container__cta'>All Use Cases <span class="right-chevron"></span></p>
                      </div>
                    </a>
                  </li>
                  <li class="cell small-4">
                    <a href="/customer-stories/">
                      <div
                        class="industries-card-container industries-card-container-right grid-container py-2 card-art--customer-stories">
                        <p style="font-size:14px;font-weight:600;margin-bottom:5px;">Customer Success
                          Stories</p>
                        <p class="pr-12" style="font-size:14px;z-index: 1;position: relative;">Case studies, customer videos,
                          proof points, and more</p>
                        <p class='industries-card-container__cta'>All Customer Stories <span class="right-chevron"></span></p>
                      </div>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
      </div>
    </div>
  </div>
</div></li><li id='n-developers-menu' class='group relative m-0 flex items-center self-stretch n-developers-menu' role='menuitem'><span class='text-neutral-60 hover:text-black px-4 text-sm font-normal cursor-default'>Developers</span><button class='dropdown-toggle -ml-4 mr-4' aria-expanded='false' type='button'><span class='show-for-sr'>Developers: submenu</span><i class='n-icon n-icon-chevron-down n-icon-sm mx-1' aria-hidden='true'></i></button>
<div class="dropdown absolute top-full use-cases-item-li" style="top: 100%;">
  <div class="border-none border-radius menu-dropdown-shadow bg-white text-left m-0 dropdown-submenu rounded-md use-cases-menu-bg">
    <div class="flex flex-row gap-x-4">
      <div class="flex flex-col w-full grid-container">
          <div class="flex flex-row grid-x">
            <!-- col left -->
            <div class="cell small-8">
              <div class="">
                <ul class="grid-x" style="margin-left: 0;">
                  <li class="cell mr-6" style="width:41.66667%">
                    <a href="/developer/">
                      <div class="developers-card-container developers-card-container-top grid-container py-2 ml-2">
                        <p style="font-size:14px;font-weight:600;margin-bottom:0;">Developer Center</p>
                        <p class="" style="font-size:14px;z-index: 1;position: relative;">Best practices, guides, tutorials, and downloads</p>
                        <p>Learn More <span class="right-chevron"></span></p>
                      </div>
                    </a>
                    <a target="_blank" href="https://graphacademy.neo4j.com/">
                      <div class="developers-card-container developers-card-container-bottom grid-container py-2 ml-2">
                        <p style="font-size:14px;font-weight:600;margin-bottom:0;">GraphAcademy</p>
                        <p class="" style="font-size:14px;z-index: 1;position: relative;">Free online courses and certifications. Join the 100K+ Neo4j experts.</p>
                        <p>Learn More <span class="right-chevron"></span></p>
                      </div>
                    </a>
                  </li>
                  <li class="cell small-6">
                    <span class="main-menu-submenu-header px-4 block">Developers</span>
                    <ul style="margin-left: 0;">
                    



<li class="menu-item-wrapper ">
  <a href="/deployment-center/"
    data-l="Deployment Center"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Deployment Center    </span>
    <span class="menu-item-description">Deploy Neo4j on any cloud or architecture</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="/docs/"
    data-l="Documentation"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Documentation<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Manuals for Neo4j products, Cypher, and drivers</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="/blog/developer/"
    data-l="Developer Blog"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Developer Blog    </span>
    <span class="menu-item-description">Deep dives into more technical Neo4j topics</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="https://community.neo4j.com/"
    data-l="Community" target="_blank" rel="noopener"rel="noopener" class="menu-dropdown-item">
    <span class="menu-item-title">
      Community    </span>
    <span class="menu-item-description">A global forum for online discussion</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                    </ul>
                  </li>
                </ul>
              </div>
            </div>

            <!-- col right -->
            <div class="cell small-4 developer-menu-right-column">
              <span class="main-menu-submenu-header px-6 block">DATA SCIENTISTS</span>
                <div class="grid-x" style="padding-left: 0.5rem;">
                  <div class="cell small-12">
                    <ul style="margin-left: 0;">
                      



<li class="menu-item-wrapper ">
  <a href="/docs/graph-data-science/current/"
    data-l="Data Science Documentation"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Data Science Documentation<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Manuals for the Graph Data Science library</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="/product/graph-data-science/"
    data-l="Graph Data Science Home"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Graph Data Science Home    </span>
    <span class="menu-item-description">Learn what Neo4j offers for data science</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="/graph-data-science-software/"
    data-l="Get Started With Graph Data Science"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Get Started With Graph Data Science    </span>
    <span class="menu-item-description">Download or get started in Sandbox today</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/"
    data-l="Data Science Community" target="_blank" rel="noopener"rel="noopener" class="menu-dropdown-item">
    <span class="menu-item-title">
      Data Science Community    </span>
    <span class="menu-item-description">A global forum for data-driven professionals</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                    </ul>
                  </div>
                </div>
            </div>
          </div>
      </div>
    </div>
  </div>
</div></li><li id='n-ai-systems-menu' class='group relative m-0 flex items-center self-stretch n-ai-systems-menu' role='menuitem'><a data-l='AI Systems' href='/use-cases/ai-systems/' class='text-neutral-60 hover:text-black px-4 text-sm font-normal cursor-pointer'>AI Systems</a></li><li id='n-learn-menu' class='group relative m-0 flex items-center self-stretch n-learn-menu' role='menuitem'><span class='text-neutral-60 hover:text-black px-4 text-sm font-normal cursor-default'>Learn</span><button class='dropdown-toggle -ml-4 mr-4' aria-expanded='false' type='button'><span class='show-for-sr'>Learn: submenu</span><i class='n-icon n-icon-chevron-down n-icon-sm mx-1' aria-hidden='true'></i></button>
<div class="dropdown absolute top-full use-cases-item-li" style="top: 100%;">
  <div class="border-none border-radius menu-dropdown-shadow bg-white text-left m-0 dropdown-submenu rounded-md use-cases-menu-bg">
    <div class="flex flex-row gap-x-4">
      <div class="flex flex-col w-full grid-container">
          <div class="flex flex-row grid-x grid-margin-x">
            <!-- col left -->
            <div class="cell small-4" style="border-right: 1px solid #BBBEC3;">
              <span class="main-menu-submenu-header px-6 block">LEARN</span>
                <div class="grid-x" style="padding-left: 0.5rem;">
                  <div class="cell small-12">
                    <ul style="margin-left: 0;">
                      



<li class="menu-item-wrapper ">
  <a href="/docs/"
    data-l="Documentation"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Documentation<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Manuals for Neo4j products, Cypher, and drivers</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="https://graphacademy.neo4j.com/"
    data-l="GraphAcademy"  class="menu-dropdown-item">
    <span class="menu-item-title">
      GraphAcademy<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Free online courses and certifications</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="/resources/"
    data-l="Resource Library"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Resource Library    </span>
    <span class="menu-item-description">White papers, datasheets, and more</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="/customer-stories/"
    data-l="Customer Success Stories"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Customer Success Stories    </span>
    <span class="menu-item-description">Case studies, customer videos, proof points, and more</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                    </ul>
                  </div>
                </div>
            </div>

            <!-- col middle -->
            <div class="cell small-4">
              <span class="main-menu-submenu-header px-6 block">CONNECT</span>
                <div class="grid-x" style="padding-left: 0.5rem;">
                  <div class="cell small-12">
                    <ul style="margin-left: 0;">
                      



<li class="menu-item-wrapper ">
  <a href="/events/"
    data-l="Neo4j Events Hub"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Events Hub<img style="vertical-align: bottom;margin-left: 6px;" src="https://dist.neo4j.com/wp-content/uploads/20240402072514/Icon-Events.svg" alt="" aria-hidden="true" width="20" height="20" loading="lazy" />    </span>
    <span class="menu-item-description">Live and on-demand events, training, webinars, and demos</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                      



<li class="menu-item-wrapper ">
  <a href="/blog/"
    data-l="Neo4j Blog"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Blog    </span>
    <span class="menu-item-description">Announcements, guides, and best practices</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

											



<li class="menu-item-wrapper ">
  <a href="/videos/"
    data-l="Neo4j Video Hub"  class="menu-dropdown-item">
    <span class="menu-item-title">
      Neo4j Video Hub    </span>
    <span class="menu-item-description">Covering graph databases, data science, analytics & AI</span>  </a>
  <!-- Maybe flyout submenu -->
  
</li>

                    </ul>
                  </div>
                </div>
            </div>

            <!-- col right -->
            <div class="pl-4 cell small-4 developer-menu-right-column">
              <span class="main-menu-submenu-header px-6 block">FEATURED EVENTS</span>
                <div class="grid-x pt-4" style="padding-left: 0.5rem;">
                  <ul class="cell small-12" style="margin-left: 0;">
                    <li>
                      <a href="/graphsummit/">
                        <div class="featured-events-card-container featured-events-card-container-bottom grid-container py-2 ml-2">
													<img src="https://dist.neo4j.com/wp-content/uploads/20250306090638/graphsummit-logo.svg" width="121" alt="GraphSummit Logo" />
													<p class="h5 font-semibold mt-2 mb-6" style="font-size:18px;z-index: 1;position: relative;color:#fff;line-height: 21.6px;">Graphs + AI: Transform Your Data Into Knowledge</p>
													<span class="graph-summit-learn-more">Learn more</span>
                        </div>
                      </a>
                    </li>
                    <li>
                      <a href="/nodes-ai/" rel="noopener noreferrer">
                        <div class="featured-events-card-container grid-container py-2 pl-4 ml-2 mt-4" style="background-color: #002b43; color: white; background: linear-gradient(270deg, rgba(0, 43, 67, 0) 4.07%, #002B43 75.24%), url(https://dist.neo4j.com/wp-content/uploads/20251118144929/ai-banner-background.svg), linear-gradient(180deg, #002b43 0%, #002b43 100%);background-size: cover;background-position: center right;background-repeat: no-repeat;">
                          <img  width="115" src="https://dist.neo4j.com/wp-content/uploads/20251118144030/Nodes-White-Subhead-Date.svg" alt="Neo4j Nodes AI 2026 logo" loading="lazy" />
                          <p class="h5 font-semibold mt-3 text-white" style="font-size: 20px;">Virtual Conference Dedicated to Graph + AI</p>
													<div style="background-color: #FAFF00; color: #09090A; font-size: 14px; line-height: 20px; display: inline-block; border-radius: 16px; padding: 4px 12px; margin: 10px 0;">Save the Date</div>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
            </div>
          </div>
      </div>
    </div>
  </div>
</div>
</li><li id='n-pricing-menu' class='group relative m-0 flex items-center self-stretch n-pricing-menu' role='menuitem'><a data-l='Pricing' href='/pricing/' class='text-neutral-60 hover:text-black px-4 text-sm font-normal cursor-pointer'>Pricing</a></li><li id='n-contact-us-menu' class='group relative m-0 flex items-center self-stretch n-contact-us-menu' role='menuitem'><a data-l='Contact Us' href='/contact-us/' class='text-neutral-60 hover:text-black px-4 text-sm font-normal cursor-pointer'>Contact Us</a></li><li id='n-get-started-free-menu' class='group relative m-0 flex items-center self-stretch n-get-started-free-menu' role='menuitem'><a data-l='Get Started Free' href='https://console.neo4j.io/' class='text-neutral-60 hover:text-black px-4 text-sm font-normal cursor-pointer'>Get Started Free</a></li>
</ul>          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<style>
.js-warning {
  background-color: red;
  color: white !important;
  text-align: center;
  padding: 10px;
  border: 1px solid white;
  font-size: 1.25rem;
}
</style>
<noscript>
  <h3 class="js-warning">Warning: JavaScript is disabled on your browser. Parts of Neo4j.com will not work properly.
  </h3>
</noscript>
  <div id="skip-to-content"></div>


		<main id="content" role="main">
			<div class='wp-block-blog entry-content has-global-padding is-layout-constrained'>
				
<div class="wp-block-group alignfull neo4j-blog-navigation has-neutral-80-color has-neutral-10-background-color has-text-color has-background has-link-color wp-elements-07f4705aebb498b0c8c2c3d3a0c40035 has-global-padding is-layout-constrained wp-block-group-is-layout-constrained wp-container-2 is-position-sticky" style="border-top-style:none;border-top-width:0px;border-right-style:none;border-right-width:0px;border-bottom-color:var(--wp--preset--color--neutral-20);border-bottom-style:solid;border-bottom-width:1px;border-left-style:none;border-left-width:0px;padding-top:0;padding-bottom:0"><nav class="has-expandable-modal-submenus is-responsive items-justified-center blog-navigation wp-block-navigation is-content-justification-center is-layout-flex wp-container-core-navigation-is-layout-a89b3969 wp-block-navigation-is-layout-flex" aria-label="Blog Navigation" 
		 data-wp-interactive="core/navigation" data-wp-context='{"overlayOpenedBy":{"click":false,"hover":false,"focus":false},"type":"overlay","roleAttribute":"","ariaLabel":"Menu"}'><button aria-haspopup="dialog"  class="wp-block-navigation__responsive-container-open" 
				data-wp-on--click="actions.openMenuOnClick"
				data-wp-on--keydown="actions.handleMenuKeydown"
			>Blog Home <svg width="12" height="8" viewBox="0 0 12 8" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11 1.5L6 6.5L1 1.5" stroke="#4D5157" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
				<div class="wp-block-navigation__responsive-container"  id="modal-1" 
				data-wp-class--has-modal-open="state.isMenuOpen"
				data-wp-class--is-menu-open="state.isMenuOpen"
				data-wp-watch="callbacks.initMenu"
				data-wp-on--keydown="actions.handleMenuKeydown"
				data-wp-on--focusout="actions.handleMenuFocusout"
				tabindex="-1"
			>
					<div class="wp-block-navigation__responsive-close" tabindex="-1">
						<div class="wp-block-navigation__responsive-dialog" 
				data-wp-bind--aria-modal="state.ariaModal"
				data-wp-bind--aria-label="state.ariaLabel"
				data-wp-bind--role="state.roleAttribute"
			>
							<button  class="wp-block-navigation__responsive-container-close" 
				data-wp-on--click="actions.closeMenuOnClick"
			>Close</button>
							<div class="wp-block-navigation__responsive-container-content" 
				data-wp-watch="callbacks.focusFirstElement"
			 id="modal-1-content">
								<ul class="wp-block-navigation__container is-responsive items-justified-center blog-navigation wp-block-navigation"><li class=" wp-block-navigation-item wp-block-navigation-link"><a class="wp-block-navigation-item__content"  href="/blog/"><span class="wp-block-navigation-item__label">Blog Home</span></a></li><li class=" wp-block-navigation-item wp-block-navigation-link"><a class="wp-block-navigation-item__content"  href="/blog/developer/"><span class="wp-block-navigation-item__label">Developer</span></a></li><li class=" wp-block-navigation-item wp-block-navigation-link"><a class="wp-block-navigation-item__content"  href="/blog/genai/"><span class="wp-block-navigation-item__label">GenAI</span></a></li><li class=" wp-block-navigation-item wp-block-navigation-link"><a class="wp-block-navigation-item__content"  href="/blog/news/"><span class="wp-block-navigation-item__label">News</span></a></li></ul>
							</div>
						</div>
					</div>
				</div></nav></div>
				
<div class="wp-block-group alignwide has-global-padding is-layout-constrained wp-block-group-is-layout-constrained" style="margin-top:var(--wp--preset--spacing--60);margin-bottom:var(--wp--preset--spacing--60)">
<div class="wp-block-columns alignwide is-layout-flex wp-container-core-columns-is-layout-a42798d2 wp-block-columns-is-layout-flex" style="border-top-style:none;border-top-width:0px;border-right-style:none;border-right-width:0px;border-bottom-color:var(--wp--preset--color--neutral-20);border-bottom-style:solid;border-bottom-width:2px;border-left-style:none;border-left-width:0px;padding-bottom:var(--wp--preset--spacing--80)">
<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow"><div class="wp-block-neo4j-limited-terms">
		<ul class='wp-block-neo4j-limited-terms__list'>
																		<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-genai'
							   href="https://neo4j.com/blog/genai/">GenAI</a>
											</li>
										</ul>
</div>


<h1 class="is-style-h2 wp-block-post-title">How to Build a GenAI Chatbot From Technical Documents Using Neo4j and Unstructured.io</h1>

	<div class="multiple-contributors wp-block-neo4j-blog-contributors">
		<div class='wp-block-neo4j-blog-contributors__photos'>
							<div class='wp-block-neo4j-blog-contributors__photo'>
											<img src='https://dist.neo4j.com/wp-content/uploads/20250225113404/OLD-Michael-Moore-Headshot-150x150.png'
							 alt='Photo of Michael Moore' width="150"
							 height="150"/>
									</div>
								<div class='wp-block-neo4j-blog-contributors__photo'>
											<img src='https://dist.neo4j.com/wp-content/uploads/20230818092333/morgan-150x150.jpeg'
							 alt='Photo of Morgan Sénéchal' width="150"
							 height="150"/>
									</div>
						</div>
		<div class='wp-block-neo4j-blog-contributors__content'>
							<p>
					<a href='https://neo4j.com/blog/contributor/michael-moore/'>Michael Moore</a>,				</p>
								<p>
					<a href='https://neo4j.com/blog/contributor/morgan-senechal/'>Morgan Sénéchal</a>				</p>
						</div>

	</div>




<div class="wp-block-group has-neutral-55-color has-text-color has-link-color wp-elements-f66778e2b39d390902c89d839b642d8d is-nowrap is-layout-flex wp-container-core-group-is-layout-6c531013 wp-block-group-is-layout-flex"><div class="wp-block-post-date"><time datetime="2025-07-30T08:45:05-07:00">July 30, 2025</time></div>

	<p class="wp-block-neo4j-reading-time">
		6 min read	</p>
</div>
</div>



<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow"><figure style="aspect-ratio:auto;height:300px;" class="wp-block-post-featured-image"><img width="1200" height="627" src="https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io.png" class="attachment-post-thumbnail size-post-thumbnail wp-post-image" alt="" style="width:100%;height:100%;object-fit:contain;" decoding="async" srcset="https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io.png 1200w, https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io-300x157.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io-1024x535.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io-150x78.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io-768x401.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729202935/graphrag-chatbot-neo4j-unstructured-io-600x314.png 600w" sizes="(max-width: 1200px) 100vw, 1200px" /></figure></div>
</div>
</div>



<div class="wp-block-group alignwide has-global-padding is-layout-constrained wp-block-group-is-layout-constrained">
<div class="wp-block-columns alignwide is-layout-flex wp-container-core-columns-is-layout-79d6dacc wp-block-columns-is-layout-flex">
<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow" style="flex-basis:68.85%">

<div class="entry-content wp-block-post-content is-layout-flow wp-block-post-content-is-layout-flow">
<p>A common challenge when building GenAI applications for technical audiences is providing accurate responses that also contain relevant unstructured information, such as charts, diagrams, and tables.</p>



<p>In this blog, we’ll build a simple <a href="https://github.com/graphadvantage/aura-chatbot/tree/images-tables">GenAI chatbot</a> using open-source technical documentation from the energy industry. We’ll use <a href="http://unstructured.io">Unstructured.io</a> to perform high-resolution chunking, extracting tables and images along the way, and build a Neo4j <a href="https://neo4j.com/blog/knowledge-graph/how-to-build-knowledge-graph/">knowledge graph</a> that preserves the chunk sequence in document context. We’ll deploy a chatbot built using <a href="https://neo4j.com/labs/neo4j-needle-starterkit/">Neo4j’s Needle Starter Kit</a>, which will perform inspectable retrieval and generation operations with the Neo4j GraphRAG Package for Python (<a href="https://neo4j.com/docs/neo4j-graphrag-python/current/user_guide_rag.html">neo4j-graphrag</a>). Later, we’ll step through how to:&nbsp;</p>



<ol class="wp-block-list">
<li>Build vector indexes on chunks and full-text indexes on entity terms</li>



<li>Parse and ingest document text, images, and tables into the knowledge graph</li>



<li>Perform vector embedding on document chunks</li>



<li>Perform entity extraction on document chunks</li>



<li>Add metadata to the images to filter out junk images</li>



<li>Deploy the chatbot application, using the neo4j-graphrag HybridCypherRetriever to perform simultaneous semantic and full-text chunk discovery, augmented by nearest-neighbor traversals to related chunks, images, and tables</li>
</ol>



<p>But first, let’s see what the finished result looks like and why we’re going down this path.</p>



<h2 class="wp-block-heading" id="h-a-chatbot-that-understands-your-documents">A Chatbot That Understands Your Documents</h2>



<p>Let’s start with the knowledge graph schema. <code>:Document</code> nodes have <code>:Chunk</code> nodes, these are sequenced in document order with a <code>:NEXT_CHUNK</code> relationship. <code>:Chunk</code> nodes have an embedding property for the vector backed by a Neo4j vector index. Images and tables in the text chunk are saved as <code>:Image</code> and <code>:Table</code> nodes, and kept in context with a <code>:RELATED_CONTENT</code> relationship. Extracted entities are instantiated as <code>:Entity</code> nodes (backed by a Neo4j Lucene full-text index) and mapped to chunks (within and across documents) by the <code>:HAS_ENTITY</code> relationship. This is known as a lexical graph, since it has decomposed the document into its various elements.</p>



<figure class="wp-block-image size-large"><img decoding="async" width="1024" height="689" src="https://dist.neo4j.com/wp-content/uploads/20250729112033/lexical-knowledge-graph-schema-1024x689.png" alt="" class="wp-image-385581" srcset="https://dist.neo4j.com/wp-content/uploads/20250729112033/lexical-knowledge-graph-schema-1024x689.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729112033/lexical-knowledge-graph-schema-300x202.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729112033/lexical-knowledge-graph-schema-150x101.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729112033/lexical-knowledge-graph-schema-768x516.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729112033/lexical-knowledge-graph-schema-1536x1033.png 1536w, https://dist.neo4j.com/wp-content/uploads/20250729112033/lexical-knowledge-graph-schema-600x404.png 600w, https://dist.neo4j.com/wp-content/uploads/20250729112033/lexical-knowledge-graph-schema.png 1600w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption class="wp-element-caption">The lexical knowledge graph schema</figcaption></figure>



<p>We can take a look at how the document is represented in Neo4j using this query:</p>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='cypher'>MATCH path0 = (n:Document {name: "StatoilHydro_Volve_15_9_F_14_Report.pdf"})&lt;-[:PART_OF_DOCUMENT]-(c0:Chunk)
WHERE NOT (c0)&lt;-[:NEXT_CHUNK]-()
MATCH (n)&lt;-[:PART_OF_DOCUMENT]-(c:Chunk)
WITH path0, COLLECT(c) AS chunks
UNWIND chunks AS chunk
CALL(chunk) {
    MATCH path1 = (chunk)-[:NEXT_CHUNK|RELATED_CONTENT]-()
    RETURN path1
}
RETURN path0, path1</pre>
</div>



<p>The graph preserves the basic structure of the document –&nbsp;a sequence of <code>:Chunk</code> nodes chained in order of appearance, along with any associated <code>:Image</code> and <code>:Table</code> nodes. For this particular document, we have parsed 47 narrative text chunks, 32 images, and 11 tables.</p>



<figure class="wp-block-image size-large"><img decoding="async" width="1024" height="618" src="https://dist.neo4j.com/wp-content/uploads/20250729112117/lexical-graph-single-doc-1024x618.png" alt="" class="wp-image-385582" srcset="https://dist.neo4j.com/wp-content/uploads/20250729112117/lexical-graph-single-doc-1024x618.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729112117/lexical-graph-single-doc-300x181.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729112117/lexical-graph-single-doc-150x91.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729112117/lexical-graph-single-doc-768x464.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729112117/lexical-graph-single-doc-1536x927.png 1536w, https://dist.neo4j.com/wp-content/uploads/20250729112117/lexical-graph-single-doc-600x362.png 600w, https://dist.neo4j.com/wp-content/uploads/20250729112117/lexical-graph-single-doc.png 1600w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption class="wp-element-caption">Example lexical graph for a single document</figcaption></figure>



<p>We can zoom in and see how this looks. The <code>:Document</code> node is in the lower left corner, and you can see the sequenced <code>:Chunk</code> nodes with related <code>:Image</code> and <code>:Table</code> nodes.<br></p>



<figure class="wp-block-image size-large"><img loading="lazy" decoding="async" width="1024" height="442" src="https://dist.neo4j.com/wp-content/uploads/20250729112150/lexical-graph-close-up-1024x442.png" alt="" class="wp-image-385583" srcset="https://dist.neo4j.com/wp-content/uploads/20250729112150/lexical-graph-close-up-1024x442.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729112150/lexical-graph-close-up-300x129.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729112150/lexical-graph-close-up-150x65.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729112150/lexical-graph-close-up-768x331.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729112150/lexical-graph-close-up-1536x662.png 1536w, https://dist.neo4j.com/wp-content/uploads/20250729112150/lexical-graph-close-up-600x259.png 600w, https://dist.neo4j.com/wp-content/uploads/20250729112150/lexical-graph-close-up.png 1600w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /><figcaption class="wp-element-caption">Close-up of the lexical graph showing <code>:Document</code>, <code>:Chunk</code>, <code>:Image</code>, and <code>:Table</code> nodes</figcaption></figure>



<h2 class="wp-block-heading" id="h-accuracy-and-explainability-with-neo4j-graphrag">Accuracy and Explainability With Neo4j GraphRAG</h2>



<p>So how does this help us improve GenAI accuracy? With this lexical graph structure, we can discover texts (and related content) using four retrieval methods:</p>



<ol class="wp-block-list">
<li>Semantic search of <code>:Chunk</code> text embeddings using vector indexing</li>



<li>Full-text index search of extracted entities and traversal to their source texts</li>



<li>Traversal to nearest-neighbor texts for <code>:Chunk</code> nodes discovered by methods 1 and 2</li>



<li>Traversal to images and tables related to <code>:Chunk</code> nodes discovered by methods 1 and 2</li>
</ol>



<p>Results for methods 1-3 are packaged to provide rich, accurate, and structured context for summarization by the LLM. Results for method 4 (images and tables) are displayed post-generation in the chatbot (see below).</p>



<p>This all sounds complicated, but fortunately, the heavy lifting is done by the&nbsp; <a href="https://neo4j.com/docs/neo4j-graphrag-python/current/api.html#hybridcypherretriever">HybridCypherRetriever</a> method in the neo4j-graphrag package:</p>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>#this query pulls the adjacent Chunks, Entities
RETRIEVAL_QUERY = (
"""
WITH node, score
OPTIONAL MATCH (node)-[:NEXT_CHUNK]-(c) // get chunk neighbors
OPTIONAL MATCH (node)&lt;-[HAS_ENTITY]-(e) // get entity context chunks
ORDER BY score DESC LIMIT 100
RETURN apoc.convert.toSet(COLLECT(elementId(node))+COLLECT(elementId(e))+COLLECT(elementId(c))) AS listIds,
COLLECT (e.id) as contextNodes, node.text as nodeText, score ORDER BY score DESC
"""
)

def __init__(self, driver, embedder, vector_index_name, fulltext_index_name):
        self._retriever = HybridCypherRetriever(
            driver,
            vector_index_name=vector_index_name,
            fulltext_index_name=fulltext_index_name,
            retrieval_query=self.RETRIEVAL_QUERY,
            result_formatter=self.formatter,
            embedder=embedder,
            neo4j_database="neo4j",
        )</pre>
</div>



<p>We tell the retriever the names of the vector and full-text indexes to use, pass in the embedder for the user’s prompt, and specify the augmenting <a href="https://neo4j.com/docs/getting-started/cypher/">Cypher</a> query we’re using to traverse to nearest-neighbor <code>:Chunk</code> nodes from the discovered nodes, along with the database to use.</p>



<h2 class="wp-block-heading" id="h-example-prompt">Example Prompt</h2>



<p>Let’s see it in action. There are some <a href="https://github.com/graphadvantage/aura-chatbot/blob/images-tables/graph-build/example-questions.txt">example questions</a> in the repo, so let’s try one:</p>



<p><code>What is meant by a sinusoid in the EcoScope analyses?</code></p>



<p>We get a robust, specific answer back (and as a former earth scientist, having read these documents closely, I can say this is a good and correct result), but let’s see if we’re really convinced. Pretending to be a petroleum engineer, I can click on the graph icon to inspect the content used to prepare the response.</p>



<figure class="wp-block-image size-large"><img loading="lazy" decoding="async" width="1024" height="734" src="https://dist.neo4j.com/wp-content/uploads/20250729112323/detailed-response-knowledge-graph-1024x734.png" alt="" class="wp-image-385584" srcset="https://dist.neo4j.com/wp-content/uploads/20250729112323/detailed-response-knowledge-graph-1024x734.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729112323/detailed-response-knowledge-graph-300x215.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729112323/detailed-response-knowledge-graph-150x108.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729112323/detailed-response-knowledge-graph-768x551.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729112323/detailed-response-knowledge-graph-600x430.png 600w, https://dist.neo4j.com/wp-content/uploads/20250729112323/detailed-response-knowledge-graph.png 1410w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /><figcaption class="wp-element-caption">Detailed response to user prompt, sourced entirely from the lexical knowledge graph</figcaption></figure>



<p>Now we can see the inner workings of the HybridCypherRetriever. We have a lexical subgraph to explore that shows the <code>:Chunk</code> and <code>:Entity</code> nodes discovered by semantic and full-text search, respectively; the nearest-neighbor chunks discovered by local traversal inside the document sequence; and all the related <code>:Table</code> and <code>:Image</code> nodes.</p>



<figure class="wp-block-image size-large"><img loading="lazy" decoding="async" width="1024" height="734" src="https://dist.neo4j.com/wp-content/uploads/20250729112446/graphrag-retriever-summarized-1024x734.png" alt="" class="wp-image-385586" srcset="https://dist.neo4j.com/wp-content/uploads/20250729112446/graphrag-retriever-summarized-1024x734.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729112446/graphrag-retriever-summarized-300x215.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729112446/graphrag-retriever-summarized-150x108.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729112446/graphrag-retriever-summarized-768x551.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729112446/graphrag-retriever-summarized-600x430.png 600w, https://dist.neo4j.com/wp-content/uploads/20250729112446/graphrag-retriever-summarized.png 1410w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /><figcaption class="wp-element-caption">Inspection of nodes discovered by the GraphRAG retriever and summarized by the LLM</figcaption></figure>



<p>I can click on any of these nodes in the visualization and see their content.</p>



<figure class="wp-block-image size-large"><img loading="lazy" decoding="async" width="1024" height="734" src="https://dist.neo4j.com/wp-content/uploads/20250729112528/text-chunk-1024x734.png" alt="" class="wp-image-385587" srcset="https://dist.neo4j.com/wp-content/uploads/20250729112528/text-chunk-1024x734.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729112528/text-chunk-300x215.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729112528/text-chunk-150x108.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729112528/text-chunk-768x551.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729112528/text-chunk-600x430.png 600w, https://dist.neo4j.com/wp-content/uploads/20250729112528/text-chunk.png 1410w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /><figcaption class="wp-element-caption">Example text chunk discovered by the neo4j-graphrag HybridCypherRetriever</figcaption></figure>



<p>And if I click on an <code>:Image</code> node, I can see a diagram that shows how the EcoScope analysis works, which might be the best and most intuitive answer to my original question.</p>



<figure class="wp-block-image size-large"><img loading="lazy" decoding="async" width="1024" height="734" src="https://dist.neo4j.com/wp-content/uploads/20250729112626/contextual-traversal-1024x734.png" alt="" class="wp-image-385588" srcset="https://dist.neo4j.com/wp-content/uploads/20250729112626/contextual-traversal-1024x734.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729112626/contextual-traversal-300x215.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729112626/contextual-traversal-150x108.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729112626/contextual-traversal-768x551.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729112626/contextual-traversal-600x430.png 600w, https://dist.neo4j.com/wp-content/uploads/20250729112626/contextual-traversal.png 1410w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /><figcaption class="wp-element-caption">Example image discovered by contextual traversal from discovered text chunks</figcaption></figure>



<h2 class="wp-block-heading" id="h-so-what-the-genai-quick-take">So What? The GenAI Quick-Take</h2>



<p>This blog shows how <a href="https://neo4j.com/whitepapers/developers-guide-how-to-build-knowledge-graph/">Neo4j knowledge graphs</a> can provide contextualized, accurate, and inspectable GenAI responses (complete with images and tables) for technical audiences. Achieving this level of specificity and trust is challenging using only LLMs or vector databases.&nbsp;</p>



<p><a href="http://unstructured.io">Unstructured.io</a> enables intelligent extraction of narrative text in document context, along with associated images and tables for additional explanatory context. <a href="https://neo4j.com">Neo4j</a> enables you to easily build a knowledge graph that combines both descriptive information from unstructured data and business facts &amp; hierarchy from structured data.</p>



<p>By leveraging a Neo4j knowledge graph as the persistence layer for your GenAI application, you can provide a performant and trustworthy experience for your end users, layering on <a href="https://neo4j.com/labs/genai-ecosystem/neoconverse/">agentic frameworks</a> and <a href="https://neo4j.com/developer/genai-ecosystem/model-context-protocol-mcp/">MCP</a> integrations as needed for even more sophisticated knowledge discovery methods.</p>



<p>The concepts presented here can be extended to any corpus of technical documents with only slight modifications to the repo code. The next sections step through how you can leverage these approaches to build a Neo4j knowledge graph and chatbot from your own documents.</p>



<h2 class="wp-block-heading">Document Parsing With Unstructured.io</h2>



<p>First, we need to parse our technical documents. To do this, we’ll use some great tools from <a href="https://unstructured.io">Unstructured.io</a>, a new Neo4j partner.&nbsp;</p>



<p>Unstructured.io provides sophisticated tooling for extracting a wide range of content elements from documents and is able to examine the document layout to infer additional context. Unstructured.io recently released a Neo4j connector that allows you to build a lexical graph of text chunks as part of a parallelized Unstructured.io document processing pipeline. You can use <a href="http://unstructured.io">Unstructured.io</a> services through their web console or API.</p>



<figure class="wp-block-image size-large"><img loading="lazy" decoding="async" width="1024" height="464" src="https://dist.neo4j.com/wp-content/uploads/20250729191128/parsing-pipeline-1024x464.png" alt="" class="wp-image-385641" srcset="https://dist.neo4j.com/wp-content/uploads/20250729191128/parsing-pipeline-1024x464.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729191128/parsing-pipeline-300x136.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729191128/parsing-pipeline-150x68.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729191128/parsing-pipeline-768x348.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729191128/parsing-pipeline-1536x696.png 1536w, https://dist.neo4j.com/wp-content/uploads/20250729191128/parsing-pipeline-600x272.png 600w, https://dist.neo4j.com/wp-content/uploads/20250729191128/parsing-pipeline.png 1600w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /><figcaption class="wp-element-caption">Example parsing pipeline built in the <a href="http://unstructured.io">Unstructured.io</a> console using a Neo4j graph destination</figcaption></figure>



<p>Unstructured.io pipelines use a few <a href="https://docs.unstructured.io/ui/overview">basic components</a>. We’ll focus on the partitioner, chunker, embedder, entity extractor, and Neo4j destination.&nbsp;</p>



<p>The partitioner is the workhorse of the Unstructured.io platform. Able to operate in parallel, it can quickly shred a document, then identify and tag elements like titles, headers, footers, page numbers, narrative text, lists, formulas, etc. – and, as we’ll see later, even extract images and tables.</p>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>        partitioner_config=PartitionerConfig(
            partition_by_api=True,
            api_key=(UNSTRUCTURED_API_KEY),
            partition_endpoint=UNSTRUCTURED_API_URL,
            additional_partition_args={
                "split_pdf_page": True,
                "split_pdf_allow_failed": True,
                "split_pdf_concurrency_level": 15
            }</pre>
</div>



<p>The chunker is a configurable layer of contextual intelligence that gathers elements produced by the partitioner into larger text blocks for presentation to an LLM. If you use the <code>by_title</code> option, it&#8217;ll look at document indenting and whitespace to determine natural boundaries in the narrative.</p>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>        chunker_config=ChunkerConfig(
            chunking_strategy="by_title"
            max_characters=1500
            ),</pre>
</div>



<p>The embedder generates vector embeddings for chunks to support semantic search, and the entity extractor parses entities from the chunks and can pass a prompt to the LLM.</p>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>        embedder_config=EmbedderConfig(
            embedding_provider="openai",
            embedding_api_key=OPENAI_API_KEY
        ),</pre>
</div>



<p>The Neo4j destination connector builds some constraints and native vector indexes, then loads the pipeline&#8217;s output into Neo4j, building a lexical graph that connects sequenced chunk nodes to a node representing the processed document. Entity nodes connect chunk nodes for additional traversable context.</p>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>        destination_connection_config=Neo4jConnectionConfig(
            access_config=Neo4jAccessConfig(password=NEO4J_PASSWORD),
            username=NEO4J_USERNAME,
            uri=NEO4J_URI,
            database=NEO4J_DATABASE,
        ),
        stager_config=Neo4jUploadStagerConfig(),
        uploader_config=Neo4jUploaderConfig(batch_size=100)</pre>
</div>



<p>For our application, we’ll use the Unstructured.io parsing API, performing all the parsing and chunking operations. The <a href="https://github.com/graphadvantage/aura-chatbot/tree/images-tables">GitHub repo</a> contains all the notebooks, application code, and links to example files. Follow the repo instructions on how to provision a free Neo4j Aura graph database and get your Unstructured.io API key.</p>



<p>I’ll go through building the graph step by step in the next section.</p>



<h2 class="wp-block-heading">Lexical Graph Pipeline</h2>



<p>Here’s the full pipeline used to build the lexical knowledge graph.</p>



<h3 class="wp-block-heading">Step 1. Build Vector Indexes on Document Chunks and Full-Text Indexes on Entity Terms</h3>



<p>First, we’ll do some configurations and set up the necessary indexes for native semantic and full-text searching in Neo4j using the neo4j-graphrag package.&nbsp;</p>



<h4 class="wp-block-heading">Install Dependencies</h4>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>!pip install unstructured-client
!pip install neo4j
!pip install neo4j-graphrag</pre>
</div>



<h4 class="wp-block-heading">Configure Variables</h4>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>unstructured_api_key="UNSTRUCTURED_API_KEY"
neo4j_uri = "NEO4J_URI"
neo4j_database = "neo4j" 
neo4j_user = "neo4j" 
neo4j_password = "NEO4J_PASSWORD"
openai_api_key ="OPENAI_API_KEY"</pre>
</div>



<h4 class="wp-block-heading">Set Vector and Full-Text Indexes in Neo4j</h4>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>from neo4j import GraphDatabase
from neo4j_graphrag.indexes import create_vector_index
from neo4j_graphrag.indexes import create_fulltext_index

# Neo4j driver setup
driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

VECTOR_INDEX_NAME = "chunk_embedding"

# Creating the vector index
create_vector_index(
    driver,
    VECTOR_INDEX_NAME,
    label="Chunk",
    embedding_property="embedding",
    dimensions=1536,
    similarity_fn="cosine",
    fail_if_exists=False,
)

FULLTEXT_INDEX_NAME = "entity_text"

# Creating the full text index
create_fulltext_index(
    driver,
    FULLTEXT_INDEX_NAME,
    label="Entity",
    node_properties= ["text", "variants"],
    fail_if_exists=False,
)

query = '''
SHOW INDEXES
'''

with driver.session() as session:
            result = session.run(query)
            for record in result:
                print(record)</pre>
</div>



<h3 class="wp-block-heading">Step 2. Parse and Ingest Document Text, Images, and Tables Into the Knowledge Graph</h3>



<p>Next, we’ll parse our document set and build the knowledge graph. We’ll create nodes for <code>:Document</code>, <code>:Chunk</code>, <code>:Image</code>, and :<code>Table</code>. You’ll see that we use the <code>apoc.nodes.link()</code> procedure to link all of the <code>:Chunk</code> nodes in order of appearance in the <code>:Document</code>, and also that we’re creating additional <code>:Image</code> and <code>:Table</code> nodes if they were part of the <code>:Chunk</code> content. We’re storing the images as binaries and OCR text, and tables as images, HTML, and text.</p>



<h4 class="wp-block-heading">Extract and Chunk PDFs With Unstructured.io</h4>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>import os
import base64
import zlib
import json
import logging
import nltk

from neo4j import GraphDatabase
from unstructured_client import UnstructuredClient
from unstructured_client.models import operations, shared
from unstructured.staging.base import elements_from_dicts, elements_to_json

# Disable logging
logging.disable(logging.CRITICAL)

# Configuration
directory_path = "PATH_TO_DOCUMENTS/"

client = UnstructuredClient(
    api_key_auth=unstructured_api_key,
    server_url="https://api.unstructuredapp.io"
)

driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

CHUNK_QUERY = '''
WITH apoc.convert.fromJsonList($json) AS maps
UNWIND maps AS map
WITH apoc.map.clean(map,[],["  ",""]) AS m
MERGE (d:Document {name: m.metadata.filename})
WITH m, d
CALL(m, d) {
  CREATE (n:Chunk {id: m.element_id})
  SET
    n.type = "NarrativeText",
    n.text = m.text,
    n.filename = m.metadata.filename,
    n.filetype = m.metadata.filetype,
    n.languages = m.metadata.languages,
    n.page_number = m.metadata.page_number,
    n.tokens = m.tokens
  CREATE (n)-[:PART_OF_DOCUMENT]->(d)
  RETURN n
}
WITH m, d, n
CALL(m, d, n) {
  WITH m, d, n
  WHERE m.metadata.type IN ["Image", "Table"]
  CREATE (i:$(m.metadata.type) {id: m.element_id})
  SET i.type = m.metadata.type,
      i.figure_caption = m.metadata.figure_caption,
      i.text = m.metadata.text,
      i.filename = m.metadata.filename,
      i.filetype = m.metadata.filetype,
      i.languages = m.metadata.languages,
      i.page_number = m.metadata.page_number,
      i.image_base64 = m.metadata.image_base64,
      i.image_mime_type = m.metadata.image_mime_type,
      i.text_as_html = m.metadata.text_as_html
  MERGE (n)-[:RELATED_CONTENT]->(i)
  MERGE (i)-[:PART_OF_DOCUMENT]->(d)
}
WITH DISTINCT d, n
WITH d, COLLECT(n) AS nodes
CALL apoc.nodes.link(nodes, "NEXT_CHUNK")
'''

def run_query(tx, query, json_data):
    return tx.run(query, {"json": json_data}).consume()

def extract_orig_elements(encoded):
    decoded = base64.b64decode(encoded)
    decompressed = zlib.decompress(decoded)
    return json.loads(decompressed.decode("utf-8"))

def process_file(filepath, filename):
    print(f"\nProcessing file: {filename}")
    
    with open(filepath, "rb") as f:
        files = shared.Files(
            content=f.read(),
            file_name=filename
        )

    request = operations.PartitionRequest(
        partition_parameters=shared.PartitionParameters(
            files=files,
            strategy="hi_res",
            hi_res_model_name="yolox",
            element_exclude=["Header", "Footer", "ListItem", "Formula", "UncategorizedText"],
            extract_image_block_types=["Image", "Table"],
            chunking_strategy="by_title",
            max_characters=1500,
            split_pdf_page=True,
            split_pdf_allow_failed=True,
            split_pdf_concurrency_level=15
        )
    )

    response = client.general.partition(request=request)
    element_dicts = [e for e in response.elements]

    for i, element in enumerate(element_dicts):
        if element.get("text"):
            element["tokens"] = len(nltk.word_tokenize(element["text"]))

        metadata = element.get("metadata", {})
        if metadata.get("orig_elements"):
            orig_elements = extract_orig_elements(metadata["orig_elements"])

            for obj in orig_elements:
                if obj.get("type") == "FigureCaption" and obj.get("text", "").lower().startswith("figure"):
                    metadata["figure_caption"] = obj["text"]

                if obj.get("type") == "Image":
                    metadata.update({
                        "element_id": obj["element_id"],
                        "type": obj["type"],
                        "image_base64": obj["metadata"]["image_base64"],
                        "image_mime_type": obj["metadata"]["image_mime_type"],
                        "text": obj["text"]
                    })

                if obj.get("type") == "Table":
                    metadata.update({
                        "element_id": obj["element_id"],
                        "type": obj["type"],
                        "text_as_html": obj["metadata"]["text_as_html"],
                        "image_base64": obj["metadata"]["image_base64"],
                        "image_mime_type": obj["metadata"]["image_mime_type"],
                        "text": obj["text"]
                    })

        element_dicts[i]["metadata"].pop("orig_elements", None)

    json_data = json.dumps(element_dicts, indent=4)

    with driver.session() as session:
        summary = session.execute_write(run_query, CHUNK_QUERY, json_data)
        print(f"nodes created => {summary.counters.nodes_created}, rels created => {summary.counters.relationships_created}")
    session.close() 
    print(f"Finished processing: {filename}")

def main():
    for filename in os.listdir(directory_path):
        if filename.startswith(".") or not os.path.isfile(os.path.join(directory_path, filename)):
            continue

        try:
            process_file(os.path.join(directory_path, filename), filename)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    driver.close()
    print("Done!")

if __name__ == "__main__":
    main()</pre>
</div>



<h3 class="wp-block-heading">Step 3. Perform Vector Embedding on Document Chunks</h3>



<p>Next, we’ll use OpenAI to perform vector embedding on the chunk texts and write these as properties. Because we already declared a vector index on the embedding property, similarities will be automatically calculated behind the scenes.</p>



<h4 class="wp-block-heading">Embed Vectors With Neo4j GraphRAG</h4>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'># vector embedding on Chunk text for semantic search
from neo4j import GraphDatabase
from neo4j_graphrag.embeddings import OpenAIEmbeddings
import logging
import sys

# Disable logging output
logging.disable(sys.maxsize)

# --- Configuration ---
EMBEDDING_MODEL = "text-embedding-ada-002"
MAX_CHUNK_LENGTH = 12000

# Initialize OpenAI embedder
embedder = OpenAIEmbeddings(model=EMBEDDING_MODEL, api_key=openai_api_key)

# Initialize Neo4j driver
driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))


def embed_chunks():
    with driver.session() as session:
        result = session.run("""
            MATCH (n:Chunk)
            WHERE n.text IS NOT NULL AND n.embedding IS NULL
            RETURN n.id AS id, n.text AS data
        """)

        for record in result:
            chunk_id = record["id"]
            data = record["data"]

            if len(data) > MAX_CHUNK_LENGTH:
                print(f"Skipping chunk {chunk_id} (length: {len(data)})")
                continue

            print(f"\rEmbedding chunk: {chunk_id}", end="", flush=True)

            try:
                embedding = embedder.embed_query(data)

                session.run("""
                    MATCH (n:Chunk {id: $chunk_id})
                    SET n.embedding = $embedding
                """, chunk_id=chunk_id, embedding=embedding)

            except Exception as e:
                print(f"\nFailed to embed chunk {chunk_id}: {e}")


def main():
    embed_chunks()
    driver.close()
    print("\nDone embedding chunks!")


if __name__ == "__main__":
    main()     </pre>
</div>



<h3 class="wp-block-heading">Step 4. Perform Entity Extraction on Document Chunks</h3>



<p>We’ll use OpenAI to perform entity extraction on the chunk texts and link the entities together.&nbsp;Because this is a compute-intensive operation, I like to use a <code>:ProcessMe</code> label to speed up the query.&nbsp;&nbsp;</p>



<p>You’ll notice that we’re using a data domain-specific prompt to guide the entity extraction and result format:&nbsp;</p>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>Extract all the entities from the following text. 

Identify only entities, abbreviations and technical terms commonly used in the petroleum exploration, petroleum geology, reservoir analysis, and oil &amp; gas production.

Return entities in this format: ["entity1", "entity2"]</pre>
</div>



<p>Be sure to customize this for your own data domain to properly extract entities.</p>



<h4 class="wp-block-heading">Label Chunk Nodes for Processing</h4>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'># entity extraction on Chunk text for full text search

from neo4j import GraphDatabase

# Neo4j driver setup
driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

# to perform selective entity extraction using "ProcessMe" label execute this query

PROCESS_ME ='''
MATCH (n:Chunk {type:"NarrativeText"}) 
WHERE NOT (n)-[:HAS_ENTITY]->() AND n.entities IS NULL
SET n:ProcessMe
'''

with driver.session() as session:
    res = session.run(PROCESS_ME)
session.close() 
print("done!")</pre>
</div>



<h4 class="wp-block-heading" id="h-entity-extraction-on-labeled-chunk-nodes">Entity Extraction on Labeled Chunk Nodes</h4>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'># prompted entity extraction with some very light entity resolution
import logging
import sys
from neo4j import GraphDatabase
from openai import OpenAI

# --- Config ---
MAX_CHUNKS = 1000
OPENAI_MODEL = "gpt-4o"  # or "gpt-4"

# --- Logging ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.disable(sys.maxsize)  # Disable logging if needed

# --- Clients ---
client = OpenAI(api_key=openai_api_key)
driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

# --- Cypher Queries ---
FETCH_CHUNKS_QUERY = """
MATCH (n:Chunk:ProcessMe)
RETURN n.id AS id, replace(n.text,"\n","") AS text
LIMIT $limit
"""

ENTITY_INSERT_QUERY = """
WITH $entities AS entities
MATCH (n:Chunk:ProcessMe {id: $id})
WITH n, entities
CALL apoc.do.when(
    entities[0] = "[]" OR entities[0] STARTS WITH "The text provided does not contain",
    "WITH n SET n.entities = 'failed' REMOVE n:ProcessMe RETURN 0 AS rels",
    "WITH n, apoc.convert.fromJsonList(entities[0]) AS names
     UNWIND names AS name
     MERGE (e:Entity {text: toLower(name)})
     ON CREATE SET e.variants = [name]
     ON MATCH SET e.variants = apoc.convert.toSet(e.variants + [name])
     MERGE (n)-[:HAS_ENTITY]->(e)
     WITH DISTINCT n, COUNT(e) AS rels
     REMOVE n:ProcessMe
     RETURN rels",
    {n: n, entities: entities}
) YIELD value
RETURN value
"""

FAIL_MARK_QUERY = """
MATCH (n:Chunk:ProcessMe {id: $id})
SET n.entities = "failed"
REMOVE n:ProcessMe
"""

# --- Entity Extraction Prompt ---
# modify as needed for your data domain
def extract_entities(text: str) -> list:
    prompt = f"""
Extract all the entities from the following text. 

Identify only entities, abbreviations and technical terms commonly used in the petroleum exploration, petroleum geology, reservoir analysis, and oil &amp; gas production.

Return entities in this format: ["entity1", "entity2"]

Do not include any extra text or explanation.

Text: {text}
"""

    messages = [
        {"role": "system", "content": "You help extract entities from petroleum-related text."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages,
        max_tokens=500,
        temperature=0
    )

    return [response.choices[0].message.content.strip()]


# --- Main Function ---
def main():
    processed_count = 0

    with driver.session() as session:
        chunks = session.run(FETCH_CHUNKS_QUERY, limit=MAX_CHUNKS)

        for chunk in chunks:
            chunk_id = chunk["id"]
            text = chunk["text"]
            processed_count += 1

            try:
                entities = extract_entities(text)
                result = session.run(ENTITY_INSERT_QUERY, id=chunk_id, entities=entities)

                for record in result:
                    rels = record["value"]["rels"]
                    print(f"\rRelationships created: {rels} | Processed: {processed_count}     ", end="", flush=True)

                result.consume()

            except Exception as e:
                logging.warning(f"\nFailed to process chunk {chunk_id}: {e}")
                session.run(FAIL_MARK_QUERY, id=chunk_id)
    driver.close()
    print("\nDone extracting entities!")


if __name__ == "__main__":
    main()</pre>
</div>



<h3 class="wp-block-heading" id="h-step-5-add-metadata-to-the-images-to-filter-junk-images">Step 5. Add metadata to the images to filter junk images</h3>



<p>We’re almost done! If you were to look at some of the images captured, you’d see a lot of non-interesting graphics like logos and other extraction artifacts. As a final step, we’ll capture the image metadata so we can filter out non-interesting images when we do retrieval.</p>



<h4 class="wp-block-heading" id="h-calculate-image-sizes-and-dimensions">Calculate Image Sizes and Dimensions</h4>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>#filtering properties for the frontend to hide logos and other uninteresting images
import base64
from io import BytesIO
from PIL import Image
from neo4j import GraphDatabase
import json

driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

# Cypher query to fetch nodes with base64 images
QUERY_IMAGES= """
MATCH (n:Image|Table)
WHERE n.image_base64 IS NOT NULL AND n.bytes IS NULL
RETURN n.id AS id, n.image_base64 AS image_base64
"""

def get_image_properties(image_base64: str):
    try:
        image_data = base64.b64decode(image_base64)
        with Image.open(BytesIO(image_data)) as image:
            width, height = image.size
            aspect_ratio = max(width / height, height / width) if width and height else None
            return {
                "bytes": len(image_base64),
                "width": width,
                "height": height,
                "aspect_ratio": aspect_ratio
            }
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def update_image_properties(driver):
    with driver.session() as session:
        result = session.run(QUERY_IMAGES)
        
        for record in result:
            node_id = record["id"]
            image_base64 = record["image_base64"]
            props = get_image_properties(image_base64)

            if props:
                session.run(
                    """
                    WITH apoc.convert.fromJsonMap($json) AS map
                    MATCH (n:Image|Table {id: $id})
                    SET n += map
                    """,
                    {"id": node_id, "json": json.dumps(props)}
                )


if __name__ == "__main__":
    update_image_properties(driver)
    driver.close()
    print("Image metadata updated.")</pre>
</div>



<h2 class="wp-block-heading">GraphRAG Chatbot</h2>



<p>Now that we have our graph built, let’s wire up the chatbot. Follow the instructions in the <a href="https://github.com/graphadvantage/aura-chatbot/tree/images-tables">GitHub repo</a>.&nbsp;</p>



<p>The application is built using the <a href="https://neo4j.com/labs/neo4j-needle-starterkit/">Neo4j Needle Starter Kit</a> accelerator, and includes a Python backend and a React front end with some native graph visualizations using the <a href="https://neo4j.com/docs/api/nvl/current/index.html">Neo4j Visualization Library</a>. The back-end component we’ll focus on is <a href="https://github.com/graphadvantage/aura-chatbot/blob/images-tables/backend/app/retrieval/retriever.py">retriever.py</a>.</p>



<p>You were probably wondering how the semantic search and full-text search indexes were going to work together. The quick answer is the hybrid retrievers that are part of neo4j-graphrag. The HybridCypherRetriever takes the user’s prompt and uses it as an input for a simultaneous vector search (of text embeddings) and full-text search (of entity terms), then returns the combined list of discovered nodes, ranked using a weighted average of the respective scores. Check out <a href="https://neo4j.com/blog/developer/hybrid-retrieval-graphrag-python-package/">Hybrid Retrieval for GraphRAG Applications Using the GraphRAG Python Package</a> for details.&nbsp;</p>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1024" height="483" src="https://dist.neo4j.com/wp-content/uploads/20250729194455/weighted-average.png" alt="" class="wp-image-385644" srcset="https://dist.neo4j.com/wp-content/uploads/20250729194455/weighted-average.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729194455/weighted-average-300x142.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729194455/weighted-average-150x71.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729194455/weighted-average-768x362.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729194455/weighted-average-600x283.png 600w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /><figcaption class="wp-element-caption">Weighted average scoring for top_k = 3 simultaneous vector and full-text searching by the neo4j-graphrag HybridCypherRetriever</figcaption></figure>



<p>In our application, we’re using the HybridCypherRetriever, which allows us to add a Cypher statement for additional traversals. This is where we can mine the knowledge graph for additional context – in this case, discovering chunks that both precede and follow (in document sequence) our search-discovered chunks. These neighbor chunks provide useful narrative context for a more complete and accurate GenAI result.</p>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>#this query pulls the adjacent Chunks, Entities
    RETRIEVAL_QUERY = (
            """
            WITH node, score
            OPTIONAL MATCH (node)-[:NEXT_CHUNK]-(c) // get chunk neighbors
            OPTIONAL MATCH (node)&lt;-[HAS_ENTITY]-(e) // get entity context chunks
            ORDER BY score DESC LIMIT 100
            RETURN apoc.convert.toSet(COLLECT(elementId(node))+COLLECT(elementId(e))+COLLECT(elementId(c))) AS listIds,
            COLLECT (e.id) as contextNodes, node.text as nodeText, score ORDER BY score DESC
            """
        )

    def __init__(self, driver, embedder, vector_index_name, fulltext_index_name):
        self._retriever = HybridCypherRetriever(
            driver,
            vector_index_name=vector_index_name,
            fulltext_index_name=fulltext_index_name,
            retrieval_query=self.RETRIEVAL_QUERY,
            result_formatter=self.formatter,
            embedder=embedder,
            neo4j_database="neo4j",
        )</pre>
</div>



<p>On the front end, we have a component <a href="https://github.com/graphadvantage/aura-chatbot/blob/images-tables/frontend/src/templates/shared/components/RetrievalInformation.tsx">RetrievalInformation.tsx</a> (launched by the little graph icon in the result window), which displays all the <code>:Chunk</code> nodes sent to the LLM for summarization. It also displays the <code>:Image</code> and <code>:Table</code> nodes related to the summarized result. Each of these can be individually inspected by the user. This inspectability improves confidence in the system – the end user can see the discovered texts and related content that contributed to the final LLM summarized result.</p>


<div style="--max-height: 300px; --title-color: #ffffff; --title-background: #404752;" class="wp-block-neo4j-neo-codemirror">
		<pre data-lang='python'>RetrievalInformation.tsx  

function run() {
    const formattedSources = sources.map((source) => `"${source}"`).join(',');

    const query1 = `
    MATCH (a:Chunk)-[r:PART_OF_DOCUMENT]->(b:Document)
    WHERE elementId(a) in [${formattedSources}]
    RETURN DISTINCT a,r,b
    UNION
    MATCH (a:Chunk)-[r:HAS_ENTITY|NEXT_CHUNK]-(b:Chunk|Entity)
    WHERE elementId(a) in [${formattedSources}] AND elementId(b) in [${formattedSources}]
    RETURN DISTINCT a,r,b
    UNION
    MATCH (a:Chunk)-[r:RELATED_CONTENT]-(b:Image|Table)
    WHERE elementId(a) in [${formattedSources}] AND b.aspect_ratio &lt; 10 AND b.bytes > 1024 * 9
    RETURN DISTINCT a,r,b
    LIMIT 500
    `;</pre>
</div>



<figure class="wp-block-image size-large"><img loading="lazy" decoding="async" width="1024" height="734" src="https://dist.neo4j.com/wp-content/uploads/20250729194822/example-response-1024x734.png" alt="" class="wp-image-385647" srcset="https://dist.neo4j.com/wp-content/uploads/20250729194822/example-response-1024x734.png 1024w, https://dist.neo4j.com/wp-content/uploads/20250729194822/example-response-300x215.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729194822/example-response-150x108.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729194822/example-response-768x551.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729194822/example-response-600x430.png 600w, https://dist.neo4j.com/wp-content/uploads/20250729194822/example-response.png 1410w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /><figcaption class="wp-element-caption">Example response</figcaption></figure>



<p>I like clicking around in the result subgraph, but you could just as easily display these items inline with the text result. You may have noticed that Unstructured.io is also providing an OCR text result for the images and HTML for the tables. Another potential enhancement would be to make these texts searchable as well.</p>



<figure class="wp-block-image aligncenter size-full is-resized"><img loading="lazy" decoding="async" width="862" height="857" src="https://dist.neo4j.com/wp-content/uploads/20250729194933/subgraph-nodes-retrieved.png" alt="" class="wp-image-385648" style="width:600px" srcset="https://dist.neo4j.com/wp-content/uploads/20250729194933/subgraph-nodes-retrieved.png 862w, https://dist.neo4j.com/wp-content/uploads/20250729194933/subgraph-nodes-retrieved-300x298.png 300w, https://dist.neo4j.com/wp-content/uploads/20250729194933/subgraph-nodes-retrieved-150x150.png 150w, https://dist.neo4j.com/wp-content/uploads/20250729194933/subgraph-nodes-retrieved-768x764.png 768w, https://dist.neo4j.com/wp-content/uploads/20250729194933/subgraph-nodes-retrieved-600x597.png 600w" sizes="auto, (max-width: 862px) 100vw, 862px" /><figcaption class="wp-element-caption">Example inspection of discovered subgraph nodes contributing to the prompt results above (in this case, an image node that is a nearest neighbor of a text chunk node)</figcaption></figure>



<h2 class="wp-block-heading">Summary</h2>



<p>There are lots of potential enhancements and integrations you can add to this GenAI chatbot application, and as we’ve pointed out, you can apply the knowledge graph pipeline to any corpus of documents with only slight modifications to the code. If you have any questions about how to get started on your Neo4j GraphRAG project, please feel free to reach out to us.</p>



<h3 class="wp-block-heading" id="h-related-resources">Related Resources</h3>



<div class="wp-block-group has-global-padding is-layout-constrained wp-block-group-is-layout-constrained">
<ul class="wp-block-list">
<li><a href="https://console-preview.neo4j.io/">Neo4j Aura</a></li>



<li><a href="https://neo4j.com/labs/genai-ecosystem/">Neo4j GenAI Ecosystem</a></li>



<li><a href="https://neo4j.com/docs/neo4j-graphrag-python/current/index.html">Neo4j GraphRAG for Python</a></li>



<li><a href="https://neo4j.com/labs/neo4j-needle-starterkit/">Neo4j Needle Starter Kit</a></li>



<li><a href="https://needle-starterkit.graphapp.io/">Neo4j Needle Demo</a></li>



<li><a href="https://neo4j.com/docs/nvl/current/">Neo4j Visualization Library</a></li>



<li><a href="https://docs.unstructured.io/api-reference/workflow/destinations/neo4j">Unstructured.io</a></li>
</ul>
</div>



<p></p>
</div>

</div>



<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow" style="flex-basis:31.15%">
<div class="wp-block-group has-global-padding is-layout-constrained wp-block-group-is-layout-constrained">
<h2 class="wp-block-heading is-style-text-overline" id="h-share-article">Share Article</h2>


<div class="wp-block-neo4j-share-links" >
	<ul class="social-media-icons">
		<li><!-- LinkedIn -->
			<a href="https://www.linkedin.com/shareArticle?mini=true&url=https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/"
			   rel="noreferrer" target="_blank">
				<svg xmlns="http://www.w3.org/2000/svg" width="16" height="14" fill="none"><path fill="#fff" d="M3.85 13.97H.661V4.837H3.85v9.135Zm6.616-6.157a1.403 1.403 0 0 0-1.403 1.403v4.755H5.712V4.836h3.35v1.043a4.433 4.433 0 0 1 2.807-1.05c2.079 0 3.522 1.541 3.522 4.466v4.676h-3.522V9.216a1.403 1.403 0 0 0-1.403-1.41v.007ZM3.908 1.675a1.64 1.64 0 1 1-1.64-1.64 1.64 1.64 0 0 1 1.627 1.64h.013Z"/></svg>
			</a>
		</li>
		<li><!-- Twitter -->
			<a href="https://twitter.com/intent/tweet?url=https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/&text="
			   rel="noreferrer" target="_blank">
				<svg xmlns="http://www.w3.org/2000/svg" width="14" height="12" fill="none"><path fill="#fff" d="M10.635.198h1.939l-4.235 4.84 4.982 6.588H9.42L6.364 7.63l-3.496 3.995H.928l4.53-5.178L.678.198h4L7.442 3.85 10.635.198Zm-.68 10.267h1.074L4.095 1.298H2.943l7.012 9.167Z"/></svg>
			</a>
		</li>
		<li><!-- Facebook -->
			<a href="https://www.facebook.com/sharer/sharer.php?u=https://neo4j.com/blog/genai/graphrag-chatbot-unstructured-io/"
			   rel="noreferrer" target="_blank">
				<svg xmlns="http://www.w3.org/2000/svg" width="10" height="18" fill="none"><path fill="#fff" d="M9.6 5.812H6.402V4.379a.75.75 0 0 1 .75-.826h2.251v-3H6.156c-2.949 0-3.504 2.25-3.504 3.646v1.613H.402v3h2.25v8.628h3.751V8.812h2.888l.308-3Z"/></svg>
			</a>
		</li>
	</ul>
</div>


<div class="wp-block-neo4j-blog-sidebar-posts">

									<div>
				
<figure class="wp-block-image size-full"><a href="/product/auradb/"><img loading="lazy" decoding="async" width="688" height="300" src="https://dist.neo4j.com/wp-content/uploads/20250430121502/Aura-1.jpg" alt="" class="wp-image-375753" srcset="https://dist.neo4j.com/wp-content/uploads/20250430121502/Aura-1.jpg 688w, https://dist.neo4j.com/wp-content/uploads/20250430121502/Aura-1-300x131.jpg 300w, https://dist.neo4j.com/wp-content/uploads/20250430121502/Aura-1-150x65.jpg 150w, https://dist.neo4j.com/wp-content/uploads/20250430121502/Aura-1-600x262.jpg 600w" sizes="auto, (max-width: 688px) 100vw, 688px" /></a></figure>
			</div>
								<div>
				
<figure class="wp-block-image size-full"><a href="https://graphacademy.neo4j.com/" target="_blank" rel=" noreferrer noopener"><img loading="lazy" decoding="async" width="688" height="300" src="https://dist.neo4j.com/wp-content/uploads/20250430121707/GA.jpg" alt="" class="wp-image-375758" srcset="https://dist.neo4j.com/wp-content/uploads/20250430121707/GA.jpg 688w, https://dist.neo4j.com/wp-content/uploads/20250430121707/GA-300x131.jpg 300w, https://dist.neo4j.com/wp-content/uploads/20250430121707/GA-150x65.jpg 150w, https://dist.neo4j.com/wp-content/uploads/20250430121707/GA-600x262.jpg 600w" sizes="auto, (max-width: 688px) 100vw, 688px" /></a></figure>
			</div>
								<div>
				
<figure class="wp-block-image size-full"><a href="/videos/"><img loading="lazy" decoding="async" width="1032" height="450" src="https://dist.neo4j.com/wp-content/uploads/20250430121852/VideoHub.jpg" alt="" class="wp-image-375763" srcset="https://dist.neo4j.com/wp-content/uploads/20250430121852/VideoHub.jpg 1032w, https://dist.neo4j.com/wp-content/uploads/20250430121852/VideoHub-300x131.jpg 300w, https://dist.neo4j.com/wp-content/uploads/20250430121852/VideoHub-1024x447.jpg 1024w, https://dist.neo4j.com/wp-content/uploads/20250430121852/VideoHub-150x65.jpg 150w, https://dist.neo4j.com/wp-content/uploads/20250430121852/VideoHub-768x335.jpg 768w, https://dist.neo4j.com/wp-content/uploads/20250430121852/VideoHub-600x262.jpg 600w" sizes="auto, (max-width: 1032px) 100vw, 1032px" /></a></figure>
			</div>
			</div>



<h2 class="wp-block-heading is-style-text-overline" id="h-explore">Explore</h2>


<div class="wp-block-neo4j-display-terms">
	<ul	class="wp-block-neo4j-display-terms__list">
								<li class="wp-block-neo4j-display-terms__term">
				<a class="wp-block-neo4j-display-terms__link" href="https://neo4j.com/blog/knowledge-graph/">Knowledge Graph</a>
			</li>
								<li class="wp-block-neo4j-display-terms__term">
				<a class="wp-block-neo4j-display-terms__link" href="https://neo4j.com/blog/supply-chain-and-logistics/">Supply Chain &amp; Logistics</a>
			</li>
								<li class="wp-block-neo4j-display-terms__term">
				<a class="wp-block-neo4j-display-terms__link" href="https://neo4j.com/blog/fraud-detection/">Fraud Detection</a>
			</li>
								<li class="wp-block-neo4j-display-terms__term">
				<a class="wp-block-neo4j-display-terms__link" href="https://neo4j.com/blog/graph-visualization/">Graph Visualization</a>
			</li>
								<li class="wp-block-neo4j-display-terms__term">
				<a class="wp-block-neo4j-display-terms__link" href="https://neo4j.com/blog/auradb/">AuraDB</a>
			</li>
								<li class="wp-block-neo4j-display-terms__term">
				<a class="wp-block-neo4j-display-terms__link" href="https://neo4j.com/blog/digital-twin/">Digital Twin</a>
			</li>
			</ul>
</div>
</div>
</div>
</div>
</div>



<div class="wp-block-group alignwide has-global-padding is-layout-constrained wp-block-group-is-layout-constrained">
<hr class="wp-block-separator has-text-color has-neutral-20-color has-alpha-channel-opacity has-neutral-20-background-color has-background is-style-wide alignwide" style="margin-top:var(--wp--preset--spacing--80);margin-bottom:var(--wp--preset--spacing--160)"/>



<div class="wp-block-group alignwide is-content-justification-space-between is-layout-flex wp-container-core-group-is-layout-9366075c wp-block-group-is-layout-flex">
<h2 class="wp-block-heading is-style-h3" id="h-related-articles">Related Articles</h2>



<div class="related-swiper-navigation"><div class="related-swiper-prev"></div>			<div class="related-swiper-next"></div></div>
</div>


<div style="margin-top:var(--wp--preset--spacing--80);margin-bottom:var(--wp--preset--spacing--120);" class="alignwide alignwide wp-block-neo4j-blog-related-posts">
			<div class='wp-block-neo4j-blog-related-posts__swiper swiper'>
			<div class='swiper-wrapper'>
				<div class="swiper-slide">
<div class="wp-block-neo4j-blog-card">
<div class="wp-block-neo4j-blog-card__featured-image" >
	<img width="1200" height="628" src="https://dist.neo4j.com/wp-content/uploads/20260129081039/agentic-ai-vs-generative-ai.png" class="attachment-full size-full wp-post-image" alt="" decoding="async" loading="lazy" srcset="https://dist.neo4j.com/wp-content/uploads/20260129081039/agentic-ai-vs-generative-ai.png 1200w, https://dist.neo4j.com/wp-content/uploads/20260129081039/agentic-ai-vs-generative-ai-300x157.png 300w, https://dist.neo4j.com/wp-content/uploads/20260129081039/agentic-ai-vs-generative-ai-1024x536.png 1024w, https://dist.neo4j.com/wp-content/uploads/20260129081039/agentic-ai-vs-generative-ai-150x79.png 150w, https://dist.neo4j.com/wp-content/uploads/20260129081039/agentic-ai-vs-generative-ai-768x402.png 768w, https://dist.neo4j.com/wp-content/uploads/20260129081039/agentic-ai-vs-generative-ai-600x314.png 600w" sizes="auto, (max-width: 1200px) 100vw, 1200px" /></div>
<div class='wp-block-neo4j-blog-card__content'>
<div class="wp-block-neo4j-limited-terms">
<ul class='wp-block-neo4j-limited-terms__list'>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-agentic-ai'
							   href="https://neo4j.com/blog/agentic-ai/">Agentic AI</a>
											</li>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-genai'
							   href="https://neo4j.com/blog/genai/">GenAI</a>
											</li>
</ul>
</div>
<h2 class='wp-block-neo4j-blog-card__title has-xl-font-size'>
		Agentic AI vs. Generative AI: Why Agents Need Memory, Context, and Guardrails	</h2>
<p>	<a href='https://neo4j.com/blog/agentic-ai/agentic-ai-vs-generative-ai/' class="wp-block-neo4j-reading-time"><br />
		22 min read	</a></p>
</div></div>
</div><div class="swiper-slide">
<div class="wp-block-neo4j-blog-card">
<div class="wp-block-neo4j-blog-card__featured-image" >
	<img width="1024" height="530" src="https://dist.neo4j.com/wp-content/uploads/20260123074624/neo4j-mcp-architecture.png" class="attachment-full size-full wp-post-image" alt="" decoding="async" loading="lazy" srcset="https://dist.neo4j.com/wp-content/uploads/20260123074624/neo4j-mcp-architecture.png 1024w, https://dist.neo4j.com/wp-content/uploads/20260123074624/neo4j-mcp-architecture-300x155.png 300w, https://dist.neo4j.com/wp-content/uploads/20260123074624/neo4j-mcp-architecture-150x78.png 150w, https://dist.neo4j.com/wp-content/uploads/20260123074624/neo4j-mcp-architecture-768x398.png 768w, https://dist.neo4j.com/wp-content/uploads/20260123074624/neo4j-mcp-architecture-600x311.png 600w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /></div>
<div class='wp-block-neo4j-blog-card__content'>
<div class="wp-block-neo4j-limited-terms">
<ul class='wp-block-neo4j-limited-terms__list'>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-developer'
							   href="https://neo4j.com/blog/developer/">Developer</a>
											</li>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-genai'
							   href="https://neo4j.com/blog/genai/">GenAI</a>
											</li>
</ul>
</div>
<h2 class='wp-block-neo4j-blog-card__title has-xl-font-size'>
		Getting Started With MCP Servers: A Technical Deep Dive	</h2>
<p>	<a href='https://neo4j.com/blog/developer/model-context-protocol/' class="wp-block-neo4j-reading-time"><br />
		15 min read	</a></p>
</div></div>
</div><div class="swiper-slide">
<div class="wp-block-neo4j-blog-card">
<div class="wp-block-neo4j-blog-card__featured-image" >
	<img decoding="async" src="https://neo4j.com/wp-content/themes/neo4jweb/assets/images/blog-card-default-3.jpg" alt="Powering India’s AI Future with Graph Intelligence"></div>
<div class='wp-block-neo4j-blog-card__content'>
<div class="wp-block-neo4j-limited-terms">
<ul class='wp-block-neo4j-limited-terms__list'>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-genai'
							   href="https://neo4j.com/blog/genai/">GenAI</a>
											</li>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-graph-database'
							   href="https://neo4j.com/blog/graph-database/">Graph Database</a>
											</li>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-knowledge-graph'
							   href="https://neo4j.com/blog/knowledge-graph/">Knowledge Graph</a>
											</li>
</ul>
</div>
<h2 class='wp-block-neo4j-blog-card__title has-xl-font-size'>
		Powering India’s AI Future with Graph Intelligence	</h2>
<p>	<a href='https://neo4j.com/blog/graph-database/powering-indias-ai-future-with-graph-intelligence/' class="wp-block-neo4j-reading-time"><br />
		5 min read	</a></p>
</div></div>
</div><div class="swiper-slide">
<div class="wp-block-neo4j-blog-card">
<div class="wp-block-neo4j-blog-card__featured-image" >
	<img width="1024" height="576" src="https://dist.neo4j.com/wp-content/uploads/20260126032432/1ZzZkzNlWShfRZiOt1pzi0g.png" class="attachment-full size-full wp-post-image" alt="" decoding="async" loading="lazy" srcset="https://dist.neo4j.com/wp-content/uploads/20260126032432/1ZzZkzNlWShfRZiOt1pzi0g.png 1024w, https://dist.neo4j.com/wp-content/uploads/20260126032432/1ZzZkzNlWShfRZiOt1pzi0g-300x169.png 300w, https://dist.neo4j.com/wp-content/uploads/20260126032432/1ZzZkzNlWShfRZiOt1pzi0g-150x84.png 150w, https://dist.neo4j.com/wp-content/uploads/20260126032432/1ZzZkzNlWShfRZiOt1pzi0g-768x432.png 768w, https://dist.neo4j.com/wp-content/uploads/20260126032432/1ZzZkzNlWShfRZiOt1pzi0g-600x338.png 600w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /></div>
<div class='wp-block-neo4j-blog-card__content'>
<div class="wp-block-neo4j-limited-terms">
<ul class='wp-block-neo4j-limited-terms__list'>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-agentic-ai'
							   href="https://neo4j.com/blog/agentic-ai/">Agentic AI</a>
											</li>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-genai'
							   href="https://neo4j.com/blog/genai/">GenAI</a>
											</li>
</ul>
</div>
<h2 class='wp-block-neo4j-blog-card__title has-xl-font-size'>
		Empowering Microsoft Agent Framework with Neo4j Knowledge Graphs	</h2>
<p>	<a href='https://neo4j.com/blog/genai/empowering-microsoft-agent-framework-with-neo4j-knowledge-graphs/' class="wp-block-neo4j-reading-time"><br />
		3 min read	</a></p>
</div></div>
</div><div class="swiper-slide">
<div class="wp-block-neo4j-blog-card">
<div class="wp-block-neo4j-blog-card__featured-image" >
	<img width="1200" height="628" src="https://dist.neo4j.com/wp-content/uploads/20260116093843/context-engineering-vs-prompt-engineering.png" class="attachment-full size-full wp-post-image" alt="" decoding="async" loading="lazy" srcset="https://dist.neo4j.com/wp-content/uploads/20260116093843/context-engineering-vs-prompt-engineering.png 1200w, https://dist.neo4j.com/wp-content/uploads/20260116093843/context-engineering-vs-prompt-engineering-300x157.png 300w, https://dist.neo4j.com/wp-content/uploads/20260116093843/context-engineering-vs-prompt-engineering-1024x536.png 1024w, https://dist.neo4j.com/wp-content/uploads/20260116093843/context-engineering-vs-prompt-engineering-150x79.png 150w, https://dist.neo4j.com/wp-content/uploads/20260116093843/context-engineering-vs-prompt-engineering-768x402.png 768w, https://dist.neo4j.com/wp-content/uploads/20260116093843/context-engineering-vs-prompt-engineering-600x314.png 600w" sizes="auto, (max-width: 1200px) 100vw, 1200px" /></div>
<div class='wp-block-neo4j-blog-card__content'>
<div class="wp-block-neo4j-limited-terms">
<ul class='wp-block-neo4j-limited-terms__list'>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-genai'
							   href="https://neo4j.com/blog/genai/">GenAI</a>
											</li>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-knowledge-graph'
							   href="https://neo4j.com/blog/knowledge-graph/">Knowledge Graph</a>
											</li>
</ul>
</div>
<h2 class='wp-block-neo4j-blog-card__title has-xl-font-size'>
		Why AI Teams Are Moving From Prompt Engineering to Context Engineering	</h2>
<p>	<a href='https://neo4j.com/blog/genai/context-engineering-vs-prompt-engineering/' class="wp-block-neo4j-reading-time"><br />
		19 min read	</a></p>
</div></div>
</div><div class="swiper-slide">
<div class="wp-block-neo4j-blog-card">
<div class="wp-block-neo4j-blog-card__featured-image" >
	<img width="1024" height="1024" src="https://dist.neo4j.com/wp-content/uploads/20260115124013/1FnSflzXExvs-17SPIhrphQ.png" class="attachment-full size-full wp-post-image" alt="" decoding="async" loading="lazy" srcset="https://dist.neo4j.com/wp-content/uploads/20260115124013/1FnSflzXExvs-17SPIhrphQ.png 1024w, https://dist.neo4j.com/wp-content/uploads/20260115124013/1FnSflzXExvs-17SPIhrphQ-300x300.png 300w, https://dist.neo4j.com/wp-content/uploads/20260115124013/1FnSflzXExvs-17SPIhrphQ-150x150.png 150w, https://dist.neo4j.com/wp-content/uploads/20260115124013/1FnSflzXExvs-17SPIhrphQ-768x768.png 768w, https://dist.neo4j.com/wp-content/uploads/20260115124013/1FnSflzXExvs-17SPIhrphQ-600x600.png 600w" sizes="auto, (max-width: 1024px) 100vw, 1024px" /></div>
<div class='wp-block-neo4j-blog-card__content'>
<div class="wp-block-neo4j-limited-terms">
<ul class='wp-block-neo4j-limited-terms__list'>
<li class='wp-block-neo4j-limited-terms__term'>
													<a class='wp-element-button wp-block-neo4j-limited-terms__link neo4j-term-genai'
							   href="https://neo4j.com/blog/genai/">GenAI</a>
											</li>
</ul>
</div>
<h2 class='wp-block-neo4j-blog-card__title has-xl-font-size'>
		Hands On With Context Graphs And Neo4j	</h2>
<p>	<a href='https://neo4j.com/blog/genai/hands-on-with-context-graphs-and-neo4j/' class="wp-block-neo4j-reading-time"><br />
		11 min read	</a></p>
</div></div>
</div>			</div>
		</div>
	</div>
</div>
			</div>
		</main>

	

<footer data-c="footer navigation">
  
<div id="footer-v2" class="bg-baltic-80 text-white pb-16 text-sm">
  <style>
  /* #get-started-free mobile */
  #get-started-free {
    position: relative;
    overflow: hidden;
    z-index: 3;
    background-color: #0A6190;
    text-align: center;
  }

  #get-started-free .started-bg-left {
    left: 0;
    position: absolute;
    top: 0;
    height: 100%;
    z-index: -1;
  }
  
  #get-started-free .started-bg-right {
    right: 0;
    position: absolute;
    top: 0;
    height: 100%;
    z-index: -1;
  }

  /* #get-started-free desktop */
  @media screen and (min-width: 767px) {
    #get-started-free .started-bg-left {
      left: 57%;
    }

    #get-started-free .started-bg-right {
      right: 57%;
    }
  }
</style>

<section id="get-started-free">
  <div class="grid-container">
    <div class="grid-x align-center items-center">
      <img loading="lazy" class="started-bg-right show-for-medium" src="https://dist.neo4j.com/wp-content/uploads/20230921083327/homepage-viz_ART-left.svg" alt="" aria-hidden="true" />
      <img loading="lazy" class="started-bg-left show-for-medium" src="https://dist.neo4j.com/wp-content/uploads/20230921083329/homepage-viz_ART-right.svg" alt="" aria-hidden="true" />
      <img loading="lazy" class="started-bg-left hide-for-medium" src="https://dist.neo4j.com/wp-content/uploads/20230921082858/homepage-viz_left-side-art_375.svg" alt="" aria-hidden="true" />
      <img loading="lazy" class="started-bg-right hide-for-medium" src="https://dist.neo4j.com/wp-content/uploads/20230921082910/homepage-viz_right-side-art_375.svg" alt="" aria-hidden="true" />

      <div class="cell small-12 medium-6 text-white">
        <h2 class="mb-0">Build Intelligent Apps Easily</h2>
        <p class="section-subtitle">Transform your data into knowledge to build smart, accurate, and adaptive applications.</p>
        <a href="/product/auradb/" class="button hollow mt-8 section-subtitle py-2 px-8" style="color: #fff;background-color:transparent; font-weight: bold;border-radius: 4px;border: 1px solid #FFF;padding: 12px 24px;">Start Building</a>
      </div>
    </div>
  </div>
</section>
  <div class="grid-container flex flex-col gap-y-8">
    <div id="top-footer-section" class="grid-x grid-padding-y grid-margin-y">
      <!-- Products column -->
      <div class="cell small-12 medium-3 flex flex-col gap-y-3">

        <div class="uppercase font-bold">Products</div>
        <ul class="list-none m-0 mb-4">
          <li class="mb-2"><a data-l="Neo4j AuraDB" class="leading-6" href="/product/auradb/">Neo4j AuraDB</a></li>
          <li class="mb-2"><a data-l="Neo4j Graph Database" class="leading-6" href="/product/neo4j-graph-database/">Neo4j Graph Database</a></li>  
          <li class="mb-2"><a data-l="Neo4j Graph Analytics" class="leading-6" href="/product/aura-graph-analytics/">Neo4j Graph Analytics</a></li>
          <li class="mb-2"><a data-l="Neo4j Graph Data Science" class="leading-6" href="/product/graph-data-science/">Neo4j Graph Data Science</a></li>
          <li class="mb-2"><a data-l="Neo4j Fleet Manager" class="leading-6" href="/product/fleet-manager/">Neo4j Fleet Manager</a></li>
          <li class="mb-2"><a data-l="Neo4j Bloom" class="leading-6" href="/product/bloom/">Neo4j Bloom</a></li>
          <li class="mb-2"><a data-l="Cypher Query Language" class="leading-6" href="/product/cypher-graph-query-language/">Cypher Query Language</a></li>
          <li class="mb-2"><a data-l="Neo4j GraphQL" class="leading-6" href="/product/graphql-library/">Neo4j GraphQL</a></li>
          <li class="mb-2"><a data-l="Pricing" class="leading-6" href="/pricing/">Pricing</a></li>
          <li class="mb-2"><a data-l="Neo4j Community Edition" class="leading-6" href="/product/community-edition/">Neo4j Community Edition</a></li>
        </ul>
        
        <div class="uppercase font-bold">Use Cases</div>
        <ul class="list-none m-0 mb-4">
          <li class="mb-2"><a data-l="AI Systems" class="leading-6" href="/use-cases/ai-systems/">AI Systems</a></li>
          <li class="mb-2"><a data-l="Generative AI" class="leading-6" href="/generativeai/">Generative AI</a></li>
          <li class="mb-2"><a data-l="Knowledge Graphs" class="leading-6" href="/use-cases/knowledge-graph/">Knowledge Graphs</a></li>
           <li class="mb-2"><a data-l="Pattern Matching" class="leading-6" href="/use-cases/pattern-matching/">Pattern Matching</a></li>
          <li class="mb-2"><a data-l="Industries & Use Cases" class="leading-6" href="/use-cases/">Industries & Use Cases</a></li>
          <li class="mb-2"><a data-l="Case Studies" class="leading-6" href="https://neo4j.com/customer-stories/">Case Studies</a></li>
        </ul>
      </div>
      <div class="cell small-12 medium-3 flex flex-col gap-y-3">
        
        <!-- Developers -->
        <div class="uppercase font-bold">Developers</div>
        <ul class="list-none m-0 mb-4">
          <li class="mb-2"><a data-l="Developer Home" class="leading-6" href="/developer/">Developer Home</a></li>
          <li class="mb-2"><a data-l="Documentation" class="leading-6" href="/docs/">Documentation</a></li>
          <li class="mb-2"><a data-l="Deployment Center" class="leading-6" href="/deployment-center/">Deployment Center</a></li>
          <li class="mb-2"><a data-l="Developer Blog" class="leading-6" href="/blog/developer/">Developer Blog</a></li>
          <li class="mb-2"><a data-l="Community" class="leading-6" href="https://community.neo4j.com/" target="_blank">Community</a></li>
          <li class="mb-2"><a data-l="Virtual Events" class="leading-6" href="/events/?_event_type=virtual">Virtual Events</a></li>
          <li class="mb-2"><a data-l="GraphAcademy" class="leading-6" href="https://graphacademy.neo4j.com/" target="_blank">GraphAcademy</a></li>
          <li class="mb-2"><a data-l="Release Notes" class="leading-6" href="/release-notes/">Release Notes</a></li>
        </ul>
        <!-- Data Scientists -->
        <div class="uppercase font-bold">Data Scientists</div>
        <ul class="list-none m-0 mb-4">
          <li class="mb-2"><a data-l="Graph Data Science Home" class="leading-6" href="/product/graph-data-science/">Graph Data Science Home</a></li>
          <li class="mb-2"><a data-l="Data Science Documentation" class="leading-6" href="/docs/graph-data-science/current/">Data Science Documentation</a></li>
          <li class="mb-2"><a data-l="Get Started with Graph Data Science" class="leading-6" href="/graph-data-science-software/">Get Started with Graph Data Science</a></li>
          <li class="mb-2"><a data-l="Data Science Community" class="leading-6" href="https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/73" target="_blank">Data Science Community</a></li>
          <li class="mb-2"><a data-l="GraphAcademy for Data Science" class="leading-6" href="https://graphacademy.neo4j.com/categories/data-scientist/" target="_blank">GraphAcademy for Data Science</a></li>
        </ul>
      </div>

      <div class="cell small-12 medium-3 flex flex-col gap-y-3">
        
        <!-- Learn column -->
        <div class="uppercase font-bold">Learn</div>
        <ul class="list-none m-0 mb-4">
          <li class="mb-2"><a data-l="resources" class="leading-6" href="/resources/">Resource Library</a></li>
          <li class="mb-2"><a data-l="blog" class="leading-6" href="/blog/">Neo4j Blog</a></li>
          <li class="mb-2"><a data-l="GraphAcademy" class="leading-6" href="https://graphacademy.neo4j.com/" target="_blank">GraphAcademy</a></li>
          <li class="mb-2"><a data-l="Research Center" class="leading-6" href="/research/">Research Center</a></li>
          <li class="mb-2"><a data-l="Case Studies" class="leading-6" href="/customer-stories/">Case Studies</a></li>
          <li class="mb-2"><a data-l="Neo4j Video Hub" class="leading-6" href="/videos/">Neo4j Video Hub</a></li>
          <li class="mb-2"><a data-l="Neo4j Events Hub" class="leading-6" href="/events/">Neo4j Events Hub</a></li>
          <li class="mb-2"><a data-l="GraphSummit" class="leading-6" href="/graphsummit/">GraphSummit</a></li>
          <li class="mb-2"><a data-l="Nodes" class="leading-6" href="/nodes-2025/">NODES</a></li>
          <li class="mb-2"><a data-l="Webinars" class="leading-6" href="/webinars/">Webinars</a></li>
          <li class="mb-2"><a data-l="GraphRAG" class="leading-6" href="https://graphrag.com/" target="_blank">GraphRAG</a></li>
        </ul>
        <!-- Partners -->
        <div class="uppercase font-bold">Partners</div>
        <ul class="list-none m-0 mb-4">
          <li class="mb-2"><a data-l="Find a Partner" class="leading-6" href="/partners/directory/">Find a Partner</a></li>
          <li class="mb-2"><a data-l="Become a Partner" class="leading-6" href="/partners/neo4j-partner-program/">Become a Partner</a></li>
          <li class="mb-2"><a data-l="Solution Partners" class="leading-6" href="/partners/solution-partners/">Solution Partners</a></li>
          <li class="mb-2"><a data-l="OEM Partners" class="leading-6" href="/partners/oem-partners/">OEM Partners</a></li>
          <li class="mb-2"><a data-l="Technology Partners" class="leading-6" href="/partners/technology-partners/">Technology Partners</a></li>
          <li class="mb-2"><a data-l="Partner Portal Login" class="leading-6" href="https://neo4j.my.site.com/Neo4jPartnerCommunity" target="_blank">Partner Portal Login</a></li>
        </ul>
      </div>

      <!-- About column -->
      <div class="cell small-12 medium-3 flex flex-col gap-y-3">
        <!-- company -->
        <div class="uppercase font-bold">Company</div>
        <ul class="list-none m-0 mb-4">
          <li class="mb-2"><a data-l="company" class="leading-6" href="/company/">About Us</a></li>
          <li class="mb-2"><a data-l="newsroom" class="leading-6" href="/news/">Newsroom</a></li>
          <li class="mb-2"><a data-l="awards and honors" class="leading-6" href="/awards/">Awards and Honors</a></li>
          <li class="mb-2"><a data-l="Graphs4Good" class="leading-6" href="/graphs4good/">Graphs4Good</a></li>
          <li class="mb-2"><a data-l="careers" class="leading-6" href="/careers/">Careers</a></li>
          <li class="mb-2"><a data-l="culture" class="leading-6" href="/culture/">Culture</a></li>
          <li class="mb-2"><a data-l="staff" class="leading-6" href="/leadership/">Leadership</a></li>
          <li class="mb-2"><a data-l="support" class="leading-6" href="https://support.neo4j.com/s/" target="_blank">Support</a></li>
          <li class="mb-2"><a data-l="trust center" class="leading-6" href="https://trust.neo4j.com/" target="_blank">Trust Center</a></li>
        </ul>
        <div class="uppercase font-bold"><a class="font-bold" data-l="contact us" href="/contact-us/?ref=footer">Contact Us →</a></div>
        <div>
          <ul class="list-none m-0 mb-4">
            <li class="leading-6 mb-2">US: <a data-l="US phone" href="tel:1-855-636-4532">1-855-636-4532</a></li>
            <li class="leading-6 mb-2">Sweden: <a data-l="Sweden phone" href="tel:+46 171 480 113">+46 171 480 113</a></li>
            <li class="leading-6 mb-2">UK: <a data-l="UK phone" href="tel:+44 20 3868 3223">+44 20 3868 3223</a></li>
            <li class="leading-6 mb-2">France: <a data-l="France phone" href="tel:+33 (0) 1 88 46 13 20">+33 (0) 1 88 46 13 20</a></li>            
            <li class="leading-6 mb-2">Singapore: <a data-l="Singapore phone" href="tel:+65 6859 0336">+65 6859 0336</a></li>
            <li class="leading-6 mb-2">Australia: <a data-l="Australia phone" href="tel:+61 2 8395 2895">+61 2 8395 2895</a></li>
        </div>
        <div id="social-icons">
          <div class="uppercase font-bold mb-4">Social Networks</div>
          <a data-l="linkedin icon" href="https://www.linkedin.com/company/neo4j" target="_blank" rel="noopener">
            <div class="bg-baltic-55 rounded-full p-2 mr-1 inline-flex justify-center">
              <i style="height: 14px; width: 14px" class="n-icon n-icon-linkedin n-icon-white"></i>
            </div>
          </a>

          <a data-l="twitter icon" href="https://x.com/neo4j" target="_blank" rel="noopener">
            <div class="bg-baltic-55 rounded-full p-2 mr-1 inline-flex justify-center">
              <i style="height: 14px; width: 14px" class="n-icon n-icon-twitter-x n-icon-white"></i>
            </div>
          </a>

          <a data-l="youtube icon" href="https://youtube.com/neo4j" target="_blank" rel="noopener">
            <div class="bg-baltic-55 rounded-full p-2 mr-1 inline-flex justify-center">
              <i style="height: 14px; width: 14px" class="n-icon n-icon-youtube n-icon-white"></i>
            </div>
          </a>

          <a data-l="facebook icon" href="https://www.facebook.com/neo4j.graph.database" target="_blank" rel="noopener">
            <div class="bg-baltic-55 rounded-full p-2 mr-1 inline-flex justify-center">
              <i style="height: 14px; width: 14px" class="n-icon n-icon-facebook n-icon-white"></i>
            </div>
          </a>

          <a data-l="community icon" href="https://community.neo4j.com" target="_blank"
            rel="noopener">
            <div class="bg-baltic-55 rounded-full p-2 inline-flex justify-center">
              <i style="height: 14px; width: 14px" class="n-icon n-icon-conversation-text n-icon-white"></i>
            </div>
          </a>

          <a data-l="github icon" href="https://github.com/neo4j" target="_blank" rel="noopener">
            <div class="bg-baltic-55 rounded-full p-2 inline-flex justify-center">
              <i style="height: 14px; width: 14px" class="n-icon n-icon-github n-icon-white"></i>
            </div>
          </a>
        </div>
      </div>
      
    </div>

    <div id="bottom-footer-section" class="grid-x grid-padding-y">
      <div class="cell small-12 medium-3">
        <div>&#169; <span id="footer-copyright-year">2026</span> Neo4j, Inc.
        </div>
        <div>
          <a data-l="terms" href="https://legal.neo4j.com/#website-terms-of-use">Terms</a> | <a data-l="privacy" href="https://legal.neo4j.com/#privacy-policy">Privacy Policy</a> | <a
            data-l="sitemap" href="/sitemap/">Sitemap</a>
            <br>
            <a data-l="corruption" href="https://assets.neo4j.com/Neo4j_Anti-Corruption_Policy.pdf" target="_blank">Anti-Corruption Policy</a>
        </div>
      </div>
      <div class="cell small-12 medium-9">
        Neo4j®, Neo Technology®, Cypher®, Neo4j® Bloom™, Neo4j® AuraDS™ and Neo4j® AuraDB™ are registered trademarks
        of Neo4j, Inc. All other marks are owned by their respective companies.
      </div>
    </div>
  </div>
  <div class="hidden show-for-large contact-us-btn-container" style="position: fixed; right: 1rem; bottom: 0rem;">
    <a href="/contact-us/" style="color: white; text-decoration: none" class="contact-us-btn button"><img class="mr-1" style="filter: brightness(0) invert(1); vertical-align: bottom; padding-bottom: 1px; margin-left: -1px;" src="https://dist.neo4j.com/wp-content/uploads/20210608133508/icon-tooltip-info.svg" alt="" aria-hidden="true"> Contact Us</a>
  </div>
</div>
</div>
</footer>


<a class="exit-off-canvas"></a>
</div>
</div>
<script type="speculationrules">
{"prefetch":[{"source":"document","where":{"and":[{"href_matches":"/*"},{"not":{"href_matches":["/wp-*.php","/wp-admin/*","/wp-content/uploads/*","/wp-content/*","/wp-content/plugins/*","/wp-content/themes/neo4jweb/*","/*\\?(.+)"]}},{"not":{"selector_matches":"a[rel~=\"nofollow\"]"}},{"not":{"selector_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]}
</script>
		<script>
		( function ( body ) {
			'use strict';
			body.className = body.className.replace( /\btribe-no-js\b/, 'tribe-js' );
		} )( document.body );
		</script>
		<script type="importmap" id="wp-importmap">
{"imports":{"@wordpress/interactivity":"https://neo4j.com/wp-includes/js/dist/script-modules/interactivity/index.min.js?ver=8964710565a1d258501f"}}
</script>
<script type="module" src="https://neo4j.com/wp-includes/js/dist/script-modules/block-library/navigation/view.min.js?ver=b0f909c3ec791c383210" id="@wordpress/block-library/navigation/view-js-module" fetchpriority="low" data-wp-router-options="{&quot;loadOnClientNavigation&quot;:true}"></script>
<link rel="modulepreload" href="https://neo4j.com/wp-includes/js/dist/script-modules/interactivity/index.min.js?ver=8964710565a1d258501f" id="@wordpress/interactivity-js-modulepreload" fetchpriority="low">
<script> /* <![CDATA[ */var tribe_l10n_datatables = {"aria":{"sort_ascending":": activate to sort column ascending","sort_descending":": activate to sort column descending"},"length_menu":"Show _MENU_ entries","empty_table":"No data available in table","info":"Showing _START_ to _END_ of _TOTAL_ entries","info_empty":"Showing 0 to 0 of 0 entries","info_filtered":"(filtered from _MAX_ total entries)","zero_records":"No matching records found","search":"Search:","all_selected_text":"All items on this page were selected. ","select_all_link":"Select all pages","clear_selection":"Clear Selection.","pagination":{"all":"All","next":"Next","previous":"Previous"},"select":{"rows":{"0":"","_":": Selected %d rows","1":": Selected 1 row"}},"datepicker":{"dayNames":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"dayNamesShort":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"dayNamesMin":["S","M","T","W","T","F","S"],"monthNames":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthNamesShort":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthNamesMin":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"nextText":"Next","prevText":"Prev","currentText":"Today","closeText":"Done","today":"Today","clear":"Clear"}};/* ]]> */ </script><script type="text/javascript" src="https://neo4j.com/wp-content/plugins/the-events-calendar/common/build/js/user-agent.js?ver=bb8d9bdff91d9409c9afbb43cee2e70d" id="tec-user-agent"></script>
<script type="text/javascript" src="https://neo4j.com/wp-content/themes/neo4jweb/assets_v2/scripts/neo4j/dist/mixpanel.min.js?ver=20250718-1230" id="neo4j-mixpanel-js" defer="defer" data-wp-strategy="defer"></script>
<script type="text/javascript" src="https://neo4j.com/wp-content/themes/neo4jweb/assets/js/dist/dist.min.js?ver=20240119-1506" id="neo_app-js" defer="defer" data-wp-strategy="defer"></script>
<script type="text/javascript" src="https://neo4j.com/wp-content/themes/neo4jweb/assets_v2/scripts/neo4j/dist/neo_codemirror.min.js?ver=20250909-1135" id="neo4j-codemirror-js" defer="defer" data-wp-strategy="defer"></script>
<script type="text/javascript" src="https://neo4j.com/wp-content/themes/neo4jweb/assets/js/dist/components/blog-single.min.js?ver=1.1" id="single-sidebar-js"></script>
<script type="text/javascript" src="https://neo4j.com/wp-content/themes/neo4jweb/assets/neo4j-react-modules-assets/search-preact/bundle.80619a01.js?ver=6.9" id="/var/www/wp-content/themes/neo4jweb/assets/neo4j-react-modules-assets/search-preact/bundle.80619a01.js-js" defer="defer" data-wp-strategy="defer"></script>
<script type="module" fetchpriority="low" src="https://neo4j.com/wp-content/themes/neo4jweb/assets/js/dist/components/site-animations.min.js?ver=1770082058" id="site-animations-js" defer="defer" data-wp-strategy="defer"></script>
<script type="text/javascript" src="https://neo4j.com/wp-content/themes/neo4jweb/assets/js/dist/components/sticky-group-offsets.min.js?ver=1770082024" id="neo4j-sticky-group-offsets-js"></script>
<script type="text/javascript" src="https://neo4j.com/wp-content/themes/neo4jweb/assets/js/dist/components/navigation.min.js?ver=20240801-1730" id="neo4j-nav-js" defer="defer" data-wp-strategy="defer"></script>
<script type="text/javascript" src="https://neo4j.com/wp-content/themes/neo4jweb/assets/js/dist/components/code.min.js?ver=1770082024" id="neo4j-expand-core-code-block-js"></script>
<script type="text/javascript" src="https://neo4j.com/wp-content/plugins/neo4j-blocks/build/blocks/blog/blog-related-posts/view.js?ver=5afcac61b0804d8099f4" id="neo4j-blog-related-posts-view-script-js" defer="defer" data-wp-strategy="defer"></script>
<script id="wp-emoji-settings" type="application/json">
{"baseUrl":"https://s.w.org/images/core/emoji/17.0.2/72x72/","ext":".png","svgUrl":"https://s.w.org/images/core/emoji/17.0.2/svg/","svgExt":".svg","source":{"concatemoji":"https://neo4j.com/wp-includes/js/wp-emoji-release.min.js?ver=6.9"}}
</script>
<script type="module">
/* <![CDATA[ */
/*! This file is auto-generated */
const a=JSON.parse(document.getElementById("wp-emoji-settings").textContent),o=(window._wpemojiSettings=a,"wpEmojiSettingsSupports"),s=["flag","emoji"];function i(e){try{var t={supportTests:e,timestamp:(new Date).valueOf()};sessionStorage.setItem(o,JSON.stringify(t))}catch(e){}}function c(e,t,n){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);t=new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data);e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(n,0,0);const a=new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data);return t.every((e,t)=>e===a[t])}function p(e,t){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);var n=e.getImageData(16,16,1,1);for(let e=0;e<n.data.length;e++)if(0!==n.data[e])return!1;return!0}function u(e,t,n,a){switch(t){case"flag":return n(e,"\ud83c\udff3\ufe0f\u200d\u26a7\ufe0f","\ud83c\udff3\ufe0f\u200b\u26a7\ufe0f")?!1:!n(e,"\ud83c\udde8\ud83c\uddf6","\ud83c\udde8\u200b\ud83c\uddf6")&&!n(e,"\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f","\ud83c\udff4\u200b\udb40\udc67\u200b\udb40\udc62\u200b\udb40\udc65\u200b\udb40\udc6e\u200b\udb40\udc67\u200b\udb40\udc7f");case"emoji":return!a(e,"\ud83e\u1fac8")}return!1}function f(e,t,n,a){let r;const o=(r="undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?new OffscreenCanvas(300,150):document.createElement("canvas")).getContext("2d",{willReadFrequently:!0}),s=(o.textBaseline="top",o.font="600 32px Arial",{});return e.forEach(e=>{s[e]=t(o,e,n,a)}),s}function r(e){var t=document.createElement("script");t.src=e,t.defer=!0,document.head.appendChild(t)}a.supports={everything:!0,everythingExceptFlag:!0},new Promise(t=>{let n=function(){try{var e=JSON.parse(sessionStorage.getItem(o));if("object"==typeof e&&"number"==typeof e.timestamp&&(new Date).valueOf()<e.timestamp+604800&&"object"==typeof e.supportTests)return e.supportTests}catch(e){}return null}();if(!n){if("undefined"!=typeof Worker&&"undefined"!=typeof OffscreenCanvas&&"undefined"!=typeof URL&&URL.createObjectURL&&"undefined"!=typeof Blob)try{var e="postMessage("+f.toString()+"("+[JSON.stringify(s),u.toString(),c.toString(),p.toString()].join(",")+"));",a=new Blob([e],{type:"text/javascript"});const r=new Worker(URL.createObjectURL(a),{name:"wpTestEmojiSupports"});return void(r.onmessage=e=>{i(n=e.data),r.terminate(),t(n)})}catch(e){}i(n=f(s,u,c,p))}t(n)}).then(e=>{for(const n in e)a.supports[n]=e[n],a.supports.everything=a.supports.everything&&a.supports[n],"flag"!==n&&(a.supports.everythingExceptFlag=a.supports.everythingExceptFlag&&a.supports[n]);var t;a.supports.everythingExceptFlag=a.supports.everythingExceptFlag&&!a.supports.flag,a.supports.everything||((t=a.source||{}).concatemoji?r(t.concatemoji):t.wpemoji&&t.twemoji&&(r(t.twemoji),r(t.wpemoji)))});
//# sourceURL=https://neo4j.com/wp-includes/js/wp-emoji-loader.min.js
/* ]]> */
</script>

<!-- end of if is_singular etc -->

</body>

</html>
<!-- Dynamic page generated in 0.526 seconds. -->