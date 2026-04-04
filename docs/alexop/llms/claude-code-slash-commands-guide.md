# Source: https://alexop.dev/posts/claude-code-slash-commands-guide

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/claude-code-slash-commands-guide/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>How to Speed Up Your Claude Code Experience with Slash Commands | alexop.dev</title><meta name="title" content="How to Speed Up Your Claude Code Experience with Slash Commands | alexop.dev"><meta name="description" content="Learn how to transform Claude Code from a chatbot into a deterministic engine using Slash Commands. This guide covers the technical setup and a complete 'Full Circle' workflow that automates your entire feature lifecycle."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="How to Speed Up Your Claude Code Experience with Slash Commands | alexop.dev"><meta property="og:description" content="Learn how to transform Claude Code from a chatbot into a deterministic engine using Slash Commands. This guide covers the technical setup and a complete 'Full Circle' workflow that automates your entire feature lifecycle."><meta property="og:url" content="https://alexop.dev/posts/claude-code-slash-commands-guide/"><meta property="og:image" content="https://alexop.dev/posts/how-to-speed-up-your-claude-code-experience-with-slash-commands/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-11-22T00:00:00.000Z"><meta property="article:modified_time" content="2025-11-22T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/claude-code-slash-commands-guide/"><meta property="twitter:title" content="How to Speed Up Your Claude Code Experience with Slash Commands | alexop.dev"><meta property="twitter:description" content="Learn how to transform Claude Code from a chatbot into a deterministic engine using Slash Commands. This guide covers the technical setup and a complete 'Full Circle' workflow that automates your entire feature lifecycle."><meta property="twitter:image" content="https://alexop.dev/posts/how-to-speed-up-your-claude-code-experience-with-slash-commands/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"How to Speed Up Your Claude Code Experience with Slash Commands | alexop.dev","description":"Learn how to transform Claude Code from a chatbot into a deterministic engine using Slash Commands. This guide covers the technical setup and a complete 'Full Circle' workflow that automates your entire feature lifecycle.","image":"https://alexop.dev/posts/how-to-speed-up-your-claude-code-experience-with-slash-commands/index.png","datePublished":"2025-11-22T00:00:00.000Z","dateModified":"2025-11-22T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: how-to-speed-up-your-claude-code-experience-with-slash-commands; }@layer astro { ::view-transition-old(how-to-speed-up-your-claude-code-experience-with-slash-commands) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(how-to-speed-up-your-claude-code-experience-with-slash-commands) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(how-to-speed-up-your-claude-code-experience-with-slash-commands) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(how-to-speed-up-your-claude-code-experience-with-slash-commands) { 
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
	animation-name: astroFadeIn; }</style><style>.alert:where(.astro-7kdbuayl){margin-top:1.5rem;margin-bottom:1.5rem;border-radius:.5rem;border-left-width:4px;background-color:rgba(var(--color-card),var(--tw-bg-opacity, 1));--tw-bg-opacity: .5;padding:1rem}.alert-title:where(.astro-7kdbuayl){margin-bottom:.5rem;display:flex;align-items:center;gap:.5rem;font-weight:700;--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1))}.alert-icon:where(.astro-7kdbuayl){font-size:1.25rem;line-height:1.75rem}.alert-content:where(.astro-7kdbuayl){--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1))}.alert-content:where(.astro-7kdbuayl) :where(.astro-7kdbuayl):is(:where(p):not(:where([class~=not-prose],[class~=not-prose] *))){margin-top:0}.alert-note:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .6 }.alert-tip:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .7 }.alert-important:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: 1 }.alert-warning:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .8 }.alert-caution:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .9 }.alert-definition:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .5 }.alert-github:where(.astro-7kdbuayl){border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-border-opacity: .75 }
</style><style>:root{--color-skin-card: rgb(var(--color-card));--color-skin-card-muted: rgb(var(--color-card-muted));--color-skin-border: rgb(var(--color-border));--color-skin-text-base: rgb(var(--color-text-base));--color-skin-accent: rgb(var(--color-accent));--color-skin-note: rgb(59, 130, 246);--color-skin-tip: rgb(16, 185, 129);--color-skin-caution: rgb(245, 158, 11);--color-skin-danger: rgb(239, 68, 68);--color-skin-info: rgb(99, 102, 241)}.aside:where(.astro-37uy2q7c){background-color:var(--color-skin-card);border-left:4px solid;border-radius:.5rem;box-shadow:0 4px 6px -1px #0000001a,0 2px 4px -1px #0000000f;margin:1.5rem 0;transition:all .3s ease}.aside:where(.astro-37uy2q7c):hover{box-shadow:0 10px 15px -3px #0000001a,0 4px 6px -2px #0000000d}.aside-content:where(.astro-37uy2q7c){padding:1rem 1.5rem}.aside-title:where(.astro-37uy2q7c){display:flex;align-items:center;font-weight:700;font-size:1.1rem;margin-bottom:.75rem}.aside-emoji:where(.astro-37uy2q7c){font-size:1.4rem;margin-right:.75rem}.aside-body:where(.astro-37uy2q7c){color:var(--color-skin-text-base);font-size:.95rem;line-height:1.6}.aside-note:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-note),.1);border-left-color:var(--color-skin-note)}.aside-note:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-note)}.aside-tip:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-tip),.1);border-left-color:var(--color-skin-tip)}.aside-tip:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-tip)}.aside-caution:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-caution),.1);border-left-color:var(--color-skin-caution)}.aside-caution:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-caution)}.aside-danger:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-danger),.1);border-left-color:var(--color-skin-danger)}.aside-danger:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-danger)}.aside-info:where(.astro-37uy2q7c){background-color:rgba(var(--color-skin-info),.1);border-left-color:var(--color-skin-info)}.aside-info:where(.astro-37uy2q7c) .aside-title:where(.astro-37uy2q7c){color:var(--color-skin-info)}
</style><style>.file-tree__item:where(.astro-o25vlg2d){margin:0;padding:0;position:relative}.file-tree__item:where(.astro-o25vlg2d):before{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:0;bottom:0;width:1px;background:rgba(var(--color-text-base),.15)}.file-tree__item:where(.astro-o25vlg2d):last-child:before{bottom:50%}.file-tree__item:where(.astro-o25vlg2d):after{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:50%;width:.75rem;height:1px;background:rgba(var(--color-text-base),.15)}.file-tree__folder:where(.astro-o25vlg2d){margin:0;padding:0}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d){list-style:none;cursor:pointer;display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}.file-tree__folder:where(.astro-o25vlg2d)[open]>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(90deg)}.file-tree__folder:where(.astro-o25vlg2d):not([open])>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(0)}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d)::-webkit-details-marker{display:none}.file-tree__list:where(.astro-o25vlg2d){list-style:none;margin:0;padding:0}.file-tree__file:where(.astro-o25vlg2d){display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;text-decoration:none;color:inherit;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__file:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}a:where(.astro-o25vlg2d).file-tree__file:hover .file-tree__name:where(.astro-o25vlg2d){color:rgb(var(--color-accent))}.file-tree__icon:where(.astro-o25vlg2d){width:1rem;height:1rem;flex-shrink:0;color:rgba(var(--color-text-base),.4);display:inline-flex;align-items:center;justify-content:center}.file-tree__icon--file:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.4)}.file-tree__icon--colored:where(.astro-o25vlg2d){color:inherit}.file-tree__icon--text:where(.astro-o25vlg2d){font-weight:600;font-size:.875rem;display:inline-flex;align-items:center;justify-content:center;width:1rem;height:1rem}.file-tree__name:where(.astro-o25vlg2d){white-space:nowrap;transition:color .15s ease;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace}.file-tree__comment:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.5);font-style:italic;margin-left:.5rem;white-space:nowrap;font-size:.9em}.file-tree__caret:where(.astro-o25vlg2d){width:.75rem;height:.75rem;transition:transform .2s ease;flex-shrink:0;color:rgba(var(--color-text-base),.5);font-size:.625rem;display:inline-flex;align-items:center;justify-content:center;transform-origin:center}
</style><style>.file-tree:where(.astro-htwbjus4){font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;font-size:.8125rem;background:rgb(var(--color-card));color:rgb(var(--color-text-base));border:1px solid rgba(var(--color-border),.5);border-radius:.5rem;padding:.75rem;margin:1.5rem 0;overflow-x:auto}.file-tree__list:where(.astro-htwbjus4){list-style:none;margin:0;padding:0}.file-tree__list:where(.astro-htwbjus4)>li:where(.astro-htwbjus4):first-child:before,.file-tree__list:where(.astro-htwbjus4)>li:where(.astro-htwbjus4):first-child:after{display:none}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar{height:.5rem}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-track{background:rgb(var(--color-fill))}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-thumb{background:rgb(var(--color-border));border-radius:.25rem}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-thumb:hover{background:rgb(var(--color-card-muted))}
</style><style>.internal-link-wrapper:where(.astro-3tyn5ojg){position:relative;display:inline-block}.internal-link:where(.astro-3tyn5ojg){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));text-decoration-line:underline;text-decoration-style:dashed;text-decoration-thickness:1px;text-underline-offset:4px;transition-property:all;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.internal-link:where(.astro-3tyn5ojg):hover{text-decoration-style:solid}.internal-link:where(.astro-3tyn5ojg){cursor:pointer;display:inline}.preview-card:where(.astro-3tyn5ojg){display:block;position:absolute;bottom:calc(100% + 8px);left:50%;transform:translate(-50%);z-index:9999;width:320px;max-width:90vw;border-radius:.5rem;border-width:1px;--tw-border-opacity: 1;border-color:rgba(var(--color-border),var(--tw-border-opacity, 1));--tw-bg-opacity: 1;background-color:rgba(var(--color-card),var(--tw-bg-opacity, 1));--tw-shadow: 0 10px 15px -3px rgb(0 0 0 / .1), 0 4px 6px -4px rgb(0 0 0 / .1);--tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000),var(--tw-ring-shadow, 0 0 #0000),var(--tw-shadow);opacity:0;visibility:hidden;transition:opacity .2s ease-in-out,visibility .2s ease-in-out}.preview-card:where(.astro-3tyn5ojg).is-fixed{position:fixed!important;bottom:auto!important;top:var(--pc-top, 0px)!important;left:var(--pc-left, 0px)!important;transform:none!important}.preview-content:where(.astro-3tyn5ojg){display:block;padding:1rem}.preview-title:where(.astro-3tyn5ojg){display:block;margin-bottom:.5rem;font-size:1rem;line-height:1.5rem;font-weight:600;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1));line-height:1.3}.preview-title:where(.astro-3tyn5ojg) .heading-link:where(.astro-3tyn5ojg){display:none!important}.preview-description:where(.astro-3tyn5ojg){display:block;margin-bottom:.75rem;font-size:.875rem;line-height:1.25rem;color:rgba(var(--color-text-base),.8);line-height:1.4;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}.preview-tags:where(.astro-3tyn5ojg){margin-bottom:.5rem;display:flex;flex-wrap:wrap;gap:.375rem}.preview-tag:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;background-color:rgba(var(--color-accent),.1);--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));font-weight:500}.preview-tag-more:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;--tw-bg-opacity: 1;background-color:rgba(var(--color-fill),var(--tw-bg-opacity, 1));color:rgba(var(--color-text-base),.6);font-weight:500}.preview-date:where(.astro-3tyn5ojg){font-size:.75rem;line-height:1rem;color:rgba(var(--color-text-base),.6);display:block;margin-top:8px;font-style:italic}.preview-card:where(.astro-3tyn5ojg):after{content:"";position:absolute;top:100%;left:50%;transform:translate(-50%);border:6px solid transparent;border-top-color:var(--color-card)}.preview-card:where(.astro-3tyn5ojg).is-fixed:after{display:none}
</style><style>.prompt-link:where(.astro-7tc5uzmh){margin-top:1.5rem;margin-bottom:1.5rem;display:block;border-radius:.5rem;border-width:1px;--tw-border-opacity: 1;border-color:rgba(var(--color-border),var(--tw-border-opacity, 1));--tw-bg-opacity: 1;background-color:rgba(var(--color-card),var(--tw-bg-opacity, 1));padding:1rem;text-decoration-line:none;transition-property:all;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.2s}.prompt-link:where(.astro-7tc5uzmh):hover{--tw-border-opacity: 1;border-color:rgba(var(--color-accent),var(--tw-border-opacity, 1));--tw-bg-opacity: .8 }.prompt-link-header:where(.astro-7tc5uzmh){display:flex;align-items:center;gap:.5rem;font-size:.875rem;line-height:1.25rem;font-weight:600;--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1))}.prompt-link-icon:where(.astro-7tc5uzmh){font-size:1.125rem;line-height:1.75rem}.prompt-link-title:where(.astro-7tc5uzmh){flex:1 1 0%}.prompt-link-arrow:where(.astro-7tc5uzmh){font-size:.75rem;line-height:1rem;opacity:.6;transition-property:transform;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.2s}.prompt-link:where(.astro-7tc5uzmh):hover .prompt-link-arrow:where(.astro-7tc5uzmh){--tw-translate-x: .125rem;--tw-translate-y: -.125rem;transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skew(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));opacity:1}.prompt-link-content:where(.astro-7tc5uzmh){margin-top:.5rem;font-size:.875rem;line-height:1.25rem;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1));opacity:.9}
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: ai; }@layer astro { ::view-transition-old(ai) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: claude-code; }@layer astro { ::view-transition-old(claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(claude-code) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(claude-code) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">How to Speed Up Your Claude Code Experience with Slash Commands</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-11-22T00:00:00.000Z">Nov 22, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="1ktlfA" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;How to Speed Up Your Claude Code Experience with Slash Commands&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport Aside from \&quot;@features/mdx-components/components/Aside.astro\&quot;;\nimport PromptLink from \&quot;@features/prompts/components/PromptLink.astro\&quot;;\nimport FileTree from \&quot;@features/filetree/components/FileTree.astro\&quot;;\nimport Figure from \&quot;@features/mdx-components/components/Figure.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport promptSlash from \&quot;@assets/images/claude/promptSlash.png\&quot;;\nimport terminalTest from \&quot;@assets/images/claude/terminalTest.png\&quot;;\n\nI was wasting time. Every commit message, every branch name, every PR description. I typed the same things over and over.\nThen I discovered Slash Commands in Claude Code. Now I type `/commit` and it writes the message for me. `/branch \&quot;add dark mode\&quot;` and it creates `feat/add-dark-mode`. `/pr` and it generates a full PR description from my commits.\nThis post shows you how to build the same workflow. I&#39;ll cover how Slash Commands work, then we&#39;ll build a complete system that automates your entire git lifecycle.\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;Related Reading\&quot;&gt;\nSlash Commands are just one piece of the Claude Code puzzle. For the full picture—including MCP, hooks, subagents, and skills—see my &lt;InternalLink slug=\&quot;understanding-claude-code-full-stack\&quot;&gt;comprehensive guide to Claude Code&#39;s feature stack&lt;/InternalLink&gt;.\n&lt;/Aside&gt;\n\n&lt;Figure src={terminalTest} alt=\&quot;Claude Code executing /branch command showing git operations\&quot; caption=\&quot;The /branch command creates a feature branch automatically\&quot; /&gt;\n\n&lt;Alert type=\&quot;important\&quot; title=\&quot;Prerequisites\&quot;&gt;\nYou need Git and the GitHub CLI (`gh`). Install `gh` with `brew install gh` on macOS or check [cli.github.com](https://cli.github.com). Run `gh auth login` to authenticate.\n\nWithout `gh`, commands like `/pr` and `/fix-pipeline` will not work.\n&lt;/Alert&gt;\n\n\n## Two things you need to know\n\nBefore we build the workflow, you need to understand two features.\n\n### Bash command execution\n\nWrite `!git status` inside a command file. Claude runs the command first, captures the output, and injects it into the prompt. The AI sees the result before it starts thinking.\n\nThis is how `/commit` knows what you changed. It runs `!git diff` automatically. See the [official documentation](https://docs.anthropic.com/en/docs/claude-code/slash-commands#bash-command-execution) for more details.\n\n### Model selection\n\nYou don&#39;t need a powerful model to fix a missing semicolon.\nClaude Code lets you pick the model in the frontmatter:\n\n- `sonnet` — for complex reasoning (default)\n- `haiku` — fast and cheap\n\nAdd `model: haiku` and commands run almost instantly.\n\n## Command structure\n\nSlash commands are Markdown files stored in `.claude/commands/` (project-level) or `~/.claude/commands/` (personal). The filename becomes the command name: `commit.md` becomes `/commit`.\n\n&lt;FileTree\n  tree={[\n    {\n      name: \&quot;my-project\&quot;,\n      open: true,\n      children: [\n        {\n          name: \&quot;.claude\&quot;,\n          open: true,\n          children: [\n            { name: \&quot;settings.json\&quot;, comment: \&quot;project settings\&quot; },\n            {\n              name: \&quot;commands\&quot;,\n              open: true,\n              children: [\n                { name: \&quot;branch.md\&quot;, comment: \&quot;/branch\&quot; },\n                { name: \&quot;commit.md\&quot;, comment: \&quot;/commit\&quot; },\n                { name: \&quot;pr.md\&quot;, comment: \&quot;/pr\&quot; },\n                { name: \&quot;lint.md\&quot;, comment: \&quot;/lint\&quot; },\n              ],\n            },\n          ],\n        },\n        { name: \&quot;src\&quot; },\n        { name: \&quot;package.json\&quot; },\n      ],\n    },\n  ]}\n/&gt;\n\nHere is a complete example:\n\n```markdown\n---\ndescription: Create a git commit with a conventional message\nallowed-tools: Bash(git add:*), Bash(git commit:*)\nargument-hint: [message]\nmodel: haiku\n---\n\n# Commit Changes\n\n&lt;git_diff&gt;\n!`git diff --cached`\n&lt;/git_diff&gt;\n\nCreate a commit message following Conventional Commits.\nIf $ARGUMENTS is provided, use it as the commit message.\n```\n\n&lt;Figure src={promptSlash} alt=\&quot;Claude Code slash command autocomplete showing available commands\&quot; caption=\&quot;Slash commands appear in autocomplete when you type /\&quot; /&gt;\n\n### Frontmatter options\n\n| Option | Purpose | Default |\n|--------|---------|---------|\n| `description` | Brief description shown in `/help` | First line of prompt |\n| `allowed-tools` | Tools the command can use | Inherits from conversation |\n| `model` | Model to use (`sonnet`, `haiku`, or full model ID) | Inherits from conversation |\n| `argument-hint` | Shows expected arguments in autocomplete | None |\n\n### Arguments\n\nUse `$ARGUMENTS` to capture everything passed to the command:\n\n```markdown\nCreate a branch named: $ARGUMENTS\n```\n\nFor multiple arguments, use positional parameters `$1`, `$2`, etc:\n\n```markdown\n---\nargument-hint: [pr-number] [priority]\n---\n\nReview PR #$1 with priority $2.\n```\n\n### File references\n\nInclude file contents with the `@` prefix:\n\n```markdown\nReview the implementation in @src/utils/helpers.js\n```\n\n## The workflow\n\nI replaced my manual git rituals with custom commands. They live in `.claude/commands/`. Here is how I drive a feature from start to merge.\n\n```mermaid\n---\ntitle: Development Workflow\n---\nflowchart LR\n    %% Initial Setup\n    Start((Start)) --&gt; Branch[\&quot;/branch\&quot;]\n    Branch --&gt; Code[Write Code]\n\n    %% Local Iteration Loop\n    Code --&gt; Lint[\&quot;/lint&lt;br/&gt;(Haiku)\&quot;]\n    Lint -- \&quot;Auto-fix\&quot; --&gt; Lint\n    Lint --&gt; Test[\&quot;/vitest&lt;br/&gt;(Haiku)\&quot;]\n    Test -- \&quot;Fix Failure\&quot; --&gt; Test\n    \n    %% Deployment Flow\n    Test --&gt; Push[\&quot;/push\&quot;]\n    Push --&gt; PR[\&quot;/pr\&quot;]\n    PR --&gt; CI{CI Pass?}\n\n    %% CI Debugging Loop\n    CI -- \&quot;No\&quot; --&gt; Fix[\&quot;/fix-pipeline&lt;br/&gt;(Sonnet)\&quot;]\n    Fix -- \&quot;Fix &amp; Push\&quot; --&gt; CI\n\n    %% Final Review &amp; Merge\n    CI -- \&quot;Yes\&quot; --&gt; Review[\&quot;/review-coderabbit\&quot;]\n    Review --&gt; Merge[\&quot;/merge-to-main\&quot;]\n    Merge --&gt; Done((Done))\n```\n\n### /branch — start a task\n\n&lt;PromptLink href=\&quot;/prompts/claude/claude-branch-command\&quot;&gt;\nI type `/branch \&quot;implement dark mode toggle\&quot;` and Claude checks out main, pulls latest, and creates `feat/dark-mode-toggle`. No more thinking about naming conventions.\n&lt;/PromptLink&gt;\n\n### /lint — fix before commit\n\n&lt;PromptLink href=\&quot;/prompts/claude/claude-lint-command\&quot;&gt;\nI type `/lint`. It runs the linter with auto-fix, and if errors remain, Claude fixes them. Uses Haiku for speed—runs in about 20 seconds.\n&lt;/PromptLink&gt;\n\n### /vitest — run unit tests\n\n&lt;PromptLink href=\&quot;/prompts/claude/claude-vitest-command\&quot;&gt;\nI type `/vitest`. It runs the test suite and fixes any failures. The prompt tells Claude to fix the code, not the test—implementation should match expected behavior.\n&lt;/PromptLink&gt;\n\n### /commit — save your work\n\n&lt;PromptLink href=\&quot;/prompts/claude/claude-commit-command\&quot;&gt;\nI type `/commit`. Claude analyzes the diff, generates a Conventional Commit message, and commits. It looks at recent commits to match your project&#39;s style.\n&lt;/PromptLink&gt;\n\n### /push — commit and push in one step\n\n&lt;PromptLink href=\&quot;/prompts/claude/claude-push-command\&quot;&gt;\nI type `/push`. It stages everything, generates a commit message, commits, and pushes. My most-used command—one word and the code is on GitHub.\n&lt;/PromptLink&gt;\n\n### /fix-pipeline — fix failing CI tests\n\n&lt;PromptLink href=\&quot;/prompts/claude/claude-fix-pipeline-command\&quot;&gt;\nI type `/fix-pipeline`. It fetches the failed logs via `gh`, analyzes the error, and fixes it. Uses Sonnet because debugging requires reasoning. The prompt includes guardrails—Claude must read the actual error before proposing fixes.\n&lt;/PromptLink&gt;\n\n### /pr — create a pull request\n\n&lt;PromptLink href=\&quot;/prompts/claude/claude-pr-command\&quot;&gt;\nI type `/pr`. It analyzes all commits on the branch, generates a PR title and description, and opens it via `gh pr create`. Checks if a PR already exists first.\n&lt;/PromptLink&gt;\n\n### /review-coderabbit — address review comments\n\n&lt;PromptLink href=\&quot;/prompts/claude/claude-review-coderabbit-command\&quot;&gt;\nI type `/review-coderabbit`. It fetches CodeRabbit&#39;s comments via GraphQL, verifies each suggestion against the codebase, implements valid fixes or pushes back with reasoning, and resolves every thread. AI reviewers aren&#39;t always right—the prompt ensures Claude verifies before acting.\n&lt;/PromptLink&gt;\n\n### /merge-to-main — finish the task\n\n&lt;PromptLink href=\&quot;/prompts/claude/claude-merge-to-main-command\&quot;&gt;\nI type `/merge-to-main`. It squash merges the PR, deletes the branch, and pulls main. Done.\n&lt;/PromptLink&gt;\n\n## Summary\n\nBy moving your process into `.claude/commands/`, you are building a system.\n\n- Bash command execution injects real-time context\n- Model selection balances speed vs reasoning\n- The workflow automates branching, linting, committing, CI debugging, PRs, and merging\n\nDefine the process once. Claude executes it every time.\n\nWant to extend Claude Code even further? Connect external tools via &lt;InternalLink slug=\&quot;what-is-model-context-protocol-mcp\&quot;&gt;MCP (Model Context Protocol)&lt;/InternalLink&gt; or package your commands into a &lt;InternalLink slug=\&quot;building-my-first-claude-code-plugin\&quot;&gt;shareable plugin&lt;/InternalLink&gt;.\n\nI don&#39;t think about naming conventions, commit messages, or PR descriptions anymore. The commands handle it.\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Bonus: Shell aliases for even faster execution\&quot;&gt;\nYou can skip the interactive prompt entirely with `claude -p`. Add aliases to your `.zshrc` or `.bashrc`:\n\n```bash\nalias clint=\&quot;claude -p &#39;/lint&#39;\&quot;\nalias cpush=\&quot;claude -p &#39;/push&#39;\&quot;\nalias ccommit=\&quot;claude -p &#39;/commit&#39;\&quot;\nalias cbranch=\&quot;claude -p &#39;/branch&#39;\&quot;\n```\n\nNow `clint` runs the lint command without opening the interactive session. The `-p` flag passes the prompt directly—Claude executes and exits. Two steps become one keystroke.\n&lt;/Alert&gt;&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <p>I was wasting time. Every commit message, every branch name, every PR description. I typed the same things over and over.
Then I discovered Slash Commands in Claude Code. Now I type <code>/commit</code> and it writes the message for me. <code>/branch &quot;add dark mode&quot;</code> and it creates <code>feat/add-dark-mode</code>. <code>/pr</code> and it generates a full PR description from my commits.
This post shows you how to build the same workflow. I’ll cover how Slash Commands work, then we’ll build a complete system that automates your entire git lifecycle.</p>
<aside aria-label="Related Reading" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> Related Reading </p> <section class="aside-body astro-37uy2q7c"> <p>Slash Commands are just one piece of the Claude Code puzzle. For the full picture—including MCP, hooks, subagents, and skills—see my <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/understanding-claude-code-full-stack/" class="internal-link astro-3tyn5ojg"> comprehensive guide to Claude Code’s feature stack </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained</span> <span class="preview-description astro-3tyn5ojg">A practical guide to Claude Code&#39;s features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">mcp</span> <span class="preview-tag-more astro-3tyn5ojg">+2</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 9, 2025</time> </span> </span> </span>  <script>
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
</script>.</p> </section> </div> </aside> 
<figure class=" mx-auto "> <img src="/_astro/terminalTest.CG0bvubF_Z1zl0KE.webp" alt="Claude Code executing /branch command showing git operations" loading="lazy" decoding="async" fetchpriority="auto" width="1822" height="1754" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> The /branch command creates a feature branch automatically </figcaption> </figure>
<div class="alert alert-important astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">📢</span> Prerequisites </p> <div class="alert-content astro-7kdbuayl"> <p>You need Git and the GitHub CLI (<code>gh</code>). Install <code>gh</code> with <code>brew install gh</code> on macOS or check <a href="https://cli.github.com" rel="noopener noreferrer" target="_blank">cli.github.com</a>. Run <code>gh auth login</code> to authenticate.</p><p>Without <code>gh</code>, commands like <code>/pr</code> and <code>/fix-pipeline</code> will not work.</p> </div> </div> 
<h2 id="two-things-you-need-to-know">Two things you need to know<a class="heading-link" aria-label="Link to section" href="#two-things-you-need-to-know"><span class="heading-link-icon">#</span></a></h2>
<p>Before we build the workflow, you need to understand two features.</p>
<h3 id="bash-command-execution">Bash command execution<a class="heading-link" aria-label="Link to section" href="#bash-command-execution"><span class="heading-link-icon">#</span></a></h3>
<p>Write <code>!git status</code> inside a command file. Claude runs the command first, captures the output, and injects it into the prompt. The AI sees the result before it starts thinking.</p>
<p>This is how <code>/commit</code> knows what you changed. It runs <code>!git diff</code> automatically. See the <a href="https://docs.anthropic.com/en/docs/claude-code/slash-commands#bash-command-execution" rel="noopener noreferrer" target="_blank">official documentation</a> for more details.</p>
<h3 id="model-selection">Model selection<a class="heading-link" aria-label="Link to section" href="#model-selection"><span class="heading-link-icon">#</span></a></h3>
<p>You don’t need a powerful model to fix a missing semicolon.
Claude Code lets you pick the model in the frontmatter:</p>
<ul>
<li><code>sonnet</code> — for complex reasoning (default)</li>
<li><code>haiku</code> — fast and cheap</li>
</ul>
<p>Add <code>model: haiku</code> and commands run almost instantly.</p>
<h2 id="command-structure">Command structure<a class="heading-link" aria-label="Link to section" href="#command-structure"><span class="heading-link-icon">#</span></a></h2>
<p>Slash commands are Markdown files stored in <code>.claude/commands/</code> (project-level) or <code>~/.claude/commands/</code> (personal). The filename becomes the command name: <code>commit.md</code> becomes <code>/commit</code>.</p>
<nav class="file-tree astro-htwbjus4" aria-label="File tree"> <ul class="file-tree__list astro-htwbjus4"> <li class="file-tree__item astro-o25vlg2d" style="--level: 0;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">my-project</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">.claude</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d"> <span class="file-tree__icon file-tree__icon--text astro-o25vlg2d" style="color: #F59E0B" aria-hidden="true"> {} </span>   <span class="file-tree__name astro-o25vlg2d">settings.json</span> <span class="file-tree__comment astro-o25vlg2d">project settings</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">commands</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">branch.md</span> <span class="file-tree__comment astro-o25vlg2d">/branch</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">commit.md</span> <span class="file-tree__comment astro-o25vlg2d">/commit</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">pr.md</span> <span class="file-tree__comment astro-o25vlg2d">/pr</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">lint.md</span> <span class="file-tree__comment astro-o25vlg2d">/lint</span> </span> </li>  </ul> </details>   </li>  </ul> </details>   </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;">   <span class="file-tree__file astro-o25vlg2d">   <svg class="file-tree__icon file-tree__icon--file astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">src</span>  </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;">   <span class="file-tree__file astro-o25vlg2d"> <span class="file-tree__icon file-tree__icon--text astro-o25vlg2d" style="color: #F59E0B" aria-hidden="true"> {} </span>   <span class="file-tree__name astro-o25vlg2d">package.json</span>  </span> </li>  </ul> </details>   </li>  </ul> </nav> 
<p>Here is a complete example:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Create a git commit with a conventional message</span></span>
<span class="line"><span style="color:#F7768E">allowed-tools</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Bash(git add:*), Bash(git commit:*)</span></span>
<span class="line"><span style="color:#F7768E">argument-hint</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> [</span><span style="color:#9ECE6A">message</span><span style="color:#89DDFF">]</span></span>
<span class="line"><span style="color:#F7768E">model</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> haiku</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Commit Changes</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#DE5971">git_diff</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#9AA5CE">!`git diff --cached`</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#DE5971">git_diff</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Create a commit message following Conventional Commits.</span></span>
<span class="line"><span style="color:#9AA5CE">If $ARGUMENTS is provided, use it as the commit message.</span></span></code><button type="button" class="copy" data-code="---
description: Create a git commit with a conventional message
allowed-tools: Bash(git add:*), Bash(git commit:*)
argument-hint: [message]
model: haiku
---

# Commit Changes

<git_diff>
!`git diff --cached`
</git_diff>

Create a commit message following Conventional Commits.
If $ARGUMENTS is provided, use it as the commit message." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<figure class=" mx-auto "> <img src="/_astro/promptSlash.D3xG41Gd_Z2pbH79.webp" alt="Claude Code slash command autocomplete showing available commands" loading="lazy" decoding="async" fetchpriority="auto" width="2784" height="1536" class="w-full"> <figcaption class="mt-2 text-center text-sm text-gray-500"> Slash commands appear in autocomplete when you type / </figcaption> </figure>
<h3 id="frontmatter-options">Frontmatter options<a class="heading-link" aria-label="Link to section" href="#frontmatter-options"><span class="heading-link-icon">#</span></a></h3>






























<table><thead><tr><th>Option</th><th>Purpose</th><th>Default</th></tr></thead><tbody><tr><td data-label="Option"><code>description</code></td><td data-label="Purpose">Brief description shown in <code>/help</code></td><td data-label="Default">First line of prompt</td></tr><tr><td data-label="Option"><code>allowed-tools</code></td><td data-label="Purpose">Tools the command can use</td><td data-label="Default">Inherits from conversation</td></tr><tr><td data-label="Option"><code>model</code></td><td data-label="Purpose">Model to use (<code>sonnet</code>, <code>haiku</code>, or full model ID)</td><td data-label="Default">Inherits from conversation</td></tr><tr><td data-label="Option"><code>argument-hint</code></td><td data-label="Purpose">Shows expected arguments in autocomplete</td><td data-label="Default">None</td></tr></tbody></table>
<h3 id="arguments">Arguments<a class="heading-link" aria-label="Link to section" href="#arguments"><span class="heading-link-icon">#</span></a></h3>
<p>Use <code>$ARGUMENTS</code> to capture everything passed to the command:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#9AA5CE">Create a branch named: $ARGUMENTS</span></span></code><button type="button" class="copy" data-code="Create a branch named: $ARGUMENTS" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>For multiple arguments, use positional parameters <code>$1</code>, <code>$2</code>, etc:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">argument-hint</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> [</span><span style="color:#9ECE6A">pr-number</span><span style="color:#89DDFF">]</span><span style="color:#89DDFF"> [</span><span style="color:#9ECE6A">priority</span><span style="color:#89DDFF">]</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Review PR #$1 with priority $2.</span></span></code><button type="button" class="copy" data-code="---
argument-hint: [pr-number] [priority]
---

Review PR #$1 with priority $2." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="file-references">File references<a class="heading-link" aria-label="Link to section" href="#file-references"><span class="heading-link-icon">#</span></a></h3>
<p>Include file contents with the <code>@</code> prefix:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#9AA5CE">Review the implementation in @src/utils/helpers.js</span></span></code><button type="button" class="copy" data-code="Review the implementation in @src/utils/helpers.js" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="the-workflow">The workflow<a class="heading-link" aria-label="Link to section" href="#the-workflow"><span class="heading-link-icon">#</span></a></h2>
<p>I replaced my manual git rituals with custom commands. They live in <code>.claude/commands/</code>. Here is how I drive a feature from start to merge.</p>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:2207.09375px" viewBox="0 -50 2207.09375 356.57501220703125" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M71.172,185.575L75.339,185.575C79.505,185.575,87.839,185.575,95.505,185.575C103.172,185.575,110.172,185.575,113.672,185.575L117.172,185.575" id="L_Start_Branch_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Start_Branch_0" data-points="W3sieCI6NzEuMTcxODc1LCJ5IjoxODUuNTc1MDAwMDAxMTE3Nn0seyJ4Ijo5Ni4xNzE4NzUsInkiOjE4NS41NzUwMDAwMDExMTc2fSx7IngiOjEyMS4xNzE4NzUsInkiOjE4NS41NzUwMDAwMDExMTc2fV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M248.609,185.575L252.776,185.575C256.943,185.575,265.276,185.575,272.943,185.575C280.609,185.575,287.609,185.575,291.109,185.575L294.609,185.575" id="L_Branch_Code_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Branch_Code_0" data-points="W3sieCI6MjQ4LjYwOTM3NSwieSI6MTg1LjU3NTAwMDAwMTExNzZ9LHsieCI6MjczLjYwOTM3NSwieSI6MTg1LjU3NTAwMDAwMTExNzZ9LHsieCI6Mjk4LjYwOTM3NSwieSI6MTg1LjU3NTAwMDAwMTExNzZ9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M454.938,185.575L459.104,185.575C463.271,185.575,471.604,185.575,479.271,185.575C486.938,185.575,493.938,185.575,497.438,185.575L500.938,185.575" id="L_Code_Lint_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Code_Lint_0" data-points="W3sieCI6NDU0LjkzNzUsInkiOjE4NS41NzUwMDAwMDExMTc2fSx7IngiOjQ3OS45Mzc1LCJ5IjoxODUuNTc1MDAwMDAxMTE3Nn0seyJ4Ijo1MDQuOTM3NSwieSI6MTg1LjU3NTAwMDAwMTExNzZ9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M632.375,149.593L636.542,147.24C640.708,144.887,649.042,140.181,667.986,137.828C686.931,135.475,716.487,135.475,731.266,135.475L746.044,135.475" id="Lint-cyclic-special-1" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="Lint-cyclic-special-1" data-points="W3sieCI6NjMyLjM3NSwieSI6MTQ5LjU5MjY0NzA1ODg3MDl9LHsieCI6NjU3LjM3NSwieSI6MTM1LjQ3NDk5OTk5OTYyNzQ3fSx7IngiOjc0Ni4wNDM3NDk5OTkyNTQ5LCJ5IjoxMzUuNDc0OTk5OTk5NjI3NDd9XQ=="></path><path d="M746.144,135.475L767.344,135.475C788.544,135.475,830.944,135.475,871.738,140.902C912.533,146.329,951.722,157.182,971.316,162.609L990.911,168.036" id="Lint-cyclic-special-mid" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="Lint-cyclic-special-mid" data-points="W3sieCI6NzQ2LjE0Mzc1MDAwMDc0NTEsInkiOjEzNS40NzQ5OTk5OTk2Mjc0N30seyJ4Ijo4NzMuMzQzNzUsInkiOjEzNS40NzQ5OTk5OTk2Mjc0N30seyJ4Ijo5OTAuOTEwOTM3NDk5MjU0OSwieSI6MTY4LjAzNjE1MjEwOTQ3MjE0fV0="></path><path d="M990.911,168.055L971.316,170.046C951.722,172.037,912.533,176.018,871.73,178.009C830.927,180,788.51,180,752.516,180C716.521,180,686.948,180,668.66,180.22C650.372,180.44,643.37,180.88,639.868,181.1L636.367,181.32" id="Lint-cyclic-special-2" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="Lint-cyclic-special-2" data-points="W3sieCI6OTkwLjkxMDkzNzQ5OTI1NDksInkiOjE2OC4wNTUwODAwNDA2NzQzfSx7IngiOjg3My4zNDM3NSwieSI6MTgwfSx7IngiOjc0Ni4wOTM3NSwieSI6MTgwfSx7IngiOjY1Ny4zNzUsInkiOjE4MH0seyJ4Ijo2MzIuMzc1LCJ5IjoxODEuNTcwOTc1Njk1OTgyNH1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M615.413,224.575L622.407,230.408C629.401,236.242,643.388,247.908,653.881,253.742C664.375,259.575,671.375,259.575,674.875,259.575L678.375,259.575" id="L_Lint_Test_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Lint_Test_0" data-points="W3sieCI6NjE1LjQxMzQyOTA1NDA1NDEsInkiOjIyNC41NzUwMDAwMDExMTc2fSx7IngiOjY1Ny4zNzUsInkiOjI1OS41NzUwMDAwMDExMTc2fSx7IngiOjY4Mi4zNzUsInkiOjI1OS41NzUwMDAwMDExMTc2fV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M809.813,250.8L820.401,249.341C830.99,247.883,852.167,244.967,882.35,243.508C912.533,242.05,951.722,242.05,971.316,242.05L990.911,242.05" id="Test-cyclic-special-1" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="Test-cyclic-special-1" data-points="W3sieCI6ODA5LjgxMjUsInkiOjI1MC43OTk1ODg2NTUxNTUwMn0seyJ4Ijo4NzMuMzQzNzUsInkiOjI0Mi4wNTAwMDAwMDA3NDUwNn0seyJ4Ijo5OTAuOTEwOTM3NDk5MjU0OSwieSI6MjQyLjA1MDAwMDAwMDc0NTA2fV0="></path><path d="M991.011,242.05L1013.014,242.05C1035.018,242.05,1079.024,242.05,1121.426,247.889C1163.827,253.729,1204.623,265.407,1225.021,271.246L1245.419,277.086" id="Test-cyclic-special-mid" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="Test-cyclic-special-mid" data-points="W3sieCI6OTkxLjAxMDkzNzUwMDc0NTEsInkiOjI0Mi4wNTAwMDAwMDA3NDUwNn0seyJ4IjoxMTIzLjAzMTI1LCJ5IjoyNDIuMDUwMDAwMDAwNzQ1MDZ9LHsieCI6MTI0NS40MTg3NDk5OTkyNTUsInkiOjI3Ny4wODU2ODY1NzYwNTk2fV0="></path><path d="M1245.419,277.1L1225.021,277.1C1204.623,277.1,1163.827,277.1,1121.417,277.1C1079.008,277.1,1034.984,277.1,993.37,277.1C951.755,277.1,912.549,277.1,883.019,275.733C853.488,274.365,833.631,271.631,823.703,270.263L813.775,268.896" id="Test-cyclic-special-2" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="Test-cyclic-special-2" data-points="W3sieCI6MTI0NS40MTg3NDk5OTkyNTUsInkiOjI3Ny4xMDAwMDAwMDE0OTAxfSx7IngiOjExMjMuMDMxMjUsInkiOjI3Ny4xMDAwMDAwMDE0OTAxfSx7IngiOjk5MC45NjA5Mzc1LCJ5IjoyNzcuMTAwMDAwMDAxNDkwMX0seyJ4Ijo4NzMuMzQzNzUsInkiOjI3Ny4xMDAwMDAwMDE0OTAxfSx7IngiOjgwOS44MTI1LCJ5IjoyNjguMzUwNDExMzQ3MDgwMn1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M775.533,220.575L791.835,198.979C808.137,177.383,840.74,134.192,866.964,112.596C893.188,91,913.031,91,922.953,91L932.875,91" id="L_Test_Push_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Test_Push_0" data-points="W3sieCI6Nzc1LjUzMzE2ODY1NjE4OTIsInkiOjIyMC41NzUwMDAwMDExMTc2fSx7IngiOjg3My4zNDM3NSwieSI6OTF9LHsieCI6OTM2Ljg3NSwieSI6OTF9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1045.047,91L1058.044,91C1071.042,91,1097.036,91,1122.365,91C1147.693,91,1172.354,91,1184.685,91L1197.016,91" id="L_Push_PR_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Push_PR_0" data-points="W3sieCI6MTA0NS4wNDY4NzUsInkiOjkxfSx7IngiOjExMjMuMDMxMjUsInkiOjkxfSx7IngiOjEyMDEuMDE1NjI1LCJ5Ijo5MX1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1289.922,91L1294.089,91C1298.255,91,1306.589,91,1314.255,91C1321.922,91,1328.922,91,1332.422,91L1335.922,91" id="L_PR_CI_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_PR_CI_0" data-points="W3sieCI6MTI4OS45MjE4NzUsInkiOjkxfSx7IngiOjEzMTQuOTIxODc1LCJ5Ijo5MX0seyJ4IjoxMzM5LjkyMTg3NSwieSI6OTF9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1455.202,75.218L1470.026,70.515C1484.851,65.812,1514.5,56.406,1544.864,51.703C1575.229,47,1606.31,47,1621.85,47L1637.391,47" id="L_CI_Fix_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_CI_Fix_0" data-points="W3sieCI6MTQ1NS4yMDE5NTAzNjg4MjYxLCJ5Ijo3NS4yMTc1NzUzNjg4MjYxOH0seyJ4IjoxNTQ0LjE0ODQzNzUsInkiOjQ3fSx7IngiOjE2NDEuMzkwNjI1LCJ5Ijo0N31d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1641.391,68.464L1625.184,72.22C1608.977,75.976,1576.563,83.488,1548.828,87.244C1521.094,91,1498.039,91,1486.512,91L1474.984,91" id="L_Fix_CI_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Fix_CI_0" data-points="W3sieCI6MTY0MS4zOTA2MjUsInkiOjY4LjQ2NDA3NzAzMDY5NzA3fSx7IngiOjE1NDQuMTQ4NDM3NSwieSI6OTF9LHsieCI6MTQ3MC45ODQzNzUsInkiOjkxfV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1448.591,113.394L1464.517,121.661C1480.443,129.929,1512.296,146.465,1539.749,154.732C1567.203,163,1590.258,163,1601.785,163L1613.313,163" id="L_CI_Review_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_CI_Review_0" data-points="W3sieCI6MTQ0OC41OTA2NjM3MDE4NDMsInkiOjExMy4zOTM3MTEyOTgxNTcxNH0seyJ4IjoxNTQ0LjE0ODQzNzUsInkiOjE2M30seyJ4IjoxNjE3LjMxMjUsInkiOjE2M31d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M1850.703,163L1854.87,163C1859.036,163,1867.37,163,1875.036,163C1882.703,163,1889.703,163,1893.203,163L1896.703,163" id="L_Review_Merge_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Review_Merge_0" data-points="W3sieCI6MTg1MC43MDMxMjUsInkiOjE2M30seyJ4IjoxODc1LjcwMzEyNSwieSI6MTYzfSx7IngiOjE5MDAuNzAzMTI1LCJ5IjoxNjN9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M2095.563,163L2099.729,163C2103.896,163,2112.229,163,2119.896,163C2127.563,163,2134.563,163,2138.063,163L2141.563,163" id="L_Merge_Done_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_Merge_Done_0" data-points="W3sieCI6MjA5NS41NjI1LCJ5IjoxNjN9LHsieCI6MjEyMC41NjI1LCJ5IjoxNjN9LHsieCI6MjE0NS41NjI1LCJ5IjoxNjN9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_Start_Branch_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Branch_Code_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Code_Lint_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="Lint-cyclic-special-1" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(873.34375, 135.47499999962747)"><g class="label" data-id="Lint-cyclic-special-mid" transform="translate(-38.53125, -12)"><foreignObject width="77.0625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Auto-fix</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="Lint-cyclic-special-2" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Lint_Test_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="Test-cyclic-special-1" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(1123.03125, 242.05000000074506)"><g class="label" data-id="Test-cyclic-special-mid" transform="translate(-52.984375, -12)"><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Fix Failure</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="Test-cyclic-special-2" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Test_Push_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Push_PR_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_PR_CI_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(1544.1484375, 47)"><g class="label" data-id="L_CI_Fix_0" transform="translate(-9.6328125, -12)"><foreignObject width="19.265625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>No</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(1544.1484375, 91)"><g class="label" data-id="L_Fix_CI_0" transform="translate(-48.1640625, -12)"><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Fix &amp; Push</p></span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(1544.1484375, 163)"><g class="label" data-id="L_CI_Review_0" transform="translate(-14.453125, -12)"><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"><p>Yes</p></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Review_Merge_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_Merge_Done_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-Start-0" transform="translate(39.5859375, 185.5750000011176)"><circle class="basic label-container" style="" r="31.5859375" cx="0" cy="0"></circle><g class="label" style="" transform="translate(-24.0859375, -12)"><rect></rect><foreignObject width="48.171875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Start</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Branch-1" transform="translate(184.890625, 185.5750000011176)"><rect class="basic label-container" style="" x="-63.71875" y="-27" width="127.4375" height="54"></rect><g class="label" style="" transform="translate(-33.71875, -12)"><rect></rect><foreignObject width="67.4375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>/branch</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Code-3" transform="translate(376.7734375, 185.5750000011176)"><rect class="basic label-container" style="" x="-78.1640625" y="-27" width="156.328125" height="54"></rect><g class="label" style="" transform="translate(-48.1640625, -12)"><rect></rect><foreignObject width="96.328125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Write Code</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Lint-5" transform="translate(568.65625, 185.5750000011176)"><rect class="basic label-container" style="" x="-63.71875" y="-39" width="127.4375" height="78"></rect><g class="label" style="" transform="translate(-33.71875, -24)"><rect></rect><foreignObject width="67.4375" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>/lint<br/>(Haiku)</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Test-9" transform="translate(746.09375, 259.5750000011176)"><rect class="basic label-container" style="" x="-63.71875" y="-39" width="127.4375" height="78"></rect><g class="label" style="" transform="translate(-33.71875, -24)"><rect></rect><foreignObject width="67.4375" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>/vitest<br/>(Haiku)</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Push-13" transform="translate(990.9609375, 91)"><rect class="basic label-container" style="" x="-54.0859375" y="-27" width="108.171875" height="54"></rect><g class="label" style="" transform="translate(-24.0859375, -12)"><rect></rect><foreignObject width="48.171875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>/push</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-PR-15" transform="translate(1245.46875, 91)"><rect class="basic label-container" style="" x="-44.453125" y="-27" width="88.90625" height="54"></rect><g class="label" style="" transform="translate(-14.453125, -12)"><rect></rect><foreignObject width="28.90625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>/pr</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-CI-17" transform="translate(1405.453125, 91)"><polygon points="65.53125,0 131.0625,-65.53125 65.53125,-131.0625 0,-65.53125" class="label-container" transform="translate(-65.03125, 65.53125)"></polygon><g class="label" style="" transform="translate(-38.53125, -12)"><rect></rect><foreignObject width="77.0625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>CI Pass?</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Fix-19" transform="translate(1734.0078125, 47)"><rect class="basic label-container" style="" x="-92.6171875" y="-39" width="185.234375" height="78"></rect><g class="label" style="" transform="translate(-62.6171875, -24)"><rect></rect><foreignObject width="125.234375" height="48"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>/fix-pipeline<br/>(Sonnet)</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Review-23" transform="translate(1734.0078125, 163)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>/review-coderabbit</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Merge-25" transform="translate(1998.1328125, 163)"><rect class="basic label-container" style="" x="-97.4296875" y="-27" width="194.859375" height="54"></rect><g class="label" style="" transform="translate(-67.4296875, -12)"><rect></rect><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>/merge-to-main</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-Done-27" transform="translate(2172.328125, 163)"><circle class="basic label-container" style="" r="26.765625" cx="0" cy="0"></circle><g class="label" style="" transform="translate(-19.265625, -12)"><rect></rect><foreignObject width="38.53125" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Done</p></span></div></foreignObject></g></g><g class="label edgeLabel" id="Lint---Lint---1" transform="translate(746.09375, 135.47499999962747)"><rect width="0.1" height="0.1"></rect><g class="label" style="" transform="translate(0, 0)"><rect></rect><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:10px;text-align:center"><span class="nodeLabel"></span></div></foreignObject></g></g><g class="label edgeLabel" id="Lint---Lint---2" transform="translate(990.9609375, 168.05000000074506)"><rect width="0.1" height="0.1"></rect><g class="label" style="" transform="translate(0, 0)"><rect></rect><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:10px;text-align:center"><span class="nodeLabel"></span></div></foreignObject></g></g><g class="label edgeLabel" id="Test---Test---1" transform="translate(990.9609375, 242.05000000074506)"><rect width="0.1" height="0.1"></rect><g class="label" style="" transform="translate(0, 0)"><rect></rect><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:10px;text-align:center"><span class="nodeLabel"></span></div></foreignObject></g></g><g class="label edgeLabel" id="Test---Test---2" transform="translate(1245.46875, 277.1000000014901)"><rect width="0.1" height="0.1"></rect><g class="label" style="" transform="translate(0, 0)"><rect></rect><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:10px;text-align:center"><span class="nodeLabel"></span></div></foreignObject></g></g></g></g></g><text text-anchor="middle" x="1103.546875" y="-25" class="flowchartTitleText">Development Workflow</text></svg></p>
<h3 id="branch--start-a-task">/branch — start a task<a class="heading-link" aria-label="Link to section" href="#branch--start-a-task"><span class="heading-link-icon">#</span></a></h3>
<a href="/prompts/claude/claude-branch-command" target="_blank" rel="noopener noreferrer" class="prompt-link astro-7tc5uzmh"> <div class="prompt-link-header astro-7tc5uzmh"> <span class="prompt-link-icon astro-7tc5uzmh">🤖</span> <span class="prompt-link-title astro-7tc5uzmh">View full prompt</span> <span class="prompt-link-arrow astro-7tc5uzmh">↗</span> </div> <div class="prompt-link-content astro-7tc5uzmh"> <p>I type <code>/branch &quot;implement dark mode toggle&quot;</code> and Claude checks out main, pulls latest, and creates <code>feat/dark-mode-toggle</code>. No more thinking about naming conventions.</p> </div> </a> 
<h3 id="lint--fix-before-commit">/lint — fix before commit<a class="heading-link" aria-label="Link to section" href="#lint--fix-before-commit"><span class="heading-link-icon">#</span></a></h3>
<a href="/prompts/claude/claude-lint-command" target="_blank" rel="noopener noreferrer" class="prompt-link astro-7tc5uzmh"> <div class="prompt-link-header astro-7tc5uzmh"> <span class="prompt-link-icon astro-7tc5uzmh">🤖</span> <span class="prompt-link-title astro-7tc5uzmh">View full prompt</span> <span class="prompt-link-arrow astro-7tc5uzmh">↗</span> </div> <div class="prompt-link-content astro-7tc5uzmh"> <p>I type <code>/lint</code>. It runs the linter with auto-fix, and if errors remain, Claude fixes them. Uses Haiku for speed—runs in about 20 seconds.</p> </div> </a> 
<h3 id="vitest--run-unit-tests">/vitest — run unit tests<a class="heading-link" aria-label="Link to section" href="#vitest--run-unit-tests"><span class="heading-link-icon">#</span></a></h3>
<a href="/prompts/claude/claude-vitest-command" target="_blank" rel="noopener noreferrer" class="prompt-link astro-7tc5uzmh"> <div class="prompt-link-header astro-7tc5uzmh"> <span class="prompt-link-icon astro-7tc5uzmh">🤖</span> <span class="prompt-link-title astro-7tc5uzmh">View full prompt</span> <span class="prompt-link-arrow astro-7tc5uzmh">↗</span> </div> <div class="prompt-link-content astro-7tc5uzmh"> <p>I type <code>/vitest</code>. It runs the test suite and fixes any failures. The prompt tells Claude to fix the code, not the test—implementation should match expected behavior.</p> </div> </a> 
<h3 id="commit--save-your-work">/commit — save your work<a class="heading-link" aria-label="Link to section" href="#commit--save-your-work"><span class="heading-link-icon">#</span></a></h3>
<a href="/prompts/claude/claude-commit-command" target="_blank" rel="noopener noreferrer" class="prompt-link astro-7tc5uzmh"> <div class="prompt-link-header astro-7tc5uzmh"> <span class="prompt-link-icon astro-7tc5uzmh">🤖</span> <span class="prompt-link-title astro-7tc5uzmh">View full prompt</span> <span class="prompt-link-arrow astro-7tc5uzmh">↗</span> </div> <div class="prompt-link-content astro-7tc5uzmh"> <p>I type <code>/commit</code>. Claude analyzes the diff, generates a Conventional Commit message, and commits. It looks at recent commits to match your project’s style.</p> </div> </a> 
<h3 id="push--commit-and-push-in-one-step">/push — commit and push in one step<a class="heading-link" aria-label="Link to section" href="#push--commit-and-push-in-one-step"><span class="heading-link-icon">#</span></a></h3>
<a href="/prompts/claude/claude-push-command" target="_blank" rel="noopener noreferrer" class="prompt-link astro-7tc5uzmh"> <div class="prompt-link-header astro-7tc5uzmh"> <span class="prompt-link-icon astro-7tc5uzmh">🤖</span> <span class="prompt-link-title astro-7tc5uzmh">View full prompt</span> <span class="prompt-link-arrow astro-7tc5uzmh">↗</span> </div> <div class="prompt-link-content astro-7tc5uzmh"> <p>I type <code>/push</code>. It stages everything, generates a commit message, commits, and pushes. My most-used command—one word and the code is on GitHub.</p> </div> </a> 
<h3 id="fix-pipeline--fix-failing-ci-tests">/fix-pipeline — fix failing CI tests<a class="heading-link" aria-label="Link to section" href="#fix-pipeline--fix-failing-ci-tests"><span class="heading-link-icon">#</span></a></h3>
<a href="/prompts/claude/claude-fix-pipeline-command" target="_blank" rel="noopener noreferrer" class="prompt-link astro-7tc5uzmh"> <div class="prompt-link-header astro-7tc5uzmh"> <span class="prompt-link-icon astro-7tc5uzmh">🤖</span> <span class="prompt-link-title astro-7tc5uzmh">View full prompt</span> <span class="prompt-link-arrow astro-7tc5uzmh">↗</span> </div> <div class="prompt-link-content astro-7tc5uzmh"> <p>I type <code>/fix-pipeline</code>. It fetches the failed logs via <code>gh</code>, analyzes the error, and fixes it. Uses Sonnet because debugging requires reasoning. The prompt includes guardrails—Claude must read the actual error before proposing fixes.</p> </div> </a> 
<h3 id="pr--create-a-pull-request">/pr — create a pull request<a class="heading-link" aria-label="Link to section" href="#pr--create-a-pull-request"><span class="heading-link-icon">#</span></a></h3>
<a href="/prompts/claude/claude-pr-command" target="_blank" rel="noopener noreferrer" class="prompt-link astro-7tc5uzmh"> <div class="prompt-link-header astro-7tc5uzmh"> <span class="prompt-link-icon astro-7tc5uzmh">🤖</span> <span class="prompt-link-title astro-7tc5uzmh">View full prompt</span> <span class="prompt-link-arrow astro-7tc5uzmh">↗</span> </div> <div class="prompt-link-content astro-7tc5uzmh"> <p>I type <code>/pr</code>. It analyzes all commits on the branch, generates a PR title and description, and opens it via <code>gh pr create</code>. Checks if a PR already exists first.</p> </div> </a> 
<h3 id="review-coderabbit--address-review-comments">/review-coderabbit — address review comments<a class="heading-link" aria-label="Link to section" href="#review-coderabbit--address-review-comments"><span class="heading-link-icon">#</span></a></h3>
<a href="/prompts/claude/claude-review-coderabbit-command" target="_blank" rel="noopener noreferrer" class="prompt-link astro-7tc5uzmh"> <div class="prompt-link-header astro-7tc5uzmh"> <span class="prompt-link-icon astro-7tc5uzmh">🤖</span> <span class="prompt-link-title astro-7tc5uzmh">View full prompt</span> <span class="prompt-link-arrow astro-7tc5uzmh">↗</span> </div> <div class="prompt-link-content astro-7tc5uzmh"> <p>I type <code>/review-coderabbit</code>. It fetches CodeRabbit’s comments via GraphQL, verifies each suggestion against the codebase, implements valid fixes or pushes back with reasoning, and resolves every thread. AI reviewers aren’t always right—the prompt ensures Claude verifies before acting.</p> </div> </a> 
<h3 id="merge-to-main--finish-the-task">/merge-to-main — finish the task<a class="heading-link" aria-label="Link to section" href="#merge-to-main--finish-the-task"><span class="heading-link-icon">#</span></a></h3>
<a href="/prompts/claude/claude-merge-to-main-command" target="_blank" rel="noopener noreferrer" class="prompt-link astro-7tc5uzmh"> <div class="prompt-link-header astro-7tc5uzmh"> <span class="prompt-link-icon astro-7tc5uzmh">🤖</span> <span class="prompt-link-title astro-7tc5uzmh">View full prompt</span> <span class="prompt-link-arrow astro-7tc5uzmh">↗</span> </div> <div class="prompt-link-content astro-7tc5uzmh"> <p>I type <code>/merge-to-main</code>. It squash merges the PR, deletes the branch, and pulls main. Done.</p> </div> </a> 
<h2 id="summary">Summary<a class="heading-link" aria-label="Link to section" href="#summary"><span class="heading-link-icon">#</span></a></h2>
<p>By moving your process into <code>.claude/commands/</code>, you are building a system.</p>
<ul>
<li>Bash command execution injects real-time context</li>
<li>Model selection balances speed vs reasoning</li>
<li>The workflow automates branching, linting, committing, CI debugging, PRs, and merging</li>
</ul>
<p>Define the process once. Claude executes it every time.</p>
<p>Want to extend Claude Code even further? Connect external tools via <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/what-is-model-context-protocol-mcp/" class="internal-link astro-3tyn5ojg"> MCP (Model Context Protocol) </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">What Is the Model Context Protocol (MCP)? How It Works</span> <span class="preview-description astro-3tyn5ojg">Learn how MCP (Model Context Protocol) standardizes AI tool integration, enabling LLMs to interact with external services, databases, and APIs through a universal protocol similar to USB-C for AI applications.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">mcp</span><span class="preview-tag astro-3tyn5ojg">typescript</span><span class="preview-tag astro-3tyn5ojg">ai</span>  </span> <time class="preview-date astro-3tyn5ojg">Aug 10, 2025</time> </span> </span> </span>  <script>
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
</script> or package your commands into a <span class="internal-link-wrapper astro-3tyn5ojg"> <a href="/posts/building-my-first-claude-code-plugin/" class="internal-link astro-3tyn5ojg"> shareable plugin </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Building My First Claude Code Plugin</span> <span class="preview-description astro-3tyn5ojg">How I built a Claude Code plugin to generate skills, agents, commands, and more—and stopped copy-pasting boilerplate.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">tooling</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 8, 2025</time> </span> </span> </span>  <script>
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
</script>.</p>
<p>I don’t think about naming conventions, commit messages, or PR descriptions anymore. The commands handle it.</p>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Bonus: Shell aliases for even faster execution </p> <div class="alert-content astro-7kdbuayl"> <p>You can skip the interactive prompt entirely with <code>claude -p</code>. Add aliases to your <code>.zshrc</code> or <code>.bashrc</code>:</p><pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#BB9AF7">alias</span><span style="color:#C0CAF5"> clint</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">claude -p &#39;/lint&#39;</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">alias</span><span style="color:#C0CAF5"> cpush</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">claude -p &#39;/push&#39;</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">alias</span><span style="color:#C0CAF5"> ccommit</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">claude -p &#39;/commit&#39;</span><span style="color:#89DDFF">&quot;</span></span>
<span class="line"><span style="color:#BB9AF7">alias</span><span style="color:#C0CAF5"> cbranch</span><span style="color:#89DDFF">=</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">claude -p &#39;/branch&#39;</span><span style="color:#89DDFF">&quot;</span></span></code><button type="button" class="copy" data-code="alias clint=&#34;claude -p '/lint'&#34;
alias cpush=&#34;claude -p '/push'&#34;
alias ccommit=&#34;claude -p '/commit'&#34;
alias cbranch=&#34;claude -p '/branch'&#34;" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre><p>Now <code>clint</code> runs the lint command without opening the interactive session. The <code>-p</code> flag passes the prompt directly—Claude executes and exits. Two steps become one keystroke.</p> </div> </div>  </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_claude-code-slash-commands-guide" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="claude-code-slash-commands-guide" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/claude-code/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">claude-code</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/claude-code-slash-commands-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/claude-code-slash-commands-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/claude-code-slash-commands-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/claude-code-slash-commands-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/claude-code-slash-commands-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/claude-code-slash-commands-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/claude-code-slash-commands-guide/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/understanding-claude-code-full-stack/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained</h3> <p class="related-post-description astro-vj4tpspi"> A practical guide to Claude Code&#39;s features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-11-09T00:00:00.000Z">Nov 9, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> claude-code </span> </div> </div> </a><a href="/posts/claude-code-notification-hooks/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Get Notified When Claude Code Finishes With Hooks</h3> <p class="related-post-description astro-vj4tpspi"> Set up desktop notifications in Claude Code to know when Claude needs your input or permission. Learn how to use hooks for instant alerts instead of constantly checking. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-11-23T00:00:00.000Z">Nov 23, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> claude-code </span> </div> </div> </a><a href="/posts/building-my-first-claude-code-plugin/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Building My First Claude Code Plugin</h3> <p class="related-post-description astro-vj4tpspi"> How I built a Claude Code plugin to generate skills, agents, commands, and more—and stopped copy-pasting boilerplate. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-11-08T00:00:00.000Z">Nov 8, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> claude-code </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "claude-code-slash-commands-guide";

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