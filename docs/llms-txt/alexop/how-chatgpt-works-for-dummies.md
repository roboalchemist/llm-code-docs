# Source: https://alexop.dev/posts/how-chatgpt-works-for-dummies

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/how-chatgpt-works-for-dummies/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>How ChatGPT Works (for Dummies) | alexop.dev</title><meta name="title" content="How ChatGPT Works (for Dummies) | alexop.dev"><meta name="description" content="A plain English guide to how ChatGPT works—from token prediction to hallucinations. Perfect for developers who want to understand the AI they're building with."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="How ChatGPT Works (for Dummies) | alexop.dev"><meta property="og:description" content="A plain English guide to how ChatGPT works—from token prediction to hallucinations. Perfect for developers who want to understand the AI they're building with."><meta property="og:url" content="https://alexop.dev/posts/how-chatgpt-works-for-dummies/"><meta property="og:image" content="https://alexop.dev/posts/how-chat-gpt-works-for-dummies/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-04-21T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/how-chatgpt-works-for-dummies/"><meta property="twitter:title" content="How ChatGPT Works (for Dummies) | alexop.dev"><meta property="twitter:description" content="A plain English guide to how ChatGPT works—from token prediction to hallucinations. Perfect for developers who want to understand the AI they're building with."><meta property="twitter:image" content="https://alexop.dev/posts/how-chat-gpt-works-for-dummies/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"How ChatGPT Works (for Dummies) | alexop.dev","description":"A plain English guide to how ChatGPT works—from token prediction to hallucinations. Perfect for developers who want to understand the AI they're building with.","image":"https://alexop.dev/posts/how-chat-gpt-works-for-dummies/index.png","datePublished":"2025-04-21T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: how-chat-gpt-works-for-dummies; }@layer astro { ::view-transition-old(how-chat-gpt-works-for-dummies) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(how-chat-gpt-works-for-dummies) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(how-chat-gpt-works-for-dummies) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(how-chat-gpt-works-for-dummies) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: ai; }@layer astro { ::view-transition-old(ai) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(ai) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(ai) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(ai) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">How ChatGPT Works (for Dummies)</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-04-21T00:00:00.000Z">Apr 21, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z1D0zJb" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;How ChatGPT Works (for Dummies)&quot;],&quot;content&quot;:[0,&quot;import { Image } from \&quot;astro:assets\&quot;;\nimport monsterImg from \&quot;../../assets/images/chatgpt/monster.png\&quot;;\nimport fineTuningComic from \&quot;../../assets/images/chatgpt/fineTuningComic.png\&quot;;\nimport swissCheeseImg from \&quot;../../assets/images/chatgpt/swiss.png\&quot;;\n\n## Introduction\n\nTwo and a half years ago, humanity witnessed the beginning of its biggest achievement.\nOr maybe I should say (we got introduced to it): **ChatGPT**.\nSince its launch in November 2022, a lot has happened. And honestly?\nWe&#39;re still deep in the chaos. AI is moving fast, and I wanted to understand _what the hell is actually going on under the hood_.\n\n&gt; This post was highly inspired by Chip Huyen&#39;s excellent technical deep-dive on RLHF and how ChatGPT works: [RLHF: Reinforcement Learning from Human Feedback](https://huyenchip.com/2023/05/02/rlhf.html). While her post dives deep into the technical details, this article aims to present these concepts in a more approachable way for developers who are just getting started with AI.\n\nSo I went full nerd mode:\n\n- Watched a ton of Andrej Karpathy videos\n- Read Stephen Wolfram&#39;s \&quot;[What Is ChatGPT Doing … and Why Does It Work?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/)\&quot; (and even bought the book)\n- Currently halfway through _AI Engineering: Building Applications with Foundation Models_ by Chip Huyen\n\nThis post is my attempt to break down what I&#39;ve learned.\nJust a simple overview of how something like ChatGPT even works.\nBecause honestly? If you&#39;re building with AI (even just using it), you _need_ a basic understanding of what&#39;s happening behind the scenes.\n\nIf you spend just a little time on this, you&#39;ll get _way_ better at:\n\n- Prompting\n- Debugging\n- Building with AI tools\n- Collaborating with these systems in smart ways\n\nLet&#39;s go.\n\n## What Happens When You Use ChatGPT?\n\n```mermaid\nflowchart LR\nA[User input] --&gt; B[Text split into tokens]\nB --&gt; C[Model processes tokens]\nC --&gt; D[Predict next token]\nD --&gt; E{Response complete?}\nE --&gt;|No| D\nE --&gt;|Yes| F[Display response]\n```\n\n## The Fancy Autocomplete: How ChatGPT Predicts What Comes Next\n\nThink about when you text on your phone and it suggests the next word. ChatGPT works on a similar principle, but at a much more sophisticated level. Instead of just looking at the last word, it looks at everything you&#39;ve written so far.\n\nHere&#39;s what actually happens:\n\n### Your text gets broken down into \&quot;tokens\&quot;\n\nTokens are like the vocabulary units that AI models understand - they&#39;re not always complete words. Sometimes a token is a full word like \&quot;hello\&quot;, sometimes it&#39;s part of a word like \&quot;ing\&quot;, and sometimes it&#39;s even just a single character. Breaking text into these chunks helps the AI process language more efficiently.\n\nLet&#39;s see how tokenization works with a simple example:\n\nThe sentence \&quot;I love programming in JavaScript\&quot; might be split into:\n`[&#39;I&#39;, &#39; love&#39;, &#39; program&#39;, &#39;ming&#39;, &#39; in&#39;, &#39; Java&#39;, &#39;Script&#39;]`\n\nNotice how \&quot;programming\&quot; got split into \&quot;program\&quot; and \&quot;ming\&quot;, while \&quot;JavaScript\&quot; became \&quot;Java\&quot; and \&quot;Script\&quot;. This is how the AI sees your text!\n\n### These tokens get converted into numbers\n\nThe model doesn&#39;t understand text - it understands numbers. So each token gets converted to a unique ID number, like:\n`[20, 5692, 12073, 492, 41, 8329, 6139]`\n\n### The model plays a sophisticated game of \&quot;what comes next?\&quot;\n\nAfter processing your text, ChatGPT calculates probabilities for every possible next token in its vocabulary (which contains hundreds of thousands of options).\n\nIf you type \&quot;The capital of France is\&quot;, the model might calculate:\n\n- \&quot; Paris\&quot;: 92% probability\n- \&quot; Lyon\&quot;: 3% probability\n- \&quot; located\&quot;: 1% probability\n- [thousands of other possibilities with smaller probabilities]\n\nIt then selects a token based on these probabilities (usually picking high-probability tokens, but occasionally throwing in some randomness for creativity).\n\n### The process repeats token by token\n\nAfter selecting a token, it adds that to what it&#39;s seen so far and calculates probabilities for the next token. This continues until it completes the response.\n\n### A Relatable Example\n\nThis process is similar to how you might predict the last word in \&quot;Mary had a little \\_\\_\\_\&quot;. You&#39;d probably say \&quot;lamb\&quot; because you&#39;ve seen that pattern before. ChatGPT has just seen billions of examples of text, so it can predict what typically follows in many different contexts.\n\n### Try It Yourself!\n\nTry out this interactive tokenizer from [dqbd](https://github.com/dqbd/tiktokenizer) to see how text gets split into tokens:\n\n&lt;div\n  class=\&quot;light-theme-wrapper\&quot;\n  style=\&quot;background: white; color: black; padding: 1rem; border-radius: 8px; margin: 2rem 0;\&quot;\n&gt;\n  &lt;iframe\n    src=\&quot;https://tiktokenizer.vercel.app/\&quot;\n    width=\&quot;100%\&quot;\n    height=\&quot;500px\&quot;\n    loading=\&quot;lazy\&quot;\n    style=\&quot;color-scheme: light; background: white;\&quot;\n    sandbox=\&quot;allow-scripts allow-same-origin allow-forms\&quot;\n    title=\&quot;Interactive GPT Tokenizer\&quot;\n  &gt;&lt;/iframe&gt;\n&lt;/div&gt;\n\nThink of it like the world&#39;s most sophisticated autocomplete.\nIt&#39;s not \&quot;thinking\&quot; - it&#39;s predicting what text should follow your input based on patterns it&#39;s learned.\n\nNow that we understand how ChatGPT predicts tokens, let&#39;s explore the fascinating process that enables it to make these predictions in the first place. How does a model learn to understand and generate human-like text?\n\n## The Three-Stage Training Process\n\n&lt;Image\n  src={monsterImg}\n  alt=\&quot;A friendly monster illustration representing AI model transformation\&quot;\n  width={400}\n  class=\&quot;mx-auto\&quot;\n/&gt;\n\nFirst, the model needs to learn how language works (and also pick up some basic knowledge about the world). Once that&#39;s done, it&#39;s basically just a fancy autocomplete. So we need to fine-tune it to behave more like a helpful chat assistant. Finally, we bring humans into the loop to nudge it toward the kind of answers we actually want and away from the ones we don&#39;t.\n\nThe image above is a popular AI meme that illustrates an important concept: a pre-trained model, having absorbed vast amounts of unfiltered internet data, can be potentially harmful or dangerous. The \&quot;friendly face\&quot; represents how fine-tuning and alignment transform this raw model into something helpful and safe for human interaction.\n\n### 1. Pre-training: Learning from the Internet\n\nThe model downloads and processes massive amounts of internet text. And when I say massive, I mean MASSIVE:\n\n- GPT-3 was trained on 300 billion tokens (that&#39;s like reading millions of books!)\n- LLaMA was trained on 1.4 trillion tokens\n- CommonCrawl, a major data source, captures about 3.1 billion web pages per monthly crawl (with 1.0-1.4 billion new URLs each time)\n\nHere&#39;s what happens during pre-training:\n\n- Companies like OpenAI filter the raw internet data\n- They remove spam, adult content, malware sites, etc.\n- The cleaned text is converted into tokens\n- The model learns to predict what tokens come next in a sequence\n\n### 2. Supervised Fine-Tuning: Learning to Be an Assistant\n\nThis is where the magic happens - transforming a basic text predictor into a helpful AI assistant. Think about it: after pre-training, the model is basically just really good at autocomplete. It can predict what words come next, but it doesn&#39;t know how to have a conversation or be helpful.\n\nHere&#39;s how humans step in to teach it:\n\n#### The Training Process\n\n- Expert human trainers create thousands of example conversations\n- These aren&#39;t just any trainers - 90% have college degrees!\n- Each trainer must pass a tough screening test\n- They create between 10,000 to 100,000 training examples\n\n#### What Good Examples Look Like\n\nHere&#39;s a real example from OpenAI&#39;s training data:\n\n```\nHuman: \&quot;Serendipity means the occurrence and development of events by chance in a happy or beneficial way. Use the word in a sentence.\&quot;\nAssistant: \&quot;Running into Margaret and being introduced to Tom was a fortunate stroke of serendipity.\&quot;\n```\n\nTo understand why this step is crucial, let&#39;s see what might happen with just pre-training (Step 1) versus after fine-tuning (Step 2):\n\n**Pre-training only (Step 1):**\n\n```\nHuman: Can you help me understand what recursion is in programming?\nModel: recursion is when a function calls itself. Here&#39;s an example in Python:\n\ndef factorial(n):\n    if n == 0:\n    return 1\n    return n * factorial(n-1)\n\nThis function calculates the factorial of a number using recursion. For more information, check out our tutorial at www.codingsite.com or buy our premium course for $49.99!\n```\n\n**After fine-tuning (Step 2):**\n\n```\nHuman: Can you help me understand what recursion is in programming?\nAssistant: I&#39;ll explain recursion in a clear and helpful way. Recursion is when a function calls itself to solve a problem by breaking it down into smaller, similar sub-problems. Let me give you a simple example:\n\nThink of it like looking at yourself between two mirrors - you see smaller versions of yourself repeating infinitely. In programming, it works similarly:\n\n1. A recursive function handles a small, simple case (called the base case)\n2. For bigger cases, it breaks down the problem and calls itself\n3. This continues until it reaches the base case\n\nWould you like me to show you a practical example in code?\n```\n\nNotice the differences:\n\n- The pre-trained model just predicts likely next tokens based on internet data\n- It might include ads or inappropriate content\n- It doesn&#39;t understand it&#39;s supposed to be an assistant\n\nThe fine-tuned model:\n\n- Understands it&#39;s an AI assistant\n- Maintains a helpful, professional tone\n- Offers clear explanations\n- Asks if the user needs more help\n- Avoids inappropriate content or advertising\n\n#### What the Model Learns\n\nThrough these examples, the model starts to understand:\n\n- When to ask follow-up questions\n- How to structure explanations\n- What tone and style to use\n- How to be helpful while staying ethical\n- When to admit it doesn&#39;t know something\n\nThis is crucial to understand: **When you use ChatGPT, you&#39;re not talking to a magical AI - you&#39;re interacting with a model that&#39;s learned to imitate helpful responses through careful training.** It&#39;s following patterns it learned from thousands of carefully crafted training conversations.\n\n&lt;Image\n  src={fineTuningComic}\n  alt=\&quot;Comic illustrating the fine-tuning process of AI models\&quot;\n  class=\&quot;w-full\&quot;\n/&gt;\n\n### 3. Reinforcement Learning: Learning to Improve (Optional Optimization)\n\nThink of the first two steps as essential cooking ingredients - you need them to make the dish. Step 3 is like having a professional chef taste and refine the recipe. It&#39;s not strictly necessary, but it can make things much better.\n\nHere&#39;s a concrete example of how this optimization works:\n\n```\nHuman: What&#39;s the capital of France?\n\nPossible Model Responses:\nA: \&quot;The capital of France is Paris.\&quot;\nB: \&quot;Paris is the capital of France. With a population of over 2 million people, it&#39;s known for the Eiffel Tower, the Louvre, and its rich cultural heritage.\&quot;\nC: \&quot;Let me tell you about France&#39;s capital! 🗼 Paris is such a beautiful city! I absolutely love it there, though I haven&#39;t actually been since I&#39;m an AI 😊 The food is amazing and...\&quot;\n```\n\nHuman raters would then rank these responses:\n\n- Response B gets highest rating (informative but concise)\n- Response A gets medium rating (correct but minimal)\n- Response C gets lowest rating (too chatty, unnecessary personal comments)\n\nThe model learns from these preferences:\n\n1. Being informative but not overwhelming is good\n2. Staying focused on the question is important\n3. Avoiding fake personal experiences is preferred\n\n#### The Training Process\n\n- The model tries many different responses to the same prompt\n- Each response gets a score from the reward model\n- Responses that get high scores are reinforced (like giving a dog a treat)\n- The model gradually learns what makes humans happy\n\nThink of Reinforcement Learning from Human Feedback (RLHF) as teaching the AI social skills. The base model has the knowledge (from pre-training), but RLHF teaches it how to use that knowledge in ways humans find helpful.\n\n## What Makes These Models Special?\n\n### They Need Tokens to Think\n\nUnlike humans, these models need to distribute their computation across many tokens. Each token has only a limited amount of computation available.\n\nEver notice how ChatGPT walks through problems step by step instead of jumping straight to the answer? This isn&#39;t just for your benefit - it&#39;s because:\n\n1. The model can only do so much computation per token\n2. By spreading reasoning across many tokens, it can solve harder problems\n3. This is why asking for \&quot;the answer immediately\&quot; often leads to wrong results\n\nHere&#39;s a concrete example:\n\n**Bad Prompt (Forcing Immediate Answer)**:\n\n```\nGive me the immediate answer without explanation: What&#39;s the total cost of buying 7 books at $12.99 each with 8.5% sales tax? Just the final number.\n```\n\nThis approach is more likely to produce errors because it restricts the model&#39;s ability to distribute computation across tokens.\n\n**Good Prompt (Allowing Token-Based Thinking)**:\n\n```\nCalculate the total cost of buying 7 books at $12.99 each with 8.5% sales tax. Please show your work step by step.\n```\n\nThis allows the model to break down the problem:\n\n1. Base cost: 7 × $12.99 = $90.93\n2. Sales tax amount: $90.93 × 0.085 = $7.73\n3. Total cost: $90.93 + $7.73 = $98.66\n\nThe second approach is more reliable because it gives the model space to distribute its computation across multiple tokens, reducing the chance of errors.\n\n### Context Is King\n\nWhat these models see is drastically different from what we see:\n\n- We see words, sentences, and paragraphs\n- Models see token IDs (numbers representing text chunks)\n- There&#39;s a limited \&quot;context window\&quot; that determines how much the model can \&quot;see\&quot; at once\n\nWhen you paste text into ChatGPT, it goes directly into this context window - the model&#39;s working memory. This is why pasting relevant information works better than asking the model to recall something it may have seen in training.\n\n### The Swiss Cheese Problem\n\n&lt;Image\n  src={swissCheeseImg}\n  alt=\&quot;Swiss cheese illustration representing gaps in AI capabilities\&quot;\n  width={300}\n  class=\&quot;mx-auto\&quot;\n/&gt;\n\nThese models have what Andrew Karpahty calls \&quot;Swiss cheese capabilities\&quot; - they&#39;re brilliant in many areas but have unexpected holes:\n\n- Can solve complex math problems but struggle with comparing 9.11 and 9.9\n- Can write elaborate code but might not count characters correctly\n- Can generate human-level responses but get tripped up by simple reasoning tasks\n\nThis happens because of how they&#39;re trained and their tokenization process. The models don&#39;t see characters as we do - they see tokens, which makes certain tasks surprisingly difficult.\n\n## How to Use LLMs Effectively\n\nAfter all my research, here&#39;s my advice:\n\n1. **Use them as tools, not oracles**: Always verify important information\n2. **Give them tokens to think**: Let them reason step by step\n3. **Put knowledge in context**: Paste relevant information rather than hoping they remember it\n4. **Understand their limitations**: Be aware of the \&quot;Swiss cheese\&quot; problem\n5. **Try reasoning models**: For complex problems, use models specifically designed for reasoning&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="introduction">Introduction<a class="heading-link" aria-label="Link to section" href="#introduction"><span class="heading-link-icon">#</span></a></h2>
<p>Two and a half years ago, humanity witnessed the beginning of its biggest achievement.
Or maybe I should say (we got introduced to it): <strong>ChatGPT</strong>.
Since its launch in November 2022, a lot has happened. And honestly?
We’re still deep in the chaos. AI is moving fast, and I wanted to understand <em>what the hell is actually going on under the hood</em>.</p>
<blockquote>
<p>This post was highly inspired by Chip Huyen’s excellent technical deep-dive on RLHF and how ChatGPT works: <a href="https://huyenchip.com/2023/05/02/rlhf.html" rel="noopener noreferrer" target="_blank">RLHF: Reinforcement Learning from Human Feedback</a>. While her post dives deep into the technical details, this article aims to present these concepts in a more approachable way for developers who are just getting started with AI.</p>
</blockquote>
<p>So I went full nerd mode:</p>
<ul>
<li>Watched a ton of Andrej Karpathy videos</li>
<li>Read Stephen Wolfram’s “<a href="https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/" rel="noopener noreferrer" target="_blank">What Is ChatGPT Doing … and Why Does It Work?</a>” (and even bought the book)</li>
<li>Currently halfway through <em>AI Engineering: Building Applications with Foundation Models</em> by Chip Huyen</li>
</ul>
<p>This post is my attempt to break down what I’ve learned.
Just a simple overview of how something like ChatGPT even works.
Because honestly? If you’re building with AI (even just using it), you <em>need</em> a basic understanding of what’s happening behind the scenes.</p>
<p>If you spend just a little time on this, you’ll get <em>way</em> better at:</p>
<ul>
<li>Prompting</li>
<li>Debugging</li>
<li>Building with AI tools</li>
<li>Collaborating with these systems in smart ways</li>
</ul>
<p>Let’s go.</p>
<h2 id="what-happens-when-you-use-chatgpt">What Happens When You Use ChatGPT?<a class="heading-link" aria-label="Link to section" href="#what-happens-when-you-use-chatgpt"><span class="heading-link-icon">#</span></a></h2>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:1665.40625px" viewBox="0 0 1665.40625 243.390625" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M164.328,121.695L168.495,121.695C172.661,121.695,180.995,121.695,188.661,121.695C196.328,121.695,203.328,121.695,206.828,121.695L210.328,121.695" id="L_A_B_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MTY0LjMyODEyNSwieSI6MTIxLjY5NTMxMjV9LHsieCI6MTg5LjMyODEyNSwieSI6MTIxLjY5NTMxMjV9LHsieCI6MjE0LjMyODEyNSwieSI6MTIxLjY5NTMxMjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M474.328,121.695L478.495,121.695C482.661,121.695,490.995,121.695,498.661,121.695C506.328,121.695,513.328,121.695,516.828,121.695L520.328,121.695" id="L_B_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_C_0" data-points="W3sieCI6NDc0LjMyODEyNSwieSI6MTIxLjY5NTMxMjV9LHsieCI6NDk5LjMyODEyNSwieSI6MTIxLjY5NTMxMjV9LHsieCI6NTI0LjMyODEyNSwieSI6MTIxLjY5NTMxMjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M784.328,121.695L788.495,121.695C792.661,121.695,800.995,121.695,808.661,121.695C816.328,121.695,823.328,121.695,826.828,121.695L830.328,121.695" id="L_C_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_D_0" data-points="W3sieCI6Nzg0LjMyODEyNSwieSI6MTIxLjY5NTMxMjV9LHsieCI6ODA5LjMyODEyNSwieSI6MTIxLjY5NTMxMjV9LHsieCI6ODM0LjMyODEyNSwieSI6MTIxLjY5NTMxMjV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1067.719,109.357L1073.491,108.747C1079.263,108.136,1090.807,106.916,1103.534,107.056C1116.26,107.196,1130.169,108.696,1137.123,109.446L1144.078,110.196" id="L_D_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_E_0" data-points="W3sieCI6MTA2Ny43MTg3NSwieSI6MTA5LjM1NzA1NzQ2NjQ0Mjk1fSx7IngiOjExMDIuMzUxNTYyNSwieSI6MTA1LjY5NTMxMjV9LHsieCI6MTE0OC4wNTQ0NTIwMTgxNjEsInkiOjExMC42MjUyMzU0ODE4Mzg5M31d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1148.054,132.765L1140.437,133.587C1132.82,134.409,1117.586,136.052,1104.86,136.333C1092.133,136.615,1081.915,135.535,1076.806,134.994L1071.697,134.454" id="L_E_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_D_0" data-points="W3sieCI6MTE0OC4wNTQ0NTIwMTgxNjEsInkiOjEzMi43NjUzODk1MTgxNjEwN30seyJ4IjoxMTAyLjM1MTU2MjUsInkiOjEzNy42OTUzMTI1fSx7IngiOjEwNjcuNzE4NzUsInkiOjEzNC4wMzM1Njc1MzM1NTcwNn1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1364.375,121.695L1370.951,121.695C1377.526,121.695,1390.677,121.695,1403.161,121.695C1415.646,121.695,1427.464,121.695,1433.372,121.695L1439.281,121.695" id="L_E_F_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_E_F_0" data-points="W3sieCI6MTM2NC4zNzUsInkiOjEyMS42OTUzMTI1fSx7IngiOjE0MDMuODI4MTI1LCJ5IjoxMjEuNjk1MzEyNX0seyJ4IjoxNDQzLjI4MTI1LCJ5IjoxMjEuNjk1MzEyNX1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_B_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_C_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_D_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_D_E_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(1107.89051, 137.09783)"><g class="label" data-id="L_E_D_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(1403.828125, 121.6953125)"><g class="label" data-id="L_E_F_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(86.1640625, 121.6953125)"><rect class="basic label-container" style="" x="-78.1640625" y="-27" width="156.328125" height="54"></rect><g class="label" style="" transform="translate(-48.1640625, -12)"><rect></rect><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>User input</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(344.328125, 121.6953125)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Text split into tokens</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-3" transform="translate(654.328125, 121.6953125)"><rect class="basic label-container" style="" x="-130" y="-39" width="260" height="78"></rect><g class="label" style="" transform="translate(-100, -24)"><rect></rect><foreignObject width="200" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table;white-space:break-spaces;line-height:1.5;max-width:200px;text-align:center;width:200px"><span class="nodeLabel"><p>Model processes tokens</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-5" transform="translate(951.0234375, 121.6953125)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Predict next token</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-7" transform="translate(1250.6796875, 121.6953125)"><polygon points="113.6953125,0 227.390625,-113.6953125 113.6953125,-227.390625 0,-113.6953125" class="label-container" transform="translate(-113.1953125, 113.6953125)"></polygon><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Response complete?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-F-11" transform="translate(1550.34375, 121.6953125)"><rect class="basic label-container" style="" x="-107.0625" y="-27" width="214.125" height="54"></rect><g class="label" style="" transform="translate(-77.0625, -12)"><rect></rect><foreignObject width="154.125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Display response</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<h2 id="the-fancy-autocomplete-how-chatgpt-predicts-what-comes-next">The Fancy Autocomplete: How ChatGPT Predicts What Comes Next<a class="heading-link" aria-label="Link to section" href="#the-fancy-autocomplete-how-chatgpt-predicts-what-comes-next"><span class="heading-link-icon">#</span></a></h2>
<p>Think about when you text on your phone and it suggests the next word. ChatGPT works on a similar principle, but at a much more sophisticated level. Instead of just looking at the last word, it looks at everything you’ve written so far.</p>
<p>Here’s what actually happens:</p>
<h3 id="your-text-gets-broken-down-into-tokens">Your text gets broken down into “tokens”<a class="heading-link" aria-label="Link to section" href="#your-text-gets-broken-down-into-tokens"><span class="heading-link-icon">#</span></a></h3>
<p>Tokens are like the vocabulary units that AI models understand - they’re not always complete words. Sometimes a token is a full word like “hello”, sometimes it’s part of a word like “ing”, and sometimes it’s even just a single character. Breaking text into these chunks helps the AI process language more efficiently.</p>
<p>Let’s see how tokenization works with a simple example:</p>
<p>The sentence “I love programming in JavaScript” might be split into:
<code>[&#39;I&#39;, &#39; love&#39;, &#39; program&#39;, &#39;ming&#39;, &#39; in&#39;, &#39; Java&#39;, &#39;Script&#39;]</code></p>
<p>Notice how “programming” got split into “program” and “ming”, while “JavaScript” became “Java” and “Script”. This is how the AI sees your text!</p>
<h3 id="these-tokens-get-converted-into-numbers">These tokens get converted into numbers<a class="heading-link" aria-label="Link to section" href="#these-tokens-get-converted-into-numbers"><span class="heading-link-icon">#</span></a></h3>
<p>The model doesn’t understand text - it understands numbers. So each token gets converted to a unique ID number, like:
<code>[20, 5692, 12073, 492, 41, 8329, 6139]</code></p>
<h3 id="the-model-plays-a-sophisticated-game-of-what-comes-next">The model plays a sophisticated game of “what comes next?”<a class="heading-link" aria-label="Link to section" href="#the-model-plays-a-sophisticated-game-of-what-comes-next"><span class="heading-link-icon">#</span></a></h3>
<p>After processing your text, ChatGPT calculates probabilities for every possible next token in its vocabulary (which contains hundreds of thousands of options).</p>
<p>If you type “The capital of France is”, the model might calculate:</p>
<ul>
<li>” Paris”: 92% probability</li>
<li>” Lyon”: 3% probability</li>
<li>” located”: 1% probability</li>
<li>[thousands of other possibilities with smaller probabilities]</li>
</ul>
<p>It then selects a token based on these probabilities (usually picking high-probability tokens, but occasionally throwing in some randomness for creativity).</p>
<h3 id="the-process-repeats-token-by-token">The process repeats token by token<a class="heading-link" aria-label="Link to section" href="#the-process-repeats-token-by-token"><span class="heading-link-icon">#</span></a></h3>
<p>After selecting a token, it adds that to what it’s seen so far and calculates probabilities for the next token. This continues until it completes the response.</p>
<h3 id="a-relatable-example">A Relatable Example<a class="heading-link" aria-label="Link to section" href="#a-relatable-example"><span class="heading-link-icon">#</span></a></h3>
<p>This process is similar to how you might predict the last word in “Mary had a little ___”. You’d probably say “lamb” because you’ve seen that pattern before. ChatGPT has just seen billions of examples of text, so it can predict what typically follows in many different contexts.</p>
<h3 id="try-it-yourself">Try It Yourself!<a class="heading-link" aria-label="Link to section" href="#try-it-yourself"><span class="heading-link-icon">#</span></a></h3>
<p>Try out this interactive tokenizer from <a href="https://github.com/dqbd/tiktokenizer" rel="noopener noreferrer" target="_blank">dqbd</a> to see how text gets split into tokens:</p>
<div class="light-theme-wrapper" style="background: white; color: black; padding: 1rem; border-radius: 8px; margin: 2rem 0;"><iframe src="https://tiktokenizer.vercel.app/" width="100%" height="500px" loading="lazy" style="color-scheme: light; background: white;" sandbox="allow-scripts allow-same-origin allow-forms" title="Interactive GPT Tokenizer"></iframe></div>
<p>Think of it like the world’s most sophisticated autocomplete.
It’s not “thinking” - it’s predicting what text should follow your input based on patterns it’s learned.</p>
<p>Now that we understand how ChatGPT predicts tokens, let’s explore the fascinating process that enables it to make these predictions in the first place. How does a model learn to understand and generate human-like text?</p>
<h2 id="the-three-stage-training-process">The Three-Stage Training Process<a class="heading-link" aria-label="Link to section" href="#the-three-stage-training-process"><span class="heading-link-icon">#</span></a></h2>
<img src="/_astro/monster.DOIJKwqy_2nh7DJ.webp" alt="A friendly monster illustration representing AI model transformation" loading="lazy" decoding="async" fetchpriority="auto" width="400" height="270" class="mx-auto">
<p>First, the model needs to learn how language works (and also pick up some basic knowledge about the world). Once that’s done, it’s basically just a fancy autocomplete. So we need to fine-tune it to behave more like a helpful chat assistant. Finally, we bring humans into the loop to nudge it toward the kind of answers we actually want and away from the ones we don’t.</p>
<p>The image above is a popular AI meme that illustrates an important concept: a pre-trained model, having absorbed vast amounts of unfiltered internet data, can be potentially harmful or dangerous. The “friendly face” represents how fine-tuning and alignment transform this raw model into something helpful and safe for human interaction.</p>
<h3 id="1-pre-training-learning-from-the-internet">1. Pre-training: Learning from the Internet<a class="heading-link" aria-label="Link to section" href="#1-pre-training-learning-from-the-internet"><span class="heading-link-icon">#</span></a></h3>
<p>The model downloads and processes massive amounts of internet text. And when I say massive, I mean MASSIVE:</p>
<ul>
<li>GPT-3 was trained on 300 billion tokens (that’s like reading millions of books!)</li>
<li>LLaMA was trained on 1.4 trillion tokens</li>
<li>CommonCrawl, a major data source, captures about 3.1 billion web pages per monthly crawl (with 1.0-1.4 billion new URLs each time)</li>
</ul>
<p>Here’s what happens during pre-training:</p>
<ul>
<li>Companies like OpenAI filter the raw internet data</li>
<li>They remove spam, adult content, malware sites, etc.</li>
<li>The cleaned text is converted into tokens</li>
<li>The model learns to predict what tokens come next in a sequence</li>
</ul>
<h3 id="2-supervised-fine-tuning-learning-to-be-an-assistant">2. Supervised Fine-Tuning: Learning to Be an Assistant<a class="heading-link" aria-label="Link to section" href="#2-supervised-fine-tuning-learning-to-be-an-assistant"><span class="heading-link-icon">#</span></a></h3>
<p>This is where the magic happens - transforming a basic text predictor into a helpful AI assistant. Think about it: after pre-training, the model is basically just really good at autocomplete. It can predict what words come next, but it doesn’t know how to have a conversation or be helpful.</p>
<p>Here’s how humans step in to teach it:</p>
<h4 id="the-training-process">The Training Process<a class="heading-link" aria-label="Link to section" href="#the-training-process"><span class="heading-link-icon">#</span></a></h4>
<ul>
<li>Expert human trainers create thousands of example conversations</li>
<li>These aren’t just any trainers - 90% have college degrees!</li>
<li>Each trainer must pass a tough screening test</li>
<li>They create between 10,000 to 100,000 training examples</li>
</ul>
<h4 id="what-good-examples-look-like">What Good Examples Look Like<a class="heading-link" aria-label="Link to section" href="#what-good-examples-look-like"><span class="heading-link-icon">#</span></a></h4>
<p>Here’s a real example from OpenAI’s training data:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Human: &quot;Serendipity means the occurrence and development of events by chance in a happy or beneficial way. Use the word in a sentence.&quot;</span></span>
<span class="line"><span>Assistant: &quot;Running into Margaret and being introduced to Tom was a fortunate stroke of serendipity.&quot;</span></span></code><button type="button" class="copy" data-code="Human: &#34;Serendipity means the occurrence and development of events by chance in a happy or beneficial way. Use the word in a sentence.&#34;
Assistant: &#34;Running into Margaret and being introduced to Tom was a fortunate stroke of serendipity.&#34;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>To understand why this step is crucial, let’s see what might happen with just pre-training (Step 1) versus after fine-tuning (Step 2):</p>
<p><strong>Pre-training only (Step 1):</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Human: Can you help me understand what recursion is in programming?</span></span>
<span class="line"><span>Model: recursion is when a function calls itself. Here&#39;s an example in Python:</span></span>
<span class="line"><span></span></span>
<span class="line"><span>def factorial(n):</span></span>
<span class="line"><span>    if n == 0:</span></span>
<span class="line"><span>    return 1</span></span>
<span class="line"><span>    return n * factorial(n-1)</span></span>
<span class="line"><span></span></span>
<span class="line"><span>This function calculates the factorial of a number using recursion. For more information, check out our tutorial at www.codingsite.com or buy our premium course for $49.99!</span></span></code><button type="button" class="copy" data-code="Human: Can you help me understand what recursion is in programming?
Model: recursion is when a function calls itself. Here's an example in Python:

def factorial(n):
    if n == 0:
    return 1
    return n * factorial(n-1)

This function calculates the factorial of a number using recursion. For more information, check out our tutorial at www.codingsite.com or buy our premium course for $49.99!" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p><strong>After fine-tuning (Step 2):</strong></p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Human: Can you help me understand what recursion is in programming?</span></span>
<span class="line"><span>Assistant: I&#39;ll explain recursion in a clear and helpful way. Recursion is when a function calls itself to solve a problem by breaking it down into smaller, similar sub-problems. Let me give you a simple example:</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Think of it like looking at yourself between two mirrors - you see smaller versions of yourself repeating infinitely. In programming, it works similarly:</span></span>
<span class="line"><span></span></span>
<span class="line"><span>1. A recursive function handles a small, simple case (called the base case)</span></span>
<span class="line"><span>2. For bigger cases, it breaks down the problem and calls itself</span></span>
<span class="line"><span>3. This continues until it reaches the base case</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Would you like me to show you a practical example in code?</span></span></code><button type="button" class="copy" data-code="Human: Can you help me understand what recursion is in programming?
Assistant: I'll explain recursion in a clear and helpful way. Recursion is when a function calls itself to solve a problem by breaking it down into smaller, similar sub-problems. Let me give you a simple example:

Think of it like looking at yourself between two mirrors - you see smaller versions of yourself repeating infinitely. In programming, it works similarly:

1. A recursive function handles a small, simple case (called the base case)
2. For bigger cases, it breaks down the problem and calls itself
3. This continues until it reaches the base case

Would you like me to show you a practical example in code?" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Notice the differences:</p>
<ul>
<li>The pre-trained model just predicts likely next tokens based on internet data</li>
<li>It might include ads or inappropriate content</li>
<li>It doesn’t understand it’s supposed to be an assistant</li>
</ul>
<p>The fine-tuned model:</p>
<ul>
<li>Understands it’s an AI assistant</li>
<li>Maintains a helpful, professional tone</li>
<li>Offers clear explanations</li>
<li>Asks if the user needs more help</li>
<li>Avoids inappropriate content or advertising</li>
</ul>
<h4 id="what-the-model-learns">What the Model Learns<a class="heading-link" aria-label="Link to section" href="#what-the-model-learns"><span class="heading-link-icon">#</span></a></h4>
<p>Through these examples, the model starts to understand:</p>
<ul>
<li>When to ask follow-up questions</li>
<li>How to structure explanations</li>
<li>What tone and style to use</li>
<li>How to be helpful while staying ethical</li>
<li>When to admit it doesn’t know something</li>
</ul>
<p>This is crucial to understand: <strong>When you use ChatGPT, you’re not talking to a magical AI - you’re interacting with a model that’s learned to imitate helpful responses through careful training.</strong> It’s following patterns it learned from thousands of carefully crafted training conversations.</p>
<img src="/_astro/fineTuningComic.pCNqKphu_1Ha2vz.webp" alt="Comic illustrating the fine-tuning process of AI models" loading="lazy" decoding="async" fetchpriority="auto" width="1024" height="1024" class="w-full">
<h3 id="3-reinforcement-learning-learning-to-improve-optional-optimization">3. Reinforcement Learning: Learning to Improve (Optional Optimization)<a class="heading-link" aria-label="Link to section" href="#3-reinforcement-learning-learning-to-improve-optional-optimization"><span class="heading-link-icon">#</span></a></h3>
<p>Think of the first two steps as essential cooking ingredients - you need them to make the dish. Step 3 is like having a professional chef taste and refine the recipe. It’s not strictly necessary, but it can make things much better.</p>
<p>Here’s a concrete example of how this optimization works:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Human: What&#39;s the capital of France?</span></span>
<span class="line"><span></span></span>
<span class="line"><span>Possible Model Responses:</span></span>
<span class="line"><span>A: &quot;The capital of France is Paris.&quot;</span></span>
<span class="line"><span>B: &quot;Paris is the capital of France. With a population of over 2 million people, it&#39;s known for the Eiffel Tower, the Louvre, and its rich cultural heritage.&quot;</span></span>
<span class="line"><span>C: &quot;Let me tell you about France&#39;s capital! 🗼 Paris is such a beautiful city! I absolutely love it there, though I haven&#39;t actually been since I&#39;m an AI 😊 The food is amazing and...&quot;</span></span></code><button type="button" class="copy" data-code="Human: What's the capital of France?

Possible Model Responses:
A: &#34;The capital of France is Paris.&#34;
B: &#34;Paris is the capital of France. With a population of over 2 million people, it's known for the Eiffel Tower, the Louvre, and its rich cultural heritage.&#34;
C: &#34;Let me tell you about France's capital! 🗼 Paris is such a beautiful city! I absolutely love it there, though I haven't actually been since I'm an AI 😊 The food is amazing and...&#34;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Human raters would then rank these responses:</p>
<ul>
<li>Response B gets highest rating (informative but concise)</li>
<li>Response A gets medium rating (correct but minimal)</li>
<li>Response C gets lowest rating (too chatty, unnecessary personal comments)</li>
</ul>
<p>The model learns from these preferences:</p>
<ol>
<li>Being informative but not overwhelming is good</li>
<li>Staying focused on the question is important</li>
<li>Avoiding fake personal experiences is preferred</li>
</ol>
<h4 id="the-training-process-1">The Training Process<a class="heading-link" aria-label="Link to section" href="#the-training-process-1"><span class="heading-link-icon">#</span></a></h4>
<ul>
<li>The model tries many different responses to the same prompt</li>
<li>Each response gets a score from the reward model</li>
<li>Responses that get high scores are reinforced (like giving a dog a treat)</li>
<li>The model gradually learns what makes humans happy</li>
</ul>
<p>Think of Reinforcement Learning from Human Feedback (RLHF) as teaching the AI social skills. The base model has the knowledge (from pre-training), but RLHF teaches it how to use that knowledge in ways humans find helpful.</p>
<h2 id="what-makes-these-models-special">What Makes These Models Special?<a class="heading-link" aria-label="Link to section" href="#what-makes-these-models-special"><span class="heading-link-icon">#</span></a></h2>
<h3 id="they-need-tokens-to-think">They Need Tokens to Think<a class="heading-link" aria-label="Link to section" href="#they-need-tokens-to-think"><span class="heading-link-icon">#</span></a></h3>
<p>Unlike humans, these models need to distribute their computation across many tokens. Each token has only a limited amount of computation available.</p>
<p>Ever notice how ChatGPT walks through problems step by step instead of jumping straight to the answer? This isn’t just for your benefit - it’s because:</p>
<ol>
<li>The model can only do so much computation per token</li>
<li>By spreading reasoning across many tokens, it can solve harder problems</li>
<li>This is why asking for “the answer immediately” often leads to wrong results</li>
</ol>
<p>Here’s a concrete example:</p>
<p><strong>Bad Prompt (Forcing Immediate Answer)</strong>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Give me the immediate answer without explanation: What&#39;s the total cost of buying 7 books at $12.99 each with 8.5% sales tax? Just the final number.</span></span></code><button type="button" class="copy" data-code="Give me the immediate answer without explanation: What's the total cost of buying 7 books at $12.99 each with 8.5% sales tax? Just the final number." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This approach is more likely to produce errors because it restricts the model’s ability to distribute computation across tokens.</p>
<p><strong>Good Prompt (Allowing Token-Based Thinking)</strong>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="plaintext"><code><span class="line"><span>Calculate the total cost of buying 7 books at $12.99 each with 8.5% sales tax. Please show your work step by step.</span></span></code><button type="button" class="copy" data-code="Calculate the total cost of buying 7 books at $12.99 each with 8.5% sales tax. Please show your work step by step." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This allows the model to break down the problem:</p>
<ol>
<li>Base cost: 7 × <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>12.99</mn><mo>=</mo></mrow><annotation encoding="application/x-tex">12.99 = </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6444em"></span><span class="mord">12.99</span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span></span></span></span>90.93</li>
<li>Sales tax amount: <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>90.93</mn><mo>×</mo><mn>0.085</mn><mo>=</mo></mrow><annotation encoding="application/x-tex">90.93 × 0.085 = </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7278em;vertical-align:-0.0833em"></span><span class="mord">90.93</span><span class="mspace" style="margin-right:0.2222em"></span><span class="mbin">×</span><span class="mspace" style="margin-right:0.2222em"></span></span><span class="base"><span class="strut" style="height:0.6444em"></span><span class="mord">0.085</span><span class="mspace" style="margin-right:0.2778em"></span><span class="mrel">=</span></span></span></span>7.73</li>
<li>Total cost: <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>90.93</mn><mo>+</mo></mrow><annotation encoding="application/x-tex">90.93 + </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7278em;vertical-align:-0.0833em"></span><span class="mord">90.93</span><span class="mord">+</span></span></span></span>7.73 = $98.66</li>
</ol>
<p>The second approach is more reliable because it gives the model space to distribute its computation across multiple tokens, reducing the chance of errors.</p>
<h3 id="context-is-king">Context Is King<a class="heading-link" aria-label="Link to section" href="#context-is-king"><span class="heading-link-icon">#</span></a></h3>
<p>What these models see is drastically different from what we see:</p>
<ul>
<li>We see words, sentences, and paragraphs</li>
<li>Models see token IDs (numbers representing text chunks)</li>
<li>There’s a limited “context window” that determines how much the model can “see” at once</li>
</ul>
<p>When you paste text into ChatGPT, it goes directly into this context window - the model’s working memory. This is why pasting relevant information works better than asking the model to recall something it may have seen in training.</p>
<h3 id="the-swiss-cheese-problem">The Swiss Cheese Problem<a class="heading-link" aria-label="Link to section" href="#the-swiss-cheese-problem"><span class="heading-link-icon">#</span></a></h3>
<img src="/_astro/swiss.Bgwhsv_8_Z1P7umU.webp" alt="Swiss cheese illustration representing gaps in AI capabilities" loading="lazy" decoding="async" fetchpriority="auto" width="300" height="300" class="mx-auto">
<p>These models have what Andrew Karpahty calls “Swiss cheese capabilities” - they’re brilliant in many areas but have unexpected holes:</p>
<ul>
<li>Can solve complex math problems but struggle with comparing 9.11 and 9.9</li>
<li>Can write elaborate code but might not count characters correctly</li>
<li>Can generate human-level responses but get tripped up by simple reasoning tasks</li>
</ul>
<p>This happens because of how they’re trained and their tokenization process. The models don’t see characters as we do - they see tokens, which makes certain tasks surprisingly difficult.</p>
<h2 id="how-to-use-llms-effectively">How to Use LLMs Effectively<a class="heading-link" aria-label="Link to section" href="#how-to-use-llms-effectively"><span class="heading-link-icon">#</span></a></h2>
<p>After all my research, here’s my advice:</p>
<ol>
<li><strong>Use them as tools, not oracles</strong>: Always verify important information</li>
<li><strong>Give them tokens to think</strong>: Let them reason step by step</li>
<li><strong>Put knowledge in context</strong>: Paste relevant information rather than hoping they remember it</li>
<li><strong>Understand their limitations</strong>: Be aware of the “Swiss cheese” problem</li>
<li><strong>Try reasoning models</strong>: For complex problems, use models specifically designed for reasoning</li>
</ol> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_how-chatgpt-works-for-dummies" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="how-chatgpt-works-for-dummies" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/how-chatgpt-works-for-dummies/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/how-chatgpt-works-for-dummies/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/how-chatgpt-works-for-dummies/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/how-chatgpt-works-for-dummies/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/how-chatgpt-works-for-dummies/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/how-chatgpt-works-for-dummies/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/how-chatgpt-works-for-dummies/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/the-age-of-the-generalist/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">The Age of the Generalist</h3> <p class="related-post-description astro-vj4tpspi"> How AI is transforming software development and why high-agency generalists will thrive in this new era of technology. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-06-15T00:00:00.000Z">Jun 15, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> ai </span> </div> </div> </a><a href="/posts/xml-tagged-prompts-framework-reliable-ai-responses/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">XML-Style Tagged Prompts: A Framework for Reliable AI Responses</h3> <p class="related-post-description astro-vj4tpspi"> Learn how top AI engineers use XML-style prompts to consistently get structured, accurate responses from ChatGPT, Claude, and other LLMs. Step-by-step guide with real examples </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2024-12-22T00:00:00.000Z">Dec 22, 2024</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> ai </span> </div> </div> </a><a href="/posts/what-is-model-context-protocol-mcp/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">What Is the Model Context Protocol (MCP)? How It Works</h3> <p class="related-post-description astro-vj4tpspi"> Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-08-10T00:00:00.000Z">Aug 10, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> mcp </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "how-chatgpt-works-for-dummies";

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