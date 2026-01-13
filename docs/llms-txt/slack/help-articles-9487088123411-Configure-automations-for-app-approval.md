<!-- Source: https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval -->

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
</script><link rel="canonical" href="https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval">

<link rel="alternate" hreflang="en-us" href="https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval"><link rel="alternate" hreflang="en-au" href="https://slack.com/intl/en-au/help/articles/9487088123411-Configure-automations-for-app-approval"><link rel="alternate" hreflang="en-gb" href="https://slack.com/intl/en-gb/help/articles/9487088123411-Configure-automations-for-app-approval"><link rel="alternate" hreflang="en-in" href="https://slack.com/intl/en-in/help/articles/9487088123411-Configure-automations-for-app-approval"><link rel="alternate" hreflang="fr-ca" href="https://slack.com/intl/fr-ca/help/articles/9487088123411-Configurer-l’automatisation-de-l’approbation-des-applications"><link rel="alternate" hreflang="fr-fr" href="https://slack.com/intl/fr-fr/help/articles/9487088123411-Configurer-l’automatisation-de-l’approbation-des-applications"><link rel="alternate" hreflang="de-de" href="https://slack.com/intl/de-de/help/articles/9487088123411-Automatisierungen-für-App-Genehmigungen-konfigurieren"><link rel="alternate" hreflang="es-es" href="https://slack.com/intl/es-es/help/articles/9487088123411-Cómo-configurar-automatizaciones-para-la-aprobación-de-aplicaciones"><link rel="alternate" hreflang="es" href="https://slack.com/intl/es-la/help/articles/9487088123411-Configurar-automaciones-para-la-aprobación-de-aplicaciones"><link rel="alternate" hreflang="ja-jp" href="https://slack.com/intl/ja-jp/help/articles/9487088123411-アプリの承認の自動化を設定する"><link rel="alternate" hreflang="pt-br" href="https://slack.com/intl/pt-br/help/articles/9487088123411-Configure-automações-para-a-aprovação-de-apps"><link rel="alternate" hreflang="ko-kr" href="https://slack.com/intl/ko-kr/help/articles/9487088123411-앱-승인을-위한-자동화-구성"><link rel="alternate" hreflang="it-it" href="https://slack.com/intl/it-it/help/articles/9487088123411-Configurare-le-automazioni-per-l’approvazione-delle-app"><link rel="alternate" hreflang="zh-cn" href="https://slack.com/intl/zh-cn/help/articles/9487088123411-配置自动化功能以批准应用安装"><link rel="alternate" hreflang="zh-tw" href="https://slack.com/intl/zh-tw/help/articles/9487088123411-設定應用程式核准自動化"><link rel="alternate" hreflang="x-default" href="https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval"><noscript><meta http-equiv="refresh" content="0; URL=/help/articles/9487088123411-Configure-automations-for-app-approval?nojsmode=1"></noscript><script type="text/javascript">var safe_hosts = ['app.optimizely.com', 'tinyspeck.dev.slack.com', 'houston-dev.tinyspeck.com', 'houston.tinyspeck.com'];

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
GA.boot_data.request_uri = "\/help\/articles\/9487088123411-Configure-automations-for-app-approval";
GA.boot_data.canonical_web_url = "https:\/\/slack.com\/help\/articles\/9487088123411-Configure-automations-for-app-approval";
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

}</script><link rel="stylesheet" href="//code.jquery.com/ui/1.11.0/themes/smoothness/jquery-ui.css"><title>Configure automations for app approval | Slack</title><meta name="description" content="By default, members can install apps without approval from a Workspace Owner, but you can choose to approve and restrict apps on a case by case basis, or you can automate the process by configuring..."><meta property="og:type" content="website"><meta property="og:site_name" content="Slack Help Center"><meta property="og:title" content="Configure automations for app approval"><meta property="og:image" content="https://a.slack-edge.com/80588/marketing/img/meta/slack_hash_256.png"><meta property="og:description" content="By default, members can install apps without approval from a Workspace Owner, but you can choose to approve and restrict apps on a case by case basis, or you can automate the process by configuring..."><meta property="og:url" content="https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval"><meta name="twitter:site" content="@slackhq"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="Configure automations for app approval"><meta name="twitter:description" content="By default, members can install apps without approval from a Workspace Owner, but you can choose to approve and restrict apps on a case by case basis, or you can automate the process by configuring..."><meta name="twitter:image" content="https://a.slack-edge.com/80588/marketing/img/meta/slack_hash_256.png"><meta charset="utf-8"><meta name="author" content="Slack"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta name="referrer" content="origin-when-cross-origin"><link id="favicon" rel="shortcut icon" href="https://a.slack-edge.com/e6a93c1/img/icons/favicon-32.png" sizes="16x16 32x32 48x48" type="image/png"><link href="https://a.slack-edge.com/bv1-13/rollup-style-helpcenter.72c788dcb8b08ab0902b.min.css" rel="stylesheet" type="text/css" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null" crossorigin="anonymous"><script src="https://reveal.clearbit.com/v1/companies/reveal?variable=reveal&amp;authorization=pk_7144fadb90a8fdd9c89e1395ff4171a3" referrerpolicy="origin"></script><script>
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
		"visitor_uid" : "b9643162bc67369adfae476b4935eeac",
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
window.optimizely.push(window.optimizely_fmt);</script><script src="https://d34u8crftukxnk.cloudfront.net/snippets/12119108777.js"></script></head><body class=" t-octothorpe"><a class="c-button v--primary c-skip-link is-focusable v--white-bg" href="#main" data-clog-click data-clog-ui-element="link_skip" data-clog-ui-component="inc_skip_link">Skip to main content</a><div id="announce" aria-live="polite" class="u-visually-hidden"></div><header class="header category_header header_white" style=""><div class="header_logo"><a class="logo_holder" href="https://slack.com/help" data-clog-click="true" data-clog-ui-component="hc_header_nav" data-clog-ui-element="link_hc_home"><img alt="Help Center" id="logo_w" src="https://a.slack-edge.com/9b5ded/helpcenter/img/slack_help_center_monochrome_white_RGB@2x.png"><img alt="Help Center" role="presentation" id="logo_b" src="https://a.slack-edge.com/9b5ded/helpcenter/img/slack_help_center_logo.svg"></a></div><nav class="menu_nav"><a href="#" class="open_search"> </a><a href="#" data-clog-click="true" data-clog-ui-component="hc_header_nav" data-clog-ui-element="show_responsive_menu" class="open_menu">Menu</a></nav><nav class="header_nav"><div class="header_search"><form class="search" data-clog-ui-component="hc_header_nav" accept-charset="UTF-8" action="https://slack.com/help/search" method="get" role="search"><div style="display:none"><input name="utf8" type="hidden" value="✓"></div><input id="query" name="query" data-clog-ui-component="hc_header_nav" title="Search the Help Center" placeholder="Search the Help Center" data-clog-search-type="lunr" type="text"><input name="commit" type="submit" value="Search"></form></div><a href="https://slack.com/get-started?entry_point=help_center" class="create-workspace enrich_create_workspace_cta" data-clog-click="true" data-clog-ui-component="hc_header_nav" data-clog-ui-element="btn_create_workspace">Sign Up</a></nav><i class="hidden ts_icon ts_icon_times_circle ts_icon_inherit close_search"></i></header><div class="fs_menu hidden"><a href="https://slack.com/" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="link_home"><img class="fs_logo" src="https://a.slack-edge.com/34aa8/helpcenter/img/icon_slack_white.svg" alt="Help Center"></a><a href="#" data-clog-click="true" data-clog-ui-component="hc_header_nav" data-clog-ui-element="close_responsive_menu" class="close_menu" aria-label="close"><i class="ts_icon ts_icon_times ts_icon_inherit"></i></a><ul><li><a href="https://slack.com/get-started?entry_point=help_center" class="enrich_create_workspace_cta" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="btn_create_workspace">Sign Up</a></li><li><a href="https://slack.com/help/categories/360000049043" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="link_getting_started">Getting Started</a></li><li><a href="https://slack.com/help/categories/200111606" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="link_using_slack">Using Slack</a></li><li><a href="https://slack.com/help/categories/200122103" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="link_team_administration">Workspace Administration</a></li><li><a href="https://slack-status.com/" data-clog-click="true" data-clog-ui-component="hc_mobile_nav" data-clog-ui-element="link_status">Slack Status</a></li></ul></div><main id="main" role="main"><section class="banner"><div class="banner_container"><h1 class="banner_title">Workspace administration</h1><p class="banner_desc">Learn how to manage your Slack workspace or Enterprise org.</p></div><div class="section_menu" id="global_menu"><ul><li><a href="https://slack.com/help/categories/360000049043">Getting Started</a><ul><li><a href="https://slack.com/help/sections/360000110083">Intro to Slack</a></li><li><a href="https://slack.com/help/sections/360000111046"> Get started: admins </a></li><li><a href="https://slack.com/help/sections/360000111026">Get started: users</a></li><li><a href="https://slack.com/help/sections/360000111066">Roles &amp; permissions</a></li></ul></li><li><a href="https://slack.com/help/categories/200111606">Using Slack</a><ul><li><a href="https://slack.com/help/sections/360000110143">Channels</a></li><li><a href="https://slack.com/help/sections/1500000005182">Direct messages</a></li><li><a href="https://slack.com/help/sections/1500002198082">Format & style messages</a></li><li><a href="https://slack.com/help/sections/360000111086">Message features &amp; tools</a></li><li><a href="https://slack.com/help/sections/360000111106">Audio &amp; video</a></li><li><a href="https://slack.com/help/sections/360000110163">Share files &amp; conversations</a></li><li><a href="https://slack.com/help/sections/360000110183">Search in Slack</a></li><li><a href="https://slack.com/help/sections/360000779752">Keyboard shortcuts &amp; accessibility</a></li></ul></li><li><a href="https://slack.com/help/categories/360000047906">Your Profile</a><ul><li><a href="https://slack.com/help/sections/360000110223">Manage your account</a></li><li><a href="https://slack.com/help/sections/360000110243">Adjust your notifications</a></li><li><a href="https://slack.com/help/sections/360000111166">Change your settings & preferences</a></li><li><a href="https://slack.com/help/sections/360000111146">Get troubleshooting tips</a></li></ul></li><li><a href="https://slack.com/help/categories/360000047926">Connect Tools</a><ul><li><a href="https://slack.com/help/sections/360000111186">Connect tools from the Slack App Directory</a></li><li><a href="https://slack.com/help/sections/360000111206">Automate tasks with Workflow Builder</a></li><li><a href="https://slack.com/help/sections/360000110263">Explore apps in the Slack App Directory</a></li><li><a href="https://slack.com/help/sections/360000111226">Create custom apps</a></li></ul></li><li><a href="https://slack.com/help/categories/200122103">Administration</a><ul><li><a href="https://slack.com/help/sections/360000110303">Manage members</a></li><li><a href="https://slack.com/help/sections/1500000019342">Manage channels</a></li><li><a href="https://slack.com/help/sections/360000111266">Manage billing, payments &amp; plans</a></li><li><a href="https://slack.com/help/sections/360000110283">Workspace settings &amp; permissions</a></li><li><a href="https://slack.com/help/sections/360000777951">Workspace customization</a></li><li><a href="https://slack.com/help/sections/1500000019001">Enterprise Grid settings &amp; permissions</a></li><li><a href="https://slack.com/help/sections/360011048274">Manage apps &amp; workflows</a></li><li><a href="https://slack.com/help/sections/360000110323">Configure access &amp; security</a></li><li><a href="https://slack.com/help/sections/360000110343">Slack data &amp; analytics</a></li></ul></li><li><a href="https://slack.com/help/categories/360000049063">Tutorials & videos</a><ul><li><a href="https://slack.com/help/sections/360012152193">Tutorials</a></li><li><a href="https://slack.com/help/sections/360000110363"> Videos </a></li><li><a href="https://slack.com/help/sections/4412760408723">Discover more</a></li></ul></li></ul></div></section><div class="hidden" id="next_prev"><option value="next">Next</option><option value="prev">Previous</option></div><div class="hidden" id="highlighting_words"><option value="highlighting">Actions,activity,access logs,accessibility,add,add an app,Add members,Add to Slack,administrators,all passwords,analytics,android,announcement,announcements,App Directory,app icon,Apple Watch,approving apps,archive,Asana,Atlassian,Automation apps,badge,billing details,billing,Bitbucket,bot user,box,browse,calls,Calls:,cancel,changes,channels,channel instantly,channel management,channel notification,channel suggestions,claim domains,close,company culture,compliance exports,compose,computers,conversations,convert,connect,connected accounts,connection,connecting,copy messages,create,customization,customize,custom SAML,custom,customer support teams,data exports,data security,deactivate,default channels,delete,deletion,deploy slack,desktop,direct messages,directory,disable,discover and join,Discovery APIs,display name,DMs,Do Not Disturb,domain,domains,downgrade,dropbox,duplicate accounts,edit,editing,education,email address,email,emoji,emoticons,Enterprise Grid,Enterprise Mobility Management,executives,export,failed payments,Fair Billing,faqs,finding,format,formatting,framework for apps,free trials,general,getting started,giphy,github integration,github organization,github,glossary,google apps,google calendar,google drive,guests,highlights,hipchat,human resources,IFTTT,import,Incoming WebHooks,integrations,ios,invite,IT teams,JIRA,join,Keep up,keyboard layout,keyboard shortcuts,Keychain Access,keyword notifications,language,languages,leave,link previews,loading,limits,links,linux,mac,manage a workspace,manage apps,manage members,marketing,mention,merge,message actions,messages are displayed,message display,microsoft products,mobile,mobile push,move channels,moving workspaces,multiple,mute,name,names,noise,nonprofits,notify,OneDrive,onboard,owners,password,payment,payments,permissions,phones,pin,plan,plans,plus plan,polls,primary ownership,privacy policies,prioritize tasks,private,private channel,private notes and files,project management,public channel,purpose,Quick Switcher,quote,reactivate,read,recruitment,referrer information,reminder,remove,rename,retention,Request a new workspace,role,roles,RSS,sales,Salesforce,SAML,SCIM,SCIM provisioning,screen reader,search,send,session duration,share messages,share,shared channel,shared channels,sidebar,sign in,sign out,signup mode,single sign-on,Slack Day,Slack for Teams,Slack notifications,Save notes and files,Service Level Agreements,ServiceNow,sign up,slack status,slackbot,slash commands,snippet,snooze,software developers,star,statistics,Stride,sync,tablets,tax,threads,time zone,tips,to-do lists,topic,triage channels,Terms of Service,Trello,troubleshoot,trouble receiving,tour,twitter,two-factor authentication,unread messages,updates,upgrade,upload,username,user groups,URL,vacation,Vendor and remittance,video,voice call,voice,what is,what's important,whitelisting,windows phone,windows,working in,workspace apps,workspace creation requests,workspace discovery,workspace's settings,wunderlist,your actions,Zapier,zoom,features,#general,File storage,posts,dark mode,theme,Workflow Builder,Voice,video,screen sharing,workflows,Outlook Calendar,Invited members,Transfer ownership,Whitelist,Enterprise Key Management,Transport Layer Security,Strong customer authentication,CSV,text file,work hours,</option></div><div class="hidden" id="search_meta"><option value="search_for">Search for “[term]”</option><option value="see_n_results">See [n]+ more results →</option></div><div class="loc_banner_container"></div><div class="article_page"><div class="article_container"><div class="article_spacer"></div><div class="article_breadcrumbs"><div class="article_breadcrumbs_container"><ol class="breadcrumbs"><li title="Slack Help Center"><a href="https://slack.com/help">Slack Help Center</a></li><li title="Workspace administration"><a href="https://slack.com/help/categories/200122103-Workspace-administration">Workspace administration</a></li><li title="Manage apps &amp; workflows"><a href="https://slack.com/section">Manage apps &amp; workflows</a></li><span class="article_breadcrumb_title">Configure automations for app approval</span></ol></div></div><div class="content_col"><div><h1 class="article_title">Configure automations for app approval</h1><div class="article_body"><p>By default, members can install apps without approval from a Workspace Owner, but you can choose to <a href="https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace" target="_blank" rel="noopener noreferrer">approve and restrict</a> apps on a case by case basis, or you can automate the process by configuring rules so that apps that meet your assigned criteria are automatically approved.</p><p class="bug"><strong>Note</strong>: We recommend developing and testing these features in a testing environment before using the functionality in production.</p><h2 id="h_01HEK56XR64J2WTMBK3TQJX40V"><strong>Before getting started</strong></h2><ul>
<li data-list-item-id="ecbe549d7338329ae334203d3c86999c3">Review the <a href="https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval" target="_blank" rel="noopener noreferrer">Guide to automation rules for app approval</a> to familiarize yourself with the outcomes of each rule.</li>
<li data-list-item-id="e4f1e5a45a96cd9737eb5c962c842dbbf">
<a href="#h_01GHY35SHQ1Q8D2G0WGD1GEEDA" target="_self">Rate and review scopes</a> and their risk levels to use them in a rule.</li>
</ul><p> </p><h2 id="h_01HEK56XR65G189S4A09KK6KPC"><strong>Create a rule</strong></h2><p>You can create rules based on a chain of comparisons for each app request to be checked against. Any app that meets the conditions of your rule will be automatically approved or restricted based on the resolution you specify.</p><div class="tabs enclosed">
<p class="option" title="tab_one">Free, Pro, and Business+ plans</p>
<p class="option" title="tab_two">Enterprise plans</p>
<section title="tab_one"><ol>
<li data-list-item-id="e43a4ac8ef3995c919e0349f5008684fe">From your desktop, click <em class="svg-settings"><em><strong> </strong></em></em><strong> Admin</strong> in the sidebar.</li>
<li data-list-item-id="ea85cad501bc7fe4b34bb05b6f2719e03">Select <strong>Apps and workflows</strong> from the menu to open the Slack Marketplace. </li>
<li data-list-item-id="ec022e09ee64f1b56cbf3a8eccdae1fde">Click <strong>Requests</strong> in the left sidebar, then select the <strong>Automation rules</strong> tab. If you don't see <strong>Requests</strong>, make sure <a href="https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace" target="_blank" rel="noopener noreferrer">app approval</a> is enabled for your workspace.</li>
<li data-list-item-id="e739bd8e46c80621e25c7bcbeec96b83d">At the top of the list, select <em class="ts_icon middle c-icon--plus-circle"><em> </em></em> <strong>Create a rule</strong>, then, give your rule a name and add a description.</li>
<li data-list-item-id="e0b870c6a7ebd4cfb944a4ef66251616b">Choose if <strong>all</strong> conditions need to match, or <strong>any</strong> single condition.</li>
<li data-list-item-id="eea7fccedbfb5ec54b36b00d598bf0216">Choose what condition you’d like the rule to look for from the drop-down menu. You can also choose a comparison from the following drop-down menu, if you need to.</li>
<li data-list-item-id="ec88accb7ad9fb094f915525242920758">To add additional conditions, click <strong>Add new condition.</strong>
</li>
<li data-list-item-id="e4da19eab8384e6318dbd6f4be5ff8343">Choose to <strong>Approve, Deny, Dismiss</strong> or <strong>Restrict</strong> an app that meets the conditions.</li>
<li data-list-item-id="eb218a7da653daae785098e17bcf220f4">If you'd like, select who to notify about the resolution and include a message to send the requestor.</li>
<li data-list-item-id="ef7261f3bf4ce4ea1c65567c81fb93f38">Click <strong>Save</strong>.</li>
</ol></section><section title="tab_two"><ol>
<li data-list-item-id="e87f07cf0ea6042dec918c56549b7fe43">From your desktop, click your <strong>organization name</strong> in the sidebar.<br><img class="localize_image_workspace_picker image--size-50 image--border-round" src="https://a.slack-edge.com/8e8e4/helpcenter/img/workspace-picker@2x.jpg">
</li>
<li data-list-item-id="e68b344e9205f7e093ee690c7470329f6">Hover over <strong>Tools &amp; settings</strong>, then click <strong>Organization settings</strong>.</li>
<li data-list-item-id="e1eda1eb6d5da7b251acf4fcaa709a9b6">From the left sidebar, click <strong>Integrations</strong> , then click <strong>Requests </strong>and select the <strong>Automation Rules</strong> tab.</li>
<li data-list-item-id="e4bb94a15c602b4228c72688678aa56b2">At the top of the list, select <em class="ts_icon middle c-icon--plus-circle"><em> </em></em> <strong>Create a rule, </strong>then, give your rule a name and add a description.</li>
<li data-list-item-id="e75aa625db4bf429dc64162771347a227">Choose if <strong>all</strong> conditions need to match, or <strong>any</strong> single condition.</li>
<li data-list-item-id="e443c1da066ff7c708e451bc41986ec26">Choose what condition you’d like the rule to look for from the drop-down menu. You can also choose a comparison from the following drop-down menu, if you need to.</li>
<li data-list-item-id="e2332f1e07d4effbd68361baaced33061">To add additional conditions, click <strong>Add new condition.</strong>
</li>
<li data-list-item-id="ea936a13c7c166f791eb902e60242a6dc">Choose to <strong>Approve, Deny, Dismiss</strong> or <strong>Restrict</strong> an app that meets the conditions.</li>
<li data-list-item-id="e595272d28722b965ac784d213f7fc105">If you'd like, select who to notify about the resolution and include a message to send the requestor.</li>
<li data-list-item-id="e6aab1fd3b7d5e62546cdeda3425238a8">Click <strong>Save</strong>.</li>
</ol></section>
</div><p class="tip singleline"><strong>Tip</strong>: Rules you create will not be enabled until you <a href="#h_01GDBJRP4FM0PDTJJKME94DRZ4" target="_self">activate them</a>. </p><p> </p><h2 id="h_01GDBJRP4FM0PDTJJKME94DRZ4"><strong>Manage rules</strong></h2><div class="tabs enclosed">
<p class="option" title="tab_one">Free, Pro, and Business+ plans</p>
<p class="option" title="tab_two">Enterprise plans</p>
<section title="tab_one"><ol>
<li data-list-item-id="e8f6d896af91f61dd7dfb04cdb6db5fdd">From your desktop, click <em class="svg-settings"><em><strong> </strong></em></em><strong> Admin</strong> in the sidebar.</li>
<li data-list-item-id="e731edfd9057607988a79551e5b005ca4">Select <strong>Apps and workflows</strong> from the menu to open the Slack Marketplace.</li>
<li data-list-item-id="e8bdb6999990cb74596c3752e8ca25b52">Click <strong>Requests</strong> in the left sidebar. </li>
<li data-list-item-id="e651ef494f4e48232d6f57a43de2fd62b">Click <strong>Automation rules </strong>to view a list of your existing rules, then click the <em class="ts_icon middle ts_icon_ellipsis"><em> </em></em><strong>three dots icon</strong>  next to the rule you’d like to <strong>Activate</strong>,<strong> Pause</strong>,<strong> Edit</strong>, or <strong>Remove.</strong>
</li>
</ol></section><section title="tab_two"><ol>
<li data-list-item-id="e7945684a28ce526f376ecff8661ea9f8">From your desktop, click your <strong>organization name</strong> in the sidebar.<br><img class="localize_image_workspace_picker image--size-50 image--border-round" src="https://a.slack-edge.com/8e8e4/helpcenter/img/workspace-picker@2x.jpg">
</li>
<li data-list-item-id="e2ccf1cc943ac98390855b09a64d493c8">Hover over <strong>Tools &amp; settings</strong>, then click <strong>Organization settings</strong>.</li>
<li data-list-item-id="e0006ab46c026de9bcab1b200241a6aba">From the left sidebar, click <strong>Integrations</strong>, then click <strong>Requests</strong>.</li>
<li data-list-item-id="e7bc0623eb07ec6ae106980a451cdda77">Click <strong>Automation Rules </strong>to view a list of your existing rules, then click the <em class="ts_icon middle ts_icon_ellipsis"><em> </em></em><strong>three dots icon</strong>  next to the rule you’d like to <strong>Activate, Pause, Edit</strong> or <strong>Remove.</strong>
</li>
</ol></section>
</div><p class="bug"><strong>Note</strong>: Removing a rule will not undo previous requests that were resolved by this rule. Removing a rule cannot be undone, and you'll need to recreate it from scratch. Proceed with caution!</p><p> </p><h2 id="h_01HEK56XR6AXKBJ36J21KD8ADS"><strong>Reorder rules</strong></h2><p>The order of the rules in the list is relevant to your automation, since a requested app will be resolved at the first matching rule. If you have multiple rules, you can reorder the list if you determine a rule should take priority over another.</p><div class="tabs enclosed">
<p class="option" title="tab_one">Free, Pro, and Business+ plans</p>
<p class="option" title="tab_two">Enterprise plans</p>
<section title="tab_one"><ol>
<li data-list-item-id="edaf8b752595c89d8916303fcf3cda719">From your desktop, click <em class="svg-settings"><em><strong> </strong></em></em><strong> Admin</strong> in the sidebar.</li>
<li data-list-item-id="e1d39197fc881e3508dd5889ec11f163e">Select <strong>Apps and workflows</strong> from the menu to open the Slack Marketplace.</li>
<li data-list-item-id="e66da5264fce59a4ca85c0158376cc26b">Click <strong>Requests</strong> in the left sidebar. </li>
<li data-list-item-id="ee3181800c538d033b2487a3976bcb2c4">Click <strong>Automation rules </strong>to view a list of your existing rules, then click <strong>Reorder list</strong>.</li>
<li data-list-item-id="e6c3ace7b7835630b8eb2b226e9c103b0">Using the available actions, choose if you’d like to move the rule up, down, to the top, or bottom of the automation rules list, then click <strong>Save</strong>.</li>
</ol></section><section title="tab_two"><ol>
<li data-list-item-id="e41e17f9309d571fb999d87d2856b9923">From your desktop, click your <strong>organization name</strong> in the sidebar.<br><img class="localize_image_workspace_picker image--size-50 image--border-round" src="https://a.slack-edge.com/8e8e4/helpcenter/img/workspace-picker@2x.jpg">
</li>
<li data-list-item-id="e3af3062bbed5da63d68603195a79efd9">Hover over <strong>Tools &amp; settings</strong>, then click <strong>Organization settings</strong>.</li>
<li data-list-item-id="e8bcee315a9d70906d59dfb397992776e">From the left sidebar, click <strong>Integrations</strong>, then click <strong>Requests.</strong>
</li>
<li data-list-item-id="e99fd17053c9671a827edeb4c90cd9ccf">Click <strong>Automation Rules </strong>to view a list of your existing rules, then click <strong>Reorder rules</strong>.</li>
<li data-list-item-id="e48f60c5112be370efe746e6ae22f2c4f">Using the available actions, choose if you’d like to move the rule up, down, to the top, or bottom of the automation rules list, then click <strong>Save</strong>.</li>
</ol></section>
</div><p> </p><h2 id="h_01GHY35SHQ1Q8D2G0WGD1GEEDA"><strong>Rate scopes as safe or unsafe</strong></h2><p>All apps have a unique set of permissions called scopes that determine what information an app can access. You can review and rate scopes as high, medium, or low risk. An app’s rating will populate rating lists for your organization. Once a scope has been rated, it can be used as a condition for automation.</p><div class="tabs enclosed">
<p class="option" title="tab_one">Free, Pro and Business+</p>
<p class="option" title="tab_two">Enterprise Grid</p>
<section title="tab_one"><ol>
<li data-list-item-id="e66ca3067b923400d4b45b0e40dfadfdf">From your desktop, click <em class="svg-settings"><em><strong> </strong></em></em><strong> Admin</strong> in the sidebar.</li>
<li data-list-item-id="ed1c61663c54ea83d44744de3cbd243cd">Select <strong>Apps and workflows</strong> from the menu to open the Slack Marketplace.</li>
<li data-list-item-id="e37361bf43498ae4ad0642b5d57bb504b">From the left sidebar, click <strong>Requests</strong>.</li>
<li data-list-item-id="eea81412b653ddbff80b40f9b8b1878e1">Click <strong>Scope ratings </strong>to view a list of all available scopes to be rated.</li>
<li data-list-item-id="ef4060939610deec597e56dcf4ba7b8ca">From the <strong>Name</strong> column, click the check box next to the scope you'd like to rate.</li>
<li data-list-item-id="ea7cbec69fe1a1356133f919ca33f2de6">Rate the scopes as <strong>high</strong>, <strong>medium</strong>, or <strong>low</strong> <strong>risk</strong> by clicking the desired option at the top of the scope list.</li>
</ol></section><section title="tab_two"><ol>
<li data-list-item-id="eb07e6dca39987f529ca65708a0118870">From your desktop, click your <strong>organization name</strong> in the sidebar.<br><img class="localize_image_workspace_picker image--size-50 image--border-round" src="https://a.slack-edge.com/8e8e4/helpcenter/img/workspace-picker@2x.jpg">
</li>
<li data-list-item-id="e53eda73e267ba765d3dd02eb1c4ca2f8">Hover over <strong>Tools &amp; settings</strong>, then click <strong>Organization settings</strong>.</li>
<li data-list-item-id="ec08378188041d8b2a57dcd90fb327aa1">From the left sidebar, click <strong>Integrations</strong> , then click <strong>Requests.</strong>
</li>
<li data-list-item-id="e0ed8f50c0b721b203d2d8d2206bfa151">Click <strong>Scope ratings </strong>to view a list of all available scopes to be rated.</li>
<li data-list-item-id="eb2e2c3165173d09ee4e5c88ac2f3a13b">From the <strong>Name</strong> column, click the check box next to the scope you'd like to rate.</li>
<li data-list-item-id="ec059d572082a335e812051778e78f642">Rate the scopes as <strong>high</strong>, <strong>medium</strong>, or <strong>low</strong> <strong>risk</strong> by clicking the desired option at the top of the scope list.</li>
</ol></section>
</div><p class="tip"><strong>Tip</strong>: To apply the same rating to multiple scopes, select all the desired scopes then click the <strong>Rate as high risk, Rate as medium risk</strong> or <strong>Rate as low risk</strong> action at the top of the scope list.</p><div class="boxed roles">
<p><strong>Who can use this feature?</strong></p>
<ul>
<li class="ts_icon ts_icon_user" data-list-item-id="ef28d95d2c2bc29aa2ad46459ecc2dcbd">
<strong>Workspace Owners/Admins, Org Owners</strong>/<strong>Admins</strong>, and <strong>members</strong> with <a href="https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#choose-how-app-requests-work">permission to manage apps</a>
</li>
<li class="ts_icon ts_icon_flag" data-list-item-id="ec766540c6b47f32ccab4b5f721b31018">Available on <a href="https://slack.com/pricing" target="_self"><strong>all plans</strong></a>
</li>
</ul>
</div></div></div><div class="article_footer"><div class="article-vote"><div class="vote-thanks"><p><b><i class="ts_icon ts_icon_happy_smile"></i> Awesome!</b></p><p>Thanks so much for your feedback!</p><p>If you’d like a member of our support team to respond to you, please send a note to <a href="mailto:feedback@slack.com">feedback@slack.com</a>.</p></div><div class="feedback-thanks"><p><b><i class="ts_icon ts_icon_check_circle_o_large"></i>Got it!</b></p><p>If you’d like a member of our support team to respond to you, please send a note to <a href="mailto:feedback@slack.com">feedback@slack.com</a>.</p></div><div class="article-vote-controls"><form id="voteForm" action="#" method="get" accept-charset="UTF-8"><input type="hidden" name="article_id" value="9487088123411"><span class="article-vote-question" data-guide="Was this guide helpful?" data-video="Was this video helpful?">Was this article helpful?</span><a id="up" role="button" rel="nofollow" class="article-vote-up" title="Yes, thanks!"><span class="article-button-text">Yes, thanks!</span></a><a id="down" role="button" rel="nofollow" class="article-vote-down" title="Not really"><span class="article-button-text">Not really</span></a></form></div><div class="article-feedback-form"><form id="feedbackForm" action="#" method="get" accept-charset="UTF-8"><input type="hidden" name="article_id" value="9487088123411"><div class="article-feedback-drive vote_feedback_drivers"><span class="article-vote-question" data-guide="Was this guide helpful?" data-video="Was this video helpful?">Sorry about that! What did you find most unhelpful?</span><label for="feedback_drive-1"><input type="radio" name="vote_feedback_drivers" id="feedback_drive-1" value="helpfulness"><span>This article didn’t answer my questions or solve my problem</span></label><label for="feedback_drive-2"><input type="radio" name="vote_feedback_drivers" id="feedback_drive-2" value="readability"><span>I found this article confusing or difficult to read</span></label><label for="feedback_drive-3"><input type="radio" name="vote_feedback_drivers" id="feedback_drive-3" value="product"><span>I don’t like how the feature works</span></label><label for="feedback_drive-4"><input type="radio" name="vote_feedback_drivers" id="feedback_drive-4" value="other"><span>Other</span></label></div><textarea id="feedback_up" maxlength="600" rows="4" class="vote_feedback_up" name="vote_feedback_up" placeholder="What did you like about this article?"></textarea><textarea id="feedback_down" maxlength="600" rows="4" class="vote_feedback_down" name="vote_feedback_down" placeholder="Is there anything else you'd like to share?"></textarea><div id="char_num"><span>0</span>/600</div><script type="text/javascript">var grecaptchaWidgetId = '';
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
};</script><script src="https://www.google.com/recaptcha/enterprise.js?render=explicit" async defer></script><div style="text-align:center"><div style="display:inline-block" id="slack_captcha"></div></div><a id="sendFeedback" role="button" rel="nofollow" title="Submit article feedback" class="article-send-feedback"><span class="article-button-text">Submit article feedback</span></a></form><p class="get-support">If you’d like a member of our support team to respond to you, please send a note to <a href="mailto:feedback@slack.com">feedback@slack.com</a>.</p></div><p class="vote-err"><i class="ts_icon ts_icon_warning"></i>Oops! We're having trouble. Please try again later!</p></div></div></div><div class="category_list" id="nav_holder"><div class="nav_scroll hidden"><div class="section_list_container"><p class="c-type-eyebrow">IN THIS ARTICLE</p><ul class="section-list" id="nav_list"></ul></div><ul class="section-list" id="cat_list"></ul></div></div></div></div></main><footer class="c-nav c-nav--expanded-footer o-content-container"><div class="c-nav--expanded-footer__supermenu"><div class="c-locale-new-overlay" id="new_locale_overlay"><div class="c-locale-new-menu" role="dialog" aria-label="Change Region"><button id="btn_close_locale" data-clog-manual role="button" class="c-locale-new-menu__close" data-clog-click aria-label="Close"><svg width="18" height="18" xmlns="http://www.w3.org/2000/svg" viewBox="-255 347 100 100" aria-hidden="true"><path d="M-160.4 434.2l-37.2-37.2 37.1-37.1-7-7-37.1 37.1-37.1-37.1-7 7 37.1 37.1-37.2 37.2 7.1 7 37.1-37.2 37.2 37.2"></path></svg></button><div id="new_locale_overlay_contents" class="c-locale-new-menu__contents"><p class="c-feature-grid__item__title">Change Region</p><p class="c-locale-new-menu__info">Selecting a different region will change the language and content of slack.com.</p><div class="c-locale-new-menu__cols"><div class="c-locale-new-menu__col"><p class="c-locale-new-menu__continent">Americas</p><a class="c-locale-new-menu__locale " href="https://slack.com/intl/es-la/help/articles/9487088123411-Configure-automations-for-app-approval" data-locale="es-LA" data-clog-manual data-geocode="es-la">Latinoamérica (español)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/pt-br/help/articles/9487088123411-Configure-automações-para-a-aprovação-de-apps" data-locale="pt-BR" data-clog-manual data-geocode="pt-br">Brasil (português)</a><a class="c-locale-new-menu__locale is-selected" href="https://slack.com/help/articles/9487088123411-Configure-automations-for-app-approval" data-locale="en-US" data-clog-manual data-geocode="en-us">United States (English)</a></div><div class="c-locale-new-menu__col"><p class="c-locale-new-menu__continent">Europe</p><a class="c-locale-new-menu__locale " href="https://slack.com/intl/de-de/help/articles/9487088123411-Automatisierungen-für-App-Genehmigungen-konfigurieren" data-locale="de-DE" data-clog-manual data-geocode="de-de">Deutschland (Deutsch)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/es-es/help/articles/9487088123411-Cómo-configurar-automatizaciones-para-la-aprobación-de-aplicaciones" data-locale="es-ES" data-clog-manual data-geocode="es-es">España (español)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/fr-fr/help/articles/9487088123411-Configurer-l’automatisation-de-l’approbation-des-applications" data-locale="fr-FR" data-clog-manual data-geocode="fr-fr">France (français)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/it-it/help/articles/9487088123411-Configurare-le-automazioni-per-l’approvazione-delle-app" data-locale="it-IT" data-clog-manual data-geocode="it-it">Italia (italiano)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/en-gb/help/articles/9487088123411-Configure-automations-for-app-approval" data-locale="en-GB" data-clog-manual data-geocode="en-gb">United Kingdom (English)</a></div><div class="c-locale-new-menu__col"><p class="c-locale-new-menu__continent">Asia Pacific</p><a class="c-locale-new-menu__locale " href="https://slack.com/intl/zh-cn/help/articles/9487088123411-配置自动化功能以批准应用安装" data-locale="zh-CN" data-clog-manual data-geocode="zh-cn">简体中文</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/zh-tw/help/articles/9487088123411-設定應用程式核准自動化" data-locale="zh-TW" data-clog-manual data-geocode="zh-tw">繁體中文</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/en-in/help/articles/9487088123411-Configure-automations-for-app-approval" data-locale="en-GB" data-clog-manual data-geocode="en-in">India (English)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/ja-jp/help/articles/9487088123411-アプリの承認の自動化を設定する" data-locale="ja-JP" data-clog-manual data-geocode="ja-jp">日本 (日本語)</a><a class="c-locale-new-menu__locale " href="https://slack.com/intl/ko-kr/help/articles/9487088123411-앱-승인을-위한-자동화-구성" data-locale="ko-KR" data-clog-manual data-geocode="ko-kr">대한민국 (한국어)</a></div></div></div></div></div><a id="new_locale_switcher" class="c-locale-new-switcher " href="#" data-locale="en-US" role="button" aria-haspopup="true" data-clog-click data-clog-ui-component="inc_footer_nav" data-clog-ui-element="link_locale_picker" data-qa="locale-switcher"><svg class="c-locale-new-switcher__globe" width="18" height="18" viewBox="0 0 100 100"><path d="M50.008 5.874c-11.308 0-22.613 4.3-31.219 12.906-17.211 17.211-17.211 45.226 0 62.438 17.211 17.21 45.195 17.21 62.406 0 17.212-17.212 17.243-45.227.032-62.438-8.606-8.606-19.912-12.906-31.22-12.906zm-3.125 6.125h.125v34.969H28.914c.58-10.29 4.095-20.385 10.594-28.157 2.27-2.715 4.757-4.983 7.375-6.812zm6.125 0h.062a38 38 0 0 1 7.407 6.812c6.498 7.772 10.014 17.866 10.593 28.157H53.008v-34.97zm-18.094 2.937c-7.508 8.978-11.557 20.412-12.156 32.032H11.977c.687-8.725 4.343-17.25 11.03-23.938a38.166 38.166 0 0 1 11.907-8.094zm30.219.062a38.176 38.176 0 0 1 11.812 8.063c6.685 6.685 10.369 15.19 11.063 23.906H77.227c-.598-11.59-4.623-23-12.094-31.969zm-53.156 37.97h10.78c.59 11.638 4.638 23.07 12.157 32.062a38.133 38.133 0 0 1-11.875-8.063c-6.7-6.7-10.376-15.258-11.062-24zm16.937 0h18.094V88.03h-.063c-2.644-1.838-5.146-4.135-7.437-6.875-6.512-7.787-10.025-17.876-10.594-28.188zm24.094 0H71.07c-.568 10.31-4.082 20.4-10.593 28.187-2.298 2.747-4.817 5.034-7.47 6.875V52.967zm24.219 0h10.812c-.679 8.741-4.39 17.295-11.094 24A38.07 38.07 0 0 1 65.04 85.06c.01-.011.022-.02.031-.031 7.52-8.992 11.568-20.424 12.157-32.063z"></path></svg><span>Change Region</span></a><ul class="c-nav__social_list"><li class="listitem-social"><a data-clog-click data-clog-ui-component="inc_footer_exp_nav" data-clog-ui-element="link_social_linkedin_exp_nav" aria-label="LinkedIn" title="LinkedIn" target="_blank" rel="noopener" href="https://www.linkedin.com/company/tiny-spec-inc/" data-qa="linkedin"><svg width="18" height="18" version="1" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg"><path d="M1.84613 3.69226C2.86519 3.69226 3.69226 2.86519 3.69226 1.84613C3.69226 0.827067 2.86519 0 1.84613 0C0.827067 0 0 0.827067 0 1.84613C0 2.86519 0.827067 3.69226 1.84613 3.69226ZM0 16V4.92317H3.69226V16H0ZM6.15441 4.92317H9.55991V6.66838H9.60916C10.0829 5.81794 11.2423 4.92317 12.9716 4.92317C16.5666 4.92317 17.2312 7.16068 17.2312 10.0714V16H13.6804V10.7446C13.6804 9.49173 13.6546 7.87821 11.8343 7.87821C9.98578 7.87821 9.70267 9.24311 9.70267 10.6536V16H6.15441V4.92317Z" fill="black"></path></svg></a></li><li class="listitem-social"><a data-clog-click data-clog-ui-component="inc_f
```
