# Source: https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Adding Obsidian-Style Wiki Links to My Astro Blog | alexop.dev</title><meta name="title" content="Adding Obsidian-Style Wiki Links to My Astro Blog | alexop.dev"><meta name="description" content="I added [[wiki link]] syntax to my Astro blog with hover preview cards. Here's how it works and how you can build it too."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Adding Obsidian-Style Wiki Links to My Astro Blog | alexop.dev"><meta property="og:description" content="I added [[wiki link]] syntax to my Astro blog with hover preview cards. Here's how it works and how you can build it too."><meta property="og:url" content="https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog/"><meta property="og:image" content="https://alexop.dev/posts/adding-obsidian-style-wiki-links-to-my-astro-blog/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-01-10T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog/"><meta property="twitter:title" content="Adding Obsidian-Style Wiki Links to My Astro Blog | alexop.dev"><meta property="twitter:description" content="I added [[wiki link]] syntax to my Astro blog with hover preview cards. Here's how it works and how you can build it too."><meta property="twitter:image" content="https://alexop.dev/posts/adding-obsidian-style-wiki-links-to-my-astro-blog/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Adding Obsidian-Style Wiki Links to My Astro Blog | alexop.dev","description":"I added [[wiki link]] syntax to my Astro blog with hover preview cards. Here's how it works and how you can build it too.","image":"https://alexop.dev/posts/adding-obsidian-style-wiki-links-to-my-astro-blog/index.png","datePublished":"2025-01-10T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
<style>a:where(.astro-blwjyjpt){transition:all .3s ease}a:where(.astro-blwjyjpt):hover{transform:translateY(-2px);box-shadow:0 4px 6px -1px #0000001a,0 2px 4px -1px #0000000f}
.minimal-posts-list:where(.astro-eenky23y){width:100%;max-width:64rem;margin:0 auto;padding:2rem 1rem;background:rgb(var(--color-fill));color:rgb(var(--color-text-base))}.posts-title:where(.astro-eenky23y){font-size:2rem;margin-bottom:2rem;color:rgb(var(--color-accent));font-family:inherit;font-weight:600;letter-spacing:.02em}.year-group:where(.astro-eenky23y){margin-bottom:2.5rem}.year-heading:where(.astro-eenky23y){font-size:1.3rem;color:rgb(var(--color-text-base));margin:2.5rem 0 1.2rem;font-family:inherit;font-weight:500;letter-spacing:.04em}.year-group:where(.astro-eenky23y) ul:where(.astro-eenky23y){list-style:none;padding:0;margin:0}.post-item:where(.astro-eenky23y){display:flex;justify-content:space-between;align-items:center;padding:1rem 0;border-bottom:1px solid rgba(var(--color-border),.2)}.post-link:where(.astro-eenky23y){color:rgb(var(--color-text-base));text-decoration:none;font-size:1.1rem;transition:color .2s}.post-link:where(.astro-eenky23y):hover{color:rgb(var(--color-accent))}.post-date:where(.astro-eenky23y){color:rgb(var(--color-card-muted));font-size:.95rem;font-family:inherit;letter-spacing:.05em;min-width:70px;text-align:right}
@keyframes astroFadeInOut{0%{opacity:1}to{opacity:0}}@keyframes astroFadeIn{0%{opacity:0;mix-blend-mode:plus-lighter}to{opacity:1;mix-blend-mode:plus-lighter}}@keyframes astroFadeOut{0%{opacity:1;mix-blend-mode:plus-lighter}to{opacity:0;mix-blend-mode:plus-lighter}}@keyframes astroSlideFromRight{0%{transform:translate(100%)}}@keyframes astroSlideFromLeft{0%{transform:translate(-100%)}}@keyframes astroSlideToRight{to{transform:translate(100%)}}@keyframes astroSlideToLeft{to{transform:translate(-100%)}}@media(prefers-reduced-motion){::view-transition-group(*),::view-transition-old(*),::view-transition-new(*){animation:none!important}[data-astro-transition-scope]{animation:none!important}}
</style>
<link rel="stylesheet" href="/_astro/index.Ck-KI3hC.css">
<style>.subagent-diagram-container:where(.astro-tpygpejy){display:flex;flex-direction:column;align-items:center;margin:2rem 0;width:100%}.subagent-diagram-fallback:where(.astro-tpygpejy){width:100%;max-width:600px}.subagent-diagram-svg:where(.astro-tpygpejy){width:100%;height:auto}.agent-circle:where(.astro-tpygpejy){fill:rgb(var(--color-accent) / .1);stroke:rgb(var(--color-accent));stroke-width:2}.subagent-circle:where(.astro-tpygpejy){fill:rgb(var(--color-accent) / .05);stroke:rgb(var(--color-accent) / .7);stroke-width:2;stroke-dasharray:4 2}.agent-icon:where(.astro-tpygpejy){font-size:24px}.agent-label:where(.astro-tpygpejy){fill:rgb(var(--color-text-base));font-size:12px;font-weight:500}.arrow-path:where(.astro-tpygpejy){fill:none;stroke:rgb(var(--color-text-base) / .5);stroke-width:2}.arrow-path:where(.astro-tpygpejy).dashed{stroke-dasharray:5 3}.arrow-path:where(.astro-tpygpejy).search-arrow{stroke:rgb(var(--color-accent) / .6)}.arrowhead-fill:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .5)}.arrow-label:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .6);font-size:11px;font-style:italic}.file-tree:where(.astro-tpygpejy) .folder:where(.astro-tpygpejy){fill:rgb(var(--color-text-base));font-size:14px;font-family:ui-monospace,monospace}.file-tree:where(.astro-tpygpejy) .file:where(.astro-tpygpejy){fill:rgb(var(--color-text-base) / .7);font-size:14px;font-family:ui-monospace,monospace}.file-tree:where(.astro-tpygpejy) .file:where(.astro-tpygpejy).highlight{fill:rgb(var(--color-accent));font-weight:600}.subagent-diagram-caption:where(.astro-tpygpejy){margin-top:1rem;text-align:center;font-size:.875rem;color:rgb(var(--color-text-base) / .7)}.subagent-diagram-fallback:where(.astro-tpygpejy){display:none}
.parallel-subagent-diagram-container:where(.astro-u2chhpb2){display:flex;flex-direction:column;align-items:center;margin:2rem 0;width:100%}.parallel-subagent-diagram-fallback:where(.astro-u2chhpb2){width:100%;max-width:800px}.parallel-subagent-diagram-svg-static:where(.astro-u2chhpb2){width:100%;height:auto}.agent-circle:where(.astro-u2chhpb2){fill:rgb(var(--color-accent) / .1);stroke:rgb(var(--color-accent));stroke-width:2}.subagent-circle:where(.astro-u2chhpb2){stroke-width:2;stroke-dasharray:4 2}.agent-icon:where(.astro-u2chhpb2){font-size:24px}.agent-label:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base));font-size:12px;font-weight:500}.task-label:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .8);font-size:13px;font-family:ui-monospace,monospace}.arrow-path:where(.astro-u2chhpb2){fill:none;stroke:rgb(var(--color-text-base) / .5);stroke-width:2}.arrow-path:where(.astro-u2chhpb2).dashed{stroke-dasharray:5 3}.arrow-path:where(.astro-u2chhpb2).report{stroke:#22c55e}.arrowhead-fill:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .5)}.domain-box-rect:where(.astro-u2chhpb2){fill:rgb(var(--color-fill) / .5);stroke-width:1.5}.domain-label:where(.astro-u2chhpb2){font-size:11px;font-weight:600}.finding-text:where(.astro-u2chhpb2){fill:rgb(var(--color-text-base) / .7);font-size:10px;font-family:ui-monospace,monospace}.synthesis-box:where(.astro-u2chhpb2){fill:#22c55e1a;stroke:#22c55e;stroke-width:2}.synthesis-text:where(.astro-u2chhpb2){fill:#22c55e;font-size:13px;font-weight:600}.parallel-subagent-diagram-caption:where(.astro-u2chhpb2){margin-top:1rem;text-align:center;font-size:.875rem;color:rgb(var(--color-text-base) / .7)}.parallel-subagent-diagram-fallback:where(.astro-u2chhpb2){display:none}
.shiki-magic-move-container{position:relative;white-space:pre}.shiki-magic-move-line-number{opacity:.3;-webkit-user-select:none;-moz-user-select:none;user-select:none}.shiki-magic-move-item{display:inline-block;transition:color var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-enter-active,.shiki-magic-move-leave-active,.shiki-magic-move-move{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-container-resize,.shiki-magic-move-container-restyle{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease");transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-container, 1))}.shiki-magic-move-move{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-move, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-enter-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-enter, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-leave-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-leave, 1) + var(--smm-stagger, 0))}.shiki-magic-move-enter-from,.shiki-magic-move-leave-to{opacity:0}br.shiki-magic-move-leave-active{display:none}
.shiki-magic-move-container{position:relative;white-space:pre}.shiki-magic-move-line-number{opacity:.3;-webkit-user-select:none;-moz-user-select:none;user-select:none}.shiki-magic-move-item{display:inline-block;transition:color var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-enter-active,.shiki-magic-move-leave-active,.shiki-magic-move-move{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease")}.shiki-magic-move-container-resize,.shiki-magic-move-container-restyle{transition:all var(--smm-duration,.5s) var(--smm-easing,"ease");transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-container, 1))}.shiki-magic-move-move{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-move, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-enter-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-enter, 1) + var(--smm-stagger, 0));z-index:1}.shiki-magic-move-leave-active{transition-delay:calc(var(--smm-duration, .5s)*var(--smm-delay-leave, 1) + var(--smm-stagger, 0))}.shiki-magic-move-enter-from,.shiki-magic-move-leave-to{opacity:0}br.shiki-magic-move-leave-active{display:none}
.jazz-demo-root[data-v-1a336f1a]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-1a336f1a]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-1a336f1a]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-1a336f1a]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-1a336f1a]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-1a336f1a]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-1a336f1a]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-1a336f1a]{background:#2563eb}.jazz-demo-toggle-off[data-v-1a336f1a]{background:#4b5563}.jazz-demo-toggle-dot[data-v-1a336f1a]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-1a336f1a]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-1a336f1a]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-1a336f1a]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-1a336f1a]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-1a336f1a]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-1a336f1a]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-1a336f1a]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card[data-v-1a336f1a]{padding:1.5rem}.jazz-counter-display[data-v-1a336f1a]{font-size:3rem;font-weight:700;color:#fff;text-align:center;padding:1rem 0;font-variant-numeric:tabular-nums}.jazz-counter-controls[data-v-1a336f1a]{display:flex;gap:.5rem}.jazz-counter-btn[data-v-1a336f1a]{flex:1;padding:.5rem;font-size:1.25rem;font-weight:600;border:1px solid #374151;border-radius:.5rem;background:#1f2937;color:#e5e7eb;cursor:pointer;transition:background-color .2s}.jazz-counter-btn[data-v-1a336f1a]:hover{background:#374151}.jazz-counter-btn-primary[data-v-1a336f1a]{background:#2563eb;border-color:#2563eb;color:#fff}.jazz-counter-btn-primary[data-v-1a336f1a]:hover{background:#1d4ed8}
.jazz-demo-root[data-v-d8349330]{background:#030712;border:1px solid #374151;border-radius:.75rem;padding:1rem;font-family:system-ui,-apple-system,sans-serif;color:#e5e7eb;font-size:14px}.jazz-demo-header[data-v-d8349330]{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}.jazz-demo-title[data-v-d8349330]{color:#fff;font-size:1rem;font-weight:600}.jazz-demo-toggles[data-v-d8349330]{display:flex;align-items:center;gap:.75rem}.jazz-demo-toggle-wrap[data-v-d8349330]{display:flex;align-items:center;gap:.5rem}.jazz-demo-toggle-label[data-v-d8349330]{color:#d1d5db;font-size:.75rem}.jazz-demo-toggle[data-v-d8349330]{position:relative;display:inline-flex;height:1.25rem;width:2.25rem;align-items:center;border-radius:9999px;transition:background-color .2s;border:none;cursor:pointer;padding:0}.jazz-demo-toggle-on[data-v-d8349330]{background:#2563eb}.jazz-demo-toggle-off[data-v-d8349330]{background:#4b5563}.jazz-demo-toggle-dot[data-v-d8349330]{display:inline-block;height:.875rem;width:.875rem;border-radius:9999px;background:#fff;transition:transform .2s}.jazz-demo-toggle-dot-on[data-v-d8349330]{transform:translate(1.125rem)}.jazz-demo-toggle-dot-off[data-v-d8349330]{transform:translate(.125rem)}.jazz-demo-covalue-id[data-v-d8349330]{display:flex;align-items:center;gap:.375rem;margin-bottom:.5rem;padding:.25rem .5rem;background:#1e1b4b;border:1px solid #3730a3;border-radius:.375rem;overflow:hidden}.jazz-demo-covalue-label[data-v-d8349330]{color:#a78bfa;font-size:.625rem;font-weight:600;white-space:nowrap}.jazz-demo-covalue-code[data-v-d8349330]{color:#c4b5fd;font-size:.625rem;font-family:ui-monospace,monospace;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.jazz-demo-card[data-v-d8349330]{background:#111827;border:1px solid #374151;border-radius:.75rem;padding:1rem}.jazz-demo-loading[data-v-d8349330]{color:#9ca3af;text-align:center;padding:2rem 0}.jazz-demo-card-title[data-v-d8349330]{font-size:1.25rem;font-weight:700;color:#fff;margin:0 0 .75rem}.jazz-demo-form[data-v-d8349330]{margin-bottom:.75rem;display:flex;flex-direction:column;gap:.5rem}.jazz-demo-input[data-v-d8349330]{width:100%;padding:.375rem .625rem;background:#1f2937;border:1px solid #4b5563;border-radius:.5rem;color:#fff;font-size:.8125rem;outline:none;box-sizing:border-box}.jazz-demo-input[data-v-d8349330]:focus{border-color:#3b82f6;box-shadow:0 0 0 2px #3b82f64d}.jazz-demo-input[data-v-d8349330]::-moz-placeholder{color:#6b7280}.jazz-demo-input[data-v-d8349330]::placeholder{color:#6b7280}.jazz-demo-add-btn[data-v-d8349330]{width:100%;padding:.375rem .75rem;background:#2563eb;color:#fff;border:none;border-radius:.5rem;font-weight:500;font-size:.8125rem;cursor:pointer;transition:background-color .2s}.jazz-demo-add-btn[data-v-d8349330]:hover{background:#1d4ed8}.jazz-demo-list[data-v-d8349330]{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.25rem}.jazz-demo-item[data-v-d8349330]{display:flex;align-items:center;gap:.5rem;padding:.375rem;border-radius:.5rem}.jazz-demo-item[data-v-d8349330]:hover{background:#1f2937}.jazz-demo-item:hover .jazz-demo-delete[data-v-d8349330]{opacity:1}.jazz-demo-drag[data-v-d8349330]{cursor:grab;color:#4b5563;transition:color .2s;-webkit-user-select:none;-moz-user-select:none;user-select:none;display:flex;align-items:center}.jazz-demo-drag[data-v-d8349330]:active{cursor:grabbing}.jazz-demo-item:hover .jazz-demo-drag[data-v-d8349330]{color:#9ca3af}.jazz-demo-svg[data-v-d8349330]{width:1rem;height:1rem}.jazz-demo-checkbox[data-v-d8349330]{width:.875rem;height:.875rem;accent-color:#2563eb}.jazz-demo-text[data-v-d8349330]{flex:1;color:#e5e7eb;font-size:.8125rem}.jazz-demo-text-done[data-v-d8349330]{text-decoration:line-through;color:#6b7280}.jazz-demo-delete[data-v-d8349330]{opacity:0;transition:opacity .2s;color:#6b7280;background:none;border:none;padding:.125rem;cursor:pointer;display:flex;align-items:center}.jazz-demo-delete[data-v-d8349330]:hover{color:#f87171}.jazz-demo-empty[data-v-d8349330]{color:#6b7280;text-align:center;padding:1rem 0;margin:0;font-size:.8125rem}
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: adding-obsidian-style-wiki-links-to-my-astro-blog; }@layer astro { ::view-transition-old(adding-obsidian-style-wiki-links-to-my-astro-blog) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(adding-obsidian-style-wiki-links-to-my-astro-blog) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(adding-obsidian-style-wiki-links-to-my-astro-blog) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(adding-obsidian-style-wiki-links-to-my-astro-blog) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: astro; }@layer astro { ::view-transition-old(astro) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(astro) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(astro) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(astro) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: markdown; }@layer astro { ::view-transition-old(markdown) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(markdown) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(markdown) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(markdown) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: obsidian; }@layer astro { ::view-transition-old(obsidian) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(obsidian) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(obsidian) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(obsidian) { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Adding Obsidian-Style Wiki Links to My Astro Blog</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-01-10T00:00:00.000Z">Jan 10, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z8OgWh" prefix="r6" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Adding Obsidian-Style Wiki Links to My Astro Blog&quot;],&quot;content&quot;:[0,&quot;## TLDR\n\nI built a remark plugin that transforms `[[slug]]` syntax into internal links with hover preview cards. It supports multiple content collections, custom display text, and shows broken link warnings at build time.\n\n## Live Examples\n\nHover over these links to see the preview cards in action:\n\n**Blog post:** [[are-llms-creative]]\n\n**Blog post with alias:** [[are-llms-creative|my thoughts on LLM creativity]]\n\n**TIL:** [[til:dynamic-pinia-stores]]\n\n**Notes:** [[notes:software-testing-with-generative-ai|Testing with AI]]\n\n**Broken link:** [[this-post-does-not-exist]]\n\nAll of these are written as simple `[[slug]]` syntax in the markdown source.\n\n## Why I Built This\n\nI use Obsidian for note-taking and love the `[[wiki link]]` syntax. It&#39;s fast to type and creates connections between notes naturally. I wanted the same experience when writing blog posts.\n\nBefore this, I had an `InternalLink` component that required MDX imports:\n\n```mdx\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\n\nCheck out &lt;InternalLink slug=\&quot;some-post\&quot;&gt;this post&lt;/InternalLink&gt;.\n```\n\nToo verbose. I wanted to just type `[[some-post]]` and have it work.\n\n## How It Works\n\nThe solution uses a custom remark plugin that:\n\n1. Finds `[[...]]` patterns in markdown text\n2. Looks up the post metadata from the file system\n3. Generates the full preview card HTML at build time\n\n### Supported Syntax\n\n```markdown\n[[slug]]                           # Links to blog post\n[[slug|custom text]]               # With display text\n[[til:slug]]                       # Links to TIL collection\n[[notes:slug|my notes]]            # Other collections with alias\n```\n\n### The Preview Card\n\nHover over any wiki link to see a preview card with:\n\n- Post title\n- Description (3 lines max)\n- Tags (first 3)\n- Publication date\n\nThe card uses fixed positioning to escape overflow containers and flips below the link when too close to the viewport top.\n\n## Building the Remark Plugin\n\nThe plugin runs during markdown processing. It reads all content collection files at initialization and caches the metadata for fast lookups.\n\n```ts\n// src/lib/remarkWikiLinks.ts\nimport { visit } from \&quot;unist-util-visit\&quot;;\nimport matter from \&quot;gray-matter\&quot;;\nimport fs from \&quot;node:fs\&quot;;\n\nconst WIKI_LINK_REGEX = /\\[\\[([^\\]|]+?)(?:\\|([^\\]]+))?\\]\\]/g;\n\nexport function remarkWikiLinks() {\n  // Load all posts at plugin init\n  const cache = loadAllPosts();\n\n  return (tree) =&gt; {\n    visit(tree, \&quot;text\&quot;, (node, index, parent) =&gt; {\n      const matches = [...node.value.matchAll(WIKI_LINK_REGEX)];\n      if (matches.length === 0) return;\n\n      // Replace matches with HTML nodes containing preview cards\n      // ...\n    });\n  };\n}\n```\n\nThe key insight: remark plugins can output raw HTML nodes. The plugin generates the complete preview card markup, so no separate rehype processing is needed.\n\n### Parsing the Syntax\n\nThe regex captures two groups:\n\n1. The target (either `slug` or `collection:slug`)\n2. The optional alias after the pipe\n\n```ts\nfunction parseWikiLink(target: string, alias?: string) {\n  let collection = \&quot;blog\&quot;;\n  let slug = target;\n\n  if (target.includes(\&quot;:\&quot;)) {\n    const [col, sl] = target.split(\&quot;:\&quot;, 2);\n    if ([\&quot;blog\&quot;, \&quot;til\&quot;, \&quot;notes\&quot;, \&quot;prompts\&quot;].includes(col)) {\n      collection = col;\n      slug = sl;\n    }\n  }\n\n  return { collection, slug, alias };\n}\n```\n\n### Loading Post Metadata\n\nThe plugin reads frontmatter directly from content files using `gray-matter`:\n\n```ts\nfunction loadCollectionPosts(collection: string) {\n  const posts = new Map();\n  const dir = `src/content/${collection}`;\n\n  for (const file of fs.readdirSync(dir, { recursive: true })) {\n    if (!file.endsWith(\&quot;.md\&quot;) &amp;&amp; !file.endsWith(\&quot;.mdx\&quot;)) continue;\n\n    const content = fs.readFileSync(`${dir}/${file}`, \&quot;utf-8\&quot;);\n    const { data } = matter(content);\n\n    if (data.draft) continue;\n\n    const slug = file.replace(/\\.(md|mdx)$/, \&quot;\&quot;);\n    posts.set(slug, {\n      title: data.title,\n      description: data.description,\n      tags: data.tags,\n      pubDatetime: data.pubDatetime,\n    });\n  }\n\n  return posts;\n}\n```\n\n### Generating Preview Card HTML\n\nThe plugin outputs the same HTML structure as my existing `InternalLink` component:\n\n```ts\nfunction createPreviewCardHtml(post, href, displayText) {\n  return `\n    &lt;span class=\&quot;internal-link-wrapper\&quot;&gt;\n      &lt;a href=\&quot;${href}\&quot; class=\&quot;internal-link\&quot;&gt;${displayText}&lt;/a&gt;\n      &lt;span class=\&quot;preview-card\&quot; role=\&quot;tooltip\&quot;&gt;\n        &lt;span class=\&quot;preview-content\&quot;&gt;\n          &lt;span class=\&quot;preview-title\&quot;&gt;${post.title}&lt;/span&gt;\n          &lt;span class=\&quot;preview-description\&quot;&gt;${post.description}&lt;/span&gt;\n          &lt;!-- tags and date --&gt;\n        &lt;/span&gt;\n      &lt;/span&gt;\n    &lt;/span&gt;\n  `;\n}\n```\n\n## Broken Link Detection\n\nWhen a wiki link references a non-existent post, the plugin:\n\n1. Logs a warning during build: `[wiki-links] Post not found: blog:missing-slug`\n2. Renders the link with error styling (red wavy underline)\n\n```ts\nif (!postData) {\n  console.warn(`[wiki-links] Post not found: ${collection}:${slug}`);\n  return `&lt;span class=\&quot;wiki-link-broken\&quot; title=\&quot;Post not found: ${slug}\&quot;&gt;${displayText}&lt;/span&gt;`;\n}\n```\n\nThis catches typos and stale references before they hit production.\n\n## Adding the Plugin to Astro\n\nRegister the plugin in `astro.config.ts`:\n\n```ts\nimport { remarkWikiLinks } from \&quot;./src/lib/remarkWikiLinks\&quot;;\n\nexport default defineConfig({\n  markdown: {\n    remarkPlugins: [\n      remarkWikiLinks,\n      // other plugins...\n    ],\n  },\n});\n```\n\nThe plugin runs first so wiki links are processed before other transformations.\n\n## The CSS\n\nThe styles match my existing `InternalLink` component:\n\n```css\n.internal-link-wrapper {\n  position: relative;\n  display: inline-block;\n}\n\n.internal-link {\n  @apply text-skin-accent underline decoration-dashed;\n}\n\n.preview-card {\n  position: absolute;\n  bottom: calc(100% + 8px);\n  opacity: 0;\n  visibility: hidden;\n  transition: opacity 0.2s;\n}\n\n.wiki-link-broken {\n  @apply text-red-400 underline decoration-wavy;\n}\n```\n\n## The Hover Script\n\nA small inline script handles the preview card positioning:\n\n```js\ndocument.addEventListener(\&quot;astro:page-load\&quot;, () =&gt; {\n  document.querySelectorAll(\&quot;.internal-link-wrapper\&quot;).forEach((wrapper) =&gt; {\n    wrapper.addEventListener(\&quot;mouseenter\&quot;, () =&gt; {\n      const card = wrapper.querySelector(\&quot;.preview-card\&quot;);\n      // Calculate position, flip if needed, show card\n    });\n  });\n});\n```\n\nThe script runs on `astro:page-load` to work with Astro&#39;s view transitions.\n\n## Result\n\nNow I can write posts with natural wiki link syntax:\n\n```markdown\nI wrote about [[are-llms-creative|LLM creativity]] last month.\nSee also my [[til:dynamic-pinia-stores|TIL on Pinia stores]].\n```\n\nThe links render with hover previews, and broken references get caught at build time. Much better than importing components everywhere.\n\n## What&#39;s Next\n\nA few improvements I&#39;m considering:\n\n- Fuzzy matching for slug typos\n- Backlinks section showing which posts link to the current one\n- Support for heading anchors: `[[post#section]]`&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="tldr">TLDR<a class="heading-link" aria-label="Link to section" href="#tldr"><span class="heading-link-icon">#</span></a></h2>
<p>I built a remark plugin that transforms <code>[[slug]]</code> syntax into internal links with hover preview cards. It supports multiple content collections, custom display text, and shows broken link warnings at build time.</p>
<h2 id="live-examples">Live Examples<a class="heading-link" aria-label="Link to section" href="#live-examples"><span class="heading-link-icon">#</span></a></h2>
<p>Hover over these links to see the preview cards in action:</p>
<p><strong>Blog post:</strong> <span class="internal-link-wrapper"><a href="/posts/are-llms-creative/" class="internal-link">Are LLMs Creative?</a><span class="preview-card" role="tooltip"><span class="preview-content"><span class="preview-title">Are LLMs Creative?</span><span class="preview-description">Exploring the fundamental nature of creativity in Large Language Models compared to human creativity, sparked by reflections on OpenAI's latest image model.</span><span class="preview-tags"><span class="preview-tag">ai</span></span><time class="preview-date">Apr 1, 2025</time></span></span></span></p>
<p><strong>Blog post with alias:</strong> <span class="internal-link-wrapper"><a href="/posts/are-llms-creative/" class="internal-link">my thoughts on LLM creativity</a><span class="preview-card" role="tooltip"><span class="preview-content"><span class="preview-title">Are LLMs Creative?</span><span class="preview-description">Exploring the fundamental nature of creativity in Large Language Models compared to human creativity, sparked by reflections on OpenAI's latest image model.</span><span class="preview-tags"><span class="preview-tag">ai</span></span><time class="preview-date">Apr 1, 2025</time></span></span></span></p>
<p><strong>TIL:</strong> <span class="internal-link-wrapper"><a href="/tils/dynamic-pinia-stores/" class="internal-link">Dynamic Pinia Stores in Vue 3</a><span class="preview-card" role="tooltip"><span class="preview-content"><span class="preview-title">Dynamic Pinia Stores in Vue 3</span><span class="preview-description">Create dynamic Pinia stores with unique IDs for separate component instances</span><span class="preview-tags"><span class="preview-tag">vue</span><span class="preview-tag">pinia</span><span class="preview-tag">typescript</span></span><time class="preview-date">Nov 28, 2024</time></span></span></span></p>
<p><strong>Notes:</strong> <span class="internal-link-wrapper"><a href="/notes/software-testing-with-generative-ai/" class="internal-link">Testing with AI</a><span class="preview-card" role="tooltip"><span class="preview-content"><span class="preview-title">Software Testing with Generative AI</span><span class="preview-description">A beginner friendly guide for leveraging AI in software testing practices</span><span class="preview-tags"><span class="preview-tag">testing</span><span class="preview-tag">ai</span><span class="preview-tag">book-summary</span></span><time class="preview-date">Jan 1, 2025</time></span></span></span></p>
<p><strong>Broken link:</strong> <span class="wiki-link-broken" title="Post not found: this-post-does-not-exist">this-post-does-not-exist</span></p>
<p>All of these are written as simple <code>[[slug]]</code> syntax in the markdown source.</p>
<h2 id="why-i-built-this">Why I Built This<a class="heading-link" aria-label="Link to section" href="#why-i-built-this"><span class="heading-link-icon">#</span></a></h2>
<p>I use Obsidian for note-taking and love the <code>[[wiki link]]</code> syntax. It’s fast to type and creates connections between notes naturally. I wanted the same experience when writing blog posts.</p>
<p>Before this, I had an <code>InternalLink</code> component that required MDX imports:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="mdx"><code><span class="line"><span style="color:#A9B1D6">import InternalLink from "</span><span style="color:#89DDFF">@</span><span style="color:#73DACA">features/mdx-components</span><span style="color:#A9B1D6">/components/InternalLink.astro";</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A9B1D6">Check out &#x3C;InternalLink slug="some-post">this post&#x3C;/InternalLink>.</span></span></code><button type="button" class="copy" data-code="import InternalLink from &#x22;@features/mdx-components/components/InternalLink.astro&#x22;;

Check out <InternalLink slug=&#x22;some-post&#x22;>this post</InternalLink>." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Too verbose. I wanted to just type <code>[[some-post]]</code> and have it work.</p>
<h2 id="how-it-works">How It Works<a class="heading-link" aria-label="Link to section" href="#how-it-works"><span class="heading-link-icon">#</span></a></h2>
<p>The solution uses a custom remark plugin that:</p>
<ol>
<li>Finds <code>[[...]]</code> patterns in markdown text</li>
<li>Looks up the post metadata from the file system</li>
<li>Generates the full preview card HTML at build time</li>
</ol>
<h3 id="supported-syntax">Supported Syntax<a class="heading-link" aria-label="Link to section" href="#supported-syntax"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#9AA5CE">[</span><span style="color:#89DDFF">[</span><span style="color:#73DACA">slug</span><span style="color:#89DDFF">]</span><span style="color:#9AA5CE">]                           # Links to blog post</span></span>
<span class="line"><span style="color:#9AA5CE">[[slug|custom text]]               # With display text</span></span>
<span class="line"><span style="color:#9AA5CE">[</span><span style="color:#89DDFF">[</span><span style="color:#73DACA">til:slug</span><span style="color:#89DDFF">]</span><span style="color:#9AA5CE">]                       # Links to TIL collection</span></span>
<span class="line"><span style="color:#9AA5CE">[[notes:slug|my notes]]            # Other collections with alias</span></span></code><button type="button" class="copy" data-code="[[slug]]                           # Links to blog post
[[slug|custom text]]               # With display text
[[til:slug]]                       # Links to TIL collection
[[notes:slug|my notes]]            # Other collections with alias" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="the-preview-card">The Preview Card<a class="heading-link" aria-label="Link to section" href="#the-preview-card"><span class="heading-link-icon">#</span></a></h3>
<p>Hover over any wiki link to see a preview card with:</p>
<ul>
<li>Post title</li>
<li>Description (3 lines max)</li>
<li>Tags (first 3)</li>
<li>Publication date</li>
</ul>
<p>The card uses fixed positioning to escape overflow containers and flips below the link when too close to the viewport top.</p>
<h2 id="building-the-remark-plugin">Building the Remark Plugin<a class="heading-link" aria-label="Link to section" href="#building-the-remark-plugin"><span class="heading-link-icon">#</span></a></h2>
<p>The plugin runs during markdown processing. It reads all content collection files at initialization and caches the metadata for fast lookups.</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#51597D;font-style:italic">// src/lib/remarkWikiLinks.ts</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">visit</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">unist-util-visit</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> matter</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">gray-matter</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7DCFFF">import</span><span style="color:#0DB9D7"> fs</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">node:fs</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> WIKI_LINK_REGEX</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> /</span><span style="color:#C0CAF5">\[\[</span><span style="color:#F7768E">(</span><span style="color:#E0AF68">[</span><span style="color:#89DDFF">^</span><span style="color:#C0CAF5">\]</span><span style="color:#E0AF68">|]</span><span style="color:#89DDFF">+?</span><span style="color:#F7768E">)(?:</span><span style="color:#C0CAF5">\|</span><span style="color:#F7768E">(</span><span style="color:#E0AF68">[</span><span style="color:#89DDFF">^</span><span style="color:#C0CAF5">\]</span><span style="color:#E0AF68">]</span><span style="color:#89DDFF">+</span><span style="color:#F7768E">))</span><span style="color:#89DDFF">?</span><span style="color:#C0CAF5">\]\]</span><span style="color:#89DDFF">/g</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#BB9AF7"> function</span><span style="color:#7AA2F7"> remarkWikiLinks</span><span style="color:#9ABDF5">()</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">  // Load all posts at plugin init</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> cache</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> loadAllPosts</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">tree</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">    visit</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">tree</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">text</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> (</span><span style="color:#E0AF68">node</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> index</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> parent</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> matches</span><span style="color:#89DDFF"> =</span><span style="color:#9ABDF5"> [</span><span style="color:#F7768E;font-weight:bold">...</span><span style="color:#C0CAF5">node</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">value</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">matchAll</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">WIKI_LINK_REGEX</span><span style="color:#9ABDF5">)]</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">      if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">matches</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">length</span><span style="color:#BB9AF7"> ===</span><span style="color:#FF9E64"> 0</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7;font-style:italic">return</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Replace matches with HTML nodes containing preview cards</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // ...</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="// src/lib/remarkWikiLinks.ts
import { visit } from &#x22;unist-util-visit&#x22;;
import matter from &#x22;gray-matter&#x22;;
import fs from &#x22;node:fs&#x22;;

const WIKI_LINK_REGEX = /\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]/g;

export function remarkWikiLinks() {
  // Load all posts at plugin init
  const cache = loadAllPosts();

  return (tree) => {
    visit(tree, &#x22;text&#x22;, (node, index, parent) => {
      const matches = [...node.value.matchAll(WIKI_LINK_REGEX)];
      if (matches.length === 0) return;

      // Replace matches with HTML nodes containing preview cards
      // ...
    });
  };
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The key insight: remark plugins can output raw HTML nodes. The plugin generates the complete preview card markup, so no separate rehype processing is needed.</p>
<h3 id="parsing-the-syntax">Parsing the Syntax<a class="heading-link" aria-label="Link to section" href="#parsing-the-syntax"><span class="heading-link-icon">#</span></a></h3>
<p>The regex captures two groups:</p>
<ol>
<li>The target (either <code>slug</code> or <code>collection:slug</code>)</li>
<li>The optional alias after the pipe</li>
</ol>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> parseWikiLink</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">target</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> alias</span><span style="color:#89DDFF">?:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> collection</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">blog</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  let</span><span style="color:#BB9AF7"> slug</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> target</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">target</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">includes</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">:</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">)) {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#89DDFF"> [</span><span style="color:#BB9AF7">col</span><span style="color:#89DDFF">,</span><span style="color:#BB9AF7"> sl</span><span style="color:#89DDFF">]</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> target</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">split</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">:</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#FF9E64"> 2</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> ([</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">blog</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">til</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">notes</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">prompts</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">]</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">includes</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">col</span><span style="color:#9ABDF5">)) {</span></span>
<span class="line"><span style="color:#C0CAF5">      collection</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> col</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">      slug</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> sl</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">    }</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#9ABDF5"> { </span><span style="color:#C0CAF5">collection</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> slug</span><span style="color:#89DDFF">,</span><span style="color:#C0CAF5"> alias</span><span style="color:#9ABDF5"> }</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="function parseWikiLink(target: string, alias?: string) {
  let collection = &#x22;blog&#x22;;
  let slug = target;

  if (target.includes(&#x22;:&#x22;)) {
    const [col, sl] = target.split(&#x22;:&#x22;, 2);
    if ([&#x22;blog&#x22;, &#x22;til&#x22;, &#x22;notes&#x22;, &#x22;prompts&#x22;].includes(col)) {
      collection = col;
      slug = sl;
    }
  }

  return { collection, slug, alias };
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="loading-post-metadata">Loading Post Metadata<a class="heading-link" aria-label="Link to section" href="#loading-post-metadata"><span class="heading-link-icon">#</span></a></h3>
<p>The plugin reads frontmatter directly from content files using <code>gray-matter</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> loadCollectionPosts</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">collection</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> string</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> posts</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> new</span><span style="color:#7AA2F7"> Map</span><span style="color:#9ABDF5">()</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">  const</span><span style="color:#BB9AF7"> dir</span><span style="color:#89DDFF"> =</span><span style="color:#89DDFF"> `</span><span style="color:#9ECE6A">src/content/</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">collection</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">  for</span><span style="color:#9ABDF5"> (</span><span style="color:#9D7CD8;font-style:italic">const</span><span style="color:#BB9AF7"> file</span><span style="color:#89DDFF"> of</span><span style="color:#C0CAF5"> fs</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">readdirSync</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">dir</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> { </span><span style="color:#73DACA">recursive</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> true</span><span style="color:#9ABDF5"> })) {</span></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">file</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">endsWith</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">.md</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">&#x26;&#x26;</span><span style="color:#BB9AF7"> !</span><span style="color:#C0CAF5">file</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">endsWith</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">.mdx</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">)) </span><span style="color:#BB9AF7">continue</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> content</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> fs</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">readFileSync</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">dir</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">/</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">file</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">utf-8</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#89DDFF"> {</span><span style="color:#BB9AF7"> data</span><span style="color:#89DDFF"> }</span><span style="color:#89DDFF"> =</span><span style="color:#7AA2F7"> matter</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">content</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7">    if</span><span style="color:#9ABDF5"> (</span><span style="color:#C0CAF5">data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">draft</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">continue</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">    const</span><span style="color:#BB9AF7"> slug</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> file</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">replace</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">/</span><span style="color:#C0CAF5">\.</span><span style="color:#F7768E">(</span><span style="color:#B4F9F8">md</span><span style="color:#BB9AF7">|</span><span style="color:#B4F9F8">mdx</span><span style="color:#F7768E">)</span><span style="color:#BB9AF7">$</span><span style="color:#89DDFF">/</span><span style="color:#89DDFF">,</span><span style="color:#89DDFF"> ""</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#C0CAF5">    posts</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">set</span><span style="color:#9ABDF5">(</span><span style="color:#C0CAF5">slug</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">      title</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">title</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      description</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">description</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      tags</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">tags</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#73DACA">      pubDatetime</span><span style="color:#89DDFF">:</span><span style="color:#C0CAF5"> data</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">pubDatetime</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#C0CAF5"> posts</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="function loadCollectionPosts(collection: string) {
  const posts = new Map();
  const dir = &#x60;src/content/${collection}&#x60;;

  for (const file of fs.readdirSync(dir, { recursive: true })) {
    if (!file.endsWith(&#x22;.md&#x22;) &#x26;&#x26; !file.endsWith(&#x22;.mdx&#x22;)) continue;

    const content = fs.readFileSync(&#x60;${dir}/${file}&#x60;, &#x22;utf-8&#x22;);
    const { data } = matter(content);

    if (data.draft) continue;

    const slug = file.replace(/\.(md|mdx)$/, &#x22;&#x22;);
    posts.set(slug, {
      title: data.title,
      description: data.description,
      tags: data.tags,
      pubDatetime: data.pubDatetime,
    });
  }

  return posts;
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="generating-preview-card-html">Generating Preview Card HTML<a class="heading-link" aria-label="Link to section" href="#generating-preview-card-html"><span class="heading-link-icon">#</span></a></h3>
<p>The plugin outputs the same HTML structure as my existing <code>InternalLink</code> component:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#BB9AF7">function</span><span style="color:#7AA2F7"> createPreviewCardHtml</span><span style="color:#9ABDF5">(</span><span style="color:#E0AF68">post</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> href</span><span style="color:#89DDFF">,</span><span style="color:#E0AF68"> displayText</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#89DDFF"> `</span></span>
<span class="line"><span style="color:#9ECE6A">    &#x3C;span class="internal-link-wrapper"></span></span>
<span class="line"><span style="color:#9ECE6A">      &#x3C;a href="</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">href</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">" class="internal-link"></span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">displayText</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">&#x3C;/a></span></span>
<span class="line"><span style="color:#9ECE6A">      &#x3C;span class="preview-card" role="tooltip"></span></span>
<span class="line"><span style="color:#9ECE6A">        &#x3C;span class="preview-content"></span></span>
<span class="line"><span style="color:#9ECE6A">          &#x3C;span class="preview-title"></span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">post</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">title</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">&#x3C;/span></span></span>
<span class="line"><span style="color:#9ECE6A">          &#x3C;span class="preview-description"></span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">post</span><span style="color:#89DDFF">.</span><span style="color:#7DCFFF">description</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">&#x3C;/span></span></span>
<span class="line"><span style="color:#9ECE6A">          &#x3C;!-- tags and date --></span></span>
<span class="line"><span style="color:#9ECE6A">        &#x3C;/span></span></span>
<span class="line"><span style="color:#9ECE6A">      &#x3C;/span></span></span>
<span class="line"><span style="color:#9ECE6A">    &#x3C;/span></span></span>
<span class="line"><span style="color:#89DDFF">  `</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="function createPreviewCardHtml(post, href, displayText) {
  return &#x60;
    <span class=&#x22;internal-link-wrapper&#x22;>
      <a href=&#x22;${href}&#x22; class=&#x22;internal-link&#x22;>${displayText}</a>
      <span class=&#x22;preview-card&#x22; role=&#x22;tooltip&#x22;>
        <span class=&#x22;preview-content&#x22;>
          <span class=&#x22;preview-title&#x22;>${post.title}</span>
          <span class=&#x22;preview-description&#x22;>${post.description}</span>
          <!-- tags and date -->
        </span>
      </span>
    </span>
  &#x60;;
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="broken-link-detection">Broken Link Detection<a class="heading-link" aria-label="Link to section" href="#broken-link-detection"><span class="heading-link-icon">#</span></a></h2>
<p>When a wiki link references a non-existent post, the plugin:</p>
<ol>
<li>Logs a warning during build: <code>[wiki-links] Post not found: blog:missing-slug</code></li>
<li>Renders the link with error styling (red wavy underline)</li>
</ol>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#BB9AF7">if</span><span style="color:#9ABDF5"> (</span><span style="color:#BB9AF7">!</span><span style="color:#C0CAF5">postData</span><span style="color:#9ABDF5">)</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  console</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">warn</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">`</span><span style="color:#9ECE6A">[wiki-links] Post not found: </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">collection</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">:</span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">slug</span><span style="color:#7DCFFF">}</span><span style="color:#89DDFF">`</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#BB9AF7;font-style:italic">  return</span><span style="color:#89DDFF"> `</span><span style="color:#9ECE6A">&#x3C;span class="wiki-link-broken" title="Post not found: </span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">slug</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">"></span><span style="color:#7DCFFF">${</span><span style="color:#C0CAF5">displayText</span><span style="color:#7DCFFF">}</span><span style="color:#9ECE6A">&#x3C;/span></span><span style="color:#89DDFF">`</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code="if (!postData) {
  console.warn(&#x60;[wiki-links] Post not found: ${collection}:${slug}&#x60;);
  return &#x60;<span class=&#x22;wiki-link-broken&#x22; title=&#x22;Post not found: ${slug}&#x22;>${displayText}</span>&#x60;;
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>This catches typos and stale references before they hit production.</p>
<h2 id="adding-the-plugin-to-astro">Adding the Plugin to Astro<a class="heading-link" aria-label="Link to section" href="#adding-the-plugin-to-astro"><span class="heading-link-icon">#</span></a></h2>
<p>Register the plugin in <code>astro.config.ts</code>:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="ts"><code><span class="line"><span style="color:#7DCFFF">import</span><span style="color:#9ABDF5"> { </span><span style="color:#0DB9D7">remarkWikiLinks</span><span style="color:#9ABDF5"> }</span><span style="color:#7DCFFF"> from</span><span style="color:#89DDFF"> "</span><span style="color:#9ECE6A">./src/lib/remarkWikiLinks</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7DCFFF">export</span><span style="color:#7DCFFF"> default</span><span style="color:#7AA2F7"> defineConfig</span><span style="color:#9ABDF5">({</span></span>
<span class="line"><span style="color:#73DACA">  markdown</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#73DACA">    remarkPlugins</span><span style="color:#89DDFF">:</span><span style="color:#9ABDF5"> [</span></span>
<span class="line"><span style="color:#7DCFFF">      remarkWikiLinks</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // other plugins...</span></span>
<span class="line"><span style="color:#9ABDF5">    ]</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">  }</span><span style="color:#89DDFF">,</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="import { remarkWikiLinks } from &#x22;./src/lib/remarkWikiLinks&#x22;;

export default defineConfig({
  markdown: {
    remarkPlugins: [
      remarkWikiLinks,
      // other plugins...
    ],
  },
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The plugin runs first so wiki links are processed before other transformations.</p>
<h2 id="the-css">The CSS<a class="heading-link" aria-label="Link to section" href="#the-css"><span class="heading-link-icon">#</span></a></h2>
<p>The styles match my existing <code>InternalLink</code> component:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="css"><code><span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">internal-link-wrapper</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  position</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> relative</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  display</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> inline-block</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">internal-link</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9ABDF5">  @apply text-skin-accent underline decoration-dashed</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">preview-card</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#7AA2F7">  position</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> absolute</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  bottom</span><span style="color:#89DDFF">:</span><span style="color:#0DB9D7"> calc</span><span style="color:#9ABDF5">(</span><span style="color:#FF9E64">100</span><span style="color:#F7768E">%</span><span style="color:#89DDFF"> +</span><span style="color:#FF9E64"> 8</span><span style="color:#F7768E">px</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  opacity</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> 0</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  visibility</span><span style="color:#89DDFF">:</span><span style="color:#FF9E64"> hidden</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#7AA2F7">  transition</span><span style="color:#89DDFF">:</span><span style="color:#BB9AF7"> opacity </span><span style="color:#FF9E64">0.2</span><span style="color:#F7768E">s</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span>
<span class="line"></span>
<span class="line"><span style="color:#E0AF68">.</span><span style="color:#9ECE6A">wiki-link-broken</span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9ABDF5">  @apply text-red-400 underline decoration-wavy</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">}</span></span></code><button type="button" class="copy" data-code=".internal-link-wrapper {
  position: relative;
  display: inline-block;
}

.internal-link {
  @apply text-skin-accent underline decoration-dashed;
}

.preview-card {
  position: absolute;
  bottom: calc(100% + 8px);
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s;
}

.wiki-link-broken {
  @apply text-red-400 underline decoration-wavy;
}" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h2 id="the-hover-script">The Hover Script<a class="heading-link" aria-label="Link to section" href="#the-hover-script"><span class="heading-link-icon">#</span></a></h2>
<p>A small inline script handles the preview card positioning:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="js"><code><span class="line"><span style="color:#C0CAF5">document</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">addEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">astro:page-load</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> ()</span><span style="color:#BB9AF7"> =></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">  document</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">querySelectorAll</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">.internal-link-wrapper</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">forEach</span><span style="color:#9ABDF5">((</span><span style="color:#E0AF68">wrapper</span><span style="color:#9ABDF5">) </span><span style="color:#BB9AF7">=></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#C0CAF5">    wrapper</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">addEventListener</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">mouseenter</span><span style="color:#89DDFF">"</span><span style="color:#89DDFF">,</span><span style="color:#9ABDF5"> () </span><span style="color:#BB9AF7">=></span><span style="color:#9ABDF5"> {</span></span>
<span class="line"><span style="color:#9D7CD8;font-style:italic">      const</span><span style="color:#BB9AF7"> card</span><span style="color:#89DDFF"> =</span><span style="color:#C0CAF5"> wrapper</span><span style="color:#89DDFF">.</span><span style="color:#7AA2F7">querySelector</span><span style="color:#9ABDF5">(</span><span style="color:#89DDFF">"</span><span style="color:#9ECE6A">.preview-card</span><span style="color:#89DDFF">"</span><span style="color:#9ABDF5">)</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#51597D;font-style:italic">      // Calculate position, flip if needed, show card</span></span>
<span class="line"><span style="color:#9ABDF5">    })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">  })</span><span style="color:#89DDFF">;</span></span>
<span class="line"><span style="color:#9ABDF5">})</span><span style="color:#89DDFF">;</span></span></code><button type="button" class="copy" data-code="document.addEventListener(&#x22;astro:page-load&#x22;, () => {
  document.querySelectorAll(&#x22;.internal-link-wrapper&#x22;).forEach((wrapper) => {
    wrapper.addEventListener(&#x22;mouseenter&#x22;, () => {
      const card = wrapper.querySelector(&#x22;.preview-card&#x22;);
      // Calculate position, flip if needed, show card
    });
  });
});" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The script runs on <code>astro:page-load</code> to work with Astro’s view transitions.</p>
<h2 id="result">Result<a class="heading-link" aria-label="Link to section" href="#result"><span class="heading-link-icon">#</span></a></h2>
<p>Now I can write posts with natural wiki link syntax:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word;" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#9AA5CE">I wrote about [[are-llms-creative|LLM creativity]] last month.</span></span>
<span class="line"><span style="color:#9AA5CE">See also my [[til:dynamic-pinia-stores|TIL on Pinia stores]].</span></span></code><button type="button" class="copy" data-code="I wrote about [[are-llms-creative|LLM creativity]] last month.
See also my [[til:dynamic-pinia-stores|TIL on Pinia stores]]." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add(&#x27;copied&#x27;);
            setTimeout(() => this.classList.remove(&#x27;copied&#x27;), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>The links render with hover previews, and broken references get caught at build time. Much better than importing components everywhere.</p>
<h2 id="whats-next">What’s Next<a class="heading-link" aria-label="Link to section" href="#whats-next"><span class="heading-link-icon">#</span></a></h2>
<p>A few improvements I’m considering:</p>
<ul>
<li>Fuzzy matching for slug typos</li>
<li>Backlinks section showing which posts link to the current one</li>
<li>Support for heading anchors: <code>[[post#section]]</code></li>
</ul> </article> <script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();</script><astro-island uid="Z1XneyL" component-url="/_astro/presentation.C3Wa0mjp.js" component-export="VMarkBlogRenderer" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;containerSelector&quot;:[0,&quot;#article&quot;],&quot;class&quot;:[0,&quot;astro-vj4tpspi&quot;]}" ssr client="only" opts="{&quot;name&quot;:&quot;VMarkBlogRenderer&quot;,&quot;value&quot;:&quot;react&quot;}"></astro-island> <!-- Fullscreen Modal Container using native dialog --><dialog id="mermaid-modal" class="mermaid-modal" aria-label="Fullscreen diagram view"> <div class="mermaid-modal-content"> <button class="mermaid-modal-close" aria-label="Close fullscreen view" type="button"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"> <line x1="18" y1="6" x2="6" y2="18"></line> <line x1="6" y1="6" x2="18" y2="18"></line> </svg> </button> <div class="mermaid-modal-diagram"></div> <div class="mermaid-modal-hint">Press <kbd>Esc</kbd> or click outside to close</div> </div> </dialog>  <script type="module">const p=new Set;function g(){const e=document.getElementById("mermaid-modal"),c=e?.querySelector(".mermaid-modal-diagram"),f=e?.querySelector(".mermaid-modal-close");if(!e||!c)return;document.querySelectorAll('svg[id^="mermaid-"]').forEach(t=>{if(!t.id.match(/^mermaid-\d+$/)||p.has(t.id)||t.parentElement?.classList.contains("mermaid-fullscreen-wrapper")||t.closest(".mermaid-modal"))return;p.add(t.id);const n=document.createElement("div");n.className="mermaid-fullscreen-wrapper mermaid-clickable",n.setAttribute("tabindex","0"),n.setAttribute("role","button"),n.setAttribute("aria-label","Click to view diagram fullscreen"),t.parentElement?.insertBefore(n,t),n.appendChild(t);const o=document.createElement("div");o.className="mermaid-expand-icon",o.innerHTML=`
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_adding-obsidian-wiki-links-to-astro-blog" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="adding-obsidian-wiki-links-to-astro-blog" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/astro/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">astro</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/markdown/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">markdown</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/obsidian/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">obsidian</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/adding-obsidian-wiki-links-to-astro-blog/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
</h2> <div class="md:grid-cols-3 grid grid-cols-1 gap-6 astro-vj4tpspi"> <a href="/posts/building-my-first-claude-code-plugin/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Building My First Claude Code Plugin</h3> <p class="related-post-description astro-vj4tpspi"> How I built a Claude Code plugin to generate skills, agents, commands, and more—and stopped copy-pasting boilerplate. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-11-08T00:00:00.000Z">Nov 8, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> claude-code </span> </div> </div> </a><a href="/posts/semantic-related-posts-astro-transformersjs/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">No Server, No Database: Smarter Related Posts in Astro with `transformers.js`</h3> <p class="related-post-description astro-vj4tpspi"> How I used Hugging Face embeddings to create smart “Related Posts” for my Astro blog—no backend, no database, just TypeScript. </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-sm"><time dateTime="2025-05-18T00:00:00.000Z">May 18, 2025</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> ai </span> </div> </div> </a><a href="/posts/presentation-mode-demo/" class="related-post-card group astro-vj4tpspi"> <div class="p-5 astro-vj4tpspi"> <h3 class="related-post-title astro-vj4tpspi">Presentation Mode: Turn Your Blog Posts into Slides</h3> <p class="related-post-description astro-vj4tpspi"> A complete demo of presentation mode with v-click animations and drawing annotations. Press P to see keyboard navigation, incremental reveals, and press D to draw on slides! </p> <div class="flex items-center justify-between text-xs text-skin-base text-opacity-60 astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-90 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="italic text-sm">Updated:</span><span class="italic text-sm"><time dateTime="2026-01-24T00:00:00.000Z">Jan 24, 2026</time><span class="sr-only"> at </span></span></div> <span class="related-post-tag astro-vj4tpspi"> demo </span> </div> </div> </a> </div> </div> </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "adding-obsidian-wiki-links-to-astro-blog";

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