# Source: https://alexop.dev/posts/create-pwa-vue3-vite-4-steps

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite | alexop.dev</title><meta name="title" content="Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite | alexop.dev"><meta name="description" content="Transform your Vue 3 project into a powerful Progressive Web App in just 4 steps. Learn how to create offline-capable, installable web apps using Vite and modern PWA techniques."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
      document.addEventListener("DOMContentLoaded", function () {
        if (typeof renderMathInElement === "function") {
          renderMathInElement(document.body, {
            delimiters: [
              { left: "$$", right: "$$", display: true },
              { left: "$", right: "$", display: false },
              { left: "\\(", right: "\\)", display: false },
              { left: "\\[", right: "\\]", display: true },
            ],
            throwOnError: false,
            trust: true,
            strict: false,
            output: "html",
          });
        }
      });
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite | alexop.dev"><meta property="og:description" content="Transform your Vue 3 project into a powerful Progressive Web App in just 4 steps. Learn how to create offline-capable, installable web apps using Vite and modern PWA techniques."><meta property="og:url" content="https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/"><meta property="og:image" content="https://alexop.dev/posts/create-a-native-like-app-in-4-steps-pwa-magic-with-vue-3-and-vite/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2024-10-20T07:44:12.000Z"><meta property="article:modified_time" content="2024-12-30T22:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/"><meta property="twitter:title" content="Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite | alexop.dev"><meta property="twitter:description" content="Transform your Vue 3 project into a powerful Progressive Web App in just 4 steps. Learn how to create offline-capable, installable web apps using Vite and modern PWA techniques."><meta property="twitter:image" content="https://alexop.dev/posts/create-a-native-like-app-in-4-steps-pwa-magic-with-vue-3-and-vite/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite | alexop.dev","description":"Transform your Vue 3 project into a powerful Progressive Web App in just 4 steps. Learn how to create offline-capable, installable web apps using Vite and modern PWA techniques.","image":"https://alexop.dev/posts/create-a-native-like-app-in-4-steps-pwa-magic-with-vue-3-and-vite/index.png","datePublished":"2024-10-20T07:44:12.000Z","dateModified":"2024-12-30T22:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
<style>a:where(.astro-blwjyjpt){transition:all .3s ease}a:where(.astro-blwjyjpt):hover{transform:translateY(-2px);box-shadow:0 4px 6px -1px #0000001a,0 2px 4px -1px #0000000f}
.minimal-posts-list:where(.astro-eenky23y){width:100%;max-width:64rem;margin:0 auto;padding:2rem 1rem;background:rgb(var(--color-fill));color:rgb(var(--color-text-base))}.posts-title:where(.astro-eenky23y){font-size:2rem;margin-bottom:2rem;color:rgb(var(--color-accent));font-family:inherit;font-weight:600;letter-spacing:.02em}.year-group:where(.astro-eenky23y){margin-bottom:2.5rem}.year-heading:where(.astro-eenky23y){font-size:1.3rem;color:rgb(var(--color-text-base));margin:2.5rem 0 1.2rem;font-family:inherit;font-weight:500;letter-spacing:.04em}.year-group:where(.astro-eenky23y) ul:where(.astro-eenky23y){list-style:none;padding:0;margin:0}.post-item:where(.astro-eenky23y){display:flex;justify-content:space-between;align-items:center;padding:1rem 0;border-bottom:1px solid rgba(var(--color-border),.2)}.post-link:where(.astro-eenky23y){color:rgb(var(--color-text-base));text-decoration:none;font-size:1.1rem;transition:color .2s}.post-link:where(.astro-eenky23y):hover{color:rgb(var(--color-accent))}.post-date:where(.astro-eenky23y){color:rgb(var(--color-card-muted));font-size:.95rem;font-family:inherit;letter-spacing:.05em;min-width:70px;text-align:right}
@keyframes astroFadeInOut{0%{opacity:1}to{opacity:0}}@keyframes astroFadeIn{0%{opacity:0;mix-blend-mode:plus-lighter}to{opacity:1;mix-blend-mode:plus-lighter}}@keyframes astroFadeOut{0%{opacity:1;mix-blend-mode:plus-lighter}to{opacity:0;mix-blend-mode:plus-lighter}}@keyframes astroSlideFromRight{0%{transform:translate(100%)}}@keyframes astroSlideFromLeft{0%{transform:translate(-100%)}}@keyframes astroSlideToRight{to{transform:translate(100%)}}@keyframes astroSlideToLeft{to{transform:translate(-100%)}}@media(prefers-reduced-motion){::view-transition-group(*),::view-transition-old(*),::view-transition-new(*){animation:none!important}[data-astro-transition-scope]{animation:none!important}}
</style>
<link rel="stylesheet" href="/_astro/index.Ck-KI3hC.css">
<style>.subagent-diagram-container:where(.astro-tpygpejy){display:flex;flex-direction:column;align-items:center;margin:2rem 0;width:100%}.subagent-diagram-fallback:where(.astro-tpygpejy){width:100%;max-width:600px}.subagent-diagram-svg:where(.astro-tpygpejy){width:100%;height:auto}.agent-circle:where(.astro-tpygpejy){fill:rgb(var(--color-accent) / .1);stroke:rgb(var(--color-accent));stroke-width:2}.subagent-circle:where(.astro-tpygpejy){fill:rgb(var(--color-accent) / .05);stroke:rgb(var(--color-accent) / .7);stroke-width:2;stroke-dasharray:4 2}.agent-icon:where(.astro-tpygpejy){font-size:24px}.agent-label:where(.astro-tpygpejy){fill:rgb(var(--color-text-base));font-size:12px;font-weight:500}.arrow-path:where(.astro-tpygpejy){fill:none;stroke:rgb(var(--color-text-base) / .5);stroke-width:2}.arrow-path:where(.astro-tpygpejy).dashed{stroke-dasharray:5 3}.arrow-path:where(.astro-tpygpejy).search-arrow{stroke:rgb(var(--color-accent) / .6)}.arrowhead-fill:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .5)}.arrow-label:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .6);font-size:11px;font-style:italic}.file-tree:where(.astro-tpygpejy) .folder:where(.astro-tpygpejy){fill:rgb(var(--color-text-base));font-size:14px;font-family:ui-monospace,monospace}.file-tree:where(.astro-tpygpejy) .file:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .7);font-size:14px;font-family:ui-monospace,monospace}.file-tree:where(.astro-tpygpejy) .file:where(.astro-tpygpejy).highlight{fill:rgb(var(--color-accent));font-weight:600}.subagent-diagram-caption:where(.astro-tpygpejy){margin-top:1rem;text-align:center;font-size:.875rem;color:rgb(var(--color-text-base) / .7)}.subagent-diagram-fallback:where(.astro-tpygpejy){display:none}
.parallel-subagent-diagram-container:where(.astro-u2chhpb2){display:flex;flex-direction:column;align-items:center;margin:2rem 0;width:100%}.parallel-subagent-diagram-fallback:where(.astro-u2chhpb2){width:100%;max-width:800px}.parallel-subagent-diagram-svg-static:where(.astro-u2chhpb2){width:100%;height:auto}.agent-circle:where(.astro-u2chhpb2){fill:rgb(var(--color-accent) / .1);stroke:rgb(var(--color-accent));stroke-width:2}.subagent-circle:where(.astro-u2chhpb2){stroke-width:2;stroke-dasharray:4 2}.agent-icon:where(.astro-u2chhpb2){font-size:24px}.agent-label:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base));font-size:12px;font-weight:500}.task-label:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .8);font-size:13px;font-family:ui-monospace,monospace}.arrow-path:where(.astro-u2chhpb2){fill:none;stroke:rgb(var(--color-text-base) / .5);stroke-width:2}.arrow-path:where(.astro-u2chhpb2).dashed{stroke-dasharray:5 3}.arrow-path:where(.astro-u2chhpb2).report{stroke:#22c55e}.arrowhead-fill:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .5)}.domain-box-rect:where(.astro-u2chhpb2){fill:rgb(var(--color-fill) / .5);stroke-width:1.5}.domain-label:where(.astro-u2chhpb2){font-size:11px;font-weight:600}.finding-text:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .7);font-size:10px;font-family:ui-monospace,monospace}.synthesis-box:where(.astro-u2chhpb2){fill:#22c55e1a;stroke:#22c55e;stroke-width:2}.synthesis-text:where(.astro-u2chhpb2){fill:#22c55e;font-size:13px;font-weight:600}.parallel-subagent-diagram-caption:where(.astro-u2chhpb2){margin-top:1rem;text-align:center;font-size:.875rem;color:rgb(var(--color-text-base) / .7)}.parallel-subagent-diagram-fallback:where(.astro-u2chhpb2){display:none}
.shiki-magic-move-container{position:relative;white-space:pre}.shiki-magic-move-line-number{opacity:.3;-webkit-user-select:none;-moz-user-select:none;user-select:none}.shiki-magic-move-item{display:inline-block;transition:color var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-enter-active,.shiki-magic-move-leave-active,.shiki-magic-move-move{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-container-resize,.shiki-magic-move-container-restyle{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease");transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-container, 1))}.shiki-magic-move-move{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-move, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-enter-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-enter, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-leave-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-leave, 1) + var(--smm-stagger, 0))}.shiki-magic-move-enter-from,.shiki-magic-move-leave-to{opacity:0}br.shiki-magic-move-leave-active{display:none}
.jazz-demo-root[data-v-d8349330]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-d8349330]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-d8349330]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-d8349330]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-d8349330]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-d8349330]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-d8349330]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-d8349330]{background:#2563eb}.jazz-demo-toggle-off[data-v-d8349330]{background:#4b5563}.jazz-demo-toggle-dot[data-v-d8349330]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-d8349330]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-d8349330]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-d8349330]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-d8349330]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-d8349330]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-d8349330]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-d8349330]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card-title[data-v-d8349330]{font-size:1.25rem;font-weight:700;color:#fff;margin:0 0 .75rem}.jazz-demo-form[data-v-d8349330]{margin-bottom:.75rem;display:flex;flex-direction:column;gap:.5rem}.jazz-demo-input[data-v-d8349330]{width:100%;padding:.375rem .625rem;background:#1f2937;border:1px solid #4b5563;border-radius:.5rem;color:#fff;font-size:.8125rem;outline:none;box-sizing:border-box}.jazz-demo-input[data-v-d8349330]:focus{border-color:#3b82f6;box-shadow:0 0 0 2px #3b82f64d}.jazz-demo-input[data-v-d8349330]::-moz-placeholder{color:#6b7280}.jazz-demo-input[data-v-d8349330]::placeholder{color:#6b7280}.jazz-demo-add-btn[data-v-d8349330]{width:100%;padding:.375rem .75rem;background:#2563eb;color:#fff;border:none;border-radius:.5rem;font-weight:500;font-size:.8125rem;cursor:pointer;transition:background-color .2s}.jazz-demo-add-btn[data-v-d8349330]:hover{background:#1d4ed8}.jazz-demo-list[data-v-d8349330]{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.25rem}.jazz-demo-item[data-v-d8349330]{display:flex;align-items:center;gap:.5rem;padding:.375rem;border-radius:.5rem}.jazz-demo-item[data-v-d8349330]:hover{background:#1f2937}.jazz-demo-item:hover .jazz-demo-delete[data-v-d8349330]{opacity:1}.jazz-demo-drag[data-v-d8349330]{cursor:grab;color:#4b5563;transition:color .2s;-webkit-user-select:none;-moz-user-select:none;user-select:none;display:flex;align-items:center}.jazz-demo-drag[data-v-d8349330]:active{cursor:grabbing}.jazz-demo-item:hover .jazz-demo-drag[data-v-d8349330]{color:#9ca3af}.jazz-demo-svg[data-v-d8349330]{width:1rem;height:1rem}.jazz-demo-checkbox[data-v-d8349330]{width:.875rem;height:.875rem;accent-color:#2563eb}.jazz-demo-text[data-v-d8349330]{flex:1;color:#e5e7eb;font-size:.8125rem}.jazz-demo-text-done[data-v-d8349330]{text-decoration:line-through;color:#6b7280}.jazz-demo-delete[data-v-d8349330]{opacity:0;transition:opacity .2s;color:#6b7280;background:none;border:none;padding:.125rem;cursor:pointer;display:flex;align-items:center}.jazz-demo-delete[data-v-d8349330]:hover{color:#f87171}.jazz-demo-empty[data-v-d8349330]{color:#6b7280;text-align:center;padding:1rem 0;margin:0;font-size:.8125rem}
.jazz-demo-root[data-v-1a336f1a]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-1a336f1a]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-1a336f1a]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-1a336f1a]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-1a336f1a]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-1a336f1a]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-1a336f1a]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-1a336f1a]{background:#2563eb}.jazz-demo-toggle-off[data-v-1a336f1a]{background:#4b5563}.jazz-demo-toggle-dot[data-v-1a336f1a]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-1a336f1a]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-1a336f1a]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-1a336f1a]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-1a336f1a]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-1a336f1a]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-1a336f1a]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-1a336f1a]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card[data-v-1a336f1a]{padding:1.5rem}.jazz-counter-display[data-v-1a336f1a]{font-size:3rem;font-weight:700;color:#fff;text-align:center;padding:1rem 0;font-variant-numeric:tabular-nums}.jazz-counter-controls[data-v-1a336f1a]{display:flex;gap:.5rem}.jazz-counter-btn[data-v-1a336f1a]{flex:1;padding:.5rem;font-size:1.25rem;font-weight:600;border:1px solid #374151;border-radius:.5rem;background:#1f2937;color:#e5e7eb;cursor:pointer;transition:background-color .2s}.jazz-counter-btn[data-v-1a336f1a]:hover{background:#374151}.jazz-counter-btn-primary[data-v-1a336f1a]{background:#2563eb;border-color:#2563eb;color:#fff}.jazz-counter-btn-primary[data-v-1a336f1a]:hover{background:#1d4ed8}
.shiki-magic-move-container{position:relative;white-space:pre}.shiki-magic-move-line-number{opacity:.3;-webkit-user-select:none;-moz-user-select:none;user-select:none}.shiki-magic-move-item{display:inline-block;transition:color var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-enter-active,.shiki-magic-move-leave-active,.shiki-magic-move-move{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-container-resize,.shiki-magic-move-container-restyle{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease");transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-container, 1))}.shiki-magic-move-move{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-move, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-enter-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-enter, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-leave-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-leave, 1) + var(--smm-stagger, 0))}.shiki-magic-move-enter-from,.shiki-magic-move-leave-to{opacity:0}br.shiki-magic-move-leave-active{display:none}
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: create-a-native-like-app-in-4-steps-pwa-magic-with-vue-3-and-vite; }@layer astro { ::view-transition-old(create-a-native-like-app-in-4-steps-pwa-magic-with-vue-3-and-vite) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(create-a-native-like-app-in-4-steps-pwa-magic-with-vue-3-and-vite) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(create-a-native-like-app-in-4-steps-pwa-magic-with-vue-3-and-vite) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(create-a-native-like-app-in-4-steps-pwa-magic-with-vue-3-and-vite) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-plk3gbjq-1"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-plk3gbjq-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-plk3gbjq-1"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-plk3gbjq-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-plk3gbjq-1"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-plk3gbjq-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-plk3gbjq-1"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-plk3gbjq-1"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style><style>:root{--color-skin-card: rgb(var(--color-card));--color-skin-card-muted: rgb(var(--color-card-muted));--color-skin-border: rgb(var(--color-border));--color-skin-text-base: rgb(var(--color-text-base));--color-skin-accent: rgb(var(--color-accent));--color-skin-note: rgb(59, 130, 246);--color-skin-tip: rgb(16, 185, 129);--color-skin-caution: rgb(245, 158, 11);--color-skin-danger: rgb(239, 68, 68);--color-skin-info: rgb(99, 102, 241)}.aside:where(.astro-37uy2q7c){background-color:var(--color-skin-card);border-left:4px solid;border-radius:.5rem;box-shadow:0 4px 6px -1px #0000001a,0 2px 4px -1px #0000000f;margin:1.5rem 0;transition:all .3s ease}.aside:where(.astro-37uy2q7c):hover{box-shadow:0 10px 15px -3px #0000001a,0 4px 6px -2px #0000000d}.aside-content:where(.astro-37uy2q7c){padding:1rem 1.5rem}.aside-title:where(.astro-37uy2q7c){display:flex;align-items:center;font-weight:700;font-size:1.1rem;margin-bottom:.75rem}.aside-emoji:where(.astro-37uy2q7c){font-size:1.4rem;margin-right:.75rem}.aside-body:where(.astro-37uy2q7c){color:var(--color-skin-text-base);font-size:.95rem;line-height:1.6}.aside-note:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-note),.1);border-left-color:var(--color-skin-note)}.aside-note:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-note)}.aside-tip:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-tip),.1);border-left-color:var(--color-skin-tip)}.aside-tip:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-tip)}.aside-caution:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-caution),.1);border-left-color:var(--color-skin-caution)}.aside-caution:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-caution)}.aside-danger:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-danger),.1);border-left-color:var(--color-skin-danger)}.aside-danger:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-danger)}.aside-info:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-info),.1);border-left-color:var(--color-skin-info)}.aside-info:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-info)}
</style><style>.captioned-image:where(.astro-t2d64o5a){margin:2rem auto;text-align:center;max-width:600px}.captioned-image:where(.astro-t2d64o5a) img:where(.astro-t2d64o5a){max-width:100%;height:auto}.captioned-image:where(.astro-t2d64o5a) figcaption:where(.astro-t2d64o5a){margin-top:.5rem;font-style:italic;color:var(--text-base)}
</style><style>.excalidraw-figure:where(.astro-hxyrieg5){margin-top:2rem;margin-bottom:2rem;width:100%;max-width:100%}.excalidraw-svg:where(.astro-hxyrieg5){width:100%;--excalidraw-text: rgb(var(--color-text-base));--excalidraw-fill: rgb(var(--color-card));--excalidraw-accent: rgb(var(--color-accent))}.excalidraw-svg svg.excalidraw-rendered{display:block;height:auto;width:100%}figcaption:where(.astro-hxyrieg5){margin-top:1rem;text-align:center;font-size:.875rem;line-height:1.25rem;font-style:italic;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1))}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));transition-property:opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.2s}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5):hover{opacity:.8}figcaption:where(.astro-hxyrieg5) a:where(.astro-hxyrieg5){text-decoration:underline}
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: vue; }@layer astro { ::view-transition-old(vue) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(vue) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(vue) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(vue) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-2"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-2"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-2"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-2"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-2"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: pwa; }@layer astro { ::view-transition-old(pwa) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(pwa) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(pwa) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(pwa) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-3"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-3"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-3"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-3"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-3"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-3"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-3"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-3"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: vite; }@layer astro { ::view-transition-old(vite) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(vite) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(vite) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(vite) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-4"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-4"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-4"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-4"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-4"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-4"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-4"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-4"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }</style></head> <body class="astro-sckkx6r4"> <div class="conference-wrapper border-b border-skin-line bg-skin-fill px-4 py-3 text-center text-skin-base astro-z2v4rtzb"><div class="mx-auto flex max-w-3xl flex-col items-center justify-center gap-3 sm:flex-row sm:gap-4 astro-z2v4rtzb"><div class="text-center sm:text-left astro-z2v4rtzb"><p class="text-lg font-semibold astro-z2v4rtzb"><span class="pulse-dot astro-z2v4rtzb"></span>
Next Talk: How to Build Local-First Apps with Vue</p><p class="text-sm opacity-80 astro-z2v4rtzb">March 12, 2026 — Vue.js Amsterdam</p></div><a href="https://vuejs.amsterdam/" class="conference-button inline-flex transform items-center justify-center gap-2 whitespace-nowrap rounded-md bg-skin-card px-4 py-2 font-medium text-skin-accent shadow transition-all duration-200 ease-in-out hover:scale-105 hover:bg-skin-card-muted hover:shadow-md astro-z2v4rtzb" target="_blank" rel="noopener noreferrer"><svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 astro-z2v4rtzb" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" class="astro-z2v4rtzb"></path><polyline points="15 3 21 3 21 9" class="astro-z2v4rtzb"></polyline><line x1="10" y1="14" x2="21" y2="3" class="astro-z2v4rtzb"></line></svg>
Conference
</a></div></div>  <header class="astro-3ef6ksr2"> <a id="skip-to-content" href="#main-content" class="astro-3ef6ksr2">Skip to content</a> <div class="nav-container astro-3ef6ksr2"> <div class="top-nav-wrap astro-3ef6ksr2"> <a href="/" class="logo whitespace-nowrap astro-3ef6ksr2"> alexop.dev </a> <nav id="nav-menu" aria-label="Main" class="astro-3ef6ksr2"> <button class="hamburger-menu focus-outline astro-3ef6ksr2" aria-label="Open Menu" aria-expanded="false" aria-controls="menu-items"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="menu-icon astro-3ef6ksr2"> <line x1="7" y1="12" x2="21" y2="12" class="line astro-3ef6ksr2"></line> <line x1="3" y1="6" x2="21" y2="6" class="line astro-3ef6ksr2"></line> <line x1="12" y1="18" x2="21" y2="18" class="line astro-3ef6ksr2"></line> <line x1="18" y1="6" x2="6" y2="18" class="close astro-3ef6ksr2"></line> <line x1="6" y1="6" x2="18" y2="18" class="close astro-3ef6ksr2"></line> </svg> </button> <ul id="menu-items" class="display-none sm:flex astro-3ef6ksr2"> <li class="astro-3ef6ksr2"> <a href="/posts/" class=" astro-3ef6ksr2">
📝 Posts
</a> </li> <li class="astro-3ef6ksr2"> <a href="/tils/" class=" astro-3ef6ksr2">
💡 TILs
</a> </li> <li class="astro-3ef6ksr2"> <a href="/notes/" class=" astro-3ef6ksr2">
📔 Notes
</a> </li> <li class="astro-3ef6ksr2"> <a href="/talks/" class=" astro-3ef6ksr2">
🎤 Talks
</a> </li> <li class="astro-3ef6ksr2"> <a href="/projects/" class=" astro-3ef6ksr2">
🚀 Projects
</a> </li> <li class="astro-3ef6ksr2"> <a href="/prompts/" class=" astro-3ef6ksr2">
🤖 Prompts
</a> </li> <li class="astro-3ef6ksr2"> <a href="/tags/" class=" astro-3ef6ksr2">
🏷️ Tags
</a> </li> <li class="astro-3ef6ksr2"> <a href="/about/" class=" astro-3ef6ksr2">
👤 About
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-base">Updated:</span><span class="italic text-base"><time dateTime="2024-12-30T22:00:00.000Z">Dec 30, 2024</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z1SIGQ" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite&quot;],&quot;content&quot;:[0,&quot;import ExcalidrawSVG from \&quot;@features/mdx-components/components/ExcalidrawSVG.astro\&quot;;\nimport Aside from \&quot;@features/mdx-components/components/Aside.astro\&quot;;\nimport myDiagram from \&quot;../../assets/images/test2.svg?raw\&quot;;\nimport fourSteps from \&quot;../../assets/images/pwa/4Steps.svg?raw\&quot;;\n\nimport CaptionedImage from \&quot;@features/mdx-components/components/CaptionedImage.astro\&quot;;\nimport pwaServisceWorker from \&quot;../../assets/images/pwa/pwa-servicer-worker.png\&quot;;\n\n## Table of Contents\n\n## Introduction\n\nProgressive Web Apps (PWAs) have revolutionized our thoughts on web applications. PWAs offer a fast, reliable, and engaging user experience by combining the best web and mobile apps. They work offline, can be installed on devices, and provide a native app-like experience without app store distribution.\n\nThis guide will walk you through creating a Progressive Web App using Vue 3 and Vite. By the end of this tutorial, you’ll have a fully functional PWA that can work offline, be installed on users’ devices, and leverage modern web capabilities.\n\n## Understanding the Basics of Progressive Web Apps (PWAs)\n\nBefore diving into the development process, it&#39;s crucial to grasp the fundamental concepts of PWAs:\n\n- **Multi-platform Compatibility**: PWAs are designed for applications that can function across multiple platforms, not just the web.\n- **Build Once, Deploy Everywhere**: With PWAs, you can develop an application once and deploy it on Android, iOS, Desktop, and Web platforms.\n- **Enhanced User Experience**: PWAs offer features like offline functionality, push notifications, and home screen installation.\n\nFor a more in-depth understanding of PWAs, refer to the [MDN Web Docs on Progressive Web Apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps).\n\n## Prerequisites for Building a PWA with Vue 3 and Vite\n\nBefore you start, make sure you have the following tools installed:\n\n1. Node.js installed on your system\n2. Package manager: pnpm, npm, or yarn\n3. Basic familiarity with Vue 3\n\n&lt;ExcalidrawSVG\n  src={fourSteps}\n  alt=\&quot;Four steps to create a PWA\&quot;\n  caption=\&quot;Four steps to create a PWA\&quot;\n/&gt;\n\n## Step 1: Setting Up the Vue Project\n\nFirst, we&#39;ll set up a new Vue project using the latest Vue CLI. This will give us a solid foundation to build our PWA upon.\n\n1. Create a new Vue project by running the following command in your terminal:\n\n   ```bash\n   pnpm create vue@latest\n   ```\n\n2. Follow the prompts to configure your project. Here&#39;s an example configuration:\n\n   ```shell\n   ✔ Project name: … local-first-example\n   ✔ Add TypeScript? … Yes\n   ✔ Add JSX Support? … Yes\n   ✔ Add Vue Router for Single Page Application development? … Yes\n   ✔ Add Pinia for state management? … Yes\n   ✔ Add Vitest for Unit Testing? … Yes\n   ✔ Add an End-to-End Testing Solution? › No\n   ✔ Add ESLint for code quality? … Yes\n   ✔ Add Prettier for code formatting? … Yes\n   ✔ Add Vue DevTools 7 extension for debugging? (experimental) … Yes\n   ```\n\n3. Once the project is created, navigate to your project directory and install dependencies:\n   ```bash\n   cd local-first-example\n   pnpm install\n   pnpm run dev\n   ```\n\nGreat! You now have a basic Vue 3 project up and running. Let&#39;s move on to adding PWA functionality.\n\n## Step 2: Create the needed assets for the PWA\n\nWe need to add specific assets and configurations to transform our Vue app into a PWA.\nPWAs can be installed on various devices, so we must prepare icons and other assets for different platforms.\n\n1. First, let&#39;s install the necessary packages:\n\n   ```bash\n   pnpm add -D vite-plugin-pwa @vite-pwa/assets-generator\n   ```\n\n2. Create a high-resolution icon (preferably an SVG or a PNG with at least 512x512 pixels) for your PWA and place it in your `public` directory. Name it something like `pwa-icon.svg` or `pwa-icon.png`.\n\n3. Generate the PWA assets by running:\n   ```bash\n   npx pwa-asset-generator --preset minimal public/pwa-icon.svg\n   ```\n\nThis command will automatically generate a set of icons and a web manifest file in your `public` directory. The `minimal` preset will create:\n\n- favicon.ico (48x48 transparent icon for browser tabs)\n- favicon.svg (SVG icon for modern browsers)\n- apple-touch-icon-180x180.png (Icon for iOS devices when adding to home screen)\n- maskable-icon-512x512.png (Adaptive icon that fills the entire shape on Android devices)\n- pwa-64x64.png (Small icon for various UI elements)\n- pwa-192x192.png (Medium-sized icon for app shortcuts and tiles)\n- pwa-512x512.png (Large icon for high-resolution displays and splash screens)\n\nOutput will look like this:\n\n```shell\n&gt; vue3-pwa-timer@0.0.0 generate-pwa-assets /Users/your user/git2/vue3-pwa-example\n&gt; pwa-assets-generator \&quot;--preset\&quot; \&quot;minimal-2023\&quot; \&quot;public/pwa-icon.svg\&quot;\n\nZero Config PWA Assets Generator v0.2.6\n◐ Preparing to generate PWA assets...\n◐ Resolving instructions...\n✔ PWA assets ready to be generated, instructions resolved\n◐ Generating PWA assets from public/pwa-icon.svg image\n◐ Generating assets for public/pwa-icon.svg...\n✔ Generated PNG file: /Users/your user/git2/vue3-pwa-example/public/pwa-64x64.png\n✔ Generated PNG file: /Users/your user/git2/vue3-pwa-example/public/pwa-192x192.png\n✔ Generated PNG file: /Users/your user/git2/vue3-pwa-example/public/pwa-512x512.png\n✔ Generated PNG file: /Users/your user/git2/vue3-pwa-example/public/maskable-icon-512x512.png\n✔ Generated PNG file: /Users/your user/git2/vue3-pwa-example/public/apple-touch-icon-180x180.png\n✔ Generated ICO file: /Users/your user/git2/vue3-pwa-example/public/favicon.ico\n✔ Assets generated for public/pwa-icon.svg\n◐ Generating Html Head Links...\n&lt;link rel=\&quot;icon\&quot; href=\&quot;/favicon.ico\&quot; sizes=\&quot;48x48\&quot;&gt;\n&lt;link rel=\&quot;icon\&quot; href=\&quot;/pwa-icon.svg\&quot; sizes=\&quot;any\&quot; type=\&quot;image/svg+xml\&quot;&gt;\n&lt;link rel=\&quot;apple-touch-icon\&quot; href=\&quot;/apple-touch-icon-180x180.png\&quot;&gt;\n✔ Html Head Links generated\n◐ Generating PWA web manifest icons entry...\n{\n  \&quot;icons\&quot;: [\n    {\n      \&quot;src\&quot;: \&quot;pwa-64x64.png\&quot;,\n      \&quot;sizes\&quot;: \&quot;64x64\&quot;,\n      \&quot;type\&quot;: \&quot;image/png\&quot;\n    },\n    {\n      \&quot;src\&quot;: \&quot;pwa-192x192.png\&quot;,\n      \&quot;sizes\&quot;: \&quot;192x192\&quot;,\n      \&quot;type\&quot;: \&quot;image/png\&quot;\n    },\n    {\n      \&quot;src\&quot;: \&quot;pwa-512x512.png\&quot;,\n      \&quot;sizes\&quot;: \&quot;512x512\&quot;,\n      \&quot;type\&quot;: \&quot;image/png\&quot;\n    },\n    {\n      \&quot;src\&quot;: \&quot;maskable-icon-512x512.png\&quot;,\n      \&quot;sizes\&quot;: \&quot;512x512\&quot;,\n      \&quot;type\&quot;: \&quot;image/png\&quot;,\n      \&quot;purpose\&quot;: \&quot;maskable\&quot;\n    }\n  ]\n}\n✔ PWA web manifest icons entry generated\n✔ PWA assets generated\n```\n\nThese steps will ensure your PWA has all the necessary icons and assets to function correctly across different devices and platforms.\nThe minimal-2023 preset provides a modern, optimized set of icons that meet the latest PWA requirements.\n\n## Step 3: Configuring Vite for PWA Support\n\nWith our assets ready, we must configure Vite to enable PWA functionality. This involves setting up the manifest and other PWA-specific options.\n\nFirst, update your main HTML file (usually `index.html`) to include important meta tags in the `&lt;head&gt;` section:\n\n```html\n&lt;head&gt;\n  &lt;meta charset=\&quot;UTF-8\&quot; /&gt;\n  &lt;meta name=\&quot;viewport\&quot; content=\&quot;width=device-width, initial-scale=1.0\&quot; /&gt;\n  &lt;meta name=\&quot;theme-color\&quot; content=\&quot;#ffffff\&quot; /&gt;\n  &lt;link rel=\&quot;icon\&quot; href=\&quot;/favicon.ico\&quot; sizes=\&quot;48x48\&quot; /&gt;\n  &lt;link rel=\&quot;icon\&quot; href=\&quot;/favicon.svg\&quot; sizes=\&quot;any\&quot; type=\&quot;image/svg+xml\&quot; /&gt;\n  &lt;link rel=\&quot;apple-touch-icon\&quot; href=\&quot;/apple-touch-icon-180x180.png\&quot; /&gt;\n&lt;/head&gt;\n```\n\nNow, update your `vite.config.ts` file with the following configuration:\n\n```typescript\nimport { fileURLToPath, URL } from \&quot;node:url\&quot;;\nimport { VitePWA } from \&quot;vite-plugin-pwa\&quot;;\nimport { defineConfig } from \&quot;vite\&quot;;\nimport vue from \&quot;@vitejs/plugin-vue\&quot;;\n\nexport default defineConfig({\n  plugins: [\n    vue(),\n    VitePWA({\n      registerType: \&quot;autoUpdate\&quot;,\n      includeAssets: [\n        \&quot;favicon.ico\&quot;,\n        \&quot;apple-touch-icon-180x180.png\&quot;,\n        \&quot;maskable-icon-512x512.png\&quot;,\n      ],\n      manifest: {\n        name: \&quot;My Awesome PWA\&quot;,\n        short_name: \&quot;MyPWA\&quot;,\n        description: \&quot;A PWA built with Vue 3\&quot;,\n        theme_color: \&quot;#ffffff\&quot;,\n        icons: [\n          {\n            src: \&quot;pwa-64x64.png\&quot;,\n            sizes: \&quot;64x64\&quot;,\n            type: \&quot;image/png\&quot;,\n          },\n          {\n            src: \&quot;pwa-192x192.png\&quot;,\n            sizes: \&quot;192x192\&quot;,\n            type: \&quot;image/png\&quot;,\n          },\n          {\n            src: \&quot;pwa-512x512.png\&quot;,\n            sizes: \&quot;512x512\&quot;,\n            type: \&quot;image/png\&quot;,\n            purpose: \&quot;any\&quot;,\n          },\n          {\n            src: \&quot;maskable-icon-512x512.png\&quot;,\n            sizes: \&quot;512x512\&quot;,\n            type: \&quot;image/png\&quot;,\n            purpose: \&quot;maskable\&quot;,\n          },\n        ],\n      },\n      devOptions: {\n        enabled: true,\n      },\n    }),\n  ],\n});\n```\n\n&lt;Aside type=\&quot;note\&quot;&gt;\n  The `devOptions: { enabled: true }` setting is crucial for testing your PWA on localhost. Normally, PWAs require HTTPS, but this setting allows the PWA features to work on `http://localhost` during development. Remember to remove or set this to `false` for production builds.\n&lt;/Aside&gt;\n\nThis configuration generates a Web App Manifest, a JSON file that tells the browser about your Progressive Web App and how it should behave when installed on the user’s desktop or mobile device. The manifest includes the app’s name, icons, and theme colors.\n\n## PWA Lifecycle and Updates\n\nThe `registerType: &#39;autoUpdate&#39;` option in our configuration sets up automatic updates for our PWA. Here&#39;s how it works:\n\n1. When a user visits your PWA, the browser downloads and caches the latest version of your app.\n2. On subsequent visits, the service worker checks for updates in the background.\n3. If an update is available, it&#39;s downloaded and prepared for the next launch.\n4. The next time the user opens or refreshes the app, they&#39;ll get the latest version.\n\nThis ensures that users always have the most up-to-date version of your app without manual intervention.\n\n## Step 4: Implementing Offline Functionality with Service Workers\n\nThe real power of PWAs comes from their ability to work offline. We&#39;ll use the `vite-plugin-pwa` to integrate Workbox, which will handle our service worker and caching strategies.\n\nBefore we dive into the configuration, let&#39;s understand the runtime caching strategies we&#39;ll be using:\n\n1. **StaleWhileRevalidate** for static resources (styles, scripts, and workers):\n   - This strategy serves cached content immediately while fetching an update in the background.\n   - It&#39;s ideal for frequently updated resources that aren&#39;t 100% up-to-date.\n   - We&#39;ll limit the cache to 50 entries and set an expiration of 30 days.\n\n2. **CacheFirst** for images:\n   - This strategy serves cached images immediately without network requests if they&#39;re available.\n   - It&#39;s perfect for static assets that don&#39;t change often.\n   - We&#39;ll limit the image cache to 100 entries and set an expiration of 60 days.\n\nThese strategies ensure that your PWA remains functional offline while efficiently managing cache storage.\n\nNow, let&#39;s update your `vite.config.ts` file to include service worker configuration with these advanced caching strategies:\n\n```typescript\nimport vue from \&quot;@vitejs/plugin-vue\&quot;;\nimport { defineConfig } from \&quot;vite\&quot;;\nimport { VitePWA } from \&quot;vite-plugin-pwa\&quot;;\n\nexport default defineConfig({\n  plugins: [\n    vue(),\n    VitePWA({\n      devOptions: {\n        enabled: true,\n      },\n      registerType: \&quot;autoUpdate\&quot;,\n      includeAssets: [\&quot;favicon.ico\&quot;, \&quot;apple-touch-icon.png\&quot;, \&quot;masked-icon.svg\&quot;],\n      manifest: {\n        name: \&quot;Vue 3 PWA Timer\&quot;,\n        short_name: \&quot;PWA Timer\&quot;,\n        description: \&quot;A customizable timer for Tabata and EMOM workouts\&quot;,\n        theme_color: \&quot;#ffffff\&quot;,\n        icons: [\n          {\n            src: \&quot;pwa-192x192.png\&quot;,\n            sizes: \&quot;192x192\&quot;,\n            type: \&quot;image/png\&quot;,\n          },\n          {\n            src: \&quot;pwa-512x512.png\&quot;,\n            sizes: \&quot;512x512\&quot;,\n            type: \&quot;image/png\&quot;,\n          },\n        ],\n      },\n      workbox: {\n        runtimeCaching: [\n          {\n            urlPattern: ({ request }) =&gt;\n              request.destination === \&quot;style\&quot; ||\n              request.destination === \&quot;script\&quot; ||\n              request.destination === \&quot;worker\&quot;,\n            handler: \&quot;StaleWhileRevalidate\&quot;,\n            options: {\n              cacheName: \&quot;static-resources\&quot;,\n              expiration: {\n                maxEntries: 50,\n                maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days\n              },\n            },\n          },\n          {\n            urlPattern: ({ request }) =&gt; request.destination === \&quot;image\&quot;,\n            handler: \&quot;CacheFirst\&quot;,\n            options: {\n              cacheName: \&quot;images\&quot;,\n              expiration: {\n                maxEntries: 100,\n                maxAgeSeconds: 60 * 24 * 60 * 60, // 60 days\n              },\n            },\n          },\n        ],\n      },\n    }),\n  ],\n});\n```\n\n&lt;ExcalidrawSVG\n  src={myDiagram}\n  alt=\&quot;Diagram explaining how PWAs use service workers to enable offline functionality\&quot;\n  caption=\&quot;How PWAs leverage service workers for offline functionality\&quot;\n/&gt;\n\n## Testing Your PWA\n\nNow that we&#39;ve set up our PWA, it&#39;s time to test its capabilities:\n\n1. Test your PWA locally:\n\n   ```bash\n   pnpm run dev\n   ```\n\n2. Open Chrome DevTools and navigate to the Application tab.\n   - Check the \&quot;Manifest\&quot; section to ensure your Web App Manifest is loaded correctly.\n   - In the \&quot;Service Workers\&quot; section, verify that your service worker is registered and active.\n     [![PWA Service Worker](../../assets/images/pwa/serviceWorker.png)\n\n3. Test offline functionality:\n   - Go to the Network tab in DevTools and check the \&quot;Offline\&quot; box to simulate offline conditions.\n   - Refresh the page and verify that your app still works without an internet connection.\n   - Uncheck the “Offline” box and refresh to ensure the app works online.\n\n4. Test caching:\n   - In the Application tab, go to \&quot;Cache Storage\&quot; to see the caches created by your service worker.\n   - Verify that assets are being cached according to your caching strategies.\n\n5. Test installation:\n   - On desktop: Look for the install icon in the address bar or the three-dot menu.\n     [![PWA Install Icon](../../assets/images/pwa/desktopInstall.png)](../../assets/images/pwa/desktopInstall.png)\n     [![PWA Install Icon](../../assets/images/pwa/installApp.png)](../../assets/images/pwa/installApp.png)\n\n   - On mobile: You should see a prompt to \&quot;Add to Home Screen\&quot;.\n\n6. Test updates:\n   - Make a small change to your app and redeploy.\n   - Revisit the app and check if the service worker updates (you can monitor this in the Application tab).\n\nBy thoroughly testing these aspects, you can ensure that your PWA functions correctly across various scenarios and platforms.\n\n&lt;Aside type=\&quot;info\&quot;&gt;\n  If you want to see a full-fledged PWA in action, check out\n  [Elk](https://elk.zone/), a nimble Mastodon web client. It&#39;s built with Nuxt\n  and is anexcellent example of a production-ready PWA. You can also explore its\n  open-source code on [GitHub](https://github.com/elk-zone/elk) to see how\n  they&#39;ve implemented various PWA features.\n&lt;/Aside&gt;\n\n## Conclusion\n\nCongratulations! You&#39;ve successfully created a Progressive Web App using Vue 3 and Vite.\nYour app can now work offline, be installed on users&#39; devices, and provide a native-like experience.\n\nRefer to the [Vite PWA Workbox documentation](https://vite-pwa-org.netlify.app/workbox/) for more advanced Workbox configurations and features.\n\nThe more challenging part is building suitable components with a native-like feel on all the devices you want to support.\nPWAs are also a main ingredient in building local-first applications.\nIf you are curious about what I mean by that, check out the following: [What is Local First Web Development](../what-is-local-first-web-development).\n\nFor a complete working example of this Vue 3 PWA, you can check out the complete source code at [full example](https://github.com/alexanderop/vue3-pwa-example).\nThis repository contains the finished project, allowing you to see how all the pieces come together in a real-world application.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div> <nav class="mb-8 astro-sbmhws2g" aria-labelledby="series-heading"> <div class="mb-1 text-sm font-bold tracking-wide text-skin-accent astro-sbmhws2g"> Local-First Web Development Series </div> <h2 id="series-heading" class="mb-2 text-xs font-semibold uppercase tracking-widest text-skin-accent astro-sbmhws2g">
This post is part of a series
</h2> <ol class="space-y-2 astro-sbmhws2g">  <li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 1.
</span> <a href="/posts/what-is-local-first-web-development/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> What is Local-first Web Development? </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> What is local-first software and why does it matter? This guide covers local-first architecture, offline-capable apps with automatic sync, data ownership, and how to build a local-first web app with Vue step by step. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all border-l-4 border-skin-accent bg-skin-card/60  astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-accent astro-sbmhws2g"> 2.
</span> <a href="/posts/create-pwa-vue3-vite-4-steps/" class="font-medium underline-offset-4 pointer-events-none text-skin-accent astro-sbmhws2g" aria-current="page"> Create a Native-Like App in 4 Steps: PWA Magic with Vue 3 and Vite </a> <span class="ml-2 text-xs font-bold text-green-400 astro-sbmhws2g">
(current)
</span> </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Transform your Vue 3 project into a powerful Progressive Web App in just 4 steps. Learn how to create offline-capable, installable web apps using Vite and modern PWA techniques. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 3.
</span> <a href="/posts/sqlite-vue3-offline-first-web-apps-guide/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> SQLite in Vue: Complete Guide to Building Offline-First Web Apps </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Learn how to build offline-capable Vue 3 apps using SQLite and WebAssembly in 2024. Step-by-step tutorial includes code examples for database operations, query playground implementation, and best practices for offline-first applications. </div> </li><li class="relative flex flex-col rounded py-2 pl-4 transition-all   astro-sbmhws2g"> <div class="flex items-center gap-2 astro-sbmhws2g"> <span class="font-mono text-xs text-skin-base/60 astro-sbmhws2g"> 4.
</span> <a href="/posts/building-local-first-apps-vue-dexie/" class="font-medium underline-offset-4 text-skin-accent/80 hover:underline astro-sbmhws2g"> Building Local-First Apps with Vue and Dexie.js </a>  </div> <div class="ml-6 mt-1 text-xs text-skin-base/70 astro-sbmhws2g"> Learn how to create offline-capable, local-first applications using Vue 3 and Dexie.js. Discover patterns for data persistence, synchronization, and optimal user experience. </div> </li> <li class="ml-4 text-xs text-skin-base/50 astro-sbmhws2g" aria-hidden="true">
…
</li> </ol> <div class="mt-4 border-b border-skin-line opacity-40 astro-sbmhws2g"></div> </nav>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="table-of-contents">Table of Contents<a class="heading-link" aria-label="Link to section" href="#table-of-contents"><span class="heading-link-icon">#</span></a></h2>
<p></p><details><summary>Open Table of Contents</summary><p></p>
<ul>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#understanding-the-basics-of-progressive-web-apps-pwas">Understanding the Basics of Progressive Web Apps (PWAs)</a></li>
<li><a href="#prerequisites-for-building-a-pwa-with-vue-3-and-vite">Prerequisites for Building a PWA with Vue 3 and Vite</a></li>
<li><a href="#step-1-setting-up-the-vue-project">Step 1: Setting Up the Vue Project</a></li>
<li><a href="#step-2-create-the-needed-assets-for-the-pwa">Step 2: Create the needed assets for the PWA</a></li>
<li><a href="#step-3-configuring-vite-for-pwa-support">Step 3: Configuring Vite for PWA Support</a></li>
<li><a href="#pwa-lifecycle-and-updates">PWA Lifecycle and Updates</a></li>
<li><a href="#step-4-implementing-offline-functionality-with-service-workers">Step 4: Implementing Offline Functionality with Service Workers</a></li>
<li><a href="#testing-your-pwa">Testing Your PWA</a></li>
<li><a href="#conclusion">Conclusion</a></li>
</ul>
<p></p></details><p></p>
<h2 id="introduction">Introduction<a class="heading-link" aria-label="Link to section" href="#introduction"><span class="heading-link-icon">#</span></a></h2>
<p>Progressive Web Apps (PWAs) have revolutionized our thoughts on web applications. PWAs offer a fast, reliable, and engaging user experience by combining the best web and mobile apps. They work offline, can be installed on devices, and provide a native app-like experience without app store distribution.</p>
<p>This guide will walk you through creating a Progressive Web App using Vue 3 and Vite. By the end of this tutorial, you’ll have a fully functional PWA that can work offline, be installed on users’ devices, and leverage modern web capabilities.</p>
<h2 id="understanding-the-basics-of-progressive-web-apps-pwas">Understanding the Basics of Progressive Web Apps (PWAs)<a class="heading-link" aria-label="Link to section" href="#understanding-the-basics-of-progressive-web-apps-pwas"><span class="heading-link-icon">#</span></a></h2>
<p>Before diving into the development process, it’s crucial to grasp the fundamental concepts of PWAs:</p>
<ul>
<li><strong>Multi-platform Compatibility</strong>: PWAs are designed for applications that can function across multiple platforms, not just the web.</li>
<li><strong>Build Once, Deploy Everywhere</strong>: With PWAs, you can develop an application once and deploy it on Android, iOS, Desktop, and Web platforms.</li>
<li><strong>Enhanced User Experience</strong>: PWAs offer features like offline functionality, push notifications, and home screen installation.</li>
</ul>
<p>For a more in-depth understanding of PWAs, refer to the <a href="https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps" rel="noopener noreferrer" target="_blank">MDN Web Docs on Progressive Web Apps</a>.</p>
<h2 id="prerequisites-for-building-a-pwa-with-vue-3-and-vite">Prerequisites for Building a PWA with Vue 3 and Vite<a class="heading-link" aria-label="Link to section" href="#prerequisites-for-building-a-pwa-with-vue-3-and-vite"><span class="heading-link-icon">#</span></a></h2>
<p>Before you start, make sure you have the following tools installed:</p>
<ol>
<li>Node.js installed on your system</li>
<li>Package manager: pnpm, npm, or yarn</li>
<li>Basic familiarity with Vue 3</li>
</ol>
<figure class="excalidraw-figure astro-hxyrieg5"> <div class="excalidraw-svg astro-hxyrieg5" role="img" aria-label="Four steps to create a PWA"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 265" width="100%" class="excalidraw-rendered" preserveAspectRatio="xMidYMid meet">
  <!-- svg-source:excalidraw -->
  
  <defs>
    <style class="style-fonts">
      @font-face {
        font-family: Excalifont;
        src: url(data:font/woff2;base64,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);
          }
    </style>
    
  <style>
  .ed-text { fill: var(--excalidraw-text, #222e36); }
  .ed-fill { fill: var(--excalidraw-fill, #eaced7); }
  .ed-accent-fill { fill: var(--excalidraw-accent, #d3006a); }
  .ed-accent-stroke { stroke: var(--excalidraw-accent, #d3006a); }
</style></defs>
  <g stroke-linecap="round" transform="translate(10 10) rotate(0 100 50)"><path d="M25 0 C65.96 -1.81, 100.81 0.66, 175 0 M25 0 C60.64 -1.25, 96.49 -0.76, 175 0 M175 0 C192.29 2.03, 200.29 5.64, 200 25 M175 0 C196.17 1.33, 198.05 10.24, 200 25 M200 25 C199.84 36.03, 202.46 50.67, 200 75 M200 25 C201.58 39.92, 200.66 57.41, 200 75 M200 75 C200.68 88.01, 187.71 101.26, 175 100 M200 75 C202.77 91.46, 196 103.51, 175 100 M175 100 C141.95 103.73, 115.84 98.24, 25 100 M175 100 C137.87 99.89, 99.86 98.93, 25 100 M25 100 C7.7 101.98, 2.35 88.46, 0 75 M25 100 C9.25 102.66, 3.58 88.5, 0 75 M0 75 C-3.36 60.51, 0.57 44.22, 0 25 M0 75 C-0.81 62.62, 2.13 48.7, 0 25 M0 25 C-2.83 4.65, 6.21 2.3, 25 0 M0 25 C-0.44 4.04, 6.62 -3.05, 25 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(44.930032044649124 47.5) rotate(0 65.06996795535088 12.5)"><text x="65.06996795535088" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">1. Set Up Vue</text></g><g stroke-linecap="round"><g transform="translate(110 110) rotate(0 0 30)"><path d="M0.99 0.64 C1.42 13.77, 0.55 32.08, 2.35 56.79 M-1.38 -0.1 C-0.03 19.55, -1.17 38.53, 0.11 59.37" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(110 110) rotate(0 0 30)"><path d="M16.36 0.73 C12.32 0.02, 8.22 1.29, 1.87 -0.56 M15.47 0.45 C10.92 0.79, 5.69 0.75, 1.03 0.4" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(110 110) rotate(0 0 30)"><path d="M-13.64 1.03 C-10.16 0.29, -6.73 1.48, 1.87 -0.56 M-14.53 0.75 C-9.48 0.76, -5.11 0.63, 1.03 0.4" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(110 110) rotate(0 0 30)"><path d="M-1.84 61.27 L-5.15 47.83 L3.98 47.38 L-0.84 58.7" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M0.48 59.61 C-1.64 55.52, -3.68 53.39, -5.81 44.79 M-0.41 59.33 C-2.42 55.27, -5.02 50.91, -6.65 45.76 M-7.29 46.64 C-2.04 46.28, -0.8 44.68, 5.3 46.29 M-7.11 45.76 C-2.82 46.02, 1.11 45.84, 6.47 45.63 M7.24 45.05 C4.73 50.01, 2.63 52.87, 0.18 59.2 M6.24 46.08 C3.6 49.34, 2.81 53.01, 0.28 59.05 M0.11 59.37 C0.11 59.37, 0.11 59.37, 0.11 59.37 M0.11 59.37 C0.11 59.37, 0.11 59.37, 0.11 59.37" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round" transform="translate(10 170) rotate(0 100 40)"><path d="M20 0 C79.01 0.87, 137.18 0.42, 180 0 M20 0 C68.57 -0.26, 116.75 2.04, 180 0 M180 0 C197.31 1, 197.17 2.99, 200 20 M180 0 C190.89 2.64, 199.56 2.37, 200 20 M200 20 C200.68 31.16, 202.27 41.33, 200 60 M200 20 C200.5 36.4, 201.77 49.55, 200 60 M200 60 C201.27 74.11, 193.67 77.43, 180 80 M200 60 C200.23 72.83, 192.87 79.37, 180 80 M180 80 C122.2 80.93, 72.79 79.14, 20 80 M180 80 C129.41 81.45, 74.68 84.12, 20 80 M20 80 C7.57 80.77, 2.53 71.6, 0 60 M20 80 C6.27 75.47, -0.65 75.74, 0 60 M0 60 C-2.87 50.09, 4.18 41.54, 0 20 M0 60 C1.66 52.19, 1.6 39.29, 0 20 M0 20 C3.64 4.78, 5.33 -3.03, 20 0 M0 20 C-3.44 5.7, 8.45 -3.4, 20 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(17.57006072998047 197.5) rotate(0 92.42993927001953 12.5)"><text x="92.42993927001953" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Create Vue Project</text></g><g stroke-linecap="round" transform="translate(250 10) rotate(0 100 50)"><path d="M25 0 C77.15 3.35, 138.92 -0.86, 175 0 M25 0 C85.24 3.82, 145.58 4.37, 175 0 M175 0 C192.24 -2.94, 197.23 9.24, 200 25 M175 0 C190.56 -1.38, 197.02 9.84, 200 25 M200 25 C198.69 34.22, 196.64 47.07, 200 75 M200 25 C198.89 41.21, 198.68 59.29, 200 75 M200 75 C202.54 91.86, 193.13 96.15, 175 100 M200 75 C197.46 92.13, 188.65 101.37, 175 100 M175 100 C134.46 105.69, 100.89 105.37, 25 100 M175 100 C119.5 98.66, 63.69 95.93, 25 100 M25 100 C4.6 99.68, 3.47 91.75, 0 75 M25 100 C7.72 96.83, -0.19 89.18, 0 75 M0 75 C3.78 64.21, 1.96 52.57, 0 25 M0 75 C0.18 57.53, 1.21 36.63, 0 25 M0 25 C1.29 5.62, 8.49 -3.82, 25 0 M0 25 C-2.15 11.54, 8 3.41, 25 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(266.00005462765694 47.5) rotate(0 83.99994537234306 12.5)"><text x="83.99994537234306" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">2. Create Assets</text></g><g stroke-linecap="round"><g transform="translate(350 110) rotate(0 0 30)"><path d="M3.89 0.23 C-2.44 21.18, 3.61 42.56, 3.96 60.58 M-0.48 -0.6 C-2.13 14.24, -1.78 25.71, 1.22 59.71" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(350 110) rotate(0 0 30)"><path d="M20.35 0.77 C12.72 0.9, 10.01 1.31, 5.38 0.45 M18.71 0.46 C15.01 0.86, 11.74 -0.04, 4.35 0.12" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(350 110) rotate(0 0 30)"><path d="M-9.64 -0.13 C-7.32 0.52, -0.07 1.22, 5.38 0.45 M-11.28 -0.44 C-8.19 0.09, -4.67 -0.6, 4.35 0.12" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(350 110) rotate(0 0 30)"><path d="M-0.62 61.66 L-6.3 47.68 L4.5 44.61 L2.23 61.4" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M2.68 59.8 C-2.51 55.81, -2.69 52.03, -4.69 46.88 M1.04 59.49 C-0.85 57.02, -2.4 53.26, -5.72 46.55 M-5.49 46.25 C-4.08 46.05, -1.68 45.7, 5.76 46.46 M-6.53 46.73 C-2.74 46.67, 1.23 46.02, 7.01 45.28 M7.5 44.64 C3.24 50.91, 3.56 55.89, 0.15 58.31 M6.36 45.14 C5.02 49.36, 3.14 53.7, 1.65 60.38 M1.22 59.71 C1.22 59.71, 1.22 59.71, 1.22 59.71 M1.22 59.71 C1.22 59.71, 1.22 59.71, 1.22 59.71" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round" transform="translate(250 170) rotate(0 100 40)"><path d="M20 0 C53.04 1.09, 95.32 2.57, 180 0 M20 0 C82.47 2.81, 147.23 1.75, 180 0 M180 0 C190.75 1.31, 198.1 3.71, 200 20 M180 0 C196.14 -0.66, 196.08 3.66, 200 20 M200 20 C198.45 27.25, 197.46 35.64, 200 60 M200 20 C201.24 27.87, 199.4 39.78, 200 60 M200 60 C197.38 74.53, 191.51 79.07, 180 80 M200 60 C203.98 70.6, 196.89 82.55, 180 80 M180 80 C117.39 77.6, 64.41 76.75, 20 80 M180 80 C145.18 79.79, 106.63 78.37, 20 80 M20 80 C6.5 77.84, -2.05 72.44, 0 60 M20 80 C9.29 84.09, 1.89 75.33, 0 60 M0 60 C1.62 46.87, 1.97 34.5, 0 20 M0 60 C-0.18 47.84, -1.19 40.88, 0 20 M0 20 C-0.29 9.63, 3.64 -0.64, 20 0 M0 20 C-1.33 9.17, 2.44 4.48, 20 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(259.46006774902344 185) rotate(0 90.53993225097656 25)"><text x="90.53993225097656" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Generate Icons &amp; </text><text x="90.53993225097656" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Manifest</text></g><g stroke-linecap="round" transform="translate(490 10) rotate(0 100 50)"><path d="M25 0 C80.24 2.13, 130.46 2.4, 175 0 M25 0 C66.53 1.83, 104.6 1.92, 175 0 M175 0 C193.58 3.01, 203.05 6.1, 200 25 M175 0 C188.47 1.15, 197.67 7.89, 200 25 M200 25 C197.52 38.31, 199.96 44.87, 200 75 M200 25 C202.06 44.8, 202.32 59.83, 200 75 M200 75 C199.87 90.01, 191.11 103.82, 175 100 M200 75 C201.16 90.27, 193.49 103.28, 175 100 M175 100 C127.1 97.65, 72.93 100.86, 25 100 M175 100 C128.27 101.7, 79.25 101.36, 25 100 M25 100 C8.26 102.62, 2.85 94.39, 0 75 M25 100 C11.65 100.66, -0.3 93.05, 0 75 M0 75 C0.05 62.92, 4.33 47.16, 0 25 M0 75 C0.66 63.57, 1.75 49.81, 0 25 M0 25 C-1.4 4.44, 4.5 3.5, 25 0 M0 25 C-0.15 4.16, 7.59 -2.39, 25 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(508.6100540161133 47.5) rotate(0 81.38994598388672 12.5)"><text x="81.38994598388672" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">3. Configure Vite</text></g><g stroke-linecap="round"><g transform="translate(590 111) rotate(0 0 29.5)"><path d="M-1.41 2.77 C-3.77 22.44, -2.03 37.95, -1.92 60.91 M-1.39 0.5 C-0.11 21.94, -0.98 46.06, -1.26 57.31" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(590 111) rotate(0 0 29.5)"><path d="M13.06 4.15 C7.37 4.4, 3.24 3.05, -2.13 3.48 M13.07 3.3 C7.58 2.82, 1.62 3.44, -1.88 2.13" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(590 111) rotate(0 0 29.5)"><path d="M-16.93 3.46 C-13.06 3.85, -7.62 2.72, -2.13 3.48 M-16.93 2.61 C-11.15 2.56, -5.85 3.43, -1.88 2.13" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(590 111) rotate(0 0 29.5)"><path d="M-1.58 56.37 L-6.76 45.32 L4.66 45.64 L0.59 55.94" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M-1.79 58.35 C-4.62 54.3, -5.88 48.68, -7.97 44.28 M-1.79 57.5 C-4 52.05, -6.57 47.63, -7.73 42.93 M-6.47 44.53 C-2.35 44.53, 3.35 44.82, 4.56 43.85 M-7.09 43.37 C-3.73 43.98, -0.5 43.12, 5.5 44.18 M5.76 45.04 C4.46 48.24, 2.5 50.88, -1.26 57.29 M5.96 44 C3.03 49.07, 0.25 53.22, -1.98 57.19 M-1.26 57.31 C-1.26 57.31, -1.26 57.31, -1.26 57.31 M-1.26 57.31 C-1.26 57.31, -1.26 57.31, -1.26 57.31" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round" transform="translate(490 170) rotate(0 100 42.5)"><path d="M21.25 0 C68.69 1.45, 121.71 -1.86, 178.75 0 M21.25 0 C62.49 -3.49, 99.28 -1.87, 178.75 0 M178.75 0 C190.89 -0.39, 196.23 10.66, 200 21.25 M178.75 0 C190.01 -3.88, 203.48 6.01, 200 21.25 M200 21.25 C200.98 35.85, 203.94 48.38, 200 63.75 M200 21.25 C199.69 33.04, 200.48 40.4, 200 63.75 M200 63.75 C201.58 80.77, 194.18 81.89, 178.75 85 M200 63.75 C200.57 80.04, 189.79 82.05, 178.75 85 M178.75 85 C131.35 90.7, 81.07 89.42, 21.25 85 M178.75 85 C132.87 88.42, 85.59 87.35, 21.25 85 M21.25 85 C6.83 86.2, -2.03 75.09, 0 63.75 M21.25 85 C2.7 84.25, 0.44 82.08, 0 63.75 M0 63.75 C0.24 54.77, 1.83 47.29, 0 21.25 M0 63.75 C-1.62 54.86, 0.23 40.66, 0 21.25 M0 21.25 C-0.64 5.01, 5.95 -2.84, 21.25 0 M0 21.25 C-1.74 11.24, 6.35 -2.17, 21.25 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(502.6200637817383 175) rotate(0 87.37993621826172 37.5)"><text x="87.37993621826172" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Update </text><text x="87.37993621826172" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">vite.config.ts for </text><text x="87.37993621826172" y="67.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">PWA support</text></g><g stroke-linecap="round" transform="translate(730 10) rotate(0 100 50)"><path d="M25 0 C85.65 1.35, 137.63 1.14, 175 0 M25 0 C73.39 -1.58, 121.71 1.52, 175 0 M175 0 C188.78 0.96, 203.23 12.02, 200 25 M175 0 C194.64 2.55, 197.89 9.5, 200 25 M200 25 C201.72 37.35, 200.39 43.82, 200 75 M200 25 C199.47 38.49, 201.02 51.95, 200 75 M200 75 C202.33 92.39, 189.87 98.69, 175 100 M200 75 C197.8 92.44, 194.47 97.49, 175 100 M175 100 C128.51 103.32, 76.83 102.5, 25 100 M175 100 C137.59 102.16, 99.72 103.5, 25 100 M25 100 C12.18 100.51, 0.33 94.37, 0 75 M25 100 C8.04 102.69, 3.75 93.98, 0 75 M0 75 C2.83 56.28, 3.32 36.53, 0 25 M0 75 C0.92 58.53, -1.11 44.98, 0 25 M0 25 C-2.52 10.63, 6.13 0.42, 25 0 M0 25 C-0.13 7.09, 9.31 -3.98, 25 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(755.5900497436523 35) rotate(0 74.40995025634766 25)"><text x="74.40995025634766" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">4. Implement </text><text x="74.40995025634766" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Offline Support</text></g><g stroke-linecap="round"><g transform="translate(830 110) rotate(0 0 30)"><path d="M0.67 -0.13 C-0.21 25.43, -3.1 50.72, 3.83 57.11 M1.29 1.11 C0.05 19.95, -0.86 39.69, -2 60.66" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(830 110) rotate(0 0 30)"><path d="M15.93 0.06 C9.95 0.8, 2.94 1.3, 2.11 -1.21 M16.16 0.53 C10.47 0.36, 5.26 0.4, -0.08 0.12" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(830 110) rotate(0 0 30)"><path d="M-14.07 -0.41 C-8.2 0.24, -3.36 0.93, 2.11 -1.21 M-13.84 0.05 C-9.8 -0.24, -5.29 -0.05, -0.08 0.12" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(830 110) rotate(0 0 30)"><path d="M-1.94 59.3 L-6.65 44.85 L3.97 49.39 L-0.39 60.3" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M-1.75 60.61 C-3.93 55.86, -7.24 50.95, -6.18 45.67 M-1.51 61.07 C-4.27 56.39, -6.44 52, -8.36 47 M-8.01 46.86 C-3.58 46.65, 1.24 47.87, 5.09 48.16 M-7.92 46.86 C-3.2 46.66, 0.56 46.68, 5.21 47.65 M4.38 46.26 C3.17 52.96, 0.33 58.13, -0.51 62.1 M5 47.86 C3.47 51.98, 1.18 55.35, -1.52 61.09 M-2 60.66 C-2 60.66, -2 60.66, -2 60.66 M-2 60.66 C-2 60.66, -2 60.66, -2 60.66" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round" transform="translate(730 170) rotate(0 100 40)"><path d="M20 0 C82.9 1.82, 142.39 3.4, 180 0 M20 0 C84.94 1.08, 147.93 0.34, 180 0 M180 0 C191.5 1.01, 196.33 8.28, 200 20 M180 0 C188.74 1.52, 202.23 6.65, 200 20 M200 20 C198.55 28.75, 199.84 41.84, 200 60 M200 20 C199.57 31.48, 199.51 44.6, 200 60 M200 60 C202.44 71.15, 194.12 76.59, 180 80 M200 60 C201.16 75.02, 196.28 77.4, 180 80 M180 80 C127.06 79.37, 71.36 80.3, 20 80 M180 80 C116.32 81.76, 52.18 81.58, 20 80 M20 80 C9.93 82.01, 2.84 71.19, 0 60 M20 80 C9.62 82.64, -0.19 76.53, 0 60 M0 60 C1.33 50.59, -1.64 35.9, 0 20 M0 60 C-0.6 45.42, 0.45 29.87, 0 20 M0 20 C0.85 3.21, 5.02 3.86, 20 0 M0 20 C4.5 8.95, 6.81 -3.12, 20 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(738.2500762939453 185) rotate(0 91.74992370605469 25)"><text x="91.74992370605469" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Add service worker</text><text x="91.74992370605469" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">&amp; Set up Caching</text></g><g stroke-linecap="round"><g transform="translate(210 70) rotate(0 0 0)"><path d="M0 0 C0 0, 0 0, 0 0 M0 0 C0 0, 0 0, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 70) rotate(0 0 0)"><path d="MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 70) rotate(0 0 0)"><path d="MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 70) rotate(0 0 0)"><path d="M-1.17 0.51 LNaN NaN LNaN NaN L0.88 0.5" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN M0 0 C0 0, 0 0, 0 0 M0 0 C0 0, 0 0, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round"><g transform="translate(210 70) rotate(0 0 0)"><path d="M0 0 C0 0, 0 0, 0 0 M0 0 C0 0, 0 0, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 70) rotate(0 0 0)"><path d="MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 70) rotate(0 0 0)"><path d="MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 70) rotate(0 0 0)"><path d="M0.21 -0.98 LNaN NaN LNaN NaN L-0.14 1" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN MNaN NaN CNaN NaN, NaN NaN, NaN NaN M0 0 C0 0, 0 0, 0 0 M0 0 C0 0, 0 0, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round"><g transform="translate(210 70) rotate(0 20 0)"><path d="M-1.8 -0.08 C9.99 0.95, 16.14 1.17, 41.22 1.42 M0.99 -0.3 C12.79 -0.68, 24.5 -0.89, 39.78 -0.85" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 70) rotate(0 20 0)"><path d="M-2.4 -15.11 C-0.39 -10.87, -2.54 -7.41, -0.89 0.99 M-0.3 -15.28 C-0.46 -11.06, -0.78 -6.79, -1.97 -0.71" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 70) rotate(0 20 0)"><path d="M-3.9 14.85 C-1.42 12.5, -3.24 9.37, -0.89 0.99 M-1.81 14.68 C-1.69 10.04, -1.56 5.45, -1.97 -0.71" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(210 70) rotate(0 20 0)"><path d="M38.47 -0.88 L26.45 4.56 L24.98 -8.96 L38.92 -2.76" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M38.43 -0.91 C37.66 1.52, 32.69 3.08, 27.11 6.58 M40.52 -1.08 C36.52 0.63, 32.41 2.36, 26.03 4.88 M25.71 4.92 C25.18 -0.13, 26.49 -4.78, 25.88 -7.35 M25.72 6.02 C26.33 1.89, 25.61 -0.9, 26.25 -6.68 M25.57 -8.66 C30.98 -4.66, 33.03 -4.5, 41.12 0.52 M26.66 -7.82 C31.36 -4.98, 35.93 -2.86, 39.46 -0.36 M39.78 -0.85 C39.78 -0.85, 39.78 -0.85, 39.78 -0.85 M39.78 -0.85 C39.78 -0.85, 39.78 -0.85, 39.78 -0.85" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round"><g transform="translate(450 70) rotate(0 20 0)"><path d="M-1.58 -0.45 C14.16 1.65, 30.43 -2.07, 39.24 -0.94 M-0.13 -0.23 C8.43 -0.71, 17.95 0.49, 39.24 0.8" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(450 70) rotate(0 20 0)"><path d="M-3.01 -15.78 C-3.09 -8.01, -2.69 -4.85, -2.16 -1.15 M-1.92 -15.62 C-1.95 -12.71, -1.2 -8.59, -2.15 0.15" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(450 70) rotate(0 20 0)"><path d="M-2.54 14.21 C-2.64 10.1, -2.42 1.35, -2.16 -1.15 M-1.45 14.38 C-1.44 10.85, -0.79 8.54, -2.15 0.15" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(450 70) rotate(0 20 0)"><path d="M38.85 0.55 L24.24 7.24 L26.08 -5.24 L39.9 -0.54" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M38.05 0.46 C32.47 4.77, 27.31 4.34, 24.91 6.05 M39.14 0.63 C36.15 1.63, 33.9 3.8, 24.91 7.36 M24.61 6.92 C26.68 2.18, 26.98 -0.79, 25.32 -7.18 M25.17 7.33 C26.11 2.5, 25.81 -3.12, 26.24 -6.47 M25.12 -6.54 C31.34 -3.07, 35.47 -1.72, 40.42 1.91 M25.28 -5.47 C30.81 -3.62, 34.65 -1.39, 39.8 1.33 M39.24 0.8 C39.24 0.8, 39.24 0.8, 39.24 0.8 M39.24 0.8 C39.24 0.8, 39.24 0.8, 39.24 0.8" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/><g stroke-linecap="round"><g transform="translate(690 70) rotate(0 20 0)"><path d="M1.13 -1.51 C13 0.45, 20.81 -1.8, 38.64 0.25 M0.81 -0.4 C14.01 0.3, 30.59 -0.85, 39.52 0.9" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(690 70) rotate(0 20 0)"><path d="M2.51 -17.64 C2.61 -11.65, -0.23 -9.07, 0.1 -1.33 M2.27 -16.8 C0.68 -10.38, 1.66 -5.62, 0.77 -0.84" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(690 70) rotate(0 20 0)"><path d="M1.43 12.34 C2.04 9.78, -0.5 3.82, 0.1 -1.33 M1.19 13.18 C0.08 8.34, 1.46 1.85, 0.77 -0.84" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(690 70) rotate(0 20 0)"><path d="M38.99 -0.76 L23.79 4.14 L26.28 -8.54 L39.38 -0.93" stroke="none" stroke-width="0" fill-rule="evenodd" class="ed-fill"/><path d="M40.36 -0.24 C36.66 3.02, 29.95 2.77, 24.37 6.13 M40.13 0.6 C33.46 3.41, 29.34 4.44, 25.03 6.61 M24.19 6.77 C24.67 1.49, 25.89 -3.98, 25.97 -7.21 M25.24 6.44 C26.25 1.6, 25.71 -3.21, 26.11 -6.3 M26.42 -5.56 C32.23 -3.42, 35.07 -2.55, 39.23 0.93 M26.67 -7.04 C31.15 -4.39, 36.34 -1.46, 39.26 1.01 M39.52 0.9 C39.52 0.9, 39.52 0.9, 39.52 0.9 M39.52 0.9 C39.52 0.9, 39.52 0.9, 39.52 0.9" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask/></svg></div> <figcaption class="astro-hxyrieg5">Four steps to create a PWA</figcaption> </figure> <script type="module">function n(i){const t=new DOMParser().parseFromString(i,"image/svg+xml"),o=t.documentElement;o.removeAttribute("filter"),t.querySelectorAll("[filter]").forEach(e=>e.removeAttribute("filter")),o.classList.add("excalidraw-rendered"),o.setAttribute("width","100%"),o.removeAttribute("height"),o.setAttribute("preserveAspectRatio","xMidYMid meet"),o.getAttribute("viewBox")||o.setAttribute("viewBox","0 0 800 600"),t.querySelectorAll("text").forEach(e=>{const r=e.getAttribute("y");if(!r||r==="NaN"||isNaN(parseFloat(r))){const c=parseFloat(e.getAttribute("font-size")||"16");e.setAttribute("y",String(Math.round(c*.85)))}});const a={"#222e36":"var(--excalidraw-text)","#eaced7":"var(--excalidraw-fill)","#d3006a":"var(--excalidraw-accent)"};return t.querySelectorAll("[fill]").forEach(e=>{const r=e.getAttribute("fill")?.toLowerCase();r&&a[r]&&e.setAttribute("fill",a[r])}),t.querySelectorAll("[stroke]").forEach(e=>{const r=e.getAttribute("stroke")?.toLowerCase();r&&a[r]&&e.setAttribute("stroke",a[r])}),new XMLSerializer().serializeToString(t)}function l(){document.querySelectorAll(".excalidraw-svg[data-svg-url]").forEach(async i=>{const s=i.dataset.svgUrl;if(s)try{const t=await fetch(s);if(!t.ok)throw new Error(`Failed to fetch SVG: ${t.statusText}`);i.innerHTML=n(await t.text())}catch(t){console.error("Error in ExcalidrawSVG component:",t)}})}document.addEventListener("DOMContentLoaded",l);document.addEventListener("astro:page-load",l);</script> 
<h2 id="step-1-setting-up-the-vue-project">Step 1: Setting Up the Vue Project<a class="heading-link" aria-label="Link to section" href="#step-1-setting-up-the-vue-project"><span class="heading-link-icon">#</span></a></h2>
<p>First, we’ll set up a new Vue project using the latest Vue CLI. This will give us a solid foundation to build our PWA upon.</p>
<ol>
<li>
<p>Create a new Vue project by running the following command in your terminal:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">pnpm</span><span style="color:#9ECE6A"> create</span><span style="color:#9ECE6A"> vue@latest</span></span></code><button type="button" class="copy" data-code="pnpm create vue@latest" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
<li>
<p>Follow the prompts to configure your project. Here’s an example configuration:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="shell"><code><span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Project</span><span style="color:#9ECE6A"> name:</span><span style="color:#9ECE6A"> …</span><span style="color:#9ECE6A"> local-first-example</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Add</span><span style="color:#9ECE6A"> TypeScript?</span><span style="color:#9ECE6A"> …</span><span style="color:#9ECE6A"> Yes</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Add</span><span style="color:#9ECE6A"> JSX</span><span style="color:#9ECE6A"> Support?</span><span style="color:#9ECE6A"> …</span><span style="color:#9ECE6A"> Yes</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Add</span><span style="color:#9ECE6A"> Vue</span><span style="color:#9ECE6A"> Router</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> Single</span><span style="color:#9ECE6A"> Page</span><span style="color:#9ECE6A"> Application</span><span style="color:#9ECE6A"> development?</span><span style="color:#9ECE6A"> …</span><span style="color:#9ECE6A"> Yes</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Add</span><span style="color:#9ECE6A"> Pinia</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> state</span><span style="color:#9ECE6A"> management?</span><span style="color:#9ECE6A"> …</span><span style="color:#9ECE6A"> Yes</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Add</span><span style="color:#9ECE6A"> Vitest</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> Unit</span><span style="color:#9ECE6A"> Testing?</span><span style="color:#9ECE6A"> …</span><span style="color:#9ECE6A"> Yes</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Add</span><span style="color:#9ECE6A"> an</span><span style="color:#9ECE6A"> End-to-End</span><span style="color:#9ECE6A"> Testing</span><span style="color:#9ECE6A"> Solution?</span><span style="color:#9ECE6A"> ›</span><span style="color:#9ECE6A"> No</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Add</span><span style="color:#9ECE6A"> ESLint</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> code</span><span style="color:#9ECE6A"> quality?</span><span style="color:#9ECE6A"> …</span><span style="color:#9ECE6A"> Yes</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Add</span><span style="color:#9ECE6A"> Prettier</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> code</span><span style="color:#9ECE6A"> formatting?</span><span style="color:#9ECE6A"> …</span><span style="color:#9ECE6A"> Yes</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Add</span><span style="color:#9ECE6A"> Vue</span><span style="color:#9ECE6A"> DevTools</span><span style="color:#FF9E64"> 7</span><span style="color:#9ECE6A"> extension</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> debugging?</span><span style="color:#A9B1D6"> (experimental) … Yes</span></span></code><button type="button" class="copy" data-code="✔ Project name: … local-first-example
✔ Add TypeScript? … Yes
✔ Add JSX Support? … Yes
✔ Add Vue Router for Single Page Application development? … Yes
✔ Add Pinia for state management? … Yes
✔ Add Vitest for Unit Testing? … Yes
✔ Add an End-to-End Testing Solution? › No
✔ Add ESLint for code quality? … Yes
✔ Add Prettier for code formatting? … Yes
✔ Add Vue DevTools 7 extension for debugging? (experimental) … Yes" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
<li>
<p>Once the project is created, navigate to your project directory and install dependencies:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#0DB9D7">cd</span><span style="color:#9ECE6A"> local-first-example</span></span>
<span class="line"><span style="color:#C0CAF5">pnpm</span><span style="color:#9ECE6A"> install</span></span>
<span class="line"><span style="color:#C0CAF5">pnpm</span><span style="color:#9ECE6A"> run</span><span style="color:#9ECE6A"> dev</span></span></code><button type="button" class="copy" data-code="cd local-first-example
pnpm install
pnpm run dev" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
</ol>
<p>Great! You now have a basic Vue 3 project up and running. Let’s move on to adding PWA functionality.</p>
<h2 id="step-2-create-the-needed-assets-for-the-pwa">Step 2: Create the needed assets for the PWA<a class="heading-link" aria-label="Link to section" href="#step-2-create-the-needed-assets-for-the-pwa"><span class="heading-link-icon">#</span></a></h2>
<p>We need to add specific assets and configurations to transform our Vue app into a PWA.
PWAs can be installed on various devices, so we must prepare icons and other assets for different platforms.</p>
<ol>
<li>
<p>First, let’s install the necessary packages:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">pnpm</span><span style="color:#9ECE6A"> add</span><span style="color:#E0AF68"> -D</span><span style="color:#9ECE6A"> vite-plugin-pwa</span><span style="color:#9ECE6A"> @vite-pwa/assets-generator</span></span></code><button type="button" class="copy" data-code="pnpm add -D vite-plugin-pwa @vite-pwa/assets-generator" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
<li>
<p>Create a high-resolution icon (preferably an SVG or a PNG with at least 512x512 pixels) for your PWA and place it in your <code>public</code> directory. Name it something like <code>pwa-icon.svg</code> or <code>pwa-icon.png</code>.</p>
</li>
<li>
<p>Generate the PWA assets by running:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">npx</span><span style="color:#9ECE6A"> pwa-asset-generator</span><span style="color:#E0AF68"> --preset</span><span style="color:#9ECE6A"> minimal</span><span style="color:#9ECE6A"> public/pwa-icon.svg</span></span></code><button type="button" class="copy" data-code="npx pwa-asset-generator --preset minimal public/pwa-icon.svg" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
</ol>
<p>This command will automatically generate a set of icons and a web manifest file in your <code>public</code> directory. The <code>minimal</code> preset will create:</p>
<ul>
<li>favicon.ico (48x48 transparent icon for browser tabs)</li>
<li>favicon.svg (SVG icon for modern browsers)</li>
<li>apple-touch-icon-180x180.png (Icon for iOS devices when adding to home screen)</li>
<li>maskable-icon-512x512.png (Adaptive icon that fills the entire shape on Android devices)</li>
<li>pwa-64x64.png (Small icon for various UI elements)</li>
<li>pwa-192x192.png (Medium-sized icon for app shortcuts and tiles)</li>
<li>pwa-512x512.png (Large icon for high-resolution displays and splash screens)</li>
</ul>
<p>Output will look like this:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="shell"><code><span class="line"><span style="color:#89DDFF">&gt;</span><span style="color:#A9B1D6"> vue3-pwa-timer@0.0.0 generate-pwa-assets /Users/your user/git2/vue3-pwa-example</span></span>
<span class="line"><span style="color:#89DDFF">&gt;</span><span style="color:#A9B1D6"> pwa-assets-generator </span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">--preset</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">minimal-2023</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">public/pwa-icon.svg</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">Zero</span><span style="color:#9ECE6A"> Config</span><span style="color:#9ECE6A"> PWA</span><span style="color:#9ECE6A"> Assets</span><span style="color:#9ECE6A"> Generator</span><span style="color:#9ECE6A"> v0.2.6</span></span>
<span class="line"><span style="color:#C0CAF5">◐</span><span style="color:#9ECE6A"> Preparing</span><span style="color:#9ECE6A"> to</span><span style="color:#9ECE6A"> generate</span><span style="color:#9ECE6A"> PWA</span><span style="color:#9ECE6A"> assets...</span></span>
<span class="line"><span style="color:#C0CAF5">◐</span><span style="color:#9ECE6A"> Resolving</span><span style="color:#9ECE6A"> instructions...</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> PWA</span><span style="color:#9ECE6A"> assets</span><span style="color:#9ECE6A"> ready</span><span style="color:#9ECE6A"> to</span><span style="color:#9ECE6A"> be</span><span style="color:#9ECE6A"> generated,</span><span style="color:#9ECE6A"> instructions</span><span style="color:#9ECE6A"> resolved</span></span>
<span class="line"><span style="color:#C0CAF5">◐</span><span style="color:#9ECE6A"> Generating</span><span style="color:#9ECE6A"> PWA</span><span style="color:#9ECE6A"> assets</span><span style="color:#9ECE6A"> from</span><span style="color:#9ECE6A"> public/pwa-icon.svg</span><span style="color:#9ECE6A"> image</span></span>
<span class="line"><span style="color:#C0CAF5">◐</span><span style="color:#9ECE6A"> Generating</span><span style="color:#9ECE6A"> assets</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> public/pwa-icon.svg...</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Generated</span><span style="color:#9ECE6A"> PNG</span><span style="color:#9ECE6A"> file:</span><span style="color:#9ECE6A"> /Users/your</span><span style="color:#9ECE6A"> user/git2/vue3-pwa-example/public/pwa-64x64.png</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Generated</span><span style="color:#9ECE6A"> PNG</span><span style="color:#9ECE6A"> file:</span><span style="color:#9ECE6A"> /Users/your</span><span style="color:#9ECE6A"> user/git2/vue3-pwa-example/public/pwa-192x192.png</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Generated</span><span style="color:#9ECE6A"> PNG</span><span style="color:#9ECE6A"> file:</span><span style="color:#9ECE6A"> /Users/your</span><span style="color:#9ECE6A"> user/git2/vue3-pwa-example/public/pwa-512x512.png</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Generated</span><span style="color:#9ECE6A"> PNG</span><span style="color:#9ECE6A"> file:</span><span style="color:#9ECE6A"> /Users/your</span><span style="color:#9ECE6A"> user/git2/vue3-pwa-example/public/maskable-icon-512x512.png</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Generated</span><span style="color:#9ECE6A"> PNG</span><span style="color:#9ECE6A"> file:</span><span style="color:#9ECE6A"> /Users/your</span><span style="color:#9ECE6A"> user/git2/vue3-pwa-example/public/apple-touch-icon-180x180.png</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Generated</span><span style="color:#9ECE6A"> ICO</span><span style="color:#9ECE6A"> file:</span><span style="color:#9ECE6A"> /Users/your</span><span style="color:#9ECE6A"> user/git2/vue3-pwa-example/public/favicon.ico</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Assets</span><span style="color:#9ECE6A"> generated</span><span style="color:#9ECE6A"> for</span><span style="color:#9ECE6A"> public/pwa-icon.svg</span></span>
<span class="line"><span style="color:#C0CAF5">◐</span><span style="color:#9ECE6A"> Generating</span><span style="color:#9ECE6A"> Html</span><span style="color:#9ECE6A"> Head</span><span style="color:#9ECE6A"> Links...</span></span>
<span class="line"><span style="color:#89DDFF">&lt;</span><span style="color:#A9B1D6">link </span><span style="color:#C0CAF5">rel</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">icon</span><span style="color:#89DDFF">&quot;</span><span style="color:#C0CAF5"> href</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">/favicon.ico</span><span style="color:#89DDFF">&quot;</span><span style="color:#C0CAF5"> sizes</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">48x48</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">&gt;</span></span>
<span class="line"><span style="color:#89DDFF">&lt;</span><span style="color:#A9B1D6">link </span><span style="color:#C0CAF5">rel</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">icon</span><span style="color:#89DDFF">&quot;</span><span style="color:#C0CAF5"> href</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">/pwa-icon.svg</span><span style="color:#89DDFF">&quot;</span><span style="color:#C0CAF5"> sizes</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">any</span><span style="color:#89DDFF">&quot;</span><span style="color:#C0CAF5"> type</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">image/svg+xml</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">&gt;</span></span>
<span class="line"><span style="color:#89DDFF">&lt;</span><span style="color:#A9B1D6">link </span><span style="color:#C0CAF5">rel</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">apple-touch-icon</span><span style="color:#89DDFF">&quot;</span><span style="color:#C0CAF5"> href</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">/apple-touch-icon-180x180.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">&gt;</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> Html</span><span style="color:#9ECE6A"> Head</span><span style="color:#9ECE6A"> Links</span><span style="color:#9ECE6A"> generated</span></span>
<span class="line"><span style="color:#C0CAF5">◐</span><span style="color:#9ECE6A"> Generating</span><span style="color:#9ECE6A"> PWA</span><span style="color:#9ECE6A"> web</span><span style="color:#9ECE6A"> manifest</span><span style="color:#9ECE6A"> icons</span><span style="color:#9ECE6A"> entry...</span></span>
<span class="line"><span style="color:#9ABDF5">{</span></span>
<span class="line"><span style="color:#C0CAF5">  &quot;icons&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#A9B1D6"> [</span></span>
<span class="line"><span style="color:#9ABDF5">    {</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;src&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pwa-64x64.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;sizes&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">64x64</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;type&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/png</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#A9B1D6">,</span></span>
<span class="line"><span style="color:#9ABDF5">    {</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;src&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pwa-192x192.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;sizes&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">192x192</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;type&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/png</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#A9B1D6">,</span></span>
<span class="line"><span style="color:#9ABDF5">    {</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;src&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pwa-512x512.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;sizes&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">512x512</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;type&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/png</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span><span style="color:#A9B1D6">,</span></span>
<span class="line"><span style="color:#9ABDF5">    {</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;src&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">maskable-icon-512x512.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;sizes&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">512x512</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;type&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/png</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">,</span></span>
<span class="line"><span style="color:#C0CAF5">      &quot;purpose&quot;</span><span style="color:#0DB9D7">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">maskable</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#A9B1D6">  ]</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> PWA</span><span style="color:#9ECE6A"> web</span><span style="color:#9ECE6A"> manifest</span><span style="color:#9ECE6A"> icons</span><span style="color:#9ECE6A"> entry</span><span style="color:#9ECE6A"> generated</span></span>
<span class="line"><span style="color:#C0CAF5">✔</span><span style="color:#9ECE6A"> PWA</span><span style="color:#9ECE6A"> assets</span><span style="color:#9ECE6A"> generated</span></span></code><button type="button" class="copy" data-code="> vue3-pwa-timer@0.0.0 generate-pwa-assets /Users/your user/git2/vue3-pwa-example
> pwa-assets-generator &#34;--preset&#34; &#34;minimal-2023&#34; &#34;public/pwa-icon.svg&#34;

Zero Config PWA Assets Generator v0.2.6
◐ Preparing to generate PWA assets...
◐ Resolving instructions...
✔ PWA assets ready to be generated, instructions resolved
◐ Generating PWA assets from public/pwa-icon.svg image
◐ Generating assets for public/pwa-icon.svg...
✔ Generated PNG file: /Users/your user/git2/vue3-pwa-example/public/pwa-64x64.png
✔ Generated PNG file: /Users/your user/git2/vue3-pwa-example/public/pwa-192x192.png
✔ Generated PNG file: /Users/your user/git2/vue3-pwa-example/public/pwa-512x512.png
✔ Generated PNG file: /Users/your user/git2/vue3-pwa-example/public/maskable-icon-512x512.png
✔ Generated PNG file: /Users/your user/git2/vue3-pwa-example/public/apple-touch-icon-180x180.png
✔ Generated ICO file: /Users/your user/git2/vue3-pwa-example/public/favicon.ico
✔ Assets generated for public/pwa-icon.svg
◐ Generating Html Head Links...
<link rel=&#34;icon&#34; href=&#34;/favicon.ico&#34; sizes=&#34;48x48&#34;>
<link rel=&#34;icon&#34; href=&#34;/pwa-icon.svg&#34; sizes=&#34;any&#34; type=&#34;image/svg+xml&#34;>
<link rel=&#34;apple-touch-icon&#34; href=&#34;/apple-touch-icon-180x180.png&#34;>
✔ Html Head Links generated
◐ Generating PWA web manifest icons entry...
{
  &#34;icons&#34;: [
    {
      &#34;src&#34;: &#34;pwa-64x64.png&#34;,
      &#34;sizes&#34;: &#34;64x64&#34;,
      &#34;type&#34;: &#34;image/png&#34;
    },
    {
      &#34;src&#34;: &#34;pwa-192x192.png&#34;,
      &#34;sizes&#34;: &#34;192x192&#34;,
      &#34;type&#34;: &#34;image/png&#34;
    },
    {
      &#34;src&#34;: &#34;pwa-512x512.png&#34;,
      &#34;sizes&#34;: &#34;512x512&#34;,
      &#34;type&#34;: &#34;image/png&#34;
    },
    {
      &#34;src&#34;: &#34;maskable-icon-512x512.png&#34;,
      &#34;sizes&#34;: &#34;512x512&#34;,
      &#34;type&#34;: &#34;image/png&#34;,
      &#34;purpose&#34;: &#34;maskable&#34;
    }
  ]
}
✔ PWA web manifest icons entry generated
✔ PWA assets generated" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>These steps will ensure your PWA has all the necessary icons and assets to function correctly across different devices and platforms.
The minimal-2023 preset provides a modern, optimized set of icons that meet the latest PWA requirements.</p>
<h2 id="step-3-configuring-vite-for-pwa-support">Step 3: Configuring Vite for PWA Support<a class="heading-link" aria-label="Link to section" href="#step-3-configuring-vite-for-pwa-support"><span class="heading-link-icon">#</span></a></h2>
<p>With our assets ready, we must configure Vite to enable PWA functionality. This involves setting up the manifest and other PWA-specific options.</p>
<p>First, update your main HTML file (usually <code>index.html</code>) to include important meta tags in the <code>&lt;head&gt;</code> section:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="html"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">head</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">meta</span><span style="color:#BB9AF7"> charset</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">UTF-8</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">meta</span><span style="color:#BB9AF7"> name</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">viewport</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> content</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">width=device-width, initial-scale=1.0</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">meta</span><span style="color:#BB9AF7"> name</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">theme-color</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> content</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">#ffffff</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">link</span><span style="color:#BB9AF7"> rel</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">icon</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> href</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">/favicon.ico</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> sizes</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">48x48</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">link</span><span style="color:#BB9AF7"> rel</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">icon</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> href</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">/favicon.svg</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> sizes</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">any</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> type</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">image/svg+xml</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">link</span><span style="color:#BB9AF7"> rel</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">apple-touch-icon</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> href</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">/apple-touch-icon-180x180.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#BA3C97"> /&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">head</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<head>
  <meta charset=&#34;UTF-8&#34; />
  <meta name=&#34;viewport&#34; content=&#34;width=device-width, initial-scale=1.0&#34; />
  <meta name=&#34;theme-color&#34; content=&#34;#ffffff&#34; />
  <link rel=&#34;icon&#34; href=&#34;/favicon.ico&#34; sizes=&#34;48x48&#34; />
  <link rel=&#34;icon&#34; href=&#34;/favicon.svg&#34; sizes=&#34;any&#34; type=&#34;image/svg+xml&#34; />
  <link rel=&#34;apple-touch-icon&#34; href=&#34;/apple-touch-icon-180x180.png&#34; />
</head>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Now, update your <code>vite.config.ts</code> file with the following configuration:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">fileURLToPath</span><span style="color:#89DDFF">,</span><span style="color:#0DB9D7"> URL</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">node:url</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">VitePWA</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vite-plugin-pwa</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">defineConfig</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vite</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> vue</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@vitejs/plugin-vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#7DCFFF"> default</span><span style="color:#7AA2F7"> defineConfig</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">  plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#7AA2F7">    vue</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">    VitePWA</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">      registerType</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">autoUpdate</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      includeAssets</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#9ECE6A">favicon.ico</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#9ECE6A">apple-touch-icon-180x180.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#89DDFF">        &quot;</span><span style="color:#9ECE6A">maskable-icon-512x512.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      manifest</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">        name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">My Awesome PWA</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">        short_name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">MyPWA</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">        description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">A PWA built with Vue 3</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">        theme_color</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">#ffffff</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">        icons</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#41A6B5">            src</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pwa-64x64.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            sizes</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">64x64</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#41A6B5">            src</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pwa-192x192.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            sizes</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">192x192</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#41A6B5">            src</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pwa-512x512.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            sizes</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">512x512</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            purpose</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">any</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#41A6B5">            src</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">maskable-icon-512x512.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            sizes</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">512x512</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            purpose</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">maskable</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      devOptions</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">        enabled</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import { fileURLToPath, URL } from &#34;node:url&#34;;
import { VitePWA } from &#34;vite-plugin-pwa&#34;;
import { defineConfig } from &#34;vite&#34;;
import vue from &#34;@vitejs/plugin-vue&#34;;

export default defineConfig({
  plugins: [
    vue(),
    VitePWA({
      registerType: &#34;autoUpdate&#34;,
      includeAssets: [
        &#34;favicon.ico&#34;,
        &#34;apple-touch-icon-180x180.png&#34;,
        &#34;maskable-icon-512x512.png&#34;,
      ],
      manifest: {
        name: &#34;My Awesome PWA&#34;,
        short_name: &#34;MyPWA&#34;,
        description: &#34;A PWA built with Vue 3&#34;,
        theme_color: &#34;#ffffff&#34;,
        icons: [
          {
            src: &#34;pwa-64x64.png&#34;,
            sizes: &#34;64x64&#34;,
            type: &#34;image/png&#34;,
          },
          {
            src: &#34;pwa-192x192.png&#34;,
            sizes: &#34;192x192&#34;,
            type: &#34;image/png&#34;,
          },
          {
            src: &#34;pwa-512x512.png&#34;,
            sizes: &#34;512x512&#34;,
            type: &#34;image/png&#34;,
            purpose: &#34;any&#34;,
          },
          {
            src: &#34;maskable-icon-512x512.png&#34;,
            sizes: &#34;512x512&#34;,
            type: &#34;image/png&#34;,
            purpose: &#34;maskable&#34;,
          },
        ],
      },
      devOptions: {
        enabled: true,
      },
    }),
  ],
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<aside aria-label="Note" class="aside aside-note astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">📝</span> Note </p> <section class="aside-body astro-37uy2q7c"> <p>The <code>devOptions: { enabled: true }</code> setting is crucial for testing your PWA on localhost. Normally, PWAs require HTTPS, but this setting allows the PWA features to work on <code>http://localhost</code> during development. Remember to remove or set this to <code>false</code> for production builds.</p> </section> </div> </aside> 
<p>This configuration generates a Web App Manifest, a JSON file that tells the browser about your Progressive Web App and how it should behave when installed on the user’s desktop or mobile device. The manifest includes the app’s name, icons, and theme colors.</p>
<h2 id="pwa-lifecycle-and-updates">PWA Lifecycle and Updates<a class="heading-link" aria-label="Link to section" href="#pwa-lifecycle-and-updates"><span class="heading-link-icon">#</span></a></h2>
<p>The <code>registerType: &#39;autoUpdate&#39;</code> option in our configuration sets up automatic updates for our PWA. Here’s how it works:</p>
<ol>
<li>When a user visits your PWA, the browser downloads and caches the latest version of your app.</li>
<li>On subsequent visits, the service worker checks for updates in the background.</li>
<li>If an update is available, it’s downloaded and prepared for the next launch.</li>
<li>The next time the user opens or refreshes the app, they’ll get the latest version.</li>
</ol>
<p>This ensures that users always have the most up-to-date version of your app without manual intervention.</p>
<h2 id="step-4-implementing-offline-functionality-with-service-workers">Step 4: Implementing Offline Functionality with Service Workers<a class="heading-link" aria-label="Link to section" href="#step-4-implementing-offline-functionality-with-service-workers"><span class="heading-link-icon">#</span></a></h2>
<p>The real power of PWAs comes from their ability to work offline. We’ll use the <code>vite-plugin-pwa</code> to integrate Workbox, which will handle our service worker and caching strategies.</p>
<p>Before we dive into the configuration, let’s understand the runtime caching strategies we’ll be using:</p>
<ol>
<li>
<p><strong>StaleWhileRevalidate</strong> for static resources (styles, scripts, and workers):</p>
<ul>
<li>This strategy serves cached content immediately while fetching an update in the background.</li>
<li>It’s ideal for frequently updated resources that aren’t 100% up-to-date.</li>
<li>We’ll limit the cache to 50 entries and set an expiration of 30 days.</li>
</ul>
</li>
<li>
<p><strong>CacheFirst</strong> for images:</p>
<ul>
<li>This strategy serves cached images immediately without network requests if they’re available.</li>
<li>It’s perfect for static assets that don’t change often.</li>
<li>We’ll limit the image cache to 100 entries and set an expiration of 60 days.</li>
</ul>
</li>
</ol>
<p>These strategies ensure that your PWA remains functional offline while efficiently managing cache storage.</p>
<p>Now, let’s update your <code>vite.config.ts</code> file to include service worker configuration with these advanced caching strategies:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="typescript"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> vue</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">@vitejs/plugin-vue</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">defineConfig</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vite</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">VitePWA</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">vite-plugin-pwa</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#7DCFFF"> default</span><span style="color:#7AA2F7"> defineConfig</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">  plugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#7AA2F7">    vue</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#7AA2F7">    VitePWA</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">      devOptions</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">        enabled</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      registerType</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">autoUpdate</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      includeAssets</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">favicon.ico</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">apple-touch-icon.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">masked-icon.svg</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      manifest</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">        name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Vue 3 PWA Timer</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">        short_name</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">PWA Timer</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">        description</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">A customizable timer for Tabata and EMOM workouts</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">        theme_color</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">#ffffff</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">        icons</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#41A6B5">            src</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pwa-192x192.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            sizes</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">192x192</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#41A6B5">            src</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">pwa-512x512.png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            sizes</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">512x512</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            type</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image/png</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      workbox</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">        runtimeCaching</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#7AA2F7">            urlPattern</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#89DDFF">{</span><span style="color:#E0AF68"> request</span><span style="color:#89DDFF"> }</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span></span>
<span class="line"><span style="color:#C0CAF5">              request</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">destination</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">style</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#C0CAF5">              request</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">destination</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">script</span><span style="color:#89DDFF">&quot;</span><span style="color:#BB9AF7"> ||</span></span>
<span class="line"><span style="color:#C0CAF5">              request</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">destination</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">worker</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            handler</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">StaleWhileRevalidate</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            options</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">              cacheName</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">static-resources</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">              expiration</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">                maxEntries</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 50</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">                maxAgeSeconds</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 30</span><span style="color:#89DDFF"> *</span><span style="color:#FF9E64"> 24</span><span style="color:#89DDFF"> *</span><span style="color:#FF9E64"> 60</span><span style="color:#89DDFF"> *</span><span style="color:#FF9E64"> 60</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic"> // 30 days</span></span>
<span class="line"><span style="color:#9ABDF5">              }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">            }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          {</span></span>
<span class="line"><span style="color:#7AA2F7">            urlPattern</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> (</span><span style="color:#89DDFF">{</span><span style="color:#E0AF68"> request</span><span style="color:#89DDFF"> }</span><span style="color:#9ABDF5">)</span><span style="color:#BB9AF7"> =&gt;</span><span style="color:#C0CAF5"> request</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">destination</span><span style="color:#BB9AF7"> ===</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">image</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            handler</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">CacheFirst</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">            options</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">              cacheName</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">images</span><span style="color:#89DDFF">&quot;</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">              expiration</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#41A6B5">                maxEntries</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 100</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#41A6B5">                maxAgeSeconds</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 60</span><span style="color:#89DDFF"> *</span><span style="color:#FF9E64"> 24</span><span style="color:#89DDFF"> *</span><span style="color:#FF9E64"> 60</span><span style="color:#89DDFF"> *</span><span style="color:#FF9E64"> 60</span><span style="color:#89DDFF">,</span><span style="color:#51597D;font-style:italic"> // 60 days</span></span>
<span class="line"><span style="color:#9ABDF5">              }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">            }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">          }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">        ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">      }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import vue from &#34;@vitejs/plugin-vue&#34;;
import { defineConfig } from &#34;vite&#34;;
import { VitePWA } from &#34;vite-plugin-pwa&#34;;

export default defineConfig({
  plugins: [
    vue(),
    VitePWA({
      devOptions: {
        enabled: true,
      },
      registerType: &#34;autoUpdate&#34;,
      includeAssets: [&#34;favicon.ico&#34;, &#34;apple-touch-icon.png&#34;, &#34;masked-icon.svg&#34;],
      manifest: {
        name: &#34;Vue 3 PWA Timer&#34;,
        short_name: &#34;PWA Timer&#34;,
        description: &#34;A customizable timer for Tabata and EMOM workouts&#34;,
        theme_color: &#34;#ffffff&#34;,
        icons: [
          {
            src: &#34;pwa-192x192.png&#34;,
            sizes: &#34;192x192&#34;,
            type: &#34;image/png&#34;,
          },
          {
            src: &#34;pwa-512x512.png&#34;,
            sizes: &#34;512x512&#34;,
            type: &#34;image/png&#34;,
          },
        ],
      },
      workbox: {
        runtimeCaching: [
          {
            urlPattern: ({ request }) =>
              request.destination === &#34;style&#34; ||
              request.destination === &#34;script&#34; ||
              request.destination === &#34;worker&#34;,
            handler: &#34;StaleWhileRevalidate&#34;,
            options: {
              cacheName: &#34;static-resources&#34;,
              expiration: {
                maxEntries: 50,
                maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
              },
            },
          },
          {
            urlPattern: ({ request }) => request.destination === &#34;image&#34;,
            handler: &#34;CacheFirst&#34;,
            options: {
              cacheName: &#34;images&#34;,
              expiration: {
                maxEntries: 100,
                maxAgeSeconds: 60 * 24 * 60 * 60, // 60 days
              },
            },
          },
        ],
      },
    }),
  ],
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<figure class="excalidraw-figure astro-hxyrieg5"> <div class="excalidraw-svg astro-hxyrieg5" role="img" aria-label="Diagram explaining how PWAs use service workers to enable offline functionality"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950.1015625 246.13671875" width="100%" class="excalidraw-rendered" preserveAspectRatio="xMidYMid meet">
  <!-- svg-source:excalidraw -->
  
  <defs>
    <style class="style-fonts">
      @font-face {
        font-family: Excalifont;
        src: url(data:font/woff2;base64,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);
          }
    </style>
    
  <style>
  .ed-text { fill: var(--excalidraw-text, #222e36); }
  .ed-fill { fill: var(--excalidraw-fill, #eaced7); }
  .ed-accent-fill { fill: var(--excalidraw-accent, #d3006a); }
  .ed-accent-stroke { stroke: var(--excalidraw-accent, #d3006a); }
</style></defs>
  <g stroke-linecap="round" transform="translate(10 101.1081897081267) rotate(0 36.8984375 21.960169666873753)"><path d="M10.98 0 C31.37 1.16, 52.19 0.99, 62.82 0 M10.98 0 C24.78 -0.28, 38.96 0.2, 62.82 0 M62.82 0 C68.49 -0.61, 71.87 2.49, 73.8 10.98 M62.82 0 C71.37 1.37, 71.95 5.77, 73.8 10.98 M73.8 10.98 C75.2 13.79, 72.01 18.34, 73.8 32.94 M73.8 10.98 C74.08 19.19, 73.28 28.05, 73.8 32.94 M73.8 32.94 C73.72 41.4, 69.6 44.62, 62.82 43.92 M73.8 32.94 C74.72 39.06, 72.09 42.7, 62.82 43.92 M62.82 43.92 C51.83 45.63, 40.69 42.19, 10.98 43.92 M62.82 43.92 C48.24 44.67, 33.1 43.93, 10.98 43.92 M10.98 43.92 C1.79 43.89, 0.61 40.72, 0 32.94 M10.98 43.92 C5.94 42.74, 0.53 40.79, 0 32.94 M0 32.94 C1.64 25.98, 1.82 15.29, 0 10.98 M0 32.94 C0.55 28.07, -0.48 24.04, 0 10.98 M0 10.98 C1.44 3.2, 2.16 0.62, 10.98 0 M0 10.98 C1.58 2.94, 1.92 1.02, 10.98 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(26.288446068763733 110.568359375) rotate(0 20.609991431236267 12.5)"><text x="20.609991431236267" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">PWA</text></g><g stroke-linecap="round" transform="translate(265.671875 10) rotate(0 113.2734375 113.068359375)"><path d="M114 0 C149.23 35.68, 183.11 68.64, 226.55 114 M114 0 C156.93 43.97, 198.94 86.55, 226.55 114 M226.55 114 C204.15 135.85, 181.86 158.51, 114 226.14 M226.55 114 C203.41 137.15, 180.25 161.66, 114 226.14 M114 226.14 C83.38 194.29, 53.09 163.86, 0 114 M114 226.14 C74 185.98, 33.74 145.92, 0 114 M0 114 C24.28 90.62, 48.64 62.77, 114 0 M0 114 C32.17 81.61, 64.74 48.08, 114 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(340.9986267089844 98.0341796875) rotate(0 37.809967041015625 25)"><text x="37.809967041015625" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Service </text><text x="37.809967041015625" y="42.62" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Worker</text></g><g stroke-linecap="round" transform="translate(802.140625 52.19690272281696) rotate(0 54.25 21.960169666873753)"><path d="M0 0 C38.51 -1.89, 79.9 -0.83, 108.5 0 M0 0 C33.34 -0.98, 67.36 -1.26, 108.5 0 M108.5 0 C110.6 13.74, 106.87 32.64, 108.5 43.92 M108.5 0 C107.16 17.4, 107.89 32.56, 108.5 43.92 M108.5 43.92 C74.15 43.34, 37.44 42.87, 0 43.92 M108.5 43.92 C72.99 42.82, 34.93 43.56, 0 43.92 M0 43.92 C0.04 26.97, -0.27 15.6, 0 0 M0 43.92 C-0.04 29.73, -1.08 15.72, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(815.9706649780273 61.657072389690256) rotate(0 40.419960021972656 12.5)"><text x="40.419960021972656" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Backend</text></g><g stroke-linecap="round" transform="translate(772.6796875 150.01947669343554) rotate(0 83.7109375 21.960169666873753)"><path d="M0 0 C60.56 0.85, 118.15 1.36, 167.42 0 M0 0 C59.77 -0.07, 122 1.11, 167.42 0 M167.42 0 C165.93 11.22, 169.43 17.48, 167.42 43.92 M167.42 0 C166.8 8.85, 167.34 19.53, 167.42 43.92 M167.42 43.92 C126.15 43.32, 83.29 44.65, 0 43.92 M167.42 43.92 C125.06 43.23, 84.83 43.08, 0 43.92 M0 43.92 C-0.26 29.15, 0.4 11.69, 0 0 M0 43.92 C-0.98 27.92, 0.25 12.18, 0 0" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(792.2406768798828 159.47964636030883) rotate(0 64.14994812011719 12.5)"><text x="64.14994812011719" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">Offline Cache</text></g><g mask="url(#mask-kGXc6l0EZUpsODE8ld6Ex)" stroke-linecap="round"><g transform="translate(84.29700000000048 116.50881926339662) rotate(0 94.1244999999999 -8.94827004448598)"><path d="M-0.16 0.18 C15.07 -2.84, 59.35 -16.02, 90.59 -17.14 C121.82 -18.27, 171.18 -8.28, 187.26 -6.57 M-1.7 -0.77 C13.46 -4.22, 57.83 -18.09, 89.72 -18.87 C121.61 -19.65, 173.47 -7.56, 189.64 -5.44" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(84.29700000000048 116.50881926339662) rotate(0 94.1244999999999 -8.94827004448598)"><path d="M165.02 -1.08 C171.03 -1.82, 177.74 -4.73, 189.64 -5.44 M165.02 -1.08 C172.24 -1.52, 177.53 -2.37, 189.64 -5.44" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(84.29700000000048 116.50881926339662) rotate(0 94.1244999999999 -8.94827004448598)"><path d="M167.98 -17.93 C173.43 -14.73, 179.45 -13.71, 189.64 -5.44 M167.98 -17.93 C174.23 -13.84, 178.73 -10.15, 189.64 -5.44" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-kGXc6l0EZUpsODE8ld6Ex"><rect x="0" y="0" fill="#fff" width="372.5460000000005" height="234.40535935236827"/><rect x="123.79403570556678" y="86.11227917442466" fill="#000" width="101.87992858886719" height="25" opacity="1"/></mask><g transform="translate(123.79403570556678 86.11227917442466) rotate(0 54.47237041493008 21.032158202254323)"><text x="50.939964294433594" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">1. Request</text></g><g mask="url(#mask-2lNE8wwrpQO0Dksw5A0YI)" stroke-linecap="round"><g transform="translate(467.759 98.65220675563796) rotate(0 164.30650000000014 -24.47560728326107)"><path d="M0.15 0.75 C27.46 -7.5, 109.15 -43.82, 163.7 -49.32 C218.25 -54.81, 299.87 -35.28, 327.46 -32.19 M-1.23 0.1 C26.46 -7.99, 110.73 -42.75, 165.9 -47.97 C221.06 -53.2, 302.42 -33.75, 329.75 -31.25" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(467.759 98.65220675563796) rotate(0 164.30650000000014 -24.47560728326107)"><path d="M305.23 -26.37 C313.51 -29.45, 318.68 -31.12, 329.75 -31.25 M305.23 -26.37 C310.32 -26.78, 316.15 -29.82, 329.75 -31.25" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(467.759 98.65220675563796) rotate(0 164.30650000000014 -24.47560728326107)"><path d="M307.83 -43.27 C315.39 -41.5, 319.82 -38.32, 329.75 -31.25 M307.83 -43.27 C312.39 -39.58, 317.59 -38.54, 329.75 -31.25" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-2lNE8wwrpQO0Dksw5A0YI"><rect x="0" y="0" fill="#fff" width="896.372" height="247.6034213221598"/><rect x="584.6990241100784" y="37.20099218911582" fill="#000" width="95.49995177984238" height="25" opacity="1"/></mask><g transform="translate(584.6990241100784 37.20099218911582) rotate(0 47.318332609372646 36.685570463915155)"><text x="47.74997588992119" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">2a. Online</text></g><g mask="url(#mask-fc75vKaR74Ls-nHsQI4HY)" stroke-linecap="round"><g transform="translate(483.2359999999999 134.031038278501) rotate(0 141.8375000000001 13.866349860335049)"><path d="M-0.99 -0.36 C23.66 1.64, 100.51 7.99, 148.06 12.79 C195.61 17.59, 261.88 25.77, 284.32 28.45 M0.7 -1.6 C25.68 0.48, 102.96 9.28, 150.16 13.96 C197.36 18.64, 261.84 24.33, 283.89 26.48" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(483.2359999999999 134.031038278501) rotate(0 141.8375000000001 13.866349860335049)"><path d="M259.71 32.81 C266.62 29.11, 273.62 30.13, 283.89 26.48 M259.71 32.81 C267.56 29.37, 277.94 28.84, 283.89 26.48" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(483.2359999999999 134.031038278501) rotate(0 141.8375000000001 13.866349860335049)"><path d="M261.29 15.79 C267.82 17.39, 274.32 23.73, 283.89 26.48 M261.29 15.79 C268.44 18.48, 278.25 24.08, 283.89 26.48" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-fc75vKaR74Ls-nHsQI4HY"><rect x="0" y="0" fill="#fff" width="866.9109999999998" height="261.7637379991714"/><rect x="581.1390265514847" y="135.0235661597344" fill="#000" width="102.61994689702988" height="25" opacity="1"/></mask><g transform="translate(581.1390265514847 135.0235661597344) rotate(0 43.76287094157942 12.430604790064535)"><text x="51.30997344851494" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">2b. Offline</text></g><g mask="url(#mask-5lIJDljAvuoMjbIRetXTF)" stroke-linecap="round"><g transform="translate(801.6409999999996 80.58098349886222) rotate(0 -156.56550000000016 15.997484507552144)"><path d="M-1.15 -0.7 C-29.08 2.48, -116.39 13.11, -168.55 18.75 C-220.7 24.38, -289.82 31.08, -314.1 33.1 M0.44 1.55 C-27.5 4.42, -117.13 12.04, -169.16 17 C-221.18 21.96, -287.48 28.94, -311.71 31.33" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(801.6409999999996 80.58098349886222) rotate(0 -156.56550000000016 15.997484507552144)"><path d="M-289.2 20.45 C-295.3 23.68, -297.84 23.36, -311.71 31.33 M-289.2 20.45 C-297.33 25.3, -307.84 27.97, -311.71 31.33" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(801.6409999999996 80.58098349886222) rotate(0 -156.56550000000016 15.997484507552144)"><path d="M-287.47 37.46 C-293.9 36.97, -296.81 32.95, -311.71 31.33 M-287.47 37.46 C-296.12 35.64, -307.31 31.64, -311.71 31.33" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-5lIJDljAvuoMjbIRetXTF"><rect x="0" y="0" fill="#fff" width="1214.7719999999995" height="212.5759525139667"/><rect x="535.9990717163082" y="86.11227917442648" fill="#000" width="192.8998565673828" height="25" opacity="1"/></mask><g transform="translate(535.9990717163082 86.11227917442648) rotate(0 108.81394963417279 10.666080776217768)"><text x="96.4499282836914" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">3a. Online Response</text></g><g mask="url(#mask-cb9I3oLRAoVfUs-biHxG1)" stroke-linecap="round"><g transform="translate(772.1800000000003 180.62253279536526) rotate(0 -149.66399999999976 -6.9334244775504885)"><path d="M0.64 0.72 C-22.61 3.65, -90.52 22.17, -140.7 16.91 C-190.87 11.66, -274.12 -23.21, -300.4 -30.81 M-0.48 0.05 C-23.26 2.73, -88.89 20.39, -138.49 15.37 C-188.09 10.35, -271.55 -22.4, -298.07 -30.09" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(772.1800000000003 180.62253279536526) rotate(0 -149.66399999999976 -6.9334244775504885)"><path d="M-273.08 -30.78 C-276.99 -32.11, -281.44 -32.16, -298.07 -30.09 M-273.08 -30.78 C-279.12 -31.23, -284.28 -29.61, -298.07 -30.09" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(772.1800000000003 180.62253279536526) rotate(0 -149.66399999999976 -6.9334244775504885)"><path d="M-278.49 -14.55 C-281.2 -19.22, -284.55 -22.57, -298.07 -30.09 M-278.49 -14.55 C-283.54 -18.38, -287.6 -20.09, -298.07 -30.09" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-cb9I3oLRAoVfUs-biHxG1"><rect x="0" y="0" fill="#fff" width="1171.5080000000003" height="326.1140224498242"/><rect x="532.4390741577154" y="183.93485314504414" fill="#000" width="200.0198516845703" height="25" opacity="1"/></mask><g transform="translate(532.4390741577154 183.93485314504414) rotate(0 89.86096574944213 -9.796224106053614)"><text x="100.00992584228516" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">3b. Offline Response</text></g><g mask="url(#mask-8HSb_w8UMy4crdAHed-IZ)" stroke-linecap="round"><g transform="translate(277.8060000000005 135.1809526174211) rotate(0 -94.15200000000004 4.3920339333749325)"><path d="M-0.96 1.1 C-18.43 2.85, -73.08 11.82, -104.15 11.21 C-135.21 10.59, -173.15 0.03, -187.36 -2.59 M0.73 0.63 C-16.43 2.42, -70.61 12.99, -102 12.15 C-133.39 11.31, -173.01 -1.75, -187.63 -4.43" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(277.8060000000005 135.1809526174211) rotate(0 -94.15200000000004 4.3920339333749325)"><path d="M-162.78 -7.21 C-169.72 -8.22, -182.23 -3.87, -187.63 -4.43 M-162.78 -7.21 C-173.2 -5.66, -181.92 -6.15, -187.63 -4.43" stroke-width="2" fill="none" class="ed-accent-stroke"/></g><g transform="translate(277.8060000000005 135.1809526174211) rotate(0 -94.15200000000004 4.3920339333749325)"><path d="M-166.81 9.41 C-172.42 2.55, -183.51 1.03, -187.63 -4.43 M-166.81 9.41 C-175.54 4.67, -182.73 -2.14, -187.63 -4.43" stroke-width="2" fill="none" class="ed-accent-stroke"/></g></g><mask id="mask-8HSb_w8UMy4crdAHed-IZ"><rect x="0" y="0" fill="#fff" width="566.1100000000005" height="251.08211183529818"/><rect x="116.42403906846084" y="135.0235661597344" fill="#000" width="116.61992186307907" height="25" opacity="1"/></mask><g transform="translate(116.42403906846084 135.0235661597344) rotate(0 67.9324864866312 4.04122103347845)"><text x="58.309960931539536" y="17.619999999999997" font-family="Excalifont, Segoe UI Emoji" font-size="20px" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic" class="ed-text">4. Response</text></g></svg></div> <figcaption class="astro-hxyrieg5">How PWAs leverage service workers for offline functionality</figcaption> </figure>  
<h2 id="testing-your-pwa">Testing Your PWA<a class="heading-link" aria-label="Link to section" href="#testing-your-pwa"><span class="heading-link-icon">#</span></a></h2>
<p>Now that we’ve set up our PWA, it’s time to test its capabilities:</p>
<ol>
<li>
<p>Test your PWA locally:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">pnpm</span><span style="color:#9ECE6A"> run</span><span style="color:#9ECE6A"> dev</span></span></code><button type="button" class="copy" data-code="pnpm run dev" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
</li>
<li>
<p>Open Chrome DevTools and navigate to the Application tab.</p>
<ul>
<li>Check the “Manifest” section to ensure your Web App Manifest is loaded correctly.</li>
<li>In the “Service Workers” section, verify that your service worker is registered and active.
[<img src="/_astro/serviceWorker.D4bn4NZe_33Jdg.webp" alt="PWA Service Worker" loading="lazy" decoding="async" fetchpriority="auto" width="1800" height="1342"></li>
</ul>
</li>
<li>
<p>Test offline functionality:</p>
<ul>
<li>Go to the Network tab in DevTools and check the “Offline” box to simulate offline conditions.</li>
<li>Refresh the page and verify that your app still works without an internet connection.</li>
<li>Uncheck the “Offline” box and refresh to ensure the app works online.</li>
</ul>
</li>
<li>
<p>Test caching:</p>
<ul>
<li>In the Application tab, go to “Cache Storage” to see the caches created by your service worker.</li>
<li>Verify that assets are being cached according to your caching strategies.</li>
</ul>
</li>
<li>
<p>Test installation:</p>
<ul>
<li>
<p>On desktop: Look for the install icon in the address bar or the three-dot menu.
<a href="../../assets/images/pwa/desktopInstall.png"><img src="/_astro/desktopInstall.DEGe9pES_Z1PdTur.webp" alt="PWA Install Icon" loading="lazy" decoding="async" fetchpriority="auto" width="2500" height="94"></a>
<a href="../../assets/images/pwa/installApp.png"><img src="/_astro/installApp.Kfwlj6rv_Z1zuBlG.webp" alt="PWA Install Icon" loading="lazy" decoding="async" fetchpriority="auto" width="872" height="330"></a></p>
</li>
<li>
<p>On mobile: You should see a prompt to “Add to Home Screen”.</p>
</li>
</ul>
</li>
<li>
<p>Test updates:</p>
<ul>
<li>Make a small change to your app and redeploy.</li>
<li>Revisit the app and check if the service worker updates (you can monitor this in the Application tab).</li>
</ul>
</li>
</ol>
<p>By thoroughly testing these aspects, you can ensure that your PWA functions correctly across various scenarios and platforms.</p>
<aside aria-label="Info" class="aside aside-info astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">ℹ️</span> Info </p> <section class="aside-body astro-37uy2q7c"> <p>If you want to see a full-fledged PWA in action, check out
<a target="_blank" rel="noopener noreferrer" href="https://elk.zone/" rel="noopener noreferrer" target="_blank">Elk</a>, a nimble Mastodon web client. It’s built with Nuxt
and is anexcellent example of a production-ready PWA. You can also explore its
open-source code on <a target="_blank" rel="noopener noreferrer" href="https://github.com/elk-zone/elk" rel="noopener noreferrer" target="_blank">GitHub</a> to see how
they’ve implemented various PWA features.</p> </section> </div> </aside> 
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<p>Congratulations! You’ve successfully created a Progressive Web App using Vue 3 and Vite.
Your app can now work offline, be installed on users’ devices, and provide a native-like experience.</p>
<p>Refer to the <a href="https://vite-pwa-org.netlify.app/workbox/" rel="noopener noreferrer" target="_blank">Vite PWA Workbox documentation</a> for more advanced Workbox configurations and features.</p>
<p>The more challenging part is building suitable components with a native-like feel on all the devices you want to support.
PWAs are also a main ingredient in building local-first applications.
If you are curious about what I mean by that, check out the following: <a href="../what-is-local-first-web-development">What is Local First Web Development</a>.</p>
<p>For a complete working example of this Vue 3 PWA, you can check out the complete source code at <a href="https://github.com/alexanderop/vue3-pwa-example" rel="noopener noreferrer" target="_blank">full example</a>.
This repository contains the finished project, allowing you to see how all the pieces come together in a real-world application.</p> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 3 21 3 21 9"></polyline>
          <polyline points="9 21 3 21 3 15"></polyline>
          <line x1="21" y1="3" x2="14" y2="10"></line>
          <line x1="3" y1="21" x2="10" y2="14"></line>
        </svg>
        <span>Fullscreen</span>
      `,n.appendChild(o);const d=m=>{m.stopPropagation(),c.innerHTML="";const i=t.cloneNode(!0),s=t.id,w=`-modal-${Date.now()}`,u=`${s}${w}`;i.setAttribute("id",u);const E=new Map;i.querySelectorAll("[id]").forEach(l=>{if(l===i)return;const a=l.getAttribute("id"),h=a+w;E.set(a,h),l.setAttribute("id",h)});let r=i.innerHTML;E.forEach((l,a)=>{r=r.replace(new RegExp(`url\\(#${a}\\)`,"g"),`url(#${l})`),r=r.replace(new RegExp(`href="#${a}"`,"g"),`href="#${l}"`)}),r=r.replace(new RegExp(`#${s}([^_\\w-])`,"g"),`#${u}$1`),r=r.replace(new RegExp(`#${s}\\{`,"g"),`#${u}{`),i.innerHTML=r,i.removeAttribute("style");const y=i.getAttribute("viewBox");if(y){const[,,l,a]=y.split(" ").map(Number);i.setAttribute("width",String(l)),i.setAttribute("height",String(a))}c.appendChild(i),e.showModal(),f.focus()};n.addEventListener("click",d),n.addEventListener("keydown",m=>{(m.key==="Enter"||m.key===" ")&&(m.preventDefault(),d(m))})}),f?.addEventListener("click",v),e?.addEventListener("click",t=>{const o=e?.querySelector(".mermaid-modal-content")?.getBoundingClientRect(),d=t;o&&(d.clientX<o.left||d.clientX>o.right||d.clientY<o.top||d.clientY>o.bottom)&&v()}),e.addEventListener("close",b)}function v(){const e=document.getElementById("mermaid-modal");e&&e.open&&e.close()}function b(){const c=document.getElementById("mermaid-modal")?.querySelector(".mermaid-modal-diagram");c&&(c.innerHTML="")}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",g):g();document.addEventListener("astro:page-load",()=>{p.clear(),g()});</script>  <div id="cta-follow" class="notification-container fixed bottom-24 left-0 z-50 max-w-sm -translate-x-full opacity-0 transition-all duration-500 ease-out astro-vj4tpspi"> <div class="mx-4 transform rounded-lg border-l-4 border-skin-accent bg-skin-card p-6 shadow-xl transition-transform duration-200 hover:scale-[1.02] astro-vj4tpspi"> <div class="flex flex-col gap-4 astro-vj4tpspi"> <div class="flex items-center gap-3 astro-vj4tpspi"> <div class="rounded-full bg-skin-accent bg-opacity-10 p-2 astro-vj4tpspi"> <svg class="h-6 w-6 text-skin-accent astro-vj4tpspi" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg> </div> <h3 class="text-xl font-bold text-skin-accent astro-vj4tpspi">Stay Updated!</h3> </div> <div class="space-y-2 astro-vj4tpspi"> <p class="text-base leading-relaxed text-skin-base astro-vj4tpspi">
Subscribe to my newsletter for more TypeScript, Vue, and web dev
              insights directly in your inbox.
</p> <ul class="ml-1 list-inside list-disc space-y-1 text-sm text-skin-base astro-vj4tpspi"> <li class="astro-vj4tpspi">Background information about the articles</li> <li class="astro-vj4tpspi">
Weekly Summary of all the interesting blog posts that I read
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_create-pwa-vue3-vite-4-steps" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="create-pwa-vue3-vite-4-steps" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vue/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vue</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/pwa/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">pwa</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/vite/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">vite</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/create-pwa-vue3-vite-4-steps/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <rect x="4" y="4" width="16" height="16" rx="2"></rect>
    <line x1="8" y1="11" x2="8" y2="16"></line>
    <line x1="8" y1="8" x2="8" y2="8.01"></line>
    <line x1="12" y1="16" x2="12" y2="11"></line>
    <path d="M16 16v-3a2 2 0 0 0 -4 0"></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on LinkedIn</span> </a> </div> </div>  </div> <section id="comments-section" class="giscus-container"></section> <script type="module">function a(){const e=document.getElementById("comments-section");if(!e)return;e.querySelector(".giscus, iframe")&&(e.innerHTML="");const t=document.createElement("script");t.src="https://giscus.app/client.js",t.setAttribute("data-repo","alexanderop/blog-comments"),t.setAttribute("data-repo-id","R_kgDON-LviQ"),t.setAttribute("data-category","Q&A"),t.setAttribute("data-category-id","DIC_kwDON-Lvic4CnPll"),t.setAttribute("data-mapping","url"),t.setAttribute("data-strict","0"),t.setAttribute("data-reactions-enabled","1"),t.setAttribute("data-emit-metadata","0"),t.setAttribute("data-input-position","bottom"),t.setAttribute("data-theme","dark"),t.setAttribute("data-lang","en"),t.setAttribute("data-loading","lazy"),t.setAttribute("crossorigin","anonymous"),t.async=!0,e.appendChild(t)}a();document.addEventListener("astro:page-load",a);</script> <div data-pagefind-ignore class="mb-8 mt-16 astro-vj4tpspi"> <h2 class="mb-6 text-3xl font-bold text-skin-accent astro-vj4tpspi">
Most Related Posts
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/vue-accessibility-blueprint-8-steps/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Vue Accessibility Blueprint: 8 Steps</h3> <p class="related-post-description astro-vj4tpspi"> Master Vue accessibility with our comprehensive guide. Learn 8 crucial steps to create inclusive, WCAG-compliant web applications that work for all users. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-sm">Updated:</span><span class="italic text-sm"><time dateTime="2024-09-29T15:22:00.000Z">Sep 29, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/sqlite-vue3-offline-first-web-apps-guide/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">SQLite in Vue: Complete Guide to Building Offline-First Web Apps</h3> <p class="related-post-description astro-vj4tpspi"> Learn how to build offline-capable Vue 3 apps using SQLite and WebAssembly in 2024. Step-by-step tutorial includes code examples for database operations, query playground implementation, and best practices for offline-first applications. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-11-25T07:44:12.000Z">Nov 25, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a><a href="/posts/how-to-write-clean-vue-components/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">How to Write Clean Vue Components</h3> <p class="related-post-description astro-vj4tpspi"> There are many ways to write better Vue components. One of my favorite ways is to separate business logic into pure functions. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-01-28T15:22:00.000Z">Jan 28, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> vue </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M9 19c-4.3 1.4 -4.3 -2.5 -6 -3m12 5v-3.5c0 -1 .1 -1.4 -.5 -2c2.8 -.3 5.5 -1.4 5.5 -6a4.6 4.6 0 0 0 -1.3 -3.2a4.2 4.2 0 0 0 -.1 -3.2s-1.1 -.3 -3.5 1.3a12.3 12.3 0 0 0 -6.2 0c-2.4 -1.6 -3.5 -1.3 -3.5 -1.3a4.2 4.2 0 0 0 -.1 3.2a4.6 4.6 0 0 0 -1.3 3.2c0 4.6 2.7 5.7 5.5 6c-.6 .6 -.6 1.2 -.5 2v3.5"
    ></path>
  </svg> <span class="sr-only astro-upu6fzxr"> alexop.dev on Github</span> </a><a href="https://de.linkedin.com/in/alexander-opalic-55464a169" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title="alexop.dev on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <rect x="4" y="4" width="16" height="16" rx="2"></rect>
    <line x1="8" y1="11" x2="8" y2="16"></line>
    <line x1="8" y1="8" x2="8" y2="8.01"></line>
    <line x1="12" y1="16" x2="12" y2="11"></line>
    <path d="M16 16v-3a2 2 0 0 0 -4 0"></path>
  </svg> <span class="sr-only astro-upu6fzxr">alexop.dev on LinkedIn</span> </a><a href="mailto:alex.opalic.dev@gmail.com" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title="Send an email to alexop.dev" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-upu6fzxr">Send an email to alexop.dev</span> </a><a href="https://twitter.com/alexanderopalic" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title="alexop.dev on X" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-upu6fzxr">alexop.dev on X</span> </a><a href="https://bsky.app/profile/alexvue.bsky.social" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title="alexop.dev on BlueSky" target="_blank" rel="noopener noreferrer"> <svg 
      xmlns="http://www.w3.org/2000/svg" 
      class="icon-tabler" 
      viewBox="0 0 64 57"
    >
      <path fill="none" stroke="currentColor" stroke-width="2" d="M13.873 3.805C21.21 9.332 29.103 20.537 32 26.55v15.882c0-.338-.13.044-.41.867-1.512 4.456-7.418 21.847-20.923 7.944-7.111-7.32-3.819-14.64 9.125-16.85-7.405 1.264-15.73-.825-18.014-9.015C1.12 23.022 0 8.51 0 6.55 0-3.268 8.579-.182 13.873 3.805ZM50.127 3.805C42.79 9.332 34.897 20.537 32 26.55v15.882c0-.338.13.044.41.867 1.512 4.456 7.418 21.847 20.923 7.944 7.111-7.32 3.819-14.64-9.125-16.85 7.405 1.264 15.73-.825 18.014-9.015C62.88 23.022 64 8.51 64 6.55c0-9.818-8.578-6.732-13.873-2.745Z"></path>
    </svg> <span class="sr-only astro-upu6fzxr">alexop.dev on BlueSky</span> </a> </div>  </div> <div class="license-info astro-sz7xmlte"> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer" class="cc-license astro-sz7xmlte"> <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="CC" class="cc-icon astro-sz7xmlte"> <img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="BY" class="cc-icon astro-sz7xmlte">
Content licensed under CC BY 4.0
</a> </div> <div class="legal-links astro-sz7xmlte"> <a href="/imprint/" class="legal-link astro-sz7xmlte"> Imprint </a> <span class="separator astro-sz7xmlte">|</span> <a href="/data-privacy/" class="legal-link astro-sz7xmlte"> Data Privacy </a> </div> </div> </footer>   <!-- Wiki link preview card hover script --> <script>
      function initInternalLinks() {
        const wrappers = document.querySelectorAll(".internal-link-wrapper");

        wrappers.forEach(wrapper => {
          const card = wrapper.querySelector(".preview-card");
          const link = wrapper.querySelector(".internal-link");
          if (!card || !link) return;

          // Skip if already initialized
          if (wrapper.dataset.initialized === "true") return;
          wrapper.dataset.initialized = "true";

          // Function to hide the card
          const hideCard = () => {
            card.classList.remove("is-fixed");
            card.style.removeProperty("--pc-top");
            card.style.removeProperty("--pc-left");
            card.style.opacity = "";
            card.style.visibility = "";
            // Remove scroll listener when hiding
            window.removeEventListener("scroll", hideCard);
          };

          wrapper.addEventListener("mouseenter", () => {
            // Make visible first so it has size
            card.style.opacity = "1";
            card.style.visibility = "visible";

            // Use fixed positioning to escape overflow clipping
            const linkRect = link.getBoundingClientRect();
            const cardRect = card.getBoundingClientRect();

            // Position above by default; flip below if too close to top
            const aboveTop = linkRect.top - 8 - cardRect.height;
            const belowTop = linkRect.bottom + 8;
            const top = aboveTop < 10 ? belowTop : aboveTop;

            // Center horizontally on the link
            const left = linkRect.left + linkRect.width / 2 - cardRect.width / 2;

            // Constrain to viewport
            const vw = document.documentElement.clientWidth;
            const safeLeft = Math.max(8, Math.min(left, vw - cardRect.width - 8));

            // Apply fixed position with coordinates
            card.classList.add("is-fixed");
            card.style.setProperty("--pc-top", `${Math.round(top)}px`);
            card.style.setProperty("--pc-left", `${Math.round(safeLeft)}px`);

            // Hide card on scroll
            window.addEventListener("scroll", hideCard, { passive: true });
          });

          wrapper.addEventListener("mouseleave", hideCard);
        });
      }

      // Initialize on both initial load and after client-side navigation
      document.addEventListener("astro:page-load", initInternalLinks);
    </script> </body> </html>  <script>(function(){const postSlug = "create-pwa-vue3-vite-4-steps";

  function updateCTAFollowVisibility() {
    const cta = document.getElementById("cta-follow");
    const article = document.getElementById("article");
    if (!cta || !article) return;

    // If it has the force-hidden class, don't try to show it
    if (cta.classList.contains("force-hidden")) {
      return;
    }

    const viewportHeight = window.innerHeight;
    const articleBottom = article.getBoundingClientRect().bottom;

    // Only show if user has reached the end of the article (article bottom is visible)
    // and hasn't dismissed or subscribed
    if (
      articleBottom <= viewportHeight + 100 && // 100px buffer
      !localStorage.getItem("newsletter_dismissed") &&
      !localStorage.getItem("newsletter_subscribed")
    ) {
      cta.dataset.visible = "true";
      cta.style.transform = "translateX(0)";
      cta.style.opacity = "1";
    } else {
      cta.dataset.visible = "false";
      cta.style.transform = "translateX(-120%)";
      cta.style.opacity = "0";
    }
  }

  // Initialize visibility check
  window.addEventListener("scroll", updateCTAFollowVisibility);
  window.addEventListener("resize", updateCTAFollowVisibility);

  // Add a small delay to initial check to ensure proper positioning
  setTimeout(updateCTAFollowVisibility, 500);

  // Handle newsletter subscribe click with proper tracking
  document
    .getElementById("newsletter-subscribe-button")
    ?.addEventListener("click", () => {
      localStorage.setItem("newsletter_subscribed", "true");

      // Force the popup to stay hidden
      const cta = document.getElementById("cta-follow");
      if (cta) {
        cta.classList.add("force-hidden");
        cta.style.transform = "translateX(-120%)";
        cta.style.opacity = "0";
      }

      if (window.plausible) {
        window.plausible("Newsletter Subscribe Click", {
          props: {
            post: postSlug,
            location: "end_of_article",
            source: "notification",
          },
        });
      }
    });

  // Handle newsletter dismiss click
  document
    .getElementById("newsletter-dismiss")
    ?.addEventListener("click", function () {
      const slug = this.getAttribute("data-post-slug");
      localStorage.setItem("newsletter_dismissed", "true");

      const cta = document.getElementById("cta-follow");
      if (cta) {
        cta.classList.add("force-hidden");
        cta.style.transform = "translateX(-120%)";
        cta.style.opacity = "0";
      }

      if (window.plausible) {
        window.plausible("Newsletter Dismissed", {
          props: {
            post: slug,
            location: "end_of_article",
            source: "notification",
          },
        });
      }
    });
})();</script>  <script>
  /** Create a progress indicator
   *  at the top */
  function createProgressBar() {
    // Create the main container div
    const progressContainer = document.createElement("div");
    progressContainer.className =
      "progress-container fixed top-0 z-10 h-1 w-full bg-skin-fill";

    // Create the progress bar div
    const progressBar = document.createElement("div");
    progressBar.className = "progress-bar h-1 w-0 bg-skin-accent";
    progressBar.id = "myBar";

    // Append the progress bar to the progress container
    progressContainer.appendChild(progressBar);

    // Append the progress container to the document body or any other desired parent element
    document.body.appendChild(progressContainer);
  }
  createProgressBar();

  /** Update the progress bar
   *  when user scrolls */
  function updateScrollProgress() {
    const winScroll =
      document.body.scrollTop || document.documentElement.scrollTop;
    const height =
      document.documentElement.scrollHeight -
      document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    const myBar = document.getElementById("myBar");
    if (myBar) {
      myBar.style.width = scrolled + "%";
    }
  }
  document.addEventListener("scroll", updateScrollProgress);

  /** Make headings groups for hover effect on anchor links */
  function makeHeadingsGroups() {
    const headings = Array.from(
      document.querySelectorAll(".prose h2, .prose h3, .prose h4, .prose h5, .prose h6")
    );
    for (const heading of headings) {
      heading.classList.add("group");
    }
  }

  // Run after DOM is loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", makeHeadingsGroups);
  } else {
    makeHeadingsGroups();
  }

  /** Scroll back to top functionality */
  function attachBackToTop() {
    const backToTopBtn = document.getElementById("back-to-top");
    if (backToTopBtn) {
      backToTopBtn.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
      });
    }
  }
  attachBackToTop();
</script>