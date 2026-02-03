# Source: https://docs.modular.com/mojo/std/collections/string/String

# Source: https://docs.modular.com/mojo/std/collections/string/string/String

<!doctype html><html lang=en dir=ltr class="docs-wrapper plugin-docs plugin-id-default docs-version-current docs-doc-page docs-doc-id-mojo/std/collections/string/string/String" data-has-hydrated=false><head><meta charset=UTF-8><meta name=generator content="Docusaurus v3.9.2"><title data-rh=true>String | Modular</title><meta data-rh=true name=viewport content="width=device-width, initial-scale=1.0"/><meta data-rh=true name=twitter:card content=summary_large_image /><meta data-rh=true property=og:url content=https://docs.modular.com/mojo/std/collections/string/string/String /><meta data-rh=true property=og:locale content=en /><meta data-rh=true name=docusaurus_locale content=en /><meta data-rh=true name=docsearch:language content=en /><meta data-rh=true name=docusaurus_version content=current /><meta data-rh=true name=docusaurus_tag content=docs-default-current /><meta data-rh=true name=docsearch:version content=current /><meta data-rh=true name=docsearch:docusaurus_tag content=docs-default-current /><meta data-rh=true property=og:title content="String | Modular"/><meta data-rh=true name=description content="Represents a mutable string."/><meta data-rh=true property=og:description content="Represents a mutable string."/><meta data-rh=true property=og:image content=https://docs.modular.com/images/mojo-metadata.png /><meta data-rh=true name=twitter:image content=https://docs.modular.com/images/mojo-metadata.png /><link data-rh=true rel=icon href=/images/favicon.ico /><link data-rh=true rel=canonical href=https://docs.modular.com/mojo/std/collections/string/string/String /><link data-rh=true rel=alternate href=https://docs.modular.com/mojo/std/collections/string/string/String hreflang=en /><link data-rh=true rel=alternate href=https://docs.modular.com/mojo/std/collections/string/string/String hreflang=x-default /><link rel=preconnect href=https://www.google-analytics.com><link rel=preconnect href=https://www.googletagmanager.com><script async src="https://www.googletagmanager.com/gtag/js?id=G-X9RN6M7PSJ"></script><script>function gtag(){dataLayer.push(arguments)}window.dataLayer=window.dataLayer||[],gtag("js",new Date),gtag("config","G-X9RN6M7PSJ",{anonymize_ip:!0})</script><link rel=search type=application/opensearchdescription+xml title=Modular href=/opensearch.xml><script async defer type=text/javascript data-cookiecategory=tracking src=//js.hs-scripts.com/24141518.js></script></head><body class=navigation-with-keyboard><img referrerpolicy=no-referrer-when-downgrade data-cookiecategory=tracking src="https://static.scarf.sh/a.png?x-pxid=d240bcad-0bb5-4db6-8c37-9061bb991d8e" class="absolute bottom-0" alt=" ">
<link rel=stylesheet href=https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css type=text/css integrity=sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM crossorigin=anonymous><script src=/cookieconsent.js async defer></script>
<script src=/customerio.js defer></script><link rel=stylesheet href=/assets/css/styles.3239a756.css />
<script src=/assets/js/runtime~main.348987f4.js defer></script>
<script src=/assets/js/main.fa867fdd.js defer></script>


<svg style="display: none;"><defs>
<symbol id=theme-svg-external-link viewBox="0 0 24 24"><path fill=currentColor d="M21 13v10h-21v-19h12v2h-10v15h17v-8h2zm3-12h-10.988l4.035 4-6.977 7.07 2.828 2.828 6.977-7.07 4.125 4.172v-11z"/></symbol>
</defs></svg>
<script>!function(){var t=function(){try{return new URLSearchParams(window.location.search).get("docusaurus-theme")}catch(t){}}()||function(){try{return window.localStorage.getItem("theme")}catch(t){}}();document.documentElement.setAttribute("data-theme",t||(window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light")),document.documentElement.setAttribute("data-theme-choice",t||"system")}(),function(){try{for(var[t,e]of new URLSearchParams(window.location.search).entries())if(t.startsWith("docusaurus-data-")){var a=t.replace("docusaurus-data-","data-");document.documentElement.setAttribute(a,e)}}catch(t){}}()</script><div id=__docusaurus><style data-mantine-styles=true>:root{--mantine-cursor-type:pointer;--mantine-line-height:1.4;--mantine-font-family:Inter;--mantine-font-family-monospace:Roboto Mono,PT Mono,Courier New,Courier,monospace;--mantine-font-family-headings:Inter;--mantine-heading-font-weight:400;--mantine-radius-default:calc(.125rem*var(--mantine-scale));--mantine-breakpoint-sm:640px;--mantine-breakpoint-md:768px;--mantine-breakpoint-lg:1024px;--mantine-breakpoint-xl:1280px;--mantine-breakpoint-docs-desktop:997px;--mantine-breakpoint-xxl:1400px;--mantine-breakpoint-cbl:900px;--mantine-breakpoint-cbm:590px;--mantine-spacing-1:calc(.25rem*var(--mantine-scale));--mantine-spacing-2:calc(.5rem*var(--mantine-scale));--mantine-spacing-3:calc(.75rem*var(--mantine-scale));--mantine-spacing-4:calc(1rem*var(--mantine-scale));--mantine-spacing-5:calc(1.25rem*var(--mantine-scale));--mantine-spacing-6:calc(1.5rem*var(--mantine-scale));--mantine-spacing-7:calc(1.75rem*var(--mantine-scale));--mantine-spacing-8:calc(2rem*var(--mantine-scale));--mantine-spacing-9:calc(2.25rem*var(--mantine-scale));--mantine-spacing-10:calc(2.5rem*var(--mantine-scale));--mantine-spacing-11:calc(2.75rem*var(--mantine-scale));--mantine-spacing-12:calc(3rem*var(--mantine-scale));--mantine-spacing-14:calc(3.5rem*var(--mantine-scale));--mantine-spacing-16:calc(4rem*var(--mantine-scale));--mantine-spacing-20:calc(5rem*var(--mantine-scale));--mantine-spacing-24:calc(6rem*var(--mantine-scale));--mantine-spacing-28:calc(7rem*var(--mantine-scale));--mantine-spacing-32:calc(8rem*var(--mantine-scale));--mantine-spacing-36:calc(9rem*var(--mantine-scale));--mantine-spacing-40:calc(10rem*var(--mantine-scale));--mantine-spacing-44:calc(11rem*var(--mantine-scale));--mantine-spacing-48:calc(12rem*var(--mantine-scale));--mantine-spacing-52:calc(13rem*var(--mantine-scale));--mantine-spacing-56:calc(14rem*var(--mantine-scale));--mantine-spacing-60:calc(15rem*var(--mantine-scale));--mantine-spacing-64:calc(16rem*var(--mantine-scale));--mantine-spacing-72:calc(18rem*var(--mantine-scale));--mantine-spacing-80:calc(20rem*var(--mantine-scale));--mantine-spacing-96:calc(24rem*var(--mantine-scale));--mantine-spacing-xxs:calc(.5rem*var(--mantine-scale));--mantine-spacing-xxl:calc(2.5rem*var(--mantine-scale));--mantine-spacing-3x:calc(4rem*var(--mantine-scale));--mantine-spacing-4x:calc(5rem*var(--mantine-scale));--mantine-spacing-5x:calc(7.5rem*var(--mantine-scale));--mantine-line-height-sm:1.33;--mantine-line-height-md:1.4;--mantine-line-height-lg:1.5;--mantine-line-height-xl:1.66;--mantine-color-dark-0:#fff;--mantine-color-dark-1:#b8b8b8;--mantine-color-dark-4:#353d42;--mantine-color-dark-5:#020c13;--mantine-color-dark-6:#020c13;--mantine-color-dark-7:#020c13;--mantine-color-dark-8:#020c13;--mantine-color-dark-9:#020c13;--mantine-color-red-0:#ff9c9c;--mantine-color-red-1:#fd6666;--mantine-color-red-2:#fc3937;--mantine-color-red-3:#fd1f1b;--mantine-color-red-4:#fd0f0c;--mantine-color-red-5:#e20101;--mantine-color-red-6:#ca0000;--mantine-color-red-7:#ca0000;--mantine-color-red-8:#b10000;--mantine-color-red-9:#b10000;--mantine-color-blue-0:#e6ebff;--mantine-color-blue-1:#cdd7ff;--mantine-color-blue-2:#b5c0f6;--mantine-color-blue-3:#b5c0f6;--mantine-color-blue-4:#b5c0f6;--mantine-color-blue-5:#b5c0f6;--mantine-color-blue-6:#7584de;--mantine-color-blue-7:#6370be;--mantine-color-blue-8:#515d9e;--mantine-color-blue-9:#414a80;--mantine-h1-font-weight:400;--mantine-h2-font-weight:400;--mantine-h3-font-weight:400;--mantine-h4-font-weight:400;--mantine-h5-font-weight:400;--mantine-h6-font-weight:400}:root[data-mantine-color-scheme=dark]{--mantine-primary-color-contrast:var(--mantine-color-black);--mantine-color-dark-filled:var(--mantine-color-dark-5);--mantine-color-dark-filled-hover:var(--mantine-color-dark-6);--mantine-color-dark-light:#69696926;--mantine-color-dark-light-hover:#69696933;--mantine-color-dark-light-color:var(--mantine-color-dark-0);--mantine-color-dark-outline:var(--mantine-color-dark-1);--mantine-color-dark-outline-hover:#b8b8b80d;--mantine-color-gray-filled:var(--mantine-color-gray-5);--mantine-color-gray-filled-hover:var(--mantine-color-gray-6);--mantine-color-gray-light:#dee2e626;--mantine-color-gray-light-hover:#dee2e633;--mantine-color-gray-light-color:var(--mantine-color-gray-0);--mantine-color-gray-outline:var(--mantine-color-gray-1);--mantine-color-gray-outline-hover:#f1f3f50d;--mantine-color-red-filled:var(--mantine-color-red-5);--mantine-color-red-filled-hover:var(--mantine-color-red-6);--mantine-color-red-light:#fd1f1b26;--mantine-color-red-light-hover:#fd1f1b33;--mantine-color-red-light-color:var(--mantine-color-red-0);--mantine-color-red-outline:var(--mantine-color-red-1);--mantine-color-red-outline-hover:#fd66660d;--mantine-color-pink-filled:var(--mantine-color-pink-5);--mantine-color-pink-filled-hover:var(--mantine-color-pink-6);--mantine-color-pink-light:#faa2c126;--mantine-color-pink-light-hover:#faa2c133;--mantine-color-pink-light-color:var(--mantine-color-pink-0);--mantine-color-pink-outline:var(--mantine-color-pink-1);--mantine-color-pink-outline-hover:#ffdeeb0d;--mantine-color-grape-filled:var(--mantine-color-grape-5);--mantine-color-grape-filled-hover:var(--mantine-color-grape-6);--mantine-color-grape-light:#e599f726;--mantine-color-grape-light-hover:#e599f733;--mantine-color-grape-light-color:var(--mantine-color-grape-0);--mantine-color-grape-outline:var(--mantine-color-grape-1);--mantine-color-grape-outline-hover:#f3d9fa0d;--mantine-color-violet-filled:var(--mantine-color-violet-5);--mantine-color-violet-filled-hover:var(--mantine-color-violet-6);--mantine-color-violet-light:#b197fc26;--mantine-color-violet-light-hover:#b197fc33;--mantine-color-violet-light-color:var(--mantine-color-violet-0);--mantine-color-violet-outline:var(--mantine-color-violet-1);--mantine-color-violet-outline-hover:#e5dbff0d;--mantine-color-indigo-filled:var(--mantine-color-indigo-5);--mantine-color-indigo-filled-hover:var(--mantine-color-indigo-6);--mantine-color-indigo-light:#91a7ff26;--mantine-color-indigo-light-hover:#91a7ff33;--mantine-color-indigo-light-color:var(--mantine-color-indigo-0);--mantine-color-indigo-outline:var(--mantine-color-indigo-1);--mantine-color-indigo-outline-hover:#dbe4ff0d;--mantine-color-blue-filled:var(--mantine-color-blue-5);--mantine-color-blue-filled-hover:var(--mantine-color-blue-6);--mantine-color-blue-light:#b5c0f626;--mantine-color-blue-light-hover:#b5c0f633;--mantine-color-blue-light-color:var(--mantine-color-blue-0);--mantine-color-blue-outline:var(--mantine-color-blue-1);--mantine-color-blue-outline-hover:#cdd7ff0d;--mantine-color-cyan-filled:var(--mantine-color-cyan-5);--mantine-color-cyan-filled-hover:var(--mantine-color-cyan-6);--mantine-color-cyan-light:#66d9e826;--mantine-color-cyan-light-hover:#66d9e833;--mantine-color-cyan-light-color:var(--mantine-color-cyan-0);--mantine-color-cyan-outline:var(--mantine-color-cyan-1);--mantine-color-cyan-outline-hover:#c5f6fa0d;--mantine-color-teal-filled:var(--mantine-color-teal-5);--mantine-color-teal-filled-hover:var(--mantine-color-teal-6);--mantine-color-teal-light:#63e6be26;--mantine-color-teal-light-hover:#63e6be33;--mantine-color-teal-light-color:var(--mantine-color-teal-0);--mantine-color-teal-outline:var(--mantine-color-teal-1);--mantine-color-teal-outline-hover:#c3fae80d;--mantine-color-green-filled:var(--mantine-color-green-5);--mantine-color-green-filled-hover:var(--mantine-color-green-6);--mantine-color-green-light:#8ce99a26;--mantine-color-green-light-hover:#8ce99a33;--mantine-color-green-light-color:var(--mantine-color-green-0);--mantine-color-green-outline:var(--mantine-color-green-1);--mantine-color-green-outline-hover:#d3f9d80d;--mantine-color-lime-filled:var(--mantine-color-lime-5);--mantine-color-lime-filled-hover:var(--mantine-color-lime-6);--mantine-color-lime-light:#c0eb7526;--mantine-color-lime-light-hover:#c0eb7533;--mantine-color-lime-light-color:var(--mantine-color-lime-0);--mantine-color-lime-outline:var(--mantine-color-lime-1);--mantine-color-lime-outline-hover:#e9fac80d;--mantine-color-yellow-filled:var(--mantine-color-yellow-5);--mantine-color-yellow-filled-hover:var(--mantine-color-yellow-6);--mantine-color-yellow-light:#ffe06626;--mantine-color-yellow-light-hover:#ffe06633;--mantine-color-yellow-light-color:var(--mantine-color-yellow-0);--mantine-color-yellow-outline:var(--mantine-color-yellow-1);--mantine-color-yellow-outline-hover:#fff3bf0d;--mantine-color-orange-filled:var(--mantine-color-orange-5);--mantine-color-orange-filled-hover:var(--mantine-color-orange-6);--mantine-color-orange-light:#ffc07826;--mantine-color-orange-light-hover:#ffc07833;--mantine-color-orange-light-color:var(--mantine-color-orange-0);--mantine-color-orange-outline:var(--mantine-color-orange-1);--mantine-color-orange-outline-hover:#ffe8cc0d}:root[data-mantine-color-scheme=light]{--mantine-primary-color-contrast:var(--mantine-color-black);--mantine-color-anchor:var(--mantine-color-blue-5);--mantine-color-dark-filled:var(--mantine-color-dark-5);--mantine-color-dark-filled-hover:var(--mantine-color-dark-6);--mantine-color-dark-light:#020c131a;--mantine-color-dark-light-hover:#020c131f;--mantine-color-dark-light-color:var(--mantine-color-dark-5);--mantine-color-dark-outline:var(--mantine-color-dark-5);--mantine-color-dark-outline-hover:#020c130d;--mantine-color-gray-filled:var(--mantine-color-gray-5);--mantine-color-gray-filled-hover:var(--mantine-color-gray-6);--mantine-color-gray-light:#adb5bd1a;--mantine-color-gray-light-hover:#adb5bd1f;--mantine-color-gray-light-color:var(--mantine-color-gray-5);--mantine-color-gray-outline:var(--mantine-color-gray-5);--mantine-color-gray-outline-hover:#adb5bd0d;--mantine-color-red-filled:var(--mantine-color-red-5);--mantine-color-red-filled-hover:var(--mantine-color-red-6);--mantine-color-red-light:#e201011a;--mantine-color-red-light-hover:#e201011f;--mantine-color-red-light-color:var(--mantine-color-red-5);--mantine-color-red-outline:var(--mantine-color-red-5);--mantine-color-red-outline-hover:#e201010d;--mantine-color-pink-filled:var(--mantine-color-pink-5);--mantine-color-pink-filled-hover:var(--mantine-color-pink-6);--mantine-color-pink-light:#f065951a;--mantine-color-pink-light-hover:#f065951f;--mantine-color-pink-light-color:var(--mantine-color-pink-5);--mantine-color-pink-outline:var(--mantine-color-pink-5);--mantine-color-pink-outline-hover:#f065950d;--mantine-color-grape-filled:var(--mantine-color-grape-5);--mantine-color-grape-filled-hover:var(--mantine-color-grape-6);--mantine-color-grape-light:#cc5de81a;--mantine-color-grape-light-hover:#cc5de81f;--mantine-color-grape-light-color:var(--mantine-color-grape-5);--mantine-color-grape-outline:var(--mantine-color-grape-5);--mantine-color-grape-outline-hover:#cc5de80d;--mantine-color-violet-filled:var(--mantine-color-violet-5);--mantine-color-violet-filled-hover:var(--mantine-color-violet-6);--mantine-color-violet-light:#845ef71a;--mantine-color-violet-light-hover:#845ef71f;--mantine-color-violet-light-color:var(--mantine-color-violet-5);--mantine-color-violet-outline:var(--mantine-color-violet-5);--mantine-color-violet-outline-hover:#845ef70d;--mantine-color-indigo-filled:var(--mantine-color-indigo-5);--mantine-color-indigo-filled-hover:var(--mantine-color-indigo-6);--mantine-color-indigo-light:#5c7cfa1a;--mantine-color-indigo-light-hover:#5c7cfa1f;--mantine-color-indigo-light-color:var(--mantine-color-indigo-5);--mantine-color-indigo-outline:var(--mantine-color-indigo-5);--mantine-color-indigo-outline-hover:#5c7cfa0d;--mantine-color-blue-filled:var(--mantine-color-blue-5);--mantine-color-blue-filled-hover:var(--mantine-color-blue-6);--mantine-color-blue-light:#b5c0f61a;--mantine-color-blue-light-hover:#b5c0f61f;--mantine-color-blue-light-color:var(--mantine-color-blue-5);--mantine-color-blue-outline:var(--mantine-color-blue-5);--mantine-color-blue-outline-hover:#b5c0f60d;--mantine-color-cyan-filled:var(--mantine-color-cyan-5);--mantine-color-cyan-filled-hover:var(--mantine-color-cyan-6);--mantine-color-cyan-light:#22b8cf1a;--mantine-color-cyan-light-hover:#22b8cf1f;--mantine-color-cyan-light-color:var(--mantine-color-cyan-5);--mantine-color-cyan-outline:var(--mantine-color-cyan-5);--mantine-color-cyan-outline-hover:#22b8cf0d;--mantine-color-teal-filled:var(--mantine-color-teal-5);--mantine-color-teal-filled-hover:var(--mantine-color-teal-6);--mantine-color-teal-light:#20c9971a;--mantine-color-teal-light-hover:#20c9971f;--mantine-color-teal-light-color:var(--mantine-color-teal-5);--mantine-color-teal-outline:var(--mantine-color-teal-5);--mantine-color-teal-outline-hover:#20c9970d;--mantine-color-green-filled:var(--mantine-color-green-5);--mantine-color-green-filled-hover:var(--mantine-color-green-6);--mantine-color-green-light:#51cf661a;--mantine-color-green-light-hover:#51cf661f;--mantine-color-green-light-color:var(--mantine-color-green-5);--mantine-color-green-outline:var(--mantine-color-green-5);--mantine-color-green-outline-hover:#51cf660d;--mantine-color-lime-filled:var(--mantine-color-lime-5);--mantine-color-lime-filled-hover:var(--mantine-color-lime-6);--mantine-color-lime-light:#94d82d1a;--mantine-color-lime-light-hover:#94d82d1f;--mantine-color-lime-light-color:var(--mantine-color-lime-5);--mantine-color-lime-outline:var(--mantine-color-lime-5);--mantine-color-lime-outline-hover:#94d82d0d;--mantine-color-yellow-filled:var(--mantine-color-yellow-5);--mantine-color-yellow-filled-hover:var(--mantine-color-yellow-6);--mantine-color-yellow-light:#fcc4191a;--mantine-color-yellow-light-hover:#fcc4191f;--mantine-color-yellow-light-color:var(--mantine-color-yellow-5);--mantine-color-yellow-outline:var(--mantine-color-yellow-5);--mantine-color-yellow-outline-hover:#fcc4190d;--mantine-color-orange-filled:var(--mantine-color-orange-5);--mantine-color-orange-filled-hover:var(--mantine-color-orange-6);--mantine-color-orange-light:#ff922b1a;--mantine-color-orange-light-hover:#ff922b1f;--mantine-color-orange-light-color:var(--mantine-color-orange-5);--mantine-color-orange-outline:var(--mantine-color-orange-5);--mantine-color-orange-outline-hover:#ff922b0d}</style><style data-mantine-styles=classes>@media (width<=35.9938em){.mantine-visible-from-xs{display:none!important}}@media (width>=36em){.mantine-hidden-from-xs{display:none!important}}@media (width<=639.9px){.mantine-visible-from-sm{display:none!important}}@media (width>=640px){.mantine-hidden-from-sm{display:none!important}}@media (width<=767.9px){.mantine-visible-from-md{display:none!important}}@media (width>=768px){.mantine-hidden-from-md{display:none!important}}@media (width<=1023.9px){.mantine-visible-from-lg{display:none!important}}@media (width>=1024px){.mantine-hidden-from-lg{display:none!important}}@media (width<=1279.9px){.mantine-visible-from-xl{display:none!important}}@media (width>=1280px){.mantine-hidden-from-xl{display:none!important}}@media (width<=996.9px){.mantine-visible-from-docs-desktop{display:none!important}}@media (width>=997px){.mantine-hidden-from-docs-desktop{display:none!important}}@media (width<=1399.9px){.mantine-visible-from-xxl{display:none!important}}@media (width>=1400px){.mantine-hidden-from-xxl{display:none!important}}@media (width<=899.9px){.mantine-visible-from-cbl{display:none!important}}@media (width>=900px){.mantine-hidden-from-cbl{display:none!important}}@media (width<=589.9px){.mantine-visible-from-cbm{display:none!important}}@media (width>=590px){.mantine-hidden-from-cbm{display:none!important}}</style><div role=region aria-label="Skip to main content"><a class=skipToContent_fXgn href=#__docusaurus_skipToContent_fallback>Skip to main content</a></div><div class="fixed left-0 top-0 z-[400] w-screen bg-white"><div class="sticky top-0 z-10 border-0 border-b border-solid border-Elements-Twilight-Alpha bg-Elements-Twilight-0-90"><div class=mantine-visible-from-sm><div style="--group-gap:0rem;--group-align:center;--group-justify:space-between;--group-wrap:wrap;margin-inline:auto;padding-inline:calc(1.5rem * var(--mantine-scale));max-width:calc(90rem * var(--mantine-scale))" class="h-[72px] m_4081bf90 mantine-Group-root"><div style="--group-gap:calc(0.75rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:nowrap" class="m_4081bf90 mantine-Group-root"><a href=https://www.modular.com/ target=_blank rel="noopener noreferrer"><svg style="width:calc(4.75rem * var(--mantine-scale));height:calc(1rem * var(--mantine-scale))" xmlns=http://www.w3.org/2000/svg viewBox="0 0 132 28" class="mt-1.5 text-black"><path stroke=transparent fill=currentColor d="M42.5 7.5C37 7.5 33 11.6 33 17.7 33 24 37 28 42.5 28c5.3 0 9.4-4.1 9.4-10.3 0-6-4.1-10.2-9.4-10.2Zm0 17.7c-3.6 0-6.6-3-6.6-7.5s3-7.4 6.6-7.4c3.5 0 6.5 3 6.5 7.4 0 4.6-3 7.5-6.5 7.5Zm26.9-14.6h-.2a7.5 7.5 0 0 0-6.3-3.1c-5.2 0-9.1 4.1-9.1 10.2 0 6.2 3.9 10.3 9 10.3 2.9 0 4.8-1.1 6.4-3.2h.2v2.8h3V0h-3v10.6ZM63 25.2c-3.4 0-6.3-3-6.3-7.5s3-7.4 6.3-7.4 6.3 3 6.3 7.4c0 4.6-3 7.5-6.3 7.5ZM89.2 8h3v19.7h-3v-2.2H89a8 8 0 0 1-6 2.6c-4.4 0-7.8-3.4-7.8-8.3V8h3v11.8c0 3.2 2.4 5.5 5.3 5.5 3.2 0 5.7-2.5 5.7-5.5V8Zm6-7.9H98v27.6h-3V0Zm20.7 10.6h-.2a7.5 7.5 0 0 0-6.3-3.1c-5.2 0-9 4.1-9 10.2 0 6.2 3.8 10.3 9 10.3 2.8 0 4.7-1.1 6.3-3.2h.2v2.8h3V8h-3v2.7Zm-6.3 14.6c-3.4 0-6.3-3-6.3-7.5s3-7.4 6.3-7.4 6.3 3 6.3 7.4c0 4.6-3 7.5-6.3 7.5ZM132 8v2.7h-7c-.2 0-.3.1-.3.2v16.8h-3v-17h2.8l.2-.1V7.9h7.3ZM27.8 4h3v23.5h-3.2V4.3l-.2-.2H26l-8.3 23.5H13L4.7 4.1H3.2v23.5H0V0h6.5L15 24h.8l8.4-24h3.4v4l.2.1Z"/></svg></a><p style=margin:0rem;padding:0rem class="body-16-light !mt-[1px] mantine-Text-root">/<div class="grid grid-cols-2 !gap-2 rounded-sm bg-Elements-Twilight-5-80 p-1"><a class="flex h-[36px] cursor-pointer items-center justify-center text-black hover:text-black hover:no-underline sm:h-[29px] sm:w-[72px] sm:text-sm bg-Elements-Twilight-0-90 rounded-sm border border-solid border-Elements-Twilight-30-70 shadow-3" target=_self href=/>Docs</a><a href=https://builds.modular-dev.com target=_self rel="noopener noreferrer" class="flex h-[36px] cursor-pointer items-center justify-center text-black hover:text-black hover:no-underline sm:h-[29px] sm:w-[72px] sm:text-sm bg-transparent !text-Elements-Twilight-60-50 hover:bg-Elements-Twilight-20-70">Code</a></div><div style="width:calc(0.375rem * var(--mantine-scale));min-width:calc(0.375rem * var(--mantine-scale))" class=""></div><div class=mantine-visible-from-xl><div class=mantine-visible-from-xl><nav aria-label=Main class="navbar navbar--fixed-top"><div class="!pr-0 pl-6 xl:pl-0 navbar__inner"><div class=navbar__items><div style="--group-gap:calc(1.375rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:wrap" class="m_4081bf90 mantine-Group-root"><a class="navbar__item navbar__link" href=/max/intro>Guides</a><a aria-current=page class="navbar__item navbar__link navbar__link--active" href=/max/api/>APIs</a><a class="navbar__item navbar__link" href=/mojo/manual/>Mojo</a></div></div><div class="navbar__items navbar__items--right"></div></div><div role=presentation class=navbar-sidebar__backdrop></div></nav></div></div></div><div style=--group-gap:var(--mantine-spacing-md);--group-align:center;--group-justify:flex-start;--group-wrap:nowrap class="m_4081bf90 mantine-Group-root"><div class="dropdown dropdown--hoverable w-24"><a aria-current=page class="navbar__link version-dropdown-link mt-2 pb-2 active" aria-haspopup=true aria-expanded=false role=button href=/mojo/std/collections/string/string/String><div class=font-inter><div style="--group-gap:calc(0.25rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:nowrap" class="m_4081bf90 mantine-Group-root"><svg viewBox="0 0 20 20" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(1.25rem * var(--mantine-scale));height:calc(1.25rem * var(--mantine-scale))" color=var(--Elements-Neb-Ultra)><g stroke=currentColor stroke-width=1.5><path d="M16.04 11.24a5.4 5.4 0 0 1-7.28-7.28 7.19 7.19 0 1 0 7.28 7.28ZM13.18.96v3.65M17.21 5.2v3.65M15 2.79h-3.65M19.04 7.03h-3.65"/></g></svg><p style="font-size:calc(1rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto m_b6d8b162 mantine-Text-root">Nightly</div></div></a><ul class="dropdown__menu !w-[205px] !rounded-sm border border-solid border-Elements-Twilight-5-80 !p-0"><div class=""><button class="mantine-focus-auto w-full p-6 hover:!bg-Elements-Twilight-5-80 md:px-2.5 md:py-1.5 bg-Elements-Twilight-5-80 m_87cf2631 mantine-UnstyledButton-root" type=button><div style=--stack-gap:0rem;--stack-align:stretch;--stack-justify:flex-start class="m_6d731127 mantine-Stack-root"><div style="--group-gap:calc(0.125rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:wrap" class="text-Elements-Neb-Ultra m_4081bf90 mantine-Group-root"><svg viewBox="0 0 20 20" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(1rem * var(--mantine-scale));height:calc(1rem * var(--mantine-scale))"><g stroke=currentColor stroke-width=1.5><path d="M16.04 11.24a5.4 5.4 0 0 1-7.28-7.28 7.19 7.19 0 1 0 7.28 7.28ZM13.18.96v3.65M17.21 5.2v3.65M15 2.79h-3.65M19.04 7.03h-3.65"/></g></svg><p style="font-size:calc(1rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto m_b6d8b162 mantine-Text-root">Nightly</div><div class=text-xs color=var(--Elements-Twilight-60-40)>Work in progress</div></div></button><div style=--divider-color:var(--Elements-Twilight-5-80) class="m_3eebeb36 mantine-Divider-root" data-orientation=horizontal role=separator></div></div><div class=""><button class="mantine-focus-auto w-full p-6 hover:!bg-Elements-Twilight-5-80 md:px-2.5 md:py-1.5 m_87cf2631 mantine-UnstyledButton-root" type=button><div style=--stack-gap:0rem;--stack-align:stretch;--stack-justify:flex-start class="m_6d731127 mantine-Stack-root"><div style="--group-gap:calc(0.125rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:wrap" class="text-black m_4081bf90 mantine-Group-root"><p style="font-size:calc(1rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto m_b6d8b162 mantine-Text-root">v26.1</div><div class=text-xs color=var(--Elements-Twilight-60-40)><div style="--group-gap:calc(0.125rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:nowrap" class="m_4081bf90 mantine-Group-root"><time datetime="Thu Jan 29 2026 00:00:00 GMT+0000 (Coordinated Universal Time)" itemprop=datePublished data-visual-test=blackout>Jan 29, 2026</time>/ Stable release</div></div></div></button></div></ul></div><div class=""><div class=toggle_vylO><button class="clean-btn toggleButton_gllP toggleButtonDisabled_aARS" type=button disabled title="system mode" aria-label="Switch between dark and light mode (currently system mode)"><svg aria-hidden=true class="toggleIcon_g3eP lightToggleIcon_pyhR" width=22 height=22 fill=none xmlns=http://www.w3.org/2000/svg><g stroke=currentColor stroke-width=1.5><path d="m3.5 18.5 2-2M16.5 16.5l2 2M18.5 3.5l-2 2M5.5 5.5l-2-2M11 22v-3M11 3V0M0 11h3M19 11h3M7.5 11a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0Z"/></g></svg><svg aria-hidden=true class="toggleIcon_g3eP darkToggleIcon_wfgR" width=22 height=22 fill=none xmlns=http://www.w3.org/2000/svg><path d="M8 1a10 10 0 1 1-5.74 18.2 8.5 8.5 0 0 0 0-16.4A9.95 9.95 0 0 1 8 1Z" stroke=white stroke-width=1.5 /></svg><svg viewBox="0 0 24 24" width=24 height=24 aria-hidden=true class="toggleIcon_g3eP systemToggleIcon_QzmC"><path fill=currentColor d="m12 21c4.971 0 9-4.029 9-9s-4.029-9-9-9-9 4.029-9 9 4.029 9 9 9zm4.95-13.95c1.313 1.313 2.05 3.093 2.05 4.95s-0.738 3.637-2.05 4.95c-1.313 1.313-3.093 2.05-4.95 2.05v-14c1.857 0 3.637 0.737 4.95 2.05z"/></svg></button></div></div><a href=https://github.com/modular/modular target=_blank rel="noopener noreferrer" style="--ai-size:calc(2rem * var(--mantine-scale));--ai-bg:transparent;--ai-hover:transparent;--ai-color:var(--mantine-color-blue-light-color);--ai-bd:calc(0.0625rem * var(--mantine-scale)) solid transparent" class="mantine-focus-auto mantine-active m_8d3f4000 mantine-ActionIcon-root m_87cf2631 mantine-UnstyledButton-root" data-variant=transparent><span class="m_8d3afb97 mantine-ActionIcon-icon"><svg viewBox="0 0 12 12" xmlns=http://www.w3.org/2000/svg style="width:calc(1.25rem * var(--mantine-scale));height:calc(1.25rem * var(--mantine-scale))" color=var(--Black) fill=currentColor><g clip-path=url(#:Rbatllldcleh:)><path fill-rule=evenodd clip-rule=evenodd d="M6 .8c2.9 0 5.2 2.4 5.2 5.3 0 2.4-1.5 4.4-3.6 5-.2.1-.3 0-.3-.2V9.5c0-.5-.2-.9-.4-1 1.2-.1 2.4-.6 2.4-2.6 0-.6-.2-1.1-.5-1.5 0-.1.2-.7 0-1.4 0 0-.5-.1-1.5.6a4.9 4.9 0 0 0-2.6 0c-1-.7-1.4-.6-1.4-.6a2 2 0 0 0 0 1.4A2 2 0 0 0 2.6 6c0 2 1.2 2.5 2.4 2.6-.2.1-.3.4-.4.7-.3.1-1 .4-1.5-.4 0 0-.3-.6-.8-.6 0 0-.5 0 0 .3 0 0 .3.2.6.8 0 0 .3 1 1.7.6v1c0 .2 0 .3-.3.3-2.1-.7-3.6-2.7-3.6-5C.8 3.1 3.1.7 6 .7Z"/></g><defs><clipPath id=:Rbatllldcleh:><path fill=var(--White) transform="translate(.8 .8)" d="M0 0h10.4v10.4H0z"/></clipPath></defs></svg></span></a><div class="docs-search-bar DocSearch-Button-Only"><div class=shared-search-bar><button type=button class="DocSearch DocSearch-Button" aria-label="Search (Meta+k)" aria-keyshortcuts=Meta+k><span class=DocSearch-Button-Container><svg width=20 height=20 class=DocSearch-Search-Icon viewBox="0 0 24 24" aria-hidden=true><circle cx=11 cy=11 r=8 stroke=currentColor fill=none stroke-width=1.4 /><path d="m21 21-4.3-4.3" stroke=currentColor fill=none stroke-linecap=round stroke-linejoin=round /></svg><span class=DocSearch-Button-Placeholder>Search</span></span><span class=DocSearch-Button-Keys></span></button></div></div></div></div></div></div><div class=mantine-hidden-from-xl><nav aria-label=Main class="navbar navbar--fixed-top"><div class="!pr-0 pl-6 xl:pl-0 navbar__inner"><div class=navbar__items><div style="--group-gap:calc(1.375rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:wrap" class="m_4081bf90 mantine-Group-root"><a class="navbar__item navbar__link" href=/max/intro>Guides</a><a aria-current=page class="navbar__item navbar__link navbar__link--active" href=/max/api/>APIs</a><a class="navbar__item navbar__link" href=/mojo/manual/>Mojo</a></div></div><div class="navbar__items navbar__items--right"></div></div><div role=presentation class=navbar-sidebar__backdrop></div></nav></div></div><div style="height:calc(4.5rem * var(--mantine-scale));min-height:calc(4.5rem * var(--mantine-scale))" class=""></div><div style="height:calc(2.625rem * var(--mantine-scale));min-height:calc(2.625rem * var(--mantine-scale))" class="mantine-hidden-from-xl mantine-visible-from-sm"></div><div id=__docusaurus_skipToContent_fallback class="theme-layout-main main-wrapper mainWrapper_z2l0"><div class=docsWrapper_yGWD><button aria-label="Scroll back to top" class="clean-btn theme-back-to-top-button backToTopButton_sjWU" type=button></button><div class=docRoot_oL3q><aside class="theme-doc-sidebar-container docSidebarContainer_XbDZ"><div class=sidebarViewport_cWno><div class=sidebar_YabQ><nav aria-label="Docs sidebar" class="menu thin-scrollbar menu_SIkG"><ul class="theme-doc-sidebar-menu menu__list"><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-1 menu__list-item"><a class=menu__link href=/max/api/><span title=Overview class=linkLabel_WmDU>Overview</span></a><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item sidebar-heading"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist menu__link--sublist-caret" role=button aria-expanded=true href=/max/api/python/><span title=Python class=categoryLinkLabel_W154>Python</span></a></div><ul class=menu__list><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/><span title=max class=linkLabel_WmDU>max</span></a><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-2 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist menu__link--sublist-caret" role=button aria-expanded=false tabindex=0 href=/max/api/python/diagnostics/gpu/><span title=diagnostics class=categoryLinkLabel_W154>diagnostics</span></a></div><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/driver><span title=driver class=linkLabel_WmDU>driver</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/dtype><span title=dtype class=linkLabel_WmDU>dtype</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/engine><span title=engine class=linkLabel_WmDU>engine</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/entrypoints><span title=entrypoints class=linkLabel_WmDU>entrypoints</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/functional><span title=functional class=linkLabel_WmDU>functional</span></a><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-2 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/max/api/python/graph/><span title=graph class=categoryLinkLabel_W154>graph</span></a><button aria-label="Expand sidebar category 'graph'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/interfaces><span title=interfaces class=linkLabel_WmDU>interfaces</span></a><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-2 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/max/api/python/kv_cache/><span title=kv_cache class=categoryLinkLabel_W154>kv_cache</span></a><button aria-label="Expand sidebar category 'kv_cache'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-2 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/max/api/python/nn/><span title=nn class=categoryLinkLabel_W154>nn</span></a><button aria-label="Expand sidebar category 'nn'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-2 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/max/api/python/pipelines/><span title=pipelines class=categoryLinkLabel_W154>pipelines</span></a><button aria-label="Expand sidebar category 'pipelines'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/profiler><span title=profiler class=linkLabel_WmDU>profiler</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/random><span title=random class=linkLabel_WmDU>random</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/tensor><span title=tensor class=linkLabel_WmDU>tensor</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/python/torch><span title=torch class=linkLabel_WmDU>torch</span></a></ul><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item sidebar-heading"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist menu__link--sublist-caret menu__link--active" role=button aria-expanded=true href=/mojo/lib><span title=Mojo class=categoryLinkLabel_W154>Mojo</span></a></div><ul class=menu__list><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/mojo/lib><span title=Overview class=linkLabel_WmDU>Overview</span></a><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-2 menu__list-item"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist menu__link--sublist-caret menu__link--active" role=button aria-expanded=true tabindex=0 href=/mojo/std/><span title="Standard library" class=categoryLinkLabel_W154>Standard library</span></a></div><ul class=menu__list><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-3 menu__list-item"><a class=menu__link tabindex=0 href=/mojo/std/><span title=std class=linkLabel_WmDU>std</span></a><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/algorithm/><span title=algorithm class=categoryLinkLabel_W154>algorithm</span></a><button aria-label="Expand sidebar category 'algorithm'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/base64/><span title=base64 class=categoryLinkLabel_W154>base64</span></a><button aria-label="Expand sidebar category 'base64'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/benchmark/><span title=benchmark class=categoryLinkLabel_W154>benchmark</span></a><button aria-label="Expand sidebar category 'benchmark'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/bit/><span title=bit class=categoryLinkLabel_W154>bit</span></a><button aria-label="Expand sidebar category 'bit'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/builtin/><span title=builtin class=categoryLinkLabel_W154>builtin</span></a><button aria-label="Expand sidebar category 'builtin'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist menu__link--active" tabindex=0 href=/mojo/std/collections/><span title=collections class=categoryLinkLabel_W154>collections</span></a><button aria-label="Collapse sidebar category 'collections'" aria-expanded=true type=button class="clean-btn menu__caret"></button></div><ul class=menu__list><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/bitset/><span title=bitset class=categoryLinkLabel_W154>bitset</span></a><button aria-label="Expand sidebar category 'bitset'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/counter/><span title=counter class=categoryLinkLabel_W154>counter</span></a><button aria-label="Expand sidebar category 'counter'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/deque/><span title=deque class=categoryLinkLabel_W154>deque</span></a><button aria-label="Expand sidebar category 'deque'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/dict/><span title=dict class=categoryLinkLabel_W154>dict</span></a><button aria-label="Expand sidebar category 'dict'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/inline_array/><span title=inline_array class=categoryLinkLabel_W154>inline_array</span></a><button aria-label="Expand sidebar category 'inline_array'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/interval/><span title=interval class=categoryLinkLabel_W154>interval</span></a><button aria-label="Expand sidebar category 'interval'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/linked_list/><span title=linked_list class=categoryLinkLabel_W154>linked_list</span></a><button aria-label="Expand sidebar category 'linked_list'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/list/><span title=list class=categoryLinkLabel_W154>list</span></a><button aria-label="Expand sidebar category 'list'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/optional/><span title=optional class=categoryLinkLabel_W154>optional</span></a><button aria-label="Expand sidebar category 'optional'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/set/><span title=set class=categoryLinkLabel_W154>set</span></a><button aria-label="Expand sidebar category 'set'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-4 menu__list-item"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist menu__link--active" tabindex=0 href=/mojo/std/collections/string/><span title=string class=categoryLinkLabel_W154>string</span></a><button aria-label="Collapse sidebar category 'string'" aria-expanded=true type=button class="clean-btn menu__caret"></button></div><ul class=menu__list><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-5 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/string/codepoint/><span title=codepoint class=categoryLinkLabel_W154>codepoint</span></a><button aria-label="Expand sidebar category 'codepoint'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-5 menu__list-item"><a class=menu__link tabindex=0 href=/mojo/std/collections/string/format/><span title=format class=linkLabel_WmDU>format</span></a><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-5 menu__list-item"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist menu__link--active" tabindex=0 href=/mojo/std/collections/string/string/><span title=string class=categoryLinkLabel_W154>string</span></a><button aria-label="Collapse sidebar category 'string'" aria-expanded=true type=button class="clean-btn menu__caret"></button></div><ul class=menu__list><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-6 menu__list-item"><a class="menu__link menu__link--active" aria-current=page tabindex=0 href=/mojo/std/collections/string/string/String><span title=String class=linkLabel_WmDU>String</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-6 menu__list-item"><a class=menu__link tabindex=0 href=/mojo/std/collections/string/string/ascii><span title=ascii class=linkLabel_WmDU>ascii</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-6 menu__list-item"><a class=menu__link tabindex=0 href=/mojo/std/collections/string/string/atof><span title=atof class=linkLabel_WmDU>atof</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-6 menu__list-item"><a class=menu__link tabindex=0 href=/mojo/std/collections/string/string/atol><span title=atol class=linkLabel_WmDU>atol</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-6 menu__list-item"><a class=menu__link tabindex=0 href=/mojo/std/collections/string/string/chr><span title=chr class=linkLabel_WmDU>chr</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-6 menu__list-item"><a class=menu__link tabindex=0 href=/mojo/std/collections/string/string/ord><span title=ord class=linkLabel_WmDU>ord</span></a></ul><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-5 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/collections/string/string_slice/><span title=string_slice class=categoryLinkLabel_W154>string_slice</span></a><button aria-label="Expand sidebar category 'string_slice'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div></ul></ul><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/compile/><span title=compile class=categoryLinkLabel_W154>compile</span></a><button aria-label="Expand sidebar category 'compile'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/complex/><span title=complex class=categoryLinkLabel_W154>complex</span></a><button aria-label="Expand sidebar category 'complex'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/documentation/><span title=documentation class=categoryLinkLabel_W154>documentation</span></a><button aria-label="Expand sidebar category 'documentation'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/format/><span title=format class=categoryLinkLabel_W154>format</span></a><button aria-label="Expand sidebar category 'format'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/gpu/><span title=gpu class=categoryLinkLabel_W154>gpu</span></a><button aria-label="Expand sidebar category 'gpu'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/hashlib/><span title=hashlib class=categoryLinkLabel_W154>hashlib</span></a><button aria-label="Expand sidebar category 'hashlib'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/io/><span title=io class=categoryLinkLabel_W154>io</span></a><button aria-label="Expand sidebar category 'io'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/iter/><span title=iter class=categoryLinkLabel_W154>iter</span></a><button aria-label="Expand sidebar category 'iter'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/itertools/><span title=itertools class=categoryLinkLabel_W154>itertools</span></a><button aria-label="Expand sidebar category 'itertools'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/logger/><span title=logger class=categoryLinkLabel_W154>logger</span></a><button aria-label="Expand sidebar category 'logger'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/math/><span title=math class=categoryLinkLabel_W154>math</span></a><button aria-label="Expand sidebar category 'math'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/memory/><span title=memory class=categoryLinkLabel_W154>memory</span></a><button aria-label="Expand sidebar category 'memory'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/os/><span title=os class=categoryLinkLabel_W154>os</span></a><button aria-label="Expand sidebar category 'os'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/pathlib/><span title=pathlib class=categoryLinkLabel_W154>pathlib</span></a><button aria-label="Expand sidebar category 'pathlib'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-3 menu__list-item"><a class=menu__link tabindex=0 href=/mojo/std/prelude/><span title=prelude class=linkLabel_WmDU>prelude</span></a><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/pwd/><span title=pwd class=categoryLinkLabel_W154>pwd</span></a><button aria-label="Expand sidebar category 'pwd'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/python/><span title=python class=categoryLinkLabel_W154>python</span></a><button aria-label="Expand sidebar category 'python'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/random/><span title=random class=categoryLinkLabel_W154>random</span></a><button aria-label="Expand sidebar category 'random'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/reflection/><span title=reflection class=categoryLinkLabel_W154>reflection</span></a><button aria-label="Expand sidebar category 'reflection'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/runtime/><span title=runtime class=categoryLinkLabel_W154>runtime</span></a><button aria-label="Expand sidebar category 'runtime'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/stat/><span title=stat class=categoryLinkLabel_W154>stat</span></a><button aria-label="Expand sidebar category 'stat'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/subprocess/><span title=subprocess class=categoryLinkLabel_W154>subprocess</span></a><button aria-label="Expand sidebar category 'subprocess'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/sys/><span title=sys class=categoryLinkLabel_W154>sys</span></a><button aria-label="Expand sidebar category 'sys'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/tempfile/><span title=tempfile class=categoryLinkLabel_W154>tempfile</span></a><button aria-label="Expand sidebar category 'tempfile'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/testing/><span title=testing class=categoryLinkLabel_W154>testing</span></a><button aria-label="Expand sidebar category 'testing'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/time/><span title=time class=categoryLinkLabel_W154>time</span></a><button aria-label="Expand sidebar category 'time'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-3 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist" tabindex=0 href=/mojo/std/utils/><span title=utils class=categoryLinkLabel_W154>utils</span></a><button aria-label="Expand sidebar category 'utils'" aria-expanded=false type=button class="clean-btn menu__caret"></button></div></ul><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-2 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist menu__link--sublist-caret" role=button aria-expanded=false tabindex=0 href=/mojo/kernels/comm/><span title="MAX AI kernels" class=categoryLinkLabel_W154>MAX AI kernels</span></a></div><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-2 menu__list-item menu__list-item--collapsed"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist menu__link--sublist-caret" role=button aria-expanded=false tabindex=0 href=/mojo/manual/decorators/><span title=Decorators class=categoryLinkLabel_W154>Decorators</span></a></div></ul><li class="theme-doc-sidebar-item-category theme-doc-sidebar-item-category-level-1 menu__list-item sidebar-heading"><div class=menu__list-item-collapsible><a class="categoryLink_byQd menu__link menu__link--sublist menu__link--sublist-caret" role=button aria-expanded=true href=/max/api/serve><span title=REST class=categoryLinkLabel_W154>REST</span></a></div><ul class=menu__list><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/serve><span title="Get started" class=linkLabel_WmDU>Get started</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/serve#section/OpenAI-API-compatibility><span title="OpenAI API compatibility" class=linkLabel_WmDU>OpenAI API compatibility</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/serve#operation/createChatCompletion><span title="Create chat completion" class=linkLabel_WmDU>Create chat completion</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/serve#operation/createCompletion><span title="Create completion" class=linkLabel_WmDU>Create completion</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/serve#operation/createEmbedding><span title="Create embeddings" class=linkLabel_WmDU>Create embeddings</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/serve#operation/createBatch><span title="Create batch" class=linkLabel_WmDU>Create batch</span></a><li class="theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item"><a class=menu__link tabindex=0 href=/max/api/serve#operation/listModels><span title="List models" class=linkLabel_WmDU>List models</span></a></ul></ul></nav><div class=mantine-hidden-from-xl><button type=button title="Collapse sidebar" aria-label="Collapse sidebar" class="button button--secondary button--outline collapseSidebarButton_JQXm"><div style="--group-gap:calc(0.75rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:wrap" class="m_4081bf90 mantine-Group-root"><svg viewBox="0 0 20 20" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(1rem * var(--mantine-scale));height:calc(1rem * var(--mantine-scale))" class=collapseSidebarButtonIcon_Pv6V><path d="m6.958 1.042 8.75 8.75-8.75 8.75" stroke=currentColor stroke-width=1.5 /><path d="m.708 1.042 8.75 8.75-8.75 8.75" stroke=currentColor stroke-width=1.5 /></svg> <p style=margin:0rem;padding:0rem class="body-14-light mantine-Text-root">Collapse sidebar</div></button></div></div></div></aside><main class=docMainContainer_TBSr><div class="container padding-top--md padding-bottom--lg"><div class=row><div class="col docItemCol_R_bt"><div class=docItemContainer_qGQi><article class=struct><div class=mantine-visible-from-sm><nav class="theme-doc-breadcrumbs line-clamp-1 w-[calc(100%-24px)] mb-6 mt-3 xl:mt-0" aria-label=Breadcrumbs><ul class=breadcrumbs itemscope itemtype=https://schema.org/BreadcrumbList><a aria-label="Home page" class=breadcrumbs__link href=/><svg viewBox="0 0 14 14" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(0.875rem * var(--mantine-scale));height:calc(0.875rem * var(--mantine-scale))" class=mt-0.5><path d="M6.5 1.042.542 7v5.953h4.875V9.161h2.166v3.797h3.792v-.812c0-.152.12-.27.27-.27h.813V7L6.5 1.042Zm2.167 7.041H4.333v3.792H1.625V7.45L6.5 2.575l4.875 4.875v4.154c0 .152-.12.271-.27.271H8.666V8.083Z" fill=currentColor /></svg> Docs</a><li itemscope itemprop=itemListElement itemtype=https://schema.org/ListItem class=breadcrumbs__item><span class=breadcrumbs__link>/</span><a class=breadcrumbs__link itemprop=item href=/max/api/><span itemprop=name>APIs</span></a><meta itemprop=position content=2 /><li class=breadcrumbs__item><span class=breadcrumbs__link>/</span><span class=breadcrumbs__link>Mojo</span><meta itemprop=position content=1 /><li class=breadcrumbs__item><span class=breadcrumbs__link>/</span><span class=breadcrumbs__link>Standard library</span><meta itemprop=position content=2 /><li itemscope itemprop=itemListElement itemtype=https://schema.org/ListItem class=breadcrumbs__item><span class=breadcrumbs__link>/</span><a class=breadcrumbs__link itemprop=item href=/mojo/std/collections/><span itemprop=name>collections</span></a><meta itemprop=position content=3 /><li itemscope itemprop=itemListElement itemtype=https://schema.org/ListItem class=breadcrumbs__item><span class=breadcrumbs__link>/</span><a class=breadcrumbs__link itemprop=item href=/mojo/std/collections/string/><span itemprop=name>string</span></a><meta itemprop=position content=4 /><li itemscope itemprop=itemListElement itemtype=https://schema.org/ListItem class=breadcrumbs__item><span class=breadcrumbs__link>/</span><a class=breadcrumbs__link itemprop=item href=/mojo/std/collections/string/string/><span itemprop=name>string</span></a><meta itemprop=position content=5 /><li itemscope itemprop=itemListElement itemtype=https://schema.org/ListItem class="breadcrumbs__item breadcrumbs__item--active"><span class=breadcrumbs__link>/</span><span class=breadcrumbs__link itemprop=name>String</span><meta itemprop=position content=6 /></ul></nav></div><div class=mantine-hidden-from-sm><div class="my-4 theme-doc-toc-mobile tocMobile_ITEo !border-none"><div style=--group-gap:var(--mantine-spacing-md);--group-align:center;--group-justify:space-between;--group-wrap:nowrap class="mb-3 m_4081bf90 mantine-Group-root"><nav class="theme-doc-breadcrumbs line-clamp-1 w-[calc(100%-24px)] mb-6 mt-3 xl:mt-0" aria-label=Breadcrumbs><ul class=breadcrumbs itemscope itemtype=https://schema.org/BreadcrumbList><a aria-label="Home page" class=breadcrumbs__link href=/><svg viewBox="0 0 14 14" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(0.875rem * var(--mantine-scale));height:calc(0.875rem * var(--mantine-scale))" class=mt-0.5><path d="M6.5 1.042.542 7v5.953h4.875V9.161h2.166v3.797h3.792v-.812c0-.152.12-.27.27-.27h.813V7L6.5 1.042Zm2.167 7.041H4.333v3.792H1.625V7.45L6.5 2.575l4.875 4.875v4.154c0 .152-.12.271-.27.271H8.666V8.083Z" fill=currentColor /></svg> Docs</a><li itemscope itemprop=itemListElement itemtype=https://schema.org/ListItem class=breadcrumbs__item><span class=breadcrumbs__link>/</span><a class=breadcrumbs__link itemprop=item href=/max/api/><span itemprop=name>APIs</span></a><meta itemprop=position content=2 /><li class=breadcrumbs__item><span class=breadcrumbs__link>/</span><span class=breadcrumbs__link>Mojo</span><meta itemprop=position content=1 /><li class=breadcrumbs__item><span class=breadcrumbs__link>/</span><span class=breadcrumbs__link>Standard library</span><meta itemprop=position content=2 /><li itemscope itemprop=itemListElement itemtype=https://schema.org/ListItem class=breadcrumbs__item><span class=breadcrumbs__link>/</span><a class=breadcrumbs__link itemprop=item href=/mojo/std/collections/><span itemprop=name>collections</span></a><meta itemprop=position content=3 /><li itemscope itemprop=itemListElement itemtype=https://schema.org/ListItem class=breadcrumbs__item><span class=breadcrumbs__link>/</span><a class=breadcrumbs__link itemprop=item href=/mojo/std/collections/string/><span itemprop=name>string</span></a><meta itemprop=position content=4 /><li itemscope itemprop=itemListElement itemtype=https://schema.org/ListItem class=breadcrumbs__item><span class=breadcrumbs__link>/</span><a class=breadcrumbs__link itemprop=item href=/mojo/std/collections/string/string/><span itemprop=name>string</span></a><meta itemprop=position content=5 /><li itemscope itemprop=itemListElement itemtype=https://schema.org/ListItem class="breadcrumbs__item breadcrumbs__item--active"><span class=breadcrumbs__link>/</span><span class=breadcrumbs__link itemprop=name>String</span><meta itemprop=position content=6 /></ul></nav><button class="mantine-focus-auto clean-btn tocCollapsibleButton_QABo tocCollapsibleButtonCollapsed_CrWs m_87cf2631 mantine-UnstyledButton-root" type=button></button></div></div></div><div class="theme-doc-markdown markdown"><header class=api><p class=suptitle>Mojo <span class=page-type>struct</span><h1>String</h1></header><section class=mojo-docs>
<div class=mojo-function-sig>
<p><code>struct String</code></p>
</div>
<p>Represents a mutable string.</p>
<p>This is Mojo's primary text representation, designed to efficiently handle
UTF-8 encoded text while providing a safe and ergonomic interface for
string manipulation.</p>
<p>You can create a <code>String</code> by assigning a string literal to a variable or
with the <code>String</code> constructor:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code># From string literals (String type is inferred)
var hello = "Hello"

# From String constructor
var world = String("World")
print(hello, world)    # "Hello World"</code></pre></div></div>
<p>You can convert many Mojo types to a <code>String</code> because it's common to
implement the <a class="" href=/mojo/std/builtin/str/Stringable><code>Stringable</code></a> trait:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>var int : Int = 42
print(String(int))    # "42"</code></pre></div></div>
<p>If you have a custom type you want to convert to a string, you can implement
the <a class="" href=/mojo/std/builtin/str/Stringable><code>Stringable</code></a> trait like this:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>@fieldwise_init
struct Person(Stringable):
    var name: String
    var age: Int

    fn __str__(self) -> String:
        return self.name + " (" + String(self.age) + ")"

var person = Person("Alice", 30)
print(String(person))      # => Alice (30)</code></pre></div></div>
<p>However, <code>print()</code> doesn't actually specify <code>String</code> as its argument type.
Instead, it accepts any type that conforms to the
<a class="" href=/mojo/std/format/Writable><code>Writable</code></a> trait (<code>String</code> conforms to
this trait, which is why you can pass it to <code>print()</code>). That means it's
actually more efficient to pass any type that implements <code>Writable</code>
directly to <code>print()</code> (instead of first converting it to <code>String</code>).
For example, float types are also writable:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>var float : Float32 = 3.14
print(float)</code></pre></div></div>
<p>Be aware of the following characteristics when working with <code>String</code>:</p>
<ul>
<li class="">
<p><strong>UTF-8 encoding</strong>: Strings store UTF-8 encoded text, so byte length may
differ from character count. Use <code>len(string.codepoints())</code> to get
the codepoint count:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>var text = "cafÃ©"                # 4 Unicode characters
print(len(text))                 # Prints 5 (Ã© is 2 bytes in UTF-8)
print(len(text.codepoints()))    # Prints 4 (correct Unicode count)</code></pre></div></div>
</li>
<li class="">
<p><strong>Always mutable</strong>: You can modify strings in-place:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>var message = "Hello"
message += " World"        # In-place concatenation
print(message)             # "Hello World"</code></pre></div></div>
<p>If you want a compile-time immutable string, use <code>comptime</code>:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>comptime GREETING = "Immutable string"  # Fixed at compile time
GREETING = "Not gonna happen"        # error: expression must be mutable in assignment</code></pre></div></div>
</li>
<li class="">
<p><strong>Value semantics</strong>: String assignment creates a copy, but it's optimized
with copy-on-write so that the actual copying happens only if/when one of
the strings is modified.</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>var str1 = "Hello"
var str2 = str1            # Currently references the same data
str2 += " World"           # Now str2 becomes a copy of str1
print(str1)                # "Hello"
print(str2)                # "Hello World"</code></pre></div></div>
</li>
</ul>
<p>More examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>var text = "Hello"

# String properties and indexing
print(len(text))     # 5
print(text[1])       # e
print(text[-1])      # o

# In-place concatenation
text += " World"
print(text)

# Searching and checking
if "World" in text:
    print("Found 'World' in text")

var pos = text.find("World")
if pos != -1:
    print("'World' found at position:", pos)

# String replacement
var replaced = text.replace("Hello", "Hi")   # "Hi World"
print(replaced)

# String formatting
var name = "Alice"
var age = 30
var formatted = "{} is {} years old".format(name, age)
print(formatted)    # "Alice is 30 years old"</code></pre></div></div>
<p>Related functions:</p>
<ul>
<li class="">String-to-number conversions:
<a class="" href=/mojo/std/collections/string/string/atof><code>atof()</code></a>,
<a class="" href=/mojo/std/collections/string/string/atol><code>atol()</code></a>).</li>
<li class="">Character code conversions:
<a class="" href=/mojo/std/collections/string/string/chr><code>chr()</code></a>,
<a class="" href=/mojo/std/collections/string/string/ord><code>ord()</code></a>).</li>
<li class="">String formatting:
<a class="" href=/mojo/std/collections/string/string/String/#format><code>format()</code></a>.</li>
</ul>
<p>Related types:</p>
<ul>
<li class=""><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: A non-owning
view of string data, which can be either mutable or immutable.</li>
<li class=""><a class="" href=/mojo/std/collections/string/string_slice/#StaticString><code>StaticString</code></a>: An
alias for an immutable constant <code>StringSlice</code>.</li>
<li class=""><a class="" href=/mojo/std/builtin/string_literal/StringLiteral/><code>StringLiteral</code></a>: A
string literal. String literals are compile-time values.</li>
</ul>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id=implemented-traits>Implemented traits<a href=#implemented-traits class=hash-link aria-label="Direct link to Implemented traits" title="Direct link to Implemented traits" translate=no>â</a></h2>
<p><a class="" href=/mojo/std/builtin/anytype/AnyType><code>AnyType</code></a>,
<a class="" href=/mojo/std/builtin/bool/Boolable><code>Boolable</code></a>,
<a class="" href=/mojo/std/builtin/comparable/Comparable><code>Comparable</code></a>,
<a class="" href=/mojo/std/python/conversions/ConvertibleFromPython><code>ConvertibleFromPython</code></a>,
<a class="" href=/mojo/std/python/conversions/ConvertibleToPython><code>ConvertibleToPython</code></a>,
<a class="" href=/mojo/std/builtin/value/Copyable><code>Copyable</code></a>,
<a class="" href=/mojo/std/builtin/value/Defaultable><code>Defaultable</code></a>,
<a class="" href=/mojo/std/builtin/comparable/Equatable><code>Equatable</code></a>,
<a class="" href=/mojo/std/builtin/floatable/FloatableRaising><code>FloatableRaising</code></a>,
<a class="" href=/mojo/std/hashlib/hash/Hashable><code>Hashable</code></a>,
<a class="" href=/mojo/std/builtin/value/ImplicitlyCopyable><code>ImplicitlyCopyable</code></a>,
<a class="" href=/mojo/std/builtin/anytype/ImplicitlyDestructible><code>ImplicitlyDestructible</code></a>,
<a class="" href=/mojo/std/builtin/int/IntableRaising><code>IntableRaising</code></a>,
<a class="" href=/mojo/std/builtin/value/Movable><code>Movable</code></a>,
<a class="" href=/mojo/std/os/pathlike/PathLike><code>PathLike</code></a>,
<a class="" href=/mojo/std/builtin/repr/Representable><code>Representable</code></a>,
<a class="" href=/mojo/std/builtin/len/Sized><code>Sized</code></a>,
<a class="" href=/mojo/std/builtin/str/Stringable><code>Stringable</code></a>,
<a class="" href=/mojo/std/format/Writable><code>Writable</code></a>,
<a class="" href=/mojo/std/format/Writer><code>Writer</code></a></p>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id=comptime-members><code>comptime</code> members<a href=#comptime-members class=hash-link aria-label="Direct link to comptime-members" title="Direct link to comptime-members" translate=no>â</a></h2>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__copyinit__is_trivial><code>__copyinit__is_trivial</code><a href=#__copyinit__is_trivial class=hash-link aria-label="Direct link to __copyinit__is_trivial" title="Direct link to __copyinit__is_trivial" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime __copyinit__is_trivial = False</code></p>
</div>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__del__is_trivial><code>__del__is_trivial</code><a href=#__del__is_trivial class=hash-link aria-label="Direct link to __del__is_trivial" title="Direct link to __del__is_trivial" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime __del__is_trivial = False</code></p>
</div>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__moveinit__is_trivial><code>__moveinit__is_trivial</code><a href=#__moveinit__is_trivial class=hash-link aria-label="Direct link to __moveinit__is_trivial" title="Direct link to __moveinit__is_trivial" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime __moveinit__is_trivial = False</code></p>
</div>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=ascii_letters><code>ASCII_LETTERS</code><a href=#ascii_letters class=hash-link aria-label="Direct link to ascii_letters" title="Direct link to ascii_letters" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime ASCII_LETTERS = String.ASCII_LOWERCASE.__add__["abcdefghijklmnopqrstuvwxyz"](String.ASCII_UPPERCASE)</code></p>
</div>
<p>All ASCII letters (lowercase and uppercase).</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=ascii_lowercase><code>ASCII_LOWERCASE</code><a href=#ascii_lowercase class=hash-link aria-label="Direct link to ascii_lowercase" title="Direct link to ascii_lowercase" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"</code></p>
</div>
<p>All lowercase ASCII letters.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=ascii_uppercase><code>ASCII_UPPERCASE</code><a href=#ascii_uppercase class=hash-link aria-label="Direct link to ascii_uppercase" title="Direct link to ascii_uppercase" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"</code></p>
</div>
<p>All uppercase ASCII letters.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=digits><code>DIGITS</code><a href=#digits class=hash-link aria-label="Direct link to digits" title="Direct link to digits" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime DIGITS = "0123456789"</code></p>
</div>
<p>All decimal digit characters.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=flag_has_nul_terminator><code>FLAG_HAS_NUL_TERMINATOR</code><a href=#flag_has_nul_terminator class=hash-link aria-label="Direct link to flag_has_nul_terminator" title="Direct link to flag_has_nul_terminator" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime FLAG_HAS_NUL_TERMINATOR = (1 &lt;&lt; (Int.BITWIDTH - 3))</code></p>
</div>
<p>Flag indicating string has accessible nul terminator.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=flag_is_inline><code>FLAG_IS_INLINE</code><a href=#flag_is_inline class=hash-link aria-label="Direct link to flag_is_inline" title="Direct link to flag_is_inline" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime FLAG_IS_INLINE = (1 &lt;&lt; (Int.BITWIDTH - 1))</code></p>
</div>
<p>Flag indicating string uses inline (SSO) storage.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=flag_is_ref_counted><code>FLAG_IS_REF_COUNTED</code><a href=#flag_is_ref_counted class=hash-link aria-label="Direct link to flag_is_ref_counted" title="Direct link to flag_is_ref_counted" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime FLAG_IS_REF_COUNTED = (1 &lt;&lt; (Int.BITWIDTH - 2))</code></p>
</div>
<p>Flag indicating string uses reference-counted storage.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=hex_digits><code>HEX_DIGITS</code><a href=#hex_digits class=hash-link aria-label="Direct link to hex_digits" title="Direct link to hex_digits" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime HEX_DIGITS = String.DIGITS.__add__["0123456789"]("abcdef").__add__["0123456789abcdef"]("ABCDEF")</code></p>
</div>
<p>All hexadecimal digit characters.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=inline_capacity><code>INLINE_CAPACITY</code><a href=#inline_capacity class=hash-link aria-label="Direct link to inline_capacity" title="Direct link to inline_capacity" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime INLINE_CAPACITY = (((Int.BITWIDTH // 8) * 3) - 1)</code></p>
</div>
<p>Maximum bytes for inline (SSO) string storage.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=inline_length_mask><code>INLINE_LENGTH_MASK</code><a href=#inline_length_mask class=hash-link aria-label="Direct link to inline_length_mask" title="Direct link to inline_length_mask" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime INLINE_LENGTH_MASK = (31 &lt;&lt; String.INLINE_LENGTH_START)</code></p>
</div>
<p>Bit mask for extracting inline string length.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=inline_length_start><code>INLINE_LENGTH_START</code><a href=#inline_length_start class=hash-link aria-label="Direct link to inline_length_start" title="Direct link to inline_length_start" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime INLINE_LENGTH_START = (Int.BITWIDTH - 8)</code></p>
</div>
<p>Bit position where inline length field starts.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=oct_digits><code>OCT_DIGITS</code><a href=#oct_digits class=hash-link aria-label="Direct link to oct_digits" title="Direct link to oct_digits" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime OCT_DIGITS = "01234567"</code></p>
</div>
<p>All octal digit characters.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=printable><code>PRINTABLE</code><a href=#printable class=hash-link aria-label="Direct link to printable" title="Direct link to printable" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime PRINTABLE = String.DIGITS.__add__["0123456789"](String.ASCII_LETTERS).__add__["0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"](String.PUNCTUATION).__add__["0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\22#$%&'()*+,-./:;&lt;=>?@[\\]^_</code>{|}~"](" \t\n\r\v\f")`</p>
</div>
<p>All printable ASCII characters.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=punctuation><code>PUNCTUATION</code><a href=#punctuation class=hash-link aria-label="Direct link to punctuation" title="Direct link to punctuation" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime PUNCTUATION = "!\22#$%&'()*+,-./:;&lt;=>?@[\\]^_</code>{|}~"`</p>
</div>
<p>All ASCII punctuation characters.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=ref_count_size><code>REF_COUNT_SIZE</code><a href=#ref_count_size class=hash-link aria-label="Direct link to ref_count_size" title="Direct link to ref_count_size" translate=no>â</a></h3>
<div class=mojo-alias-detail>
<div class=mojo-alias-sig>
<p><code>comptime REF_COUNT_SIZE = size_of[Atomic[DType.index]]()</code></p>
</div>
<p>Size of the reference count prefix for heap strings.</p>
</div>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id=methods>Methods<a href=#methods class=hash-link aria-label="Direct link to Methods" title="Direct link to Methods" translate=no>â</a></h2>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__init__><code>__init__</code><a href=#__init__ class=hash-link aria-label="Direct link to __init__" title="Direct link to __init__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__(out self)</code></p>
</div>
<p>Construct an empty string.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__(out self, *, capacity: Int)</code></p>
</div>
<p>Construct an empty string with a given capacity.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>capacity</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The capacity of the string to allocate.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>@implicit</code>
<code>__init__(out self, data: StringSlice[StaticConstantOrigin])</code></p>
</div>
<p>Construct a <code>String</code> from a <code>StaticString</code> without allocating.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>data</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The static constant string to refer to.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>@implicit</code>
<code>__init__(out self, data: StringLiteral[value])</code></p>
</div>
<p>Construct a <code>String</code> from a <code>StringLiteral</code> without allocating.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>data</b> (<a class="" href=/mojo/std/builtin/string_literal/StringLiteral><code>StringLiteral</code></a>): The static constant string to refer to.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__(out self, *, unsafe_from_utf8: Span[Byte, origin])</code></p>
</div>
<p>Construct a string by copying the data. This constructor is explicit because it can involve memory allocation.</p>
<p>Consider using the <code>String(from_utf8=...)</code> or
<code>String(from_utf8_lossy=...)</code> constructors instead, as they are safer
alternatives to the <code>unsafe_from_utf8</code> constructor.</p>
<p>Safety:
<code>unsafe_from_utf8</code> MUST be valid UTF-8 encoded data.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>unsafe_from_utf8</b> (<a class="" href=/mojo/std/memory/span/Span><code>Span</code></a>): The utf8 bytes to copy.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__(out self, *, from_utf8_lossy: Span[Byte, origin])</code></p>
</div>
<p>Construct a string from a span of bytes, including invalid UTF-8.</p>
<p>Since <code>String</code> is guaranteed to be valid UTF-8, invalid UTF-8 sequences
are replaced with the <code>U+FFFD</code> replacement character: <code>ï¿½</code>.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code># Valid UTF-8 sequence
var fire_emoji_bytes = [Byte(0xF0), 0x9F, 0x94, 0xA5]
var fire_emoji = String(from_utf8_lossy=fire_emoji_bytes)
assert_equal(fire_emoji, "ð¥")

# Invalid UTF-8 sequence
# "mojo&lt;invalid sequence>"
var mojo_bytes = [Byte(0x6D), 0x6F, 0x6A, 0x6F, 0xF0, 0x90, 0x80]
var mojo = String(from_utf8_lossy=mojo_bytes)
assert_equal(mojo, "mojoï¿½")</code></pre></div></div>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>from_utf8_lossy</b> (<a class="" href=/mojo/std/memory/span/Span><code>Span</code></a>): The bytes to convert to a string.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__(out self, *, from_utf8: Span[Byte, origin])</code></p>
</div>
<p>Construct a string from a span of bytes, raising an error if the data is not valid UTF-8.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>from_utf8</b> (<a class="" href=/mojo/std/memory/span/Span><code>Span</code></a>): The bytes to convert to a string.</li>
</ul>
<p><strong>Raises:</strong></p>
<p>An error if the data is not valid UTF-8.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__[T: Stringable](out self, value: T)</code></p>
</div>
<p>Initialize from a type conforming to <code>Stringable</code>.</p>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>T</b> (<a class="" href=/mojo/std/builtin/str/Stringable><code>Stringable</code></a>): The type conforming to Stringable.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>value</b> (<code>T</code>): The object to get the string representation of.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__[*Ts: Writable](out self, *args: *Ts, *, sep: StringSlice[StaticConstantOrigin] = "", end: StringSlice[StaticConstantOrigin] = "")</code></p>
</div>
<p>Construct a string by concatenating a sequence of Writable arguments.</p>
<p>Examples:</p>
<p>Construct a String from several <code>Writable</code> arguments:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>var string = String(1, 2.0, "three", sep=", ")
print(string) # "1, 2.0, three"</code></pre></div></div>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>*Ts</b> (<a class="" href=/mojo/std/format/Writable><code>Writable</code></a>): Types of the provided argument sequence.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>*args</b> (<code>*Ts</code>): A sequence of Writable arguments.</li>
<li class="">â<b>sep</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The separator used between elements.</li>
<li class="">â<b>end</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The String to write after printing the elements.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__[*Ts: Writable](out self, args: VariadicPack[is_owned, Writable, Ts], sep: StringSlice[StaticConstantOrigin] = "", end: StringSlice[StaticConstantOrigin] = "")</code></p>
</div>
<p>Construct a string by passing a variadic pack.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>fn variadic_pack_to_string[
    *Ts: Writable,
](*args: *Ts) -> String:
    return String(args)

string = variadic_pack_to_string(1, ", ", 2.0, ", ", "three")</code></pre></div></div>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>*Ts</b> (<a class="" href=/mojo/std/format/Writable><code>Writable</code></a>): Types of the provided argument sequence.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>args</b> (<a class="" href=/mojo/std/builtin/variadics/VariadicPack><code>VariadicPack</code></a>): A VariadicPack of Writable arguments.</li>
<li class="">â<b>sep</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The separator used between elements.</li>
<li class="">â<b>end</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The String to write after printing the elements.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__(out self, *, unsafe_uninit_length: Int)</code></p>
</div>
<p>Construct a String with the specified length, with uninitialized memory. This is unsafe, as it relies on the caller initializing the elements with unsafe operations, not assigning over the uninitialized data.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>unsafe_uninit_length</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The number of bytes to allocate.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__(out self, *, unsafe_from_utf8_ptr: UnsafePointer[c_char, origin])</code></p>
</div>
<p>Creates a string from a UTF-8 encoded nul-terminated pointer.</p>
<p>Safety:</p>
<ul>
<li class=""><code>unsafe_from_utf8_ptr</code> MUST be valid UTF-8 encoded data.</li>
<li class=""><code>unsafe_from_utf8_ptr</code> MUST be null terminated.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>unsafe_from_utf8_ptr</b> (<a class="" href=/mojo/std/memory/unsafe_pointer/UnsafePointer><code>UnsafePointer</code></a>): An <code>UnsafePointer[Byte]</code> of null-terminated bytes encoded in UTF-8.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__(out self, *, unsafe_from_utf8_ptr: UnsafePointer[UInt8, origin])</code></p>
</div>
<p>Creates a string from a UTF-8 encoded nul-terminated pointer.</p>
<p>Safety:</p>
<ul>
<li class=""><code>unsafe_from_utf8_ptr</code> MUST be valid UTF-8 encoded data.</li>
<li class=""><code>unsafe_from_utf8_ptr</code> MUST be null terminated.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>unsafe_from_utf8_ptr</b> (<a class="" href=/mojo/std/memory/unsafe_pointer/UnsafePointer><code>UnsafePointer</code></a>): An <code>UnsafePointer[Byte]</code> of null-terminated bytes encoded in UTF-8.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__init__(out self, *, py: PythonObject)</code></p>
</div>
<p>Construct a <code>String</code> from a PythonObject.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>py</b> (<a class="" href=/mojo/std/python/python_object/PythonObject><code>PythonObject</code></a>): The PythonObject to convert from.</li>
</ul>
<p><strong>Raises:</strong></p>
<p>An error if the conversion failed.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__copyinit__><code>__copyinit__</code><a href=#__copyinit__ class=hash-link aria-label="Direct link to __copyinit__" title="Direct link to __copyinit__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__copyinit__(out self, other: Self)</code></p>
</div>
<p>Copy initialize the string from another string.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>other</b> (<code>Self</code>): The string to copy.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__moveinit__><code>__moveinit__</code><a href=#__moveinit__ class=hash-link aria-label="Direct link to __moveinit__" title="Direct link to __moveinit__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__moveinit__(out self, deinit other: Self)</code></p>
</div>
<p>Move initialize the string from another string.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>other</b> (<code>Self</code>): The string to move.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__del__><code>__del__</code><a href=#__del__ class=hash-link aria-label="Direct link to __del__" title="Direct link to __del__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__del__(deinit self)</code></p>
</div>
<p>Destroy the string data.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__bool__><code>__bool__</code><a href=#__bool__ class=hash-link aria-label="Direct link to __bool__" title="Direct link to __bool__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__bool__(self) -> Bool</code></p>
</div>
<p>Checks if the string is not empty.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if the string length is greater than zero, and False otherwise.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__getitem__><code>__getitem__</code><a href=#__getitem__ class=hash-link aria-label="Direct link to __getitem__" title="Direct link to __getitem__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__getitem__[I: Indexer, //](self, *, byte: I) -> StringSlice[self]</code></p>
</div>
<p>Gets a single byte at the specified byte index.</p>
<p>This performs byte-level indexing, not character (codepoint) indexing.
For strings containing multi-byte UTF-8 characters <code>byte</code> must fall on
a codepoint boundary and an entire codepoint will be returned.
Aborts if <code>byte</code> does not fall on a codepoint boundary.</p>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>I</b> (<a class="" href=/mojo/std/builtin/int/Indexer><code>Indexer</code></a>): A type that can be used as an index.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>byte</b> (<code>I</code>): The byte index (0-based). Negative indices count from the end.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: A StringSlice containing a single byte at the specified position.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__getitem__(self, span: ContiguousSlice) -> StringSlice[self]</code></p>
</div>
<p>Gets a substring at the specified byte positions.</p>
<p>This performs byte-level slicing, not character (codepoint) slicing.
The start and end positions are byte indices. For strings containing
multi-byte UTF-8 characters, slicing at byte positions that do not fall
on codepoint boundaries will abort.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>span</b> (<a class="" href=/mojo/std/builtin/builtin_slice/ContiguousSlice><code>ContiguousSlice</code></a>): A slice that specifies byte positions of the new substring.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: A StringSlice containing the bytes in the specified range.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__lt__><code>__lt__</code><a href=#__lt__ class=hash-link aria-label="Direct link to __lt__" title="Direct link to __lt__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__lt__(self, rhs: Self) -> Bool</code></p>
</div>
<p>Compare this String to the RHS using LT comparison.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>rhs</b> (<code>Self</code>): The other String to compare against.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if this String is strictly less than the RHS String and False
otherwise.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__eq__><code>__eq__</code><a href=#__eq__ class=hash-link aria-label="Direct link to __eq__" title="Direct link to __eq__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__eq__(self, rhs: Self) -> Bool</code></p>
</div>
<p>Compares two Strings if they have the same values.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>rhs</b> (<code>Self</code>): The rhs of the operation.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if the Strings are equal and False otherwise.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__eq__(self, other: StringSlice[origin]) -> Bool</code></p>
</div>
<p>Compares two Strings if they have the same values.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>other</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The rhs of the operation.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if the Strings are equal and False otherwise.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__ne__><code>__ne__</code><a href=#__ne__ class=hash-link aria-label="Direct link to __ne__" title="Direct link to __ne__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__ne__(self, other: StringSlice[origin]) -> Bool</code></p>
</div>
<p>Compares two Strings if they have the same values.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>other</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The rhs of the operation.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if the Strings are equal and False otherwise.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__contains__><code>__contains__</code><a href=#__contains__ class=hash-link aria-label="Direct link to __contains__" title="Direct link to __contains__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__contains__(self, substr: StringSlice[origin]) -> Bool</code></p>
</div>
<p>Returns True if the substring is contained within the current string.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>substr</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The substring to check.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if the string contains the substring.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__add__><code>__add__</code><a href=#__add__ class=hash-link aria-label="Direct link to __add__" title="Direct link to __add__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__add__(self, other: StringSlice[origin]) -> Self</code></p>
</div>
<p>Creates a string by appending a string slice at the end.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>other</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The string slice to append.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: The new constructed string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__mul__><code>__mul__</code><a href=#__mul__ class=hash-link aria-label="Direct link to __mul__" title="Direct link to __mul__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__mul__(self, n: Int) -> Self</code></p>
</div>
<p>Concatenates the string <code>n</code> times.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>n</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The number of times to concatenate the string.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: The string concatenated <code>n</code> times.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__radd__><code>__radd__</code><a href=#__radd__ class=hash-link aria-label="Direct link to __radd__" title="Direct link to __radd__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__radd__(self, other: StringSlice[origin]) -> Self</code></p>
</div>
<p>Creates a string by prepending another string slice to the start.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>other</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The string to prepend.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: The new constructed string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__iadd__><code>__iadd__</code><a href=#__iadd__ class=hash-link aria-label="Direct link to __iadd__" title="Direct link to __iadd__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__iadd__(mut self, other: StringSlice[origin])</code></p>
</div>
<p>Appends another string slice to this string.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>other</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The string to append.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=write><code>write</code><a href=#write class=hash-link aria-label="Direct link to write" title="Direct link to write" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>static write[*Ts: Writable](*args: *Ts, *, sep: StringSlice[StaticConstantOrigin] = "", end: StringSlice[StaticConstantOrigin] = "") -> Self</code></p>
</div>
<p>Construct a string by concatenating a sequence of Writable arguments.</p>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>*Ts</b> (<a class="" href=/mojo/std/format/Writable><code>Writable</code></a>): Types of the provided argument sequence.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>*args</b> (<code>*Ts</code>): A sequence of Writable arguments.</li>
<li class="">â<b>sep</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The separator used between elements.</li>
<li class="">â<b>end</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The String to write after printing the elements.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: A string formed by formatting the argument sequence.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>write[*Ts: Writable](mut self, *args: *Ts)</code></p>
</div>
<p>Write a sequence of Writable arguments to the provided Writer.</p>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>*Ts</b> (<a class="" href=/mojo/std/format/Writable><code>Writable</code></a>): Types of the provided argument sequence.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>*args</b> (<code>*Ts</code>): Sequence of arguments to write to this Writer.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>write[T: Writable](mut self, value: T)</code></p>
</div>
<p>Write a single Writable argument to the provided Writer.</p>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>T</b> (<a class="" href=/mojo/std/format/Writable><code>Writable</code></a>): The type of the value to write, which must implement <code>Writable</code>.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>value</b> (<code>T</code>): The <code>Writable</code> argument to write.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>static write[T: Writable](value: T) -> Self</code></p>
</div>
<p>Write a single Writable argument to the provided Writer.</p>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>T</b> (<a class="" href=/mojo/std/format/Writable><code>Writable</code></a>): The type of the value to write, which must implement <code>Writable</code>.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>value</b> (<code>T</code>): The <code>Writable</code> argument to write.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: A new <code>String</code> containing the written value.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=capacity><code>capacity</code><a href=#capacity class=hash-link aria-label="Direct link to capacity" title="Direct link to capacity" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>capacity(self) -> Int</code></p>
</div>
<p>Get the current capacity of the <code>String</code>'s internal buffer.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>: The number of bytes that can be stored before reallocation is needed.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=write_string><code>write_string</code><a href=#write_string class=hash-link aria-label="Direct link to write_string" title="Direct link to write_string" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>write_string(mut self, string: StringSlice[origin])</code></p>
</div>
<p>Write a <code>StringSlice</code> to this <code>String</code>.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>string</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The <code>StringSlice</code> to write to this String.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=append_byte><code>append_byte</code><a href=#append_byte class=hash-link aria-label="Direct link to append_byte" title="Direct link to append_byte" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>append_byte(mut self, byte: UInt8)</code></p>
</div>
<p>Append a byte to the string.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>byte</b> (<a class="" href=/mojo/std/builtin/simd/#uint8><code>UInt8</code></a>): The byte to append.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=append><code>append</code><a href=#append class=hash-link aria-label="Direct link to append" title="Direct link to append" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>append(mut self, codepoint: Codepoint)</code></p>
</div>
<p>Append a codepoint to the string.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>codepoint</b> (<a class="" href=/mojo/std/collections/string/codepoint/Codepoint><code>Codepoint</code></a>): The codepoint to append.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__iter__><code>__iter__</code><a href=#__iter__ class=hash-link aria-label="Direct link to __iter__" title="Direct link to __iter__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__iter__(self) -> CodepointSliceIter[self]</code></p>
</div>
<p>Iterate over the string, returning immutable references.</p>
<p><strong>Returns:</strong></p>
<p><code>CodepointSliceIter</code>: An iterator of references to the string elements.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__reversed__><code>__reversed__</code><a href=#__reversed__ class=hash-link aria-label="Direct link to __reversed__" title="Direct link to __reversed__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__reversed__(self) -> CodepointSliceIter[self, False]</code></p>
</div>
<p>Iterate backwards over the string, returning immutable references.</p>
<p><strong>Returns:</strong></p>
<p><code>CodepointSliceIter</code>: A reversed iterator of references to the string elements.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__len__><code>__len__</code><a href=#__len__ class=hash-link aria-label="Direct link to __len__" title="Direct link to __len__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__len__(self) -> Int</code></p>
</div>
<p>Get the string length of in bytes.</p>
<p>This function returns the number of bytes in the underlying UTF-8
representation of the string.</p>
<p>To get the number of Unicode codepoints in a string, use
<code>len(str.codepoints())</code>.</p>
<p>Examples:</p>
<p>Query the length of a string, in bytes and Unicode codepoints:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>from testing import assert_equal

var s = "à²¨à²®à²¸à³à²à²¾à²°"

assert_equal(len(s), 21)
assert_equal(len(s.codepoints()), 7)</code></pre></div></div>
<p>Strings containing only ASCII characters have the same byte and
Unicode codepoint length:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>from testing import assert_equal

var s = "abc"

assert_equal(len(s), 3)
assert_equal(len(s.codepoints()), 3)</code></pre></div></div>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>: The string length in bytes.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__str__><code>__str__</code><a href=#__str__ class=hash-link aria-label="Direct link to __str__" title="Direct link to __str__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__str__(self) -> Self</code></p>
</div>
<p>Gets the string itself.</p>
<p>This method ensures that you can pass a <code>String</code> to a method that
takes a <code>Stringable</code> value.</p>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: The string itself.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__repr__><code>__repr__</code><a href=#__repr__ class=hash-link aria-label="Direct link to __repr__" title="Direct link to __repr__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__repr__(self) -> Self</code></p>
</div>
<p>Return a Mojo-compatible representation of the <code>String</code> instance.</p>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: A new representation of the string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__fspath__><code>__fspath__</code><a href=#__fspath__ class=hash-link aria-label="Direct link to __fspath__" title="Direct link to __fspath__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__fspath__(self) -> Self</code></p>
</div>
<p>Return the file system path representation (just the string itself).</p>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: The file system path representation as a string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=to_python_object><code>to_python_object</code><a href=#to_python_object class=hash-link aria-label="Direct link to to_python_object" title="Direct link to to_python_object" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>to_python_object(var self) -> PythonObject</code></p>
</div>
<p>Convert this value to a PythonObject.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/python/python_object/PythonObject><code>PythonObject</code></a>: A PythonObject representing the value.</p>
<p><strong>Raises:</strong></p>
<p>If the operation fails.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=write_to><code>write_to</code><a href=#write_to class=hash-link aria-label="Direct link to write_to" title="Direct link to write_to" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>write_to(self, mut writer: T)</code></p>
</div>
<p>Formats this string to the provided Writer.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>writer</b> (<code>T</code>): The object to write to.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=write_repr_to><code>write_repr_to</code><a href=#write_repr_to class=hash-link aria-label="Direct link to write_repr_to" title="Direct link to write_repr_to" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>write_repr_to(self, mut writer: T)</code></p>
</div>
<p>Formats this string slice to the provided <code>Writer</code>.</p>
<p>Notes:
Mojo's repr always prints single quotes (<code>'</code>) at the start and end
of the repr. Any single quote inside a string should be escaped
(<code>\'</code>).</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>writer</b> (<code>T</code>): The object to write to.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=join><code>join</code><a href=#join class=hash-link aria-label="Direct link to join" title="Direct link to join" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>join[T: Copyable & Writable](self, elems: Span[T, origin]) -> Self</code></p>
</div>
<p>Joins string elements using the current string as a delimiter. Defaults to writing to the stack if total bytes of <code>elems</code> is less than <code>buffer_size</code>, otherwise will allocate once to the heap and write directly into that. The <code>buffer_size</code> defaults to 4096 bytes to match the default page size on arm64 and x86-64.</p>
<p>Notes:</p>
<ul>
<li class="">Defaults to writing directly to the string if the bytes
fit in an inline <code>String</code>, otherwise will process it by chunks.</li>
<li class="">The <code>buffer_size</code> defaults to 4096 bytes to match the default
page size on arm64 and x86-64, but you can increase this if you're
joining a very large <code>List</code> of elements to write into the stack
instead of the heap.</li>
</ul>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>T</b> (<a class="" href=/mojo/std/builtin/value/Copyable><code>Copyable</code></a> & <a class="" href=/mojo/std/format/Writable><code>Writable</code></a>): The type of the elements. Must implement the <code>Copyable</code>,
and <code>Writable</code> traits.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>elems</b> (<a class="" href=/mojo/std/memory/span/Span><code>Span</code></a>): The input values.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: The joined string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=codepoints><code>codepoints</code><a href=#codepoints class=hash-link aria-label="Direct link to codepoints" title="Direct link to codepoints" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>codepoints(self) -> CodepointsIter[self]</code></p>
</div>
<p>Returns an iterator over the <code>Codepoint</code>s encoded in this string slice.</p>
<p>Examples:</p>
<p>Print the characters in a string:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>from testing import assert_equal, assert_raises

var s = "abc"
var iter = s.codepoints()
assert_equal(iter.__next__(), Codepoint.ord("a"))
assert_equal(iter.__next__(), Codepoint.ord("b"))
assert_equal(iter.__next__(), Codepoint.ord("c"))
with assert_raises():
    _ = iter.__next__() # raises StopIteration</code></pre></div></div>
<p><code>codepoints()</code> iterates over Unicode codepoints, and supports multibyte
codepoints:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>from testing import assert_equal, assert_raises

# A visual character composed of a combining sequence of 2 codepoints.
var s = "aÌ"
assert_equal(s.byte_length(), 3)

var iter = s.codepoints()
assert_equal(iter.__next__(), Codepoint.ord("a"))
 # U+0301 Combining Acute Accent
assert_equal(iter.__next__().to_u32(), 0x0301)
with assert_raises():
    _ = iter.__next__() # raises StopIteration</code></pre></div></div>
<p><strong>Returns:</strong></p>
<p><code>CodepointsIter</code>: An iterator type that returns successive <code>Codepoint</code> values stored in
this string slice.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=codepoint_slices><code>codepoint_slices</code><a href=#codepoint_slices class=hash-link aria-label="Direct link to codepoint_slices" title="Direct link to codepoint_slices" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>codepoint_slices(self) -> CodepointSliceIter[self]</code></p>
</div>
<p>Returns an iterator over single-character slices of this string.</p>
<p>Each returned slice points to a single Unicode codepoint encoded in the
underlying UTF-8 representation of this string.</p>
<p>Examples:</p>
<p>Iterate over the character slices in a string:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>from testing import assert_equal, assert_raises, assert_true

var s = "abc"
var iter = s.codepoint_slices()
assert_true(iter.__next__() == "a")
assert_true(iter.__next__() == "b")
assert_true(iter.__next__() == "c")
with assert_raises():
    _ = iter.__next__() # raises StopIteration</code></pre></div></div>
<p><strong>Returns:</strong></p>
<p><code>CodepointSliceIter</code>: An iterator of references to the string elements.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=codepoint_slices_reversed><code>codepoint_slices_reversed</code><a href=#codepoint_slices_reversed class=hash-link aria-label="Direct link to codepoint_slices_reversed" title="Direct link to codepoint_slices_reversed" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>codepoint_slices_reversed(self) -> CodepointSliceIter[self, False]</code></p>
</div>
<p>Iterates backwards over the string, returning single-character slices.</p>
<p>Each returned slice points to a single Unicode codepoint encoded in the
underlying UTF-8 representation of this string, starting from the end
and moving towards the beginning.</p>
<p><strong>Returns:</strong></p>
<p><code>CodepointSliceIter</code>: A reversed iterator of references to the string elements.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=unsafe_ptr><code>unsafe_ptr</code><a href=#unsafe_ptr class=hash-link aria-label="Direct link to unsafe_ptr" title="Direct link to unsafe_ptr" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>unsafe_ptr(self) -> UnsafePointer[Byte, self]</code></p>
</div>
<p>Retrieves a pointer to the underlying memory.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/memory/unsafe_pointer/UnsafePointer><code>UnsafePointer</code></a>: The pointer to the underlying memory.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=unsafe_ptr_mut><code>unsafe_ptr_mut</code><a href=#unsafe_ptr_mut class=hash-link aria-label="Direct link to unsafe_ptr_mut" title="Direct link to unsafe_ptr_mut" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>unsafe_ptr_mut(mut self, var capacity: Int = 0) -> UnsafePointer[Byte, self]</code></p>
</div>
<p>Retrieves a mutable pointer to the unique underlying memory. Passing a larger capacity will reallocate the string to the new capacity if larger than the existing capacity, allowing you to write more data.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>capacity</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The new capacity of the string.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/memory/unsafe_pointer/UnsafePointer><code>UnsafePointer</code></a>: The pointer to the underlying memory.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=as_c_string_slice><code>as_c_string_slice</code><a href=#as_c_string_slice class=hash-link aria-label="Direct link to as_c_string_slice" title="Direct link to as_c_string_slice" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>as_c_string_slice(mut self) -> CStringSlice[origin_of((muttoimm self))]</code></p>
</div>
<p>Return a <code>CStringSlice</code> to the underlying memory of the string.</p>
<p><strong>Returns:</strong></p>
<p><code>CStringSlice</code>: The <code>CStringSlice</code> of the string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=unsafe_cstr_ptr><code>unsafe_cstr_ptr</code><a href=#unsafe_cstr_ptr class=hash-link aria-label="Direct link to unsafe_cstr_ptr" title="Direct link to unsafe_cstr_ptr" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>unsafe_cstr_ptr(mut self) -> UnsafePointer[c_char, origin_of((muttoimm self))]</code></p>
</div>
<p>Retrieves a C-string-compatible pointer to the underlying memory.</p>
<p>The returned pointer is guaranteed to be null, or NUL terminated.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/memory/unsafe_pointer/UnsafePointer><code>UnsafePointer</code></a>: The pointer to the underlying memory.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=as_bytes><code>as_bytes</code><a href=#as_bytes class=hash-link aria-label="Direct link to as_bytes" title="Direct link to as_bytes" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>as_bytes(self) -> Span[Byte, self]</code></p>
</div>
<p>Returns a contiguous slice of the bytes owned by this string.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/memory/span/Span><code>Span</code></a>: A contiguous slice pointing to the bytes owned by this string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=as_bytes_mut><code>as_bytes_mut</code><a href=#as_bytes_mut class=hash-link aria-label="Direct link to as_bytes_mut" title="Direct link to as_bytes_mut" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>as_bytes_mut(mut self) -> Span[Byte, self]</code></p>
</div>
<p>Returns a mutable contiguous slice of the bytes owned by this string. This name has a _mut suffix so the as_bytes() method doesn't have to guarantee mutability.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/memory/span/Span><code>Span</code></a>: A contiguous slice pointing to the bytes owned by this string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=as_string_slice><code>as_string_slice</code><a href=#as_string_slice class=hash-link aria-label="Direct link to as_string_slice" title="Direct link to as_string_slice" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>as_string_slice(self) -> StringSlice[self]</code></p>
</div>
<p>Returns a string slice of the data owned by this string.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: A string slice pointing to the data owned by this string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=byte_length><code>byte_length</code><a href=#byte_length class=hash-link aria-label="Direct link to byte_length" title="Direct link to byte_length" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>byte_length(self) -> Int</code></p>
</div>
<p>Get the string length in bytes.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>: The length of this string in bytes.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=count_codepoints><code>count_codepoints</code><a href=#count_codepoints class=hash-link aria-label="Direct link to count_codepoints" title="Direct link to count_codepoints" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>count_codepoints(self) -> Int</code></p>
</div>
<p>Calculates the length in Unicode codepoints encoded in the UTF-8 representation of this string.</p>
<p>This is an O(n) operation, where n is the length of the string, as it
requires scanning the full string contents.</p>
<p>Examples:</p>
<p>Query the length of a string, in bytes and Unicode codepoints:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>
var s = StringSlice("à²¨à²®à²¸à³à²à²¾à²°")
assert_equal(s.count_codepoints(), 7)
assert_equal(s.byte_length(), 21)</code></pre></div></div>
<p>Strings containing only ASCII characters have the same byte and
Unicode codepoint length:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>
var s = StringSlice("abc")
assert_equal(s.count_codepoints(), 3)
assert_equal(s.byte_length(), 3)</code></pre></div></div>
<p>The character length of a string with visual combining characters is
the length in Unicode codepoints, not grapheme clusters:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>
var s = StringSlice("aÌ")
assert_equal(s.count_codepoints(), 2)
assert_equal(s.byte_length(), 3)</code></pre></div></div>
<p>Notes:
This method needs to traverse the whole string to count, so it has
a performance hit compared to using the byte length.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>: The length in Unicode codepoints.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=set_byte_length><code>set_byte_length</code><a href=#set_byte_length class=hash-link aria-label="Direct link to set_byte_length" title="Direct link to set_byte_length" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>set_byte_length(mut self, new_len: Int)</code></p>
</div>
<p>Set the byte length of the <code>String</code>.</p>
<p>This is an internal helper method that updates the length field.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>new_len</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The new byte length to set.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=count><code>count</code><a href=#count class=hash-link aria-label="Direct link to count" title="Direct link to count" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>count(self, substr: StringSlice[origin]) -> Int</code></p>
</div>
<p>Return the number of non-overlapping occurrences of substring <code>substr</code> in the string.</p>
<p>If sub is empty, returns the number of empty strings between characters
which is the length of the string plus one.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>substr</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The substring to count.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>: The number of occurrences of <code>substr</code>.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=find><code>find</code><a href=#find class=hash-link aria-label="Direct link to find" title="Direct link to find" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>find(self, substr: StringSlice[origin], start: Int = 0) -> Int</code></p>
</div>
<p>Finds the offset of the first occurrence of <code>substr</code> starting at <code>start</code>. If not found, returns -1.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>substr</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The substring to find.</li>
<li class="">â<b>start</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The offset from which to find.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>: The offset of <code>substr</code> relative to the beginning of the string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=rfind><code>rfind</code><a href=#rfind class=hash-link aria-label="Direct link to rfind" title="Direct link to rfind" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>rfind(self, substr: StringSlice[origin], start: Int = 0) -> Int</code></p>
</div>
<p>Finds the offset of the last occurrence of <code>substr</code> starting at <code>start</code>. If not found, returns -1.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>substr</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The substring to find.</li>
<li class="">â<b>start</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The offset from which to find.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>: The offset of <code>substr</code> relative to the beginning of the string.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=isspace><code>isspace</code><a href=#isspace class=hash-link aria-label="Direct link to isspace" title="Direct link to isspace" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>isspace(self) -> Bool</code></p>
</div>
<p>Determines whether every character in the given String is a python whitespace String. This corresponds to Python's <a href=https://docs.python.org/3/library/stdtypes.html#str.splitlines target=_blank rel="noopener noreferrer" class="">universal separators</a> <code>" \t\n\v\f\r\x1c\x1d\x1e\x85\u2028\u2029"</code>.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if the whole String is made up of whitespace characters
listed above, otherwise False.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=split><code>split</code><a href=#split class=hash-link aria-label="Direct link to split" title="Direct link to split" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>split(self, sep: StringSlice[origin]) -> List[StringSlice[self]]</code></p>
</div>
<p>Split the string by a separator.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code># Splitting a space
_ = StringSlice("hello world").split(" ") # ["hello", "world"]
# Splitting adjacent separators
_ = StringSlice("hello,,world").split(",") # ["hello", "", "world"]
# Splitting with starting or ending separators
_ = StringSlice(",1,2,3,").split(",") # ['', '1', '2', '3', '']
# Splitting with an empty separator
_ = StringSlice("123").split("") # ['', '1', '2', '3', '']</code></pre></div></div>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>sep</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The string to split on.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/list/List><code>List</code></a>: A List of Strings containing the input split by the separator.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>split(self, sep: StringSlice[origin], maxsplit: Int) -> List[StringSlice[self]]</code></p>
</div>
<p>Split the string by a separator.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code># Splitting with maxsplit
_ = StringSlice("1,2,3").split(",", maxsplit=1) # ['1', '2,3']
# Splitting with starting or ending separators
_ = StringSlice(",1,2,3,").split(",", maxsplit=1) # ['', '1,2,3,']
# Splitting with an empty separator
_ = StringSlice("123").split("", maxsplit=1) # ['', '123']</code></pre></div></div>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>sep</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The string to split on.</li>
<li class="">â<b>maxsplit</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The maximum amount of items to split from String.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/list/List><code>List</code></a>: A List of Strings containing the input split by the separator.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>split(self, sep: NoneType = None) -> List[StringSlice[self]]</code></p>
</div>
<p>Split the string by every Whitespace separator.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code># Splitting an empty string or filled with whitespaces
_ = StringSlice("      ").split() # []
_ = StringSlice("").split() # []

# Splitting a string with leading, trailing, and middle whitespaces
_ = StringSlice("      hello    world     ").split() # ["hello", "world"]
# Splitting adjacent universal newlines:
_ = StringSlice(
    "hello \t\n\v\f\r\x1c\x1d\x1e\x85\u2028\u2029world"
).split()  # ["hello", "world"]</code></pre></div></div>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>sep</b> (<a class="" href=/mojo/std/builtin/none/NoneType><code>NoneType</code></a>): None.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/list/List><code>List</code></a>: A List of Strings containing the input split by the separator.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>split(self, sep: NoneType = None, *, maxsplit: Int) -> List[StringSlice[self]]</code></p>
</div>
<p>Split the string by every Whitespace separator.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code># Splitting with maxsplit
_ = StringSlice("1     2  3").split(maxsplit=1) # ['1', '2  3']</code></pre></div></div>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>sep</b> (<a class="" href=/mojo/std/builtin/none/NoneType><code>NoneType</code></a>): None.</li>
<li class="">â<b>maxsplit</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The maximum amount of items to split from String.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/list/List><code>List</code></a>: A List of Strings containing the input split by the separator.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=splitlines><code>splitlines</code><a href=#splitlines class=hash-link aria-label="Direct link to splitlines" title="Direct link to splitlines" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>splitlines(self, keepends: Bool = False) -> List[StringSlice[self]]</code></p>
</div>
<p>Split the string at line boundaries. This corresponds to Python's <a href=https://docs.python.org/3/library/stdtypes.html#str.splitlines target=_blank rel="noopener noreferrer" class="">universal newlines:</a> <code>"\r\n"</code> and <code>"\t\n\v\f\r\x1c\x1d\x1e\x85\u2028\u2029"</code>.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>keepends</b> (<a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>): If True, line breaks are kept in the resulting strings.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/list/List><code>List</code></a>: A List of Strings containing the input split by line boundaries.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=replace><code>replace</code><a href=#replace class=hash-link aria-label="Direct link to replace" title="Direct link to replace" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>replace(self, old: StringSlice[origin], new: StringSlice[origin]) -> Self</code></p>
</div>
<p>Return a copy of the string with all occurrences of substring <code>old</code> if replaced by <code>new</code>.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>old</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The substring to replace.</li>
<li class="">â<b>new</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The substring to replace with.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: The string where all occurrences of <code>old</code> are replaced with <code>new</code>.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=strip><code>strip</code><a href=#strip class=hash-link aria-label="Direct link to strip" title="Direct link to strip" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>strip(self, chars: StringSlice[origin]) -> StringSlice[self]</code></p>
</div>
<p>Return a copy of the string with leading and trailing characters removed.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>chars</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): A set of characters to be removed. Defaults to whitespace.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: A copy of the string with no leading or trailing characters.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>strip(self) -> StringSlice[self]</code></p>
</div>
<p>Return a copy of the string with leading and trailing whitespaces removed. This only takes ASCII whitespace into account: <code>" \t\n\v\f\r\x1c\x1d\x1e"</code>.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: A copy of the string with no leading or trailing whitespaces.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=rstrip><code>rstrip</code><a href=#rstrip class=hash-link aria-label="Direct link to rstrip" title="Direct link to rstrip" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>rstrip(self, chars: StringSlice[origin]) -> StringSlice[self]</code></p>
</div>
<p>Return a copy of the string with trailing characters removed.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>chars</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): A set of characters to be removed. Defaults to whitespace.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: A copy of the string with no trailing characters.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>rstrip(self) -> StringSlice[self]</code></p>
</div>
<p>Return a copy of the string with trailing whitespaces removed. This only takes ASCII whitespace into account: <code>" \t\n\v\f\r\x1c\x1d\x1e"</code>.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: A copy of the string with no trailing whitespaces.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=lstrip><code>lstrip</code><a href=#lstrip class=hash-link aria-label="Direct link to lstrip" title="Direct link to lstrip" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>lstrip(self, chars: StringSlice[origin]) -> StringSlice[self]</code></p>
</div>
<p>Return a copy of the string with leading characters removed.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>chars</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): A set of characters to be removed. Defaults to whitespace.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: A copy of the string with no leading characters.</p>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>lstrip(self) -> StringSlice[self]</code></p>
</div>
<p>Return a copy of the string with leading whitespaces removed. This only takes ASCII whitespace into account: <code>" \t\n\v\f\r\x1c\x1d\x1e"</code>.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: A copy of the string with no leading whitespaces.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__hash__><code>__hash__</code><a href=#__hash__ class=hash-link aria-label="Direct link to __hash__" title="Direct link to __hash__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__hash__[H: Hasher](self, mut hasher: H)</code></p>
</div>
<p>Updates hasher with the underlying bytes.</p>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>H</b> (<a class="" href=/mojo/std/hashlib/hasher/Hasher><code>Hasher</code></a>): The hasher type.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>hasher</b> (<code>H</code>): The hasher instance.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=lower><code>lower</code><a href=#lower class=hash-link aria-label="Direct link to lower" title="Direct link to lower" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>lower(self) -> Self</code></p>
</div>
<p>Returns a copy of the string with all cased characters converted to lowercase.</p>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: A new string where cased letters have been converted to lowercase.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=upper><code>upper</code><a href=#upper class=hash-link aria-label="Direct link to upper" title="Direct link to upper" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>upper(self) -> Self</code></p>
</div>
<p>Returns a copy of the string with all cased characters converted to uppercase.</p>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: A new string where cased letters have been converted to uppercase.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=startswith><code>startswith</code><a href=#startswith class=hash-link aria-label="Direct link to startswith" title="Direct link to startswith" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>startswith(self, prefix: StringSlice[origin], start: Int = 0, end: Int = -1) -> Bool</code></p>
</div>
<p>Checks if the string starts with the specified prefix between start and end positions. Returns True if found and False otherwise.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>prefix</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The prefix to check.</li>
<li class="">â<b>start</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The start offset from which to check.</li>
<li class="">â<b>end</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The end offset from which to check.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if the <code>self[start:end]</code> is prefixed by the input prefix.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=endswith><code>endswith</code><a href=#endswith class=hash-link aria-label="Direct link to endswith" title="Direct link to endswith" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>endswith(self, suffix: StringSlice[origin], start: Int = 0, end: Int = -1) -> Bool</code></p>
</div>
<p>Checks if the string end with the specified suffix between start and end positions. Returns True if found and False otherwise.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>suffix</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The suffix to check.</li>
<li class="">â<b>start</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The start offset from which to check.</li>
<li class="">â<b>end</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The end offset from which to check.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if the <code>self[start:end]</code> is suffixed by the input suffix.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=removeprefix><code>removeprefix</code><a href=#removeprefix class=hash-link aria-label="Direct link to removeprefix" title="Direct link to removeprefix" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>removeprefix(self, prefix: StringSlice[origin], /) -> StringSlice[self]</code></p>
</div>
<p>Returns a new string with the prefix removed if it was present.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>print(String('TestHook').removeprefix('Test')) # 'Hook'
print(String('BaseTestCase').removeprefix('Test')) # 'BaseTestCase'</code></pre></div></div>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>prefix</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The prefix to remove from the string.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: <code>string[len(prefix):]</code> if the string starts with the prefix string,
or a copy of the original string otherwise.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=removesuffix><code>removesuffix</code><a href=#removesuffix class=hash-link aria-label="Direct link to removesuffix" title="Direct link to removesuffix" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>removesuffix(self, suffix: StringSlice[origin], /) -> StringSlice[self]</code></p>
</div>
<p>Returns a new string with the suffix removed if it was present.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>print(String('TestHook').removesuffix('Hook')) # 'Test'
print(String('BaseTestCase').removesuffix('Test')) # 'BaseTestCase'</code></pre></div></div>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>suffix</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The suffix to remove from the string.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>: <code>string[:-len(suffix)]</code> if the string ends with the suffix string,
or a copy of the original string otherwise.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__int__><code>__int__</code><a href=#__int__ class=hash-link aria-label="Direct link to __int__" title="Direct link to __int__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__int__(self) -> Int</code></p>
</div>
<p>Parses the given string as a base-10 integer and returns that value. If the string cannot be parsed as an int, an error is raised.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>: An integer value that represents the string, or otherwise raises.</p>
<p><strong>Raises:</strong></p>
<p>If the operation fails.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=__float__><code>__float__</code><a href=#__float__ class=hash-link aria-label="Direct link to __float__" title="Direct link to __float__" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>__float__(self) -> Float64</code></p>
</div>
<p>Parses the string as a float point number and returns that value. If the string cannot be parsed as a float, an error is raised.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/simd/#float64><code>Float64</code></a>: A float value that represents the string, or otherwise raises.</p>
<p><strong>Raises:</strong></p>
<p>If the operation fails.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=format><code>format</code><a href=#format class=hash-link aria-label="Direct link to format" title="Direct link to format" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>format[*Ts: Writable](self, *args: *Ts) -> Self</code></p>
</div>
<p>Produce a formatted string using the current string as a template.</p>
<p>The template, or "format string" can contain literal text and/or
replacement fields delimited with curly braces (<code>{}</code>). Returns a copy of
the format string with the replacement fields replaced with string
representations of the <code>args</code> arguments.</p>
<p>For more information, see the discussion in the
<a class="" href=/mojo/std/collections/string/format/><code>format</code> module</a>.</p>
<p>Example:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code># Manual indexing:
print("{0} {1} {0}".format("Mojo", 1.125)) # Mojo 1.125 Mojo
# Automatic indexing:
print("{} {}".format(True, "hello world")) # True hello world</code></pre></div></div>
<p><strong>Parameters:</strong></p>
<ul>
<li class="">â<b>*Ts</b> (<a class="" href=/mojo/std/format/Writable><code>Writable</code></a>): The types of substitution values that implement <code>Writable</code>.</li>
</ul>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>*args</b> (<code>*Ts</code>): The substitution values.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: The template with the given values substituted.</p>
<p><strong>Raises:</strong></p>
<p>If the operation fails.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=is_ascii_digit><code>is_ascii_digit</code><a href=#is_ascii_digit class=hash-link aria-label="Direct link to is_ascii_digit" title="Direct link to is_ascii_digit" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>is_ascii_digit(self) -> Bool</code></p>
</div>
<p>A string is a digit string if all characters in the string are ASCII digits and there is at least one character in the string.</p>
<p>Note that this currently only works with ASCII strings.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if all characters are digits and it's not empty else False.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=isupper><code>isupper</code><a href=#isupper class=hash-link aria-label="Direct link to isupper" title="Direct link to isupper" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>isupper(self) -> Bool</code></p>
</div>
<p>Returns True if all cased characters in the string are uppercase and there is at least one cased character.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if all cased characters in the string are uppercase and there
is at least one cased character, False otherwise.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=islower><code>islower</code><a href=#islower class=hash-link aria-label="Direct link to islower" title="Direct link to islower" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>islower(self) -> Bool</code></p>
</div>
<p>Returns True if all cased characters in the string are lowercase and there is at least one cased character.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if all cased characters in the string are lowercase and there
is at least one cased character, False otherwise.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=is_ascii_printable><code>is_ascii_printable</code><a href=#is_ascii_printable class=hash-link aria-label="Direct link to is_ascii_printable" title="Direct link to is_ascii_printable" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>is_ascii_printable(self) -> Bool</code></p>
</div>
<p>Returns True if all characters in the string are ASCII printable.</p>
<p>Note that this currently only works with ASCII strings.</p>
<p><strong>Returns:</strong></p>
<p><a class="" href=/mojo/std/builtin/bool/Bool><code>Bool</code></a>: True if all characters are printable else False.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=ascii_rjust><code>ascii_rjust</code><a href=#ascii_rjust class=hash-link aria-label="Direct link to ascii_rjust" title="Direct link to ascii_rjust" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>ascii_rjust(self, width: Int, fillchar: StringSlice[StaticConstantOrigin] = " ") -> Self</code></p>
</div>
<p>Returns the string right justified in a string of specified width.</p>
<p>Pads the string on the left with the specified fill character so that
the total (byte) length of the resulting string equals <code>width</code>. If the original
string is already longer than or equal to <code>width</code>, returns the original
string unchanged.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>var s = String("hello")
print(s.ascii_rjust(10))        # "     hello"
print(s.ascii_rjust(10, "*"))   # "*****hello"
print(s.ascii_rjust(3))         # "hello" (no padding)</code></pre></div></div>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>width</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The total width (in bytes) of the resulting string. This is
not the amount of padding, but the final length of the returned
string.</li>
<li class="">â<b>fillchar</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The padding character to use (defaults to space). Must be
a single-byte character.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: A right-justified string of (byte) length <code>width</code>, or the original string
if its length is already greater than or equal to <code>width</code>.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=ascii_ljust><code>ascii_ljust</code><a href=#ascii_ljust class=hash-link aria-label="Direct link to ascii_ljust" title="Direct link to ascii_ljust" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>ascii_ljust(self, width: Int, fillchar: StringSlice[StaticConstantOrigin] = " ") -> Self</code></p>
</div>
<p>Returns the string left justified in a string of specified width.</p>
<p>Pads the string on the right with the specified fill character so that
the total (byte) length of the resulting string equals <code>width</code>. If the original
string is already longer than or equal to <code>width</code>, returns the original
string unchanged.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>var s = String("hello")
print(s.ascii_ljust(10))        # "hello     "
print(s.ascii_ljust(10, "*"))   # "hello*****"
print(s.ascii_ljust(3))         # "hello" (no padding)</code></pre></div></div>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>width</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The total width (in bytes) of the resulting string. This is
not the amount of padding, but the final length of the returned
string.</li>
<li class="">â<b>fillchar</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The padding character to use (defaults to space). Must be
a single-byte character.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: A left-justified string of (byte) length <code>width</code>, or the original string
if its length is already greater than or equal to <code>width</code>.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=ascii_center><code>ascii_center</code><a href=#ascii_center class=hash-link aria-label="Direct link to ascii_center" title="Direct link to ascii_center" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>ascii_center(self, width: Int, fillchar: StringSlice[StaticConstantOrigin] = " ") -> Self</code></p>
</div>
<p>Returns the string center justified in a string of specified width.</p>
<p>Pads the string on both sides with the specified fill character so that
the total length of the resulting string equals <code>width</code>. If the padding
needed is odd, the extra character goes on the right side. If the
original string is already longer than or equal to <code>width</code>, returns the
original string unchanged.</p>
<p>Examples:</p>
<div class="language-mojo codeBlockContainer_Ckt0 theme-code-block" style="--prism-background-color:rgb(238, 240, 244);--prism-color:rgb(38, 44, 48)"><div class=codeBlockContent_QJqH><pre class=codeBlockBg><code>var s = String("hello")
print(s.center(10))        # "  hello   "
print(s.center(11, "*"))   # "***hello***"
print(s.center(3))         # "hello" (no padding)</code></pre></div></div>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>width</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The total width (in bytes) of the resulting string. This is
not the amount of padding, but the final length of the returned
string.</li>
<li class="">â<b>fillchar</b> (<a class="" href=/mojo/std/collections/string/string_slice/StringSlice><code>StringSlice</code></a>): The padding character to use (defaults to space). Must be
a single-byte character.</li>
</ul>
<p><strong>Returns:</strong></p>
<p><code>Self</code>: A center-justified string of length <code>width</code>, or the original string
if its length is already greater than or equal to <code>width</code>.</p>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=resize><code>resize</code><a href=#resize class=hash-link aria-label="Direct link to resize" title="Direct link to resize" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>resize(mut self, length: Int, fill_byte: UInt8 = 0)</code></p>
</div>
<p>Resize the string to a new length. Panics if new_len does not lie on a codepoint boundary or if fill_byte is non-ascii (>=128).</p>
<p>Notes:
If the new length is greater than the current length, the string is
extended by the difference, and the new bytes are initialized to
<code>fill_byte</code>.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>length</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The new length of the string.</li>
<li class="">â<b>fill_byte</b> (<a class="" href=/mojo/std/builtin/simd/#uint8><code>UInt8</code></a>): The byte to fill any new space with. Must be a valid single-byte
utf-8 character.</li>
</ul>
</div>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>resize(mut self, *, unsafe_uninit_length: Int)</code></p>
</div>
<p>Resizes the string to the given new size leaving any new data uninitialized. Panics if the new length does not lie on a codepoint boundary.</p>
<p>If the new size is smaller than the current one, elements at the end
are discarded. If the new size is larger than the current one, the
string is extended and the new data is left uninitialized.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>unsafe_uninit_length</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The new size.</li>
</ul>
</div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id=reserve><code>reserve</code><a href=#reserve class=hash-link aria-label="Direct link to reserve" title="Direct link to reserve" translate=no>â</a></h3>
<div class=mojo-function-detail>
<div class=mojo-function-sig>
<p><code>reserve(mut self, new_capacity: Int)</code></p>
</div>
<p>Reserves the requested capacity.</p>
<p>Notes:
If the current capacity is greater or equal, this is a no-op.
Otherwise, the storage is reallocated and the data is moved.</p>
<p><strong>Args:</strong></p>
<ul>
<li class="">â<b>new_capacity</b> (<a class="" href=/mojo/std/builtin/int/Int><code>Int</code></a>): The new capacity in stored bytes.</li>
</ul>
</div>
</section><div class="hidden docs-desktop:block w-full docs-desktop:mt-11"><div style=--group-gap:0rem;--group-align:center;--group-justify:flex-start;--group-wrap:wrap class="relative transition-all duration-200 w-full justify-end docs-desktop:justify-center m_4081bf90 mantine-Group-root"><p style="color:var(--Elements-Twilight-70-20);font-size:calc(1rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto mr-1 !text-sm docs-desktop:mr-3 docs-desktop:!text-base m_b6d8b162 mantine-Text-root">Was this page helpful?</p><button style="--ai-bg:transparent;--ai-hover:color-mix(in srgb, var(--Elements-Twilight-60-50), transparent 88%);--ai-color:var(--Elements-Twilight-60-50);--ai-bd:calc(0.0625rem * var(--mantine-scale)) solid transparent" class="mantine-focus-auto mantine-active w-8 docs-desktop:w-[42px] m_8d3f4000 mantine-ActionIcon-root m_87cf2631 mantine-UnstyledButton-root" data-variant=subtle type=button><span class="m_8d3afb97 mantine-ActionIcon-icon"><svg viewBox="0 0 20 18" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(1.25rem * var(--mantine-scale));height:calc(1.25rem * var(--mantine-scale))"><path d="M5 8.58v7.92M16.25 16.5H1.67V8.58H5L7.08 1.5h.75a3 3 0 0 1 3 3v2h7.5l-2.08 10Z" stroke=currentColor stroke-width=1.5 /></svg></span></button><button style="--ai-bg:transparent;--ai-hover:color-mix(in srgb, var(--Elements-Twilight-60-50), transparent 88%);--ai-color:var(--Elements-Twilight-60-50);--ai-bd:calc(0.0625rem * var(--mantine-scale)) solid transparent" class="mantine-focus-auto mantine-active w-8 docs-desktop:w-[42px] m_8d3f4000 mantine-ActionIcon-root m_87cf2631 mantine-UnstyledButton-root" data-variant=subtle type=button><span class="m_8d3afb97 mantine-ActionIcon-icon"><svg viewBox="0 0 20 18" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(1.25rem * var(--mantine-scale));height:calc(1.25rem * var(--mantine-scale))" class=rotate-180><path d="M5 8.58v7.92M16.25 16.5H1.67V8.58H5L7.08 1.5h.75a3 3 0 0 1 3 3v2h7.5l-2.08 10Z" stroke=currentColor stroke-width=1.5 /></svg></span></button></div><p style="color:var(--Elements-Twilight-70-20);font-size:calc(1rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto h-0 docs-desktop:translate-y-4 scale-y-0 opacity-0 relative m-auto transition-all duration-200 text-center !text-sm docs-desktop:!text-base m_b6d8b162 mantine-Text-root">Thank you! We'll create more content like this.<p style="color:var(--Elements-Twilight-70-20);font-size:calc(1rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto h-0 docs-desktop:translate-y-4 scale-y-0 opacity-0 relative m-auto transition-all duration-200 text-center !text-sm docs-desktop:!text-base m_b6d8b162 mantine-Text-root">Thank you for helping us improve!<div style=--stack-gap:0rem;--stack-align:center;--stack-justify:flex-start;margin-top:var(--mantine-spacing-md) class="m_6d731127 mantine-Stack-root"><div style=--stack-gap:var(--mantine-spacing-md);--stack-align:stretch;--stack-justify:flex-start class="h-0 docs-desktop:translate-y-4 scale-y-0 opacity-0 m-auto w-60 relative m-auto transition-all duration-200 hidden docs-desktop:flex m_6d731127 mantine-Stack-root"><p style="font-size:calc(1.5rem * var(--mantine-scale));font-weight:400;line-height:calc(2rem * var(--mantine-scale))" class="mantine-focus-auto m_b6d8b162 mantine-Text-root">ð What went wrong?<div class="m_46b77525 mantine-InputWrapper-root mantine-RadioGroup-root"><div role=radiogroup aria-labelledby=mantine-R3ar5rcmlalleh-label><div style=--stack-gap:var(--mantine-spacing-md);--stack-align:stretch;--stack-justify:flex-start;margin-top:var(--mantine-spacing-xs) class="m_6d731127 mantine-Stack-root"><div style=--radio-icon-color:var(--White);--radio-color:var(--Elements-Neb-Ultra-Super) class="m_f3f1af94 mantine-Radio-root m_5f75b09e mantine-Radio-root" data-label-position=right><div class="m_5f6e695e mantine-Radio-body"><div class="m_89c4f5e4 mantine-Radio-inner" data-label-position=right><input class="mantine-focus-auto border-Elements-Twilight-60-50 m_8a3dbb89 mantine-Radio-radio" name=mantine-R1ar5rcmlalleh id=mantine-Rmnfar5rcmlalleh type=radio value=broken_code /><svg xmlns=http://www.w3.org/2000/svg fill=none viewBox="0 0 5 5" aria-hidden=true class="m_f3ed6b2b mantine-Radio-icon"><circle cx=2.5 cy=2.5 r=2.5 fill=currentColor /></svg></div><div class="m_d3ea56bb mantine-Radio-labelWrapper"><label class="m_8ee546b8 mantine-Radio-label" for=mantine-Rmnfar5rcmlalleh>Some code doesnât work</label></div></div></div><div style=--radio-icon-color:var(--White);--radio-color:var(--Elements-Neb-Ultra-Super) class="m_f3f1af94 mantine-Radio-root m_5f75b09e mantine-Radio-root" data-label-position=right><div class="m_5f6e695e mantine-Radio-body"><div class="m_89c4f5e4 mantine-Radio-inner" data-label-position=right><input class="mantine-focus-auto border-Elements-Twilight-60-50 m_8a3dbb89 mantine-Radio-radio" name=mantine-R1ar5rcmlalleh id=mantine-R16nfar5rcmlalleh type=radio value=factual_error /><svg xmlns=http://www.w3.org/2000/svg fill=none viewBox="0 0 5 5" aria-hidden=true class="m_f3ed6b2b mantine-Radio-icon"><circle cx=2.5 cy=2.5 r=2.5 fill=currentColor /></svg></div><div class="m_d3ea56bb mantine-Radio-labelWrapper"><label class="m_8ee546b8 mantine-Radio-label" for=mantine-R16nfar5rcmlalleh>It includes inaccurate information</label></div></div></div><div style=--radio-icon-color:var(--White);--radio-color:var(--Elements-Neb-Ultra-Super) class="m_f3f1af94 mantine-Radio-root m_5f75b09e mantine-Radio-root" data-label-position=right><div class="m_5f6e695e mantine-Radio-body"><div class="m_89c4f5e4 mantine-Radio-inner" data-label-position=right><input class="mantine-focus-auto border-Elements-Twilight-60-50 m_8a3dbb89 mantine-Radio-radio" name=mantine-R1ar5rcmlalleh id=mantine-R1mnfar5rcmlalleh type=radio value=missing_info /><svg xmlns=http://www.w3.org/2000/svg fill=none viewBox="0 0 5 5" aria-hidden=true class="m_f3ed6b2b mantine-Radio-icon"><circle cx=2.5 cy=2.5 r=2.5 fill=currentColor /></svg></div><div class="m_d3ea56bb mantine-Radio-labelWrapper"><label class="m_8ee546b8 mantine-Radio-label" for=mantine-R1mnfar5rcmlalleh>It's missing information I need</label></div></div></div><div style=--radio-icon-color:var(--White);--radio-color:var(--Elements-Neb-Ultra-Super) class="m_f3f1af94 mantine-Radio-root m_5f75b09e mantine-Radio-root" data-label-position=right><div class="m_5f6e695e mantine-Radio-body"><div class="m_89c4f5e4 mantine-Radio-inner" data-label-position=right><input class="mantine-focus-auto border-Elements-Twilight-60-50 m_8a3dbb89 mantine-Radio-radio" name=mantine-R1ar5rcmlalleh id=mantine-R26nfar5rcmlalleh type=radio value=confusing /><svg xmlns=http://www.w3.org/2000/svg fill=none viewBox="0 0 5 5" aria-hidden=true class="m_f3ed6b2b mantine-Radio-icon"><circle cx=2.5 cy=2.5 r=2.5 fill=currentColor /></svg></div><div class="m_d3ea56bb mantine-Radio-labelWrapper"><label class="m_8ee546b8 mantine-Radio-label" for=mantine-R26nfar5rcmlalleh>It was difficult to understand</label></div></div></div><div style=--radio-icon-color:var(--White);--radio-color:var(--Elements-Neb-Ultra-Super) class="m_f3f1af94 mantine-Radio-root m_5f75b09e mantine-Radio-root" data-label-position=right><div class="m_5f6e695e mantine-Radio-body"><div class="m_89c4f5e4 mantine-Radio-inner" data-label-position=right><input class="mantine-focus-auto border-Elements-Twilight-60-50 m_8a3dbb89 mantine-Radio-radio" name=mantine-R1ar5rcmlalleh id=mantine-R2mnfar5rcmlalleh type=radio value=other /><svg xmlns=http://www.w3.org/2000/svg fill=none viewBox="0 0 5 5" aria-hidden=true class="m_f3ed6b2b mantine-Radio-icon"><circle cx=2.5 cy=2.5 r=2.5 fill=currentColor /></svg></div><div class="m_d3ea56bb mantine-Radio-labelWrapper"><label class="m_8ee546b8 mantine-Radio-label" for=mantine-R2mnfar5rcmlalleh>Other</label></div></div></div><div style=--stack-gap:0rem;--stack-align:stretch;--stack-justify:flex-start class="m_6d731127 mantine-Stack-root"><a href="https://github.com/modular/modular/issues/new?assignees=&labels=documentation%2Cmodular-repo%2Cmojo&projects=&template=doc_issue.yaml&title=%5BDocs%5D&url=https://docs.modular.com/mojo/std/collections/string/string/String" target=_blank rel="noopener noreferrer" style="opacity:0.4;background:var(--Elements-Neb-100-Twilight-60);color:var(--Black);--button-height:calc(1.75rem * var(--mantine-scale));--button-padding-x:calc(0.875rem * var(--mantine-scale));--button-fz:calc(0.75rem * var(--mantine-scale));--button-color:var(--Elements-Twilight-100);--button-bg:var(--Elements-Neb-90-Ultra);--button-hover:var(--Elements-Neb-Ultra-Super);font-weight:400" class="mantine-focus-auto onActive_LK5j onHover_fkhK no-transition !font-normal m_77c9d27d mantine-Button-root m_87cf2631 mantine-UnstyledButton-root" data-size=xs data-disabled=true disabled=""><span class="m_80f1301b mantine-Button-inner"><span class="m_811560b9 mantine-Button-label">Submit</span></span></a></div></div></div></div></div></div></div></div></article></div></div><div class="col col--3 !mx-0"><div class="rightRail_g3t8 thin-scrollbar"><style data-mantine-styles=inline>.__m__-R36lalleh{flex-direction:row}@media (width>=997px){.__m__-R36lalleh{flex-direction:column}}</style><div class="hidden flex-col gap-4 pb-4 pt-1 docs-desktop:flex text-sm lg:text-base docs-desktop:mt-2 m_8bffd616 mantine-Flex-root __m__-R36lalleh"><div class=mantine-hidden-from-docs-desktop><a href=https://github.com/modular/modular/tree/main/mojo/stdlib/std/collections/string/string.mojo target=_blank rel="noopener noreferrer" style="--button-bg:transparent;--button-hover:var(--Elements-Twilight-5-80);--button-color:var(--Elements-Twilight-60-50);--button-bd:calc(0.0625rem * var(--mantine-scale)) solid transparent;--button-height:calc(2.5rem * var(--mantine-scale));--button-padding-x:calc(1.375rem * var(--mantine-scale));--button-fz:calc(1rem * var(--mantine-scale));font-weight:400" class="mantine-focus-auto mantine-active onActive_LK5j onHover_fkhK no-transition !font-normal group my-auto px-4 hover:bg-Elements-Twilight-5-80 hover:no-underline m_77c9d27d mantine-Button-root m_87cf2631 mantine-UnstyledButton-root" data-variant=subtle><span class="m_80f1301b mantine-Button-inner"><span class="m_811560b9 mantine-Button-label"><div style="--group-gap:calc(0.5rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:wrap" class="text-Elements-Twilight-60-40 m_4081bf90 mantine-Group-root"><svg viewBox="0 0 12 12" xmlns=http://www.w3.org/2000/svg style="width:calc(0.875rem * var(--mantine-scale));height:calc(0.875rem * var(--mantine-scale))" class=group-hover:text-black fill=currentColor><g clip-path=url(#:Rrdbbbb6lalleh:)><path fill-rule=evenodd clip-rule=evenodd d="M6 .8c2.9 0 5.2 2.4 5.2 5.3 0 2.4-1.5 4.4-3.6 5-.2.1-.3 0-.3-.2V9.5c0-.5-.2-.9-.4-1 1.2-.1 2.4-.6 2.4-2.6 0-.6-.2-1.1-.5-1.5 0-.1.2-.7 0-1.4 0 0-.5-.1-1.5.6a4.9 4.9 0 0 0-2.6 0c-1-.7-1.4-.6-1.4-.6a2 2 0 0 0 0 1.4A2 2 0 0 0 2.6 6c0 2 1.2 2.5 2.4 2.6-.2.1-.3.4-.4.7-.3.1-1 .4-1.5-.4 0 0-.3-.6-.8-.6 0 0-.5 0 0 .3 0 0 .3.2.6.8 0 0 .3 1 1.7.6v1c0 .2 0 .3-.3.3-2.1-.7-3.6-2.7-3.6-5C.8 3.1 3.1.7 6 .7Z"/></g><defs><clipPath id=:Rrdbbbb6lalleh:><path fill=var(--White) transform="translate(.8 .8)" d="M0 0h10.4v10.4H0z"/></clipPath></defs></svg><p style="font-size:calc(0.875rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto group-hover:text-black m_b6d8b162 mantine-Text-root">View source</div></span></span></a></div><a href=https://github.com/modular/modular/tree/main/mojo/stdlib/std/collections/string/string.mojo target=_blank rel="noopener noreferrer" class="mantine-focus-auto my-auto hover:no-underline docs-desktop:-mt-2 m_87cf2631 mantine-UnstyledButton-root mantine-visible-from-docs-desktop"><div style="--group-gap:calc(0.5rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:wrap" class="group text-Elements-Twilight-60-40 hover:text-black m_4081bf90 mantine-Group-root"><svg viewBox="0 0 12 12" xmlns=http://www.w3.org/2000/svg style="width:calc(0.875rem * var(--mantine-scale));height:calc(0.875rem * var(--mantine-scale))" fill=currentColor><g clip-path=url(#:Rrdbb6lalleh:)><path fill-rule=evenodd clip-rule=evenodd d="M6 .8c2.9 0 5.2 2.4 5.2 5.3 0 2.4-1.5 4.4-3.6 5-.2.1-.3 0-.3-.2V9.5c0-.5-.2-.9-.4-1 1.2-.1 2.4-.6 2.4-2.6 0-.6-.2-1.1-.5-1.5 0-.1.2-.7 0-1.4 0 0-.5-.1-1.5.6a4.9 4.9 0 0 0-2.6 0c-1-.7-1.4-.6-1.4-.6a2 2 0 0 0 0 1.4A2 2 0 0 0 2.6 6c0 2 1.2 2.5 2.4 2.6-.2.1-.3.4-.4.7-.3.1-1 .4-1.5-.4 0 0-.3-.6-.8-.6 0 0-.5 0 0 .3 0 0 .3.2.6.8 0 0 .3 1 1.7.6v1c0 .2 0 .3-.3.3-2.1-.7-3.6-2.7-3.6-5C.8 3.1 3.1.7 6 .7Z"/></g><defs><clipPath id=:Rrdbb6lalleh:><path fill=var(--White) transform="translate(.8 .8)" d="M0 0h10.4v10.4H0z"/></clipPath></defs></svg><p style="font-size:calc(0.875rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto m_b6d8b162 mantine-Text-root">View source</div></a></div><div class="tableOfContents_otRY theme-doc-toc-desktop"><ul class="table-of-contents table-of-contents__left-border"><li><a href=#implemented-traits class="table-of-contents__link toc-highlight">Implemented traits</a><li><a href=#comptime-members class="table-of-contents__link toc-highlight"><code>comptime</code> members</a><ul><li><a href=#__copyinit__is_trivial class="table-of-contents__link toc-highlight"><code>__copyinit__is_trivial</code></a><li><a href=#__del__is_trivial class="table-of-contents__link toc-highlight"><code>__del__is_trivial</code></a><li><a href=#__moveinit__is_trivial class="table-of-contents__link toc-highlight"><code>__moveinit__is_trivial</code></a><li><a href=#ascii_letters class="table-of-contents__link toc-highlight"><code>ASCII_LETTERS</code></a><li><a href=#ascii_lowercase class="table-of-contents__link toc-highlight"><code>ASCII_LOWERCASE</code></a><li><a href=#ascii_uppercase class="table-of-contents__link toc-highlight"><code>ASCII_UPPERCASE</code></a><li><a href=#digits class="table-of-contents__link toc-highlight"><code>DIGITS</code></a><li><a href=#flag_has_nul_terminator class="table-of-contents__link toc-highlight"><code>FLAG_HAS_NUL_TERMINATOR</code></a><li><a href=#flag_is_inline class="table-of-contents__link toc-highlight"><code>FLAG_IS_INLINE</code></a><li><a href=#flag_is_ref_counted class="table-of-contents__link toc-highlight"><code>FLAG_IS_REF_COUNTED</code></a><li><a href=#hex_digits class="table-of-contents__link toc-highlight"><code>HEX_DIGITS</code></a><li><a href=#inline_capacity class="table-of-contents__link toc-highlight"><code>INLINE_CAPACITY</code></a><li><a href=#inline_length_mask class="table-of-contents__link toc-highlight"><code>INLINE_LENGTH_MASK</code></a><li><a href=#inline_length_start class="table-of-contents__link toc-highlight"><code>INLINE_LENGTH_START</code></a><li><a href=#oct_digits class="table-of-contents__link toc-highlight"><code>OCT_DIGITS</code></a><li><a href=#printable class="table-of-contents__link toc-highlight"><code>PRINTABLE</code></a><li><a href=#punctuation class="table-of-contents__link toc-highlight"><code>PUNCTUATION</code></a><li><a href=#ref_count_size class="table-of-contents__link toc-highlight"><code>REF_COUNT_SIZE</code></a></ul><li><a href=#methods class="table-of-contents__link toc-highlight">Methods</a><ul><li><a href=#__init__ class="table-of-contents__link toc-highlight"><code>__init__</code></a><li><a href=#__copyinit__ class="table-of-contents__link toc-highlight"><code>__copyinit__</code></a><li><a href=#__moveinit__ class="table-of-contents__link toc-highlight"><code>__moveinit__</code></a><li><a href=#__del__ class="table-of-contents__link toc-highlight"><code>__del__</code></a><li><a href=#__bool__ class="table-of-contents__link toc-highlight"><code>__bool__</code></a><li><a href=#__getitem__ class="table-of-contents__link toc-highlight"><code>__getitem__</code></a><li><a href=#__lt__ class="table-of-contents__link toc-highlight"><code>__lt__</code></a><li><a href=#__eq__ class="table-of-contents__link toc-highlight"><code>__eq__</code></a><li><a href=#__ne__ class="table-of-contents__link toc-highlight"><code>__ne__</code></a><li><a href=#__contains__ class="table-of-contents__link toc-highlight"><code>__contains__</code></a><li><a href=#__add__ class="table-of-contents__link toc-highlight"><code>__add__</code></a><li><a href=#__mul__ class="table-of-contents__link toc-highlight"><code>__mul__</code></a><li><a href=#__radd__ class="table-of-contents__link toc-highlight"><code>__radd__</code></a><li><a href=#__iadd__ class="table-of-contents__link toc-highlight"><code>__iadd__</code></a><li><a href=#write class="table-of-contents__link toc-highlight"><code>write</code></a><li><a href=#capacity class="table-of-contents__link toc-highlight"><code>capacity</code></a><li><a href=#write_string class="table-of-contents__link toc-highlight"><code>write_string</code></a><li><a href=#append_byte class="table-of-contents__link toc-highlight"><code>append_byte</code></a><li><a href=#append class="table-of-contents__link toc-highlight"><code>append</code></a><li><a href=#__iter__ class="table-of-contents__link toc-highlight"><code>__iter__</code></a><li><a href=#__reversed__ class="table-of-contents__link toc-highlight"><code>__reversed__</code></a><li><a href=#__len__ class="table-of-contents__link toc-highlight"><code>__len__</code></a><li><a href=#__str__ class="table-of-contents__link toc-highlight"><code>__str__</code></a><li><a href=#__repr__ class="table-of-contents__link toc-highlight"><code>__repr__</code></a><li><a href=#__fspath__ class="table-of-contents__link toc-highlight"><code>__fspath__</code></a><li><a href=#to_python_object class="table-of-contents__link toc-highlight"><code>to_python_object</code></a><li><a href=#write_to class="table-of-contents__link toc-highlight"><code>write_to</code></a><li><a href=#write_repr_to class="table-of-contents__link toc-highlight"><code>write_repr_to</code></a><li><a href=#join class="table-of-contents__link toc-highlight"><code>join</code></a><li><a href=#codepoints class="table-of-contents__link toc-highlight"><code>codepoints</code></a><li><a href=#codepoint_slices class="table-of-contents__link toc-highlight"><code>codepoint_slices</code></a><li><a href=#codepoint_slices_reversed class="table-of-contents__link toc-highlight"><code>codepoint_slices_reversed</code></a><li><a href=#unsafe_ptr class="table-of-contents__link toc-highlight"><code>unsafe_ptr</code></a><li><a href=#unsafe_ptr_mut class="table-of-contents__link toc-highlight"><code>unsafe_ptr_mut</code></a><li><a href=#as_c_string_slice class="table-of-contents__link toc-highlight"><code>as_c_string_slice</code></a><li><a href=#unsafe_cstr_ptr class="table-of-contents__link toc-highlight"><code>unsafe_cstr_ptr</code></a><li><a href=#as_bytes class="table-of-contents__link toc-highlight"><code>as_bytes</code></a><li><a href=#as_bytes_mut class="table-of-contents__link toc-highlight"><code>as_bytes_mut</code></a><li><a href=#as_string_slice class="table-of-contents__link toc-highlight"><code>as_string_slice</code></a><li><a href=#byte_length class="table-of-contents__link toc-highlight"><code>byte_length</code></a><li><a href=#count_codepoints class="table-of-contents__link toc-highlight"><code>count_codepoints</code></a><li><a href=#set_byte_length class="table-of-contents__link toc-highlight"><code>set_byte_length</code></a><li><a href=#count class="table-of-contents__link toc-highlight"><code>count</code></a><li><a href=#find class="table-of-contents__link toc-highlight"><code>find</code></a><li><a href=#rfind class="table-of-contents__link toc-highlight"><code>rfind</code></a><li><a href=#isspace class="table-of-contents__link toc-highlight"><code>isspace</code></a><li><a href=#split class="table-of-contents__link toc-highlight"><code>split</code></a><li><a href=#splitlines class="table-of-contents__link toc-highlight"><code>splitlines</code></a><li><a href=#replace class="table-of-contents__link toc-highlight"><code>replace</code></a><li><a href=#strip class="table-of-contents__link toc-highlight"><code>strip</code></a><li><a href=#rstrip class="table-of-contents__link toc-highlight"><code>rstrip</code></a><li><a href=#lstrip class="table-of-contents__link toc-highlight"><code>lstrip</code></a><li><a href=#__hash__ class="table-of-contents__link toc-highlight"><code>__hash__</code></a><li><a href=#lower class="table-of-contents__link toc-highlight"><code>lower</code></a><li><a href=#upper class="table-of-contents__link toc-highlight"><code>upper</code></a><li><a href=#startswith class="table-of-contents__link toc-highlight"><code>startswith</code></a><li><a href=#endswith class="table-of-contents__link toc-highlight"><code>endswith</code></a><li><a href=#removeprefix class="table-of-contents__link toc-highlight"><code>removeprefix</code></a><li><a href=#removesuffix class="table-of-contents__link toc-highlight"><code>removesuffix</code></a><li><a href=#__int__ class="table-of-contents__link toc-highlight"><code>__int__</code></a><li><a href=#__float__ class="table-of-contents__link toc-highlight"><code>__float__</code></a><li><a href=#format class="table-of-contents__link toc-highlight"><code>format</code></a><li><a href=#is_ascii_digit class="table-of-contents__link toc-highlight"><code>is_ascii_digit</code></a><li><a href=#isupper class="table-of-contents__link toc-highlight"><code>isupper</code></a><li><a href=#islower class="table-of-contents__link toc-highlight"><code>islower</code></a><li><a href=#is_ascii_printable class="table-of-contents__link toc-highlight"><code>is_ascii_printable</code></a><li><a href=#ascii_rjust class="table-of-contents__link toc-highlight"><code>ascii_rjust</code></a><li><a href=#ascii_ljust class="table-of-contents__link toc-highlight"><code>ascii_ljust</code></a><li><a href=#ascii_center class="table-of-contents__link toc-highlight"><code>ascii_center</code></a><li><a href=#resize class="table-of-contents__link toc-highlight"><code>resize</code></a><li><a href=#reserve class="table-of-contents__link toc-highlight"><code>reserve</code></a></ul></ul><style data-mantine-styles=inline>.__m__-Rl6lalleh{flex-direction:row}@media (width>=997px){.__m__-Rl6lalleh{flex-direction:column}}</style><div style="gap:calc(0.75rem * var(--mantine-scale))" class="flex flex-col gap-4 border-0 border-l border-solid border-l-Elements-Twilight-20-70 pl-3 text-sm lg:text-base docs-desktop:pt-5 w-full hidden m_8bffd616 mantine-Flex-root __m__-Rl6lalleh"></div></div></div></div></div><div class="sticky bottom-0 z-[100] bg-Elements-Twilight-0-90 docs-desktop:hidden border-0 border-y border-solid border-y-Elements-Twilight-20-70 px-4"><div style="--group-gap:var(--mantine-spacing-md);--group-align:center;--group-justify:space-between;--group-wrap:nowrap;height:calc(4.125rem * var(--mantine-scale))" class="m_4081bf90 mantine-Group-root"><div style="--group-gap:calc(0.75rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:nowrap" class="grow justify-between md:justify-start m_4081bf90 mantine-Group-root"><style data-mantine-styles=inline>.__m__-R1lmqlalleh{flex-direction:row}@media (width>=997px){.__m__-R1lmqlalleh{flex-direction:column}}</style><div class="text-sm lg:text-base docs-desktop:mt-2 m_8bffd616 mantine-Flex-root __m__-R1lmqlalleh"><div class=mantine-hidden-from-docs-desktop><a href=https://github.com/modular/modular/tree/main/mojo/stdlib/std/collections/string/string.mojo target=_blank rel="noopener noreferrer" style="--button-bg:transparent;--button-hover:var(--Elements-Twilight-5-80);--button-color:var(--Elements-Twilight-60-50);--button-bd:calc(0.0625rem * var(--mantine-scale)) solid transparent;--button-height:calc(2.5rem * var(--mantine-scale));--button-padding-x:calc(1.375rem * var(--mantine-scale));--button-fz:calc(1rem * var(--mantine-scale));font-weight:400" class="mantine-focus-auto mantine-active onActive_LK5j onHover_fkhK no-transition !font-normal group my-auto px-4 hover:bg-Elements-Twilight-5-80 hover:no-underline m_77c9d27d mantine-Button-root m_87cf2631 mantine-UnstyledButton-root" data-variant=subtle><span class="m_80f1301b mantine-Button-inner"><span class="m_811560b9 mantine-Button-label"><div style="--group-gap:calc(0.5rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:wrap" class="text-Elements-Twilight-60-40 m_4081bf90 mantine-Group-root"><svg viewBox="0 0 12 12" xmlns=http://www.w3.org/2000/svg style="width:calc(0.875rem * var(--mantine-scale));height:calc(0.875rem * var(--mantine-scale))" class=group-hover:text-black fill=currentColor><g clip-path=url(#:Rdmlllllmqlalleh:)><path fill-rule=evenodd clip-rule=evenodd d="M6 .8c2.9 0 5.2 2.4 5.2 5.3 0 2.4-1.5 4.4-3.6 5-.2.1-.3 0-.3-.2V9.5c0-.5-.2-.9-.4-1 1.2-.1 2.4-.6 2.4-2.6 0-.6-.2-1.1-.5-1.5 0-.1.2-.7 0-1.4 0 0-.5-.1-1.5.6a4.9 4.9 0 0 0-2.6 0c-1-.7-1.4-.6-1.4-.6a2 2 0 0 0 0 1.4A2 2 0 0 0 2.6 6c0 2 1.2 2.5 2.4 2.6-.2.1-.3.4-.4.7-.3.1-1 .4-1.5-.4 0 0-.3-.6-.8-.6 0 0-.5 0 0 .3 0 0 .3.2.6.8 0 0 .3 1 1.7.6v1c0 .2 0 .3-.3.3-2.1-.7-3.6-2.7-3.6-5C.8 3.1 3.1.7 6 .7Z"/></g><defs><clipPath id=:Rdmlllllmqlalleh:><path fill=var(--White) transform="translate(.8 .8)" d="M0 0h10.4v10.4H0z"/></clipPath></defs></svg><p style="font-size:calc(0.875rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto group-hover:text-black m_b6d8b162 mantine-Text-root">View source</div></span></span></a></div><a href=https://github.com/modular/modular/tree/main/mojo/stdlib/std/collections/string/string.mojo target=_blank rel="noopener noreferrer" class="mantine-focus-auto my-auto hover:no-underline docs-desktop:-mt-2 m_87cf2631 mantine-UnstyledButton-root mantine-visible-from-docs-desktop"><div style="--group-gap:calc(0.5rem * var(--mantine-scale));--group-align:center;--group-justify:flex-start;--group-wrap:wrap" class="group text-Elements-Twilight-60-40 hover:text-black m_4081bf90 mantine-Group-root"><svg viewBox="0 0 12 12" xmlns=http://www.w3.org/2000/svg style="width:calc(0.875rem * var(--mantine-scale));height:calc(0.875rem * var(--mantine-scale))" fill=currentColor><g clip-path=url(#:Rdmlllmqlalleh:)><path fill-rule=evenodd clip-rule=evenodd d="M6 .8c2.9 0 5.2 2.4 5.2 5.3 0 2.4-1.5 4.4-3.6 5-.2.1-.3 0-.3-.2V9.5c0-.5-.2-.9-.4-1 1.2-.1 2.4-.6 2.4-2.6 0-.6-.2-1.1-.5-1.5 0-.1.2-.7 0-1.4 0 0-.5-.1-1.5.6a4.9 4.9 0 0 0-2.6 0c-1-.7-1.4-.6-1.4-.6a2 2 0 0 0 0 1.4A2 2 0 0 0 2.6 6c0 2 1.2 2.5 2.4 2.6-.2.1-.3.4-.4.7-.3.1-1 .4-1.5-.4 0 0-.3-.6-.8-.6 0 0-.5 0 0 .3 0 0 .3.2.6.8 0 0 .3 1 1.7.6v1c0 .2 0 .3-.3.3-2.1-.7-3.6-2.7-3.6-5C.8 3.1 3.1.7 6 .7Z"/></g><defs><clipPath id=:Rdmlllmqlalleh:><path fill=var(--White) transform="translate(.8 .8)" d="M0 0h10.4v10.4H0z"/></clipPath></defs></svg><p style="font-size:calc(0.875rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto m_b6d8b162 mantine-Text-root">View source</div></a></div><style data-mantine-styles=inline>.__m__-R2lmqlalleh{flex-direction:row}@media (width>=997px){.__m__-R2lmqlalleh{flex-direction:column}}</style><div style="gap:calc(0.75rem * var(--mantine-scale))" class="w-full sm:w-fit text-sm lg:text-base docs-desktop:pt-5 w-full hidden m_8bffd616 mantine-Flex-root __m__-R2lmqlalleh"></div></div><div class="min-w-60 mantine-visible-from-md"><div class="w-full docs-desktop:mt-11"><div style=--group-gap:0rem;--group-align:center;--group-justify:flex-start;--group-wrap:wrap class="relative transition-all duration-200 w-full justify-end docs-desktop:justify-center m_4081bf90 mantine-Group-root"><p style="color:var(--Elements-Twilight-70-20);font-size:calc(1rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto mr-1 !text-sm docs-desktop:mr-3 docs-desktop:!text-base m_b6d8b162 mantine-Text-root">Was this page helpful?</p><button style="--ai-bg:transparent;--ai-hover:color-mix(in srgb, var(--Elements-Twilight-60-50), transparent 88%);--ai-color:var(--Elements-Twilight-60-50);--ai-bd:calc(0.0625rem * var(--mantine-scale)) solid transparent" class="mantine-focus-auto mantine-active w-8 docs-desktop:w-[42px] m_8d3f4000 mantine-ActionIcon-root m_87cf2631 mantine-UnstyledButton-root" data-variant=subtle type=button><span class="m_8d3afb97 mantine-ActionIcon-icon"><svg viewBox="0 0 20 18" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(1.25rem * var(--mantine-scale));height:calc(1.25rem * var(--mantine-scale))"><path d="M5 8.58v7.92M16.25 16.5H1.67V8.58H5L7.08 1.5h.75a3 3 0 0 1 3 3v2h7.5l-2.08 10Z" stroke=currentColor stroke-width=1.5 /></svg></span></button><button style="--ai-bg:transparent;--ai-hover:color-mix(in srgb, var(--Elements-Twilight-60-50), transparent 88%);--ai-color:var(--Elements-Twilight-60-50);--ai-bd:calc(0.0625rem * var(--mantine-scale)) solid transparent" class="mantine-focus-auto mantine-active w-8 docs-desktop:w-[42px] m_8d3f4000 mantine-ActionIcon-root m_87cf2631 mantine-UnstyledButton-root" data-variant=subtle type=button><span class="m_8d3afb97 mantine-ActionIcon-icon"><svg viewBox="0 0 20 18" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(1.25rem * var(--mantine-scale));height:calc(1.25rem * var(--mantine-scale))" class=rotate-180><path d="M5 8.58v7.92M16.25 16.5H1.67V8.58H5L7.08 1.5h.75a3 3 0 0 1 3 3v2h7.5l-2.08 10Z" stroke=currentColor stroke-width=1.5 /></svg></span></button></div><p style="color:var(--Elements-Twilight-70-20);font-size:calc(1rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto h-0 docs-desktop:translate-y-4 scale-y-0 opacity-0 relative m-auto transition-all duration-200 text-center !text-sm docs-desktop:!text-base m_b6d8b162 mantine-Text-root">Thank you! We'll create more content like this.<p style="color:var(--Elements-Twilight-70-20);font-size:calc(1rem * var(--mantine-scale));line-height:calc(1.5rem * var(--mantine-scale))" class="mantine-focus-auto h-0 docs-desktop:translate-y-4 scale-y-0 opacity-0 relative m-auto transition-all duration-200 text-center !text-sm docs-desktop:!text-base m_b6d8b162 mantine-Text-root">Thank you for helping us improve!</div></div></div></div></div></main></div></div></div><div class=docsite-footer><div class="m_3eebeb36 mantine-Divider-root" data-orientation=horizontal role=separator></div><div class="page-footer mx-auto max-w-[1440px] font-inter"><img class="absolute left-0" referrerpolicy=no-referrer-when-downgrade src="https://static.scarf.sh/a.png?x-pxid=d240bcad-0bb5-4db6-8c37-9061bb991d8e" alt="" /><div class="my-6 grid grid-cols-1 gap-x-10 gap-y-6 px-5 docs-desktop:grid-cols-7 docs-desktop:gap-y-0 [&_p]:text-black"><a href=https://www.modular.com target=_self rel="noopener noreferrer" class=docs-desktop:col-span-2><svg style="width:calc(6rem * var(--mantine-scale));height:calc(1.25rem * var(--mantine-scale))" xmlns=http://www.w3.org/2000/svg viewBox="0 0 132 28" color=var(--Black)><path stroke=transparent fill=currentColor d="M42.5 7.5C37 7.5 33 11.6 33 17.7 33 24 37 28 42.5 28c5.3 0 9.4-4.1 9.4-10.3 0-6-4.1-10.2-9.4-10.2Zm0 17.7c-3.6 0-6.6-3-6.6-7.5s3-7.4 6.6-7.4c3.5 0 6.5 3 6.5 7.4 0 4.6-3 7.5-6.5 7.5Zm26.9-14.6h-.2a7.5 7.5 0 0 0-6.3-3.1c-5.2 0-9.1 4.1-9.1 10.2 0 6.2 3.9 10.3 9 10.3 2.9 0 4.8-1.1 6.4-3.2h.2v2.8h3V0h-3v10.6ZM63 25.2c-3.4 0-6.3-3-6.3-7.5s3-7.4 6.3-7.4 6.3 3 6.3 7.4c0 4.6-3 7.5-6.3 7.5ZM89.2 8h3v19.7h-3v-2.2H89a8 8 0 0 1-6 2.6c-4.4 0-7.8-3.4-7.8-8.3V8h3v11.8c0 3.2 2.4 5.5 5.3 5.5 3.2 0 5.7-2.5 5.7-5.5V8Zm6-7.9H98v27.6h-3V0Zm20.7 10.6h-.2a7.5 7.5 0 0 0-6.3-3.1c-5.2 0-9 4.1-9 10.2 0 6.2 3.8 10.3 9 10.3 2.8 0 4.7-1.1 6.3-3.2h.2v2.8h3V8h-3v2.7Zm-6.3 14.6c-3.4 0-6.3-3-6.3-7.5s3-7.4 6.3-7.4 6.3 3 6.3 7.4c0 4.6-3 7.5-6.3 7.5ZM132 8v2.7h-7c-.2 0-.3.1-.3.2v16.8h-3v-17h2.8l.2-.1V7.9h7.3ZM27.8 4h3v23.5h-3.2V4.3l-.2-.2H26l-8.3 23.5H13L4.7 4.1H3.2v23.5H0V0h6.5L15 24h.8l8.4-24h3.4v4l.2.1Z"/></svg></a><div style=--group-gap:var(--mantine-spacing-md);--group-align:center;--group-justify:flex-start;--group-wrap:wrap class="min-w-[450px] docs-desktop:col-span-3 docs-desktop:mx-auto m_4081bf90 mantine-Group-root"><a href="https://builds.modular.com/?category=models" target=_self rel="noopener noreferrer"><p style=margin:0rem;padding:0rem class="body-14-light mantine-Text-root">Models</p></a><a href=https://github.com/modular/max-agentic-cookbook target=_self rel="noopener noreferrer"><p style=margin:0rem;padding:0rem class="body-14-light mantine-Text-root">Cookbook</p></a><a href=https://puzzles.modular.com/ target=_self rel="noopener noreferrer"><p style=margin:0rem;padding:0rem class="body-14-light mantine-Text-root">Puzzles</p></a><a href=https://www.modular.com/blog target=_self rel="noopener noreferrer"><p style=margin:0rem;padding:0rem class="body-14-light mantine-Text-root">Blog</p></a><a href=https://www.modular.com/community target=_self rel="noopener noreferrer"><p style=margin:0rem;padding:0rem class="body-14-light mantine-Text-root">Community</p></a><a href=https://www.modular.com/request-demo target=_self rel="noopener noreferrer"><p style=margin:0rem;padding:0rem class="body-14-light mantine-Text-root">Contact</p></a></div><div style=--group-gap:var(--mantine-spacing-md);--group-align:flex-start;--group-justify:space-between;--group-wrap:wrap class="docs-desktop:col-span-2 m_4081bf90 mantine-Group-root"><div style=flex:1 class="hidden docs-desktop:block"></div><div style=--group-gap:var(--mantine-spacing-xxs);--group-align:center;--group-justify:flex-start;--group-wrap:wrap class="my-auto m_4081bf90 mantine-Group-root"><a href=https://github.com/modular target=_self rel="noopener noreferrer" class="flex h-5 items-center"><svg viewBox="0 0 12 12" xmlns=http://www.w3.org/2000/svg style="width:calc(1.625rem * var(--mantine-scale));height:calc(1.625rem * var(--mantine-scale))" class=mr-1 color=var(--Elements-Twilight-40-60) fill=currentColor><g clip-path=url(#:Rdltlmleh:)><path fill-rule=evenodd clip-rule=evenodd d="M6 .8c2.9 0 5.2 2.4 5.2 5.3 0 2.4-1.5 4.4-3.6 5-.2.1-.3 0-.3-.2V9.5c0-.5-.2-.9-.4-1 1.2-.1 2.4-.6 2.4-2.6 0-.6-.2-1.1-.5-1.5 0-.1.2-.7 0-1.4 0 0-.5-.1-1.5.6a4.9 4.9 0 0 0-2.6 0c-1-.7-1.4-.6-1.4-.6a2 2 0 0 0 0 1.4A2 2 0 0 0 2.6 6c0 2 1.2 2.5 2.4 2.6-.2.1-.3.4-.4.7-.3.1-1 .4-1.5-.4 0 0-.3-.6-.8-.6 0 0-.5 0 0 .3 0 0 .3.2.6.8 0 0 .3 1 1.7.6v1c0 .2 0 .3-.3.3-2.1-.7-3.6-2.7-3.6-5C.8 3.1 3.1.7 6 .7Z"/></g><defs><clipPath id=:Rdltlmleh:><path fill=var(--White) transform="translate(.8 .8)" d="M0 0h10.4v10.4H0z"/></clipPath></defs></svg></a><a href=https://discord.gg/modular target=_self rel="noopener noreferrer" class="flex h-5 items-center"><svg viewBox="0 0 20 20" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(2rem * var(--mantine-scale));height:calc(2rem * var(--mantine-scale))"><path d="M15.2 4.97c-.96-.45-2-.78-3.09-.97-.13.24-.29.57-.4.82-1.15-.17-2.3-.17-3.42 0a8.8 8.8 0 0 0-.4-.82c-1.1.19-2.13.52-3.1.97a12.98 12.98 0 0 0-2.23 8.7c1.3.97 2.56 1.55 3.8 1.94.3-.42.58-.87.81-1.34a8 8 0 0 1-1.28-.62l.32-.25a8.75 8.75 0 0 0 7.58 0l.32.25c-.4.24-.84.45-1.28.62.23.47.5.92.8 1.34 1.25-.38 2.5-.97 3.8-1.94.32-3.3-.53-6.16-2.22-8.7Zm-7.7 6.95c-.73 0-1.34-.7-1.34-1.54 0-.84.6-1.53 1.35-1.53.75 0 1.36.69 1.35 1.53 0 .84-.6 1.54-1.35 1.54Zm5 0c-.75 0-1.36-.7-1.36-1.54 0-.84.6-1.53 1.35-1.53.76 0 1.36.69 1.35 1.53 0 .84-.6 1.54-1.35 1.54Z" fill=var(--Elements-Twilight-40-60) /></svg></a><a href=https://twitter.com/modular target=_self rel="noopener noreferrer" class="flex h-5 items-center"><svg viewBox="0 0 24 24" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(2rem * var(--mantine-scale));height:calc(2rem * var(--mantine-scale))" color=var(--Elements-Twilight-40-60)><path d="M13.14 11.09 17.61 6h-1.06l-3.88 4.42L9.57 6H6l4.69 6.68L6 18h1.06l4.1-4.66L14.42 18H18M7.44 6.78h1.63l7.48 10.49h-1.62" fill=currentColor /></svg></a><a href=https://www.youtube.com/@modularinc target=_self rel="noopener noreferrer" class="flex h-5 items-center"><svg viewBox="0 0 40 40" fill=none xmlns=http://www.w3.org/2000/svg style="width:calc(2rem * var(--mantine-scale));height:calc(2rem * var(--mantine-scale))"><g filter=url(#:R15ltlmleh:)><path fill-rule=evenodd clip-rule=evenodd d="M8.49 30.56A3.49 3.49 0 0 1 5 27.07V12.49A3.49 3.49 0 0 1 8.49 9H31.5A3.49 3.49 0 0 1 35 12.49v14.58a3.49 3.49 0 0 1-3.49 3.49H8.5Zm9.45-15.1 6.18 4.32-6.18 4.32v-8.64Z" fill=var(--Elements-Twilight-40-60) /></g><defs><filter id=:R15ltlmleh: x=4.86 y=9 width=30.28 height=21.84 filterUnits=userSpaceOnUse color-interpolation-filters=sRGB><feFlood flood-opacity=0 result=BackgroundImageFix /><feColorMatrix in=SourceAlpha values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result=hardAlpha /><feOffset dy=.14 /><feGaussianBlur stdDeviation=.07 /><feComposite in2=hardAlpha operator=out /><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/><feBlend in2=BackgroundImageFix result=effect1_dropShadow_1082_489 /><feBlend in=SourceGraphic in2=effect1_dropShadow_1082_489 result=shape /></filter></defs></svg></a><a href=https://www.linkedin.com/company/modular-ai/ target=_self rel="noopener noreferrer" class="flex h-5 items-center"><svg viewBox="0 0 40 40" style="width:calc(2rem * var(--mantine-scale));height:calc(2rem * var(--mantine-scale))" fill=none xmlns=http://www.w3.org/2000/svg><path fill-rule=evenodd clip-rule=evenodd d="M29.33 32H10.67A2.67 2.67 0 0 1 8 29.33V10.67C8 9.19 9.2 8 10.67 8h18.66C30.81 8 32 9.2 32 10.67v18.66c0 1.48-1.2 2.67-2.67 2.67Zm-4.22-3.33h3.56v-7.32c0-3.1-1.76-4.6-4.2-4.6-2.46 0-3.5 1.92-3.5 1.92V17.1h-3.43v11.56h3.44V22.6c0-1.62.74-2.6 2.18-2.6 1.31 0 1.95.94 1.95 2.6v6.07Zm-13.78-15.2c0 1.17.95 2.13 2.12 2.13 1.17 0 2.12-.96 2.12-2.13 0-1.18-.95-2.14-2.12-2.14-1.17 0-2.12.96-2.12 2.14Zm3.93 15.2h-3.58V17.1h3.58v11.56Z" fill=var(--Elements-Twilight-40-60) /></svg></a></div></div></div></div></div></div></body>