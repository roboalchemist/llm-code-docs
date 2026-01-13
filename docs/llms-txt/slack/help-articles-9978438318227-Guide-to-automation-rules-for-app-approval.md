<!-- Source: https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval -->

```html
<!DOCTYPE html><html lang="en-US" class="slackhc" data-cdn="https://a.slack-edge.com/"><head><script type="text/human">
/*

          ++++      :::::                                   LLLLL                                          KKKKK
         ++++++    :::::::                                  LLLLL                                          KKKKK
          +++++    :::::::                                  LLLLL                                          KKKKK
                   :::::::                                  LLLLL                                          KKKKK
    ++++++++++++   :::::::   ::::            sSSSSSSSSs     LLLLL       aAAAAaa AAAAA        ccccccc       KKKKK     KKKKK
   ++++++++++++++  :::::::  ::::::         SSSSSSSSSSSSSs   LLLLL     aAAAAAAAAAAAAAA      CCCCCCCCCCCc    KKKKK    KKKKK
    ++++++++++++    :::::   :::::         SSSSSS    SSSSs   LLLLL    aAAAAAAAAAAAAAAA    cCCCCCCCCCCCCCC   KKKKK  KKKKK
                                          SSSSSs            LLLLL   aAAAAa     AAAAAA    CCCCC     cCCCc   KKKKKKKKKK
   :::::   :::::    +++++++++++++          sSSSSSSSSSs      LLLLL   aAAAA       AAAAA   CCCCC              KKKKKKKKKK
  ::::::  :::::::  +++++++++++++++               sSSSSSs    LLLLL   aAAAAa     aAAAAA   CCCCCC     cCCCc   KKKKKkKKKKK
   ::::   :::::::   +++++++++++++         SSSS     SSSSSs   LLLLL    aAAAAAAAAAAAAAAA    CCCCCcccccCCCCC   KKKKK  KKKKK
          :::::::                         SSSSSSSSSSSSSs    LLLLL     aAAAAAAAAAAAAAA     cCCCCCCCCCCCC    KKKKK    KKKKK
          :::::::  +++++                    sSSSSSSSSSs     LLLLL       aAAAAaa AAAAA       CCCCCCCCc      KKKKK     KKKKK
          :::::::  ++++++
           :::::    ++++


Thanks for taking a peek! Maybe a job is what you seek?
https://slack.com/careers

*/
</script><link rel="canonical" href="https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval">

<link rel="alternate" hreflang="en-us" href="https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval"><link rel="alternate" hreflang="en-au" href="https://slack.com/intl/en-au/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval"><link rel="alternate" hreflang="en-gb" href="https://slack.com/intl/en-gb/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval"><link rel="alternate" hreflang="en-in" href="https://slack.com/intl/en-in/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval"><link rel="alternate" hreflang="fr-ca" href="https://slack.com/intl/fr-ca/help/articles/9978438318227-Guide-des-règles-d’automatisation-pour-l’approbation-des-applications"><link rel="alternate" hreflang="fr-fr" href="https://slack.com/intl/fr-fr/help/articles/9978438318227-Guide-des-règles-d’automatisation-pour-l’approbation-des-applications"><link rel="alternate" hreflang="de-de" href="https://slack.com/intl/de-de/help/articles/9978438318227-Leitfaden-zu-Automatisierungsregeln-für-App-Genehmigungen"><link rel="alternate" hreflang="es-es" href="https://slack.com/intl/es-es/help/articles/9978438318227-Guía-para-crear-reglas-de-automatización-para-la-aprobación-de-aplicaciones"><link rel="alternate" hreflang="es" href="https://slack.com/intl/es-la/help/articles/9978438318227-Guía-de-reglas-de-automatización-para-la-aprobación-de-aplicaciones"><link rel="alternate" hreflang="ja-jp" href="https://slack.com/intl/ja-jp/help/articles/9978438318227-アプリの承認のためのオートメーションルールのガイド"><link rel="alternate" hreflang="pt-br" href="https://slack.com/intl/pt-br/help/articles/9978438318227-Guia-para-regras-de-automação-na-aprovação-de-apps"><link rel="alternate" hreflang="ko-kr" href="https://slack.com/intl/ko-kr/help/articles/9978438318227-앱-승인을-위한-자동화-규칙-가이드"><link rel="alternate" hreflang="it-it" href="https://slack.com/intl/it-it/help/articles/9978438318227-Guida-alle-regole-di-automazione-per-l’approvazione-dell’app"><link rel="alternate" hreflang="zh-cn" href="https://slack.com/intl/zh-cn/help/articles/9978438318227-应用批准自动化规则指南"><link rel="alternate" hreflang="zh-tw" href="https://slack.com/intl/zh-tw/help/articles/9978438318227-應用程式核准自動化規則指南"><link rel="alternate" hreflang="x-default" href="https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval"><noscript><meta http-equiv="refresh" content="0; URL=/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval?nojsmode=1"></noscript><script type="text/javascript">var safe_hosts = ['app.optimizely.com', 'tinyspeck.dev.slack.com', 'houston-dev.tinyspeck.com', 'houston.tinyspeck.com'];

if (self !== top && safe_hosts.indexOf(top.location.host) === -1) {
	window.document.write(
		'\u003Cstyle>body * {display:none !important;}\u003C/style>\u003Ca href="#" onclick=' +
			'"top.location.href=window.location.href" style="display:block !important;padding:10px">Go to Slack.com\u003C/a>'
	);
}

(function() {
	var timer;
	if (self !== top && safe_hosts.indexOf(top.location.host) === -1) {
		timer = window.setInterval(function() {
			if (window) {
				try {
					var pageEl = document.getElementById('page');
					var clientEl = document.getElementById('client-ui');
					var sectionEls = document.querySelectorAll('nav, header, section');

					pageEl.parentNode.removeChild(pageEl);
					clientEl.parentNode.removeChild(clientEl);
					for (var i = 0; i < sectionEls.length; i++) {
						sectionEls[i].parentNode.removeChild(sectionEls[i]);
					}
					window.TS = null;
					window.TD = null;
					window.clearInterval(timer);
				} catch (e) {}
			}
		}, 200);
	}
})();</script><script>window.GA = window.GA || {};
window.GA.boot_data = window.GA.boot_data || {};
GA.boot_data.xhp = true;
GA.boot_data.version_uid = "bd6dd8487946c295416663f77e0cf729b5d79498";
GA.boot_data.environment = "prod";
GA.boot_data.abs_root_url = "https:\/\/slack.com\/";
GA.boot_data.document_referrer = "";

GA.boot_data.anonymous_visitor = false;
GA.boot_data.beacon_timing_url = "https:\/\/slack.com\/beacon\/timing";
GA.boot_data.referral_code = "";
GA.boot_data.auth_cookie_domain = ".slack.com";

GA.boot_data.geo = {"ip":"23.93.151.210","country":"US","is_in_european_union":false,"region":"CA","city":"Redwood City","zip":"94062","lat":37.4245,"lon":-122.296,"metro":807,"country_label":"United States","region_label":"California","country3":"USA","continent":"NA","isp":"Sonic.net, LLC"};
GA.boot_data.geocode = "en-us";
GA.boot_data.intl_prefix = "";
GA.boot_data.request_uri = "\/help\/articles\/9978438318227-Guide-to-automation-rules-for-app-approval";
GA.boot_data.canonical_web_url = "https:\/\/slack.com\/help\/articles\/9978438318227-Guide-to-automation-rules-for-app-approval";
GA.boot_data.i18n_locale = "en-US";
GA.boot_data.geo_root_url = "https:\/\/slack.com\/";

GA.boot_data.is_usa = true;
GA.boot_data.is_spain = false;
GA.boot_data.is_germany = false;
GA.boot_data.is_france = false;
GA.boot_data.is_japan = false;
GA.boot_data.is_europe = false;

GA.boot_data.is_latam = false;
GA.boot_data.is_brazil = false;
GA.boot_data.is_india = false;
GA.boot_data.is_uk = false;

GA.boot_data.is_english = true;
GA.boot_data.is_spanish = false;
GA.boot_data.is_german = false;
GA.boot_data.is_french = false;
GA.boot_data.is_japanese = false;
GA.boot_data.is_portuguese = false;

GA.boot_data.job_board_token = "slack";
GA.boot_data.zd_locale = "en-us";
</script><meta name="facebook-domain-verification" content="chiwsajpoybn2cnqyj9w8mvrey56m0"><script type="text/javascript">
window.dataLayer = window.dataLayer || [];
function gtag(){window.dataLayer.push(arguments);}

gtag('consent', "default", {"ad_storage":"granted","ad_user_data":"granted","ad_personalization":"granted","personalization_storage":"granted","analytics_storage":"granted","functionality_storage":"granted","security_storage":"granted","wait_for_update":1000});

function loadGTM() {
	window.dataLayer.push({
		'gtm.start': Date.now(),
		'event': 'gtm.js',
		'AnalyticsActiveGroups': ",1,2,3,4,",
		'policy_ga_only': false,
	});
	var firstScript = document.getElementsByTagName('script')[0];
	var thisScript = document.createElement('script');
	thisScript.async = true;
	thisScript.src = '//www.googletagmanager.com/gtm.js?id=GTM-KH2LPK';
	firstScript.parentNode.insertBefore(thisScript, firstScript);
}


</script><script src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js" data-document-language="true" data-domain-script="3bcd90cf-1e32-46d7-adbd-634f66b65b7d"></script><script>window.OneTrustLoaded = true;</script><script>
window.dataLayer = window.dataLayer || [];

function afterConsentScripts() {
	window.TD.analytics.doPush();

	const bottomBannerEl = document.querySelector('.c-announcement-banner-bottom');
	if (bottomBannerEl !== null) {
		bottomBannerEl.classList.remove('c-announcement-banner-bottom-invisible');
	}
}



let initOneTrustReady = false;
let intOneTrustLoaded = false;
function OptanonWrapper() {
	
	if (!intOneTrustLoaded) {
		document.dispatchEvent(new CustomEvent('OneTrustLoaded'));
		intOneTrustLoaded = true;
	}
	window.dataLayer.push({'event': 'OneTrustReady'});
	if (!initOneTrustReady) {
		document.dispatchEvent(new CustomEvent('OneTrustReady'));
		loadGTM();
		initOneTrustReady = true;
	}

	if (!Optanon.GetDomainData().ShowAlertNotice || false) {
		afterConsentScripts();
	} else {
		document.querySelector('#onetrust-accept-btn-handler').focus()
	}
	Optanon.OnConsentChanged(function() {
		afterConsentScripts();
	});

}</script><link rel="stylesheet" href="//code.jquery.com/ui/1.11.0/themes/smoothness/jquery-ui.css"><title>Guide to automation rules for app approval | Slack</title><meta name="description" content="When setting up automated app approvals for your organization, it's important to proceed with care and ensure that your rules meet any unique security requirements established by your team. Read on..."><meta property="og:type" content="website"><meta property="og:site_name" content="Slack Help Center"><meta property="og:title" content="Guide to automation rules for app approval"><meta property="og:image" content="https://a.slack-edge.com/80588/marketing/img/meta/slack_hash_256.png"><meta property="og:description" content="When setting up automated app approvals for your organization, it's important to proceed with care and ensure that your rules meet any unique security requirements established by your team. Read on..."><meta property="og:url" content="https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval"><meta name="twitter:site" content="@slackhq"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="Guide to automation rules for app approval"><meta name="twitter:description" content="When setting up automated app approvals for your organization, it's important to proceed with care and ensure that your rules meet any unique security requirements established by your team. Read on..."><meta name="twitter:image" content="https://a.slack-edge.com/80588/marketing/img/meta/slack_hash_256.png"><meta charset="utf-8"><meta name="author" content="Slack"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta name="referrer" content="origin-when-cross-origin"><link id="favicon" rel="shortcut icon" href="https://a.slack-edge.com/e6a93c1/img/icons/favicon-32.png" sizes="16x16 32x32 48x48" type="image/png"><link href="https://a.slack-edge.com/bv1-13/rollup-style-helpcenter.72c788dcb8b08ab0902b.min.css" rel="stylesheet" type="text/css" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null" crossorigin="anonymous"><script src="https://reveal.clearbit.com/v1/companies/reveal?variable=reveal&amp;authorization=pk_7144fadb90a8fdd9c89e1395ff4171a3" referrerpolicy="origin"></script><script>
if (window.reveal && window.reveal.company) {
	var r = window.reveal;
	window.clearbit_fmt = {
		cb_traffic_type: r.type,
		cb_company_name: r.company.name,
		cb_industry_tags: r.company.tags.join(', '),
		cb_industry_sector: r.company.category.sector,
		cb_industry_group:  r.company.category.industryGroup,
		cb_industry_name: r.company.category.industry,
		cb_industry_sub: r.company.category.subIndustry,
		cb_company_city: r.company.geo.city,
		cb_company_state:r.company.geo.state,
		cb_company_country: r.company.geo.country,
		cb_alexa_us: r.company.metrics.alexaUsRank,
		cb_alexa_global: r.company.metrics.alexaGlobalRank,
		cb_size_employees: r.company.metrics.employees,
		cb_size_range: r.company.metrics.employeesRange,
		cb_size_annual_revenue: r.company.metrics.annualRevenue,
		cb_size_est_revenue: r.company.metrics.estimatedAnnualRevenue,
	}
}

window.optimizely_fmt = {
	"type": "user",
	"attributes": {
		"visitor_uid" : "5690884dea5e6de0ed32aad091c59725",
		"visitor_type": "prospect",
		"is_first_visit": false,
		"traffic_type": "logged_out",	}
}
if (window.reveal && window.reveal.company) {
	window.dataLayer = window.dataLayer || [];
	window.dataLayer.push(window.clearbit_fmt);
	window.dataLayer.push({event: 'Clearbit'});
}
if (window.reveal && window.reveal.company) {
	for (var p in window.clearbit_fmt) {
		if (window.clearbit_fmt.hasOwnProperty(p)) {
			window.optimizely_fmt.attributes[p] = window.clearbit_fmt[p];
		}
	}
}window.optimizely = window.optimizely || [];
window.optimizely.push({'type':'optOut','isOptOut':false});
window.optimizely.push(window.optimizely_fmt);</script><script src="https://d34u8crftukxnk.cloudfront.net/snippets/12119108777.js"></script></head><body class=" t-octothorpe"><a class="c-button v--primary c-skip-link is-focusable v--white-bg" href="#main" data-clog-click data-clog-ui-element="link_skip" data-clog-ui-component="inc_skip_link">Skip to main content</a><div id="announce" aria-live="polite" class="u-visually-hidden"></div><header class="header category_header header_white" style=""><div class="header_logo"><a class="logo_holder" href="https://slack.com/help" data-clog-click="true" data-clog-ui-component="hc_header_nav" data-clog-ui-element="link_hc_home"><img alt="Help Center" id="logo_w" src="https://a.slack-edge.com/9b5ded/helpcenter/img/slack_help_center_monochrome_white_RGB@2x.png"><img alt="Help Center" role="presentation" id="logo_b" src="https://a.slack-edge.com/9b5ded/helpcenter/img/slack_help_center_logo.svg"></a></div><nav class="menu_nav"><a href="#" class="open_search"> </a><a href="#" data-clog-click="true" data-clog-ui-component="hc_header_nav" data-clog-ui-element="show_responsive_menu" class="open_menu">Menu</a></nav><nav class="header_nav"><div class="header_search"><form class="search" data-clog-ui-component="hc_header_nav" accept-charset="UTF-8" action="https://slack.com/help/search" method="get" role="search"><div style="display:none"><input name="utf8" type="hidden" value="✓"></div><input id="query" name="query" data-clog-ui-component="hc_header_nav" title="Search the Help Center" placeholder="Search the Help Center" data-clog-search-type="lunr" type="text"><input name="commit" type="submit" value="Search"></form></div><a href="https://slack.com/get-started?entry_point=help_center" class="create-workspace enrich_create_workspace_cta" data-clog-click="true" data-clog-ui-component="hc_header_nav" data-clog-ui-element="btn_create_workspace">Sign Up</a></nav><i class="hidden ts_icon ts_icon_times_circle ts_icon_inherit close_search"></i></header><div class="fs_menu hidden"><a href="https://slack.com/" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="link_home"><img class="fs_logo" src="https://a.slack-edge.com/34aa8/helpcenter/img/icon_slack_white.svg" alt="Help Center"></a><a href="#" data-clog-click="true" data-clog-ui-component="hc_header_nav" data-clog-ui-element="close_responsive_menu" class="close_menu" aria-label="close"><i class="ts_icon ts_icon_times ts_icon_inherit"></i></a><ul><li><a href="https://slack.com/get-started?entry_point=help_center" class="enrich_create_workspace_cta" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="btn_create_workspace">Sign Up</a></li><li><a href="https://slack.com/help/categories/360000049043" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="link_getting_started">Getting Started</a></li><li><a href="https://slack.com/help/categories/200111606" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="link_using_slack">Using Slack</a></li><li><a href="https://slack.com/help/categories/200122103" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="link_team_administration">Workspace Administration</a></li><li><a href="https://slack-status.com/" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="link_status">Slack Status</a></li></ul></div><main id="main" role="main"><section class="banner"><div class="banner_container"><h1 class="banner_title">Workspace administration</h1><p class="banner_desc">Learn how to manage your Slack workspace or Enterprise org.</p></div><div class="section_menu" id="global_menu"><ul><li><a href="https://slack.com/help/categories/360000049043">Getting Started</a><ul><li><a href="https://slack.com/help/sections/360000110083">Intro to Slack</a></li><li><a href="https://slack.com/help/sections/360000111046"> Get started: admins </a></li><li><a href="https://slack.com/help/sections/360000111026">Get started: users</a></li><li><a href="https://slack.com/help/sections/360000111066">Roles &amp; permissions</a></li></ul></li><li><a href="https://slack.com/help/categories/200111606">Using Slack</a><ul><li><a href="https://slack.com/help/sections/360000110143">Channels</a></li><li><a href="https://slack.com/help/sections/1500000005182">Direct messages</a></li><li><a href="https://slack.com/help/sections/1500002198082">Format & style messages</a></li><li><a href="https://slack.com/help/sections/360000111086">Message features &amp; tools</a></li><li><a href="https://slack.com/help/sections/360000111106">Audio &amp; video</a></li><li><a href="https://slack.com/help/sections/360000110163">Share files &amp; conversations</a></li><li><a href="https://slack.com/help/sections/360000110183">Search in Slack</a></li><li><a href="https://slack.com/help/sections/360000779752">Keyboard shortcuts &amp; accessibility</a></li></ul></li><li><a href="https://slack.com/help/categories/360000047906">Your Profile</a><ul><li><a href="https://slack.com/help/sections/360000110223">Manage your account</a></li><li><a href="https://slack.com/help/sections/360000110243">Adjust your notifications</a></li><li><a href="https://slack.com/help/sections/360000111166">Change your settings & preferences</a></li><li><a href="https://slack.com/help/sections/360000111146">Get troubleshooting tips</a></li></ul></li><li><a href="https://slack.com/help/categories/360000047926">Connect Tools</a><ul><li><a href="https://slack.com/help/sections/360000111186">Connect tools from the Slack App Directory</a></li><li><a href="https://slack.com/help/sections/360000111206">Automate tasks with Workflow Builder</a></li><li><a href="https://slack.com/help/sections/360000110263">Explore apps in the Slack App Directory</a></li><li><a href="https://slack.com/help/sections/360000111226">Create custom apps</a></li></ul></li><li><a href="https://slack.com/help/categories/200122103">Administration</a><ul><li><a href="https://slack.com/help/sections/360000110303">Manage members</a></li><li><a href="https://slack.com/help/sections/1500000019342">Manage channels</a></li><li><a href="https://slack.com/help/sections/360000111266">Manage billing, payments &amp; plans</a></li><li><a href="https://slack.com/help/sections/360000110283">Workspace settings &amp; permissions</a></li><li><a href="https://slack.com/help/sections/360000777951">Workspace customization</a></li><li><a href="https://slack.com/help/sections/1500000019001">Enterprise Grid settings &amp; permissions</a></li><li><a href="https://slack.com/help/sections/360011048274">Manage apps &amp; workflows</a></li><li><a href="https://slack.com/help/sections/360000110323">Configure access &amp; security</a></li><li><a href="https://slack.com/help/sections/360000110343">Slack data &amp; analytics</a></li></ul></li><li><a href="https://slack.com/help/categories/360000049063">Tutorials & videos</a><ul><li><a href="https://slack.com/help/sections/360012152193">Tutorials</a></li><li><a href="https://slack.com/help/sections/360000110363"> Videos </a></li><li><a href="https://slack.com/help/sections/4412760408723">Discover more</a></li></ul></li></ul></div></section><div class="hidden" id="next_prev"><option value="next">Next</option><option value="prev">Previous</option></div><div class="hidden" id="highlighting_words"><option value="highlighting">Actions,activity,access logs,accessibility,add,add an app,Add members,Add to Slack,administrators,all passwords,analytics,android,announcement,announcements,App Directory,app icon,Apple Watch,approving apps,archive,Asana,Atlassian,Automation apps,badge,billing details,billing,Bitbucket,bot user,box,browse,calls,Calls:,cancel,changes,channels,channel instantly,channel management,channel notification,channel suggestions,claim domains,close,company culture,compliance exports,compose,computers,conversations,convert,connect,connected accounts,connection,connecting,copy messages,create,customization,customize,custom SAML,custom,customer support teams,data exports,data security,deactivate,default channels,delete,deletion,deploy slack,desktop,direct messages,directory,disable,discover and join,Discovery APIs,display name,DMs,Do Not Disturb,domain,domains,downgrade,dropbox,duplicate accounts,edit,editing,education,email address,email,emoji,emoticons,Enterprise Grid,Enterprise Mobility Management,executives,export,failed payments,Fair Billing,faqs,finding,format,formatting,framework for apps,free trials,general,getting started,giphy,github integration,github organization,github,glossary,google apps,google calendar,google drive,guests,highlights,hipchat,human resources,IFTTT,import,Incoming WebHooks,integrations,ios,invite,IT teams,JIRA,join,Keep up,keyboard layout,keyboard shortcuts,Keychain Access,keyword notifications,language,languages,leave,link previews,loading,limits,links,linux,mac,manage a workspace,manage apps,manage members,marketing,mention,merge,message actions,messages are displayed,message display,microsoft products,mobile,mobile push,move channels,moving workspaces,multiple,mute,name,names,noise,nonprofits,notify,OneDrive,onboard,owners,password,payment,payments,permissions,phones,pin,plan,plans,plus plan,polls,primary ownership,privacy policies,prioritize tasks,private,private channel,private notes and files,project management,public channel,purpose,Quick Switcher,quote,reactivate,read,recruitment,referrer information,reminder,remove,rename,retention,Request a new workspace,role,roles,RSS,sales,Salesforce,SAML,SCIM,SCIM provisioning,screen reader,search,send,session duration,share messages,share,shared channel,shared channels,sidebar,sign in,sign out,signup mode,single sign-on,Slack Day,Slack for Teams,Slack notifications,Save notes and files,Service Level Agreements,ServiceNow,sign up,slack status,slackbot,slash commands,snippet,snooze,software developers,star,statistics,Stride,sync,tablets,tax,threads,time zone,tips,to-do lists,topic,triage channels,Terms of Service,Trello,troubleshoot,trouble receiving,tour,twitter,two-factor authentication,unread messages,updates,upgrade,upload,username,user groups,URL,vacation,Vendor and remittance,video,voice call,voice,what is,what's important,whitelisting,windows phone,windows,working in,workspace apps,workspace creation requests,workspace discovery,workspace's settings,wunderlist,your actions,Zapier,zoom,features,#general,File storage,posts,dark mode,theme,Workflow Builder,Voice,video,screen sharing,workflows,Outlook Calendar,Invited members,Transfer ownership,Whitelist,Enterprise Key Management,Transport Layer Security,Strong customer authentication,CSV,text file,work hours,</option></div><div class="hidden" id="search_meta"><option value="search_for">Search for “[term]”</option><option value="see_n_results">See [n]+ more results →</option></div><div class="loc_banner_container"></div><div class="article_page"><div class="article_container"><div class="article_spacer"></div><div class="article_breadcrumbs"><div class="article_breadcrumbs_container"><ol class="breadcrumbs"><li title="Slack Help Center"><a href="https://slack.com/help">Slack Help Center</a></li><li title="Workspace administration"><a href="https://slack.com/help/categories/200122103-Workspace-administration">Workspace administration</a></li><li title="Manage apps &amp; workflows"><a href="https://slack.com/section">Manage apps &amp; workflows</a></li><span class="article_breadcrumb_title">Guide to automation rules for app approval</span></ol></div></div><div class="content_col"><div><h1 class="article_title">Guide to automation rules for app approval</h1><div class="article_body"><p>When setting up <a href="https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval">automated app approvals</a> for your organization, it's important to proceed with care and ensure that your rules meet any unique <a href="https://slack.com/help/articles/360001670528-Security-recommendations-for-approving-apps">security requirements</a> established by your team. Read on for an overview of the components that make up rules and how to apply them.</p>
<p class="bug"><strong>Note:</strong> We recommend testing these features in a separate testing environment before implementing them in production. For additional support, you can <a href="https://slack.com/help/requests/new" target="_blank" rel="noopener">contact us</a> at any time.</p>
<p> </p>
<h2 id="h_01HW32C1P7M4PEQ5ESMFNQRT7J" class="anchor">How it works</h2>
<p>App installation requests can be automatically approved, restricted, dismissed, or flagged for human review based on conditions that your rules will look out for. Rules can be comprised of several rule components, which will be evaluated in the order that you determine. If the requested app meets the requirements of the rule, your predetermined resolution will be automatically applied. </p>
<p> </p>
<h2 id="h_01HW32C1P7ZHEV89RK1QY7PVQ9" class="anchor">Terms to know</h2>
<div class="boxed">
<ul>
<li>
<strong>Rule component</strong><br>Components are what a rule looks out for to determine an automated outcome.
<table style="border-collapse: collapse; width: 100%;" border="0">
<tbody>
<tr>
<td style="width: 100%;">
<p>Available components<br><span class="code_modifier">Scopes</span> <span class="code_modifier">Previous resolution</span> <span class="code_modifier">App distribution</span> <span class="code_modifier">App IDs</span></p>
</td>
</tr>
</tbody>
</table>
</li>
<li>
<strong>Conditions</strong><br>Conditional statements modify how the component and comparison interact.
<table style="border-collapse: collapse; width: 100%; height: 44px;" border="0">
<tbody>
<tr style="height: 44px;">
<td style="width: 100%; height: 44px;">
<p>Available conditions<br><span class="code_modifier">Is</span> <span class="code_modifier">Is not</span></p>
</td>
</tr>
</tbody>
</table>
</li>
<li>
<strong>Comparisons</strong><br>Comparisons are the state of the rule component. Each component has its own set of available comparisons.
<table style="border-collapse: collapse; width: 100%;" border="0">
<tbody>
<tr>
<td style="width: 100%;">
<p>Available comparisons</p>
<p><span class="code_modifier">Includes</span> <span class="code_modifier">Is empty</span> <span class="code_modifier">Approved</span> <span class="code_modifier">Restricted</span> <span class="code_modifier">Unresolved</span><br><span class="code_modifier">Internal app</span> <span class="code_modifier">Slack Marketplace approved</span> <span class="code_modifier">Specific app ID</span></p>
</td>
</tr>
</tbody>
</table>
</li>
<li>
<strong>Resolutions<br></strong>Resolutions determine how you'd like to action a requested app that contains all the elements of a rule.
<table style="border-collapse: collapse; width: 100%;" border="0">
<tbody>
<tr>
<td style="width: 100%;">
<p>Available resolutions<br><span class="code_modifier">Restrict</span> <span class="code_modifier">Approve</span> <span class="code_modifier">Cancel</span> <span class="code_modifier">Review</span></p>
</td>
</tr>
</tbody>
</table>
</li>
<li>
<strong>Rules</strong><br>The available components, conditions and comparisons are constructed into a conditional statement with a resolution, known as a rule:<br>
<table style="border-collapse: collapse; width: 100%;" border="0">
<tbody>
<tr>
<td style="width: 100%;">
<p>If <strong>any</strong> or <strong>all</strong> <span class="code_modifier">Component</span> + <span class="code_modifier">Condition</span> + <span class="code_modifier">Comparison</span></p>
<p>then <strong>Resolution</strong> = <span class="code_modifier">Restrict</span> <span class="code_modifier">Approve</span> <span class="code_modifier">Cancel</span> <span class="code_modifier">Review</span></p>
</td>
</tr>
</tbody>
</table>
</li>
</ul>
</div>
<p> </p>
<h3 id="h_01HW32C1P85KBYMR1WD4VMD1NN">Scopes</h3>
<p>Scopes are the unique <a href="https://slack.com/help/articles/115003461503-Understand-app-permissions" target="_blank" rel="noopener">set of permissions</a> that tell you what an app can access. Each app installed to your workspace has an individualized set of scopes that allow the app to function. You can find a detailed list of scopes in our <a href="https://api.slack.com/scopes" target="_blank" rel="noopener">API documentation</a>, and set a rule to resolve app requests based on what scopes are used in the app.</p>
<div class="tabs enclosed">
<p class="option" title="tab_one">Scopes Requested</p>
<p class="option" title="tab_two">Scopes Resolved</p>
<section title="tab_one">
<p>Scopes requested refers to all the scopes present in any requested app.</p>
<table style="border-collapse: collapse; height: 50px; width: 98.2853%;">
<tbody>
<tr class="white" style="height: 22px;">
<td style="width: 14.6004%; height: 10px;">
<p><strong>Comparison</strong></p>
</td>
<td class="white" style="width: 32.3332%; height: 10px;">
<p><strong>Rating list</strong></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="width: 14.6004%; height: 10px;">
<p>Includes any of those in</p>
</td>
<td style="width: 32.3332%; height: 10px;">
<p>Low risk list</p>
</td>
</tr>
<tr style="height: 22px;">
<td style="width: 14.6004%; height: 10px;">
<p>Includes only those in</p>
</td>
<td style="width: 32.3332%; height: 10px;">
<p>Medium risk list</p>
</td>
</tr>
<tr style="height: 22px;">
<td style="width: 14.6004%; height: 10px;">
<p>Is empty</p>
</td>
<td style="width: 32.3332%; height: 10px;">
<p>High risk list</p>
</td>
</tr>
<tr style="height: 22px;">
<td style="width: 14.6004%; height: 10px;">
<p>Is not empty</p>
</td>
<td style="width: 32.3332%; height: 10px;">
<p>Unrated list</p>
</td>
</tr>
</tbody>
</table>
<p><br><strong>Example</strong></p>
"If scopes requested includes any of those in high risk list, <a href="#h_01GHF2CAE68H3FCD996G1AM0X1" target="_self">restrict</a>"</section>
<section title="tab_two">
<p>Scopes resolved refers to the set of scopes in an app that has been previously requested and approved.</p>
<table style="border-collapse: collapse; height: 60px; width: 98.2853%;">
<tbody>
<tr class="white" style="height: 22px;">
<td style="width: 14.6004%; height: 10px;">
<p><strong>Comparison</strong></p>
</td>
<td class="white" style="width: 32.3332%; height: 10px;">
<p><strong>Rating list</strong></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="width: 14.6004%; height: 10px;">
<p>Includes any of those in</p>
</td>
<td style="width: 32.3332%; height: 10px;">
<p>Low risk list</p>
</td>
</tr>
<tr style="height: 44px;">
<td style="width: 14.6004%; height: 10px;">
<p>Includes only those in</p>
</td>
<td style="width: 32.3332%; height: 10px;">
<p>Medium risk list</p>
</td>
</tr>
<tr style="height: 22px;">
<td style="width: 14.6004%; height: 10px;">
<p>Is empty</p>
</td>
<td style="width: 32.3332%; height: 10px;">
<p>High risk list</p>
</td>
</tr>
<tr style="height: 22px;">
<td style="width: 14.6004%; height: 10px;">
<p>Is not empty</p>
</td>
<td style="width: 32.3332%; height: 10px;">
<p>Unrated list</p>
</td>
</tr>
</tbody>
</table>
<p><br><strong>Example</strong></p>
"If scopes resolved includes any of those in high risk list, <a href="#h_01GHF2CAE68H3FCD996G1AM0X1" target="_self">restrict</a>"</section>
</div>
<p class="tip"><strong>Tip</strong>: Before getting started, take a look at the <strong>Scope ratings</strong> tab and ensure you've <a href="https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval" target="_blank" rel="noopener">rated</a> the appropriate scopes.</p>
<h3 id="h_01HW32C1P8QT1BG0TJA0YZ1B02">Previous resolution</h3>
<p>If an app was previously requested in your workspace, you can set a rule to apply the same resolution.</p>
<div class="tabs enclosed">
<p class="option" title="tab_one">Previous resolution is</p>
<p class="option" title="tab_two">Previous resolution is not</p>
<section title="tab_one">
<table style="border-collapse: collapse; height: 88px; width: 96.8554%;">
<tbody>
<tr class="white" style="height: 22px;">
<td class="wysiwyg-text-align-left" style="height: 22px; width: 27.8001%;">
<p><strong>Condition</strong></p>
</td>
<td class="white" style="width: 122.858%; height: 22px;">
<p><strong>Comparison</strong></p>
</td>
</tr>
<tr style="height: 22px;">
<td class="wysiwyg-text-align-left" style="height: 22px; width: 27.8001%;">
<p>Is</p>
</td>
<td style="width: 122.858%; height: 22px;">
<p>Approved</p>
</td>
</tr>
<tr style="height: 22px;">
<td class="wysiwyg-text-align-left" style="height: 22px; width: 27.8001%;">
<p>Is</p>
</td>
<td style="width: 122.858%; height: 22px;">
<p>Restricted</p>
</td>
</tr>
<tr style="height: 22px;">
<td class="wysiwyg-text-align-left" style="height: 22px; width: 27.8001%;">
<p class="wysiwyg-text-align-left">Is</p>
</td>
<td style="width: 122.858%; height: 22px;">
<p>Unresolved</p>
</td>
</tr>
</tbody>
</table>
<p><br><strong>Example</strong></p>
"If previous resolution is approved, <a href="#h_01GHF2CAE68H3FCD996G1AM0X1" target="_self">approve</a>"</section>
<section title="tab_two">
<table style="border-collapse: collapse; height: 52px; width: 96.8556%; margin-left: 0px; margin-right: auto;">
<tbody>
<tr class="white" style="height: 22px;">
<td class="wysiwyg-text-align-left" style="width: 27.5672%; height: 22px;">
<p><strong>Condition</strong></p>
</td>
<td class="white" style="width: 106.321%; height: 22px;">
<p><strong>Comparison</strong></p>
</td>
</tr>
<tr style="height: 22px;">
<td class="wysiwyg-text-align-left" style="width: 27.5672%; height: 22px;">
<p>Is not</p>
</td>
<td style="width: 106.321%; height: 22px;">
<p>Approved</p>
</td>
</tr>
<tr style="height: 44px;">
<td class="wysiwyg-text-align-left" style="width: 27.5672%; height: 22px;">
<p>Is not</p>
</td>
<td style="width: 106.321%; height: 22px;">
<p>Restricted</p>
</td>
</tr>
<tr style="height: 22px;">
<td class="wysiwyg-text-align-left" style="width: 27.5672%; height: 22px;">
<p>Is not</p>
</td>
<td style="width: 106.321%; height: 22px;">
<p>Unresolved</p>
</td>
</tr>
</tbody>
</table>
<p><br><strong>Example<br></strong>"If previous resolution is not restricted, <a href="#h_01GHF2CAE68H3FCD996G1AM0X1" target="_self">approve</a>"</p>
</section>
</div>
<h3 id="h_01HW32C1P8DZ9GXQVC2KBY6YEM">App distribution</h3>
<p>Base a rule on where the app originates: either internally or from the Slack Marketplace.</p>
<div class="tabs enclosed">
<p class="option" title="tab_one">App distribution is</p>
<p class="option" title="tab_two">App distribution is not</p>
<section title="tab_one">
<table style="border-collapse: collapse; height: 54px; width: 98.2853%;">
<tbody>
<tr class="white" style="height: 22px;">
<td style="width: 1.42857%; height: 22px;">
<p><strong>Condition</strong></p>
</td>
<td class="white" style="width: 12.9908%; height: 22px;">
<p><strong>Comparison</strong></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="height: 10px; width: 1.42857%;">
<p>Is</p>
</td>
<td style="width: 12.9908%; height: 10px;">
<p>An internal app</p>
</td>
</tr>
<tr style="height: 22px;">
<td style="width: 1.42857%; height: 22px;">
<p>Is</p>
</td>
<td style="width: 12.9908%; height: 22px;">
<p>Slack Marketplace approved</p>
</td>
</tr>
</tbody>
</table>
<p><br><strong>Example<br></strong>"If app requested is an internal app, <a href="#h_01GHF2CAE68H3FCD996G1AM0X1" target="_self">send for review</a>"</p>
</section>
<section title="tab_two">
<table style="border-collapse: collapse; height: 54px; width: 98.2853%;">
<tbody>
<tr class="white" style="height: 22px;">
<td style="width: 1.42857%; height: 22px;">
<p><strong>Condition</strong></p>
</td>
<td class="white" style="width: 12.9908%; height: 22px;">
<p><strong>Comparison</strong></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="height: 10px; width: 1.42857%;">
<p>Is not</p>
</td>
<td style="width: 12.9908%; height: 10px;">
<p>An internal app</p>
</td>
</tr>
<tr style="height: 44px;">
<td style="width: 1.42857%; height: 22px;">
<p>Is not</p>
</td>
<td style="width: 12.9908%; height: 22px;">
<p>Slack Marketplace approved</p>
</td>
</tr>
</tbody>
</table>
<p><br><strong>Example<br></strong>"If app requested is not Slack Marketplace approved, <a href="#h_01GHF2CAE68H3FCD996G1AM0X1" target="_self">send for review</a>"</p>
</section>
</div>
<h3 id="h_01HW32C1P8D2PZ49YRFT7F0TG4">App IDs</h3>
<p>Create a rule to approve specific apps based on their unique app IDs. </p>
<div class="tabs enclosed">
<p class="option" title="tab_one">App ID is</p>
<section title="tab_one">
<table style="height: 22px; width: 98.2853%;">
<tbody>
<tr class="white" style="height: 22px;">
<td style="width: 1.42857%; height: 12px;">
<p><strong>Condition</strong></p>
</td>
<td style="width: 6.8314%; height: 12px;">
<p><strong>Comparison</strong></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="width: 1.42857%; height: 10px;">
<p>Is</p>
</td>
<td style="width: 6.8314%; height: 10px;">
<p>A specific app ID</p>
</td>
</tr>
</tbody>
</table>
<p><br><strong>Example<br></strong>"If app ID is [any app ID], <a href="#h_01GHF2CAE68H3FCD996G1AM0X1" target="_self">cancel</a>"</p>
</section>
</div>
<p> </p>
<h2 id="h_01GHF2CAE68H3FCD996G1AM0X1" class="anchor">Resolutions</h2>
<p>When a requested app meets all the conditions of a rule, it will be resolved based on the set resolution and the requestor will be notified.</p>
<div class="boxed">
<ul>
<li>
<strong>Restrict</strong><br>App cannot be installed and cannot be requested again unless the scopes change.</li>
<li>
<strong>Approve</strong><br>App will be installed.</li>
<li>
<strong>Cancel<br></strong>Dismiss the request without making a decision. A new request can be made anytime.</li>
<li>
<strong>Review</strong><br>App will be sent to a human for review and approval.</li>
</ul>
</div>
<div class="boxed roles">
<strong>Who can use this feature?</strong>
<ul>
<li class="ts_icon ts_icon_user">
<strong>Workspace</strong>/<strong>Org Owners</strong>, <strong>Workspace</strong>/<strong>Org Admins</strong> and <strong>members</strong> with <a href="https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#choose-how-app-requests-work">permission to manage apps</a>
</li>
<li class="ts_icon ts_icon_flag">Available on <a href="https://slack.com/pricing" target="_self"><strong>all plans</strong></a>
</li>
</ul>
</div></div></div><div class="article_footer"><div class="article-vote"><div class="vote-thanks"><p><b><i class="ts_icon ts_icon_happy_smile"></i> Awesome!</b></p><p>Thanks so much for your feedback!</p><p>If you’d like a member of our support team to respond to you, please send a note to <a href="mailto:feedback@slack.com">feedback@slack.com</a>.</p></div><div class="feedback-thanks"><p><b><i class="ts_icon ts_icon_check_circle_o_large"></i>Got it!</b></p><p>If you’d like a member of our support team to respond to you, please send a note to <a href="mailto:feedback@slack.com">feedback@slack.com</a>.</p></div><div class="article-vote-controls"><form id="voteForm" action="#" method="get" accept-charset="UTF-8"><input type="hidden" name="article_id" value="9978438318227"><span class="article-vote-question" data-guide="Was this guide helpful?" data-video="Was this video helpful?">Was this article helpful?</span><a id="up" role="button" rel="nofollow" class="article-vote-up" title="Yes, thanks!"><span class="article-button-text">Yes, thanks!</span></a><a id="down" role="button" rel="nofollow" class="article-vote-down" title="Not really"><span class="article-button-text">Not really</span></a></form></div><div class="article-feedback-form"><form id="feedbackForm" action="#" method="get" accept-charset="UTF-8"><input type="hidden" name="article_id" value="9978438318227"><div class="article-feedback-drive vote_feedback_drivers"><span class="article-vote-question" data-guide="Was this guide helpful?" data-video="Was this video helpful?">Sorry about that! What did you find most unhelpful?</span><label for="feedback_drive-1"><input type="radio" name="vote_feedback_drivers" id="feedback_drive-1" value="helpfulness"><span>This article didn’t answer my questions or solve my problem</span></label><label for="feedback_drive-2"><input type="radio" name="vote_feedback_drivers" id="feedback_drive-2" value="readability"><span>I found this article confusing or difficult to read</span></label><label for="feedback_drive-3"><input type="radio" name="vote_feedback_drivers" id="feedback_drive-3" value="product"><span>I don’t like how the feature works</span></label><label for="feedback_drive-4"><input type="radio" name="vote_feedback_drivers" id="feedback_drive-4" value="other"><span>Other</span></label></div><textarea id="feedback_up" maxlength="600" rows="4" class="vote_feedback_up" name="vote_feedback_up" placeholder="What did you like about this article?"></textarea><textarea id="feedback_down" maxlength="600" rows="4" class="vote_feedback_down" name="vote_feedback_down" placeholder="Is there anything else you'd like to share?"></textarea><div id="char_num"><span>0</span>/600</div><script type="text/javascript">var grecaptchaWidgetId = '';
var isRecaptchaEnterpriseMigrationEnabled = true;
window.onload = function() {
// wait until grecaptcha is defined
if (typeof grecaptcha !== "undefined") {
	grecaptcha.enterprise.ready(function () {
		grecaptchaWidgetId = grecaptcha.enterprise.render('slack_captcha', {
			'sitekey': "6LcRpcIrAAAAAFAe8rv1DygnSMeBZNtDL8rhu2Ze"
		});
	});
}
};</script><script src="https://www.google.com/recaptcha/enterprise.js?render=explicit" async defer></script><div style="text-align:center"><div style="display:inline-block" id="slack_captcha"></div></div><a id="sendFeedback" role="button" rel="nofollow" title="Submit article feedback" class="article-send-feedback"><span class="article-button-text">Submit article feedback</span></a></form><p class="get-support">If you’d like a member of our support team to respond to you, please send a note to <a href="mailto:feedback@slack.com">feedback@slack.com</a>.</p></div><p class="vote-err"><i class="ts_icon ts_icon_warning"></i>Oops! We're having trouble. Please try again later!</p></div></div></div><div class="category_list" id="nav_holder"><div class="nav_scroll hidden"><div class="section_list_container"><p class="c-type-eyebrow">IN THIS ARTICLE</p><ul class="section-list" id="nav_list"></ul></div><ul class="section-list" id="cat_list"></ul></div></div></div></div></main><footer class="c-nav c-nav--expanded-footer o-content-container"><div class="c-nav--expanded-footer__supermenu"><div class="c-locale-new-overlay" id="new_locale_overlay"><div class="c-locale-new-menu" role="dialog" aria-label="Change Region"><button id="btn_close_locale" data-clog-manual role="button" class="c-locale-new-menu__close" data-clog-click aria-label="Close"><svg width="18" height="18" xmlns="http://www.w3.org/2000/svg" viewBox="-255 347 100 100" aria-hidden="true"><path d="M-160.4 434.2l-37.2-37.2 37.1-37.1-7-7-37.1 37.1-37.1-37.1-7 7 37.1 37.1-37.2 37.2 7.1 7 37.1-37.2 37.2 37.2"></path></svg></button><div id="new_locale_overlay_contents" class="c-locale-new-menu__contents"><p class="c-feature-grid__item__title">Change Region</p><p class="c-locale-new-menu__info">Selecting a different region will change the language and content of slack.com.</p><div class="c-locale-new-menu__cols"><div class="c-locale-new-menu__col"><p class="c-locale-new-menu__continent">Americas</p><a class="c-locale-new-menu__locale " href="https://slack.com/intl/es-la/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval" data-locale="es-LA" data-clog-manual data-geocode="es-la">Latinoamérica (español)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/pt-br/help/articles/9978438318227-Guia-para-regras-de-automação-na-aprovação-de-apps" data-locale="pt-BR" data-clog-manual data-geocode="pt-br">Brasil (português)</a><a class="c-locale-new-menu__locale is-selected" href="https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval" data-locale="en-US" data-clog-manual data-geocode="en-us">United States (English)</a></div><div class="c-locale-new-menu__col"><p class="c-locale-new-menu__continent">Europe</p><a class="c-locale-new-menu__locale " href="https://slack.com/intl/de-de/help/articles/9978438318227-Leitfaden-zu-Automatisierungsregeln-für-App-Genehmigungen" data-locale="de-DE" data-clog-manual data-geocode="de-de">Deutschland (Deutsch)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/es-es/help/articles/9978438318227-Guía-para-crear-reglas-de-automatización-para-la-aprobación-de-aplicaciones" data-locale="es-ES" data-clog-manual data-geocode="es-es">España (español)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/fr-fr/help/articles/9978438318227-Guide-des-règles-d’automatisation-pour-l’approbation-des-applications" data-locale="fr-FR" data-clog-manual data-geocode="fr-fr">France (français)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/it-it/help/articles/9978438318227-Guida-alle-regole-di-automazione-per-l’approvazione-dell’app" data-locale="it-IT" data-clog-manual data-geocode="it-it">Italia (italiano)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/en-gb/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval" data-locale="en-GB" data-clog-manual data-geocode="en-gb">United Kingdom (English)</a></div><div class="c-locale-new-menu__col"><p class="c-locale-new-menu__continent">Asia Pacific</p><a class="c-locale-new-menu__locale " href="https://slack.com/intl/zh-cn/help/articles/9978438318227-应用批准自动化规则指南" data-locale="zh-CN" data-clog-manual data-geocode="zh-cn">简体中文</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/zh-tw/help/articles/9978438318227-應用程式核准自動化規則指南" data-locale="zh-TW" data-clog-manual data-geocode="zh-tw">繁體中文</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/en-in/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval" data-locale="en-GB" data-clog-manual data-geocode="en-in">India (English)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/ja-jp/help/articles/9978438318227-アプリの承認のためのオートメーションルールのガイド" data-locale="ja-JP" data-clog-manual data-geocode="ja-jp">日本 (日本語)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/ko-kr/help/articles/9978438318227-앱-승인을-위한-자동화-규칙-가이드" data-locale="ko-KR" data-clog-manual data-geocode="ko-kr">대한민국 (한국어)</a></div></div></div></div></div><a id="new_locale_switcher" class="c-locale-new-switcher " href="#" data-locale="en-US" role="button" aria-haspopup="true" data-clog-click data-clog-ui-component="inc_footer_nav" data-clog-ui-element="link_locale_picker" data-qa="locale-switcher"><svg class="c-locale-new-switcher__globe" width="18" height="18" viewBox="0 0 100 100"><path d="M50.008 5.874c-11.308 0-22.613 4.3-31.219 12.906-17.211 17.211-17.211 45.226 0 62.438 17.211 17.21 45.195 17.21 62.406 0 17.212-17.212 17.243-45.227.032-62.438-8.606-8.606-19.912-12.906-31.22-12.906zm-3.125 6.125h.125v34.969H28.914c.58-10.29 4.095-20.385 10.594-28.157 2.27-2.715 4.757-4.983 7.375-6.812zm6.125 0h.062a38 38 0 0 1 7.407 6.812c6.498 7.772 10.014 17.866 10.593 28.157H53.008v-34.97zm-18.094 2.937c-7.508 8.978-11.557 20.412-12.156 32.032H11.977c.687-8.725 4.343-17.25 11.03-23.938a38.166 38.166 0 0 1 11.907-8.094zm30.219.062a38.176 38.176 0 0 1 11.812 8.063c6.685 6.685 10.369 15.19 11.063 23.906H77.227c-.598-11.59-4.623-23-12.094-31.969zm-53.156 37.97h10.78c.59 11.638 4.638 23.07 12.157 32.062a38.133 38.133 0 0 1-11.875-8.063c-6.7-6.7-10.376-15.258-11.062-24zm16.937 0h18.094V88.03h-.063c-2.644-1.838-5.146-4.135-7.437-6.875-6.512-7.787-10.025-17.876-10.594-28.188zm24.094 0H71.07c-.568 10.31-4.082 20.4-10.593 28.187-2.298 2.747-4.817 5.034-7.47 6.875V52.967zm24.219 0h10.812c-.679 8.741-4.39 17.295-11.094 24A38.07 38.07 0 0 1 65.04 85.06c.01-.011.022-.02.031-.031 7.52-8.992 11.568-20.424 12.157-32.063z"></path></svg><span>Change Region</span></a><ul class="c-nav__social_list"><li class="listitem-social"><a data-clog-click data-clog-ui-component="inc_footer_exp_nav" data-clog-ui-element="link_social_linkedin_exp_nav" aria-label="LinkedIn" title="LinkedIn" target="_blank" rel="noopener" href="https://www.linkedin.com/company/tiny-spec-inc/" data-qa="linkedin"><svg width="18" height="18" version="1" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg"><path d="M1.84613 3.69226C2.86519 3.69226 3.69226 2.86519 3.69226 1.84613C3.69226 0.827
```
